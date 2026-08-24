---
title: "Comic Page — Multi-Panel Layout with Gutters & Speech-Safe Areas"
category: image-generation/comic-sequential
description: "Generate a multi-panel comic page with controlled gutters, panel flow, and speech-bubble-safe areas, keeping characters on-model across panels."
techniques:
  - ST-01
  - ST-02
  - SV-12
  - SV-13
  - SV-15
  - SV-17
difficulty: advanced
tags:
  - comic
  - sequential-art
  - panels
  - gutters
  - speech-bubbles
  - gpt-image-2
  - nano-banana
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/comic-sequential/manga_style_panel.md
  - domain-image-generation/comic-sequential/webtoon_vertical_strip.md
  - domain-image-generation/STORYBOARD_WORKFLOW.md
  - domain-image-generation/CHARACTER_BIBLE_PIPELINE.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# Comic Page — Multi-Panel Layout with Gutters & Speech-Safe Areas

**Objective:** Produce a single finished **comic page**: multiple panels with intentional **gutters**, a left-to-right / top-to-bottom (Western) reading flow, **speech-bubble-safe areas** reserved in each panel, and consistent character identity across panels. Use case: Western comics, graphic novels, comic strips, pitch pages.

**Why model choice matters:** A comic page is one composition with several internal frames and reserved bubble space. **gpt-image-2** is the first choice for one-pass multi-panel pages — it holds cross-panel character consistency best in a single generation and renders panel gutters cleanly. **Nano Banana 2** is the choice when iterating individual panels fast or carrying a role-separated character reference pack. This prompt is the comic-page specialization of the [STORYBOARD_WORKFLOW.md](../STORYBOARD_WORKFLOW.md) — use that for shot-progression theory and the video handoff; use this for the printed/static comic page.

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `/v1/images/generations` (one-pass page) or `/v1/images/edits` (carry character refs), `quality="high"`, `size="1024x1536"` (portrait comic page), `n=1`
- Nano Banana path: `model="gemini-3.1-flash-image"` (NB2, per-panel) or `"gemini-3-pro-image"` (Pro, style slot); `quality="high"`

---

## Inputs

- `[PAGE NUMBER]` — which page
- `[PANEL COUNT]` + `[LAYOUT]` — e.g., "6 panels, 3 rows of 2"; or an irregular grid
- `[CHARACTER NAME(S)]` + `[CHARACTER BIBLE]` + `[REFERENCE PACK]` — for on-model characters
- `[BEAT SHEET]` — per panel: shot type, action, expression, camera (see STORYBOARD_WORKFLOW.md)
- `[DIALOGUE MAP]` — which panels carry speech/caption and roughly where the bubble sits (used to reserve bubble-safe space; do NOT render lettering unless explicitly asked)
- `[STYLE]` — canonical comic style (e.g., "clean ink-and-flat-color, bold outlines, cel shading")
- `[COLOR GRADE]` — uniform across all panels
- `[GUTTER]` — gutter color/width (e.g., "white, 12px")

---

## Constraints (Must / Must Not)

**Must:**
- Render clear **gutters** between panels and follow a consistent reading order (Western: left-to-right, top-to-bottom).
- Reserve **speech-bubble-safe areas** (calm negative space, usually upper region of a panel) wherever `[DIALOGUE MAP]` marks dialogue; keep faces and key action out of those zones.
- Adjacent panels should **differ by at least one shot-size step** (avoid two identical medium shots in a row).
- Restate the character bible and canonical `[STYLE]`; keep characters on-model across panels.
- Keep the `[COLOR GRADE]` and lighting direction uniform across the page.

**Must Not:**
- Render speech-bubble lettering or sound effects unless explicitly requested (letterers add type separately).
- Crowd every panel edge-to-edge (leaves no bubble-safe space).
- Let the character drift between panels.
- Mix reading directions (this is a Western LTR page; for right-to-left, use manga_style_panel.md).

---

## Production Prompt — gpt-image-2 path (one-pass page)

```
SCENE:
A single comic-book PAGE (page [PAGE NUMBER]), portrait orientation, [PANEL COUNT] panels in this layout: [LAYOUT — e.g., 3 rows of 2 equal panels].
Reading order: left to right, top to bottom (Western).
Gutters: [GUTTER — e.g., clean white, ~12px] between every panel. Thin neat panel borders.

CHARACTER BIBLE — [CHARACTER NAME(S)] (must persist across all panels):
- Hair: [color, length, style]
- Eyes: [color, shape]
- Skin: [tone]
- Build: [proportions]
- Default outfit: [garment by garment, colors]
- Distinctive marks: [drift detector]

PANEL BEATS (left-to-right, top-to-bottom):
- Panel 1: [SHOT TYPE] — [action]. Expression: [emotion]. Camera: [angle].
- Panel 2: [SHOT TYPE] — [action]. ...
- [continue for all panels; ensure adjacent panels differ by a shot-size step]

SPEECH-BUBBLE-SAFE AREAS:
- Panel [X]: reserve the [region — e.g., upper-left] as calm negative space for a speech balloon; keep faces and key action clear of it. Do NOT draw lettering.
- Panel [Y]: reserve [region] for a caption box. Do NOT draw text.

STYLE: [STYLE] — canonical, identical across all panels.
COLOR GRADE: [COLOR GRADE] — uniform across every panel.
LIGHTING: consistent key-light direction across the page.

USE CASE:
Finished comic page for [print / digital]. A letterer will add balloons and captions later in the reserved safe areas.

CONSTRAINTS:
- Clear gutters; correct Western reading order.
- Speech-bubble-safe areas kept calm; no rendered lettering or SFX.
- Character on-model across all panels; consistent style and color grade.
- Adjacent panels differ by at least one shot-size step.
- Format: portrait page, quality="high".

If lettering is rendered, if speech-safe areas are crowded, if the reading order is ambiguous, or if the character/style drifts between panels, the page is incorrect.
```

---

## Production Prompt — Nano Banana path (per-panel, then assemble)

```
TASK: Generate panel [N] of [PANEL COUNT] for comic page [PAGE NUMBER].

REFERENCES (Char slots): reference pack for [CHARACTER NAME].
TAKE: face, hair, skin, eye color, proportions, outfit, distinctive marks.
[Nano Banana Pro: Style 1 = a prior finished panel. TAKE the ink/color style + grade, IGNORE composition.]

CHARACTER BIBLE — [CHARACTER NAME] (restated): [full bible]

PANEL CONTEXT:
This is panel [N] of [TOTAL] in a Western comic page. Previous panel showed [N-1 summary]; next panel will show [N+1 summary].

PANEL BEAT: [SHOT TYPE] — [action]. Expression: [emotion]. Camera: [angle].

SPEECH-BUBBLE-SAFE AREA: reserve [region] as calm negative space for a balloon/caption; keep faces and key action clear. Do NOT render lettering.

STYLE: [STYLE] — canonical, identical to other panels.
COLOR GRADE: [COLOR GRADE] — must match all panels.
LIGHTING: [key-light direction] — consistent across the page.

PRESERVE: [CHARACTER NAME]'s exact face/hair/eyes/proportions/marks; canonical style; color grade.

CONSTRAINTS:
- MUST: on-model character; uniform style + grade; reserved bubble-safe area; no lettering.
- MUST NOT: drift identity; change grade; crowd the bubble zone.
- Quality: "high".

Assemble the panels into the [LAYOUT] page externally, adding [GUTTER] gutters.
If the character/style/grade drifts from other panels, the panel is incorrect.
```

---

## Iteration Plan

1. "Panels 2 and 3 are both medium shots and feel static — make panel 3 a close-up for a shot-size change."
2. "The speech-safe area in panel 4 is covered by the character's head — shift the figure down and clear the upper-left."
3. "The color grade warmed up in the bottom row — restore the uniform `[COLOR GRADE]`."
4. "`[CHARACTER NAME]`'s outfit color changed in panel 5 — restore the default outfit from the reference pack."
5. "Gutters are uneven — make all gutters `[GUTTER]` width and the borders consistent."

---

## Verification

- [ ] Clear, consistent gutters; unambiguous Western reading order.
- [ ] Speech-bubble-safe areas reserved where `[DIALOGUE MAP]` marks dialogue; faces/action clear of them.
- [ ] No lettering or SFX rendered (unless explicitly requested).
- [ ] Adjacent panels differ by at least one shot-size step.
- [ ] Character on-model across all panels (no drift).
- [ ] Style and color grade uniform across the page.
- [ ] Consistent lighting direction.
- [ ] Portrait page orientation correct.
