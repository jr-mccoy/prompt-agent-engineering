---
title: "Validation Design for Scientific ML — Dependence-Aware Grouped, Temporal, and Spatial Splits, External Validation Tiers, and Unit-Level Uncertainty"
category: science/ml-for-science
description: "Design how an ML model used for a scientific claim will be validated: diagnose every dependence axis in the data (subject, batch, site, time, space, sequence or scaffold similarity), choose grouped, forward-chaining, spatially blocked, or similarity-clustered splits sized from that dependence, plan internal-to-external validation tiers that match the strength of the claim, resample uncertainty at the independent-unit level, and map the design to REFORMS / DOME / TRIPOD+AI reporting items."
techniques:
  - ST-01
  - ST-03
  - NE-11
  - QA-02
  - QA-04
difficulty: advanced
tags:
  - ml-for-science
  - cross-validation
  - spatial-block-cv
  - grouped-split
  - external-validation
  - cluster-bootstrap
  - reporting-checklist
  - is-my-test-set-really-independent
  - model-works-in-our-lab-only
updated: "2026-10-03"
related_prompts:
  - domain-science/computational/science_ml_for_science_benchmark_design.md
  - domain-science/computational/science_ml_for_science_validation_audit.md
  - domain-AI-ML/classical-ml-modeling/mlmodel_cross_validation_design.md
---

# Validation Design for Scientific ML

**Objective:** Produce a validation design in which the held-out data are genuinely
independent of the training data at the level the scientific claim generalises over, the
external-validation tier achieved is matched to the claim's wording, and uncertainty
reflects the number of independent units rather than the number of rows.

**When to use:** After scoping has said ML is warranted and before any reportable
evaluation is run; when data have hierarchical, temporal, spatial, or phylogenetic /
sequence-similarity structure; when a model must be shown to transfer to another site,
instrument, season, or lab. **Boundary:** `domain-AI-ML/` covers validation of ML systems
for deployment (`domain-AI-ML/classical-ml-modeling/mlmodel_cross_validation_design.md`,
`domain-AI-ML/data-for-ml/mldata_train_test_split_strategy.md`); this prompt covers ML as an
instrument for scientific inference, where the split defines which claim is licensed.
Within science: `../computational/science_ml_for_science_benchmark_design.md` owns
baselines, metrics, ablations, error analysis, and the test-set query budget — use it
alongside this prompt, which owns the **dependence diagnosis, split geometry, external
validation tiers, and unit-level uncertainty**; `../computational/science_ml_for_science_validation_audit.md`
audits a pipeline after the fact.

**Required inputs:**
- **Discipline.** [user-supplied]
- **Study type.** [user-supplied]
- **The claim,** in one sentence, and the population/regime it must generalise to
  (new subjects, new sites, future seasons, unsampled locations, unseen protein families).
- **Data structure.** Every grouping variable present (subject, animal, litter, plate,
  batch, run, instrument, operator, site, date, coordinates, sequence or chemical scaffold).
- **Available external data,** if any: other sites, instruments, labs, time periods.

**Optional inputs:**
- Estimated ICC by grouping level; spatial autocorrelation range (from a variogram of
  residuals or of the outcome); temporal autocorrelation lag `[user-supplied]`.
- Sequence-identity or structural-similarity thresholds conventional in the field
  `[user-supplied — cite the field convention]`.
- Number of hyperparameter configurations to be tuned.

**Constraints — Must:**
- Enumerate every dependence axis and state, for each, whether it is handled by the split,
  by stratification, by adjustment, or knowingly left (with the consequence for the claim).
- Choose the split from the claim: the held-out unit must be the unit the claim says is new.
- Size spatial blocks or buffers and temporal gaps from the measured dependence range,
  not by convenience; if the range is unknown, say so and plan to estimate it.
- Use nested validation whenever tuning and evaluation would otherwise share data.
- Assign each planned result an external-validation tier and restrict claim wording to it.
- Compute uncertainty by resampling or modelling at the independent-unit level.
- Lock the design before evaluation; later changes are exploratory and reported as such.
- Default to the Open Science branch: publish split assignments (unit IDs per fold), seeds,
  and code.

**Constraints — Must Not:**
- Do not invent ICCs, autocorrelation ranges, similarity thresholds, citations, or results;
  mark them `[user-supplied]` or plan to estimate them.
- Do not describe random row-level splits as independent when any dependence axis exists.
- Do not call a temporal or cross-validation result "external validation."
- Do not apply conformal prediction or bootstrap intervals that assume exchangeable rows
  to grouped, temporal, or spatial data without saying how exchangeability is restored.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" in drafted text.

**Instructions:**

1. **Restate claim and target (ST-01).** Name the new unit the claim is about.
2. **Diagnose dependence.** List each axis; estimate or request its strength (ICC per
   level; spatial range; temporal lag; similarity clusters). Rank axes by how much they
   could inflate held-out performance.
3. **Choose split geometry.**
   - *Grouped* (leave-group-out / GroupKFold) at the highest level the claim generalises over.
   - *Temporal*: forward-chaining folds with a gap at least the autocorrelation lag between
     training end and test start; never train on the future.
   - *Spatial*: block CV with block size at least the autocorrelation range, or buffered
     leave-one-out with buffer equal to the range; check blocks span the covariate space.
   - *Similarity-clustered*: cluster sequences/scaffolds at the field's threshold and split
     by cluster.
   - Combined structures (e.g., sites × years): hold out the combination the claim needs.
4. **Plan nested tuning.** Inner loop for hyperparameters, outer loop for evaluation, both
   respecting the same grouping.
5. **Assign external-validation tiers.** T0 internal resampling; T1 internal but
   temporally later; T2 external, same protocol, different site/instrument/batch; T3 fully
   independent (different team, protocol, or population). Map each claim sentence to the
   tier that licenses it (e.g., "generalises to new sites" needs T2 or higher).
6. **Plan uncertainty at the unit level (NE-11).** Cluster bootstrap over independent units
   (resample groups, not rows); report between-fold and between-site spread, not only the
   pooled mean. Note that interval width is driven by the number of held-out units:
   10 held-out sites give a wide interval regardless of 100,000 held-out rows.
7. **Stress-test (QA-02).** For each axis left unhandled, describe the most plausible way
   it inflates performance and what result would reveal it (e.g., performance falls when
   the held-out set is restricted to unseen batches).
8. **Map to reporting items and state limits (QA-04).** Fill the reporting map; list what
   the design cannot show.

**Output format (locked):**

```
## Claim & New Unit
- Discipline / study type:
- Claim (one sentence):
- New unit the claim generalises to:

## Dependence Diagnosis
| Axis | Levels/count | Strength (ICC / range / lag) [source] | Inflation risk | Handling (split / stratify / adjust / left) |
|---|---|---|---|---|

## Split Design
| Fold scheme | Held-out unit | Block/buffer/gap size and basis | Folds | Nested tuning |
|---|---|---|---|---|

## External-Validation Tiers
| Claim sentence | Tier required | Tier planned | Data source | Allowed wording |
|---|---|---|---|---|

## Uncertainty Plan
- Resampling unit: ; method: ; independent held-out units: n =
- Spread reported: between-fold / between-site

## Unhandled Axes & Stress Tests
## Reporting Map
| Item (REFORMS / DOME / TRIPOD+AI) | Where addressed | Gap |
|---|---|---|
## Limits of this design
## Pre-specified vs exploratory
## Open Science release (split assignments, seeds, code)
```

**Reporting-standard alignment:** REFORMS (data splits, leakage, generalisability);
DOME (data partition independence, evaluation); TRIPOD+AI terminology for
internal vs external validation where clinical; spatial/temporal/hierarchical/phylogenetic
cross-validation guidance from the ecology methods literature (blocking by dependence
structure); Kapoor–Narayanan leakage taxonomy.

**Verification checklist (before delivering):**
- [ ] Claim's new unit named and used as the held-out unit.
- [ ] Every dependence axis listed with strength (or "unknown — estimate") and handling.
- [ ] Block, buffer, and gap sizes justified from measured or to-be-measured dependence.
- [ ] Tuning nested and grouping-respecting.
- [ ] Every claim sentence mapped to a validation tier; no CV result labelled external.
- [ ] Uncertainty resampled at the unit level; number of independent held-out units stated.
- [ ] Reporting map filled; limits and exploratory items stated.
- [ ] No invented values or citations; unknowns marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Group split at the wrong level | Split by image while subjects repeat across folds | Hold out the highest level the claim generalises over |
| Spatial CV with small blocks | Blocks smaller than the autocorrelation range leave neighbours in train and test | Size blocks/buffers from the variogram range; report it |
| Temporal split without a gap | Test starts the day after training ends; autocorrelation carries over | Insert a gap ≥ temporal lag |
| CV called external validation | "Validated" claim from 5-fold CV on one site | Tier table; wording restricted to the tier achieved |
| Row-level bootstrap CI | Narrow CI from 100,000 rows across 10 sites | Cluster bootstrap over sites; state n of independent units |
| Conformal coverage assumed | Coverage guarantee claimed under spatial dependence | State the exchangeability assumption and how blocking restores it, or drop the guarantee |
