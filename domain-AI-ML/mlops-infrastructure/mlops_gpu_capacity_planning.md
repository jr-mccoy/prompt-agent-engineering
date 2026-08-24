---
title: "GPU Capacity Planning"
category: AI-ML/mlops-infrastructure
description: "Plan accelerator capacity across training and serving — sizing from measured utilization rather than device count, separating memory-bound from compute-bound workloads, and deciding the reserved/on-demand/spot mix against interruption tolerance."
techniques:
  - RT-02
  - DS-02
  - CM-02
  - QA-12
  - DS-06
difficulty: advanced
tags:
  - gpu-capacity
  - accelerator-planning
  - utilization
  - spot-instances
  - infrastructure-cost
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/mlops-infrastructure/mlops_infra_cost_optimization.md
  - domain-AI-ML/mlops-infrastructure/mlops_cost_budget_forecasting.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_hardware_accelerator_selection.md
  - domain-AI-ML/mlops-infrastructure/mlops_batch_vs_streaming_inference.md
---

# GPU Capacity Planning

**Objective:** Size accelerator capacity for training and serving from measured behaviour rather than device counts — distinguishing memory-bound from compute-bound workloads, sizing serving against tail load and training against queue depth, and choosing the commitment mix from interruption tolerance rather than from headline discount rates.

**When to Use:**
- Requesting or renewing accelerator capacity and needing a defensible number.
- Training jobs queue for days, or inference latency degrades at peak, and you need to know whether the answer is more devices or better utilization.
- Accelerator spend is rising and nobody can say what drives it.

**When NOT to Use:**
- The question is which accelerator type suits a model — use `../model-optimization-efficiency/mlopt_hardware_accelerator_selection.md`.
- The question is attributing existing spend to teams — use `mlops_cost_attribution_showback.md`.
- The bottleneck is data loading rather than the accelerator — use `../deep-learning/dl_data_loading_bottleneck_audit.md`; buying devices will not fix it.

## Inputs / Context

- **Current utilization** — accelerator utilization *and* memory utilization, separately, over time. Device count without utilization tells you nothing.
- **Training workload profile** — job sizes, durations, queue depth, and how much of the queue is genuinely urgent.
- **Serving workload profile** — request rate over time including peak, tail latency, and batch behaviour.
- **Interruption tolerance** — per workload: which can checkpoint and resume, and which cannot.
- **Growth expectation** — new models, higher traffic, larger models, with the basis for each.
- **Commitment options available** — reserved, on-demand, spot or preemptible, and the terms.

## Constraints

**Must:**
- Size from **measured utilization**, and report accelerator and memory utilization separately — a fleet at 30% compute and 95% memory is a memory problem and adding devices for compute reasons will not help.
- Distinguish training capacity (sized against queue depth and tolerable wait) from serving capacity (sized against peak load and tail latency); they have different sizing logic and should never be pooled into one number.
- Establish whether current low utilization is a scheduling problem before recommending more capacity — badly packed devices look exactly like insufficient devices.
- Tie the commitment mix to per-workload interruption tolerance, not to discount rates alone.
- State the failure behaviour at capacity: what queues, what degrades, and who is affected.

**Must Not:**
- Assert utilization benchmarks, device throughput figures, pricing, or discount rates from memory; mark every quantity `[measure in your environment]` or `[verify current pricing]`.
- Recommend capacity growth without first reporting what the existing fleet achieves — this is the most expensive shortcut available.
- Size serving on mean load; the tail is what causes incidents.
- Put an interruption-intolerant workload on preemptible capacity without a checkpointing and resumption design.
- Treat headroom as waste without stating what it buys — burst absorption and failure tolerance are functions, not slack.

**Instructions:**

1. **Measure the current fleet.** Accelerator utilization, memory utilization, and idle time, broken down by workload class and over a period long enough to include peaks. Report the distribution, not the mean.

2. **Classify each workload as memory-bound or compute-bound.** Different bottlenecks call for different device types and different scaling directions, and this single classification frequently changes the recommendation entirely.

3. **Diagnose low utilization before buying.** Common causes that look like insufficient capacity: fragmentation from poor scheduling, jobs holding devices while data-loading, interactive sessions left idle, and single-device jobs on multi-device nodes. Quantify how much of the gap each accounts for, and state what capacity would be recovered by fixing them.

4. **Size training capacity from queue economics.** Queue depth, wait time distribution, and the cost of waiting — distinguishing genuinely blocking waits from those nobody notices. Capacity is sized to the tolerable wait, not to zero wait, which is never economic.

5. **Size serving capacity from tail load and latency.** Peak concurrent load, the latency budget at p99, and the batching behaviour. Include failure-domain headroom: capacity must absorb a device or zone failure without breaching the budget.

6. **Set the commitment mix by interruption tolerance.**
   - *Reserved / committed* — the baseline that runs continuously, typically serving.
   - *On-demand* — burst above the baseline and short-notice needs.
   - *Spot / preemptible* — checkpointable training only, with resumption designed and tested, never assumed.
   Report the mix against each workload's tolerance, and mark all pricing `[verify current]`.

7. **Model growth with its basis.** Each growth driver — traffic, model size, new models — with the evidence behind it. Growth assumed without a basis is how capacity plans become wrong in both directions.

8. **State the at-capacity behaviour.** What happens when demand exceeds supply: training queues lengthen, serving sheds load, or a workload class is preempted. Decide the priority order in advance rather than during the incident.

9. **Define the review trigger.** Utilization thresholds and growth events that re-open the plan.

**Output Format:**

A markdown plan:
- **Current Fleet** — table: Workload class | Devices | Accelerator util | Memory util | Idle %.
- **Bottleneck Classification** — memory-bound vs compute-bound per workload.
- **Utilization Recovery** — table: Cause | Capacity lost | Fix | Recoverable.
- **Training Capacity** — queue depth, tolerable wait, resulting size.
- **Serving Capacity** — peak load, p99 budget, failure headroom, resulting size.
- **Commitment Mix** — table: Workload | Interruption tolerance | Commitment type | Pricing `[verify]`.
- **Growth Model** — driver, basis, projected need.
- **At-Capacity Behaviour** — priority order and who is affected.
- **Review Triggers** — thresholds and events.

## Verification

- [ ] Accelerator and memory utilization are reported separately.
- [ ] Each workload is classified memory-bound or compute-bound.
- [ ] Utilization recovery is quantified before capacity growth is recommended.
- [ ] Training is sized from queue economics; serving from tail load.
- [ ] Serving capacity includes failure-domain headroom.
- [ ] Commitment mix follows interruption tolerance, with resumption designed for preemptible work.
- [ ] Every growth driver has a stated basis.
- [ ] At-capacity priority order is defined in advance.
- [ ] All pricing and throughput figures are marked for verification, not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Report "we have N GPUs at 40% utilization, we need more" — 40% utilization with a full queue is a scheduling problem, and buying devices makes it a more expensive scheduling problem.
- Pool training and serving into a single capacity number; one is sized by tolerable wait, the other by tail latency, and averaging them satisfies neither.
- Size serving to mean request rate — the incident happens at peak, which is the number that should drive the plan.
- Put a non-checkpointing training job on preemptible capacity for the discount; the restarts will cost more than the saving.
- Quote device throughput or hourly pricing from memory into a plan someone will commit budget against.
- Treat all headroom as waste — some of it is the failure tolerance that keeps serving inside its latency budget when a zone drops.

✅ **DO:**
- Report the utilization distribution over a period covering peaks, split by compute and memory.
- Classify the bottleneck first; a memory-bound fleet needs different devices, not more of the same.
- Quantify recoverable capacity from scheduling and idle-session fixes before requesting growth.
- Size training against tolerable wait and serving against p99 plus failure headroom.
- Match commitment type to tested interruption tolerance, and verify pricing at the time you commit.
- Decide the at-capacity priority order before the day it is needed.

## Example Output

```markdown
## GPU Capacity Plan: ML Platform, Next Fiscal Year

### Current Fleet
| Workload class | Devices | Accel util (p50/p95) | Memory util (p50/p95) | Idle % |
|---|---|---|---|---|
| Training — scheduled | `[measure]` | `[measure]` | `[measure]` | `[measure]` |
| Training — interactive | `[measure]` | **low expected** | `[measure]` | **high expected** |
| Serving — real-time | `[measure]` | `[measure]` | `[measure]` | `[measure]` |
| Serving — batch | `[measure]` | `[measure]` | `[measure]` | `[measure]` |

### Bottleneck Classification
| Workload | Bound by | Implication |
|---|---|---|
| LLM fine-tuning | **Memory** | more of the same device does not help; needs higher-memory devices or sharding |
| Vision training | Compute | scales with device count |
| Real-time serving | **Memory** (model resident) + latency | device count driven by replicas, not throughput |
| Batch serving | Compute | genuinely throughput-scalable |

Two of four workloads are memory-bound. A plan that adds compute-oriented devices would leave
both exactly where they are — which is why this table precedes any purchase recommendation.

### Utilization Recovery — before buying anything
| Cause | Capacity lost | Fix | Recoverable |
|---|---|---|---|
| Interactive notebooks left running | `[measure]` | idle timeout + reclamation | High — no purchase needed |
| Single-device jobs on multi-device nodes | `[measure]` | bin-packing in the scheduler | Moderate |
| Devices idle during data loading | `[measure]` | prefetch pipeline fix | Moderate — see dl_data_loading_bottleneck_audit |
| Fragmentation between large jobs | `[measure]` | gang scheduling / backfill | Moderate |

Recoverable capacity is subtracted from the growth request. Requesting growth before this table
exists is the single most expensive error available in capacity planning.

### Training Capacity
Sized against **tolerable wait**, not zero wait. Current queue depth and wait distribution
`[measure]`. Distinguish blocking waits (a release depends on the job) from background waits
(exploratory runs nobody is waiting on). Size so blocking waits stay within the agreed bound;
background waits absorb the remaining variance.

### Serving Capacity
Sized against **p95 concurrent load** and the p99 latency budget, plus **failure-domain headroom**
sufficient to lose one zone without breaching the budget. That headroom is not slack — it is the
function that keeps the latency SLO true during a failure, and it should be labelled as such in
the budget conversation.

### Commitment Mix
| Workload | Interruption tolerance | Commitment | Note |
|---|---|---|---|
| Real-time serving | **None** | Reserved | must not be preemptible |
| Batch serving | Tolerant (retryable) | Spot + on-demand fallback | |
| Scheduled training | Tolerant **if checkpointed** | Spot | **requires tested resumption**, not assumed |
| Interactive training | Low (sessions lost) | On-demand | |

All pricing `[verify current rates at commitment time]`. The spot allocation for scheduled
training is contingent on checkpoint/resume being tested end to end — without that test, the
discount is a liability.

### Growth Model
| Driver | Basis | Projected need |
|---|---|---|
| Traffic growth | product forecast, cited | `[compute]` |
| Larger models | roadmap commitment to a larger checkpoint | `[compute]` — memory-driven |
| New model families | 3 planned, 1 confirmed | `[compute]` — count only the confirmed one |

Only the confirmed driver is included in the committed request; the other two are recorded as
options with a decision date, so the plan is not sized against a roadmap that may not land.

### At-Capacity Behaviour
Priority when demand exceeds supply, decided now rather than during the incident:
1. Real-time serving — never preempted.
2. Batch serving — degrades to longer completion windows.
3. Scheduled training — queues.
4. Interactive training — reclaimed first, with notice.

### Review Triggers
- Sustained accelerator or memory utilization above threshold for 2 consecutive weeks.
- Blocking queue wait exceeding the agreed bound.
- Any confirmed new model family or a model size change.
- Quarterly regardless.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** workload class × bottleneck type × commitment × growth driver is the planning grid.
- **DS-02 (Metric Specification):** utilization is specified as separate compute and memory distributions rather than a single average.
- **CM-02 (Constraint Specification):** the measure-before-buying and verify-pricing rules bound what may be committed.
- **QA-12 (False Positives Identification):** separates a scheduling problem from a genuine capacity shortfall, which look identical in a device count.
- **DS-06 (Prioritization and Severity Guidance):** the at-capacity priority order is set in advance.

**Related Prompts:**
- `mlops_infra_cost_optimization.md` — reducing the cost of the capacity you have.
- `mlops_cost_budget_forecasting.md` — turning this plan into a budget.
- `../model-optimization-efficiency/mlopt_hardware_accelerator_selection.md` — which device type, once the bottleneck is classified.
- `mlops_batch_vs_streaming_inference.md` — the serving-shape decision that changes what capacity is needed.
