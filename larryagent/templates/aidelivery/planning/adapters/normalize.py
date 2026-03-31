from pathlib import Path
import json

def normalize_requirement(requirement_text: str, source: str = "manual") -> dict:
    return {
        "source": source,
        "title": requirement_text.strip().splitlines()[0][:120] if requirement_text.strip() else "Untitled Requirement",
        "raw_requirement": requirement_text,
        "domains": [],
        "constraints": [],
        "assumptions": [],
    }

def save_normalized_requirement(output_path: str, data: dict) -> None:
    Path(output_path).write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
