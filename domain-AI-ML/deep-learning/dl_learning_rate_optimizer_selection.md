---
title: "Learning Rate & Optimizer Selection"
category: AI-ML/deep-learning
description: "Choose an optimizer and a learning-rate schedule (warmup/decay), run an LR-range test to find a working band, and tune one variable at a time with reproducible runs."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - learning-rate
  - optimizer
  - lr-schedule
  - warmup
  - reproducibility
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/deep-learning/dl_training_not_converging_debug.md
  - domain-AI-ML/deep-learning/dl_regularization_strategy.md
  - domain-AI-ML/deep-learning/dl_mixed_precision_setup.md
---

# Learning Rate & Optimizer Selection

**Objective:** Select an optimizer and a learning-rate schedule appropriate to the architecture, batch size, and training budget; find a working learning-rate band empirically with an LR-range test; and define warmup/decay and a single-variable tuning protocol with fixed seeds so results are attributable and reproducible.

**When to Use:**
- Starting training and unsure which optimizer/LR/schedule to use.
- Training converges but slowly, plateaus, or is unstable, and the bug-vs-tuning question is already settled as tuning.
- After scaling batch size or moving to a new architecture and the old LR no longer works.

**When NOT to Use:**
- Loss is flat at baseline or NaN from a likely bug — triage first with `dl_training_not_converging_debug.md`.
- The problem is overfitting, not optimization (use `dl_regularization_strategy.md`).
- Instability stems from mixed-precision overflow specifically (`dl_mixed_precision_setup.md`).

## Inputs / Context

Provide what you can:
- **Framework & version**, architecture family, model size, and hardware.
- **Batch size** (and whether using gradient accumulation), and total training budget (steps/epochs).
- **Current optimizer/LR/schedule** and the observed behavior (slow, unstable, plateau).
- **Whether the run includes BatchNorm/LayerNorm, residuals, attention** (affects warmup needs).
- **Reproducibility settings** — seed, determinism flags.

## Constraints

**Must:**
- Recommend finding the LR band empirically via an LR-range test rather than guessing a single number.
- Tie the optimizer choice to the architecture (e.g., AdamW common for Transformers; SGD+momentum often strong for CNNs) with a stated rationale, framed as a starting point to verify.
- Scale LR with batch size deliberately and tune one variable at a time on a fixed seed.

**Must Not:**
- Quote a "best" learning rate for the user's model as established fact — LR is data/architecture specific and must be measured.
- Change optimizer, LR, schedule, and batch size all at once.
- Recommend a schedule that conflicts with the early-stopping/regularization plan without noting the interaction.

**Instructions:**

1. **Pick the optimizer family with rationale.** Match optimizer to architecture and history (AdamW/Adam for Transformers and noisy gradients; SGD+momentum with proper LR for many vision CNNs; note Lion/Adafactor as alternatives). State why, and that it is a starting hypothesis to validate.

2. **Run an LR-range test.** Sweep LR from very small to large over a short run, plot loss vs LR, and read off the band where loss falls fastest before diverging. Pick the initial LR from the steepest-descent region, not the minimum.

3. **Set warmup.** For Transformers, large batches, or unnormalized early layers, prescribe a linear warmup over the first small fraction of steps to avoid early divergence; justify when warmup is unnecessary.

4. **Choose a decay schedule.** Match decay (cosine, step, linear, or constant-then-decay) to the training budget and the metric trajectory; specify the end LR and any restarts.

5. **Scale to batch size.** If batch size changed, scale LR (e.g., linear scaling rule as a starting point) and re-verify with a short run; note the regime where linear scaling breaks down.

6. **Define the single-variable tuning protocol.** Vary LR first (largest effect), then schedule, then optimizer hyperparameters, each on a fixed seed with a short comparable run; record the metric that decides.

7. **Lock reproducibility.** Pin the seed and log the full optimizer/schedule config so the chosen setting is repeatable.

**Output Format:**

A markdown report:
- **Optimizer Recommendation** — choice + rationale + alternatives.
- **LR-Range Test Plan** — sweep range, what to plot, how to read the band.
- **Warmup & Decay** — concrete schedule (illustrative numbers) + budget fit.
- **Batch-Size Scaling** — rule applied and re-verify step.
- **Tuning Protocol** — variable order + fixed-seed comparison.
- **Reproducibility Block** — seed + logged config.

## Verification

- [ ] LR is chosen from an empirical range test, not asserted as a fixed best value.
- [ ] Optimizer choice is justified by architecture and framed as a hypothesis to verify.
- [ ] Warmup/decay matches the stated training budget.
- [ ] Batch-size scaling is handled explicitly when batch size changed.
- [ ] Tuning is one-variable-at-a-time on a fixed seed.

## False-Positive Prevention

❌ **DON'T:**
- Hard-code "3e-4 always works" — that's folklore, not a measurement for this model.
- Skip warmup on a large-batch Transformer and then blame instability on the optimizer.
- Sweep LR and schedule and optimizer at once and attribute the win to the wrong knob.
- Pick the LR at the loss minimum of the range test (often already too high) instead of the steepest-descent band.

✅ **DO:**
- Read the working LR band off an LR-range test on this model and data.
- Add warmup where early divergence is likely (large batch, attention, unnormalized starts).
- Scale LR with batch size and re-verify on a short run.
- Tune one variable at a time on a fixed seed and log the config.

## Example Output

```markdown
## LR & Optimizer Plan: ViT-style Classifier, batch 512, 30k steps

### Optimizer Recommendation
AdamW (β1=0.9, β2=0.999, wd=0.05) as the starting hypothesis for an attention model; SGD+momentum kept as a fallback. Validate via short runs.

### LR-Range Test Plan
Sweep LR 1e-6 → 1e-1 over ~500 steps; plot loss vs LR (log x). Pick initial LR from the steepest-descent region — illustratively ~1e-3, below the divergence knee.

### Warmup & Decay
Linear warmup over first ~5% of steps (~1.5k) to peak LR, then cosine decay to ~1e-5. Warmup justified by large batch + attention.

### Batch-Size Scaling
Moving 128→512 (×4): scale LR ~×4 from the small-batch value as a starting point; re-verify with a 1k-step run (linear scaling may break above this batch).

### Tuning Protocol
Vary LR first (seed 0, 2k-step runs) → then decay shape → then β2/wd. Decide on val metric per run.

### Reproducibility Block
Seed 0; log {optimizer, betas, wd, peak_lr, warmup_steps, schedule, batch_size}.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** optimizer → range test → warmup → decay → scaling → tune.
- **RT-02 (Multi-Dimensional Analysis Framework):** weighs optimizer options across architecture fit and stability.
- **DS-02 (Metric Specification):** the LR-range test and per-run decision metric.
- **CM-02 (Constraint Specification):** training budget and batch size bound the schedule.
- **QA-01 (Self-Verification):** checklist enforces empirical, single-variable, reproducible tuning.

**Related Prompts:**
- `dl_training_not_converging_debug.md` — rule out bugs before treating it as a tuning problem.
- `dl_regularization_strategy.md` — schedules interact with early stopping and weight decay.
- `dl_mixed_precision_setup.md` — when instability is a precision/overflow issue.
```