---
title: "Math Error Analysis Task Designer"
category: education-teaching/instructor/subject-pedagogy/math
description: "Design a task in which students analyze a fictional student's wrong solution — locating the error, classifying the misconception, and writing the correction with reasoning — to convert misconception data into instructional leverage."
techniques:
  - CM-01
  - ST-02
  - DS-01
  - OC-01
  - QA-02
difficulty: intermediate
tags:
  - math
  - error-analysis
  - misconceptions
  - metacognition
  - middle-school
  - high-school
  - formative
updated: "2026-05-10"
related_prompts:
  - domain-education-teaching/instructor/response-cycle/teaching_misconception_diagnoser.md
  - domain-education-teaching/learner/math-science/learn_math_error_analyzer.md
  - domain-education-teaching/instructor/subject-pedagogy/math/teaching_problem_string_designer.md
---

# Math Error Analysis Task Designer

## Objective

Produce a complete student-facing error-analysis task in which students examine a fictional student's worked solution, identify the error, classify the misconception, and produce a correct solution with reasoning. Output includes the wrong solution, scaffolded prompts, an answer key with the error category named, and discourse moves.

## When to Use

- After a unit assessment surfaces a common misconception you want to attack head-on
- Building metacognition — students who can spot errors stop making them
- Differentiating: stronger students analyze, struggling students get a worked example
- Replacing a "redo your missed problems" assignment with a task that actually changes thinking

## When NOT to Use

- Coaching a single student through their own mistakes — use `learnmath_error_analyzer_own_work.md`
- Diagnosing what misconceptions exist in the first place — use `teaching_misconception_diagnoser.md`
- A practice set where students just compute — use `teaching_study_practice_problems.md`

---

## Inputs Needed

- **Grade level:** [Grade or course]
- **Topic / standard:** [What the problem is about]
- **Target misconception(s):** [Specific error you want students to spot — e.g., "distributing the exponent over a sum: (a+b)² = a² + b²"]
- **Source of the misconception (optional):** [Real student work, common pitfall list, or generated]
- **Cognitive demand target:** [Recognize / explain / correct / generalize]
- **Time available:** [10, 20, or 30 minutes]

---

## Instructions

### Step 1: Name the Misconception Precisely

Write the misconception as a one-sentence rule the fictional student is following. Examples:

- "When a number is in front of a fraction, multiply only the numerator."
- "Negative signs distribute through one term, not all terms in the parentheses."
- "Cross-multiplication works the same way for all equations involving fractions."

If you can't state the underlying rule, the task isn't targeted yet — stop and refine.

### Step 2: Construct the Wrong Solution

Write a fictional student's full worked solution that:

- Is **plausible** — looks like real student work, not random scribbling
- Contains **exactly one** target error (or a chain of errors traceable to one underlying misconception)
- Includes **at least one correct step** so students must locate, not just spot
- Uses numbers that don't accidentally make the wrong answer right (avoid 0, 1, identical values)

Format the wrong solution as it would appear on paper — with all student work shown.

### Step 3: Write the Student-Facing Prompt

Use this template:

```
Avery solved this problem and got [wrong answer]. Their work is below.

[Full worked solution as Avery wrote it]

Your job is NOT to redo the problem. Your job is to:
1. Find the line where Avery's reasoning first goes wrong.
2. Explain in your own words what Avery was thinking — what rule were they following?
3. Show what Avery should have done at that line, and why.
4. Solve the problem correctly from that point forward.
5. Write one sentence Avery could remember to avoid this mistake next time.
```

Use a fictional name — never "the student" (depersonalizes) or a real classmate (humiliating). Rotate names across tasks.

### Step 4: Scaffolding Tiers

Provide three tiered versions for differentiation:

| Tier | Scaffold |
|------|---------|
| **Heavy** | Circle drawn around the wrong line; "Look at line 3 — what happened to the negative sign?" |
| **Medium** | "The error is somewhere in the first three lines. Find it." |
| **Light** | No scaffold; student locates from scratch |

### Step 5: Answer Key

Produce the teacher answer key with:

- **Error location:** [Line number]
- **Misconception category:** [Conceptual / procedural / careless / notational — and which sub-type]
- **What Avery was thinking:** [Plausible internal logic, stated charitably]
- **Correct move:** [What should happen at that line]
- **Correct final answer:** [Worked through]
- **Memorable rule for students:** [One sentence]

### Step 6: Discourse Plan

Provide 3–5 questions for whole-class discussion after students complete the task:

1. "How did you decide which line was the error?"
2. "What rule was Avery following? Why does it work in some cases but not here?"
3. "Where else could this same mistake show up?"
4. "What would you tell a sibling to help them avoid this?"

### Step 7: Variant Bank

Produce 2 variants of the same task with different numbers but the same misconception, for spaced practice across the week.

### Step 8: Self-Check

- [ ] Is exactly one underlying misconception present?
- [ ] Is the wrong solution plausible (not contrived)?
- [ ] Do the numbers prevent accidental correctness?
- [ ] Does the student-facing prompt require explanation, not just computation?
- [ ] Does the memorable rule address the underlying misconception, not the surface error?

---

## Output Format

1. Misconception statement (one sentence)
2. Wrong solution (formatted as student work)
3. Student-facing prompt with 5 numbered tasks
4. Tiered scaffolding versions
5. Teacher answer key
6. Discourse question set
7. Variant bank (2 additional problems)
8. Self-check confirmation

---

## False-Positive Prevention

❌ **DON'T:**
- Stack multiple unrelated errors in one solution — students lose the signal
- Use a wrong solution so obviously wrong students spot it instantly
- Frame the fictional student as "stupid" or "lazy" — model charitable error analysis
- Let numbers accidentally produce the right answer despite wrong reasoning
- Skip the "what was Avery thinking?" step — that's the metacognitive payoff

✅ **DO:**
- Make the wrong solution look like real student work, with at least one correct step
- Demand explanation, not just correction
- Name the misconception in teacher-facing language and student-facing language
- Provide tiered scaffolding for differentiation
- Connect to a memorable rule students can carry forward

---

## Quality Indicators

- [ ] One precise misconception is targeted
- [ ] Wrong solution is plausible and contains at least one correct step
- [ ] Student-facing prompt requires locate + explain + correct + generalize
- [ ] Tiered scaffolds support differentiation
- [ ] Answer key categorizes the error type
- [ ] Discourse questions push beyond "what's wrong" to "why does this happen"

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Grade, topic, and target misconception anchor every choice in the task. |
| **ST-02** | Eight-step build: name → construct → prompt → scaffold → key → discourse → variants. |
| **DS-01** | Error taxonomy (conceptual / procedural / careless / notational) frames classification. |
| **OC-01** | Five-step student prompt template enforces locate → explain → correct → generalize. |
| **QA-02** | Self-check stress-tests for plausibility, accidental correctness, and singularity of the error. |
