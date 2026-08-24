---
title: "3D & Point-Cloud Model Design"
category: AI-ML/specialized-ml/computer-vision
description: "Choose a 3D representation (voxel grid, raw point set, mesh, multi-view projection, or range image) and design for permutation and rotation invariance, sensor fusion (LiDAR + camera), and density/sampling — matched to the sensor, task, and compute budget, with scan-overlap-aware evaluation."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-01
  - QA-12
difficulty: advanced
tags:
  - computer-vision
  - point-cloud
  - 3d-deep-learning
  - sensor-fusion
  - invariance
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/computer-vision/cv_task_framing.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_segmentation_approach.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_object_detection_eval.md
---

# 3D & Point-Cloud Model Design

**Objective:** Help the user pick a 3D data representation and design the invariances and fusion strategy their task actually needs, instead of forcing 3D data into a 2D-CNN shape by default. The central choice is how to represent geometry — voxel grids (regular but cubically expensive), raw point sets (efficient, unordered, requires permutation-invariant operators), meshes (connectivity-aware), multi-view projections (reuse 2D backbones, lose geometry), or range/spherical images (efficient for rotating LiDAR). On top of that sit invariance requirements (point order should never change the prediction; whether rotation invariance is needed or harmful), sensor fusion when LiDAR and camera are both available, and density/sampling decisions driven by sensor range falloff. This prompt produces a framework-neutral design with a leakage-safe evaluation plan.

**When to Use:**
- You have 3D data (LiDAR, depth/RGB-D, photogrammetry, CAD) and must choose a representation before building a model.
- Your task is 3D classification, 3D object detection, 3D semantic/instance segmentation, or registration.
- You need to decide whether and how to fuse LiDAR with camera imagery.

**When NOT to Use:**
- The task is purely 2D image understanding — use `cv_task_framing.md`.
- You already have a representation fixed and only need a 2D-style segmentation design — see `cv_segmentation_approach.md`.
- You need detection metrics design specifically — see `cv_object_detection_eval.md`.

## Inputs / Context

Provide what you can:
- **Sensor(s) & format** — LiDAR (rotating/solid-state), RGB-D, stereo, mesh/CAD; coordinate frame and units.
- **Task definition** — classification, detection (3D boxes), segmentation (point labels), or registration.
- **Point density & range** — points per scene, how density falls off with distance, and occlusion patterns.
- **Scene grouping metadata** — scan ID, drive/run ID, location — needed to prevent scan-overlap leakage.
- **Invariance requirements** — must predictions be invariant to point ordering (always) and to object rotation (task-dependent)?
- **Fusion availability** — calibrated, time-synced camera frames? Extrinsics/intrinsics known?
- **Compute & latency budget** — training hardware and whether inference is real-time (e.g., on-vehicle).

## Constraints

**Must:**
- Justify the representation choice from the sensor type, task, density, and compute budget.
- Guarantee permutation invariance for any raw-point operator (point order must not change the output).
- State explicitly whether rotation invariance is required, harmful (orientation is signal), or handled via augmentation.
- Define splits grouped so overlapping scans of the same physical scene cannot span train and test.

**Must Not:**
- Fabricate accuracy, mAP, or benchmark numbers from memory; reason from the user's data and mark unknowns "measure on your data."
- Assert version-specific API behavior of any 3D library from memory — flag "verify against current docs."
- Recommend one representation as universally best; present the tradeoff and defer to evaluation.
- Ignore permutation invariance or allow scan-overlap leakage between splits.

**Instructions:**

1. **Restate the task and output geometry.** Clarify whether the output is a per-scene label, oriented 3D boxes, per-point labels, or a transform — this constrains the representation and head.
2. **Profile the data.** Note point density, range falloff, occlusion, and coordinate frame. Sparse, range-varying LiDAR favors different representations than dense RGB-D.
3. **Compare representations.** Present voxel grids, raw point sets, meshes, multi-view projections, and range images as a tradeoff table, mapping each to the data and compute budget.
4. **Resolve invariances.** Require permutation invariance for point-set operators. Decide rotation handling: needed (canonicalize or use invariant features), harmful (preserve orientation), or approximated via rotation augmentation — and say which and why.
5. **Design sensor fusion (if applicable).** Decide early/mid/late fusion of LiDAR and camera, contingent on calibration quality and time sync. If calibration is poor, recommend validating extrinsics before fusing.
6. **Set sampling/density handling.** Specify fixed-size sampling (FPS/random) or voxelization resolution, and how to handle density variation with range. Tie the choice to memory and the operator family.
7. **Define leakage-safe evaluation.** Group splits by physical scene / drive so overlapping scans never cross splits. Specify metrics (3D IoU thresholds for detection; mIoU for segmentation) and a baseline.
8. **Pin metrics and a baseline.** Choose metrics matching the output geometry, name a simple baseline to beat, and flag all expected numbers as "to be measured."

**Output Format:**

A markdown design brief:
- **Task & Output Geometry** — restated task and prediction structure.
- **Data Profile** — density, range, occlusion, coordinate frame.
- **Representation Options** — table comparing voxel/point/mesh/multi-view/range with fit rationale.
- **Invariance Plan** — permutation handling and rotation decision with justification.
- **Sensor Fusion** — fusion stage and calibration prerequisites (or N/A).
- **Sampling & Density** — sampling/voxelization strategy and range handling.
- **Evaluation Protocol** — scene-grouped splits, metrics, IoU thresholds, baseline.
- **Open Questions / Measure-On-Your-Data** — unknowns flagged for empirical resolution.

## Verification

- [ ] The representation choice is justified by sensor, task, density, and compute.
- [ ] Permutation invariance is guaranteed for any raw-point operator.
- [ ] Rotation handling is explicitly decided (required / harmful / augmented) with a reason.
- [ ] Splits are grouped by physical scene so overlapping scans cannot leak across train/test.
- [ ] Fusion strategy names its stage and calibration prerequisites, or is marked N/A.
- [ ] No benchmark/mAP numbers are invented and no version-specific API behavior is asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Use an operator that depends on point order, making the prediction change when the same cloud is shuffled.
- Add rotation invariance reflexively when object orientation is actually the signal (e.g., upright vs. fallen).
- Split scans randomly so overlapping sweeps of the same physical scene appear in both train and test.
- Fuse LiDAR and camera without validating extrinsic calibration and time synchronization first.

✅ **DO:**
- Use symmetric (permutation-invariant) aggregation for point-set operators and test by shuffling inputs.
- Decide rotation handling from whether orientation carries task meaning, and document the choice.
- Group splits by drive/scene ID so overlapping scans stay on one side of the split.
- Confirm calibration quality before committing to a fusion stage; prefer late fusion when calibration is uncertain.

## Example Output

```markdown
## Task & Output Geometry
Outdoor LiDAR 3D object detection → oriented 3D boxes per scene.

### Data Profile
Rotating 64-beam LiDAR; ~120k points/sweep; density falls sharply past 40m; heavy occlusion.

### Representation Options
| Representation | Fit | Cost |
|----------------|-----|------|
| Voxel grid | Regular, detector-friendly | Cubic memory |
| Raw point set | Efficient, needs perm-invariant ops | Medium |
| Range image | Native to rotating LiDAR, fast | Loses some geometry |
| Multi-view | Reuse 2D backbones | Geometry loss |

### Invariance Plan
Permutation: symmetric max-pool aggregation, verified by shuffle test.
Rotation: orientation IS signal (heading) → do NOT impose rotation invariance; augment yaw lightly.

### Sensor Fusion
Camera available but extrinsics drift → late fusion of per-modality detections after calibration check.

### Evaluation Protocol
Splits grouped by drive ID (no overlapping sweeps across splits).
Metric: 3D mAP at IoU 0.5/0.7. Baseline: voxel detector. Numbers: measure on your data.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Ordered steps move task → data profile → representation → invariance → fusion → evaluation.
- **RT-02 (Multi-Dimensional Analysis Framework):** Each choice is bound to a stated sensor/task property rather than asserted.
- **CM-02 (Constraint Specification):** Representations are weighed in a tradeoff table, not reduced to one pick.
- **DS-01 (Framework Application):** Named brief sections capture the design reproducibly.
- **QA-12 (False Positives Identification):** Checks force permutation invariance and scan-overlap-grouped splits.

**Related Prompts:**
- `cv_task_framing.md` — frames the underlying task before a representation is chosen.
- `cv_segmentation_approach.md` — designs segmentation heads and losses, applicable to per-point labeling.
- `cv_object_detection_eval.md` — defines detection metrics and IoU-based matching, including 3D boxes.
