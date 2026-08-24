---
name: worksheet_difficulty_calibration
description: "Run when a worksheet must be tuned to a target proficiency band before classroom use."
version: "1.0.0"
category: education
tags: [calibration, difficulty, education, worksheet]
agents_used: []
---
# Worksheet Difficulty Calibration

## Trigger phrase
Run when a worksheet must be tuned to a target proficiency band before classroom use.

## Required inputs
- Target learner profile (grade, prior knowledge, accommodations).
- Draft worksheet questions with answer key or scoring rubric.
- Desired difficulty distribution (e.g., 30% basic, 50% proficient, 20% stretch).

## Output schema
- `difficulty_profile`: current estimated distribution by difficulty tier.
- `item_diagnostics`: per-question cognitive demand, likely misconception, and time estimate.
- `revision_plan`: question-level edits to hit target distribution while preserving objective coverage.

## Validation checklist
- [ ] All worksheet items receive a difficulty tier and rationale.
- [ ] Estimated distribution is compared against the desired distribution.
- [ ] Revisions do not remove coverage of required learning objectives.
- [ ] Accessibility and readability considerations are included where relevant.
