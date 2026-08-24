---
title: "Preregistration Drafter"
category: science/methods-foundations
description: "Draft an OSF-style preregistration with hypotheses, design, sampling plan, variables, a confirmatory analysis plan, inference criteria, and an explicit deviations clause."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - preregistration
  - osf
  - confirmatory-analysis
  - exploratory-analysis
  - sampling-plan
  - inference-criteria
  - deviations-clause
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/methods-foundations/science_research_question_refiner.md
  - domain-science/methods-foundations/science_registered_report_stage1_drafter.md
---

# Preregistration Drafter

**Objective:** Produce a time-stampable, OSF-style preregistration that locks the study's hypotheses, design, sampling plan, variables, confirmatory analysis plan, and inference criteria before data are observed. The draft hard-distinguishes confirmatory from exploratory analyses throughout and includes an explicit deviations clause for transparently logging any departure from the plan.

**When to use:** After the research question and design are settled but strictly before data collection (or before looking at outcome data, if data already exist for a confirmatory secondary analysis). Use to convert a finalized plan into a registry-ready document.

**Required inputs:**
- **Discipline.** The field (e.g., ecology / clinical trial / condensed matter / computational social science). `[user-supplied]`
- **Study type.** Observational / experimental / computational / secondary-data. `[user-supplied]`
- **Hypotheses.** Directional or non-directional statements the study will test. `[user-supplied]`
- **Design summary.** Conditions/groups, manipulations or exposures, and unit of analysis. `[user-supplied]`
- **Primary outcome(s) and how measured.** Operationalization of each dependent/response variable. `[user-supplied]`

**Optional inputs:**
- **Planned sample size / stopping rule and its basis** (power analysis inputs, resource ceiling, or sequential plan). `[user-supplied]`
- **Covariates / nuisance variables.** `[user-supplied]`
- **Planned exclusions and missing-data approach.** `[user-supplied]`
- **Known exploratory questions** the team also wants to ask (kept separate). `[user-supplied]`
- **Data/code sharing intent.** `[user-supplied]`

**Constraints — Must:**
- Confirm discipline and study type before drafting; if hypotheses or primary outcomes are missing, ask before proceeding.
- Mirror the OSF "Prereg" template field structure: study information, hypotheses, design plan, sampling plan, variables, analysis plan, inference criteria, and other (exclusions, missing data, exploratory).
- Label every analysis as **Confirmatory** or **Exploratory** and never let an exploratory analysis carry confirmatory inferential weight.
- State explicit inference criteria (e.g., the decision threshold, correction for multiplicity, or model-comparison rule) tied to each confirmatory hypothesis.
- Include a sampling plan with the target N (or stopping rule) and its justification; if a power analysis is claimed, require its inputs as `[user-supplied]`.
- Include a written deviations clause specifying how any departure from the plan will be documented and dated in the OSF record.
- Default to data and code sharing under FAIR principles; if the user chooses closed data, name that explicitly as the non-default branch with the justification it requires.

**Constraints — Must Not:**
- Do not invent citations, DOIs, journal names, dataset names, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not compute or assert a power-analysis result or required N without user-supplied inputs (effect size, alpha, power, design).
- Do not relabel an exploratory analysis as confirmatory, or imply HARKing is acceptable.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" anywhere in the drafted document.

**Instructions:**

1. **Confirm framing.** Restate discipline, study type, hypotheses, design, and primary outcomes. Surface any missing required input as a single consolidated question.
2. **Write study information.** State the title, research question, and the specific testable hypotheses, each phrased so a refuting result is identifiable.
3. **Specify the design plan.** Describe study type, blinding/randomization (if any), conditions, and the unit of analysis. Note manipulated vs. measured variables.
4. **Specify the sampling plan.** State data collection status (no data collected / collected-not-examined), target N or stopping rule, and the basis for it. Mark power-analysis inputs `[user-supplied]` if absent.
5. **Define variables.** List independent/predictor, dependent/outcome, and covariate variables with precise operationalizations and units.
6. **Write the confirmatory analysis plan.** For each confirmatory hypothesis, name the statistical model/test, the predictors, the multiplicity correction, and the exact inference criterion. Keep one analysis per hypothesis where possible.
7. **Specify exclusions and missing data.** State pre-planned exclusion rules and the missing-data handling (e.g., listwise, imputation approach) before any data are seen.
8. **Separate exploratory analyses.** Place any non-preregistered or hypothesis-generating analyses in a clearly fenced Exploratory section with no confirmatory claims attached.
9. **Add the deviations clause and sharing plan.** Write how departures will be logged/dated in OSF, and state the data/code sharing branch (FAIR default, or named closed-data exception).

**Output format (locked):**

```
## Study Information
- Title: ...
- Research question: ...
- Hypotheses (each refutable):
  - H1 (confirmatory): ...
  - H2 (confirmatory): ...

## Design Plan
- Study type: ...
- Randomization / blinding: ... (or N/A)
- Conditions / groups: ...
- Unit of analysis: ...
- Manipulated vs measured variables: ...

## Sampling Plan
- Data collection status: no data collected / collected, not examined
- Target N or stopping rule: ...
- Basis / power inputs: [user-supplied: effect size, alpha, power, design]

## Variables
| Role | Variable | Operationalization | Units |
|---|---|---|---|
| Predictor | ... | ... | ... |
| Outcome | ... | ... | ... |
| Covariate | ... | ... | ... |

## Analysis Plan — Confirmatory
| Hypothesis | Model / test | Predictors | Multiplicity correction | Inference criterion |
|---|---|---|---|---|
| H1 | ... | ... | ... | ... |
| H2 | ... | ... | ... | ... |

## Inference Criteria (summary)
[decision thresholds and what counts as support vs. non-support per hypothesis]

## Planned Exclusions
- ...

## Missing-Data Handling
- ...

## Exploratory Analyses (NOT confirmatory)
- ...

## Deviations Clause
[how any departure from this plan will be documented and dated in the OSF registration; confirmatory status is not retroactively assigned]

## Data, Code & Materials Sharing
- Default (FAIR): ...
- If closed data: [named non-default branch + justification required]

## Open Questions / [user-supplied] gaps
- ...
```

**Reporting-standard alignment:** Field structure mirrors the OSF preregistration ("Prereg") template — study information, design plan, sampling plan, variables, analysis plan, and inference criteria. The confirmatory/exploratory partition and the deviations clause follow Center for Open Science preregistration practice and OSF deviations logging. Data/code sharing defaults follow the FAIR principles. Where the study is a clinical or biomedical trial, the user should additionally route the eventual report through the relevant EQUATOR guideline (e.g., CONSORT/STROBE) — named here only as a downstream pointer, not drafted.

**Verification checklist (before delivering):**
- [ ] Discipline and study type confirmed; hypotheses and primary outcomes present before drafting.
- [ ] Every hypothesis is stated so a refuting result is identifiable.
- [ ] Sampling plan states data-collection status and target N / stopping rule with its basis (or `[user-supplied]`).
- [ ] Each confirmatory hypothesis maps to exactly one analysis with an explicit inference criterion and multiplicity handling.
- [ ] Exclusions and missing-data handling are pre-specified.
- [ ] Exploratory analyses are fenced and carry no confirmatory claims.
- [ ] A deviations clause specifying OSF-dated logging is present.
- [ ] No fabricated citations/datasets/effect sizes/specs; no power result asserted without inputs; no banned hype words.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| HARKing leak | An exploratory finding is written as if it were a preregistered hypothesis | Confirmatory/exploratory label required on every analysis; exploratory section is fenced and inference-free |
| Phantom power analysis | A target N is stated as if powered, with no inputs | Require effect size/alpha/power/design as `[user-supplied]`; never assert a computed N |
| Vague inference criterion | "We will test whether X" with no threshold or correction | Inference-criteria column must be non-empty per confirmatory hypothesis, including multiplicity handling |
| Researcher degrees of freedom | Outcome or exclusions left flexible "to decide later" | Pre-specify exclusions and missing-data rules before any data are examined; flag any deferral |
| Toothless deviations clause | Says deviations "may be noted" with no mechanism | Require dated OSF logging and a statement that confirmatory status is not retroactively assigned |
