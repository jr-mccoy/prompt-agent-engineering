---
title: "Query Letter & Synopsis (Adult Fiction)"
category: creative-writing
description: "Build an adult-fiction agent query letter and a 1-2 page synopsis — hook, metadata, bio, comps — following submission norms, with a hard no-fabrication guard on agents, comps, and credits"
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
  - query-letter
  - synopsis
  - agent-submission
updated: "2026-06-18"
related_prompts:
  - domain-creative-writing/publishing-career/writing_pitch_logline_and_comp_titles.md
  - domain-creative-writing/craft-tools/writing_opening_pages_and_hook.md
  - domain-creative-writing/craft-tools/writing_beta_reader_feedback_synthesis.md
---

**Purpose:** Help an adult-fiction author write a tight, professional agent **query letter** and a **1-2 page synopsis** that follow current trade-publishing norms — a compelling hook, correct metadata, a grounded bio, and honest comps — without inventing a single agent, agency, comp title, sale, or credential.

**When to use:** When you have a complete, revised adult-fiction manuscript and are ready to query literary agents; when your query is too long, generic, or vague; when you keep getting form rejections; when you need a synopsis (which agents request and most writers dread).

**Don't use when:** You're writing for children/teens (use `domain-childrens-writing/publishing-business/`); the manuscript isn't finished and revised (querying early is the most common avoidable mistake); you need to develop the logline and comps themselves (use the Pitch, Logline & Comp Titles prompt first, then return).

> **No-fabrication guard:** This prompt will **never invent** an agent name, agency, a book the agent represents, a wish-list quote, a comp title, a sales figure, an award, a publication, or a credential. Anything not supplied by the author is inserted as a clearly bracketed `[PLACEHOLDER — research & verify]`. Fabricated personalization or comps are worse than none.

**Input needed:**
- Manuscript metadata: title, genre/category, final word count, complete & revised? (yes/no)
- The story: protagonist + want + conflict + stakes (and the broad arc, for the synopsis)
- Your real bio facts (relevant credentials/publications — or "none yet")
- Researched comps (real, recent, adult titles) — or a note that you still need them
- The specific agent (or "personalize per-agent later")

---

## Your Input

**Title / Genre / Word count:** [...]
**Manuscript complete & revised?** [yes / no]
**Protagonist + want + conflict + stakes:** [...]
**Broad arc (for synopsis):** [beginning → turn → ending, INCLUDING the real ending]
**Your real bio facts:** [credentials/pubs — or "none yet"]
**Comps (real, researched):** [Title by Author (year); ... — or "NEED TO RESEARCH"]
**Target agent:** [name + why — or "personalize later"]

---

## Instructions

You are a literary agent who reads the slush pile. Build a query that respects the form and never fabricates. If the manuscript isn't complete and revised, say so first — querying early wastes the author's best shot.

### Step 1: Metadata Line

State title, word count, genre/category. Flag if the word count is outside common ranges for the category — agents read an out-of-range count as a craft signal — but **present ranges as common defaults the author should confirm against current guidelines; do not invent precise numbers.**

### Step 2: The Hook / Pitch Paragraph(s)

Write 1-2 paragraphs (the heart of the query): protagonist, their want, the conflict/antagonist force, the stakes, and the central dramatic question — in the *voice and tone* of the book. End on tension, not resolution (the query withholds the ending; the synopsis reveals it). No rhetorical-question clichés ("What would you do if...").

### Step 3: Comps & Positioning

Use **only** the real, recent (~last 3-5 years), same-category comps the author supplied. If none were given, insert `[COMP — research & verify]` placeholders — **do not generate plausible-sounding titles.** Frame comps as positioning ("for readers of X and Y"), not as claims of equal success.

### Step 4: Bio

One short paragraph from the author's **real** supplied facts (relevant writing, credentials, expertise that lends authority to this book). If unpublished, one graceful confident line — unpublished is normal; **do not apologize or invent credits.** Never fabricate memberships, contest placements, or sales.

### Step 5: Housekeeping & Format

Personalize the opening to the agent **only** from facts the author supplied (a manuscript they repped, a stated wish-list item). If none supplied, use a clean professional opening and mark `[PERSONALIZE — research agent]`. Standard polite close. Note submission norms (paste in body, follow each agency's guidelines).

### Step 6: The Synopsis (1-2 pages)

Write a present-tense, third-person synopsis that:
- Covers the **whole arc including the ending** (synopses reveal the ending — that's their job).
- Follows the protagonist's throughline; names only the few characters essential to the plot (NAME in caps on first mention, per convention).
- Conveys causality and emotional turns, not just events.
- Uses only the plot the author supplied; mark `[PLOT GAP — confirm]` where the arc input is incomplete rather than inventing events.

### Step 7: Anti-Fabrication Check (do not skip)

Scan both documents. Flag **every** unverifiable specific — agent name, agency, comp, comp author, award, publication, membership, sale, wish-list quote. Each must be author-supplied or a clearly bracketed `[PLACEHOLDER — verify]`. Output a "Verify Before Sending" list.

---

## Output Format

1. **Readiness Note** (if manuscript isn't complete/revised, flag before anything else)
2. **Query Letter** (full, formatted: personalization → hook → comps/positioning → bio → close)
3. **Synopsis** (1-2 pages, present tense, whole arc with ending)
4. **Verify Before Sending** (anti-fabrication punch-list of every placeholder)
5. **Submission Notes** (norms + reminders, framed as "confirm against each agency's guidelines")

---

## Quality Indicators

**A strong query + synopsis:**
- [ ] Hook conveys character, conflict, stakes in the book's voice; withholds the ending
- [ ] Metadata correct; word count addressed honestly
- [ ] Comps real, recent, same-category — or clearly flagged placeholders
- [ ] Bio truthful; no apology, no invented credits
- [ ] Synopsis covers the full arc *including the ending*, with causality
- [ ] Zero fabricated specifics; everything unverifiable is bracketed

**Red flags:** invented agents/comps/sales; query that summarizes the plot instead of pitching; rhetorical-question openings; a synopsis that hides the ending; over-long query (aim ~250-350 words).

---

## False-Positive Prevention

**DON'T:**
- Invent any agent, agency, comp title, award, sale, or credential — bracket it `[verify]`
- Generate "plausible" comps the author hasn't read and confirmed are real and recent
- Apologize for being unpublished or pad the bio
- Quietly proceed if the manuscript isn't finished — flag it first
- State precise word-count ranges or submission rules as fact — frame as defaults to confirm

**DO:**
- Treat the no-fabrication guard as the controlling constraint
- Match the query's voice to the manuscript's
- Reveal the ending in the synopsis (that's its function) — but only the author's real ending
- Output a complete verify-before-sending checklist
