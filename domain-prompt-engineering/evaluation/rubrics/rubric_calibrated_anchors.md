---
title: "Calibrated Rubric Anchors"
category: prompt-engineering/evaluation/rubrics
description: "Create concrete output examples that anchor each score point (1–5) on a rubric dimension, ensuring scorers apply scores consistently and reducing inter-rater variance."
techniques:
  - ST-03
  - CM-02
  - QA-01
  - RT-05
difficulty: intermediate
tags:
  - rubric_design
  - anchor_examples
  - scoring_calibration
  - inter_rater_agreement
  - eval_infrastructure
updated: "2026-05-11"
related_prompts:
  - domain-prompt-engineering/evaluation/rubrics/rubric_inter_rater_agreement_protocol.md
  - domain-prompt-engineering/evaluation/rubrics/rubric_pairwise_vs_pointwise.md
  - domain-prompt-engineering/evaluation/correctness_eval_design_prompt.md
---

## Objective

Produce concrete output examples anchoring each score point (1–5) on a specified rubric dimension. Anchors replace abstract descriptors ("good", "acceptable") with real or constructed output specimens that scorers can compare directly, reducing calibration drift and inter-rater disagreement.

## When to Use

- Designing a new rubric before an eval campaign
- After discovering high inter-rater disagreement on a specific dimension
- When onboarding new human scorers or switching to an LLM judge
- When a rubric dimension produces bimodal score distributions (scorers avoid the middle)

## Inputs

| Field | Required | Description |
|-------|----------|-------------|
| `dimension_name` | Yes | Name of the rubric dimension (e.g., "factual accuracy", "conciseness") |
| `dimension_definition` | Yes | What this dimension measures, in one sentence |
| `task_description` | Yes | What the prompt does; context for what "good" means |
| `real_outputs` | Optional | 5–20 past outputs to use as anchor candidates |
| `score_labels` | Optional | Custom labels for scores (e.g., 1=Failing, 3=Acceptable, 5=Excellent) |

## Constraints

**Must:**
- Produce one concrete anchor example per score point (1–5)
- State the `anchor_rationale` for each anchor: which specific features of the output caused this score
- Ensure anchors are discriminative — a scorer must be able to distinguish adjacent scores (1 vs 2, 2 vs 3, etc.)
- Use real outputs from `real_outputs` when provided; construct examples otherwise
- State the `boundary rule` between each pair of adjacent score points

**Must Not:**
- Use abstract descriptors alone (e.g., "somewhat accurate") without a concrete output
- Produce anchors that could plausibly be scored ±1 from their assigned score — they must be unambiguous
- Anchor only the extremes (1 and 5) and leave middle points abstract

## Instructions

**Step 1 — Dimension decomposition**

Before writing anchors, decompose the dimension into 2–4 observable sub-properties:

```
Dimension: [dimension_name]
Definition: [dimension_definition]
Sub-properties:
  P1: [observable property — present/absent or measurable]
  P2: [observable property]
  P3: [optional]
```

Sub-properties are what scorers actually look at when assigning a score.

**Step 2 — Score-to-property mapping**

| Score | P1 | P2 | P3 | Label |
|-------|----|----|-----|-------|
| 5 | [state] | [state] | [state] | Excellent |
| 4 | [state] | [state] | [state] | Good |
| 3 | [state] | [state] | [state] | Acceptable |
| 2 | [state] | [state] | [state] | Poor |
| 1 | [state] | [state] | [state] | Failing |

**Step 3 — Anchor schema**

```json
{
  "score": 5,
  "label": "Excellent",
  "output_text": "<verbatim output or representative excerpt>",
  "anchor_rationale": "<which sub-properties are satisfied/violated and how>",
  "distinguishing_features": ["<feature that separates this from score 4>"]
}
```

**Step 4 — Boundary rules**

For each pair of adjacent scores, state the decision rule:

| Boundary | Rule |
|----------|------|
| 5 vs 4 | [Observable condition that tips from 4 to 5] |
| 4 vs 3 | [Observable condition] |
| 3 vs 2 | [Observable condition] |
| 2 vs 1 | [Observable condition] |

Boundary rules must be checkable from the output text alone — no domain knowledge required.

**Step 5 — Calibration test**

After writing anchors, produce a calibration mini-set:
- 5 additional outputs not used as anchors
- Assign each a "ground truth" score and rationale
- Use these to train scorers before the main eval run

**Step 6 — Anchor quality checks**

- Adjacent anchors must differ on ≥1 sub-property
- The score-3 anchor must represent the realistic center of the distribution, not the worst-acceptable
- Anchors drawn from `real_outputs` preferred; flag constructed anchors as `[CONSTRUCTED]`

## Output Format

1. **Dimension decomposition** — definition + sub-properties P1–P3
2. **Score-to-property mapping table** — 5 rows
3. **Anchor array** — JSON, one object per score point
4. **Boundary rules table** — 4 boundaries with decision rules
5. **Calibration mini-set** — 5 examples with ground truth scores and rationales

## Verification

- [ ] All 5 score points have concrete output text (not just descriptions)
- [ ] Every anchor has `anchor_rationale` citing specific sub-properties
- [ ] Adjacent anchors differ on ≥1 sub-property
- [ ] All 4 boundary rules checkable from output text alone
- [ ] Score-3 anchor represents the realistic center, not a marginal pass
