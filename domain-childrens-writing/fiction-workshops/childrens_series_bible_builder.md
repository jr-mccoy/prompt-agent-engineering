---
title: "Series Bible & Style-Guide Builder (Early Reader to Middle Grade)"
category: childrens-writing
description: "Build a forward-looking series bible for a children's series (voice and house-style guide, per-book format template, continuity tracker, renewable problem engine, and a cheat sheet for whoever writes book 4+), distinct from the one-step Series Engine in the early-reader workshop and from the adult-fiction continuity audit that extracts a bible from finished books."
techniques:
  - ST-01
  - AG-39
  - OC-03
  - CM-02
  - NE-20
difficulty: advanced
tags:
  - childrens-writing
  - series-bible
  - style-guide
  - chapter-book
  - kidlit
  - planning-a-book-series
  - keeping-books-consistent
updated: "2026-09-24"
related_prompts:
  - domain-childrens-writing/fiction-workshops/childrens_early_reader_chapter_book_workshop.md
  - domain-childrens-writing/craft-tools/childrens_character_creation.md
  - domain-creative-writing/craft-tools/writing_series_continuity_audit.md
---

# Series Bible & Style-Guide Builder (Early Reader to Middle Grade)

## When to Use

- You are planning (or have sold) a series of early readers, chapter books, or middle-grade novels and need one reference document that keeps every book consistent.
- A co-writer, ghostwriter, or future-you will draft later books and needs the voice, format, and continuity rules written down, not carried in one person's head.
- Books 1–2 exist and book 3 is drifting: chapter lengths creep, a sidekick's voice changes, the recurring gag disappears.
- You need to prove to yourself (before pitching "book 1 of a series") that the premise can generate many books, not two.

**Not this prompt if:**
- You are drafting one early reader or chapter book and only need a quick "is this series-able?" check. Use the Series Engine step in `domain-childrens-writing/fiction-workshops/childrens_early_reader_chapter_book_workshop.md`.
- You want to audit finished adult or YA books for contradictions, timeline breaks, and dropped threads. Use `domain-creative-writing/craft-tools/writing_series_continuity_audit.md`.
- You need to keep a character looking the same across illustrations. Use `domain-image-generation/childrens-illustration/childrens_consistent_style_series.md`.
- The series is mature teen YA (explicit content, adult themes). That is out of this domain's 0–14 scope; route to `domain-creative-writing/`.

## Inputs

- **Form and band:** early reader (5–9), chapter book (6–10), middle grade (8–12), or upper-MG crossover (11–14).
- **Series premise:** constant character(s), setting, and the situation that makes new stories.
- **What exists:** pitch only / book 1 drafted / books 1–N published (paste or summarize each).
- **Who writes future books:** the author alone / co-author / ghostwriters / a packager's writer pool.
- **Known constraints** from a contract or editor (word count, chapter count, delivery cadence), if any. Leave blank rather than guess.

## Method

1. **State the series promise in one sentence.** "Every book, [constant character] faces [kind of problem] in [kind of place] and solves it by [signature method], and the reader gets [signature pleasure: laughs, a mystery solved, a new animal fact]." If you cannot fill every slot, the series has no engine yet. Say so before building anything else.
2. **Stress-test the renewable problem source.** List 8 book-length problems the premise generates without strain. Label each *fresh* (new situation), *variant* (a known situation with a twist), or *repeat* (same book with new props). If more than 3 of 8 are repeats, redesign the source: a job that generates cases, a new place per book, a rotating guest character, a collection the protagonist is completing. The child protagonist must solve every one of the 8. An adult solving it breaks the domain's child-agency rule.
3. **Separate the fixed from the free.** Build a three-column table:
   - **Fixed:** never changes (protagonist's age, core personality, the signature method, POV, tense).
   - **Slow-change:** may grow across the series, but only on purpose (a friendship deepening, a skill improving). Record what changed and in which book.
   - **Free:** changes every book (setting of the week, guest characters, the specific problem).
   Ghostwriters break series by treating fixed things as free. This table is the main defense.
4. **Write the voice and house-style guide.** Give concrete, checkable rules, not adjectives:
   - Narration: POV, tense, narrative distance, and 3 sample sentences in voice beside 3 near-misses that are *off* voice, with the reason for each.
   - Each recurring character: speech tics, words they would never say, and how they show fear, joy, and anger in action (not labels).
   - Mechanics: numerals vs. words, invented-word spellings, capitalization of made-up places, sound-effect style (italics? caps?), chapter-title style.
   - Humor rules: what kind of joke this series makes and which it never makes (e.g., no humor at a character's body or identity).
5. **Lock the per-book format template.** Word-count band, chapter count, chapter length range, opening-chapter job, midpoint beat, climax placement, closing beat, and any signature structural element (a list, a map, a "case file" page). Use the README's age-band table as the starting range. Mark any contract-specific figure as `[VERIFY: per contract/editor]`. Do not invent a publisher's house requirement.
6. **Build the continuity tracker.** Tables for characters (name spellings, ages, physical details that appear *in text*, family structure, pets), places (layout facts the text has committed to), objects and rules (what the magic or gadget can and cannot do), and running threads (setups still open, and which book opened each). Each entry cites the book and chapter where it was established. For planned books with no text yet, mark entries *planned* rather than *canon*.
7. **Add a representation line to the tracker.** For every recurring character whose identity the author does not share, record who reviewed the portrayal and when, or `[not yet reviewed]`. The bible never certifies accuracy. It records that review is owed and routes to `domain-childrens-writing/representation-collaboration/childrens_writing_across_difference_audit.md`.
8. **Write the book 4+ cheat sheet.** One page for a new writer: the series promise, the 10 fixed rules, the 5 most common drift errors seen so far, the voice samples, and a pre-submission checklist.
9. **Flag the gaps.** List every place where the author must decide something the existing books have not settled (a birthday, a sibling's name, whether the dog can talk to adults). Do not decide these silently.

## Output Format

```markdown
## Series Promise
[One sentence, all slots filled, or a statement that a slot is missing]

## Renewable Problem Stress Test
| # | Book-length problem | Fresh / Variant / Repeat | Child solves it by… |

## Fixed / Slow-Change / Free
| Fixed | Slow-change (book where it changed) | Free |

## Voice & House-Style Guide
### Narration rules  ### In-voice vs. off-voice samples  ### Character voice cards  ### Mechanics  ### Humor rules

## Per-Book Format Template
| Element | Range / rule | Source (README band / contract [VERIFY] / author choice) |

## Continuity Tracker
### Characters  ### Places  ### Objects & rules  ### Open threads  ### Representation review log

## Book 4+ Cheat Sheet (one page)

## Open Decisions for the Author
- [ ] ...
```

## Verification

- [ ] The series promise has every slot filled, or the gap is named.
- [ ] At least 8 problems are listed, repeats are ≤3, and the child solves every one.
- [ ] Every voice rule is checkable: another writer could apply it to a sentence and say pass or fail.
- [ ] Every format figure is labelled with its source; contract-dependent figures carry `[VERIFY]`.
- [ ] Every continuity entry cites a book/chapter or is marked *planned*.
- [ ] Recurring characters from identities the author does not share have a review-log line and no claim of accuracy.
- [ ] The cheat sheet fits on one page and stands alone.
- [ ] Open decisions are listed, not silently resolved.

## False-Positive Prevention

- **Inventing canon.** The model fills gaps (a middle name, a street layout) and presents them as established. Anything not in the supplied text goes under Open Decisions or is marked *planned*.
- **Adjective-only voice guides.** "Warm, funny, energetic" cannot be enforced. Every voice rule needs a paired in-voice/off-voice example.
- **Stating house or contract rules from memory.** Do not claim what a publisher or packager requires for chapter count, word count, or delivery. Use the README's general bands and flag the rest `[VERIFY]`.
- **Over-freezing the character.** A bible that makes everything *fixed* produces a static protagonist. Keep a deliberate slow-change column so growth across books is planned, not accidental.
- **Scope creep into YA.** If later-book plans move toward mature teen content, say so and route to `domain-creative-writing/`. Do not extend the bible into material outside this domain's scope.

## Example

**Input sketch:** Chapter-book series (ages 7–9), book 1 drafted. Premise: Tavi Okoro-Lind, age 8, runs a "Lost Things Desk" from her family's laundromat. Future books may use a ghostwriter.

**Abbreviated output:**

> **Series Promise:** Every book, Tavi takes a case at the Lost Things Desk, follows clues through her neighborhood, and returns the lost thing by noticing what grown-ups overlooked. The reader gets a solvable mystery plus one laundromat gag.
>
> **Stress test (excerpt):** 1. Lost hearing aid (Fresh). 2. Lost library book (Variant: the "thief" is the book's author). 3. Lost dog (Repeat of a common kidlit case: needs a twist or cut). Repeats: 2/8 ✓
>
> **Fixed / Slow / Free:** Fixed: first-person past, Tavi is 8, she always writes a "Case Card." Slow-change: friendship with Mr. Adeyemi (book 1 wary → book 3 trusted). Free: the lost object, guest characters.
>
> **Voice sample:** In voice: "Lost things are never really lost. They're just somewhere nobody looked." Off voice: "Tavi felt a deep sense of determination." (That is a label, not action, and third person.)
>
> **Format template:** 9–11 chapters `[author choice]`; ~7,000–9,000 words (within the README chapter-book band); Case Card page opens chapter 1 and closes the last chapter.
>
> **Representation log:** Tavi's family background: `[author to specify — never inferred from a name]`; review status: `[not yet reviewed]`. Route to the across-difference audit before book 1 goes out.
>
> **Open decisions:** Does Tavi have a sibling? (Book 1 implies it but never names one.)
