---
title: "Decodable Text Mechanics (Phonics-Controlled Stories)"
category: childrens-writing
description: "Write or audit a phonics-controlled decodable story against a supplied scope and sequence: word-by-word classification (decodable / taught high-frequency / untaught), substitution fixes, and a story that still has voice and child agency; distinct from the education-teaching phonics scope-and-sequence builder (which designs the instructional sequence) and from the reading-level calibrator (formula-based leveling)."
techniques:
  - CM-02
  - DP-04
  - DD-07
  - CM-09
difficulty: advanced
tags:
  - childrens-writing
  - decodable-text
  - phonics
  - early-reader
  - kidlit
  - write-a-book-my-beginning-reader-can-sound-out
  - phonics-story
updated: "2026-09-24"
related_prompts:
  - domain-education-teaching/instructor/subject-pedagogy/ela/teaching_phonics_scope_sequence.md
  - domain-childrens-writing/craft-tools/childrens_age_reading_level_calibrator.md
  - domain-childrens-writing/fiction-workshops/childrens_early_reader_chapter_book_workshop.md
---

# Decodable Text Mechanics (Phonics-Controlled Stories)

## When to Use

- You are writing a decodable story for beginning readers, where nearly every word must use only the letter-sound patterns the reader has already been taught.
- You have a draft "early reader" and a phonics sequence, and you need to know exactly which words break it.
- A decodable draft passes the word check but reads like a list ("Sam sat. Sam had a hat."), and you want a real story inside the constraint.
- You are writing a series of decodables that climbs through a sequence, and each book must stay inside its stage.

**Not this prompt if:**
- You need to *design* the phonics scope and sequence itself (the order in which sounds and spellings are taught). That is instruction design. Use `domain-education-teaching/instructor/subject-pedagogy/ela/teaching_phonics_scope_sequence.md`.
- You need to hit a Lexile, Guided Reading, or Flesch-Kincaid target. Use `domain-childrens-writing/craft-tools/childrens_age_reading_level_calibrator.md`. Formula levels and phonics decodability are different measures.
- You want general controlled-vocabulary early-reader craft without a phonics sequence. Use `domain-childrens-writing/fiction-workshops/childrens_early_reader_chapter_book_workshop.md`.
- You are planning a reading intervention for a specific child. Use `domain-education-teaching/instructor/student-support/teaching_dyslexia_structured_literacy_plan.md`.

## Inputs

- **The scope and sequence in force:** the list of grapheme–phoneme correspondences (GPCs) and patterns taught *up to and including* the target stage, in the author's or program's own words. If none is supplied, the model must ask for one, or else use a clearly labelled *illustrative* sequence and state that alignment with any real program is not established.
- **Taught high-frequency ("heart"/irregular) words** permitted at this stage.
- **Target stage and approximate length** (words or pages).
- **Story seed or existing draft.**
- **Any decodability threshold** the author or a program requires `[VERIFY: from the program or publisher; do not assume]`.

## Method

1. **Treat the supplied sequence as the authority.** Restate the permitted GPCs and heart words as a locked list. Do not add patterns the author did not list, even common ones. A pattern that is "usually taught by now" is still untaught if the sequence does not include it.
2. **Classify every word in the draft**, token by token:
   - **D (decodable):** every GPC is in the permitted list. Check inflections separately: plural *-s* pronounced /z/, *-es*, *-ed* (three pronunciations: /t/, /d/, /ɪd/), and *-ing* each count only if taught.
   - **H (taught high-frequency):** on the permitted heart-word list.
   - **U (untaught):** anything else. Name the specific untaught element (e.g., "*rain*: vowel team *ai* not yet taught").
   - **N (story name/label):** character names must be decodable too. "Sam" works at an early short-vowel stage; "Chloe" does not.
3. **Report decodability.** Give the count and percentage of D+H tokens and list every U token. Compare against the author's supplied threshold, if one exists. Do not invent a "standard" percentage.
4. **Fix untaught words with ranked substitutions.** For each U word, offer (a) a decodable synonym, (b) a sentence rewrite that removes the need, or (c) a note that it is essential, such as a story name, to be pre-taught or flagged for the adult reader. Never "fix" by swapping in another untaught pattern. Re-check each substitution.
5. **Put a story back inside the constraint.** Decodable text often collapses into list sentences. Apply the domain's core conventions within the permitted words:
   - A child protagonist who wants something and solves the problem themselves.
   - A small arc: want → try → setback → own solution → payoff, even in 60 words.
   - Humor and surprise. A decodable "twist" can be a single word on the page-turn.
   - Varied sentence openings, using taught words only.
   Show the draft before and after for at least one passage.
6. **Check illustrations against the decoding goal.** Many structured-literacy approaches discourage guessing words from pictures. Flag any page where the illustration would let a child guess a word rather than decode it, and any page where art contradicts the text. Treat this as a design note for the illustrator; the author's program decides how strict to be.
7. **Mark stage progression (for series).** If the book belongs to a climbing set, list the new pattern this book practices (its *focus* GPC), confirm it appears often enough to practice, and note which later stage each untaught-but-wanted word would unlock.
8. **Keep claims modest.** State that the audit checks the text against the *supplied* sequence only. Say nothing about alignment with any named commercial program, state standard, or research claim unless the author supplies the source; mark any such claim `[VERIFY]`.

## Output Format

```markdown
## Locked Sequence (as supplied)
- Permitted GPCs/patterns: [...]
- Permitted heart words: [...]
- Source: [author/program — or "ILLUSTRATIVE, not aligned to any program"]

## Word Classification
| Token | Class (D/H/U/N) | Untaught element (if U) |

## Decodability Report
- D+H: [n] / [total] = [%]  ·  Threshold: [supplied value or "none supplied"]
- Untaught tokens: [list]

## Substitution Fixes
| Untaught word | Option A (synonym) | Option B (rewrite) | Option C (keep + flag) | Re-checked? |

## Story Pass (before → after)

## Illustration Notes (guessing risk / contradictions)

## Stage Progression Notes (series only)

## Scope Statement
[Checked against the supplied sequence only; no program-alignment claim.]
```

## Verification

- [ ] Every token is classified; the total matches the draft's word count.
- [ ] Inflectional endings are checked as separate patterns.
- [ ] Every substitution was re-checked and contains no untaught pattern.
- [ ] Names are classified and either decodable or flagged.
- [ ] Any decodability threshold is the author's supplied figure, never a model default.
- [ ] The story pass keeps a child-driven arc and at least one moment of humor or surprise.
- [ ] No claim of alignment with a named program, standard, or study appears without `[VERIFY]`.

## False-Positive Prevention

- **Assuming a sequence.** The most common failure is quietly applying a "typical" phonics order. Different programs sequence differently, so without a supplied sequence, label everything illustrative.
- **Missing morphology.** "Jumped" is not decodable just because "jump" is. The *-ed* ending is its own pattern. The same goes for plural *-s* as /z/ and for *-es*.
- **Counting by spelling, not sound.** "Was" looks CVC but the *a* is not short *a*. "Put" and "push" do not follow the short-*u* rule. Irregular words go in H only if they are on the supplied heart list.
- **Fixing decodability by killing the story.** A 100%-decodable text of flat list sentences fails the domain's respect-the-reader convention. Report the trade-off and show the story pass.
- **Straying into instruction design.** Do not recommend lesson plans, assessments, or teaching order. Route those to `domain-education-teaching/`, as the README boundary requires.

## Example

**Input sketch:** Fictional author Noor Vasquez-Bell. Stage: short vowels *a, i, o*; consonants *s, t, p, n, m, d, g, c/k, r, h, b, f*; digraphs *sh, ck*; plural *-s* as /s/ only. Heart words: *the, a, is, to*. ~50 words. Draft line: *"The ship sailed to the rocks and Pip jumped."*

**Abbreviated output:**

> **Classification (excerpt):**
> | ship | D | — |
> | sailed | U | vowel team *ai* and *-ed* not taught |
> | rocks | D | (*ck* ✓; plural *-s* as /s/ ✓) |
> | Pip | N | decodable name ✓ |
> | jumped | U | *j*, short *u*, and *-ed* not taught |
>
> **Decodability:** 7/9 = 78% on this line (D+H, plus the decodable name *Pip*). No threshold supplied.
>
> **Fixes:** *sailed* → "The ship hit the rocks." (rewrite; re-checked ✓). *jumped* → "Pip hops" rejected: a verb *-s* is not the taught plural *-s*. "Pip ran" accepted (*r, a, n* ✓).
>
> **Story pass:** Before: "Pip is on a ship. Pip is sad." After: "Bam! The ship hit the rocks. Pip got a big mop. Mop, mop, mop! A fish got the mop. Pip got the fish!" (Every token re-checked D/H/N. Pip solves it, and the fish-steals-mop beat supplies the surprise.)
>
> **Scope statement:** Checked against the supplied sequence only. No claim of alignment with any program.
