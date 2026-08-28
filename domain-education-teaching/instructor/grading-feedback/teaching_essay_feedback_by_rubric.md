---
title: "Essay Feedback by Rubric Criterion"
category: education-teaching/grading-feedback
description: "Generate criterion-by-criterion essay feedback that quotes specific student evidence, names a single highest-leverage revision, and produces a one-line warm + cool summary — without rewriting the student's work."
techniques:
  - CM-01
  - ST-02
  - OC-01
  - QA-02
  - RT-04
difficulty: intermediate
tags:
  - grading
  - feedback
  - essay
  - writing
  - rubric
  - revision
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/teaching_student_feedback_composer.md
  - domain-education-teaching/teaching_assessment_rubric_builder.md
  - domain-education-teaching/grading-feedback/grading_whole_class_feedback_memo.md
---

# Essay Feedback by Rubric Criterion

## Objective

Produce criterion-by-criterion feedback on a single student essay. Quote the student's own evidence for each comment, name a single highest-leverage revision, and stay strictly out of rewriting. Designed for student growth, not validation.

## When to Use

- Returning constructed-response or essay work
- Conferring prep — what to discuss with the student
- Building feedback that drives revision
- Calibrating across a stack — feedback follows the rubric, not subjective response

## When NOT to Use

- Whole-class trends from many essays — use `grading_whole_class_feedback_memo.md`
- Generic strengths-based comment for a transcript — use `teaching_student_feedback_composer.md`
- Teacher needs to write the essay for the student — explicitly out of scope

---

## Inputs Needed

- **Student essay (full text):** [...]
- **Rubric used:** [Criteria + level descriptors]
- **Grade / course:** [...]
- **Genre:** [Argument / informational / narrative / literary analysis / DBQ / other]
- **Stage of process:** [Draft / final / revision check]
- **Feedback length cap:** [Short comment / paragraph / full sheet]
- **Tone preference:** [Direct / warm / mix — default: direct + warm]

---

## Instructions

### Step 1: Read for Comprehension First

Before commenting, summarize in one internal sentence what the student is trying to argue/explain/narrate. If the essay's purpose is unclear, note that as the first observation — without it, criterion feedback isn't useful.

### Step 2: Score Against the Rubric

For each criterion, assign a score and locate **specific text evidence** in the student's writing. No score without quoted evidence.

| Criterion | Score | Evidence (quoted from student) |
|-----------|-------|-------------------------------|

### Step 3: Generate Per-Criterion Feedback

For each criterion, produce:

```
CRITERION: [Name]
Score: [N]
What's working: [1 sentence quoting student evidence — "When you write '[quote]', you…"]
What's not yet there: [1 sentence — what the rubric expects at one level higher]
Revision move: [One specific, actionable revision the student could try — verb + object — NOT a rewrite]
```

**Hard rules for the per-criterion comments:**

- Quote at least one direct phrase from the student's essay per criterion
- "What's not yet there" describes the gap in rubric terms, not the student's character
- The revision move is something the student does — not text the teacher writes for them
- Never include rewritten paragraphs, suggested sentences to copy in, or thesis statements you'd substitute

### Step 4: Identify the One Highest-Leverage Revision

Across all criteria, name the **single revision** that would most move the essay forward. State:

- The revision (verb + object)
- Why this one (which criteria it lifts)
- An example of where in the essay to start — quote student text and point at the next move

Example: "Start by sharpening your thesis (lifts Claim and Analysis). Look at your sentence in paragraph 1: '[quote].' Right now it tells me your topic. Try rewriting it so it tells me your position on that topic — what you're arguing about it."

### Step 5: Warm-Cool Summary

End with a 2-line summary:

- **Warm (1 line):** What this writer is genuinely doing well — quote-specific, not generic
- **Cool (1 line):** The one thing to focus on next — points to Step 4 revision

### Step 6: Optional — Conferring Question Set

If the essay is in draft (not final), produce 2–3 questions the teacher can ask in a 5-minute conference:

1. [Question that gets the student to articulate the move named in Step 4]
2. [Question that surfaces what the student was trying to do]
3. [Question that hands ownership back: "What would you change first?"]

### Step 7: Self-Check Before Output

- [ ] Did I quote student evidence for every criterion?
- [ ] Did I avoid writing any sentence the student could copy verbatim into the essay?
- [ ] Is the highest-leverage revision actually higher leverage than the others?
- [ ] Are warm and cool both quote-specific?
- [ ] Did I keep within the length cap?

---

## Output Format

1. One-sentence essay summary (what the student is arguing)
2. Per-criterion feedback table or block
3. Highest-leverage revision (named, justified, anchored in student text)
4. Warm + cool summary (2 lines)
5. Optional conferring question set
6. Self-check confirmation

---

## False-Positive Prevention

❌ **DON'T:**
- Rewrite student sentences or paragraphs
- Score without quoting evidence
- Pile on every weakness — students can act on one revision at a time
- Write generic praise ("nice job!") or generic critique ("needs more support")
- Confuse style preference with rubric criteria

✅ **DO:**
- Quote the student's words for every comment
- Name one highest-leverage revision and justify it
- Use rubric language for gaps, not personal attributes
- Keep revision moves verb-first and student-executable
- End with both warm and cool — never one without the other

---

## Quality Indicators

- [ ] Every criterion has a score AND a quoted evidence comment
- [ ] No teacher-rewritten text appears
- [ ] Highest-leverage revision is identified and justified
- [ ] Warm and cool are both specific
- [ ] Length stays within cap

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Rubric, genre, grade, and process stage shape comment depth and tone. |
| **ST-02** | Sequential read → score → comment → prioritize → summarize. |
| **OC-01** | Per-criterion comment template enforces consistent structure across stacks. |
| **QA-02** | Self-check stress-tests the feedback against rewriting and generic-praise failure modes. |
| **RT-04** | Warm/cool summary protects the student-teacher relationship while delivering hard feedback. |
