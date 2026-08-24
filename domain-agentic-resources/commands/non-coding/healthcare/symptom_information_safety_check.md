---
name: symptom_information_safety_check
description: "Run when reviewing symptom guidance content for safety, triage clarity, and harm prevention."
version: "1.0.0"
category: healthcare
tags: [healthcare, information, safety, symptom]
agents_used: []
---
# Symptom Information Safety Check

## Trigger phrase
Run when reviewing symptom guidance content for safety, triage clarity, and harm prevention.

## Required inputs
- Symptom guidance draft or script.
- Target care setting (home care, primary care, urgent care, ER triage).
- Safety standards or clinical escalation policy.

## Output schema
- `safety_findings`: identified safety, ambiguity, or omission risks.
- `triage_clarity_matrix`: symptom scenarios mapped to recommended care level and timeframe.
- `required_revisions`: high-priority edits to reduce unsafe interpretation.

## Validation checklist
- [ ] Red-flag symptoms and emergency triggers are explicit.
- [ ] Triage guidance is consistent with stated care setting and policy.
- [ ] Ambiguous wording that could delay care is identified and revised.
- [ ] Content avoids diagnostic overreach and includes appropriate disclaimers.
