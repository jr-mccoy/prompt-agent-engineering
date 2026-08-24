---
title: "ML Drift Detection Design"
category: AI-ML/production-monitoring
description: "Design data, concept, and prediction drift detection with explicit reference windows, statistical tests, and alert thresholds — so drift claims are evidenced, not eyeballed."
techniques:
  - ST-02
  - RT-05
  - DS-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - drift-detection
  - data-drift
  - concept-drift
  - monitoring
  - thresholds
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_monitoring_dashboard_design.md
  - domain-AI-ML/production-monitoring/mlmonitor_performance_degradation_triage.md
  - domain-AI-ML/production-monitoring/mlmonitor_retraining_trigger_strategy.md
---

# ML Drift Detection Design

**Objective:** Design a drift detection scheme for a production model that distinguishes data (covariate) drift, prediction (output) drift, and concept drift; specifies a reference/baseline window for each; selects appropriate tests per feature type; and sets magnitude and significance thresholds so that every "drift" alert is backed by a baseline comparison rather than a single suspicious snapshot.

**When to Use:**
- Standing up monitoring for a newly deployed model.
- Replacing ad-hoc "the inputs look weird this week" checks with a principled, thresholded scheme.
- After an incident where drift was suspected but could not be confirmed for lack of a baseline.

**When NOT to Use:**
- To diagnose an already-confirmed performance drop (use `mlmonitor_performance_degradation_triage.md`).
- To decide retraining policy once drift is detectable (use `mlmonitor_retraining_trigger_strategy.md`).
- For pure label/data-quality auditing of the input pipeline (use `mlmonitor_data_pipeline_health_audit.md`).

## Inputs / Context

Provide what you can; the design degrades gracefully if some are missing:
- **Model & task** — what is predicted, prediction frequency, and how/when ground-truth labels arrive (immediately, delayed by days/weeks, or never).
- **Feature inventory** — names, types (numeric, categorical, high-cardinality, embedding), and approximate volumes per scoring window.
- **Traffic profile** — request volume, seasonality (hour/day/week), and known legitimate variation.
- **Reference data** — the training distribution and/or a "known-good" production window you trust.
- **Operational constraints** — acceptable alert latency, compute budget for monitoring, and who responds to alerts.

## Constraints

**Must:**
- Define a named **reference window** for each drift type before any drift can be declared.
- Pair every test with a **magnitude threshold** (effect size) AND a **significance/consistency rule** (e.g., breach on N consecutive windows) — never significance alone.
- Separate the three drift types and state what each does and does not imply about model quality.

**Must Not:**
- Fabricate numeric thresholds as universal truths; thresholds must be justified by the data scale or stated as a starting value to be calibrated.
- Treat statistical significance on large samples as evidence of meaningful drift — large N makes trivial differences "significant."
- Claim concept drift from input statistics alone; concept drift requires the input→label relationship to change, which needs labels.

**Instructions:**

1. **Separate the three drift questions.** Distinguish: (a) *data drift* — have feature distributions P(X) shifted? (b) *prediction drift* — has the output distribution P(ŷ) shifted? (c) *concept drift* — has P(y|X) shifted, i.e., the same inputs now map to different outcomes? State which are detectable given the label-arrival reality from Inputs.

2. **Fix the reference window per drift type.** Choose a baseline — training distribution, a rolling trailing window, or a fixed golden window — and justify it against the traffic's seasonality so normal weekly cycles are not mistaken for drift.

3. **Select tests by feature type.** Map each feature to an appropriate detector: e.g., PSI/KL/Wasserstein or KS for numeric; chi-square/PSI for categorical; novel-category rate for high-cardinality; distance-on-summary-statistics for embeddings. Note multiple-comparison risk across many features.

4. **Set magnitude thresholds and a consistency rule.** For each test, give a starting effect-size threshold (e.g., PSI bands) plus a rule that requires the breach to persist (N-of-M windows) before alerting, to suppress single-window noise.

5. **Design prediction-drift monitoring.** Track the output distribution and confidence/score histogram against the reference; this is the earliest signal available when labels are delayed.

6. **Design concept-drift detection conditioned on labels.** When labels arrive (even delayed), monitor rolling performance and/or error-rate change tests; specify how delayed labels are joined back to predictions without backfilling future information.

7. **Account for volume and seasonality.** Specify minimum sample sizes per window, how low-traffic windows are handled, and how seasonal baselines (day-of-week, holiday) are normalized.

8. **Specify alert routing and severity.** Define what fires a warning vs a page, deduplication, and the first triage step an on-call should take so an alert leads to action, not noise.

**Output Format:**

A markdown design document:
- **Drift Coverage Map** — table: Drift Type | Detectable Now? (label dependency) | Reference Window | Primary Signal
- **Per-Feature Detector Plan** — table: Feature/Group | Type | Test | Magnitude Threshold | Consistency Rule
- **Prediction & Concept Drift Plan** — signals, label-join logic, thresholds
- **Seasonality & Sample-Size Handling** — rules
- **Alerting & Severity** — warning vs page, routing, first triage step
- **Calibration Plan** — how thresholds will be tuned on historical data before going live

## Verification

- [ ] Each drift type has an explicitly named reference window.
- [ ] Every detector pairs a magnitude threshold with a consistency/significance rule.
- [ ] Tests are matched to feature types (numeric vs categorical vs high-cardinality vs embedding).
- [ ] Concept-drift detection is gated on label availability and timing.
- [ ] Seasonality and minimum sample size are addressed.
- [ ] Multiple-comparison risk across many features is acknowledged and handled.

## False-Positive Prevention

❌ **DON'T:**
- Declare drift from a single window with no baseline comparison.
- Alert on p-values alone — with millions of requests, negligible shifts become "significant."
- Treat a normal Monday-vs-Sunday traffic change as drift because the baseline ignored seasonality.
- Call input drift "concept drift" — input shift may leave P(y|X) and accuracy untouched.
- Fire an alert per feature and drown the on-call when 200 features all wiggle slightly.

✅ **DO:**
- Require a named reference window plus a persisted breach (N-of-M windows) before alerting.
- Combine effect size (PSI/Wasserstein magnitude) with significance, and prefer magnitude on large N.
- Build seasonal/day-of-week baselines or normalize before comparing.
- Reserve "concept drift" for confirmed P(y|X) change with labels; otherwise say "data drift, impact on quality unknown."
- Aggregate feature-level signals into a model-level drift score with controlled false-discovery rate.

## Example Output

```markdown
## Drift Detection Design: Fraud Scoring Model v4

### Drift Coverage Map
| Drift Type | Detectable Now? | Reference Window | Primary Signal |
|---|---|---|---|
| Data (P(X)) | Yes, immediate | Trailing 28d, day-of-week normalized | PSI per feature |
| Prediction (P(ŷ)) | Yes, immediate | Same trailing 28d | Score histogram + mean drift |
| Concept (P(y|X)) | Delayed ~14d (chargeback labels) | Last 8 fully-labeled weeks | Rolling precision/recall + error-rate test |

### Per-Feature Detector Plan
| Feature/Group | Type | Test | Magnitude Threshold | Consistency Rule |
|---|---|---|---|---|
| txn_amount | Numeric | Wasserstein + PSI | PSI > 0.2 | 3 of 4 daily windows |
| merchant_category | Categorical | PSI (chi-square backstop) | PSI > 0.2 | 3 of 4 daily windows |
| device_id_new_rate | High-card | Novel-category rate | +50% vs baseline rate | 2 consecutive days |
| user_embedding | Embedding | Centroid + covariance distance | >2σ of historical | 3 of 4 windows |

### Prediction & Concept Drift Plan
- Prediction drift: alert if mean fraud score shifts > 0.05 absolute AND score-histogram PSI > 0.2 for 3 of 4 days. Earliest available signal.
- Concept drift: once chargeback labels land (~14d), run a rolling 8-week precision/recall and a proportion-test on FN rate; only labeled predictions counted; no future labels backfilled into earlier windows.

### Seasonality & Sample-Size Handling
- Minimum 5,000 scored requests per window; below that, pool to weekly.
- Baselines computed per day-of-week to absorb weekend volume dips.

### Alerting & Severity
- Warning (Slack): single feature PSI breach. Page: model-level drift score > threshold OR prediction-drift breach. First triage step: open the degradation-triage runbook.

### Calibration Plan
- Replay 6 months of history; tune PSI bands and N-of-M so historical false-alert rate < 1/month while catching the two known past shifts.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** drift design proceeds through a fixed separate-then-detect sequence.
- **RT-05 (Evidence-Based Reasoning):** every alert is anchored to a baseline comparison and threshold.
- **DS-02 (Metric Specification):** specifies tests, effect sizes, and thresholds per signal.
- **CM-02 (Constraint Specification):** the reference window is the governing constraint for all drift claims.
- **QA-12 (False Positives Identification):** core to separating real drift from seasonality and large-N significance noise.

**Related Prompts:**
- `mlmonitor_monitoring_dashboard_design.md` — surface these drift signals at the right cadence.
- `mlmonitor_performance_degradation_triage.md` — when a drift alert fires, diagnose the cause.
- `mlmonitor_retraining_trigger_strategy.md` — turn detected drift into a retraining decision.
