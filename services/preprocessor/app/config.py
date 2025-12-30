import os

# Loki base URL (Docker / Local / Prod)
LOKI_BASE_URL = os.getenv("LOKI_URL", "http://loki:3100")

# Loki API endpoints (paths only)
LOKI_PUSH_ENDPOINT = "/loki/api/v1/push"
LOKI_QUERY_ENDPOINT = "/loki/api/v1/query_range"


SSH_ERROR_PATTERNS = {

    # 🔹 Layer 1: Strong SSH failure signals (high confidence)
    "L1_STRONG": [
        r"Permission denied \(publickey\)",
        r"Host key verification failed",
        r"REMOTE HOST IDENTIFICATION HAS CHANGED",
        r"Could not read from remote repository",
        r"ssh_exchange_identification",
        r"No supported authentication methods available",
        r"Too many authentication failures",
        r"Connection timed out",
        r"No route to host",
        r"Connection reset by peer",
        r"Operation timed out",
        r"Connection closed by .* port 22",
        r"ssh: connect to host .* port 22"
    ],

    # 🔹 Layer 2: Git / Jenkins wrapper errors (medium confidence)
    "L2_GIT_WRAPPERS": [
        r"returned status code 128",
        r"Failed to fetch from",
        r"Error fetching remote repo",
        r"fatal:.*repository",
        r"hudson\.plugins\.git\.GitException",
        r"git fetch .* returned status code",
        r"SCMStep\.checkout",
        r"Maximum checkout retry attempts reached"
    ],

    # 🔹 Layer 3: Contextual SSH indicators (supporting signals)
    "L3_CONTEXT": [
        r"git@github\.com",
        r"ssh://",
        r"port 22",
        r"known_hosts",
        r"identity file",
        r"credential.*not found",
        r"using ssh",
        r"publickey"
    ]
}



CONTEXT_BEFORE = 5
CONTEXT_AFTER = 5
