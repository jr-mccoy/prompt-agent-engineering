---
name: topology-pick
description: "Surgical Stage-2 run: select the lowest-complexity topology from the 9-topology catalog and name the primitives."
version: "1.0.0"
category: orchestration
tags: [agentic-system, topology, surgical]
agents_used: [system-architect]
---

# /topology-pick — Stage 2 (surgical)

## Context
Jump to topology selection when scope is known. Surgical jumps *between* gates: requires Gate 0 to have passed; does not bypass any gate.

## Requirements
- Scope (`ARCHITECTURE.md §1`) including blast radius. Gate 0 already passed.

## Stages routed & gates enforced
- Stage 2 only. Gate 0 must already be satisfied (the command checks it).

## Scripts this command runs
```bash
python3 scripts/check_gate.py --gate 0 ./bundle   # precondition; refuses if Gate 0 unmet
```

## Hand-off
Stage prompt: `prompts/stage-2-topology.md`; catalog in `authoring/system-patterns/SYSTEM_PATTERN_INDEX.md`.

## Output Format
`ARCHITECTURE.md §3` (topology + selection-variable rationale + primitives).
