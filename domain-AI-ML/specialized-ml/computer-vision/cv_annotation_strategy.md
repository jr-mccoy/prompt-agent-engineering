---
title: "CV Annotation Strategy"
category: AI-ML/specialized-ml/computer-vision
description: "Design an image/video annotation strategy — label schema, annotation guidelines, edge-case rules, quality control, and tooling — that produces consistent labels matched to the task and metric."
techniques:
  - ST-02
  - CM-02
  - QA-04
  - DS-06
  - RT-05
difficulty: intermediate
tags:
  - computer-vision
  - annotation
  - labeling
  - data-quality
  - inter-annotator-agreement
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/computer-vision/cv_task_framing.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_augmentation_strategy.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_segmentation_approach.md
---

# CV Annotation Strategy

**Objective:** Produce a complete, executable annotation plan for an image or video dataset — label schema, written guidelines, edge-case adjudication rules, quality-control protocol with agreement metrics, and tooling choice — so that labels are consistent across annotators and faithful to the framed task and its metric.

**When to Use:**
- The CV task type is fixed and you are about to commission or run labeling.
- Existing labels are noisy/inconsistent and you need to redesign the guideline.
- Onboarding multiple annotators or a vendor and need a spec they can follow.

**When NOT to Use:**
- The task type itself is unsettled (use `cv_task_framing.md` first).
- You only need synthetic label variation, not human labels (use `cv_augmentation_strategy.md`).

## Inputs / Context

Provide what you can:
- **Task type & label unit** — boxes / polygons-masks / image tags / keypoints.
- **Class taxonomy** — class names and any hierarchy; expected frequency/rarity.
- **Domain visuals & ambiguity** — occlusion, truncation, small objects, motion blur, similar-looking classes.
- **Video specifics** — frame rate, whether tracking/IDs are needed, key-frame vs every-frame.
- **Scale & resources** — number of items, annotator count, vendor vs in-house, budget, deadline.
- **Tooling constraints** — existing platform, export format, integration needs.

## Constraints

**Must:**
- Define every class with a positive definition *and* explicit boundaries against the easiest-to-confuse classes.
- Specify a decision rule for each named edge case (occlusion, truncation, ambiguity, "don't label" cases).
- Include a measurable QC protocol with an agreement metric and a re-work threshold.

**Must Not:**
- Produce a class list without disambiguation rules — that is the primary source of label noise.
- Recommend a tool or vendor without tying the choice to the label unit and export format.
- Fabricate class frequencies or annotation throughput; mark unknowns as assumptions to validate on a pilot.

**Instructions:**

1. **Lock the annotation unit to the metric.** Confirm that the label geometry (tight boxes vs loose, full polygons vs simplified) matches how the metric (IoU/mAP/Dice) will score it; tighter metrics demand stricter geometry rules.

2. **Write operational class definitions.** For each class give a one-line positive definition plus "include / exclude" examples, and an explicit rule separating it from its nearest confusable class. Decide single-label vs multi-label and a default/`other` bucket.

3. **Enumerate edge-case rules.** Specify handling for occlusion (label visible extent? amodal?), truncation at frame edge, group/crowd regions, tiny objects below a size floor, ambiguous/illegible items, and reflections/screens. Each gets a deterministic rule, not "use judgment."

4. **Design the video protocol (if applicable).** Decide key-frame interval vs every-frame, interpolation, identity persistence across frames, and entry/exit handling. State which frames are scored.

5. **Specify the QC protocol.** Define a gold/honeypot set, the agreement metric (e.g., IoU-matched agreement, Cohen's/Fleiss' κ for tags), the sampling rate for review, the pass threshold, and the re-annotation loop for failures.

6. **Plan annotator calibration.** Define onboarding (label the gold set, compare to reference), a disagreement-adjudication path, and guideline-versioning so changes are tracked and old labels flagged for review.

7. **Choose tooling and export.** Recommend a tool that supports the label unit, QC review, and the required export format; note pre-labeling/model-assist if data volume justifies it.

8. **Recommend a pilot.** Specify a small pilot batch to validate guidelines, measure agreement, and revise before full-scale labeling.

**Output Format:**

A markdown annotation spec:
- **Annotation Unit & Geometry Rules**
- **Class Definitions Table** — Class | Definition | Confused-with rule | Include/Exclude examples.
- **Edge-Case Rulebook** — case → rule.
- **Video Protocol** (if applicable).
- **QC Protocol** — gold set, agreement metric, threshold, re-work loop.
- **Calibration & Versioning Plan**.
- **Tooling & Export Recommendation**.
- **Pilot Plan & Open Assumptions**.

## Verification

- [ ] Every class has a definition AND a rule distinguishing it from its nearest confusable class.
- [ ] Each listed edge case has a deterministic decision rule.
- [ ] An agreement metric and a quantitative pass/re-work threshold are specified.
- [ ] Label geometry rules are tied to the scoring metric.
- [ ] A pilot is recommended and unknowns are flagged as assumptions, not invented facts.

## False-Positive Prevention

❌ **DON'T:**
- Ship a class list as "the guideline" — undocumented class boundaries are the top cause of inter-annotator noise.
- Leave occlusion/truncation/crowd handling to annotator discretion; inconsistent edge-case calls silently degrade IoU.
- Measure quality only by throughput; high speed with no agreement metric hides systematic label drift.
- Assume vendor labels are correct without a gold/honeypot set seeded into their queue.

✅ **DO:**
- Pair every class with explicit "confused-with" disambiguation and concrete include/exclude examples.
- Write a deterministic rule for each edge case and version the guideline when rules change.
- Quantify quality with an agreement metric on a held-out gold set and define a re-annotation threshold.
- Run a pilot, measure agreement, and revise the guideline before scaling — assumptions about throughput and ambiguity rarely survive contact with real images.

## Example Output

```markdown
## Annotation Strategy: Retail Shelf Product Detection (boxes)

### Annotation Unit & Geometry
Axis-aligned boxes, tight to visible product extent. Metric is mAP@0.5, so boxes must be tight enough to clear 0.5 IoU even for thin items; ±2px tolerance on visible edges.

### Class Definitions (excerpt)
| Class | Definition | Confused-with rule | Include / Exclude |
|---|---|---|---|
| `bottle` | Rigid neck + body container | vs `can`: label `can` if no neck/seam-top | Incl. lying-down bottles; Excl. empty caps |
| `can` | Cylindrical metal, seamed top | vs `bottle`: see above | Incl. dented cans; Excl. crushed/unidentifiable |

### Edge-Case Rulebook
- Occlusion: label visible extent only; skip if <30% visible.
- Truncation at shelf edge: label visible part, flag `truncated=true`.
- Stacked identical SKUs: one box per visible front face.
- Blurry/illegible product: box it, class = `unknown_product`.

### QC Protocol
Gold set: 200 pre-labeled images seeded at 5% into queues. Metric: IoU-matched box agreement vs reference. Pass threshold: ≥0.85 agreement per annotator. Below → retrain + re-label their batch.

### Calibration & Versioning
Onboarding: label gold set, review disagreements with lead. Guideline v1.2; the stacked-SKU rule (v1.1→v1.2) flags all pre-v1.2 batches for re-check.

### Tooling & Export
CVAT (box + honeypot + review). Export COCO JSON. Model-assist pre-labeling enabled after 5k boxes to cut effort.

### Pilot Plan & Open Assumptions
Pilot: 500 images, 3 annotators. Validate `bottle`/`can` confusion rate and small-item recall. Assumed ~40 boxes/image (unverified) — confirm on pilot to size budget.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** a fixed schema → edge-cases → QC → tooling → pilot flow.
- **CM-02 (Constraint Specification):** geometry rules are bound to the scoring metric and label unit.
- **QA-04 (Consistency Enforcement):** disambiguation rules and agreement metrics enforce cross-annotator consistency.
- **DS-06 (Prioritization & Severity Guidance):** QC thresholds and re-work loops prioritize systematic errors.
- **RT-05 (Evidence-Based Reasoning):** quality is judged by measured agreement on a gold set, not assertion.

**Related Prompts:**
- `cv_task_framing.md` — settle the task and label unit before designing annotation.
- `cv_augmentation_strategy.md` — synthetic variation that must preserve these label semantics.
- `cv_segmentation_approach.md` — when the label unit is pixel masks rather than boxes.
