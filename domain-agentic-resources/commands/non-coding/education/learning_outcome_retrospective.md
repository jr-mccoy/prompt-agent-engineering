---
name: learning_outcome_retrospective
description: "Run after instruction to analyze outcome data and refine future teaching cycles."
version: "1.0.0"
category: education
tags: [education, learning, outcome, retrospective]
agents_used: []
---
# Learning Outcome Retrospective

## Trigger phrase
Run after instruction to analyze outcome data and refine future teaching cycles.

## Required inputs
- Learning objectives and success criteria used during instruction.
- Outcome evidence (scores, observations, student work samples).
- Context notes (attendance, pacing changes, interventions used).

## Output schema
- `outcome_snapshot`: objective-by-objective attainment summary with confidence level.
- `root_cause_analysis`: key drivers of success and shortfall categorized by curriculum, instruction, and learner factors.
- `next_cycle_adjustments`: concrete changes for the next cycle with owner and timing.

## Validation checklist
- [ ] Retrospective references objective-level evidence, not only overall averages.
- [ ] At least one root cause is identified for each underperforming objective.
- [ ] Proposed adjustments are specific, assignable, and time-bounded.
- [ ] Recommendations distinguish high-confidence findings from hypotheses.
