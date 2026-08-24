---
name: plain_language_discharge_instructions
description: "Run when discharge instructions must be rewritten for patient-friendly comprehension."
version: "1.0.0"
category: healthcare
tags: [discharge, healthcare, instructions, language, plain]
agents_used: []
---
# Plain Language Discharge Instructions

## Trigger phrase
Run when discharge instructions must be rewritten for patient-friendly comprehension.

## Required inputs
- Clinical discharge content (medications, follow-up, warning signs).
- Patient context (language proficiency, health literacy, caregiver support).
- Institution requirements (mandatory legal/safety wording).

## Output schema
- `plain_language_instructions`: patient-facing instructions in plain language with clear sequencing.
- `teach_back_prompts`: questions staff can use to confirm patient understanding.
- `safety_escalation_section`: urgent red-flag symptoms and action steps.

## Validation checklist
- [ ] Medical jargon is minimized or immediately explained.
- [ ] Medication and follow-up steps are specific, ordered, and unambiguous.
- [ ] Urgent symptoms include explicit escalation actions and timing.
- [ ] Required institutional/legal statements are preserved.
