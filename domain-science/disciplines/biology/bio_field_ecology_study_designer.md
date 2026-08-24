---
title: "Field Ecology Study Designer"
category: science/disciplines/biology
description: "Design a field ecology study with explicit replication units, pseudoreplication audit, BACI / gradient / control-impact framing, and detection-imperfection handling"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - ecology
  - field-study
  - baci
  - pseudoreplication
  - occupancy
  - detection-probability
  - spatial-autocorrelation
updated: "2026-05-19"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/disciplines/earth-climate/earth_field_campaign_designer.md
---

# Field Ecology Study Designer

**Objective:** Design a field ecology / observational ecology study that explicitly names its true replication unit, audits for pseudoreplication, structures the design appropriately for the question (BACI, before-after, control-impact, gradient, paired plot, removal / addition experiment), and handles imperfect detection where animals or events can be missed.

**When to use:** Before a field season, when the user has an ecological question that will be answered by going outside (not by a manipulative bench experiment) and needs the design defensible against the standard reviewer critique: pseudoreplication, confounded space-with-treatment, detection bias, scale mismatch.

**Required inputs:**
- **Ecological question** as a testable claim, with the response variable named (abundance, occupancy, biomass, diversity, behavior, survival, reproduction, community composition, rate).
- **System.** Taxon, biome / habitat, region.
- **Manipulation status.** Manipulative experiment, before-after intervention, observational comparison, gradient, long-term monitoring.
- **Spatial extent and temporal duration available.**
- **Detection challenge.** Is the target detected perfectly when present, or imperfectly (cryptic species, mobile animals, ephemeral events)?
- **Logistics.** Crew size, transport, season, permitting status.
- **Replication unit candidates.** What the user thinks is a replicate (e.g., plot, transect, site, season, tree).

**Optional inputs:**
- Existing baseline data.
- Anticipated effect size or detection probability.
- Spatial autocorrelation prior (variogram if known).
- Citizen-science integration.

**Constraints — Must:**
- Identify the true replication unit and audit for pseudoreplication (sensu Hurlbert 1984). Treat multiple measurements within a single plot / site / season as sub-samples unless statistically modeled as such.
- Distinguish manipulative (cause-inferring) from observational (association-only) designs in the output and constrain the claims accordingly.
- Where animals or events can be missed, require an explicit detection-probability framework: distance sampling, capture-recapture, occupancy with repeat visits, N-mixture, removal sampling.
- Address spatial autocorrelation: state how the analysis will detect it (Moran's I, variogram, Mantel) and accommodate it (mixed model with spatial term, INLA, kriging residuals).
- Specify whether site selection is randomized, stratified, opportunistic, or accessibility-biased — and acknowledge the inference consequence of each.
- Align reporting to journal expectations (Ecology, Journal of Applied Ecology, Methods in Ecology and Evolution) and to ROSES if a synthesis component is included.

**Constraints — Must Not:**
- Do not call a design "BACI" if there is no before period or no control.
- Do not propose pooling across sites with strong spatial autocorrelation without modeling it.
- Do not propose perfect-detection statistics for cryptic species without justifying perfect detection.
- Do not invent baseline values, detection probabilities, or population densities.
- Do not propose unmarked-individual repeat counts as independent samples.
- Do not propose comparisons across treatments confounded with year, site, or observer.

**Instructions:**

1. **Restate the question with the response variable and inference target.** Inference target is one of: population abundance / density, occupancy, demographic rate, behavioral rate, community metric, interaction / network, ecosystem flux. State whether the goal is causal or associational and constrain accordingly.

2. **Replication-unit audit.** Build a table: candidate replication unit, what within it is sub-sample, what between-unit factor is confounded with treatment. Pick the unit. Compute N at that unit, not at sub-sample.

3. **Design family selection.** From {BACI, before-after, control-impact, gradient, paired-plot, randomized manipulation, capture-recapture / occupancy / distance, time-series}, recommend one primary and explain why. State the inference each supports.

4. **Site selection plan.** Spatially stratified random; matched-pair (treatment / control matched on covariates); gradient with planned coverage of the predictor range. Specify how matching covariates are measured. Surface accessibility bias if present.

5. **Detection-probability plan.** If detection is imperfect, specify: number of repeat visits per unit, distance-sampling protocol, capture method, double-observer protocol, removal protocol — whichever fits. State the assumption of the framework (e.g., closure for occupancy across repeat visits).

6. **Sampling intensity and effort.** Per-unit visit duration, transect length, plot size, sampling time window, hours of effort. Distinguish *effort* from *sample size*. Compute total effort.

7. **Covariates to record at every visit.** Date, time, observer, weather, moon phase / tide / season (if relevant), recent disturbance, habitat covariates. These become candidate detection covariates.

8. **Power and effect-size scenarios.** Three scenarios (pessimistic / central / optimistic) with the assumption set (effect size on the response, baseline variance, detection probability, N units). Cite the method (e.g., `unmarked` simulation, `RPresence`, custom Monte-Carlo). Do not invent effect sizes — `[user-supplied]` if missing.

9. **Spatial autocorrelation handling.** Diagnostic (variogram / Moran's I); modeling approach (random effect on site, spatial term, GLS / INLA / spaMM); cluster-randomization vs. individual-plot decision.

10. **Pre-specified analysis plan.** Primary model (e.g., binomial GLMM for occupancy with detection covariates; negative-binomial GLMM for counts; Cox PH for survival; PERMANOVA for community composition). Random effects structure. Multiple-testing strategy if multiple response variables. Sensitivity analyses.

11. **Ethics, permits, and data sharing.** Wildlife / IACUC equivalent; site-access permits; Indigenous-data CARE compliance where relevant; data-deposit target (GBIF, DataONE, Movebank, Dryad, Zenodo) and metadata schema (Darwin Core, Ecological Metadata Language).

**Output format (locked):**

```
## Question and inference target
[claim + response variable + causal/associational]

## Replication-unit audit
| Candidate unit | Sub-samples within | Confound between | Selected? | N at unit |

## Design family
- Primary:
- Rationale:
- Inference supported:

## Site selection plan
- Strategy:
- Matching covariates (if paired):
- Accessibility-bias surfaced:

## Detection-probability plan
- Framework:
- Repeat-visit structure / distance protocol / capture protocol:
- Closure assumption:

## Sampling intensity
| Unit | Visit duration | Repeat visits | Effort total |

## Visit-level covariates recorded
[list with units]

## Power scenarios
| Scenario | N units | Effect | Detection p | Power | Method |

## Spatial autocorrelation handling
- Diagnostic:
- Modeling approach:

## Pre-specified analysis plan
- Primary model:
- Random effects:
- Multiple-testing:
- Sensitivity analyses:

## Ethics, permits, deposition
- Permits required:
- IACUC / equivalent:
- Data-deposit target + metadata schema:
- CARE / Indigenous-data considerations (if applicable):

## Reporting-standard alignment
[ARRIVE if animal handling; ROSES if synthesis; Darwin Core for deposit]

## Pitfalls and validation
| Pitfall | Detection | Mitigation |

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** ARRIVE 2.0 (animal handling); ROSES (if synthesis); Ecological Metadata Language and Darwin Core (deposit); journal-specific reporting checklists. CARE principles where Indigenous lands or data are involved.

**Verification checklist:**
- [ ] True replication unit named and N computed at that unit.
- [ ] Pseudoreplication audit table present.
- [ ] Design family matches inference target (manipulative vs. observational).
- [ ] Detection framework specified if detection is imperfect.
- [ ] Site-selection strategy named; accessibility bias surfaced.
- [ ] Spatial autocorrelation handling specified.
- [ ] Power scenarios written with full assumption set; no invented numbers.
- [ ] Pre-specified analysis model and random-effects structure.
- [ ] Deposit target and metadata schema named.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Pseudoreplication | Sub-samples within a plot treated as independent replicates | Unit audit table; N at true unit |
| Space-confounded-with-treatment | All treatment plots on one side of the watershed | Site-selection plan with stratification |
| Perfect-detection assumption for cryptic species | "We counted X individuals" with no detection model | Detection framework required if imperfect |
| BACI without before or without control | Design called BACI when one arm is missing | Definition enforced in design-family step |
| Spatial autocorrelation ignored | Standard errors too small; false significance | Diagnostic + modeling specified |
| Observer / year confound with treatment | Same observer always surveys treatment sites | Visit-covariates + analytic adjustment |
| Invented baseline / detection numbers | Plausible-looking 0.7 detection probability | `[user-supplied]` if no anchor |
| ARRIVE / permit non-compliance | Animal-handling protocol unreviewed | Ethics step required |
