---
title: "Self-Quiz & Recall Drill — Test Your Memory and Comprehension on YOUR Supplied Text"
category: biblical-studies/learner-self-study
description: "Help a solo learner self-test recall and comprehension of a passage or book — but only on text the learner supplies in a named translation. The model never quotes Scripture from memory and never quizzes on wording it generated; questions are built strictly from the learner's pasted text. A personal study tool, not pastoral counseling."
techniques:
  - ST-01
  - ST-02
  - RT-05
  - QA-04
  - QA-05
difficulty: beginner
tags:
  - learner-self-study
  - self-quiz
  - recall
  - retention
  - comprehension
updated: "2026-06-19"
related_prompts:
  - domain-biblical-studies/learner-self-study/biblical_learner_comprehension_self_check.md
  - domain-biblical-studies/learner-self-study/biblical_learner_self_directed_study_plan.md
  - domain-biblical-studies/learner-self-study/biblical_learner_reflection_journal_companion.md
  - domain-biblical-studies/study-methods-teaching/biblical_memorization_retention_plan.md
  - domain-biblical-studies/study-methods-teaching/biblical_inductive_study_method.md
---

# Self-Quiz & Recall Drill

**Objective:** Test your own recall and comprehension of a passage or book using only the text you supply in a named translation — with questions generated strictly from your pasted text, never from the model's memory of Scripture.

> **Boundary guardrail.** These are personal study and formation tools — NOT pastoral counseling, crisis support, or a substitute for church community. Acute spiritual distress, mental-health crisis, abuse, or self-harm routes to a pastor, a licensed counselor, or appropriate emergency services / professionals.

**When to use:**
- You've studied a passage or book and want to check what stuck.
- You're working toward memorization or retention and want active recall.
- You want comprehension questions, not just rote word-recall.

**When NOT to use:**
- You want to explain a passage back in your own words (deeper than recall) — use `biblical_learner_comprehension_self_check.md`.
- You want a full memorization plan with scheduling — use `biblical_memorization_retention_plan.md`.
- You haven't supplied text yet — paste the passage first; the model will not generate verse text to quiz on.

**Audience:** The self-directed individual learner (S).

---

## Inputs / Context

1. **The text (required).** The actual passage(s), pasted by the learner, in a named translation. This is the ONLY source of quiz content.
2. **Goal.** Verbatim recall, fill-in-the-blank, comprehension, or a mix.
3. **Difficulty.** Easier (cued) vs. harder (free recall).
4. **Number of questions.** How many items the learner wants.
5. **Translation.** Named, so the learner knows which wording is being checked.

---

## Constraints

### Must
- Build every question only from the learner's pasted text, in their named translation.
- Tie each question to the address of the verse(s) it tests.
- Provide an answer key derived solely from the supplied text.
- Mix item types (recall, fill-in-blank, comprehension) per the learner's goal.
- If the learner has not pasted text, ask for it — do not proceed from memory.

### Must Not
- Quote, complete, or reconstruct Scripture from memory or from another translation.
- Invent verses, blanks, cross-references, or answers not present in the supplied text.
- Quiz on interpretation as if there were one correct doctrinal answer.
- Substitute model-generated text for the learner's pasted text.

### Tradition-neutral stance (Must / Must Not)
- **Must:** keep recall items factual (what the supplied text says); where a comprehension item touches a contested reading, frame it as "what does the text state" or note that traditions differ.
- **Must Not:** score a contested interpretation as right/wrong; privilege one tradition's reading; smooth disagreement into a single "correct" answer.

---

## Instructions

### Step 1 — Confirm the source text
Verify the learner has pasted the passage in a named translation. If not, request it and stop. Restate the address range and translation.

### Step 2 — Confirm goal and format
Restate the goal (recall / fill-in-blank / comprehension), difficulty, and number of questions.

### Step 3 — Generate items from the pasted text only
Build the requested items, each drawn from and tied to the supplied text by address. Comprehension items ask what the text states, not what it "really means."

### Step 4 — Produce the answer key
Give an answer key derived solely from the supplied text, each answer tagged with its address.

### Step 5 — Self-scoring guidance
Tell the learner how to score honestly (QA-04: partial credit, note gaps) and what a low score signals (re-read, don't guess).

### Step 6 — Next step
Point to comprehension self-check for deeper understanding or the study plan for spaced review.

---

## Output Format

```
# Self-Quiz — [reference], [translation]

## Quiz
1. [question] — (tests [address])
2. ...

## Answer Key
1. [answer from supplied text] — [address]
2. ...

## Self-scoring
- How to score: [..]
- If you scored low: [re-read guidance]

## Next
- [sibling prompt]
```

---

## Verification

- [ ] Every item drawn only from the learner's pasted text in a named translation.
- [ ] Each question tied to a verse address.
- [ ] Answer key derived solely from the supplied text.
- [ ] No Scripture quoted, completed, or reconstructed from memory.
- [ ] No invented verses, blanks, cross-references, or answers.
- [ ] Comprehension items avoid scoring contested interpretation as right/wrong.

---

## False-Positive Prevention

❌ **DON'T:**
- Generate the verse text yourself to build a fill-in-the-blank.
- Quiz on a different translation's wording than the learner supplied.
- Mark a contested interpretation as the "correct" answer.
- Proceed when the learner hasn't pasted any text.

✅ **DO:**
- Require the pasted text and build items only from it.
- Tie each item and answer to an address.
- Keep recall factual and flag contested comprehension as such.
- Give honest self-scoring guidance and a next step.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Opens with the single objective — self-test on learner-supplied text only — making the no-memory constraint explicit from the start.
- **ST-02 (Structured Sequential Instructions):** The numbered sequence (confirm source → confirm format → generate → answer key → self-score → next) enforces the source-text gate before any item is made.
- **RT-05 (Evidence-Based Reasoning):** Every question and answer is traced to the supplied text by address; nothing is asserted without that textual basis.
- **QA-04 (Uncertainty Acknowledgment):** Self-scoring guidance treats partial recall honestly and interprets low scores as a signal to re-read rather than guess.
- **QA-05 (Citation Requirements):** Items are tied to addresses and built only from the named translation the learner pasted; no verse is recalled or invented.
