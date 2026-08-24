---
title: "GPT Image 2 — Logo Batch Variations"
category: image-generation/branding
description: "Generate 4 logo variations from a brand brief using gpt-image-2's n parameter."
techniques:
  - ST-01
  - ST-02
  - SV-13
  - SV-17
difficulty: intermediate
tags:
  - gpt-image-2
  - logo
  - branding
  - batch-generation
  - openai
updated: "2026-05-05"
related_prompts:
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
  - domain-image-generation/branding/visual-identity
---

# GPT Image 2 — Logo Batch Variations

**Objective:** Brief gpt-image-2 like a designer to produce **4 distinct logo variations** in a single API call using `n=4`.

**API parameters (required):**
- `model="gpt-image-2"`
- `size="1024x1024"` (square; provides clean centered logo with padding)
- `quality="high"` (always; logos must be sharp and the wordmark verbatim)
- `n=4`
- `background="opaque"` if you want a clean white background for downstream use

---

## Inputs

- `[BRAND NAME]` — exact spelling (used for the wordmark)
- `[CATEGORY]` — what the brand sells / does
- `[AUDIENCE]` — primary target user
- `[PERSONALITY]` — 3 adjectives (e.g., "warm, simple, timeless")
- `[USE CASE]` — where the logo lives (app icon, storefront sign, packaging, business card)
- `[VIBE REFERENCE]` — optional: brand category to evoke (e.g., "feels like a 1970s Italian café")
- `[FORBIDDEN]` — anything to explicitly avoid (e.g., "no coffee bean iconography", "no leaves")

---

## Constraints (Must / Must Not)

**Must:**
- Brief the model like a designer (brand → audience → personality → use case), not as a rendering description.
- Render the brand wordmark verbatim with the text-rendering contract.
- Request "clean, vector-like shapes, strong silhouette, balanced negative space".
- Center the logo with generous padding for downstream cropping.

**Must Not:**
- Generate trademarked elements or logos that mimic existing brands (Nike swoosh, Apple bite, etc.).
- Use slop quality boosters ("best logo", "award-winning").
- Render decorative slogans or taglines unless explicitly provided.
- Use gradients or 3D effects unless the personality specifically calls for them.

---

## Production Prompt

```
DESIGN BRIEF:
Brand: [BRAND NAME].
Category: [CATEGORY].
Audience: [AUDIENCE].
Personality: [PERSONALITY].
Primary use case: [USE CASE].
Vibe reference (mood, not visual copying): [VIBE REFERENCE].

DELIVERABLE:
A single, original, non-infringing logo for [BRAND NAME]. Centered in the frame with generous padding on all sides. Clean, vector-like shapes — no photographic elements, no 3D rendering, no gradients (unless the personality demands one — and even then, two-stop only).

KEY DETAILS:
- Wordmark renders the brand name exactly: "[BRAND NAME]".
- Strong silhouette readable at favicon size (32×32 px).
- Balanced negative space — the logo should still feel composed when shrunk.
- Color palette: [if specified, hex codes; otherwise: a constrained 2-color palette with high contrast].
- Mark + wordmark relationship: [if specified: "icon to the left of the wordmark" / "icon above" / "wordmark only"].

USE CASE:
Brand identity for [USE CASE]. The logo should feel [PERSONALITY].

CONSTRAINTS:
- Style commitment: clean vector-style logo, not photographic, not 3D, not illustrative.
- EXACT TEXT (the wordmark, verbatim, no extra characters): "[BRAND NAME]" — render in a [serif / sans-serif / display / monospace] face that fits the personality. The wordmark must be 100% readable at full resolution and at favicon size.
- Forbidden: trademarked iconography (no swooshes, no apple silhouettes, no recognizable brand marks); also forbidden: [FORBIDDEN].
- Forbidden: photographic elements, 3D rendering, drop shadows, glossy bevels, watermarks, taglines (unless provided).
- Format: square 1024×1024, single centered logo with at least 15% padding on all sides.

If the wordmark is misspelled or extends to the edge of the canvas, the output is incorrect.
```

API call:

```python
client.images.generate(
    model="gpt-image-2",
    prompt=PROMPT,
    size="1024x1024",
    quality="high",
    n=4,
    background="opaque",
)
```

---

## Iteration Plan

1. "Variation 2 was closest — push it more [minimal / decorative / geometric]. Drop the [specific element]."
2. "Use a [serif / sans / display] wordmark instead of the current face."
3. "Tighten the negative space between the icon and the wordmark by ~20%."

---

## Verification

- [ ] Brand name spelled in EXACT TEXT block.
- [ ] Personality is 3 concrete adjectives, not vague hype.
- [ ] Forbidden list includes both user-specific avoids AND generic trademark avoids.
- [ ] `quality="high"` and `n=4`.
- [ ] Padding requirement stated (at least 15% on all sides).
- [ ] Favicon-size legibility requirement stated.
