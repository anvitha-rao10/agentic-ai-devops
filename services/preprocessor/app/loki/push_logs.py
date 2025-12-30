import time
from app.loki.client import loki_post
from app.config import LOKI_PUSH_ENDPOINT


def push_logs_to_loki(job_name: str, build_id: str, logs: list[str]):
    timestamp_ns = lambda: str(int(time.time() * 1e9))

    streams = [{
        "stream": {
            "job": job_name,
            "build_id": build_id
        },
        "values": [[timestamp_ns(), line] for line in logs]
    }]

    payload = {"streams": streams}
    loki_post(LOKI_PUSH_ENDPOINT, payload)
