---
title: "Flashcard Deck Builder (from Lecture, Chapter, or Podcast)"
category: medical-education/learner-study-systems
description: "Convert a chunk of source material (lecture transcript, slide set, textbook section, podcast notes) into a numbered flashcard deck that follows minimum-information, atomic-question rules. Each card is scored against a six-criterion rubric; cards that fail are rewritten or rejected. Output is a printable / Anki-importable deck with explicit rejects shown."
techniques:
  - ST-02
  - ST-03
  - DS-29
  - CM-02
  - NE-04
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - intern
  - resident-junior
  - nursing-student
  - pa-student
  - pharmacy-student
tags:
  - flashcards
  - anki
  - spaced-repetition
  - study-system
  - retrieval-practice
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-study-systems/study_spaced_repetition_schedule_designer.md
  - domain-medical-education/learner-study-systems/study_textbook_chapter_to_anki.md
  - domain-medical-education/learner-study-systems/study_lecture_slide_to_study_guide.md
  - domain-medical-education/learner-foundational-sciences/study_pharmacology_mechanism_flashcard_set.md
---

## Objective

Turn a pasted chunk of source material into a structured flashcard deck of 15–40 cards. Each card is **atomic** (one fact per card), **minimum-information** (the shortest question that still discriminates the target fact), and **cloze-safe** (no ambiguous referents). Reject and rewrite cards that violate the six-criterion rubric. Output is plain text Anki-import-ready plus a printable table.

## Your Role

Senior med-ed knowledge engineer. Your job is to *kill* bad cards, not preserve them. Most first-pass cards are too long, too compound, or test the wrong fact. You generate ruthlessly, audit ruthlessly, and ship fewer-but-better cards.

## Inputs

- `source_type`: `lecture-transcript | lecture-slides | textbook-section | review-article | podcast-notes | board-review-chapter`
- `source_content`: the actual pasted text (or structured slide titles + bullets)
- `learner_level`: `pre-clinical | clinical | intern | resident | nursing-student | pa-student | pharmacy-student`
- `target_card_count`: `15 | 25 | 40` (default 25). Hard cap at 40 — if source is bigger than that, chunk first.
- `card_format`: `basic (Q/A) | cloze | image-occlusion-spec | mixed` (default mixed where source allows)
- `exam_anchor`: optional — `USMLE Step 1 | Step 2 CK | NCLEX-RN | NAPLEX | PANCE | none`
- `skip_topics`: explicit ban list (e.g., "skip embryology", "skip pharmacology of statins — already in my deck")

## Method

1. **Tag the source.** Identify the 5–10 *testable concepts* in the source. A testable concept is something a learner can be quizzed on with a discrete answer. Discard table-of-contents, transitions, summary slides, anecdotes.

2. **Atomize.** For each testable concept, list every discrete fact (one fact = one card). Compound concepts ("name the drug, its mechanism, and its adverse effects") become 3 cards, not 1.

3. **Draft cards.** Apply the **DS-29 med-flashcard pattern library**:
   - **Pattern A — Definition:** "What is X?" → one-sentence definition.
   - **Pattern B — Mechanism:** "How does X cause Y?" → one-clause chain.
   - **Pattern C — Discriminator:** "What distinguishes X from Y?" → 1–2 features.
   - **Pattern D — Trigger / red flag:** "What finding makes you think X?" → 1 finding.
   - **Pattern E — First-step / next-step:** "First step when X?" → 1 action.
   - **Pattern F — Number / threshold:** "What is the cutoff for X?" → 1 number with units.
   - **Pattern G — Cloze:** target word is hidden; the surrounding sentence is sufficient context.

4. **Six-criterion rubric (CM-02 + QA-12 enforcement)** — score each card 0/1/2:
   - **C1 — Atomic.** Tests exactly one fact. Compound = 0.
   - **C2 — Minimum information.** Cue is the shortest viable cue. Verbose stems = 0.
   - **C3 — Cloze-safe / no ambiguous referent.** "It," "this drug," "the disease" without antecedent = 0.
   - **C4 — Discriminating.** Answer can't be guessed from the cue without the fact. "What is the most common cause of...?" with no qualifier often fails C4.
   - **C5 — Stable / not exam-fad.** Doesn't depend on a transient guideline edition more than 2 years old without dating.
   - **C6 — Honest difficulty.** No trick wording, no triple-negatives, no "all of the following except" buried in cloze.

   **A card with any criterion = 0 is rejected and rewritten or killed.**

5. **Show rejects.** Include a `>>> REJECTED CARDS` block with the original draft and which criterion failed. Minimum 2 rejected cards required (NE-04 good-vs-bad calibration; QA-12 false-positive guard).

6. **Pack output.** Two formats:
   - Plain-text Anki import (one card per line, `Q\tA`, or `{{c1::...}}` cloze).
   - Printable table with columns: `#`, `Pattern`, `Front`, `Back`, `Score`.

7. **Coverage map.** End with a 2-column table: testable concept → card numbers covering it. If any concept is uncovered, flag it.

## Output Format

```
FLASHCARD DECK — [source title]
Source type: [...]   Learner level: [...]   Target cards: [N]   Format: [...]   Exam anchor: [...]

>>> TESTABLE CONCEPTS (5–10)
1. [concept]
2. ...

>>> DECK (printable table)
| # | Pattern | Front | Back | Score |
|---|---|---|---|---|
| 1 | A — Definition | ... | ... | 12/12 |
...

>>> DECK (Anki import — tab-separated)
[front]<TAB>[back]
{{c1::[masked term]}} in the context of [surrounding sentence]
...

>>> REJECTED CARDS (minimum 2)
REJECT 1
  Original: Q: "Tell me about diabetic ketoacidosis."  A: "..."
  Failed: C1 (compound — anion gap + insulin deficit + treatment in one card), C2 (verbose).
  Rewritten as: cards #7, #8, #14.

REJECT 2
  Original: ...
  Failed: ...
  Rewritten as: ...

>>> COVERAGE MAP
| Testable concept | Card numbers |
|---|---|
| Insulin deficit → ketogenesis | 7, 8 |
| Anion gap calculation | 14 |
| ...

>>> GAPS
[Concept X not covered — source did not include enough detail to make atomic cards. Skipped.]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `card_format` | Forces basic Q/A, cloze, or image-occlusion (text spec) |
| `target_card_count` | Caps deck size; forces tighter atomization |
| `exam_anchor` | Skews discriminators toward NBME / NCSBN / NCCPA style |
| `learner_level` | Adjusts depth — MS1 cards focus on mechanism, intern cards focus on action |
| `cloze_ratio` | Force `>=50% cloze` for declarative-fact-heavy source |
| `include_image_occlusion` | If source has figures, generate occlusion spec ("mask label 3, ask for what label 3 names") |
| `pair_with_drill` | If true, append a 5-day spaced-rep drill plan keyed to card IDs |

## Verification Checklist

- [ ] Every card scored against the six-criterion rubric; rubric visible to learner.
- [ ] Every card scoring ≥ 10/12; cards below 10 are rewritten or killed (not "shipped anyway").
- [ ] Minimum 2 rejected cards shown with reason and rewrite pointer.
- [ ] No card asks about content not present in the source (no hallucinated facts).
- [ ] Numbers and units are exact (no "approximately 140" if source says 135–145; preserve range).
- [ ] No card is compound (no "and" connecting two facts that should be separate cards).
- [ ] No card uses "it / this / the patient" without antecedent.
- [ ] Coverage map shows which testable concepts are covered; gaps flagged.
- [ ] Anki import block is tab-separated and import-safe (no embedded tabs / unescaped newlines).

## Worked Example (compact)

**Input:** `source_type = lecture-transcript`, `source_content = "[3-sentence excerpt about anion-gap metabolic acidosis: MUDPILES mnemonic, anion gap formula Na - (Cl + HCO3) > 12, treatment of DKA = fluids + insulin + K replacement]"`, `learner_level = MS2`, `target_card_count = 6`, `card_format = mixed`.

**Output:**

```
FLASHCARD DECK — AGMA (excerpt)
Source: lecture-transcript   Level: MS2   Target: 6   Format: mixed

>>> TESTABLE CONCEPTS
1. Anion gap formula
2. Anion gap threshold for "elevated"
3. MUDPILES differential
4. DKA: insulin role
5. DKA: fluid resuscitation
6. DKA: potassium replacement rule

>>> DECK (printable)
| # | Pattern | Front | Back | Score |
|---|---|---|---|---|
| 1 | F — Number | Anion gap formula? | Na − (Cl + HCO₃) | 12/12 |
| 2 | F — Number | Cutoff for elevated anion gap (mEq/L)? | > 12 | 12/12 |
| 3 | G — Cloze | "MUDPILES" → {{c1::Methanol, Uremia, DKA, Propylene glycol, Iron/INH, Lactic acidosis, Ethylene glycol, Salicylates}} | (see cloze) | 11/12 |
| 4 | B — Mechanism | Why give insulin in DKA? | Shuts off ketogenesis and shifts K intracellularly | 12/12 |
| 5 | E — First-step | First fluid in DKA (adult, no shock)? | Isotonic saline | 12/12 |
| 6 | F — Number | Replace K in DKA if serum K < what? | < 5.2 mEq/L (and hold insulin if < 3.3) | 12/12 |

>>> DECK (Anki import)
Anion gap formula?	Na − (Cl + HCO₃)
Cutoff for elevated anion gap (mEq/L)?	> 12
MUDPILES → {{c1::Methanol, Uremia, DKA, Propylene glycol, Iron/INH, Lactic acidosis, Ethylene glycol, Salicylates}}
Why give insulin in DKA?	Shuts off ketogenesis and shifts K intracellularly
First fluid in DKA (adult, no shock)?	Isotonic saline
Replace K in DKA if serum K < what?	< 5.2 mEq/L (and hold insulin if < 3.3)

>>> REJECTED CARDS
REJECT 1
  Original: Q: "Tell me about DKA." A: "It's high anion gap, give fluids and insulin and watch K."
  Failed: C1 (compound — 3 facts in one card), C2 (verbose), C3 (no specific anchor).
  Rewritten as: cards #4, #5, #6.

REJECT 2
  Original: Q: "What's the most common cause of high anion gap?" A: "DKA."
  Failed: C4 (not discriminating — depends on setting / age / context).
  Rewritten as: card #3 (the MUDPILES cloze, which forces full recall of the differential).

>>> COVERAGE MAP
| Concept | Cards |
|---|---|
| Anion gap formula | 1 |
| Anion gap threshold | 2 |
| MUDPILES differential | 3 |
| Insulin role | 4 |
| Fluids | 5 |
| K replacement | 6 |

>>> GAPS
None — all 6 testable concepts covered. Source did not specify exact infusion rates; deferred to a later card set.
```
