---
name: source_quality_triage
description: "Run when collecting references and deciding which sources are credible enough for synthesis."
version: "1.0.0"
category: research
tags: [quality, research, source, triage]
agents_used: []
---
# Source Quality Triage

## Trigger phrase
Run when collecting references and deciding which sources are credible enough for synthesis.

## Required inputs
- Research question or decision context.
- Candidate source list (links, citations, or documents).
- Quality criteria (authority, recency, methodology rigor, relevance).

## Output schema
- `triage_decisions`: each source labeled Keep/Use with Caution/Exclude with rationale.
- `quality_scorecard`: normalized scoring per criterion for retained sources.
- `followup_needs`: missing evidence areas and additional source types to seek.

## Validation checklist
- [ ] Every candidate source has a documented triage decision.
- [ ] Recency and methodological rigor are explicitly assessed.
- [ ] Exclusions include clear reason codes (e.g., bias risk, weak methods).
- [ ] Retained set is sufficient to address the full research question scope.
