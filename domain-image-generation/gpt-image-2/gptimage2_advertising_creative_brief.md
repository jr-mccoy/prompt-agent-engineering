---
title: "GPT Image 2 — Advertising Creative Brief"
category: image-generation/advertising
description: "Campaign-grade ad image briefed as a creative brief, with verbatim copy and constrained taste decisions."
techniques:
  - ST-01
  - ST-02
  - SV-13
  - SV-17
difficulty: advanced
tags:
  - gpt-image-2
  - advertising
  - campaign
  - creative-brief
  - openai
updated: "2026-05-05"
related_prompts:
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
  - domain-advertising/
---

# GPT Image 2 — Advertising Creative Brief

**Objective:** Brief gpt-image-2 like an agency creative director — give it a brand, audience, cultural moment, concept, and exact copy, then let it make taste-driven decisions inside the boundaries.

**API parameters (recommended):**
- `model="gpt-image-2"`
- `size="1536x1024"` (landscape — most ad placements) or `1024x1536` (portrait — IG/TikTok stories)
- `quality="high"` (required; copy must be verbatim)
- `n=2` or `n=4` for creative pool

---

## Inputs

- `[BRAND]` — name and one-line identity ("a Japanese craft tea co-op")
- `[AUDIENCE]` — concrete persona ("urban 28–35 home cooks who shop at specialty grocers")
- `[CULTURAL MOMENT]` — what's true in the world right now ("late spring; first warm weekend; people opening windows")
- `[CONCEPT]` — the idea in one sentence ("the ritual of the first iced tea of the year")
- `[HEADLINE]` — verbatim copy
- `[SUBHEAD]` — verbatim copy (optional)
- `[CTA]` — verbatim button/link copy (optional)
- `[BRAND PALETTE]` — hex codes
- `[FORBIDDEN]` — competitor signals, off-brand aesthetics

---

## Constraints (Must / Must Not)

**Must:**
- Read like a creative brief, not an asset description.
- Place verbatim copy under EXACT TEXT with full typography spec.
- State the cultural moment so the model can ground composition in it.
- Allow taste decisions inside the brief (composition, lighting nuance, gesture) — but lock copy, palette, and forbidden zones.

**Must Not:**
- Use celebrity likenesses without explicit reference images and rights.
- Render trademarked logos of brands not the client.
- Use slop hype words.
- Add invented copy.

---

## Production Prompt

```
CREATIVE BRIEF:

Brand: [BRAND].
Audience: [AUDIENCE].
Cultural moment: [CULTURAL MOMENT].
Concept: [CONCEPT].
Tone: [3 adjectives — e.g., "warm, unhurried, slightly nostalgic"].
Format: [single still image / hero ad / IG portrait / billboard].

SCENE:
Build the scene around the concept. The setting should feel inhabited — not staged. Lighting should feel like the cultural moment described.

SUBJECT:
[The hero of the frame — product, person, gesture, or scene element]. Place it so the eye lands there first; the headline second.

KEY DETAILS:
- Brand palette: primary [HEX], secondary [HEX], accent [HEX]. The accent should appear sparingly — one or two touches, not a wash.
- Texture: real materials, real wear. No studio-perfect surfaces.
- Composition: leave a clean negative-space zone in the [upper-left / upper-right / lower-third] for the headline. The zone should be at least 25% of the canvas and visually quiet (no busy texture in that area).
- Hand and human details (if people are in frame): natural, unposed; gaze not at camera unless concept demands.

USE CASE:
Campaign-grade [hero ad / billboard / social hero / OOH]. The image runs at full size and is the primary surface where the headline lives.

CONSTRAINTS:
- Style commitment: photorealistic editorial photography, [film stock or lighting reference, e.g., "shot on Kodak Gold 200, soft window light"].
- EXACT TEXT (verbatim, no extra characters):
  - Headline: "[HEADLINE]" — [serif/sans/display], [weight], [hex color], placed in the [upper-left/upper-right/lower-third] zone, occupying ~10–15% of the canvas height. 100% readable at full resolution.
  - Subhead (if present): "[SUBHEAD]" — [smaller weight/size], [hex color], directly under the headline.
  - CTA (if present): "[CTA]" — [button style or plain text], [hex color and background], placed [location].
- Preserve: the negative-space zone behind the headline must remain visually quiet.
- Forbidden: competitor logos, [FORBIDDEN], stock-photo cliché compositions (handshake, pointing-at-laptop, generic "happy team"), watermarks, lorem ipsum, additional copy beyond what is listed above.
- Format: [size], [orientation].

If any of the headline/subhead/CTA copy is misspelled, has extra characters, or extends outside the negative-space zone, the output is incorrect.
```

---

## Iteration Plan

1. "Strengthen the cultural moment — the [season / time of day / weather] needs to feel more present."
2. "Tighten the headline zone — too much busy texture is bleeding into it. Make the upper-left more uniform."
3. "Push the accent color [further / less] — currently appearing in [N] places, target [M]."

---

## Verification

- [ ] Reads like a creative brief, not a render description.
- [ ] EXACT TEXT block for every piece of copy.
- [ ] Negative-space zone for headline specified by location and size.
- [ ] Brand palette in hex codes.
- [ ] Forbidden zone includes competitor logos and stock-photo clichés.
- [ ] `quality="high"`.
