---
title: "SLO/SLI Design for ML Services"
category: AI-ML/production-monitoring
description: "Define SLIs and SLOs for an ML service across quality, latency, and availability, with error budgets — accounting for delayed labels and the difference between operational health and model correctness."
techniques:
  - ST-02
  - DS-02
  - CM-02
  - RT-02
  - QA-12
difficulty: advanced
tags:
  - slo
  - sli
  - error-budget
  - reliability
  - quality-metrics
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_monitoring_dashboard_design.md
  - domain-AI-ML/production-monitoring/mlmonitor_ml_incident_response.md
  - domain-AI-ML/production-monitoring/mlmonitor_performance_degradation_triage.md
---

# SLO/SLI Design for ML Services

**Objective:** Define a coherent set of SLIs (service-level indicators) and SLOs (objectives) for a production ML service spanning operational reliability (latency, availability/error rate) *and* model quality (accuracy/precision/calibration/business proxy), with explicit error budgets — while correctly handling the fact that ML quality SLIs often depend on delayed labels and that operational health does not imply model correctness.

**When to Use:**
- Formalizing reliability targets for an ML service so alerting, on-call, and release gates have a shared definition of "good enough."
- Translating vague expectations ("the model should be accurate and fast") into measurable, budgeted commitments.
- Before designing dashboards or incident severity, which should reference these SLOs.

**When NOT to Use:**
- To build the dashboard that displays SLO compliance (use `mlmonitor_monitoring_dashboard_design.md`).
- To design drift detectors (use `mlmonitor_drift_detection_design.md`).
- For pure offline model evaluation (that belongs in model-evaluation prompts).

## Inputs / Context

Provide what you can:
- **Service & consumers** — what the model serves, who/what depends on it, and the cost of each kind of failure.
- **Label latency** — immediate, delayed (how long), or no ground truth — central to which quality SLIs are real-time vs lagging.
- **Task type & metric semantics** — classification/regression/ranking/generation, class balance, and which errors hurt most.
- **Traffic & criticality** — volume, peak patterns, and blast radius (user-facing, money, safety).
- **Existing measurements** — current latency, error, and quality numbers if any (do not invent these).
- **Tolerance** — acceptable downtime/quality-loss and the business appetite for risk.

## Constraints

**Must:**
- Cover three dimensions — quality, latency, availability — and state which quality SLIs are real-time vs lagging due to label delay.
- Define each SLI precisely (numerator/denominator, measurement window, baseline) and each SLO as a target over that window, with an error budget.
- Choose quality SLIs that respect the task (class-specific metrics for imbalanced problems, calibration where probabilities are consumed) — not raw accuracy by default.

**Must Not:**
- Set a quality SLO on a metric whose labels arrive too late to act within the SLO window, without flagging it as lagging and pairing it with a real-time proxy.
- Use aggregate accuracy as the quality SLI on imbalanced data (a majority-class baseline can "meet" it while the model is useless).
- Fabricate target numbers; derive them from stated requirements/current measurements or mark as "to be set after baselining."

**Instructions:**

1. **Enumerate consumers and failure costs.** For each consumer, identify what "the service failed them" means — slow, unavailable, or wrong — and how costly each is. This decides where to spend SLO stringency.

2. **Define availability/error SLIs.** Specify success criteria for a served request (returns a valid prediction within time, no error), the measurement window, and the SLO target + error budget. Distinguish hard errors (5xx/timeouts) from soft failures (fallback served).

3. **Define latency SLIs.** Choose percentiles (p50/p95/p99) appropriate to the consumer experience, set targets, and state how cold starts / batch vs real-time paths are handled.

4. **Define quality SLIs respecting the task.** Pick metrics that bite: precision/recall/F-beta or per-class metrics for imbalanced classification, calibration (ECE) where probabilities are consumed, ranking metrics where relevant, business proxies where labels are scarce. Compare each against a baseline (majority/prior model).

5. **Resolve the label-latency problem.** For each quality SLI, state whether it is real-time or lagging. For lagging SLIs, pair a real-time leading proxy (prediction-distribution health, engagement signal) so the service is not "blind until labels arrive," and define the lagging SLI's evaluation cadence.

6. **Set error budgets and burn policy.** For each SLO, define the budget (allowed failure over the window) and the burn-rate alerting (fast-burn pages, slow-burn warns), and what budget exhaustion means (freeze releases, prioritize reliability).

7. **Tie SLOs to action.** Map SLO/budget states to incident severity, release gates (canary must not burn budget), and retraining urgency — so the SLOs govern behavior, not just reporting.

8. **Plan baselining and review.** If targets are unknown, specify a baselining period to set them empirically, and a cadence to review SLOs as the service and traffic evolve.

**Output Format:**

A markdown SLO spec:
- **Consumers & Failure Costs** — table
- **SLI/SLO Catalog** — table: Dimension | SLI (precise definition) | Window | SLO Target | Error Budget | Real-time/Lagging
- **Quality Metric Rationale** — why these metrics for this task + baselines
- **Label-Latency Handling** — lagging SLIs and their real-time proxies
- **Error-Budget Policy** — burn-rate alerts, exhaustion consequences
- **SLO → Action Map** — severity, release gates, retraining links
- **Baselining & Review Plan** — how unknown targets get set

## Verification

- [ ] All three dimensions (quality, latency, availability) have SLIs and SLOs.
- [ ] Each SLI has a precise definition, window, and baseline; each SLO has an error budget.
- [ ] Quality SLIs respect the task (class-specific/calibration where appropriate), not raw accuracy on imbalanced data.
- [ ] Every quality SLI is marked real-time or lagging, and lagging ones have a real-time proxy.
- [ ] Error budgets have burn-rate alerting and an exhaustion policy.
- [ ] Target numbers are derived/baselined, not fabricated.

## False-Positive Prevention

❌ **DON'T:**
- Set an accuracy SLO on imbalanced data that a majority-class predictor would already satisfy.
- Commit to a quality SLO whose labels arrive weeks later than the window in which you must act.
- Treat "service is up and fast" as evidence the model is correct.
- Invent SLO targets with no baseline measurement to anchor them.

✅ **DO:**
- Use class-specific metrics and a baseline so the quality SLO reflects real skill.
- Mark lagging quality SLIs and pair them with real-time leading proxies.
- Keep operational and quality SLOs separate — both can fail independently.
- Baseline first, then set targets; mark unknowns as "to be set after baselining."

## Example Output

```markdown
## SLO Spec: Loan Default Scoring Service

### Consumers & Failure Costs
| Consumer | Slow | Unavailable | Wrong |
|---|---|---|---|
| Underwriting API | app stalls | manual fallback | bad credit decision (high $) |

### SLI/SLO Catalog
| Dim | SLI | Window | SLO | Budget | RT/Lag |
|---|---|---|---|---|---|
| Availability | valid response / total requests | 30d | 99.9% | 43m/mo | RT |
| Latency | p99 scoring latency | 30d | < 250ms | 1% over | RT |
| Quality | precision @ approval threshold | rolling 30d matured | ≥ 0.80 | — | Lagging (~30d) |
| Quality | calibration ECE (probabilities used for pricing) | 30d matured | ≤ 0.05 | — | Lagging |
| Quality (proxy) | score-distribution PSI vs golden | daily | < 0.2 | — | RT proxy |

### Quality Metric Rationale
- Default is imbalanced (~6%); raw accuracy is meaningless (94% by predicting "no default"). Precision/recall + calibration chosen because scores set prices. Baseline: prior model precision 0.76.

### Label-Latency Handling
- Default labels mature ~30–45d. Lagging precision/ECE evaluated monthly; real-time proxy = score-distribution PSI + approval-rate stability, which page first.

### Error-Budget Policy
- Availability fast-burn (2% budget in 1h) → page; slow-burn (10% in 3d) → warn. Budget exhausted → freeze model releases until restored.

### SLO → Action Map
- Latency/availability breach → SEV per incident matrix. Quality SLO breach (matured) → degradation triage + retraining evaluation. Proxy breach → early triage.

### Baselining & Review Plan
- Targets above set from 90-day baseline; review quarterly and after each major retrain.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** consumers → availability → latency → quality → budgets → actions flow.
- **DS-02 (Metric Specification):** every SLI is precisely defined with window, baseline, and target.
- **CM-02 (Constraint Specification):** label latency and error budgets constrain which SLOs are actionable.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances quality, latency, and availability dimensions.
- **QA-12 (False Positives Identification):** prevents accuracy-on-imbalanced and up-implies-correct fallacies.

**Related Prompts:**
- `mlmonitor_monitoring_dashboard_design.md` — surfaces SLO compliance and burn rates.
- `mlmonitor_ml_incident_response.md` — uses these SLOs to classify incident severity.
- `mlmonitor_performance_degradation_triage.md` — invoked when a quality SLO is breached.
```