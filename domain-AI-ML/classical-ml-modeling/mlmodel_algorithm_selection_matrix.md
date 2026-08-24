---
title: "ML Algorithm Selection Matrix"
category: AI-ML/classical-ml-modeling
description: "Choose a model family for a tabular/classical ML problem by scoring candidates against task type, data size and shape, interpretability needs, and latency constraints in a transparent decision matrix."
techniques:
  - ST-03
  - RT-02
  - QA-17
  - CM-02
  - DS-06
difficulty: intermediate
tags:
  - model-selection
  - decision-matrix
  - tradeoffs
  - interpretability
  - latency
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/classical-ml-modeling/mlmodel_baseline_modeling_plan.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_interpretability_first_modeling.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_cross_validation_design.md
---

# ML Algorithm Selection Matrix

**Objective:** Recommend a short list of candidate model families for a classical/tabular ML problem by scoring each against the constraints that actually decide fitness — task type, dataset size and shape, interpretability requirements, training/inference latency, and operational maturity — and produce a defensible decision matrix instead of a single off-the-cuff pick.

**When to Use:**
- Starting a new modeling problem and deciding what to try first (and second).
- Justifying a model-family choice to reviewers, regulators, or teammates.
- Re-evaluating a stack when constraints change (e.g., a new latency SLA, an interpretability mandate).

**When NOT to Use:**
- Tuning hyperparameters within an already-chosen family (use `mlmodel_hyperparameter_tuning_strategy.md`).
- Designing the evaluation protocol itself (use `mlmodel_baseline_modeling_plan.md`).
- Deep-learning / unstructured-data problems where the family is dictated by the modality (vision, text, audio).

## Inputs / Context

Provide what you can; the matrix degrades gracefully if some are missing:
- **Task type** — binary/multiclass classification, regression, ranking, anomaly detection, survival.
- **Data shape** — rows, columns, feature types (numeric/categorical/text/mixed), sparsity, missingness.
- **Interpretability requirement** — none / global explanations / per-prediction reasons / fully transparent.
- **Latency & resource constraints** — training budget, inference latency SLA, memory/footprint limits, batch vs online.
- **Operational context** — team familiarity, monitoring/retraining maturity, deployment target.
- **Framework preference** — ask the user; do not assume sklearn vs XGBoost vs LightGBM vs CatBoost.

## Constraints

**Must:**
- Score every candidate on the same named criteria with an explicit weighting tied to the user's stated constraints.
- Recommend at least two families to try (a strong baseline and a likely-stronger contender), not a single winner.
- State the decisive constraint(s) that separate the top candidates.

**Must Not:**
- Default to "use gradient boosting" without checking interpretability and latency requirements against it.
- Quote benchmark accuracy numbers from memory as if they apply to the user's data — reason from data shape, not recalled leaderboards.
- Recommend a deep model for small tabular data without flagging the data-efficiency risk.

**Instructions:**

1. **Restate the decision frame.** Name the task type and the hard constraints (latency SLA, interpretability mandate, data size). Separate hard constraints (disqualifiers) from soft preferences (tie-breakers).

2. **Assemble the candidate set.** List 4–6 plausible families for the task type (e.g., for tabular classification: logistic/linear regression, regularized linear, random forest, gradient-boosted trees, k-NN, a simple neural net). Drop any that violate a hard constraint and say why.

3. **Define and weight the criteria.** Use named axes: predictive headroom, interpretability, training cost, inference latency, robustness to messy/small data, categorical/missing handling, operational maturity. Weight them by the user's constraints.

4. **Score each candidate.** Give a 1–5 score per axis with a one-line justification grounded in the data shape (not a memorized benchmark). Compute a weighted total.

5. **Apply the disqualifier pass.** Re-check the top candidates against hard constraints — a high weighted score that violates the latency SLA or interpretability mandate is disqualified regardless of total.

6. **Recommend a try-order.** Name the family to baseline with and the family most likely to win, with the specific evidence that would confirm the choice (e.g., "if a linear baseline already hits the SLA target, stop").

7. **State the revisit trigger.** Name the condition that should send the user back to this matrix (new SLA, interpretability requirement, 10x data growth).

**Output Format:**

A markdown report:
- **Decision Frame** — task type, hard constraints, soft preferences.
- **Candidate Decision Matrix** — table: Family | each weighted criterion score | Weighted Total | Disqualified? (reason).
- **Recommendation** — try-order with the decisive constraint named.
- **What Would Confirm / Change This** — the test that validates the pick and the revisit trigger.

## Verification

- [ ] Every candidate is scored on the same named axes with weights tied to stated constraints.
- [ ] Hard constraints are applied as disqualifiers, separate from weighted totals.
- [ ] At least two families are recommended (baseline + contender), not one.
- [ ] No accuracy/benchmark numbers are presented as fact; scores are reasoned from data shape.
- [ ] A revisit trigger is stated.

## False-Positive Prevention

❌ **DON'T:**
- Reflexively pick gradient boosting because it "usually wins" — it can violate latency or interpretability constraints outright.
- Recommend a neural net on a few thousand rows of tabular data citing deep-learning prestige.
- Cite a remembered leaderboard score as evidence the family will work on this dataset.
- Treat a high weighted total as the answer while ignoring a hard-constraint violation.

✅ **DO:**
- Treat interpretability and latency as potential disqualifiers, not just soft criteria.
- Reason predictive headroom from data shape (rows, signal, feature types), and mark it as a hypothesis to be confirmed by the baseline run.
- Recommend the simplest family that can meet the constraints first, and escalate only on evidence.
- Name the empirical check (baseline metric vs target) that would settle the choice.

## Example Output

```markdown
## Algorithm Selection: Churn Classification (B2B SaaS)

### Decision Frame
- Task: binary classification (churn next quarter).
- Hard constraints: per-prediction reason codes required (account-manager facing); <50ms inference.
- Soft preferences: minimize retraining toil; mixed numeric + categorical features; ~40k rows, ~60 features.

### Candidate Decision Matrix (weights: interpretability 0.30, headroom 0.25, latency 0.20, ops 0.15, data-fit 0.10)
| Family | Interp | Headroom | Latency | Ops | Data-fit | Weighted |
| --- | --- | --- | --- | --- | --- | --- |
| Regularized logistic regression | 5 | 3 | 5 | 5 | 4 | 4.30 |
| Gradient-boosted trees | 3 | 5 | 4 | 3 | 5 | 3.95 |
| Random forest | 3 | 4 | 3 | 4 | 5 | 3.60 |
| k-NN | 2 | 3 | 2 | 4 | 3 | 2.65 |
| Small MLP | 1 | 4 | 4 | 2 | 2 | 2.55 |

### Recommendation
- Baseline with **regularized logistic regression** — clears the interpretability mandate natively (coefficients → reason codes) and the latency SLA easily.
- Contender: **gradient-boosted trees** with SHAP for reasons — only if logistic headroom is insufficient AND SHAP latency stays under 50ms at serve time (verify, do not assume).

### What Would Confirm / Change This
- Confirm: logistic AUC within ~2 points of GBT on grouped CV → ship logistic, stop.
- Revisit if: SLA tightens below 10ms, dataset grows past ~1M rows, or reason-code requirement is dropped.
```

**Techniques Used:**
- **ST-03 (Output Format Specification):** locks the decision matrix and recommendation structure.
- **RT-02 (Multi-Dimensional Analysis Framework):** scores candidates across weighted axes.
- **QA-17 (Named Scores for Multi-Dimensional Metrics):** the per-axis 1–5 scoring scheme.
- **CM-02 (Constraint Specification):** hard constraints act as disqualifiers.
- **DS-06 (Prioritization & Severity Guidance):** produces a ranked try-order.

**Related Prompts:**
- `mlmodel_baseline_modeling_plan.md` — once a family is chosen, design the first honest model.
- `mlmodel_interpretability_first_modeling.md` — when interpretability is a hard constraint.
- `mlmodel_cross_validation_design.md` — pick the evaluation scheme that will adjudicate candidates.
