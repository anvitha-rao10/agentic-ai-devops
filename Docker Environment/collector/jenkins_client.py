import requests

JENKINS_URL = "http://localhost:8080"
JOB_NAME = "agentic-ai-devops-pipeline"
USERNAME = "admin"
API_TOKEN = "YOUR_JENKINS_API_TOKEN"


def fetch_last_build():
    url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/api/json"
    r = requests.get(url, auth=(USERNAME, API_TOKEN))
    r.raise_for_status()
    return r.json()


def fetch_console_log():
    url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/consoleText"
    r = requests.get(url, auth=(USERNAME, API_TOKEN))
    r.raise_for_status()
    return r.text
