---
title: "Turn My Wrong Answers Into a Study Plan"
category: education-teaching/learner-assessment
description: "Paste in your wrong answers from any quiz or practice test — the model analyzes what each error reveals about your mental model, groups errors into themes, and produces a targeted study plan with specific remediation steps."
techniques:
  - RT-03
  - ST-01
  - DS-01
  - QA-04
  - RT-05
difficulty: beginner
tags:
  - learner-facing
  - self-study
  - wrong-answers
  - error-analysis
  - study-plan
  - exam-prep
  - metacognition
audience: learner
updated: "2026-05-15"
related_prompts:
  - domain-education-teaching/learner-assessment/learner_quiz_to_mastery.md
  - domain-education-teaching/learner-assessment/learner_weak_point_diagnostic.md
  - domain-education-teaching/assessment/assessment_item_analysis_report.md
---

# Turn My Wrong Answers Into a Study Plan

## Objective

Convert a set of wrong answers into a targeted study plan — not "study chapter 3" but a specific analysis of what each error reveals about how you were thinking, a grouped summary of your error patterns, and prioritized remediation steps you can act on immediately.

## Who This Is For

Learners who:
- Finished a practice test or quiz and want to understand their errors, not just count them
- Studied but got things wrong and aren't sure why
- Want to avoid repeating the same errors on the real test
- Need to prioritize limited study time before an exam

## How to Use This Prompt

**Paste this prompt into a conversation with an AI model and include your wrong answers.** The more context you give per wrong answer (the question, what you answered, and what the correct answer was), the more targeted the analysis.

Minimum input: "I got question 4 wrong — I said B, correct was D."
Better input: The full question + your answer + the correct answer.
Best input: The full question, your answer, the correct answer, and your reasoning if you remember it.

---

## Your Inputs

Provide the following:

- **Subject and topic:** [e.g., "AP Chemistry — Stoichiometry and Limiting Reagents"]
- **What this quiz/test was for:** [e.g., "Practice test 2 from my study book" / "Chapter 7 quiz from class"]
- **Your upcoming goal:** [e.g., "AP exam in 3 weeks" / "Midterm Thursday"]
- **Wrong answers:** [For each wrong answer, provide as much as you have:]

```
Q[N]: [Question text or description]
My answer: [What you chose or wrote]
Correct answer: [The right answer]
My reasoning (optional): [What you were thinking when you answered]
```

Repeat for each wrong answer. You can include as few as 3 or as many as 20.

---

## Instructions for the Model

### Step 1: Per-Error Analysis

For each wrong answer, analyze what it reveals about the learner's understanding:

```
ERROR ANALYSIS — Q[N]
─────────────────────────────────────────────
Question: [Description or text]
Learner answered: [Their answer]
Correct answer: [Right answer]
Learner's stated reasoning (if provided): [...]

WHAT THIS ERROR REVEALS:
[Describe what the learner was likely thinking. Not "they got it wrong" — describe their mental model.
e.g., "You applied the limiting reagent calculation correctly for the first compound but treated
the excess reagent as if it fully reacted — this suggests you understand the concept but haven't
yet connected it to the 'compare mole ratios' step."]

TYPE OF ERROR:
[ ] Conceptual gap — missing or wrong understanding of the underlying principle
[ ] Procedural error — right concept, wrong execution (calculation error, formula misapplication)
[ ] Reading/attention error — misread the question, answered a different question
[ ] Partial knowledge — knew part of it, missing the connecting step
[ ] Retrieval failure — likely knew this but couldn't access it under pressure

MISCONCEPTION (if conceptual gap or partial knowledge):
[Name the specific misconception — e.g., "Assumed all reagents react completely" /
"Confused limiting reagent with the one present in smaller amount"]
```

### Step 2: Group Errors by Theme

After analyzing all wrong answers, cluster them by pattern:

```
ERROR THEMES
─────────────────────────────────────────────

THEME 1: [Name the pattern — e.g., "Limiting reagent calculation errors"]
Questions: [Q3, Q7, Q11]
What these have in common: [Describe the shared misconception or procedural gap]
Underlying issue: [The root cause — e.g., "You're finding which reactant is present in smaller
quantity instead of comparing mole ratios to stoichiometry"]

THEME 2: [Name — e.g., "Misreading questions with two-step reasoning"]
Questions: [Q2, Q9]
What these have in common: [...]
Underlying issue: [...]

THEME 3 (if applicable): [...]

SINGLE-ERROR ITEMS (no pattern — isolated mistakes):
Questions: [Q5, Q12] — may be careless errors or one-off gaps
Note: Don't over-invest study time here unless one of these is a high-weight topic
```

### Step 3: Root Cause Analysis

For the largest or most impactful theme:

```
ROOT CAUSE — THEME 1: [Name]
─────────────────────────────────────────────

WHAT YOU CURRENTLY BELIEVE:
[Describe the learner's current mental model in 2–3 sentences — the version that produces these errors]

WHAT'S ACTUALLY TRUE:
[The corrected understanding — clear, precise, and at the learner's level]

WHERE THIS CONFUSION LIKELY COMES FROM:
[Why this misconception makes sense — what prior learning or intuition leads here]

THE KEY DISTINCTION YOU NEED TO MAKE:
"[The thing] is NOT [wrong understanding]. It IS [correct understanding]."
[Concrete example that illustrates this distinction]
```

### Step 4: Prioritized Study Plan

```
STUDY PLAN — RANKED BY IMPACT ON [GOAL]
─────────────────────────────────────────────

PRIORITY 1: [Theme 1 — highest frequency + high-weight topic]
Why it matters: [How often this shows up on [the target exam/test] / How many points it's worth]
Study move: [Specific — not "review limiting reagents" but "work 5 problems where you must
  (1) write the balanced equation, (2) find mole ratios, (3) compare to find the limiting reagent,
  (4) calculate product. Write out every step. Skip calculator shortcuts for now."]
Time estimate: [N hours / N practice sessions]
Check yourself: [How you'll know you've got it — "Do 3 new problems without looking at notes.
  If you get all 3, you're ready."]

PRIORITY 2: [Theme 2]
Why it matters: [...]
Study move: [Specific]
Time estimate: [...]
Check yourself: [...]

PRIORITY 3 (if applicable): [Theme 3]

FOR SINGLE-ERROR ITEMS:
[Address only if these topics are high-weight or if you remember being confused.
Suggested: 20 minutes maximum.]

─────────────────────────────────────────────
TOTAL ESTIMATED STUDY TIME: [N hours]
RECOMMENDED STUDY ORDER: [Priority 1 first — correct the worst root cause before reinforcing partial understanding]

ONE THING TO DO IN THE NEXT 30 MINUTES:
[The single most immediate action — e.g., "Read the mole ratio explanation in [chapter X] and
then do problems 3, 5, and 8 from that section with the steps written out."]
```

---

## What the Model Must NOT Do

- Say "you got this wrong" without explaining what the wrong answer reveals
- Produce a generic study plan ("review chapters 3–5")
- Treat all errors as equally important — rank by theme frequency and topic weight
- Diagnose the same root cause for every error — investigate each one
- Give study advice that doesn't account for the learner's stated deadline

---

## Quality Indicators (Learner Self-Check)

After receiving the analysis:
- [ ] I understand why each wrong answer was wrong (not just that it was wrong)
- [ ] The error themes match patterns I recognize in my own thinking
- [ ] The study plan gives me specific actions, not just topics to review
- [ ] I have a first step I can take right now

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **RT-03** | Error analysis traces the learner's mental model behind each wrong answer. |
| **ST-01** | Structured pipeline: per-error analysis → theme clustering → root cause → study plan. |
| **DS-01** | Error type taxonomy (conceptual / procedural / reading / partial knowledge) structures the classification. |
| **QA-04** | Study plan ranked by impact on the specific stated goal; check-yourself criteria defined. |
| **RT-05** | Root cause explanation and themed grouping build the learner's metacognitive awareness. |
