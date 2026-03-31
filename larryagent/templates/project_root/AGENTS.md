# AGENTS.md

This repository uses **LarryAgent** as an AI delivery control plane.

## Source of truth
- Planning artifacts live in `aidelivery/planning/outputs/`
- Capability contracts live in `aidelivery/capabilities/`
- Workflow templates live in `aidelivery/workflow-templates/`
- The compiled execution truth is `aidelivery/compiler/generated-workflow-instance.json`

## Rules
- Do not bypass governance in `aidelivery/governance/`
- Do not treat workflow templates as runtime truth
- Update evidence reports after delivery work
- Prefer small, testable, evidence-backed changes
