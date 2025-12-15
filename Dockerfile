FROM python:3.10-slim

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

CMD ["bash"]
