---
title: "Interpreting ML Models for Scientific Claims — What Feature Attributions, Saliency, and Learned Representations Can and Cannot Support"
category: science/ml-for-science
description: "Turn ML interpretability output (SHAP, permutation importance, saliency maps, attention, learned embeddings) into calibrated scientific claims: place each claim on a ladder from predictive to model-attribution to data-association to mechanistic, test attributions for stability, correlated-feature artefacts, Rashomon disagreement, and confound or shortcut learning, and state the experiment needed before any mechanistic claim is made."
techniques:
  - ST-01
  - RT-05
  - QA-02
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - ml-for-science
  - interpretability
  - feature-attribution
  - shortcut-learning
  - mechanistic-claims
  - saliency-maps
  - confounding
  - does-shap-prove-causation
  - what-did-the-model-learn
  - overclaiming-ml-results
updated: "2026-10-03"
related_prompts:
  - domain-AI-ML/feature-engineering/mlfeature_importance_analysis.md
  - domain-science/statistics/science_causal_inference_design.md
  - domain-science/computational/science_ml_for_science_validation_audit.md
---

# Interpreting ML Models for Scientific Claims

**Objective:** Decide which scientific statements an interpretability analysis actually
licenses. Each candidate claim is placed on a four-rung ladder — predictive, model
attribution, data association, mechanistic — and tested against the known failure modes of
interpretability methods and against confounds in how the data were collected. The output
is a claim ledger with calibrated wording and, for any mechanistic aspiration, the
experiment or causal design that would be required.

**When to use:** When drafting the Results or Discussion of a paper whose findings include
"the model identified feature X," "the model attends to region Y," or "the embedding
reveals structure Z"; when reviewing such a paper; or before turning model attributions
into follow-up experiments. **Boundary:** `domain-AI-ML/` covers interpretability for
building, debugging, and governing ML systems
(`domain-AI-ML/feature-engineering/mlfeature_importance_analysis.md` for model development;
`domain-AI-ML/responsible-ai-governance/rai_interpretability_analysis.md` for trust in a
deployed model); this prompt covers ML as an instrument for scientific inference, where
the question is what a statement about the model allows you to say about the world.
Whether the model's performance itself is trustworthy is
`../computational/science_ml_for_science_validation_audit.md` — run that first; an
interpretation of a leaky model is an interpretation of the leak.

**Required inputs:**
- **Discipline.** [user-supplied]
- **Study type.** [user-supplied]
- **The model and its validated performance,** with the split it was validated on
  (grouped / temporal / external tier) `[user-supplied]`.
- **Interpretability outputs** and the method behind each (SHAP variant, permutation
  importance, integrated gradients, saliency, attention weights, embedding projection),
  computed on which data (train / held-out).
- **The candidate claims,** verbatim, as the authors would like to write them.

**Optional inputs:**
- Correlation structure among top features; known confounders and nuisance variables
  (batch, site, scanner, operator, acquisition date).
- Attributions across seeds, folds, or alternative model classes.
- Prior mechanistic knowledge or existing experimental evidence `[user-supplied]`.

**Constraints — Must:**
- Assign every candidate claim to one rung: (1) **predictive** — Y is predictable from X in
  population P; (2) **model attribution** — this model relies on F; (3) **data
  association** — F is associated with Y in P; (4) **mechanistic/causal** — F affects Y
  via M. State what evidence each rung needs.
- Treat attributions as properties of the model, not of the world, until rung 3 evidence
  (stability, correlated-feature handling, confound checks) is in place.
- Test stability across seeds, folds, and at least one alternative model class with
  similar performance (Rashomon set); report disagreement rather than averaging it away.
- Check for shortcut learning: can the confounders be predicted from the inputs, and do
  top attributions coincide with acquisition artefacts?
- For any rung-4 aspiration, name the intervention or causal design that would test it,
  and label the ML finding hypothesis-generating.
- Keep pre-specified interpretation analyses separate from exploratory ones.
- Default to the Open Science branch: release attribution code, seeds, and the data split.

**Constraints — Must Not:**
- Do not invent attributions, effect sizes, citations, or biological/physical mechanisms;
  mark gaps `[user-supplied]`.
- Do not phrase SHAP values, permutation importance, saliency, or attention weights as
  causes, drivers, or mechanisms.
- Do not interpret attributions computed on a model that has not passed a leakage audit
  without stating that caveat in the first line.
- Do not use "novel," "groundbreaking," "first-ever," "gold standard," or "reveals the
  mechanism" in drafted text.

**Instructions:**

1. **Restate each candidate claim (ST-01)** and assign its rung.
2. **Confirm the predictive base.** Rung 1 requires validated performance on the split
   that matches the claim population; if the model was validated only on random splits,
   every higher rung inherits that limit.
3. **Interrogate each attribution (RT-05).**
   - *Correlated features:* attribution is split or arbitrarily assigned among correlated
     features; marginal permutation creates unrealistic samples — use grouped or
     conditional importance and report the correlation structure.
   - *Method validity:* saliency methods can be insensitive to model weights (run
     model- and label-randomisation sanity checks); attention weights are not
     explanations by default.
   - *Stability:* rank agreement of top features across seeds/folds/model classes.
   - *Faithfulness:* remove-and-retrain or ablation — does performance fall when F is removed?
4. **Hunt for confounds and shortcuts (QA-02).** Predict each known nuisance variable from
   the inputs; inspect whether attributions concentrate on borders, markers, text overlays,
   scanner-specific texture, or batch-correlated features; compare performance within
   batch/site strata.
5. **Grade each claim.** Supported at rung 1/2/3, or not supported; give calibrated wording
   (CM-02: wording constrained to the rung achieved).
6. **Specify the next evidence for higher rungs.** For rung 3: adjusted association in an
   independent dataset. For rung 4: perturbation/knockout/intervention experiment, or a
   causal identification strategy (route to `science_causal_inference_design.md`).
7. **State uncertainty and limits (QA-04).** Which claims rest on one model class, one
   seed, one site; what an alternative explanation would predict.

**Output format (locked):**

```
## Predictive Base
- Model / validation split / tier / performance with interval:
- Leakage audit status: [passed / not run → caveat applies to everything below]

## Claim Ledger
| # | Candidate claim (verbatim) | Rung sought | Evidence available | Rung supported | Calibrated wording |
|---|---|---|---|---|---|

## Attribution Checks
| Feature/region | Method | Correlated with | Stable across seeds/folds/models? | Ablation effect | Sanity check |
|---|---|---|---|---|---|

## Confound & Shortcut Checks
| Nuisance variable | Predictable from inputs? | Overlap with top attributions | Within-stratum performance |
|---|---|---|---|

## Next Evidence Required
| Claim | Target rung | Experiment / causal design | What result would refute it |
|---|---|---|---|

## Pre-specified vs Exploratory
## Limits and alternative explanations
## Open Science release
```

**Reporting-standard alignment:** REFORMS items on interpretation and claims; DOME
(model interpretability and evaluation); TRIPOD+AI where clinical; saliency-map sanity
checks and shortcut-learning literature; Rashomon-set / model-class-reliance reasoning;
causal-inference standards for any mechanistic follow-up (route to statistics/).

**Verification checklist (before delivering):**
- [ ] Every candidate claim has a rung sought and a rung supported.
- [ ] Leakage-audit status stated before any interpretation.
- [ ] Correlated features identified and importance computed accordingly.
- [ ] Stability across seeds/folds/model classes reported, including disagreement.
- [ ] Confound predictability and within-stratum performance checked.
- [ ] No attribution phrased as cause, driver, or mechanism.
- [ ] Each rung-4 aspiration has a named experiment or causal design and a refutation result.
- [ ] No invented values, mechanisms, or citations; gaps marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Attribution as mechanism | "Gene F drives resistance (top SHAP)" | Rung 2 wording: "the model relies on F"; name the knockout that would test it |
| Shortcut learning | Saliency on the hospital marker or slide edge; high accuracy | Predict site/batch from inputs; mask artefacts; stratified performance |
| Correlated-feature artefact | F ranked top while its correlated twin ranks low | Grouped/conditional importance; report the correlation cluster |
| Single-model story | One architecture's attributions presented as "what the data show" | Compare with ≥1 equally accurate model class; report rank disagreement |
| Pretty saliency, weight-insensitive | Maps look the same after randomising weights | Run model- and label-randomisation sanity checks before interpreting |
| Embedding clusters as discovery | UMAP clusters align with processing date | Colour by nuisance variables; test cluster–batch association |
