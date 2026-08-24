---
title: "Lossy Compression Inside a Quality Tolerance"
category: prompt-engineering/compression-and-cost
description: "Compress a prompt past lossless, accepting bounded behavior changes that pass a tolerance check on the test set."
techniques:
  - CM-01
  - QA-01
difficulty: advanced
tags:
  - lossy
  - compression
  - tolerance
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/compression-and-cost/compression_lossless_rewrite.md
---

## Objective

Reduce token count beyond what lossless rewriting allows by accepting small, bounded changes in behavior, only if the test set still passes within a stated tolerance.

## When to Use

- Lossless compression is not enough
- You have a defined quality bar with measurable tolerance
- Cost or latency wins justify accepting a small quality dip

## Inputs

1. Lossless-compressed prompt
2. Test set with expected outputs
3. Tolerance: e.g., "≥95% of cases pass," "average rubric score ≥0.85"
4. Pre-defined token target

## Constraints

**Must:**
- Define tolerance numerically before compressing
- Apply changes incrementally; measure after each
- Roll back any change that crosses tolerance
- Report which test cases changed and how

**Must Not:**
- Compress without measurement
- Accept hidden regressions on safety/refusal cases
- Skip rollback if tolerance breached

## Lossy Techniques

- Remove redundant examples
- Replace examples with rules
- Remove rationale sentences attached to rules
- Reduce few-shot count
- Replace verbose schema descriptions with terse JSON Schema

## Instructions

1. Set tolerance and target token count.
2. Apply one technique. Run test set. Measure.
3. If pass: keep. If fail beyond tolerance: revert.
4. Repeat until target reached or no acceptable changes remain.
5. Report kept and rejected changes.

## Output Format

```
TOLERANCE
  metric: <accuracy | rubric score | pass rate>
  bar: <value>

ATTEMPTS
  attempt 1: <change>
    tokens saved: <n>
    metric: <value>
    decision: kept | rejected
  attempt 2: ...

KEPT CHANGES
  - <change>: net tokens, behavior delta

REJECTED CHANGES
  - <change>: tolerance breached on <case>

FINAL PROMPT
<prompt>

FINAL METRICS
  tokens: before <n> → after <n>
  metric: before <v> → after <v>
  cases that changed: [<id>]

SAFETY/REFUSAL CHECK
  - <case>: unchanged | flagged
```

## Verification

- Tolerance set numerically before changes
- Each attempt has a measured metric
- Rollbacks occurred when tolerance breached
- Safety/refusal cases unchanged or escalated, not silently regressed
