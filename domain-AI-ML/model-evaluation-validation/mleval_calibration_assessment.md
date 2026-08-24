---
title: "Probability Calibration Assessment"
category: AI-ML/model-evaluation-validation
description: "Assess whether a model's predicted probabilities mean what they say (calibration), measure miscalibration, and decide whether and how to recalibrate before downstream use."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - CM-02
  - QA-12
difficulty: intermediate
tags:
  - calibration
  - reliability-diagram
  - ece
  - probability-quality
  - recalibration
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_confusion_matrix_interpretation.md
  - domain-AI-ML/model-evaluation-validation/mleval_metric_selection_guide.md
  - domain-AI-ML/model-evaluation-validation/mleval_error_analysis_slicing.md
---

# Probability Calibration Assessment

**Objective:** Determine whether a model's predicted probabilities are trustworthy as probabilities — i.e., among items it calls "70% likely," roughly 70% actually occur — quantify any miscalibration, identify where it is worst, and recommend whether and how to recalibrate before the scores are consumed downstream.

**When to Use:**
- A downstream system consumes the probabilities directly (expected-value thresholds, cost-based decisions, risk scores, ranking with cutoffs).
- Probabilities are shown to users or used to set thresholds, and you need them to be meaningful.
- A model ranks well (good AUC) but its raw scores are used as if they were true probabilities.

**When NOT to Use:**
- Only the discrete decision/label matters and probabilities are never consumed (calibration may not matter).
- You're reading per-class errors rather than score quality (use `mleval_confusion_matrix_interpretation.md`).

## Inputs / Context

Provide what you can:
- **Predicted probabilities + outcomes** on an evaluation set (the same items, not aggregates).
- **How the probabilities are used** — thresholds, expected-value calculations, displayed to users, ranking.
- **Class balance** — base rate of the positive class.
- **Important slices** — subgroups where calibration may differ (segment, score region, time).
- **Model type** — note that some models (e.g., certain boosted/SVM/neural outputs) are known to be poorly calibrated by default.

## Constraints

**Must:**
- Distinguish **calibration** (do probabilities match observed frequencies) from **discrimination** (does the model rank well) — a model can be excellent at one and poor at the other.
- Measure calibration with a reliability diagram **and** a summary metric (ECE/Brier), with bin support shown so sparse bins aren't over-read.
- Check calibration per slice and per score region, not just overall — average calibration can hide local miscalibration.

**Must Not:**
- Recommend recalibration when probabilities are never consumed as probabilities (only the ranking is used).
- Fabricate calibration numbers or reliability curves; if outcomes aren't provided, describe the method and the data needed.
- Tune the calibrator on the same data used to measure calibration — require a held-out calibration set.

**Instructions:**

1. **Confirm probabilities are actually consumed.** State exactly how the scores are used. If only the ranking/argmax matters, note calibration may be moot and stop or scope down.

2. **Separate discrimination from calibration.** Report a ranking metric (e.g., AUC) and a calibration assessment; make clear they answer different questions.

3. **Build a reliability diagram with support.** Bin predictions, plot predicted vs. observed frequency per bin, and show the count per bin. Identify systematic over- or under-confidence and where.

4. **Compute summary calibration metrics.** Report ECE (and/or MCE) and Brier score, noting binning sensitivity; pair them with the curve rather than reporting a single number alone.

5. **Check calibration across slices and score regions.** Examine whether high-score and low-score regions, and key subgroups, are calibrated; flag local miscalibration the global ECE hides.

6. **Decide whether to recalibrate.** Judge against the downstream tolerance: does the miscalibration change a decision or mislead a user? If yes, recommend recalibration; if the impact is negligible, say so.

7. **Recommend a method and validation.** If recalibrating, suggest a method (Platt/sigmoid, isotonic, temperature scaling for neural nets), fit on a *separate* calibration split, and re-measure ECE/reliability on a held-out set — confirming discrimination is preserved.

**Output Format:**

A markdown assessment:
- **Usage Check** — how probabilities are consumed (and whether calibration matters).
- **Discrimination vs. Calibration** — ranking metric + calibration summary, contrasted.
- **Reliability Diagram** — per-bin predicted vs. observed with support; over/under-confidence pattern.
- **Calibration Metrics** — ECE/Brier with binning note.
- **Slice/Region Calibration** — where calibration is worst.
- **Recommendation** — recalibrate or not; method + validation plan if yes.
- **INSUFFICIENT EVIDENCE** — the correct recommendation where bins carry too little support for the reliability diagram to mean anything, or where the evaluation set is not drawn from the deployment distribution. Recalibrating on a shifted or thin set fits noise and ships it. Name the unblocking datum: the per-bin support needed, or a held-out set from the serving distribution.

## Verification

- [ ] Whether probabilities are actually consumed as probabilities is confirmed first.
- [ ] Discrimination and calibration are reported separately and not conflated.
- [ ] The reliability diagram shows per-bin support so sparse bins aren't over-read.
- [ ] A summary calibration metric (ECE/Brier) accompanies the curve.
- [ ] Calibration is checked per slice/score region, not only overall.
- [ ] Any recalibration is fit on a held-out split and re-validated, preserving discrimination.
- [ ] Where bin support is too thin or the evaluation set is not from the deployment distribution, the recommendation is INSUFFICIENT EVIDENCE with the required support or set named — not "well calibrated."

## False-Positive Prevention

❌ **DON'T:**
- Trust raw model scores as probabilities because AUC is high — good ranking does not imply good calibration.
- Read a reliability bin with 11 items as evidence of miscalibration; sparse bins are noisy.
- Report a single ECE and call it calibrated; local miscalibration in the high-score region can be hidden.
- Fit the calibrator on the same data you measure calibration on — that reports optimistic, leaked results.

✅ **DO:**
- Report discrimination and calibration as distinct properties.
- Show bin support and weight conclusions by it; widen bins or collect data where sparse.
- Inspect the score regions and slices that drive decisions, not just the global average.
- Calibrate on a separate split and re-measure on held-out data, confirming AUC is unchanged.

## Example Output

```markdown
## Calibration Assessment: Loan-Approval Risk Score

### Usage Check
Scores feed an expected-loss threshold (approve if P(default) < 0.08) and are shown to underwriters.
Probabilities are consumed directly → calibration matters a lot.

### Discrimination vs. Calibration
AUC = 0.83 (good ranking). But calibration is poor: the model is systematically over-confident in the
mid-risk region. Ranking quality ≠ probability quality here.

### Reliability Diagram (10 bins, support shown)
| Pred. prob bin | Observed freq | n |
|---|---|---|
| 0.0–0.1 | 0.04 | 9,200 |
| 0.1–0.2 | 0.21 | 3,100 |
| 0.2–0.3 | 0.34 | 1,400 (over-confident: predicts ~0.25, sees 0.34) |
| 0.3–0.4 | 0.46 | 540 |
| 0.9–1.0 | 0.71 | 60 (sparse — interpret cautiously) |

### Calibration Metrics
ECE = 0.071 (10 equal-width bins); Brier = 0.052. Miscalibration concentrated in 0.2–0.5 range.

### Slice/Region Calibration
Thin-file applicants: ECE = 0.13 (worse). The approval threshold (0.08) sits in a region that's roughly
calibrated overall but under-confident for thin-file → some safe applicants wrongly rejected.

### Recommendation
Recalibrate: isotonic regression fit on a held-out calibration split (the relationship is non-monotone-ish
and there's enough data). Re-measure ECE per slice and confirm AUC unchanged before adjusting the 0.08 threshold.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** usage → discrimination/calibration → reliability → metrics → slices → decision.
- **RT-02 (Multi-Dimensional Analysis Framework):** separates ranking, calibration, and slice dimensions.
- **DS-02 (Metric Specification):** precise calibration metrics (ECE/Brier) with binning caveats.
- **CM-02 (Constraint Specification):** the downstream tolerance governs whether to recalibrate.
- **QA-12 (False Positives Identification):** sparse-bin and AUC-implies-calibration traps are guarded.

**Related Prompts:**
- `mleval_confusion_matrix_interpretation.md` — when the decision is discrete and you need the error breakdown.
- `mleval_metric_selection_guide.md` — decide whether probability quality is a required metric at all.
- `mleval_error_analysis_slicing.md` — drill into the slice where calibration is worst.
