---
title: "Test a Prompt's Portability Across Models"
category: prompt-engineering/model-optimization
description: "Run a portability check that scores a prompt's behavior consistency across multiple models and identifies the patterns causing divergence."
techniques:
  - QA-01
difficulty: advanced
tags:
  - portability
  - cross-model
  - testing
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/model-optimization/modelopt_cross_model_migration.md
---

## Objective

Quantify how consistently a prompt behaves across N target models on a fixed test set, and identify which prompt patterns cause divergence so the prompt can be made more portable (or split into per-model variants).

## When to Use

- A team wants one prompt across multiple deployments
- Outputs differ across models and you need to decide: harmonize or split
- Vendor diversification strategy

## Inputs

1. The prompt
2. List of target models (≥3 for a portability claim)
3. Test set with expected behavior or rubric
4. Tolerance for cross-model variance

## Constraints

**Must:**
- Run the same test set on every model
- Score per-model and per-test-case
- Compute a portability score (e.g., agreement rate across models)
- Identify which prompt patterns drive divergence

**Must Not:**
- Conclude portability from average score alone (one model's good might offset another's bad)
- Make claims based on a single test case
- Skip rubric pre-registration; define grading before running

## Instructions

1. Pre-register the rubric.
2. Run the prompt on each model with same test set.
3. Score each model × case.
4. Compute pairwise agreement and overall portability score.
5. Diagnose: which prompt sections trigger different responses?
6. Propose: harmonization edits or per-model variants.

## Output Format

```
SETUP
  prompt ref: ...
  models: [...]
  test set: ...
  rubric: ...

SCORE MATRIX
  case × model | M1 | M2 | M3 | agreement
  c1           | s11| s12| s13| ...
  ...

PORTABILITY SCORE: <fraction>

DIVERGENCE ANALYSIS
  - section <X>: <models> behave differently because <reason>
  - section <Y>: ...

HARMONIZATION OPTIONS
  option 1: edit section <X> to use <neutral pattern>
    expected portability: <new score>
  option 2: split into per-model variants
    expected maintenance cost: ...

DECISION
  - harmonize | split | accept variance
```

## Verification

- Test set identical across models
- Rubric pre-registered
- Portability score is computed, not asserted
- Divergence traces to specific prompt sections
