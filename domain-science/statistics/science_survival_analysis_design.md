---
title: "Survival Analysis Design"
category: science/statistics
description: "Define event and time origin, handle censoring correctly, assess proportional hazards, and choose between Kaplan-Meier, Cox, parametric/AFT, and competing-risks models."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - survival-analysis
  - censoring
  - cox-regression
  - proportional-hazards
  - competing-risks
  - kaplan-meier
  - fine-gray
  - time-to-event
updated: "2026-06-26"
related_prompts:
  - domain-science/statistics/science_statistical_test_selector.md
  - domain-science/methods-foundations/science_methodology_decision_tree.md
  - domain-science/methods-foundations/science_confound_and_bias_audit.md
---

# Survival Analysis Design

**Objective:** Help a researcher design a defensible time-to-event analysis. Pin down the event definition and time origin, characterize the censoring type and mechanism, select an appropriate estimator/model, plan a proportional-hazards assessment, and decide whether competing risks must be modeled and how.

**When to use:** The outcome is time until an event (death, relapse, failure, discharge, conversion) and some subjects do not experience the event during follow-up, or experience a different event first.

**Required inputs:**
- **Discipline.** [user-supplied] (e.g., oncology, reliability engineering, epidemiology, demography).
- **Study type.** [user-supplied] (observational cohort / RCT / registry / experimental).
- **Event definition.** The precise event of interest and how it is ascertained.
- **Time origin and time scale.** Randomization, diagnosis, enrollment, or birth; calendar vs age vs on-study time.
- **Censoring/truncation.** Expected mechanism (administrative end of follow-up, loss to follow-up, dropout) and whether competing events occur.

**Optional inputs:**
- Covariates of interest and whether any are time-varying.
- Sample size, event count, and follow-up length.
- Pre-registered vs exploratory status.
- Whether the goal is etiologic (mechanism) or predictive (absolute risk).

**Constraints — Must:**
- State the event, time origin, and time scale explicitly before any model is chosen.
- Classify censoring as right / left / interval and the mechanism as informative vs non-informative; flag informative censoring as a threat that biases estimates and cannot be assumed away.
- Match the estimator to the question: Kaplan-Meier + log-rank for description/group comparison; Cox proportional-hazards for covariate effects; parametric/AFT models when an absolute time scale or extrapolation is justified.
- Plan a proportional-hazards assessment for any Cox model: Schoenfeld residuals (global and per-covariate), log-log survival plots, and a remedy path (stratification, time-varying coefficients, or AFT) if violated.
- Address competing risks when present: choose cause-specific hazards for etiology vs Fine-Gray subdistribution hazards for absolute-risk prediction, and never use 1 − Kaplan-Meier as a cumulative-incidence estimate under competing risks.
- Default to the Open Science branch: share the analysis script, event/censoring definitions, and (where permitted) the time-to-event dataset.

**Constraints — Must Not:**
- Do not invent citations, DOIs, datasets, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not treat censoring as non-informative without an explicit justification.
- Do not ignore competing risks or report cause-specific and subdistribution hazard ratios interchangeably.
- Do not report a hazard ratio as if it were constant when proportional hazards is untested or violated.
- Do not use the words "novel", "groundbreaking", "first-ever", or "gold standard" in drafted prose.

**Instructions:**

1. **Define the event and time axis.** State the event, time origin, and time scale, and confirm everyone starts at risk at time zero (check for immortal-time bias). Mark whether confirmatory or exploratory.
2. **Characterize censoring and truncation.** Determine right/left/interval censoring and left truncation (delayed entry). Diagnose whether censoring is plausibly non-informative; if dropout relates to prognosis, flag the bias and consider sensitivity analyses.
3. **Detect competing risks.** Identify any event that prevents the event of interest. If present, route to a competing-risks framework rather than standard survival.
4. **Select the estimator/model.** Choose Kaplan-Meier/log-rank, Cox PH, parametric/AFT, or a competing-risks model (cause-specific Cox vs Fine-Gray) by question and data, justifying each choice.
5. **Plan the proportional-hazards assessment (if Cox).** Specify Schoenfeld residual tests, log-log plots, and what you will do if PH fails (stratify, add time × covariate interaction, or switch to AFT).
6. **Decide the competing-risks estimand.** For etiology, model cause-specific hazards; for risk prediction/communication, model subdistribution hazards (Fine-Gray) and report cumulative incidence functions.
7. **Plan covariate handling.** Address time-varying covariates (use the counting-process/start-stop format), nonlinear effects (splines), and the events-per-variable rule of thumb for model stability.
8. **Self-check.** Confirm follow-up adequacy, event count vs covariates, ties handling (Efron), and that the reported quantity (HR, RMST, median survival, CIF) matches the stated question.

**Output format (locked):**

```
## Event & Time Definition
- Event:
- Time origin / time scale:
- Confirmatory or exploratory:
- Immortal-time / left-truncation check:

## Censoring & Competing Risks
- Censoring type (right/left/interval) + truncation:
- Informative vs non-informative (justification):
- Competing events present? Implication:

## Model Selection
| Goal | Estimator/Model | Justification |
|---|---|---|

## Proportional-Hazards Assessment (if Cox)
- Tests/plots:
- Remedy if violated:

## Competing-Risks Estimand (if applicable)
- Cause-specific vs Fine-Gray + why:
- Reported quantity (HR / CIF / RMST):

## Covariate & Stability Plan
- Time-varying / nonlinear handling:
- Events-per-variable check:

## Open Science
- Script / definitions / dataset sharing plan:

## Open Questions / [user-supplied] gaps
```

**Reporting-standard alignment:** Align with STROBE for observational cohorts and CONSORT for randomized trials; report estimand, censoring handling, PH assessment, and competing-risks method per these standards.

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured (or marked `[user-supplied]`).
- [ ] Event, time origin, and time scale defined; immortal-time/left-truncation checked.
- [ ] Censoring type and mechanism classified; informative censoring flagged if plausible.
- [ ] Competing risks identified and routed appropriately (no 1 − KM misuse).
- [ ] Estimator/model justified against the question.
- [ ] PH assessment specified with a remedy path for violations.
- [ ] Cause-specific vs Fine-Gray choice tied to etiology vs prediction.
- [ ] No fabricated citations/data/specs; banned hype words absent; Open Science branch present.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Competing-risks overstatement | 1 − KM gives a clean "incidence" curve | Use cumulative incidence functions; never 1 − KM under competing risks |
| Untested PH | Single HR reported as the effect | Require Schoenfeld/log-log assessment before reporting a constant HR |
| Informative censoring | KM curve looks smooth and unbiased | Justify non-informativeness; run dependent-censoring sensitivity analyses |
| Immortal time | Treated group "survives longer" | Verify at-risk status at time zero; align time origin with exposure |
| Estimand mismatch | Cause-specific HR used for patient risk counseling | Use Fine-Gray/CIF for absolute risk; reserve cause-specific for etiology |
