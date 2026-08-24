---
name: agent-eval
description: "Surgical Stage-5 run: design the two independent Gate-B suites (ABC-valid capability + real-tool safety) and emit both markers."
version: "1.0.0"
category: orchestration
tags: [agentic-system, gate-b, eval, safety, surgical]
agents_used: [eval-harness-writer]
---

# /agent-eval — Stage 5 (surgical)

## Context
Jump to the eval harness. Enforces capability ≠ safety: a capable system with no safety eval does not pass Gate B.

## Requirements
- Success criteria + the system's real risk surface (blast radius + untrusted-content seams).

## Stages routed & gates enforced
- Stage 5; runs Gate B at the end.

## Scripts this command runs
```bash
python3 scripts/check_gate.py --gate B ./bundle
```

## Hand-off
Stage prompt: `prompts/stage-5-eval.md`.

## Output Format
`EVAL_HARNESS.md` with both `GATE-B-CAPABILITY` and `GATE-B-SAFETY` markers; Gate B must exit 0.
