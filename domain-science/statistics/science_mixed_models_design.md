---
title: "Mixed-Effects Model Design"
category: science/statistics
description: "Specify fixed vs random effects, nested vs crossed structures, and a justifiable random-effects structure while diagnosing singular fits and choosing REML vs ML."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - mixed-models
  - random-effects
  - lme4
  - glmm
  - reml-vs-ml
  - singular-fit
  - nested-crossed
  - parsimony
updated: "2026-06-26"
related_prompts:
  - domain-science/statistics/science_statistical_test_selector.md
  - domain-science/methods-foundations/science_methodology_decision_tree.md
  - domain-science/methods-foundations/science_confound_and_bias_audit.md
---

# Mixed-Effects Model Design

**Objective:** Help a researcher specify a defensible mixed-effects (multilevel) model for clustered or repeated-measures data. Decide what enters as fixed vs random, whether grouping factors are nested or crossed, what random-slope structure the design can support, and how to estimate and compare models. Surface the tension between the maximal random-effects structure (Barr et al.) and parsimony to avoid singular fits (Matuschek et al.).

**When to use:** You have non-independent observations — repeated measures within subjects, pupils within classrooms within schools, items crossed with subjects, plots within blocks — and need to model the grouping structure rather than ignore or fully aggregate it.

**Required inputs:**
- **Discipline.** [user-supplied] (e.g., psycholinguistics, ecology, education, neuroscience).
- **Study type.** [user-supplied] (observational / experimental / longitudinal / etc.).
- **Response variable + its distribution.** Continuous, binary, count, proportion, ordinal, etc.
- **Grouping/clustering factors.** Names and approximate level counts (e.g., 40 subjects, 200 items, 6 schools).
- **Predictors of interest.** Which are within-cluster vs between-cluster; which are the confirmatory targets.

**Optional inputs:**
- Sample size per cluster and balance.
- Whether this analysis is pre-registered/confirmatory or exploratory.
- Software preference (lme4, glmmTMB, brms, nlme).
- Prior convergence warnings or singular-fit messages already seen.

**Constraints — Must:**
- Distinguish LMM from GLMM: if the response is non-Gaussian, specify the distribution family and link, and address overdispersion (e.g., observation-level random effect or a quasi/negative-binomial/Beta family in glmmTMB).
- State explicitly which terms are fixed vs random and why; partial pooling rationale must be given for each random effect.
- Determine nested vs crossed structure from the design, not from default coding; warn that implicit nesting (reused level labels across groups) must be coded explicitly.
- Apply REML for variance-component estimation and for comparing models that differ only in random effects; require ML (REML=FALSE) for likelihood-ratio comparison of models differing in fixed effects.
- Present both the maximal-justifiable random-effects structure (Barr et al. "keep it maximal" for confirmatory designs) and a parsimonious alternative (Matuschek et al.), and recommend by data support.
- Default to the Open Science branch: share data, model-fitting code/script, and the random-effects specification.

**Constraints — Must Not:**
- Do not invent citations, DOIs, datasets, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not recommend a maximal model the data cannot support; do not silently drop random slopes without flagging the inferential cost.
- Do not interpret a singular fit as a valid simplification without diagnosis.
- Do not use the words "novel", "groundbreaking", "first-ever", or "gold standard" in drafted prose.
- Do not compare fixed effects with REML-fitted likelihoods.

**Instructions:**

1. **Restate the design and dependency structure.** Name each source of non-independence and how many levels it has. State whether the question is confirmatory (pre-specified) or exploratory.
2. **Classify each predictor.** Mark within-cluster vs between-cluster. Only within-cluster predictors can have meaningful random slopes; between-cluster predictors cannot vary within a group.
3. **Choose LMM vs GLMM.** If non-Gaussian, fix the family/link and plan an overdispersion check. Note when glmmTMB is preferable to lme4 (zero-inflation, dispersion modeling, non-standard families).
4. **Decide nested vs crossed.** Determine whether grouping factors are hierarchically nested (school/class/pupil) or crossed (subjects × items). Specify explicit syntax so reused labels are not mistakenly pooled.
5. **Build the maximal random-effects structure.** Include random intercepts for each grouping factor and random slopes for every within-cluster predictor whose variation the design can identify (Barr et al.).
6. **Plan REML vs ML usage.** Use REML for the final variance estimates and for random-effects comparisons; switch to ML for likelihood-ratio tests of fixed effects; refit with REML for reporting.
7. **Specify singularity/convergence diagnostics.** Plan to inspect variance estimates near zero, perfect correlations (±1) among random effects, and convergence warnings. List remedies in order: rescale/center predictors, change optimizer, reduce correlation parameters (`||`), then drop the least-supported random slope.
8. **Define the parsimony fallback.** Per Matuschek et al., describe a reduced model that preserves the slopes critical for the confirmatory test while removing unsupported terms; pre-commit the simplification path so it is not a garden of forking paths.
9. **Adversarial pass.** Ask what inflates Type I error if random slopes are dropped, whether the cluster count is large enough to estimate variance components, and whether degrees-of-freedom / p-value method (Satterthwaite, Kenward-Roger, parametric bootstrap) is appropriate for the cluster count.

**Output format (locked):**

```
## Design Summary
- Response (+ distribution/family/link):
- Confirmatory or exploratory:
- Dependency structure (grouping factors, level counts):

## Fixed vs Random Specification
| Term | Fixed / Random | Within or Between cluster | Rationale (partial pooling) |
|---|---|---|---|

## Random-Effects Structure
- Nested vs crossed (with explicit syntax):
- Maximal model (Barr et al.):
- Parsimonious model (Matuschek et al.):
- Recommended starting structure + why:

## Estimation Plan
- REML vs ML usage by comparison:
- p-value / df method:

## Diagnostics & Singularity Plan
- Convergence checks:
- Singular-fit remedies (ordered):
- Overdispersion check (if GLMM):

## Open Science
- Data / code / model-spec sharing plan:

## Open Questions / [user-supplied] gaps
```

**Reporting-standard alignment:** Report per lme4/glmmTMB conventions (full random-effects structure, estimation method, optimizer, convergence status, software versions); align experimental designs with CONSORT and observational designs with STROBE where applicable.

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured (or marked `[user-supplied]`).
- [ ] Each random effect justified; within vs between predictors classified.
- [ ] Nested vs crossed resolved with explicit, non-ambiguous syntax.
- [ ] LMM vs GLMM decided; family/link and overdispersion addressed if GLMM.
- [ ] Maximal and parsimonious structures both presented with a recommendation.
- [ ] REML vs ML correctly assigned to each comparison.
- [ ] Singularity/convergence diagnostics and ordered remedies specified.
- [ ] No fabricated citations/data/specs; banned hype words absent; Open Science branch present.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Maximal model on thin data | Model "converges" but with ±1 random-effect correlations | Treat boundary correlations as singular; reduce per pre-committed path |
| Implicit nesting | Crossed syntax silently pools reused level labels | Force explicit nesting syntax; verify level membership |
| REML LRT on fixed effects | Likelihood-ratio test "significant" but invalid | Refit with ML before comparing fixed effects |
| Anti-conservative test | Dropping random slopes lowers p below threshold | Keep slopes for the confirmatory contrast; report the cost of removal |
| Ignored overdispersion | GLMM SEs look tight and significant | Check dispersion; add OLRE or use a dispersion-modeling family |
