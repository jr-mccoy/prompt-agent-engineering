---
title: "Manga-Style Page — Screentone Look, Right-to-Left, Dynamic Paneling"
category: image-generation/comic-sequential
description: "Generate a manga-style page: screentone shading look, optional right-to-left reading order, and dynamic/diagonal paneling, with on-model characters."
techniques:
  - ST-01
  - ST-02
  - SV-12
  - SV-13
  - SV-15
  - SV-17
difficulty: advanced
tags:
  - manga
  - sequential-art
  - screentone
  - right-to-left
  - dynamic-paneling
  - gpt-image-2
  - nano-banana
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/comic-sequential/comic_panel_page.md
  - domain-image-generation/comic-sequential/webtoon_vertical_strip.md
  - domain-image-generation/STORYBOARD_WORKFLOW.md
  - domain-image-generation/CHARACTER_BIBLE_PIPELINE.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# Manga-Style Page — Screentone Look, Right-to-Left, Dynamic Paneling

**Objective:** Produce a single **manga-style page**: the black-and-white **screentone** shading look (halftone dot fields and gradients instead of flat gray), optional **right-to-left** reading order (Japanese convention), and **dynamic/diagonal paneling** (slanted gutters, overlapping panels, bleeds) for energy. Characters stay on-model across panels.

**Why model choice matters:** Manga's signature is the screentone-and-ink look plus expressive paneling. **gpt-image-2** holds one-pass cross-panel character consistency best and follows explicit screentone/paneling briefs. **Nano Banana 2** is good for fast per-panel iteration; **Nano Banana Pro** can lock the screentone render in a style slot. This page complements the Western [comic_panel_page.md](comic_panel_page.md) (LTR, flat color) and the [STORYBOARD_WORKFLOW.md](../STORYBOARD_WORKFLOW.md).

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `/v1/images/generations` or `/v1/images/edits`, `quality="high"`, `size="1024x1536"` (portrait page), `n=1`
- Nano Banana path: `model="gemini-3.1-flash-image"` (NB2) or `"gemini-3-pro-image"` (Pro, screentone style slot); `quality="high"`

---

## Inputs

- `[PAGE NUMBER]` — which page
- `[READING DIRECTION]` — `right-to-left` (manga convention) or `left-to-right`
- `[PANEL COUNT]` + `[PANEL DYNAMICS]` — number of panels and the dynamic layout (e.g., "5 panels, diagonal gutters, one full-bleed splash at top")
- `[CHARACTER NAME(S)]` + `[CHARACTER BIBLE]` + `[REFERENCE PACK]`
- `[BEAT SHEET]` — per panel: shot type, action, expression, camera
- `[SCREENTONE SPEC]` — tone density and where to apply (e.g., "60-line dot tone on shadows, gradient tone on skies, solid black hair")
- `[DIALOGUE MAP]` — bubble-safe areas per panel (vertical-text-friendly placement if RTL; do NOT render lettering unless asked)
- `[MANGA SUBSTYLE]` — shonen / shojo / seinen feel, line weight, eye style

---

## Constraints (Must / Must Not)

**Must:**
- Render the **screentone look**: halftone dot fields / gradients and solid blacks (not flat digital gray), per `[SCREENTONE SPEC]`.
- Follow the stated `[READING DIRECTION]` consistently across the page (RTL panels flow right→left, top→bottom).
- Use **dynamic paneling** per `[PANEL DYNAMICS]` while keeping the reading order unambiguous.
- Reserve **speech-bubble-safe areas**; for vertical Japanese text leave taller, narrower calm zones.
- Keep characters on-model; restate the bible and the manga substyle.

**Must Not:**
- Render lettering, furigana, or SFX kana unless explicitly requested.
- Add color (manga pages are black-and-white screentone) unless a color spread is requested.
- Make dynamic paneling so chaotic the reading order becomes ambiguous.
- Let the character drift between panels.

> **Reading-order note:** If you intend RTL, state it explicitly. Image models default to LTR composition; you must instruct RTL panel flow and bubble placement, then verify the eye genuinely reads right-to-left.

---

## Production Prompt — gpt-image-2 path (one-pass page)

```
SCENE:
A single black-and-white MANGA PAGE (page [PAGE NUMBER]), portrait orientation, [MANGA SUBSTYLE] style.
Reading direction: [READING DIRECTION — e.g., RIGHT-TO-LEFT, top-to-bottom]. Composition and panel flow must read in that direction.
Paneling: [PANEL COUNT] panels with [PANEL DYNAMICS — e.g., diagonal slanted gutters, one full-bleed splash at the top, overlapping inset panel]. Reading order must stay clear.

RENDER LOOK:
- Black-and-white screentone: [SCREENTONE SPEC — e.g., 60-line halftone dot tone on shadows, gradient tone on skies, solid black for hair and dark fabric].
- Clean ink linework, [line weight], expressive [MANGA SUBSTYLE] eyes and faces.
- No color.

CHARACTER BIBLE — [CHARACTER NAME(S)] (persist across panels):
[hair, eyes, build, face, default outfit, distinctive marks — rendered in screentone/ink]

PANEL BEATS (in [READING DIRECTION] order):
- Panel 1: [SHOT TYPE] — [action]. Expression: [emotion]. Camera: [angle].
- [continue; vary shot sizes between adjacent panels]

SPEECH-BUBBLE-SAFE AREAS:
- Panel [X]: reserve a [tall narrow / standard] calm zone at [region] for a balloon (vertical-text-friendly if RTL). Keep faces and action clear. Do NOT draw lettering.

USE CASE:
Finished manga page; a letterer adds balloons and SFX later in the reserved areas.

CONSTRAINTS:
- Screentone look (no flat gray, no color); solid blacks where specified.
- [READING DIRECTION] flow, unambiguous order despite dynamic paneling.
- Bubble-safe areas reserved; no lettering/SFX rendered.
- Character on-model; consistent [MANGA SUBSTYLE] across panels.
- Format: portrait page, quality="high".

If the page reads in the wrong direction, if it uses flat gray instead of screentone, if lettering is rendered, or if the character drifts, the page is incorrect.
```

---

## Production Prompt — Nano Banana path (per-panel)

```
TASK: Generate panel [N] of [PANEL COUNT] for a black-and-white manga page, [MANGA SUBSTYLE], [READING DIRECTION].

REFERENCES (Char slots): reference pack for [CHARACTER NAME].
[Nano Banana Pro: Style 1 = a prior manga panel. TAKE the screentone/ink look, IGNORE composition.]

CHARACTER BIBLE — [CHARACTER NAME] (restated): [full bible]

PANEL BEAT: [SHOT TYPE] — [action]. Expression: [emotion]. Camera: [angle].

RENDER LOOK: black-and-white screentone per [SCREENTONE SPEC]; clean ink line; solid black hair; no color.

SPEECH-BUBBLE-SAFE AREA: reserve [region] (vertical-friendly if RTL) for a balloon; keep faces/action clear. No lettering.

PRESERVE: [CHARACTER NAME]'s identity; the screentone/ink style.

CONSTRAINTS:
- MUST: screentone look (no flat gray, no color); on-model character; reserved bubble zone.
- MUST NOT: render lettering/SFX; add color; drift identity/style.
- Quality: "high".

Assemble panels into the dynamic layout externally in [READING DIRECTION] order.
```

---

## Iteration Plan

1. "The shadows are flat digital gray — convert to halftone dot screentone per the `[SCREENTONE SPEC]`."
2. "The page reads left-to-right but I need right-to-left — flip the panel flow and re-place bubble-safe zones for vertical text."
3. "The dynamic paneling made the order ambiguous between panels 3 and 4 — adjust gutter angles so the eye clearly moves to the next panel."
4. "The eye style drifted from `[MANGA SUBSTYLE]` — restore the canonical face/eye style."
5. "`[CHARACTER NAME]`'s hair lost its solid black — restore solid-black hair with tone highlights."

---

## Verification

- [ ] Screentone look (halftone dots/gradients + solid blacks), not flat gray; no color.
- [ ] Reading direction matches `[READING DIRECTION]` and is unambiguous despite dynamic paneling.
- [ ] Dynamic paneling applied per `[PANEL DYNAMICS]`.
- [ ] Speech-bubble-safe areas reserved (vertical-friendly if RTL); no lettering/SFX rendered.
- [ ] Character on-model across panels.
- [ ] `[MANGA SUBSTYLE]` consistent (line weight, eye/face style).
- [ ] Adjacent panels vary in shot size.
- [ ] Portrait page orientation correct.
