---
title: "Distributed Training Plan"
category: AI-ML/deep-learning
description: "Choose among data, model, pipeline, and tensor parallelism for a training job by model/memory fit and interconnect; plan communication, sharding, and correctness checks against a single-device reference."
techniques:
  - RT-02
  - ST-02
  - CM-02
  - QA-01
  - DS-06
difficulty: advanced
tags:
  - distributed-training
  - data-parallel
  - model-parallel
  - pipeline-parallel
  - reproducibility
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/deep-learning/dl_mixed_precision_setup.md
  - domain-AI-ML/deep-learning/dl_data_loading_bottleneck_audit.md
  - domain-AI-ML/deep-learning/dl_reproducibility_setup.md
---

# Distributed Training Plan

**Objective:** Decide the parallelism strategy — data parallel, sharded data parallel (ZeRO/FSDP-style), tensor/model parallel, pipeline parallel, or a hybrid — for a training job based on whether the model and optimizer state fit in device memory and the cluster's interconnect, then plan communication, gradient sync/accumulation, and correctness checks that validate the distributed run against a single-device reference.

**When to Use:**
- A model or its optimizer state no longer fits on one device, or single-device training is too slow.
- Scaling from one GPU/TPU to many and deciding how to split work.
- A multi-node run produces different loss than single-device and you need a correctness plan.

**When NOT to Use:**
- The bottleneck is the input pipeline starving one GPU (`dl_data_loading_bottleneck_audit.md`).
- You only need to enable mixed precision for memory headroom (`dl_mixed_precision_setup.md`).
- Single-device training already fits and is fast enough — don't add distributed complexity.

## Inputs / Context

Provide what you can:
- **Framework & version** and its distributed API (e.g., DDP/FSDP, tf.distribute, jax pmap/sharding).
- **Model size**, optimizer state size, and per-device memory; activation memory profile.
- **Cluster topology** — devices per node, nodes, interconnect (NVLink/PCIe/InfiniBand/Ethernet) bandwidth.
- **Global vs per-device batch size** target and total step budget.
- **Current symptom** if debugging (loss mismatch, hangs, OOM, poor scaling efficiency).
- **Seeds/determinism** expectations.

## Constraints

**Must:**
- Choose parallelism by what fits in device memory first, then by interconnect bandwidth and scaling efficiency.
- Preserve the effective optimization semantics (global batch size, LR scaling, gradient averaging) when sharding.
- Validate the distributed run against a single-device reference on a tiny deterministic problem before scaling.

**Must Not:**
- Quote a specific scaling-efficiency percentage as guaranteed — frame throughput claims as to-be-measured.
- Reach for tensor/pipeline parallelism when sharded data parallel would fit and is simpler.
- Change global batch size implicitly when adding devices without re-scaling LR.

**Instructions:**

1. **Establish the memory fit.** Determine whether model + optimizer state + activations fit per device. If they fit, data parallel; if optimizer/params don't, sharded data parallel; if a single layer doesn't fit, tensor/pipeline parallel.

2. **Map the strategy to topology.** Match the communication pattern to the interconnect: all-reduce-heavy data parallel needs fast intra/inter-node links; tensor parallel demands very high bandwidth (keep within a node); pipeline parallel tolerates slower links but needs micro-batching.

3. **Design the sharding/hybrid.** For large models, combine: tensor parallel within node, pipeline across nodes, data parallel across replicas. Specify the degrees of each dimension.

4. **Preserve optimization semantics.** Fix the global batch size, gradient averaging (not summing) across replicas, LR scaling rule, and gradient accumulation if needed to hit the target batch.

5. **Plan communication & overlap.** Specify gradient bucketing/overlap with backward, activation checkpointing for memory, and pipeline bubble mitigation via micro-batches.

6. **Build the correctness ladder.** Step 1: single-device deterministic baseline on a tiny problem. Step 2: 2-device run must match single-device loss within numerical tolerance. Step 3: scale up and check loss curve parity and that gradients are synced.

7. **Define scaling diagnostics.** Specify how to measure throughput/scaling efficiency and detect stragglers, hangs (collective mismatch), and silent non-sync (loss diverges across replicas).

**Output Format:**

A markdown report:
- **Memory-Fit Verdict** — what fits → which family.
- **Strategy Recommendation** — parallelism dimensions + degrees.
- **Topology Mapping** — comm pattern vs interconnect.
- **Optimization-Semantics Plan** — batch/LR/averaging/accumulation.
- **Communication & Memory Tactics.**
- **Correctness Ladder** — single → 2-device → scaled checks.
- **Scaling Diagnostics.**

## Verification

- [ ] Parallelism family follows from the memory-fit analysis.
- [ ] Global batch size, gradient averaging, and LR scaling are preserved when sharding.
- [ ] A single-device reference and a 2-device parity check are specified before scaling.
- [ ] Communication pattern is matched to the interconnect.
- [ ] Throughput/scaling figures are framed as to-be-measured, not asserted.

## False-Positive Prevention

❌ **DON'T:**
- Use tensor parallelism across slow inter-node links — communication will dominate.
- Add replicas without re-scaling LR or fixing the global batch, then blame the optimizer.
- Sum instead of average gradients across replicas and silently change the effective LR.
- Declare "it scales" from a single run without a single-device parity check.

✅ **DO:**
- Choose parallelism by memory fit first, then interconnect.
- Keep tensor parallel within a node; use pipeline/data parallel across nodes.
- Validate distributed loss against a single-device reference on a tiny deterministic problem.
- Measure scaling efficiency and watch for hangs (collective mismatch) and non-sync (replica divergence).

## Example Output

```markdown
## Distributed Plan: 13B-Param Model, 4 nodes × 8 GPUs, InfiniBand

### Memory-Fit Verdict
Params + optimizer state exceed single-GPU memory; individual layers fit → sharded + tensor parallel needed.

### Strategy Recommendation
Hybrid: tensor parallel degree 8 (within node) × pipeline parallel degree 2 (across node pairs) × data parallel degree 2.

### Topology Mapping
Tensor-parallel all-reduce stays on NVLink (intra-node); pipeline stages cross IB; DP all-reduce over IB.

### Optimization-Semantics Plan
Global batch fixed; micro-batches to fill the pipeline; gradients averaged across DP replicas; LR scaled to global batch.

### Communication & Memory Tactics
Activation checkpointing on; gradient bucketing overlapped with backward; pipeline micro-batch count tuned to shrink bubbles.

### Correctness Ladder
1. Single-GPU deterministic toy run. 2. TP=2 must match within fp tolerance. 3. Full hybrid: loss curve parity + verify DP gradients synced.

### Scaling Diagnostics
Track tokens/sec vs device count; flag stragglers; alert if replica losses diverge (non-sync) or a collective hangs (shape/world-size mismatch).
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** weighs parallelism options across memory/interconnect/efficiency.
- **ST-02 (Structured Sequential Instructions):** memory fit → strategy → semantics → correctness ladder.
- **CM-02 (Constraint Specification):** memory and interconnect are the governing constraints.
- **QA-01 (Self-Verification):** the correctness ladder and checklist validate the distributed run.
- **DS-06 (Prioritization & Severity Guidance):** orders the correctness checks from cheapest/most-discriminating.

**Related Prompts:**
- `dl_mixed_precision_setup.md` — recover memory and speed before/with parallelism.
- `dl_data_loading_bottleneck_audit.md` — ensure the input pipeline isn't the real limiter.
- `dl_reproducibility_setup.md` — pin seeds and ops for the single-device reference.
```