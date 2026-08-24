---
title: "SEO Title, Description & Tags Packager"
category: content-creation/discovery
description: "Generate platform-appropriate titles, a structured description, and tags that maximize discovery and CTR without clickbait or keyword stuffing, grounded in the actual content."
techniques:
  - ST-01
  - CM-01
  - RT-02
  - CM-02
  - ST-03
  - QA-01
difficulty: beginner
tags:
  - faceless
  - seo
  - metadata
  - titles
  - discovery
updated: "2026-05-27"
related_prompts:
  - content_thumbnail_image_brief.md
  - content_long_form_script.md
  - content_repurpose_one_to_many.md
---

# SEO Title, Description & Tags Packager

**Objective:** Produce a set of test-ready titles plus a structured description and tag set that
improve discoverability and click-through while accurately representing the content — no clickbait,
no keyword stuffing. *(ST-01)*

---

## When to Use

Packaging a finished or outlined piece for a search/recommendation-driven platform (YouTube, blog,
podcast directory, etc.). Pair with the thumbnail prompt — title and thumbnail are tested together.

---

## Inputs / Context *(CM-01)*

**Required:**
- `<content_summary>` — what the piece actually covers and its payoff.
- Platform and its title/description limits.
- Primary topic/keyword the audience would search.

**Optional:**
- Channel voice / naming conventions.
- Competing titles in the niche.
- Timestamps/chapters, links, and a CTA for the description.

**If `<content_summary>` or platform is missing:** Ask. Limits and accuracy depend on both.

---

## Constraints *(CM-02)*

**Must:**
- Keep every title truthful to `<content_summary>` — the content must deliver the title's promise.
- Front-load the primary keyword/topic naturally where the platform rewards it.
- Respect the platform's character limits exactly. *(ST-03)*
- Offer a spread of title angles for testing. *(RT-02)*

**Must Not:**
- Use clickbait the content doesn't pay off, or ALL-CAPS/excessive-emoji bait unless on-brand.
- Keyword-stuff the description or tags (repeating terms unnaturally).
- Invent stats, names, or claims for the description that aren't in `<content_summary>`.

---

## Instructions *(ST-02)*

1. Identify the searchable intent + the payoff in one line. If the payoff is weak, flag it.
2. Generate titles across angles: keyword-led, curiosity, benefit/outcome, contrarian, numbered. Label each and note character count. *(RT-02)*
3. Write a description: hook line → 2–4 sentence summary → chapters/timestamps (if given) → links/CTA. Natural keyword use only.
4. Propose a tag/keyword set ordered by relevance (no stuffing).
5. Recommend the top 2 titles to test with the thumbnail, and why.

---

## Output Format *(ST-03)*

### Search Intent
One line: what the viewer is looking for + the payoff.

### Titles
| # | Title | Angle | Chars | Truthful to content? |
|---|---|---|---|---|

### Description
The full description block, ready to paste.

### Tags / Keywords
Comma-separated, ordered by relevance.

### Top 2 to Test
Ranked, one-line rationale each.

---

## Verification *(QA-01)*

**Quick self-check (always):**
- [ ] Every title is deliverable by `<content_summary>` (no clickbait gap).
- [ ] All titles within platform character limits.
- [ ] Description has no invented facts and no keyword stuffing.
- [ ] Primary topic appears naturally; tags ordered by relevance.
