---
title: "Medical Imaging Modeling Considerations"
category: AI-ML/specialized-ml/computer-vision
description: "Design a medical-imaging modeling approach with DICOM/modality handling, patient-level splits to prevent leakage, class imbalance and external validation strategy, and regulatory / no-diagnostic-claim guardrails — framework-neutral and grounded in the user's data."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-01
  - QA-12
difficulty: advanced
tags:
  - computer-vision
  - medical-imaging
  - patient-level-splits
  - external-validation
  - regulatory
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/computer-vision/cv_task_framing.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_segmentation_approach.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_transfer_learning_pretrained_selection.md
---

# Medical Imaging Modeling Considerations

**Objective:** Help the user design a medical-imaging model with the methodological guardrails this domain demands, where ordinary CV shortcuts produce dangerously optimistic results. The decisions are how to handle DICOM and modality-specific intensities (windowing, normalization, 2D slices vs. 3D volumes), how to split data at the patient level so no patient's slices or studies appear in both train and test, how to handle class imbalance (rare findings) without distorting reported performance, and how to validate externally on a different site/scanner rather than trusting a single-source split. Equally important is staying within scope: this prompt produces a research/engineering design — not a diagnostic or medical-device claim — and flags where regulatory review applies. The output is framework-neutral and grounded in the user's own data.

**When to Use:**
- You are building a model on medical images (radiology, pathology, ophthalmology, dermatology) and need a methodologically sound design.
- You must split data correctly across patients and validate beyond a single source.
- You need to surface the regulatory and scope guardrails before training begins.

**When NOT to Use:**
- The task is non-medical image understanding — use `cv_task_framing.md`.
- You need a generic segmentation head/loss design — see `cv_segmentation_approach.md` (apply the patient-split rule here too).
- You need to select a pretrained backbone in isolation — see `cv_transfer_learning_pretrained_selection.md`.

## Inputs / Context

Provide what you can:
- **Modality & format** — CT/MR/X-ray/ultrasound/pathology WSI; DICOM metadata available?
- **Task definition** — classification, detection, segmentation; per-image, per-study, or per-patient label.
- **Patient/study grouping** — patient ID, study/series ID, scanner, site — required for leakage-safe splits.
- **Class distribution** — prevalence of the finding; how rare are positives?
- **Data sources** — single site/scanner or multiple; availability of an external validation set.
- **Intended use & scope** — research, decision support, screening — and whether any deployment is contemplated.
- **Ground-truth provenance** — who labeled, reader agreement, reference standard.

## Constraints

**Must:**
- Split strictly at the patient level so no patient's slices or studies cross train/val/test boundaries.
- Specify modality-appropriate preprocessing (DICOM windowing/normalization) tied to the imaging type.
- Plan external validation on a different site/scanner, or explicitly flag its absence as a limitation.
- State the regulatory scope and treat outputs as research/engineering design, not clinical claims.

**Must Not:**
- Produce a medical-device, diagnostic, or clinical-performance claim; flag where regulatory review (e.g., device classification) applies and stay within research/engineering scope.
- Fabricate sensitivity, specificity, AUC, or benchmark numbers from memory; reason from the user's data and mark unknowns "measure on your data."
- Assert version-specific API behavior of any imaging/DL library from memory — flag "verify against current docs."
- Allow slices or studies of one patient to appear in both train and test, or report metrics from single-source data as if externally validated.

**Instructions:**

1. **Restate the task, label unit, and intended use.** Clarify the prediction unit (image/study/patient) and confirm scope is research/engineering — not a diagnostic claim. Flag any deployment contemplation for regulatory review.
2. **Handle modality and DICOM.** Specify windowing/normalization and 2D-slice vs. 3D-volume handling appropriate to the modality. Note metadata (spacing, orientation) that must be respected.
3. **Define patient-level splits.** Require grouping by patient ID so all of a patient's slices/studies stay on one side of every split. Make this the non-negotiable first step before any sampling.
4. **Address class imbalance.** Choose handling (resampling, loss weighting, threshold tuning) and ensure prevalence-aware metrics (e.g., PR-AUC, sensitivity at fixed specificity) rather than raw accuracy on rare findings.
5. **Plan external validation.** Specify an out-of-distribution test from a different site/scanner. If unavailable, document this as a limitation and avoid generalization claims.
6. **Ground the reference standard.** Note labeler qualifications, reader agreement, and the reference standard, since metric meaning depends on label quality.
7. **Set transfer and augmentation carefully.** Decide pretraining source (natural-image vs. domain) and augmentations that preserve clinically meaningful features; avoid augmentations that fabricate or destroy diagnostic cues.
8. **Define metrics, baseline, and scope statement.** Choose prevalence-aware metrics, name a baseline, restate that results are not a clinical claim, and flag all numbers as "to be measured."

**Output Format:**

A markdown design brief:
- **Task, Label Unit & Intended Use** — restated task and explicit research/engineering scope.
- **Modality & DICOM Handling** — windowing, normalization, 2D/3D, metadata.
- **Patient-Level Split Plan** — grouping rule and verification.
- **Class Imbalance Strategy** — handling and prevalence-aware metrics.
- **External Validation Plan** — OOD test source, or documented limitation.
- **Reference Standard** — label provenance and agreement.
- **Transfer & Augmentation** — pretraining and clinically safe augmentations.
- **Metrics, Baseline & Scope Statement** — metrics, baseline, no-diagnostic-claim note, regulatory flag.
- **Open Questions / Measure-On-Your-Data** — unknowns flagged for empirical resolution.

## Verification

- [ ] Splits are grouped by patient ID; no patient's slices or studies cross train/val/test.
- [ ] Preprocessing is modality-appropriate (DICOM windowing/normalization, 2D/3D) and specified.
- [ ] Class imbalance is handled and metrics are prevalence-aware, not raw accuracy on rare findings.
- [ ] External validation on a different site/scanner is planned, or its absence is flagged as a limitation.
- [ ] The output is framed as research/engineering with no diagnostic/medical-device claim, and regulatory scope is flagged.
- [ ] No sensitivity/specificity/AUC or benchmark numbers are invented and no version-specific API behavior is asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Split slices or studies randomly so the same patient appears in both train and test — patient-level leakage inflates every metric.
- Report single-site performance as evidence the model generalizes, with no external/prospective validation.
- Make or imply a diagnostic or clinical-performance claim from an internal research metric.
- Use raw accuracy on a rare-finding dataset, masking poor sensitivity on the positive class.

✅ **DO:**
- Group every split by patient ID first, and verify no patient ID spans splits.
- Validate on an out-of-distribution site/scanner and state the limitation if you cannot.
- Keep outputs scoped as research/engineering and flag where regulatory (device) review would be required.
- Use prevalence-aware metrics (PR-AUC, sensitivity at fixed specificity) for imbalanced findings.

## Example Output

```markdown
## Task, Label Unit & Intended Use
Chest X-ray finding classification; per-study label. Scope: research only — NOT a diagnostic claim.
Any deployment would require regulatory review (device classification flagged).

### Modality & DICOM Handling
Apply standard window/level, normalize per-image; 2D study-level model; respect pixel spacing.

### Patient-Level Split Plan
Group by patient ID; verify zero patient overlap across train/val/test before sampling.

### Class Imbalance Strategy
Positive prevalence ~4%. Loss weighting + threshold tuning; report PR-AUC and sensitivity@95% specificity.

### External Validation Plan
Hold out a second hospital's scanner as OOD test. (If unavailable: documented as a key limitation.)

### Metrics, Baseline & Scope Statement
PR-AUC, sensitivity at fixed specificity. Baseline: ImageNet-pretrained backbone.
Results are research metrics, not clinical performance. All numbers: measure on your data.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Ordered steps move task/scope → DICOM → patient splits → imbalance → external validation → metrics.
- **RT-02 (Multi-Dimensional Analysis Framework):** Each design choice is bound to modality, prevalence, and scope constraints.
- **CM-02 (Constraint Specification):** Imbalance handling and transfer sources are weighed as tradeoffs.
- **DS-01 (Framework Application):** Named brief sections capture the methodologically sound design reproducibly.
- **QA-12 (False Positives Identification):** Checks enforce patient-level splits, external validation, and no-diagnostic-claim scope.

**Related Prompts:**
- `cv_task_framing.md` — frames the underlying task and label unit before modeling.
- `cv_segmentation_approach.md` — designs segmentation heads/losses; apply patient-level splits here too.
- `cv_transfer_learning_pretrained_selection.md` — selects pretrained backbones, including domain vs. natural-image sources.
