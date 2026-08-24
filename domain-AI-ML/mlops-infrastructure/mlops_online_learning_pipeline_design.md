---
title: "Online Learning Pipeline Design"
category: AI-ML/mlops-infrastructure
description: "Design continuous model updating from streaming feedback — establishing that label latency permits it, guarding the feedback loop that lets a model teach itself its own errors, and building the rollback path that a continuously updating model needs most."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - online-learning
  - continuous-training
  - feedback-loop
  - label-latency
  - rollback
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/production-monitoring/mlmonitor_retraining_trigger_strategy.md
  - domain-AI-ML/production-monitoring/mlmonitor_feedback_loop_detection.md
  - domain-AI-ML/deep-learning/dl_continual_learning_strategy.md
  - domain-AI-ML/production-monitoring/mlmonitor_rollback_strategy.md
---

# Online Learning Pipeline Design

**Objective:** Design a pipeline that updates a model continuously from production feedback — gated first on whether label latency makes online learning meaningful at all, then built around the two things that determine whether it survives: a guard on the feedback loop, and a rollback path fast enough for a model that changes every few minutes.

**When to Use:**
- The environment changes faster than a scheduled retraining cadence can follow, and labels arrive quickly.
- Scheduled retraining is chronically behind and the gap is measurable in lost performance.
- Cold-start or rapidly shifting populations make a static model stale within its own release cycle.

**When NOT to Use:**
- Labels arrive slowly relative to the change rate — online learning without timely labels updates on noise. Use `../production-monitoring/mlmonitor_retraining_trigger_strategy.md`.
- The change is new tasks or classes rather than distribution shift — use `../deep-learning/dl_continual_learning_strategy.md`.
- The domain is regulated such that every model version must be validated before use; continuous updating and per-version validation are structurally incompatible, and that must be resolved before design.

## Inputs / Context

- **Label latency** — the delay between prediction and ground truth, and its distribution. This is the gate.
- **Change rate** — how fast the relationship being modelled actually moves, measured.
- **Feedback origin** — whether labels come from outcomes independent of the model, or from behaviour the model influenced.
- **Update mechanism** — full retrain on a window, incremental update, or parameter-efficient adaptation.
- **Validation capability** — what can be checked automatically before an update is promoted.
- **Rollback capability** — how quickly a bad update can be reversed, and to what.

## Constraints

**Must:**
- Gate on label latency versus change rate. If labels arrive slower than the environment moves, online learning updates on stale information; state this and stop.
- Address the **feedback loop explicitly**: where the model's own predictions influence the labels it later trains on. This is the characteristic failure of online learning, and it degrades quietly rather than visibly.
- Validate every update before promotion, automatically, against a held-out or delayed-label set — a pipeline that promotes without a gate is an unmonitored write path into production.
- Design rollback to a known-good checkpoint with a **stated time-to-rollback**, since the failure mode is gradual drift discovered late.
- Bound how far the model may move per update and cumulatively between human reviews.

**Must Not:**
- Assert update frequencies, learning-rate schedules, or window sizes from memory; mark quantities `[measure on your workload]`.
- Train on labels derived from actions the model itself selected without correcting for that selection — the model will confirm its own choices and narrow indefinitely.
- Promote updates without a validation gate because "it is only a small update"; small updates compound.
- Retain only the current model; rollback needs a checkpoint history, and the retention window must exceed the time it typically takes to notice a problem.
- Treat improving online metrics as validation when those metrics are computed on traffic the model shaped.

**Instructions:**

1. **Gate on label latency versus change rate.** Measure both. Online learning is justified only when labels arrive materially faster than the environment moves. If they do not, say so and route to scheduled retraining.

2. **Classify the feedback source.** *Independent outcomes* — the label occurs regardless of the model's prediction. *Model-influenced* — the model chose what the user saw, and the label reflects that choice. The second requires explicit correction, and most production feedback is the second.

3. **Design the feedback-loop guard.** Where feedback is model-influenced: reserve a fraction of traffic for randomized or unmodified serving to generate unbiased labels, apply importance weighting to correct for selection, and monitor the diversity of what the model exposes over time. Narrowing exposure diversity is the early signal that the loop is closing.

4. **Choose the update mechanism.** Full retrain on a sliding window is simplest and most robust; incremental update is cheapest and hardest to reason about; parameter-efficient adaptation sits between. State the window length or update rate and why, and what happens to older data.

5. **Design the validation gate.** Every candidate update is checked before promotion: performance on a held-out set with delayed labels, prediction-distribution shift bounds, and per-slice regression checks. Define the automatic reject conditions — this gate is the only thing standing between a bad batch of labels and production.

6. **Bound movement.** Maximum parameter or prediction change per update, and cumulative drift permitted between human reviews. Without a cumulative bound, many individually acceptable updates arrive somewhere nobody approved.

7. **Design rollback for the actual failure mode.** Gradual drift is noticed late, so rollback must reach checkpoints from hours or days ago, not just the previous one. State the checkpoint retention window, the time-to-rollback, and how the corrupting update window is identified so it can be excluded from the next training pass.

8. **Define monitoring.** Prediction-distribution drift, per-slice performance, exposure diversity, label-volume anomalies, and update-magnitude trend. An update magnitude that is rising is a signal in itself.

9. **Set the human review cadence.** What a human checks, how often, and what they can trigger. A continuously updating model with no scheduled human review has no owner between incidents.

**Output Format:**

A markdown design:
- **Gate: Label Latency vs Change Rate** — both measured; the go/no-go.
- **Feedback Source Classification** — independent or model-influenced.
- **Feedback-Loop Guard** — randomized fraction, correction method, diversity monitor.
- **Update Mechanism** — type, window/rate, treatment of old data.
- **Validation Gate** — checks and automatic reject conditions.
- **Movement Bounds** — per update and cumulative.
- **Rollback Design** — retention window, time-to-rollback, corrupt-window identification.
- **Monitoring** — signals and what each reveals.
- **Human Review** — cadence, scope, available actions.

## Verification

- [ ] Label latency and change rate are both measured, and the gate decision follows from them.
- [ ] The feedback source is classified, and model-influenced feedback has an explicit correction.
- [ ] A randomized or unmodified traffic fraction generates unbiased labels.
- [ ] Every update passes an automatic validation gate with defined reject conditions.
- [ ] Per-update and cumulative movement bounds are set.
- [ ] Rollback reaches checkpoints old enough to precede a slow drift, with a stated time-to-rollback.
- [ ] Exposure diversity is monitored.
- [ ] A human review cadence with defined scope and actions exists.
- [ ] No update frequencies or window sizes are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Build online learning when labels lag the change rate — the pipeline will update confidently on information that is already out of date.
- Train on clicks from items the model chose to show without correcting for that selection; the model learns that its own choices were right and narrows until it is recommending a handful of items to everyone.
- Read rising online metrics as validation when those metrics come from traffic the model shaped — the loop flatters itself.
- Retain only the last checkpoint; slow degradation is noticed days later, and the checkpoint you need is the one you deleted.
- Skip the validation gate for small updates; the failure mode is accumulation, and every large drift is made of small updates.
- Leave a continuously updating model without a scheduled human review because the automation is working.

✅ **DO:**
- Measure both sides of the gate and accept "scheduled retraining is the right answer" as a legitimate outcome.
- Reserve unbiased traffic; it is the only source of labels the loop cannot corrupt.
- Monitor exposure diversity as the early warning that the loop is closing.
- Bound cumulative movement between reviews, not just per-update movement.
- Retain checkpoints for longer than it typically takes to notice a problem, and rehearse the rollback.
- Give a human a scheduled look with defined actions, so the system has an owner between incidents.

## Example Output

```markdown
## Online Learning Design: Marketplace Search Ranking

### Gate: Label Latency vs Change Rate
| Quantity | Measurement |
|---|---|
| Label latency (click) | seconds |
| Label latency (purchase — the label we actually want) | `[measure — hours to days]` |
| Change rate (inventory turnover, seasonal shift) | `[measure]` |

Click labels arrive fast; purchase labels do not. **Gate decision: online learning on clicks,
with purchase labels feeding a slower scheduled retrain.** Treating clicks as a proxy for
purchase intent is an accepted approximation and must be stated as one, not hidden — the fast
signal and the signal we care about are not the same.

### Feedback Source Classification
**Model-influenced, strongly.** Users click what the ranker showed them. A result the ranker
never surfaced generates no positive label, ever. Left uncorrected, the ranker converges on
whatever it already ranked highly — the textbook closing loop.

### Feedback-Loop Guard
- **Randomized fraction:** a small share of sessions serve a randomized or exploration-weighted
  ranking. These are the only labels not shaped by the model, and they anchor everything else.
- **Correction:** inverse-propensity weighting on logged exposure probability for the remainder.
- **Diversity monitor:** distribution of distinct items surfaced per query cluster, tracked over
  time. **A narrowing distribution is the loop closing** and is the earliest available signal —
  it moves well before ranking quality visibly degrades.

### Update Mechanism
Incremental updates on a sliding window `[choose length from the change-rate measurement]`.
Older data ages out rather than being reweighted, so seasonal patterns from previous cycles are
not held indefinitely. Update rate `[measure — balance responsiveness against validation cost]`.

### Validation Gate
Every candidate update must pass, automatically, before promotion:
| Check | Automatic reject if |
|---|---|
| Held-out ranking quality (randomized-traffic labels) | below current model by any margin |
| Prediction-distribution shift | beyond a set bound |
| Per-segment regression (top query clusters, new sellers) | any segment regresses beyond bound |
| Exposure diversity | falls below the floor |

The randomized-traffic held-out set is what makes this gate meaningful; validating on
model-shaped traffic would let the loop pass its own exam.

### Movement Bounds
Per update: bounded parameter change. **Cumulative: total drift from the last human-reviewed
checkpoint is bounded**, and when the bound is reached, updates pause pending review rather than
continuing. Many acceptable updates in the same direction is exactly how a model arrives
somewhere nobody chose.

### Rollback Design
| Attribute | Value |
|---|---|
| Checkpoint retention | every update for 7 days; daily for 30 days |
| Time-to-rollback | target minutes, **rehearsed monthly** |
| Corrupt-window identification | update log with the label batch each update consumed |

Retention exceeds the time it typically takes to notice slow degradation — retaining only the
previous checkpoint would mean rolling back to a model that already contains the problem. The
update log lets a bad label window be excluded from the next training pass rather than being
re-consumed immediately after rollback.

### Monitoring
- Prediction-distribution drift, continuous.
- Per-segment ranking quality on randomized traffic, daily.
- **Exposure diversity, continuous** — the loop-closure signal.
- Label-volume anomalies (a tracking outage looks like a behaviour change).
- **Update-magnitude trend** — rising magnitude means the model is chasing something, and is
  worth investigating before quality moves.

### Human Review
Weekly. Scope: exposure diversity trend, cumulative drift since last review, segment
performance on randomized traffic, and any paused updates. Available actions: approve continued
updating, force rollback, pause online updates and fall back to the scheduled model, or widen
the randomized fraction.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** the label-latency gate precedes design, so the pipeline is not built where it cannot work.
- **RT-02 (Multi-Dimensional Analysis Framework):** feedback source × correction × validation × rollback is the design grid.
- **CM-02 (Constraint Specification):** the unbiased-traffic requirement and cumulative movement bound are hard constraints.
- **QA-12 (False Positives Identification):** rejects model-shaped metrics as validation, which is the failure that makes a closing loop look healthy.
- **DS-06 (Prioritization and Severity Guidance):** monitoring signals are ordered by how early they reveal loop closure.

**Related Prompts:**
- `../production-monitoring/mlmonitor_retraining_trigger_strategy.md` — the scheduled alternative when the gate fails.
- `../production-monitoring/mlmonitor_feedback_loop_detection.md` — detecting the loop this design guards against.
- `../deep-learning/dl_continual_learning_strategy.md` — when increments are new tasks rather than shift.
- `../production-monitoring/mlmonitor_rollback_strategy.md` — the general rollback design this specializes.
