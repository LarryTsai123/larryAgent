from pathlib import Path
import json

def inject_governance(workflow_path: str, testing_policy_path: str) -> dict:
    workflow = json.loads(Path(workflow_path).read_text(encoding="utf-8"))
    policy = Path(testing_policy_path).read_text(encoding="utf-8").lower()

    step_ids = [step["id"] for step in workflow["steps"]]

    if "integration test" in policy or "integration-test" in policy:
        if "backend-implementation" in step_ids and "integration-test" not in step_ids:
            insert_at = step_ids.index("backend-implementation") + 1
            workflow["steps"].insert(insert_at, {
                "id": "integration-test",
                "capability": "integration-test",
                "depends_on": ["backend-implementation"],
                "inputs": ["test-plan.md", "changed_files"],
                "outputs": ["integration-test-report.md"],
                "success_criteria": ["integration tests passed"],
                "failure_codes": ["MISSING_INPUT", "VALIDATION_FAILED", "EXECUTION_ERROR", "UNKNOWN_ERROR"],
                "evidence_required": ["integration-test-report.md"],
                "on_success": "runtime-validation" if "runtime-validation" in step_ids else "complete",
                "on_failure": "stop"
            })

    Path(workflow_path).write_text(json.dumps(workflow, indent=2, ensure_ascii=False), encoding="utf-8")
    return workflow
