---
title: "Gradient Issue Debug (Vanishing / Exploding / NaN)"
category: AI-ML/deep-learning
description: "Decision-tree triage for vanishing gradients, exploding gradients, and NaNs/infs: localize the bad layer/op, then prescribe clipping, init, normalization, or numerical-stability fixes."
techniques:
  - RT-10
  - RT-09
  - ST-02
  - QA-13
  - DS-02
difficulty: advanced
tags:
  - gradients
  - vanishing-gradient
  - exploding-gradient
  - nan
  - numerical-stability
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/deep-learning/dl_training_not_converging_debug.md
  - domain-AI-ML/deep-learning/dl_mixed_precision_setup.md
  - domain-AI-ML/deep-learning/dl_learning_rate_optimizer_selection.md
---

# Gradient Issue Debug (Vanishing / Exploding / NaN)

**Objective:** Diagnose gradient pathologies — vanishing gradients (deep layers stop learning), exploding gradients (loss spikes), or NaNs/infs — by inspecting per-layer gradient norms to localize the offending layer or operation, then walk a decision tree to the right fix: clipping, initialization, normalization, activation choice, or a numerically stable op.

**When to Use:**
- Loss spikes intermittently then recovers or diverges (exploding).
- Early/deep layers barely update while others train (vanishing).
- NaNs/infs appear in loss or gradients after some steps.

**When NOT to Use:**
- Loss is simply flat at baseline with no gradient flow — that's the broader convergence triage (`dl_training_not_converging_debug.md`).
- NaNs are specifically from fp16 overflow/underflow (`dl_mixed_precision_setup.md`).
- The model trains fine and you only want a better LR schedule (`dl_learning_rate_optimizer_selection.md`).

## Inputs / Context

Provide what you can:
- **Framework & version**, architecture (depth, residuals, normalization, activations), and whether mixed precision is on.
- **Symptom** — vanishing / exploding / NaN, and when in training it appears.
- **Per-layer gradient norms** if available, or whether gradient logging exists.
- **Init scheme, normalization layers, activation functions, LR, clipping** currently set.
- **Any custom ops, exponentials/logs/divisions** in the model or loss.
- **Seeds/determinism** for reproducible localization.

## Constraints

**Must:**
- Localize the problem to a layer/op via gradient-norm inspection before prescribing a fix.
- Distinguish the three pathologies (vanishing / exploding / NaN) — each has a different fix branch.
- Recommend one change at a time with a fixed-seed confirmation, comparing gradient norms before/after.

**Must Not:**
- Reach straight for gradient clipping as a blanket cure without identifying whether the issue is exploding vs vanishing vs NaN.
- Quote a specific "healthy gradient norm" value as universal — judge by relative per-layer magnitudes and trends.
- Assume the architecture is at fault when a single unstable op (log of 0, division) produces the NaN.

**Instructions:**

1. **Instrument per-layer gradient norms.** Add logging of gradient norms per layer/block (and loss/activation stats). This is the discriminating measurement that localizes the issue.

2. **Classify the pathology.** Spiking norms / loss → exploding. Norms shrinking toward zero in deep/early layers → vanishing. inf/NaN in a specific layer's gradient or activation → numerical instability.

3. **Vanishing branch.** Check init (use variance-preserving init for the activation), add/repair residual connections and normalization, prefer non-saturating activations; verify deep-layer norms rise after the change.

4. **Exploding branch.** Apply gradient clipping (by global norm) as a stabilizer, lower the LR, verify normalization placement, and check for a too-large init; confirm norm spikes disappear.

5. **NaN/inf branch.** Bisect to the first NaN-producing op: guard log/sqrt/division with epsilons, use numerically stable loss formulations (log-sum-exp, logits-based cross-entropy), check for overflow (and mixed precision via `dl_mixed_precision_setup.md`), and detect bad inputs (NaN/inf in data).

6. **Cross-check the data and loss path.** Confirm inputs are finite and normalized and that the loss receives values in the expected form — bad data is a common NaN source masquerading as a model bug.

7. **Apply one fix and confirm.** Change a single thing, re-run on a fixed seed, and verify via the per-layer gradient norms that the pathology is resolved without creating a new one.

**Output Format:**

A markdown report:
- **Pathology Classification** — vanishing / exploding / NaN + evidence (norms).
- **Localization** — the layer/op implicated.
- **Decision-Tree Path** — branch taken + each check's result.
- **Root Cause** — with the gradient-norm/op evidence.
- **Fix & Confirmation** — single change + before/after norm check + seed.
- **Open Hypotheses** — if unconfirmed, remaining suspects + next probe.

## Verification

- [ ] Per-layer gradient norms (or a plan to log them) localize the issue.
- [ ] The pathology is classified into the correct branch before a fix is chosen.
- [ ] The fix matches the branch (not blanket clipping for everything).
- [ ] One change at a time with a fixed-seed before/after norm comparison.
- [ ] Data/loss-path NaN sources were checked, not just the architecture.

## False-Positive Prevention

❌ **DON'T:**
- Slap on gradient clipping for a vanishing-gradient problem — it won't help and masks the real cause.
- Call shrinking norms "exploding" or vice versa without looking at the per-layer trend.
- Assume a deep-architecture fault when one unguarded log/division produces the NaN.
- Ignore NaN/inf values in the input data while debugging the model.

✅ **DO:**
- Log per-layer gradient norms to localize before fixing.
- Fix by branch: init/residual/norm for vanishing; clip/LR/norm-placement for exploding; epsilon/stable-op for NaN.
- Bisect to the first NaN-producing op rather than guessing.
- Change one thing and confirm with before/after gradient norms on a fixed seed.

## Example Output

```markdown
## Gradient Debug: 40-Layer Net, Loss Spikes to inf at ~step 600

### Pathology Classification
Global grad norm spikes 100×+ before the inf; per-layer norms show the spike originates in mid-block attention. Symptom: exploding → NaN.

### Localization
Attention block 18 produces the first inf in its gradient; activation stats show large pre-softmax scores.

### Decision-Tree Path
1. Per-layer norms logged. 2. Spike localized to block 18. 3. Exploding branch: clip + inspect attention scaling. 4. Found missing score scaling causing huge logits.

### Root Cause
Unscaled attention scores → exploding pre-softmax magnitudes → gradient blow-up to inf. Evidence: localized spike + oversized score stats.

### Fix & Confirmation
Add the proper attention score scaling (single change) and global-norm gradient clipping as a guard. Seed 0: per-layer norms stay bounded, no inf through 5k steps.

### Open Hypotheses
None; resolved. Clipping retained as a safety net.
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** vanishing/exploding/NaN branches drive the fix.
- **RT-09 (Root Cause Explanation):** the cause is localized to a layer/op with norm evidence.
- **ST-02 (Structured Sequential Instructions):** instrument → classify → branch → confirm.
- **QA-13 (Failure Recovery Specification):** minimal fix plus a before/after confirmation.
- **DS-02 (Metric Specification):** per-layer gradient norms are the diagnostic metric.

**Related Prompts:**
- `dl_training_not_converging_debug.md` — when there's no gradient flow at all, not a pathology.
- `dl_mixed_precision_setup.md` — when NaNs trace to fp16 overflow/underflow.
- `dl_learning_rate_optimizer_selection.md` — lower/scheduled LR as part of the exploding-gradient fix.
```