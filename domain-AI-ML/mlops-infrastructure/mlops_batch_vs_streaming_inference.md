---
title: "Batch vs Streaming Inference Decision"
category: AI-ML/mlops-infrastructure
description: "Choose between batch, micro-batch, streaming, and on-demand inference by working backwards from when the prediction is actually consumed — exposing prediction staleness as the real cost, and pricing train/serve skew risk per serving shape."
techniques:
  - RT-10
  - RT-02
  - DS-02
  - CM-02
  - QA-12
difficulty: intermediate
tags:
  - batch-inference
  - streaming-inference
  - serving-architecture
  - prediction-freshness
  - train-serve-skew
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_model_serving_architecture.md
  - domain-AI-ML/mlops-infrastructure/mlops_gpu_capacity_planning.md
  - domain-AI-ML/mlops-infrastructure/mlops_feature_pipeline_design.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_throughput_batching_optimization.md
---

# Batch vs Streaming Inference Decision

**Objective:** Choose the serving shape by working backwards from the moment a prediction is consumed — surfacing prediction staleness as the cost that batch scheduling actually incurs, and pricing the different train/serve skew exposure each shape carries.

**When to Use:**
- Designing a new inference path and the serving shape is genuinely open.
- Real-time serving is expensive and you suspect the freshness it buys is not needed.
- Batch predictions are being consumed in a context where they may be too stale to be correct.

**When NOT to Use:**
- Latency requirements make the choice obvious — proceed to `mlops_model_serving_architecture.md`.
- The question is how to batch efficiently within real-time serving — use `../model-optimization-efficiency/mlopt_throughput_batching_optimization.md`.
- The bottleneck is feature availability rather than inference — use `mlops_feature_pipeline_design.md`.

## Inputs / Context

- **Consumption moment** — when the prediction is actually read and acted on, which is often much later than when it is requested.
- **Acceptable staleness** — how out-of-date a prediction may be before it becomes wrong, not merely old.
- **Input availability** — when the features a prediction needs become known; a prediction cannot precede its inputs.
- **Prediction space size** — whether all possible inputs can be enumerated and precomputed, or only observed ones.
- **Request volume and distribution** — including how much of the precomputed space is ever actually read.
- **Cost profile** — per-prediction cost, and the cost of idle capacity in an always-on path.

## Constraints

**Must:**
- Work backwards from the **consumption moment**, not the request moment. A prediction computed nightly and read at 4pm is 16 hours stale at the point of use, and that is the number that matters.
- Quantify staleness cost explicitly: how much prediction quality degrades between computation and consumption, measured rather than assumed.
- Check input availability against computation time — precomputing a prediction whose inputs arrive later means serving a prediction made without them.
- Compare **wasted computation** in batch (predictions computed and never read) against **idle capacity** in real-time, since those are the two shapes' respective waste modes.
- State the train/serve skew exposure of each shape; batch pipelines and real-time paths fail differently and one is much easier to keep aligned than the other.

**Must Not:**
- Choose real-time because it "feels" more modern; per-prediction cost and operational burden are higher and the freshness is frequently unused.
- Assert throughput or cost-ratio figures from memory; mark quantities `[measure on your workload]`.
- Assume batch predictions are free to over-produce — computing predictions for an entire user base when 3% are read is a real and often large cost.
- Ignore the cold-start case in a precomputed design: a new entity has no precomputed prediction, and that path must be designed rather than discovered.
- Treat micro-batching as a compromise without stating which of the two failure modes it inherits.

**Instructions:**

1. **Locate the consumption moment.** When is the prediction actually read and acted on? Trace it through the product. This step alone frequently changes the answer, because teams design against request time and users consume much later.

2. **Measure staleness tolerance.** How does prediction quality degrade with age? Compute predictions at t and evaluate at t+1h, +6h, +24h against outcomes. The curve tells you the maximum batch interval; without it, batch frequency is guesswork.

3. **Check input availability.** For each feature, when does it become known? If a needed feature arrives after the batch runs, the batch prediction is made without it — which is a correctness problem wearing a scheduling costume.

4. **Assess precomputability.** Can the prediction space be enumerated? Then measure the read rate: what fraction of precomputed predictions is ever consumed? A low read rate makes batch far more expensive than the per-prediction cost suggests.

5. **Screen the four shapes.**
   - *Batch* — scheduled, precomputed, served from a store. Cheapest per prediction, staleness bounded by interval, waste proportional to unread predictions.
   - *Micro-batch* — frequent small batches. Reduces staleness, keeps most of the batch cost profile, adds scheduling complexity.
   - *Streaming* — triggered by events. Fresh when inputs change, requires event infrastructure, cost tracks event volume.
   - *On-demand / real-time* — computed at request. Freshest, highest per-prediction cost and idle capacity, simplest to reason about for correctness.

6. **Compare the waste modes.** Batch waste is unread predictions; real-time waste is idle capacity between requests. Quantify both for this workload; the answer is frequently counterintuitive when the read rate is low or traffic is bursty.

7. **Assess train/serve skew per shape.** A batch pipeline often shares code with training, which reduces skew; a separate real-time path frequently reimplements feature logic, which is a classic skew source. State which risk you are taking and what guards it.

8. **Design the cold-start path.** For precomputed shapes: what happens for an entity with no prediction yet — fall back to on-demand, serve a default, or block. This is where precomputed designs most often fail in production.

9. **Recommend, with the staleness the choice accepts** stated in the same sentence as the choice.

**Output Format:**

A markdown decision:
- **Consumption Moment** — when the prediction is read, versus when it is computed.
- **Staleness Curve** — quality by prediction age; the resulting maximum interval.
- **Input Availability** — feature vs availability time; any precomputation conflict.
- **Precomputability & Read Rate** — enumerable? what fraction is read?
- **Shape Comparison** — table: Shape | Staleness | Cost profile | Waste mode | Skew risk.
- **Waste Comparison** — unread predictions vs idle capacity, quantified.
- **Cold-Start Path** — for precomputed designs.
- **Recommendation** — the shape, and the staleness it accepts.

## Verification

- [ ] The consumption moment is traced, not assumed to be the request moment.
- [ ] Staleness tolerance is measured as a quality-versus-age curve.
- [ ] Input availability is checked against computation time for every feature.
- [ ] Read rate is measured for any precomputed design.
- [ ] Both waste modes are quantified for this workload.
- [ ] Train/serve skew exposure is stated per shape.
- [ ] A cold-start path is designed for precomputed shapes.
- [ ] The recommendation states the staleness it accepts.
- [ ] No throughput or cost-ratio figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Design against request time when the prediction is consumed hours later; the staleness that matters accrues to consumption, not to computation.
- Assume nightly batch is fine because "the data only updates daily" without checking when the *consumer* reads it and what has changed since.
- Treat precomputed predictions as cheap when most are never read — the unread fraction is pure cost, and it is often the majority.
- Pick real-time for freshness the product does not use; you pay per-prediction cost and idle capacity for a property nobody consumes.
- Ship a precomputed design without a cold-start path; the first new entity in production finds it for you.
- Present micro-batching as a free compromise without saying which failure mode it keeps.

✅ **DO:**
- Trace the prediction to where it is actually read and act on that moment.
- Measure the staleness curve and let it set the maximum interval.
- Check that every feature exists before the prediction is computed.
- Quantify unread-prediction waste against idle-capacity waste for this specific workload.
- Name the skew risk each shape carries and the guard against it.
- State the accepted staleness alongside the recommendation, so it is a decision rather than a side effect.

## Example Output

```markdown
## Serving Shape Decision: Customer Churn Score

### Consumption Moment
Scores are currently computed nightly at 02:00. They are read by:
| Consumer | Read time | Age at consumption |
|---|---|---|
| Retention dashboard | throughout the day | 0–22 h |
| Outbound campaign selection | Mondays 09:00 | up to 7 days (uses Monday's batch) |
| **In-app offer at login** | any time | **0–22 h** |

The in-app consumer is the one nobody accounted for: it was added after the batch was designed
and reads a score that can be nearly a day old at the moment a customer is on the screen.

### Staleness Curve
Compute scores at t, evaluate against churn outcomes at t+6h, +24h, +72h, +7d `[measure]`.
Expect degradation to accelerate after a significant customer event — a failed payment or a
support escalation makes yesterday's score wrong, not merely old. The curve sets the maximum
tolerable interval per consumer, and those intervals differ, which is the core finding.

### Input Availability
| Feature | Available | Conflict with 02:00 batch? |
|---|---|---|
| Billing history | T-1 close | No |
| Support tickets | real-time | **Yes** — a 09:00 escalation is invisible until the next night |
| Product usage | hourly rollup | **Yes** — up to 22 h stale |
| Account tenure | static | No |

Two features change during the day. A score computed at 02:00 is not merely stale; for a
customer who raised a ticket at 09:00 it was computed **without the most predictive signal
available**. That is a correctness issue, not a freshness preference.

### Precomputability & Read Rate
Prediction space is enumerable — all active customers. **Read rate: `[measure]`** — the fraction
of nightly scores ever read by any consumer. If, as suspected, only a minority of customers log
in or are campaign-selected on a given day, most of the nightly compute is discarded.

### Shape Comparison
| Shape | Staleness | Cost profile | Waste mode | Skew risk |
|---|---|---|---|---|
| Nightly batch | 0–22 h | lowest per prediction | unread scores | **Low** — shares training pipeline code |
| Micro-batch (hourly) | 0–1 h | ~24× batch runs, same code | unread scores, more often | Low — same pipeline |
| **Streaming (event-triggered)** | minutes after a relevant event | tracks event volume | few wasted — only changed customers | **Medium** — needs event-time feature logic |
| On-demand at login | none | highest per prediction; idle otherwise | idle capacity | **High** — separate feature path, classic skew source |

### Waste Comparison
- Batch waste = (1 − read rate) × all customers, every night.
- On-demand waste = idle capacity between logins, plus recomputing for customers who log in
  repeatedly with nothing changed.
Quantify both `[measure]`. With a low read rate and clustered logins, streaming is likely to
dominate both — it computes only for customers whose inputs actually changed.

### Cold-Start Path
A customer created today has no precomputed score. Under batch this returns null and the in-app
offer silently does not fire — which is how this class of bug reaches production unnoticed.
**Design:** on-demand computation as fallback whenever a precomputed score is missing or older
than the consumer's tolerance, with the fallback rate monitored as a health signal.

### Recommendation
**Event-triggered streaming for the in-app and dashboard consumers, retaining a nightly batch as
the floor** for customers with no events. Campaign selection continues to read the batch, since
its 7-day tolerance is comfortably inside the staleness curve.

**Accepted staleness:** in-app scores are fresh within minutes of a relevant event; customers
with no events carry a score up to 24 hours old, which the staleness curve shows is acceptable
precisely because nothing about them has changed. The medium skew risk from event-time feature
logic is guarded by computing streaming features through the same transformation code as
training, with a scheduled parity check.
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** consumption moment → staleness tolerance → input availability → precomputability is the decision path.
- **RT-02 (Multi-Dimensional Analysis Framework):** shape × staleness × cost × waste mode × skew risk is the comparison grid.
- **DS-02 (Metric Specification):** staleness tolerance and read rate are defined as measured quantities rather than assumptions.
- **CM-02 (Constraint Specification):** the consumption-moment and input-availability rules bound the decision.
- **QA-12 (False Positives Identification):** separates a freshness preference from an actual correctness problem, and catches unread-prediction cost.

**Related Prompts:**
- `mlops_model_serving_architecture.md` — implementing the chosen shape.
- `mlops_feature_pipeline_design.md` — the feature availability this decision depends on.
- `mlops_gpu_capacity_planning.md` — the capacity implications of each shape.
- `../model-optimization-efficiency/mlopt_throughput_batching_optimization.md` — batching within a real-time path.
