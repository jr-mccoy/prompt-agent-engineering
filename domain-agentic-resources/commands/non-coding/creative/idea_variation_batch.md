---
name: idea_variation_batch
description: "Run when multiple distinct concept variations are needed from a single creative brief."
version: "1.0.0"
category: creative
tags: [batch, creative, idea, variation]
agents_used: []
---
# Idea Variation Batch

## Trigger phrase
Run when multiple distinct concept variations are needed from a single creative brief.

## Required inputs
- Base creative brief or seed idea.
- Variation constraints (tone, audience, medium, taboo/exclusion rules).
- Desired number of variations and novelty level.

## Output schema
- `variation_batch`: numbered set of concept variations with one-line hook each.
- `divergence_notes`: how each variation differs in angle, tone, or mechanism.
- `selection_shortlist`: top candidates with rationale against brief goals.

## Validation checklist
- [ ] Variations are meaningfully distinct rather than superficial rewrites.
- [ ] All variations respect stated constraints and exclusions.
- [ ] Novelty level matches the requested risk profile.
- [ ] Shortlist rationale references brief goals and audience fit.
