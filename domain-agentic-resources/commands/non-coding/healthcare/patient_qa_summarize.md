---
name: patient_qa_summarize
description: "Run after patient Q&A interactions to produce concise, accurate visit communication summaries."
version: "1.0.0"
category: healthcare
tags: [healthcare, patient, summarize]
agents_used: []
---
# Patient Qa Summarize

## Trigger phrase
Run after patient Q&A interactions to produce concise, accurate visit communication summaries.

## Required inputs
- Transcript or notes from patient questions and clinician responses.
- Care plan details (medications, tests, follow-up).
- Documentation constraints (EHR fields, privacy/redaction requirements).

## Output schema
- `patient_facing_summary`: concise recap of key answers and next steps in plain language.
- `open_questions_log`: unresolved patient concerns requiring follow-up.
- `documentation_extract`: structured fields for clinical documentation workflows.

## Validation checklist
- [ ] Summary reflects clinician guidance without adding new medical claims.
- [ ] Next steps include owner, timeline, and contact route when possible.
- [ ] Unresolved questions are clearly separated from resolved items.
- [ ] Privacy-sensitive information is handled according to documentation constraints.
