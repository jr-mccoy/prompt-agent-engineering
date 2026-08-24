---
title: "Data Visualization as an Image — Chart / Graph Render"
category: image-generation/scientific-technical
description: "Render a chart or graph as an image, with a strong data-accuracy protocol: image models distort proportions and invent values — supply exact data, prefer search grounding (Nano Banana Pro) or a real charting tool, and verify every value."
techniques:
  - ST-01
  - ST-02
  - SV-12
  - SV-13
difficulty: intermediate
tags:
  - data-visualization
  - chart
  - graph
  - infographic
  - accuracy
  - anti-fabrication
  - nano-banana
  - gpt-image-2
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/scientific-technical/scientific_illustration.md
  - domain-image-generation/scientific-technical/technical_exploded_diagram.md
  - domain-image-generation/nano-banana/nanobana_search_grounded_infographic.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# Data Visualization as an Image — Chart / Graph Render

**Objective:** Render a **chart or graph as an image** — a bar/line/pie/scatter visualization styled for a slide, poster, report, or social post. Use case: presentation hero charts, editorial data graphics, infographic chart panels.

> ## ⚠️ Data-Accuracy Protocol (read first — this is the most error-prone task in this directory)
> **Image models do not plot data — they draw something that looks like a chart.** Bar heights, line slopes, pie-slice angles, and axis ticks are rendered **approximately and often wrong**; the model can also **invent values, labels, and axis numbers**. A generated chart can misrepresent your data while looking polished.
>
> Mandatory practice — choose one:
> 1. **Best (for real accuracy): use an actual charting tool.** For any chart whose values must be correct (analysis, publication, anything decision-bearing), render it with a real library (matplotlib, D3, a spreadsheet, etc.) — not an image model. Use the image model only for purely illustrative/decorative "chart-like" visuals.
> 2. **If you must use an image model:**
>    - **Supply the exact data** — every value, every label, every axis tick — in the prompt. Never let the model choose numbers.
>    - **Prefer Nano Banana Pro** for its near-perfect text rendering and **Google Search grounding** when the figure must reflect verifiable current data (grounding can fetch/verify values; it does not guarantee correct *plotting*).
>    - **Measure the output against the data.** Check that bar heights/angles/slopes actually match the supplied values — image models distort proportions even when given exact numbers.
> 3. **Never present an image-model chart as a faithful data plot without value-by-value verification.**

**Why model choice matters:** **Nano Banana Pro** is the first choice for chart *images* because of its text accuracy and search grounding. **gpt-image-2** can produce a polished chart-styled layout with ~95% text accuracy but the same proportion-distortion risk. For correctness, neither replaces a real charting library.

**API parameters:**
- Nano Banana path: `model="gemini-3-pro-image"` (Pro — text + grounding) preferred; `quality="high"`, `n=1`
- gpt-image-2 path: `model="gpt-image-2"`, `/v1/images/generations`, `quality="high"`, `n=1`

---

## Inputs

- `[CHART TYPE]` — bar / grouped bar / line / pie / scatter / area
- `[EXACT DATA]` — every data point with its label and value (you supply this; the model must not invent any)
- `[AXES SPEC]` — axis titles, units, exact tick values, ranges
- `[SERIES/LABELS]` — exact legend and data labels (verbatim)
- `[STYLE]` — palette, flat/3D (prefer flat 2D for honesty), background, font feel
- `[TITLE/CAPTION]` — exact title and caption text (verbatim)
- `[USE]` — decorative/illustrative vs. data-bearing (if data-bearing, route to a real charting tool)

---

## Constraints (Must / Must Not)

**Must:**
- Use **only the values, labels, and ticks in `[EXACT DATA]` / `[AXES SPEC]`** — verbatim, nothing invented.
- Prefer **flat 2D** chart styling (3D and exotic effects worsen proportion distortion and mislead).
- State that the output is an **unverified chart image** requiring value-by-value verification.
- Route any **data-bearing / decision-bearing** chart to a real charting library instead.

**Must Not:**
- Let the model choose, round, or fill in any data values, axis ticks, or labels.
- Present the image as a faithful plot without measuring it against the data.
- Use 3D/perspective tricks that distort apparent proportions.
- Add gridlines, ticks, or data points not specified.

---

## Production Prompt — Nano Banana Pro path (text-accurate, optional grounding)

```
TASK: Render a clean, flat 2D [CHART TYPE] as a presentation-quality image. Background: [STYLE background]. Palette: [STYLE palette]. This is a chart IMAGE, not a data plot.

EXACT DATA (use ONLY these values and labels, verbatim — invent, round, or add nothing):
[EXACT DATA — list every category/point with its exact value and label]

AXES (render exactly as specified):
- X axis: title "[x title]", ticks: [exact ticks].
- Y axis: title "[y title]", units [units], range [min–max], ticks: [exact ticks].

SERIES / LABELS (verbatim): [SERIES/LABELS]
TITLE (verbatim): "[TITLE/CAPTION]"

[If values must reflect current verifiable data:]
Use Google Search grounding to confirm the supplied values reflect the latest published figures; if grounding finds a discrepancy, flag it rather than silently changing the chart.

STYLE: flat 2D (no 3D/perspective), [palette], clean axis lines, legible labels.

CONSTRAINTS:
- MUST: bar heights / slopes / slice angles must match the supplied values proportionally; render only the supplied labels/ticks/title verbatim.
- MUST NOT: invent or round any value/label/tick; use 3D distortion; add unstated elements.
- Quality: "high".

This is an UNVERIFIED chart image. The values must be checked against the supplied data before any use.
```

---

## Production Prompt — gpt-image-2 path (polished chart-styled layout)

```
SCENE:
A clean, flat 2D [CHART TYPE] styled for a [slide / report / poster]. [STYLE background], [STYLE palette]. This is a chart IMAGE, not a computed plot.

DATA TO DEPICT (use ONLY these, verbatim — invent nothing):
[EXACT DATA]

AXES: X "[x title]" ticks [exact ticks]; Y "[y title]" [units], range [min–max], ticks [exact ticks].
LABELS/LEGEND (verbatim): [SERIES/LABELS].
TITLE (verbatim): "[TITLE/CAPTION]".

KEY DETAILS:
- Flat 2D only; proportions of bars/lines/slices should match the supplied values.
- Clean axis lines, legible labels, generous margins.

USE CASE: An UNVERIFIED illustrative chart image. Values must be verified against the data; for data-bearing charts use a real charting library instead.

CONSTRAINTS:
- Render only the supplied data/labels/ticks/title; invent nothing.
- No 3D/perspective distortion; no unstated gridlines or points.
- Format: [size], quality="high".

If any value, label, tick, or title differs from the supplied data, or proportions misrepresent the values, the image is incorrect.
```

---

## Iteration Plan

1. "Bar 3's height doesn't match its value relative to the others — rescale so heights are proportional to the supplied data."
2. "An axis tick appeared that I didn't specify (`[tick]`) — use only the exact ticks I listed."
3. "A data label was invented/changed — render the labels verbatim as supplied."
4. "It rendered in 3D and distorts the comparison — switch to flat 2D."
5. "For this chart accuracy is decision-bearing — abandon the image model and render it in [matplotlib/D3/spreadsheet] instead, using this image only as a style reference."

---

## Verification

> The proportion check is the core gate — do it value by value.

- [ ] Every value, label, axis tick, legend entry, and title matches `[EXACT DATA]` / `[AXES SPEC]` verbatim — nothing invented.
- [ ] Bar heights / line slopes / pie-slice angles are **proportionally correct** vs. the supplied values (measured, not eyeballed).
- [ ] Flat 2D styling; no 3D/perspective distortion.
- [ ] No unstated gridlines, ticks, or data points added.
- [ ] If the chart is **data-bearing/decision-bearing**, it was rendered with a real charting tool — not the image model.
- [ ] Output documented as an AI-generated chart image with value-verification provenance.
