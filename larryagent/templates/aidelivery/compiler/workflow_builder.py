from pathlib import Path
import json
import yaml

def build_workflow(template_path: str, capability_map_path: str, output_path: str) -> dict:
    template = yaml.safe_load(Path(template_path).read_text(encoding="utf-8"))
    capability_map = json.loads(Path(capability_map_path).read_text(encoding="utf-8"))
    ordered = [step for step in template["default_steps"] if step in capability_map["required_capabilities"]]
    steps = []
    for idx, step in enumerate(ordered):
        steps.append({
            "id": step,
            "capability": step,
            "depends_on": [] if idx == 0 else [ordered[idx - 1]],
            "inputs": [],
            "outputs": [],
            "success_criteria": [f"{step} succeeded"],
            "failure_codes": ["MISSING_INPUT", "VALIDATION_FAILED", "EXECUTION_ERROR", "UNKNOWN_ERROR"],
            "evidence_required": [],
            "on_success": ordered[idx + 1] if idx < len(ordered) - 1 else "complete",
            "on_failure": "stop"
        })
    workflow = {
        "workflow_id": "generated-workflow-001",
        "template": template["name"],
        "version": template["version"],
        "steps": steps,
        "completion_criteria": ["all required steps succeeded", "required evidence collected"]
    }
    Path(output_path).write_text(json.dumps(workflow, indent=2, ensure_ascii=False), encoding="utf-8")
    return workflow
