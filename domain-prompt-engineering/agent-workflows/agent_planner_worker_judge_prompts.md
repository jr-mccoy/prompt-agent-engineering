---
title: "Planner / Worker / Judge Three-Prompt Pattern"
category: prompt-engineering/agent-workflows
description: "Author three prompts that form a planner-worker-judge cycle, with strict input/output contracts and a maximum revision loop."
techniques:
  - DC-01
  - QA-01
difficulty: advanced
tags:
  - agents
  - planner-worker-judge
  - chains
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/reasoning-strategies/reasoning_plan_then_execute_split.md
---

## Objective

Produce three prompts — planner, worker, judge — that form a complete loop: planner emits a plan; worker executes it; judge scores. If judge fails the work, route back to worker (or planner) within a revision cap.

## When to Use

- Tasks where execution quality is variable and judging is cheaper than reworking blindly
- Auditable agentic workflows
- Multi-step generation that needs gating

## Inputs

1. The end task and final output schema
2. Plan schema, work output schema, judge rubric
3. Maximum worker-judge cycles (default 2)
4. Whether failed work returns to worker or to planner

## Constraints

**Must:**
- Define each prompt's role, input schema, output schema
- Judge emits a pass/fail per criterion with reasons; never a single overall verdict alone
- Cap revision cycles
- After cap, route to escalation, not silent acceptance

**Must Not:**
- Let the judge also do the work
- Let the worker self-judge (use the judge prompt)
- Pass entire prior history into every prompt; pass only what each needs

## Instructions

1. Define plan schema and judge rubric first.
2. Write planner prompt.
3. Write worker prompt that consumes plan and produces work.
4. Write judge prompt that consumes work + rubric and emits per-criterion result.
5. Define routing on judge failure: re-worker (light) or re-planner (heavy).
6. Define escalation after cap.

## Output Format (the bundle)

```
PLAN SCHEMA
  {steps: [...], constraints: [...]}

WORK SCHEMA
  {step_id, output, evidence}

JUDGE RUBRIC
  - criterion_1: pass condition
  - criterion_2: ...

PROMPT A: PLANNER
  Role: ...
  Input: <task>
  Output: <plan>
  Constraints:
    - emit plan only
    - constraint set must be complete

PROMPT B: WORKER
  Role: ...
  Input: <plan + task context>
  Output: <work matching schema>
  Constraints:
    - follow plan literally
    - if step infeasible, surface and stop

PROMPT C: JUDGE
  Role: ...
  Input: <plan + work + rubric>
  Output:
    {
      "per_criterion": [{name, pass, reason}],
      "overall": "pass" | "fail",
      "route": "accept" | "re_worker" | "re_planner",
      "feedback": "<specific actionable items>"
    }

LOOP
  cycle = 0
  while cycle < <cap>:
    work = worker(plan)
    verdict = judge(work)
    if verdict.overall == "pass": return work
    plan = planner(plan, verdict.feedback) if verdict.route == "re_planner" else plan
    cycle += 1
  escalate
```

## Verification

- Each prompt is independently runnable with its declared inputs
- Judge output is per-criterion, not just overall
- Cycle cap prevents infinite loop
- Routing decision is in judge output, not in caller logic
