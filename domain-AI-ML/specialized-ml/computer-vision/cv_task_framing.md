---
title: "CV Task Framing"
category: AI-ML/specialized-ml/computer-vision
description: "Translate a fuzzy vision goal into a concrete CV task type (classification / detection / segmentation / keypoint) and derive the label format, metric, and data implications each choice forces."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - computer-vision
  - task-framing
  - problem-definition
  - metrics
  - labeling
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/computer-vision/cv_annotation_strategy.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_object_detection_eval.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_segmentation_approach.md
---

# CV Task Framing

**Objective:** Convert a stated business/visual goal into a precise computer-vision task formulation — choosing among image classification, object detection, semantic/instance/panoptic segmentation, and keypoint/landmark estimation — and make explicit the label format, evaluation metric, and annotation cost each formulation forces, so downstream work is not built on a mis-framed task.

**When to Use:**
- A stakeholder describes what they want to "see" or "find" in images/video but hasn't named a task type.
- You are choosing between cheaper (classification) and richer (detection/segmentation) framings.
- Before commissioning annotation, since the task type dictates the label schema and budget.

**When NOT to Use:**
- The task type is already settled and you only need annotation design (use `cv_annotation_strategy.md`) or metric setup (use `cv_object_detection_eval.md` / `cv_segmentation_approach.md`).
- The problem is non-visual or is an LLM/multimodal generation task (cross-link `genai-llm-engineering`).

## Inputs / Context

Provide what you can; framing degrades gracefully:
- **Goal in plain language** — what decision or action the vision output drives.
- **What must be known per image** — "is X present?", "where is each X?", "exact pixels of X?", "how many?", "pose of X?".
- **Granularity & multiplicity** — single object vs many; counting required; overlapping/occluded instances.
- **Downstream consumer** — human review, automated trigger, measurement, tracking.
- **Constraints** — latency, edge vs server, annotation budget, available data volume.

## Constraints

**Must:**
- Map the goal to exactly one primary task type (plus optional secondary stages) and justify against the stated need.
- For the chosen task, state the label format, the primary metric, and the annotation unit explicitly.
- Surface the cheapest framing that still satisfies the requirement, and name what is lost by going cheaper.

**Must Not:**
- Default to detection/segmentation when classification or counting would meet the need.
- Invent latency, volume, or accuracy requirements the user did not give — list them as open questions.
- Quote benchmark numbers from memory as if they apply to the user's data.

**Instructions:**

1. **Extract the decision the output serves.** Pin down what is done with the prediction (alert, count, measure, locate, redact). The action determines the minimum task richness required — frame to that floor, not to the maximum.

2. **Test each task type against the requirement.** Ask, in order: Does "present/absent or which class" suffice (classification)? Is "where + which" needed (detection)? Are exact pixel boundaries or area needed (segmentation)? Is structured pose/landmarks needed (keypoint)? Stop at the first that satisfies.

3. **Resolve multiplicity and counting.** If multiple instances must be distinguished or counted, classification is insufficient; choose detection or instance segmentation. State whether instance identity matters (instance vs semantic).

4. **Derive the label format.** For the chosen task, specify the annotation unit: image-level tags, bounding boxes, polygons/masks, or keypoint sets — and any class taxonomy and "ignore/background" handling.

5. **Bind the metric to the task.** Classification → accuracy/F1/AUC with class balance noted; detection → mAP at stated IoU thresholds; segmentation → IoU/Dice; keypoint → PCK/OKS. State the primary metric and why it matches the decision.

6. **Cost and data check.** Estimate relative annotation cost (tags << boxes << masks) and flag whether available data volume supports the chosen task; recommend a cheaper fallback if data/budget is thin.

7. **Name the open questions.** List unstated constraints (latency, volume, accuracy bar) that should be confirmed before committing.

**Output Format:**

A markdown brief:
- **Decision Served** — one line on what the output triggers.
- **Recommended Task Type** — primary (and any secondary stage) with justification.
- **Task Framing Table** — Candidate task | Satisfies need? | Label unit | Primary metric | Relative cost.
- **Label Schema** — classes, annotation unit, ignore/background rules.
- **Metric Choice** — primary metric + rationale.
- **Cheaper Fallback** — what it loses.
- **Open Questions** — constraints to confirm.

## Verification

- [ ] The chosen task type is justified against the stated downstream decision, not chosen by default.
- [ ] Label format, primary metric, and annotation unit are all specified for the recommendation.
- [ ] Multiplicity/counting requirements were explicitly addressed.
- [ ] A cheaper fallback is named with what it sacrifices.
- [ ] Unstated constraints are listed as open questions rather than invented.

## False-Positive Prevention

❌ **DON'T:**
- Recommend segmentation when the consumer only needs a yes/no or a count — pixel masks are 5-20x the annotation cost.
- Conflate "detect" with "classify": "find the defects" can mean "is there a defect?" (classification) or "where is each defect?" (detection) — these have different labels and metrics.
- Assume instance separation is needed when semantic (per-pixel class, no instance ID) suffices.
- Pick a metric that hides the failure that matters (e.g., overall accuracy when the rare positive class is the whole point).

✅ **DO:**
- Frame to the minimum task richness that satisfies the decision, and state what richer framings would add.
- Force the user to answer "present?", "where?", "exact pixels?", or "how many?" before committing.
- Match the metric to the operational cost of each error type (missed instance vs false alarm).
- Flag when the data volume is too small for the chosen task and propose a cheaper or transfer-learning fallback.

## Example Output

```markdown
## CV Task Framing: Warehouse Damaged-Package Detection

### Decision Served
Route a parcel to manual inspection when damage is visible on the conveyor camera feed.

### Recommended Task Type
**Object detection** (primary). Counting and locating multiple damaged regions per parcel is required to route correctly; image-level classification cannot say *where* or *how many*. No pixel-exact area is needed, so segmentation is over-spec.

### Task Framing Table
| Candidate | Satisfies need? | Label unit | Primary metric | Relative cost |
|---|---|---|---|---|
| Classification (damaged y/n) | Partial — no localization/count | Image tag | F1 (imbalanced) | Low |
| Detection | Yes | Bounding boxes | mAP@0.5 | Medium |
| Instance segmentation | Yes but over-spec | Polygons | Mask IoU | High |

### Label Schema
Classes: `dent`, `tear`, `crush`, `wet`. Annotation unit: axis-aligned boxes. Background = undamaged surface (no box). Ignore region: occluded by gripper arm.

### Metric Choice
**mAP@0.5** as primary (localization tolerance acceptable), with per-class AP since `wet` is rare. Recall@high-precision tracked operationally (a missed damaged parcel costs more than a false flag).

### Cheaper Fallback
Image-level classification (~1/8 the labeling cost). Loses location and count; acceptable only if a flagged parcel is fully re-inspected by hand anyway.

### Open Questions
- Conveyor speed → latency budget? (affects model size / edge vs server)
- Estimated daily volume and damage base rate? (affects class imbalance handling)
- Is multi-damage counting actually used downstream, or just "any damage"?
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** a fixed decision-to-task-to-label-to-metric sequence.
- **RT-02 (Multi-Dimensional Analysis Framework):** candidate task types scored across satisfaction, label unit, metric, and cost.
- **CM-02 (Constraint Specification):** the downstream decision and budget act as governing constraints on task richness.
- **DS-02 (Metric Specification):** binds each task type to its appropriate primary metric.
- **QA-01 (Self-Verification):** the checklist guards against over-spec framing.

**Related Prompts:**
- `cv_annotation_strategy.md` — design the labeling once the task type is fixed.
- `cv_object_detection_eval.md` — evaluate the detection framing correctly.
- `cv_segmentation_approach.md` — if pixel-level output turns out to be required.
