---
name: author-agentic-system
description: "Full guided run of the agentic-system factory: interview the use case, walk stages 0–6 (optional 7), enforce gates 0/A/B/C via the scripts, and emit the framework-agnostic design bundle."
version: "1.0.0"
category: orchestration
tags: [agentic-system, factory, gate-enforcement, guided]
agents_used: [system-architect, security-gate-reviewer, eval-harness-writer]
---

# /author-agentic-system — Full Guided Run

## Context
The factory's main entry point. Hands control to `orchestrator_agentic_system.md` in **guided** mode against a bundle directory (default `./bundle/`).

## Requirements
- A use case (one or two sentences). Everything else the orchestrator interviews for.

## Stages routed & gates enforced
- Stage 0 (Gate 0) → 1 → 2 → 3 → Stage 4 (Gate A) → Stage 5 (Gate B) → Stage 6 (Gate C) → optional Stage 7.
- Each gate is enforced by running the script and reading its exit code; the orchestrator refuses to advance on non-zero.

## Scripts this command runs
```bash
python3 scripts/check_gate.py --gate 0 ./bundle
python3 scripts/check_gate.py --gate A ./bundle
python3 scripts/check_gate.py --gate B ./bundle
python3 scripts/validate_bundle.py ./bundle && python3 scripts/check_gate.py --gate C ./bundle && python3 scripts/score_rubric.py ./bundle
```

## Hand-off
Orchestrator: `orchestrator_agentic_system.md` (guided mode).

## Output Format
The terminal framework-agnostic design bundle (see `templates/BUNDLE_MANIFEST_TEMPLATE.md`), production-ready only when validate + all gates + score exit 0.
