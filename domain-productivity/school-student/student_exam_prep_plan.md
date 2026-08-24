---
title: "Exam Prep Plan"
category: productivity/school-student
description: "Design a multi-phase exam preparation strategy covering what to study, how to study it, and how to gauge readiness."
techniques:
  - ST-01
  - ST-03
  - DS-02
  - CM-02
  - QA-01
  - RT-06
difficulty: intermediate
tags:
  - exam-prep
  - studying
  - strategy
  - academic
  - readiness
updated: "2026-05-12"
related_prompts:
  - domain-productivity/deep-work/deepwork_decompose_complex_task.md
  - domain-productivity/deep-work/deepwork_focus_parameters_estimator.md
  - domain-productivity/bottlenecks/bottleneck_procrastination_systems_diagnostic.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
---

# Exam Prep Plan

**Objective:** Design a three-phase exam preparation strategy — Coverage, Practice, and Review — that specifies not just when to study but how to study, calibrated to the exam format and what has worked for this student in the past.

**When to use:** When a student has several days to several weeks before an exam and wants more than a schedule — they want a learning strategy. Best used after completing a study schedule (or alongside one). Especially valuable for high-stakes exams or formats the student finds difficult.

**Audience:** High school, undergraduate, and graduate students preparing for a defined exam. Most useful when the exam type is known (multiple choice, essay, problem set, oral, practical). Not for open-ended skill development without an exam target.

---

## Inputs Required

1. **Exam type.** The format of the exam:
   - Multiple choice (recall and recognition under time pressure)
   - Essay or long-form written (synthesis, argumentation, written fluency)
   - Problem set or quantitative (math, science, engineering — solving under test conditions)
   - Oral or presentation (verbal fluency, handling follow-up questions)
   - Practical or lab (applied skill demonstration)
   - Mixed format (describe the mix)

2. **Subject and key topics.** What the exam covers. Include any stated learning objectives, syllabus topics, or professor-flagged areas. More specific is better: "Cell signaling pathways, especially MAPK and PI3K/Akt" beats "Unit 3."

3. **Exam format details (if known).** Number of questions, time limit, open/closed book, point distribution, sample questions or past exams available.

4. **Past exam performance.** How the student has prepared for similar exams before and what happened:
   - What study methods did they use?
   - What did they feel prepared for vs. surprised by?
   - Did they run out of time? Blank on material they had studied? Write unorganized essays?

5. **Time until exam.** Days or weeks remaining. This determines how ambitious the three phases can be.

---

## Instructions

### Step 1 — Identify the exam's actual demands

Before designing prep, characterize what the exam actually tests:
- **Recall-heavy** (definitions, facts, dates): benefits from spaced repetition and flashcards
- **Application-heavy** (problem-solving, case analysis): benefits from practice problems under timed conditions
- **Synthesis-heavy** (essays, arguments): benefits from outlining, writing practice, and peer review
- **Verbal/performance** (oral, practical): benefits from simulation and out-loud practice

State which demand type this exam primarily involves. If mixed, weight the phases accordingly.

### Step 2 — Design the three phases

**Phase 1 — Coverage (first 40–50% of prep time)**
Goal: every topic on the exam has been reviewed at least once.
- Activity depends on demand type: first-read pass for recall exams, worked examples for application exams, outline drafting for essay exams
- Output: a coverage checklist the student can tick off as each topic is reviewed
- Criteria to exit Phase 1: every topic on the exam is checked off at least once

**Phase 2 — Practice (next 35–40% of prep time)**
Goal: test knowledge under conditions resembling the actual exam.
- Activity: practice problems (timed), practice essays (timed), flashcard self-testing, oral Q&A with a study partner or aloud to oneself
- Must simulate exam conditions: closed book (if applicable), time pressure, no checking notes mid-problem
- Output: a running list of topics or question types where errors or uncertainty appear — these feed Phase 3
- Criteria to exit Phase 2: at least one full timed practice session completed; weak spots list generated

**Phase 3 — Review (final 15–20% of prep time)**
Goal: address weak spots only. No re-reading topics already mastered.
- Work through the weak spots list from Phase 2
- One final timed self-test 24–48 hours before the exam
- No new material in this phase

### Step 3 — Define readiness criteria

State specifically what "ready" looks like for this exam type. Examples:
- Multiple choice: "Complete a 50-question practice set in under 45 minutes with fewer than 8 errors, with no full-topic blind spots."
- Essay: "Outline and write a complete essay response in under 40 minutes that covers all three required components without notes."
- Problem set: "Solve practice problems from all major topic areas with fewer than 15% errors under timed conditions."
- Oral: "Answer 10 consecutive unprompted questions on core topics without pausing longer than 5 seconds or needing notes."

Readiness criteria should be measurable and testable — not "feel confident."

### Step 4 — Recommend study methods by demand type

Match specific methods to the exam's primary demand:

| Demand type | High-value methods | Low-value methods (avoid) |
|-------------|-------------------|--------------------------|
| Recall | Spaced repetition (Anki/paper flashcards), self-testing, the Feynman technique | Re-reading notes passively |
| Application | Timed practice problems, worked examples, error analysis | Reading solution walkthroughs without attempting first |
| Synthesis | Timed essay outlines, writing from memory, thesis-first drafting | Re-reading source material without writing |
| Oral/practical | Simulated Q&A out loud, record-and-review, physical practice | Reading silently |

### Step 5 — Flag past-prep mistakes

Based on what the student reported in Input 4, identify the specific prep mistake to avoid repeating:
- Prepared but still got surprised → likely did not practice under exam-like conditions
- Ran out of time on the exam → timed practice was missing from prep
- Blanked on studied material → likely did passive re-reading instead of retrieval practice
- Wrote unorganized essays → did not practice outlining under time pressure

Name the mistake and the correction explicitly.

---

## Constraints

### Must
- Name the exam's primary demand type before designing the phases
- Assign specific activities to each phase (not just "study more")
- Include concrete readiness criteria that are measurable without the student guessing
- Flag and correct at least one prep mistake from the student's past if Input 4 is provided
- State when Phase 2 practice must simulate real exam conditions (closed book, timed)

### Must Not
- Design prep that is entirely passive (re-reading, highlighting, watching videos) for any exam type
- Skip Phase 2 practice even if time is short — compress Phase 1 instead
- Offer generic study tips ("take breaks," "sleep well") unless directly connected to a specific phase
- Define "ready" as a subjective feeling ("feeling confident")
- Add motivational framing or emotional coaching not requested

---

## False-Positive Prevention

1. **Passive prep presented as practice:** Re-reading notes, watching lecture videos, and re-highlighting are coverage activities, not practice. Phase 2 must involve active retrieval — attempting problems or recalling answers without looking at material. Flag if the student's past approach was entirely passive.

2. **Phase 1 that never ends:** Some students stay in coverage mode indefinitely because it feels safer than self-testing. If more than 55% of prep time is allocated to Phase 1, flag it and rebalance.

3. **Readiness criteria that cannot be tested:** "Understanding the material deeply" is not a readiness criterion. It must be operationalized as something the student can actually check (score on practice test, timed essay completion, etc.).

4. **Exam-format mismatch:** Designing an essay-based prep plan for a multiple-choice exam, or a flashcard-heavy plan for a problem-solving exam, is a mismatch. Check that the primary prep activities match the stated exam format.

5. **Ignoring past failure patterns:** If the student reports being "surprised by the exam" repeatedly but the prep plan includes no simulation-under-exam-conditions, the pattern will repeat. The correction must appear in the plan.

---

## Output Format

```
EXAM PREP PLAN — [Subject] — [Exam Type] — Exam: [Date]

EXAM DEMAND PROFILE
Primary demand: [Recall | Application | Synthesis | Verbal/Practical | Mixed]
Weighting: [If mixed, describe the split]
High-value methods for this exam: [List 2–3]
Low-value methods to avoid: [List 1–2]

PAST-PREP CORRECTION
[Only if Input 4 provided]
Past pattern: [What went wrong]
Correction: [Specific change to make in this prep cycle]

PHASE 1 — COVERAGE ([Start date] → [End date], ~[X] days)
Goal: Every exam topic reviewed at least once
Activities:
  - [Specific activity for this demand type]
  - ...
Coverage checklist:
  [ ] [Topic 1]
  [ ] [Topic 2]
  ...
Exit criteria: All topics checked off

PHASE 2 — PRACTICE ([Start date] → [End date], ~[X] days)
Goal: Test knowledge under exam-like conditions; generate weak-spots list
Activities:
  - [Specific timed/retrieval practice activity]
  - [How to simulate exam conditions]
Weak spots log: [Student fills in as errors appear]
Exit criteria: [At least one full timed session completed; weak spots list generated]

PHASE 3 — REVIEW ([Start date] → [End date], ~[X] days)
Goal: Address weak spots only; no new material
Activities:
  - Work through weak spots log from Phase 2
  - Final timed self-test: [Date, 24–48 hr before exam]
Exit criteria: Final timed test meets readiness criteria below

READINESS CRITERIA
You are ready when you can:
  - [Measurable criterion 1]
  - [Measurable criterion 2]
  - [Measurable criterion 3]
```

---

## Verification

- [ ] Exam demand type is named (not assumed)
- [ ] Three phases have distinct activities, not just time labels
- [ ] Phase 2 includes at least one activity that simulates real exam conditions
- [ ] Readiness criteria are measurable — no "feel confident" language
- [ ] A past-prep mistake is named and corrected if Input 4 was provided
- [ ] Phase 1 does not consume more than 55% of total prep time
- [ ] High-value vs. low-value study methods are matched to this exam's format
