---
title: "Meta-Analysis Protocol"
category: science/statistics
description: "Draft a PRISMA-aligned systematic-review-and-meta-analysis protocol: question, search, dual screening, extraction, risk-of-bias, synthesis model, heterogeneity, publication bias, sensitivity, and GRADE."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - meta-analysis
  - prisma
  - systematic-review
  - risk-of-bias
  - heterogeneity
  - publication-bias
  - grade
  - prospero
updated: "2026-06-26"
related_prompts:
  - domain-science/statistics/science_statistical_test_selector.md
  - domain-science/methods-foundations/science_methodology_decision_tree.md
  - domain-science/methods-foundations/science_confound_and_bias_audit.md
---

# Meta-Analysis Protocol

**Objective:** Help a researcher draft a registrable systematic-review-and-meta-analysis protocol aligned with PRISMA 2020 and PRISMA-P. Specify the question, eligibility, search, dual screening, extraction, risk-of-bias appraisal, effect-size and synthesis-model choice, heterogeneity exploration, small-study/publication-bias assessment, sensitivity analyses, and GRADE certainty rating — all pre-specified before data are touched.

**When to use:** You intend to systematically identify, appraise, and quantitatively synthesize studies on a defined question and need a protocol that withstands peer and reproducibility review.

**Required inputs:**
- **Discipline.** [user-supplied] (e.g., clinical medicine, ecology, education, psychology).
- **Study type.** [user-supplied] of the included evidence (RCTs, observational studies, or mixed).
- **Question in PICO(S) form.** Population, Intervention/Exposure, Comparator, Outcome(s), Study designs.
- **Primary vs secondary outcomes.** Pre-specified, with the effect measure for each.
- **Databases / search sources.** Intended databases and any registries/grey-literature sources (`[user-supplied]` if not yet chosen).

**Optional inputs:**
- Date and language limits and their justification.
- Anticipated sources of heterogeneity (pre-specified subgroups/moderators).
- Software (metafor, RevMan, meta, robumeta).
- Whether the review will be registered on PROSPERO or an equivalent registry.

**Constraints — Must:**
- Structure the protocol per PRISMA 2020 + PRISMA-P; recommend prospective registration (PROSPERO or equivalent) before screening.
- Pre-specify primary vs secondary outcomes, effect measures, and the synthesis model; keep the line between pre-specified and exploratory analyses explicit throughout.
- Require dual independent screening and extraction with a conflict-resolution rule and an inter-rater agreement metric (e.g., Cohen's kappa).
- Specify a validated risk-of-bias tool by evidence type: RoB 2 for randomized trials, ROBINS-I for non-randomized studies; use MOOSE alongside PRISMA for observational meta-analyses.
- Justify fixed-effect vs random-effects synthesis; under random effects, plan to report tau² and I² and to quantify the prediction interval, not just the pooled estimate.
- Restrict heterogeneity exploration (subgroup analysis, meta-regression) to pre-specified moderators with adequate study counts; assess small-study effects/publication bias (funnel plot, Egger's test, trim-and-fill) only when ≥10 studies and with stated caveats.
- Rate certainty of evidence with GRADE per outcome.
- Default to the Open Science branch: share the protocol, search strings, screening decisions, extraction sheet, and analysis code.

**Constraints — Must Not:**
- Do not invent citations, DOIs, datasets, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not vote-count (tallying significant vs non-significant studies) in place of effect-size synthesis.
- Do not fabricate or impute included-study data, sample sizes, or outcomes; missing data are queried, not guessed.
- Do not over-interpret funnel-plot asymmetry as proof of publication bias.
- Do not use the words "novel", "groundbreaking", "first-ever", or "gold standard" in drafted prose.

**Instructions:**

1. **Lock the question.** State the PICO(S), primary/secondary outcomes, and effect measure for each. Confirm the review is prospective and recommend registration.
2. **Define eligibility.** Specify inclusion/exclusion by population, design, comparator, outcome, dates, and language, each with a rationale.
3. **Design the search.** Draft the source list and structured search strategy (terms/Boolean per database, `[user-supplied]` where databases or controlled vocabulary are not yet provided); include grey literature and reference chaining.
4. **Specify screening.** Require two independent reviewers at title/abstract and full-text stages, a conflict-resolution rule, a kappa agreement metric, and a PRISMA flow diagram for the count.
5. **Specify extraction.** Define the extraction sheet fields (study characteristics, effect estimates with variance, risk-of-bias items) and dual extraction with verification.
6. **Plan risk-of-bias appraisal.** Assign RoB 2 (RCTs) or ROBINS-I (non-randomized); state how bias informs synthesis and sensitivity.
7. **Specify synthesis.** Choose and justify fixed vs random effects, the effect measure and variance method, and how to handle dependent effect sizes (e.g., robust variance estimation); plan tau², I², and prediction intervals.
8. **Plan heterogeneity and bias assessment.** List pre-specified subgroups/meta-regression moderators; specify small-study/publication-bias methods with their ≥10-study threshold and caveats; specify sensitivity analyses (leave-one-out, risk-of-bias restriction, alternative models).
9. **Rate certainty and self-check.** Apply GRADE per outcome; confirm no vote-counting, no fabricated data, and that every analysis is labeled pre-specified or exploratory.

**Output format (locked):**

```
## Question & Registration
- PICO(S):
- Primary / secondary outcomes + effect measures:
- Registry (PROSPERO/equivalent): [user-supplied if undecided]

## Eligibility Criteria
- Include / exclude (with rationale):

## Search Strategy
- Sources/databases:
- Structured search (per source) [user-supplied where needed]:
- Grey literature / reference chaining:

## Screening & Extraction
- Dual-reviewer process + conflict rule + kappa:
- Extraction fields:
- PRISMA flow plan:

## Risk of Bias
- Tool (RoB 2 / ROBINS-I) + use in synthesis:

## Synthesis Model
- Fixed vs random effects (justification):
- Effect measure / variance method / dependence handling:
- tau², I², prediction interval:

## Heterogeneity, Bias & Sensitivity
- Pre-specified subgroups / meta-regression:
- Small-study/publication-bias methods (≥10 studies) + caveats:
- Sensitivity analyses:

## Certainty of Evidence
- GRADE per outcome:

## Open Science
- Protocol / search / data / code sharing:

## Open Questions / [user-supplied] gaps
```

**Reporting-standard alignment:** Align with PRISMA 2020 and PRISMA-P (protocol), the Cochrane Handbook (methods), MOOSE (observational meta-analyses), and GRADE (certainty rating).

**Verification checklist (before delivering):**
- [ ] Discipline and evidence/study type captured (or marked `[user-supplied]`).
- [ ] PICO(S), outcomes, and effect measures pre-specified; registration recommended.
- [ ] Search strategy structured per source (or `[user-supplied]`); grey literature included.
- [ ] Dual screening/extraction with conflict rule and kappa specified.
- [ ] Risk-of-bias tool matched to evidence type (RoB 2 / ROBINS-I).
- [ ] Fixed vs random effects justified; tau²/I²/prediction interval planned.
- [ ] Heterogeneity moderators pre-specified; publication-bias methods gated at ≥10 studies; sensitivity analyses listed; GRADE applied.
- [ ] No vote-counting; no fabricated study data; banned hype words absent; Open Science branch present.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Vote-counting | "Most studies were significant, so the effect is real" | Synthesize effect sizes with variance; ban significance tallies |
| Spurious moderators | A subgroup "explains" heterogeneity post hoc | Restrict to pre-specified moderators with adequate k; label exploratory |
| Funnel-plot over-reading | Asymmetry "proves" publication bias | Require ≥10 studies; treat asymmetry as one possible cause among several |
| Pooled estimate without spread | Tight CI on the mean looks conclusive | Report tau²/I² and a prediction interval to show true-effect dispersion |
| Imputed/guessed data | Extraction sheet looks complete | Query missing values; never fabricate sample sizes or effect estimates |
