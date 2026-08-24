---
name: lesson_objective_alignment
description: "Run when a lesson plan needs explicit alignment between activities, assessments, and stated learning objectives."
version: "1.0.0"
category: education
tags: [alignment, education, lesson, objective]
agents_used: []
---
# Lesson Objective Alignment

## Trigger phrase
Run when a lesson plan needs explicit alignment between activities, assessments, and stated learning objectives.

## Required inputs
- Lesson context (grade/level, subject, session length).
- Learning objectives (standards or instructor-authored).
- Planned activities, materials, and assessment method.

## Output schema
- `alignment_summary`: one-paragraph judgment on overall objective alignment.
- `objective_alignment_table`: list of objectives with supporting activity, evidence artifact, and alignment rating (Strong/Partial/Missing).
- `gap_actions`: prioritized fixes for weak or missing alignment with estimated effort (Low/Medium/High).

## Validation checklist
- [ ] Every objective appears at least once in the alignment table.
- [ ] Each activity maps to at least one objective or is flagged as non-instructional.
- [ ] At least one measurable evidence artifact exists per objective.
- [ ] Gap actions are actionable, specific, and ordered by instructional impact.
