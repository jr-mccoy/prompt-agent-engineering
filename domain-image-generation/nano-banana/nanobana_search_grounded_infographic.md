---
title: "Nano Banana Pro — Search-Grounded Infographic"
category: image-generation/infographic
description: "Generate a data-driven infographic where Nano Banana Pro's Google Search grounding verifies facts and data in real time."
techniques:
  - ST-01
  - ST-02
  - SV-12
  - SV-17
  - SV-18
difficulty: intermediate
tags:
  - nano-banana
  - nano-banana-pro
  - infographic
  - search-grounding
  - data-visualization
  - google
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/NANO_BANANA_GUIDE.md
  - domain-image-generation/gpt-image-2/gptimage2_dense_text_infographic.md
---

# Nano Banana Pro — Search-Grounded Infographic

**Objective:** Generate a publication-quality infographic where data values, statistics, and factual claims are verified against current information via Google Search grounding. The model can ground against real-time data rather than relying on stale training data.

**Why Nano Banana Pro:** Near-perfect text rendering, Google Search grounding for factual accuracy, full LLM reasoning before generation, and exact font specification. This is the differentiator — gpt-image-2 has web search during generation, but Nano Banana Pro's search grounding is explicitly positioned for factual data visualizations.

**API parameters:**
- `model="gemini-3-pro-image"`
- `quality="high"` (required for text-heavy outputs)
- `tools=[{"google_search": {}}]` (enables search grounding)
- `n=1`

---

## Inputs

- `[TOPIC]` — the subject of the infographic
- `[DATA POINTS]` — specific metrics, rankings, or statistics to display (or "use current data via search")
- `[AUDIENCE]` — who will read this (executives, students, general public, domain experts)
- `[FORMAT]` — vertical (9:16 mobile), horizontal (16:9 presentation), square (1:1 social)
- `[BRAND PALETTE]` — hex codes for primary, secondary, accent, background, text colors
- `[FONT STACK]` — title font, body font (Nano Banana Pro renders named fonts)
- `[SOURCE ATTRIBUTION]` — how to credit data sources

---

## Constraints (Must / Must Not)

**Must:**
- Use Google Search grounding to verify all data values.
- All text must be legible at the target display size.
- Include source attribution for grounded data.
- Use exact fonts specified in the font stack.
- Follow the stated visual hierarchy (title > section headers > data > body > source).

**Must Not:**
- Use placeholder or fabricated data when search grounding is enabled.
- Render data values that cannot be verified — flag uncertainties.
- Use decorative elements that don't convey information.
- Mix more than 3 font weights in one infographic.
- Use gradients or 3D effects unless specifically requested.

---

## Production Prompt

```
TASK: Create a data-driven infographic about [TOPIC].
Use Google Search grounding to verify all data values against current sources.

FORMAT: [FORMAT] — [dimensions or aspect ratio].

LAYOUT:
- Title bar: top [15-20]% of canvas.
- Data sections: [N] sections stacked below, each ~[percentage]% height.
- Source attribution: bottom [5]% strip.
- Margins: [generous / tight] — at least [Npx] on all sides.

DATA SECTIONS:
Section 1: [METRIC NAME]
- Display: large number ([font], [size], [color hex]), subtitle below, [chart type if any].
- Data: [specific value OR "verify via search grounding"].

Section 2: [METRIC NAME]
- Display: [layout description].
- Data: [specific value OR "verify via search grounding"].

Section 3: [COMPARISON / TREND]
- Display: [chart type — bar / line / pie / comparison].
- Data: [values OR "use current data via search"].

[Additional sections as needed.]

TYPOGRAPHY:
Title: "[EXACT TITLE TEXT]" in [TITLE FONT] [weight], [size], [color hex].
Section headers: [FONT] [weight], [size], [color hex].
Data numbers: [FONT] [weight], [size], [color hex].
Body text: [FONT] [weight], [size], [color hex].
Source line: [FONT] Italic, [size], [color hex].

COLOR PALETTE:
Primary: [hex] — used for [what].
Secondary: [hex] — used for [what].
Accent: [hex] — used for [what].
Background: [hex].
Text: [hex].

STYLE:
[Clean / modern / editorial / corporate / playful].
[Flat design — no 3D, no gradients, no drop shadows] OR [specific style direction].

DATA VERIFICATION:
Use search grounding to verify every data value displayed.
If a value cannot be verified, display "[VERIFY]" instead of fabricating.
Include the data source in the attribution bar.

SOURCE ATTRIBUTION:
"Sources: [source names]" in [font], [size], [color], bottom of canvas.

CONSTRAINTS:
- MUST: All data values legible at [target display size]
- MUST: Source attribution visible and readable
- MUST: Visual hierarchy follows Title > Sections > Data > Body > Sources
- MUST NOT: Decorative elements that don't convey information
- MUST NOT: Placeholder or unverified data (use search grounding or flag [VERIFY])
- MUST NOT: More than 3 font weights total
- Quality: "high"
```

---

## Example: Technology Market Infographic

```
TASK: Create a data-driven infographic about the top 5 AI image generation
platforms by market adoption in 2026.
Use Google Search grounding to verify all data values.

FORMAT: Vertical 9:16 for mobile/social.

LAYOUT:
- Title bar: top 18%.
- 5 ranked entries: each 14% height, horizontal bar chart format.
- Insight callout: 8% height.
- Source attribution: bottom 4%.

DATA SECTIONS:
Rank each platform by estimated monthly active users or API call volume.
Use search grounding for current data. If exact numbers unavailable,
use relative rankings with "[approximate]" flag.

TYPOGRAPHY:
Title: "AI Image Generation: Market Leaders 2026" in Inter Bold, 32pt, #FFFFFF on #1E293B.
Platform names: Inter SemiBold, 18pt, #1E293B.
Data values: Inter Bold, 24pt, #2563EB.
Body text: Source Sans Pro Regular, 12pt, #475569.
Source line: Source Sans Pro Italic, 9pt, #94A3B8.

COLOR PALETTE:
Primary: #2563EB (data bars). Secondary: #F59E0B (highlights).
Background: #F8FAFC. Text: #1E293B. Muted: #94A3B8.

STYLE:
Clean, modern, corporate. Flat design — no 3D, no gradients.
Horizontal bar chart with rounded ends, 8px bar height.

CONSTRAINTS:
- MUST: All platform names and values legible on a phone screen
- MUST: Bars proportional to actual data (not decorative)
- MUST: Source attribution readable
- MUST NOT: Fabricated adoption numbers
- Quality: "high"
```

---

## Iteration Plan

1. "The data value for [platform] seems outdated — re-verify via search grounding and update."
2. "Section 3's chart labels overlap — increase spacing or reduce font size."
3. "The source attribution is too small to read on mobile — increase to 10pt minimum."
4. "The color contrast between data bars and background fails WCAG AA — darken the bar color."

---

## Verification

- [ ] All data values verified via search grounding (no fabricated numbers).
- [ ] Source attribution present and readable.
- [ ] Visual hierarchy is clear (title → sections → data → body → sources).
- [ ] All text legible at target display size.
- [ ] Named fonts rendered correctly.
- [ ] Color palette matches specification (check hex codes).
- [ ] No decorative elements that don't convey information.
- [ ] Chart/graph proportions accurately reflect the data.
- [ ] `quality="high"` set.
