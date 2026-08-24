---
title: "Neuroimaging Analysis Plan"
category: science/disciplines/neuroscience
description: "Pre-specify a fMRI / EEG / MEG / fNIRS analysis pipeline: BIDS layout, preprocessing, model, multiple-comparison correction, and reproducibility artifacts"
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-02
  - QA-02
difficulty: advanced
tags:
  - fmri
  - eeg
  - meg
  - fnirs
  - preprocessing
  - multiple-comparisons
  - bids
  - cluster-correction
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/neuroscience/neuro_electrophysiology_protocol_designer.md
  - domain-science/disciplines/neuroscience/neuro_circuit_perturbation_experiment_designer.md
---

# Neuroimaging Analysis Plan

**Objective:** Pre-specify a human (or non-human primate) neuroimaging analysis pipeline — fMRI (task / rest / quantitative), structural MRI, dMRI, ASL, EEG, MEG, fNIRS — including BIDS data layout, preprocessing pipeline with version pinning, statistical model, multiple-comparisons strategy, and reproducibility artifacts. The plan should be lockable before any analyses are run on the actual data, in line with current open and replicable-neuroimaging practice.

**When to use:** Before submitting a registered report; before unblinding a study; when responding to NeuroImage / Imaging Neuroscience / eLife replication-and-reproducibility reviewer requests; when porting a pipeline across labs.

**Required inputs:**
- **Modality.** fMRI task / rest; sMRI; dMRI; ASL; EEG; MEG; fNIRS.
- **Study design.** Block, event-related, mixed, resting-state, longitudinal, intervention, cross-sectional.
- **Sample.** N, demographics, sub-populations, exclusion thresholds.
- **Research question.** Detection (where), magnitude (how strong), connectivity (pattern), prediction (individual differences).
- **Available tools.** fMRIPrep / SPM / AFNI / FSL / MNE / EEGLAB / FieldTrip / Brainstorm / QSIPrep / dcm2niix / nipype / BIDS apps.
- **Computational budget.**

**Optional inputs:**
- Prior effect-size estimate (user-supplied).
- Whether the lab uses surface-based vs. volume-based analysis.
- Whether the eventual report is a registered report.

**Constraints — Must:**
- Use BIDS for the data layout. Specify the BIDS version. Specify the validation step.
- Pin pipeline versions (container hash for fMRIPrep / QSIPrep / MRIQC; toolbox version for SPM / FSL / AFNI / MNE; software dependencies). Commit a Docker / Singularity / Apptainer image or a reproducible environment file.
- Pre-specify motion / quality exclusion thresholds before unblinding: framewise displacement threshold; percentage of volumes scrubbed; QC-FC correlation acceptance; electrode-impedance threshold; minimum trial counts post-rejection.
- Pre-specify the statistical model in full: contrasts, covariates, mixed-effects structure, smoothing, baseline. Distinguish first-level and group-level.
- Pre-specify multiple-comparisons strategy with method *and* threshold: voxel-wise + cluster-wise (and cluster-defining threshold); TFCE; FDR; permutation; non-parametric. Explicitly choose; do not list options.
- For EEG / MEG: pre-specify time-window of interest, region / channel cluster, frequency band, baseline correction window, and statistical test (cluster-based permutation, F-test, t-test with correction).
- For connectivity (functional or structural): pre-specify atlas, ROI definition, whether seed-based / ICA / graph-theoretic, whether thresholded.
- For prediction / classification: pre-specify cross-validation scheme (subject-stratified k-fold; nested CV; leave-one-site-out), feature selection (only inside CV folds), performance metric, and chance-baseline test (permutation null).
- Align reporting to COBIDAS (fMRI) / COBIDAS-MEEG (EEG / MEG) / BIDS / OHBM Open Science / FAIR.

**Constraints — Must Not:**
- Do not invent fMRIPrep / FSL / SPM version numbers or atlas names.
- Do not mix surface-based and volume-based pipelines silently.
- Do not apply double-dipping (define ROI on the same data used to test it).
- Do not change motion threshold after seeing the data.
- Do not report voxel-wise p < 0.001 uncorrected as evidence.
- Do not propose mass-univariate testing without an explicit multiple-comparisons method.
- Do not perform feature selection outside cross-validation folds.
- Do not silently drop subjects without a pre-specified rule.

**Instructions:**

1. **Lock the inference goal.** Detection (where the effect is), magnitude (effect-size estimation), pattern / connectivity, individual-difference prediction, or longitudinal change. The pipeline differs by goal.

2. **Data layout in BIDS.** Specify directory structure; required JSON sidecars; events.tsv content; phenotype files; deface / anonymization plan; BIDS-Validator step; storage location with access controls.

3. **Pre-registration block.** Hypothesis, primary contrast, ROI / whole-brain / cluster-defining threshold, multiple-comparisons method and threshold, motion-exclusion threshold, minimum-trial-count threshold, planned post-hoc analyses (labeled exploratory), planned sensitivity analyses.

4. **Preprocessing pipeline.** Pin the version (fMRIPrep 24.x with container hash; SPM12 r####; AFNI YY.MM.DD; FSL 6.x.x; MNE 1.x). Specify each step: distortion correction, motion correction, slice-timing, coregistration, normalization (template + space), smoothing kernel (matched to inference goal — small for prediction, larger for univariate detection). For EEG / MEG: filtering, ICA, artifact rejection, epoching, baseline correction.

5. **Quality control.** MRIQC / MNE / EEGLAB QC report per subject. Specify thresholds and how subjects are excluded. Store QC artifacts.

6. **Statistical model.** First-level: HRF model, nuisance regressors (motion, physiological, CompCor), temporal filtering. Group-level: mixed-effects, random effects, covariates (age, sex, site, scanner, head motion summary). Contrasts: pre-specified primary, pre-specified secondary, exploratory clearly labeled.

7. **Multiple-comparisons control.** Choose: cluster-based permutation (e.g., FSL randomise, AFNI 3dClustSim with ACF, SPM via PALM, MNE permutation cluster); TFCE; FDR. State cluster-defining threshold (e.g., p < 0.001 for cluster permutation per Eklund et al. 2016). For EEG / MEG: cluster-based permutation in the chosen time × frequency × space domain.

8. **ROI strategy (if any).** Pre-specified atlases (HCP-MMP, Schaefer, AAL, Glasser, Destrieux, Brodmann surrogates). Functional ROI only via independent data (leave-one-subject-out or independent localizer). No double dipping.

9. **Connectivity / prediction (if relevant).** Atlas-based or voxel-based; correlation / partial / dynamic / graph metrics; CV scheme for prediction (subject-stratified); chance baseline via permutation.

10. **Reproducibility artifacts.** Container image; commit pipeline scripts; deposit derivatives to NeuroVault / OpenNeuro / IDA / Zenodo; data-sharing posture compliant with consent; provenance via BIDS-Apps; long-form methods paragraph ready for paper.

**Output format (locked):**

```
## Inference goal
- Type (detection / magnitude / connectivity / prediction / longitudinal):

## BIDS data layout
- BIDS version + validator:
- Sidecars / events / phenotype:
- Anonymization / deface:
- Storage / access:

## Pre-registration block
- Hypothesis + primary contrast:
- Multiple-comparisons method + threshold:
- Motion / QC exclusion thresholds:
- Minimum trial counts:
- Exploratory labels:

## Preprocessing pipeline
- Toolbox + version (container hash):
- Steps in order:
- Smoothing kernel matched to goal:
- Modality-specific (EEG / MEG / fMRI / dMRI / ASL):

## Quality control
- Tool:
- Thresholds:
- Storage of QC artifacts:

## Statistical model
- First-level (regressors, contrasts):
- Group-level (mixed-effects, covariates):
- Pre-specified contrasts:
- Exploratory contrasts:

## Multiple-comparisons control
- Method + threshold:
- Software call:

## ROI strategy
- Atlas / functional ROI source:
- Double-dipping safeguard:

## Connectivity / prediction (if relevant)
- Atlas / metric:
- CV scheme:
- Chance baseline:

## Reproducibility artifacts
- Container image:
- Code commit:
- Deposit (NeuroVault / OpenNeuro / IDA / Zenodo):
- Methods paragraph ready:

## Reporting standard alignment
[COBIDAS / COBIDAS-MEEG / BIDS / FAIR / OHBM Open Science]

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** COBIDAS (fMRI) and COBIDAS-MEEG (EEG / MEG); BIDS specification; OHBM Open Science / Committee on Best Practice; Eklund et al. 2016 recommendations on cluster correction; FAIR principles; OpenNeuro / NeuroVault / IDA deposit conventions.

**Verification checklist:**
- [ ] Inference goal stated.
- [ ] BIDS layout + validator step specified.
- [ ] Pipeline versions pinned via container or environment file.
- [ ] Motion / QC thresholds pre-specified.
- [ ] Multiple-comparisons method + threshold named explicitly (not "depending on results").
- [ ] No double-dipping in ROI definition.
- [ ] CV scheme + chance baseline for prediction tasks.
- [ ] Reproducibility artifacts (container, code, deposit) listed.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Voxel-wise p < .001 uncorrected | Reported as significance | Cluster / FDR / permutation required |
| Double dipping | ROI defined on test data | Independent ROI source enforced |
| Inflated cluster significance | Old-school cluster correction not corrected for spatial smoothness | Per Eklund et al.; permutation default |
| Motion-threshold p-hacking | FD threshold adjusted post-hoc | Threshold pre-specified |
| Subject-leakage in CV | Same subject in train and test | Subject-stratified CV |
| Feature selection outside CV | Pre-CV reduction inflates accuracy | Inside-fold only |
| Smoothing mismatch with goal | 8 mm smoothing for multivariate decoding | Goal-matched kernel |
| Mixed surface / volume silently | Group analysis on different bases | Pipeline consistency enforced |
| Invented tool version | Plausible-looking FSL 6.0.7.3 | Container hash pin |
| Site / scanner confound | Multi-site without harmonization (ComBat / longCombat) | Covariate or harmonization required |
