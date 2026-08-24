---
title: "Prune Few-Shot Examples for Token Savings"
category: prompt-engineering/compression-and-cost
description: "Remove few-shot examples that do not contribute unique signal, validated by per-example ablation against the test set."
techniques:
  - CM-01
  - PR-03
difficulty: advanced
tags:
  - few-shot
  - pruning
  - ablation
updated: "2026-05-09"
related_prompts:
  - domain-prompt-engineering/few-shot-examples/fewshot_example_selector.md
---

## Objective

Drop few-shot examples that do not improve outputs over the remaining set, measured by per-example ablation on a test set. Output: pruned set + ablation evidence.

## When to Use

- Few-shot pack is over budget
- Some examples may be redundant (covering the same axis)
- You want a defensible reason for each kept example

## Inputs

1. Current few-shot pack
2. Test set with expected outputs and a metric
3. Minimum acceptable metric

## Constraints

**Must:**
- Run ablation: remove each example individually, measure metric
- Keep examples whose removal drops metric beyond a threshold
- Drop examples whose removal does not move metric
- Tie-breaking: prefer examples covering otherwise-uncovered axes

**Must Not:**
- Drop examples without ablation evidence
- Skip ablation on the smallest examples (they may still be load-bearing)
- Drop the only example covering an axis even if metric doesn't move (that axis is rare in the test set)

## Instructions

1. Establish baseline metric with full pack.
2. For each example, remove and re-run.
3. Record metric delta.
4. Prune examples with delta below threshold and not sole cover of an axis.
5. Re-run with pruned pack to confirm metric.

## Output Format

```
BASELINE
  examples: <n>
  metric: <value>

ABLATION RESULTS
  example | removed → metric | delta | sole cover of axis? | decision
  e1      | <m1>            | <d1>  | yes/no              | keep | drop
  ...

PRUNED PACK
  - <kept ids>

DROPPED
  - <id>: delta=<d> | reason

FINAL METRIC
  metric: <value>
  delta vs baseline: <within tolerance>

TOKEN SAVINGS
  before: <n>
  after: <n>
```

## Verification

- Every example has ablation data
- Drops do not violate axis coverage
- Final metric within tolerance of baseline
- Token savings reported
