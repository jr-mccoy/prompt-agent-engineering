---
title: "ML Monitoring Dashboard Design"
category: AI-ML/production-monitoring
description: "Design an ML monitoring dashboard: which signals to surface, at what cadence, against which baselines, and with what alert tiers — so operators can tell healthy from degrading at a glance."
techniques:
  - ST-02
  - ST-03
  - DS-02
  - RT-02
  - CM-02
difficulty: intermediate
tags:
  - monitoring
  - dashboard
  - observability
  - alerting
  - slis
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_drift_detection_design.md
  - domain-AI-ML/production-monitoring/mlmonitor_slo_design_for_ml.md
  - domain-AI-ML/production-monitoring/mlmonitor_performance_degradation_triage.md
---

# ML Monitoring Dashboard Design

**Objective:** Design a layered monitoring dashboard for a production ML service that surfaces operational health, data/input health, prediction behavior, and model quality — each signal paired with a baseline and a cadence — so that an operator can answer "is the model healthy right now?" in seconds and drill into "why not?" without guesswork.

**When to Use:**
- Launching a model and needing a single pane of glass for it.
- Consolidating scattered metrics (latency here, drift there, accuracy in a notebook) into one coherent view.
- After an incident revealed that the relevant signal existed but was not visible in time.

**When NOT to Use:**
- To define the underlying drift tests (use `mlmonitor_drift_detection_design.md` first).
- To set the formal SLO targets and error budgets (use `mlmonitor_slo_design_for_ml.md`).
- To build an incident runbook (use `mlmonitor_ml_incident_response.md`).

## Inputs / Context

Provide what you can:
- **Model & business purpose** — what the model does and which business metric it moves.
- **Label latency** — immediate, delayed, or no ground truth (this decides which quality panels are real-time vs lagging).
- **Existing signals** — what is already instrumented (latency, error rates, feature stats, scores).
- **Audience** — who reads the dashboard: on-call SRE, ML engineer, product/leadership.
- **Cadence needs** — real-time, hourly, daily; and the acceptable detection latency for degradation.
- **Baselines available** — training distribution, last-good window, rolling averages.

## Constraints

**Must:**
- Group signals into clear layers (operational, input/data, prediction, quality) and order them by what an operator checks first.
- Pair each panel with an explicit baseline/reference and a cadence; a number with no reference is not a panel, it is noise.
- Distinguish real-time signals from lagging (label-dependent) signals and mark which is which on the dashboard.

**Must Not:**
- Put a quality metric that depends on delayed labels in a "real-time health" position as if it were live.
- Recommend an alert without stating its baseline, threshold, and severity tier.
- Overload the top view; reserve fine-grained per-feature charts for drill-downs.

**Instructions:**

1. **Map the audience and the decision each panel serves.** For each viewer (on-call, ML eng, leadership), list the questions they need answered. Every panel must serve a named question; drop panels that serve none.

2. **Layer the signals.** Organize into: (a) operational — latency p50/p95/p99, throughput, error/timeout rate, resource saturation; (b) input/data health — null rates, schema/range violations, volume, drift summary; (c) prediction behavior — score distribution, class mix, confidence; (d) model quality — accuracy/precision/recall/calibration, marked as lagging if labels are delayed.

3. **Attach a baseline to every signal.** Specify the reference (training dist, trailing window, SLO target) and how the panel shows deviation (vs baseline band, vs threshold line), so "good vs bad" is visible without interpretation.

4. **Set the cadence per signal.** Real-time signals (latency, errors, volume) refresh continuously; data/prediction drift summaries hourly/daily; quality metrics on the label-arrival cadence. State each explicitly.

5. **Design the top-line health summary.** A small set of status indicators that roll up the layers into green/amber/red, each tied to a defined rule — this is what answers "healthy now?" instantly.

6. **Define the alert tiers and routing.** Map signals to warning (notify) vs critical (page), with thresholds, consistency rules, dedup, and the runbook each alert links to.

7. **Plan drill-downs and segment views.** From any rolled-up signal, allow drill into per-feature, per-segment (region, device, customer tier) charts so a global amber can be localized.

8. **State refresh, retention, and cost.** Note data retention windows, query cost of heavy panels, and how stale data is shown (so an unrefreshed panel never reads as healthy).

**Output Format:**

A markdown dashboard spec:
- **Audience → Questions Map** — table
- **Panel Inventory by Layer** — table: Layer | Panel | Signal | Baseline | Cadence | Real-time vs Lagging
- **Top-Line Health Summary** — the rollup indicators and their rules
- **Alert Tiers** — table: Signal | Threshold | Consistency Rule | Severity | Routing | Runbook link
- **Drill-Down & Segment Plan** — what each rollup expands into
- **Refresh / Retention / Stale-Data Handling** — notes

## Verification

- [ ] Every panel serves a named question for a named audience.
- [ ] Every signal has an explicit baseline and a cadence.
- [ ] Lagging (label-dependent) quality panels are clearly distinguished from real-time panels.
- [ ] Top-line health rollup has defined green/amber/red rules.
- [ ] Each alert states threshold, consistency rule, severity, routing, and runbook.
- [ ] Drill-down path exists from rollups to per-feature/per-segment detail.

## False-Positive Prevention

❌ **DON'T:**
- Show a single accuracy number with no baseline so any value looks "fine."
- Display delayed-label quality metrics as if they were live model health.
- Render a stale/unrefreshed panel as green when data simply stopped flowing.
- Pack 200 per-feature drift charts on the top view and make health unreadable.
- Wire alerts to raw thresholds with no consistency rule, generating pager noise.

✅ **DO:**
- Plot every metric against its baseline band or target line.
- Tag lagging panels with their label-latency and last-update time.
- Add a "freshness" indicator so absent data reads as red/unknown, not green.
- Roll feature-level signals into a summary panel; keep detail in drill-downs.
- Tie alerts to thresholds + N-of-M consistency + a linked runbook.

## Example Output

```markdown
## Monitoring Dashboard Spec: Recommendation Ranker v7

### Audience → Questions Map
| Audience | Question |
|---|---|
| On-call SRE | Is it up, fast, and serving? |
| ML engineer | Are inputs/predictions normal vs baseline? |
| Product lead | Is CTR / quality holding (lagging)? |

### Panel Inventory by Layer
| Layer | Panel | Signal | Baseline | Cadence | RT/Lagging |
|---|---|---|---|---|---|
| Operational | Latency | p50/p95/p99 | SLO 200ms p95 | Real-time | RT |
| Operational | Errors | 5xx + timeout rate | <0.5% target | Real-time | RT |
| Input | Feature health | null/range violations | Schema contract | 15 min | RT |
| Input | Drift summary | model-level PSI | Trailing 28d | Hourly | RT |
| Prediction | Score dist | rank-score histogram | Trailing 28d | Hourly | RT |
| Prediction | Class/slate mix | top-k category share | Trailing 28d | Hourly | RT |
| Quality | CTR / NDCG | engagement-derived | Last-good week | Daily | Lagging (~1d) |
| Quality | Calibration | ECE | Trained ECE | Daily | Lagging |

### Top-Line Health Summary
- 🟢/🟡/🔴 Serving (errors+latency vs SLO) · Inputs (drift score + freshness) · Predictions (score-dist PSI) · Quality (CTR vs last-good, with lag badge).

### Alert Tiers
| Signal | Threshold | Consistency | Severity | Routing | Runbook |
|---|---|---|---|---|---|
| p95 latency | >300ms | 5 min | Critical | Page SRE | incident-response |
| Drift score | breach | 3 of 4 hrs | Warning | Slack ML | degradation-triage |
| CTR | -15% vs last-good | 2 days | Critical | Page ML | degradation-triage |

### Drill-Down & Segment Plan
- Drift score → per-feature PSI. CTR → per-region, per-device, new-vs-returning user.

### Refresh / Retention / Stale-Data Handling
- 90d retention; freshness badge per panel; panel with no data >2 intervals turns red.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** the design proceeds audience → layers → baselines → alerts.
- **ST-03 (Output Format Specification):** locks a panel-inventory + alert-tier dashboard spec.
- **DS-02 (Metric Specification):** each panel names its signal, baseline, and cadence.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances operational, data, prediction, and quality layers.
- **CM-02 (Constraint Specification):** baselines and label-latency constrain how each signal may be presented.

**Related Prompts:**
- `mlmonitor_drift_detection_design.md` — define the drift tests that feed the drift panels.
- `mlmonitor_slo_design_for_ml.md` — set the targets the dashboard plots against.
- `mlmonitor_performance_degradation_triage.md` — the runbook the quality alerts link to.
