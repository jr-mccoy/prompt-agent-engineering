---
title: "Bayesian Analysis Plan"
category: science/statistics
description: "Pre-specify priors, prior predictive checks, computation diagnostics, posterior summaries, a decision rule, and a multi-prior sensitivity analysis."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - NE-10
difficulty: advanced
tags:
  - bayesian
  - prior-selection
  - sensitivity-analysis
  - rope-hdi
  - bayes-factor
  - posterior-predictive-check
  - mcmc-diagnostics
  - pre-specification
updated: "2026-06-26"
related_prompts:
  - domain-science/statistics/science_pre_specified_analysis_plan.md
  - domain-science/statistics/science_outlier_handling_decision.md
  - domain-science/statistics/science_p_hacking_self_check.md
  - domain-science/methods-foundations/science_preregistration_drafter.md
  - domain-science/methods-foundations/science_replicability_premortem.md
---

# Bayesian Analysis Plan

**Objective:** Help the researcher pre-specify a complete Bayesian workflow: prior selection on the scale of the data, a prior predictive check, the likelihood/model, the computation and its diagnostics, the posterior summaries, an explicit decision rule, and a sensitivity analysis across multiple priors. The plan makes clear that Bayesian inference is not a license to skip pre-specification.

**When to use:** You intend to fit a Bayesian model and want the priors, model, decision rule, and sensitivity analysis fixed before seeing the outcome data, with diagnostics and reporting locked in advance.

**Required inputs:**
- **Discipline.** [user-supplied]
- **Study type.** [user-supplied] (observational / experimental / computational / hierarchical / etc.)
- **Estimand / quantity of interest.** [user-supplied] (e.g., group difference, slope, odds ratio, variance component)
- **Likelihood / outcome distribution and link.** [user-supplied] (e.g., Gaussian, Bernoulli-logit, negative binomial)
- **Available domain knowledge for priors.** [user-supplied] (plausible effect ranges, prior studies, expert elicitation)

**Optional inputs:**
- Pre-registration identifier (OSF / AsPredicted).
- Planned sample size or a Bayes Factor Design Analysis (BFDA) target.
- Software/sampler (e.g., Stan, PyMC, brms) and version.
- A ROPE (region of practical equivalence) width with scientific justification.

**Constraints — Must:**
- Default to **weakly-informative** priors unless strong, justified information exists; show each prior on the scale of the data (parameter units), not as a bare distribution name.
- Run a **prior predictive check**: simulate data from the priors and confirm the implied outcomes are physically/scientifically plausible.
- Specify the full model: likelihood, link, hierarchy/random effects, and every prior.
- Specify computation and **MCMC diagnostics with thresholds**: R-hat (e.g., < 1.01), effective sample size (bulk and tail ESS targets), divergent transitions (target zero), and energy/BFMI where applicable.
- Report posterior summaries as a point estimate **and** a credible interval (state equal-tailed vs HDI), plus the posterior probability of direction and/or of a magnitude of interest.
- Pick and justify **one** primary decision rule: a Bayes factor threshold, **or** ROPE + HDI (Kruschke), **or** a posterior-probability target.
- Pre-specify a **prior sensitivity analysis** across at least 2–3 priors (e.g., weakly-informative, more diffuse, more skeptical/regularizing) and a **posterior predictive check**.
- Align reporting with a named Bayesian reporting standard (e.g., BARG / Bayesian analysis reporting guidelines) where one applies.

**Constraints — Must Not:**
- Do not invent citations, DOIs, datasets, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not choose priors after seeing the outcome data, or tune priors to push the posterior past a decision threshold.
- Do not report only a point estimate, or interpret a credible interval as a frequentist confidence interval.
- Do not treat "we used a flat prior" as automatically uninformative — show what it implies on the data scale.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" in drafted text.

**Instructions:**

1. **Fix the quantity of interest.** State the estimand and the parameter(s) that encode it; state the likelihood/link and any hierarchy.
2. **Select priors on the data scale.** For each parameter, propose a weakly-informative prior, justify it from domain knowledge, and translate it into implied effect units (e.g., "Normal(0, 1) on log-OR implies OR mostly within [0.14, 7]").
3. **Run a prior predictive check.** Describe simulating outcomes from the priors and the criterion for plausibility (e.g., no impossible values, ranges consistent with the field); state how an implausible prior would be revised — before data.
4. **Specify computation + diagnostics.** Name the sampler, chains, iterations, warmup, and the diagnostic thresholds (R-hat, bulk/tail ESS, divergences, BFMI). State the action if a diagnostic fails (reparameterize, increase adapt_delta, etc.).
5. **Define posterior summaries.** Specify the point estimate (median/mean), the interval (HDI or equal-tailed, with mass), and the posterior probabilities to report (P(effect > 0), P(effect in ROPE), P(|effect| > threshold)).
6. **Pick and justify the decision rule.** Choose Bayes factor (state threshold + how computed, e.g., bridge sampling, and guard against marginal-likelihood prior sensitivity), or ROPE + HDI (state ROPE width + decision logic), or posterior-probability target. Map results to decisions with probability-weighted scenarios.
7. **Pre-specify the sensitivity analysis.** List the 2–3 alternative priors and state in advance that conclusions are robust only if the decision is stable across them; specify how disagreement across priors will be reported, not hidden.
8. **Plan the posterior predictive check.** Specify the test quantities (e.g., distribution of replicated data, specific moments, group-level fit) used to assess model adequacy, and what misfit would trigger model revision.

**Output format (locked):**

```
## Bayesian Analysis Plan — v[X.Y], frozen [DATE], precedes data lock [DATE]
Discipline: [...]   Study type: [...]   Pre-registration: [user-supplied or none]

## 1. Quantity of interest + model
Estimand: ...   Likelihood/link: ...   Hierarchy: ...

## 2. Priors (on the data scale)
| Parameter | Prior | Justification | Implied effect range |
|---|---|---|---|

## 3. Prior predictive check
Procedure: ...   Plausibility criterion: ...   Revision rule (pre-data): ...

## 4. Computation + diagnostics
Sampler/version: ...   Chains/iter/warmup: ...
Thresholds: R-hat < ...   Bulk/Tail ESS > ...   Divergences target: 0   BFMI: ...
Action on failure: ...

## 5. Posterior summaries
Point: ...   Interval (HDI/ETI, mass): ...   Posterior probabilities: P(...)=report

## 6. Decision rule (ONE, justified)
Type: [Bayes factor | ROPE+HDI | posterior-probability target]
Threshold/logic: ...

## 7. Prior sensitivity analysis
| Prior set | Description | Decision under this prior |
|---|---|---|
Robustness criterion: decision stable across all rows.

## 8. Posterior predictive check
Test quantities: ...   Misfit trigger: ...

## 9. Result → decision scenarios
| Posterior scenario | Decision |
|---|---|
```

**Reporting-standard alignment:** Kruschke ROPE+HDI framework; ASA statement on p-values (re: not reframing Bayesian outputs as significance); BFDA for design; BARG-style Bayesian reporting guidelines where applicable; OSF / AsPredicted for pre-registration.

**Verification checklist (before delivering):**
- [ ] Every prior is shown on the scale of the data with implied effect ranges.
- [ ] A prior predictive check and a pre-data revision rule are specified.
- [ ] MCMC diagnostics have explicit thresholds and a failure action.
- [ ] Posterior summaries include a point estimate, an interval (type stated), and posterior probabilities.
- [ ] Exactly one decision rule is chosen and justified.
- [ ] A 2–3 prior sensitivity analysis and a robustness criterion are pre-specified.
- [ ] A posterior predictive check with misfit triggers is specified.
- [ ] The plan states that Bayesian inference does not waive pre-specification.
- [ ] No fabricated citations, effect sizes, or specs; unknowns marked `[user-supplied]`.
- [ ] No banned hype language in drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Hidden-informative "flat" prior | A vague prior that implies absurd effect sizes | Require prior shown on data scale + prior predictive check |
| Prior tuned to result | Posterior crosses threshold under exactly one prior | Pre-specify 2–3 priors; require decision stability |
| BF prior fragility | A clean Bayes factor that swings with prior width | Report BF across priors; prefer ROPE+HDI when BF is unstable |
| Convergence theater | Pretty posteriors from non-converged chains | Enforce R-hat/ESS/divergence thresholds + failure action |
| CI misread | Credible interval reported as a confidence interval | State interval type and Bayesian interpretation explicitly |
| Skipped model check | Good-looking posterior, untested model fit | Require posterior predictive check with misfit trigger |
