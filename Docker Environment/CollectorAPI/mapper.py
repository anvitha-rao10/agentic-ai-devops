def map_jenkins_metadata(data):
    build = data["build"]
    actions = build.get("actions", [])

    repo = None
    commit = None
    author = None

    for action in actions:
        if "remoteUrls" in action:
            repo = action["remoteUrls"][0]
        if "lastBuiltRevision" in action:
            commit = action["lastBuiltRevision"]["SHA1"]

    changes = build.get("changeSets", [])
    if changes and changes[0]["items"]:
        author = changes[0]["items"][0]["author"]["fullName"]

    return {
        "source": "jenkins",
        "job": {
            "name": data["job_name"],
            "repo": repo,
            "branch": "main"
        },
        "build": {
            "run_id": build["number"],
            "status": build["result"],
            "timestamp": build["timestamp"],
            "url": build["url"]
        },
        "scm": {
            "commit_id": commit,
            "author": author
        },
        "pipeline": {
            "failed_stage": "Checkout Code (SSH)"
        },
        "logs": {
            "raw": data["console"].splitlines()[-15:]
        }
    }
