---
title: "Scientific Illustration — Clean Labeled Figure (Journal Style)"
category: image-generation/scientific-technical
description: "Generate a clean, labeled scientific illustration in a journal/figure style — with a mandatory accuracy and anti-fabrication protocol: image models are not reliable for precise scientific structures and expert verification is required."
techniques:
  - ST-01
  - ST-02
  - SV-12
  - SV-13
difficulty: advanced
tags:
  - scientific-illustration
  - figure
  - journal
  - labeled-diagram
  - accuracy
  - anti-fabrication
  - gpt-image-2
  - nano-banana
updated: "2026-06-23"
related_prompts:
  - domain-image-generation/scientific-technical/technical_exploded_diagram.md
  - domain-image-generation/scientific-technical/data_visualization_chart_image.md
  - domain-image-generation/IMAGE_MODEL_SELECTION_GUIDE.md
  - domain-image-generation/nano-banana/nanobana_search_grounded_infographic.md
---

# Scientific Illustration — Clean Labeled Figure (Journal Style)

**Objective:** Produce a clean, publication-style **scientific illustration** — a labeled figure suitable for a paper, textbook, poster, or slide (e.g., a cell, an anatomical structure, a physical process, an apparatus). The output is a **stylistically clean, accurately labeled draft** that a domain expert then verifies and corrects.

> ## ⚠️ Accuracy & Anti-Fabrication Protocol (read first — load-bearing)
> **Image models are NOT reliable for precise scientific structures.** They routinely invent plausible-looking but **incorrect** anatomy, molecular geometry, organelle counts, bond angles, wiring, and label placement. They also **hallucinate label text** — generated letters may be misspelled, misplaced, or fabricated.
>
> Treat every generated scientific image as an **unverified visual draft**, never as a source of truth. Mandatory practice:
> 1. **Supply the ground truth in the prompt** — enumerate the exact structures, their correct relationships, and the exact label text. Do not let the model decide what is "anatomically correct."
> 2. **Add labels in post, not by the model**, whenever accuracy matters. Generate a clean unlabeled (or lightly callout-placeholdered) illustration, then place verified text/labels in a vector editor. Model-rendered text is unreliable.
> 3. **Expert verification is required before any publication, teaching, or clinical use.** A subject-matter expert must confirm every structure, relationship, and label.
> 4. **Do not present model output as factual evidence.** For real anatomical/molecular accuracy, prefer verified reference atlases, scientific-illustration databases, or expert-drawn figures.
> 5. Include a provenance note ("AI-generated draft, expert-verified on [date] by [name]") in any downstream use.

**Why model choice matters:** **gpt-image-2** has the clearest support for clean labeled-figure layouts and decent (95%+) text rendering — but its text is still not trustworthy for scientific labels. **Nano Banana Pro** offers near-perfect text rendering and **Google Search grounding**, which can reduce (not eliminate) factual error; it is the better path when the figure must reflect current/verifiable information — but grounding is not a substitute for expert verification.

**API parameters:**
- gpt-image-2 path: `model="gpt-image-2"`, `/v1/images/generations`, `quality="high"`, `size` per figure aspect, `n=1`
- Nano Banana path: `model="gemini-3-pro-image"` (Pro — text + search grounding) preferred; `quality="high"`

---

## Inputs

- `[SUBJECT]` — exactly what to illustrate (e.g., "a generalized animal cell," "the human knee joint, sagittal view")
- `[GROUND TRUTH STRUCTURE LIST]` — the exact structures to include, their correct spatial relationships, and any that must be excluded (you supply this from a verified source)
- `[EXACT LABEL TEXT]` — the precise label strings (preferably added in post)
- `[VIEW/ORIENTATION]` — cross-section / sagittal / dorsal / exploded / schematic
- `[FIGURE STYLE]` — flat vector / textbook-shaded / line-art / micrograph-style
- `[PALETTE]` — colorblind-safe palette if for publication
- `[CALLOUT STYLE]` — leader lines to numbered callouts (preferred) vs. inline labels

---

## Constraints (Must / Must Not)

**Must:**
- Render **only the structures in `[GROUND TRUTH STRUCTURE LIST]`**, in the specified relationships.
- Prefer **numbered callouts / placeholder leader lines** over model-rendered text, so verified labels can be placed in post.
- Use a clean, even, **publication-appropriate** style with a neutral/white background.
- State explicitly that the figure is an **unverified draft pending expert review**.
- Use a **colorblind-safe palette** if the figure is for publication.

**Must Not:**
- Let the model invent structures, organelle counts, or relationships not in the ground-truth list.
- Rely on model-rendered label text for accuracy.
- Present the output as anatomically/scientifically correct without expert verification.
- Add decorative or speculative detail that could be mistaken for real structure.

---

## Production Prompt — gpt-image-2 path (clean draft, callouts not text)

```
SCENE:
A clean, publication-style scientific illustration of [SUBJECT], [VIEW/ORIENTATION]. White/neutral background, even flat lighting. Style: [FIGURE STYLE].

STRUCTURES TO DEPICT (depict ONLY these, in these relationships — do not add or invent any others):
[GROUND TRUTH STRUCTURE LIST — enumerate each structure and its correct position/relationship explicitly]

LABELING:
- Draw thin neutral leader lines from each listed structure to a numbered callout marker (1, 2, 3, …) placed in the margin.
- Do NOT render descriptive label words inside the figure — leave numbered callout placeholders only. (Verified label text will be added in post.)

KEY DETAILS:
- Palette: [PALETTE — colorblind-safe if for publication].
- Clean line work; clear separation between structures; no decorative or speculative detail.
- Neutral background, no environmental context.

USE CASE:
An UNVERIFIED draft figure for [paper / textbook / poster / slide]. A subject-matter expert will verify every structure and add/correct labels before any use.

CONSTRAINTS:
- Depict ONLY the listed structures; invent nothing.
- Numbered callouts, not rendered words (model text is unreliable).
- Publication-clean, neutral background, colorblind-safe palette.
- Format: [size], quality="high".

If the figure adds structures not in the list, invents relationships, or renders unreliable label words, it is incorrect and must be regenerated.
```

---

## Production Prompt — Nano Banana Pro path (search-grounded, text-capable)

```
TASK: Create a clean, publication-style scientific illustration of [SUBJECT], [VIEW/ORIENTATION], style [FIGURE STYLE], on a neutral/white background.

GROUND TRUTH (depict ONLY these structures and relationships — do not invent others):
[GROUND TRUTH STRUCTURE LIST]

[If grounding helps verify current/established depiction:]
Use Google Search grounding to confirm the standard depiction of [SUBJECT]'s structures and their relationships. Grounding informs the draft but does NOT replace expert verification.

LABELS:
- If labels are requested in-image, render EXACTLY this text, verbatim, placed at the listed structures: [EXACT LABEL TEXT]. Do not paraphrase, add, or invent any label.
- Otherwise use numbered callouts and leave text for post-production.

STYLE: [FIGURE STYLE], [PALETTE — colorblind-safe], clean line work, no speculative detail.

CONSTRAINTS:
- MUST: depict only the ground-truth structures; render only the exact provided label text; neutral background.
- MUST NOT: invent structures/relationships/labels; add decorative detail; present as verified.
- Quality: "high".

This is an UNVERIFIED draft. Flag any structure the model is uncertain about for expert review.
```

---

## Iteration Plan

1. "The figure added [structure] that is not in the ground-truth list — remove it; depict only the listed structures."
2. "The spatial relationship between [A] and [B] is wrong — [A] should be [correct relationship]; correct it."
3. "The rendered labels are misspelled/misplaced — switch to numbered callouts so I can add verified labels in post."
4. "The palette isn't colorblind-safe — switch to a colorblind-safe palette for publication."
5. "There is speculative shading that reads as real structure — flatten it; show only confirmed structures."

---

## Verification

> Verification here is not optional polish — it is the accuracy gate.

- [ ] Only the ground-truth structures are depicted; nothing invented.
- [ ] Spatial relationships match the supplied ground truth.
- [ ] Labels are either numbered callouts (preferred) or exactly the supplied verbatim text — no model-invented words.
- [ ] Palette is colorblind-safe (if for publication).
- [ ] Background neutral; style publication-clean.
- [ ] **A subject-matter expert has verified every structure, relationship, and label** before any use.
- [ ] Output is documented as an AI-generated draft with verification provenance ("verified on [date] by [name]").
