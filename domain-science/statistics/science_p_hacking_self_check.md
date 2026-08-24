---
title: "P-Hacking & Garden-of-Forking-Paths Self-Check"
category: science/statistics
description: "Adversarially audit the researcher degrees of freedom taken, build a forking-paths register, and prescribe multiverse / specification-curve remedies."
techniques:
  - ST-01
  - QA-01
  - QA-02
  - RT-01
  - CM-02
  - NE-10
difficulty: advanced
tags:
  - p-hacking
  - garden-of-forking-paths
  - researcher-degrees-of-freedom
  - multiverse-analysis
  - specification-curve
  - harking
  - robustness-reporting
  - pre-registration
updated: "2026-06-26"
related_prompts:
  - domain-science/statistics/science_pre_specified_analysis_plan.md
  - domain-science/statistics/science_bayesian_analysis_plan.md
  - domain-science/statistics/science_outlier_handling_decision.md
  - domain-science/methods-foundations/science_preregistration_drafter.md
  - domain-science/methods-foundations/science_replicability_premortem.md
---

# P-Hacking & Garden-of-Forking-Paths Self-Check

**Objective:** Run an adversarial audit of an analysis to count and document the researcher degrees of freedom that were exercised — optional stopping, selective outcome/covariate/subgroup reporting, flexible exclusions and transformations, multiple model specifications, HARKing, and p-rounding. For each decision point, ask whether it was pre-specified and how many alternative paths existed, then prescribe remedies (multiverse / specification-curve analysis, pre-registration going forward, full robustness reporting, and disclosure of all measured variables).

**When to use:** Before submitting or finalizing an analysis, or when reviewing your own (or a collaborator's) result that "feels" too clean — to estimate its exposure to false-positive inflation and decide what to disclose or re-run.

**Required inputs:**
- **Discipline.** [user-supplied]
- **Study type.** [user-supplied] (observational / experimental / computational / secondary-data / etc.)
- **The reported result(s) and the model/test that produced them.** [user-supplied]
- **What was pre-registered or pre-specified, if anything.** [user-supplied] (OSF / AsPredicted / protocol, or "none")
- **All outcomes, covariates, and conditions that were measured/collected.** [user-supplied]

**Optional inputs:**
- The analysis history / decision log or code revision history.
- The number of models actually fit before the reported one.
- Sample-size history (was data collection stopped/extended based on interim looks?).

**Constraints — Must:**
- Adopt an **adversarial stance**: assume forking paths exist and try to find them; absence of evidence is not evidence of pre-specification.
- Enumerate each researcher-degree-of-freedom class explicitly and, for each, ask: was it pre-specified? how many alternatives were available? was the choice outcome-dependent?
- Distinguish the **garden of forking paths** (a single analysis that *would have differed* had the data differed — no p-hacking intent required, Gelman-Loken) from active p-hacking (Simmons-Nelson-Simonsohn).
- Estimate exposure to false-positive inflation qualitatively (low / moderate / high) per decision point, with reasoning.
- Prescribe concrete remedies: **multiverse analysis** (Steegen et al.) or **specification-curve analysis** for the live forking paths, pre-registration for future work, robustness reporting, and disclosure of all measured variables.
- Recommend reporting that separates confirmatory from exploratory claims and discloses the full set of analyses considered.

**Constraints — Must Not:**
- Do not invent citations, DOIs, datasets, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not certify an analysis as "clean" — output an exposure assessment, not absolution.
- Do not recommend silently rerunning until a path "works"; the multiverse must report the whole distribution of results.
- Do not let an unregistered post-hoc hypothesis be relabeled as the original prediction (HARKing).
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" in drafted text.

**Instructions:**

1. **Reconstruct the decision history.** From the inputs and any logs, list every analytic choice point between raw data and reported result (collection stop, exclusions, transformations, variable coding, covariate set, model form, subgroup, outcome selected, test, threshold).
2. **Enumerate the degrees of freedom by class.** For each class below, record whether it was exercised and how: optional stopping; selective outcome reporting; selective covariate selection; selective subgroup reporting; flexible exclusions; flexible transformations; multiple model specifications; HARKing; p-rounding / threshold-gaming.
3. **Pre-specification interrogation.** For each exercised choice, mark pre-specified (Y/N) against the registration/protocol, and count the plausible alternatives that were available at that fork.
4. **Estimate path count and inflation exposure.** Approximate the multiplicative size of the forking-paths space and rate each fork's false-positive exposure (low/moderate/high) with reasoning; use probability-weighted scenarios for what the result might have been under sibling paths.
5. **Flag HARKing and selective reporting.** Compare the reported hypothesis and outcomes against everything measured; identify any outcome/predictor that was measured but not reported, or any hypothesis that postdates the data.
6. **Prescribe the multiverse / specification curve.** Define the set of defensible alternative specifications and recommend running them all, reporting the full distribution of effect estimates and the share that cross the threshold — not just the reported point.
7. **Prescribe forward-looking fixes.** Recommend pre-registration for the next study, a disclosure statement listing all measured variables and analyses considered, and robustness reporting attached to the manuscript.
8. **Write the honest framing.** Draft a calibrated paragraph that states which claims are confirmatory vs exploratory and reports the analysis's exposure to forking-paths inflation.

**Output format (locked):**

```
## Forking-Paths Self-Check — [DATE]
Discipline: [...]   Study type: [...]   Pre-registration: [user-supplied or none]
Result under audit: ...

## 1. Forking-paths register
| Decision point | Alternatives available | Pre-specified? | Outcome-dependent? | False-positive exposure |
|---|---|---|---|---|
(one row per choice point; exposure = low/moderate/high + reason)

## 2. Degrees-of-freedom by class
| DoF class | Exercised? | How | Pre-specified? |
|---|---|---|---|
| Optional stopping | | | |
| Selective outcome reporting | | | |
| Selective covariate selection | | | |
| Selective subgroup reporting | | | |
| Flexible exclusions | | | |
| Flexible transformations | | | |
| Multiple model specifications | | | |
| HARKing | | | |
| p-rounding / threshold-gaming | | | |

## 3. Path-space estimate + sibling-result scenarios
Approx. number of defensible paths: ...
| Sibling specification | Plausible result |
|---|---|

## 4. HARKing / selective-reporting flags
Measured-but-unreported variables: ...   Post-hoc-as-predicted hypotheses: ...

## 5. Remedies
Multiverse / specification-curve set: ...
Pre-registration plan (next study): ...
Disclosure statement (all measured vars + analyses considered): ...
Robustness reporting to attach: ...

## 6. Calibrated honest framing (draft)
[confirmatory vs exploratory claims + exposure statement]
```

**Reporting-standard alignment:** Simmons-Nelson-Simonsohn (researcher degrees of freedom, disclosure of all measured variables); Gelman-Loken (garden of forking paths); Steegen et al. (multiverse analysis); specification-curve analysis; ASA statement on p-values; OSF / AsPredicted for pre-registration.

**Verification checklist (before delivering):**
- [ ] Every analytic choice point is listed in the forking-paths register.
- [ ] All nine degrees-of-freedom classes are explicitly assessed (exercised Y/N + pre-specified Y/N).
- [ ] Pre-specification is checked against the actual registration/protocol, not assumed.
- [ ] An approximate path-space size and per-fork inflation exposure are stated.
- [ ] HARKing and measured-but-unreported variables are surfaced.
- [ ] A concrete multiverse / specification-curve set is prescribed, reporting the full distribution.
- [ ] Forward fixes (pre-registration, disclosure statement, robustness reporting) are given.
- [ ] The output assesses exposure rather than certifying "clean."
- [ ] No fabricated citations, effect sizes, or specs; unknowns marked `[user-supplied]`.
- [ ] No banned hype language in drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| False "all pre-specified" | Claims of pre-specification with no registration | Check each fork against the actual registration; mark N when absent |
| Innocent forking missed | "No p-hacking intent, so we're fine" | Apply Gelman-Loken: data-contingent choices inflate error even without intent |
| Cherry-picked multiverse | A multiverse that only reports the favorable corner | Require the full distribution of specifications and the share crossing threshold |
| HARKing relabel | Post-hoc hypothesis presented as the original | Compare reported hypothesis to measured set + timestamps |
| Hidden outcomes | Only the significant outcome reported | Require disclosure of all measured outcomes/predictors |
| Audit-as-absolution | Treating a passed self-check as proof of validity | Output exposure rating, not a clean-bill certification |
