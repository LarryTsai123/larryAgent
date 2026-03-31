from pathlib import Path
import yaml

def merge_contracts(base_contract_path: str, capability_contract_path: str) -> dict:
    base = yaml.safe_load(Path(base_contract_path).read_text(encoding="utf-8"))
    child = yaml.safe_load(Path(capability_contract_path).read_text(encoding="utf-8"))

    merged = dict(base)
    for key, value in child.items():
        if key == "extends":
            continue
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            inner = dict(merged[key])
            inner.update(value)
            merged[key] = inner
        else:
            merged[key] = value
    return merged
