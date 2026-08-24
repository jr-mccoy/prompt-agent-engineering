---
title: "ML Cross-Validation Design"
category: AI-ML/classical-ml-modeling
description: "Choose the cross-validation scheme that matches the data's structure — k-fold, stratified, grouped, or time-series — so the estimated performance reflects real-world generalization instead of a leaky fold split."
techniques:
  - ST-02
  - RT-10
  - QA-12
  - CM-02
  - RT-05
difficulty: intermediate
tags:
  - cross-validation
  - grouped-cv
  - time-series-cv
  - stratification
  - leakage
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_hyperparameter_tuning_strategy.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_baseline_modeling_plan.md
---

# ML Cross-Validation Design

**Objective:** Recommend the correct cross-validation (CV) scheme for a dataset by reasoning from its structure — independence of rows, grouping of correlated entities, class balance, and time ordering — so that the CV estimate is an honest proxy for production generalization rather than an inflated number produced by a mismatched split.

**When to Use:**
- Setting up evaluation for a new model and unsure whether plain k-fold is valid.
- A model's CV score is much higher than its production performance (a split-structure smell).
- Designing the validation protocol that tuning and model comparison will rely on.

**When NOT to Use:**
- Hunting for already-introduced leakage in a built pipeline (use `mldata_data_leakage_detector.md`).
- Selecting the metric to score within CV (use `mlmodel_baseline_modeling_plan.md`).

## Inputs / Context

Provide what you can:
- **Row independence** — are rows i.i.d., or do multiple rows belong to the same entity (user, device, patient, session)?
- **Grouping keys** — any ID that links correlated rows.
- **Time structure** — is there a timestamp and is the deployment use prospective (predict the future)?
- **Target distribution** — class balance (classification), skew (regression).
- **Data size** — total rows and rows per group / per time window.
- **Deployment regime** — batch vs online; how the model will encounter new data.

## Constraints

**Must:**
- Match the CV scheme to the *real* generalization question (predict new entities? predict the future? predict within-distribution?).
- When entities span multiple rows, keep each entity entirely within one fold (grouped CV).
- For time-ordered prospective tasks, never let a fold train on data later than its validation window.

**Must Not:**
- Recommend plain random k-fold when grouping or time structure is present.
- Apply stratification on the target in a way that breaks grouping or time order.
- Quote "typical" CV scores or fold-count effects as fact; reason from structure.

**Instructions:**

1. **State the generalization question.** Decide what "new data" means in production: new entities, future time, or i.i.d. samples. The scheme must simulate that.

2. **Test for row dependence.** Identify grouping keys (same user/device/patient appearing multiple times). If present, the default becomes GroupKFold / leave-one-group-out — random folds would leak entity memorization.

3. **Test for time structure.** If the task predicts the future, choose forward-chaining / expanding-window or rolling-window time-series CV with an embargo/gap to block lookahead and boundary leakage.

4. **Handle class/target balance.** For imbalanced classification, add stratification — but only in a way compatible with grouping (StratifiedGroupKFold) or time order (stratify within windows, not across them).

5. **Set fold count and repeats.** Choose k from data size and variance needs; consider repeated CV for small data; note the bias/variance and compute tradeoffs, without asserting a universally "best" k.

6. **Define the held-out estimate.** Specify whether CV is for selection only and a separate golden/temporal holdout provides the final unbiased estimate (especially if tuning will follow).

7. **Specify pipeline placement.** Confirm all preprocessing is fit inside each training fold; for time CV, features must use only past windows.

8. **State the validity check.** Name a sanity test (e.g., compare grouped vs random CV — a large gap exposes entity leakage; compare time CV vs random — a gap exposes temporal leakage).

**Output Format:**

A markdown report:
- **Generalization Question** — what "new data" means here.
- **Structure Findings** — dependence, time, balance — each with the implied constraint.
- **Recommended CV Scheme** — exact scheme + grouping/stratification/time settings + fold count.
- **Final Estimate Plan** — CV-for-selection vs separate holdout.
- **Pipeline Placement** — fit-in-fold confirmation.
- **Validity Check** — the comparison that confirms the scheme isn't leaking.

## Verification

- [ ] The generalization question is stated and the scheme simulates it.
- [ ] Grouping keys, if present, keep entities within a single fold.
- [ ] Time-ordered tasks use forward-chaining with an embargo/gap.
- [ ] Stratification (if used) is compatible with grouping/time order.
- [ ] A separate unbiased final estimate is specified when tuning will follow.
- [ ] A validity check (grouped-vs-random or time-vs-random gap) is named.

## False-Positive Prevention

❌ **DON'T:**
- Use random k-fold when the same user/device/patient appears in multiple rows — it leaks memorization and inflates the score.
- Use random CV on a prospective time-series task — it trains on the future to predict the past.
- Stratify across time windows in a way that mixes future and past into the same fold.
- Read a high CV score as production-ready without checking the scheme matches deployment.

✅ **DO:**
- Identify grouping keys first and default to GroupKFold / StratifiedGroupKFold when they exist.
- Use expanding/rolling-window CV with an embargo for forecasting and any future-prediction task.
- Keep a separate temporal or grouped golden holdout for the final number when tuning is involved.
- Confirm the scheme by checking that grouped/time CV is not suspiciously higher than its random counterpart.

## Example Output

```markdown
## CV Design: Readmission Risk (per-admission rows, patients repeat)

### Generalization Question
- Production scores *new patients*, prospectively. The CV must simulate unseen patients in future time.

### Structure Findings
- Dependence: patients have multiple admissions → entity leakage risk → grouping required (group = patient_id).
- Time: admissions are time-ordered; deployment is prospective → forward-chaining required.
- Balance: ~12% readmission → stratify the positive class within folds.

### Recommended CV Scheme
- StratifiedGroupKFold on patient_id for model comparison (5 folds), with class stratification.
- Plus a temporal holdout: train on admissions before a cutoff date, evaluate on after, with a 30-day embargo to avoid horizon bleed.

### Final Estimate Plan
- Grouped CV used for selection/tuning; the post-cutoff temporal holdout (touched once) provides the reported estimate.

### Pipeline Placement
- Imputation, encoding, scaling fit inside each training fold. Rolling features use only pre-admission data.

### Validity Check
- Compare StratifiedGroupKFold vs plain StratifiedKFold. If random folds score materially higher, patient-level leakage is confirmed and grouping is justified.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** question → structure → scheme → check flow.
- **RT-10 (Troubleshooting Decision Tree):** branches on dependence/time/balance to a scheme.
- **QA-12 (False Positives Identification):** guards against grouped/temporal leakage via fold design.
- **CM-02 (Constraint Specification):** entity-within-fold and no-lookahead are governing constraints.
- **RT-05 (Evidence-Based Reasoning):** the validity check anchors the scheme in a measurable gap.

**Related Prompts:**
- `mldata_data_leakage_detector.md` — hunt leakage that a bad split would have introduced.
- `mlmodel_hyperparameter_tuning_strategy.md` — the nested protocol that consumes this CV scheme.
- `mlmodel_baseline_modeling_plan.md` — pairs the CV scheme with metric and baseline choices.
