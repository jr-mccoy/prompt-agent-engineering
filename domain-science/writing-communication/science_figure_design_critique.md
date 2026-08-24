---
title: "Figure Design Critique (Accessibility, Honesty, Encoding)"
category: science/writing-communication
description: "Audit an existing or planned scientific figure for color-blind safety, chart junk, encoding appropriateness, accessibility, and axis honesty, returning a ranked issue→why→fix table."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-02
  - CM-02
  - NE-10
difficulty: advanced
tags:
  - figure-design
  - color-blind-safe
  - data-visualization
  - accessibility
  - chart-junk
  - axis-honesty
  - encoding
  - tufte
updated: "2026-06-26"
related_prompts:
  - domain-science/writing-communication/science_figure_legend_drafter.md
  - domain-science/writing-communication/science_table_design_critique.md
---

# Figure Design Critique (Accessibility, Honesty, Encoding)

**Objective:** Critique a scientific figure (existing or planned) for visual honesty, encoding appropriateness, color-blind safety, chart junk, and accessibility, producing a ranked, actionable issue→why→fix table. The critique takes an adversarial stance toward visual overclaiming — truncated axes, bar-of-mean plots that hide distribution, red-green-only encoding — and recommends concrete, palette-specific fixes. It evaluates only the figure the user describes; it never invents the underlying data.

**When to use:** Before submitting or finalizing a figure, when a reviewer or coauthor flags clarity/fairness concerns, or when standardizing a figure set against accessibility and reporting norms.

**Required inputs:**
- **Discipline.** Field — sets convention expectations (e.g., flow-cytometry plots, ecology ordinations, dose-response curves).
- **Figure context.** What the figure shows: chart type(s), axes, encoded variables, groups, and how data are summarized — user-supplied; never invented.
- **Target venue.** Journal/conference and its figure spec if known (resolution/DPI, RGB vs. CMYK, font embedding, max width).

**Optional inputs:**
- **Current color/marker scheme** and whether color is the sole encoder of any variable.
- **How data are aggregated** (bar of mean, box, violin, dot/raw points) and per-group n.
- **Axis ranges/baselines**, log vs. linear, dual axes, broken axes.
- **Output medium** (print column width, slide, poster) and intended print scale font sizes.
- **A rendered image or mock** if available for direct inspection.

**Constraints — Must:**
- Recommend **color-blind-safe palettes by name** (Okabe-Ito, ColorBrewer qualitative/sequential, viridis) and never accept red-green alone as a discriminator.
- Apply **Tufte data-ink / chart-junk** reasoning: flag non-data ink (heavy gridlines, 3D, gratuitous gradients, redundant legends).
- Flag **distribution-hiding encodings** (bar-of-mean) and recommend showing the data (dot/box/violin) when n is small enough.
- Flag **axis honesty** problems: truncated/non-zero baselines that exaggerate effects on bar charts, mismatched dual axes, inconsistent scales across panels.
- Treat **accessibility as first-class**: contrast (WCAG-style ratios), minimum font size at print scale, and redundant (non-color) encoding.
- Rank issues by severity (misleading > inaccessible > suboptimal > cosmetic) and tie each to a concrete fix.

**Constraints — Must Not:**
- Do not invent the underlying data, sample sizes, statistics, units, or what the figure/table actually shows. Critique/draft only from user-supplied content; mark gaps `[user-supplied]`.
- Do not recommend a fix that would misrepresent the data (e.g., do not propose smoothing or trimming that hides variance).
- Do not assert that a zero baseline is always required — apply it to magnitude/bar encodings, not to all line/position encodings; reason explicitly.
- Do not introduce promotional framing; critique is descriptive and severity-ranked.

**Instructions:**

1. **Restate the figure and inventory encodings.** Summarize discipline, figure context, and venue. List each visual channel (position, length, area, color, shape) and the variable it encodes. Mark any unstated detail `[user-supplied]`.
2. **Color-blind safety pass.** Check whether any variable is encoded by color alone, and whether the palette survives deuteranopia/protanopia/tritanopia. Recommend a named safe palette (Okabe-Ito for categorical, viridis for sequential) and a redundant cue (shape, line style, direct labels).
3. **Chart-junk / data-ink pass.** Identify non-data ink: 3D effects, drop shadows, dense gridlines, redundant legends, decorative backgrounds. Recommend removals that raise the data-ink ratio without losing information.
4. **Encoding appropriateness pass.** Judge whether the chart type fits the data: bar-of-mean hiding distribution (→ dot/box/violin), pie for proportions that need comparison, dual axes implying false correlation, area encoding magnitude misleadingly.
5. **Axis honesty pass (adversarial).** Inspect baselines, ranges, log/linear choice, and cross-panel scale consistency. Flag truncation that exaggerates a difference; state how the reader is misled and the honest alternative.
6. **Accessibility pass.** Evaluate contrast against background, font size at the stated print width, line weights, and whether the figure is interpretable in grayscale. Provide concrete minimums (e.g., readable at single-column print scale).
7. **Venue/spec compliance.** Check resolution/DPI, color mode (RGB/CMYK), embedded fonts, and size limits if the venue is known; otherwise mark `[user-supplied]`.
8. **Probability-weighted reviewer concerns.** Enumerate the most likely reviewer objections with a rough likelihood (high/medium/low) so the author can triage what to fix first.
9. **Rank and assemble.** Order all findings by severity, each with why-it-misleads-or-excludes and a specific fix; close with a prioritized fix list.

**Output format (locked):**

```
## Encoding inventory
| Visual channel | Variable encoded | Notes / [user-supplied] |
|---|---|---|
| ... | ... | ... |

## Ranked critique
| # | Severity | Issue | Why it misleads / excludes | Fix |
|---|---|---|---|---|
| 1 | misleading | ... | ... | ... |
| 2 | inaccessible | ... | ... | ... |
| ... | ... | ... | ... | ... |

## Likely reviewer concerns (probability-weighted)
- [high] ...
- [medium] ...
- [low] ...

## Prioritized fix list
1. ...
2. ...
```

**Reporting-standard / convention alignment:** Tufte (data-ink ratio, chart junk); color-blind-safe palettes (Okabe-Ito, ColorBrewer, viridis); WCAG contrast guidance applied to figures; journal figure guidelines (resolution/DPI, RGB vs. CMYK, font embedding, max width); "show the data" guidance favoring dot/box/violin over bar-of-mean; error-bar disclosure norms (Cumming et al.); grayscale-legibility and redundant-encoding accessibility practice.

**Verification checklist (before delivering):**
- [ ] Every variable's encoding channel is inventoried; color-only encodings are flagged.
- [ ] A named color-blind-safe palette is recommended where color matters.
- [ ] Bar-of-mean or other distribution-hiding encodings are flagged with a show-the-data alternative.
- [ ] Axis baseline/range/log choices are checked; any exaggerating truncation is named.
- [ ] Contrast, print-scale font size, and grayscale legibility are assessed.
- [ ] Each issue carries a severity rank and a concrete, non-distorting fix.
- [ ] Venue spec items (DPI, color mode, fonts) are checked or marked `[user-supplied]`.
- [ ] No underlying data, n, or statistic was invented.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Pretty but inaccessible | A polished, colorful figure that fails in deuteranopia/grayscale | Run color-blind + grayscale pass regardless of aesthetic polish |
| Honest-looking truncation | A non-zero baseline that "fits the data" but triples the apparent effect | Adversarial axis pass; require zero baseline for magnitude/bar encodings |
| Over-zealous zero baseline | Forcing a zero baseline on a line/position plot where it destroys resolution | Apply baseline rule to magnitude encodings only; reason per chart type |
| Distribution hidden | Bar-of-mean + SEM that looks clean but conceals spread/outliers | Recommend dot/box/violin when n permits showing raw data |
| Fabricated fix | Suggesting smoothing/trimming that improves looks but hides variance | Forbid fixes that alter the data's honest representation |
