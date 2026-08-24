---
title: "Decompose a Task Into Ordered Subtasks"
category: prompt-engineering/reasoning-strategies
description: "Author a prompt that explicitly splits a task into ordered subtasks the model executes in sequence with intermediate outputs."
techniques:
  - DC-01
  - ST-02
difficulty: intermediate
tags:
  - decomposition
  - subtasks
  - sequential
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/prompt-creation/creation_chain_prompt_designer.md
  - domain-prompt-engineering/reasoning-strategies/reasoning_plan_then_execute_split.md
---

## Objective

Build a prompt that names subtasks explicitly, executes them in order, surfaces intermediate outputs, and only emits a final answer after the subtask outputs are coherent.

## When to Use

- The task has natural stages (read → classify → produce → verify)
- Skipping a stage causes failures
- You want intermediate outputs available for downstream consumers

## Inputs

1. The full task
2. Known stages or decomposition
3. Whether intermediate outputs surface to the user

## Constraints

**Must:**
- Name each subtask with a unique label
- Define each subtask's input, output, and acceptance check
- Run subtasks in order; do not start subtask N+1 if N's check fails
- Concatenate intermediate outputs in the response in execution order

**Must Not:**
- Run subtasks in parallel within one prompt unless the task is genuinely parallelizable
- Allow subtask N to silently overwrite subtask M's output
- Skip the acceptance check between subtasks

## Instructions

1. List subtasks. Confirm each has a clear input → output mapping.
2. Define an acceptance check per subtask (a falsifiable test of its output).
3. Define behavior on subtask failure: retry, fallback, escalate, or stop.
4. Lay out the prompt as: SUBTASK 1 → CHECK → SUBTASK 2 → CHECK → ... → FINAL.

## Output Format

```
PROMPT STRUCTURE

SUBTASK 1: <name>
  input: ...
  produce: ...
  acceptance check: ...
  on failure: <retry | stop | fallback>

[Output of SUBTASK 1]

SUBTASK 2: <name>
  ...

[Output of SUBTASK 2]

...

FINAL ANSWER: <schema>

EXECUTION RULE
  - Halt at first failed acceptance check
  - Surface partial outputs achieved before halt
```

## Verification

- Every subtask has a falsifiable acceptance check
- On-failure behavior named per subtask
- Intermediate outputs are visible before final
- Halt rule prevents downstream subtasks running on failed predecessor
