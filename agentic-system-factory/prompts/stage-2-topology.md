---
title: "Stage 2 — Select the Topology"
category: agentic-system-factory/stage-2-topology
description: "Pick the lowest-complexity topology that reliably meets the scope, using the three selection variables (who controls the next step; sequence/parallel/conversation; plan known vs runtime). Map to the 9-topology catalog, never escalate beyond the rung Gate 0 justified, and name the primitives the design will need."
techniques:
  - ST-01
  - ST-02
  - DS-06
difficulty: advanced
tags:
  - topology-selection
  - primitives
  - lowest-complexity-fit
updated: "2026-07-02"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_orchestration_topology_selection.md
  - authoring/system-patterns/SYSTEM_PATTERN_INDEX.md
  - agentic-system-factory/prompts/stage-1-scope.md
---

# Stage 2 — Select the Topology

## Objective
Choose the **lowest-complexity topology** that reliably meets the scope, and name the primitives. Record in `ARCHITECTURE.md §3`.

## When to Use
- After Stage 1 scope is complete.
- Surgically via `/topology-pick` when you only need the topology decision.

## Inputs / Context
- Scope (`ARCHITECTURE.md §1`) including blast radius and autonomy level.
- The Stage-0 rung (the complexity floor — don't go below the justified rung, don't escalate above it without reason).

## Constraints

**Must:**
- Choose by the three selection variables: (1) who controls the next step — code or model? (2) sequence, parallel, or conversation? (3) plan known in advance or built at runtime?
- Pick the **lowest-complexity** topology that fits, not the most impressive.
- Name the primitives needed (model call, tool, state, memory, agent, handoff, guardrail, tracing, HITL).

**Must Not:**
- Default to orchestrator-workers or multi-agent without an input-dependent subtask count or genuine breadth-first parallelism.
- Skip naming primitives — they drive Stage 3.

## Instructions
1. Apply the three selection variables and record the answers.
2. Map to the 9-topology catalog (full detail in `authoring/system-patterns/SYSTEM_PATTERN_INDEX.md`):
   1. Direct call · 2. Single agent (loop) · 3. Sequential/chaining · 4. Routing/handoff · 5. Parallel/concurrent · 6. Orchestrator-workers · 7. Evaluator-optimizer · 8. Group chat/debate · 9. Magentic/task-ledger.
3. Justify the choice against the next-lower topology (why it isn't enough) — the mirror of Stage 0's "rejected lower rungs."
4. Name the primitives and note per-primitive specifics (how many agents, which tools, shared vs isolated state, memory type, handoff style, guardrail positions, HITL location).
5. Record the topology + selection-variable rationale + primitives table in `ARCHITECTURE.md §3`.

> Everything compiles to the agent loop (call LLM → typed final output stops; handoff swaps active agent; tool calls run and re-loop; bounded by `max_turns`). A topology is just *how control transfers* in/around that loop.

## Output Format
Fill `ARCHITECTURE.md §3` (Topology & primitives; section layout in [`../templates/ARCHITECTURE_TEMPLATE.md`](../templates/ARCHITECTURE_TEMPLATE.md)).

## Verification Checklist
- [ ] Topology chosen via the three selection variables, recorded.
- [ ] It is the lowest-complexity fit; the next-lower topology is shown to be insufficient.
- [ ] Primitives are named with per-primitive specifics.
- [ ] The chosen rung is consistent with the Stage-0 justification.

## False-Positive Prevention
- A topology chosen because it is impressive (or matches a diagram the user liked) and rationalized backwards is a false fit — the three selection variables must *drive* the choice, and the next-lower topology must be shown insufficient for a named, concrete reason ("router can't X"), not "it felt too simple."
- Naming primitives without per-primitive specifics ("state, memory, guardrails") is false completeness: Stage 3 cannot consume it, and the gap surfaces two stages later as an unspecifiable agent.

## References (assembled, not duplicated)
- ⭐ `domain-AI-ML/agentic-ai-systems/aiagent_orchestration_topology_selection.md` — scorecard selector.
- `domain-AI-ML/agentic-ai-systems/aiagent_planning_decomposition_design.md` — decomposition design.
- `domain-engineering-workflows/ai-patterns/ai_pattern_agent_work_loop_design.md` — run-time loop.

## Produces
`ARCHITECTURE.md §3` → feeds Stage 3 (architecture).
