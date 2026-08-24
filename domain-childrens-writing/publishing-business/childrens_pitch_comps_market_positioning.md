---
title: "Pitch, Comp Titles & Market Positioning"
category: childrens-writing
description: "Sharpen a one-line logline, choose and articulate real comp titles, and position a children's book honestly in the kidlit market — with a hard guard against AI-invented titles, authors, and sales figures"
techniques:
  - ST-01
  - CM-02
  - RP-02
  - QA-04
  - OC-03
difficulty: advanced
tags:
  - childrens-writing
  - comps
  - logline
  - positioning
  - publishing
updated: "2026-06-18"
related_prompts:
  - domain-childrens-writing/publishing-business/childrens_query_letter_kidlit.md
  - domain-childrens-writing/publishing-business/childrens_synopsis_submission_package.md
  - domain-childrens-writing/fiction-workshops/childrens_picture_book_workshop.md
---

**Purpose:** Help a children's-book author find the book's hook, distill it into a one-line logline, *choose and articulate* comparable titles the author has actually researched, and position the book honestly in the market — without the AI ever generating a book title, author, or sales figure from memory and presenting it as real.

**When to use:** Before writing a query, when you can't say what your book *is* in one line; when an agent asks "what are your comps?"; when your positioning feels vague or grandiose ("there's nothing like it"); when you have a finished manuscript and need to articulate where it sits and who it's for.

**Don't use when:** The manuscript isn't finished (you can't position what isn't done); you need the full query or synopsis (do those after this); you want the AI to *supply* comp titles for you — that's the one thing this prompt refuses to do, because it cannot verify they're real.

**Input needed:**
- The manuscript's premise, age category, and what makes it distinctive
- Candidate comp titles you've read or researched (real books) — or a plan to find them
- Your sense of the intended reader (who is this *for*?)
- Any honest market context you actually know (not assumed)

---

## Your Input

**Premise & Form:** [One-paragraph premise — age category, genre]
**What's Distinctive:** [The hook — the thing that isn't in every book like this]
**Candidate Comps (real, that you've researched):** [Title by Author; Title by Author — or "need help choosing criteria, I'll research"]
**Intended Reader:** [Who is this for — age, what they love, what they're looking for]
**Known Market Context:** [Anything you actually know to be true — or "none"]

---

## Instructions

You are a children's literary agent who pitches editors. Help the author find the hook, write the logline, and reason about comps — but **never invent a comp.** Work the steps, then deliver in the locked format.

### Step 1: Find the Hook

The hook is the one element that makes this book *this book* — a fresh premise, an unexpected voice, a high-concept "what if," a setting no one's mined.

- Strip the premise to: *who* + *the unusual thing*. ("A lighthouse keeper's daughter who must put out the light to break her father's bargain with the sea.")
- Test it: could this sentence describe a hundred other books? If yes, dig for the specific, ownable angle.
- The hook is what the logline and the comps both serve.

### Step 2: Draft the Logline

Two reliable shapes:

| Formula | Example |
|---------|---------|
| "For fans of [X] and [Y], this is a [age/genre] about [character + hook]." | "For fans of [COMP A] and [COMP B], this is a middle-grade ghost story about a girl who must extinguish her dead father's lighthouse to break his debt to the sea." |
| Stakes shape: "[Character] must [action] before [stakes]." | "Wren has three nights to learn what her father traded to the sea — before it takes her too." |

Keep it one breath. Lead with character + desire + the wrench. (The `[COMP]` slots stay bracketed until Step 3 verifies real titles.)

### Step 3: Comp-Title Criteria + How to Research (the AI does NOT invent comps)

A comp is a **real, published book** that signals where yours sits. Good comps are:

| Criterion | Why |
|-----------|-----|
| **Recent** (~last 3-5 years) | Shows you know the current market |
| **Same age category** | An MG book comps to MG, not adult or PB |
| **Successful but not a mega-hit** | Comping to the single biggest title of the decade reads as naïve; aim for solid, respected books |
| **Illuminates positioning** | Speaks to *tone, voice, or angle* — not just "it's also fantasy" |
| **Real** | The author has read or verified it exists |

**Where to find real comps:** the author's own reading; bookstore/library shelves in the category; recent Publishers Marketplace deal announcements; "if you liked X" lists; award shortlists; the backlists of agents you're querying.

> **The AI must not generate comp titles, author names, imprints, or sales figures.** Provide the *criteria* and the *research method*. If the author supplied candidates, evaluate those against the criteria. If they supplied none, output `[COMP — author to research & verify]` placeholders — never a "plausible" title.

### Step 4: Articulate the "X meets Y" Pitch

Once the author has real comps, sharpen the comparison so it does *work*, not just name-drop:

- "[X]'s [quality] meets [Y]'s [quality]" — e.g., "the haunted-coast atmosphere of [COMP A] meets the fierce daughter-grief of [COMP B]."
- Each comp should add a *different* dimension (one for tone, one for structure or audience). Two comps that say the same thing waste a slot.
- If a candidate doesn't survive the criteria in Step 3, cut it — a weak comp hurts more than a missing one.

### Step 5: Honest Market Positioning

Where does this book sit, and who is it for — stated plainly, without hype.

- **Audience:** the real reader ("kids 9-12 who loved spooky-but-not-gory ghost stories and want a heroine who saves herself").
- **Shelf placement:** the section, the adjacent books, the gap it fills.
- **No market-size hype.** Avoid "everyone will love this," "huge untapped market," invented trend claims, or fabricated sales/category statistics. If you don't know a market fact, say so.

### Step 6: Anti-Fabrication Verify (dedicated, do not skip)

> Scan everything produced. **Flag every comp title, author, imprint, award, sales number, advance figure, and market statistic.** Each must be either (a) supplied/verified by the author, or (b) a bracketed `[VERIFY]` / `[author to research]` placeholder. The AI asserts *zero* book titles or market figures from its own memory. Output a "Comp & Claim Verification" list enumerating every item the author must confirm before using any of this publicly.

---

## Output Format

```markdown
## Hook
[The one ownable element, in a sentence]

## Logline
[One-line pitch; comps bracketed until verified]

## Comp Criteria Applied
[For each author-supplied candidate: meets/fails which criteria, keep/cut]
[If none supplied: research instructions + [COMP — verify] placeholders]

## "X meets Y" Pitch
[Sharpened comparison — each comp doing different work; comps bracketed if unverified]

## Honest Positioning
- Audience: [the real reader]
- Shelf: [where it sits]
- No hype claims

## Comp & Claim Verification (anti-fabrication list)
- [ ] [COMP A] — real, recent, same category? (author confirms)
- [ ] [COMP B] — real, recent, same category? (author confirms)
- [ ] Any market/sales claim — sourced or removed
```

---

## Example Output

**Hook:** A grieving daughter who must *put out* the lighthouse — the opposite of her job — to break her dead father's unfinished bargain with the sea.

**Logline:** "For fans of [COMP A — verify] and [COMP B — verify], THE LIGHTHOUSE KEEPER'S DAUGHTER is a middle-grade ghost story about a girl who has three nights to learn what her father traded to the sea before it comes back for her."

**Comp Criteria Applied:** *Author supplied no candidates.* Research instruction: browse recent (2021-2026) MG "atmospheric/spooky grief" titles on library shelves and award shortlists; pick one for **coastal-gothic tone** and one for **child-grief-with-agency**. Insert as `[COMP A — verify]` / `[COMP B — verify]`. **No titles invented here.**

**"X meets Y" Pitch:** "[COMP A]'s haunted-coast dread meets [COMP B]'s portrait of a child who refuses to be rescued." (One comp carries *tone*, the other carries *character stance* — different work each.)

**Honest Positioning:** Audience — readers 9-12 who want spooky-not-gory and a heroine who saves herself. Shelf — MG fiction, beside contemporary-fantasy and ghost stories. No claim about market size or sales is made; the author has not verified any.

**Comp & Claim Verification:** [ ] [COMP A] real/recent/MG? · [ ] [COMP B] real/recent/MG? · [ ] no market or sales figure asserted ✓.

*Annotations: every comp slot is a placeholder, never a generated title; the positioning names a real reader without hype; the verification list forces the author to supply the comps.*

---

## Quality Indicators

**Strong pitch, comps & positioning:**
- [ ] The hook names one ownable, specific element
- [ ] The logline lands in one breath, character + desire + wrench first
- [ ] Comp criteria are applied; weak comps are cut
- [ ] Each comp does *different* positioning work
- [ ] Positioning names a real reader and shelf, with no market hype
- [ ] Every comp/claim is author-verified or bracketed `[verify]`

**Common positioning pitfalls:**

| Pitfall | Sign | Fix |
|---------|------|-----|
| AI-invented comps | A title that "sounds real" appears unsourced | Bracket it; require author research |
| Mega-hit comps | Comping to the decade's single biggest book | Choose respected, mid-list-successful titles |
| Redundant comps | Both comps say "it's fantasy" | Make one carry tone, one carry audience/structure |
| "Nothing like it" | Author claims no comps exist | Find adjacents; "no comps" reads as not-well-read |
| Market hype | "Huge untapped market," invented stats | State the real reader; drop unsourced numbers |

---

## False-Positive Prevention

**DON'T:**
- Generate comp titles, author names, imprints, awards, advances, or sales/market figures from memory and present them as real — this is the load-bearing rule.
- Comp to the single biggest blockbuster in the category (reads as naïve).
- Let two comps make the same point.
- Inflate the market with invented trends or statistics.
- Write a logline that could describe a hundred other books.

**DO:**
- Supply comp *criteria* and a *research method*; make the author find and verify the titles.
- Bracket every unverifiable title or figure as `[verify]` and enumerate them.
- Choose comps that are real, recent, same-category, and illuminate positioning.
- Position honestly: a real reader, a real shelf, no hype.
- Lead the logline with the character, the want, and the obstacle.

## Related Prompts

- [childrens_query_letter_kidlit.md](childrens_query_letter_kidlit.md) — Drop the verified logline and comps into the agent query
- [childrens_synopsis_submission_package.md](childrens_synopsis_submission_package.md) — Build the synopsis and submission package once positioning is set
- [childrens_picture_book_workshop.md](../fiction-workshops/childrens_picture_book_workshop.md) — Develop a picture-book manuscript before positioning it
