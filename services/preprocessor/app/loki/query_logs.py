from app.loki.client import loki_get
from app.config import LOKI_QUERY_ENDPOINT


def query_ssh_errors(job_name: str):
    query = f'{{job="{job_name}"}} |= "ssh"'

    params = {
        "query": query,
        "limit": 1000
    }

    response = loki_get(LOKI_QUERY_ENDPOINT, params)
    return response["data"]["result"]
