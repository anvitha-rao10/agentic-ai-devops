from fastapi import FastAPI
from jenkins import get_last_failed_build

app = FastAPI()

@app.get("/collect/jenkins")
def collect():
    return get_last_failed_build()
