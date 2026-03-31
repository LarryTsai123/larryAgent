from pathlib import Path

def load_spec_kit_artifacts(source_dir: str) -> dict:
    root = Path(source_dir)
    return {
        "source": "spec-kit",
        "requirement_text": (root / "spec.md").read_text(encoding="utf-8") if (root / "spec.md").exists() else "",
        "plan_text": (root / "plan.md").read_text(encoding="utf-8") if (root / "plan.md").exists() else "",
        "tasks_text": (root / "tasks.md").read_text(encoding="utf-8") if (root / "tasks.md").exists() else "",
    }
