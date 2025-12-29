import requests
from config import JENKINS_URL, JOB_NAME

def fetch_last_build():
    return requests.get(
        f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/api/json"
    ).json()

def fetch_console_log():
    return requests.get(
        f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/consoleText"
    ).text
