---
title: "Decide When to Add a Few-Shot Example"
category: prompt-engineering/few-shot-examples
description: "Diagnose whether a task needs zero, one, or several few-shot examples, and which to add first if any."
techniques:
  - PR-03
  - QA-01
difficulty: intermediate
tags:
  - few-shot
  - decision
  - zero-shot
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/few-shot-examples/fewshot_example_selector.md
---

## Objective

Decide whether the prompt should run zero-shot, one-shot, or few-shot, based on observed failure modes. Avoid adding examples when explicit rules would do the same job more cheaply.

## When to Use

- A prompt is being designed and you want to start as lean as possible
- An existing prompt has unclear behavior on a new input class
- Token budget is tight and you want to defend each example's place

## Decision Rules

| Failure mode | Add example? | Or alternative |
|---|---|---|
| Output structure inconsistent | Yes (one shot is often enough) | Or: declare schema |
| Vocabulary register wrong | Maybe (one shot) | Or: declare register operationally |
| Wrong content selection (picking wrong field, wrong scope) | Yes | Or: explicit rule |
| Hallucination | No (examples can encourage hallucination) | Use grounding rules |
| Refusal failures | Yes (one negative + one refusal example) | Plus explicit refusal policy |
| Format-only issues | No (declare format) | Schema declaration |
| Ambiguity in interpretation | Yes (two contrasting examples) | Plus disambiguation rule |
| Length overruns | No | Hard cap rule |

## Constraints

**Must:**
- Diagnose which failure mode actually occurs before adding examples
- Prefer rules over examples when both work; defend any example you add
- If adding examples, justify "why one isn't enough" before adding two
- Re-evaluate after each addition

**Must Not:**
- Add examples to "make the prompt feel more complete"
- Add examples for problems that rules already solve
- Skip the diagnosis step

## Instructions

1. List observed failure modes.
2. Map each to the table; pick rule-or-example.
3. If example, pick smallest case that demonstrates the corrected behavior.
4. Add and re-test. If still failing, add a contrasting second example.
5. Stop when failure modes resolve.

## Output Format

```
FAILURE MODES
  - <mode>: <evidence>

DECISIONS
  mode | choice (rule|example) | rationale | added text

PROGRESSION LOG
  step 0: zero-shot
    failures: ...
  step 1: added <example/rule>
    new failures: ...
  step 2: ...

STOPPING CRITERION
  - all listed failure modes resolved
  - or budget reached at K examples

FINAL STATE
  shots: <n>
  rules added: <n>
```

## Verification

- Every added example traces to a specific failure mode
- Rule alternatives were considered and rejected with reason
- Progression stopped when failures resolved
- Token cost recorded per addition
