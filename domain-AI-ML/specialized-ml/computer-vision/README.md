# Computer Vision

Vision tasks from framing through annotation, augmentation, and evaluation, plus the four modalities that behave differently enough to need their own treatment — video, 3D/point cloud, OCR, and medical imaging.

**10 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Framing a vision task, or deciding how to annotate for it.
- Detection or segmentation evaluation is giving numbers nobody trusts.
- The input is video, 3D, scanned documents, or medical imagery.

**Not here:**
- The task is generative image synthesis → `domain-image-generation/`.
- The concern is clinical validity rather than modelling → `domain-healthcare-clinical/`.

## Prompts

| Prompt | Use it to |
|---|---|
| [`cv_task_framing.md`](cv_task_framing.md) | Translate a fuzzy vision goal into a concrete CV task type (classification / detection / segmentation / keypoint) and derive the label format, metric, and data implications each choice forces. |
| [`cv_annotation_strategy.md`](cv_annotation_strategy.md) | Design an image/video annotation strategy — label schema, annotation guidelines, edge-case rules, quality control, and tooling — that produces consistent labels matched to the task and metric. |
| [`cv_augmentation_strategy.md`](cv_augmentation_strategy.md) | Choose image/video augmentations that genuinely improve robustness to deployment conditions without breaking label validity, distorting class semantics, or creating train/serve mismatch. |
| [`cv_transfer_learning_pretrained_selection.md`](cv_transfer_learning_pretrained_selection.md) | Select a pretrained backbone and adaptation strategy (linear probe / partial fine-tune / full fine-tune) for a vision task with limited data, matching domain gap, data volume, and compute to the right approach. |
| [`cv_object_detection_eval.md`](cv_object_detection_eval.md) | Evaluate an object detector correctly — mAP across IoU thresholds, per-class and per-size breakdowns, confidence/NMS effects, and the small-object and class-imbalance pitfalls that hide behind a single headline number. |
| [`cv_segmentation_approach.md`](cv_segmentation_approach.md) | Choose between semantic, instance, and panoptic segmentation for a task and design its evaluation (IoU/Dice/PQ) with boundary precision, class imbalance, and small-region pitfalls accounted for. |
| [`cv_video_understanding_design.md`](cv_video_understanding_design.md) | Design a video-understanding approach — clip/frame sampling, temporal modeling (3D CNN, two-stream, video transformer, or frame-aggregation), task framing (action recognition, temporal action localization, video classification), and leakage-safe evaluation — matched to the data's temporal structure, label granularity, and compute budget. |
| [`cv_3d_point_cloud_design.md`](cv_3d_point_cloud_design.md) | Choose a 3D representation (voxel grid, raw point set, mesh, multi-view projection, or range image) and design for permutation and rotation invariance, sensor fusion (LiDAR + camera), and density/sampling — matched to the sensor, task, and compute budget, with scan-overlap-aware evaluation. |
| [`cv_ocr_pipeline_design.md`](cv_ocr_pipeline_design.md) | Design a detect → recognize → post-process OCR pipeline with layout/structure recovery, language/script coverage, and CER/WER-based evaluation — matched to the document types, scripts, and downstream consumers, with template-overfit-aware splits. |
| [`cv_medical_imaging_considerations.md`](cv_medical_imaging_considerations.md) | Design a medical-imaging modeling approach with DICOM/modality handling, patient-level splits to prevent leakage, class imbalance and external validation strategy, and regulatory / no-diagnostic-claim guardrails — framework-neutral and grounded in the user's data. |

## Conventions

- **Prefix:** `cv_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/specialized-ml/computer-vision`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- Adversarial robustness for vision models → [`../../model-security/mlsec_adversarial_robustness_assessment.md`](../../model-security/mlsec_adversarial_robustness_assessment.md).
- CV incident patterns in production → [`../../production-monitoring/mlmonitor_cv_incident_patterns.md`](../../production-monitoring/mlmonitor_cv_incident_patterns.md).
