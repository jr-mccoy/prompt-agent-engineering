---
title: "Earth-Science Field Campaign Designer"
category: science/disciplines/earth-climate
description: "Design a field campaign with siting strategy, sensor placement, calibration, redundancy, sampling strategy, and a defensible data-uncertainty budget"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - CM-02
  - DS-02
  - QA-02
difficulty: advanced
tags:
  - field-campaign
  - sensor-placement
  - calibration
  - siting
  - data-uncertainty
  - heterogeneity
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/biology/bio_field_ecology_study_designer.md
  - domain-science/methods-foundations/science_experimental_design_advisor.md
---

# Earth-Science Field Campaign Designer

**Objective:** Design an earth-science field campaign (atmospheric, oceanographic, hydrologic, geologic, cryospheric, volcanologic, geomorphic) with a defensible siting strategy, sensor selection and placement, calibration plan, redundancy, sampling that matches the spatiotemporal scale of the phenomenon, and an itemized data-uncertainty budget that survives reviewer scrutiny.

**When to use:** Before equipment goes to the field, when the user has a phenomenon-scale question and a candidate study domain. Useful also for retrofitting an ongoing campaign that has surfaced unexpected heterogeneity, gap, or sensor issue.

**Required inputs:**
- **Phenomenon and target quantity.** Flux, concentration, temperature, salinity, velocity, strain, displacement, isotope, gas mole-fraction, depth, etc.
- **Spatial and temporal scale.** Spatial extent (m / km), spatial heterogeneity scale, temporal duration, temporal resolution needed (Hz / minute / hour / day / month).
- **Domain and access.** Region, terrain, accessibility, weather, season, permitting.
- **Logistics envelope.** Personnel, vehicles, power, data return, comms.
- **Existing infrastructure.** Met stations, eddy-flux towers, moorings, GNSS / seismic networks, gauges, satellites, prior campaigns.
- **Inference target.** Mean, gradient, rate, anomaly, trend, event detection, mass balance, budget closure, source attribution.

**Optional inputs:**
- Anticipated effect / signal magnitude.
- Heterogeneity prior (variogram, climatology).
- Co-located satellite overpass times / scenes.
- Modeling target the data will feed (forecast, reanalysis assimilation, inverse model).

**Constraints — Must:**
- Match measurement scale to phenomenon scale. State the *footprint* of each sensor (e.g., eddy-flux footprint area as a function of stability and wind) and verify it matches the phenomenon's spatial scale.
- Treat heterogeneity as first-class. If the user is sampling a heterogeneous domain (forest stand vs. catchment, coastal upwelling vs. open ocean, glacier surface vs. tongue), require either stratified sampling or explicit upscaling assumption.
- Plan calibration *before* deployment, *during* deployment (in-situ comparison, intercomparison overlaps), and *after* recovery. Specify the traceability path back to a standard.
- Require redundancy on every measurement that drives the headline result. No single point of failure.
- Specify data-return strategy and data-loss budget: how data come back (cellular / satellite / wired / manual download), what happens on outage, what the acceptable data-loss fraction is.
- Itemize uncertainty: instrument accuracy + drift + spatial representativeness + temporal aliasing + footprint mismatch + interpolation error.
- Align reporting to community data standards: WMO BSRN / CIMO / GCOS for met / climate; CF / ACDD / ISO 19115 for spatial metadata; OceanSITES / Argo for ocean; CUAHSI / GHCN for hydrology; FDSN miniSEED / StationXML for seismic; FAIR for everything.

**Constraints — Must Not:**
- Do not assume one sensor location is representative of a heterogeneous footprint.
- Do not invent calibration constants, instrument-accuracy specs, or footprint estimates. Mark `[user-supplied]` for spec sheets.
- Do not propose temporal sampling slower than the Nyquist of the dominant variability without naming the aliasing consequence.
- Do not omit metadata at the point of capture.
- Do not propose single-sensor headline results.
- Do not assume access — permits, ice / shipping windows, host-country / Indigenous-territory consents must be confirmed.

**Instructions:**

1. **Phenomenon-scale mapping.** Output a small table: phenomenon spatial scale, temporal scale → required sensor footprint, required sampling rate. Compare to candidate sensors' specs.

2. **Inference target → measurement target.** From the inference target (mean / gradient / rate / event / budget), derive the measurement target (point time series; gradient pair; transect; network; profile; flux footprint).

3. **Siting strategy.** From the inference target and heterogeneity prior, pick a strategy: representative point, stratified network, transect, grid, mobile / autonomous (UAV, glider, drifter), opportunistic. Specify per-site rationale.

4. **Sensor selection per measurement.** For each target quantity: candidate sensor (user-named manufacturer or generic class), accuracy, drift, sample rate, power draw, data rate, environmental envelope, known failure modes. Mark `[user-supplied]` for spec values.

5. **Redundancy plan.** Per headline result: a backup sensor, a co-located independent measurement, a cross-validation with satellite / reanalysis / nearby station.

6. **Calibration plan.** Pre-deployment (lab-traceable; primary / secondary standard); deployment (in-situ comparison with co-located reference; sensor-pair intercomparison); during-deployment (drift checks, calibration field-trips); recovery (post-deployment re-cal). Traceability path stated.

7. **Sampling strategy.** Temporal sampling rate (Nyquist plus oversampling factor); duration; gap policy. Spatial sampling rule (random / stratified / systematic / fixed network). Aliasing check on dominant variability.

8. **Operational risks.** Weather; permitting; ship / aircraft / vehicle availability; visa; ice / season window; remoteness; data-return outage; instrument failure; sample logistics (custody, freezer chain, transport).

9. **Uncertainty budget.** Itemize: instrument accuracy, drift, footprint / representativeness, temporal aliasing, calibration transfer, interpolation, model-comparison mismatch. Sum to a likely band; identify dominant.

10. **Data management plan.** Where data go each day; how metadata are captured at the point of measurement; QA / QC tier (NRT / preliminary / final); deposit target (PANGAEA, OceanSITES, AmeriFlux / FLUXNET, USGS, IRIS, EarthChem, Zenodo); license; embargo.

11. **Closure / cross-validation.** What independent check will confirm or refute the headline measurement (mass balance, isotope mass balance, model-data comparison, satellite overflight, paired-site agreement)?

**Output format (locked):**

```
## Phenomenon and scale
| Phenomenon | Spatial scale | Temporal scale | Required sensor footprint | Required sampling rate |

## Inference target → measurement target
- Inference:
- Measurement type (point / gradient / transect / network / profile / footprint):

## Siting strategy
| Site / unit | Coords | Rationale | Heterogeneity context |

## Sensor selection
| Quantity | Sensor class | Accuracy | Drift | Sample rate | Power | Failure modes |

## Redundancy plan
| Headline result | Primary | Redundancy | Cross-validation |

## Calibration plan
| Phase | Action | Standard / source | Traceability |

## Sampling strategy
- Temporal rate + Nyquist check:
- Duration:
- Spatial rule:
- Aliasing-check status:

## Operational risks
| Risk | Likelihood | Mitigation |

## Uncertainty budget
| Source | Magnitude | Direction |
| Likely band:
| Dominant:

## Data management plan
- Daily upload / archive:
- Metadata at point of capture:
- QA / QC tiers:
- Deposit target + license + embargo:

## Closure / cross-validation
- Independent check:
- Pass criterion:

## Reporting standard alignment
[BSRN / GCOS / CF / ACDD / OceanSITES / FAIR / ISO 19115 — name applicable]

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** WMO CIMO Guide for meteorological instruments; GCOS Essential Climate Variables; OceanSITES / Argo / GO-SHIP for ocean; CUAHSI / WaterML for hydrology; FDSN miniSEED / StationXML for seismic; CF / ACDD / ISO 19115 metadata for spatial data; FAIR principles for deposit.

**Verification checklist:**
- [ ] Sensor footprint matches phenomenon spatial scale.
- [ ] Temporal sampling clears Nyquist of dominant variability.
- [ ] Stratification or upscaling assumption made explicit for heterogeneous domains.
- [ ] Calibration plan traces to a standard at every phase.
- [ ] Redundancy plan covers every headline result.
- [ ] Uncertainty budget itemized and dominant identified.
- [ ] Metadata captured at point of measurement, not post-hoc.
- [ ] Closure / cross-validation plan named with pass criterion.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Footprint mismatch | Eddy-flux tower in patchy canopy reported as catchment flux | Footprint vs. phenomenon scale required |
| Heterogeneity collapse | Single sample reported as domain mean | Stratification / upscaling required |
| Aliasing | Hourly sample of diurnally cycling signal | Nyquist check required |
| Sensor drift unnoticed | Single calibration at deployment, none after | Multi-phase calibration plan |
| Permit failure mid-campaign | Access denied half-way | Permit confirmation in risk register |
| Data-return loss silent | 30% gap, treated as random | Data-loss budget + diagnosis |
| Single-sensor headline | One instrument fails → result lost | Redundancy plan enforced |
| Invented spec | Plausible accuracy spec | `[user-supplied]` |
| Metadata reconstructed later | Site, observer, weather lost to time | Capture at point of measurement |
| Closure missing | No independent test of result | Closure step required |
