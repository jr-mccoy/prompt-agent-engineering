---
title: "GPT Image 2 — Verbatim In-Image Marketing Copy"
category: image-generation/marketing
description: "Marketing visual where the headline, subhead, and CTA must be 100% verbatim — leveraging gpt-image-2's 95%+ text rendering accuracy."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
difficulty: intermediate
tags:
  - gpt-image-2
  - marketing
  - text-rendering
  - typography
  - openai
updated: "2026-05-05"
related_prompts:
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
  - domain-image-generation/gpt-image-2/gptimage2_advertising_creative_brief.md
---

# GPT Image 2 — Verbatim In-Image Marketing Copy

**Objective:** Generate a marketing image where every word of in-image text — headline, subhead, CTA, badge — is rendered exactly as specified, with locked typography, color, and placement.

**API parameters (required):**
- `model="gpt-image-2"`
- `size="1080x1080"` (IG square — but use 1024x1024 since 1080 is not multiple of 16) → use `1024x1024`. For story / reels: `1024x1536`. For banners: `1536x1024`.
- `quality="high"` (required; non-negotiable)
- `n=1` or `n=2`

**Note on dimensions:** gpt-image-2 requires multiples of 16. If you target IG's 1080×1080, use 1024×1024 and let downstream tooling resize.

---

## Inputs

- `[BACKGROUND]` — what's behind the text (a photo, a solid color, a soft gradient, a product, a scene)
- `[HEADLINE]` — verbatim, including any punctuation
- `[SUBHEAD]` — verbatim (optional)
- `[CTA]` — verbatim button or link copy (optional)
- `[BADGE/TAG]` — verbatim corner badge (optional, e.g., "LIMITED EDITION")
- `[FONT FAMILY]` — serif / sans-serif / display / monospace
- `[BRAND PALETTE]` — hex codes for text and accent
- `[NEGATIVE-SPACE ZONE]` — where the headline lives ("upper-left third", "centered horizontally on lower third")

---

## Constraints (Must / Must Not)

**Must:**
- `quality="high"`.
- Wrap every quoted string in EXACT TEXT with full typography spec.
- Specify hex colors, not "white" or "dark grey".
- Lock the negative-space zone for the headline so background doesn't compete.
- Spell hard or non-English words letter-by-letter (e.g., "Kløver: K-L-O-with-stroke-V-E-R").

**Must Not:**
- Allow the model to "improve" copy — render verbatim.
- Use slop quality boosters.
- Add decorative typography effects (3D, neon glow, drop shadows) unless explicitly briefed.

---

## Production Prompt

```
SCENE:
[BACKGROUND]. The composition leaves a quiet, low-contrast zone in the [NEGATIVE-SPACE ZONE] sized to hold the headline.

SUBJECT:
The headline is the hero of the frame. The eye lands there first.

KEY DETAILS:
- Background composition: visually quiet in the negative-space zone, with the rest of the frame supporting the message but not competing.
- Hierarchy: headline → subhead → CTA → badge. Each element steps down in size and weight.
- Typography family: [FONT FAMILY]. No mixing.

USE CASE:
Marketing creative for [IG square / story / banner / billboard / web hero]. Will be viewed at full size. All copy must be 100% readable at full resolution.

CONSTRAINTS:
- Style commitment: clean editorial-grade marketing typography.
- EXACT TEXT (verbatim — render every quoted string exactly, with no extra characters, no punctuation drift, no inserted line breaks unless I specify them):
  - HEADLINE: "[HEADLINE]" — [FONT FAMILY] [bold/regular/light], [hex color e.g., #1A1A1A], placed in the [NEGATIVE-SPACE ZONE], occupying ~12–18% of canvas height. 100% readable at full resolution.
  - SUBHEAD (if present): "[SUBHEAD]" — [FONT FAMILY] regular, [hex color, typically lighter than headline], directly below headline at ~5% canvas height.
  - CTA (if present): "[CTA]" — [hex text color] on [hex background color] pill button, [FONT FAMILY] medium, placed [location].
  - BADGE (if present): "[BADGE]" — [FONT FAMILY] bold uppercase, [hex color], small (~3–4% canvas height), placed in [corner].
- Letter-by-letter spelling for any non-English / hard-to-render words: [list any].
- Preserve: the negative-space zone behind the headline must remain visually quiet — no busy texture, no high-contrast shapes intruding into it.
- Forbidden: 3D type, neon glows, heavy drop shadows on text, lens flares on text, additional copy beyond what's listed above, watermarks, lorem ipsum.
- Format: [size], [orientation].

Render the typography contract exactly. If any quoted string has a typo, has an extra character, has a missing accent or diacritic, or extends outside its specified zone, the output is incorrect.
```

---

## Iteration Plan

1. "The headline is reading too small — push it to ~16% canvas height."
2. "Tighten the negative-space zone — there's too much background bleed into the headline."
3. "The CTA pill is the wrong color — use the brand secondary [HEX] background instead."

---

## Verification

- [ ] Every visible string in EXACT TEXT.
- [ ] Hex colors for every text element.
- [ ] Typography family stated, no mixing.
- [ ] Negative-space zone described by location AND size.
- [ ] Letter-by-letter spelling for any hard words.
- [ ] `quality="high"`.
- [ ] Failure conditions stated for typos.
