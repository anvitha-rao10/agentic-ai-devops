from app.loki.push_logs import push_logs_to_loki
from app.processing.extract_ssh_errors import extract_ssh_error_lines
from app.processing.normalize import normalize_log



def process_logs(job_name: str, build_id: str, logs: list[str]):
    # Push raw logs to Loki (storage only)
    push_logs_to_loki(job_name, build_id, logs)

    # Extract ONLY SSH error lines
    ssh_errors = extract_ssh_error_lines(logs)

    # Normalize each error line
    cleaned = [normalize_log(line) for line in ssh_errors]

    return cleaned
