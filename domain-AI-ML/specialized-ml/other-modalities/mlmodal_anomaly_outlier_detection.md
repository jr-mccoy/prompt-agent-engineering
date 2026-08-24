---
title: "Anomaly & Outlier Detection Design"
category: AI-ML/specialized-ml/other-modalities
description: "Design anomaly/outlier detection under extreme class imbalance — choose unsupervised vs semi-supervised framing, set defensible thresholds, and evaluate with metrics that don't lie when positives are rare."
techniques:
  - ST-02
  - DS-02
  - QA-12
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - anomaly-detection
  - outlier-detection
  - class-imbalance
  - thresholding
  - evaluation
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/graph-ml/graphml_task_framing.md
  - domain-AI-ML/specialized-ml/other-modalities/mlmodal_multimodal_architecture.md
  - domain-AI-ML/specialized-ml/other-modalities/mlmodal_speech_asr_tts_framing.md
---

# Anomaly & Outlier Detection Design

**Objective:** Design an anomaly/outlier detection system under the conditions that define the problem — extreme class imbalance and few or no labeled anomalies — by choosing the right framing (unsupervised, semi-supervised, or supervised-if-labels-exist), setting a threshold tied to operating cost, and selecting evaluation metrics that remain honest when positives are vanishingly rare.

**When to Use:**
- You must detect rare abnormal events (fraud, faults, intrusions, defects) where anomalies are few and possibly unlabeled.
- An anomaly detector reports high "accuracy" but misses the anomalies you care about.
- You need a defensible threshold and evaluation plan, not just an anomaly score.

**When NOT to Use:**
- You have abundant balanced labels and a standard classifier suffices (treat it as ordinary classification).
- The "anomalies" are actually a well-defined class with plenty of examples (supervised, not anomaly detection).

## Inputs / Context

Provide what you can:
- **What counts as an anomaly** — the operational definition and examples of true positives and acceptable normals.
- **Label availability** — none (unsupervised), only normal data labeled (semi-supervised), or a few labeled anomalies.
- **Base rate** — how rare anomalies are (e.g., 1 in 10,000).
- **Data type** — tabular, time-series, images, graph, multivariate sensor.
- **Cost structure** — relative cost of a false negative (missed anomaly) vs false positive (false alarm); alert/triage capacity.
- **Drift** — whether "normal" changes over time (non-stationary).

## Constraints

**Must:**
- Pick the framing (unsupervised / semi-supervised / supervised) based on actual label availability, and state it explicitly.
- Choose evaluation metrics that survive extreme imbalance — precision@k, recall at a fixed alert budget, PR-AUC / average precision — never raw accuracy.
- Tie the decision threshold to the cost structure or alert capacity, not to a default 0.5 or an arbitrary percentile.

**Must Not:**
- Report accuracy or ROC-AUC alone as success on a 0.01%-positive problem — both can look great while the system is useless.
- Fabricate a base rate, cost ratio, or anomaly examples the user didn't give; mark them as needed inputs.
- Evaluate on a window/period that contains no real anomalies and claim the detector "works."

**Instructions:**

1. **Operationalize "anomaly."** Write the precise definition, with positive examples and the kinds of normal variation that must NOT trigger alerts. Vague definitions produce uncheckable detectors.

2. **Select the framing from label reality.** No labels → unsupervised (density/distance/isolation/reconstruction-error). Only-normal labeled → semi-supervised (model normality, flag deviations). A few anomaly labels → use them for thresholding/validation and possibly PU/weakly-supervised learning. State which and why.

3. **Pick a method family matched to data + framing.** Distance/density (tabular, low-dim), isolation-based (high-dim tabular), reconstruction error (sequences/images/autoencoders), forecasting-residual (time-series), graph-based (relational). Justify against data type.

4. **Establish a base-rate-aware baseline.** Define a trivial baseline (random at the base rate, simple rule/threshold on a known signal). The detector must beat it; "99.99% accuracy" by predicting all-normal must be explicitly disqualified.

5. **Design the threshold around cost/capacity.** Convert anomaly scores to decisions using the false-negative vs false-positive cost ratio or a fixed alert budget (top-k per day). Report the operating point, not just a score distribution.

6. **Choose imbalance-honest evaluation.** Use precision@k, recall at the chosen alert budget, PR-AUC / average precision, and a confusion matrix at the operating threshold. Validate on data that actually contains anomalies; estimate confidence given the small positive count.

7. **Handle drift and re-thresholding.** If normal drifts, specify a reference window, periodic re-fitting/re-thresholding, and a guard against the detector "learning" anomalies as normal over time.

8. **Deliver the design + honest eval plan.** Output framing, method, threshold logic, the imbalance-aware metrics, and the watchpoints (alert fatigue, drift, evaluation with too few positives).

**Output Format:**

A markdown report:
- **Anomaly Definition** — operational, with positive examples and acceptable normals.
- **Framing** — unsupervised / semi-supervised / supervised + label-reality justification.
- **Method Family** — choice + data-type rationale.
- **Baseline** — base-rate trivial baseline to beat; all-normal disqualification.
- **Thresholding** — cost/capacity-based operating point.
- **Evaluation Plan** — imbalance-honest metrics + confidence given positive count.
- **Drift Handling** — reference window + re-thresholding.
- **Watchlist** — alert fatigue, drift, too-few-positives evaluation.

## Verification

- [ ] The framing matches actual label availability and is stated.
- [ ] Metrics are imbalance-honest (precision@k, recall@budget, PR-AUC) — accuracy/ROC-AUC are not reported alone.
- [ ] The threshold is tied to cost or alert capacity, not a default.
- [ ] A base-rate baseline is defined and all-normal "high accuracy" is explicitly disqualified.
- [ ] Evaluation uses a period containing real anomalies, with confidence acknowledging the small positive count.
- [ ] Base rate / cost ratio that were not provided are flagged as needed inputs.

## False-Positive Prevention

❌ **DON'T:**
- Celebrate 99.9% accuracy when predicting "all normal" gives 99.99% on a rare-anomaly problem.
- Use ROC-AUC alone — it can look excellent while precision at any usable alert rate is near zero.
- Set the threshold at 0.5 or an arbitrary percentile divorced from the cost of false alarms vs misses.
- Validate on a clean window with zero anomalies and conclude the detector works.

✅ **DO:**
- Report precision@k and recall at a fixed alert budget, plus PR-AUC / average precision.
- Disqualify the trivial all-normal predictor explicitly and beat a base-rate baseline.
- Derive the operating threshold from the false-negative/false-positive cost ratio or triage capacity.
- Evaluate on periods that contain real anomalies and state confidence given how few positives exist.

## Example Output

```markdown
## Anomaly Detection: Manufacturing Defect Detection (sensor time-series)

### Anomaly Definition
A defect = sensor pattern preceding a unit failing QC. Positive examples: pressure spike + temp drop sequences. Acceptable normals: shift-change ramps, routine recalibration dips (must NOT alert).

### Framing
Semi-supervised: ~2 years of mostly-normal runs labeled, only ~40 confirmed defect events. Model normality; use the 40 labels for thresholding/validation.

### Method Family
Forecasting-residual on multivariate sensor streams (predict next window, flag large residuals) — fits temporal, mostly-normal data.

### Baseline
Base rate ~0.05% of windows. All-normal predictor = 99.95% accuracy and useless → disqualified. Beat a simple fixed-threshold-on-pressure rule (recall 0.45 @ 30 alerts/day).

### Thresholding
Triage capacity = 30 alerts/day. Set threshold to top-30 residual scores/day. Cost: a missed defect ≈ 50× a false alarm → favor recall within the 30-alert budget.

### Evaluation Plan
- Precision@30/day, recall@30/day, PR-AUC.
- Evaluate over the 8 months containing 18 of the 40 defects.
- Confidence: only 18 positives → wide CIs; report bootstrap intervals and avoid over-claiming.

### Drift Handling
Reference window = trailing 30 days; re-fit weekly. Guard: freeze updates around known defect periods so the model doesn't absorb anomalies as normal.

### Watchlist
- Alert fatigue if precision@30 < ~0.2.
- Drift after line retooling → re-threshold.
- Too few positives → resist strong claims from single-period results.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** definition → framing → method → baseline → threshold → eval.
- **DS-02 (Metric Specification):** precision@k, recall@budget, PR-AUC over accuracy/ROC-AUC.
- **QA-12 (False Positives Identification):** core to disqualifying accuracy and all-normal illusions.
- **CM-02 (Constraint Specification):** alert capacity and cost ratio as the threshold-governing constraints.
- **DS-06 (Prioritization & Severity Guidance):** false-negative/false-positive cost drives the operating point.

**Related Prompts:**
- `../graph-ml/graphml_task_framing.md` — for anomaly detection on relational/graph data.
- `mlmodal_multimodal_architecture.md` — when anomaly signals span multiple modalities.
- `mlmodal_speech_asr_tts_framing.md` — for detecting out-of-condition audio inputs.
