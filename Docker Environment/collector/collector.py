import uuid
from datetime import datetime
from jenkins_client import fetch_last_build, fetch_console_log

LATEST_FAILURE_EVENT = None

def collect_failed_event():
    global LATEST_FAILURE_EVENT

    build = fetch_last_build()

    # ✅ STRICT: only FAILURE
    if build.get("result") != "FAILURE":
        return None

    log = fetch_console_log()
    change = build.get("changeSets", [{}])[0].get("items", [{}])[0]

    LATEST_FAILURE_EVENT = {
        "event_id": f"evt-{uuid.uuid4()}",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "source": "jenkins",
        "ci": {
            "job_name": build.get("fullDisplayName"),
            "build_id": build.get("number"),
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

    return LATEST_FAILURE_EVENT


def get_failed_event():
    if LATEST_FAILURE_EVENT is None:
        return collect_failed_event()
    return LATEST_FAILURE_EVENT
