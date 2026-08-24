---
title: "Qualifying Exam Question Bank"
category: science/lab-operations-mentorship
description: "Generates a field-specific qualifying-exam question bank with model-answer outlines and a mastery-level grading rubric, spanning foundational concepts, methods, and experiment-design reasoning."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - QA-02
  - DS-02
difficulty: advanced
tags:
  - qualifying-exam
  - candidacy-exam
  - question-bank
  - grading-rubric
  - exam-prep
  - graduate-mentorship
  - critical-reasoning
  - experiment-design
updated: "2026-06-26"
related_prompts:
  - domain-science/lab-operations-mentorship/science_thesis_committee_meeting_prep.md
  - domain-science/lab-operations-mentorship/science_individual_development_plan_drafter.md
  - domain-science/methods-foundations/science_research_question_refiner.md
---

# Qualifying Exam Question Bank

**Objective:** Build a practice question bank for a qualifying / candidacy / comprehensive exam in the user's specific field. It produces categorized questions (foundational concepts, methods, and critical-reasoning / "design an experiment" prompts), a model-answer outline for each, and a mastery-level grading rubric so the candidate can self-assess. The bank is a study tool — it sharpens reasoning and exposes gaps; it is not a leaked exam.

**When to use:** When a PhD student or candidate is preparing for a qualifying/candidacy exam and supplies the field and the topics or reading list the exam will cover, and wants graded practice rather than passive review.

**Required inputs:**
- **Discipline.** Field and subfield (e.g., molecular genetics, physical chemistry, computational neuroscience).
- **Career stage / context.** Year in program, exam type (written / oral / both), and how soon the exam is.
- **Topics / scope.** The concepts, methods, and reading the exam covers, as the candidate understands them (user-supplied).

**Optional inputs:**
- **Exam format.** Closed-book vs open-book, time limits, oral follow-up style, number of examiners — `[user-supplied]` if unknown.
- **Known weak spots.** Topics the candidate finds shaky.
- **Prior questions the program shares.** Sample questions the program has publicly released or the advisor provided.
- **Target depth.** Whether the candidate wants breadth coverage or deep drills on a few topics.

**Constraints — Must:**
- Confirm **discipline** and **career stage / exam type** before generating questions.
- Cover three categories explicitly: (1) foundational concepts, (2) methods/techniques and their assumptions, (3) critical-reasoning and experiment-design questions.
- Provide a **model-answer outline** (key points, not a verbatim essay) and the rubric level a strong answer reaches for every question.
- Build a single shared **mastery-level rubric** (e.g., Insufficient / Developing / Proficient / Mastery) with observable descriptors per level.
- State plainly that these are practice questions generated from the candidate's stated scope, not the actual exam.
- Keep the difficulty calibrated to the stated stage; label each question's difficulty.

**Constraints — Must Not:**
- Do not invent institutional/program requirements, exam content the user hasn't supplied, salary/startup figures, or named people. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not claim or imply any question is an actual or likely exact exam question.
- Do not fabricate field facts, citations, mechanisms, or values inside model answers; where a model answer depends on a specific datum, name the concept and mark specifics `[user-supplied / verify against course materials]`.
- Do not use inflated language ("novel," "groundbreaking," "first-ever," "gold standard") in question or answer text.
- Do not invent program-specific rules about passing scores, retakes, or committee composition.

**Instructions:**

1. **Confirm scope.** Restate discipline, stage, exam type, and the topic list. If exam format or passing rules are unknown, mark them `[user-supplied]` and proceed with practice content only.
2. **Map the topic space.** Organize the candidate's stated topics into the three categories (foundations / methods / critical-reasoning), noting any topic the candidate flagged as weak.
3. **Build the mastery rubric first.** Define 3–4 named levels with observable descriptors (what an answer at each level does and omits). This rubric governs all model answers.
4. **Generate foundational-concept questions.** Write questions that test understanding, not recall alone ("explain why X follows from Y," "what breaks if assumption Z fails"). Tag difficulty.
5. **Generate methods questions.** For each method in scope, ask about when it applies, its assumptions, its failure modes, and how to interpret a confusing result.
6. **Generate critical-reasoning / experiment-design questions.** Pose open prompts ("design an experiment to distinguish hypothesis A from B," "this result is surprising — propose explanations and the next test"). These reward reasoning structure over a single right answer.
7. **Write model-answer outlines.** For each question, list the key points a strong answer covers, common wrong turns, and the rubric level a complete answer reaches. Mark any specific value/citation `[user-supplied / verify]`.
8. **Add a how-to-practice guide.** Recommend a self-grading loop: answer cold → grade against the rubric → identify the missing level → re-attempt; plus oral-rehearsal tips if the exam has an oral component.
9. **Close with a scope honesty note.** Reiterate these are practice questions from the stated scope, and list `[user-supplied]` items the candidate should confirm with their program.

**Output format (locked):**

```
## Exam Context
- Discipline / stage / exam type:
- Topics in scope (user-supplied):
- Exam format: [user-supplied]
- Honesty note: practice questions generated from stated scope; NOT the actual exam.

## Mastery Rubric
| Level | Descriptor (what the answer does / omits) |
|---|---|
| Mastery | |
| Proficient | |
| Developing | |
| Insufficient | |

## Category 1 — Foundational Concepts
| # | Question | Difficulty | Model-answer outline (key points) | Common wrong turns | Level a complete answer reaches |
|---|---|---|---|---|---|

## Category 2 — Methods & Techniques
| # | Question | Difficulty | Model-answer outline | Assumptions / failure modes | Level a complete answer reaches |
|---|---|---|---|---|---|

## Category 3 — Critical Reasoning & Experiment Design
| # | Question | Difficulty | Strong-answer structure | What distinguishes Proficient from Mastery |
|---|---|---|---|---|

## How to Practice
- Self-grading loop:
- Oral-rehearsal tips (if applicable):

## Confirm With Your Program [user-supplied]
- [ ]
```

**Reporting-standard alignment:** No formal reporting standard governs qualifying-exam practice; the mastery rubric aligns to competency-based assessment norms (observable, level-anchored descriptors) and to common graduate-program candidacy-milestone expectations (program-specific; `[user-supplied]`).

**Verification checklist (before delivering):**
- [ ] Discipline and exam type confirmed before generating questions.
- [ ] All three question categories are present and populated.
- [ ] Every question has a model-answer outline and a target rubric level.
- [ ] The mastery rubric has named levels with observable descriptors.
- [ ] No question is presented as an actual/likely exam item.
- [ ] No fabricated field facts, citations, or values; specifics flagged `[user-supplied / verify]`.
- [ ] Inflated language absent from question and answer text.
- [ ] Program rules (passing score, retakes, format) marked `[user-supplied]`, not asserted.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Leak impersonation | "Here are the questions you'll be asked" | State plainly: practice questions from stated scope, not the real exam |
| Fabricated facts | A model answer asserting a specific constant or citation from memory | Name the concept; mark specifics `[user-supplied / verify against course materials]` |
| Recall-only questions | Trivia that tests memory, not understanding | Foundational questions must probe "why/what-if," not just "define" |
| Rubric inflation | Every answer rated "Mastery" | Levels must have distinct, observable descriptors; place each answer honestly |
| Assumed program rules | Asserting a passing threshold or retake policy | Mark all program-specific rules `[user-supplied]` |
| Overclaiming difficulty fit | Questions far above/below the stated stage | Calibrate and label difficulty to the confirmed career stage |
