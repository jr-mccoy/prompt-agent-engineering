---
title: "CV Object Detection Evaluator"
category: AI-ML/specialized-ml/computer-vision
description: "Evaluate an object detector correctly — mAP across IoU thresholds, per-class and per-size breakdowns, confidence/NMS effects, and the small-object and class-imbalance pitfalls that hide behind a single headline number."
techniques:
  - ST-02
  - DS-02
  - QA-12
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - computer-vision
  - object-detection
  - evaluation
  - mAP
  - IoU
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/computer-vision/cv_task_framing.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_segmentation_approach.md
  - domain-AI-ML/model-evaluation-validation/mleval_eval_result_skepticism_audit.md
---

# CV Object Detection Evaluator

**Objective:** Produce a correct, decision-useful evaluation of an object detector — decomposing a single mAP figure into per-class, per-IoU-threshold, and per-object-size performance, exposing the effects of confidence and NMS choices, and surfacing the small-object and rare-class failures that aggregate metrics conceal — so the result reflects real deployment behavior, not benchmark optics.

**When to Use:**
- After training a detector, before claiming it is "good" or comparing it to another model.
- When a detector's mAP looks fine but real-world misses/false alarms are reported.
- When choosing an operating point (confidence threshold) for deployment.

**When NOT to Use:**
- The task is segmentation, not box detection (use `cv_segmentation_approach.md`).
- You suspect the *data/eval setup* itself is corrupt rather than mis-measured (use `mleval_eval_result_skepticism_audit.md`).

## Inputs / Context

- **Predictions & ground truth** — boxes with classes and confidence scores, and the matched ground-truth annotations.
- **Class list & frequencies** — including which classes are rare.
- **Object size distribution** — small/medium/large breakdown (e.g., COCO size bands) if available.
- **Evaluation protocol claimed** — IoU threshold(s), mAP variant (mAP@0.5 vs mAP@[.5:.95]), NMS settings, confidence threshold.
- **Deployment cost asymmetry** — relative cost of a missed object vs a false detection, per class if it varies.

## Constraints

**Must:**
- Report mAP across the IoU threshold range the protocol claims, and never let a single mAP@0.5 number stand alone.
- Break results down per class and per object-size band, and identify where the headline metric is being carried by easy classes/sizes.
- Tie the chosen confidence threshold to the precision/recall the deployment cost asymmetry requires.

**Must Not:**
- Average away rare-class or small-object failure into a flattering mean.
- Confuse mAP@0.5 with mAP@[.5:.95]; state which is reported and why.
- Invent per-class numbers — if a breakdown was not supplied, request it or mark it as unmeasured rather than estimating.

**Instructions:**

1. **Pin the protocol.** State the IoU threshold(s), mAP variant, NMS IoU, and confidence threshold actually used. Mismatches between claimed and computed protocol are the first thing to flag.

2. **Decompose the headline.** Report mAP@0.5, mAP@0.75, and mAP@[.5:.95] (or the relevant range). A model strong at IoU 0.5 but weak at 0.75 has loose localization — say so.

3. **Break down per class.** Surface per-class AP; flag classes carried by frequency and rare classes hidden in the mean. Inspect the class-confusion structure (what gets misclassified as what).

4. **Break down per object size.** Report AP for small/medium/large. Small-object collapse is the most common silent failure; quantify it.

5. **Separate the error types.** Distinguish localization errors (right class, IoU below threshold), classification errors, duplicate detections (NMS), background false positives, and missed objects — each implies a different fix.

6. **Sweep the operating point.** Show the precision-recall curve and the precision/recall at candidate confidence thresholds; recommend the threshold that matches the miss-vs-false-alarm cost.

7. **Probe NMS effects.** Check whether NMS IoU is merging true neighbors (crowded scenes) or leaving duplicates; report sensitivity.

8. **Conclude with deployment reality.** State what the detector can and cannot be trusted to do, by class and size, at the recommended operating point.

**Output Format:**

A markdown evaluation report:
- **Protocol Confirmed** — IoU/mAP variant/NMS/confidence actually used.
- **Headline Decomposition** — mAP@0.5 / @0.75 / @[.5:.95].
- **Per-Class AP** — table, rare classes flagged.
- **Per-Size AP** — small / medium / large.
- **Error-Type Breakdown** — localization / classification / duplicate / background FP / miss.
- **Operating-Point Recommendation** — threshold + P/R + cost-asymmetry rationale.
- **NMS Sensitivity** — finding.
- **Deployment Verdict** — trustworthy slices vs not.

## Verification

- [ ] mAP is reported across IoU thresholds, not a lone mAP@0.5.
- [ ] Per-class and per-size breakdowns are present and rare/small failures are called out.
- [ ] The mAP variant and NMS/confidence settings are stated and matched to the claim.
- [ ] Error types are separated so fixes are actionable.
- [ ] The recommended confidence threshold is tied to the miss-vs-false-alarm cost.

## False-Positive Prevention

❌ **DON'T:**
- Report mAP@0.5 alone and call localization "good" — loose boxes pass at 0.5 and fail at 0.75.
- Let a high mean AP hide that the rare safety-critical class scores near zero.
- Ignore small-object AP when the deployment cares about distant/tiny targets.
- Pick a confidence threshold that maximizes F1 when missing an object is far costlier than a false alarm (or vice versa).

✅ **DO:**
- Always decompose mAP across IoU thresholds, classes, and sizes before judging.
- Read per-class AP and weight conclusions by deployment importance, not frequency.
- Classify errors (localization vs classification vs NMS vs background) to choose the right remedy.
- Set the operating point from the cost asymmetry, shown on the PR curve.

## Example Output

```markdown
## Detection Eval: Warehouse Forklift/Pedestrian Detector

### Protocol Confirmed
mAP@[.5:.95], NMS IoU 0.5, eval at confidence 0.25. (Report had claimed "mAP 0.71" — that was mAP@0.5 only.)

### Headline Decomposition
- mAP@0.5: 0.71 | mAP@0.75: 0.48 | mAP@[.5:.95]: 0.44 → localization is loose.

### Per-Class AP (@[.5:.95])
| Class | AP | Note |
|---|---|---|
| forklift | 0.61 | frequent; carries the mean |
| pedestrian | 0.29 | **rare + safety-critical — under-performs** |
| pallet | 0.52 | |

### Per-Size AP
small 0.18 | medium 0.47 | large 0.63 → distant pedestrians (small) are largely missed.

### Error-Type Breakdown
Pedestrian misses dominated by (a) small-object misses (52%) and (b) background FP suppression at high threshold. Few classification errors.

### Operating-Point Recommendation
Missing a pedestrian >> false alarm. Lower confidence to 0.15 for the pedestrian class: recall 0.61 → 0.82, precision 0.74 → 0.58 — acceptable given cost. Keep 0.30 for forklift.

### NMS Sensitivity
Raising NMS IoU to 0.6 recovers 3% recall in crowded aisles without notable duplicate inflation.

### Deployment Verdict
Trust for medium/large forklifts and pallets. **Do not trust for distant pedestrians** without small-object retraining (higher input resolution / tiling) — this is a safety gap, not a tuning gap.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** protocol → decompose → per-class → per-size → errors → operating point.
- **DS-02 (Metric Specification):** correct mAP/IoU semantics and operating-point selection.
- **QA-12 (False Positives Identification):** exposes metric inflation by easy classes/sizes and protocol mismatch.
- **RT-05 (Evidence-Based Reasoning):** verdicts tied to per-slice numbers, no estimation.
- **DS-06 (Prioritization & Severity Guidance):** weights findings by deployment importance, not frequency.

**Related Prompts:**
- `cv_task_framing.md` — confirm detection was the right framing.
- `cv_segmentation_approach.md` — when box overlap is insufficient and pixel extent matters.
- `mleval_eval_result_skepticism_audit.md` — when the eval setup itself is suspect.
