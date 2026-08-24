---
title: "Kidlit Query Letter Builder"
category: childrens-writing
description: "Build a form-specific agent query letter for a children's book — metadata line, personalized hook, pitch, and bio — with kidlit submission norms and a no-fabrication guard on agents and comps"
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RP-02
  - QA-04
difficulty: intermediate
tags:
  - childrens-writing
  - query-letter
  - agent-submission
  - pitch
  - publishing
updated: "2026-06-18"
related_prompts:
  - domain-childrens-writing/publishing-business/childrens_synopsis_submission_package.md
  - domain-childrens-writing/publishing-business/childrens_pitch_comps_market_positioning.md
  - domain-childrens-writing/fiction-workshops/childrens_middle_grade_fiction_workshop.md
---

**Purpose:** Guide a children's-book author through writing a tight, professional agent query letter that follows the conventions of its specific form — picture book, chapter book, middle grade, or YA crossover — so the pitch reads like it came from someone who knows the kidlit market, without inventing a single agent, agency, or comp title.

**When to use:** When you have a polished, finished manuscript (or, for novels, a complete and revised draft) and are ready to query literary agents; when your existing query is generic, too long, or pitched at the wrong form; when you keep getting form-rejections and want to tighten the anatomy.

**Don't use when:** The manuscript isn't finished and revised (querying early is the most common avoidable mistake); you want a synopsis or the full submission package (use the synopsis-and-submission assembler); you're sharpening the logline and comp choices themselves (use the pitch/comps/positioning prompt first, then come back here).

**Input needed:**
- Manuscript metadata: title, age category, genre, final word count
- The story (character + want + obstacle + stakes), and for novels, the broad arc
- Your real bio facts (credentials, publications, relevant background — or "none yet")
- Comp titles you have researched (real, recent books) — or a note that you still need to find them
- The specific agent you're querying (or a note that you'll personalize per-agent)

---

## Your Input

**Title & Form:** [Title — Picture Book / Chapter Book / Middle Grade / YA]
**Metadata:** [Final word count · genre · age range, e.g. "MG contemporary fantasy, ages 8-12"]
**Story Core:** [Character who wants ___ but ___, and the stakes if they fail]
**Plot (novels only):** [The setup, the central conflict, the turn — without the ending]
**Comps (real, researched):** [Title 1 by Author; Title 2 by Author — or "NEED TO RESEARCH"]
**Bio Facts:** [Publications, awards, relevant career/expertise — or "unpublished, no relevant credentials"]
**Target Agent:** [Agent name + agency, or "personalize per agent — placeholder for now"]
**Author-Illustrator?:** [Yes / No — changes picture-book norms]

---

## Instructions

You are a children's literary agent who reads the slush pile. Help the author assemble a query that respects the form's norms and never fabricates a fact. Work the steps, then deliver in the locked format.

### Step 1: Gather and Lock the Metadata Line

Every query carries a one-line "stats" sentence. Confirm the numbers are real and form-appropriate before writing anything else.

| Form | Word-count norm (state the real number) | Plot pitch depth | Illustration handling |
|------|------------------------------------------|------------------|------------------------|
| Picture book | ~Under 600 (often 200-500) | Light — premise + arc, not a full plot | **No art notes, no found illustrator** unless author-illustrator |
| Chapter book | ~4,000-12,000 (by series/age) | Light-to-medium | None |
| Middle grade | ~30,000-55,000 (genre-dependent) | Stronger plot pitch | None |
| YA crossover | ~50,000-90,000 | Full stakes-driven pitch | None |

If the word count falls far outside the norm, flag it — agents read an out-of-range count as a craft signal. **Do not invent a "typical range" you're unsure of; present these as common defaults the author should confirm against current agency guidelines.**

### Step 2: Personalize the Opening (and how to research it)

A query opens with a reason you chose *this* agent. Generic queries read as mass-mailed.

- The author supplies the real personalization. If they haven't, **leave a bracketed placeholder** — `[AGENT NAME]` and `[PERSONALIZATION — e.g., a title they repped, an interview wish-list item, an #MSWL post]` — and tell them where to find it (the agency site, the agent's manuscript-wish-list, recent deal announcements, interviews).
- **Never invent** a book the agent supposedly represents, a wish-list quote, or a personal detail. Fabricated personalization is worse than none.

### Step 3: Write the Hook and the Pitch

- **Hook (1-2 sentences):** the irresistible core — character, desire, the wrench. For novels, end on the stakes.
- **Pitch body:** PB = one short paragraph (premise + emotional arc, no need to spoil the ending). Chapter/MG/YA = one to two paragraphs that build through the central conflict and stop at the brink of the climax — the query *teases*; the synopsis *tells*.
- Keep the manuscript's own voice. A funny book's query should be a little funny.

### Step 4: Write the Bio (including "I'm unpublished")

| Have | Include |
|------|---------|
| Publications/awards | Named, relevant ones only — no padding with non-writing trivia |
| Relevant expertise | If it informs the book (a nurse writing a hospital story) |
| Nothing yet | One graceful line: a short, confident close. Unpublished is normal — do not apologize or invent credits |

**Never fabricate credentials, contest placements, or memberships.** If a fact isn't supplied, leave it out.

### Step 5: Housekeeping, Format & Comps Line

- Standard close: word count + comps + the polite sign-off ("Thank you for your time and consideration").
- **Comps:** use only the real, recent (~last 3-5 years), same-age-category titles the author supplied. If none were provided, insert `[COMP — research & verify]` placeholders — **do not generate plausible-sounding titles.**
- Format: business-letter tone, ~250-350 words total, paste into the email body, no attachments unless the agency's guidelines request them. PB authors: **no illustration notes, no "I've found an illustrator."**

### Step 6: Anti-Fabrication Check (do not skip)

> Scan the finished draft. Flag **every** unverifiable specific: agent name, agency name, comp title, comp author, award, publication, membership, deal, or wish-list quote. Each must be either (a) supplied by the author, or (b) a clearly bracketed `[PLACEHOLDER — verify]`. If you cannot confirm it, you must not assert it. Output a short "Verify Before Sending" list of every placeholder.

---

## Output Format

```markdown
## Metadata Check
- Form: [PB/CB/MG/YA] · Word count: [n] vs. norm: [range] · Genre/age: [...]
- Flags: [anything out of range or norm-breaking]

## Query Letter Draft
[Full letter, paste-ready, with bracketed placeholders for anything unverifiable]

## Verify Before Sending (anti-fabrication list)
- [ ] [AGENT NAME] / agency — confirm spelling, current status
- [ ] [PERSONALIZATION] — research the agent's MSWL/interviews
- [ ] [COMP titles] — confirm real, recent, same age category
- [ ] Bio facts — every credit is true

## Notes for THIS Query
[The 2-3 highest-leverage improvements for this specific letter]
```

---

## Example Output

**Metadata Check:** Form: MG contemporary · Word count: 42,000 (norm ~30-55k ✓) · Genre/age: MG contemporary fantasy, ages 8-12 · Flags: none.

**Query Letter Draft**

> Dear [AGENT NAME],
>
> Because you've said you're looking for [PERSONALIZATION — e.g., "middle-grade fantasy rooted in real grief" per your #MSWL], I hope you'll consider THE LIGHTHOUSE KEEPER'S DAUGHTER, a 42,000-word contemporary middle-grade fantasy.
>
> Eleven-year-old Wren has kept her late father's lighthouse burning every night since he drowned — because the night she forgets is the night, the old stories say, the sea comes back for what it's owed. So when the lamp finally goes dark, and something cold starts climbing the rocks, Wren has three nights to learn what her father really traded to the sea, and what it will cost her to pay the rest.
>
> THE LIGHTHOUSE KEEPER'S DAUGHTER will appeal to readers of [COMP 1 — research & verify] and [COMP 2 — research & verify], pairing a haunted-coast atmosphere with a daughter who refuses to be rescued.
>
> [BIO — author-supplied: e.g., "I grew up on the Maine coast and worked summers as a harbor pilot's apprentice." If unpublished and no relevant background: a single confident closing line.]
>
> Thank you for your time and consideration. The full manuscript is available on request.
>
> Warmly,
> [Author Name + contact]

*Annotations: the opening names a real reason (placeholder until researched); the pitch builds to the climax and stops; the comps and agent are bracketed, not invented; Wren resolves her own crisis (child agency); no moral is stated.*

**Verify Before Sending:** [ ] [AGENT NAME]/agency · [ ] [PERSONALIZATION] · [ ] both [COMP] titles real & recent · [ ] bio facts true.

**Notes for THIS Query:** (1) Tighten the stakes line — "what it will cost her" can name the concrete price. (2) The comps will do heavy lifting; choose two that signal *tone* not just genre. (3) Confirm 42k isn't padded; MG fantasy this age often lands 35-50k.

---

## Quality Indicators

**A strong kidlit query:**
- [ ] Names the correct form and a real, in-range word count
- [ ] Opens with genuine personalization (or a flagged placeholder)
- [ ] Pitches at the right depth for the form (PB light; MG/YA stakes-driven, ending withheld)
- [ ] Carries a bio that's honest, whether credentialed or not
- [ ] Uses only real, recent, same-category comps — or clean placeholders
- [ ] Follows PB norms (no art notes, no found illustrator) when applicable

**Common query pitfalls:**

| Pitfall | Sign | Fix |
|---------|------|-----|
| Wrong form norms | PB query pitches plot like a novel, or includes illustration ideas | Strip art notes; match pitch depth to the form |
| Spoiled or vague | The query gives away the ending, or never names the conflict | Tease to the climax; name character + want + obstacle |
| Padded bio | Lists hobbies, day job, kids' ages | Cut to relevant credits or one graceful line |
| Invented specifics | Comp/agent/award that "sounds right" | Replace with `[placeholder — verify]`; never assert |
| Too long | 500+ words, multiple paragraphs of plot | Cut to ~250-350; one pitch movement |

---

## False-Positive Prevention

**DON'T:**
- Invent agent names, agency names, repped titles, wish-list quotes, comp titles, awards, or publications — ever.
- Add illustration notes or an illustrator to a picture-book query (unless the author is an author-illustrator).
- Generate a "plausible" comp because the author didn't supply one — bracket it instead.
- Inflate an unpublished author's bio to seem more impressive.
- State a word-count "norm" you're unsure of as fact; present ranges as defaults to confirm.

**DO:**
- Ask the form first — it changes word count, pitch depth, and illustration handling.
- Leave every unverifiable specific as a clearly labeled `[placeholder — verify]`.
- Preserve the manuscript's voice in the query's tone.
- Keep the child character as the one who drives and resolves the story in the pitch.
- Route comp-choosing and logline work to the positioning prompt before finalizing.

## Related Prompts

- [childrens_synopsis_submission_package.md](childrens_synopsis_submission_package.md) — Write the one-page synopsis and assemble the full, correctly formatted submission package
- [childrens_pitch_comps_market_positioning.md](childrens_pitch_comps_market_positioning.md) — Sharpen the logline and choose real, honest comp titles before drafting the query
- [childrens_middle_grade_fiction_workshop.md](../fiction-workshops/childrens_middle_grade_fiction_workshop.md) — Develop the MG manuscript itself before querying
