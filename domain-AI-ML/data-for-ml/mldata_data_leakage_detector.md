---
title: "ML Data Leakage Detector"
category: AI-ML/data-for-ml
description: "Systematically hunt for train/test contamination, target leakage, and temporal leakage that inflate offline metrics and collapse in production."
techniques:
  - ST-02
  - RT-05
  - QA-12
  - DS-02
  - CM-02
difficulty: advanced
tags:
  - data-leakage
  - target-leakage
  - train-test-contamination
  - validation
  - reproducibility
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_eval_result_skepticism_audit.md
  - domain-AI-ML/data-for-ml/mldata_train_test_split_strategy.md
  - domain-AI-ML/feature-engineering/mlfeature_leakage_safe_pipeline.md
---

# ML Data Leakage Detector

**Objective:** Audit a dataset, feature set, and validation setup for the three families of data leakage — train/test contamination, target (label) leakage, and temporal leakage — and produce a ranked, evidence-backed list of suspected leaks with concrete remediation, before the model is trusted or shipped.

**When to Use:**
- Offline metrics look "too good to be true" (e.g., AUC > 0.98 on a hard business problem).
- A model that scored well offline degrades sharply in production.
- Before promoting any model past a baseline gate.
- When inheriting a pipeline or notebook you did not write.

**When NOT to Use:**
- For routine metric selection (use `mleval_metric_selection_guide.md`).
- For pure feature-importance interpretation without a leakage concern (use `mlfeature_importance_analysis.md`).

## Inputs / Context

Provide what you can; the audit degrades gracefully if some are missing:
- **Task & target definition** — what is predicted, and the exact moment the label becomes known in the real world.
- **Feature list** — names, source tables, and (critically) *when each feature is computed/observed* relative to the prediction time.
- **Split strategy** — random / stratified / grouped / temporal; ratios; whether splitting happens before or after preprocessing.
- **Preprocessing & feature pipeline** — scalers, encoders, imputation, resampling (SMOTE etc.), feature selection — and whether each is fit on train-only or on all data.
- **Headline metrics** and any suspiciously strong features.

## Constraints

**Must:**
- Anchor every suspected leak to a specific feature, step, or split decision in the user's input — no generic warnings.
- Classify each finding by leakage family and assign a confidence level (High / Medium / Low) with the evidence that sets it.
- Tie each leak to the production consequence (why offline ≠ online).

**Must Not:**
- Declare leakage on suspicion alone — distinguish *confirmed* (mechanism identified) from *suspected* (pattern consistent with leakage, needs a check).
- Invent feature semantics the user did not provide; if a feature's timing is unknown, list it as an open question, not a confirmed leak.
- Recommend simply dropping a strong feature without first establishing whether it is legitimately available at prediction time.

**Instructions:**

1. **Reconstruct the prediction-time boundary.** Pin down the exact instant of inference in production and what information is legitimately available at or before it. Every later-arriving signal is a leakage candidate.

2. **Hunt target leakage.** For each feature, ask: could its value only be known *after* (or *because of*) the label? Flag proxies (e.g., `account_closed_date` for churn), post-outcome aggregates, and features derived from the target.

3. **Hunt train/test contamination.** Check whether preprocessing (scaling, encoding, imputation, feature selection, resampling) was fit on the full dataset before splitting; whether duplicates or near-duplicates straddle the split; whether grouped entities (same user/device/patient) appear in both folds.

4. **Hunt temporal leakage.** For any time-ordered process, verify the split respects time, that rolling/aggregate features use only past windows, and that no future-derived label horizons bleed backward.

5. **Run the "too good to be true" cross-check.** Compare headline metrics to a sane baseline and to plausibility for the domain. Identify single features whose removal would collapse performance — interrogate them first.

6. **Rank and remediate.** Order findings by (consequence × confidence). For each, give the specific fix (leak-safe pipeline placement, regroup split, recompute feature with a time cutoff, drop-and-revalidate).

**Output Format:**

A markdown report:
- **Leakage Risk Summary** — table: Finding | Family | Confidence | Production Impact
- **Confirmed Leaks** — mechanism + evidence + remediation, ranked
- **Suspected Leaks / Open Questions** — what to check and how
- **Clean Aspects Verified** — what you checked and found sound (so it isn't re-litigated)
- **Recommended Re-Validation Protocol** — the corrected setup to re-run before trusting metrics
- **INSUFFICIENT EVIDENCE** — an available verdict per leakage family. Temporal leakage in particular cannot be ruled out without per-column availability timestamps relative to the prediction-time boundary; where those are absent, say so and name them as the unblocking datum rather than reporting the family clean.

## Verification

- [ ] Every finding cites a specific feature/step/split from the input, not a generic category.
- [ ] Each finding is labeled Confirmed vs Suspected, with a confidence level.
- [ ] The prediction-time boundary is stated explicitly and used as the reference for timing claims.
- [ ] All three leakage families were checked (target, contamination, temporal) — including a note where a family is N/A and why.
- [ ] Each remediation is actionable and names where in the pipeline it applies.
- [ ] Any family that could not be evaluated is reported as INSUFFICIENT EVIDENCE with the timestamps or lineage needed to resolve it — never as "clean."

## False-Positive Prevention

❌ **DON'T:**
- Flag a strong feature as leakage just because it is predictive — strong-and-legitimate is common.
- Assume preprocessing leaked without confirming whether it was fit on train-only.
- Treat a random split as temporal leakage when the process is genuinely i.i.d.
- Call duplicates "contamination" without checking whether they are legitimate repeated events.

✅ **DO:**
- Establish *when* a feature is observable before judging it; ask the user when timing is unknown.
- Trace the fit/transform boundary of each preprocessing step explicitly.
- Separate "this is leakage" (mechanism shown) from "this smells like leakage" (needs a probe), and label accordingly.
- Confirm the suspected leak by predicting its signature (e.g., "removing X should drop AUC from 0.98 to ~baseline") and recommending that test.

## Example Output

```markdown
## Data Leakage Audit: Loan Default Prediction v3

### Leakage Risk Summary
| Finding | Family | Confidence | Production Impact |
|---|---|---|---|
| `days_since_last_payment` computed post-default | Target | High | Inflates AUC; unavailable at scoring time |
| StandardScaler fit on full dataset pre-split | Contamination | High | Optimistic CV; mild metric inflation |
| Same `customer_id` in train and test | Contamination | High | Memorization; overstates generalization |
| Random split on monthly application data | Temporal | Medium | Future leaks into past; needs time split |
| `branch_avg_default_rate` (target-encoded) | Target/Contamination | Medium | Encoding likely fit on all rows incl. test |

### Confirmed Leaks (ranked)
1. **`days_since_last_payment` is post-outcome.** This counter only updates after a missed payment that constitutes default — it cannot exist at application scoring time. Evidence: feature is defined off the payment ledger which is updated by the default event itself. Remediation: drop; if a pre-application proxy is needed, recompute strictly from data available before `application_ts`.
2. **Global scaling before split.** `StandardScaler().fit(X)` runs before `train_test_split`. Test statistics bleed into train normalization. Remediation: move scaling inside a Pipeline fit on train folds only.
3. **Customer overlap across folds.** 8,412 `customer_id`s appear in both train and test. Remediation: switch to GroupKFold on `customer_id`.

### Suspected Leaks / Open Questions
- **`branch_avg_default_rate`**: confirm whether target encoding was fit train-only and with out-of-fold means. Check: re-fit with OOF encoding; expect a measurable AUC drop if leaking.

### Clean Aspects Verified
- Label definition (90+ DPD) is fixed at a clear time horizon; no horizon bleed detected.
- No exact-duplicate rows beyond the customer-overlap issue.

### Recommended Re-Validation Protocol
1. Rebuild as a leak-safe sklearn Pipeline (impute → encode[OOF] → scale → model), fit inside CV only.
2. GroupKFold(customer_id), and a temporal holdout on the most recent 3 months.
3. Drop `days_since_last_payment`; re-measure. Expect AUC to fall from 0.982 toward the ~0.78 baseline — that drop is the *real* signal.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** the audit proceeds through a fixed boundary-then-three-families sequence.
- **RT-05 (Evidence-Based Reasoning):** every leak is anchored to a named feature/step.
- **QA-12 (False Positives Identification):** core to separating confirmed from suspected leaks.
- **DS-02 (Metric Specification):** uses baseline/plausibility comparisons to surface leakage.
- **CM-02 (Constraint Specification):** the prediction-time boundary is the governing constraint.

**Related Prompts:**
- `mleval_eval_result_skepticism_audit.md` — when metrics look too good and you want the eval, not the data, interrogated.
- `mldata_train_test_split_strategy.md` — design a leak-safe split up front.
- `mlfeature_leakage_safe_pipeline.md` — build preprocessing that cannot leak.
