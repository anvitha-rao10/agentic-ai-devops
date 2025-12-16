# agentic-ai-devops

This project implements an **Agentic AI–based AIOps / SRE remediation framework** that automatically detects, analyzes, and resolves system and CI/CD pipeline errors (Jenkins, GitHub, etc.) using intelligent agents.

The entire stack runs inside **Docker** to ensure a consistent Linux + Python + Jenkins environment for all collaborators.

---

## Prerequisites

- Docker Desktop (installed and running)
- Git

---

## Clone the Repository

```bash
git clone https://github.com/anvitha-rao10/agentic-ai-devops.git
cd agentic-ai-devops
````

---

## Start the Docker Environment (Python + Jenkins)

Build and start all services:

```bash
docker compose up --build
```

Keep this terminal running.

---

## Access the Python Environment (Inside Container)

Open a new terminal and enter the Python container:

```bash
docker exec -it agentic-ai-devops-env bash
```

Start Python:

```bash
python
```

Exit Python:

```bash
exit()
```

Exit the container:

```bash
exit
```

---

## Stop the Docker Environment

From the project root (host terminal):

```bash
docker compose down
```

---

## Verify Environment (Optional)

Inside the container, you can verify the setup:

```bash
pwd
ls
python --version
```

Expected output:

* Working directory: `/workspace`
* Python version: `3.10`

---

## Jenkins Setup (Running Inside Docker)

Jenkins runs inside a Docker container as part of this project.

After starting Docker Compose, open Jenkins in your browser:

```
http://localhost:8080
```

---

## Unlock Jenkins (First-Time Setup)

On the first launch, Jenkins shows an **Unlock Jenkins** screen.

Jenkins generates a one-time admin password inside the container.

Retrieve the password using:

```bash
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Copy the full output string.

---

## Complete Jenkins Setup

1. Open `http://localhost:8080` in your browser
2. Paste the admin password
3. Click **Continue**
4. Select **Install suggested plugins**
5. Create an admin user (username & password)
6. Finish setup to reach the Jenkins dashboard

---

## Jenkins Plugin Installation

During first launch, Jenkins automatically installs recommended plugins required for:

* Git, Git client, Pipeline

This process may take a few minutes depending on network speed.
Green check marks indicate successful installation.
Any temporary red entries usually resolve automatically as dependencies are installed.

Once completed, Jenkins opens the main dashboard and is ready for pipeline execution.

---
## Add SSH Key for GitHub Integration
Generate SSH Key (Inside Jenkins Container)
```bash
docker exec -it jenkins bash
ssh-keygen -t ed25519 -C "jenkins-github"
```
Press Enter for all prompts (no passphrase).
Add SSH Key to GitHub
Copy the public key:
cat ~/.ssh/id_ed25519.pub


## Steps on GitHub:

1. Go to **GitHub → Settings → SSH and GPG keys**
2. Click **New SSH key**
3. Title: `Jenkins SSH Key`
4. Paste the public key
5. Click **Add SSH key**

---

### Add SSH Key to Jenkins Credentials

1. Jenkins Dashboard → **Manage Jenkins**
2. **Credentials** → **System** → **Global credentials**
3. Click **Add Credentials**
4. Kind: **SSH Username with private key**
5. Username: `git`
6. Private Key → **Enter directly**
7. Paste contents of:

```bash
cat ~/.ssh/id_ed25519
```

8. ID: `github-ssh-key`
9. Save

---

## Create a Jenkins Pipeline

### Add Jenkinsfile to Repository

Create a file named `Jenkinsfile` in the GitHub repository:
Commit and push this file to GitHub.

---

### Create Pipeline Job in Jenkins

1. Jenkins Dashboard → **New Item**
2. Enter name: `agentic-ai-devops-pipeline`
3. Select **Pipeline**
4. Click **OK**
5. Under **Pipeline** section:

   * Definition: **Pipeline script from SCM**
   * SCM: **Git**
   * Repository URL:

     ```
     git@github.com:anvitha-rao10/agentic-ai-devops.git
     ```
   * Credentials: `github-ssh-key`
   * Branch: `*/main`
6. Save

---

## Run the Pipeline

Click **Build Now**.

Expected:

* Jenkins checks out code via SSH
* Pipeline runs successfully
* Workspace and Python version are displayed

## Notes

* Stopping Docker (`docker compose down`) does **not** delete Jenkins jobs or pipelines.
* Jenkins data persists via Docker volumes.
* Restarting Docker brings Jenkins and all configurations back exactly as before.



