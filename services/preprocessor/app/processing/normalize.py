import re

ANSI_ESCAPE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")

def normalize_log(line: str) -> str:
    """
    Cleans a single log line by removing ANSI colors and trimming spaces
    """
    line = ANSI_ESCAPE.sub("", line)
    return line.strip()
