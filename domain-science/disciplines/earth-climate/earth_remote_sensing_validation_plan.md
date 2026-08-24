---
title: "Remote-Sensing Validation Plan"
category: science/disciplines/earth-climate
description: "Validate a remote-sensing retrieval (satellite or airborne) against ground truth: scale-matching, retrieval-error budget, validation-sample design, and uncertainty reporting"
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-02
  - QA-02
difficulty: advanced
tags:
  - remote-sensing
  - validation
  - retrieval
  - ground-truth
  - scale-matching
  - cal-val
  - error-budget
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/earth-climate/earth_field_campaign_designer.md
  - domain-science/disciplines/earth-climate/climate_model_intercomparison_plan.md
---

# Remote-Sensing Validation Plan

**Objective:** Plan a validation campaign for a remote-sensing retrieval (satellite or airborne — optical, thermal, microwave-active, microwave-passive, lidar, hyperspectral, gravity / altimetry, SAR) against in-situ ground truth, with explicit scale-matching, retrieval-error budget, validation-sample design, and uncertainty reporting per CEOS-WGCV-style best practice.

**When to use:** When validating a new product, validating a known product over a new region / season / regime, or responding to reviewer or science-team concern about retrieval bias. Equally useful for cal/val site planning.

**Required inputs:**
- **Retrieval / product.** Algorithm name (user-supplied or generic, e.g., "LST from MODIS C6.1", "SMAP soil moisture L3"), sensor, level (L1 / L2 / L3 / L4), spatial resolution, temporal resolution.
- **Variable retrieved.** Geophysical quantity and units.
- **Ground-truth source.** In-situ network (FLUXNET / ISMN / SoilSCAPE / BSRN / ARM / GTN-P / AGAGE / NOAA Global Monitoring); campaign measurements; reference network; user-provided observations.
- **Region and period** of validation.
- **Inference target.** Bias, RMSE, anomaly correlation, distribution-tail behavior, trend agreement, event detection.

**Optional inputs:**
- Known retrieval-error budget from algorithm-theoretical basis document (user-supplied).
- Stratification axes (land cover, vegetation density, season, surface roughness).
- Concurrent multi-sensor products (for cross-validation).

**Constraints — Must:**
- Match scales explicitly. State sensor footprint, in-situ representativeness area, and the upscaling / downscaling assumption that links them. Quantify scale-mismatch error.
- Stratify validation by relevant regimes. A single overall RMSE is rarely informative. Stratify by land cover / surface type / season / cloud cover / solar zenith / atmospheric state.
- Specify the temporal matching window between satellite overpass and in-situ observation; specify the consequence of widening or narrowing it.
- Itemize retrieval-error sources: forward-model error + ancillary-data error + atmospheric correction error + cloud / contamination error + spatial-mismatch error + temporal-mismatch error + in-situ instrument error + upscaling error.
- Report bias separately from random error. Report distribution tails separately from the mean.
- Treat the in-situ data as data with uncertainty, not truth. State in-situ uncertainty and propagate.
- Align to CEOS-WGCV best practice; ESA Cal/Val protocols; CGMS / WMO validation conventions; ILRS / IOCCG protocols by domain.

**Constraints — Must Not:**
- Do not report aggregate RMSE without per-stratum decomposition.
- Do not assume in-situ observation is perfect.
- Do not invent in-situ network station IDs, ATBD section references, or retrieval algorithm versions.
- Do not match sensor pixel to point measurement without an explicit upscaling assumption.
- Do not validate a product on the same data it was trained / tuned on.
- Do not exclude failure regions (cloud, snow, water, vegetation density) silently.

**Instructions:**

1. **Validation target.** Bias / RMSE / anomaly / tail / trend / event. State what value of the metric would constitute "validated for purpose" — and what would not. Specify the purpose explicitly (e.g., "fit for data assimilation in NWP" implies a different threshold than "fit for trend detection").

2. **Match-up design.** Spatial: sensor footprint vs. in-situ representativeness area; upscaling rule (averaging in-situ network within pixel; nested-grid mean; deep-learning footprint emulator). Temporal: window around overpass; cloud-clear-only vs. all-sky; daily mean vs. instantaneous.

3. **Stratification.** Identify the regimes over which retrieval behavior is expected to vary (land-cover class; ice / snow / water; cloud cover; solar zenith; canopy density; surface roughness; vegetation index; atmospheric water vapor; ocean state). Plan per-stratum metrics.

4. **Sample design.** Required matchup count per stratum for the metric (commonly ≥30–50 matchups for stable RMSE; ≥100 for distribution-tail behavior). State how matchups are accumulated (network-year coverage; campaign).

5. **In-situ uncertainty.** Per network / instrument: stated accuracy, drift, calibration traceability, sampling depth / height representativeness, gap-filling policy.

6. **Retrieval-error budget.** Itemize: forward-model / instrument noise; ancillary (DEM / land cover / atmospheric profile / aerosol / cloud mask); atmospheric correction; cloud / contamination flags applied; spatial-mismatch; temporal-mismatch; in-situ; upscaling. Sum to a likely error band per stratum.

7. **Cross-validation against an independent product.** Where available (a different retrieval of the same variable, a model reanalysis, a different sensor's product). Independent-product agreement does not validate; it constrains.

8. **Reporting metrics.** Per stratum: bias, ubRMSE (unbiased RMSE), RMSE, correlation, anomaly correlation, slope, percentile differences, frequency-bias for thresholds. Plus distribution plots: Taylor / target / quantile-quantile.

9. **Failure-region disclosure.** Explicitly mark regions / regimes where the retrieval fails or the validation cannot constrain. Do not omit.

10. **Reporting block and archive.** Output the match-up dataset specification, the per-stratum metric table, the per-pixel uncertainty map, and the validation-report skeleton ready for the algorithm team / journal.

**Output format (locked):**

```
## Retrieval and validation target
- Product / algorithm / version:
- Variable + units:
- Metric for fitness:
- Threshold:

## Match-up design
- Spatial: sensor footprint / in-situ rep area / upscaling rule:
- Temporal: window:

## Stratification axes
| Axis | Levels | Why expected to vary |

## Sample design per stratum
| Stratum | Required N | Source |

## In-situ uncertainty
| Network / sensor | Accuracy | Drift | Traceability | Representativeness |

## Retrieval-error budget
| Source | Magnitude | Per stratum |
| Sum | Likely band:
| Dominant:

## Independent cross-validation
- Product:
- Disagreement vs. agreement implication:

## Reporting metrics per stratum
| Stratum | Bias | ubRMSE | RMSE | r | Anomaly r | Slope | Tail metric | N matchups |

## Failure regions / regimes
[explicit list — do not omit]

## Reporting standard alignment
[CEOS-WGCV / ESA Cal/Val / CGMS / WMO / domain-specific protocol]

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** CEOS-WGCV (Working Group on Calibration and Validation) Best Practices; ESA Cal/Val protocols; CGMS GSICS for inter-satellite calibration; IOCCG protocols for ocean color; ILRS for laser ranging; WMO / GCOS observation standards; FAIR for derived match-up datasets.

**Verification checklist:**
- [ ] Validation target tied to a fitness-for-purpose threshold.
- [ ] Spatial and temporal scale-matching assumptions explicit.
- [ ] Stratification by relevant regimes; per-stratum metrics.
- [ ] Sample-size requirement stated per stratum.
- [ ] In-situ uncertainty propagated, not assumed zero.
- [ ] Retrieval-error budget itemized; dominant identified.
- [ ] Failure regions disclosed, not hidden.
- [ ] No invented network IDs / algorithm versions / ATBD references.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Aggregate RMSE hides regime failure | "Overall RMSE 0.04 m³/m³" while desert is broken | Per-stratum metrics required |
| In-situ treated as truth | Network σ ignored; all error attributed to satellite | In-situ uncertainty propagated |
| Scale-mismatch unbudgeted | Point measurement vs. 36 km pixel | Upscaling rule + mismatch error |
| Temporal window too wide | Daily average matched to instantaneous overpass | Window stated + consequence |
| Validation on training data | Same in-situ used in retrieval tuning | Independence audit |
| Cloud filtering hides failure | All-sky data quietly excluded | Failure-region disclosure |
| Cross-validation as truth | Two products agree → both "validated" | Cross-validation as constraint only |
| Tail behavior omitted | RMSE alone reported | Tail / percentile metric required |
| Invented station ID / ATBD | Plausible-looking reference | `[user-supplied]` |
| Trend "validated" from short record | 3-year overlap claimed as trend agreement | Period adequacy stated |
