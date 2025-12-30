def build_context_from_indices(
    logs: list[str],
    error_indices: list[int],
    before: int = 10,
    after: int = 10
) -> list[str]:

    contexts = []
    seen_ranges = []

    for idx in error_indices:
        start = max(0, idx - before)
        end = min(len(logs), idx + after)

        # avoid duplicate overlapping blocks
        if any(start <= r[1] and end >= r[0] for r in seen_ranges):
            continue

        seen_ranges.append((start, end))
        block = "\n".join(logs[start:end])
        contexts.append(block)

    return contexts
