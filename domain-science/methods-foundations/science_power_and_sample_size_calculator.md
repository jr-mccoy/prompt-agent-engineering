---
title: "Power and Sample Size Calculator"
category: science/methods-foundations
description: "Design a power and sample-size analysis that surfaces every assumption, runs three scenarios and a sensitivity grid, and routes formal computation to the right frequentist or Bayesian tool."
techniques:
  - ST-01
  - ST-03
  - DS-02
  - NE-10
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - power-analysis
  - sample-size
  - study-design
  - frequentist
  - bayesian
  - sensitivity-analysis
  - effect-size
  - pre-registration
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/methods-foundations/science_pilot_study_designer.md
  - domain-science/methods-foundations/science_methodology_decision_tree.md
---

# Power and Sample Size Calculator

**Objective:** Produce a fully-specified power and sample-size *design* — not a single number — that writes out every assumption (effect size, variance/dispersion, alpha, target power, attrition, allocation ratio, multiplicity correction), reports a pessimistic/central/optimistic scenario set plus a sensitivity grid, and names the exact frequentist and Bayesian tools to run the formal computation. The output is auditable, pre-registerable, and honest about what it can and cannot guarantee.

**When to use:** During study design, after the question, design, and primary outcome are fixed but before data collection or pre-registration. Precondition: you have a defensible literature anchor or pilot estimate for the key parameters, or you are prepared to mark them `[user-supplied]`.

**Required inputs:**
- **Discipline.** <field, e.g. clinical trials, ecology, psychology, genomics>
- **Study type.** <observational / experimental / computational / etc.>
- **Primary hypothesis and outcome.** The single confirmatory comparison the study is powered for, and the outcome's data type (continuous / binary / count / time-to-event / clustered).
- **Statistical test or model.** The analysis the power calc must match (e.g. two-sample t-test, logistic regression, mixed-effects model, Cox PH, ANOVA).
- **Effect size anchor.** Smallest effect of interest (SESOI) and/or expected effect, each with its source — `[user-supplied]` literature, pilot, or domain judgment.

**Optional inputs:**
- Variance / SD / dispersion / event rate / baseline hazard, with source.
- Allocation ratio, number of groups/arms, repeated measures structure.
- Expected attrition / loss-to-follow-up and missingness mechanism.
- Clustering (ICC, cluster size) for multilevel designs.
- Multiplicity structure (number of primary tests, correction method).
- Cost or recruitment ceiling (max feasible N).
- Bayesian priors and decision threshold (Bayes factor cutoff, ROPE, posterior probability target).

**Constraints — Must:**
- Output **three scenarios** (pessimistic / central / optimistic), each with its complete assumption set written out explicitly.
- Include a **sensitivity-analysis table**: required N (or achieved power) across a grid of plausible effect sizes (and a second key parameter where relevant).
- Offer **both** a frequentist path and a Bayesian path, naming concrete methods/tools for each.
- State explicitly that this prompt produces the *design and assumptions* and that formal numbers must be computed in named software; show the call/parameterization to run.
- Distinguish the **pre-specified confirmatory** power target from any **exploratory** secondary analyses; secondary outcomes are not powered unless stated.
- Use calibrated language; report assumptions as assumptions and uncertainty as uncertainty.
- Default to an **Open Science** branch (share code/assumptions/seed and pre-register the power analysis); name closed-data handling only as a non-default exception with justification.

**Constraints — Must Not:**
- Do not invent citations, DOIs, effect sizes, prior-study parameters, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not output a single "the sample size is N" answer with no assumption set.
- Do not invent prior effect sizes to fill a gap — require a `[user-supplied]` literature anchor or pilot; if absent, design around the SESOI and say so.
- Do not present post-hoc / observed-power calculations as informative for an already-run study.
- Do not use "novel", "groundbreaking", "first-ever", or "gold standard" in drafted text.
- Do not claim the computed N guarantees a significant result — power is a long-run probability under stated assumptions.

**Instructions:**

1. **Lock the inferential target.** Restate the primary hypothesis, the single confirmatory test/model, the outcome data type, and the directionality (one- vs two-sided). Flag any mismatch between the stated test and the design (e.g. clustered data analyzed as independent).
2. **Surface and source every parameter.** Build an explicit assumption ledger: effect size (and SESOI), variance/dispersion/event rate, alpha, target power, allocation ratio, attrition, clustering, multiplicity. For each, record the value and its provenance (`[user-supplied]` literature / pilot / SESOI judgment). Mark gaps and ask.
3. **Set the three scenarios.** Define pessimistic, central, and optimistic assumption sets by varying the most consequential parameters (typically effect size and variance/event rate, plus attrition). Write each set out in full so a reader can reproduce it.
4. **Specify the frequentist path.** Name the appropriate method and tool: `pwr` (e.g. `pwr.t.test`, `pwr.2p.test`, `pwr.anova.test`) or G*Power for closed-form cases; `simr` or a custom Monte Carlo simulation in R/Python (`statsmodels`, `simr`, `simstudy`) for mixed-effects, longitudinal, or non-standard models. Give the exact parameterization to run for each scenario.
5. **Specify the Bayesian path.** Offer design analysis (Gelman–Carlin: Type S and Type M error rates), Bayes-factor design analysis (`BFDA`), and assurance / probability-of-success (averaging power over a prior on the effect). Name the decision rule (BF threshold, ROPE + posterior probability, or expected precision) and the tool to run it.
6. **Account for attrition and multiplicity.** Inflate the analyzable-N target to an enrolled-N target using the stated attrition rate. Adjust alpha (or the decision rule) for the pre-specified number of primary comparisons; keep secondary/exploratory tests outside the powered target.
7. **Build the sensitivity grid.** Tabulate required N (fixed power) or achieved power (fixed N) across a grid of effect sizes spanning at least the SESOI to the optimistic estimate, plus a second axis (variance, ICC, or attrition) where it materially changes the answer.
8. **Choose and justify a recommendation.** Select a planning value (usually the central or SESOI-anchored scenario), state why, and check it against any feasibility ceiling. If the feasible N cannot reach target power for the SESOI, say so plainly and list options (relax power, widen the SESOI, change design, or do not run).
9. **Hand off to computation and pre-registration.** Provide the ready-to-run software call(s), the random seed for simulation reproducibility, and a pre-registration-ready power statement (assumptions, scenarios, decision rule).

**Output format (locked):**

```
## Inferential Target
[primary hypothesis | test/model | outcome type | sided-ness | analysis-design match check]

## Assumption Ledger
| Parameter | Value | Source | Notes/uncertainty |
|---|---|---|---|
[effect size / SESOI, variance or dispersion or event rate, alpha, target power, allocation ratio, attrition, clustering (ICC/cluster size), multiplicity]

## Three Scenarios
### Pessimistic
[full assumption set written out]
### Central (planning)
[full assumption set written out]
### Optimistic
[full assumption set written out]

## Frequentist Path
[method | tool (G*Power / pwr / simr / statsmodels) | exact parameterization per scenario | enrolled-N after attrition]

## Bayesian Path
[design analysis (Type S/M) / BFDA / assurance | decision rule | tool | parameterization per scenario]

## Sensitivity Analysis
| Effect size | [2nd axis: variance/ICC/attrition] | Required N (power=__) / Achieved power (N=__) |
|---|---|---|
[grid spanning SESOI → optimistic]

## Recommendation
[planning value chosen + rationale | feasibility check vs ceiling | options if underpowered]

## Computation & Pre-Registration Handoff
[ready-to-run software call(s) | random seed | pre-registration power statement | pre-specified vs exploratory note]

## Open-Data / Reproducibility Note
[Open Science default: share code/seed/assumptions; closed-data exception only with justification]
```

**Reporting-standard alignment:** Align the power statement with the relevant trial/reporting standard — CONSORT (item 7a, sample size) for RCTs; STROBE for observational analytic studies; ARRIVE 2.0 for animal experiments; the discipline's pre-registration template (e.g. OSF, AsPredicted) for the confirmatory analysis. Name the standard explicitly in the handoff.

**Verification checklist (before delivering):**
- [ ] Output presents three scenarios, each with a complete written-out assumption set — never a lone number.
- [ ] Every parameter has a source label; no fabricated effect sizes, variances, event rates, or citations.
- [ ] Both a frequentist and a Bayesian path are given, each naming concrete methods/tools.
- [ ] A sensitivity grid spans at least SESOI → optimistic effect size.
- [ ] Attrition inflates analyzable-N to enrolled-N; multiplicity adjustment is stated.
- [ ] The stated test/model matches the design (clustering, repeated measures, outcome type honored).
- [ ] Pre-specified confirmatory target is distinguished from exploratory analyses.
- [ ] A reporting standard is named and an Open Science default branch is present.
- [ ] No banned hype terms; no claim that N guarantees significance.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Optimistic effect inflation | A literature point estimate used as the planning value, ignoring publication bias / winner's curse | Anchor on the SESOI; show a scenario where the true effect is the SESOI and the published estimate is shrunk. |
| Single-number false precision | One tidy "N = 128" with hidden assumptions | Force the three-scenario + assumption-ledger format; never deliver a bare number. |
| Design/test mismatch | Power computed for a two-sample t-test on clustered or longitudinal data | Check the analysis-design match in Step 1; route clustered/mixed designs to simulation (simr). |
| Post-hoc power | "Observed power" reported after a null result | Refuse; explain post-hoc power is a deterministic function of the p-value and uninformative. |
| Attrition ignored | Analyzable-N reported as the recruitment target | Always inflate to enrolled-N using the stated/`[user-supplied]` attrition rate. |
| Bayesian path as escape hatch | Switching to "Bayes needs no power" to dodge sizing | Use BFDA/assurance to show Bayesian designs still have a sample-size/precision tradeoff. |
