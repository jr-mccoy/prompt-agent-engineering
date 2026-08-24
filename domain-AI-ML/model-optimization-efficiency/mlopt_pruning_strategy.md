---
title: "ML Pruning Strategy (Structured vs Unstructured)"
category: AI-ML/model-optimization-efficiency
description: "Design a pruning strategy — structured vs unstructured, schedule, sparsity targets, and fine-tune recovery — that measures real wall-clock speedup on the target runtime, not just nominal sparsity, and pairs each gain with its accuracy cost."
techniques:
  - ST-02
  - RT-02
  - QA-12
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - pruning
  - structured-sparsity
  - unstructured-sparsity
  - model-compression
  - fine-tuning-recovery
  - inference-efficiency
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/model-optimization-efficiency/mlopt_compression_tradeoff_analysis.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_quantization_plan.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_inference_latency_optimization.md
---

# ML Pruning Strategy (Structured vs Unstructured)

**Objective:** Produce a pruning plan for a trained model — choosing structured vs unstructured pruning, sparsity targets, a one-shot vs iterative schedule, and a fine-tune recovery loop — that reports **real measured speedup on the target runtime** (not nominal sparsity) and pairs every efficiency gain with its accuracy cost.

**When to Use:**
- You need a smaller or faster model and want to remove redundant weights/structures.
- You must decide whether unstructured sparsity is worth it given your runtime (most runtimes do not accelerate unstructured sparsity).
- You want a defensible pruning schedule with accuracy recovery rather than ad-hoc weight zeroing.

**When NOT to Use:**
- Quantization alone may meet the budget more reliably (use `mlopt_quantization_plan.md`).
- You want to weigh pruning against distillation/quantization across all axes (use `mlopt_compression_tradeoff_analysis.md`).
- The model underfits — pruning makes that worse.

## Inputs / Context

Provide what you can:
- **Target hardware + runtime** — the accelerator and inference runtime, and crucially whether it can *accelerate* sparsity (e.g., 2:4 structured sparse kernels, channel-pruned dense execution). *Ask the user if unspecified — unstructured sparsity rarely speeds up dense hardware.*
- **Framework + version** — for the pruning toolkit and export path.
- **Model architecture** — layers, parameter distribution, where most compute/params live.
- **Accuracy budget** — metric, current score, max acceptable drop.
- **Fine-tune feasibility** — data + compute available for recovery training.
- **Goal** — is the win size, memory, or wall-clock latency? (These diverge for unstructured pruning.)

## Constraints

**Must:**
- Ask for target hardware + runtime and framework + version; distinguish nominal sparsity from runtime-realizable speedup.
- Pair every gain (params removed, size, latency) with its accuracy cost and how to measure it on a held-out set.
- State whether the chosen pruning type yields real latency wins on the named runtime, or only size/memory wins.

**Must Not:**
- Equate "80% sparse" with "5x faster" — report the actual mechanism by which (or whether) the runtime realizes speed.
- Quote specific speedup/accuracy numbers as measured — mark figures as estimates to verify on the user's hardware.
- Recommend aggressive one-shot pruning without a fine-tune recovery plan when accuracy matters.

**Instructions:**

1. **Establish the win definition and the budget.** Clarify whether the target is size, memory, or wall-clock latency, restate the accuracy budget, and note what the runtime can accelerate. This governs structured vs unstructured.

2. **Choose structured vs unstructured.** Recommend structured (channel/filter/head/block, or 2:4 if hardware-supported) when latency is the goal on dense hardware; unstructured only when the runtime has true sparse kernels or the goal is purely size/memory. Justify against the runtime.

3. **Pick the saliency criterion.** Choose how importance is scored (magnitude, L1/L2 of structures, Taylor/gradient-based) and why it fits the architecture.

4. **Design the schedule.** Prefer iterative/gradual magnitude pruning with fine-tuning between steps over aggressive one-shot when accuracy is tight; specify start/end sparsity, steps, and fine-tune epochs per step.

5. **Define the recovery loop.** Specify the fine-tuning data, LR schedule, and whether to use learning-rate rewinding / lottery-ticket style retraining; state expected recovery per increment.

6. **Specify the measurement protocol.** Require measuring real p50/p95 latency, artifact size, and peak memory on the **target hardware**, plus the accuracy metric on a held-out set — and explicitly compare latency before/after to prove the win is real.

7. **Set accept/reject gates.** Pass = accuracy drop ≤ budget AND the targeted efficiency metric improved by the required margin on the target runtime. Define the fallback (lower sparsity, switch to structured, or abandon pruning for quantization).

8. **Produce the rollout note.** Final config, residual risks (e.g., latency win not realized → revert), and post-deploy monitoring.

**Output Format:**

A markdown plan:
- **Pruning Decision Summary** — table: Decision | Choice | Rationale | Efficiency Gain (est.) | Accuracy Cost (est.) | How Measured
- **Structured vs Unstructured Recommendation** — with the runtime realizability call-out
- **Saliency & Schedule** — criterion, start/end sparsity, steps, fine-tune per step
- **Recovery Loop Spec** — data, LR, epochs, expected recovery
- **Measurement & Gate Protocol** — latency/size/memory on target hardware + accuracy metric
- **Open Questions** — runtime sparse-kernel support, budget, fine-tune resources

## Verification

- [ ] Target hardware/runtime and framework/version requested or used; sparsity-vs-speedup distinction made explicit.
- [ ] Structured vs unstructured chosen against the runtime's actual acceleration capability.
- [ ] Every efficiency gain paired with accuracy cost and a measurement method.
- [ ] A fine-tune recovery loop is specified (or justified as unnecessary).
- [ ] Real wall-clock latency on target hardware is in the measurement protocol, not just sparsity %.
- [ ] Accept/reject gates and a fallback exist.

## False-Positive Prevention

❌ **DON'T:**
- Report sparsity percentage as if it were a speedup — 90% unstructured sparsity often runs at the same speed on a dense GPU.
- Assume 2:4 / N:M structured sparsity gives speedup without confirming the runtime + hardware support its kernels.
- Prune to a high sparsity in one shot and report accuracy before fine-tuning (the recoverable drop looks catastrophic).
- Measure latency at a batch size that masks the effect (e.g., memory-bound batch=1 when the model is compute-bound at batch=32).

✅ **DO:**
- Verify the runtime actually executes the pruned structure faster; measure before/after wall-clock on the target hardware.
- Prefer structured pruning when latency on dense hardware is the goal; reserve unstructured for sparse-kernel runtimes or size-only goals.
- Always report post-fine-tune accuracy as the headline, with the pre-recovery drop noted separately.
- Compare against the quantization alternative — pruning is not always the cheapest path to the same budget.

## Example Output

```markdown
## Pruning Strategy: BERT-base Intent Classifier

### Pruning Decision Summary
| Decision | Choice | Rationale | Efficiency Gain (est.) | Accuracy Cost (est.) | How Measured |
|---|---|---|---|---|---|
| Type | Structured (attention head + FFN channel) | GPU has no sparse kernels; need real latency | ~1.6–2x latency (verify) | TBD | F1 on held-out |
| Sparsity target | 40% heads, 30% FFN | Beyond this, recovery cost rises sharply | size ~35% smaller | recoverable | ablation |
| Schedule | Iterative, 4 steps, fine-tune each | One-shot too lossy at this rate | — | minimizes drop | per-step F1 |

### Structured vs Unstructured Recommendation
Unstructured magnitude pruning would zero ~50% of weights but the target A-series GPU runs dense kernels — no latency win, only a misleading sparsity number. Choose structured head/channel pruning so the matrices actually shrink.

### Saliency & Schedule
Importance = L2 norm of head/channel weights + first-order Taylor on a calibration batch. Gradual 0% → 40%/30% over 4 steps, 1 fine-tune epoch (LR 2e-5) per step.

### Recovery Loop Spec
Fine-tune on full train set, cosine LR, 1 epoch/step; expect each step to recover ~0.4–0.8 F1 of the immediate drop.

### Measurement & Gate Protocol
- Latency: p50/p95 at batch=1 and batch=16 on target GPU, before vs after.
- Size + peak memory; accuracy: macro-F1 on held-out, 95% CI.
- Gate: pass if F1 drop ≤ 0.5 AND p95 latency improves ≥ 1.4x at batch=16. Else reduce sparsity or switch to int8 quantization.

### Open Questions
- Confirm no sparse-kernel support; confirm accuracy budget (assumed 0.5 F1).
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** win-definition → type → saliency → schedule → recovery → measurement.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighs size, memory, and real latency against accuracy.
- **QA-12 (False Positives Identification):** central to the sparsity-vs-speedup and pre-recovery-accuracy traps.
- **CM-02 (Constraint Specification):** accuracy budget + runtime acceleration capability as governing constraints.
- **DS-02 (Metric Specification):** fixes the latency/size/accuracy metrics and measurement points.

**Related Prompts:**
- `mlopt_compression_tradeoff_analysis.md` — compare pruning against quantization/distillation.
- `mlopt_quantization_plan.md` — often a more reliable latency win on dense hardware.
- `mlopt_inference_latency_optimization.md` — pursue runtime/kernel-level latency gains.
