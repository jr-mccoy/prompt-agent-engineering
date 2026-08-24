---
title: "Plan-Then-Execute Split"
category: prompt-engineering/reasoning-strategies
description: "Separate a task into a planning prompt and an execution prompt so plans can be reviewed before execution and reused."
techniques:
  - DC-01
  - ST-02
difficulty: advanced
tags:
  - plan-execute
  - two-step
  - chains
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/agent-workflows/agent_planner_worker_judge_prompts.md
  - domain-prompt-engineering/prompt-creation/creation_chain_prompt_designer.md
---

## Objective

Convert a single complex prompt into two prompts: a planner that emits a structured plan, and an executor that runs the plan. The plan is reviewable, cacheable, and reusable.

## When to Use

- Tasks where planning errors are expensive
- Plans recur with small input variations
- A team wants the plan auditable before the model executes

## Inputs

1. The current single-prompt task
2. The plan schema (what a plan looks like)
3. The cost-of-bad-plan vs cost-of-bad-execution
4. Whether plans can be cached or reviewed by humans

## Constraints

**Must:**
- Define the plan schema (steps, dependencies, expected outputs per step)
- Planner emits ONLY the plan, no execution
- Executor consumes the plan and emits results, not reasoning about the plan
- Each prompt is independently runnable

**Must Not:**
- Mix planning and execution in one prompt
- Allow the executor to silently change the plan
- Emit the plan in unstructured prose; it must be parseable

## Instructions

1. Decompose the task into PLAN and EXECUTE stages.
2. Write the planner prompt: input = task; output = plan in schema.
3. Write the executor prompt: input = plan + task context; output = results per step.
4. Define what the executor does if the plan is malformed (refuse, request re-plan).
5. Document caching: which plans can be reused unchanged.

## Output Format

```
PLAN SCHEMA
  steps:
    - id: ...
      action: ...
      inputs: ...
      expected_output: ...
      depends_on: [...]

PLANNER PROMPT
  Role: ...
  Input: <task>
  Output: <plan matching schema>
  Constraints:
    - emit plan only; do not execute

EXECUTOR PROMPT
  Role: ...
  Input: <task + plan>
  For each step in plan order:
    - perform action
    - record output
  Output: results array

DEVIATION RULE
  If the executor cannot run a step:
    - record reason
    - request new plan or escalate
    - do not improvise

CACHE NOTE
  - plans for input class <X> are stable; reuse cached plan
  - plans for input class <Y> change per call; do not cache
```

## Verification

- Planner output matches plan schema; no execution included
- Executor output references plan step IDs
- Deviation rule is named
- Cache rule is documented
