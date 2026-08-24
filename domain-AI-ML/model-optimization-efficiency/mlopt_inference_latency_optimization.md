---
title: "ML Inference Latency Optimization"
category: AI-ML/model-optimization-efficiency
description: "Reduce single-request inference latency through profiling-driven levers — batching, graph compilation, kernel/operator fusion, caching, and precision — with a measurement plan that isolates the real bottleneck and pairs each gain with its accuracy/correctness cost."
techniques:
  - ST-02
  - RT-09
  - RT-10
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - inference-latency
  - profiling
  - compilation
  - kernel-fusion
  - caching
  - serving-optimization
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-optimization-efficiency/mlopt_throughput_batching_optimization.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_quantization_plan.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_hardware_accelerator_selection.md
---

# ML Inference Latency Optimization

**Objective:** Reduce per-request inference latency to meet a stated SLA by first profiling to locate the true bottleneck (compute, memory bandwidth, data movement, host overhead, or cold start), then applying the right ordered levers — compilation, operator fusion, caching, precision, batching — and measuring each change against a fixed protocol so every latency gain is paired with its accuracy/correctness cost.

**When to Use:**
- A model meets accuracy targets but a latency SLA (p50/p95/p99) is missed in serving.
- You need to know whether latency is compute-bound, memory-bound, or overhead-bound before optimizing.
- You want a profiling-first plan instead of blindly trying optimizations.

**When NOT to Use:**
- The goal is maximizing aggregate throughput under a relaxed latency bound (use `mlopt_throughput_batching_optimization.md`).
- The real fix is different hardware (use `mlopt_hardware_accelerator_selection.md`).
- The model is too large to fit at all — compress first (`mlopt_compression_tradeoff_analysis.md`).

## Inputs / Context

Provide what you can:
- **Target hardware + runtime** — exact accelerator/CPU, inference runtime/server, and version. *Ask the user if unspecified — the bottleneck and the available kernels depend on it.*
- **Framework + version** — training/export framework and serving stack.
- **Latency SLA** — target p50/p95/p99 and the request shape (batch size, sequence length, image size, autoregressive vs single-shot).
- **Current profile** — any existing latency breakdown (per-op timings, host vs device, data-transfer time) or a note that none exists.
- **Accuracy bar** — the metric and maximum acceptable drop, since some levers (precision, caching) can change outputs.
- **Workload pattern** — request rate, burstiness, whether cold starts matter.

## Constraints

**Must:**
- Profile before prescribing — locate the dominant cost (compute / memory bandwidth / data movement / host overhead / cold start) and target it first.
- Ask for target hardware + runtime and framework + version; tie each lever to what the named stack supports.
- Pair every latency-reducing lever that can alter outputs (precision, approximate kernels, caching) with its accuracy/correctness check.

**Must Not:**
- Quote specific latency numbers as measured — frame figures as estimates to verify with the user's profiler on their hardware.
- Recommend a lever (e.g., compilation, fusion) without confirming the runtime supports it.
- Optimize a sub-component that the profile shows is not the bottleneck.

**Instructions:**

1. **Restate the SLA and request shape.** Fix the target percentiles and the exact input shape; latency at batch=1, seq=2048 is a different problem than batch=1, seq=64. This frames every measurement.

2. **Profile to find the bottleneck.** Require a breakdown into device compute, memory-bandwidth-bound ops, host↔device transfer, framework/host overhead, and cold-start/model-load. Identify the dominant contributor — optimize that, not the rest.

3. **Apply graph-level levers.** Where the bottleneck is host overhead or unfused ops: graph compilation/tracing, operator fusion, constant folding, eliminating Python-loop dispatch, static shapes. Confirm runtime support.

4. **Apply precision/kernel levers.** If compute-bound and hardware-supported: fp16/bf16/int8 and faster attention/conv kernels. Pair each with an accuracy check (these change outputs). Cross-link `mlopt_quantization_plan.md` for the full precision plan.

5. **Apply caching/algorithmic levers.** For autoregressive/repeat workloads: KV-cache, result/embedding caching, early-exit, speculative decoding — each with the correctness/staleness implication stated.

6. **Address data movement and cold start.** Pin memory / overlap transfer with compute; pre-warm models, keep weights resident, reduce serialization cost if cold start dominates tail latency.

7. **Define the measurement protocol.** Specify warmed-up p50/p95/p99 over N runs at the fixed request shape on the target hardware, isolating one change at a time, plus the accuracy metric on a held-out set for any output-altering lever.

8. **Set accept/reject gates and ordering.** Apply highest-leverage change first, re-profile, repeat. Pass = SLA met AND accuracy drop ≤ budget. Define the fallback (compress, change hardware, relax SLA).

**Output Format:**

A markdown plan:
- **SLA & Request Shape** — target percentiles, input shape
- **Bottleneck Profile** — table: Cost category | Share | Evidence | Dominant?
- **Ordered Optimization Plan** — table: Lever | Targets which bottleneck | Est. gain | Accuracy/Correctness cost | Runtime support needed
- **Measurement Protocol** — percentiles, N, hardware, isolation method
- **Accept/Reject Gates** — SLA + accuracy thresholds and fallback
- **Open Questions** — missing profile data, runtime capabilities, accuracy budget

## Verification

- [ ] The SLA and exact request shape are restated.
- [ ] A bottleneck profile (or a request for one) precedes any optimization recommendation.
- [ ] Each lever is mapped to the specific bottleneck it addresses and confirmed against runtime support.
- [ ] Output-altering levers (precision, caching, approximations) are each paired with an accuracy/correctness check.
- [ ] The measurement protocol fixes warmed-up percentiles, N, and one-change-at-a-time isolation on target hardware.
- [ ] Accept/reject gates and a fallback exist.

## False-Positive Prevention

❌ **DON'T:**
- Optimize compute when the profile shows latency is dominated by host↔device transfer or framework overhead.
- Report a speedup from a single un-warmed run — cold-start and JIT-compilation noise dominate first calls.
- Apply int8/fp16 or approximate kernels and report only latency, hiding an accuracy regression.
- Claim a fusion/compilation win without confirming the runtime actually fused the ops (read the compiled graph).

✅ **DO:**
- Profile first and spend effort only on the dominant cost category.
- Report warmed-up p50/p95/p99 over many runs at the real request shape, changing one thing at a time.
- Pair every output-altering lever with a held-out accuracy check and report both numbers together.
- Verify the runtime applied the optimization (inspect the graph / kernel timeline), not just that you requested it.

## Example Output

```markdown
## Latency Optimization: Recommendation Ranker (target: single GPU, serving runtime vX)

### SLA & Request Shape
Target p99 ≤ 25 ms at batch=1, 256 candidate items per request.

### Bottleneck Profile
| Cost category | Share | Evidence | Dominant? |
|---|---|---|---|
| Host overhead (Python dispatch) | 46% | profiler: gaps between kernels | Yes |
| Device compute | 31% | kernel timeline | No |
| Host↔device transfer | 18% | memcpy spans | No |
| Cold start | n/a | model resident | No |

### Ordered Optimization Plan
| Lever | Targets | Est. gain | Accuracy cost | Runtime support |
|---|---|---|---|---|
| Graph compile + static shapes | Host overhead | large (verify) | none (numeric-equal) | supported |
| Operator fusion | Host overhead/compute | medium | none | supported |
| fp16 compute | Compute | medium | small — check AUC | GPU has fp16 |
| Pin + overlap transfer | Transfer | small | none | supported |

### Measurement Protocol
50-run warmup, then p50/p95/p99 over 1,000 runs at batch=1/256 items on target GPU; one lever at a time. fp16 change validated against AUC on held-out, 95% CI.

### Accept/Reject Gates
Pass if p99 ≤ 25 ms AND AUC drop ≤ 0.002. Else evaluate quantization or a smaller model.

### Open Questions
- Confirm runtime supports static-shape compilation for this graph; confirm AUC budget.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** SLA → profile → graph → precision → caching → measurement → gate.
- **RT-09 (Root Cause Explanation):** the profile-first step isolates the true latency cause.
- **RT-10 (Troubleshooting Decision Tree):** levers are selected by which bottleneck the profile reveals.
- **CM-02 (Constraint Specification):** SLA and runtime capability govern lever selection.
- **DS-02 (Metric Specification):** locks warmed-up percentile measurement and the accuracy check.

**Related Prompts:**
- `mlopt_throughput_batching_optimization.md` — when aggregate throughput, not single-request latency, is the goal.
- `mlopt_quantization_plan.md` — the full plan behind the precision lever.
- `mlopt_hardware_accelerator_selection.md` — when no software lever closes the gap.
```