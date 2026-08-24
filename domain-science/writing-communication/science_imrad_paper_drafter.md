---
title: "IMRaD Paper Drafter (Skeleton-First)"
category: science/writing-communication
description: "Builds a skeleton-first IMRaD manuscript draft from user-supplied results and key claims, then runs a structural critique that traces every claim to a result."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - QA-02
  - CM-02
difficulty: advanced
tags:
  - imrad
  - manuscript-drafting
  - scientific-writing
  - equator-guidelines
  - results-to-claim-mapping
  - discussion-structure
  - reproducibility
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/writing-communication/science_abstract_compressor.md
  - domain-science/writing-communication/science_figure_first_paper_skeleton.md
  - domain-science/methods-foundations/science_methods_section_drafter.md
---

# IMRaD Paper Drafter (Skeleton-First)

**Objective:** Produce a complete IMRaD (Introduction, Methods, Results, and Discussion) manuscript draft by first locking a section/subsection scaffold with a one-sentence claim per subsection, then filling prose only from user-supplied results. The draft satisfies the IMRaD convention and the EQUATOR reporting guideline appropriate to the study type (e.g., CONSORT, STROBE, PRISMA, ARRIVE), and ends with a structural critique that verifies each claim traces to a result and that the Discussion does not overreach beyond the design.

**When to use:** After data collection and analysis are complete, results and key claims are settled, and you are ready to draft a primary research article — not during analysis, and not for review articles (use a synthesis-specific template instead).

**Required inputs:**
- **Discipline.** The field and subfield (sets reporting guideline, citation style, and convention norms).
- **Manuscript / finding context.** The study design, the analyses run, and the actual results, p-values, effect sizes, and confidence intervals — user-supplied; never invented.
- **Target venue or audience.** Target journal or conference and, if known, its structure/section requirements and word limits.
- **Study type.** RCT, observational/cohort, systematic review, in vivo animal, lab/bench, computational, etc. (selects the EQUATOR guideline).
- **Key claims.** The 1–4 take-home messages the authors intend to support, flagged as confirmatory (pre-specified) vs. exploratory/post-hoc.

**Optional inputs:**
- Pre-registration / protocol reference and any deviations from it.
- Figure/table list with the claim each supports.
- Data and code availability status and repository links.
- Prior related work the authors want positioned in the Introduction.
- Funding, ethics approval, and competing-interest statements.

**Constraints — Must:**
- Build the IMRaD scaffold (sections → subsections → one-sentence claim each) BEFORE writing any prose, and confirm the scaffold with the user.
- Map each Results paragraph to exactly one figure or table; if no figure supports a claim, mark it a gap.
- Structure Discussion paragraph 1 as a direct answer to the research question, then mechanism, then limitations, then generalization.
- Name and follow the EQUATOR reporting guideline for the stated study type so required content is not omitted.
- Preserve the confirmatory (pre-specified) vs. exploratory (post-hoc) distinction in every claim the draft makes.
- Include a data and code availability statement and surface preprint posting by default (Open Science default).
- Use calibrated, falsifiable language and substitute specific claims for promotional words.

**Constraints — Must Not:**
- Do not invent results, numbers, citations, DOIs, author claims, or journal requirements. Draft only from user-supplied content; mark gaps `[user-supplied]` and ask.
- Do not write Discussion claims that exceed the study design (e.g., causal language for observational data; clinical recommendations from a pilot).
- Do not use "novel," "groundbreaking," "first-ever," "gold standard," or "unprecedented" in drafted text.
- Do not relabel an exploratory or post-hoc result as confirmatory, or report a subgroup finding as if pre-specified.
- Do not fill Methods detail from assumption — every parameter the user did not supply is `[user-supplied]`.

**Instructions:**

1. **Confirm context and guideline.** Restate discipline, study type, target venue, and the EQUATOR guideline that applies. List its mandatory checklist items so none are silently dropped.
2. **Lock the skeleton first.** Output the IMRaD scaffold: each section, its subsections, and a single declarative one-sentence claim per subsection. Do not write prose yet. Present this for confirmation.
3. **Map claims to evidence.** For each claim, name the figure/table/result that supports it. Flag any claim with no supporting result as a `[gap]` and any result with no claim as candidate for supplement.
4. **Draft Introduction.** Funnel from broad context to the specific gap to the research question/hypothesis and the study's approach. Cite only user-supplied references; mark needed citations `[user-supplied]`.
5. **Draft Methods to the guideline.** Walk the reporting checklist; for each required element, fill from supplied detail or insert `[user-supplied]`. Keep tense and reproducibility discipline (enough to replicate).
6. **Draft Results.** One paragraph per figure/table, reporting only supplied statistics; state effect sizes and intervals, not just p-values. Keep confirmatory results first, exploratory clearly labeled. No interpretation here.
7. **Draft Discussion in the fixed order.** Paragraph 1 = direct answer; then mechanism; then limitations (including design constraints); then generalization/scope. Keep every claim within what the design supports.
8. **Add statements.** Insert data/code availability, preprint, ethics, funding, and competing-interest statements; surface preprint posting as the default option.
9. **Run the structural critique pass.** Audit: does each claim trace to a result? Is any Discussion claim broader than the design? Is any confirmatory/exploratory label wrong? Report findings as an action list.

**Output format (locked):**

```
## Reporting Guideline & Conventions
[study type → EQUATOR guideline; target venue; word/section limits]

## IMRaD Skeleton (claims locked before prose)
Introduction
  - [subsection] → [one-sentence claim]
Methods
  - [subsection] → [one-sentence claim]
Results
  - [subsection] → [one-sentence claim] → [figure/table]
Discussion
  - Answer → [claim]
  - Mechanism → [claim]
  - Limitations → [claim]
  - Generalization → [claim]

## Claim → Evidence Map
| Claim | Confirmatory/Exploratory | Supporting figure/table/result | Status |

## Draft: Introduction
[prose]

## Draft: Methods
[prose, guideline-complete]

## Draft: Results
[prose, one paragraph per figure/table]

## Draft: Discussion
[answer → mechanism → limitations → generalization]

## Availability & Disclosure Statements
- Data availability: [...]
- Code availability: [...]
- Preprint: [default: post to a recognized server; confirm]
- Ethics / Funding / Competing interests: [user-supplied]

## Structural Critique
- Untraceable claims: [...]
- Overreaching Discussion claims: [...]
- Mislabeled confirmatory/exploratory: [...]
- Outstanding [user-supplied] gaps: [...]
```

**Reporting-standard / convention alignment:** IMRaD structure; the EQUATOR Network reporting guideline matching the study type (CONSORT for RCTs, STROBE for observational, PRISMA for systematic reviews, ARRIVE for animal research, and discipline equivalents); target-journal section and word-limit requirements.

**Verification checklist (before delivering):**
- [ ] Skeleton with one-sentence claims was locked before any prose was written.
- [ ] Every Results paragraph maps to a named figure or table.
- [ ] Every Discussion claim stays within what the study design supports.
- [ ] Confirmatory vs. exploratory (and pre-specified vs. post-hoc) labels are correct and preserved.
- [ ] The correct EQUATOR guideline is named and its required items are present or marked `[user-supplied]`.
- [ ] No invented numbers, citations, DOIs, or journal requirements appear.
- [ ] Data/code availability and preprint statements are present.
- [ ] No banned promotional words ("novel," "groundbreaking," etc.) appear in drafted text.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Causal overreach | Polished Discussion asserting X causes Y from observational/correlational data | Match claim verb to design; flag any causal verb without an interventional design |
| Confirmatory inflation | A post-hoc subgroup result written as the headline pre-specified finding | Carry the confirmatory/exploratory label from the claim map into every paragraph |
| Phantom citation | A fluent sentence with a plausible but unverifiable reference | Citations only from user-supplied list; otherwise `[user-supplied]` |
| Guideline drift | Clean draft missing a mandatory checklist item (e.g., CONSORT flow) | Walk the named guideline checklist explicitly in step 5 |
| Methods confabulation | Reproducible-sounding parameters the user never provided | Any unsupplied parameter is `[user-supplied]`, never inferred |
