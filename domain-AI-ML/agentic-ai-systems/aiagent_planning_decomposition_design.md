---
title: "AI Agent Planning & Task-Decomposition Design"
category: AI-ML/agentic-ai-systems
description: "Design an agent's planning subsystem — how it decomposes a goal into steps, represents and validates a plan, and decides when to replan — choosing the lightest planning strategy that the task's structure and uncertainty actually require."
techniques:
  - ST-02
  - RT-02
  - AG-27
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - planning
  - task-decomposition
  - replanning
  - hierarchical-planning
  - plan-validation
updated: "2026-06-18"
related_prompts:
  - domain-AI-ML/agentic-ai-systems/aiagent_architecture_design.md
  - domain-AI-ML/agentic-ai-systems/aiagent_orchestration_topology_selection.md
  - domain-prompt-engineering/agent-workflows/agent_planner_worker_judge_prompts.md
---

# AI Agent Planning & Task-Decomposition Design

**Objective:** Turn a goal and its uncertainty profile into a concrete planning subsystem — the decomposition strategy, the plan representation, the validation step, and the replanning triggers — choosing the least elaborate planning approach that the task's structure actually demands rather than defaulting to an explicit planner.

**When to Use:**
- The agent's architecture (decided in `aiagent_architecture_design.md`) calls for plan-then-execute or hierarchical planning and you must now design the planner itself.
- An agent produces plans that are vague, unverifiable, or that it never revises when reality diverges.
- A long task needs to be broken into checkpointed sub-goals that survive a partial failure.

**When NOT to Use:**
- A fixed pipeline or single reactive loop suffices — designing a planner adds reasoning cost and a new failure surface (revisit `aiagent_architecture_design.md`).
- You only need the planner/worker/judge *prompt scaffolding* — use `domain-prompt-engineering/agent-workflows/agent_planner_worker_judge_prompts.md`.
- You are choosing how multiple agents coordinate — use `aiagent_orchestration_topology_selection.md`.

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Goal & done-signal** — the objective and the observable artifact/state that marks completion.
- **Task structure** — is the work decomposable into separable sub-goals, and are they sequential or parallelizable?
- **Uncertainty profile** — how much is knowable up front vs. discovered only by acting (which determines static vs. reactive planning).
- **Step cost & reversibility** — expense and blast radius of executing a planned step before it can be validated.
- **Budgets** — token/cost/latency ceilings that planning overhead competes against.

## Constraints

**Must:**
- Choose the lightest planning strategy that fits the uncertainty: fixed sequence → reactive (replan-each-step) → plan-then-execute → hierarchical, escalating only with a stated reason.
- Make every plan step have a checkable precondition and postcondition, so a step's success/failure is observable rather than assumed.
- Define explicit replanning triggers (a postcondition fails, an assumption is invalidated, new information arrives, a step-budget is exceeded) and a replanning ceiling so the agent cannot replan forever.

**Must Not:**
- Generate a multi-step plan when the next action is always determined by the latest observation (that is a reactive loop, not a plan).
- Emit plan steps whose completion can't be verified ("understand the codebase", "handle errors").
- Leave replanning open-ended — invent new plans on every minor deviation, or never replan when the world has clearly changed.
- Fabricate effort, latency, or success-probability figures for steps; reason from the user's inputs and mark unknowns.

**Instructions:**

1. **Restate the goal as a verifiable done-signal.** If "done" isn't checkable by code or rubric, fix that before planning — an unverifiable goal makes every plan unfalsifiable.

2. **Classify the uncertainty.** Decide how much of the path is knowable up front. High up-front knowability favors plan-then-execute; high discovery-as-you-go favors reactive replanning; deep nesting favors hierarchical decomposition.

3. **Select the decomposition strategy and justify lighter rejections.** State why a fixed sequence or a pure reactive loop is insufficient before adopting an explicit or hierarchical planner.

4. **Define the plan representation.** Specify the unit of a plan step: its precondition, action, postcondition (verification), and its dependency/ordering relation to other steps. Decide whether the plan is a flat list, a DAG, or a tree of sub-goals.

5. **Design plan validation.** Specify how a plan is checked before execution (feasibility, missing preconditions, irreversible steps placed before validation) and how each step's postcondition is verified after execution.

6. **Define replanning triggers and ceiling.** Enumerate the conditions that invalidate the current plan and force a replan, and cap the number of replans before the agent escalates or aborts.

7. **Place checkpoints and irreversibility gates.** Mark where partial progress is durably recorded and where an irreversible step requires validation (or human approval) before it runs.

8. **Tally planning overhead vs. benefit.** Estimate the extra tokens/latency planning adds and state the concrete reliability or cost gain that justifies it against the simpler baseline.

**Output Format:**

A markdown design doc:
- **Goal & Done-Signal** — verifiable completion condition
- **Uncertainty Classification** — knowable-up-front vs. discovered
- **Planning Strategy** — chosen approach + why lighter options were rejected
- **Plan Representation** — step schema (pre/action/post) + structure (list/DAG/tree)
- **Validation** — pre-execution plan checks + per-step postcondition checks
- **Replanning** — trigger list + replanning ceiling + escalation
- **Checkpoints & Irreversibility Gates**
- **Overhead vs. Benefit** — planning cost weighed against the baseline

## Verification

- [ ] The done-signal is checkable by code or rubric, not prose.
- [ ] The chosen planning strategy is the lightest that fits the uncertainty, with rejected lighter options named.
- [ ] Every plan step has a verifiable postcondition.
- [ ] Replanning triggers are enumerated and a replanning ceiling exists — no infinite replan.
- [ ] Irreversible steps are gated behind validation or approval, and checkpoints capture partial progress.
- [ ] Planning overhead is weighed against a concrete reliability/cost gain.

## False-Positive Prevention

❌ **DON'T:**
- Call a plan "good" because it reads coherently, without checking that each step's completion is observable.
- Add an explicit planner because the task "has many steps" — a reactive loop also executes many steps.
- Treat the first generated plan as fixed and execute irreversible steps before validating earlier postconditions.
- Replan on every small deviation (thrashing) or never replan when a core assumption has been falsified.

✅ **DO:**
- Require each step to carry a precondition and a verifiable postcondition.
- Justify an explicit/hierarchical planner against a demonstrated failure of the reactive or fixed-sequence baseline.
- Validate the plan before acting and re-validate assumptions at each checkpoint.
- Bound replanning with explicit triggers and a hard ceiling, then escalate.

## Example Output

```markdown
## Planning Design: Codebase Dependency-Upgrade Agent

### Goal & Done-Signal
Upgrade a named dependency across a repo. Done = build passes + test suite green on a branch + changelog entry written.

### Uncertainty Classification
Mostly discovered-as-you-go: breaking changes surface only when the build runs. Reactive-leaning, with a thin up-front skeleton.

### Planning Strategy
Chosen: **plan-then-execute with reactive replanning per failed build**. Rejected: pure reactive loop — wastes calls re-deriving the skeleton each step; fixed sequence — can't anticipate which call sites break.

### Plan Representation (DAG of steps)
| Step | Precondition | Action | Postcondition |
|---|---|---|---|
| 1 bump version | clean branch | edit manifest | manifest pins new version |
| 2 build | step 1 done | run build | build exits 0 (else replan) |
| 3 fix call sites | build errors listed | patch each | build exits 0 |
| 4 tests | build green | run suite | suite green |
| 5 changelog | suite green | write entry | entry present |

### Validation
Pre: no irreversible step (no publish/deploy in plan). Per-step: postcondition is a command exit code or file check.

### Replanning
Triggers: build fails (→ regenerate step-3 fix list from new errors); >2 failed builds on same error (→ escalate). Replanning ceiling: 4.

### Checkpoints & Irreversibility Gates
Checkpoint after step 2 and step 4 (commit WIP). No irreversible step in scope — publish is out of the agent's tool set.

### Overhead vs. Benefit
Planning adds ~1 call + ~1.5k tokens. Justified: avoids blind edits and gives a clean replanning seam on build failure.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** the design proceeds goal → uncertainty → strategy → representation → validation → replanning.
- **RT-02 (Multi-Dimensional Analysis Framework):** planning strategy is weighed on uncertainty, cost, and reliability together.
- **AG-27 (End-State Task Specification):** the verifiable done-signal anchors the whole plan.
- **CM-02 (Constraint Specification):** budgets, irreversibility gates, and the replanning ceiling govern the planner.
- **QA-01 (Self-Verification):** per-step postconditions and the checklist enforce falsifiable progress.

**Related Prompts:**
- `aiagent_architecture_design.md` — decide whether a planner is warranted before designing one.
- `aiagent_orchestration_topology_selection.md` — when sub-goals map to separate agents.
- `domain-prompt-engineering/agent-workflows/agent_planner_worker_judge_prompts.md` — the prompt scaffolding that implements a planning loop.
