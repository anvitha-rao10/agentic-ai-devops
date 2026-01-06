import requests
from config import JENKINS_URL, JOB_NAME

def fetch_last_build():
    url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/api/json"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()

def fetch_console_log():
    url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/consoleText"
    r = requests.get(url)
    r.raise_for_status()
    return r.text


    
