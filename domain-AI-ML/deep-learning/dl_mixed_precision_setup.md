---
title: "Mixed-Precision Training Setup"
category: AI-ML/deep-learning
description: "Enable AMP/fp16/bf16 safely: choose the dtype, configure loss scaling, keep numerically sensitive ops in fp32, and verify parity and stability against an fp32 reference."
techniques:
  - ST-02
  - CM-02
  - QA-01
  - RT-09
  - DS-02
difficulty: advanced
tags:
  - mixed-precision
  - amp
  - bf16
  - loss-scaling
  - numerical-stability
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/deep-learning/dl_gradient_issue_debug.md
  - domain-AI-ML/deep-learning/dl_distributed_training_plan.md
  - domain-AI-ML/deep-learning/dl_training_not_converging_debug.md
---

# Mixed-Precision Training Setup

**Objective:** Enable mixed-precision training (fp16 with loss scaling, or bf16) to gain speed and memory headroom *without* introducing NaNs, underflow, or accuracy loss — by choosing the right dtype for the hardware, configuring loss scaling, keeping numerically sensitive operations in fp32, and verifying parity and stability against an fp32 reference run.

**When to Use:**
- You want faster training / more memory headroom on hardware with fast reduced-precision support.
- A model trains in fp32 but you need to fit a larger batch or model.
- Mixed precision is already on and you're seeing NaNs/instability and need a safe configuration.

**When NOT to Use:**
- Training is broken in fp32 first — fix that with `dl_training_not_converging_debug.md` before adding precision complexity.
- The instability is a general gradient problem unrelated to precision (`dl_gradient_issue_debug.md`).
- Hardware lacks reduced-precision acceleration (little to gain, more risk).

## Inputs / Context

Provide what you can:
- **Framework & version** and its AMP/autocast API; **hardware** and which low-precision formats it accelerates (fp16, bf16).
- **Current fp32 behavior** — does it train stably? final metric and loss curve.
- **Model details** — presence of softmax, layer/batch norm, large reductions, custom ops, exponentials/logs.
- **Symptom if debugging** — NaN/inf timing, gradient overflow warnings, accuracy drop vs fp32.
- **Seeds/determinism** for the parity comparison.

## Constraints

**Must:**
- Choose fp16 vs bf16 by hardware support and dynamic range needs (bf16 has wider range, no loss scaling needed; fp16 needs loss scaling).
- Keep reductions, normalization statistics, softmax/cross-entropy, and accumulation in fp32 (mixed, not pure low-precision).
- Verify against an fp32 reference: loss curve parity within tolerance and equal-or-better final metric.

**Must Not:**
- Cast the entire model and loss to fp16 without loss scaling and without fp32-safe ops.
- Quote an exact speedup/memory-savings number as fact — frame as to-be-measured on the user's hardware.
- Disable loss scaling for fp16 to "simplify," then blame the optimizer for NaNs.

**Instructions:**

1. **Confirm the fp32 baseline.** Ensure the model trains stably in fp32 and record its loss curve and final metric as the reference; mixed precision must match or beat it.

2. **Choose the dtype.** If the hardware accelerates bf16, prefer it (wide range, typically no loss scaling). If only fp16 is fast, plan dynamic loss scaling. State the rationale.

3. **Apply autocast with fp32-safe regions.** Wrap the forward/loss in autocast but keep softmax/cross-entropy, normalization statistics, large reductions, and exponential/log ops in fp32.

4. **Configure loss scaling (fp16).** Use dynamic loss scaling: scale the loss before backward, unscale before the optimizer step and gradient clipping, and skip steps on inf/NaN gradients. Specify initial scale and growth behavior.

5. **Order clipping/unscale correctly.** Unscale gradients before clipping and before any norm-based logging so thresholds apply in true scale.

6. **Diagnose precision-specific failures.** If NaNs appear: check for fp16 overflow in a hot op (move to fp32), underflow (raise loss scale), or a custom op that doesn't support autocast. Map symptom → cause → fix.

7. **Verify parity and stability.** Run a short fixed-seed comparison vs fp32: loss curves should track within tolerance, no recurring overflow skips, and final metric within noise. Then measure (don't assume) speed/memory gains.

**Output Format:**

A markdown report:
- **fp32 Reference** — stability + metric to match.
- **Dtype Choice** — fp16 vs bf16 + rationale.
- **Autocast & fp32-Safe Ops** — what stays fp32 and why.
- **Loss-Scaling Config** (fp16) — scale init/growth, unscale/clip order.
- **Precision-Failure Triage** — symptom → cause → fix table.
- **Parity & Gains Verification** — comparison plan + what to measure.

## Verification

- [ ] An fp32 reference (curve + metric) is recorded to compare against.
- [ ] Dtype choice matches hardware support and dynamic-range needs.
- [ ] Numerically sensitive ops are kept in fp32.
- [ ] Loss scaling (for fp16) is configured with correct unscale-before-clip ordering.
- [ ] Parity is verified before any speed/memory gains are claimed (and gains are measured).

## False-Positive Prevention

❌ **DON'T:**
- Run fp16 without loss scaling and conclude the model "can't train in mixed precision."
- Keep softmax/cross-entropy or norm statistics in fp16 and chase the resulting NaNs elsewhere.
- Clip gradients before unscaling — the threshold then applies in scaled space.
- Claim a 2× speedup without measuring it on the actual hardware.

✅ **DO:**
- Establish an fp32 reference and require mixed precision to match or beat it.
- Prefer bf16 where supported; use dynamic loss scaling for fp16.
- Keep reductions, normalization stats, and exp/log/softmax in fp32.
- Verify loss-curve parity and only then measure speed/memory gains.

## Example Output

```markdown
## Mixed-Precision Setup: Transformer Encoder on Ampere-class GPUs

### fp32 Reference
Stable; val metric M and smooth loss curve recorded as the target to match.

### Dtype Choice
bf16 (hardware-accelerated, wide range) → no loss scaling required; simpler and stable.

### Autocast & fp32-Safe Ops
Autocast forward/loss in bf16; keep softmax + cross-entropy and LayerNorm statistics in fp32 reductions.

### Loss-Scaling Config
N/A for bf16. (If forced to fp16: dynamic scaling, init 2^16, unscale before clip, skip on inf/NaN.)

### Precision-Failure Triage
| Symptom | Likely Cause | Fix |
|---|---|---|
| NaN after few steps | overflow in attention scores | compute scores in fp32 |
| Slow loss + skipped steps (fp16) | underflow / scale too low | raise loss scale |
| NaN only with custom op | op unsupported by autocast | force fp32 region |

### Parity & Gains Verification
Seed 0, 2k steps: bf16 loss tracks fp32 within tolerance, final metric within noise. Then measure tokens/sec and peak memory vs fp32 — don't assume.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** baseline → dtype → autocast → scaling → verify.
- **CM-02 (Constraint Specification):** hardware support and fp32-safe-op rules constrain the setup.
- **QA-01 (Self-Verification):** parity-before-gains discipline in the checklist.
- **RT-09 (Root Cause Explanation):** the precision-failure triage maps NaN symptoms to causes.
- **DS-02 (Metric Specification):** loss-curve parity and measured gains define success.

**Related Prompts:**
- `dl_gradient_issue_debug.md` — when NaNs are a general gradient issue, not precision-specific.
- `dl_distributed_training_plan.md` — mixed precision pairs with parallelism for memory headroom.
- `dl_training_not_converging_debug.md` — fix fp32 training before adding mixed precision.
```