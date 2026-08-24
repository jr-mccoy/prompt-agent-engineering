---
title: "ML Quantization Plan (PTQ vs QAT)"
category: AI-ML/model-optimization-efficiency
description: "Design a quantization plan — PTQ vs QAT, precision per layer (int8/fp16/bf16), calibration, and an accuracy-recovery + validation protocol that pairs every speed/size gain with its measured quality cost."
techniques:
  - ST-02
  - RT-02
  - QA-12
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - quantization
  - ptq
  - qat
  - int8
  - inference-efficiency
  - accuracy-recovery
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-optimization-efficiency/mlopt_compression_tradeoff_analysis.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_inference_latency_optimization.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_edge_deployment_optimization.md
---

# ML Quantization Plan (PTQ vs QAT)

**Objective:** Produce a concrete quantization plan for a trained model — choosing between post-training quantization (PTQ) and quantization-aware training (QAT), selecting precision (int8 / fp16 / bf16) globally and per sensitive layer, specifying calibration, and defining an accuracy-recovery and validation protocol — so that every size/latency gain is reported alongside its measured accuracy cost.

**When to Use:**
- You have a working full-precision model and need a smaller/faster artifact for serving or edge.
- A latency/memory budget cannot be met at fp32/fp16 and you are considering int8 or lower.
- You need to decide whether cheap PTQ is enough or whether QAT's cost is justified.

**When NOT to Use:**
- The model is not yet meeting baseline accuracy at full precision (fix that first).
- The bottleneck is data movement or batching, not arithmetic precision (use `mlopt_inference_latency_optimization.md`).
- You want a holistic size/latency/accuracy comparison across many techniques (use `mlopt_compression_tradeoff_analysis.md`).

## Inputs / Context

Provide what you can; the plan degrades gracefully if some are missing:
- **Target hardware + runtime** — exact accelerator (CPU/GPU/NPU/TPU model) and inference runtime; which low-precision kernels it actually supports (e.g., int8 GEMM, bf16). *Ask the user if unspecified — kernel support, not theory, determines real speedup.*
- **Framework + version** — training/export framework and quantization toolkit and version.
- **Model architecture** — layer types, known-sensitive components (attention, normalization, embeddings, final classifier/regressor head).
- **Accuracy budget** — the metric, the current full-precision score, and the maximum acceptable drop.
- **Calibration data** — availability of a representative, label-optional sample for PTQ calibration.
- **Constraints** — retraining feasibility (compute/data access for QAT), artifact size ceiling, latency SLA.

## Constraints

**Must:**
- Ask for target hardware + runtime and framework + version before recommending a precision; tie every speedup claim to kernels the named hardware actually supports.
- Pair every efficiency gain (size, latency, memory) with its accuracy cost and the exact way to measure that cost on a held-out set.
- State whether each recommendation is PTQ or QAT and why, given the user's retraining feasibility.

**Must Not:**
- Quote specific speedup or accuracy numbers as if measured — mark any illustrative figure as an estimate to be verified on the user's data and hardware.
- Recommend uniform int8 without identifying layers that typically need higher precision (keep-in-fp16 list).
- Assume a runtime supports a precision/kernel without confirming it.

**Instructions:**

1. **Establish the precision floor and the budget.** Restate the full-precision metric, the accuracy budget (max acceptable drop), the size/latency target, and what the hardware's kernels support. This is the governing constraint for every later choice.

2. **Choose PTQ vs QAT.** Start with PTQ (cheapest). Recommend QAT only when PTQ is projected to exceed the accuracy budget AND retraining is feasible. State the cost of QAT (data, compute, pipeline changes) explicitly so the tradeoff is visible.

3. **Select precision globally, then per-layer.** Pick a default (commonly int8 for compute-bound serving, fp16/bf16 for accuracy-sensitive or unsupported-int8 hardware). Then list layers to keep at higher precision (embeddings, first/last layers, normalization, attention softmax) and justify each with its sensitivity.

4. **Specify calibration (PTQ).** Define the calibration sample size and representativeness, the observer/scheme (per-tensor vs per-channel, symmetric vs asymmetric, static vs dynamic) and why it suits the activation distributions.

5. **Define the accuracy-recovery path.** Order remedies by cost: per-channel weights → mixed precision (raise sensitive layers) → better calibration → QAT. For each, state the expected recovery and the added cost.

6. **Specify the measurement protocol.** Name the held-out set, the accuracy metric, and the efficiency metrics (artifact size, p50/p95 latency at the target batch size, peak memory) measured on the target hardware — never on the dev box if it differs.

7. **Define accept/reject gates.** State the pass condition (accuracy drop ≤ budget AND latency/size target met) and the fallback if a gate fails.

8. **Produce the rollout note.** Summarize the chosen config, residual risks, and what to monitor post-deploy (e.g., tail-latency, per-slice accuracy regressions).

**Output Format:**

A markdown plan:
- **Quantization Decision Summary** — table: Decision | Choice | Rationale | Efficiency Gain (est.) | Accuracy Cost (est.) | How Measured
- **PTQ vs QAT Recommendation** — with the cost of the heavier option made explicit
- **Precision Map** — per-layer table: Layer/Group | Precision | Reason
- **Calibration Spec** — sample, scheme, rationale
- **Accuracy-Recovery Ladder** — ordered remedies with expected recovery/cost
- **Measurement & Gate Protocol** — metrics, hardware, pass/fail thresholds
- **Open Questions** — what's needed to finalize (hardware kernels, accuracy budget, etc.)

## Verification

- [ ] Target hardware/runtime and framework/version were requested or used; speedups tied to supported kernels.
- [ ] Every efficiency gain is paired with an accuracy cost and a measurement method.
- [ ] PTQ vs QAT is decided with the QAT cost stated explicitly.
- [ ] A per-layer precision map exists with sensitive layers flagged for higher precision.
- [ ] The validation set, accuracy metric, and efficiency metrics (size, latency, memory) on target hardware are named.
- [ ] Accept/reject gates and a fallback are defined.

## False-Positive Prevention

❌ **DON'T:**
- Report a "4x speedup" from int8 when the target runtime has no int8 GEMM kernel — theoretical FLOP reduction ≠ wall-clock speedup.
- Declare "no accuracy loss" from a tiny or unrepresentative calibration set, or from accuracy measured on the calibration data itself.
- Assume per-tensor symmetric quantization is fine for activations with long-tailed or asymmetric distributions.
- Treat fp16 and bf16 as interchangeable — bf16 trades mantissa for range; the right one depends on the value distribution and hardware.

✅ **DO:**
- Confirm the runtime exposes the chosen low-precision kernel before claiming any latency win; measure wall-clock on the target device.
- Measure accuracy on a held-out set disjoint from calibration data, with confidence intervals when the test set is small.
- Choose per-channel/asymmetric schemes when distributions warrant, and keep known-sensitive layers at higher precision.
- Re-measure size, latency, and memory together — a size win that violates the latency SLA is not a win.

## Example Output

```markdown
## Quantization Plan: Product-Category Classifier (ResNet-50 variant)

### Quantization Decision Summary
| Decision | Choice | Rationale | Efficiency Gain (est.) | Accuracy Cost (est.) | How Measured |
|---|---|---|---|---|---|
| Method | PTQ first, QAT fallback | Retraining feasible but slow; try cheap path | — | — | — |
| Default precision | int8 (per-channel weights) | Target NPU has int8 GEMM | ~3–4x latency, ~4x size (verify) | TBD | held-out top-1 |
| Sensitive layers | fp16: stem conv, final FC, BN folded | First/last layers sensitive | smaller gain | protects accuracy | ablation |

### PTQ vs QAT Recommendation
Start with static int8 PTQ. If top-1 drop > 1.0% (budget), escalate to QAT (~2 GPU-days, needs labeled train subset). Document the drop before paying for QAT.

### Precision Map
| Layer/Group | Precision | Reason |
|---|---|---|
| Stem conv | fp16 | High input sensitivity |
| Body conv blocks | int8 per-channel | Compute-bound, robust |
| Final FC head | fp16 | Logit scale sensitivity |

### Calibration Spec
512 images sampled to match class + brightness distribution; per-channel weight, per-tensor activation, static observers (histogram).

### Accuracy-Recovery Ladder
1. Per-channel weights (in baseline) → recovers most PTQ loss.
2. Raise sensitive layers to fp16 → ~0.3–0.5% recovery, minor latency cost.
3. QAT if still over budget → expected near-fp32 accuracy, highest cost.

### Measurement & Gate Protocol
- Accuracy: top-1 on 10k held-out (disjoint from calibration), 95% CI.
- Efficiency: artifact size; p50/p95 latency at batch=1 and batch=8 on the target NPU; peak RAM.
- Gate: pass if top-1 drop ≤ 1.0% AND p95 ≤ 15 ms at batch=1. Else QAT, else ship fp16.

### Open Questions
- Confirm NPU int8 activation kernel support; confirm accuracy budget (assumed 1.0%).
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** floor → method → precision → calibration → recovery → measurement gate sequence.
- **RT-02 (Multi-Dimensional Analysis Framework):** balances size, latency, memory, and accuracy jointly.
- **QA-12 (False Positives Identification):** guards against theoretical-speedup and no-loss illusions.
- **CM-02 (Constraint Specification):** accuracy budget + hardware kernel support as governing constraints.
- **DS-02 (Metric Specification):** locks the accuracy and efficiency metrics and how they're measured.

**Related Prompts:**
- `mlopt_compression_tradeoff_analysis.md` — compare quantization against pruning/distillation holistically.
- `mlopt_inference_latency_optimization.md` — pursue latency gains beyond precision.
- `mlopt_edge_deployment_optimization.md` — when the target is a memory/power-constrained device.
