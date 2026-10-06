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
updated: "2026-10-06"
related_prompts:
  - domain-image-generation/social-media/social_thumbnail_cover_brief.md
  - domain-professional-writing/content-production/content_long_form_script.md
  - domain-professional-writing/content-production/content_repurpose_one_to_many.md
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

## False-Positive Prevention

1. **Limits come from the input, not from memory.** Use the title/description limit the user
   supplied; if none was given, write `[VERIFY: current platform limit]` rather than quoting a
   figure. Search results also truncate by display width, so a title under the character cap can
   still cut off before its keyword.
2. **"Truthful to content? Yes" is a claim, not a tick.** A numbered title ("7 ways…") needs seven
   in the content; a superlative ("the fastest…") needs a comparison the content actually makes;
   a curiosity title needs the reveal to be in the piece, not implied by it.
3. **Search-volume figures are not in the input.** Do not annotate titles, keywords or tags with
   monthly searches, difficulty scores, or "high-volume" labels unless the user supplied keyword
   tool data. Tag order is a relevance judgment; say so.
4. **Stuffing hides in variants.** "budget travel, budget travel tips, travel on a budget, cheap
   budget travel" is one term four times; count stems, not exact strings.
5. **Verify before handing over:** recount the Chars column for every title and the description
   (spaces included) against the supplied limit; count occurrences of the primary keyword stem
   across description and tags; for each title, quote the line of `<content_summary>` that pays it
   off — a title with no quotable line comes out of the table.

---

## Verification *(QA-01)*

**Quick self-check (always):**
- [ ] Every title is deliverable by `<content_summary>` (no clickbait gap).
- [ ] All titles within platform character limits.
- [ ] Description has no invented facts and no keyword stuffing.
- [ ] Primary topic appears naturally; tags ordered by relevance.
