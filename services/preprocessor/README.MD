# Preprocessor Agent

## Overview
The Preprocessor Agent is responsible for cleaning and extracting high-signal
SSH error lines from raw CI/CD logs. It removes Jenkins/Git noise and outputs
only the actual SSH failure messages for downstream classification.

This service is part of the AIOps Agentic DevOps platform.

---

## Responsibilities
- Receive raw build logs from the Collector Agent
- Push raw logs to Loki for observability (future)
- Detect SSH-related failures using layered pattern matching
- Normalize logs by removing ANSI codes and noise
- Output only true SSH error lines (no context)

---

## Example Input
```text
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.
