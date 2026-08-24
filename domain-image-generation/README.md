# Domain: Image Generation

**Purpose:** Prompts that generate image creation prompts for AI image models (Nano Banana, DALL-E, Midjourney, etc.).

---

## Start Here

### Which Model Should I Use?

**[IMAGE_MODEL_SELECTION_GUIDE.md](IMAGE_MODEL_SELECTION_GUIDE.md)** — Decision framework for choosing the right AI image model by task, budget, and workflow. Covers gpt-image-2, Nano Banana (all three models), Midjourney, Stable Diffusion/Flux, and Ideogram with a quick decision matrix, comparison table, and decision flowchart.

**Start here if you're unsure which model to target.**

### GPT Image 2 Guide (OpenAI)

**[GPT_IMAGE_2_GUIDE.md](GPT_IMAGE_2_GUIDE.md)** — Comprehensive prompting guide for OpenAI's flagship `gpt-image-2` (released April 2026). Native thinking mode, 95%+ text rendering, web search during generation, up to 16 reference images, native 4K, 1:3 to 3:1 aspect ratios.

Covers: parameters (size, quality, n), the 5-section prompt structure, text rendering contract, multi-image references, thinking mode, web search, change/preserve edit pattern, 12 use case strategies, anti-patterns, troubleshooting, validation checklist, and templates.

**Production prompts:** [gpt-image-2/](gpt-image-2/) — 12 ready-to-use prompts that apply this guide.

**Start here for any prompt targeting `gpt-image-2`.**

### Nano Banana Guide (Google Gemini Image Models)

**[NANO_BANANA_GUIDE.md](NANO_BANANA_GUIDE.md)** — Comprehensive prompting guide for Google's Nano Banana image model family: Nano Banana (`gemini-2.5-flash-image`), Nano Banana Pro (`gemini-3-pro-image`), and Nano Banana 2 (`gemini-3.1-flash-image`).

Covers: model selection within the family, parameters, narrative prompt structure, reference image allocation (up to 14 by role), text rendering, system prompts, Google Search grounding, JSON schema prompting, editing, character consistency pipeline, storyboard + Veo pipeline, medical imaging considerations, anti-patterns, iteration strategy, and 5 production templates.

**Start here for any prompt targeting a Nano Banana / Gemini image model.**

### Comprehensive Image Prompting Guide

**[IMAGE_PROMPTING_GUIDE.md](IMAGE_PROMPTING_GUIDE.md)** — Complete reference for crafting effective prompts across **all AI image generation models** and visual output types.

Covers the full spectrum from photorealistic photography to structured diagrams:
- **5-Layer Prompt Framework** — Subject, environment, style, technical specs, constraints
- **Subject-specific techniques** — People, landscapes, products, architecture, animals
- **Composition and camera control** — Framing, lens simulation, composition rules
- **Style and aesthetic direction** — Photography styles, illustration styles, style mixing
- **Color control** — Hex codes, palettes, lighting and color temperature
- **Text in images** — Which models render text well and how to prompt them
- **Multi-element layouts** — Grids, panels, collages, sequences
- **Structured visual outputs** — Diagrams, dashboards, timelines, comparison matrices
- **Iterative refinement** — How to refine rather than regenerate
- **Model-specific strategies** — Nano Banana, DALL-E, Midjourney, Stable Diffusion, Flux, Ideogram
- **15 prompt templates** — Ready-to-use for portraits, products, diagrams, logos, social media

**Start here for general image prompting across all models and use cases.**

### Print-Ready Materials Guide

**[IMAGE_GENERATION_GUIDE.md](IMAGE_GENERATION_GUIDE.md)** — Specialized guide for print-ready materials (badge buddies, worksheets, reference cards) with 8 constraint-enforcement techniques.

Covers the 8 core techniques for reliable print output:
1. **Terminology Steering** - Avoid "card" (triggers UI), use "flat print artwork"
2. **Grid Forcing + Enumerated Slots** - Explicit NxM grids with BOX 1, BOX 2, etc.
3. **Constraint Redundancy** - Repeat "no gradients" at multiple levels
4. **Negative Space Control** - Ban backgrounds, shadows, mockup staging
5. **Allowed vs. Forbidden** - Clear distinction for structured layouts vs. UI looks
6. **Physical Context Anchoring** - Real-world usage constrains design
7. **Deliverables Locking** - Exact count, dimensions, orientation
8. **Validation Checklist** - Final self-audit block

Includes model-specific notes for **Nano Banana**, **Nano Banana Pro**, DALL-E 3, Midjourney, Stable Diffusion, and ChatGPT.

**Read this guide for print materials, badge buddies, worksheets, and constraint-heavy outputs.**

### Cross-Model Workflows

**[CHARACTER_BIBLE_PIPELINE.md](CHARACTER_BIBLE_PIPELINE.md)** — End-to-end workflow for building a character bible, generating a reference pack, and maintaining identity across scenes. Model-agnostic: covers gpt-image-2, Nano Banana 2/Pro, Midjourney, and Stable Diffusion. Includes the 5-step pipeline (bible → anchor → reference pack → scenes → re-anchor), drift detection, and model-specific implementation notes.

**[STORYBOARD_WORKFLOW.md](STORYBOARD_WORKFLOW.md)** — End-to-end workflow for generating storyboard grids and feeding panels into video pipelines (Veo, Seedance 2.0, Kling). Covers shot planning, screening passes, consistency checks, and keyframe handoff. Includes the dead-pipeline warning (Sora shut down April 2026).

### Video Generation Guide

**[VIDEO_GENERATION_GUIDE.md](VIDEO_GENERATION_GUIDE.md)** - Comprehensive guide for creating AI video generation prompts, focused on Google Veo 3 / Veo 3.1.

This guide covers the 7 core elements for cinematic video generation:
1. **Shot Framing & Camera Motion** - Professional cinematography terminology
2. **Style & Visual Aesthetic** - Film genre, lens, and color grade direction
3. **Subject & Character Details** - Distinctive visual markers for consistency
4. **Setting & Atmosphere** - Sensory environmental detail
5. **Action & Movement** - Temporal progression and beat planning
6. **Dialogue & Audio** - Three-layer audio (dialogue + SFX + ambient)
7. **Technical Specifications** - Duration, aspect ratio, negative prompts

Also covers JSON prompting, multi-shot storytelling, and iterative workflows.

---

## What Makes These Different

These are **meta-prompts**: text prompts that output image generation prompts. They are fundamentally different from text-to-text prompts because:

1. **Output is another prompt** - The result is used as input to an image AI
2. **Visual specifications** - Include style, composition, color palettes, aspect ratios
3. **Model-specific syntax** - Different image AIs have different prompt formats
4. **Constraint enforcement is critical** - Models optimize for "looks cool" not "actually usable" without explicit constraints

---

## Directory Structure

```
domain-image-generation/
├── IMAGE_MODEL_SELECTION_GUIDE.md  # Which model for which task? Start here.
├── GPT_IMAGE_2_GUIDE.md           # gpt-image-2 (OpenAI, April 2026) prompting guide
├── NANO_BANANA_GUIDE.md           # Nano Banana family (Google Gemini image models)
├── IMAGE_PROMPTING_GUIDE.md       # Comprehensive guide for ALL image prompting
├── IMAGE_GENERATION_GUIDE.md      # Print-ready materials: 8 constraint techniques
├── CHARACTER_BIBLE_PIPELINE.md    # Cross-model character consistency workflow
├── STORYBOARD_WORKFLOW.md         # Cross-model storyboard + video pipeline workflow
├── VIDEO_GENERATION_GUIDE.md      # Video generation prompts (Veo 3 / 3.1)
├── infographic_meta_prompt.md     # Meta-prompt for generating infographic prompts
├── gpt-image-2/                   # 12 production-ready gpt-image-2 prompts
├── nano-banana/                   # 5 production prompts for Google Nano Banana family
├── branding/                      # Business visual identity and assets
├── coloring-book/                 # Coloring pages (adult, kids, KDP, mandala, themed, cover)
├── healthcare/                    # Clinician reference cards, patient education, medical diagrams
├── ecommerce-product/             # Product photography (white-bg, lifestyle, flat lay, macro, variants)
├── social-media/                  # Social graphic packs (quote, carousel, announcement, story, banner)
├── publishing-covers/             # Book / ebook / album / podcast covers
├── events-print/                  # Event posters, promo flyers, gig posters
├── merch-print-on-demand/         # T-shirt graphics, stickers, seamless patterns
├── childrens-illustration/        # Picture-book spreads, character sheets, style series
├── comic-sequential/              # Comic pages, manga panels, webtoon strips
├── scientific-technical/          # Scientific illustration, exploded diagrams, data-viz images
├── worksheet-generators/          # Printable education worksheet prompt generators
├── visualizations/                # Cross-role no-UI visualization prompt generators
└── README.md
```

---

## File Count

| Subdirectory | Count | Description |
|--------------|-------|-------------|
| `gpt-image-2/` | 12 | Production prompts for OpenAI's gpt-image-2 (portraits, products, logos, ads, infographics, UI, marketing copy, edits, multi-reference composites, character consistency, slides) |
| `nano-banana/` | 5 | Production prompts for Google's Nano Banana family (storyboard → Veo, search-grounded infographic, multi-ref character scene, JSON schema builder, product multi-angle composite) |
| `branding/` | ~7 | Logo, illustration, app asset prompts (model refs modernized to gpt-image-2 / Nano Banana) |
| `coloring-book/` | 9 | Adult intricate, kids simple, KDP interior, mandala, themed set, educational, cover, holiday, photo-to-lineart |
| `healthcare/` | 14 | Clinician reference cards (labs, ACLS, dosing, antibiogram), patient education (condition, discharge, meds, anatomy), medical diagrams (anatomy/physiology, procedure steps, pathophysiology, algorithms) — anti-fabrication first |
| `ecommerce-product/` | 5 | Product photography: white-bg catalog, lifestyle, flat lay, macro/texture, variant grid |
| `social-media/` | 5 | Social graphics: quote, carousel set, announcement, story/reel cover, profile banner |
| `publishing-covers/` | 5 | Fiction, nonfiction, KDP ebook, album, podcast covers |
| `events-print/` | 3 | Event poster, promotional flyer, concert/gig poster |
| `merch-print-on-demand/` | 3 | T-shirt graphic, sticker, seamless POD pattern |
| `childrens-illustration/` | 3 | Picture-book spread, character design sheet, consistent style series |
| `comic-sequential/` | 3 | Comic page, manga panel, webtoon vertical strip |
| `scientific-technical/` | 3 | Scientific illustration, exploded diagram, data-viz image (accuracy-gated) |
| `worksheet-generators/` | 45 | Core academics + early-childhood, arts, music, life-skills, foreign-language, specialized-formats, and assessment worksheet generators |
| `visualizations/` | 14 | Cross-role no-UI visualization prompt generators for analyst, design, education, engineering, executive, HR, marketing, ops, PM, research, strategy, and portfolio use cases |
| **Total** | **~146** | |

---

## Examples

### Branding
Input: "Design a logo for a sustainable coffee brand"
Output: Image prompt with style direction, color palette, composition

### Healthcare
Input: "Create a medication reference badge buddy for nurses"
Output: Print-ready image prompt with grid forcing and constraint redundancy

---

## When to Use This Domain

Use these prompts when you need to:
- Design visual identity elements (logos, icons, illustrations)
- Create coloring pages and KDP coloring-book interiors/covers
- Produce healthcare visuals: clinician reference cards, patient-education handouts, and medical/clinical diagrams (anti-fabrication first — the model renders verified content, never invents clinical facts)
- Shoot e-commerce/product imagery (white-background catalog, lifestyle, flat lay, macro, variant grids)
- Build social-media graphic packs (quotes, carousels, announcements, story/reel covers, banners)
- Design publishing covers (book, ebook, album, podcast), event/print collateral (posters, flyers), and print-on-demand merch (apparel, stickers, seamless patterns)
- Illustrate for children's books (spreads, character sheets, consistent style) and create sequential art (comic pages, manga, webtoon)
- Produce scientific/technical visuals (illustration, exploded diagrams, data-viz images — with accuracy gates)
- Generate printable K-12 worksheet layouts for core academics plus early-childhood, arts, music, life-skills, foreign-language, specialized-formats, assessment, and expanded social-studies
- Build clean cross-role visualization prompts for business, product, operations, and research storytelling

For print-ready materials use [IMAGE_GENERATION_GUIDE.md](IMAGE_GENERATION_GUIDE.md). For general image prompting use [IMAGE_PROMPTING_GUIDE.md](IMAGE_PROMPTING_GUIDE.md). For video use [VIDEO_GENERATION_GUIDE.md](VIDEO_GENERATION_GUIDE.md).

**Do NOT use for:** Text-based content generation (use other domains instead)
