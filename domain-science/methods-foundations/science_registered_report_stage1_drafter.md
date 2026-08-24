---
title: "Registered Report Stage-1 Drafter"
category: science/methods-foundations
description: "Draft a Stage-1 Registered Report (introduction with hypotheses, methods, proposed analysis, study-design table, outcome-neutral quality checks, and pilot data) reviewed before data collection."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-02
  - CM-02
  - NE-10
difficulty: advanced
tags:
  - registered-report
  - stage-1
  - study-design-table
  - outcome-neutral
  - positive-controls
  - in-principle-acceptance
  - pilot-data
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/methods-foundations/science_research_question_refiner.md
  - domain-science/methods-foundations/science_preregistration_drafter.md
---

# Registered Report Stage-1 Drafter

**Objective:** Produce a Stage-1 Registered Report skeleton — Introduction with hypotheses, Methods, proposed Analysis, a study-design table mapping each hypothesis to its sampling plan, analysis, and interpretation given each possible outcome, plus outcome-neutral quality checks and a pilot-data section. The draft is structured for peer review **before** data collection, targeting In-Principle Acceptance (IPA).

**When to use:** When the team intends to submit a Registered Report to a participating journal and needs the Stage-1 manuscript that reviewers evaluate prior to data collection. Precondition: the research question, design, and confirmatory analysis plan are settled (the preregistration drafter and research-question refiner feed this step).

**Required inputs:**
- **Discipline.** The field (e.g., cognitive neuroscience / ecology / materials science / health psychology). `[user-supplied]`
- **Study type.** Experimental / observational / computational / secondary-data. `[user-supplied]`
- **Hypotheses with directional predictions.** Each phrased as a specific testable prediction. `[user-supplied]`
- **Methods summary.** Design, manipulations/exposures, materials/apparatus, procedure, and unit of analysis. `[user-supplied]`
- **Proposed confirmatory analyses and inference criteria.** Per hypothesis. `[user-supplied]`
- **Sampling plan basis.** Power-analysis inputs, stopping rule, or resource ceiling. `[user-supplied]`

**Optional inputs:**
- **Pilot data.** Any preliminary data supporting feasibility or the manipulation. `[user-supplied]`
- **Positive controls / manipulation checks** the team plans. `[user-supplied]`
- **Target journal Stage-1 criteria** if known. `[user-supplied]`
- **Data/code/materials sharing intent.** `[user-supplied]`

**Constraints — Must:**
- Confirm discipline and study type before drafting; if hypotheses, methods, or analysis plan are missing, ask before proceeding.
- Follow IMRaD structure adapted for Stage-1 (Introduction → Methods → Proposed Analysis), noting that Results/Discussion are deliberately absent at Stage-1.
- Include a study-design table with one row per hypothesis mapping: hypothesis → sampling plan → analysis → rationale for inference → interpretation given different outcomes (support / non-support / inconclusive).
- Include outcome-neutral quality checks: positive controls, manipulation checks, and data-quality criteria that establish the study could detect the effect regardless of which way results fall.
- Use probability-weighted outcome scenarios in the design table so each plausible result has a pre-committed interpretation.
- Justify the sampling plan; require power-analysis inputs as `[user-supplied]` if a powered N is claimed.
- Default to data, code, and materials sharing under FAIR principles; name closed data explicitly as the non-default branch if chosen.

**Constraints — Must Not:**
- Do not invent citations, DOIs, journal names, dataset names, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not draft a Results or Discussion section or report any outcome — Stage-1 precedes data collection.
- Do not assert a powered sample size without user-supplied inputs.
- Do not use "novel," "groundbreaking," "first-ever," or "gold standard" anywhere in the drafted manuscript.

**Instructions:**

1. **Confirm framing.** Restate discipline, study type, hypotheses, methods, and proposed analyses. Consolidate any missing required input into one clarifying question.
2. **Draft the Introduction.** Motivate the question, state what is at stake, and present each hypothesis as a specific testable prediction with the refuting observation identifiable. Frame importance in calibrated terms.
3. **Draft the Methods.** Specify design, sample/specimens, materials/apparatus, procedure, and unit of analysis at the detail a replicator would need. Mark unknown specs `[user-supplied]`.
4. **Write the sampling plan.** State target N or stopping rule and its basis; surface power-analysis inputs as `[user-supplied]` if absent.
5. **Draft the proposed Analysis.** For each confirmatory hypothesis, name the model/test, predictors, multiplicity correction, and inference criterion. Keep confirmatory and any exploratory analyses separated.
6. **Build the study-design table.** One row per hypothesis: hypothesis → sampling plan → analysis → inference rationale → interpretation given support / non-support / inconclusive outcomes (probability-weighted scenarios).
7. **Specify outcome-neutral quality checks.** Define positive controls, manipulation checks, and data-quality/exclusion criteria that demonstrate the design can detect the effect if present, independent of the direction of results.
8. **Add the pilot-data section.** Summarize any user-supplied pilot data and what it establishes (feasibility, manipulation efficacy); if none, state "no pilot data" rather than implying any.
9. **Adversarial pass and sharing plan.** Stress-test against common Stage-1 reviewer objections (underpowered, ambiguous interpretation, missing positive control, post-hoc flexibility) and state the FAIR sharing branch or named closed-data exception.

**Output format (locked):**

```
## Stage-1 Status
- Reviewed BEFORE data collection (target: In-Principle Acceptance)
- Results / Discussion intentionally absent at Stage-1

## Introduction
[motivation, stakes, prior context (user-supplied only)]
- Hypotheses (specific testable predictions):
  - H1: ... | refuting observation: ...
  - H2: ... | refuting observation: ...

## Methods
- Design: ...
- Sample / specimens: ...
- Materials / apparatus: ... [user-supplied where unknown]
- Procedure: ...
- Unit of analysis: ...

## Sampling Plan
- Target N or stopping rule: ...
- Basis / power inputs: [user-supplied: effect size, alpha, power, design]

## Proposed Analysis (Confirmatory)
| Hypothesis | Model / test | Predictors | Multiplicity correction | Inference criterion |
|---|---|---|---|---|
| H1 | ... | ... | ... | ... |

## Study-Design Table
| Hypothesis | Sampling plan | Analysis | Inference rationale | Interpretation if SUPPORT | Interpretation if NON-SUPPORT | Interpretation if INCONCLUSIVE |
|---|---|---|---|---|---|---|
| H1 | ... | ... | ... | ... | ... | ... |

## Outcome-Neutral Quality Checks
- Positive controls: ...
- Manipulation checks: ...
- Data-quality / exclusion criteria: ...

## Pilot Data
- [user-supplied summary] OR "No pilot data."

## Exploratory Analyses (NOT confirmatory)
- ...

## Reviewer Stress-Test (anticipated objections)
| Objection | Response in design |
|---|---|
| Underpowered | ... |
| Ambiguous interpretation | ... |
| Missing positive control | ... |
| Post-hoc flexibility | ... |

## Data, Code & Materials Sharing
- Default (FAIR): ...
- If closed data: [named non-default branch + justification required]

## Open Questions / [user-supplied] gaps
- ...
```

**Reporting-standard alignment:** Structure follows the Registered Reports Stage-1 workflow (Center for Open Science) — peer review before data collection, a study-design table mapping hypotheses to analyses and pre-committed interpretations, outcome-neutral quality checks (positive controls/manipulation checks), and a powered sampling plan, all targeting In-Principle Acceptance. The manuscript follows IMRaD adapted for Stage-1 (no Results/Discussion). Sharing defaults follow FAIR principles. For biomedical/clinical work, the eventual Stage-2 report should additionally conform to the relevant EQUATOR guideline (e.g., CONSORT/STROBE) — named here only as a downstream pointer, not drafted.

**Verification checklist (before delivering):**
- [ ] Discipline and study type confirmed; hypotheses, methods, and analysis plan present before drafting.
- [ ] No Results or Discussion section was drafted (Stage-1 precedes data).
- [ ] Each hypothesis is a specific testable prediction with an identified refuting observation.
- [ ] Study-design table has one row per hypothesis and a pre-committed interpretation for support / non-support / inconclusive.
- [ ] Outcome-neutral quality checks include at least a positive control or manipulation check.
- [ ] Sampling plan states N / stopping rule with its basis (or `[user-supplied]`); no powered N asserted without inputs.
- [ ] Confirmatory and exploratory analyses are kept separate.
- [ ] No fabricated citations/datasets/effect sizes/specs; no banned hype words; pilot data marked `[user-supplied]` or stated absent.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Premature results | A "preliminary findings" paragraph creeps into Stage-1 | Stage-1 status banner forbids Results/Discussion; pilot data is feasibility-only, not outcome evidence |
| Non-diagnostic design | Any result would be spun as confirming the hypothesis | Study-design table requires a distinct interpretation for non-support and inconclusive outcomes |
| Missing detectability check | Design cannot show the effect is absent vs. undetectable | Require a positive control / manipulation check in outcome-neutral checks |
| Unpowered submission | Sampling plan asserts adequacy with no basis | Require power inputs as `[user-supplied]`; never assert a powered N |
| Hidden flexibility | Analysis "to be finalized after seeing data" | Lock model, predictors, correction, and inference criterion per hypothesis at Stage-1 |
| Fabricated pilot/specs | Invented apparatus specs or pilot numbers fill gaps | Mark unknown specs `[user-supplied]`; state "No pilot data" when none supplied |
