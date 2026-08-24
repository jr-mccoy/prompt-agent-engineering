---
title: "CV Segmentation Approach Designer"
category: AI-ML/specialized-ml/computer-vision
description: "Choose between semantic, instance, and panoptic segmentation for a task and design its evaluation (IoU/Dice/PQ) with boundary precision, class imbalance, and small-region pitfalls accounted for."
techniques:
  - RT-02
  - ST-02
  - DS-02
  - QA-12
  - CM-02
difficulty: advanced
tags:
  - computer-vision
  - segmentation
  - semantic-segmentation
  - instance-segmentation
  - evaluation
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/computer-vision/cv_task_framing.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_object_detection_eval.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_annotation_strategy.md
---

# CV Segmentation Approach Designer

**Objective:** Determine whether a task needs semantic, instance, or panoptic segmentation, and design the matching label format, model approach, and — critically — the evaluation (mean IoU, Dice, AP-mask, panoptic quality) so that boundary accuracy, class imbalance, and small-region performance are measured correctly rather than masked by a single global score.

**When to Use:**
- The task requires pixel-level extent (area, shape, precise boundaries), not just boxes.
- Choosing among semantic vs instance vs panoptic for a new project.
- A segmentation model's mean IoU looks acceptable but boundaries or thin/rare structures are visibly wrong.

**When NOT to Use:**
- Box-level localization suffices (use `cv_object_detection_eval.md`).
- The task type itself is unsettled (start with `cv_task_framing.md`).

## Inputs / Context

- **What the output drives** — do you need per-pixel class only, per-object instances, or both (stuff + things)?
- **Class structure** — countable "things" vs amorphous "stuff"; class count; rare/thin structures (wires, vessels, cracks).
- **Boundary tolerance** — how exact must edges be (medical/measurement) vs coarse region labeling.
- **Imagery** — resolution, modality, instance density, occlusion.
- **Data & label cost** — mask annotation budget; existing labels and their format.
- **Constraints** — inference latency, memory, deployment target.

## Constraints

**Must:**
- Select semantic / instance / panoptic by what the output consumer needs (presence-per-pixel vs separable instances vs both), and justify the choice.
- Match the metric to the variant: mean IoU/Dice for semantic; mask AP for instance; panoptic quality (PQ) for panoptic — and report per-class, not just mean.
- Address class imbalance and small/thin-region performance explicitly in the evaluation design.

**Must Not:**
- Use instance or panoptic when semantic suffices, or vice versa, without stating the cost.
- Report a single mean IoU as the verdict; small and rare classes vanish in the mean.
- Invent dataset statistics (class frequency, region sizes) — request them or mark unknown.

**Instructions:**

1. **Classify the output need.** Decide whether the consumer needs per-pixel class (semantic), separable object instances (instance), or unified stuff+things with instance identity (panoptic). State which.

2. **Define the label format.** Specify the mask format and the boundary-precision rule, drawing on the annotation strategy; flag thin/small structures that need special labeling care.

3. **Choose the metric family.** Bind the variant to its metric: mean IoU (often with Dice for medical/imbalanced) for semantic; mask AP across IoU for instance; PQ (= SQ × RQ) for panoptic. State the IoU thresholds used.

4. **Design the per-class / per-region breakdown.** Require per-class IoU/Dice/AP and a small-region slice; identify which classes the mean is hiding.

5. **Handle boundary accuracy.** Add a boundary-aware check (e.g., boundary IoU / trimap band) where edge precision matters, since region IoU is largely insensitive to thin boundary errors.

6. **Account for imbalance.** Recommend the loss/eval adjustments (Dice/Tversky/class-weighting on the loss side; macro-averaging on the eval side) appropriate to the imbalance described.

7. **Confront instance-specific pitfalls.** For instance/panoptic, address merged/split instances, overlapping masks, and how PQ penalizes them.

8. **State the deployment verdict.** Summarize what the segmentation can be trusted to delineate, by class and region size, at the chosen operating point.

**Output Format:**

A markdown approach document:
- **Output Need → Variant** — semantic / instance / panoptic + justification.
- **Label & Boundary Spec** — mask format, boundary precision, special-case structures.
- **Metric Design** — primary metric, per-class breakdown, boundary metric, thresholds.
- **Imbalance & Small-Region Plan** — loss + eval adjustments.
- **Instance/Panoptic Pitfalls** — if applicable.
- **Deployment Verdict** — trustworthy slices vs not.

## Verification

- [ ] The chosen variant is justified by the output consumer's actual need.
- [ ] The metric matches the variant (IoU/Dice vs mask AP vs PQ) with thresholds stated.
- [ ] Per-class and small-region breakdowns are required, not just a global mean.
- [ ] Boundary accuracy is addressed separately where edges matter.
- [ ] Class imbalance is handled in both loss and evaluation.

## False-Positive Prevention

❌ **DON'T:**
- Report 0.85 mean IoU as success when the rare 2%-of-pixels critical class scores 0.20.
- Use semantic segmentation when the task must count or separate touching instances (cells, cars in a jam).
- Trust region IoU to reflect boundary quality — a slightly fat/thin mask barely moves IoU but ruins measurements.
- Apply panoptic quality to a stuff-only task where semantic mean IoU is the right and simpler metric.

✅ **DO:**
- Macro-average and report per-class IoU/Dice; weight the verdict by clinical/operational importance.
- Pick instance/panoptic only when instances must be separated, and accept the labeling cost knowingly.
- Add a boundary-aware metric where edge precision is part of the requirement.
- Use Dice/Tversky or class weighting when foreground classes are tiny.

## Example Output

```markdown
## Segmentation Approach: Tumor Delineation on MRI Slices

### Output Need → Variant
Radiologist needs the tumor region's extent and shape for volume measurement; tumors are not counted as multiple instances per slice. → **Semantic segmentation** (binary foreground + background), with Dice as co-primary metric.

### Label & Boundary Spec
Polygon→mask at full slice resolution; boundary traced at the T2 hyperintensity edge per radiology rulebook. Thin peritumoral extensions labeled, not smoothed away.

### Metric Design
Primary: Dice (robust to the tumor's small pixel fraction) + IoU. Report per-slice and per-case, not pooled-pixel. Add **boundary Dice** (3px band) because volume estimates depend on edge accuracy. IoU threshold for "acceptable" case = 0.7.

### Imbalance & Small-Region Plan
Tumor is ~1–4% of pixels → Tversky loss (β favoring recall) instead of plain CE; eval macro-averaged across cases; separate slice-level small-lesion slice (<200px) reported.

### Instance/Panoptic Pitfalls
N/A — single-class semantic; no instance separation required.

### Deployment Verdict
Trust for medium/large lesions (case Dice 0.82). **Flag small lesions (<200px): Dice 0.41** — under-segments edges, biasing volume low. Recommend higher-resolution patches + boundary loss before clinical volume use.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** variant choice weighed across need, cost, and metric.
- **ST-02 (Structured Sequential Instructions):** need → label → metric → breakdown → boundary → verdict.
- **DS-02 (Metric Specification):** correct IoU/Dice/PQ semantics and thresholds.
- **QA-12 (False Positives Identification):** prevents mean-IoU and boundary-insensitivity blind spots.
- **CM-02 (Constraint Specification):** boundary tolerance and latency act as governing constraints.

**Related Prompts:**
- `cv_task_framing.md` — confirm pixel-level extent is genuinely needed.
- `cv_object_detection_eval.md` — when boxes (not masks) answer the goal.
- `cv_annotation_strategy.md` — mask-boundary labeling rules feed this design.
