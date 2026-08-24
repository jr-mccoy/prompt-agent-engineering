---
title: "Math Number Talk Designer"
category: education-teaching/subject-pedagogy
description: "Design a 5–15 minute number talk that builds mental computation, reasoning, and discourse around a single computation or visual prompt — with anticipated student strategies and teacher moves."
techniques:
  - CM-01  # Context Framing
  - ST-02  # Sequential Steps
  - OC-01  # Output Templates
  - DS-01  # Framework Application (Bloom's, DOK)
  - QA-02  # Adversarial Verification
difficulty: intermediate
tags:
  - math
  - elementary
  - middle-school
  - number-sense
  - mental-math
  - discourse
  - formative
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/teaching_lesson_plan_generator.md
  - domain-education-teaching/teaching_misconception_diagnoser.md
  - domain-education-teaching/subject-pedagogy/teachsubj_math_three_act_task_builder.md
---

# Math Number Talk Designer

## Objective

Produce a complete number talk routine (5–15 minutes) for a specific grade and topic. Output includes the prompt itself, anticipated student strategies (named and ordered), teacher recording notation, sequenced teacher questions and moves, and a closure that names the mathematical idea surfaced.

## When to Use

- Daily warm-up for grades 1–8 mathematics
- Building mental computation, place-value reasoning, or operation flexibility
- Launching a unit when you want to elicit existing strategies before formal instruction
- Targeting a specific strategy you want to surface (e.g., compensation, decomposition, partial products)

## When NOT to Use

- You need a full lesson — use `teaching_lesson_plan_generator.md`
- You need an open-middle problem-solving task — use `teachsubj_math_three_act_task_builder.md`
- You need a paper-and-pencil practice set — use `teaching_study_practice_problems.md`

---

## Inputs Needed

- **Grade level:** [K–8]
- **Topic / strand:** [e.g., addition within 100, multiplication of fractions, integer operations, percent of a number]
- **Strategy goal (optional):** [Specific strategy to elicit — e.g., "make a ten," "doubling and halving," "partial quotients"]
- **Time available:** [5, 10, or 15 minutes]
- **Format:** [Single problem string / dot image / number string of 3–5 related problems / true-or-false equation]
- **Class context:** [Whole class / small group; any ELL or IEP notes]

---

## Instructions

### Step 1: Choose the Prompt Type

Select one and justify the choice in one sentence:

| Type | Best For | Example |
|------|----------|---------|
| Single computation | Surfacing one strategy with depth | 48 × 25 |
| Number string (3–5 related problems) | Building from accessible to stretch | 5×4, 5×40, 5×39, 5×38 |
| Dot image / quick image | K–2; subitizing; structure of number | Array of dots flashed 3 seconds |
| True-or-false equation | Equality reasoning, properties | 23 + 17 = 25 + 15 |
| Which doesn't belong | Multiple right answers; classification | Four numbers/shapes |

### Step 2: Write the Prompt

Produce the exact problem(s), in the exact form students will see them. If a string, list problems in order with a one-line note on what each problem invites.

### Step 3: Anticipate Student Strategies

List 3–6 strategies a student might use, ordered from most concrete/inefficient to most sophisticated. For each:

| # | Strategy Name | What the Student Does | Sample Student Talk | Recording Notation (board) |
|---|--------------|----------------------|---------------------|---------------------------|
| 1 | [Name] | [Steps] | "I…" | [How teacher records on board] |

Include at least one **partial / common-error** strategy with the misconception named.

### Step 4: Teacher Moves Sequence

Provide the minute-by-minute sequence:

1. **Launch (30–60 sec):** How the teacher displays the prompt and what they say. Include the silent-thinking signal and the "show me a thumb when you have an answer" routine.
2. **Solo think time (1–2 min):** Time, expectations, and what the teacher is doing.
3. **Collect answers (1 min):** Record all answers without judgment, including wrong ones. Provide the exact teacher script.
4. **Share strategies (4–8 min):** Order in which to call on strategies (least to most sophisticated). For each, give the exact prompts:
   - "Whose strategy is this? Tell us how you got it."
   - "Did anyone do it a different way?"
   - "Can someone restate [student name]'s strategy in their own words?"
5. **Connect (1–2 min):** Question that connects two strategies and names the math idea.
6. **Closure (30–60 sec):** Sentence frame the teacher uses to name what was learned: "Today we noticed that…"

### Step 5: Teacher Recording Plan

Sketch (in text/ASCII) how the board should look at the end. Show:
- Problem at top
- Each strategy labeled with student initials or numbered
- Visual representations (arrays, number lines, equations)

### Step 6: Differentiation

- **Entry point for struggling students:** [Smaller numbers / concrete model / partner think]
- **Stretch for advanced students:** [Generalize to a rule / try with different numbers]
- **ELL support:** [Sentence frames: "I started by ___. Then I ___. So my answer is ___."]

### Step 7: Formative Evidence

- What you'll listen for that signals the strategy goal was met
- What to do if no student uses the target strategy (teacher move: "I'm going to share one I saw in another class — what do you think of this?")

---

## Output Format

1. Header: grade, topic, strategy goal, time
2. The prompt(s) exactly as students see them
3. Anticipated strategies table
4. Teacher moves sequence with timing and scripts
5. Board recording sketch
6. Differentiation notes
7. Formative evidence checklist

---

## False-Positive Prevention

❌ **DON'T:**
- Pick numbers that only invite one strategy (e.g., "doubles only")
- Order strategies by who said them rather than by sophistication
- Skip the wrong-answer collection — wrong answers are the discussion
- Tell students "the right way" — number talks build flexibility, not procedure
- Run past 15 minutes — the routine loses force when overgrown

✅ **DO:**
- Choose numbers that invite multiple strategies
- Anticipate at least one wrong answer with the underlying reasoning
- Provide exact teacher language, not paraphrase
- Name the mathematical idea at closure — don't leave it implicit
- Write recording notation a teacher could actually reproduce on a whiteboard

---

## Quality Indicators

- [ ] Prompt is open enough to invite ≥3 valid strategies
- [ ] At least one anticipated strategy is partial/incorrect with the misconception named
- [ ] Teacher moves include exact language, not paraphrase
- [ ] Board recording sketch is concrete enough to reproduce
- [ ] Closure names a transferable mathematical idea
- [ ] Total time fits the requested window with a 1-minute buffer

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Grade, topic, strategy goal, and time anchor every output choice. |
| **ST-02** | Six numbered phases mirror the rhythm of an actual number talk. |
| **OC-01** | Strategy table and board sketch enforce a consistent, reproducible structure. |
| **DS-01** | Strategies are ordered by sophistication, not arrival, applying a developmental framework. |
| **QA-02** | Anticipated misconceptions stress-test the prompt before it reaches the classroom. |
