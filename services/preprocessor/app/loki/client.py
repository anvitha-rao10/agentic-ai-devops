import requests
from app.config import LOKI_BASE_URL, LOKI_PUSH_ENDPOINT

def loki_post(payload: dict):
    url = f"{LOKI_BASE_URL}{LOKI_PUSH_ENDPOINT}"
    response = requests.post(url, json=payload, timeout=10)
    response.raise_for_status()
    return response.status_code
