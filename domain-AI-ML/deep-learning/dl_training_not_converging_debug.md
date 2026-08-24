---
title: "Training Not Converging — Triage"
category: AI-ML/deep-learning
description: "Decision-tree triage for a model whose loss won't decrease: isolate the cause across data, learning rate, initialization, normalization, and code bugs using cheap discriminating tests."
techniques:
  - RT-10
  - RT-09
  - ST-02
  - QA-13
  - RP-01
difficulty: intermediate
tags:
  - debugging
  - convergence
  - training-loss
  - triage
  - reproducibility
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/deep-learning/dl_gradient_issue_debug.md
  - domain-AI-ML/deep-learning/dl_learning_rate_optimizer_selection.md
  - domain-AI-ML/deep-learning/dl_reproducibility_setup.md
---

# Training Not Converging — Triage

**Objective:** Diagnose why a deep network's training loss is flat, oscillating wildly, or stuck far above what the task allows, by walking a decision tree of cheap discriminating tests that isolate the cause to one of: data/labels, learning rate, initialization, normalization, or a code bug — then prescribe the minimal fix and a confirmation test.

**When to Use:**
- Training loss does not decrease, decreases then plateaus immediately, or diverges to NaN/inf.
- The model performs at chance after many steps.
- You suspect a setup bug but don't know where to look.

**When NOT to Use:**
- Training loss *does* fall but validation loss diverges — that's overfitting (use `dl_overfitting_diagnosis_remedies.md`).
- Loss is fine but gradients spike/vanish specifically — go deeper with `dl_gradient_issue_debug.md`.
- The complaint is throughput/GPU utilization, not learning (use `dl_data_loading_bottleneck_audit.md`).

## Inputs / Context

Provide what you can:
- **Framework & version**, hardware, and whether mixed precision is on.
- **Loss curve description** — flat, oscillating, slowly decreasing, NaN, value at step 0 vs now.
- **Task & loss function** — and the loss value a random/majority baseline would produce.
- **Learning rate, optimizer, batch size, init scheme, normalization layers.**
- **Data pipeline** — normalization, label encoding, shuffling, any recent change.
- **What changed** since it last worked (if it ever did).
- **Seeds / determinism settings** (so the issue is reproducible).

## Constraints

**Must:**
- Run the decision tree in order of cheapest-and-most-discriminating first; each step must rule something in or out.
- Compare the observed loss to the theoretical baseline loss for the task (e.g., `ln(num_classes)` for balanced cross-entropy) to know whether the model has learned *anything*.
- Recommend changing **one variable at a time** and re-checking on a tiny fixed subset.

**Must Not:**
- Recommend a grab-bag of changes at once — that destroys attribution.
- Assume the cause without the discriminating test that confirms it.
- Fabricate that a given loss value "should" be a specific number for the user's data without deriving it from the task definition.

**Instructions:**

1. **Establish the baseline loss and the symptom.** Compute the expected loss at random init for this loss function and compare to step-0 and current loss. Classify the symptom: never-moves / plateaus-instantly / oscillates / diverges-to-NaN.

2. **Overfit a tiny batch (the master test).** Take 2–10 examples and try to drive loss to ~0. If it *can't* overfit a handful of examples, the cause is a code/data/loss bug — not hyperparameters. If it *can*, the architecture and loss path work; suspect LR/regularization/data scale.

3. **Triage by symptom branch:**
   - **Diverges to NaN/inf** → LR too high, missing input normalization, or unstable op (log of 0, mixed-precision overflow). Lower LR 10×; check input ranges; see `dl_mixed_precision_setup.md`.
   - **Loss exactly flat / equals baseline** → no gradient flowing: check `requires_grad`, that the optimizer steps, that the loss connects to outputs, and that labels aren't all one value or shuffled away from inputs.
   - **Oscillates, never settles** → LR too high or batch too small; try LR-range test and a schedule (`dl_learning_rate_optimizer_selection.md`).
   - **Decreases then plateaus high** → LR too low, dead units (bad init/activation), or normalization misconfigured; check init scheme and BatchNorm in train vs eval mode.

4. **Audit the data/label path.** Verify inputs are normalized to the range the architecture expects, labels align with inputs (no off-by-one/shuffle mismatch), classes aren't degenerate, and the loss receives logits-vs-probabilities in the form it expects.

5. **Audit the gradient path.** Confirm gradients are non-zero and finite at a few layers; check for an accidental `no_grad` context, detached tensors, or a frozen-everything state.

6. **Apply the minimal fix and confirm.** Change one thing, re-run the tiny-batch overfit and a short full-data run on a fixed seed, and verify the loss now moves below baseline.

7. **Lock in reproducibility.** Pin the seed and record the working config so the fix is attributable and repeatable.

**Output Format:**

A markdown report:
- **Symptom Classification** — symptom + baseline loss + what it implies
- **Tiny-Batch Overfit Result** — pass/fail and what it rules in/out
- **Decision-Tree Path** — the branch taken and each test's outcome
- **Root Cause** — the confirmed cause with evidence
- **Fix & Confirmation Test** — the single change and how to verify it
- **Open Hypotheses** — if not yet confirmed, the remaining suspects and the next test for each

## Verification

- [ ] The symptom is classified and compared to the theoretical baseline loss.
- [ ] The tiny-batch overfit test was run and its result drives the branch.
- [ ] Only one variable is changed per recommended step.
- [ ] The root cause is supported by a discriminating test, not a guess.
- [ ] A concrete confirmation test (and seed) is specified.

## False-Positive Prevention

❌ **DON'T:**
- Blame the learning rate before confirming gradients actually flow and the model can overfit a tiny batch.
- Call it "converged badly" when the model is still at baseline loss — that means it learned nothing, a different class of bug.
- Stack five fixes at once and declare victory without knowing which mattered.
- Ignore train-vs-eval mode (BatchNorm/Dropout) when loss differs between the two.

✅ **DO:**
- Use the tiny-batch overfit as the first discriminating test — it cleanly separates bugs from tuning.
- Derive the baseline loss from the task so "no learning" is unambiguous.
- Isolate one variable, re-run on a fixed seed, and confirm before moving on.
- Check the data/label alignment path explicitly — silent misalignment looks exactly like "won't learn."

## Example Output

```markdown
## Convergence Triage: Audio Tagging Model (loss flat at ~2.3)

### Symptom Classification
- 10-class balanced cross-entropy → random baseline ≈ ln(10) ≈ 2.30.
- Loss starts at 2.31 and stays at 2.30 for 2k steps → model has learned **nothing**. Symptom: loss-equals-baseline.

### Tiny-Batch Overfit Result
- Tried to overfit 4 fixed clips. Loss does NOT drop below ~2.3 → confirms a code/data/loss bug, not hyperparameters.

### Decision-Tree Path
1. Baseline check → at random loss.
2. Tiny-batch overfit → fails → bug branch.
3. Gradient check → gradients are zero at the first layer.
4. Inspected pipeline → labels were one-hot but loss expected class indices, so the loss-vs-label form was mismatched and produced a constant.

### Root Cause
Label/loss form mismatch: cross-entropy received one-hot targets where indices were expected, yielding a near-constant loss with no usable gradient. Evidence: zero first-layer gradients + inability to overfit 4 examples.

### Fix & Confirmation Test
Pass integer class indices (or switch to the matching loss variant). Single change. Confirm: re-run tiny-batch overfit on seed 0 — loss must fall below 2.3 toward ~0 within a few hundred steps.

### Open Hypotheses
None remaining; cause confirmed by the gradient + overfit evidence.
```

**Techniques Used:**
- **RT-10 (Troubleshooting Decision Tree):** symptom branches drive the diagnosis.
- **RT-09 (Root Cause Explanation):** the cause is named with the test that confirms it.
- **ST-02 (Structured Sequential Instructions):** ordered, cheapest-discriminating-first steps.
- **QA-13 (Failure Recovery Specification):** prescribes the minimal fix plus a confirmation test.
- **RP-01 (Role / Persona Assignment):** frames the responder as a methodical debugging engineer isolating one variable at a time.

**Related Prompts:**
- `dl_gradient_issue_debug.md` — when the gradient path itself is the suspect.
- `dl_learning_rate_optimizer_selection.md` — once the bug is ruled out and it's a tuning problem.
- `dl_reproducibility_setup.md` — pin seeds so the bug and fix are attributable.
