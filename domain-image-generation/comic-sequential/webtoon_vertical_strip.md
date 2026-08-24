---
title: "Webtoon Vertical Strip — Long-Scroll Sequential Art"
category: image-generation/comic-sequential
description: "Generate a vertical-scroll webtoon strip (extreme tall aspect ratio) with scroll-paced beats, vertical gutters, and speech-safe areas, keeping characters on-model."
techniques:
  - ST-01
  - ST-02
  - SV-12
  - SV-13
  - SV-15
  - SV-17
difficulty: advanced
tags:
  - webtoon
  - vertical-scroll
  - sequential-art
  - extreme-aspect-ratio
  - nano-banana
  - gpt-image-2
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/comic-sequential/comic_panel_page.md
  - domain-image-generation/comic-sequential/manga_style_panel.md
  - domain-image-generation/STORYBOARD_WORKFLOW.md
  - domain-image-generation/CHARACTER_BIBLE_PIPELINE.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
---

# Webtoon Vertical Strip — Long-Scroll Sequential Art

**Objective:** Produce a **vertical-scroll webtoon strip**: a very tall, narrow image (or a stitched run of tall segments) read by scrolling top-to-bottom on a phone, with **scroll-paced beats**, **vertical gutters** (whitespace between beats that controls pacing), and reserved **speech-safe areas**, while keeping characters on-model. Use case: Webtoon / Tapas / vertical-scroll comics.

**Why model choice matters:** Webtoons live at **extreme tall aspect ratios** (e.g., 1:4 and beyond). **Nano Banana 2** is the recommended model — it is the one model in this repo's selection guide that natively supports extreme ratios (1:8 / 8:1), so a tall strip can be generated closer to its true shape. **gpt-image-2** caps at roughly 1:3, so on that path you generate beat segments at portrait sizes and **stitch** them into the full strip externally. Nano Banana Pro can lock the style in a style slot.

**API parameters:**
- Nano Banana path (preferred for tall): `model="gemini-3.1-flash-image"` (NB2, extreme ratios) or `"gemini-3-pro-image"` (Pro, style slot); request a tall aspect ratio (e.g., 1:4); `quality="high"`
- gpt-image-2 path: `model="gpt-image-2"`, generate beat segments at `size="1024x1536"` (max ~1:3), then **stitch** vertically; `/v1/images/edits` to carry character refs; `quality="high"`

> Aspect-ratio reference (see STORYBOARD_WORKFLOW.md): Nano Banana 2 extreme vertical 1:4 ≈ 512×2048; standard mobile 9:16 = 1080×1920. For long episodes, segment the strip and stitch — even on Nano Banana, a single image has practical height limits.

---

## Inputs

- `[EPISODE/STRIP NUMBER]` — which strip
- `[BEAT COUNT]` + `[SCROLL PACING]` — number of top-to-bottom beats and the whitespace between them (tight = fast read; tall gaps = dramatic pause / beat)
- `[ASPECT RATIO]` — target tall ratio (e.g., 1:4) or per-segment portrait if stitching
- `[CHARACTER NAME(S)]` + `[CHARACTER BIBLE]` + `[REFERENCE PACK]`
- `[BEAT SHEET]` — per beat (top→bottom): shot type, action, expression
- `[DIALOGUE MAP]` — bubble-safe areas per beat (do NOT render lettering unless asked)
- `[STYLE]` + `[COLOR GRADE]` — canonical webtoon style, uniform across beats

---

## Constraints (Must / Must Not)

**Must:**
- Compose for **vertical scroll**: each beat stacked top-to-bottom, read by scrolling down, with deliberate **vertical gutters / whitespace** to pace the read.
- Use **scroll pacing** intentionally — tall empty gaps create pauses and dramatic beats; tight stacking accelerates.
- Reserve **speech-safe areas** within beats (do not crowd faces/action).
- Keep characters on-model across beats; restate the bible and `[STYLE]`.
- Keep `[COLOR GRADE]` and lighting consistent down the whole strip.
- Leave the subject with breathing room from the **left/right edges** (phone-readable, no edge-crowding).

**Must Not:**
- Compose as a side-by-side grid (webtoons read by scrolling, not page-flipping).
- Render lettering/SFX unless explicitly requested.
- Let character or color grade drift between beats (very visible during a continuous scroll).
- Pack beats with zero whitespace (kills pacing and readability on mobile).

---

## Production Prompt — Nano Banana path (tall single strip / segment)

```
TASK: Create a vertical-scroll WEBTOON strip segment (episode [EPISODE/STRIP NUMBER]) at a tall [ASPECT RATIO — e.g., 1:4] aspect ratio, read top-to-bottom by scrolling on a phone.

REFERENCES (Char slots): reference pack for [CHARACTER NAME].
TAKE: face, hair, skin, eye color, proportions, outfit, distinctive marks.
[Nano Banana Pro: Style 1 = a prior strip segment. TAKE the webtoon style + color grade, IGNORE composition.]

CHARACTER BIBLE — [CHARACTER NAME] (restated): [full bible]

VERTICAL BEATS (top to bottom):
- Beat 1 (top): [SHOT TYPE] — [action]. Expression: [emotion].
- [vertical gutter / whitespace: SCROLL PACING — e.g., short gap]
- Beat 2: [SHOT TYPE] — [action]. ...
- [tall whitespace gap for a dramatic pause before the next beat]
- Beat 3: ...
[continue top→bottom]

SCROLL PACING: [SCROLL PACING] — use the gaps between beats deliberately; tall gaps = pause/drama, tight stacking = fast read.

SPEECH-SAFE AREAS: in beats [X, Y] reserve calm space at [region] for balloons/captions; keep faces and action clear. Do NOT render lettering.

STYLE: [STYLE] — canonical webtoon look.
COLOR GRADE: [COLOR GRADE] — uniform down the entire strip.
LIGHTING: consistent direction across beats.
COMPOSITION: keep subjects clear of the left/right edges for phone readability.

CONSTRAINTS:
- Vertical scroll composition (NOT a side-by-side grid).
- Intentional vertical gutters/whitespace for pacing.
- On-model character; uniform style + grade across beats.
- Reserved speech-safe areas; no rendered lettering.
- Format: tall [ASPECT RATIO], quality="high".

If composed as a grid, if pacing whitespace is missing, if lettering is rendered, or if the character/grade drifts between beats, the strip is incorrect.
```

---

## Production Prompt — gpt-image-2 path (per-beat, then stitch)

```
TASK: Generate beat [N] of [BEAT COUNT] for a vertical-scroll webtoon (episode [EPISODE/STRIP NUMBER]). This beat will be stitched into a continuous tall strip.

REFERENCE: pass the character reference pack for [CHARACTER NAME].

CHARACTER BIBLE — [CHARACTER NAME] (restated): [full bible]

BEAT CONTEXT: beat [N] of [TOTAL], read by scrolling down. Previous beat: [N-1 summary]; next beat: [N+1 summary].

BEAT: [SHOT TYPE] — [action]. Expression: [emotion].
- Leave generous whitespace at the [top / bottom] of this segment for the scroll gutter ([SCROLL PACING]).
- Reserve [region] as a speech-safe area if this beat carries dialogue. No lettering.

STYLE: [STYLE]. COLOR GRADE: [COLOR GRADE] — must match all beats. LIGHTING: [direction], consistent.
COMPOSITION: subject clear of left/right edges; portrait segment (~1:3 max on gpt-image-2).

PRESERVE: [CHARACTER NAME]'s identity; the webtoon style; the color grade.

CONSTRAINTS:
- MUST: on-model; uniform grade; scroll-gutter whitespace; reserved speech-safe area.
- MUST NOT: render lettering; drift identity/grade; crowd edges.
- Quality: "high".

Stitch all beats vertically (top→bottom) into the final tall strip externally, preserving the pacing gutters.
```

---

## Iteration Plan

1. "The beats are packed with no whitespace — add taller vertical gutters between beats 2 and 3 for a dramatic pause."
2. "It reads like a grid — recompose as a single top-to-bottom scroll with stacked beats."
3. "The color grade shifted halfway down — restore the uniform `[COLOR GRADE]` for the lower beats."
4. "`[CHARACTER NAME]` drifted in the third beat — restore identity from the reference pack."
5. "The subject is crowding the right edge and gets cut off on a phone — pull it inward with edge breathing room."

---

## Verification

- [ ] Composed for vertical scroll (top-to-bottom), not a side-by-side grid.
- [ ] Intentional vertical gutters / whitespace pacing the read.
- [ ] Tall aspect ratio (Nano Banana path) or correctly stitched segments (gpt-image-2 path).
- [ ] Speech-safe areas reserved; no lettering rendered (unless requested).
- [ ] Character on-model across all beats.
- [ ] Color grade and lighting consistent down the whole strip.
- [ ] Subjects clear of left/right edges (phone-readable).
- [ ] Shot sizes vary between adjacent beats.
