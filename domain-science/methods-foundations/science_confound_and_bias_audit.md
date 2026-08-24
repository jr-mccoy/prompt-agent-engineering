---
title: "Confound and Bias Audit"
category: science/methods-foundations
description: "Apply a working bias taxonomy (selection, information, confounding, time-related, attrition, reporting) to a specific study and produce a ranked bias register with design- and analysis-stage mitigations."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-02
  - DS-02
  - NE-10
difficulty: advanced
tags:
  - confounding
  - selection-bias
  - information-bias
  - dag
  - immortal-time-bias
  - robins-i
  - strobe
  - bias-register
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/methods-foundations/science_threats_to_validity_walkthrough.md
  - domain-science/methods-foundations/science_blinding_and_randomization_protocol.md
  - domain-science/methods-foundations/science_negative_and_positive_control_designer.md
---

# Confound and Bias Audit

**Objective:** Systematically screen a specific study against a working bias taxonomy, make confounding explicit with a causal diagram, and deliver a ranked bias register. Each entry names the bias, its mechanism in THIS study, its likely direction and magnitude, how it is detected, and how it is mitigated at the design vs analysis stage. This is a broad audit; for a structured Cook & Campbell four-validity walkthrough, see the related prompt.

**When to use:** A design, dataset, or draft analysis exists and you need a defensible inventory of the bias threats most likely to distort the result, prioritized for action — especially for observational work or non-randomized comparisons.

**Required inputs:**
- **Discipline.** <field — e.g., epidemiology, clinical research, ecology, social science, ML evaluation>
- **Study type.** <observational (cohort / case-control / cross-sectional) / experimental / quasi-experimental / computational>
- **Exposure/intervention and outcome.** What is compared and what is measured.
- **Population and sampling.** How units entered the study; comparison group origin.
- **Measurement scheme.** How exposure and outcome are ascertained and timed.

**Optional inputs:**
- Suspected confounders or known prior causes.
- Follow-up structure, loss-to-follow-up, missing-data pattern.
- Whether the analysis is pre-specified or exploratory.
- Effect estimate(s) to date — supply or mark `[user-supplied]`.

**Constraints — Must:**
- Ask for discipline and study type before auditing.
- Cover the taxonomy explicitly: selection bias (including collider/Berkson), information/measurement bias (recall, detection, misclassification — differential vs non-differential), confounding (including confounding-by-indication), time-related bias (including immortal-time), attrition bias, and reporting/publication bias.
- Build a causal diagram (DAG) step that names common causes, mediators, and colliders before judging confounding.
- For each prioritized bias, state likely direction (toward/away from null) and qualitative magnitude.
- Separate design-stage from analysis-stage mitigations, and pre-specified from exploratory adjustment.
- Name STROBE (reporting), RoB 2 (randomized), and ROBINS-I (non-randomized) as the alignment frame.

**Constraints — Must Not:**
- Do not invent citations, DOIs, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not "adjust away" a collider or mediator — flag that conditioning on it can induce bias.
- Do not present post-hoc covariate selection as if pre-specified.
- Do not use "novel", "groundbreaking", "first-ever", or "gold standard".
- Do not rank a bias as low without stating why its mechanism is implausible here.

**Instructions:**

1. **Frame the contrast.** State the exposure–outcome contrast and the target estimand the study intends to support.
2. **Draw the DAG.** List nodes (exposure, outcome, candidate common causes, mediators, colliders, selection node) and the assumed arrows; identify which variables are confounders vs colliders vs mediators.
3. **Screen selection bias.** Assess how units entered and how the comparison group formed; test for collider/Berkson structures and selection into follow-up.
4. **Screen information/measurement bias.** Assess recall, detection, and misclassification; classify each as differential or non-differential and infer the resulting direction.
5. **Screen confounding.** From the DAG, list open backdoor paths, including confounding-by-indication; note unmeasured confounders.
6. **Screen time-related and attrition bias.** Check immortal-time windows, lookback/lag definitions, and differential loss-to-follow-up or missingness.
7. **Screen reporting/publication bias.** Check selective outcome/analysis reporting and registration status.
8. **Build the ranked register.** For each bias, score likelihood and impact, infer direction/magnitude, and rank; weight the ranking by probability of materially changing the conclusion (NE-10).
9. **Assign mitigations.** For top-ranked biases, specify design-stage fixes (restriction, matching, blinding, sampling frame) and analysis-stage fixes (stratification, adjustment with justified variables, sensitivity/E-value, negative-control outcomes), flagging which are pre-specified.

**Output format (locked):**

```
## Contrast and target estimand
[one sentence]

## Causal diagram (DAG) summary
- Confounders: ...
- Mediators (do NOT adjust): ...
- Colliders / selection nodes (conditioning induces bias): ...
- Unmeasured prior causes: ...

## Bias register (ranked)
| Rank | Bias (taxonomy class) | Mechanism in THIS study | Likely direction | Magnitude (qual.) | Detection | Mitigation (design) | Mitigation (analysis) | Pre-specified? |
|---|---|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... | ... | ... | ... |

## Highest-priority actions
[top 3, with design-vs-analysis tag]

## Residual / unmeasured threats
[what no mitigation removes]

## Reporting-standard alignment
- Frame: [STROBE / RoB 2 / ROBINS-I]
- Domains addressed: ...
- Gaps / [user-supplied]: ...
```

**Reporting-standard alignment:** STROBE (observational reporting), RoB 2 (risk of bias in randomized trials), ROBINS-I (risk of bias in non-randomized studies of interventions). Name only the frame(s) relevant to the supplied study type.

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured before auditing.
- [ ] All taxonomy classes screened (selection, information, confounding, time-related, attrition, reporting).
- [ ] A DAG step distinguishes confounders from mediators and colliders.
- [ ] No mediator/collider is recommended for adjustment without a caution.
- [ ] Each prioritized bias has a stated direction and qualitative magnitude.
- [ ] Mitigations split into design-stage vs analysis-stage; pre-specified vs exploratory flagged.
- [ ] Unmeasured/residual confounding explicitly acknowledged.
- [ ] STROBE/RoB 2/ROBINS-I mapped; gaps flagged.
- [ ] No fabricated effect sizes/citations; unknowns `[user-supplied]`; banned hype absent.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Over-adjustment | Adjusting for a mediator or collider and calling the estimate "more rigorous" | DAG step labels mediators/colliders; block adjustment with explicit caution |
| Confounding-by-indication missed | Treatment–outcome association read as causal when sicker patients got treated | Require an explicit indication-confounding check for any treatment contrast |
| Immortal-time blindspot | Survival advantage that is an artifact of exposure-window definition | Dedicated time-related bias screen for lookback/lag/exposure windows |
| Non-differential complacency | Assuming misclassification only biases toward null, ignoring differential cases | Force differential-vs-non-differential classification before inferring direction |
| Selection-as-random | Convenience/responder sample treated as representative | Trace how units entered and test for collider/selection structure |
