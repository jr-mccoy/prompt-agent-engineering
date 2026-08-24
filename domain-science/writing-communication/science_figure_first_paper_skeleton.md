---
title: "Figure-First Paper Skeleton"
category: science/writing-communication
description: "Builds a figure-first manuscript outline: lock the figures and the single claim each must support, order them into the narrative arc, then derive Results subsections and Discussion points from that figure sequence."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - RT-03
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - figure-first
  - paper-outline
  - figure-claim-mapping
  - narrative-arc
  - results-structure
  - scientific-writing
  - reproducibility
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/writing-communication/science_imrad_paper_drafter.md
  - domain-science/writing-communication/science_abstract_compressor.md
  - domain-science/methods-foundations/science_methods_section_drafter.md
---

# Figure-First Paper Skeleton

**Objective:** Treat the figures and tables as the paper's backbone. Enumerate the intended figures/tables, state the single claim each must support, order them into a narrative arc, and only then derive the Results subsections and Discussion points from that sequence. The output is a figure-claim-narrative table plus a derived skeleton — built before any prose is locked.

**When to use:** Early in manuscript planning, once analyses are done and you can name the figures, but before writing Results or Discussion prose. This is the upstream step to the IMRaD drafter.

**Required inputs:**
- **Discipline.** Field and subfield (sets figure conventions and what counts as a main-text vs. supplementary figure).
- **Manuscript / finding context.** The analyses and results that the figures will display — user-supplied; never invented.
- **Target venue or audience.** Journal/conference and, if known, its main-text figure limit and supplementary policy.
- **Figure/table candidates.** A list (even rough) of the figures and tables the authors have or intend to make.

**Optional inputs:**
- The intended overall narrative / take-home message.
- Pre-registration reference (to distinguish confirmatory display items from exploratory ones).
- Existing draft Results to reverse-engineer against the figure set.
- Data/code availability and preprint status.

**Constraints — Must:**
- Assign exactly one primary claim to each figure/table; figures must be designed before the text is locked.
- Order the figures into a single narrative arc (setup → core result → support → boundary/mechanism).
- Flag any figure that carries no distinct claim as a candidate for the supplement.
- Flag any intended claim with no supporting figure as a `[gap]`.
- Derive Results subsections and Discussion points directly from the ordered figure sequence.
- Distinguish confirmatory display items from exploratory ones and preserve that label downstream.
- Surface data/code availability and preprint posting by default (Open Science default).

**Constraints — Must Not:**
- Do not invent results, numbers, citations, DOIs, author claims, or journal requirements. Draft only from user-supplied content; mark gaps `[user-supplied]` and ask.
- Do not assign a figure a claim its underlying data cannot support.
- Do not promote an exploratory figure to confirmatory headline status.
- Do not use "novel," "groundbreaking," "first-ever," "gold standard," or "unprecedented" in drafted text.
- Do not lock prose in this step — this produces structure, not finished Results paragraphs.

**Instructions:**

1. **Confirm scope.** Restate discipline, target venue, main-text figure limit, and supplementary policy. List the candidate figures/tables the user supplied.
2. **Assign one claim per figure.** For each figure/table, write the single declarative claim it must support, drawn only from supplied results. Tag any missing data `[user-supplied]`.
3. **Test each figure's load.** Use option comparison: does this figure carry a distinct claim, or does it duplicate/decorate? Duplicative or decorative figures are flagged for the supplement.
4. **Find the gaps both ways.** List intended claims with no figure (`[gap]` — needs an analysis or display item) and figures with no claim (supplement candidates).
5. **Order into a narrative arc.** Sequence the load-bearing figures: orientation/setup, core confirmatory result, supporting results, then boundary conditions or mechanism. Justify the order.
6. **Derive Results subsections.** Convert each figure, in arc order, into a Results subsection heading + its one-sentence claim.
7. **Derive Discussion points.** From the same sequence, derive the Discussion arc: the answer (from the core figure), mechanism/support (from supporting figures), and limitations (from gaps and boundary figures).
8. **Assemble the figure-claim-narrative table and self-check.** Output the table, the derived skeleton, the supplement/gap lists, and a note that figures must be finalized before text is locked.

**Output format (locked):**

```
## Scope
[discipline; venue; main-text figure limit; supplementary policy]

## Figure–Claim–Narrative Table
| # | Figure/Table | Single claim it supports | Confirmatory/Exploratory | Arc position | Main text / Supplement |
|---|---|---|---|---|---|

## Gaps & Supplement Candidates
- Claims with no supporting figure ([gap]): [...]
- Figures with no distinct claim (→ supplement): [...]
- Outstanding [user-supplied] data: [...]

## Narrative Arc (ordered, justified)
1. [setup figure] — why first
2. [core result figure] — the answer
3. [supporting figures] — support/mechanism
4. [boundary figure] — scope/limits

## Derived Results Subsections
- [subsection heading] → [one-sentence claim] → [figure]

## Derived Discussion Points
- Answer → [from core figure]
- Mechanism/support → [from supporting figures]
- Limitations → [from gaps and boundary figures]

## Open Science Note
- Data/code availability + preprint: [default surfaced]

## Note
Figures must be designed and finalized before the manuscript text is locked.
```

**Reporting-standard / convention alignment:** IMRaD (the figure sequence seeds Results and Discussion structure); the EQUATOR reporting guideline for the study type (ensures required display items — e.g., CONSORT flow diagram, PRISMA flow diagram — are present); target-journal main-text figure limits and supplementary policy.

**Verification checklist (before delivering):**
- [ ] Each main-text figure/table has exactly one distinct primary claim.
- [ ] Figures without a distinct claim are flagged for the supplement.
- [ ] Every intended claim has a supporting figure, or is marked `[gap]`.
- [ ] The narrative arc order is stated and justified.
- [ ] Results subsections and Discussion points are derived from the figure sequence, not invented.
- [ ] Confirmatory vs. exploratory labels are assigned and preserved.
- [ ] No invented data, numbers, or journal limits appear.
- [ ] The note that figures precede locked text is present.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Decorative figure | A polished figure that restates another's claim | Step 3 option comparison; duplicative figures move to supplement |
| Orphan claim | A take-home message with no display item behind it | Step 4 gap list flags claims lacking a figure |
| Arc by habit | Figures ordered by when they were made, not by argument | Require justification for each arc position |
| Exploratory headline | An exploratory figure placed as the core result | Carry confirmatory/exploratory labels into the arc |
| Overloaded figure | One figure asked to carry several unrelated claims | One primary claim per figure; split or supplement the rest |
