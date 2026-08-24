---
title: "Quantization-Aware Training Plan"
category: AI-ML/model-optimization-efficiency
description: "Plan quantization-aware training when post-training quantization has failed — diagnosing why it failed before adding training cost, matching the QAT setup to the target runtime's actual arithmetic, and validating on task quality per slice rather than on aggregate accuracy."
techniques:
  - RT-10
  - ST-02
  - DS-02
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - quantization-aware-training
  - qat
  - post-training-quantization
  - low-precision
  - edge-deployment
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/model-optimization-efficiency/mlopt_quantization_plan.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_edge_deployment_optimization.md
  - domain-AI-ML/model-optimization-efficiency/mlopt_compression_tradeoff_analysis.md
  - domain-AI-ML/model-evaluation-validation/mleval_error_analysis_slicing.md
---

# Quantization-Aware Training Plan

**Objective:** Decide whether quantization-aware training is warranted and design it if so — diagnosing *why* post-training quantization failed before paying for retraining, matching the simulated arithmetic to what the target runtime actually does, and validating on per-slice task quality rather than an aggregate number.

**When to Use:**
- Post-training quantization has been tried and lost more accuracy than the deployment can absorb.
- A target precision is mandated by hardware and PTQ cannot reach acceptable quality there.
- A model is trained regularly anyway, so the marginal cost of quantization-aware training is small.

**When NOT to Use:**
- PTQ has not been attempted or properly tuned — try `mlopt_quantization_plan.md` first; it is far cheaper and frequently sufficient.
- The constraint is latency rather than memory, and the runtime does not accelerate the target precision — quantizing buys size, not speed, unless the kernels exist.
- The model will not be retrained and no training pipeline is available.

## Inputs / Context

- **PTQ results** — accuracy by precision and by slice, plus which layers degraded, since the failure pattern determines the approach.
- **Target precision and format** — bit width, symmetric or asymmetric, per-tensor or per-channel, and whether activations are also quantized.
- **Target runtime** — the specific inference engine and hardware, and which operations it actually executes at the target precision.
- **Quality bar** — the acceptable loss, on the task metric that matters, per slice.
- **Training pipeline availability** — data, compute, and schedule.
- **Deployment constraint** — memory, latency, energy, or a hardware mandate.

## Constraints

**Must:**
- Diagnose the PTQ failure before designing QAT — outlier activations, per-tensor scaling on a layer needing per-channel, a sensitive first or last layer, or a distribution the calibration set never covered. QAT applied without the diagnosis often fixes something that a better PTQ configuration would have fixed for free.
- Match the simulated quantization to the **target runtime's actual arithmetic**: the same bit widths, rounding, granularity, and the same set of operations quantized. A QAT model validated against a simulation the runtime does not implement will regress on device.
- Validate on **task quality per slice**, not aggregate accuracy — quantization damage concentrates in rare classes and unusual inputs.
- Confirm the target runtime provides accelerated kernels for the chosen precision before claiming a latency benefit.
- Compare against a better-tuned PTQ baseline, not the first PTQ attempt, so the added cost is justified against the real alternative.

**Must Not:**
- Assert accuracy-loss figures, bit-width recommendations, or method comparisons from memory; mark quantities `[measure on your model]`.
- Quantize the first and last layers to the same precision as the rest without checking sensitivity; they are commonly the most sensitive and are often best left at higher precision.
- Validate on a calibration or training slice; quantization sensitivity shows on data the calibration never saw.
- Claim a speedup from reduced precision where the runtime dequantizes and computes at higher precision anyway — that yields memory savings only.
- Report only top-line accuracy when the deployment cares about a rare class.

**Instructions:**

1. **Diagnose the PTQ failure.** Per-layer sensitivity analysis: which layers lose the most when quantized alone. Then identify the mechanism — activation outliers, inadequate scaling granularity, a calibration set that missed part of the distribution, or genuinely narrow dynamic range.

2. **Exhaust the cheaper fixes first.** Per-channel instead of per-tensor scaling; a better and more representative calibration set; keeping identified sensitive layers at higher precision; smoothing or clipping outlier activations. Re-run PTQ after these. **If this recovers the quality, stop — QAT is not needed**, and this step regularly ends the project favourably.

3. **Confirm the runtime story.** Which operations does the target engine genuinely execute at the target precision, and are accelerated kernels present? If the runtime dequantizes to compute, the benefit is memory and bandwidth, not latency, and the plan should say so rather than implying a speedup.

4. **Design the QAT setup to mirror the runtime.** Fake-quantization inserted at the same points the runtime quantizes; matching granularity, symmetry, and rounding; the same operations left in higher precision. Any divergence here is a gap that appears as an unexplained on-device regression.

5. **Choose the training approach.** Fine-tune from the trained checkpoint with quantization simulation — usually sufficient and much cheaper — or train from scratch with it, which is rarely justified. State the schedule, learning rate treatment, and how long simulation is active.

6. **Handle the mixed-precision decision.** Which layers stay at higher precision, based on the sensitivity analysis. Record the resulting model size and confirm it still meets the deployment constraint, since exceptions erode the saving.

7. **Validate against the tuned PTQ baseline, per slice.** Table of task metric by slice for: original, tuned PTQ, and QAT. The comparison against a *tuned* PTQ baseline is what shows whether the training cost bought anything.

8. **Verify on the actual device.** Run the exported model on target hardware and compare against the simulation. A gap here means the simulation did not match the runtime, and the numbers from step 7 do not describe what will ship.

9. **State the trade.** Size, latency (only if kernels exist), energy, and quality per slice, against the deployment constraint that motivated the work.

**Output Format:**

A markdown plan:
- **PTQ Failure Diagnosis** — per-layer sensitivity and the identified mechanism.
- **Cheaper Fixes Attempted** — table: Fix | Effect | Sufficient?
- **Runtime Confirmation** — operations at target precision, kernel availability, benefit type.
- **QAT Configuration** — simulation points, granularity, symmetry, ops kept in higher precision.
- **Training Approach** — fine-tune or from scratch, schedule.
- **Mixed-Precision Exceptions** — layers and resulting size.
- **Validation** — table: Slice | Original | Tuned PTQ | QAT.
- **On-Device Verification** — simulation vs device.
- **Trade Summary** — size, latency, energy, quality vs the constraint.

## Verification

- [ ] PTQ failure is diagnosed per layer with an identified mechanism.
- [ ] Cheaper PTQ fixes are attempted and their effect recorded before QAT is chosen.
- [ ] Runtime support for the target precision is confirmed, and the benefit type stated.
- [ ] The QAT simulation matches the runtime's arithmetic in granularity, symmetry, and op coverage.
- [ ] Mixed-precision exceptions are justified by sensitivity and the size impact is stated.
- [ ] Validation compares against a **tuned** PTQ baseline, per slice.
- [ ] On-device results are compared against simulation.
- [ ] The trade is stated against the original deployment constraint.
- [ ] No accuracy-loss or bit-width figures are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Jump to QAT after one failed PTQ attempt — per-channel scaling and a better calibration set fix a large share of PTQ failures for a fraction of the cost.
- Simulate quantization differently from the runtime and trust the validation numbers; the on-device regression that follows will look mysterious and will not be.
- Claim a latency improvement when the runtime lacks accelerated kernels for the precision — you have bought memory, which is worth saying accurately.
- Report aggregate accuracy when the deployment depends on a rare class; quantization damage concentrates exactly there.
- Quantize first and last layers uniformly without a sensitivity check; they are frequently the sensitive ones.
- Compare QAT against an untuned PTQ baseline — that comparison flatters QAT and hides that tuning alone might have sufficed.

✅ **DO:**
- Diagnose which layers fail and why before adding training cost.
- Exhaust per-channel scaling, calibration improvements, and sensitive-layer exceptions first, and be willing to stop there.
- Confirm what the runtime executes at the target precision and state whether the win is size or speed.
- Mirror the runtime exactly in the simulation, including which ops stay high-precision.
- Validate per slice against a tuned PTQ baseline, and verify on the real device.
- Report the trade against the constraint that started the work.

## Example Output

```markdown
## QAT Plan: On-Device Keyword Spotting (int8 target)
Model must fit a microcontroller budget; int8 is mandated by the runtime.

### PTQ Failure Diagnosis
Naive per-tensor int8 PTQ loses more accuracy than the 1-point budget allows.
Per-layer sensitivity (quantize one layer at a time, measure):
| Layer | Accuracy drop alone | Note |
|---|---|---|
| Input conv | `[measure — expect high]` | wide input dynamic range |
| Depthwise convs | `[measure — expect high]` | **per-channel range varies widely** |
| Pointwise convs | `[measure]` | — |
| Final classifier | `[measure — expect high]` | small logit separations |

**Mechanism:** depthwise convolutions have very different per-channel ranges, so a single
per-tensor scale is a poor fit for all channels at once. This is a scaling-granularity problem,
not evidence that the model cannot be quantized.

### Cheaper Fixes Attempted — before any training cost
| Fix | Effect | Sufficient? |
|---|---|---|
| Per-channel scaling on depthwise convs | `[measure — expect large recovery]` | `[assess]` |
| Calibration set widened to include noisy far-field audio | `[measure]` | `[assess]` |
| Keep input conv and final classifier at higher precision | `[measure]` | `[assess]` |

**If these three recover quality inside the 1-point budget, stop here.** QAT costs a training
cycle and pipeline complexity that a scaling-granularity fix does not, and the diagnosis says
granularity is the actual problem.

### Runtime Confirmation
Target engine executes int8 convolutions with accelerated kernels; **softmax and the final
dense layer are executed at higher precision** by that runtime regardless of what we request.
Benefit: memory **and** latency for the convolutional body; memory only for the tail. Quantizing
the final layer in simulation while the runtime does not would produce a validated model that
does not describe the deployed one.

### QAT Configuration
Fake quantization inserted **only where the runtime quantizes**: int8 per-channel weights on
convs, int8 per-tensor activations, final dense and softmax left in higher precision. Rounding
mode matched to the runtime's. Any mismatch here is the usual cause of an on-device gap.

### Training Approach
Fine-tune from the trained float checkpoint with simulation active — not from scratch. Reduced
learning rate, simulation active for the whole fine-tune, batch-norm statistics frozen after an
initial phase so they are not chasing the quantization noise.

### Mixed-Precision Exceptions
Input conv and final classifier at higher precision, justified by the sensitivity table.
Resulting model size `[compute]` — **must be re-checked against the microcontroller budget**,
because exceptions erode the saving that motivated quantization in the first place.

### Validation
| Slice | Original | Tuned PTQ | QAT |
|---|---|---|---|
| Overall | `[measure]` | `[measure]` | `[measure]` |
| Quiet environment | `[measure]` | `[measure]` | `[measure]` |
| **Far-field / noisy** | `[measure]` | `[measure]` | `[measure]` |
| **Accented speech** | `[measure]` | `[measure]` | `[measure]` |
| False-accept rate | `[measure]` | `[measure]` | `[measure]` |

The two watch slices are the ones where quantization damage concentrates and where an overall
number would conceal it. False-accept rate is tracked separately because a rise there is a
product failure even if accuracy holds.

### On-Device Verification
Export and run on target hardware; compare per-slice against simulation. **Any gap means the
simulation did not match the runtime** — most likely an operation the runtime handles at a
different precision than assumed — and the validation table must be regenerated after fixing it
rather than explained away.

### Trade Summary
| Dimension | Float | QAT int8 | Constraint |
|---|---|---|---|
| Model size | `[measure]` | `[measure]` | must fit MCU flash |
| Inference latency | `[measure]` | `[measure]` | within wake-word budget |
| Energy per inference | `[measure]` | `[measure]` | battery life target |
| Worst-slice accuracy | `[measure]` | `[measure]` | ≤1 pt loss |
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** the PTQ failure mechanism routes to the cheaper fix or to QAT.
- **ST-02 (Structured Sequential Instructions):** diagnosis and cheaper fixes precede training cost, so QAT is adopted only against a demonstrated need.
- **DS-02 (Metric Specification):** per-slice task quality is the defined acceptance measure, with false-accept tracked separately.
- **CM-02 (Constraint Specification):** the match-the-runtime rule and tuned-baseline comparison bound what may be claimed.
- **QA-12 (False Positives Identification):** rejects aggregate accuracy as sufficient and simulation-only validation as complete.

**Related Prompts:**
- `mlopt_quantization_plan.md` — post-training quantization, which must be exhausted first.
- `mlopt_edge_deployment_optimization.md` — the wider on-device deployment picture.
- `mlopt_compression_tradeoff_analysis.md` — comparing quantization against pruning and distillation.
- `../model-evaluation-validation/mleval_error_analysis_slicing.md` — constructing the slices this validation depends on.
