---
title: "Time-Series Anomaly Detection Design"
category: AI-ML/specialized-ml/time-series
description: "Design a time-series anomaly detector — method, seasonality handling, thresholding, and honest evaluation — that separates real anomalies from seasonal/trend variation and noise, without leaking the future into its baseline."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - QA-12
  - CM-02
difficulty: advanced
tags:
  - time-series
  - anomaly-detection
  - thresholding
  - seasonality
  - evaluation
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/time-series/ts_seasonality_decomposition.md
  - domain-AI-ML/specialized-ml/time-series/ts_data_leakage_audit.md
  - domain-AI-ML/specialized-ml/time-series/ts_backtesting_design.md
---

# Time-Series Anomaly Detection Design

**Objective:** Design a time-series anomaly detection system — choosing the detection method, handling trend and seasonality so normal periodic variation isn't flagged, setting thresholds against a leak-free baseline, and evaluating honestly under heavy class imbalance — so that the system catches genuine anomalies (point, contextual, collective) without drowning operators in false alarms.

**When to Use:**
- Monitoring a metric/series for outliers, level shifts, or unusual patterns (ops metrics, sensors, fraud signals).
- An existing detector is too noisy (alert fatigue) or misses real incidents.
- Designing alerting where seasonality (daily/weekly cycles) keeps triggering false positives.

**When NOT to Use:**
- For forecasting future values (use `ts_forecasting_model_selection.md`).
- For decomposing seasonality as an end in itself (use `ts_seasonality_decomposition.md`).
- For a forensic leakage audit (use `ts_data_leakage_audit.md`).

## Inputs / Context

Provide what you can:
- **Series & frequency** — the metric, sampling rate, and span; multiple correlated series?
- **Anomaly type sought** — point outliers, contextual (anomalous-for-the-time-of-day) anomalies, or collective/pattern anomalies, and level/trend shifts.
- **Seasonality & trend** — known cycles (hour-of-day, day-of-week, holidays) and trend.
- **Labels** — any labeled incidents (usually rare/none), and the cost asymmetry of false negatives vs false positives.
- **Latency** — real-time/streaming vs batch detection; how fast an alert must fire.
- **Constraints** — alert budget (alerts/day operators tolerate), explainability needs.

## Constraints

**Must:**
- Account for trend and seasonality so normal periodic peaks/troughs are not flagged as anomalies (contextual normality).
- Set thresholds and fit the "normal" baseline using only past data (rolling/expanding), never the full series including the future point being scored.
- Evaluate under realistic class imbalance with metrics beyond accuracy, and against a sane baseline detector.

**Must Not:**
- Use a single global mean/std threshold on a seasonal series — it will fire every peak and miss off-peak anomalies.
- Compute the detection baseline over a window that includes the point (or future points) being judged — that leaks the future.
- Fabricate precision/recall numbers; reason from the user's labels (or note their absence) and mark unknowns.

**Instructions:**

1. **Define what counts as an anomaly.** Specify the anomaly type(s) and the operational definition (what an operator would call a true incident). This determines method and evaluation.

2. **Handle trend and seasonality first.** Decide whether to detect on residuals after decomposition, use a seasonal baseline (same hour/day-of-week reference), or a model that natively encodes seasonality — so normal cyclic variation isn't flagged.

3. **Choose the detection method.** Match to the data and anomaly type: statistical (rolling z-score / ESD / robust MAD), decomposition-residual, forecasting-residual (anomaly = large forecast error), or model-based (isolation forest, density). Right-size to data volume and explainability needs.

4. **Set thresholds against a past-only baseline.** Define dynamic thresholds from rolling/expanding statistics computed strictly on prior data, with robustness to outliers (e.g., MAD over std). State how thresholds adapt over time.

5. **Manage the alert budget.** Tie threshold strictness to the operators' tolerable alert rate; add hysteresis / minimum-duration / dedup so a single excursion doesn't produce a storm of alerts.

6. **Design evaluation under imbalance.** With anomalies rare, use precision/recall/F-beta (weighted by the false-negative vs false-positive cost), time-to-detect, and range-based metrics for collective anomalies — never raw accuracy. Compare to a naive baseline (e.g., fixed-threshold).

7. **Validate without leaking the future.** Evaluate in time order (the threshold at time t uses only data before t), so reported detection performance reflects real streaming behavior.

**Output Format:**

A markdown design:
- **Anomaly Definition** — type(s) and operational meaning.
- **Seasonality/Trend Handling** — decomposition or seasonal-baseline approach.
- **Method Choice** — table: Candidate | Fit to Anomaly Type | Data Need | Explainability | Verdict.
- **Thresholding** — past-only baseline, robustness, adaptation rule.
- **Alert Budget Controls** — hysteresis/duration/dedup, tolerable rate.
- **Evaluation Plan** — imbalance-aware metrics, baseline, time-honest validation.

## Verification

- [ ] Trend/seasonality is handled so normal cyclic variation isn't flagged.
- [ ] The "normal" baseline and thresholds use only past data relative to each scored point.
- [ ] The detection method matches the targeted anomaly type(s).
- [ ] Evaluation uses imbalance-aware metrics (not accuracy) against a baseline detector.
- [ ] Validation respects time order (no future in the threshold/baseline).
- [ ] Alert-budget controls are specified; no fabricated precision/recall numbers.

## False-Positive Prevention

❌ **DON'T:**
- Apply a single fixed mean±3σ threshold to a strongly seasonal metric — it flags every daily peak and misses anomalies during troughs.
- Compute the rolling statistics over a window centered on the point being scored — it uses future values to judge the present.
- Report accuracy on a series with 0.1% anomalies — a "flag nothing" detector scores 99.9% and is useless.
- Tune thresholds to maximize recall while ignoring the alert volume operators must triage.

✅ **DO:**
- Normalize for time-of-day/day-of-week (contextual normality) so an off-peak spike is caught and an on-peak peak isn't falsely flagged.
- Build the baseline from strictly prior data (trailing/expanding), matching real streaming detection.
- Evaluate with precision/recall/F-beta and time-to-detect under realistic imbalance, against a naive threshold baseline.
- Set strictness to the operators' alert budget and add hysteresis/duration gating to suppress alert storms.

## Example Output

```markdown
## Anomaly Detection: API Request-Rate Monitoring

### Anomaly Definition
Contextual + collective: a request rate that is abnormal *for that hour-of-day/day-of-week*, and sustained level shifts (sudden drop = outage, sudden spike = abuse). Point spikes < 2 min are not actionable.

### Seasonality/Trend Handling
Strong hour-of-day + weekday/weekend cycle. Detect on residuals after STL decomposition; seasonal baseline = robust median for same (weekday, hour) over trailing 8 weeks.

### Method Choice
| Candidate | Fit to Type | Data Need | Explainability | Verdict |
|---|---|---|---|---|
| Fixed mean±3σ | Poor (ignores season) | Low | High | Baseline only |
| STL residual + robust z (MAD) | Good contextual | Moderate | High | Recommended |
| Forecast-residual (seasonal model) | Good | Moderate | Medium | Alt for spikes |
| Isolation forest | Collective patterns | High | Low | Stage 2 if needed |

### Thresholding
Robust z on STL residual using trailing-only MAD; threshold |z| > k, with k tuned to the alert budget. Baseline recomputed daily from prior data only.

### Alert Budget Controls
Require 5-min sustained breach (duration gating), hysteresis to clear, dedup per service. Target <= ~10 alerts/day.

### Evaluation Plan
On 6 months of labeled incidents (rare): precision, recall, F2 (false negatives costlier), median time-to-detect. Compare to fixed-σ baseline. Evaluate in time order — threshold at t uses only data before t.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** definition → seasonality → method → thresholds → alert budget → evaluation.
- **RT-02 (Multi-Dimensional Analysis Framework):** trades off detection power, alert volume, explainability, and latency.
- **DS-02 (Metric Specification):** imbalance-aware metrics (precision/recall/F-beta, time-to-detect) with a baseline.
- **QA-12 (False Positives Identification):** seasonal false alarms and accuracy-on-imbalance are the core traps.
- **CM-02 (Constraint Specification):** the operators' alert budget constrains thresholding.

**Related Prompts:**
- `ts_seasonality_decomposition.md` — the decomposition this detector runs on residuals of.
- `ts_data_leakage_audit.md` — ensure the baseline/thresholds don't peek at the future.
- `ts_backtesting_design.md` — time-honest validation principles applied to detection.
