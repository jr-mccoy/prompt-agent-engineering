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
updated: "2026-10-06"
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

## False-Positive Prevention

❌ **DON'T:**
- Count `n=4` as four design directions because four files came back — variations that differ only in color or wordmark weight are one concept, not four.
- Treat "readable at favicon size (32×32 px)" as satisfied because the prompt says it — the model renders at 1024×1024 and never sees the small size.
- Certify the wordmark from one correct output; each of the four images spells "[BRAND NAME]" independently, and an icon substituted for a letter (a bean for the "O") can make the word read differently.
- Read "original, non-infringing" in the brief as clearance — a simple geometric mark can still sit close to a registered mark in the same category.

✅ **DO:**
- Downscale every variation to 32×32 and 16×16 and reject any whose silhouette or wordmark stops reading.
- Proofread the wordmark in each of the four outputs letter by letter against the `[BRAND NAME]` input, and measure padding: the logo's bounding box leaves at least 154 px (15% of 1024) clear on every side.
- Before a variation goes on the shortlist, run a reverse-image and trademark-register search in the brand's category; if not done, label it "clearance not checked" rather than presenting it as usable.

---

## Verification

- [ ] Brand name spelled in EXACT TEXT block.
- [ ] Personality is 3 concrete adjectives, not vague hype.
- [ ] Forbidden list includes both user-specific avoids AND generic trademark avoids.
- [ ] `quality="high"` and `n=4`.
- [ ] Padding requirement stated (at least 15% on all sides).
- [ ] Favicon-size legibility requirement stated.
