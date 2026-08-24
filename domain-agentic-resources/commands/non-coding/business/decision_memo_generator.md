---
name: decision_memo_generator
description: "Run when stakeholders need a concise decision memo with options, tradeoffs, and recommendation."
version: "1.0.0"
category: business
tags: [business, decision, generator, memo]
agents_used: []
---
# Decision Memo Generator

## Trigger phrase
Run when stakeholders need a concise decision memo with options, tradeoffs, and recommendation.

## Required inputs
- Decision context and objective.
- Options under consideration with constraints and assumptions.
- Decision criteria (cost, risk, timeline, strategic fit, etc.).

## Output schema
- `decision_memo`: structured memo including context, options, recommendation, and rationale.
- `options_comparison_table`: criteria-based comparison with weighted scoring or qualitative rationale.
- `decision_risks_and_next_steps`: major risks, mitigations, and immediate execution actions.

## Validation checklist
- [ ] Memo includes a clear single recommendation and why alternatives were not chosen.
- [ ] Comparison criteria align with stated decision objective.
- [ ] Assumptions and uncertainties are explicitly disclosed.
- [ ] Next steps identify owners and near-term deadlines.
