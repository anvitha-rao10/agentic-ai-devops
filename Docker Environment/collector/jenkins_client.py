import requests
from config import JENKINS_URL, JOB_NAME

JENKINS_USER = "admin"          # your Jenkins username
JENKINS_API_TOKEN = "PASTE_TOKEN_HERE"

AUTH = (JENKINS_USER, JENKINS_API_TOKEN)

def fetch_last_build():
    url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/api/json"
    resp = requests.get(url, auth=AUTH)
    resp.raise_for_status()
    return resp.json()

def fetch_console_log():
    url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/consoleText"
    resp = requests.get(url, auth=AUTH)
    resp.raise_for_status()
    return resp.text
