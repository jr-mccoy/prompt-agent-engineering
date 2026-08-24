---
title: "Electrophysiology Protocol Designer"
category: science/disciplines/neuroscience
description: "Design an in-vivo / in-vitro electrophysiology experiment: recording configuration, controls, artifact rejection, spike-sorting / waveform validation, and pre-specified analysis"
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-02
  - QA-02
difficulty: advanced
tags:
  - electrophysiology
  - patch-clamp
  - in-vivo
  - silicon-probes
  - spike-sorting
  - artifact-rejection
  - waveform-validation
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/neuroscience/neuro_animal_behavior_experiment_designer.md
  - domain-science/disciplines/neuroscience/neuro_circuit_perturbation_experiment_designer.md
---

# Electrophysiology Protocol Designer

**Objective:** Design an electrophysiology experiment (whole-cell patch-clamp, sharp electrode, extracellular single-unit, multi-electrode array, silicon-probe, Neuropixels, ECoG, LFP, EMG) with a recording configuration matched to the question, explicit controls and artifact-rejection rules, spike-sorting / waveform-validation steps, and a pre-specified analysis plan.

**When to use:** Before any pilot rig session, when the user has a neural-circuit question requiring direct recording. Useful also for post-hoc audit when a dataset is yielding results that vanish under more careful analysis.

**Required inputs:**
- **Preparation.** Acute slice, organotypic culture, dissociated culture, anesthetized in-vivo, awake head-fixed, freely behaving, human intracranial.
- **Cell / region.** Brain region, layer / sub-region, cell type identification strategy.
- **Recording mode.** Whole-cell current-clamp / voltage-clamp; cell-attached; perforated; loose-patch; extracellular single-unit; LFP; multi-unit; high-density probe; tetrode; chronic vs. acute.
- **Question.** Single-cell intrinsic properties; synaptic input; circuit-level coding; population dynamics; oscillation; coupling; plasticity.
- **Stimulation / perturbation, if any.** Step current, ramp, oscillation, sensory, optogenetic, chemogenetic, electrical, behavioral.
- **Throughput.** Cell yield, session length, day count.

**Optional inputs:**
- Genetic targeting (Cre line, viral approach).
- Post-hoc identification (biocytin fill, immuno).
- Concurrent imaging / behavioral monitoring.
- Existing dataset for benchmarking.

**Constraints — Must:**
- Match recording mode to question. Patch for synaptic / intrinsic; extracellular for population / behavior-locked; high-density for circuit; chronic for learning / longitudinal.
- Pre-specify cell-acceptance criteria for patch: access resistance threshold (e.g., Rs < 25 MΩ; or < 20% change over trial); holding current; resting potential; spike width; capacitance; leak. For extracellular: SNR threshold; isolation distance / L-ratio; refractory-period contamination ceiling.
- Pre-specify artifact rejection: 60 Hz line noise (notch only when justified); cardiac / breathing pulsation; mechanical movement; saturated channels; stim-artifact handling for optogenetic / electrical stim.
- For spike sorting: name the algorithm (Kilosort version + post-curation tool such as Phy / SpikeInterface; MountainSort; JRClust); pre-specify automated and manual curation criteria; validate against ground truth (cross-correlogram refractoriness, waveform stability across time, drift correction).
- For LFP / oscillations: pre-specify referencing scheme (CAR, bipolar, white-matter ref), band-pass filters with order and zero-phase requirement, time-frequency method (Morlet wavelet / multi-taper / Hilbert).
- For optogenetic stimulation: report opsin, expression strategy, wavelength, irradiance at tissue, pulse parameters; quantify off-target heating / direct excitation if needed.
- Align reporting to MIBBI / Brain Imaging Data Structure for iEEG / NWB (Neurodata Without Borders) data format; FAIR for deposit; relevant standards (NWB:N, DANDI archive).

**Constraints — Must Not:**
- Do not invent access-resistance thresholds, SNR thresholds, isolation-distance values, or opsin / virus catalog numbers.
- Do not change Rs / SNR thresholds after seeing data.
- Do not interpret a multi-unit cluster as a "single unit" without isolation diagnostics.
- Do not rely on automated spike-sorting output without curation in current practice.
- Do not pool cells across animals as if independent without modeling the hierarchy.
- Do not silently drop trials with stimulation artifact unless rule pre-specified.

**Instructions:**

1. **Lock question and recording mode.** State the question and pick the mode (patch / single-unit / high-density / LFP / ECoG / EMG / combination). Justify briefly.

2. **Targeting and cell identification.** For patched cells: visual identification + post-hoc fill + cytochemistry / opto-tagging. For in-vivo single-units: laser-tagging via Cre-dependent opsin; antidromic activation; juxtacellular labeling; optotagging waveform / latency criteria.

3. **Recording rig configuration.** Probe geometry / patch pipette resistance; amplifier (Multiclamp / Axopatch / Intan / Open Ephys / SpikeGLX); filters; sampling rate (≥20 kHz for spikes, ≥1 kHz for LFP, ≥10 kHz for fast events); grounding / shielding.

4. **Acceptance criteria, pre-specified.** Patch: Rs, holding current, RMP, leak, % Rs change. Extracellular: SNR, ISI violation %, isolation distance, L-ratio, drift over time. State thresholds *before* any data.

5. **Stimulation / perturbation protocol.** Step / ramp / oscillation / synaptic / optogenetic / chemogenetic specifics. State intensity / duration / inter-trial interval. For optogenetic: opsin, wavelength, irradiance at tissue, pulse parameters, total light exposure, control-light condition. Mark numeric values `[user-supplied]`.

6. **Artifact rejection.** Per signal type: line-noise handling; movement; saturation; stimulation artifact (blanking, template subtraction, channel exclusion). Pre-specified.

7. **Spike sorting and waveform validation.** Algorithm + version (Kilosort 4 / SpikeInterface / etc.). Automated curation thresholds. Manual curation per unit. Drift correction. Cross-correlogram refractoriness. Waveform stability over time. Unit-yield report.

8. **Pre-specified analysis.** Per question: trial-aligned PSTH; tuning curves; firing-rate distributions; cross-correlations; coherence; phase-locking value; STA; decoding; mixed-effects with unit nested in animal. State the random-effects structure; state multiple-comparisons across units / conditions.

9. **Sample sizes and yield expectations.** State expected cells / units per animal; minimum cell / unit count for the primary analysis; minimum animal count.

10. **Reproducibility artifacts.** Raw + spike-sorted data in NWB; deposit on DANDI; analysis code committed; recording sessions logged with rig conditions and operator.

**Output format (locked):**

```
## Question and recording mode
- Question:
- Mode:
- Justification:

## Targeting / cell ID
- Strategy:
- Post-hoc identification:
- Optotagging criteria (if used):

## Rig configuration
| Element | Value (or [user-supplied]) |

## Pre-specified acceptance criteria
| Metric | Threshold | Action if violated |

## Stimulation / perturbation
| Param | Value (or [user-supplied]) |

## Artifact rejection
| Source | Method | Pre-specified rule |

## Spike sorting and validation
- Algorithm + version:
- Automated curation:
- Manual curation steps:
- Drift correction:
- Waveform-stability check:

## Pre-specified analysis
- Primary analysis:
- Random-effects structure (unit-in-animal):
- Multiple-comparisons:
- Pre-specified vs. exploratory:

## Sample sizes / yield expectations
- Expected per animal:
- Minimum for primary analysis:

## Reproducibility artifacts
- Data format (NWB):
- Deposit (DANDI / Zenodo):
- Code commit:
- Session log fields:

## Reporting standard alignment
[NWB:N / DANDI / FAIR / ARRIVE 2.0 for animal handling]

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** Neurodata Without Borders (NWB:N) data format; DANDI archive; BIDS-iEEG for human intracranial; ARRIVE 2.0 for animal handling; FAIR for deposit; relevant journal data-availability statements.

**Verification checklist:**
- [ ] Recording mode matches the question type.
- [ ] Acceptance criteria pre-specified with numeric thresholds.
- [ ] Spike-sorting algorithm + version named and curation specified.
- [ ] Artifact-rejection rules pre-specified.
- [ ] Optogenetic / electrical stim parameters listed (or `[user-supplied]`).
- [ ] Random-effects structure correctly nests unit within animal.
- [ ] NWB / DANDI deposit plan stated.
- [ ] No invented catalog numbers / virus titers / opsin IDs.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Rs drift undetected | Spike rate "increases" with deterioration | Pre-specified Rs change ceiling |
| Multi-unit treated as single | "Place cell" that is two cells | Isolation distance + ISI |
| Sorter drift across hours | Same unit split into two clusters | Drift correction |
| Stim-artifact contamination | Apparent spikes after light onset | Blanking / artifact handling |
| Off-target opsin activation | "Cell-specific" effect from leaky expression | Control-line / off-target tests |
| Inflated unit count from poor cluster splits | More units than physically plausible | Manual curation + benchmark |
| Pooling cells across animals as if independent | Variance under-estimated | Mixed model with animal random effect |
| Post-hoc SNR threshold | Threshold adjusted to retain enough cells | Pre-specified |
| Invented opsin / virus parameters | Plausible-looking titer / wavelength | `[user-supplied]` |
| No deposit plan | Data lives on a lab drive | NWB + DANDI required |
