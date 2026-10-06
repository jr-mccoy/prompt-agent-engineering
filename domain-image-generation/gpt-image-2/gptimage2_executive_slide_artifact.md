---
title: "GPT Image 2 — Executive Slide Artifact"
category: image-generation/presentation
description: "Single deck slide with title, chart, and footer — briefed as an artifact specification, not an illustration."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-12
  - SV-17
difficulty: intermediate
tags:
  - gpt-image-2
  - slide
  - presentation
  - chart
  - executive
  - openai
updated: "2026-10-06"
related_prompts:
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
  - domain-presentations/
---

# GPT Image 2 — Executive Slide Artifact

**Objective:** Generate a single, presentation-ready slide that contains a clear title, a single chart or visual, supporting bullets, and a footer — all with verbatim copy and real data.

**API parameters (required):**
- `model="gpt-image-2"`
- `size="2560x1440"` (exactly 16:9 — standard slide; the largest non-experimental size. `1536x1024` is 3:2 and letterboxes in a 16:9 deck)
- `quality="high"` (required; charts have small numbers)
- `n=1`

---

## Inputs

- `[DECK NAME]` — e.g., "Q1 2026 Business Review"
- `[SLIDE NUMBER & TOTAL]` — e.g., "Slide 4 of 12"
- `[SLIDE TITLE]` — verbatim
- `[KEY METRIC]` — the headline number on the slide (verbatim, with units)
- `[CHART TYPE]` — bar / line / column / waterfall / single-stat / quadrant / table
- `[CHART DATA]` — verbatim labels and values
- `[BULLETS]` — 2–4 supporting bullets, verbatim
- `[FOOTER]` — verbatim source line and slide number
- `[BRAND PALETTE]` — hex codes (typically primary, secondary, surface, text)

---

## Constraints (Must / Must Not)

**Must:**
- Brief the slide as an artifact specification, not an illustration request.
- Treat the chart as data — verbatim labels and values.
- Lock the slide template (title bar position, body region, footer band).
- `quality="high"`.

**Must Not:**
- Allow the model to invent or smooth data values.
- Add decorative illustrations unless explicitly briefed.
- Use multiple chart types in one slide unless explicitly briefed.
- Render lorem ipsum or placeholder copy.

---

## Production Prompt

```
SCENE / CANVAS:
A single 16:9 presentation slide for [DECK NAME]. The image IS the slide — edge-to-edge, no presentation chrome, no laptop frame.

SUBJECT / STRUCTURE:
- TITLE BAR (top ~15% of canvas): contains the slide title.
- BODY REGION (middle ~70%): two-column layout — chart on the left ~60%, supporting bullets on the right ~40%.
- FOOTER BAND (bottom ~5%): source attribution and slide number.

KEY DETAILS — verbatim content:

TITLE: "[SLIDE TITLE]"

KEY METRIC (large, prominent inside or above the chart): "[KEY METRIC]"

CHART:
- Type: [CHART TYPE].
- X-axis labels (verbatim, in order): [comma-separated labels]
- Y-axis labels / data values (verbatim, in order): [comma-separated values, with units if any]
- Chart color: brand primary [HEX]. Highlight color (for the most-recent or most-important data point): brand accent [HEX].
- Gridlines: light hairline, [hex e.g., #E5E5E5]. Y-axis labels in [hex e.g., #6B6B6B].

BULLETS (right column, 2–4 items, verbatim):
1. "[BULLET 1]"
2. "[BULLET 2]"
3. "[BULLET 3]" (if present)
4. "[BULLET 4]" (if present)

FOOTER (verbatim): "[FOOTER]" on the left; "[SLIDE NUMBER & TOTAL]" on the right.

USE CASE:
Executive presentation. Will be projected, screen-shared, and viewed in PDF. All numbers and labels must be 100% readable at full resolution and at half-zoom.

CONSTRAINTS:
- Style commitment: clean information design. Flat colors. Typography-driven. Not an illustration. Not a stylized infographic with mascots or scenes. Not a UI screenshot.
- Brand palette: primary [HEX], secondary [HEX], accent [HEX], surface [HEX], text [HEX]. Use exactly these hex values.
- Typography: single sans-serif family. Title weight: bold, ~28pt-equivalent. Body and bullet text: regular, ~16pt-equivalent. Numbers: tabular figures.
- EXACT TEXT — every quoted string above renders verbatim with no extra characters, no punctuation drift, no rounding of numbers, no smoothing of data.
- Chart data discipline: render the values exactly as provided. Do not smooth, interpolate, or "make the chart look better." If a value is 23.7, render 23.7 — not 24.
- Forbidden: decorative illustrations, mascots, stock-photo backgrounds, gradients, drop shadows, lorem ipsum, invented bullet copy, additional text beyond what's listed.
- Format: 2560×1440, 16:9 landscape.

If any chart value is rounded, smoothed, or reordered, the output is incorrect. If any quoted string has a typo or extra character, the output is incorrect.
```

---

## Iteration Plan

1. "Tighten the chart's left margin — give the y-axis labels [more / less] room."
2. "Move the key metric callout from above the chart to overlay the highlighted data point."
3. "The accent hex is too saturated — use [refined hex] for the highlighted data point only."

---

## False-Positive Prevention

❌ **DON'T:**
- Assume the canvas is 16:9 because the prompt text says "16:9 presentation slide" — the API `size` decides the canvas; check it is `2560x1440` (or another exact 16:9 size), since a 3:2 size such as `1536x1024` letterboxes or stretches in a 16:9 deck.
- Pass the chart because every value label is verbatim — the model can print "23.7" on a bar drawn taller than the "31.2" bar, or start a bar axis above zero without labeling it.
- Judge "readable at half-zoom" on the full-resolution file — axis labels and footer text at ~16pt-equivalent on a 1440-px-tall slide can blur out when projected or shrunk in a PDF thumbnail.
- Let `[KEY METRIC]` and `[CHART DATA]` disagree — a "+18% QoQ" callout over bars showing a 12% change passes every EXACT TEXT check.

✅ **DO:**
- Measure each bar or point: pixel height ÷ value should be constant across the series (within ~5%); any outlier is a mis-drawn value even if its label is right.
- Recompute the key metric from the chart data supplied (e.g., percent change between the last two values) before generation; if it cannot be derived, ask the user for its source instead of rendering it.
- View the slide at 50% scale and confirm the smallest axis label and footer still read; if not, cut labels or bullets rather than shrinking text further.

---

## Verification

- [ ] EXACT TEXT for title, metric, chart labels, bullets, footer.
- [ ] Chart data values listed verbatim, in order.
- [ ] No invented data or smoothed values.
- [ ] All five hex codes (primary, secondary, accent, surface, text) provided.
- [ ] `quality="high"`.
- [ ] Failure conditions stated for rounded/smoothed values.
