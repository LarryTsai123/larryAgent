from .executor import execute_workflow

def run_locally(workflow_path: str, trace_path: str) -> dict:
    return execute_workflow(workflow_path, trace_path)
