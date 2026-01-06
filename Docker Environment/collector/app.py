from fastapi import FastAPI
from collector import get_failed_event, start_watcher

app = FastAPI()

@app.on_event("startup")
def startup():
    start_watcher()   # 🔥 THIS WAS MISSING

@app.get("/event/failure")
def failed_event():
    return get_failed_event()
