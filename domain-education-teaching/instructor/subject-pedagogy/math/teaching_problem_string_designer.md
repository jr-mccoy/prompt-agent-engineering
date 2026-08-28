---
title: "Math Problem String Designer"
category: education-teaching/instructor/subject-pedagogy/math
description: "Sequence a 4–6 problem string warm-up that uses the first problems as a helper for the later ones — surfacing a target strategy or relationship rather than drilling random computation."
techniques:
  - CM-01
  - ST-02
  - DS-01
  - OC-01
  - QA-02
difficulty: intermediate
tags:
  - math
  - problem-string
  - elementary
  - middle-school
  - mental-math
  - number-sense
  - warm-up
updated: "2026-05-10"
related_prompts:
  - domain-education-teaching/instructor/subject-pedagogy/math/teaching_number_talks_designer.md
  - domain-education-teaching/instructor/subject-pedagogy/math/teaching_three_act_task_builder.md
  - domain-education-teaching/instructor/subject-pedagogy/math/teaching_math_error_analysis_task.md
---

# Math Problem String Designer

## Objective

Produce a 4–6 problem string in which each problem is intentionally related to the previous one so that solving earlier problems gives students a leg up on later ones. Output includes the string, the mathematical relationship the string is designed to surface, anticipated student moves at each step, and the teacher's recording and discourse plan.

## When to Use

- 10–15 minute warm-up that elicits a specific computational strategy (e.g., partial products, doubling/halving, friendly numbers, compensation, ratio reasoning)
- Building from accessible "helper" problems toward a stretch problem
- Launching a unit by surfacing the relationship the lesson will formalize
- Replacing random fluency drills with structured mental-math reasoning

## When NOT to Use

- You want a single open-ended problem with multiple solution paths — use `teachsubj_math_three_act_task_builder.md`
- You want a single computation with multiple shared strategies — use `teachsubj_math_number_talks_designer.md`
- You need a paper-and-pencil practice set, not a discourse routine — use `teaching_study_practice_problems.md`

---

## Inputs Needed

- **Grade level:** [K–8 or Algebra I]
- **Target relationship / strategy:** [What the string is designed to surface — e.g., "doubling and halving keeps the product the same," "partial products," "constant difference in subtraction"]
- **Operation domain:** [Whole number, fraction, decimal, integer, ratio, linear]
- **String length:** [4 / 5 / 6 problems]
- **Time available:** [10, 12, or 15 minutes]
- **Class context:** [Whole class / small group; ELL or IEP notes]

---

## Instructions

### Step 1: Name the Mathematical Relationship

Before writing problems, write one sentence stating the relationship the string is designed to surface. Examples:

- "Doubling one factor and halving the other preserves the product."
- "Subtracting the same amount from both numbers preserves the difference."
- "Multiplying by a unit fraction is the same as dividing by its denominator."

If you can't write this sentence, the string isn't ready. Stop and clarify.

### Step 2: Build the String from Anchor → Stretch

Sequence problems in this order, with one specific function per slot:

| # | Function | What It Does |
|---|---------|--------------|
| 1 | **Anchor** | Accessible to every student; establishes the form |
| 2 | **Helper** | Small variation that activates the target relationship |
| 3 | **Bridge** | Slightly harder; relationship now does real work |
| 4 | **Stretch** | Numbers chosen so the relationship is the efficient path |
| 5 | **(Optional) Generalization** | Variable or open-ended form: "What if…?" |
| 6 | **(Optional) Application** | Word-problem context using the relationship |

For each problem, write a one-line note: *"This problem invites students to use the previous one because…"*

### Step 3: Anticipate Student Moves Per Problem

For each problem in the string, list:

| # | Problem | Likely brute-force approach | Approach the string is inviting | Wrong answer to anticipate |
|---|---------|------------------------------|--------------------------------|---------------------------|

The "approach the string is inviting" should escalate across the string — the stretch problem should make brute force visibly inefficient.

### Step 4: Recording Plan

Sketch (in text) how the board should look after the string is complete. Show:

- Each problem stacked vertically
- The visual that makes the relationship visible (open number line, ratio table, area model, equation chain)
- Where student initials or arrows mark connections between problems

### Step 5: Teacher Moves Per Problem

For each problem, provide the teacher script in this template:

```
Problem [N]: [problem]
- Pose: [exact teacher language]
- Wait time: [seconds]
- Collect answers: [protocol]
- Strategy share order: [least sophisticated → target relationship]
- Bridge to next problem: [one teacher question that connects this to the next]
```

### Step 6: Closure

Provide:
- One question that surfaces the relationship out loud: "What did you notice across these problems?"
- A sentence frame for naming it: "When the [first number] gets [bigger/smaller] by [amount], the [other number] ___."
- One follow-up the teacher can use tomorrow if students don't generalize today.

### Step 7: Differentiation

- **Entry point for struggling students:** Smaller numbers / tools allowed (number line, hundreds chart)
- **Stretch:** "Make up problem 7 that fits this pattern"
- **ELL support:** Sentence frame for sharing strategies + visual recording

### Step 8: Self-Check

- [ ] Can a student solve problem 1 without prior teaching?
- [ ] Does each problem provide leverage for the next, not just additional difficulty?
- [ ] Does the stretch problem make the target relationship the efficient path?
- [ ] Is the relationship named in plain English in closure?

---

## Output Format

1. Header: grade, target relationship, operation, length, time
2. The relationship sentence (Step 1)
3. The string with per-problem notes
4. Anticipated student moves table
5. Recording sketch
6. Teacher script per problem
7. Closure question + sentence frame
8. Differentiation notes
9. Self-check confirmation

---

## False-Positive Prevention

❌ **DON'T:**
- Write "random fluency" — every problem must connect to the previous
- Make the stretch problem so hard it requires new content, not the relationship
- Skip the anchor — students who can't solve problem 1 are out of the routine
- Tell students the relationship up front — the string surfaces it, doesn't preview it
- Use numbers where the relationship is invisible (e.g., 7 × 13 doesn't invite doubling/halving)

✅ **DO:**
- Choose numbers where the target relationship is the efficient path
- Anticipate brute force at every step and let it surface
- Order strategies by sophistication during the share, not by who answered first
- Name the relationship at the end in students' words
- Keep the whole string under 15 minutes

---

## Quality Indicators

- [ ] Mathematical relationship is stated in one sentence before problems are written
- [ ] Each problem provides genuine leverage for the next
- [ ] Stretch problem makes the target relationship visibly efficient
- [ ] Anticipated student moves include at least one likely error per problem
- [ ] Recording plan is reproducible on a whiteboard
- [ ] Closure names the relationship without lecturing it

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Grade, target relationship, and operation anchor every numeric choice. |
| **ST-02** | Eight steps move from naming the relationship → string design → discourse plan. |
| **DS-01** | Anchor → helper → bridge → stretch is the framework that makes the string a string, not a worksheet. |
| **OC-01** | Per-problem table and teacher-script template enforce reproducible structure. |
| **QA-02** | Self-check stress-tests whether the string actually surfaces the target relationship. |
