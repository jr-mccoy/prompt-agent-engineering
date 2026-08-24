---
title: "Image Model Selection Guide"
category: image-generation/model-selection
description: "Decision framework for choosing the right AI image model by task, budget, and workflow requirements"
techniques:
  - ST-01
  - ST-02
difficulty: beginner
tags:
  - model-selection
  - gpt-image-2
  - nano-banana
  - dall-e
  - midjourney
  - stable-diffusion
  - flux
  - ideogram
  - image-generation
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/GPT_IMAGE_2_GUIDE.md
  - domain-image-generation/NANO_BANANA_GUIDE.md
  - domain-image-generation/IMAGE_PROMPTING_GUIDE.md
  - domain-image-generation/IMAGE_GENERATION_GUIDE.md
---

# Image Model Selection Guide

**Purpose:** Choose the right AI image model for your task before writing a single prompt. Wrong model choice wastes more time than a wrong prompt — the best prompt on the wrong model still produces the wrong artifact.

**Last updated:** 2026-06-23.

---

## Quick Decision Matrix

| Task | First Choice | Why | Backup |
|------|-------------|-----|--------|
| **Polished production layouts** (infographics, slides, figures) | gpt-image-2 | Best artifact-specification workflow, strong text rendering | Nano Banana Pro (search grounding for factual data) |
| **Fast ideation / many candidates** | Nano Banana 2 | Speed + 512px screening + low cost | Midjourney (strong aesthetics per generation) |
| **Photorealistic editorial / portraits** | gpt-image-2 | Polished realism, precise editing, identity-safe refs | Nano Banana Pro (full LLM reasoning for hard compositions) |
| **Character sheets / turnarounds** | gpt-image-2 | Best one-pass multi-panel consistency | Nano Banana 2/Pro (14 refs for identity locking) |
| **Character consistency across sequences** | Nano Banana 2 or Pro | 14 reference images with role-separated allocation | gpt-image-2 (16 refs, strong anchor+reuse pattern) |
| **Multi-reference compositing** (many source images) | Nano Banana 2 | 10 object + 4 character slots with clear role allocation | gpt-image-2 (16 refs with index-role-take-ignore) |
| **Text-heavy visuals / typography** | Nano Banana Pro | Near-perfect text rendering + exact font specification | gpt-image-2 (95%+ accuracy) |
| **Data-driven / factual infographics** | Nano Banana Pro | Google Search grounding verifies data in real time | gpt-image-2 (web search during generation) |
| **Storyboard keyframes for video** | Nano Banana 2 | Speed, 512px screening, official Veo pipeline | gpt-image-2 (one-pass grid consistency) |
| **Video-ready keyframes → Veo** | Nano Banana 2 | Official Google pipeline, consumer (Flow) + API | N/A (gpt-image-2 → Seedance 2.0 is community-only) |
| **Comic page / sequential art** | gpt-image-2 | Best cross-panel consistency in one-pass grids | Nano Banana 2 (fast iteration on individual panels) |
| **Brand asset production** (consistent style across batch) | Nano Banana Pro | System prompts lock style across generations | gpt-image-2 (style commitment in each prompt) |
| **Unusual aspect ratios** (1:4, 4:1, 1:8, 8:1) | Nano Banana 2 | Only model supporting extreme ratios | gpt-image-2 (1:3 to 3:1 range) |
| **Medical education diagrams** | gpt-image-2 | Clearest cookbook support for labeled figures | Nano Banana Pro (search grounding for anatomical accuracy) |
| **Synthetic medical imagery (research)** | Nano Banana | Stronger public experimentation footprint | N/A (requires institutional oversight regardless) |
| **Logo / brand mark** | gpt-image-2 | Batch variations (`n=4`), clean vector-like output | Ideogram (strong text-in-logo rendering) |
| **Artistic / aesthetic-first images** | Midjourney | Strongest aesthetic bias, stylize parameter | Stable Diffusion + LoRAs (full style control) |
| **Full control / ControlNet / inpainting** | Stable Diffusion / Flux | ControlNet, custom LoRAs, negative prompts, local deployment | ComfyUI workflows for maximum pipeline control |
| **Multilingual text in images** | Nano Banana Pro | Search grounding + font specification across scripts | Ideogram (strong multilingual text rendering) |
| **Print-ready materials** (badge buddies, worksheets) | gpt-image-2 | See [IMAGE_GENERATION_GUIDE.md](IMAGE_GENERATION_GUIDE.md) | Nano Banana Pro (text accuracy for dense content) |

---

## Model Comparison Table

| Capability | gpt-image-2 | Nano Banana 2 | Nano Banana Pro | Midjourney v6+ | SD/Flux | Ideogram |
|------------|-------------|---------------|-----------------|----------------|---------|----------|
| **Max resolution** | 4K (3840px max edge) | 4K + 512px screening | 4K | ~2K | Unlimited (local) | 2K |
| **Aspect ratios** | 1:3 to 3:1 | Standard + extreme (1:8, 8:1) | Standard + wide | Any via `--ar` | Any | Standard |
| **Reference images** | Up to 16 | Up to 14 (10 obj + 4 char) | Up to 14 (6 obj + 5 char + 3 style) | Image prompts + `--sref` | img2img / ControlNet | Limited |
| **Text rendering** | 95%+ | Good-to-excellent | Near-perfect | Moderate | Poor-to-moderate | Excellent |
| **Search grounding** | Web search | Yes | Yes | No | No | No |
| **System prompts** | No | Yes | Yes | No | No | No |
| **Thinking mode** | Yes (revised_prompt) | No | Yes (LLM reasoning) | No | No | No |
| **Editing** | Change/preserve | Change/preserve | Change/preserve | Vary/remix | Inpainting/img2img | Limited |
| **Batch generation** | `n` parameter | `n` parameter | `n` parameter | 4 per prompt | Batch scripts | `n` parameter |
| **Video pipeline** | Community (→ Seedance 2.0) | Official (→ Veo) | Official (→ Veo) | No | AnimateDiff | No |
| **Local deployment** | No (API only) | No (API only) | No (API only) | No (cloud only) | Yes | No (API only) |
| **Prompt style** | Labeled sections | Narrative / Markdown / JSON | Narrative / Markdown | Front-loaded keywords | Positive/negative split | Style-first |
| **Cost tier** | $$$ | $ | $$ | $$ | Free (local) | $$ |

---

## Decision Flowchart

```
START: What are you making?
│
├─ Is it a VIDEO or does it feed a video model?
│  ├─ YES, targeting Google Veo → Nano Banana 2 (official pipeline)
│  ├─ YES, targeting other video models → gpt-image-2 (polished keyframes)
│  └─ NO → continue
│
├─ Does it require CURRENT/FACTUAL DATA in the image?
│  ├─ YES → Nano Banana Pro (search grounding)
│  └─ NO → continue
│
├─ Does it require EXACT TEXT rendering (typography, labels, data)?
│  ├─ YES, complex typography → Nano Banana Pro (exact font control)
│  ├─ YES, moderate text → gpt-image-2 (95%+ accuracy)
│  └─ NO or minimal text → continue
│
├─ Does it require MANY REFERENCE IMAGES (>4)?
│  ├─ YES, role-separated refs → Nano Banana 2 (14 with clear roles)
│  ├─ YES, index-and-describe → gpt-image-2 (16 with TAKE/IGNORE)
│  └─ NO → continue
│
├─ Is it a PRODUCTION LAYOUT (infographic, slide, diagram)?
│  ├─ YES → gpt-image-2 (artifact specification pattern)
│  └─ NO → continue
│
├─ Is SPEED / COST the primary constraint?
│  ├─ YES → Nano Banana 2 (fastest, 512px screening)
│  └─ NO → continue
│
├─ Is AESTHETIC QUALITY the primary goal?
│  ├─ YES → Midjourney (strongest aesthetic bias)
│  └─ NO → continue
│
├─ Do you need FULL LOCAL CONTROL (ControlNet, custom models)?
│  ├─ YES → Stable Diffusion / Flux
│  └─ NO → continue
│
└─ Default → gpt-image-2 (most versatile single model)
```

---

## Prompt Format by Model

Each model expects prompts in a different shape. The same creative intent should be formatted differently:

### Same Scene, Four Formats

**Intent:** A woman in a red dress at a rainy intersection at night.

**gpt-image-2** (labeled sections):
```
SCENE: A rain-slicked urban intersection at 2 AM. Neon signs from storefronts
reflect off the wet asphalt in streaks of pink and cyan.

SUBJECT: A woman, late 20s, wearing a fitted crimson red (#DC143C) dress,
standing at the curb, looking down the empty street.

KEY DETAILS: Medium shot, 85mm lens feel, f/2.0 shallow DOF. Background
bokeh from neon signs. Natural available light from storefronts only.

USE CASE: Editorial fashion photography for a magazine spread.

CONSTRAINTS: Photorealistic. Natural skin texture. No lens flare.
No other people in frame. Dress color must be #DC143C.
```

**Nano Banana** (narrative/Markdown):
```
TASK: Create a photorealistic editorial fashion photograph.

A woman in her late 20s stands at a rain-slicked urban intersection at 2 AM.
She wears a fitted crimson red dress (#DC143C), looking down an empty street.
Neon signs from nearby storefronts reflect off the wet asphalt in streaks of
pink and cyan.

CAMERA: 85mm portrait lens, f/2.0 shallow depth of field. Medium shot,
eye-level. Background dissolves into creamy bokeh of neon colors.

LIGHTING: Available light only — neon storefronts as practical sources.
No additional fill. Natural skin texture with visible pores.

CONSTRAINTS:
- MUST: Photorealistic, natural skin, dress exactly #DC143C
- MUST NOT: Other people, lens flare, airbrushed skin
- Quality: "high"
```

**Midjourney** (front-loaded keywords):
```
editorial fashion photograph, woman late 20s in fitted crimson red dress
standing at rain-slicked urban intersection at 2AM, neon reflections on
wet asphalt, 85mm lens f/2.0 shallow DOF, available neon light only,
natural skin texture, editorial magazine quality
--ar 3:4 --v 6 --style raw --s 50 --no lens flare extra people
```

**Stable Diffusion** (positive/negative split):
```
Positive: (editorial fashion photograph:1.3), woman late 20s, fitted crimson
red dress, rain-slicked urban intersection, night, 2AM, (neon reflections:1.2)
on wet asphalt, 85mm lens, (shallow depth of field:1.3), available neon light,
(natural skin texture:1.2), magazine quality

Negative: lens flare, extra people, airbrushed skin, watermark, text,
blurry, low quality, deformed
```

---

## When to Use Multiple Models

Some workflows benefit from using different models at different stages:

| Workflow | Stage 1 | Stage 2 | Stage 3 |
|----------|---------|---------|---------|
| **Storyboard → Video** | Nano Banana 2 (512px candidates) | Nano Banana 2 (2K hero frames) | Veo (motion) |
| **Character Development** | gpt-image-2 (anchor + sheet) | Nano Banana 2 (scene variants) | Either (final polish) |
| **Brand Campaign** | Nano Banana Pro (system prompt, style lock) | gpt-image-2 (hero assets) | Nano Banana 2 (batch variants) |
| **Data Visualization** | Nano Banana Pro (grounded data) | gpt-image-2 (polished layout) | — |
| **Concept Art → Production** | Midjourney (aesthetic exploration) | gpt-image-2 (production refinement) | SD/Flux (specific edits) |

---

## Dead Pipelines (Do Not Use)

| Claimed Pipeline | Status | What Actually Works |
|-----------------|--------|-------------------|
| gpt-image-2 → Sora | **Dead.** Sora consumer app shut down April 26, 2026. API discontinued September 24, 2026. | gpt-image-2 → Seedance 2.0 (ByteDance) for storyboard-to-video (community workflow) |

---

## Links to Model-Specific Guides

- **gpt-image-2:** [GPT_IMAGE_2_GUIDE.md](GPT_IMAGE_2_GUIDE.md) + [12 production prompts](gpt-image-2/)
- **Nano Banana family:** [NANO_BANANA_GUIDE.md](NANO_BANANA_GUIDE.md)
- **Cross-model reference:** [IMAGE_PROMPTING_GUIDE.md](IMAGE_PROMPTING_GUIDE.md)
- **Print-ready materials:** [IMAGE_GENERATION_GUIDE.md](IMAGE_GENERATION_GUIDE.md)
- **Video (Veo):** [VIDEO_GENERATION_GUIDE.md](VIDEO_GENERATION_GUIDE.md)

---

*Model capabilities and pricing reflect the state of the market as of 2026-06-23. Verify current documentation before production use.*
