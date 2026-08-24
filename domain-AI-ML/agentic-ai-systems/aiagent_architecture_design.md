---
title: "AI Agent Architecture Design"
category: AI-ML/agentic-ai-systems
description: "Design an agent's planning approach, tool set, memory, control loop, and stopping conditions from the task and risk profile, pairing capability with cost, latency, and safety from the start."
techniques:
  - ST-02
  - RT-02
  - AG-29
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - agent-architecture
  - control-loop
  - planning
  - stopping-conditions
  - cost-latency-safety
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_tool_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_evaluation_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_cost_token_budget_design.md
---

# AI Agent Architecture Design

**Objective:** Turn a task and its risk profile into a concrete agent architecture — planning approach, tool set, memory design, control loop, and stopping conditions — with cost, latency, and safety budgets specified as first-class design constraints rather than afterthoughts.

**When to Use:**
- Starting a new agent and you must decide *how much agency* it needs (single-shot tool call vs. iterative loop vs. planner/executor).
- An existing agent "works in the demo" but loops, stalls, or overspends in practice.
- Before writing any orchestration code, to lock the control loop and stopping conditions on paper.

**When NOT to Use:**
- The task is a single deterministic tool call or pure retrieval — an agent loop adds cost and failure surface for no benefit.
- You have already decided the architecture and only need tool schemas (use `aiagent_tool_design.md`) or evaluation (use `aiagent_evaluation_design.md`).
- You are deciding *whether to split into multiple agents* — start with `aiagent_multi_agent_orchestration.md`.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Task definition** — the goal, the inputs the agent receives, and what "done" looks like as an observable artifact.
- **Risk profile** — can the agent take irreversible or external actions (writes, payments, emails, deploys)? What is the blast radius of a wrong action?
- **Latency & cost budget** — acceptable end-to-end latency and per-task token/dollar ceiling, if known.
- **Available tools / APIs** — what the agent can call, and which are read-only vs. state-changing.
- **Environment** — sync vs. async, single-turn vs. long-running, whether a human is available to approve steps.

## Constraints

**Must:**
- Choose the *least* agentic architecture that can plausibly succeed; justify any added autonomy against its cost and failure surface.
- Specify explicit stopping conditions (success, max-steps, budget exhausted, repeated-state/loop, escalation) — never an open-ended loop.
- Pair every capability claim with its cost, latency, and safety implication.

**Must Not:**
- Default to a multi-step planner when a single tool call or fixed pipeline suffices.
- Leave the control loop's termination implicit ("until it finishes").
- Assume tools are reliable, idempotent, or permissioned — flag those as separate design dependencies.

**Instructions:**

1. **State the task contract and the done-signal.** Define the input, the goal, and the concrete artifact or state change that marks success. If "done" can't be checked programmatically or by a rubric, fix that before designing the loop.

2. **Profile risk and reversibility.** Classify each action the agent might take as read-only, reversible-write, or irreversible/external. The highest-risk action it can take sets the oversight and sandboxing requirements (cross-link `aiagent_safety_sandboxing.md`).

3. **Select the planning approach.** Choose along the spectrum — single tool call, fixed pipeline, reactive loop (observe→act), or plan-then-execute — and justify the choice against task complexity, not novelty. State why lighter options were rejected.

4. **Specify the tool set and least privilege.** List the tools the loop needs, mark each read-only vs. state-changing, and remove anything not required by the task contract. Defer schema/error-contract detail to `aiagent_tool_design.md`.

5. **Design memory.** Decide what the agent must remember within a task (scratchpad, observations) and across tasks (long-term store), and how context is bounded. Defer detail to `aiagent_memory_design.md`; here, just name what state the loop depends on.

6. **Define the control loop and stopping conditions.** Specify the step structure, the max-step ceiling, loop/repeated-state detection, the budget circuit breaker, and the escalation path. Every exit must be enumerated.

7. **Attach cost, latency, and safety budgets.** Give a per-task token/dollar ceiling, a latency target, and the safety gate(s). State what happens when each budget is hit (degrade, escalate, abort).

8. **List design dependencies and open questions.** Surface assumptions (tool reliability, human availability, idempotency) the architecture relies on, so they are validated rather than discovered in production.

**Output Format:**

A markdown design doc:
- **Task Contract** — input, goal, done-signal
- **Risk & Reversibility Profile** — action classes + blast radius
- **Architecture Decision** — chosen planning approach + why lighter options were rejected
- **Control Loop Spec** — step structure + all stopping conditions
- **Budgets** — table: Dimension (cost/latency/safety) | Ceiling | Behavior at limit
- **Dependencies & Open Questions** — assumptions to validate

## Verification

- [ ] The chosen architecture is the lightest that can plausibly succeed, with rejected alternatives named.
- [ ] Every stopping condition is enumerated (success, max-step, budget, loop, escalation) — no open-ended loop.
- [ ] Each state-changing action is classified by reversibility and tied to an oversight requirement.
- [ ] Cost, latency, and safety each have an explicit ceiling and a defined behavior at the limit.
- [ ] The done-signal is checkable by code or rubric, not just by vibes.

## False-Positive Prevention

❌ **DON'T:**
- Call an architecture "successful" because it completed the happy-path demo, ignoring its cost, latency, and failure-mode behavior.
- Add a planner or multi-step loop because the task "feels complex" without showing a fixed pipeline would fail.
- Treat "max steps reached" as the only stopping condition and omit loop detection and budget breakers.
- Assume tools return clean, idempotent results and design the loop as if errors never happen.

✅ **DO:**
- Report success only alongside measured/estimated token cost, latency, and the worst-case unsafe action the loop allows.
- Start from the simplest viable architecture and escalate autonomy only where a concrete failure of the simpler option is shown.
- Enumerate every loop exit, including repeated-state detection and a hard budget circuit breaker.
- Treat tool errors, timeouts, and non-idempotency as first-class loop states with defined handling.

## Example Output

```markdown
## Agent Architecture: Support-Ticket Triage & Draft-Reply Agent

### Task Contract
- Input: an inbound support ticket (text + metadata).
- Goal: classify the ticket, attach relevant KB articles, and draft a reply.
- Done-signal: a draft reply + classification written to the ticket as a *suggestion* (never auto-sent).

### Risk & Reversibility Profile
| Action | Class | Blast radius |
|---|---|---|
| Read ticket / KB | Read-only | None |
| Write draft suggestion | Reversible write | Low (human edits before send) |
| Send reply to customer | Irreversible/external | High → NOT granted to agent |

### Architecture Decision
Chosen: **reactive loop (observe→act) with a 6-step ceiling**, not plan-then-execute.
Rejected: full planner — task is shallow (classify → retrieve → draft); a planner adds latency and cost without improving outcomes. Rejected: single call — KB retrieval needs an intermediate tool step.

### Control Loop Spec
Steps: classify → retrieve KB → (optional) re-retrieve → draft → self-check against rubric → emit.
Stopping conditions: (1) draft passes self-check; (2) max 6 steps; (3) token budget hit; (4) same retrieval query repeated twice → stop and emit best-so-far + flag; (5) low-confidence classification → escalate to human queue.

### Budgets
| Dimension | Ceiling | Behavior at limit |
|---|---|---|
| Cost | 8k tokens / ticket | Abort, emit partial draft, flag for human |
| Latency | 20s p95 | Return draft-in-progress, continue async |
| Safety | No outbound send | Send tool not in tool set; draft is suggestion-only |

### Dependencies & Open Questions
- KB retrieval tool assumed read-only and idempotent — confirm.
- Human review queue assumed staffed for low-confidence escalations.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** the design proceeds contract → risk → architecture → loop → budgets.
- **RT-02 (Multi-Dimensional Analysis Framework):** capability is weighed against cost, latency, and safety together.
- **AG-29 (Agent Loop Architecture):** the control loop and its stopping conditions are the core deliverable.
- **CM-02 (Constraint Specification):** budgets and reversibility act as governing constraints.
- **QA-01 (Self-Verification):** the checklist forces the lightest-viable and all-exits-enumerated checks.

**Related Prompts:**
- `aiagent_tool_design.md` — specify the tools the loop calls.
- `aiagent_evaluation_design.md` — measure whether the architecture actually works on cost + safety, not just success.
- `aiagent_cost_token_budget_design.md` — set and enforce the budgets this design references.
