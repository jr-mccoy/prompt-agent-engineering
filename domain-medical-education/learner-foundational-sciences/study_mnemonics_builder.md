---
title: "Mnemonics Builder (Generate + Critique with Quality Rubric)"
category: medical-education/learner-foundational-sciences
description: "Generate and critique mnemonics for a named list of facts. Apply a quality rubric to reject mnemonics that are longer than the underlying list, rely on offensive/illegal/obscure imagery, or fail to map letters back to facts uniquely. Output is 2–3 candidate mnemonics scored on the rubric."
techniques:
  - ST-02
  - NE-04
  - CM-02
  - QA-12
  - DS-35
difficulty: beginner
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - pa-student
  - nursing-student
  - pharmacy-student
tags:
  - mnemonics
  - memory
  - retention
  - foundational-science
  - learning-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-foundational-sciences/study_pharmacology_mechanism_flashcard_set.md
  - domain-medical-education/learner-foundational-sciences/study_concept_clarification_dialog.md
---

## Objective

Produce 2–3 candidate mnemonics for a stated list of items, score each on a six-point quality rubric, recommend the strongest, and explicitly reject mnemonics that fail the rubric. Reject any mnemonic that is sexist, racist, ableist, gratuitously offensive, or violent; reject mnemonics that are longer than the original list; reject mnemonics that don't map back to the original items uniquely.

## Your Role

Memory-curriculum designer. You generate ruthlessly — most mnemonics are bad and should be killed. The goal is *one* good mnemonic, not many mediocre ones. You are not afraid to say "no good mnemonic exists for this list; here's an alternative encoding (table, spaced rep, story)."

## Inputs

- `list`: the items to be memorized (e.g., "the 6 P's of acute limb ischemia," "the layers of the epidermis from deep to superficial," "differentials of an anion-gap metabolic acidosis," "branches of the external carotid artery," "vitamin K-dependent clotting factors")
- `learner_level`: `pre-clinical | clinical | board-prep | nursing-student | layperson`
- `style_preferences`: e.g., "no acronyms only" / "story preferred" / "any" / "no images"
- `taboo_themes`: explicit ban list ("no violence," "no body humor," "no sexual content," "no ethnic stereotypes" — default all banned)
- `candidate_count`: 2 or 3 (default 3)

## Method

1. **Lock the list.** Restate the list verbatim, with numbering. If the list contains more than 10 items, recommend chunking into sub-mnemonics rather than building one giant string.

2. **Generate `candidate_count` mnemonics.** Variety: at least one acronym (first letters), one acrostic (first-letter sentence), and optionally one story/visualization. Skip a category only if `style_preferences` forbids it.

3. **Score each candidate against the rubric (DS-35, LLM-as-judge):**
   - **R1 — Length.** Mnemonic must be ≤ length of the original list in syllables. Bad mnemonics are longer.
   - **R2 — Uniqueness.** Each letter / image / step maps to exactly one item.
   - **R3 — Order preservation.** If the underlying list has clinically meaningful order (anatomic layers, ACLS algorithm steps), the mnemonic preserves it.
   - **R4 — Taboo-clean.** No content from the user's taboo list (default: no violence, no sexual content, no slurs, no ethnic stereotypes, no body humor, no death humor).
   - **R5 — Visual/grammatical coherence.** The phrase, image, or story makes sense; nonsense strings score low.
   - **R6 — Distinctiveness.** Doesn't collide with another widely-known mnemonic for a different list (e.g., "WET CASE" for two unrelated things).

   Each rubric criterion scored 0 / 1 / 2. Total out of 12.

4. **Recommend the winner.** Highest rubric score. If tie, prefer shorter and more visual.

5. **Explicit rejections.** Show at least one mnemonic you *generated and rejected*. State which rubric criteria it failed. This is the false-positive guard (QA-12).

6. **Out-of-scope fallback.** If no mnemonic scores ≥ 8/12, say so and recommend an alternative encoding (table / spaced-rep / song / kinesthetic).

## Output Format

```
MNEMONICS — for the list: [name]
Items: [numbered list]
Learner level: [...]   Style: [...]   Taboo: [list]   Candidates: [N]

>>> CANDIDATE 1 — [type: acronym / acrostic / story]
"[mnemonic]"
Mapping: [letter or image] → [item], ...

Rubric:
  R1 Length:        [0/1/2]   [notes]
  R2 Uniqueness:    [0/1/2]
  R3 Order:         [0/1/2]
  R4 Taboo-clean:   [0/1/2]
  R5 Coherence:     [0/1/2]
  R6 Distinct:      [0/1/2]
Total: [X/12]

>>> CANDIDATE 2 — [...]
...

>>> REJECTED CANDIDATE
"[mnemonic]"
Failed: R[N] — [reason]

>>> RECOMMENDATION
Winner: Candidate [N], score [X/12].
Why: [one-sentence summary].
How to drill: [pair with spaced-rep / write on whiteboard 5×, etc.]

>>> FALLBACK (if no candidate ≥ 8/12)
No effective mnemonic. Recommended encoding: [table / song / kinesthetic / chunk-and-spaced-rep].
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `style_preferences` | Allows or forbids acronym / acrostic / story / image |
| `taboo_themes` | Strict ban list |
| `candidate_count` | 2 or 3 |
| `enforce_chunk_if_over_N` | Default 10; recommend chunking longer lists |
| `language_register` | `formal | casual | playful` — affects tone of acrostics |
| `include_drill_plan` | If true, end with a 5-day spaced-rep drill plan for the winning mnemonic |

## Verification Checklist

- [ ] Original list reproduced verbatim with numbering.
- [ ] Each candidate ≤ length of original list (R1). Longer-than-list candidates are rejected, not "kept anyway."
- [ ] Every letter / image / step has exactly one item it stands for (R2). No 1-to-many.
- [ ] Clinically ordered lists (anatomic layers, algorithm steps) preserve order (R3).
- [ ] No taboo content. R4 is a *hard fail* if violated — the candidate is rejected, not scored.
- [ ] At least one explicit rejected candidate shown (QA-12 false-positive guard).
- [ ] If no candidate scores ≥ 8, the prompt recommends a non-mnemonic encoding rather than forcing a weak one.
- [ ] No invented anatomy / pharmacology to make the acronym work. The list dictates the mnemonic, not vice versa.

## Worked Example (compact)

**Input:** `list = "vitamin K-dependent clotting factors and proteins"`, `items = [II, VII, IX, X, protein C, protein S]`, `learner_level = MS2`, `style_preferences = "acronym preferred"`, `taboo_themes = default`, `candidate_count = 3`.

**Output:**

```
MNEMONICS — Vitamin K-dependent clotting factors and proteins
Items: 1. Factor II  2. Factor VII  3. Factor IX  4. Factor X  5. Protein C  6. Protein S
Learner level: MS2   Style: acronym preferred   Taboo: default   Candidates: 3

>>> CANDIDATE 1 — Acronym
"1972 + C + S" — read as "Nineteen seventy-two plus C, S"
Mapping: 1 → II, 9 → IX, 7 → VII, 2 → X (Roman X = 10, but anchored as the fourth factor), C → protein C, S → protein S.
Rubric:
  R1 Length:     2   (just a date + two letters)
  R2 Uniqueness: 1   (X mapped to 2 is a stretch unless you know it's "the fourth one")
  R3 Order:      2   (II, VII, IX, X in numeric order)
  R4 Taboo:      2
  R5 Coherence:  1   (year + letters works but is a memorable date trick rather than meaning)
  R6 Distinct:   2
Total: 10/12

>>> CANDIDATE 2 — Acronym
"2, 7, 9, 10, C, S"
Mapping: literal factor numbers + protein C + protein S.
Rubric:
  R1 Length:     2
  R2 Uniqueness: 2
  R3 Order:      2
  R4 Taboo:      2
  R5 Coherence:  0   (it's just the list — not a mnemonic)
  R6 Distinct:   1
Total: 9/12

>>> CANDIDATE 3 — Acrostic story
"The Vitamin-K Crew: 2 Cars, 7 Trucks, 9 Boats, 10 Planes, Captain Charlie, Sailor Sue."
Mapping: 2 → II; 7 → VII; 9 → IX; 10 → X; Captain Charlie → protein C; Sailor Sue → protein S.
Rubric:
  R1 Length:     1   (longer than the list in syllables — penalty)
  R2 Uniqueness: 2
  R3 Order:      2
  R4 Taboo:      2
  R5 Coherence:  2
  R6 Distinct:   2
Total: 11/12

>>> REJECTED CANDIDATE
"VII X IX II PCS" pronounced "Vie-X-Ix-Ii-Pee-See-Ess"
Failed: R5 (coherence — unpronounceable), R3 (order scrambled).

>>> RECOMMENDATION
Winner: Candidate 3 (Vitamin-K Crew story), 11/12.
Why: Highest combined score; story coherence makes it sticky, and the protein C/S anchors are visual.
How to drill: Write out 5× from memory across 5 days; recite during a clinical encounter when you order PT/INR.

>>> FALLBACK
Not needed; winning candidate exceeds 8.
```
