def collect_evidence(step_id: str, outputs: list[str]) -> dict:
    return {
        "keys": outputs,
        "summary": f"Collected evidence for {step_id}"
    }
