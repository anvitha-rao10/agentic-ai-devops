import requests
from requests.auth import HTTPBasicAuth

JENKINS_BASE = "http://jenkins:8080"
USERNAME = "anvitha"
API_TOKEN = "1147718635800fbb97299e64021e47ac32"

auth = HTTPBasicAuth(USERNAME, API_TOKEN)


def fix_url(url: str) -> str:
    # Jenkins returns localhost URLs → fix for Docker
    return url.replace("http://localhost:8080", JENKINS_BASE)


def get_last_failed_build():
    root = requests.get(f"{JENKINS_BASE}/api/json", auth=auth)
    root.raise_for_status()

    jobs = root.json().get("jobs", [])

    for job in jobs:
        job_url = fix_url(job["url"])

        job_api = requests.get(f"{job_url}api/json", auth=auth)
        job_api.raise_for_status()

        last_failed = job_api.json().get("lastFailedBuild")
        if not last_failed:
            continue

        build_url = fix_url(last_failed["url"])

        build = requests.get(f"{build_url}api/json", auth=auth).json()
        console = requests.get(f"{build_url}consoleText", auth=auth).text

        return {
            "job_name": job["name"],
            "build": {
                "run_id": build["number"],
                "status": build["result"],
                "timestamp": build["timestamp"],
                "url": build_url
            },
            "pipeline": {
                "failed_stage": build.get("stages", "unknown")
            },
            "logs": {
                "raw": console[:5000]
            }
        }

    return {"message": "No failed builds found"}
