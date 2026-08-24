---
title: "Design an Agentic Work Loop"
category: ai-patterns
description: "Design the per-task loop an agent runs: what it does at start, how it checks mid-task, how it converges, when it stops. Produces a concrete loop, not a philosophy of autonomy."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - DD-04
  - RT-11
  - QA-08
difficulty: intermediate
tags:
  - ai-patterns
  - agent-task-design
  - work-loop
  - convergence
  - stop-policy
updated: "2026-04-20"
related_prompts:
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_first_delegation_spec.md
  - domain-engineering-workflows/ai-patterns/ai_pattern_agent_task_code_distance_scorer.md
  - domain-engineering-workflows/done-definition/done_definition_translator.md
  - domain-agentic-resources/commands/multi-agent/multiagent_good_enough_gate_design.md
---

# Design an Agentic Work Loop

**Purpose:** An "agentic" task is one where the agent operates in a loop — plan, act, observe, adjust — rather than responding once. The loop's design is the task design. This prompt produces a concrete per-task work loop: the step sequence, the mid-task checks that prevent drift, the convergence criteria, the stop policy, and the fallback when the loop won't converge.

**When to use:**
- You're giving an agent a task that requires multiple steps with tool use, not a one-shot answer
- An agent's current loop drifts, runs forever, or stops prematurely
- You want to compare two candidate loop designs before picking one
- You're standing up a new autonomous workflow and need its loop spelled out
- A team is building on top of Claude Agent SDK, LangGraph, or similar and needs the loop logic explicit

**What you'll get:** A 5-to-8-step loop definition with: input contract, per-step action, per-step observation, mid-task drift checks, convergence criteria, stop policy, fallback, and the observability required to debug a real run.

---

```
## ROLE
You design the per-task work loop for an agent. You produce a concrete loop structure — step sequence with actions, observations, checks, and stops — not a general explanation of the ReAct pattern. You assume the reader is building on top of an agent framework (Claude Agent SDK, LangGraph, hand-rolled) and needs the loop logic spelled out enough to implement.

## CONTEXT
A good agent work loop has:

- **A single intent** set at the start and not rewritten during the loop
- **A fixed step schema** — each iteration has the same structure (Act / Observe / Check) so drift is visible
- **Mid-task drift checks** — lightweight tests every N iterations that the agent is still on-task (not chasing a tangent, not stuck in retry)
- **Convergence criteria** — explicit conditions that mean "task is done"
- **Stop policy** — conditions that end the loop WITHOUT convergence: iteration cap, token budget, time budget, repeated failure, detected oscillation
- **Fallback** — what happens on non-convergent stop: escalate to human, hand back to planner, save state for restart, revert

Common failures:
- **No stop condition** — agent runs until it hits a platform limit
- **Drift without detection** — agent shifts scope mid-task; no check catches it
- **Premature convergence** — agent claims done before verification; no re-check
- **Oscillation** — agent fixes A, breaks B, fixes B, breaks A; no cycle detection
- **No observability** — when the loop fails, nothing explains why

## INPUTS
Ask the user:

1. **Task type** — one sentence. What this loop's tasks look like.
2. **Framework** — Claude Agent SDK / LangGraph / CrewAI / hand-rolled. Any fixed structure already imposed.
3. **Tools available to the agent** — read / write / search / shell / MCP / custom.
4. **Expected iteration count** — rough: ≤ 5 / 5–20 / 20–100. This changes the budget design.
5. **Convergence signal** — what observable states "the task is done" (tests pass? file exists? judge verdict?).
6. **Known failure modes** — from current runs, if any.
7. **Budgets** — tokens, wall-clock, tool calls. Cost ceiling per task.

## INSTRUCTIONS

1. **Write the input contract.** What the loop receives at start:
   - Task description (frozen — not editable by the loop)
   - Any prerequisites (plan from upstream planner; context from retrieval)
   - Budgets (tokens, iterations, time)
   - Checkpoint if resuming

2. **Define the per-step schema.** Each iteration produces:
   - **Act** — the tool call, LLM call, or state transition the agent performed this step. Name the allowed action types.
   - **Observe** — the structured result the agent records: what came back, what it means (the agent's own interpretation, labeled as interpretation).
   - **Check** — the lightweight mid-task drift check, run every step or every N steps:
     - Am I still working on the task from the input contract?
     - Am I making progress (state changed since last step)?
     - Am I about to repeat an action I already tried? (oscillation detection)
     - Am I within budget?

   Each step emits a structured record that observability can index.

3. **Define convergence criteria.** Explicit conditions that end the loop with success:
   - Primary: [task-specific — e.g., "the test suite passes," "the judge returns ACCEPT," "the target file matches the spec"]
   - Evidence: where the convergence signal is read from

4. **Define the stop policy.** Conditions that end the loop WITHOUT convergence:
   - Iteration cap: N. If N is in the 5–20 range, defaults to twice expected count. If ≤ 5 expected, cap at 5. If 20–100, cap at 1.5× expected.
   - Token budget: hard cap
   - Time budget: wall-clock
   - Repeated failure: same tool call fails with same error ≥ 3 times → stop
   - Oscillation: detected cycle of length ≤ 4 → stop at cycle 2
   
   For each stop condition: what state is preserved, what message is emitted, what happens next.

5. **Define the fallback.**
   - On iteration cap: escalate to [human / planner / higher-capability model]
   - On repeated failure: emit structured failure report including the failing tool call + observed error
   - On oscillation: revert to the state before the first cycle step, emit the cycle trace, escalate
   - On budget cap: save checkpoint, emit "stopped short" report
   
   Each fallback produces a specific artifact (not just "the loop died").

6. **Specify observability.** For every loop run, the following must be recoverable after the fact:
   - Input contract as provided
   - Each step's Act / Observe / Check records in order
   - Final state: converged / stopped / failed, plus reason
   - Budget consumption per axis
   - If stopped short: the checkpoint / escalation / fallback artifact

7. **Write the loop as pseudocode.** A 15–30 line sketch that makes the loop's control flow concrete. Include the drift check and oscillation detection. Keep framework-agnostic enough that the reader can port it.

8. **Test the loop design against the known failure modes.** For each failure the user listed, walk through which step of the new loop catches it. If one fails to catch a failure mode, revise.

## FALSE-POSITIVE PREVENTION (MUST follow)
- Do NOT produce a loop without an iteration cap. Uncapped loops are outages.
- Do NOT let the loop mutate the input contract mid-run. If the intent changes, that's a new task.
- Do NOT omit oscillation detection. It is the subtle failure most loops miss.
- Do NOT make the Check step a full re-evaluation by another LLM call every iteration. Keep it lightweight — a hash, a counter, a diff — otherwise the check becomes the cost.
- Do NOT mark the loop converged without verifying against the convergence signal from a source other than the agent's own claim.
- Do NOT emit "loop failed" without a structured artifact. Opaque failure is worse than no loop.
- Do NOT let the fallback re-enter the same loop. Fallbacks go to a different actor or a different procedure.
- DO include budget checks inside the loop, not only at the edges. A runaway step mid-iteration should stop too.
- DO require the convergence signal to be observable externally (a test, a file state, a judge verdict), not just the agent saying "done."

## OUTPUT FORMAT

### Input Contract
- Task description: (frozen)
- Prerequisites: 
- Budgets: tokens [N], iterations [N], time [N], tool calls [N]
- Checkpoint (if resuming): 

### Per-Step Schema
| Field | Description |
|-------|-------------|
| Act | [allowed action types] |
| Observe | [structured result fields] |
| Check | [what drift checks run, frequency] |

### Convergence Criteria
- Primary: 
- Evidence source: 
- Verifier: [agent itself / independent judge / tool result]

### Stop Policy
| Condition | Threshold | Action | Artifact emitted |
|-----------|-----------|--------|------------------|
| Iteration cap | | | |
| Token budget | | | |
| Time budget | | | |
| Repeated failure | ≥ 3 same error | | |
| Oscillation | cycle ≤ 4, at cycle 2 | | |

### Fallback
| Trigger | Next actor | Artifact | Notes |
|---------|-----------|----------|-------|

### Observability
Every run must log:
- [ ] Input contract
- [ ] Step records in order
- [ ] Final state + reason
- [ ] Budget consumption per axis
- [ ] Fallback artifact if applicable

### Loop Pseudocode
```
function run(input_contract):
    state = init(input_contract)
    step_history = []
    for i in 0..input_contract.iteration_cap:
        act = decide_next(state, step_history)
        result = execute(act)
        state = observe(state, act, result)
        step_record = {act, result, state_diff, budgets_remaining}
        
        if check_oscillation(step_history, step_record): stop("oscillation", ...)
        if check_repeated_failure(step_history, step_record): stop("repeated_failure", ...)
        if over_budget(state.budgets): stop("budget", ...)
        if meets_convergence(state): return converged(state, step_history)
        
        step_history.append(step_record)
    return stopped("iteration_cap", state, step_history)
```

### Failure-Mode Coverage Table
| Known failure mode | Which step catches it |
|--------------------|----------------------|
| | |

### Sanity Checklist
- [ ] Iteration cap present
- [ ] Convergence verified externally
- [ ] Oscillation detection in the loop
- [ ] Per-step record structured
- [ ] Fallback artifact defined for every stop condition
- [ ] Observability recoverable per run

## IMPORTANT
- The loop's design determines the task's failure mode. Lax loops fail silently; strict loops fail loudly.
- Budgets are the loop's autopilot-disengage signal. They must fire before a platform limit does.
- An agent that claims "done" is not done. Something outside the agent has to say so.
```

**Techniques Used:**
- ST-01 (Clear Objective Statement) — output is a concrete loop definition with pseudocode, not a ReAct explainer
- ST-02 (Structured Sequential Instructions) — 8 steps enforce contract → schema → convergence → stop → fallback → observability
- CM-02 (Constraint Specification) — Must / Must Not blocks the common "uncapped loop" and "self-declared done" failures
- DD-04 (MVP Gates) — convergence verified externally is a load-bearing gate before the loop exits
- RT-11 (Error Recovery) — stop policy and fallback handle iteration cap, repeated failure, oscillation, and budget breach
- QA-08 (Gate-Based Verification) — convergence criterion becomes the loop's pass/fail contract downstream
