---
name: methodology_risk_check
description: "Run before fielding a study or analysis plan to identify methodological failure points early."
version: "1.0.0"
category: research
tags: [methodology, research, risk]
agents_used: []
---
# Methodology Risk Check

## Trigger phrase
Run before fielding a study or analysis plan to identify methodological failure points early.

## Required inputs
- Study objective and primary hypotheses/questions.
- Proposed methodology (sampling, instruments, procedures, analysis plan).
- Operational constraints (timeline, budget, ethics/privacy requirements).

## Output schema
- `risk_register`: ranked methodological risks with likelihood, impact, and detection signal.
- `mitigation_plan`: preventive and contingency actions per high-priority risk.
- `go_no_go_summary`: readiness recommendation with critical blockers if any.

## Validation checklist
- [ ] Risks cover design, sampling, measurement, and analysis threats.
- [ ] High-priority risks include concrete mitigations and owners.
- [ ] Ethics/privacy/compliance constraints are explicitly addressed.
- [ ] Go/no-go recommendation is justified by the documented risk profile.
