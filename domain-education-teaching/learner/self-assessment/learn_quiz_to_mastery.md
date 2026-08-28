---
title: "Quiz Me Until I Master This"
category: education-teaching/learner-assessment
description: "An adaptive quiz loop that quizzes the learner, evaluates answers (requiring reasoning, not just selections), targets follow-up questions at identified gaps, and continues until a mastery threshold is reached — with a final summary of what was mastered and what residual gaps remain."
techniques:
  - ED-01
  - ST-44
  - QA-04
  - QA-11
  - RT-05
difficulty: beginner
tags:
  - learner-facing
  - self-study
  - mastery
  - adaptive
  - quiz
  - formative
  - metacognition
  - study-skills
audience: learner
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner-assessment/learner_weak_point_diagnostic.md
  - domain-education-teaching/learner-assessment/learner_wrong_answers_study_plan.md
  - domain-education-teaching/assessment/assessment_mastery_check_designer.md
---

# Quiz Me Until I Master This

## Objective

Engage in an adaptive quiz loop on a topic of your choice — the model asks questions, evaluates your reasoning (not just your answer), adjusts subsequent questions toward your weakest areas, and continues until you hit a mastery threshold you define. The loop ends with a summary of what you've mastered and any residual gaps.

## Who This Is For

Learners who want to:
- Test their own knowledge before a test, exam, or high-stakes moment
- Find out what they actually know vs. what they just feel like they know
- Build genuine retention through repeated retrieval practice
- Get harder questions in areas where they're weak and confirmation in areas where they're strong

## How to Use This Prompt

**Paste or type this prompt into a conversation with an AI model, then fill in your inputs.**

The model will quiz you interactively — do NOT ask it to generate all the questions at once. The loop only works when you respond to one question at a time.

---

## Your Inputs

Before the loop starts, provide:

- **Topic:** [What you want to be quizzed on — be specific: "Chapter 5 of cell biology" is better than "biology"]
- **Your current level:** [Beginner / Some familiarity / I've studied this / Almost ready for a test]
- **Mastery threshold:** [e.g., "5 correct in a row" / "8 out of 10 correct" / "you decide based on my level"]
- **Question format preference:** [MC / short answer / mixed / "challenge me"]
- **Time I have:** [e.g., 10 minutes, 30 minutes, no limit]

---

## Instructions for the Model

When the learner provides their topic and inputs, run the following loop:

### Phase 1: Calibration (2–3 Questions)

Start with questions that span the topic — one easier, one medium, one harder — to calibrate the learner's actual level.

After each answer:
- **Correct with good reasoning:** Acknowledge → note the strength → next question at same or higher level
- **Correct but reasoning unclear:** Ask: "That's right — but walk me through how you got there." Evaluate the explanation before advancing.
- **Partially correct:** Identify specifically what was right and what was missing → probe question
- **Incorrect:** Don't just say "wrong." Name what the answer reveals: "That tells me you might be thinking [X]. Let me come back to this from a different angle." → simpler question on that subtopic

**Critical rule:** Do NOT accept "the answer is C" or a bare fact as sufficient. Always require the learner to show their reasoning. If they can't explain it, they haven't mastered it.

### Phase 2: Targeted Loop

Based on calibration:
- Track which concepts produced correct, partial, or incorrect responses
- Weight subsequent questions toward identified weak spots
- For each concept where a gap was found: come back to it from a different angle after 2–3 other questions (spaced retrieval)
- For concepts where the learner is strong: occasional confirmation question, then advance

**After each question, state:**
- What you noticed (1 sentence)
- What the next question will target and why (1 sentence)

This makes the loop transparent — the learner knows what you're tracking.

### Phase 3: Mastery Threshold Check

Track the learner's performance by concept:

```
RUNNING TRACK (internal — share on request):
Concept | Questions asked | Correct | Partial | Incorrect | Status
[Name]  | [N]             | [N]     | [N]     | [N]       | Strong / Building / Needs work
```

When the learner has met their stated mastery threshold across the tracked concepts, declare mastery and move to Phase 4.

If the learner explicitly asks for a status update at any point, provide the running track.

### Phase 4: Mastery Summary

When the loop ends (mastery threshold met OR learner says stop), produce:

```
MASTERY SUMMARY
─────────────────────────────────────────────

CONCEPTS MASTERED:
• [Concept] — you demonstrated [specific evidence of understanding]
• [Concept] — [evidence]

CONCEPTS STILL BUILDING:
• [Concept] — you got this right [N/N times] but had trouble when [specific condition]
  → Next study move: [What to do — review this specific thing, not "study more"]

RESIDUAL GAPS (if any):
• [Concept] — this came up [N times] and you're still [describe the gap]
  → This needs more work before your [test/exam/goal]

OVERALL READINESS: [Not ready / Getting close / Ready for a test / Mastered]
TOTAL QUESTIONS: [N]   CORRECT: [N]   CORRECT FIRST TRY: [N]

ONE THING TO DO BEFORE YOUR TEST:
[The single most important study move based on this session]
```

---

## What the Model Must NOT Do

- Accept bare answers without requiring reasoning
- Just say "correct!" or "incorrect!" without explanation
- Ask all questions at the start (this is a loop, not a quiz sheet)
- Repeat the same question wording if you missed it (use a different angle)
- Stop before the stated mastery threshold unless the learner explicitly ends the session
- Give vague study advice ("study more") — all recommendations must be specific

---

## Quality Indicators (Learner Self-Check)

After the session:
- [ ] I had to explain my reasoning, not just give answers
- [ ] The model came back to concepts I struggled with
- [ ] I know specifically what I've mastered and what needs more work
- [ ] I have one concrete next study action

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **ED-01** | Iterative scaffolding: calibrate → target gaps → confirm mastery one concept at a time. |
| **ST-44** | Progressive complexity: questions advance from accessible to deeper as mastery builds. |
| **QA-04** | Mastery threshold defined upfront; loop evaluates against it continuously. |
| **QA-11** | Binary mastery/not-yet check per concept drives the adaptive targeting. |
| **RT-05** | Transparent tracking and mastery summary build learner metacognition. |
