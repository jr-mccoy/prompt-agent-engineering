---
title: "ML Probability Calibration"
category: AI-ML/classical-ml-modeling
description: "Assess whether a classifier's predicted probabilities are trustworthy (reliability curve, ECE, Brier) and, if not, apply and validate the right calibration method — Platt, isotonic, or temperature scaling — on held-out data."
techniques:
  - ST-02
  - DS-02
  - QA-12
  - RT-05
  - CM-02
difficulty: advanced
tags:
  - calibration
  - reliability-curve
  - expected-calibration-error
  - isotonic
  - brier-score
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/classical-ml-modeling/mlmodel_imbalanced_classification_approach.md
  - domain-AI-ML/model-evaluation-validation/mleval_eval_result_skepticism_audit.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_baseline_modeling_plan.md
---

# ML Probability Calibration

**Objective:** Determine whether a classifier's predicted probabilities mean what they claim — that among cases scored 0.7, roughly 70% are positive — using reliability curves and calibration metrics, and if they don't, select, apply, and validate the appropriate calibration method without leaking or degrading discrimination.

**When to Use:**
- Downstream decisions consume probabilities (expected-value thresholds, risk tiers, cost-sensitive routing, displayed risk scores).
- A model ranks well (good AUC) but its probabilities look systematically over/under-confident.
- After resampling/regularization that is known to distort probability outputs.

**When NOT to Use:**
- Only the ranking/ordering is consumed (top-K, AUC-driven) and absolute probabilities never matter.
- The discrimination itself is poor — calibration won't fix a model that can't separate classes (improve the model first).

## Inputs / Context

Provide what you can:
- **How probabilities are used** — thresholds, expected value, risk display, downstream model input.
- **Model family** — some (e.g., naive Bayes, boosted trees, SVM-margins) are notoriously miscalibrated; nets often overconfident.
- **Current evidence** — any reliability plot, ECE/Brier values, or observed over/under-confidence.
- **Data** — class balance, available held-out calibration data, grouping/time structure.
- **Framework** — ask the user (sklearn CalibratedClassifierCV / netcal / custom).

## Constraints

**Must:**
- Assess calibration with both a visual (reliability/calibration curve) and a scalar metric (ECE and/or Brier), reported on a held-out set the model did not train on.
- Fit any calibrator on a separate calibration split (or via CV), never on the training data the base model saw, and validate on yet another untouched set.
- Distinguish calibration (probability accuracy) from discrimination (ranking) — report that calibration must not materially hurt AUC.

**Must Not:**
- Report calibration on training data or claim calibration "by default."
- Quote specific ECE/Brier values or "X is better calibrated" as fact; treat all numbers as illustrative and to be measured.
- Recommend isotonic on a tiny calibration set (it overfits) without flagging the data requirement.

**Instructions:**

1. **Confirm probabilities are actually consumed.** State exactly how the probability is used downstream; if only ranking matters, calibration may be unnecessary — say so.

2. **Measure current calibration.** On a held-out set, plot the reliability curve (binned predicted vs observed frequency) and compute ECE and Brier score. Note the *shape* of miscalibration (over/under-confident, S-curve, sigmoid bias).

3. **Diagnose direction and cause.** Tie the miscalibration shape to likely causes (boosted trees pushing scores to extremes, resampling shifting base rate, small-sample noise) — this guides method choice.

4. **Choose the calibration method.** Map shape/data to method: Platt/sigmoid scaling for sigmoid-shaped distortion and small data; isotonic for monotonic non-sigmoid distortion with sufficient data; temperature scaling for neural-net overconfidence (single-parameter, data-efficient).

5. **Fit leak-safely.** Fit the calibrator on a dedicated calibration split or via cross-validated calibration; respect grouping/time structure; keep a final untouched test set for the after-calibration assessment.

6. **Re-measure and guard discrimination.** Recompute reliability curve, ECE, Brier on the test set; confirm AUC/PR-AUC did not materially drop (calibration should reshape probabilities, not destroy ranking).

7. **Account for prevalence shift.** If deployment base rate differs from the calibration set (or resampling changed it), note that calibration must reflect the *true* operating prevalence, and adjust accordingly.

**Output Format:**

A markdown report:
- **Probability Usage** — how the probability is consumed (and whether calibration is needed).
- **Current Calibration** — reliability-curve description + ECE/Brier on held-out data.
- **Miscalibration Diagnosis** — shape, direction, likely cause.
- **Method Choice** — Platt / isotonic / temperature, with rationale + data requirement.
- **Leak-Safe Fit Plan** — calibration split / CV; grouping/time respected.
- **After-Calibration Check** — re-measured calibration + discrimination guard.
- **Prevalence Note** — alignment to the true operating base rate.

## Verification

- [ ] Calibration is measured on held-out data with both a curve and a scalar metric (ECE/Brier).
- [ ] The calibrator is fit on a separate split/CV, not the base model's training data.
- [ ] The method matches the miscalibration shape and the available data size.
- [ ] Discrimination (AUC/PR-AUC) is re-checked and shown not to materially degrade.
- [ ] Prevalence/base-rate alignment is addressed.
- [ ] No ECE/Brier values are presented as fact; all are illustrative.

## False-Positive Prevention

❌ **DON'T:**
- Assume a model is calibrated because its AUC is high — ranking and calibration are independent.
- Fit the calibrator on the same data the base model trained on — it leaks and looks falsely calibrated.
- Use isotonic regression on a few hundred calibration points — it overfits and produces a jagged, unreliable map.
- Calibrate on a resampled (artificially balanced) set and deploy at the true rare prevalence without correcting the base rate.

✅ **DO:**
- Confirm probabilities are actually consumed before calibrating at all.
- Use a dedicated calibration split (or CV) and report calibration on an untouched test set.
- Pick Platt/temperature for small data or sigmoid distortion; isotonic only with enough data.
- Re-check AUC after calibration and align the calibrator to the true deployment prevalence.

## Example Output

```markdown
## Calibration Assessment: Boosted-Tree Risk Scorer

### Probability Usage
- Scores set a cost-sensitive threshold and are displayed as "risk %" to analysts → absolute probabilities matter → calibration required.

### Current Calibration
- Reliability curve on held-out data is S-shaped: low scores too low, high scores too high (classic boosted-tree extremity). Illustrative ECE ~0.11, Brier ~0.18.

### Miscalibration Diagnosis
- Over-confident at the extremes — gradient boosting pushes margins toward 0/1. Sigmoid-shaped distortion.

### Method Choice
- Platt (sigmoid) scaling fits the S-shape and is data-efficient; isotonic considered only if the calibration set is large enough to avoid overfitting the step function.

### Leak-Safe Fit Plan
- Dedicated calibration split (grouped by entity); base model never sees it. Final test set held out for the after check.

### After-Calibration Check
- Re-measured reliability curve closer to diagonal; ECE/Brier expected to drop; AUC essentially unchanged (calibration reshaped, not re-ranked).

### Prevalence Note
- Calibration set reflects true ~6% prevalence (no resampling); displayed risk % aligns to deployment base rate.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** usage → measure → diagnose → method → re-check flow.
- **DS-02 (Metric Specification):** ECE/Brier + reliability curve as the calibration metric set.
- **QA-12 (False Positives Identification):** guards against calibrating on training data and isotonic overfit.
- **RT-05 (Evidence-Based Reasoning):** method choice anchored to the observed curve shape.
- **CM-02 (Constraint Specification):** held-out fit boundary and true-prevalence alignment.

**Related Prompts:**
- `mlmodel_imbalanced_classification_approach.md` — resampling distorts probabilities and triggers calibration.
- `mleval_eval_result_skepticism_audit.md` — interrogate a model whose probabilities look off.
- `mlmodel_baseline_modeling_plan.md` — set discrimination first; calibration is downstream.
