---
title: "Table Design Critique (Precision, Units, Missingness, Footnotes)"
category: science/writing-communication
description: "Audit a scientific table for significant-figure discipline, units in every header, explicit missing-data convention, decimal alignment, footnote economy, and ordering that serves the comparison."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - table-design
  - significant-figures
  - units
  - missing-data
  - footnotes
  - scientific-writing
  - precision-reporting
  - accessibility
updated: "2026-06-26"
related_prompts:
  - domain-science/writing-communication/science_figure_design_critique.md
  - domain-science/writing-communication/science_figure_legend_drafter.md
---

# Table Design Critique (Precision, Units, Missingness, Footnotes)

**Objective:** Critique a scientific table for precision discipline, unit labeling, missing-data handling, alignment, footnote economy, and ordering — returning a ranked issue→why→fix table plus a cleaned-table template. The critique flags over-precision (more decimals than the measurement supports) as a question to the author, never a silent correction, and never invents or alters reported values. It also judges whether a figure would communicate the comparison better than the table.

**When to use:** Before submitting a manuscript table, when standardizing tables across a paper, or when a reviewer flags inconsistent precision, ambiguous units, or unclear missing entries.

**Required inputs:**
- **Discipline.** Field — sets convention expectations (e.g., clinical demographics tables, analytical chemistry results, benchmark tables).
- **Table context.** What the table shows: column headers, row entries, the values and their units, and what comparison the table is meant to support — user-supplied; never invented.
- **Target venue.** Journal/conference table style if known (e.g., STAR Methods, AMA, IEEE), for house conventions on precision, units, and footnotes.

**Optional inputs:**
- **Measurement precision** of each quantity (instrument resolution, reported uncertainty) to judge significant figures.
- **Missing-data convention** currently used (blank, "—", "ND", "NA") and whether zero ever means "not measured."
- **Footnote/abbreviation list** and any symbols (†, ‡, *) in use.
- **Intended row/column ordering** and the key comparison axis.
- **Whether a figure alternative** has been considered.

**Constraints — Must:**
- Enforce **significant-figure discipline**: precision consistent within a column and not exceeding what the measurement supports; flag mismatches as author questions.
- Require **units in every column header** (or a clearly stated table-wide unit), with consistent unit style.
- Require an **explicit missing-data convention** that is defined in a footnote, and verify that **0 is never conflated with missing/not-measured**.
- Check **decimal alignment** of numeric columns and consistent decimal places within a column.
- Apply **footnote economy**: every symbol/abbreviation defined exactly once, no orphan or undefined markers, minimal redundant notes.
- Evaluate **row/column ordering** so the layout serves the intended comparison, and assess whether a figure would communicate better.

**Constraints — Must Not:**
- Do not invent the underlying data, sample sizes, statistics, units, or what the figure/table actually shows. Critique/draft only from user-supplied content; mark gaps `[user-supplied]`.
- Do not silently round, reformat, or correct reported values; where precision looks excessive, raise it as a **question**, not a corrected value.
- Do not assume a missing entry means zero, or vice versa — flag the ambiguity for the author to resolve.
- Do not add promotional language; the cleaned-table template carries only data and definitions.

**Instructions:**

1. **Restate and map the table.** Summarize discipline, table context, and venue. Lay out the column headers and the type of each (categorical, count, measured quantity, derived statistic). Mark unstated details `[user-supplied]`.
2. **Significant-figure pass.** For each numeric column, check that decimal places are consistent and do not exceed the supported measurement precision. Where reported precision looks implausibly high relative to the quantity, flag it as a question ("Is 4 decimals supported by the instrument resolution?") — never rewrite the value.
3. **Units pass.** Confirm every quantitative column header carries a unit (or a clearly stated table-wide unit). Flag missing, inconsistent, or ambiguous units (e.g., % vs. proportion, mixed SI/non-SI).
4. **Missingness pass.** Identify how missing data are represented and whether the convention is defined. Verify zeros and blanks are not conflated; flag any cell where "0" might mean "not measured."
5. **Alignment and formatting pass.** Check decimal alignment of numbers, consistent decimal places within columns, thousands separators, and that text vs. numeric columns are visually distinguishable.
6. **Footnote/abbreviation economy pass.** Verify every symbol and abbreviation is defined exactly once, no markers are orphaned or undefined, and notes are not redundant. Recommend consolidation where possible.
7. **Ordering and comparison-fit pass.** Judge whether row/column order supports the intended comparison (e.g., group the variables a reader contrasts). Assess whether a figure (dot plot, heatmap) would communicate the same comparison more clearly.
8. **Rank and assemble.** Order findings by severity (misleading/ambiguous > inconsistent > cosmetic), each with why-it-matters and a specific fix.
9. **Produce a cleaned-table template.** Output a corrected structural template that preserves all user-supplied values unchanged, with `[user-supplied]` placeholders where data or conventions are missing.

**Output format (locked):**

```
## Column map
| Column header | Type | Unit present? | [user-supplied] notes |
|---|---|---|---|
| ... | ... | yes/no | ... |

## Ranked critique
| # | Severity | Issue | Why it matters | Fix |
|---|---|---|---|---|
| 1 | ambiguous | ... | ... | ... |
| 2 | inconsistent | ... | ... | ... |
| ... | ... | ... | ... | ... |

## Precision questions for the author (not corrections)
- [Column X reports N decimals — is that supported by measurement precision?]
- ...

## Cleaned-table template
| Header (unit) | Header (unit) | ... |
|---|---|---|
| [user-supplied values, unchanged] | ... | ... |
Footnotes: [missing-data convention defined]; [every symbol/abbreviation defined once].

## Figure-vs-table recommendation
- [Whether a figure would communicate the comparison better, with reasoning]
```

**Reporting-standard / convention alignment:** Significant-figure / uncertainty reporting (report no more precision than the measurement supports); units-in-headers and SI-style conventions; explicit missing-data conventions distinct from zero; decimal alignment and within-column consistency; footnote/abbreviation definition discipline; STAR Methods / AMA / IEEE journal table style; "show the data" reasoning when a figure beats a dense table.

**Verification checklist (before delivering):**
- [ ] Every numeric column checked for consistent decimals and plausible precision.
- [ ] Over-precision raised as a question, never as a silently corrected value.
- [ ] Every quantitative column header has a unit (or a defined table-wide unit).
- [ ] Missing-data convention is explicit and defined in a footnote.
- [ ] No cell conflates 0 with missing/not-measured (or the ambiguity is flagged).
- [ ] Decimal alignment and numeric/text distinction assessed.
- [ ] Every footnote symbol and abbreviation is defined exactly once; no orphans.
- [ ] Cleaned-table template preserves all user-supplied values unchanged; gaps are `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| False precision | "3.14159 mg" looks rigorous but exceeds instrument resolution | Flag as an author question; never rewrite the reported value |
| Zero-as-missing | A "0" cell that actually means "not measured" reads as a real measurement | Require explicit missing convention; flag every ambiguous 0 |
| Silent correction | Auto-rounding values to "fix" inconsistency alters the data | Forbid value edits; raise precision/format as questions only |
| Orphan footnote | A "†" in the table with no matching definition looks complete | Check every symbol resolves to exactly one definition |
| Unit drift | Mixed % and proportion, or SI and non-SI, across columns | Require a unit in every header and consistent unit style |
| Table that should be a figure | A dense correctness-laden table that buries the one comparison readers need | Include explicit figure-vs-table recommendation |
