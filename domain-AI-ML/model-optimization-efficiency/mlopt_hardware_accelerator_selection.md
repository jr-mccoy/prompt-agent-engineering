---
title: "ML Hardware Accelerator Selection"
category: AI-ML/model-optimization-efficiency
description: "Choose the right compute (CPU / GPU / TPU / NPU / inference accelerator) for training or serving a given workload and budget — scoring candidates on fit, throughput-per-dollar, memory ceiling, and ecosystem support, with the assumptions made explicit and verifiable."
techniques:
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - hardware-selection
  - gpu
  - tpu
  - accelerator
  - cost-performance
  - capacity-planning
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-optimization-efficiency/mlopt_throughput_batching_optimization.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_inference_latency_optimization.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_compression_tradeoff_analysis.md
---

# ML Hardware Accelerator Selection

**Objective:** Recommend a compute target (CPU, GPU, TPU, NPU, or specialized inference accelerator — and which tier/size) for a specific training or serving workload under a stated budget, by scoring candidates on workload fit, memory ceiling, throughput-per-dollar, latency capability, and ecosystem/software support — with every performance assumption made explicit and flagged for benchmark verification rather than asserted as fact.

**When to Use:**
- Choosing hardware to train or serve a model and you need a structured, budget-aware comparison.
- An existing accelerator is the bottleneck (OOM, too slow, too costly) and you are weighing alternatives.
- Capacity planning: deciding how many of which device a workload requires.

**When NOT to Use:**
- The fix is software-level (batching/compilation) on existing hardware (use `mlopt_inference_latency_optimization.md` / `mlopt_throughput_batching_optimization.md`).
- The model should be compressed to fit current hardware first (use `mlopt_compression_tradeoff_analysis.md`).

## Inputs / Context

Provide what you can; the recommendation degrades gracefully if some are missing:
- **Workload type** — training vs fine-tuning vs serving; model family and size (parameters); precision needs.
- **Performance target** — for training: time-to-train or throughput; for serving: latency SLA and required throughput.
- **Memory footprint** — model + optimizer states + activations (training) or model + KV-cache/activations (serving); the memory ceiling is often the gating factor.
- **Budget & basis** — capex vs cloud opex, cost ceiling, and whether on-prem, cloud, or both are options.
- **Framework + version** — to assess software/kernel support and portability across candidate accelerators.
- **Operational constraints** — availability/lead time, power/thermal limits, data-residency, existing fleet.

## Constraints

**Must:**
- Ask for the workload (training vs serving), model size, performance target, and budget before recommending; the answer differs sharply between training and inference.
- Score every candidate on memory ceiling first — a device that cannot hold the workload is disqualified regardless of speed.
- Mark every performance/throughput-per-dollar figure as an estimate requiring a benchmark on the actual workload; never present vendor peak FLOPs as delivered performance.

**Must Not:**
- Quote specific benchmark numbers, prices, or peak-FLOP figures as authoritative facts from memory — frame them as assumptions to verify with current pricing and a representative benchmark.
- Recommend an accelerator whose software ecosystem does not support the user's framework/kernels without flagging the porting cost.
- Optimize peak throughput while ignoring memory ceiling, latency SLA, or total cost of ownership.

**Instructions:**

1. **Classify the workload and gating metric.** Establish training vs serving, model size, precision, and the single most binding metric (time-to-train, latency SLA, or throughput). State it — it drives the whole comparison.

2. **Compute the memory requirement.** Estimate the working-set memory (weights + optimizer/activations for training; weights + cache/activations for serving) and use it as the first filter: candidates below the ceiling are out.

3. **Enumerate candidate accelerators.** List realistic options across classes (CPU, GPU tiers, TPU, NPU, inference ASICs) appropriate to the workload and budget; note availability/lead time.

4. **Score on a fixed rubric.** For each candidate rate: memory fit, delivered throughput/latency (estimate, to benchmark), throughput-per-dollar / cost-per-request or cost-per-train, software/ecosystem support for the framework, and operational fit (power, availability, portability).

5. **Apply the budget and TCO lens.** Translate to total cost: cloud opex over the expected duration vs capex+power amortized; include the cost of scaling out (multiple devices, interconnect) where one device is insufficient.

6. **Flag the verification benchmarks.** Specify the representative micro-benchmark or end-to-end run the user must execute on the shortlist to replace estimates with measured numbers before committing.

7. **Rank and recommend.** Give a primary recommendation and a runner-up, each with the conditions under which it wins, and the explicit assumptions that, if wrong, flip the decision.

8. **State residual risks.** Supply, lead time, ecosystem lock-in, and what changes (model growth, traffic growth) would force a re-evaluation.

**Output Format:**

A markdown decision document:
- **Workload & Gating Metric** — training/serving, model size, binding metric
- **Memory Requirement & Filter** — estimated working set, candidates eliminated
- **Candidate Scorecard** — table: Accelerator | Memory fit | Throughput/Latency (est.) | $/unit-of-work (est.) | Ecosystem support | Op. fit
- **TCO Comparison** — cost over the expected horizon, including scale-out
- **Verification Benchmarks** — what to measure on the shortlist before buying
- **Recommendation + Runner-Up** — with assumption-flip conditions
- **Residual Risks**

## Verification

- [ ] Workload (training vs serving), model size, performance target, and budget are established before the recommendation.
- [ ] Memory ceiling is applied as the first filter; under-ceiling candidates are eliminated.
- [ ] Every throughput/cost figure is marked as an estimate to be benchmarked, not stated as fact.
- [ ] Framework/ecosystem support is scored, with porting cost flagged where relevant.
- [ ] TCO (not just per-unit speed) and scale-out cost are included.
- [ ] A primary + runner-up recommendation with assumption-flip conditions and residual risks is given.

## False-Positive Prevention

❌ **DON'T:**
- Rank accelerators by advertised peak TFLOPs — delivered throughput on a real model is often a fraction and varies by kernel maturity.
- Pick the fastest device while ignoring that the model + activations/cache won't fit in its memory.
- Compare a cloud hourly rate to an on-prem sticker price without amortizing capex, power, and utilization.
- Recommend an accelerator with immature software support for the user's framework without pricing the porting effort.

✅ **DO:**
- Treat vendor peak numbers as upper bounds; require a representative benchmark on the shortlist.
- Filter on memory ceiling first, then rank survivors on delivered performance and cost.
- Compare on TCO over the workload's real horizon at realistic utilization, including scale-out interconnect.
- Score ecosystem/kernel support explicitly and factor porting/maintenance cost into the decision.

## Example Output

```markdown
## Accelerator Selection: Serving a 13B-parameter LLM (latency-sensitive chat)

### Workload & Gating Metric
Serving, 13B params, fp16/int8, binding metric = p99 TTFT ≤ 700 ms at ~30 req/s.

### Memory Requirement & Filter
fp16 weights ≈ 26 GB + KV-cache/activations for 32 concurrent seqs ≈ 10–14 GB → ~40 GB working set.
- Eliminated: 24 GB-class GPUs (won't hold weights + cache at target concurrency without aggressive quantization).

### Candidate Scorecard
| Accelerator | Memory fit | Throughput/Latency (est.) | $/1k req (est.) | Ecosystem | Op. fit |
|---|---|---|---|---|---|
| 80 GB datacenter GPU | Yes | high (verify) | medium | mature | available |
| 48 GB GPU + int8 | Tight | medium (verify) | lower | mature | available |
| Inference ASIC | Yes | high (verify) | low | limited kernels | lead time + porting |

### TCO Comparison
Over 12 months at ~50% utilization: 48 GB+int8 path lowest cloud opex if quantization holds accuracy; ASIC cheapest per request but porting + lead-time risk.

### Verification Benchmarks
Run end-to-end p99 TTFT and goodput at 30 req/s on the 80 GB GPU and the 48 GB+int8 path with production-shaped traffic before committing.

### Recommendation + Runner-Up
Primary: 48 GB GPU with int8 weights — meets memory and likely SLA at lowest cost, IF int8 accuracy drop ≤ budget (verify via `mlopt_quantization_plan.md`). Runner-up: 80 GB GPU (fp16) — safer accuracy, higher cost. Decision flips to 80 GB if int8 fails the accuracy gate.

### Residual Risks
GPU supply/lead time; traffic growth beyond 30 req/s forces a second replica; ASIC reconsidered only if volume justifies porting.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** workload → memory filter → candidates → scorecard → TCO → benchmark → recommend.
- **RT-02 (Multi-Dimensional Analysis Framework):** scores fit, performance, cost, ecosystem, and operations jointly.
- **DS-01 (Framework Application):** applies a fixed scoring rubric across candidates.
- **CM-02 (Constraint Specification):** memory ceiling and budget as hard filters.
- **DS-06 (Prioritization & Severity Guidance):** ranks candidates and names assumption-flip conditions.

**Related Prompts:**
- `mlopt_throughput_batching_optimization.md` — squeeze more goodput from the chosen device before buying more.
- `mlopt_inference_latency_optimization.md` — software levers that may avoid a hardware change.
- `mlopt_compression_tradeoff_analysis.md` — shrink the model to fit cheaper hardware.
```