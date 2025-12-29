from fastapi import FastAPI
from datetime import datetime
import uuid
import threading
import time

from jenkins_client import fetch_last_build, fetch_console_log

app = FastAPI()

EVENTS = []
LAST_BUILD_PROCESSED = None


def jenkins_watcher():
    global LAST_BUILD_PROCESSED

    print("🟢 Jenkins watcher started")

    while True:
        try:
            print("🔍 Checking Jenkins for latest build...")

            build = fetch_last_build()
            build_number = build.get("number")
            build_result = build.get("result")

            print(f"📦 Build #{build_number} → {build_result}")

            if (
                not build.get("building")
                and build.get("result") == "FAILURE"
                and build_number != LAST_BUILD_PROCESSED
                ):

                print("🚨 New failure detected")

                log = fetch_console_log()

                event = {
                    "event_id": f"evt-{uuid.uuid4()}",
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                    "source": "jenkins",
                    "ci": {
                        "job_name": build.get("fullDisplayName"),
                        "build_id": build_number
                    },
                    "error": {
                        "error_type": "GIT_SSH_FAILURE",
                        "raw_log": log[:1500]
                    }
                }

                EVENTS.append(event)
                LAST_BUILD_PROCESSED = build_number

                print("✅ Failure metadata collected")

        except Exception as e:
            print("❌ Watcher error:", e)

        time.sleep(10)  # poll every 10 seconds


@app.on_event("startup")
def start_background_watcher():
    thread = threading.Thread(target=jenkins_watcher, daemon=True)
    thread.start()


@app.get("/collector/events")
def view_events():
    return EVENTS


@app.get("/health")
def health():
    return {"status": "collector_running"}
