---
title: "Dataset Difficulty Stratifier"
category: prompt-engineering/evaluation/eval-datasets
description: "Score and stratify eval cases by difficulty across orthogonal axes, producing a balanced distribution and identifying which strata reveal the most about model capability gaps."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - DT-01
  - RT-05
difficulty: intermediate
tags:
  - difficulty_stratification
  - dataset_curation
  - eval_datasets
  - difficulty_scoring
  - model_capability
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/evaluation/eval-datasets/dataset_synthetic_case_generator.md
  - domain-prompt-engineering/evaluation/eval-datasets/dataset_holdout_split_designer.md
  - domain-prompt-engineering/evaluation/taskdifficulty_decompose_by_axes.md
---

## Objective

Score each case in an eval dataset on a set of difficulty axes, assign a composite difficulty tier (easy/medium/hard), and stratify the dataset so that each tier is represented at a specified proportion. Output includes per-case scores, composite tiers, a stratification plan, and an analysis of which axes differentiate model performance most.

## When to Use

- Before launching an eval campaign: ensure the dataset challenges the model appropriately
- When a dataset is suspected of being too easy (model scores >90%) or too hard (model scores <40%)
- When designing a tiered eval pipeline (canary = easy, full suite = balanced, stress suite = hard)
- When comparing two models: difficulty stratification reveals where capability gaps appear

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `case_inventory` | Yes | List of eval cases (IDs, inputs, behavior labels) |
| `task_description` | Yes | What the prompt does |
| `difficulty_axes` | Optional | Custom axes; defaults to the 5 standard axes below |
| `target_distribution` | Optional | Target % per tier; default: easy 30%, medium 40%, hard 30% |
| `model_scores` | Optional | If model has already been run: include scores per case to calibrate axis weights |

## Constraints

**Must:**
- Score every case on ≥3 difficulty axes
- Assign a composite difficulty tier (easy/medium/hard) to every case
- Produce a tier distribution and compare to `target_distribution`
- Identify which axes show the highest variance across cases (most discriminating)
- If `model_scores` provided: verify that axis-predicted difficulty correlates with observed model score

**Must Not:**
- Assign difficulty based on input length alone — length is one axis, not a proxy for all
- Produce a dataset where any tier is <10% of total cases after stratification
- Score axes without defining what each score level means for this specific task

## Instructions

**Step 1 — Difficulty axis definitions**

Default 5 axes (customize or add for specific tasks):

| Axis | Code | What makes it hard | Scale |
|------|----|---------------------|-------|
| Specification clarity | D1 | How underspecified or ambiguous the input is | 1 (explicit) – 3 (highly ambiguous) |
| Context dependency | D2 | How much implicit context is required to interpret correctly | 1 – 3 |
| Constraint density | D3 | Number of simultaneous constraints that must all be satisfied | 1 – 3 |
| Output verifiability | D4 | How hard it is to check if the output is correct | 1 – 3 |
| Adversarial framing | D5 | How likely the input is to push the model toward a wrong response | 1 – 3 |

For each axis, define what score 1, 2, and 3 means in the context of `task_description`.

**Step 2 — Composite score formula**

Default composite (equal weights):
```
composite = (D1 + D2 + D3 + D4 + D5) / 5
```

Tier assignment:
| Composite | Tier |
|-----------|------|
| 1.0 – 1.6 | Easy |
| 1.7 – 2.3 | Medium |
| 2.4 – 3.0 | Hard |

If `model_scores` are available, adjust axis weights to maximize correlation between composite and observed model failure rate.

**Step 3 — Per-case scoring**

```json
{
  "case_id": "GS-007",
  "axis_scores": {
    "D1": 2,
    "D2": 1,
    "D3": 3,
    "D4": 2,
    "D5": 1
  },
  "composite_score": 1.8,
  "difficulty_tier": "medium",
  "scoring_notes": "<optional: which axis drove the score and why>"
}
```

**Step 4 — Distribution check**

| Tier | Current count | Current % | Target % | Action |
|------|--------------|-----------|----------|--------|
| Easy | N | X% | 30% | [Add/remove/rebalance] |
| Medium | N | X% | 40% | |
| Hard | N | X% | 30% | |

If actual distribution deviates from target by >10% in any tier:
- Over-represented tier: sample down (random or by axis-score proximity to boundary)
- Under-represented tier: add synthetic cases at that tier (see `dataset_synthetic_case_generator.md`)

**Step 5 — Axis discrimination analysis**

For each axis, compute variance across all cases:
- High variance axis: discriminates well; keep in composite
- Low variance axis: all cases score similarly; investigate whether the task lacks this difficulty dimension

If `model_scores` provided, compute Spearman ρ between each axis and model failure rate.
Rank axes by ρ; use top-3 for a reduced composite if full composite is unreliable.

**Step 6 — Calibration against model scores**

If `model_scores` provided:
```
For each tier:
  model_pass_rate_easy  = passes in Easy / cases in Easy
  model_pass_rate_medium = ...
  model_pass_rate_hard   = ...

Expected: easy > medium > hard by ≥15% each
If not: axis weights or tier boundaries need adjustment
```

## Output Format

1. **Axis definitions** — what D1–D5 (or custom) mean for this task, with scale labels
2. **Per-case scores** — JSON array following schema
3. **Distribution table** — current vs. target per tier, with actions
4. **Axis discrimination report** — variance per axis, ρ with model scores if available
5. **Calibration check** — model pass rates per tier (if model scores available)

## Verification

- [ ] Every case scored on ≥3 axes with task-specific scale definitions
- [ ] Composite formula and tier boundaries documented
- [ ] Every tier has ≥10% of total cases after stratification
- [ ] Axis discrimination analysis completed (variance computed for each axis)
- [ ] Distribution deviations from target explained and actioned
