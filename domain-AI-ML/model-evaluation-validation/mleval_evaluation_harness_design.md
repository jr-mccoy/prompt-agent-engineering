---
title: "ML Evaluation Harness Design"
category: AI-ML/model-evaluation-validation
description: "Design a reusable, leak-safe evaluation harness — fixed datasets, slices, baselines, metrics, and reporting — so every model is judged the same honest way."
techniques:
  - ST-02
  - ST-03
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - evaluation-harness
  - reproducibility
  - golden-set
  - slices
  - baselines
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-evaluation-validation/mleval_error_analysis_slicing.md
  - domain-AI-ML/model-evaluation-validation/mleval_baseline_comparison_protocol.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
---

# ML Evaluation Harness Design

**Objective:** Specify a reusable evaluation harness — frozen datasets, slice definitions, baselines, metrics, and a fixed report — that any candidate model is run through identically, so comparisons are fair, reproducible, and resistant to leakage and silent metric drift.

**When to Use:**
- You evaluate models more than once (iteration, retraining, vendor comparison) and want apples-to-apples results.
- Different people report different numbers for the "same" model.
- Before standing up a model-promotion gate or leaderboard.
- Migrating from ad-hoc notebook evaluation to a repeatable process.

**When NOT to Use:**
- For a single throwaway experiment with no promotion decision.
- For online experiment design (use `mleval_ab_test_design_for_models.md`).

## Inputs / Context

Provide what you can:
- **Task & primary/guardrail metrics** — ideally already chosen (see `mleval_metric_selection_guide.md`).
- **Available data** — sources, time ranges, label provenance, known quality issues.
- **Population structure** — important subgroups/slices (segment, geography, device, class, time period).
- **Baselines** — trivial and prior-model baselines that must be re-run each time.
- **Consumers of the report** — engineers, leadership, regulators; cadence (per-PR, nightly, pre-launch).
- **Reproducibility constraints** — seeds, environment pinning, data versioning available.

## Constraints

**Must:**
- Define a **frozen golden test set** that is never used for training or tuning, with a documented refresh policy.
- Make every run **reproducible**: pinned data version, seeds, and environment recorded with results.
- Build slices and baselines into the harness so they are computed automatically, not optionally.

**Must Not:**
- Allow the golden set to leak into training/HPO — specify the guard that prevents it.
- Fabricate dataset sizes or metric values; describe the harness, not invented results.
- Let the harness report only aggregates — per-slice and baseline rows are mandatory output.

**Instructions:**

1. **Freeze the evaluation data.** Define train / validation / golden-test partitions, the split logic (grouped/temporal as needed to avoid leakage), versioning, and a refresh/expiry policy for the golden set.

2. **Run a leakage pre-check.** Before the harness is trusted, route the data through a leakage audit (target/temporal/contamination). Record the result as a harness precondition.

3. **Encode the metrics.** Implement the primary and guardrail metrics with explicit operating points; record metric definitions/versions so a metric change is visible in diffs.

4. **Define the slices.** Enumerate the subgroups and edge segments that must be reported every run (e.g., per-class, per-segment, recent-time window, rare-but-costly cases).

5. **Wire in the baselines.** The harness must compute trivial (random/majority) and prior-model baselines on the same golden set, every run, so improvements are always relative.

6. **Add interval reporting.** Attach confidence intervals (e.g., bootstrap) to each headline number so single-point comparisons are never made naked.

7. **Lock the report schema.** Define the exact report layout (overall, per-slice, vs-baseline, with CIs) and the provenance footer (data version, seed, commit, date).

8. **Define refresh and review triggers.** State when the golden set is refreshed, who reviews it, and how a metric/slice definition change is approved.

**Output Format:**

A harness specification:
- **Data Partitions** — table: Partition | Rows/range | Split logic | Versioning.
- **Leakage Precondition** — what is checked before any result is trusted.
- **Metric Registry** — primary + guardrails, definitions, operating points.
- **Slice Registry** — slices computed every run and why.
- **Baseline Registry** — baselines re-run every time.
- **Report Schema** — the locked layout including CIs and provenance footer.
- **Governance** — refresh policy, change approval, run cadence.

## Verification

- [ ] A golden test set is defined and explicitly walled off from training/HPO.
- [ ] Reproducibility fields (data version, seed, environment, commit) are part of every report.
- [ ] A leakage pre-check is a stated precondition, not an afterthought.
- [ ] Slices and baselines are computed automatically each run, not optionally.
- [ ] Every headline metric carries a confidence interval.
- [ ] The report schema is fixed so metric/slice changes show up as diffs.

## False-Positive Prevention

❌ **DON'T:**
- Reuse the golden set for tuning "just this once" — it stops being golden the moment it informs a choice.
- Report a single aggregate number and call the harness done; aggregates hide slice failures.
- Compare two runs that used different data versions or metric definitions as if they were comparable.
- Ship a harness that produces point estimates with no intervals — small datasets make noise look like signal.

✅ **DO:**
- Keep a true golden set used only at promotion time; do tuning on a separate validation split or nested CV.
- Make per-slice and vs-baseline rows mandatory output so regressions surface automatically.
- Pin and record data version, seed, and commit so any two runs are provably comparable.
- Run a leakage audit before trusting harness numbers — a clean harness over leaky data is still wrong.

## Example Output

```markdown
## Evaluation Harness Spec: Churn Model

### Data Partitions
| Partition | Rows / range | Split logic | Versioning |
|---|---|---|---|
| Train | 2023-01 to 2024-06 | GroupKFold on account_id | dvc tag data@v7 |
| Validation | 2024-07 to 2024-09 | temporal, post-train | data@v7 |
| Golden test | 2024-10 to 2024-12 | temporal holdout, frozen | data@v7-golden (locked) |

### Leakage Precondition
Run `mldata_data_leakage_detector` on the feature set each time data@vN is cut.
Harness refuses to publish results if the audit has open High-confidence findings.

### Metric Registry
- Primary: AUPRC @ full ranking (positives ~9%). metric_def v2.
- Guardrails: recall on high-LTV accounts; ECE (calibration); inference p95 latency.

### Slice Registry
Per-tenure-bucket, per-plan-tier, per-region, most-recent-30-days, high-LTV subset.
(Aggregate AUPRC hid a collapse on new accounts in v6 — slices now mandatory.)

### Baseline Registry
- Majority predictor (always "no churn") — recomputed each run.
- Heuristic: "any account with 0 logins in 30d." 
- Prior production model (champion).

### Report Schema
Overall + per-slice rows, each with metric +/- 95% bootstrap CI (1,000 resamples),
a "vs champion" delta column, and a footer: data version, seed, git SHA, run date.

### Governance
Golden set refreshed quarterly with a 2-reviewer sign-off. Metric/slice changes require PR review.
Harness runs nightly on champion + on every challenger PR.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** harness is specified as an ordered build.
- **ST-03 (Output Format Specification):** the locked report schema is central.
- **DS-02 (Metric Specification):** metric registry with operating points and baselines.
- **CM-02 (Constraint Specification):** golden-set walls and reproducibility are hard constraints.
- **QA-01 (Self-Verification):** the leakage precondition and CIs build self-checking into the harness.

**Related Prompts:**
- `mleval_error_analysis_slicing.md` — go deeper where the slice registry flags failures.
- `mleval_baseline_comparison_protocol.md` — define what the baselines should be.
- `mldata_data_leakage_detector.md` — the precondition audit the harness depends on.
