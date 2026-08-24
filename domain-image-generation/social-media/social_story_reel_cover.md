---
title: "Social — Story / Reel Cover (9:16 Vertical)"
category: image-generation/social
description: "Vertical 9:16 story or reel cover with a thumb-stopping hook, safe-zone-aware layout, and verbatim text that survives UI overlays."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - SV-13
  - SV-15
  - SV-17
difficulty: intermediate
tags:
  - social-media
  - story
  - reel
  - vertical
  - 9-16
  - cover
  - safe-zone
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/social-media/README.md
  - domain-image-generation/social-media/social_announcement_post.md
  - domain-image-generation/social-media/social_carousel_set.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# Social — Story / Reel Cover (9:16 Vertical)

**Objective:** Generate a vertical 9:16 story/reel cover with a thumb-stopping hook, composed for the platform's safe zones (the center band stays clear of top/bottom UI chrome), with verbatim text that remains legible over the design and survives platform overlays.

**Why the 9:16 + safe-zone discipline matters:** Stories/reels are full-bleed vertical. Platform UI (profile, caption, action buttons, progress bar) eats the top ~14% and bottom ~20%. Critical text and the focal subject must live in the central safe band or they get covered.

**Why gpt-image-2 (primary):** gpt-image-2 supports the tall vertical ratio and gives precise layout control to keep the hook inside the safe band while filling the full 9:16 frame edge-to-edge. With `quality="high"` it renders the hook text reliably (95%+). Use it for the hero cover.

**Why Nano Banana Pro (alternate):** When the hook is text-heavy or multilingual, or you want exact font control and a unified look across a series of reel covers, `gemini-3-pro-image` gives near-perfect text and **system-prompt** style locking across a set. Also strong for extreme/tall ratios.

> Use Nano Banana 2 (`gemini-3.1-flash-image`) only to screen background/composition options at 512px — not for the final text-bearing cover.

**API parameters:**

gpt-image-2 (primary):
- `model="gpt-image-2"`
- `size="1024x1536"` (closest portrait; export/resize to 1080×1920 for the platform) — request the tallest vertical the API supports
- `quality="high"`
- `n=4` to explore hooks/compositions

Nano Banana Pro (alternate — text-heavy / series):
- `model="gemini-3-pro-image"`
- `size="1080x1920"` (true 9:16) or nearest supported
- `quality="high"`
- `n=2`

---

## Inputs

- `[HOOK TEXT]` — the thumb-stopping hook, verbatim (short — 3–8 words)
- `[SUBHOOK]` — optional second line, verbatim (or "none")
- `[CONTENT TYPE]` — reel cover / story highlight cover / promo story
- `[BACKGROUND]` — photo/scene description / solid / gradient / product
- `[FOCAL SUBJECT]` — the main visual (person, product, illustration) — must sit in the safe band
- `[BRAND PALETTE]` — text hex, accent hex, overlay/scrim treatment
- `[FONT CHARACTER]` — bold, legible-at-distance font character
- `[LOGO/HANDLE]` — placement (within safe band)

---

## Constraints (Must / Must Not)

**Must:**
- Compose for true 9:16 vertical, full-bleed (image fills the entire frame).
- Keep all critical text and the focal subject inside the central safe band — clear of the top ~14% and bottom ~20% reserved for platform UI.
- Render `[HOOK TEXT]` (and `[SUBHOOK]`) 100% verbatim, large and legible at a glance.
- Use a scrim/overlay or high-contrast placement so text stays readable over the background.
- Make the hook thumb-stopping — strong contrast, bold type, immediate read.

**Must Not:**
- Place critical text or the focal subject in the top/bottom UI zones.
- Render the design at the wrong aspect ratio (square or landscape).
- Paraphrase, truncate, or invent the hook; no lorem ipsum.
- Let text disappear into a busy background (always ensure contrast/scrim).
- Crowd the cover — one hook, one focal subject.

---

## Production Prompt — gpt-image-2 (Primary)

```
SCENE:
A full-bleed vertical 9:16 [CONTENT TYPE] cover. Background: [BACKGROUND], filling the entire tall frame edge to edge. [If photo/scene: describe lighting and mood.] Apply a subtle scrim/overlay where the hook text sits so the text stays legible.

SUBJECT:
[FOCAL SUBJECT] composed within the central safe band of the frame (clear of the top ~14% and bottom ~20%, which are reserved for platform UI). The hook text is the dominant element, large and bold, also within the safe band.

KEY DETAILS:
- Hook font character: [FONT CHARACTER], bold and legible at a glance from a distance.
- Text color: [text hex]; accent: [accent hex]. Use exact hex; ensure strong contrast against the background via [scrim/overlay/placement].
- Small [LOGO/HANDLE] placed inside the safe band.

EXACT TEXT (verbatim):
HOOK: "[HOOK TEXT]"
SUBHOOK: "[SUBHOOK]"
HANDLE/LOGO: "[LOGO/HANDLE]"

USE CASE:
Vertical story/reel cover. Posted full-screen; platform UI overlays the top and bottom, so keep critical elements centered.

CONSTRAINTS:
- Style commitment: thumb-stopping vertical social cover. Bold, high-contrast, immediate.
- Critical text and focal subject MUST stay within the central safe band — nothing important in the top ~14% or bottom ~20%.
- EXACT TEXT verbatim as above; forbidden: paraphrase, truncation, invented/lorem-ipsum text.
- Forbidden: wrong aspect ratio (must be 9:16 vertical), text lost in a busy background, crowding.
- Format: vertical 9:16 (1080×1920 target).

If the aspect ratio is not 9:16, if critical text sits in the UI zones, or if the hook differs from the text above, the output is INCORRECT.
```

---

## Production Prompt — Nano Banana Pro (Alternate / Series)

```
SYSTEM PROMPT (for a series of reel covers — apply identically to each):
Produce full-bleed vertical 9:16 reel covers in a consistent look: [FONT CHARACTER] hook type, text [text hex], accent [accent hex], with a subtle scrim behind the hook. Keep critical text and the focal subject within the central safe band (clear of top ~14% and bottom ~20% UI zones). [LOGO/HANDLE] at [position] inside the safe band. Render all copy verbatim.

TASK:
Create a [CONTENT TYPE] cover. Background: [BACKGROUND], full-bleed. Focal subject: [FOCAL SUBJECT], centered in the safe band. Hook dominant and legible at a glance.

EXACT TEXT (verbatim):
HOOK: "[HOOK TEXT]"
SUBHOOK: "[SUBHOOK]"

CONSTRAINTS:
- MUST: true 9:16 full-bleed; critical text + subject in central safe band; verbatim hook; high contrast via scrim.
- MUST NOT: place critical elements in UI zones, use wrong aspect ratio, paraphrase/invent the hook, or lose text in the background.
- If the aspect ratio is not 9:16 or the hook differs from the text above, the output is INCORRECT.
- Quality: "high"
```

---

## Iteration Plan

1. "The hook is too close to the top — move it down into the central safe band, clear of the top 14%."
2. "The image came out square — re-render as a true full-bleed 9:16 vertical."
3. "The hook is hard to read over the photo — add/strengthen the scrim behind it and boost contrast."
4. "The focal subject is in the bottom UI zone — raise it into the safe band."
5. "The hook lost a word — re-render verbatim: \"[HOOK TEXT]\"."

---

## Verification

- [ ] True 9:16 vertical, full-bleed (fills the frame).
- [ ] Critical text and focal subject inside the central safe band (clear of top ~14% / bottom ~20%).
- [ ] `[HOOK TEXT]` and `[SUBHOOK]` rendered 100% verbatim.
- [ ] Hook is bold, large, legible at a glance.
- [ ] Scrim/overlay or contrast keeps text readable over the background.
- [ ] Exact hex colors applied.
- [ ] One hook, one focal subject — not crowded.
- [ ] `quality="high"` set (mandatory for text).
