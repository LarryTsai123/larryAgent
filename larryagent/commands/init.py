from __future__ import annotations

from pathlib import Path
import shutil


def _copy_if_missing(source: Path, target: Path) -> None:
    if target.exists():
        return
    if source.is_dir():
        shutil.copytree(source, target)
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def init():
    project_root = Path.cwd()
    package_root = Path(__file__).resolve().parents[1]

    aidelivery_template = package_root / "templates" / "aidelivery"
    aidelivery_target = project_root / "aidelivery"

    if aidelivery_target.exists():
        print("⚠️ aidelivery already exists")
    else:
        shutil.copytree(aidelivery_template, aidelivery_target)
        print("✅ aidelivery scaffold created")

    project_root_template = package_root / "templates" / "project_root"
    _copy_if_missing(project_root_template / "AGENTS.md", project_root / "AGENTS.md")
    _copy_if_missing(project_root_template / ".github" / "copilot-instructions.md", project_root / ".github" / "copilot-instructions.md")
    _copy_if_missing(project_root_template / ".github" / "agents", project_root / ".github" / "agents")
    _copy_if_missing(project_root_template / ".github" / "instructions", project_root / ".github" / "instructions")

    print("✅ larryAgent initialized")
