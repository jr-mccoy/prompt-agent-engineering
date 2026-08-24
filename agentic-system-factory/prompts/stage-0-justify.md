---
title: "Stage 0 — Justify the Agent (Gate 0: complexity ladder)"
category: agentic-system-factory/stage-0-justify
description: "The first gate of the factory. Force the question 'does this need an agent at all?' before any design. Walk the complexity ladder (function → direct call → workflow → agent → multi-agent), stop at the lowest rung that works, and either record a one-sentence written justification an agent is required, or STOP here with a workflow recommendation. Talking the user down the ladder is a success, not a failure."
techniques:
  - ST-01
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - complexity-ladder
  - gate-0
  - agent-justification
  - workflow-vs-agent
updated: "2026-07-02"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_complexity_ladder_gate.md
  - authoring/system-patterns/SYSTEM_QUICK_START.md
  - agentic-system-factory/orchestrator_agentic_system.md
---

# Stage 0 — Justify the Agent (Gate 0)

## Objective
Decide whether the use case genuinely needs an agent, and record the decision as a machine-checkable marker in `ARCHITECTURE.md`. This stage can end the whole exercise — that is the point. The repo's #1 research imperative is to **talk users down the complexity ladder**, not up it. Most things that feel like "an agent" are better served by a deterministic workflow.

## When to Use
- Always first, before any other factory stage. The orchestrator runs this before it will route to Stage 1.
- Surgically, via `/justify-agent`, when you only want the agent-vs-workflow decision.

## Inputs / Context
- The raw use case in one or two sentences.
- What the user currently does manually (if anything) and where it breaks.
- Any hard constraints (latency, cost ceiling, must-not actions).

## Constraints

**Must:**
- Walk the ladder **in order** and stop at the lowest rung that reliably works.
- Produce **either** a non-placeholder one-sentence justification **or** an explicit workflow recommendation — never an unjustified "proceed."
- Emit the Gate-0 marker in `ARCHITECTURE.md` (`GATE-0: JUSTIFIED` or `GATE-0: WORKFLOW-STOP`).

**Must Not:**
- Escalate to multi-agent "to be safe" (≈15× tokens; a poor fit for most interdependent/coding work).
- Assume an agent because the user asked for one — the user's framing is an input, not a verdict.
- Pass Gate 0 with a justification you can't complete honestly.

## Instructions
1. **Walk the ladder** (stop at the first YES):
   - Can a deterministic function / hardcoded rule do this? → **write the function. STOP.** (No LLM.)
   - Can a single model call (± retrieval / one tool) do it reliably? → **direct call. STOP.** Author it as a prompt, not a system.
   - Can a fixed, code-controlled workflow (chain / router / parallel) do it? → **build the workflow. STOP** unless runtime dynamism is genuinely required.
   - Does the task require the **model to decide the next step at runtime** (unknown step count, input-dependent decomposition, dynamic tool choice, runtime replanning)? → an agent is justified. Continue.
2. **Write the justification sentence** (record verbatim in `ARCHITECTURE.md §2`):
   > *"An agent is required because ____ (step count/order not knowable in advance / tool choice depends on intermediate results / needs runtime replanning), and a deterministic workflow cannot because ____."*

   The gate script parses the sentence only when it is wrapped in the justification block, emitted together with the marker as live text in `ARCHITECTURE.md` (the script ignores anything inside code fences):

   ```
   <!-- GATE-0: JUSTIFIED -->
   <!-- JUSTIFICATION-START -->
   An agent is required because <your completed sentence>.
   <!-- JUSTIFICATION-END -->
   ```

   The script rejects an empty block, any remaining `<…>` placeholder, or fewer than 25 characters.
3. **Note the rung and the rejected lower rungs** (why each lower rung fails) — this becomes the topology floor for Stage 2.
4. **State the accepted cost multiple** (~4× single-agent, ~15× multi-agent) against the stated value, so the cost is a conscious choice.
5. **Emit the marker.** If you stopped at a lower rung, emit `GATE-0: WORKFLOW-STOP` and hand back the workflow recommendation — the bundle terminates here, successfully.

## Output Format
- A short ladder walk (one line per rung, with the YES/NO and why).
- The written justification sentence (or the workflow recommendation).
- Rung chosen + rejected lower rungs + accepted cost multiple.
- The Gate-0 marker block for `ARCHITECTURE.md` (see [`../templates/BUNDLE_MANIFEST_TEMPLATE.md`](../templates/BUNDLE_MANIFEST_TEMPLATE.md)).

## Verification Checklist
- [ ] The ladder was walked in order and stopped at the lowest working rung.
- [ ] A non-placeholder justification sentence exists, **or** a workflow was recommended and the stage stopped.
- [ ] Rejected lower rungs are named with reasons.
- [ ] The Gate-0 marker is present in `ARCHITECTURE.md`; on the JUSTIFIED path, the `JUSTIFICATION-START/END` block wraps the sentence (live text, outside any code fence).
- [ ] `python3 scripts/check_gate.py --gate 0 <bundle>` (run from the factory root) returns PASS.

## False-Positive Prevention
- The script's honesty heuristic (non-empty, no `<…>`, ≥25 chars) is a **floor, not proof** — any 25-character sentence passes it. A justification that restates the user's ask ("an agent is required because the user wants an agent") is a false JUSTIFIED; the sentence must name a genuine runtime-dynamism reason and the failing lower rungs, and the orchestrator critique checks that, not the script.
- A false JUSTIFIED here is the most expensive error in the pipeline — every downstream gate inherits it. When the ladder walk is honestly ambiguous, `WORKFLOW-STOP` is the safer terminal (and still a pass).

## References (assembled, not duplicated)
- ⭐ `domain-AI-ML/agentic-ai-systems/aiagent_complexity_ladder_gate.md` — the full Gate-0 prompt this stage runs.
- `domain-AI-ML/agentic-ai-systems/aiagent_multi_agent_orchestration.md` — when-to-split.
- `domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_code_distance_scorer.md` — Delegate/Decompose/DIY.

## Produces
`ARCHITECTURE.md §2` (justification) + the `GATE-0` marker → **Gate 0**.
