---
title: "ML Project Scoping for a Lab Dataset — Is ML Warranted, Is the Data Enough, and Where Will It Leak"
category: science/ml-for-science
description: "Before any model is trained on a lab or field dataset, decide whether machine learning is the right instrument for the scientific question or whether classical statistics answers it better, compute the effective sample size from the data's real units of independence, map batch and sample-level leakage and confounding risks, fix the baselines ML must beat, and state the go / redesign / stop criteria."
techniques:
  - ST-01
  - CM-03
  - NE-11
  - DP-13
  - QA-02
difficulty: intermediate
tags:
  - ml-for-science
  - project-scoping
  - effective-sample-size
  - batch-effects
  - data-leakage
  - baselines
  - classical-vs-ml
  - should-i-use-machine-learning
  - small-lab-dataset
  - reviewer-asked-why-ml
updated: "2026-10-03"
related_prompts:
  - domain-AI-ML/problem-framing-scoping/mlframe_is_this_ml_problem.md
  - domain-science/statistics/science_mixed_models_design.md
  - domain-science/computational/science_ml_for_science_benchmark_design.md
---

# ML Project Scoping for a Lab Dataset

**Objective:** Decide, before modelling starts, whether ML is a sound instrument for a
specific scientific question on a specific dataset. The output is a scoping memo that
classifies the question, compares ML against the classical analysis that would answer it,
computes the effective sample size from the data's units of independence, maps leakage and
confounding risks created by how the samples were collected, fixes the baselines, and
states the evidence that would trigger go, redesign data collection, or stop.

**When to use:** At project start or at a lab meeting where someone proposes "let's throw
ML at it"; when writing the analysis section of a grant or preregistration; or when a
reviewer asks why ML was used instead of a standard model. **Boundary:** `domain-AI-ML/`
is for *building ML systems* (products, pipelines, deployment);
`domain-science/ml-for-science/` is for *ML as an instrument for scientific inference*.
The nearest AI-ML neighbour, `domain-AI-ML/problem-framing-scoping/mlframe_is_this_ml_problem.md`,
weighs ML against rules and analytics for a business or product problem; this prompt weighs
ML against the statistical model a journal reviewer would expect, and centres on the unit
of independence, batch structure, and the scientific claim. Once scoping says "go", design
the evaluation with `science_ml_validation_split_design.md` and
`../computational/science_ml_for_science_benchmark_design.md`.

**Required inputs:**
- **Discipline.** [user-supplied] (e.g., cell biology imaging, ecology, materials, neuroscience)
- **Study type.** [user-supplied] (experimental / observational / screening / measurement automation)
- **The scientific question,** in one sentence, and the claim the result would support.
- **Dataset structure.** Rows and what one row is; the hierarchy of units (e.g., cells within
  fields within wells within plates within batches; repeated measures within subjects;
  sites; dates); how labels were obtained and by whom.
- **The classical analysis** the field would normally use for this question, if known.

**Optional inputs:**
- Intraclass correlation (ICC) or variance components by level, if already estimated.
- Whether batch, plate, site, or date is balanced across classes or conditions.
- Inter-rater agreement for labels; label noise estimates.
- Any published model or heuristic for the same task `[user-supplied]`.

**Constraints — Must:**
- Classify the question as **inference about an effect**, **prediction for new units**,
  **measurement automation** (replacing a manual measurement), or **discovery/screening**
  before recommending a method; the class decides what ML can contribute.
- Compute effective sample size from independent units, not rows (formula in Instructions).
- Map every level of the data hierarchy to a leakage or confounding risk.
- Name at least two baselines: the field's classical model and a trivial reference.
- State go / redesign / stop criteria before any model is trained (pre-specified), and
  mark later scoping changes as exploratory.
- Default to the Open Science branch: planned release of code, splits, and data or a data
  access route; closed or proprietary data is named as the non-default exception.

**Constraints — Must Not:**
- Do not invent citations, DOIs, datasets, sample sizes, ICCs, or performance figures;
  mark missing values `[user-supplied]` and ask.
- Do not recommend ML for a question about the size or direction of an effect when a
  (mixed) regression answers it directly; ML may be an adjunct, not a substitute.
- Do not treat technical replicates, multiple images, or cells from the same animal as
  independent samples.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" in drafted text.

**Instructions:**

1. **Restate the question and claim (ST-01).** One sentence each; name the population the
   claim is about (new patients, new plates, new field sites, new compounds).
2. **Classify the question.** Inference → classical/mixed model first, ML only if
   prediction adds something stated. Prediction → ML candidate, judged against a regularised
   regression baseline. Measurement automation → ML judged by agreement with expert
   measurement (Bland–Altman limits, ICC, Dice/IoU for segmentation) on held-out units.
   Discovery/screening → ML ranking judged by prospective hit rate.
3. **Scope the unit of independence (CM-03).** Identify the highest level the claim
   generalises over; that level is the unit for sample size and for splitting.
4. **Compute effective sample size (NE-11).** `n_eff = n_obs / (1 + (m − 1) × ICC)` for
   clusters of average size `m`; if ICC is unknown, report the range between number of
   clusters (ICC → 1) and number of observations (ICC → 0) and say which end is plausible.
   Compare `n_eff` and the number of positive cases to the model's complexity.
5. **Map leakage and confounding by level.** For each level: could rows from one unit fall
   in both train and test? Is the level correlated with the label (e.g., all treated wells
   on plate 1)? A level perfectly confounded with the label means the model can learn the
   batch, not the biology; no analysis fixes that — it is a data-collection problem.
6. **Fix baselines.** Trivial (majority class / mean), the field's classical model, and
   any published heuristic. ML is warranted only if it is expected to beat these by a
   margin that matters for the claim; state that margin.
7. **Stress-test the plan (QA-02).** Ask: what result would a sceptical reviewer accept,
   and what would they dismiss as batch learning, overfitting, or circularity?
8. **State kill signals (DP-13).** Go / redesign (collect units, rebalance batches) / stop
   (classical model suffices or data cannot support the claim), each with its trigger.

**Output format (locked):**

```
## Question & Claim
- Discipline / study type:
- Question (one sentence):
- Claim and target population:
- Question class: [inference | prediction | measurement automation | discovery]

## Data Hierarchy & Effective Sample Size
| Level | Count | Avg size per unit | ICC [user-supplied/estimated/unknown] |
|---|---|---|---|
n_obs = .. ; clusters at claim level = .. ; n_eff = .. (range if ICC unknown)
Positive cases at claim level: ..

## Classical vs ML
| Approach | What it answers | Fit to this question | Data demand |
|---|---|---|---|

## Leakage & Confounding Map
| Level | Leakage route | Confounded with label? | Mitigation (design / split / adjustment) |
|---|---|---|---|

## Baselines and Required Margin
## Decision: [go | redesign data collection | stop / use classical model]
- Triggers for each:
- Pre-specified items (locked now):
- Exploratory items:
## Open Science plan
```

**Reporting-standard alignment:** REFORMS consensus recommendations for ML-based science
(study goals, data, leakage, baselines); DOME recommendations for supervised ML in biology
(Data, Optimisation, Model, Evaluation); TRIPOD+AI when the output is a clinical prediction
model; Kapoor–Narayanan leakage taxonomy; design-effect formula for clustered data.

**Verification checklist (before delivering):**
- [ ] Discipline, study type, question, and claim population restated.
- [ ] Question classified, and the classification drives the method recommendation.
- [ ] `n_eff` computed or bounded from the real unit of independence.
- [ ] Every hierarchy level has a leakage/confounding row.
- [ ] Label-confounded batches are named as a data-collection problem, not an analysis one.
- [ ] At least two baselines and a required margin stated.
- [ ] Go / redesign / stop triggers fixed before training; exploratory items labelled.
- [ ] No invented numbers or citations; gaps marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Rows as sample size | "We have 40,000 cells" from 6 mice | Count units at the claim level; compute `n_eff` |
| ML for an effect-size question | Classifier accuracy offered as evidence that treatment changes Y | Route inference questions to a (mixed) model; ML only as stated adjunct |
| Batch learned as biology | All controls imaged on day 1, all treated on day 2; 98% accuracy | Check level–label confounding first; stop and redesign if perfect |
| Baseline-free success | "AUC 0.81" with no comparison | Require classical and trivial baselines plus a meaningful margin |
| Automation judged by correlation | r = 0.95 with manual counts hides bias at high density | Use agreement statistics (Bland–Altman, ICC) on held-out units |
