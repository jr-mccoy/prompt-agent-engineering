---
name: justify-agent
description: "Surgical Gate-0 run: walk the complexity ladder and decide agent vs deterministic workflow, emitting the GATE-0 marker (or a workflow-stop recommendation)."
version: "1.0.0"
category: orchestration
tags: [agentic-system, gate-0, complexity-ladder, surgical]
agents_used: []
---

# /justify-agent — Gate 0 (surgical)

## Context
Jump straight to Stage 0. Often the most valuable 10 minutes: the right answer is frequently "use a workflow, not an agent."

## Requirements
- The use case + what's done manually today.

## Stages routed & gates enforced
- Stage 0 only. Emits `GATE-0: JUSTIFIED` (+ justification block) or `GATE-0: WORKFLOW-STOP`.

## Scripts this command runs
```bash
python3 scripts/check_gate.py --gate 0 ./bundle
```

## Hand-off
Stage prompt: `prompts/stage-0-justify.md`. If JUSTIFIED, suggest `/author-agentic-system` to continue.

## Output Format
The ladder walk + written justification (or workflow recommendation) + the GATE-0 marker for `ARCHITECTURE.md`.
