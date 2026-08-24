---
title: "Geochronology and Age-Model Designer"
category: science/disciplines/earth-climate
description: "Design a geochronology / age-model study: sample selection, dating-method choice, uncertainty propagation, calibration, age-depth model and stratigraphic-claim audit"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - CM-02
  - DS-02
  - QA-02
difficulty: advanced
tags:
  - geochronology
  - age-model
  - radiocarbon
  - u-pb
  - ar-ar
  - osl
  - cosmogenic
  - age-depth
  - uncertainty
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/earth-climate/earth_field_campaign_designer.md
---

# Geochronology and Age-Model Designer

**Objective:** Design a geochronology study or stratigraphic age-model with appropriate dating-method choice, sample-selection strategy, uncertainty propagation, calibration, and an age-depth (or age-elevation, age-distance) model whose stated uncertainties match what the dating actually supports.

**When to use:** Before a sampling trip when a chronologic claim is on the line; when re-analyzing existing chronologic data with a stronger framework; when a reviewer questions whether an age-model supports a paleo-environmental, archaeological, tectonic, or hazard claim.

**Required inputs:**
- **Chronologic question.** The age claim the study needs to support (a single age; a duration; a rate; an age sequence; an age-depth chronology; an event correlation).
- **Material(s) available.** Carbonate, organic, charcoal, peat, sediment, volcanic glass / tephra, feldspar, quartz, zircon, monazite, sanidine, K-feldspar, apatite, bone / tooth, speleothem, marine / lake / ice core, in-situ produced cosmogenics, etc.
- **Stratigraphic / spatial context.** Section / core / outcrop / archaeological context with stratigraphic relationships.
- **Age range expected.** Approximate, from independent context.
- **Question's required precision.** What temporal resolution must the answer have (centennial / millennial / 10 kyr / 100 kyr / Myr)?

**Optional inputs:**
- Existing chronology on the same section.
- Independent constraints (tephra correlations, paleomagnetism, biostratigraphy, varve counts).
- Available labs / equipment / budgets.

**Constraints — Must:**
- Match the dating method to the material and to the expected age range. State the method's calibrated working range and the dominant uncertainty source.
- For any single age, distinguish *analytical* uncertainty from *systematic* uncertainty (decay constant; standard; reservoir effect; initial-conditions assumption) and report both. Report the calibrated age and the conversion convention (cal yr BP vs. ka vs. Ma).
- For sequences and age-depth models, treat the model as a separate inference step. State the algorithm (linear / spline / Bayesian, e.g., Bacon / OxCal / BChron) and how it handles age inversions, outliers, prior age estimates, and section gaps.
- Surface known method-specific biases: radiocarbon reservoir effects, hard-water, old-carbon recycling, in-situ contamination; U-series initial-Th; OSL fading; cosmogenic inheritance / erosion / shielding; Ar-Ar excess Ar.
- For event correlations, require an explicit error-model that includes both age uncertainty and the uncertainty in associating the dated material with the event.
- Align reporting to IUGS / INTIMATE / IntCal / SHCal calibration conventions; to Q-Geo / Geochronology and Quaternary Geochronology editorial expectations; to FAIR for deposit (Geochron, IsoArcH, etc.).

**Constraints — Must Not:**
- Do not propose a method outside its calibrated range.
- Do not invent decay constants, half-lives, calibration-curve names, lab codes, or sample identifiers.
- Do not omit reservoir / initial-condition corrections for radiocarbon, U-series, or OSL.
- Do not collapse stochastic and systematic uncertainty into one error bar.
- Do not select samples opportunistically without an explicit stratigraphic-context model.
- Do not call an age "the age of the event" without justifying the event-material relationship.

**Instructions:**

1. **Translate the chronologic question into the required precision.** State the precision needed (e.g., ±200 yr for a Holocene correlation; ±10 kyr for an MIS boundary; ±100 kyr for hominin context; ±2 Myr for batholith emplacement). The method choice flows from this.

2. **Match method to material and age range.** Build a table: candidate method × material × calibrated range × precision floor × dominant uncertainty. From this, select primary method(s); add a secondary independent method where feasible (e.g., 14C + OSL; U-Pb + Ar-Ar; cosmogenic 10Be + 26Al).

3. **Sample-selection strategy.** Specify: stratigraphic context required per sample; what disqualifies a sample (reworking, mixing, weathering, post-depositional remobilization); how many samples per horizon for redundancy; spacing strategy along the section. Build a sample list with stratigraphic position, material, and intended method.

4. **Pre-treatment plan.** Per material and method: cleaning, chemical pre-treatment, mineral separation, grain-size selection, pre-screening (e.g., quartz purity; zircon CL imaging; AMS targeting). Mark `[user-supplied lab protocol]` where lab-specific.

5. **Analytical uncertainty.** Per method: counting statistics; instrument blank; standard reproducibility; replicate variability. State the per-sample analytical σ band.

6. **Systematic uncertainty.** Per method: decay constant uncertainty; calibration-curve uncertainty (IntCal20 / SHCal20 / MARINE20 / others); reservoir / dead-carbon effect with regional ΔR uncertainty (radiocarbon); initial 230Th, 234U / 238U disequilibrium (U-series); fading rate (feldspar OSL); inheritance / erosion / shielding correction (cosmogenic); excess Ar (Ar-Ar). Each item itemized.

7. **Age-depth / age-distance model.** Algorithm choice (Bacon, BChron, OxCal P_Sequence, rbacon, free-form spline). Priors (sedimentation rate prior, gaps, hiatuses). Outlier model. Handling of independent constraints (tephra tie-points, magnetostratigraphic reversals). Output is a probabilistic age-depth model with 68% and 95% envelopes.

8. **Event-correlation step (if applicable).** Specify how the dated material relates to the event of interest, with its own uncertainty (e.g., burial-by-tephra closely brackets ages; a charcoal-bearing layer brackets a fire but may include older charcoal).

9. **Quality-check and validation.** Replicate samples (n ≥ 2 on a subset); independent-method overlap on at least one horizon; comparison against any prior chronology with explicit reconciliation; outlier-handling rule pre-specified.

10. **Reporting and deposit.** Per IUGS / IsoArcH / Geochron requirements: per-sample table with material, lab code, raw measurement, corrections applied, calibrated age + analytical σ + systematic σ; data deposit (Geochron, PANGAEA, IsoArcH); calibration software version; age-model code committed.

**Output format (locked):**

```
## Chronologic question and required precision
- Question:
- Required precision:
- Independent context (expected age range):

## Method × material matrix
| Method | Material | Calibrated range | Precision floor | Dominant uncertainty | Selected? |

## Sample-selection plan
| Sample ID | Stratigraphic position | Material | Method | Disqualifier checks |

## Pre-treatment per method
[per method: cleaning / separation / pre-screening protocol class]

## Per-sample analytical uncertainty
| Sample / method | Counting / replicate σ |

## Systematic uncertainty (per method)
| Method | Decay constant / standard | Reservoir / initial / calibration | Method-specific bias | Total syst σ |

## Age-depth (or age-distance) model
- Algorithm:
- Priors:
- Outlier model:
- Independent tie-points:
- Output: age-depth + 68%/95% envelopes

## Event correlation
- Material-event relationship:
- Bracketing logic:
- Residual uncertainty:

## Quality-check and validation
- Replicate plan:
- Independent-method overlap:
- Reconciliation with prior chronology:
- Outlier-handling rule:

## Reporting and deposit
- Per-sample table fields:
- Software / versions:
- Deposit target:

## Reporting standard alignment
[IntCal / SHCal / Geochronology editorial; Geochron deposit; FAIR]

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** IntCal20 / SHCal20 / MARINE20 calibration curves and conventions; IUPAC decay-constant recommendations; INTIMATE event-stratigraphic conventions; Geochronology and Quaternary Geochronology editorial requirements; Geochron / IsoArcH / PANGAEA deposit conventions; FAIR principles.

**Verification checklist:**
- [ ] Precision required is stated.
- [ ] Method × material × range table present; method is in range.
- [ ] Two independent methods used where feasible.
- [ ] Analytical and systematic uncertainty reported separately.
- [ ] Method-specific bias (reservoir, fading, inheritance, excess Ar) addressed where applicable.
- [ ] Age-depth model algorithm named with priors and outlier model.
- [ ] Event-material relationship justified.
- [ ] Replicate and independent-method overlap planned.
- [ ] No invented decay constants, lab codes, calibration-curve versions.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Method outside range | 14C on a 60 ka sample | Range table required |
| Reservoir correction missing | Marine carbonate 14C age reported uncalibrated | Per-method correction step |
| Single error bar | Analytical + systematic collapsed | Separate reporting |
| Age-depth model overconfident | Linear interpolation reported as the truth | Probabilistic model + envelope |
| Outlier removed silently | Inconvenient date dropped | Pre-specified outlier rule |
| Event-material misalignment | Burning charcoal age = fire age (could be older) | Relationship justification |
| Calibration drift | Older curve (IntCal13 vs. IntCal20) silently used | Version pinned |
| Invented lab code / curve version | Plausible-looking calibration ref | `[user-supplied]` |
| Tephra correlation overclaimed | "Same age as eruption X" without geochemical match | Independent fingerprint required |
| No replicate / independent method | Single age treated as definitive | Replicate plan required |
