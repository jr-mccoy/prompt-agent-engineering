---
title: "Pitch, Logline & Comp Titles"
category: creative-writing
description: "Craft a one-line logline, a short pitch, and a comp-title positioning for a novel — sharpening hook and market framing, with a strict no-fabrication guard on comps and market data"
techniques:
  - CM-01
  - CM-02
  - ST-02
  - ST-03
  - QA-01
difficulty: intermediate
tags:
  - creative-writing
  - publishing
  - logline
  - pitch
  - comp-titles
updated: "2026-06-18"
related_prompts:
  - domain-creative-writing/publishing-career/writing_query_letter_and_synopsis.md
  - domain-creative-writing/genre-workshops/writing_genre_specific_guidance.md
  - domain-creative-writing/fiction/writing_story_structure_architect.md
---

**Purpose:** Distill a novel into a sharp **logline** (one sentence), a short **pitch** (elevator / pitch-event length), and a defensible **comp-title positioning** — clarifying the hook and where the book sits in the market — without inventing comp titles, sales figures, or market claims.

**When to use:** Before writing a query (do this first); preparing for a pitch event, conference, or #PitMad-style pitch; when you can't explain your book in one sentence; when you're unsure what your comps are or how to position the book; when the concept feels unfocused.

**Don't use when:** You need the full query letter and synopsis (use Query Letter & Synopsis — run this first, then that); you're writing for children/teens (use `domain-childrens-writing/publishing-business/`).

> **No-fabrication guard:** This prompt will **not** invent comp titles, authors, sales numbers, bestseller claims, market-size figures, or "trends." Comps must be real books the author has read or researched. Where the author hasn't supplied comps, this prompt helps define the *criteria* for finding them and inserts `[COMP — research & verify]` placeholders rather than naming books.

**Input needed:**
- Genre/category and the core concept
- Protagonist, central conflict, what makes the book distinctive
- Tone and the reader experience it delivers
- Any comps the author has actually read (real, recent) — or "need help finding criteria"

---

## Your Input

**Genre/Category:** [...]
**Concept in a few sentences:** [...]
**Protagonist + central conflict:** [...]
**What's distinctive / the hook:** [the fresh angle]
**Tone & reader experience:** [e.g., propulsive and dark; warm and witty]
**Comps you've read (real, recent):** [Title by Author (year); ... — or "NEED CRITERIA"]

---

## Instructions

You are a developmental/pitch editor. The goal is clarity and hook, honestly positioned.

### Step 1: Find the Hook

Identify what makes this book *this* book — the fresh premise, the angle, the question. Strip subplots; find the engine. If the concept is muddy, name the 2-3 candidate hooks and recommend the strongest.

### Step 2: Logline (one sentence)

Write 2-3 logline options. A working pattern (use, don't force): **[protagonist] must [goal/action] or [stakes] — but [central complication].** Keep it concrete, specific, and in the book's tone. Avoid vague abstractions and rhetorical questions. Recommend the strongest and say why.

### Step 3: Short Pitch (elevator / pitch-event)

Expand the logline into a 2-4 sentence pitch: protagonist + want + conflict + stakes + the distinctive hook + tone — ending on tension. Provide a ~50-word version (pitch event) and a ~25-word version (Twitter/PitMad-style), both in voice.

### Step 4: Comp-Title Positioning

- If the author supplied real comps: assess fit (same category, recent ~3-5 years, comparable in tone/audience — not aspirational mega-bestsellers), and frame the positioning ("X meets Y," or "for readers of A and B"). Explain what each comp signals (audience, tone, content).
- If no comps supplied: **do not invent any.** Instead, define precise **search criteria** — category, tone, themes, structure, audience — and explain how to find comps (recent releases in-category, bookstore shelves, "readers also bought," agents' lists). Insert `[COMP — research & verify]` in the positioning line.
- Flag comp pitfalls: comps that are too old, too huge, cross-category, or films instead of books (use sparingly and signal).

### Step 5: Positioning Statement

Write 1-2 sentences locating the book in the market: category, audience, and the gap/desire it fills — grounded in the concept, **not** in invented sales or trend claims.

### Step 6: Anti-Fabrication Check

Scan outputs. Any comp title, author, sales figure, or market claim must be author-supplied or a bracketed `[research & verify]` placeholder. Output the list.

---

## Output Format

1. **The Hook** (what makes it distinctive; recommended hook if ambiguous)
2. **Logline Options** (2-3, with a recommendation)
3. **Short Pitch** (50-word and 25-word versions)
4. **Comp Positioning** (assessment of supplied comps, OR search criteria + placeholders)
5. **Positioning Statement**
6. **Verify Before Using** (anti-fabrication list)

---

## Quality Indicators

**Strong pitch materials:**
- [ ] Logline is one concrete sentence conveying character, conflict, stakes, hook
- [ ] Pitch ends on tension and sounds like the book
- [ ] Comps are real, recent, same-category, comparable in scale — or honestly flagged as TBD with criteria
- [ ] Positioning names audience and gap without invented market data
- [ ] Zero fabricated comps, sales, or trends

**Red flags:** vague abstract loglines; rhetorical-question pitches; aspirational mega-bestseller comps; comps the author hasn't read; invented sales/trend claims; trying to cram the whole plot into the pitch.

---

## False-Positive Prevention

**DON'T:**
- Invent comp titles, authors, sales figures, or "the market wants X" claims — bracket and define criteria instead
- Suggest comps the author hasn't confirmed are real, recent, and same-category
- Force the "X meets Y" formula if a plain positioning is clearer
- Cram subplot into the logline — one engine, one sentence

**DO:**
- Treat the no-fabrication guard as the controlling constraint
- Prefer concrete specifics over genre buzzwords
- Offer options and a recommendation; the author chooses
- When comps are unknown, deliver *criteria and a method*, not invented titles
