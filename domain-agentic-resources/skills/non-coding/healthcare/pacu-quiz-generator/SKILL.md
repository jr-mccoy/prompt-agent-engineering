---
name: pacu-quiz-generator
description: Generate knowledge-check quizzes for PACU topics — MCQ, select-all-that-apply (SATA), matching, and scenario-based items, with answer key and rationales that cite source chapters. Use when the user asks for a "quiz", "knowledge check", "competency test", "post-test", or "orientation exam" for a PACU topic. Produces calibrated-difficulty items with distractors that reflect real orientee errors.
tags:
  - pacu
  - nursing-education
  - assessment
  - quiz
updated: "2026-04-14"
---

# PACU Quiz Generator

## Purpose

Build a knowledge-check quiz with items calibrated to the learner level. Items include rationales that teach, not just validate, so a wrong answer becomes a learning moment.

## When to use

- User asks for "quiz", "test", "knowledge check", "post-test", "competency check items".
- Preceptor wants an end-of-orientation-week check.
- Educator wants a pre/post assessment for a huddle topic.

## When NOT to use

- User wants a sign-off checklist → use a competency checklist (out of scope here; see `pacu-case-scenario-writer` for simulated performance).
- User wants flashcards for drill → use `pacu-flashcard-deck-builder`.
- User wants a study guide to prepare *for* a quiz → use `pacu-study-guide-builder`.

## Inputs required

1. **Topic(s).**
2. **Number of items** (default 10).
3. **Item mix** — default: 6 MCQ, 2 SATA, 1 matching, 1 scenario-based. Adjustable.
4. **Difficulty** — orientee baseline / mid-orientation / end-of-orientation / charge-ready.
5. **Source chapters** to anchor rationales.
6. **Include scoring rubric?** (yes/no; default yes).

## Workflow

1. **Confirm inputs.**
2. **Write a blueprint** before items: list the learning objectives the quiz covers, and map each item number to an objective. Reject topics with < 3 objectives (too narrow for a quiz — suggest a flashcard deck instead).
3. **Draft items.** Rules:
   - MCQ: 1 correct + 3 distractors. Distractors reflect plausible orientee mistakes, not nonsense.
   - SATA: 5 options, 2–4 correct.
   - Matching: 5–8 pairs, with 1–2 extra options on the right side.
   - Scenario: 150–250 word vignette → 2–3 sub-questions.
4. **Write rationales** for correct *and* incorrect answers. Cite chapter for the correct-answer rationale.
5. **Tag each item** with its objective and difficulty.
6. **Scoring rubric** — assign points, specify pass threshold (educator sets the cut score; offer a default like 80%).
7. **Self-check.**

## Output format

```markdown
# {Topic} — PACU Knowledge Check

> Safety reminder: Educational assessment only — does not replace clinical competency sign-off.

## Blueprint
| # | Objective | Item type | Difficulty |
|---|---|---|---|
| 1 | ... | MCQ | mid |
...

---

## Items

### 1. [MCQ — mid]
**Q:** ...
A. ...
B. ...
C. ...
D. ...

---

### 2. [SATA — end]
**Q:** Select all that apply.
A. ...
B. ...
...

---

[continue]

## Answer Key & Rationales
**1.** Correct: **C**.
- Why C is right: ... (*Drain's*, Ch. XX)
- Why A is wrong: ...
- Why B is wrong: ...
- Why D is wrong: ...

[continue]

## Scoring Rubric
- Total: XX points.
- Pass threshold: {default 80% — educator adjusts}.
- Remediation cue per missed objective: {suggest revisit of source chapter or skill}.
```

## Source-fidelity rules

- Every correct-answer rationale cites a chapter.
- No invented doses in stems or distractors; use ranges from cited source or "per facility protocol" placeholders.
- Avoid absolutist distractors ("always", "never") — they become tells.

## Self-check

- [ ] Blueprint maps every item to an objective.
- [ ] MCQ stems avoid double negatives and "all of the above".
- [ ] Every item has a chapter-cited rationale for the correct answer.
- [ ] Distractors are plausible orientee errors.
- [ ] Difficulty is labeled per item.
- [ ] Scoring rubric present.
- [ ] Safety reminder at top.
