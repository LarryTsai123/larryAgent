from __future__ import annotations

from pathlib import Path
import shutil


def _copy_if_missing(source: Path, target: Path):
    if not source.exists():
        print(f"⚠️ skip missing template: {source}")
        return

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

    # 1. 複製 aidelivery
    aidelivery_template = package_root / "templates" / "aidelivery"
    _copy_if_missing(aidelivery_template, project_root / "aidelivery")
    print("✅ aidelivery scaffold created")

    # 2. 複製 project_root 內容
    project_root_template = package_root / "templates" / "project_root"

    _copy_if_missing(project_root_template / "AGENTS.md", project_root / "AGENTS.md")
    _copy_if_missing(
        project_root_template / "github_files" / "copilot-instructions.md",
        project_root / ".github" / "copilot-instructions.md",
        )
    _copy_if_missing(
        project_root_template / "github_files" / "agents",
        project_root / ".github" / "agents",
        )
    _copy_if_missing(
        project_root_template / "github_files" / "instructions",
        project_root / ".github" / "instructions",
        )

    print("✅ Copilot/GitHub scaffolds created")

    # 3. 防呆：如果之前版本曾產生 github_files，就清掉
    generated_github_files = project_root / "github_files"
    if generated_github_files.exists():
        shutil.rmtree(generated_github_files)
        print("🧹 Removed temporary github_files")

    print("🎉 larryagent init complete")
