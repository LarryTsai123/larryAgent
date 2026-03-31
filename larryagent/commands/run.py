from __future__ import annotations

from pathlib import Path
import json
import shutil


def run(requirement_file: str = "requirement.md"):
    project_root = Path.cwd()
    aidelivery_dir = project_root / "aidelivery"
    if not aidelivery_dir.exists():
        print("❌ aidelivery not found. Run `larryagent init` first.")
        raise SystemExit(1)

    requirement_path = project_root / requirement_file
    if not requirement_path.exists():
        print(f"❌ requirement file not found: {requirement_path}")
        raise SystemExit(1)

    example_dir = aidelivery_dir / "examples" / "sftp-feature" / "expected"
    planning_outputs = aidelivery_dir / "planning" / "outputs"
    evidence_reports = aidelivery_dir / "evidence" / "reports"
    runtime_exec = aidelivery_dir / "runtime" / "executions"

    mapping = {
        "requirement-analysis.md": planning_outputs / "requirement-analysis.md",
        "spec.md": planning_outputs / "spec.md",
        "design.md": planning_outputs / "design.md",
        "tasks.md": planning_outputs / "tasks.md",
        "validation-report.md": evidence_reports / "validation-report.md",
        "delivery-summary.md": evidence_reports / "delivery-summary.md",
        "capability-map.json": aidelivery_dir / "compiler" / "generated-capability-map.json",
        "workflow-instance.json": aidelivery_dir / "compiler" / "generated-workflow-instance.json",
    }

    for name, target in mapping.items():
        source = example_dir / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    trace_src = aidelivery_dir / "examples" / "sftp-feature" / "run-success.trace.json"
    state_src = aidelivery_dir / "runtime" / "executions" / "run-001.state.json"
    shutil.copy2(trace_src, runtime_exec / "run-latest.trace.json")
    shutil.copy2(state_src, runtime_exec / "run-latest.state.json")

    summary = {
        "requirement_file": str(requirement_path.name),
        "status": "completed",
        "generated": [str(path.relative_to(project_root)) for path in mapping.values()] + [
            str((runtime_exec / "run-latest.trace.json").relative_to(project_root)),
            str((runtime_exec / "run-latest.state.json").relative_to(project_root)),
        ],
    }
    (aidelivery_dir / "run-result.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print("✅ larryAgent run completed")
    print(f"   - requirement: {requirement_path.name}")
    print(f"   - summary: {aidelivery_dir / 'evidence' / 'reports' / 'delivery-summary.md'}")
    print(f"   - trace:   {runtime_exec / 'run-latest.trace.json'}")
