---
title: "Causal Inference Design"
category: science/statistics
description: "Encode assumptions in a DAG, identify an estimand via the backdoor criterion or an instrument, and select among adjustment, IV, RDD, and DiD with assumptions and falsification tests stated."
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-02
  - CM-02
  - NE-10
difficulty: advanced
tags:
  - causal-inference
  - dag
  - confounding
  - instrumental-variables
  - regression-discontinuity
  - difference-in-differences
  - target-trial
  - e-value
updated: "2026-06-26"
related_prompts:
  - domain-science/statistics/science_statistical_test_selector.md
  - domain-science/methods-foundations/science_methodology_decision_tree.md
  - domain-science/methods-foundations/science_confound_and_bias_audit.md
---

# Causal Inference Design

**Objective:** Help a researcher move from an association to a credible causal estimand. Build a DAG that encodes assumptions, identify confounders/colliders/mediators, derive an identification strategy via the backdoor criterion or an instrument, select the matching design (adjustment, IV, RDD, DiD, or target-trial emulation), state the assumptions each strategy buys, and plan falsification tests plus sensitivity to unmeasured confounding.

**When to use:** You want to estimate the effect of an exposure/treatment/policy on an outcome from observational data, or you need to make the identifying assumptions of a quasi-experimental design explicit before estimating.

**Required inputs:**
- **Discipline.** [user-supplied] (e.g., epidemiology, economics, political science, program evaluation).
- **Study type.** [user-supplied] (observational / quasi-experimental / natural experiment).
- **Exposure and outcome.** Precisely defined, with timing.
- **Candidate causal structure.** Known/suspected confounders, mediators, and common effects (colliders).
- **Available design features.** Any instrument, running variable with a threshold, or policy adopted at a known time/place.

**Optional inputs:**
- Target population and the estimand of interest (ATE, ATT, LATE).
- Pre-registered vs exploratory status.
- Data structure (cross-section, panel, repeated cross-sections).
- Known threats: selection, measurement error, time-varying confounding.

**Constraints — Must:**
- Build the DAG before choosing a method; encode the exposure, outcome, and all assumed common causes/mediators/colliders, and use it to read off adjustment sets via the backdoor criterion.
- State the estimand (ATE/ATT/LATE) and the target population explicitly; for a target-trial framing, specify eligibility, treatment strategies, assignment, time zero, and outcome.
- For each candidate strategy, state the assumptions it requires: exchangeability/conditional ignorability, positivity, and consistency for adjustment; relevance + exclusion + monotonicity (+ independence) for IV; continuity at the cutoff for RDD; parallel trends (and no anticipation/confounded timing) for DiD.
- Plan falsification/probing tests appropriate to the design (negative controls, placebo outcomes, pre-trend tests for DiD, density/covariate-continuity tests for RDD, overidentification/weak-instrument diagnostics for IV).
- Include a sensitivity-to-unmeasured-confounding step (E-value or equivalent) for any adjustment-based estimate.
- Default to the Open Science branch: share the DAG, identification rationale, analysis script, and pre-registered analysis plan where possible.

**Constraints — Must Not:**
- Do not invent citations, DOIs, datasets, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not claim causation from association without stating and defending the identifying assumptions.
- Do not adjust for colliders or mediators when the target is the total effect; do not adjust away the very pathway under study.
- Do not present a weak or assumption-violating instrument as identifying.
- Do not use the words "novel", "groundbreaking", "first-ever", or "gold standard" in drafted prose.

**Instructions:**

1. **State the causal question and estimand.** Define exposure, outcome, timing, target population, and whether the estimand is ATE, ATT, or LATE. Mark confirmatory vs exploratory.
2. **Draw the DAG.** Enumerate nodes and directed edges encoding assumptions; classify each non-exposure variable as confounder, mediator, collider, or instrument. Note where assumptions are contested.
3. **Read off identification.** Apply the backdoor criterion to find a sufficient adjustment set, or identify a valid instrument/front-door path. If no admissible set exists with the measured variables, say so.
4. **Branch over identification strategies (Tree of Thoughts).** Evaluate adjustment (regression/matching/IPW/propensity), IV, RDD, DiD, and target-trial emulation against the data's selection mechanism, running variable, or policy timing. Keep the branches whose assumptions are most defensible here.
5. **State the assumptions purchased.** For the chosen strategy, list each identifying assumption and how plausible it is in this setting.
6. **Design falsification tests.** Specify the probes that would break the design if the assumptions fail (pre-trends, placebo cutoffs/outcomes, negative controls, instrument-outcome paths).
7. **Plan sensitivity analysis.** Compute or plan an E-value (or bias-bound) for unmeasured confounding; for IV/DiD/RDD, plan bandwidth/specification/robust-inference checks.
8. **Probability-weight the threats.** Lay out the scenarios under which the causal claim fails (residual confounding, exclusion violation, anticipation, manipulation at the cutoff), with a rough likelihood weight on each, so the conclusion's fragility is explicit.
9. **Lock the estimand-to-method-to-report chain.** Confirm the reported quantity matches the estimand and that uncertainty reflects design assumptions, not just sampling.

**Output format (locked):**

```
## Causal Question & Estimand
- Exposure / outcome / timing:
- Estimand (ATE/ATT/LATE) + target population:
- Confirmatory or exploratory:

## DAG
- Nodes and directed edges (text encoding):
- Confounders / mediators / colliders / instruments:
- Backdoor adjustment set (or "not identifiable with measured variables"):

## Identification Strategy (branched)
| Strategy | Fits this setting? | Identifying assumptions | Plausibility |
|---|---|---|---|
- Recommended strategy + why:

## Falsification & Sensitivity
- Falsification/placebo tests:
- E-value / unmeasured-confounding bound:
- Design-specific robustness checks:

## Threat Scenarios (probability-weighted)
| Failure mode | Rough likelihood | Effect on conclusion |
|---|---|---|

## Open Science
- DAG / plan / script sharing:

## Open Questions / [user-supplied] gaps
```

**Reporting-standard alignment:** Align with STROBE (observational reporting) and the target-trial emulation framework (Hernán-Robins); report the DAG, estimand, identification assumptions, and E-value per these conventions.

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured (or marked `[user-supplied]`).
- [ ] Estimand and target population stated; confirmatory vs exploratory marked.
- [ ] DAG encodes assumptions; confounders/colliders/mediators classified.
- [ ] Identification derived via backdoor criterion or a defended instrument.
- [ ] Strategy choice (adjustment/IV/RDD/DiD/target-trial) justified by structure.
- [ ] Each identifying assumption stated with a plausibility judgment.
- [ ] Falsification tests and an E-value/sensitivity step specified.
- [ ] No fabricated citations/data/specs; banned hype words absent; Open Science branch present.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Collider/over-adjustment | Adding more covariates "controls for everything" | Adjust only the backdoor set; never condition on colliders or mediators for total effects |
| Weak instrument | Large IV estimate, plausible story | Report first-stage F / relevance; defend the exclusion restriction explicitly |
| DiD parallel-trends failure | Significant post-period gap | Test pre-trends; check anticipation and confounded timing |
| RDD manipulation | Clean jump at the cutoff | Run density (McCrary) and covariate-continuity tests at the threshold |
| Residual confounding | Adjusted estimate looks decisive | Report an E-value; treat unmeasured confounding as live, not closed |
