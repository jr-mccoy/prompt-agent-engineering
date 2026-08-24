---
title: "GPT Image 2 Prompting Guide"
category: image-generation/model-specific
description: "Comprehensive prompting guide for OpenAI's gpt-image-2: parameters, structural patterns, text rendering, multi-image references, thinking mode, editing, and use case strategies"
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
  - gpt-image-2
  - openai
  - image-generation
  - model-guide
  - prompting
updated: "2026-05-05"
related_prompts:
  - domain-image-generation/IMAGE_PROMPTING_GUIDE.md
  - domain-image-generation/IMAGE_GENERATION_GUIDE.md
  - domain-image-generation/NANO_BANANA_GUIDE.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/gpt-image-2/README.md
---

# GPT Image 2 Prompting Guide

**Purpose:** Authoritative reference for prompting OpenAI's `gpt-image-2`, the successor to `gpt-image-1.5` released **April 21, 2026** (snapshot `gpt-image-2-2026-04-21`).

**Audience:** Anyone writing production prompts for `gpt-image-2` via the OpenAI API, ChatGPT, or third-party providers (fal.ai, Replicate, etc.).

**Relationship to other guides:**
- **[IMAGE_PROMPTING_GUIDE.md](IMAGE_PROMPTING_GUIDE.md)** — Cross-model image prompting reference.
- **[IMAGE_GENERATION_GUIDE.md](IMAGE_GENERATION_GUIDE.md)** — Print-ready material constraints (the 8 SV techniques).
- **This guide** — gpt-image-2-specific patterns: parameters, multi-image refs, text rendering, thinking mode, editing.
- **[gpt-image-2/](gpt-image-2/)** — 12 production-ready prompts that apply this guide.

---

## Table of Contents

1. [Model at a Glance](#1-model-at-a-glance)
2. [What's New in GPT Image 2](#2-whats-new-in-gpt-image-2)
3. [Parameters: Size, Quality, Batch, Background](#3-parameters)
4. [The 5-Section Prompt Structure](#4-the-5-section-prompt-structure)
5. [Text Rendering (95%+ Accuracy)](#5-text-rendering)
6. [Multi-Image References (Up to 16)](#6-multi-image-references)
7. [Thinking Mode and Web Search](#7-thinking-mode-and-web-search)
8. [Editing: Change vs. Preserve](#8-editing-change-vs-preserve)
9. [Use Case Strategies](#9-use-case-strategies)
10. [Anti-Patterns and Slop Words](#10-anti-patterns-and-slop-words)
11. [Iteration Strategy](#11-iteration-strategy)
12. [Troubleshooting](#12-troubleshooting)
13. [Quality Checklist](#13-quality-checklist)
14. [Templates](#14-templates)

---

## 1. Model at a Glance

| Property | Value |
|---|---|
| Model ID | `gpt-image-2` |
| Snapshot | `gpt-image-2-2026-04-21` |
| Released | April 21, 2026 |
| Endpoints | `/v1/images/generations`, `/v1/images/edits`, `/v1/chat/completions`, `/v1/responses`, `/v1/batch`, `/v1/assistants` |
| Input | Text + up to 16 reference images |
| Output | Image (PNG/JPEG/WebP depending on caller) |
| Quality tiers | `low`, `medium`, `high` |
| Max edge | < 3840 px (must be multiple of 16) |
| Min total pixels | 655,360 |
| Max total pixels | 8,294,400 |
| Aspect ratio range | 1:3 → 3:1 (long-to-short ≤ 3:1) |
| Native 4K | Yes (3840 × 2160 marked experimental) |
| Text rendering accuracy | 95%+ (per OpenAI) |
| Thinking mode | Native (always on for complex prompts) |
| Web search during generation | Yes (for fact-grounded visuals) |
| `input_fidelity` | **Disabled** (output is high-fidelity by default; use `gpt-image-1.5` if you need explicit input_fidelity) |
| Streaming / function calling / structured outputs / fine-tuning | Not supported |
| Rate limits | 5 IPM (Tier 1) → 250 IPM (Tier 5) |

**When to default to `gpt-image-2`:** Almost always. Use it for new workflows; keep `gpt-image-1.5` only for backward compatibility or when you specifically need `input_fidelity="high"` for likeness preservation in large scene edits.

**When to use `gpt-image-1-mini` instead:** Cost-/throughput-dominant workflows — large batch variant generation, rapid ideation, draft assets where "good enough" is the bar.

---

## 2. What's New in GPT Image 2

Compared to `gpt-image-1` and `gpt-image-1.5`:

| Capability | gpt-image-1.5 | gpt-image-2 |
|---|---|---|
| Max edge | 2048 px | < 3840 px |
| Native 4K | No | Yes (experimental above 2560×1440) |
| Aspect ratio range | 1:2 to 2:1 | 1:3 to 3:1 |
| Reference images | Up to 8 | Up to 16 |
| Text rendering accuracy | ~85% | 95%+ |
| Thinking mode | Optional | Native, always-on for complex briefs |
| Web search during generation | No | Yes |
| `input_fidelity` parameter | Available | Disabled (built-in high fidelity) |

**Practical implications:**
- Stop pre-cropping reference images for portrait/landscape — the model handles 3:1 cinematic and 1:3 vertical natively.
- Stop chaining "generate → upscale" pipelines for normal use; generate directly at 2K. Reserve external upscalers for above-4K work.
- Stop spelling brand text letter-by-letter as a default — only do it for truly difficult words.
- Stop adding `input_fidelity="high"` to your gpt-image-2 calls — it's a no-op (and the API may reject it).

---

## 3. Parameters

### 3.1 Size / Resolution

**Hard constraints:**
- Max edge: **less than 3840 px**
- Both edges: **multiple of 16**
- Long-to-short ratio: **≤ 3:1**
- Total pixels: **655,360 minimum, 8,294,400 maximum**
- Above **2560 × 1440** (3,686,400 px) is flagged **experimental** — variability increases.

**Popular sizes:**

| Use case | Size | Notes |
|---|---|---|
| Square social, default | 1024 × 1024 | Cheapest "high-quality" option |
| HD portrait | 1024 × 1536 | Mobile feeds, magazine covers |
| HD landscape | 1536 × 1024 | Slides, hero banners |
| 2K landscape | 2560 × 1440 | Desktop hero, presentations |
| 2K portrait | 1440 × 2560 | TikTok, IG reels stills |
| Cinematic ultrawide | 2880 × 960 | 3:1 — banners, headers |
| Cinematic vertical | 960 × 2880 | 1:3 — phone-wallpaper splits |
| 4K UHD landscape | 3824 × 2144 | **Experimental.** Note: 3840 is not allowed (max edge < 3840); round down to nearest multiple of 16. |
| 4K UHD portrait | 2144 × 3824 | **Experimental.** |

**Rule:** if your target dimension would equal or exceed 3840, round down to the nearest multiple of 16. Example: a 3840 × 2160 4K target becomes **3824 × 2144**.

### 3.2 Quality

| Setting | Use when | Tradeoff |
|---|---|---|
| `quality="low"` | Rapid ideation, batch variants, latency-sensitive flows, previews | Faster, cheaper; soft/imprecise text and small details |
| `quality="medium"` | Most production workflows; product mockups; portraits without dense text | Balanced |
| `quality="high"` | Dense in-image text, infographics, identity-sensitive portraits, charts with small numbers, marketing copy that must be verbatim | Slowest, most expensive; highest fidelity |

**Decision tree:**
- Has dense or small text? → `high`.
- Identity-sensitive (face, brand mark) at zoom? → `high`.
- One of many variants you'll throw away? → `low`.
- Otherwise? → `medium`.

### 3.3 Batch Generation (`n`)

Use `n` to generate multiple variations of the same prompt in a single call:

```python
client.images.generate(
    model="gpt-image-2",
    prompt="...",
    n=4,           # 4 logo variations
    size="1024x1024",
    quality="medium",
)
```

Best for: logo variations, ad creative pools, character look-dev, A/B testing of layouts.

### 3.4 Background

`background="opaque"` works for product extraction workflows. For transparent output, prefer downstream removal (the API does not expose a true alpha channel for arbitrary scenes).

### 3.5 Parameters That No Longer Apply

- **`input_fidelity`** — disabled on gpt-image-2 (output is high-fidelity by default). If your code passes it, remove it before migrating from gpt-image-1.5.

---

## 4. The 5-Section Prompt Structure

OpenAI's reference structure for gpt-image-2 prompts. Use labeled segments (line breaks or section headers), not dense paragraphs:

```
SCENE / BACKGROUND
[Where does this take place? Lighting, time of day, environment.]

SUBJECT
[The primary focus. People, products, characters — described concretely.]

KEY DETAILS
[Materials, textures, expressions, secondary objects, posture, gaze.]

USE CASE
[Ad, UI mockup, infographic, editorial, product hero. Establishes polish level.]

CONSTRAINTS
[What to preserve, what NOT to include, format/orientation, exact text.]
```

**Why include "use case" explicitly:** stating "campaign hero shot" vs "iPhone snapshot" vs "lo-fi sketch" tells the model what level of polish, which clichés to avoid, and how to weight realism vs stylization.

**Format flexibility:** plain text, JSON, instruction-style, and tag-based formats all work. Pick one and stay consistent within a project — easier to debug.

**Example — minimal application of the structure:**

```
SCENE: An overcast morning at a coastal harbor in early spring.
SUBJECT: An elderly fisherman in a yellow oilskin coat coiling a wet rope.
KEY DETAILS: Visible salt residue on the dock; rope strands frayed; weathered hands; gaze down at the rope; full body visible, feet included.
USE CASE: Editorial cover image for a longform article on small fisheries.
CONSTRAINTS: Photorealistic. 35mm film grain. No additional people. No boats clearly visible. No text in image.
```

---

## 5. Text Rendering

GPT Image 2 hits **95%+** text rendering accuracy. Treat in-image text as a contract.

### 5.1 The Text Rendering Contract

For every literal string the model must render, specify:

1. **The exact text in quotes** — `EXACT TEXT: "Limited Edition · Spring 2026"`
2. **Verbatim discipline** — `Render the quoted text exactly with no extra characters, no punctuation drift, and no inserted line breaks unless I specify them.`
3. **Typography** — font style (serif / sans / display / monospace), weight, case, size relative to canvas.
4. **Color** — hex code (`#1A1A1A`, not "dark grey").
5. **Placement** — "centered horizontally, lower third" / "top-left, 5% margin".
6. **Legibility floor** — for small or dense text, set `quality="high"` and add `100% readable at full resolution`.

### 5.2 Difficult Strings

For brand names, foreign words, technical terms, or anything the model might mishear, **spell it letter-by-letter at least once** in the prompt:

```
EXACT TEXT: "Kløver Café"
Letter-by-letter: K, L, O-with-stroke (ø), V, E, R, space, C, A, F, E-with-acute (é).
```

### 5.3 Multilingual Text

The model handles **Japanese, Korean, Chinese, Hindi, Bengali, Arabic, and most Latin-extended scripts** when typography is locked. Specify:
- Script name ("Devanagari", "Hangul", "Simplified Chinese")
- Whether punctuation should follow source-language conventions
- Direction (LTR/RTL) for Arabic / Hebrew

### 5.4 Quality Floor for Text

| Text type | Minimum quality |
|---|---|
| Single bold headline (≥ 5% of canvas) | `medium` |
| Body copy, captions, multiple typefaces | `high` |
| Charts with small numbers, infographic labels | `high` |
| Brand wordmarks (must be verbatim) | `high` |

---

## 6. Multi-Image References

GPT Image 2 accepts **up to 16 reference images**. Reference inputs by **index and description**.

### 6.1 The Index-and-Describe Pattern

```
Image 1: Product photo of the navy hoodie on a hanger.
Image 2: Studio portrait of the model — preserve face, hairstyle, body shape.
Image 3: Mood board — preserve color grading and overall lighting feel.

TASK: Place the hoodie from Image 1 onto the model in Image 2, matching the lighting and color grade of Image 3. Preserve the model's exact face and proportions.
```

### 6.2 Compositing Discipline

When transplanting elements between references, name **all four** of these:

1. **What to transplant** — "the bird from Image 1"
2. **Where it goes** — "perched on the elephant's tusk in Image 2"
3. **What must remain unchanged** — "Image 2's elephant, background, and camera angle stay identical"
4. **What must match** — "match Image 2's lighting, perspective, scale, and shadow direction"

### 6.3 Reference Allocation Strategy

When you have 16 slots, don't dump 16 random references. Allocate by purpose:

- 1–3: subject identity (face, body, brand mark)
- 4–6: garment / object reference
- 7–9: scene / environment
- 10–12: lighting / mood reference
- 13–16: style / color grade reference

State each slot's role explicitly in the prompt. The community finding: **17+ references for character consistency outperforms 2 dramatically; budget the slots, don't fill them randomly.**

---

## 7. Thinking Mode and Web Search

### 7.1 Thinking Mode

GPT Image 2 reasons about a prompt before drawing — this is on by default for complex briefs. You don't toggle it; you write prompts that let it reason effectively.

**What thinking mode rewards:**
- Stated constraints upfront (it spends reasoning budget on them)
- Explicit hierarchy ("most important: text legibility; secondary: composition")
- Stated tradeoffs ("if forced to choose, preserve face over outfit")

**What thinking mode penalizes:**
- Buried constraints in the middle of long paragraphs
- Contradictory requirements (it'll pick one and you may not like which)
- Vague mood words without concrete realization ("luxurious" — luxurious how?)

**Watch out — realism bias:** the thinking pass tends to push toward realism. For surreal, absurdist, or stylized work, **state the style commitment up front**: `STYLE: deliberately surreal — this is NOT meant to be photorealistic.`

### 7.2 Web Search During Generation

GPT Image 2 can pull live facts mid-generation. Useful for:

- Fact-grounded **infographics** — "Show the 2026 G20 member countries with current flags."
- **Product accuracy** — "Render an iPhone 17 Pro accurately to its real industrial design."
- **Logo accuracy** — when referencing real brands (subject to OpenAI's IP guardrails).
- **Current events** — sports rosters, recent map boundaries, currency design.

**Trigger phrases that surface web search behavior:**
- "Use accurate, up-to-date references for [X]."
- "Search and use the current [logo/flag/uniform] for [entity]."
- "Verify [fact] before rendering."

**When to block it:** for fictional or branded content where you don't want the model to "correct" your invented details, say `Do not use external references; use only what's described in this prompt.`

---

## 8. Editing: Change vs. Preserve

The single most useful editing pattern: **two sentences, one for change, one for preserve.**

```
CHANGE: Replace the navy hoodie with a cream cable-knit sweater.
PRESERVE: Everything else — the model's face, hair, body shape, expression, pose, hands, background, lighting, camera angle, and color grade — stays exactly the same.
```

### 8.1 Surgical Edit Rules

1. **One change per turn.** Bundling edits ("change the hoodie AND brighten the lighting AND remove the dog") produces drift. Iterate.
2. **Repeat the preserve list every iteration.** The model does not remember earlier turns' constraints with perfect fidelity — restate them.
3. **Use "ONLY" liberally.** "Replace ONLY the hoodie." "Change ONLY the lighting."
4. **Name the geometry.** "Preserve camera angle, room scale, and floor shadow direction."
5. **State the failure condition.** "If her face changes in any way, the edit is incorrect."

### 8.2 Specialty Edit Patterns

| Edit type | Critical preserve list |
|---|---|
| Object removal | Surrounding pixels, lighting, surfaces under the object |
| Object replacement | Camera angle, scale, contact shadows |
| Lighting change | Identity, geometry, object placement, camera angle |
| Weather change | Identity, geometry, camera angle, object positions |
| Background swap | Subject identity, subject lighting (or restate new lighting) |
| Outfit change (try-on) | Face, body shape, pose, hair, expression, proportions |
| Text translation | Everything except the text |
| Style transfer | Composition, subject identity (or explicitly allow drift) |

### 8.3 When to Switch to gpt-image-1.5

If you need **explicit `input_fidelity="high"`** to lock a specific person's likeness through a large scene edit, gpt-image-2 disables that knob. Either:
- Use gpt-image-2 with a stronger preserve list and accept slightly more variability, **or**
- Use gpt-image-1.5 with `input_fidelity="high"` for that one edit.

For most work, gpt-image-2's default fidelity is good enough that you don't need to fall back.

---

## 9. Use Case Strategies

Per OpenAI's official guide, the following patterns are battle-tested. Each maps to a prompt in [`gpt-image-2/`](gpt-image-2/).

### 9.1 Photorealistic Photography

- Use **photography language**: 35mm, f/2.8, golden hour, Kodak Portra, three-point lighting.
- Demand **real texture**: pores, wrinkles, fabric wear, subtle imperfections.
- **Avoid studio polish words**: "glossy", "perfect", "flawless" — they trigger plasticky AI gloss.
- Include the word **photorealistic** explicitly.
- Specify **scale and framing**: full body / half / close-up; feet visible; hands visible.

### 9.2 Logo Generation

- Brief like a designer: brand personality, audience, use case, vibe.
- Request **clean vector-like shapes, strong silhouette, balanced negative space**.
- Use `n=4` for variations.
- For wordmark, treat as Section 5 (text rendering contract).
- Specify **single centered logo with generous padding** for downstream cropping.

### 9.3 Advertising / Campaign

- Write a **creative brief**, not a description: brand, target audience, cultural moment, concept, composition, exact copy.
- Let the model make taste-driven decisions inside the brief boundaries.
- Quality: `medium` or `high` if there's headline copy.
- Lock copy with the text contract (Section 5).

### 9.4 Infographics / Diagrams

- Quality: `high`.
- Treat as **artifact specification**, not illustration request.
- Enumerate sections and labels (apply SV-12 grid forcing).
- State **audience level** (executive, K-12, technical).
- For data: state **exact numbers and labels** verbatim.
- Combine with web search if facts must be current.

### 9.5 UI Mockups

- Describe as if the product **already exists**.
- Focus on **layout, hierarchy, spacing, real interface elements**.
- **Avoid concept-art language** ("a dreamy interface that...").
- Use realistic copy, not lorem ipsum.
- Quality: `medium` (or `high` if the screen has data tables / charts).

### 9.6 Comic Strips / Sequences

- Define narrative as a **sequence of clear visual beats** — one per panel.
- Concrete actions: "raises eyebrow," "drops the cup."
- Reuse character anchor across panels (Section 6 reference allocation).

### 9.7 Scientific / Educational Visuals

- Define **audience, lesson objective, visual format, required labels, scientific constraints**.
- Quality: `high`.
- Combine with web search for fact-grounded labels.

### 9.8 Productivity Slides

- Specify the **artifact**: "Slide 4 of 12: 'Q1 Funnel Performance' — 1536×1024."
- Real data, real headers, real chart types.
- Avoid concept-art / illustration framing.

### 9.9 Style Transfer

- Describe **style cues to preserve** and **content to change** separately.
- Add `no extra elements` and `no added text` if those would drift.
- Block realism-bias: `Do not photo-realize the source — keep the painterly stylization.`

### 9.10 Virtual Try-On

- **Lock identity**: face, body, pose, hair, expression, proportions.
- Allow only garment change.
- Require **realistic fit** with consistent lighting/shadows.

### 9.11 Sketch-to-Render

- "Preserve the **exact layout, proportions, and perspective** of the sketch."
- "Choose realistic materials and lighting consistent with the implied subject."
- "Do not add new elements or text."

### 9.12 Holiday Cards / Premium Merch

- **Tactile realism**: paper layers, fibers, folds, soft studio lighting.
- Mood + scene + constraints (no trademarks, watermarks, logos).
- Quality: `medium` for premium feel; `high` if there's verbatim copy.

---

## 10. Anti-Patterns and Slop Words

Drop these from prompts. They burn tokens and produce worse outputs.

### 10.1 Banned Slop Words

| Don't write | Why | Replace with |
|---|---|---|
| "stunning" | Empty hype | The visual fact you actually want |
| "masterpiece" | Old-SD prompt-spam, no longer adds quality | Concrete style reference |
| "8K, ultra-detailed" | Token spam, doesn't change output | Set `quality="high"` and `size` explicitly |
| "luxurious" | Vague | "matte black, brushed brass, deep burgundy velvet" |
| "minimalist" (alone) | Vague | "cream background, heavy black sans-serif, generous negative space" |
| "beautiful lighting" | Vague | "soft north-window daylight" / "golden hour backlight" |
| "highly detailed" | Token spam | Specify which details (e.g., "visible thread pattern on the fabric") |
| "trending on ArtStation" | Stylistically locks output to 2022-era ArtStation tropes | Name a specific artist or medium |

### 10.2 Structural Anti-Patterns

- **Burying the most important constraint** at the bottom of a 400-word paragraph. Move it to the top of `CONSTRAINTS`.
- **Contradictions** — "minimalist but maximalist", "vintage but futuristic". Pick one or state the dominant.
- **Treating the prompt as a wishlist** — listing every nice-to-have. Each token competes for attention; cut anything you don't need.
- **Unspecified text** — "add a cool tagline" produces typos and drift. Always provide EXACT TEXT.
- **Mockup language for non-mockups** — calling a print piece a "card" or "design" triggers UI/mockup behaviors. See SV-11 (Terminology Steering).

---

## 11. Iteration Strategy

The official guidance: **start with a clean base prompt, then refine with single-change follow-ups.**

### 11.1 Three-Phase Iteration

1. **Phase 1 — Establish the base.** Short, clear, no edge-case constraints. Get a "directionally right" output.
2. **Phase 2 — Single-axis refinement.** One change per turn: "make the lighting warmer," "remove the second person," "shift the headline left."
3. **Phase 3 — Lock and produce.** Once a variant is right, capture the full prompt as a snapshot. Use `n` for final variations.

### 11.2 Naming Conventions Across Iterations

When iterating on the same character/product across multiple sessions, give them a stable name in the prompt: `Maya (lead character)`, `Kløver Roast (the product)`. This anchors the model's reasoning across edits and makes prompt diffs readable.

### 11.3 When to Restart

Restart from a clean base prompt when:
- You've layered 5+ edits and the output is drifting.
- The model is "remembering" a constraint you removed.
- You need a fundamentally different composition.

---

## 12. Troubleshooting

### 12.1 Text is wrong / typos appear

- Set `quality="high"`.
- Wrap text in quotes; add `Render verbatim with no extra characters.`
- Spell hard words letter-by-letter.
- Reduce the **amount** of in-image text — the model handles 1 headline + 1 subhead reliably; 4 paragraphs of body copy unreliably.

### 12.2 Face / identity drifted in an edit

- Add: `Preserve [name]'s exact face, expression, hairstyle, skin tone, and proportions. If the face changes in any way, the edit is incorrect.`
- Reduce edit scope — change one thing at a time.
- For maximum likeness lock, fall back to `gpt-image-1.5` with `input_fidelity="high"`.

### 12.3 Output is photorealistic when you wanted stylized

- Add at top: `STYLE COMMITMENT: deliberately illustrated / surreal / painterly. This is NOT meant to be photorealistic.`
- Name a specific medium ("gouache on cold-press paper") rather than vague style words.
- Block the realism-bias of thinking mode early in the prompt.

### 12.4 Output is stylized when you wanted photorealistic

- Add `photorealistic` literally.
- Add photography language: lens, lighting, film stock, framing.
- Demand imperfections: `pores visible, slight motion blur, real fabric weave`.
- Avoid "studio" wording if you don't want the AI-glossy look.

### 12.5 Wrong number of outputs

- Use the `n` parameter for variations — don't ask the prompt for "4 variations."
- For a single image with multiple elements (e.g., a 2×2 grid), specify it as a single composed image with explicit grid geometry.

### 12.6 Wrong aspect ratio / dimension

- Specify `size` in the API call directly. Do not rely on prompt language alone.
- Verify the size is a multiple of 16 and edge < 3840.

### 12.7 4K output is unstable

- 4K is experimental. Drop to 2560×1440 (`high` quality), then upscale separately if you genuinely need 4K. Cheaper and more reliable.

### 12.8 Multi-image composite ignored a reference

- Always describe each reference by **index AND role** (`Image 3 = lighting reference`).
- If the model still ignores a reference, restate it in the CONSTRAINTS section: `Apply the lighting from Image 3 to the entire composition.`

---

## 13. Quality Checklist

Before sending a gpt-image-2 prompt to production, verify:

- [ ] Uses the 5-section structure (Scene / Subject / Details / Use Case / Constraints) **or** an equivalent labeled structure.
- [ ] States the `size`, `quality`, and `n` you actually want — not buried in prose.
- [ ] If text is in the image: EXACT TEXT in quotes, typography specified, hex colors, placement, quality `high`.
- [ ] If multi-image: each reference indexed and given a role.
- [ ] If editing: change/preserve sentences, with "ONLY" used; failure condition stated.
- [ ] Slop words removed.
- [ ] No `input_fidelity` parameter (gpt-image-2 doesn't accept it).
- [ ] If above 2560×1440: acknowledged the experimental flag and have a fallback.
- [ ] Style commitment stated up front if you want non-photorealistic output.
- [ ] If facts must be current: explicit web search permission **or** explicit block.
- [ ] Most important constraint is at the top of CONSTRAINTS, not the bottom.

---

## 14. Templates

### 14.1 Generation Template

```
SCENE: [environment, time of day, lighting]
SUBJECT: [primary focus, framing, scale]
KEY DETAILS: [materials, expressions, secondary objects]
USE CASE: [editorial / ad / UI / infographic / product hero]
CONSTRAINTS:
- Style commitment: [photorealistic / illustrated / painterly / etc.]
- EXACT TEXT (if any): "[verbatim text]" — [font style, weight, color hex, placement, "100% readable at full resolution"]
- Preserve: [non-negotiables]
- Forbidden: [things that must not appear]
- Format: [size, orientation, n]
```

API call:

```python
client.images.generate(
    model="gpt-image-2",
    prompt=PROMPT,
    size="1536x1024",       # multiple of 16, edge < 3840
    quality="medium",       # low | medium | high
    n=1,                    # 1–N variations
)
```

### 14.2 Edit Template (Single Reference)

```
INPUT: [Image 1 description in one sentence]

CHANGE: [single concrete change, prefixed with "Replace ONLY..." or "Change ONLY..."]

PRESERVE: Everything else — [enumerate: face, hair, expression, pose, body shape, hands, camera angle, lighting, background, color grade] — stays exactly the same.

REALISM: Match the existing lighting direction, shadow softness, and color grade.

FAILURE CONDITION: If [identity / geometry / camera angle] changes in any way, the edit is incorrect.
```

API call:

```python
client.images.edit(
    model="gpt-image-2",
    image=open("input.png", "rb"),
    prompt=PROMPT,
    size="1024x1024",
    quality="high",
)
```

### 14.3 Multi-Image Composite Template

```
REFERENCES (16 slots — name each role explicitly):
Image 1 — [role: subject identity, garment, scene, lighting, color grade, ...]
Image 2 — ...
Image 3 — ...
[...up to Image 16]

TASK:
- Transplant: [what, from which image]
- Place at: [where, in which image]
- Preserve unchanged: [list]
- Match: [lighting, perspective, scale, shadow direction] from [Image X]

CONSTRAINTS:
- [size, orientation, quality]
- Style commitment: [...]
- EXACT TEXT (if any): "..."
```

### 14.4 Verbatim-Text Marketing Template

```
SCENE: [setting]
SUBJECT: [primary focus]
USE CASE: [marketing surface — IG ad, billboard, product page hero]

EXACT TEXT (verbatim):
- Headline: "[headline copy]" — [font style, weight, hex color, placement, size relative to canvas]
- Subhead: "[subhead]" — [...]
- CTA: "[button label]" — [...]

Render every quoted string exactly. No extra characters. No punctuation drift. 100% readable at full resolution.

CONSTRAINTS:
- size: [...], quality: high
- Forbidden: extra text, watermark, lorem ipsum
- Preserve negative space around the headline
```

---

## See Also

- **[gpt-image-2/README.md](gpt-image-2/README.md)** — Index of 12 production prompts that apply this guide.
- **[IMAGE_PROMPTING_GUIDE.md](IMAGE_PROMPTING_GUIDE.md)** — Cross-model image prompting reference.
- **[IMAGE_GENERATION_GUIDE.md](IMAGE_GENERATION_GUIDE.md)** — Print-ready material constraints (the 8 SV techniques).
- **[../techniques/MASTER_TECHNIQUE_INDEX.md](../techniques/MASTER_TECHNIQUE_INDEX.md)** — SV-11 through SV-18 technique definitions.

---

*Sources: [OpenAI GPT Image Models Prompting Guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide), [GPT Image 2 Model Documentation](https://developers.openai.com/api/docs/models/gpt-image-2), [fal.ai prompting guide](https://fal.ai/learn/tools/prompting-gpt-image-2), community findings as of May 2026.*
