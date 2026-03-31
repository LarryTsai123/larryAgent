from pathlib import Path
import json

KEYWORD_MAP = {
    "api": "api-design",
    "backend": "backend-implementation",
    "frontend": "frontend-implementation",
    "test": "test-design",
    "integration": "integration-test",
    "runtime": "runtime-validation",
}

BASELINE = [
    "requirement-analysis",
    "spec-generation",
    "design-generation",
    "task-slicing",
]

def resolve_capabilities(tasks_path: str, output_path: str) -> dict:
    text = Path(tasks_path).read_text(encoding="utf-8").lower()
    required = list(BASELINE)
    for keyword, capability in KEYWORD_MAP.items():
        if keyword in text and capability not in required:
            required.append(capability)
    if "code-review-request" not in required:
        required.append("code-review-request")
    if "test-design" not in required:
        required.append("test-design")
    result = {
        "required_capabilities": required,
        "missing_capabilities": [],
        "selected_workflow_template": "feature-delivery"
    }
    Path(output_path).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    return result
