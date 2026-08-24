---
title: "Nano Banana Prompting Guide (Gemini Image Models)"
category: image-generation/model-specific
description: "Comprehensive prompting guide for Google's Nano Banana image model family: Nano Banana (gemini-2.5-flash-image), Nano Banana Pro (gemini-3-pro-image), and Nano Banana 2 (gemini-3.1-flash-image)"
techniques:
  - SV-11
  - SV-12
  - SV-13
  - SV-14
  - SV-15
  - SV-16
  - SV-17
  - SV-18
  - ST-01
  - ST-02
  - ST-03
difficulty: intermediate
tags:
  - nano-banana
  - gemini
  - google
  - image-generation
  - model-guide
  - prompting
  - character-consistency
  - storyboard
  - veo
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/IMAGE_PROMPTING_GUIDE.md
  - domain-image-generation/IMAGE_GENERATION_GUIDE.md
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
  - domain-image-generation/VIDEO_GENERATION_GUIDE.md
---

# Nano Banana Prompting Guide (Gemini Image Models)

**Purpose:** Authoritative reference for prompting Google's Nano Banana image model family. Covers all three current models, their distinct strengths, prompting strategies, reference image workflows, JSON schema prompting, and integration with Google's Veo video pipeline.

**Audience:** Anyone writing production prompts for Nano Banana models via the Gemini API, Google AI Studio, or Vertex AI.

**Relationship to other guides:**
- **[IMAGE_PROMPTING_GUIDE.md](IMAGE_PROMPTING_GUIDE.md)** — Cross-model image prompting reference (covers all models at surface level).
- **[IMAGE_GENERATION_GUIDE.md](IMAGE_GENERATION_GUIDE.md)** — Print-ready material constraints (the 8 SV techniques).
- **[GPT_IMAGE_2_GUIDE.md](GPT_IMAGE_2_GUIDE.md)** — OpenAI's flagship model guide (the primary alternative).
- **[VIDEO_GENERATION_GUIDE.md](VIDEO_GENERATION_GUIDE.md)** — Veo 3 / 3.1 video generation (downstream from Nano Banana keyframes).
- **This guide** — Nano Banana-specific patterns: model selection, reference allocation, system prompts, search grounding, JSON schema prompting, Veo pipeline.

---

## Table of Contents

1. [The Model Family at a Glance](#1-the-model-family-at-a-glance)
2. [Model Selection: Which Nano Banana When](#2-model-selection)
3. [Parameters](#3-parameters)
4. [Prompt Structure](#4-prompt-structure)
5. [Reference Images (Up to 14)](#5-reference-images)
6. [Text Rendering](#6-text-rendering)
7. [System Prompts](#7-system-prompts)
8. [Google Search Grounding](#8-google-search-grounding)
9. [JSON Schema Prompting](#9-json-schema-prompting)
10. [Editing: Change vs. Preserve](#10-editing)
11. [Character Consistency](#11-character-consistency)
12. [Storyboard and Veo Pipeline](#12-storyboard-and-veo-pipeline)
13. [Medical Imaging Considerations](#13-medical-imaging-considerations)
14. [Anti-Patterns](#14-anti-patterns)
15. [Iteration Strategy](#15-iteration-strategy)
16. [Quality Checklist](#16-quality-checklist)
17. [Templates](#17-templates)

---

## 1. The Model Family at a Glance

Google's image generation models share the "Nano Banana" community nickname. Three models are currently active:

| | **Nano Banana** | **Nano Banana Pro** | **Nano Banana 2** |
|---|---|---|---|
| **Model ID** | `gemini-2.5-flash-image` | `gemini-3-pro-image` | `gemini-3.1-flash-image` |
| **Released** | Mid-2025 | November 2025 | February 2026 |
| **Positioning** | Speed / efficiency | Professional / high-fidelity | Pro-level quality at Flash speed |
| **Max output** | 1K default, 2K | 1K default, 2K, 4K | 1K default, 2K, 4K, plus 512px |
| **Aspect ratios** | Standard (1:1, 4:3, 16:9, 3:4, 9:16) | Standard + wide | Standard + extreme (1:4, 4:1, 1:8, 8:1) |
| **Reference images** | Limited | Up to 14 (6 object + 5 character + 3 style) | Up to 14 (10 object + 4 character) |
| **System prompts** | No | Yes | Yes |
| **Search grounding** | No | Yes | Yes |
| **Text rendering** | Good | Near-perfect | Good-to-excellent |
| **Context window** | 32K tokens | Full LLM context | 32K tokens |
| **Thinking mode** | No | Yes (full LLM reasoning before generation) | No |
| **Latency** | Fast (seconds) | Variable (20s to 60s+) | Fast (seconds) |

**Deprecation notice:** Preview model IDs (`gemini-3.1-flash-image-preview`, `gemini-3-pro-image-preview`) were deprecated **June 25, 2026**. Use the stable model IDs listed above.

---

## 2. Model Selection

Choose the model based on the **job**, not a generic quality preference:

| Task | Recommended Model | Why |
|------|-------------------|-----|
| Fast ideation / exploration / many candidates | Nano Banana 2 | Speed + 512px screening option |
| Storyboard keyframes for Veo | Nano Banana 2 | Speed, official Veo pairing, cheap candidates |
| Hard compositions / multi-subject fidelity | Nano Banana Pro | Full LLM reasoning before generation |
| Text-heavy visuals / infographics | Nano Banana Pro | Near-perfect text rendering + search grounding |
| Multilingual text / factual data visuals | Nano Banana Pro | Search grounding verifies data in real time |
| Character consistency across sequences | Nano Banana 2 or Pro | 14 reference images, role-separated allocation |
| Multi-reference compositing | Nano Banana 2 | 10 object + 4 character slots |
| Unusual aspect ratios (banners, scrolls) | Nano Banana 2 | Supports 1:4, 4:1, 1:8, 8:1 |
| Production assets needing consistent style | Nano Banana Pro | System prompts lock style across generations |
| Quick cost-sensitive batch work | Nano Banana (original) | Lowest cost per generation |

**When to use gpt-image-2 instead:** Polished production layouts, infographics with complex data hierarchies, comic-page continuity, one-pass multi-panel grids with cross-panel consistency, or when you need OpenAI's artifact specification workflow. See [GPT_IMAGE_2_GUIDE.md](GPT_IMAGE_2_GUIDE.md).

---

## 3. Parameters

### Output Size

| Model | Sizes | Notes |
|-------|-------|-------|
| Nano Banana | 1024×1024 (default), up to 2K | |
| Nano Banana Pro | 1024×1024 (default), 2K, 4K | 4K recommended for text-heavy outputs |
| Nano Banana 2 | 512×512, 1024×1024 (default), 2K, 4K | 512px is the storyboard screening size |

### Quality Parameter

Set `quality` in the API call:
- `"standard"` — Default. Fast, good for ideation.
- `"high"` — Recommended for production assets, text rendering, detailed compositions.

### Batch Generation

Use the `n` parameter to generate multiple candidates in one call. Combine with 512px output on Nano Banana 2 for cheap screening:

```python
response = client.images.generate(
    model="gemini-3.1-flash-image",
    prompt="...",
    n=6,
    size="512x512"
)
```

Pick the strongest composition, tighten the prompt, regenerate at 2K or 4K.

---

## 4. Prompt Structure

Google's guidance favors **narrative prompting** over keyword lists. The model responds better to scene description than disconnected adjectives.

### The Narrative Prompt Pattern

Nano Banana models are Markdown-aware. Use structure:

```
TASK: Create a [deliverable type] showing [subject].

SCENE:
[Describe the scene narratively — who/what is present, where it is, what's happening.
Think like a cinematographer: describe the shot, not a wish list.]

CAMERA:
[Shot type] at [focal length feel], [angle], [framing].
[Depth of field], [focus point].

LIGHTING:
[Direction], [quality (soft/hard)], [color temperature], [time of day].
[Practical light sources if relevant.]

STYLE:
[Rendering approach — photorealistic / illustration / painterly / etc.]
[Material finish, texture quality, color palette.]

TEXT (if any):
"[Exact wording]" in [font/weight/size], [color hex], [position].

CONSTRAINTS:
- MUST: [non-negotiable requirements]
- MUST NOT: [explicit exclusions]
- Style lock: [state canonical style if this is part of a series]
```

### Why Narrative Beats Keywords

| Approach | Example | Result |
|----------|---------|--------|
| Keyword soup | "woman, red dress, city, night, 8k, masterpiece" | Generic, uncontrolled composition |
| Narrative | "A woman in a fitted red dress stands at a rain-slicked intersection at 2 AM, neon signs reflecting off the wet asphalt. Medium shot at 85mm, shallow depth of field." | Specific framing, mood, and spatial logic |

### Camera Language

Nano Banana responds well to photography terminology. Use it to control framing:

| Term | Effect |
|------|--------|
| `85mm portrait lens` | Compressed perspective, shallow DOF, flattering proportions |
| `24mm wide-angle` | Expanded perspective, environmental context |
| `Three-point lighting` | Professional, controlled illumination |
| `Available light` | Naturalistic, contextual |
| `f/1.4 bokeh` | Strong background blur, subject isolation |
| `f/11 deep focus` | Everything sharp, documentary feel |
| `Eye-level medium shot` | Standard conversational framing |
| `Low-angle hero shot` | Power, authority, drama |
| `Bird's-eye overhead` | Pattern, layout, spatial relationship |

### Hex Color Codes

Nano Banana interprets hex codes directly. Use them instead of color names:

```
Background: #F5F0E8 (warm ivory)
Primary accent: #C0392B (fire-engine red)
Text color: #1B2838 (dark navy)
```

---

## 5. Reference Images

### Allocation Strategy

Nano Banana models support up to 14 reference images, allocated by role:

**Nano Banana Pro (14 total):**
| Slots | Role | What to provide |
|-------|------|-----------------|
| 1–6 | Object references | Product shots, props, architectural elements |
| 7–11 | Character references | Face, body, outfit, expression angles |
| 12–14 | Style references | Color grade, rendering mood, visual treatment |

**Nano Banana 2 (14 total):**
| Slots | Role | What to provide |
|-------|------|-----------------|
| 1–10 | Object references | Products, props, environments, textures |
| 11–14 | Character references | Face, body, outfit angles |

### The Reference Pack Pattern

Don't upload near-duplicates. Build a **role-separated reference kit** with diverse but compatible views:

**Character reference kit (4 images):**
1. Neutral front view (clean lighting, plain background)
2. Three-quarter view (shows depth of facial features)
3. Profile view (nose, chin, ear shape)
4. Full-body or costume view (proportions, outfit details)

**Product reference kit (up to 6 images):**
1. Hero angle (the "money shot")
2. Alternate angle (reveals hidden geometry)
3. Detail/texture close-up
4. Scale reference (product in context)
5. Color/material swatch
6. Packaging or branding element

**Style reference kit (up to 3 images):**
1. Color grade / palette target
2. Rendering style exemplar
3. Mood / atmosphere reference

### Reference Image Prompt Pattern

When using references, describe each image's role and what to extract:

```
Reference Image 1 (CHARACTER — face): Front-view headshot of the subject.
TAKE: exact facial features, skin tone, eye color, hairstyle.
IGNORE: background, lighting, clothing.

Reference Image 2 (CHARACTER — body): Full-body shot of the subject.
TAKE: body proportions, height, posture.
IGNORE: background, expression.

Reference Image 3 (OBJECT — product): The handbag from the hero angle.
TAKE: exact shape, leather texture, hardware color, stitching.
IGNORE: the surface it's sitting on, the lighting setup.

Reference Image 4 (STYLE): Wes Anderson film still.
TAKE: color palette (pastels), symmetrical composition tendency, flat lighting.
IGNORE: the specific subject or scene.
```

### Key Principle: Diverse Views Beat Duplicate Selfies

Five near-identical selfies waste reference slots. Five diverse views (front, three-quarter, profile, full-body, detail) give the model enough information to infer stable 3D identity. This applies to characters, products, architectural elements, and locations.

---

## 6. Text Rendering

### Model Comparison

| Model | Accuracy | Best Practice |
|-------|----------|---------------|
| Nano Banana (original) | Good | Markdown-formatted text instructions, ALL CAPS for emphasis |
| Nano Banana Pro | Near-perfect | Name exact fonts and weights: "Roboto Bold 24pt" |
| Nano Banana 2 | Good-to-excellent | Spell-check matters; quote exact text |

### Text Prompting Rules

1. **Quote exact text**: `The title reads "ANNUAL REPORT 2026"` — never paraphrase.
2. **Specify font** (Nano Banana Pro): `"Times New Roman Bold, 36pt, #1B2838"`.
3. **Spell unusual words letter by letter**: `"AÇAÍ" — A, C with cedilla, A with acute accent, I`.
4. **State hierarchy**: `"Title largest, subtitle half the title size, body text smallest."`.
5. **Specify placement**: `"Title centered top third, body text left-aligned below."`.
6. **Use text-first workflow**: Get the wording finalized, then ask the model to render it into the image. Don't try to fix text and composition simultaneously.

### Markdown-Aware Formatting

Nano Banana models interpret Markdown natively. Use it:

```
## Header-Level Importance
- **Bold for emphasis** in constraint lists
- `Monospace` for exact values (hex codes, sizes)
- Numbered lists for sequential requirements
```

---

## 7. System Prompts

**Available on:** Nano Banana Pro and Nano Banana 2.

System prompts lock consistent behavior across multiple generations within a session. Use them for:

### Style Consistency Across a Series

```
SYSTEM: You are generating images for a children's book illustration series.
Style: warm watercolor with visible brush texture, soft edges, muted earth tones.
Palette: #E8D5B7 (warm parchment), #6B8E6B (sage green), #B85C38 (terracotta), #4A6FA5 (dusty blue).
Characters must maintain consistent proportions and features across all generations.
Never use photorealistic rendering. Never add text unless explicitly requested.
All backgrounds should feel hand-painted with visible paper texture.
```

### Brand Guidelines Enforcement

```
SYSTEM: All generated images must follow BrandCo visual guidelines:
- Primary color: #2563EB (BrandCo Blue)
- Secondary: #F59E0B (BrandCo Gold)
- Typography: Inter for headlines, Source Sans Pro for body
- Style: clean, modern, minimal — no gradients, no 3D effects, no drop shadows
- White space: generous — never fill more than 60% of the canvas
- Photography style: natural light, candid feel, diverse representation
```

### Medical/Educational Context

```
SYSTEM: You are generating medical education illustrations.
All outputs must be clearly educational/diagrammatic — never mimic clinical scans or PACS screenshots.
Use textbook illustration style with labeled callouts, color-coded anatomy, and clean backgrounds.
Never generate fake patient identifiers, hospital UI elements, or radiology watermarks.
Always include a visual cue (arrows, labels, color coding) that marks the image as explanatory.
```

---

## 8. Google Search Grounding

**Available on:** Nano Banana Pro and Nano Banana 2.

Search grounding lets the model verify facts against real-time information during generation. This is especially valuable for:

- **Data-driven infographics**: The model can ground statistics, rankings, or market data.
- **Factual visualizations**: Maps, timelines, org charts with current information.
- **Multilingual content**: Verify translations and cultural references.
- **Current events**: Generate visuals that reflect recent developments.

### How to Invoke Grounding

In the API, enable the search grounding tool:

```python
response = client.images.generate(
    model="gemini-3-pro-image",
    prompt="Create an infographic showing the top 5 programming languages by market demand in 2026. Use current data.",
    tools=[{"google_search": {}}]
)
```

### When NOT to Use Grounding

- Creative/fictional content — grounding may fight your invented scenarios.
- Character design — the model may default to canonical versions of known characters.
- Speed-sensitive workflows — grounding adds latency.
- Outputs where you control the data — don't let the model override your numbers.

---

## 9. JSON Schema Prompting

### What This Is (and Isn't)

JSON schema prompting is a **community practice** for Nano Banana, not an official API feature. The Gemini API's structured output (`responseSchema`) is text-only — images are returned as base64 data, not as structured JSON fields.

The practice works because Nano Banana's 32K context window and Markdown awareness make it effective at parsing structured input. JSON serves as a **planning and control layer** that makes prompt parameters explicit, version-controllable, and CI-friendly.

### The Pattern

Build a JSON object that encodes all prompt decisions, then either:
- (A) Send the JSON directly as the prompt (Nano Banana parses it well), or
- (B) Use the JSON as your internal spec and serialize it into natural language for the API call.

Option (A) works well for Nano Banana. Option (B) is required for models that don't handle JSON prompts natively (including gpt-image-2).

### JSON Schema Template

```json
{
  "task": "character_sheet | product_hero | editorial_portrait | infographic | storyboard",
  "subject": {
    "name": "string — stable name used across all prompts",
    "description": "one-sentence visual description",
    "identity_features": [
      "distinctive visual trait 1",
      "distinctive visual trait 2"
    ]
  },
  "references": {
    "character": ["front.jpg", "three_quarter.jpg"],
    "object": ["product_hero.jpg"],
    "style": ["mood_board.jpg"]
  },
  "scene": {
    "environment": "where it takes place",
    "time_of_day": "morning | noon | golden_hour | dusk | night",
    "weather": "clear | overcast | rain | fog"
  },
  "camera": {
    "shot_type": "extreme_close_up | close_up | medium | full_body | wide | extreme_wide",
    "focal_length": "24mm | 35mm | 50mm | 85mm | 135mm | 200mm",
    "angle": "eye_level | low_angle | high_angle | birds_eye | worms_eye",
    "depth_of_field": "shallow | moderate | deep",
    "aspect_ratio": "1:1 | 4:3 | 16:9 | 9:16 | 3:4 | 1:4 | 4:1"
  },
  "lighting": {
    "type": "natural | studio | practical | mixed",
    "direction": "front | side | back | rim | overhead",
    "quality": "soft | hard | diffused",
    "color_temperature": "warm_2700K | neutral_5000K | cool_6500K"
  },
  "rendering": {
    "style": "photorealistic | illustration | watercolor | anime | 3d_render | pixel_art",
    "palette": ["#hex1", "#hex2", "#hex3"],
    "texture": "smooth | grainy | painterly | matte | glossy",
    "quality": "standard | high"
  },
  "text": {
    "content": "exact text in quotes",
    "font": "font name, weight, size",
    "color": "#hex",
    "position": "where on the canvas"
  },
  "constraints": {
    "must": ["requirement 1", "requirement 2"],
    "must_not": ["exclusion 1", "exclusion 2"],
    "style_lock": "the canonical style — do not drift"
  }
}
```

### When JSON Prompting Adds Value

| Scenario | Benefit |
|----------|---------|
| Team authoring (multiple people writing prompts) | Consistent structure, reviewable diffs |
| Production pipeline (CI/CD for visual assets) | Version-controlled, lintable, testable |
| Large reference packs (10+ images with roles) | Clear role assignment per reference |
| Character bibles (multi-scene consistency) | Reusable identity specs |
| A/B testing prompt variations | Change one JSON field, regenerate |

### When to Skip JSON

- One-off creative exploration — natural language is faster.
- Simple single-subject generations — JSON adds overhead without benefit.
- When targeting gpt-image-2 — it doesn't parse JSON prompts natively; serialize to text.

---

## 10. Editing

The editing pattern is consistent across both Nano Banana and gpt-image-2: **state exactly what changes and exactly what must not change.**

### The Change/Preserve Pattern

```
CHANGE: Replace the subject's jacket with a navy blazer.
PRESERVE: The exact face, hairstyle, skin tone, pose, background, lighting, composition, and color grade. Everything not listed under CHANGE stays identical to the input image.
```

### Nano Banana Editing Rules

1. **Change one element at a time.** Bundling changes (new outfit + new background + new expression) increases drift risk.
2. **Describe the desired state positively.** "The background is a warm cafe interior" works better than "remove the outdoor background and add an indoor one."
3. **Semantic negatives over lists.** Instead of "no blue, no green, no purple in the background," say "the background uses only warm earth tones — browns, ambers, and muted oranges."
4. **Restate identity invariants.** Every edit prompt that touches a character should restate: face, hair, eye color, body type, distinguishing marks.
5. **If drift starts to accumulate, restart the conversation.** Google explicitly recommends this — don't iterate 15 times on a drifting result.

### Inpainting Template

```
Edit this image. Change ONLY the following:
- [Specific change 1]
- [Specific change 2]

Keep EVERYTHING ELSE exactly the same:
- Same face, hairstyle, skin tone, expression
- Same pose and body proportions
- Same lighting direction, color temperature, and shadow quality
- Same background and environmental details
- Same visual style and rendering approach

If any preserved element changes, the edit is incorrect.
```

---

## 11. Character Consistency

### The Character Bible Pipeline

Character consistency across multiple generations is a pipeline problem, not a single-prompt problem. The recommended sequence:

#### Step 1: Create the Anchor Image

Generate one canonical reference image with:
- Clean, plain background (no scene context)
- Three-quarter view showing facial structure
- Full body visible, neutral pose
- Even, soft lighting — no dramatic shadows

```
Create a clean character anchor for [NAME]. Three-quarter view, full body,
plain #F0EDE8 background. Neutral expression, even studio lighting.

KEY IDENTITY FEATURES:
- Age: [range]
- Build: [body type]
- Skin: [tone, hex if precise]
- Hair: [color, length, style — be very specific]
- Eyes: [color, shape]
- Distinctive marks: [freckles, scar, birthmark — concrete]
- Default outfit: [garment by garment]

This is a character anchor — not a story illustration.
No environmental context, no dramatic poses, no props.
Style: [the canonical rendering style for this character].
```

#### Step 2: Build the Character Bible

Document 5–10 durable visual traits that must persist:

```
CHARACTER BIBLE — [NAME]
1. Hair: shoulder-length wavy auburn, side-parted left, cowlick at crown
2. Eyes: warm hazel, almond-shaped, slight upturn at outer corners
3. Skin: light olive (#D4A574), freckles across nose and cheeks
4. Build: athletic, 5'7", broad shoulders relative to frame
5. Face: heart-shaped, prominent cheekbones, slightly cleft chin
6. Scar: thin 2cm scar above left eyebrow (always visible)
7. Default outfit: olive canvas jacket, white crew-neck tee, dark jeans
8. Footwear: worn brown leather boots
9. Posture: slightly forward-leaning, hands often in jacket pockets
10. Style commitment: Studio Ghibli-influenced watercolor illustration
```

#### Step 3: Create the Reference Pack

Generate 3–5 reference images of the anchor character from different angles:
- Front view
- Three-quarter view (from Step 1)
- Profile view
- Full-body (if Step 1 was three-quarter crop)
- Optional: key expression (smile, concern, determination)

Upload these as character reference images (slots 11–14 on Nano Banana 2, slots 7–11 on Pro).

#### Step 4: Generate Scenes with Restatement

Every scene prompt must:
1. Pass the reference pack as character images
2. Restate the character bible (not just "same character" — list the traits)
3. Change ONE major dimension per generation (scene OR outfit OR expression)
4. State the style commitment

```
Reference Images 1–4: Character reference pack for [NAME].

PRESERVE from references (restate every turn):
- [NAME]'s exact face: [hair, eyes, marks from bible]
- Body type and proportions from reference pack
- Canonical style: [STYLE] — do not shift rendering approach

NEW SCENE:
[NAME] is [ACTION] in [SETTING]. Expression: [EMOTION].
Camera: [shot type, angle].
Lighting: [new scene's lighting].

CHANGE (what's new):
- Setting: [describe]
- Action: [describe]
- Expression: [describe]

CONSTRAINTS:
- Style must match the canonical [STYLE] from the reference pack
- If face, hair color, eye color, body type, or distinctive marks differ from the references, the output is incorrect
```

#### Step 5: Re-Anchor Every ~10 Frames

In long sequences (storybooks, comics, ad campaigns), character drift accumulates. Every ~10 generations:
1. Compare the latest output to the original anchor
2. If drift is visible, regenerate a fresh anchor in the current scene's style
3. Use the fresh anchor as the new reference going forward

If the outfit changes permanently mid-sequence, regenerate a new anchor in the new outfit.

---

## 12. Storyboard and Veo Pipeline

### Still-First Storyboarding

The key principle: **the still image carries static decisions; the video prompt carries motion decisions.**

| Decision Type | Belongs In | Examples |
|---------------|-----------|----------|
| Static | Image prompt | Subject identity, scene layout, camera angle, lighting, color palette, costume |
| Motion | Video prompt | Camera movement, subject action, timing, environmental motion |

### The Cheap-Candidate Workflow (Nano Banana 2)

1. **Screen at 512px**: Generate 6–20 low-resolution candidates quickly.
2. **Select the strongest composition**: Pick based on framing, spatial logic, readability.
3. **Tighten the prompt**: Add specific constraints based on the winning candidate.
4. **Regenerate at production resolution**: 2K or 4K for the final keyframe.

This workflow is especially cost-effective with Nano Banana 2's 512px output option.

### Storyboard Grid Template

```
TASK: Create a [N]-panel storyboard grid for a [duration]-second [genre] [content type].

LAYOUT:
[columns] columns x [rows] rows, left-to-right reading order.
Thin neutral gutters (#E0E0E0, 2px) between panels. No captions or text labels.

CHARACTER:
Same [character] in all panels — identical face, hair, outfit, and proportions.
[Restate character bible here]

LOCATION:
[Setting description — concrete environmental detail, time of day, lighting.]

PANEL BEATS:
1) [Shot type] — [what happens in this panel]
2) [Shot type] — [what happens]
3) [Shot type] — [what happens]
...
[N]) [Shot type] — [what happens]

CONSTRAINTS:
- One consistent color grade across all panels
- Realistic lens logic (wide for establishing, tight for emotion)
- Same character identity in every panel — no redesign between panels
- No extra people unless specified
- No text, captions, or panel numbers
```

### Nano Banana to Veo Pipeline

Google officially supports feeding Nano Banana keyframes into Veo for video generation. Two modes:

#### Ingredients to Video (up to 3 reference images)

Use when you want the video model to create a scene using visual elements from your references:

```
Step 1 (Nano Banana 2): Generate the hero keyframe at 2K.
Step 2 (Nano Banana 2): Generate 1–2 supporting angles or detail shots.
Step 3 (Veo): Feed all 3 as "ingredients" with a motion-only prompt:

"The camera slowly dollies forward. The subject turns to face the camera
and smiles. Wind gently moves their hair. Hold for 2 seconds on the smile.
Maintain the exact lighting, color grade, and visual style from the references."
```

#### Frames to Video (start + end keyframes)

Use when you want smooth interpolation between two composed frames:

```
Step 1 (Nano Banana 2): Generate the START frame — subject in pose A.
Step 2 (Nano Banana 2): Generate the END frame — same subject in pose B,
    same setting, same lighting, same style.
Step 3 (Veo): Feed start and end frames with a transition prompt:

"Smoothly transition from the start frame to the end frame over 4 seconds.
The subject [describes the action]. Camera [describes any camera motion].
Maintain consistent identity, lighting, and style throughout."
```

### What Makes a Good Keyframe

A still image destined for video must have:
- **Clear subject** with readable silhouette
- **Stable framing** — nothing awkwardly cropped
- **Simple background** — clutter confuses the video model
- **No motion blur** — the still should look "frozen in time"
- **Room for motion** — leave space in the frame for the intended movement
- **Consistent lighting direction** — shadows must make physical sense for animation

---

## 13. Medical Imaging Considerations

### Two-Bucket Framework

Medical image generation must be split into two distinct categories with different governance requirements:

#### Bucket 1: Educational and Communication Visuals (Lower Risk)

Anatomy explainers, pathology schematics, poster figures, slides, journal-style diagrams, patient education graphics, workflow illustrations.

**Prompt pattern:**
```
Create a clean educational medical illustration — NOT a real clinical scan.
Topic: [anatomical structure / pathology / procedure].
Output format: textbook-style labeled figure with [layout description].
Visual style: high-clarity medical textbook illustration, anatomically plausible,
muted color palette, publication-quality spacing.

LABELS: [Arrow 1] → "[label]"; [Arrow 2] → "[label]".

CONSTRAINTS:
- Synthetic educational diagram only
- No fake patient identifiers, no hospital UI, no radiology watermarks
- No attempt to mimic a real PACS screenshot or clinical scan
- Must be unmistakably explanatory: labels, arrows, color coding, or schematic style
- Clean white or light neutral background
```

#### Bucket 2: Synthetic Clinical-Looking Imagery (Higher Risk)

Radiographs, MRIs, CT-like views, pathology slides, segmentation targets, augmentation datasets.

**Governance requirements:**
- Log every prompt with full provenance
- Encode acquisition assumptions explicitly (modality, view, patient demographics)
- Vary demographics and acquisition artifacts deliberately to avoid bias
- Keep outputs segregated, labeled as synthetic, and provenance-tracked
- Never use for diagnosis, treatment, or clinical decisions
- Follow institutional review and regulatory requirements

**This bucket requires institutional oversight, not just better prompting.** The RSNA reported in March 2026 that AI-generated deepfake X-rays were realistic enough to fool radiologists. Synthetic clinical imagery is powerful and dangerous simultaneously.

### Model Selection for Medical Work

| Medical Task | Recommended | Why |
|-------------|-------------|-----|
| Teaching diagrams, paper figures, explainers | gpt-image-2 or Nano Banana Pro | OpenAI has the clearest cookbook; NB Pro has search grounding for factual accuracy |
| Synthetic modality images for research | Nano Banana (community workflows) | Stronger visible public experimentation footprint |
| Patient education graphics | Either | Both handle labeled diagrams well |

---

## 14. Anti-Patterns

### Keyword Soup

```
BAD:  "woman red dress city night 8k masterpiece best quality ultra detailed"
GOOD: "A woman in a fitted red dress stands at a rain-slicked intersection at 2 AM.
       Medium shot at 85mm, f/2.8 shallow depth of field. Neon signs reflect off
       the wet asphalt. Natural available light from storefronts."
```

### Near-Duplicate References

Don't upload 5 similar selfies. Upload diverse views: front, three-quarter, profile, full-body, detail. Each reference should contribute unique geometric information.

### "Do Not" Overload

```
BAD:  "No blue, no green, no purple, no gradients, no text, no watermark, no border"
GOOD: "Warm earth-tone palette only — browns, ambers, muted oranges. Plain composition
       with no text, watermarks, or decorative borders."
```

Describe the desired state positively. Use narrow negatives only for edit invariants.

### Style Drift Across Sessions

Without a system prompt, each new generation may drift in style. Lock style with:
- System prompts (Nano Banana Pro and 2)
- Style reference images (slots 12–14 on Pro)
- Explicit style commitment statements in every prompt

### Over-Iterating on a Drifting Result

If the output has drifted significantly from your intent after 3–4 refinement turns, **restart the conversation** rather than trying to steer it back. Drift compounds.

### Mixing All Changes at Once

Don't change scene + outfit + expression + camera angle simultaneously. Change one major dimension per generation to isolate what works.

---

## 15. Iteration Strategy

### Decision Tree

```
First generation
│
├─ 90%+ correct → Accept or make one minor tweak
│
├─ 70-90% correct → Refine in the same conversation
│  ├─ "The hair color reads ash blond — restore to auburn matching Reference Image 1"
│  ├─ "Shift the camera angle 15° left to show more of the environment"
│  └─ "The lighting is too flat — add rim light from upper-right"
│
├─ 40-70% correct → Rewrite the prompt with tighter constraints
│  └─ Don't iterate 5 times on a mediocre starting point
│
└─ <40% correct → Different approach
   ├─ Different model (Nano Banana 2 → Pro, or → gpt-image-2)
   ├─ Add reference images
   └─ Simplify the prompt — you may be asking for too much at once
```

### Refinement Language

Use specific, measurable corrections:

| Vague (Model Guesses) | Specific (Model Executes) |
|----------------------|--------------------------|
| "Make it better" | "Increase contrast between subject and background by 30%" |
| "Fix the face" | "The jawline is too narrow compared to Reference 1 — widen to match" |
| "More dramatic lighting" | "Add a hard key light from upper-left at 45°, deep shadows on the right side of the face" |
| "Wrong style" | "This reads as photorealistic — shift to the watercolor illustration style from the style reference" |

---

## 16. Quality Checklist

### Before Sending the Prompt

- [ ] **Deliverable type stated** — the model knows what artifact to produce
- [ ] **Subject described narratively** — not keyword soup
- [ ] **Camera/composition specified** — shot type, angle, focal length feel
- [ ] **Lighting described** — direction, quality, color temperature
- [ ] **Style commitment stated** — especially if part of a series
- [ ] **Reference images allocated by role** — each has a stated purpose
- [ ] **Text quoted exactly** — with font, size, color, and position
- [ ] **Constraints use Must/Must Not** — not vague preferences
- [ ] **One major change per generation** — don't bundle everything
- [ ] **Hex codes for critical colors** — not color names

### After Receiving the Output

- [ ] **Subject matches description** — face, body, outfit, identity features
- [ ] **Composition matches request** — shot type, framing, aspect ratio
- [ ] **Text is accurate** — every character, every word, correct spelling
- [ ] **Style is consistent** — matches the canonical style or style reference
- [ ] **No unwanted elements** — no extra people, no phantom text, no artifacts
- [ ] **Color palette matches** — hex codes rendered correctly
- [ ] **Lighting is physically plausible** — shadows consistent with stated light source
- [ ] **Scale is realistic** — subject proportions make sense relative to environment

---

## 17. Templates

### Template 1: Photorealistic Portrait

```
TASK: Create a photorealistic editorial portrait.

SUBJECT:
[Name/description], [age range], [build], [skin tone].
Hair: [specific description].
Eyes: [color, shape].
Expression: [specific emotion, not just "happy"].
Outfit: [garment by garment].

CAMERA:
85mm portrait lens, f/2.0 shallow depth of field.
Three-quarter framing, eye-level, subject fills 60% of frame.
Focus: eyes sharp, background creamy bokeh.

LIGHTING:
Soft key light from upper-left at 45°, large softbox.
Fill light from right at 1:3 ratio.
Subtle hair light from behind-right.
Color temperature: 5200K neutral daylight.

ENVIRONMENT:
[Background description — keep simple for portraits].

STYLE: Photorealistic editorial photography. Natural skin texture — visible pores,
subtle imperfections. No airbrushed smoothing.

CONSTRAINTS:
- MUST: Natural skin texture, catchlights in eyes, realistic fabric draping
- MUST NOT: Plastic/airbrushed skin, uncanny valley smoothness, lens flare
- Format: 3:4 portrait, quality="high"
```

### Template 2: Infographic with Search Grounding (Nano Banana Pro)

```
TASK: Create a data-driven infographic.

TOPIC: [Subject — use current data via search grounding].

LAYOUT:
Vertical 9:16 format for mobile.
Title bar at top (20% height).
3 data sections stacked below (each ~25% height).
Source attribution bar at bottom (5% height).

DATA SECTIONS:
Section 1: [Metric] — large number, subtitle, small supporting chart.
Section 2: [Metric] — large number, subtitle, small supporting chart.
Section 3: [Comparison or trend] — bar chart or line chart.

TYPOGRAPHY:
Title: "[EXACT TITLE TEXT]" in Inter Bold, 28pt, #FFFFFF on #2563EB.
Section headers: Inter SemiBold, 16pt, #1E293B.
Data numbers: Inter Bold, 48pt, #2563EB.
Body text: Source Sans Pro Regular, 12pt, #475569.
Source line: Source Sans Pro Italic, 10pt, #94A3B8.

STYLE:
Clean, modern, corporate. Flat design — no 3D, no gradients, no drop shadows.
Palette: #2563EB (primary), #F59E0B (accent), #F8FAFC (background), #1E293B (text).

CONSTRAINTS:
- MUST: All data values legible at mobile zoom
- MUST: Source attribution visible
- MUST NOT: Decorative elements that don't convey information
- MUST NOT: Fake or placeholder data — use search grounding for current values
- Quality: "high"
```

### Template 3: Character Sheet

```
TASK: Create a character reference sheet for [NAME].

LAYOUT:
Landscape 16:9.
Left half: full-body front view (60% of left panel height) + head close-ups below (3 small: front, three-quarter, profile).
Right half: 6-panel grid showing expression variations (happy, angry, sad, surprised, determined, neutral).
Bottom strip: color palette swatches + outfit detail callouts.

CHARACTER — [NAME]:
[Full character bible — 5-10 traits. See Section 11.]

RENDERING:
Style: [canonical style — anime / illustration / painterly / etc.].
Clean white background for all panels.
Even, soft studio lighting — no dramatic shadows.
Consistent proportions across all panels.

LABELS:
Small, clean sans-serif labels for each section:
"FRONT" | "3/4" | "PROFILE" | expression names under each expression panel.
Color palette: hex codes under each swatch.

CONSTRAINTS:
- MUST: Same face, proportions, and outfit in every panel
- MUST: Color palette swatches match the actual colors used in the character
- MUST NOT: Environmental backgrounds in any panel
- MUST NOT: Dynamic action poses — these are reference poses
- Style: [CANONICAL STYLE] — locked for all future [NAME] generations
- Quality: "high"
```

### Template 4: Storyboard for Video (Nano Banana 2 → Veo)

```
TASK: Create a [N]-panel storyboard grid for a [duration]-second [content type].

LAYOUT:
[columns] columns x [rows] rows.
Left-to-right, top-to-bottom reading order.
Thin #CCCCCC gutters (2px). No text, captions, or panel numbers.

CHARACTER:
[NAME] appears in all panels.
[Restate character bible — 5-10 traits.]

LOCATION:
[Detailed setting description. Time of day. Weather. Key environmental features.]

PANEL BEATS:
1) WIDE ESTABLISHING — [setting revealed, character's position in space]
2) MEDIUM — [character action, relationship to environment]
3) CLOSE-UP — [emotional beat, key detail]
4) [SHOT TYPE] — [beat description]
5) [SHOT TYPE] — [beat description]
6) HERO FRAME — [the most important single image in the sequence]

CONSTRAINTS:
- One consistent color grade across all panels: [describe]
- Same character identity in every panel — no redesign
- Each panel should work as a standalone still for Veo keyframe input
- Clear subject silhouettes — no busy backgrounds that confuse video models
- Leave compositional room for intended motion in each panel
- No motion blur — these are frozen moments
- Quality: "high" (or "standard" at 512px for screening pass)

DOWNSTREAM USE:
These panels will be fed to Veo as keyframes.
Panel 1 = start frame. Panel [N] = end frame.
Interior panels = reference for mid-sequence identity and style lock.
```

### Template 5: Product Composite (Multi-Reference)

```
REFERENCES:
Image 1 (OBJECT — product hero): [Product] from the primary marketing angle.
TAKE: exact shape, color, material, branding, proportions.
IGNORE: background, lighting.

Image 2 (OBJECT — product detail): Close-up of [specific detail].
TAKE: texture, hardware, stitching/seam quality.
IGNORE: everything else.

Image 3 (SCENE — environment): [Location/setting].
TAKE: architecture, props, depth, spatial logic, ambient color.
IGNORE: any people or products currently in the scene.

Image 4 (STYLE — color grade): [Reference image for overall mood].
TAKE: color grade, saturation, contrast, highlight/shadow tint.
IGNORE: composition, subject.

TASK:
Place the product from Images 1–2 into the scene from Image 3.
Apply the color grade from Image 4 to the entire composite.

PLACEMENT:
Product positioned [where in the scene], at [realistic scale].
Camera angle matches Image 3's perspective and vanishing points.

LIGHTING:
Match Image 3's ambient lighting direction and color temperature.
Product shadows consistent with the scene's light source.

CONSTRAINTS:
- MUST: Product shape, color, and branding exactly match Images 1–2
- MUST: Scale is physically plausible relative to the scene
- MUST: Shadows and reflections consistent with scene lighting
- MUST NOT: Alter the product design, add elements not in the references
- Quality: "high"
```

---

## Cross-Model Prompt Grammar

Both Nano Banana and gpt-image-2 respond well to the same 8-element structure. Use this as a mental checklist regardless of model:

1. **Deliverable / task mode** — What artifact are you building?
2. **Subject** — Who or what is the main focus?
3. **Action / state** — What is happening or what should differ from the reference?
4. **Environment** — Where, with what contextual logic?
5. **Camera / composition** — Shot type, framing, lens, angle, aspect ratio.
6. **Lighting / material / style** — Time of day, light direction, color grade, rendering approach.
7. **Text / labels** — Exact wording, hierarchy, placement, font.
8. **Constraints** — What must stay unchanged, what must not be added.

The same grammar works across models; only the **delivery format** differs:
- **Nano Banana**: Narrative/Markdown, JSON schema, or structured blocks
- **gpt-image-2**: Labeled sections (Scene / Subject / Key Details / Use Case / Constraints)
- **Midjourney**: Front-loaded keywords with `--` parameters
- **Stable Diffusion**: Positive/negative prompt split with `(weighting:1.4)`

---

*Guide last updated: 2026-06-23. Model IDs and capabilities reflect the state of Google's Gemini image models as of this date. Verify current API documentation for any changes to model availability, parameters, or reference image limits.*
