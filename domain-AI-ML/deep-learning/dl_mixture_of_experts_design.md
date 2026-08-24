---
title: "Mixture-of-Experts Design"
category: AI-ML/deep-learning
description: "Decide whether sparse mixture-of-experts is worth its complexity and design it if so — separating parameter count from active compute, addressing routing collapse and load imbalance before training, and accounting for the memory cost that sparsity does not remove."
techniques:
  - RT-02
  - ST-02
  - DS-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - mixture-of-experts
  - sparse-models
  - routing
  - load-balancing
  - scaling
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/deep-learning/dl_architecture_selection.md
  - domain-AI-ML/deep-learning/dl_distributed_training_plan.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_model_routing_cascade_design.md
  - domain-AI-ML/mlops-infrastructure/mlops_gpu_capacity_planning.md
---

# Mixture-of-Experts Design

**Objective:** Decide whether a sparse mixture-of-experts architecture earns its considerable complexity for a specific workload, and if so design the routing, capacity, and balancing — keeping clear throughout that MoE trades memory for compute rather than reducing cost outright.

**When to Use:**
- Model capacity is the bottleneck and dense scaling has hit a compute or latency wall.
- The workload is genuinely heterogeneous, so specialization has something to specialize on.
- Serving hardware has memory headroom but not compute headroom — the specific condition MoE exploits.

**When NOT to Use:**
- Memory is the constraint — MoE increases total parameters and usually makes this worse, not better.
- The workload is homogeneous; experts will not differentiate and you pay the complexity for nothing.
- You want to route between *separate models* by difficulty or cost — use `../model-optimization-efficiency/mlopt_model_routing_cascade_design.md`, which is a different and usually simpler thing.

## Inputs / Context

- **Current bottleneck** — compute, memory, or latency, measured rather than assumed. This single fact usually decides the answer.
- **Workload heterogeneity** — evidence that inputs cluster into meaningfully different types.
- **Serving hardware** — memory per device, interconnect bandwidth, and device count.
- **Latency budget** — including tail latency, which routing affects more than mean.
- **Training infrastructure** — whether expert-parallel training is available at all.
- **Dense baseline** — a matched dense model's quality, compute, and memory.

## Constraints

**Must:**
- Separate **total parameters** from **active parameters per token** in every statement. MoE's entire proposition lives in that gap, and conflating them is how MoE gets adopted for a memory-bound problem it makes worse.
- Confirm the bottleneck is compute and that memory headroom exists, before anything else.
- Address routing collapse and load imbalance in the design, not as a training-time surprise — they are the default behaviour, not an edge case.
- State the memory cost: all experts must be resident somewhere, so total memory grows even though per-token compute does not.
- Compare against a matched dense baseline on quality, compute, memory, and latency together — MoE wins on some and loses on others, and a single-axis comparison is meaningless.

**Must Not:**
- Assert expert counts, capacity factors, routing-method comparisons, or scaling results from memory; mark quantities `[measure on your workload]`.
- Describe MoE as "cheaper" without specifying on which axis; it is cheaper in active compute and more expensive in memory and complexity.
- Ignore tail latency — routing introduces variance and possible token dropping, and the p99 is where that shows.
- Assume experts will specialize meaningfully; verify it after training and be willing to conclude they did not.
- Recommend MoE where the training infrastructure cannot support expert parallelism.

**Instructions:**

1. **Measure the bottleneck.** Compute-bound, memory-bound, or latency-bound, with numbers. If memory-bound, MoE is the wrong direction and the recommendation is to stop here.

2. **Evidence the heterogeneity.** Show the workload contains genuinely different input types — clustering, per-segment error analysis, or domain structure. Homogeneous workloads produce experts that all learn the same thing, and the complexity is then pure overhead.

3. **Establish the dense baseline.** A matched dense model with quality, active compute, total memory, and p50/p99 latency. Everything is judged against this four-way profile.

4. **Design routing.** Number of experts, experts activated per token, and the routing mechanism. State the resulting active-versus-total parameter ratio explicitly, since that ratio *is* the design's proposition.

5. **Plan against routing collapse.** Without intervention, routing collapses onto a few experts — this is the expected behaviour. Specify the load-balancing mechanism, the auxiliary loss and its weight, and the metric that reveals collapse (expert utilization entropy or per-expert token share) as a first-class training-time monitor rather than a post-hoc check.

6. **Set expert capacity and decide the overflow policy.** Capacity per expert determines what happens when routing sends more tokens than an expert can take: drop, overflow to a second expert, or pad. State the choice and its quality cost, since dropped tokens are silently unprocessed inputs.

7. **Account for memory honestly.** All experts must be resident across the serving fleet. State total memory, per-device memory with the chosen expert-parallel layout, and the interconnect traffic routing introduces. This is the cost side of the trade and it is routinely under-reported.

8. **Model the latency profile.** Mean and tail. Routing adds a decision step, cross-device expert dispatch adds communication, and imbalanced batches add variance. Report p99, not just p50.

9. **Verify specialization after training.** Inspect what each expert receives. If experts are interchangeable, the architecture did not deliver and a dense model of matched active compute is the better answer — which is a legitimate and useful conclusion.

10. **State the operational cost.** Checkpoint size, expert-parallel deployment complexity, debugging difficulty, and what happens when a device holding experts fails.

**Output Format:**

A markdown design:
- **Bottleneck Measurement** — compute / memory / latency, with numbers; the gate decision.
- **Heterogeneity Evidence** — what justifies specialization.
- **Dense Baseline** — quality, active compute, total memory, p50/p99.
- **Routing Design** — experts, top-k, mechanism, active-vs-total ratio.
- **Load Balancing** — mechanism, auxiliary loss, collapse metric and threshold.
- **Capacity & Overflow** — capacity factor, overflow policy, quality cost.
- **Memory Accounting** — total, per device, interconnect traffic.
- **Latency Profile** — p50 and p99 versus dense.
- **Specialization Verification** — how it will be checked, and the fallback if absent.
- **Operational Cost** — checkpoints, deployment, failure behaviour.

## Verification

- [ ] The bottleneck is measured, and memory-bound cases are routed away from MoE.
- [ ] Workload heterogeneity is evidenced, not assumed.
- [ ] A matched dense baseline covers quality, compute, memory, and latency.
- [ ] Active and total parameters are stated separately throughout.
- [ ] Load balancing and a collapse metric are specified before training.
- [ ] Capacity and overflow policy are defined, with the quality cost of dropping stated.
- [ ] Total and per-device memory are accounted, including interconnect traffic.
- [ ] p99 latency is reported alongside p50.
- [ ] A post-training specialization check exists, with a fallback if experts are interchangeable.
- [ ] No expert counts, capacity factors, or scaling results are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Adopt MoE to reduce cost when the constraint is memory — total parameters go up, and the architecture makes the actual bottleneck worse.
- Quote total parameter count as the model's capability and active parameters as its cost, in the same breath, without stating both plainly each time.
- Leave load balancing until training misbehaves; routing collapse is the default trajectory, not an anomaly.
- Report p50 latency only — routing variance and expert dispatch live in the tail, which is what users experience.
- Assume experts specialized because the loss improved; check what each expert actually receives, and accept that they may be interchangeable.
- Set a capacity factor without deciding what happens to overflow tokens — silently dropped tokens are unprocessed inputs nobody is counting.

✅ **DO:**
- Measure the bottleneck first and be willing to stop at that step.
- Evidence heterogeneity before assuming there is anything to specialize on.
- Compare against a matched dense model on all four axes at once.
- Instrument expert utilization from the first training step, with a defined collapse threshold.
- Account for total and per-device memory, and say plainly that sparsity does not reduce it.
- Verify specialization after training and be prepared to conclude that dense was the better answer.

## Example Output

```markdown
## MoE Design Assessment: Multilingual Document Understanding
Serving 40 languages and 6 document types; quality plateaued on a dense model at the current
compute budget.

### Bottleneck Measurement — the gate
| Resource | Utilization | Verdict |
|---|---|---|
| Compute (GPU util at p95 load) | ~92% | **Bound** |
| Memory (per device) | ~48% of available | **Headroom** |
| Latency p99 vs budget | within budget, no slack for a dense scale-up | Bound |

Compute-bound with memory headroom — the specific condition MoE exploits. Had memory been at
90%, the recommendation would be to stop here, because MoE increases total parameters.

### Heterogeneity Evidence
Per-language and per-document-type error analysis shows distinct error profiles: CJK languages
fail differently from Latin-script; forms fail differently from prose. Feature-space clustering
recovers language-family structure without supervision. There is real structure for experts to
find — this is not a homogeneous workload where specialization would be wishful.

### Dense Baseline
| Metric | Dense |
|---|---|
| Quality (macro F1 over languages) | `[measure]` |
| Active params / token | `[measure]` |
| Total memory | `[measure]` |
| p50 / p99 latency | `[measure]` |

### Routing Design
Experts `[choose]`, top-k `[choose]` per token, learned routing.
**State plainly:** total parameters rise by roughly the expert multiplier; active parameters per
token rise only by the top-k factor. The gap between those two numbers is the entire proposition,
and both belong in every summary of this design.

### Load Balancing
Auxiliary load-balancing loss, weight `[tune]`. **Collapse metric: expert utilization entropy,
logged every step from step zero**, with a threshold below which training halts for
investigation. Routing collapse onto a few experts is the default trajectory; treating this as a
first-class training monitor rather than a post-hoc check is the difference between catching it
in the first hours and discovering it after a full run.

### Capacity & Overflow
Capacity factor `[tune]`. **Overflow policy: overflow to the next-ranked expert rather than
drop.** Dropping tokens on a document-understanding task means silently unprocessed spans of a
customer's document, which is a correctness failure that no aggregate metric surfaces. The extra
compute from overflow is the accepted price.

### Memory Accounting
| Item | Value |
|---|---|
| Total parameters (all experts) | `[compute]` |
| Per-device with expert-parallel layout | `[compute]` |
| Interconnect traffic per token | `[measure]` |

Sparsity reduces per-token compute. It does **not** reduce memory — every expert must be
resident somewhere in the fleet, and the interconnect traffic from cross-device dispatch is a new
cost that the dense model did not have.

### Latency Profile
Report both. Expect p50 to improve versus a dense model of equivalent quality, and **p99 to
worsen** relative to a dense model of equivalent active compute, because routing adds a decision
step, cross-device dispatch adds communication, and batch imbalance adds variance. If the p99
budget has no slack, that alone can disqualify the design regardless of quality gains.

### Specialization Verification
After training, tabulate token routing by language and document type. If experts receive
near-uniform mixtures, they are interchangeable and **the honest conclusion is that a dense model
of matched active compute is the better system** — simpler, cheaper to serve, easier to debug.
That outcome must be reportable rather than explained away.

### Operational Cost
Checkpoints grow with total parameters, affecting storage and restore time. Expert-parallel
deployment couples serving to a specific device layout. Debugging is harder: a quality regression
may be a routing problem rather than a model problem, which is a diagnostic path the team does
not currently have. Device failure now removes specific experts rather than a replica, so the
failure model changes and needs its own runbook.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** quality × active compute × memory × latency is the four-axis comparison MoE must be judged on.
- **ST-02 (Structured Sequential Instructions):** bottleneck measurement gates the design, so MoE is not adopted against a memory constraint.
- **DS-02 (Metric Specification):** active-versus-total parameters and the collapse metric are defined quantities with thresholds.
- **CM-02 (Constraint Specification):** the state-both-parameter-counts rule and the overflow-policy requirement bound the design.
- **QA-12 (False Positives Identification):** rejects loss improvement as evidence of specialization and p50-only latency reporting.

**Related Prompts:**
- `dl_architecture_selection.md` — the broader architecture decision this sits inside.
- `dl_distributed_training_plan.md` — expert parallelism is a distributed-training problem.
- `../model-optimization-efficiency/mlopt_model_routing_cascade_design.md` — routing between separate models, which is the simpler alternative.
- `../mlops-infrastructure/mlops_gpu_capacity_planning.md` — the memory and device-count planning this design depends on.
