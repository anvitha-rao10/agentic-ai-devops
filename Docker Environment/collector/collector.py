import uuid
import threading
import time
from datetime import datetime
from jenkins_client import fetch_last_build, fetch_console_log

LATEST_FAILURE_EVENT = None
LAST_FAILED_BUILD_NUMBER = None


def capture_failure(build):
    global LATEST_FAILURE_EVENT, LAST_FAILED_BUILD_NUMBER

    build_number = build.get("number")
    log = fetch_console_log()

    LATEST_FAILURE_EVENT = {
        "event_id": f"evt-{uuid.uuid4()}",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "source": "jenkins",
        "ci": {
            "job_name": build.get("fullDisplayName"),
            "build_id": build_number,
            "result": build.get("result"),
            "url": build.get("url")
        },
        "error": {
            "type": "PIPELINE_FAILURE",
            "raw_log": log
        }
    }

    LAST_FAILED_BUILD_NUMBER = build_number
    print(f"🚨 Failure captured: #{build_number}")


def watcher():
    global LAST_FAILED_BUILD_NUMBER

    print("🟢 Jenkins failure watcher started")

    while True:
        try:
            build = fetch_last_build()

            if (
                not build.get("building")
                and build.get("result") == "FAILURE"
            ):
                build_number = build.get("number")

                if build_number != LAST_FAILED_BUILD_NUMBER:
                    capture_failure(build)

        except Exception as e:
            print("❌ Watcher error:", e)

        time.sleep(10)


def start_watcher():
    global LAST_FAILED_BUILD_NUMBER

    # 🔥 BOOTSTRAP: capture existing failure at startup
    try:
        build = fetch_last_build()
        if (
            not build.get("building")
            and build.get("result") == "FAILURE"
        ):
            capture_failure(build)
    except Exception as e:
        print("❌ Bootstrap error:", e)

    t = threading.Thread(target=watcher, daemon=True)
    t.start()


def get_failed_event():
    return LATEST_FAILURE_EVENT or {"status": "no_failed_build_detected"}
