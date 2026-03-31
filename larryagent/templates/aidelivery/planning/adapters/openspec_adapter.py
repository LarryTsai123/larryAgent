from pathlib import Path

def load_openspec_artifacts(source_dir: str) -> dict:
    root = Path(source_dir)
    return {
        "source": "openspec",
        "proposal_text": (root / "proposal.md").read_text(encoding="utf-8") if (root / "proposal.md").exists() else "",
        "design_text": (root / "design.md").read_text(encoding="utf-8") if (root / "design.md").exists() else "",
        "tasks_text": (root / "tasks.md").read_text(encoding="utf-8") if (root / "tasks.md").exists() else "",
    }
