---
title: "Design a Multi-Call Prompt Chain"
category: prompt-engineering/prompt-creation
description: "Decompose a task into a chain of prompts with explicit handoff contracts, intermediate validation, and failure routing."
techniques:
  - ST-02
  - DC-01
difficulty: advanced
tags:
  - chains
  - decomposition
  - handoff
  - pipelines
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/agent-workflows/agent_planner_worker_judge_prompts.md
  - domain-prompt-engineering/reasoning-strategies/reasoning_plan_then_execute_split.md
---

## Objective

Break a complex task into a chain of N prompts where each step has a typed input contract, typed output contract, and a recovery path when its successor cannot proceed.

## When to Use

- A single-prompt attempt produces inconsistent quality
- Different steps need different models or different temperatures
- Intermediate steps need verification before downstream steps

## Inputs

1. The end-to-end task and its final output spec
2. The cases where the single-prompt version fails
3. Latency or cost budget for the chain
4. Whether intermediate steps are visible to the user

## Constraints

**Must:**
- Define each step's role, input schema, output schema, and rejection conditions
- Define what happens if a step fails: retry, fallback prompt, human escalation
- Forbid silent loss of information across steps
- Make the schema between steps machine-checkable

**Must Not:**
- Pass entire prior outputs forward when only a slice is needed
- Repeat work between steps
- Allow downstream steps to overwrite earlier verified facts without explicit reason

## Instructions

1. List the minimum number of steps that solve the task with isolated concerns.
2. For each step, define the input/output schemas and the rejection conditions.
3. For each step, choose model, temperature, and token budget.
4. Specify the failure routing: retry, fallback, escalate.
5. Specify which steps surface to the user and which run silently.

## Output Format

```
CHAIN: <name>

STEP 1: <name>
  role: ...
  input_schema: ...
  output_schema: ...
  reject_if: ...
  on_fail: <retry N | fallback to <prompt> | escalate>
  model: ...
  temperature: ...
  surface_to_user: <yes | no>
  prompt:
    <prompt body>

STEP 2: ...

DATAFLOW
  step1.output.<field> → step2.input.<field>
  ...

INVARIANTS
  - <fact established in step N must survive to final output>

FALLBACK CHAIN (if main chain fails)
  ...
```

## Verification

- Every input field of step N is produced by some earlier step or external source
- No information dropped between steps without explicit `discard:` annotation
- Each step has a defined failure path
- The chain's combined token cost fits the stated budget
