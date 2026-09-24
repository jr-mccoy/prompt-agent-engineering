---
title: "Illustration Brief for Hire — Self-Publishing Children's Author"
category: childrens-writing
description: "Build the brief and deal checklist a self-publishing children's author sends when hiring a human illustrator — scope and page count, story-critical visual facts, style references that don't ask for a copy of a living artist, schedule and revision rounds, and the rights and payment terms to settle in writing — with no invented rates or legal terms; distinct from childrens_illustrator_collaboration.md (art notes and dummy for traditional submission) and from the AI-image prompts in domain-image-generation/childrens-illustration/."
techniques:
  - NE-20
  - CM-03
  - CM-09
  - OC-10
  - QA-01
difficulty: intermediate
tags:
  - childrens-writing
  - illustrator
  - self-publishing
  - illustration-brief
  - hiring-an-illustrator
  - how-to-brief-an-artist
  - picture-book
updated: "2026-09-24"
related_prompts:
  - domain-childrens-writing/representation-collaboration/childrens_illustrator_collaboration.md
  - domain-legal/contracts-transactional/legal_licensing_agreement_drafter.md
  - domain-image-generation/childrens-illustration/childrens_consistent_style_series.md
---

# Illustration Brief for Hire — Self-Publishing Children's Author

## When to Use

- You are self-publishing (or running a small press) and will hire and pay a human illustrator directly.
- You need a written brief to send to candidate illustrators so their quotes are comparable.
- You've found an illustrator and need to settle scope, schedule, revisions, credit and rights before any work starts.
- A previous commission went wrong (scope creep, endless revisions, unclear ownership) and you want a tighter brief next time.

**Not this prompt if:**
- You're submitting a picture-book manuscript to agents or editors — the publisher hires the illustrator; use `domain-childrens-writing/representation-collaboration/childrens_illustrator_collaboration.md` for art-note discipline.
- You want to generate images with an AI model — use `domain-image-generation/childrens-illustration/childrens_book_illustration_spread.md` and its siblings.
- You need the contract itself drafted or reviewed — this prompt produces a term checklist; take it to `domain-legal/contracts-transactional/legal_licensing_agreement_drafter.md` and a qualified lawyer.
- You need print specs, ISBNs or distribution setup — those belong to a self-publishing production prompt, not an illustration brief.

## Inputs

- **The manuscript**, paginated if possible, with any story-critical art notes already written.
- **Book specs you have decided:** format (board / picture book / chapter book with spot art / cover only), page count, trim size and orientation if chosen — or "undecided".
- **Deliverables you need:** cover (front only or full wrap), interior spreads/spots, character sheet, sketches, file formats.
- **Style direction:** what you love about 2–5 published books or portfolios (the qualities, not "make it look like X"), plus the illustrator's own portfolio pieces you responded to.
- **Budget and timeline:** your real budget and your launch date — or "need to research".
- **Characters and settings:** who appears; any identity, disability or cultural details that are story-critical; whether you share those identities.
- **Rights you think you need:** print, ebook, audio cover, merchandise, translations, promotional use.

## Method

You are a picture-book art director who now consults for independent authors. You respect that the illustrator is a co-author of the book, not a pair of hands, and you know most commissioning disasters come from an unclear brief rather than a bad artist. Work the steps, then deliver in the locked format.

1. **Define scope precisely (CM-03).** Convert the manuscript into a deliverables list: number of full spreads, single pages, spot illustrations, cover elements, end papers, character sheet. Mark which pages carry text so the illustrator can plan text-safe space. If trim size or page count is undecided, flag it — both change the illustrator's layout and price.
2. **Separate story-critical facts from art direction.** Carry over the discipline from `childrens_illustrator_collaboration.md`: the brief states what must be *true* in the images (the dog is missing one ear; the red scarf recurs; the reveal happens on the page turn at spread 11), and leaves composition, palette and character design to the illustrator unless a fact requires it. List the facts in a table by spread.
3. **Write style direction that describes qualities.** Translate the author's references into qualities — "loose watercolour texture, lots of white space, expressive faces, humour in the background details". Do not ask a hired illustrator to imitate a named living artist's style; point to the illustrator's own portfolio pieces instead. If the author supplies references, list them as "author-supplied, for mood only".
4. **Representation and authenticity (humility rule).** If characters belong to communities the author or illustrator does not share, the brief says so plainly and proposes a paid authenticity/sensitivity reader for sketches, not only for text. The AI can list details that need checking (hair, dress, food, home, assistive devices, skin-tone consistency across spreads); it never certifies that reference imagery or depictions are accurate.
5. **Schedule with named checkpoints.** Character sketches → thumbnail dummy → rough sketches → colour sample spread → finals, with author feedback windows at each. State the number of revision rounds included at each stage and what counts as a revision versus a change of brief. Dates come from the author; if absent, show the sequence with `[date]` placeholders.
6. **Build the deal-terms checklist (CM-09, OC-10).** Items to settle in writing, each with the question to ask rather than an answer: fee structure (flat fee, per-spread, advance plus royalty) — `[VERIFY: author's budget and illustrator's quote]`; payment schedule tied to milestones; kill fee if the project stops; who owns the copyright in the art versus what licence the author receives (which formats, territories, term, exclusivity); merchandise and derivative use; credit line on cover and interior; the illustrator's right to show the work in their portfolio; file delivery (layered files or flattened, colour mode, resolution); whether AI tools may be used by either party. The model states no "standard" rate, royalty percentage or legal default — these vary and must be researched and reviewed by a lawyer.
7. **Compile a sendable brief and an internal checklist.** The brief goes to the illustrator; the checklist stays with the author and feeds the contract conversation.

## Output Format

```markdown
## Project Summary (for the illustrator)
Title · Format · Age band · Page count / trim [or UNDECIDED] · Launch target

## Deliverables
| Item | Count | Text on page? | Notes |

## Story-Critical Visual Facts
| Spread / page | Must be true in the image | Why it matters |

## Style Direction
Qualities: … · Author-supplied references (mood only): … · Your portfolio pieces we responded to: …

## Characters & Representation
[character list] · Authenticity review plan: …

## Schedule & Revision Rounds
| Stage | Deliverable | Author feedback window | Revisions included |

## Deal-Terms Checklist (settle in writing; lawyer review)
- [ ] Fee structure — VERIFY
- [ ] …

## Open Decisions for the Author
- …
```

## Verification

- [ ] Every page of the manuscript maps to a deliverable line; nothing is left implicit.
- [ ] Story-critical facts are facts, not palette, composition or character-design direction.
- [ ] Style direction names qualities; no request to replicate a named living artist.
- [ ] Characters from communities the creators don't share trigger an authenticity-review step on the art.
- [ ] Revision rounds are counted per stage and "change of brief" is defined.
- [ ] Copyright ownership, licence scope, kill fee, credit and portfolio use each appear on the checklist.
- [ ] No rate, royalty percentage, or legal default is stated as standard; each is VERIFY.

## False-Positive Prevention

1. **Quoting "going rates".** The model will offer per-spread prices or royalty splits from memory. These vary by market and experience and change over time; leave `[VERIFY]` and point the author to illustrator and author organisations' current guidance.
2. **Assuming the author owns everything once paid.** Paying for art does not by itself settle copyright or licence scope; present ownership as a term to negotiate and have reviewed, not a default.
3. **Over-directing the art.** A brief that specifies every palette and pose recreates the art-note mistake at contract scale and produces stiffer books. Keep to story-critical facts.
4. **Style mimicry.** Asking for "exactly like [famous illustrator]" invites legal and ethical trouble and ignores the hired artist's own voice.
5. **Certifying depictions.** Do not tell the author that a character's depiction or reference photo set is culturally accurate; route to a qualified reader.
6. **Silent on AI use.** Leaving AI tool use unaddressed causes disputes later; include it as an explicit checklist item.

## Example

**Input sketch:** Fictional self-published picture book *Grandpa Tavi's Kite Shop*, 32 pages, 14 spreads, trim size undecided. Deliverables: front cover, 14 spreads, character sheet. Grandpa Tavi uses a wheelchair; the author does not. Budget: "need to research". Launch: next spring.

**Abbreviated output:**

- **Project Summary:** Picture book, ages `[author to confirm]` · 32 pp · trim UNDECIDED (decide before thumbnails — affects layout and quote).
- **Story-Critical Visual Facts (excerpt):**
  | Spread | Must be true | Why |
  |---|---|---|
  | 3 | The blue fish kite is visible on the shop wall | It's the kite Nia chooses on spread 12 |
  | 9 | Grandpa's wheelchair is part of the shop's layout (low counters, ramp) | The shop is built around him; it is not a plot point |
  | 12 | The kite rises on the page turn | The reveal lands on the turn |
- **Characters & Representation:** The author lacks lived experience of wheelchair use and the illustrator's is unknown → budget a paid disability-authenticity review at character sheet and rough-sketch stages. The AI has not verified any depiction.
- **Deal-Terms Checklist (excerpt):** [ ] Fee: flat vs per-spread — VERIFY budget and quotes · [ ] Licence: print + ebook, which territories, what term — lawyer review · [ ] Kill fee at each milestone · [ ] Illustrator portfolio use after launch · [ ] AI tools: permitted or not, for either party.
