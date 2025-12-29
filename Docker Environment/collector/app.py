from fastapi import FastAPI
from datetime import datetime
import uuid
import threading
import time

from jenkins_client import fetch_last_build, fetch_console_log

app = FastAPI()

EVENTS = []
LAST_BUILD_PROCESSED = None


def collect_failure(build):
    global LAST_BUILD_PROCESSED

    log = fetch_console_log()

    event = {
        "event_id": f"evt-{uuid.uuid4()}",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "source": "jenkins",
        "ci": {
            "job_name": build.get("fullDisplayName"),
            "build_id": build.get("number")
        },
        "error": {
            "error_type": "GIT_SSH_FAILURE",
            "raw_log": log[:1500]
        }
    }

    EVENTS.append(event)
    LAST_BUILD_PROCESSED = build.get("number")

    print("✅ Failure metadata collected")


def jenkins_watcher():
    global LAST_BUILD_PROCESSED

    print("🟢 Jenkins watcher running")

    while True:
        try:
            build = fetch_last_build()

            if (
                not build.get("building")
                and build.get("result") == "FAILURE"
                and build.get("number") != LAST_BUILD_PROCESSED
            ):
                print("🚨 New failed build detected")
                collect_failure(build)

        except Exception as e:
            print("❌ Watcher error:", e)

        time.sleep(10)


@app.on_event("startup")
def startup():
    global LAST_BUILD_PROCESSED

    # 🔹 BOOTSTRAP: collect existing failed build once
    try:
        build = fetch_last_build()

        if (
            not build.get("building")
            and build.get("result") == "FAILURE"
        ):
            print("🚨 Bootstrap failed build found")
            collect_failure(build)

    except Exception as e:
        print("❌ Bootstrap error:", e)

    # 🔹 Start watcher thread
    threading.Thread(target=jenkins_watcher, daemon=True).start()


@app.get("/collector/events")
def view_events():
    return EVENTS


@app.get("/health")
def health():
    return {"status": "collector_running"}
