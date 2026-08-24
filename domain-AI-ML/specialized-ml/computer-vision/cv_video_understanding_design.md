---
title: "Computer Vision Video Understanding Design"
category: AI-ML/specialized-ml/computer-vision
description: "Design a video-understanding approach — clip/frame sampling, temporal modeling (3D CNN, two-stream, video transformer, or frame-aggregation), task framing (action recognition, temporal action localization, video classification), and leakage-safe evaluation — matched to the data's temporal structure, label granularity, and compute budget."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-01
  - QA-12
difficulty: advanced
tags:
  - computer-vision
  - video-understanding
  - temporal-modeling
  - action-recognition
  - sampling
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/computer-vision/cv_task_framing.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_augmentation_strategy.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_transfer_learning_pretrained_selection.md
---

# Computer Vision Video Understanding Design

**Objective:** Help the user design a video-understanding pipeline that fits their actual data and task rather than defaulting to whatever architecture is fashionable. The core decisions are how to turn a variable-length video into model inputs (frame/clip sampling rate, clip length, spatial resolution), how to capture temporal structure (3D convolutions, two-stream optical-flow + RGB, video transformers with spatio-temporal attention, or cheap per-frame features aggregated over time), how to frame the supervision (whole-video classification vs. action recognition over short clips vs. temporal action localization with start/end boundaries), and how to evaluate without temporal leakage. This prompt walks those tradeoffs and produces a concrete, framework-neutral design with an evaluation protocol you can defend.

**When to Use:**
- You have video data and need to choose a temporal-modeling approach and sampling strategy before committing to training infrastructure.
- Your task involves motion, ordering, or events that unfold over time (action recognition, gesture/activity detection, temporal localization).
- A per-frame image model is underperforming and you suspect temporal context is the missing signal.

**When NOT to Use:**
- The task is genuinely single-frame (e.g., classifying a thumbnail) — use `cv_task_framing.md` instead.
- You need to design image-level augmentation policy — see `cv_augmentation_strategy.md`.
- You are selecting a pretrained backbone for transfer — see `cv_transfer_learning_pretrained_selection.md`.

## Inputs / Context

Provide what you can:
- **Task definition** — what a prediction means (one label per video, per-clip action, or start/end boundaries of events).
- **Video characteristics** — typical duration, frame rate, resolution, and whether events are brief or span the whole clip.
- **Dataset size & label granularity** — number of videos, labels per video, and how labels are timestamped (if at all).
- **Temporal grouping metadata** — source video ID, recording session, camera, or subject — needed to prevent leakage.
- **Compute & latency budget** — training hardware, and whether inference is offline or real-time/streaming.
- **Motion dependence** — does the answer require motion (e.g., "falling" vs. "lying down") or is appearance enough?
- **Existing assets** — any pretrained video backbones, optical-flow tooling, or prior baselines available.

## Constraints

**Must:**
- Tie every architecture choice to a property of the data (event duration, motion dependence, label granularity).
- Specify the sampling strategy explicitly (frames per clip, stride, clips per video at train and at test time).
- Define an evaluation protocol whose splits are grouped by source video, never by individual frame or clip.
- State the train-time vs. test-time sampling difference and how predictions are aggregated to the evaluation unit.

**Must Not:**
- Fabricate accuracy numbers, SOTA results, or benchmark figures from memory; reason from the user's data and mark unknowns "measure on your data."
- Assert version-specific API behavior of any video library or framework from memory — flag "verify against current docs."
- Recommend a single "best" architecture as universally correct; present tradeoffs and defer the pick to evaluation.
- Allow frames or clips from the same source video to fall on both sides of a train/val/test split.

**Instructions:**

1. **Restate the task and its temporal unit.** Clarify whether a label applies to a whole video, a short clip, or a timestamped interval. The temporal unit of the label drives almost everything downstream.
2. **Characterize the temporal signal.** Determine event duration relative to clip length, and whether motion (not just appearance) carries the answer. Short, motion-dependent events favor denser sampling and explicit temporal modeling.
3. **Design the sampling strategy.** Specify clip length (frames), sampling stride, and how many clips per video at training vs. inference. Note that uniform/segment-based sampling and dense sampling trade coverage against compute.
4. **Choose a temporal-modeling family.** Compare: frame-aggregation (per-frame features + pooling/RNN/attention) as a cheap strong baseline; 3D CNNs; two-stream (RGB + optical flow) when motion is decisive; and video transformers when data and compute are abundant. Map each to the data's properties.
5. **Match supervision to label granularity.** Whole-video classification, clip-level action recognition, or temporal action localization each need different heads, losses, and label handling. Do not force a localization task into a classification frame.
6. **Plan transfer and pretraining.** Decide whether to start from a pretrained video backbone, an image backbone inflated to 3D, or train from scratch — guided by dataset size and domain gap. Defer the empirical choice to a small bake-off.
7. **Define leakage-safe evaluation.** Group splits by source video. Specify test-time clip sampling and the aggregation rule (e.g., average clip logits to a video prediction). For localization, define temporal IoU thresholds and the matching rule.
8. **Specify the metrics and a baseline.** Choose metrics that match the unit (clip vs. video accuracy; mAP at temporal IoU for localization) and pin a simple baseline to beat. Flag all expected numbers as "to be measured."

**Output Format:**

A markdown design brief:
- **Task & Temporal Unit** — restated task and the unit a label applies to.
- **Temporal Signal Analysis** — event duration, motion dependence, implications.
- **Sampling Strategy** — train and test sampling, clip length, stride, clips/video.
- **Architecture Options** — table of candidate temporal-modeling families with fit rationale.
- **Supervision & Heads** — task framing, loss, label handling.
- **Transfer Plan** — pretraining source and bake-off plan.
- **Evaluation Protocol** — grouped splits, aggregation rule, metrics, IoU thresholds (if localizing).
- **Open Questions / Measure-On-Your-Data** — unknowns flagged for empirical resolution.

## Verification

- [ ] Every architecture recommendation is justified by a stated property of the user's data.
- [ ] The sampling strategy specifies train-time and test-time behavior separately.
- [ ] Train/val/test splits are grouped by source video; no frame or clip crosses the boundary.
- [ ] The evaluation unit (clip vs. video) and the aggregation rule are explicit.
- [ ] Task framing (classification vs. localization) matches the label granularity.
- [ ] No benchmark/SOTA numbers are invented and no version-specific API behavior is asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Split frames or short clips randomly so frames from the same source video land in both train and validation — this temporal leakage inflates every metric.
- Report frame-level accuracy and present it as if it were clip- or video-level performance.
- Assume a per-frame image model captures motion-dependent actions just because per-frame accuracy looks high.
- Use dense test-time clip sampling while training on a single clip per video without disclosing the mismatch.

✅ **DO:**
- Group every split by source video ID before sampling any frames or clips.
- State which unit each reported number describes (frame, clip, or video) and how predictions aggregate up.
- Probe whether the task is motion-dependent before deciding a per-frame baseline is sufficient.
- Keep train-time and test-time sampling explicit and reconcile them in the aggregation rule.

## Example Output

```markdown
## Task & Temporal Unit
Action recognition: one of 12 activity labels per ~8s trimmed clip. Label unit = clip.

### Temporal Signal Analysis
Several classes ("sitting down" vs "standing up") differ only by motion direction →
motion is decisive. Events span most of the clip → moderate sampling is adequate.

### Sampling Strategy
- Train: 1 random 16-frame clip/video, stride 4, 224px, random temporal crop.
- Test: 5 uniformly spaced 16-frame clips/video, averaged logits → video prediction.

### Architecture Options
| Family | Fit | Cost |
|--------|-----|------|
| Frame-agg (TSN-style) | Baseline; weak on motion direction | Low |
| 3D CNN | Good motion capture | Medium |
| Two-stream RGB+flow | Best when motion decisive | High (flow precompute) |
| Video transformer | Needs more data/compute | High |

### Supervision & Heads
Clip-level softmax over 12 classes, cross-entropy. No localization head needed.

### Evaluation Protocol
Splits grouped by source recording ID. Metric: clip accuracy + macro-F1.
Baseline to beat: frame-agg average pooling. All numbers: measure on your data.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Ordered steps walk task definition → signal analysis → sampling → architecture → evaluation.
- **RT-02 (Multi-Dimensional Analysis Framework):** Each design choice is bound to a stated data property rather than asserted.
- **CM-02 (Constraint Specification):** Temporal-modeling families are presented as a tradeoff table, not a single pick.
- **DS-01 (Framework Application):** The brief enforces named sections for reproducible design capture.
- **QA-12 (False Positives Identification):** Explicit checks force video-grouped splits and unit-correct metric reporting.

**Related Prompts:**
- `cv_task_framing.md` — covers single-image task definition when temporal modeling is unnecessary.
- `cv_augmentation_strategy.md` — designs spatial/temporal augmentation policies for video and image data.
- `cv_transfer_learning_pretrained_selection.md` — selects pretrained backbones, including video and inflated-image models.
