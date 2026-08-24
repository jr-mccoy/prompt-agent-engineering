---
title: "ML Data Augmentation Plan"
category: AI-ML/data-for-ml
description: "Design modality-appropriate augmentation (image, text, audio, tabular, time-series) that expands coverage and improves robustness without distorting the target distribution or corrupting labels."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DT-04
  - QA-12
difficulty: intermediate
tags:
  - data-augmentation
  - robustness
  - invariance
  - label-preservation
  - coverage
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/data-for-ml/mldata_class_imbalance_strategy.md
  - domain-AI-ML/data-for-ml/mldata_synthetic_data_strategy.md
  - domain-AI-ML/data-for-ml/mldata_train_test_split_strategy.md
---

# ML Data Augmentation Plan

**Objective:** Design an augmentation strategy appropriate to the data modality that expands coverage of conditions the model will face in deployment and improves robustness — while guaranteeing that each transform preserves the label and does not push the training distribution away from the real deployment distribution.

**When to Use:**
- Training data is limited or under-covers conditions seen in production (lighting, phrasing, noise, sensor variation).
- The model is brittle to nuisance variation it should be invariant to.
- A minority class needs more *realistic* variety (paired with an imbalance strategy).

**When NOT to Use:**
- You need entirely new records, not transformed copies (use `mldata_synthetic_data_strategy.md`).
- The fix is rebalancing/weighting, not coverage (use `mldata_class_imbalance_strategy.md`).

## Inputs / Context

Provide what you can; the plan degrades gracefully if some are missing:
- **Modality & task** — image/text/audio/tabular/time-series; classification/detection/regression/etc.
- **Invariances required** — what variation the model *should* ignore (rotation, paraphrase, background noise) vs. variation that changes the label.
- **Deployment conditions** — the real-world variation to cover; known coverage gaps.
- **Label semantics** — which transforms could silently change the correct label.
- **Volume & class distribution** — where augmentation is most needed.
- **Constraints** — compute budget, online vs offline augmentation, framework + version.

## Constraints

**Must:**
- Justify each transform by an invariance the model genuinely needs, mapped to a real deployment condition.
- Guarantee label preservation per transform; for any transform that can alter the label, specify the bound or exclude it.
- Apply augmentation to training folds only and never to validation/test, so metrics measure real-distribution performance.

**Must Not:**
- Recommend transforms that distort the target distribution (e.g., augmenting one class far more, creating implausible inputs the model will never see).
- Invent that a transform is label-preserving for the user's task without reasoning about the label semantics.
- Assume more augmentation is always better — over-augmentation can teach unrealistic invariances and hurt accuracy.

**Instructions:**

1. **Map required invariances to deployment conditions.** List the nuisance variation the model must tolerate in production and the variation that legitimately changes the label — only the former is augmentable.

2. **Select modality-appropriate transforms.** Propose transforms suited to the modality (e.g., image: flips/crops/color jitter; text: paraphrase/back-translation/synonym; audio: noise/time-stretch; tabular: jitter/mixup with care; time-series: warping/window shifts), each tied to an invariance.

3. **Check label preservation per transform.** For each transform, verify it cannot change the correct label (e.g., horizontal flip breaks digit "6"/"9" or left/right-dependent tasks); set parameter bounds or drop unsafe transforms.

4. **Guard the target distribution.** Set per-class/per-segment augmentation budgets so augmentation expands coverage without skewing base rates or over-representing transformed regions; keep inputs plausible.

5. **Decide online vs offline and intensity.** Choose where augmentation runs (on-the-fly vs pre-generated), the per-epoch probability/magnitude, and a schedule, balanced against compute and overfitting.

6. **Place it leak-safely.** Confirm augmentation touches training folds only; validation/test stay raw. Cross-link the split strategy.

7. **Specify validation of the augmentation itself.** Define an A/B (with vs without) on a clean holdout and per-slice checks, so the plan is judged by real-distribution gains, not training-loss curves.

8. **Note risks and stop conditions.** Identify transforms most likely to introduce artifacts or unrealistic invariances, and the signal that says "augmenting more is now hurting."

**Output Format:**

A markdown plan:
- **Invariance Map** — augmentable nuisance variation vs label-changing variation.
- **Transform Plan** — table: Transform | Invariance/condition | Label-safe? (+bounds) | Intensity.
- **Distribution Guardrails** — per-class/segment budgets; plausibility checks.
- **Execution** — online/offline, schedule, compute.
- **Leak-Safe Placement** — train-only confirmation.
- **Validation Plan** — with/without A/B + per-slice checks.
- **Risks & Stop Conditions** — artifact-prone transforms; over-augmentation signal.

## Verification

- [ ] Every transform is tied to an invariance mapped to a real deployment condition.
- [ ] Label preservation is reasoned per transform, with bounds or exclusions for risky ones.
- [ ] Per-class/segment budgets prevent distribution distortion.
- [ ] Augmentation is confined to training folds; validation/test remain raw.
- [ ] The plan is validated by a with/without comparison on a clean holdout, per slice.

## False-Positive Prevention

❌ **DON'T:**
- Apply a transform that silently flips the label (horizontal flip on "6/9", text negation, mirroring a left/right medical view).
- Augment the minority class so heavily that the training distribution no longer resembles deployment.
- Augment the validation/test set — you'll measure performance on data that doesn't exist in production.
- Crank augmentation magnitude until inputs become implausible, teaching invariances the model should not have.

✅ **DO:**
- Reason about label semantics before adding a transform; bound or drop anything that can change the label.
- Set per-class budgets so augmentation adds coverage without skewing base rates.
- Keep validation/test raw and judge augmentation by gains on the real distribution, per slice.
- Tune intensity to stay within plausible inputs and stop when held-out accuracy stops improving.

## Example Output

```markdown
## Augmentation Plan: Retail Shelf Product Detection (images)

### Invariance Map
- Augmentable: lighting, minor rotation (≤15°), occlusion, background clutter, JPEG noise.
- Label-changing (DO NOT augment): horizontal flip (some packaging text is orientation-specific),
  heavy color shift (brand color is a cue).

### Transform Plan
| Transform | Invariance/condition | Label-safe? | Intensity |
|---|---|---|---|
| Brightness/contrast jitter | store lighting variation | Yes (±20%) | p=0.5 |
| Rotation | camera tilt | Yes (≤15°) | p=0.3 |
| Random occlusion (cutout) | shoppers/price tags | Yes | p=0.3 |
| Horizontal flip | — | NO (text/brand) | excluded |
| Hue shift | — | Bounded only (±5°) | p=0.2 |

### Distribution Guardrails
- Cap augmented copies at 2× per image; equal budget across product classes to preserve shelf base rates.

### Execution
- Online (on-the-fly) per batch; framework: <ask user + version>. Compute: negligible vs training.

### Leak-Safe Placement
- Train split only; val/test use raw store photos.

### Validation Plan
- A/B: train with vs without aug; compare mAP on a raw holdout and per-product-class slices.

### Risks & Stop Conditions
- Hue shift most likely to harm brand-color cues — keep tight. Stop increasing magnitude once holdout mAP plateaus.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** invariance map → transforms → label check → guardrails → validation.
- **RT-02 (Multi-Dimensional Analysis Framework):** transforms weighed on invariance, label-safety, intensity.
- **CM-02 (Constraint Specification):** label preservation and target-distribution fidelity are hard constraints.
- **DT-04 (Decision Criteria Specification):** explicit rules for which transforms are admissible per task.
- **QA-12 (False Positives Identification):** preempts label-flipping and distribution-distorting transforms.

**Related Prompts:**
- `mldata_class_imbalance_strategy.md` — decide if augmentation (vs weighting) is the right minority-class lever.
- `mldata_synthetic_data_strategy.md` — when transforms aren't enough and new records are needed.
- `mldata_train_test_split_strategy.md` — keep augmentation inside a leak-safe split.
