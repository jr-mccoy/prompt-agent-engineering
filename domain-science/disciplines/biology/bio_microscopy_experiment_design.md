---
title: "Microscopy Experiment Design"
category: science/disciplines/biology
description: "Design a quantitative microscopy experiment with modality selection, controls, sampling strategy, and pre-specified image-analysis plan resistant to selection bias"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - microscopy
  - imaging
  - image-analysis
  - quantification
  - controls
  - selection-bias
updated: "2026-05-19"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/disciplines/biology/bio_omics_study_metadata_planner.md
---

# Microscopy Experiment Design

**Objective:** Produce a quantitative microscopy experimental design that names the imaging modality, controls for the dominant artifacts of that modality, defines a sampling strategy resistant to field-of-view selection bias, and pre-specifies the segmentation and quantification pipeline before any images are acquired.

**When to use:** Before booking instrument time, when the user has a biological question that requires imaging and needs to demonstrate that the chosen modality, sampling, and analysis pipeline can support the claim they intend to make.

**Required inputs:**
- **Biological question** as a testable claim, including the spatial scale (sub-cellular, cellular, tissue, organ).
- **Specimen type.** Live, fixed, cleared, sectioned (thickness), or whole-mount.
- **Available modalities.** Widefield, confocal, two-photon, light-sheet, super-resolution (STED / SIM / SMLM), TIRF, electron, lattice, expansion. The user lists what is accessible.
- **Labels / markers** (with claim that user supplied — do not invent validated antibody clones).
- **Throughput constraint.** How many specimens, fields, time points feasible.
- **Quantification endpoint.** Count, intensity, ratio, colocalization, morphology, dynamics, etc.

**Optional inputs:**
- Prior microscopy of the system (user-supplied).
- Anticipated effect size (fold-change, percentage difference).
- Computational segmentation tools available.
- Whether comparison is between groups, across time, or both.

**Constraints — Must:**
- Match modality to spatial-temporal scale required by the question. State the resolution limit (lateral and axial) of the proposed modality numerically.
- Distinguish between biological replicate (independent animal / culture / preparation), technical replicate (re-imaging the same sample), and field-of-view replicate (multiple FOVs per specimen). Power is computed on biological replicates.
- Pre-specify how fields of view are sampled (systematic random, unbiased stereology, exhaustive tiling, random grid). Forbid "representative field" selection by the imager.
- Pre-specify whether the imager and the analyst are blinded to condition; if not blinded, justify and surface the bias.
- Pre-specify the segmentation / quantification pipeline (manual, semi-automated, automated; thresholding strategy; smoothing; deconvolution settings) including the random seed if applicable.
- For super-resolution, name the validation strategy (Fourier ring correlation, multi-color cross-validation, paired comparison to conventional).

**Constraints — Must Not:**
- Do not propose "representative image" claims without a sampling strategy that justifies representativeness.
- Do not propose colocalization analysis without specifying the metric (Pearson, Mander's M1/M2, Costes randomization-tested) and the chance-baseline control.
- Do not propose intensity comparisons across imaging sessions without inter-session calibration (beads, reference slide, or calibrated source).
- Do not propose pixel-level statistics on adjacent pixels as if independent samples.
- Do not recommend a specific commercial probe / antibody / staining kit; let the user supply.

**Instructions:**

1. **Map the question to the required spatial and temporal scale.** Output a small table: phenomenon size / duration → minimum resolving power → which modalities qualify. If the user's accessible list is incompatible, surface it.

2. **Specimen preparation plan.** Specify fixation (PFA vs. methanol vs. live), permeabilization, blocking, labeling, mounting, refractive-index matching (if relevant), and clearing protocol category (if relevant) at the level of *what choices the user must make* — not specific concentrations unless the user supplies them.

3. **Modality decision.** From the user's accessible list, recommend one primary modality and at most one fallback. For each, list resolution (xy, z), penetration depth, phototoxicity / bleaching, throughput, and the dominant artifact class. Match against the question.

4. **Controls.** Specify the control panel: unlabeled (autofluorescence), single-label (bleed-through), secondary-only (non-specific), beads (PSF / chromatic registration), reference slide (intensity calibration), positive biological control, negative biological control, no-primary-antibody, knockout / knockdown if available. Mark which are mandatory vs. recommended.

5. **Sampling strategy.** Define the unit of analysis and the sampling level it lives in (specimen → section → field → cell → sub-cellular ROI). Build a worked example: how many biological replicates × sections × fields × cells. State the sampling rule (systematic random, exhaustive, etc.) and forbid representative-field selection in writing.

6. **Acquisition settings, pre-specified.** Lock pixel size (sampling vs. Nyquist), bit depth, gain, laser power, dwell time, frame averaging, z-step, time interval, and time of total exposure. Specify what is allowed to vary between samples and what must be identical.

7. **Image-analysis pipeline, pre-specified.** Specify each stage: pre-processing (denoising, deconvolution, flat-field), segmentation (method and parameters), feature extraction, statistical comparison. Specify the random seed for stochastic steps. Specify the QC criteria for excluding individual cells / fields / specimens after acquisition.

8. **Power and effect size.** Compute or sketch the required biological-replicate count for the chosen effect-size assumption. If the user has not supplied an effect-size anchor, ask or mark `[user-supplied]`.

9. **Pitfalls and validation.** Enumerate the 4–6 most likely failure modes for the chosen modality (phototoxicity, bleaching, refractive-index mismatch, chromatic aberration, sampling bias, segmentation failure on edge cases) and the validation that would detect each.

**Output format (locked):**

```
## Question and required scale
[claim + spatial/temporal scale → resolution requirement]

## Modality decision
| Modality | Lateral / axial resolution | Throughput | Dominant artifact | Suitable? |

## Specimen preparation choice points
[what user must decide, not specific protocol]

## Controls panel
| Control | Purpose | Mandatory? |

## Sampling strategy
- Unit of analysis:
- Replication levels (biological / technical / FOV):
- Sampling rule:
- Per-specimen count:

## Acquisition settings (pre-specified)
| Parameter | Value | Allowed to vary? | Rationale |

## Image-analysis pipeline (pre-specified)
1. Pre-processing:
2. Segmentation method + params:
3. Feature extraction:
4. Per-cell QC inclusion criteria:
5. Statistical comparison:
6. Random seed (if any):

## Power
| Scenario | N biological replicates | Effect size assumption | Power |

## Pitfalls and validation
| Failure mode | How detected | Mitigation |

## Reporting standard alignment
[QUAREP-LiMi for quality reporting, MIBBI for metadata, journal-specific]

## Open questions for the user
[gaps marked [user-supplied] above]
```

**Reporting-standard alignment:** Align to QUAREP-LiMi guidelines for microscopy quality reporting and the relevant MIBBI components (e.g., MISFISHIE for FISH). For super-resolution, align to community-of-practice recommendations on resolution-claim reporting.

**Verification checklist:**
- [ ] Resolution requirement of the question is stated numerically and matched against the chosen modality.
- [ ] Sampling rule is named and forbids "representative field" selection.
- [ ] Biological vs. technical vs. FOV replication is distinguished.
- [ ] Acquisition settings are locked before acquisition; allowed-to-vary column is explicit.
- [ ] Analysis pipeline pre-specifies segmentation method, parameters, and random seed.
- [ ] Per-cell / per-field QC inclusion criteria are pre-specified.
- [ ] Calibration controls (beads, reference slide) included if cross-session comparison is planned.
- [ ] No invented probes, antibodies, or kit components.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Selection bias from "representative field" choice | Beautiful images that don't reflect the specimen | Sampling rule pre-specified, no imager discretion |
| Apparent difference from acquisition drift | Treatment imaged on day 2, control on day 1 with different laser | Randomized acquisition order; reference slide each session |
| Colocalization from random overlap | Pearson > 0 interpreted as "they colocalize" | Costes randomization or equivalent chance baseline |
| Resolution overclaim | Calling something "sub-cellular structure" below the modality's diffraction limit | Resolution stated numerically, claim checked against it |
| Pixel-level pseudo-replication | N = pixels rather than N = cells or N = specimens | Unit of analysis named at top |
| Survivorship bias in time-lapse | Dead/bleached cells excluded post hoc | Inclusion criteria pre-specified; attrition reported |
| Invented antibody / kit | Plausible-looking catalog number | User-supplied only; otherwise `[user-supplied]` |
