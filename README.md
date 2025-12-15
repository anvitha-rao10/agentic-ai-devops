# agentic-ai-devops

This project implements an **Agentic AI–based AIOps/SRE remediation framework** that automatically detects and resolves system and pipeline errors.

---

## 🐳 Docker & Python Environment (Start / Stop Guide)

This project uses **Docker** so all collaborators work in the same Linux + Python environment.

---

## ✅ Prerequisites
- Docker Desktop (installed and running)
- Git

---

## ▶️ START (Run Everything)

Clone the repository and move into the project directory:

```bash
git clone https://github.com/anvitha-rao10/agentic-ai-devops.git
cd agentic-ai-devops
Start the Docker environment:
docker compose up --build
Keep this terminal running.

Enter the Container
Open a new terminal and run:
docker exec -it agentic-ai-devops-env bash
Start Python
Inside the container, start Python:
python
STOP (Stop Everything)
Exit Python:
exit()
Exit the container:
exit
Stop Docker (run on host terminal):
docker compose down

Verify Setup (Optional)
Inside the container, run:
pwd
ls
python --version
Expected results:
Directory: /workspace
Python version: 3.10

## Jenkins Setup (Running Inside Docker)

This project runs **Jenkins inside a Docker container** for CI/CD automation.

---

## ▶Start Jenkins (via Docker Compose)

From the project root:

```bash
docker compose up --build
http://localhost:8080

🔐 Unlock Jenkins (First-Time Setup)

When Jenkins runs for the first time, you will see the Unlock Jenkins screen.

Jenkins generates a one-time admin password inside the container.

📌 Get the Admin Password

Run this command on the host terminal:

docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword


Copy the full output string.

🔓 Complete Jenkins Setup

Open browser:

http://localhost:8080


Paste the admin password

Click Continue

Select Install suggested plugins

Create an admin user (username & password)

Finish setup and reach Jenkins dashboard


### Jenkins Initial Plugin Installation

On first launch, Jenkins automatically installs recommended plugins required for:
- Pipelines
- Git/GitHub integration
- Credentials management
- Build utilities

This process may take a few minutes depending on network speed.  
Green check marks indicate successful installation.  
Red entries usually resolve automatically as dependencies are installed.

After plugin installation, Jenkins prompts to create an admin user and then opens the dashboard.
