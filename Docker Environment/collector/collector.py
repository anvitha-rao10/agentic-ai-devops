import uuid
from datetime import datetime
from jenkins_client import fetch_last_build, fetch_console_log

LATEST_FAILURE_EVENT = None
LAST_FAILED_BUILD_NUMBER = None


def collect_failed_event():
    global LATEST_FAILURE_EVENT, LAST_FAILED_BUILD_NUMBER

    build = fetch_last_build()

    # Only care about FAILURE
    if build.get("result") != "FAILURE":
        return LATEST_FAILURE_EVENT

    build_number = build.get("number")

    # 🔒 Prevent duplicate processing
    if LAST_FAILED_BUILD_NUMBER == build_number:
        return LATEST_FAILURE_EVENT

    log = fetch_console_log()
    change = build.get("changeSets", [{}])[0].get("items", [{}])[0]

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
        "git": {
            "commit": change.get("commitId"),
            "author": change.get("author", {}).get("fullName"),
            "message": change.get("msg")
        },
        "error": {
            "type": "PIPELINE_FAILURE",
            "raw_log": log
        }
    }

    LAST_FAILED_BUILD_NUMBER = build_number
    return LATEST_FAILURE_EVENT


def get_failed_event():
    # 🔄 Always re-check Jenkins
    return collect_failed_event() or {
        "status": "no_failed_build_detected"
    }
