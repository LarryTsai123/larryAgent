import json
from pathlib import Path

def save_state(path: str, state: dict) -> None:
    Path(path).write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")

def load_state(path: str) -> dict:
    p = Path(path)
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))
