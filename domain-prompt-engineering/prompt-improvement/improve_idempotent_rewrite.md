---
title: "Idempotent Rewrite: Improve Readability Without Changing Behavior"
category: prompt-engineering/prompt-improvement
description: "Rewrite a prompt for clarity and structure while preserving identical behavior on a regression set."
techniques:
  - CM-01
  - QA-01
difficulty: intermediate
tags:
  - rewrite
  - readability
  - behavior-preserving
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/compression-and-cost/compression_lossless_rewrite.md
---

## Objective

Improve a prompt's structure, ordering, and readability without changing what it produces. Behavior on a regression set must be identical (or measurably equivalent within tolerance).

## When to Use

- The prompt is hard to read but works
- A new owner needs to understand it before changing it
- You are preparing for a future behavior change but want clean ground first

## Inputs

1. The current prompt
2. Regression set (5+ inputs with expected outputs)
3. Acceptable equivalence tolerance (exact, semantic, structural)

## Constraints

**Must:**
- Preserve every load-bearing instruction
- Preserve refusal rules and safety language verbatim where they are operative
- Reorder for clarity but not for content change
- Run the rewritten prompt mentally on the regression set; all outputs must equivalence-match

**Must Not:**
- Add or remove rules
- Rename schema fields or output sections
- Change vocabulary in safety/refusal rules

## Instructions

1. Read the current prompt; mark each sentence as load-bearing or scaffolding.
2. Group load-bearing sentences by section (Role, Inputs, Constraints, Output, Verification).
3. Rewrite each section for clarity, preserving every load-bearing claim.
4. For each regression input, predict whether output changes; if any prediction is "yes," revert that change.
5. Emit the rewrite + the equivalence assessment.

## Output Format

```
LOAD-BEARING MAP
  - "<sentence>" → load-bearing | scaffolding

REWRITE
<full rewrite>

EQUIVALENCE ASSESSMENT
  case 1: <expected output> | predicted from rewrite: <output> | match: yes/no
  ...

CHANGES MADE
  - reordering: ...
  - merging adjacent rules: ...
  - rewording (no change in claim): ...

REVERTED CHANGES
  - <change>: <case it would have affected>
```

## Verification

- Every regression case shows `match: yes`
- No new constraint introduced
- Refusal/safety language preserved verbatim where operative
- A reader can locate any load-bearing claim in the same section as before
