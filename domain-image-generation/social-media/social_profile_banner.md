---
title: "Social — Profile / Header Banner"
category: image-generation/social
description: "Profile/header banner (LinkedIn, X, YouTube, Facebook) composed for each platform's exact dimensions and avatar/UI safe zones with verbatim text."
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
  - banner
  - header
  - profile
  - linkedin
  - x-twitter
  - youtube
  - safe-zone
  - gpt-image-2
  - nano-banana-pro
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/social-media/README.md
  - domain-image-generation/social-media/social_quote_graphic.md
  - domain-image-generation/social-media/social_announcement_post.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# Social — Profile / Header Banner

**Objective:** Generate a wide profile/header banner sized to a specific platform's exact dimensions, composed around that platform's avatar overlap and responsive-crop safe zones, with any tagline/text rendered verbatim and kept inside the visible area on both desktop and mobile.

**Why platform dimensions + safe zones matter:** Each platform uses a different banner ratio and crops it differently across devices. The avatar overlaps a corner; mobile crops the sides or top/bottom. Text and the focal element must live in the universally visible central safe zone, or they get covered or cropped.

**Why gpt-image-2 (primary):** gpt-image-2 handles wide landscape ratios (up to 3:1) and gives precise control to keep the focal subject and tagline inside the safe zone while filling the full banner. `quality="high"` keeps a tagline crisp (95%+). Use it for the hero banner.

**Why Nano Banana Pro (alternate):** For text-heavy banners, multilingual taglines, or exact font/brand control across a set of platform banners, `gemini-3-pro-image` offers near-perfect text and system-prompt style locking. Use it when typography is central or you're producing a matched set across platforms.

> Nano Banana 2 (`gemini-3.1-flash-image`) is useful only for screening background/composition options at low cost — not the final text-bearing banner.

**Platform dimensions (verify current platform specs before production):**

| Platform | Banner size | Ratio | Safe-zone note |
|----------|-------------|-------|----------------|
| LinkedIn (personal) | 1584×396 | 4:1 | Avatar overlaps lower-left; keep text center/right |
| LinkedIn (company) | 1128×191 | ~5.9:1 | Logo overlaps left; very short height |
| X / Twitter | 1500×500 | 3:1 | Avatar overlaps lower-left; bottom band may be UI |
| YouTube channel art | 2560×1440 | 16:9 | TV-safe text/logo area is center 1546×423 |
| Facebook page | 1640×856 (renders ~820×312 desktop) | ~1.9:1 | Mobile crops sides; keep content centered |

**API parameters:**

gpt-image-2 (primary):
- `model="gpt-image-2"`
- `size` = nearest supported wide ratio to the target (e.g., `1536x512`-class for 3:1); export/resize to exact platform dimensions
- `quality="high"`
- `n=4` to explore compositions

Nano Banana Pro (alternate):
- `model="gemini-3-pro-image"`
- `size` = nearest supported to target dimensions
- `quality="high"`
- `n=2`

---

## Inputs

- `[PLATFORM]` — LinkedIn / X / YouTube / Facebook (sets dimensions + safe zone)
- `[TAGLINE]` — verbatim banner text (short — name, role, value prop, or "none")
- `[FOCAL ELEMENT]` — logo / portrait / product / abstract motif (must sit in safe zone)
- `[BACKGROUND]` — scene/photo description / solid / gradient / pattern
- `[BRAND PALETTE]` — background hex, text hex, accent hex
- `[FONT CHARACTER]` — tagline font character
- `[AVATAR CORNER]` — which corner the avatar overlaps (so you keep it clear)

---

## Constraints (Must / Must Not)

**Must:**
- Compose to the exact `[PLATFORM]` ratio and fill the full banner edge-to-edge.
- Keep the `[FOCAL ELEMENT]` and all text inside the platform's central safe zone (clear of the avatar overlap and responsive-crop margins).
- Leave the `[AVATAR CORNER]` clear of critical content.
- Render `[TAGLINE]` 100% verbatim, legible at banner scale, high contrast.
- Balance the composition so it reads on both desktop (full width) and mobile (cropped sides).

**Must Not:**
- Place text or the focal element under the avatar overlap or in the crop-risk margins.
- Use the wrong aspect ratio for the platform.
- Paraphrase, truncate, or invent the tagline; no lorem ipsum.
- Let text lose contrast against a busy background.
- Crowd the banner — banners are wide and shallow; one clear focal idea.

---

## Production Prompt — gpt-image-2 (Primary)

```
SCENE:
A wide [PLATFORM] profile/header banner at its exact ratio, full-bleed edge to edge. Background: [BACKGROUND], filling the entire wide frame. Apply a scrim/contrast treatment behind any text so it stays legible.

SUBJECT:
[FOCAL ELEMENT] placed inside the platform's central safe zone. The [AVATAR CORNER] is left clear of any critical content (the user's avatar overlaps there). Optional tagline within the safe zone.

KEY DETAILS:
- Tagline font character: [FONT CHARACTER], legible at banner scale.
- Text color [text hex], accent [accent hex], background [background hex]. Use exact hex; ensure strong contrast.
- Composition balances for desktop full-width AND mobile (sides may crop) — keep content centered.

EXACT TEXT (verbatim):
TAGLINE: "[TAGLINE]"

USE CASE:
[PLATFORM] profile/header banner. Avatar overlaps the [AVATAR CORNER]; the banner is cropped differently on mobile vs desktop, so critical content stays in the central safe zone.

CONSTRAINTS:
- Style commitment: clean designed brand banner.
- Focal element and all text MUST stay in the central safe zone; the [AVATAR CORNER] stays clear; no critical content in responsive-crop margins.
- EXACT TEXT verbatim as above; forbidden: paraphrase, truncation, invented/lorem-ipsum text.
- Forbidden: wrong aspect ratio for [PLATFORM], low-contrast text, crowding.
- Format: [PLATFORM] exact ratio.

If the aspect ratio is wrong for [PLATFORM], if content sits under the avatar/crop zones, or if the tagline differs from the text above, the output is INCORRECT.
```

---

## Production Prompt — Nano Banana Pro (Alternate / Matched Set)

```
SYSTEM PROMPT (for a matched set of banners across platforms — apply identically):
Produce brand banners with a consistent look: [FONT CHARACTER] tagline type, text [text hex], accent [accent hex], background [background hex], scrim behind text for legibility. Always keep the focal element and text in the central safe zone, clear of the avatar overlap and responsive-crop margins. Render all copy verbatim.

TASK:
Create a [PLATFORM] header banner at its exact ratio, full-bleed. Background: [BACKGROUND]. Focal element: [FOCAL ELEMENT], centered in the safe zone. Keep the [AVATAR CORNER] clear.

EXACT TEXT (verbatim):
TAGLINE: "[TAGLINE]"

CONSTRAINTS:
- MUST: exact [PLATFORM] ratio, full-bleed; focal element + text in central safe zone; [AVATAR CORNER] clear; verbatim tagline; high contrast.
- MUST NOT: wrong ratio, content under avatar/crop zones, paraphrase/invent tagline, or low-contrast text.
- If the aspect ratio is wrong or the tagline differs from the text above, the output is INCORRECT.
- Quality: "high"
```

---

## Iteration Plan

1. "Content is sitting under the avatar in the [AVATAR CORNER] — shift the focal element and tagline toward the center/opposite side."
2. "The banner is the wrong shape for [PLATFORM] — re-render at the exact [ratio]."
3. "On mobile the tagline would get cropped — pull all text into the central safe zone."
4. "Text contrast is weak — strengthen the scrim or switch text to [higher-contrast hex]."
5. "The tagline lost a word — re-render verbatim: \"[TAGLINE]\"."

---

## Verification

- [ ] Exact `[PLATFORM]` aspect ratio; full-bleed.
- [ ] Focal element and all text inside the central safe zone.
- [ ] `[AVATAR CORNER]` clear of critical content.
- [ ] `[TAGLINE]` rendered 100% verbatim and legible at banner scale.
- [ ] Composition reads on both desktop (full) and mobile (cropped sides).
- [ ] Exact hex colors; strong text/background contrast.
- [ ] One clear focal idea — not crowded.
- [ ] `quality="high"` set (mandatory for text).
- [ ] Exported/resized to the platform's exact pixel dimensions.
