---
title: "Figure Legend Drafter (Self-Contained)"
category: science/writing-communication
description: "Draft a stand-alone figure legend that a reader can interpret without the main text — claim sentence, per-panel content, species, n per group, error-bar definition, statistical test, and scale bars."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - figure-legend
  - scientific-writing
  - sample-size
  - error-bars
  - statistical-reporting
  - scale-bar
  - reproducibility
  - open-science
updated: "2026-06-26"
related_prompts:
  - domain-science/writing-communication/science_figure_design_critique.md
  - domain-science/writing-communication/science_table_design_critique.md
---

# Figure Legend Drafter (Self-Contained)

**Objective:** Draft a publication-ready figure legend that is fully self-contained — readable and interpretable without the surrounding manuscript text. The legend must state the claim, describe every panel, and disclose the conventions a reader needs to evaluate the data: organism/species, sample size per group, what error bars represent, the statistical test and significance symbols, and scale bars. It drafts only from user-supplied facts; it never invents data, sample sizes, error-bar types, or statistics.

**When to use:** You have a finished or near-finished figure and need a legend that meets journal "self-contained legend" requirements and reporting standards, or you have a draft legend that omits mandatory disclosure elements.

**Required inputs:**
- **Discipline.** Field (e.g., cell biology, ecology, neuroscience, materials science) — sets convention expectations.
- **Figure context.** What the figure shows: each panel, the variables on each axis, the experimental groups — user-supplied; never invented.
- **Target venue.** Journal name or style guide if known (e.g., Nature, Cell/STAR Methods, PNAS, IEEE), to match house legend conventions.

**Optional inputs:**
- **Organism/species/cell line** and biological vs. technical replicate structure.
- **Sample size (n) per group** and what one n represents (animal, cell, field of view, run).
- **Error-bar type** (SD, SEM, 95% CI) and central-tendency measure (mean, median).
- **Statistical test(s)** and the meaning of asterisks/letters/symbols.
- **Scale-bar lengths** (for microscopy/imaging) and magnification.
- **Abbreviations** used in the panels; data-availability/source-data location.

**Constraints — Must:**
- Open the legend with a single declarative **title sentence stating the claim/result**, not a topic label.
- Require explicit disclosure of: per-group **n** and what one unit of n is; **error-bar definition** (state SD vs. SEM vs. 95% CI — never leave ambiguous); **statistical test** and the exact meaning of every significance symbol; **scale bar** length for any imaging panel.
- Distinguish **biological replicates** from **technical replicates** where relevant.
- Define every abbreviation, symbol, and non-obvious color/marker on first use within the legend.
- Use calibrated, descriptive language; mark every fact not supplied by the user as `[user-supplied]`.

**Constraints — Must Not:**
- Do not invent the underlying data, sample sizes, statistics, units, or what the figure/table actually shows. Critique/draft only from user-supplied content; mark gaps `[user-supplied]`.
- Do not assert an error-bar type, central-tendency measure, or statistical test the user did not state — leave `[user-supplied: SD / SEM / 95% CI?]`.
- Do not use "novel," "groundbreaking," "first-ever," or other promotional language in the drafted legend.
- Do not silently convert significance asterisks to p-values, or vice versa, without the user's stated mapping.

**Instructions:**

1. **Intake and gap scan.** Restate discipline, figure context, and venue. List which mandatory disclosure elements (claim, panels, species, n, error bars, test, scale bar, abbreviations) are present vs. missing. Every missing element becomes an explicit `[user-supplied: ...]` placeholder — never a guess.
2. **Write the title sentence.** One sentence that states the result the figure supports (the claim), phrased neutrally. Avoid promotional adjectives.
3. **Describe each panel.** For panels A, B, C…: state what is plotted (y vs. x), the groups/conditions, and the readout. Keep panel descriptions parallel in structure.
4. **Disclose the experimental unit.** State the organism/species/cell line, per-group n, and what one n represents (e.g., "n = [user-supplied] mice per group; each point is one animal"). Separate biological from technical replicates.
5. **Define error bars and central tendency.** State explicitly which is shown (mean ± SD, mean ± SEM, median with IQR, or 95% CI). If the user did not state it, insert `[user-supplied: error-bar type required]` and flag that SEM and 95% CI are not interchangeable.
6. **State statistics and symbol meanings.** Name the test, comparison structure, and the exact mapping of every symbol (e.g., "*p < 0.05, **p < 0.01 by [user-supplied test]"). Do not invent thresholds.
7. **Add scale bars and imaging metadata.** For any micrograph/imaging panel, state scale-bar length and, if relevant, magnification, stain/label, and channel-to-color mapping.
8. **Define abbreviations and finalize accessibility notes.** Spell out every abbreviation; note any color encodings and confirm a redundant (non-color) cue exists for color-blind readers.
9. **Append data-availability line.** Add a source-data / repository pointer per Open Science defaults (deposit underlying data; figure source data available), marked `[user-supplied]` if unknown.

**Output format (locked):**

```
## Gap scan
| Mandatory element | Present? | Placeholder if missing |
|---|---|---|
| Claim/title sentence | yes/no | ... |
| Per-panel description | yes/no | ... |
| Species / experimental unit | yes/no | ... |
| n per group + unit of n | yes/no | ... |
| Error-bar definition (SD/SEM/CI) | yes/no | ... |
| Statistical test + symbol meaning | yes/no | ... |
| Scale bar (imaging) | yes/no | ... |
| Abbreviations defined | yes/no | ... |

## Drafted legend
**Figure [N]. [Title sentence stating the claim].**
(A) [Panel A: what is plotted, groups, readout].
(B) [Panel B ...].
[Organism/species; n = [user-supplied] per group, each n = one [user-supplied unit]; biological vs. technical replicates].
Data are [mean / median] ± [user-supplied: SD / SEM / 95% CI]. [Statistical test]; [symbol]p < [threshold].
Scale bar, [user-supplied] µm.
Abbreviations: [defined].
Source data: [user-supplied repository/figure source data].

## Open items for the author
- [bullet list of every [user-supplied] placeholder to resolve]
```

**Reporting-standard / convention alignment:** Self-contained-legend requirements (Nature/Cell/PNAS author guidelines); error-bar disclosure norms (Cumming, Fidler & Vaux error-bar rules — state SD vs. SEM vs. CI, never imply equivalence); microscopy scale-bar requirements; ARRIVE-style reporting of n and experimental unit for in vivo work; STAR Methods source-data/data-availability conventions.

**Verification checklist (before delivering):**
- [ ] Title sentence states a claim, not a topic, and contains no promotional language.
- [ ] Every panel referenced in the figure context has a description.
- [ ] Species/experimental unit and per-group n are stated or marked `[user-supplied]`.
- [ ] Error-bar type is explicitly named (SD/SEM/95% CI) or flagged as required.
- [ ] Statistical test and the meaning of every significance symbol are stated.
- [ ] Scale bar is present for every imaging panel (or `[user-supplied]`).
- [ ] All abbreviations and color/marker encodings are defined.
- [ ] No data value, n, error-bar type, or test was invented; all gaps are `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Error-bar ambiguity | Legend says "± error" or "± SE" without defining SD vs. SEM vs. CI | Force explicit naming; flag that SEM/CI are not interchangeable |
| n inflation | Technical replicates counted as n, inflating apparent sample size | Require "one n = one [unit]" and separate biological vs. technical replicates |
| Invented statistic | A test or p-threshold filled in to make the legend complete | Insert `[user-supplied]`; never supply a test the author did not state |
| Topic-not-claim title | "Effect of X on Y" reads complete but states no result | Require a declarative claim sentence in the title position |
| Missing scale bar | Pretty micrograph legend with no scale bar feels finished | Checklist blocks delivery until a scale bar (or placeholder) exists |
