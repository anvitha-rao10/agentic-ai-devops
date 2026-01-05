from fastapi import FastAPI
from collector import get_failed_event

app = FastAPI()

@app.get("/event/failure")
def failed_event():
    event = get_failed_event()
    return event or {"status": "no_failed_build_detected"}
