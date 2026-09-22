---
title: "Repair the Prompt From a Bad Output"
category: prompt-engineering/prompt-improvement
description: "Given one specific bad output and the prompt that produced it, diagnose which part of the prompt failed and propose the smallest repair."
techniques:
  - QA-01
  - PR-03
difficulty: intermediate
tags:
  - repair
  - root-cause
  - failure-driven
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/debugging/debug_first_failure_cause_isolator.md
  - domain-prompt-engineering/prompt-improvement/improve_minimal_change_pass.md
---

## Objective

Take a single bad output and the prompt that produced it. Identify which prompt element failed (omission, ambiguity, conflict, missing constraint, missing example) and propose the smallest repair.

## When to Use

- A user reports one specific output that disappointed
- You want a fast, evidence-driven fix without a full audit
- The prompt is otherwise considered acceptable

## Inputs

1. The prompt
2. The exact input that triggered the bad output
3. The bad output (verbatim)
4. What the output should have been (or how it should have differed)

## Failure Cause Taxonomy

- `omission` — required behavior not stated in prompt
- `ambiguity` — prompt allows multiple interpretations; model chose wrong one
- `conflict` — two prompt rules pulled different directions; model picked the unwanted side
- `under-specified format` — output shape was guessable but not declared
- `missing example` — task is in-distribution but novel-shaped; example would have anchored
- `model deviation` — prompt was clear; model failed anyway (escalate to model-behavior diagnostic)

## Constraints

**Must:**
- Pick exactly one primary cause from the taxonomy (additional contributing causes allowed)
- Quote the prompt section responsible (or note its absence)
- Propose a minimal patch
- Predict whether the patch would break other inputs

**Must Not:**
- Default to "omission" without checking ambiguity and conflict first
- Refactor unrelated sections
- Repair a `model deviation` case with prompt edits alone — escalate

## Instructions

1. Read input → bad output → desired output. Identify the gap.
2. Walk the prompt looking for which rule should have prevented the gap.
3. Classify the cause.
4. Propose patch:
   - omission → add specific rule
   - ambiguity → tighten one phrase
   - conflict → resolve precedence
   - under-specified format → add schema
   - missing example → add one example
   - model deviation → escalate (do not patch prompt)
5. Predict patch impact on other input classes.

## Output Format

```
GAP
  desired: <what should have happened>
  actual: <what did happen>

PRIMARY CAUSE: <taxonomy code>
CONTRIBUTING CAUSES: [...]

EVIDENCE
  prompt section: <quote or note absence>

PATCH
  diff:
    + ...
    - ...

PREDICTED IMPACT
  - bad input class: now passes
  - other input class A: <expected behavior>
  - other input class B: <expected behavior>

ESCALATIONS
  - <if model-deviation>: <recommended next step>
```

## Verification

- Primary cause is named and matches the taxonomy
- Patch is minimal (single section / few lines)
- Impact prediction covers more than the failing case
- Model-deviation cases are not silently patched
