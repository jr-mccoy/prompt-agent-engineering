---
title: "ML Error Analysis by Slicing"
category: AI-ML/model-evaluation-validation
description: "Systematically dissect model errors by slice and subgroup to find where it fails, how badly, and why — turning an aggregate number into an actionable failure map."
techniques:
  - ST-02
  - RT-05
  - RT-09
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - error-analysis
  - slicing
  - subgroup-performance
  - failure-modes
  - root-cause
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_confusion_matrix_interpretation.md
  - domain-AI-ML/model-evaluation-validation/mleval_evaluation_harness_design.md
  - domain-AI-ML/model-evaluation-validation/mleval_robustness_stress_testing.md
---

# ML Error Analysis by Slicing

**Objective:** Move beyond a single aggregate metric to a structured map of *where* the model fails — by class, subgroup, feature region, and difficulty band — quantify each pocket of failure with its size and severity, and form evidence-backed hypotheses for the cause of each, producing a ranked list of what to fix.

**When to Use:**
- A model passes its aggregate metric but you suspect it fails for important segments.
- Deciding where to invest next (more data, new features, threshold changes) and need to know which errors matter.
- A stakeholder reports a specific failure ("it's bad for new users") and you need to confirm and scope it.

**When NOT to Use:**
- You only need to read a single confusion matrix (use `mleval_confusion_matrix_interpretation.md`).
- You are testing input perturbations / shift robustness specifically (use `mleval_robustness_stress_testing.md`).

## Inputs / Context

Provide what you can; analysis degrades gracefully if some are missing:
- **Predictions + ground truth** on an evaluation set (ideally the golden set), with per-example scores.
- **Slice dimensions** — available metadata to slice on (segment, geography, device, class, source, time, length/size).
- **Primary + guardrail metrics** and the operating point/threshold.
- **Known concerns** — segments the business cares about; prior complaints; high-cost error types.
- **Feature values** for examples, if available, to slice by feature region.

## Constraints

**Must:**
- Report each slice's metric *and its support (n)* so small-sample noise is never mistaken for a failure.
- Attach a confidence interval (or a clear small-n warning) to each slice metric before ranking it.
- Separate *where* the model fails (the slice) from *why* (the hypothesized cause), labeling causes as hypotheses until evidence is shown.

**Must Not:**
- Declare a slice "broken" from a metric difference that is within sampling noise for its sample size.
- Fabricate slice metrics or example counts; if a slice cannot be computed from the input, say so.
- Assert a cause as fact when only correlation in the error pattern is observed.

**Instructions:**

1. **Establish the aggregate reference.** Record the overall metric with its CI and the baseline. Every slice is judged against this and against the slice's own baseline.

2. **Enumerate candidate slices.** List slice dimensions to cut on (single-dimension first, then high-value intersections like new-user × mobile). Note which require metadata you have vs. don't.

3. **Compute per-slice metrics with support.** For each slice, report the metric, n, and CI. Flag any slice with too few examples to conclude anything (and recommend collecting more).

4. **Rank failure pockets by impact.** Order slices by (deviation-from-aggregate × slice volume × error cost). A small slice with catastrophic errors can outrank a large mediocre one — make the rule explicit.

5. **Drill into the worst pockets.** Pull representative misclassified/high-error examples per top slice. Look for shared structure: label noise, ambiguous inputs, missing features, distribution shift, threshold mismatch.

6. **Form cause hypotheses.** For each top pocket, state the most likely cause and the *check that would confirm it* (e.g., "if it's label noise, a manual re-label of 30 errors should reclassify ≥X%").

7. **Recommend targeted actions.** Map each confirmed/likely cause to a fix (more data for the slice, a feature, a per-slice threshold, a relabeling pass) and note expected effect and how to verify it.

**Output Format:**

A markdown report:
- **Aggregate Reference** — overall metric ± CI vs. baseline.
- **Slice Performance Table** — Slice | n | Metric ± CI | Δ vs. aggregate | Est. impact.
- **Top Failure Pockets** — for each: examples, shared structure, hypothesized cause + confirming check.
- **Small-Sample / Inconclusive Slices** — slices needing more data.
- **Ranked Action List** — fix, target slice, expected effect, verification.

## Verification

- [ ] Every slice metric is reported with its sample size and a CI (or small-n flag).
- [ ] Slices are ranked by impact (deviation × volume × cost), not just by metric value.
- [ ] At least one representative example is shown per top failure pocket.
- [ ] Each cause is labeled as a hypothesis with a stated confirming check.
- [ ] No slice is declared broken when its difference is within sampling noise.
- [ ] No slice metric is fabricated; uncomputable slices are flagged as such.

## False-Positive Prevention

❌ **DON'T:**
- Call a slice "the worst segment" when it has 12 examples and a wide CI — that's noise, not a finding.
- Read a single bad metric on a slice as proof of a model defect when the slice's labels are themselves noisy.
- Rank pockets purely by metric value, ignoring how many users/dollars each touches.
- Present a plausible story for a failure as the confirmed cause without an example-level check.

✅ **DO:**
- Require minimum support per slice and attach CIs before drawing conclusions.
- Inspect actual error examples to tell label noise apart from genuine model weakness.
- Rank by business impact so the fix list targets errors that matter.
- State the experiment that would confirm each cause hypothesis before recommending a fix.

## Example Output

```markdown
## Error Analysis: Support-Ticket Intent Classifier (golden set, n=8,400)

### Aggregate Reference
Macro-F1 = 0.81 (95% CI 0.79–0.83). Majority-class baseline macro-F1 = 0.14.

### Slice Performance Table
| Slice | n | Macro-F1 ± CI | Δ vs. aggregate | Est. impact |
|---|---|---|---|---|
| Channel = email | 5,100 | 0.84 (0.82–0.86) | +0.03 | low |
| Channel = chat | 2,900 | 0.77 (0.74–0.80) | −0.04 | medium |
| Language = non-English | 410 | 0.58 (0.51–0.65) | −0.23 | HIGH (growing segment) |
| Class = billing_dispute | 320 | 0.49 (0.42–0.56) | −0.32 | HIGH (high cost) |
| First-time user | 90 | 0.71 (0.58–0.83) | −0.10 | inconclusive (n=90) |

### Top Failure Pockets
1. **Non-English tickets.** 28 sampled errors: most are correct intent but the model defaults to
   `general_inquiry`. Shared structure: sparse non-English tokens. Hypothesis: under-representation in
   training. Confirming check: per-language training counts; expect non-English < 3% of data.
2. **billing_dispute class.** Errors confuse it with `payment_question`. Hypothesis: overlapping
   vocabulary + noisy labels. Confirming check: re-label 30 errors blind; expect ≥40% are mislabeled.

### Small-Sample / Inconclusive Slices
- First-time user (n=90): CI too wide to conclude; collect more before acting.

### Ranked Action List
| Fix | Target slice | Expected effect | Verify |
|---|---|---|---|
| Add non-English training data / multilingual encoder | non-English | +F1 on slice | re-run harness on slice |
| Relabel billing_dispute, merge if truly ambiguous | billing_dispute | cleaner class boundary | confusion-matrix recheck |
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** aggregate → slices → ranking → drill-down → causes → actions.
- **RT-05 (Evidence-Based Reasoning):** every pocket is backed by examples and support counts.
- **RT-09 (Root Cause Explanation):** cause hypotheses with confirming checks, not just symptoms.
- **DS-06 (Prioritization & Severity Guidance):** failure pockets ranked by impact.
- **QA-12 (False Positives Identification):** small-sample slices are quarantined from conclusions.

**Related Prompts:**
- `mleval_confusion_matrix_interpretation.md` — read per-class errors inside a flagged slice.
- `mleval_evaluation_harness_design.md` — make these slices a permanent part of every run.
- `mleval_robustness_stress_testing.md` — probe whether a weak slice is also fragile to shift.
