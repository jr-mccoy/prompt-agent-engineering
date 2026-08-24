---
title: "Climate Model Intercomparison Plan"
category: science/disciplines/earth-climate
description: "Plan a climate / earth-system model intercomparison: ensemble selection, baseline, signal-to-noise, signal definition, and sensitivity-decomposition strategy"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - CM-02
  - DS-02
  - QA-02
difficulty: advanced
tags:
  - climate-model
  - intercomparison
  - mip
  - ensemble
  - cmip
  - signal-to-noise
  - sensitivity
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/earth-climate/earth_remote_sensing_validation_plan.md
  - domain-science/disciplines/earth-climate/earth_field_campaign_designer.md
---

# Climate Model Intercomparison Plan

**Objective:** Plan a climate / earth-system / ocean-model intercomparison study with a defensible ensemble selection, baseline period, signal definition, signal-to-noise treatment, and a strategy for decomposing inter-model spread into structural vs. internal-variability vs. forcing-uncertainty contributions.

**When to use:** When the user has a climate / ocean / land / ice question that requires comparing model output across ensembles (CMIP6 / CMIP7 / HighResMIP / DECK / ScenarioMIP / DAMIP / CFMIP / LUMIP / GeoMIP / OMIP / CLIVAR), runs of a single model with perturbed initial conditions or perturbed parameters, or coupled vs. uncoupled configurations.

**Required inputs:**
- **Scientific question** as a testable claim with a quantitative target (e.g., "trend in zonal-mean precipitation 30°S–30°N over 1980–2020 ± uncertainty").
- **Time period** of interest (historical / scenario / specific window).
- **Variable(s)** and frequency (monthly / daily / 6-hourly).
- **Spatial domain and resolution.**
- **Ensemble of interest** (CMIP6 historical + SSPs; single-model initial-condition large ensemble; perturbed-physics ensemble; downscaled regional ensemble).
- **Observational / reanalysis baseline** for comparison (user-supplied product name).

**Optional inputs:**
- Computational budget for downloads / re-griding / analysis.
- Anticipated structural-vs-internal split (prior expectation).
- Downstream impact model (e.g., crop / hydrology / health).
- Bias-correction posture (raw model output vs. bias-corrected).

**Constraints — Must:**
- State whether the question is about *forced response*, *internal variability*, *sensitivity*, *bias / fidelity*, or *projection uncertainty*. The ensemble design depends on this.
- Separate structural (model-formulation), parametric (within-model perturbed), and internal (initial-condition) ensemble axes. Forbid implicit mixing.
- Choose baseline period explicitly. Justify against the signal: pre-industrial vs. 1850–1900 vs. 1981–2010 vs. 1995–2014 — different baselines support different claims.
- Surface bias before signal. Report model bias against observations / reanalysis on the same metric *before* reporting changes.
- Quantify signal-to-noise with respect to internal variability. Specify time-of-emergence, ratio-of-signal-to-σ, or formal detection-attribution framework.
- Treat model-output as data with its own uncertainty: structural ensemble σ + internal variability σ + observational uncertainty + forcing uncertainty.
- Align reporting to community conventions: CMIP / CF / ESMValTool standards; IPCC AR6 cross-chapter conventions for headline results; PCMDI metrics where applicable.

**Constraints — Must Not:**
- Do not average across structural and internal ensembles without separating them in reporting.
- Do not infer detection from a single member without an internal-variability denominator.
- Do not invent CMIP run IDs, model versions, or institutional contributions.
- Do not apply bias correction silently without naming the method (delta change vs. quantile mapping vs. ISIMIP-style) and the consequence.
- Do not extrapolate scenario differences beyond when forcings overlap.
- Do not compare across different reference periods.

**Instructions:**

1. **Lock question type.** Forced response / internal / sensitivity / bias / projection. Write the claim sentence and state the quantitative target.

2. **Pick baseline.** Justify against the question. State the baseline length and what it averages over. Note known caveats (volcanic activity, ozone depletion era, observation density).

3. **Ensemble design.**
    - *Structural axis*: list candidate models (user-supplied or CMIP-archive ID), with a notation that each model is one structural realization and a brief reason for inclusion / exclusion.
    - *Internal axis*: number of initial-condition members per model; minimum for the question (commonly ≥5 for inter-annual; large ensemble ≥30 for trends).
    - *Parametric axis*: if applicable, list perturbed parameter ensembles.
    - *Forcing axis*: list which scenarios / experiments are included (historical-only, ssp126/245/370/585, AMIP, abrupt-4xCO2, 1pctCO2).
4. **Variable handling.** Frequency, regridding (target grid; conservative / bilinear / nearest), masking (land / ocean / ice), time-conventioning (calendar handling, leap years, no-leap models). Specify whether anomaly or absolute.

5. **Bias-and-fidelity check.** Pre-compute model-vs-observation metrics on the variable of interest before computing changes. State bias-tolerance threshold for inclusion / exclusion.

6. **Signal definition and emergence.** Define the signal (linear trend over period; difference of two periods; warming-level scaling; pattern projection; teleconnection index). Compute internal-variability denominator from a control run or pre-industrial reference. Compute time-of-emergence / S/N ratio.

7. **Inter-model spread decomposition.** Hawkins & Sutton-style separation of internal / scenario / model spread; or ANOVA across structural / scenario; or constrained-projections with emergent constraints if relevant. State which method.

8. **Bias-correction posture.** Raw model output for process-level question; bias-corrected (named method) for impacts-style downstream coupling. State whether bias correction is applied and the consequence (it removes mean bias, not necessarily variability or extremes).

9. **Uncertainty reporting.** Per metric: structural ensemble spread + internal spread + observational uncertainty + (where relevant) forcing uncertainty. Report all four; do not collapse.

10. **Reproducibility artifacts.** Use ESMValTool / xarray-based workflow; commit YAML recipe; record CMIP run IDs and the exact `realization`/`physics`/`forcing` indices; archive analysis code and intermediate netCDFs to Zenodo or institutional archive.

**Output format (locked):**

```
## Question type and claim
- Type (forced / internal / sensitivity / bias / projection):
- Claim sentence + quantitative target:

## Baseline
- Period:
- Justification:
- Known caveats:

## Ensemble design
| Axis | Members | Source | Inclusion rationale | Exclusion rationale |
| Structural | | | | |
| Internal (init-cond) | | | | |
| Parametric | | | | |
| Forcing / scenario | | | | |

## Variable handling
- Variable + frequency:
- Regrid target + method:
- Mask:
- Calendar handling:
- Anomaly / absolute:

## Bias-and-fidelity check
| Metric | Observation product | Bias | Inclusion threshold | Outcome |

## Signal definition
- Signal:
- Internal-variability denominator:
- S/N or time-of-emergence:

## Inter-model spread decomposition
- Method:
- Result format:

## Bias-correction posture
- Applied? If yes: method + consequence:

## Uncertainty reporting
| Component | Magnitude | Reported separately? |

## Reproducibility artifacts
- Tooling (ESMValTool / xarray / NCO):
- Run IDs (CMIP variant labels):
- YAML / script commit:
- Archive deposit:

## Reporting standard alignment
[CMIP / CF / ESMValTool / PCMDI / IPCC AR6 chapter conventions]

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** CMIP archive conventions (variable names, frequencies, scenario IDs); CF metadata; ESMValTool / PCMDI metrics packages; IPCC AR6 chapter-level conventions for headline-result language and uncertainty wording; FAIR for any derived dataset.

**Verification checklist:**
- [ ] Question type is one of the named families and the ensemble design follows.
- [ ] Baseline period stated and justified.
- [ ] Structural / internal / parametric / forcing axes separated.
- [ ] Model-vs-observation bias reported before change.
- [ ] Signal defined and S/N computed against internal variability.
- [ ] Inter-model spread decomposition method named.
- [ ] Bias-correction posture explicit (applied or not, with consequence).
- [ ] All four uncertainty components reported separately.
- [ ] Reproducibility artifacts (YAML / run IDs / archive) present.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Single-member trend mistaken for forced | "Model X shows warming of Y" without internal-variability context | Internal-variability denominator required |
| Multi-model mean obscures bias | Ensemble looks like obs because biases cancel | Per-model bias reported |
| Baseline shopping | Period chosen to amplify signal | Baseline justified against question |
| Mixing structural and internal | Ensemble of 20 averaged regardless of source | Axis separation enforced |
| Silent bias correction | "Adjusted" temperatures without method | Method + consequence stated |
| Scenario-extrapolation | SSP1-2.6 differences applied to SSP5-8.5 era | Scenario range constrained |
| Calendar / regrid drift | No-leap vs. proleptic mishandled | Calendar handling stated |
| Invented run ID | Plausible-looking variant label | All IDs from CMIP archive |
| Collapsed uncertainty | Single "model uncertainty" reported | Four-component decomposition |
| Emergent constraints over-applied | Constrained projection treated as truth | Constraint method named + caveat |
