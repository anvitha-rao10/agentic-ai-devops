import re
from app.config import SSH_ERROR_PATTERNS

compiled = {
    layer: [re.compile(p, re.IGNORECASE) for p in patterns]
    for layer, patterns in SSH_ERROR_PATTERNS.items()
}

def extract_ssh_error_lines(logs: list[str]) -> list[str]:
    detected = []

    for line in logs:
        # Layer 1: strong SSH signals
        for p in compiled["L1_STRONG"]:
            if p.search(line):
                detected.append(line)
                break

    # Deduplicate while preserving order
    seen = set()
    result = []
    for line in detected:
        if line not in seen:
            seen.add(line)
            result.append(line)

    return result
