---
title: "Storyboard Workflow — Cross-Model Guide"
category: image-generation/workflow
description: "End-to-end workflow for generating storyboard grids across image models, with downstream video pipeline integration."
techniques:
  - ST-01
  - ST-02
  - SV-12
  - SV-13
  - SV-17
difficulty: intermediate
tags:
  - storyboard
  - keyframes
  - video-pipeline
  - cross-model
  - workflow
  - sequential-art
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/VIDEO_GENERATION_GUIDE.md
  - domain-image-generation/CHARACTER_BIBLE_PIPELINE.md
  - domain-image-generation/nano-banana/nanobana_storyboard_veo_keyframes.md
  - domain-image-generation/NANO_BANANA_GUIDE.md
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
---

# Storyboard Workflow — Cross-Model Guide

**Purpose:** A model-agnostic workflow for generating storyboard grids from AI image models and feeding the panels into video generation pipelines. Covers panel planning, shot progression, grid generation, consistency enforcement, and downstream video handoff.

**Use cases:** Ad pre-production, short film storyboards, product demo sequences, explainer videos, social media content series, pitch decks with visual narratives.

---

## Pipeline Overview

```
Phase 1: Shot Planning (text)
  Define beats, shot types, camera, character, setting
    ↓
Phase 2: Grid Generation (image model)
  Screen at low-res → select → produce at high-res
    ↓
Phase 3: Consistency Check
  Verify character, color grade, lighting across panels
    ↓
Phase 4: Video Handoff (optional)
  Feed panels as keyframes to video model (Veo, Seedance, Kling)
```

---

## Phase 1: Shot Planning

Before opening any image model, plan the visual beats on paper (or in text). A storyboard is a sequence of decisions — the image model executes them.

### Beat Sheet Template

```
PROJECT: [Title / working name]
FORMAT: [Ad / short film / product demo / explainer / social clip]
DURATION: [Total seconds of final video, if applicable]
PANELS: [Number of panels — typically 4, 6, 8, or 9]
GRID: [Columns × Rows — e.g., 3×2 for 6 panels]

CHARACTER: [Name, or "no recurring character"]
LOCATION: [Primary setting, time of day, weather]
COLOR GRADE: [Warm/cool, saturation, contrast, shadow tint — applied uniformly]

BEAT SHEET:
Panel 1: [SHOT TYPE] — [What happens. Subject position. Expression.]
  Camera: [angle, movement intent for video]
  Purpose: [Establish / build / turn / resolve / reveal]

Panel 2: [SHOT TYPE] — [What happens.]
  Camera: [angle, movement]
  Purpose: [narrative function]

Panel 3: [SHOT TYPE] — [What happens.]
  ...

[Continue for all panels.]

HERO FRAME: Panel [N] — this is the money shot.
```

### Shot Type Progression

Most effective storyboards follow a visual rhythm. Common progressions:

| Pattern | Panels | Description |
|---------|--------|-------------|
| Establishing → Detail | WS → MS → CU → ECU | Classic zoom-in narrative |
| Detail → Context | ECU → CU → MS → WS | Reveal — start tight, pull back |
| Alternating | WS → CU → MS → CU → WS → CU | Conversation / action-reaction |
| Parallel | MS × 6 | Same framing, changing content (time-lapse, comparison) |
| Escalating | MS → MS → MS → CU → CU → ECU | Building tension |

**Rule:** Adjacent panels should differ by at least one shot-size step. Two consecutive medium shots feel static.

---

## Phase 2: Grid Generation

### Model Selection for Storyboards

| Model | Best For | Grid Support | Screening |
|-------|----------|-------------|-----------|
| **Nano Banana 2** | Fastest iteration, cheapest screening, Veo pipeline | Native multi-panel grids | 512px at $0.002/image |
| **gpt-image-2** | Highest single-panel quality, text-in-panels | Generate panels individually, composite externally | No native screening tier |
| **Midjourney** | Strongest style consistency | `--ar` for aspect, manual grid assembly | No native screening |
| **Stable Diffusion** | Full control, batch automation | Script-driven grid assembly | Free (local compute) |

### Screening Pass (Nano Banana 2)

Generate 6 candidates at low resolution to find the best composition before committing.

```
TASK: Create a [PANEL COUNT]-panel storyboard grid for a [DURATION]-second [FORMAT].

LAYOUT:
[GRID] (e.g., 3 columns × 2 rows), left-to-right, top-to-bottom reading order.
Thin neutral gutters (#E0E0E0, 2px). No text, captions, or panel numbers.

[If recurring character, include CHARACTER section with full bible.]

LOCATION:
[Detailed setting description, time of day, key environmental features.]

PANEL BEATS:
[Paste the beat sheet from Phase 1, one line per panel.]

COLOR GRADE:
[Describe uniformly: warm/cool, saturation, contrast, shadow tint.]
This grade applies to ALL panels identically.

CONSTRAINTS:
- Same character identity in every panel (if applicable)
- No motion blur — frozen moments
- No busy backgrounds — clear subject silhouettes
- Room for motion in each panel (don't crop tight against frame edges)
- No text, labels, or panel numbers
- Quality: "standard" (screening pass)
```

### Production Pass

After selecting the best screening candidate, refine and regenerate at full resolution.

```
[Repeat the full screening prompt, then add:]

REFINEMENTS FROM SCREENING:
- [What to fix: "Panel 3 needs wider framing for the camera push-in"]
- [What to fix: "Lighting in panel 5 doesn't match the color grade — correct"]

Quality: "high"
Size: [2048x2048 or target aspect ratio]
```

### Per-Panel Generation (gpt-image-2 / Midjourney)

When the model doesn't support native multi-panel grids, generate each panel individually:

```
[For each panel, use a prompt that includes:]

STORYBOARD CONTEXT:
This is panel [N] of [TOTAL] in a [FORMAT] storyboard.
Previous panel: [describe what panel N-1 showed]
Next panel: [describe what panel N+1 will show]

[Full character bible if applicable]
[Shot type, camera, lighting from the beat sheet]
[Color grade — identical across all panels]

CONSTRAINTS:
- This panel must feel like part of a sequence, not a standalone image.
- Color grade: [restate] — must match all other panels in the set.
- Lighting direction: [restate] — consistent across the sequence.
- Character identity: [restate if applicable] — identical to all other panels.
```

---

## Phase 3: Consistency Check

After generating all panels, verify consistency before proceeding.

### Visual Consistency Checklist

| Check | Method | Fix |
|-------|--------|-----|
| **Character identity** | Side-by-side: same face, hair, outfit across all panels? | Regenerate drifted panels with original reference pack |
| **Color grade** | Are all panels the same warmth/saturation/contrast? | Regenerate outlier panels with explicit color grade restatement |
| **Lighting direction** | Does the key light come from the same side in every panel? | Restate lighting direction per panel if inconsistent |
| **Scale consistency** | Is the character the same relative size when at the same distance? | Specify "subject fills [X]% of frame" per panel |
| **Style unity** | Same rendering approach across all panels? | Restate canonical style; use style references (NB Pro) |
| **Shot progression** | Do the shot types follow the planned beat sheet? | Regenerate panels that don't match the planned shot type |
| **Background continuity** | Is the same location recognizable across panels? | Restate key environmental features per panel |

### Common Consistency Failures

1. **Color grade drift** — panels 1-3 are warm, panels 4-6 are cool. Fix: restate the grade in every panel prompt.
2. **Character hair color shift** — brown in panel 1, auburn in panel 4. Fix: use hex codes in the bible.
3. **Lighting direction flip** — key light from the left in panels 1-3, from the right in panels 4-6. Fix: explicit "key light from upper-left at 45°" in every prompt.
4. **Style blending** — early panels are watercolor, later panels drift toward digital illustration. Fix: restate canonical style + use style reference images.

---

## Phase 4: Video Handoff

### Pipeline Options (June 2026)

| Pipeline | Method | Best For |
|----------|--------|----------|
| **Nano Banana → Veo** | Official Google pipeline. "Ingredients" mode (up to 3 refs) or "Frames" mode (start + end keyframes) | Google ecosystem, character consistency |
| **gpt-image-2 → Seedance 2.0** | Generate stills with GPT, feed as keyframes to Seedance | Highest-quality stills + motion |
| **Any model → Kling** | Feed panels as start/end frames | Broad compatibility |

**Dead pipeline:** gpt-image-2 → Sora. Sora consumer app shut down April 2026; API discontinued September 2026. Use Seedance 2.0 (ByteDance) instead.

### Veo Handoff Template

```
[Pass Panel 1 as start frame, Panel N as end frame]

Smoothly transition from the start frame to the end frame over [DURATION] seconds.

MOTION:
- Subject: [CHARACTER NAME] [action — walking, turning, reaching].
- Camera: [movement — dolly in, pan right, static, handheld drift].
- Environment: [motion — wind in hair, passing clouds, flickering lights].

PRESERVE:
- Exact character identity from both frames.
- Color grade, lighting direction, and visual style.
- Scene layout and background composition.

TIMING:
- [0–2s]: [what happens]
- [2–4s]: [what happens]
- [4–6s]: [what happens]

CONSTRAINTS:
- No identity drift between frames.
- No style shift (maintain the storyboard's canonical look).
- No added elements not present in the keyframes.
```

### What Makes a Good Keyframe

A storyboard panel intended for video handoff needs:
- **Clear subject silhouette** — the video model needs to know what moves.
- **Compositional room** — don't crop tight; leave space for the intended motion.
- **No motion blur** — the still defines a frozen moment; the video model adds motion.
- **Clean background** — busy/cluttered backgrounds confuse video models.
- **Physically consistent lighting** — the video model interpolates between frames; inconsistent lighting creates impossible transitions.
- **Different poses** — start and end frames should show clearly different positions of the same character, giving the video model a trajectory.

### What Doesn't Work

- **Near-identical start/end frames** — the video model has nothing to interpolate.
- **Extreme angle changes** — the camera can't physically move from a bird's eye to a worm's eye in 3 seconds.
- **Text in frames** — video models don't preserve text legibility during motion.
- **Dramatic style differences** — the video model tries to morph between styles.

---

## Quick Reference: Storyboard Aspect Ratios

| Use | Aspect Ratio | Pixels (Production) |
|-----|-------------|-------------------|
| Social story / reel (vertical) | 9:16 | 1080 × 1920 |
| Social post (square) | 1:1 | 1080 × 1080 |
| YouTube / presentation (landscape) | 16:9 | 1920 × 1080 or 3840 × 2160 |
| Film / cinema (wide) | 2.39:1 | 2560 × 1072 |
| Nano Banana 2 extreme vertical | 1:4 | 512 × 2048 |
| Nano Banana 2 extreme horizontal | 4:1 | 2048 × 512 |

---

## Quick Checklist

Before generating any storyboard:
- [ ] Beat sheet written with shot type, action, and camera per panel
- [ ] Character bible prepared (if recurring character)
- [ ] Color grade defined and will be restated in every prompt
- [ ] Model selected based on task requirements (see table)
- [ ] Screening pass planned (if using Nano Banana 2)

After generation:
- [ ] Character identity consistent across all panels
- [ ] Color grade uniform across all panels
- [ ] Lighting direction consistent
- [ ] Shot progression follows the beat sheet
- [ ] Each panel has a clear subject silhouette
- [ ] No text, labels, or panel numbers in the grid (unless intentional)

If handing off to video:
- [ ] Start and end frames show clearly different poses/positions
- [ ] Compositional room exists for intended motion
- [ ] No motion blur in any panel
- [ ] Lighting is physically consistent between start/end frames
- [ ] Background is clean enough for video interpolation
