from fastapi import FastAPI, HTTPException
from datetime import datetime
import uuid
from jenkins_client import fetch_last_build, fetch_console_log

app = FastAPI()
EVENTS = []

@app.get("/collector/sync/jenkins")
def sync_jenkins():
    try:
        build = fetch_last_build()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    if build.get("result") != "FAILURE":
        return {"status": "no_failure"}

    try:
        log = fetch_console_log()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

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
    return {"status": "collected", "event": event}


@app.get("/collector/events")
def show_events():
    return EVENTS
