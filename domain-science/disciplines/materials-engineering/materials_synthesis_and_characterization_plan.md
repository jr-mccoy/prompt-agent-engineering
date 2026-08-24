---
title: "Materials Synthesis and Characterization Plan"
category: science/disciplines/materials-engineering
description: "Plan a materials synthesis-characterization-property study with claim-anchored characterization, batch / sample tracking, and property-structure traceability"
techniques:
  - ST-01
  - ST-03
  - CM-02
  - DS-02
  - QA-02
difficulty: advanced
tags:
  - materials
  - synthesis
  - characterization
  - structure-property
  - batch-tracking
  - reproducibility
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/chemistry/chem_characterization_battery_designer.md
  - domain-science/disciplines/materials-engineering/materials_doe_plan.md
---

# Materials Synthesis and Characterization Plan

**Objective:** Plan a materials study that connects a synthesis recipe to a structural characterization battery to a property measurement, with batch-level tracking, claim-anchored characterization, and traceability such that every structure-property claim is supported by data from a specific, identified sample.

**When to use:** When starting a new materials-development project, before scaling up a synthesis, or when a manuscript reviewer asks how the structural claims connect to the property claims sample-by-sample. Also useful when triaging a project that has produced data but cannot connect specific samples to specific measurements.

**Required inputs:**
- **Material class.** Metal alloy, ceramic, polymer, composite, nanoparticle, thin film, 2D material, MOF / COF, glass, semiconductor, single crystal, single-atom catalyst, battery electrode, electrolyte, etc.
- **Property of interest.** Mechanical (modulus / strength / toughness / fatigue), thermal (k / Cp / α), electrical (σ / mobility / breakdown / dielectric), optical (refractive index / absorption / PL), magnetic (M(H) / susceptibility), electrochemical (specific capacity / rate / cycle life), catalytic (TOF / selectivity / stability), barrier / transport.
- **Synthesis approach.** Solid-state, sol-gel, hydrothermal / solvothermal, CVD / ALD / PVD, MBE, electrodeposition, polymerization, melt, exfoliation, ball-milling, additive manufacturing, etc.
- **Compositional / structural variable** to be varied (dopant level, processing temperature, time, atmosphere, pressure, layer thickness, particle size, morphology).
- **Number of samples / batches planned and the synthesis throughput.**

**Optional inputs:**
- Existing structure-property correlations in the literature (user-supplied).
- Available characterization tools in-house vs. external.
- Target application benchmarks.

**Constraints — Must:**
- Tag every individual sample with an opaque, durable ID and tie every measurement to that ID. Refuse "the sample" without an ID.
- Every structure-property claim must point to data from the same physical sample (or, if from a different sample, justify the cross-sample inference).
- The characterization battery is built from the *property* claim backward: each method exists to support a named claim about composition, phase, microstructure, or interface.
- Process variables that affect the property must be logged at the batch level (temperature profile, atmosphere, dwell time, ramp, reagent lots, instrument calibration).
- For statistical claims (e.g., "increases strength by X%"), require replicate samples per condition (typically ≥3 batches, with ≥3 specimens per batch for mechanical / electrical; ≥100 particles for size distributions).
- Connect to the appropriate community standard: ASTM / ISO test methods for mechanical / thermal / electrical; XRD / TEM / SEM reporting conventions; for nano: ≥100 particle count; for battery: specific-capacity normalization (active mass / electrode area / total mass) explicit; for catalysis: TOF vs. mass-activity vs. specific-activity reported with normalization basis.
- Align deposit to FAIR (Zenodo / Materials Cloud / NOMAD / Materials Project Data); CIF for crystalline structures; raw measurement files where licenses permit.

**Constraints — Must Not:**
- Do not allow "representative sample" property claims without an explicit sampling rule.
- Do not pool measurements from samples with substantially different composition / phase / microstructure as if from the same condition.
- Do not invent ASTM / ISO standard numbers, instrument model numbers, reagent lots, or vendor catalog numbers.
- Do not omit specific-capacity / TOF normalization basis.
- Do not report properties without uncertainty (replicates' SD or standard error).
- Do not claim structure-property correlation across samples where confounders (porosity, density, defect concentration, residual stress) are not measured.

**Instructions:**

1. **Lock the property claim and the structure-property link being tested.** State it as a single sentence with the property numeric target and the structural variable being varied. Identify the structural claim that the synthesis is supposed to produce.

2. **Sample-ID schema and batch / specimen hierarchy.** Define ID format that encodes nothing about treatment (opaque). State the hierarchy: batch → specimen → measurement. Every measurement record carries the specimen ID.

3. **Synthesis-variable design.** Identify the variable of interest and the secondary variables that must be held constant (or measured if they cannot be held constant). Build the synthesis matrix. Note: for systematic compositional / processing studies, consider a separate DOE workflow (`materials_doe_plan.md`).

4. **Process logging.** Per batch, the data captured: nominal recipe, actual recipe (deviations), temperature profile, atmosphere, time, instrument ID, operator, reagent lot, date. Capture at synthesis, not retrospectively.

5. **Characterization battery anchored to claim.** From the property claim and the structural variable, derive the necessary characterization:
    - *Composition*: ICP / XRF / EDS / WDS / XPS / NMR — pick one bulk and one surface where relevant.
    - *Phase*: PXRD (Rietveld where applicable) for crystalline; SAED / TEM for nanoscale; Raman / IR for fingerprinting.
    - *Microstructure*: SEM / TEM / STEM-EDS / EBSD / focused-ion-beam tomography; porosity by gas adsorption (BET) or pycnometry.
    - *Surface / interface*: XPS, contact angle, AFM.
    - *Defects*: PL for semiconductors; EPR for paramagnetic centers; positron annihilation for vacancies.
6. **Property measurement.** Method (ASTM / ISO / community-standard); specimen geometry / preparation; environment (atmosphere, temperature, humidity); replicate count; normalization basis.

7. **Confounder measurement.** Identify the confounders likely to vary across samples (porosity, density, residual stress, grain size, defect density, water content, surface area). Measure each. State the cross-sample analysis approach: stratify, regress out, or limit inference.

8. **Structure-property traceability table.** A table that, for every structure-property claim, points to the specific sample IDs whose data support it. If the linkage is across samples (e.g., XRD on batch A, property on batch B, both claimed to be "the same"), require a same-batch sub-analysis or a representativeness argument.

9. **Statistical analysis.** Per condition: mean ± SD, sample size, distribution check (for tail metrics). Cross-condition: ANOVA / linear regression / Weibull (for mechanical strength) / appropriate model. Effect-size + CI primary; p-value secondary.

10. **Deposit and reporting.** CIF for crystals; raw spectra / patterns; instrument settings; instrument calibration logs; per-sample metadata; deposit on Zenodo / Materials Cloud / NOMAD with DOI; per-paper SI table tying every figure to specific sample IDs.

**Output format (locked):**

```
## Property claim and structural link
- Property claim:
- Structural claim:
- Variable of interest:

## Sample-ID and hierarchy
- ID regex:
- Hierarchy: batch → specimen → measurement:

## Synthesis-variable design
| Batch | Variable level | Held constant | Deviations log policy |

## Process logging
[fields captured per batch]

## Characterization battery (claim-anchored)
| Method | Claim it supports | Mandatory? | Sample state |

## Property measurement
| Method | Standard (ASTM/ISO) | Geometry | Environment | Replicates | Normalization basis |

## Confounder measurement
| Confounder | Measurement method | Handling in analysis |

## Structure-property traceability table
| Claim | Sample ID(s) | Structural data | Property data | Same sample? |

## Statistical analysis
- Per-condition statistic:
- Cross-condition model:
- Effect-size + CI:
- Weibull / distribution if mechanical:

## Deposit / reporting
- CIF / raw data deposit:
- Per-paper SI sample-figure table:
- License / embargo:

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** ASTM / ISO / IEC for mechanical / thermal / electrical / electrochemical methods; CIF deposition at CCDC / COD for crystals; ≥100 particle count for nano size distribution; BET reporting per IUPAC; specific-capacity normalization basis explicit for battery; TOF normalization basis explicit for catalysis; FAIR / NOMAD / Materials Cloud / Materials Project for data deposit.

**Verification checklist:**
- [ ] Property claim and structural claim stated together.
- [ ] Sample-ID schema opaque; hierarchy enforced.
- [ ] Characterization built from the claim, not from instrument availability.
- [ ] Process logging captures actual recipe, not nominal only.
- [ ] Replicate count adequate for statistical claim.
- [ ] Confounders identified and measured.
- [ ] Structure-property traceability table maps every claim to specific samples.
- [ ] Normalization basis explicit for any property quoted as ratio.
- [ ] No invented ASTM numbers, instrument models, reagent lots.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Cross-sample claim | Property on batch A linked to structure on batch B | Same-sample requirement or sub-analysis |
| Confounder collapse | "Higher strength" while density also changes | Confounder measured + adjusted |
| Single specimen claim | Property from one specimen reported | Replicates required |
| Specific-capacity ambiguity | Active-mass vs. total-mass not stated | Normalization basis explicit |
| Nano size from <100 particles | Mean diameter from 30 particles | ≥100 enforced |
| Process drift unlogged | Reagent lot changed mid-study | Per-batch lot logged |
| Representative micrograph | One image stands for everything | Sampling rule required |
| Invented ASTM number | Plausible-looking ASTM E### | `[user-supplied]` |
| Pooled extremes | Two morphologies pooled as one condition | Within-condition homogeneity check |
| No property uncertainty | Single number reported | Mean ± SD with N |
