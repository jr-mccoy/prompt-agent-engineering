---
title: "Math Manipulatives Lesson — Concrete-Pictorial-Abstract"
category: education-teaching/instructor/subject-pedagogy/math
description: "Design a math lesson that moves students through the concrete → pictorial → abstract (CPA) sequence so the symbolic representation grows out of physical action — not the other way around."
techniques:
  - CM-01
  - ST-02
  - DS-01
  - OC-01
  - QA-02
difficulty: intermediate
tags:
  - math
  - manipulatives
  - cpa
  - concrete-pictorial-abstract
  - elementary
  - middle-school
  - representations
updated: "2026-05-10"
related_prompts:
  - domain-education-teaching/instructor/lesson-planning/teaching_lesson_plan_generator.md
  - domain-education-teaching/instructor/subject-pedagogy/math/teaching_problem_string_designer.md
  - domain-education-teaching/instructor/response-cycle/teaching_misconception_diagnoser.md
---

# Math Manipulatives Lesson — Concrete-Pictorial-Abstract

## Objective

Produce a single math lesson plan that uses a specific manipulative to move students through the concrete → pictorial → abstract (CPA) sequence for a target concept. Output specifies the manipulative actions, the bridging diagram, the symbolic notation, and the explicit teacher moves that connect the three representations.

## When to Use

- Introducing a new operation or concept where the symbolic shortcut hides the meaning (regrouping, fraction operations, integer arithmetic, equation solving)
- Re-teaching after assessment shows procedural fluency without conceptual understanding
- Differentiating: students stuck at the abstract level get pulled back to concrete; students ready to move on get pushed forward
- Building a lesson sequence for a unit where representations matter

## When NOT to Use

- Pure fluency practice on a procedure already understood — use `teaching_study_practice_problems.md`
- Open-ended problem solving — use `teachsubj_math_three_act_task_builder.md`
- Number-talk warm-up — use `teachsubj_math_number_talks_designer.md`

---

## Inputs Needed

- **Grade level:** [K–8]
- **Concept / standard:** [What the lesson teaches — e.g., "subtraction with regrouping," "multiplying fractions," "adding integers"]
- **Manipulative available:** [Base-ten blocks / fraction tiles / two-color counters / algebra tiles / Cuisenaire rods / number line / other]
- **Lesson length:** [30, 45, or 60 minutes]
- **Class context:** [Whole class / small group; ELL or IEP notes]
- **Prior knowledge:** [What students already know about this concept]

---

## Instructions

### Step 1: Name the Translation Across Representations

For the target concept, write what each of the three representations looks like — concretely, in one sentence each.

| Representation | What students do | Example |
|----------------|------------------|---------|
| **Concrete** | Physical action with the manipulative | Trade 1 ten for 10 ones |
| **Pictorial** | Drawn picture that mirrors the action | Draw the ten as a stick, slash it, draw 10 dots |
| **Abstract** | Symbolic notation | Cross out the 4 in the tens place, write 3 above; add 10 to ones |

If the three rows don't tell the same story, the lesson isn't ready. The pictorial and abstract must mirror the concrete action, not just decorate it.

### Step 2: Choose the Manipulative Justification

Write one sentence: *"This manipulative was chosen because [the structure of the manipulative carries the structure of the concept]."*

Bad choice: counters for multi-digit subtraction (no place value)
Good choice: base-ten blocks for multi-digit subtraction (place value baked in)

If the chosen manipulative doesn't carry the structure of the concept, propose an alternative.

### Step 3: Concrete Phase Plan

Plan 10–20 minutes:

```
Launch: How students get the manipulative; storage protocol.
Modeling: Teacher demonstrates the action — exact physical move + exact words.
Student action: Specific problems students solve concretely. Number them.
Recording: How students record what they did (written log, photo, partner check).
Common errors: 2–3 wrong moves with the manipulative and the correction.
Bridge to next phase: One question that surfaces what just happened.
```

The teacher must not say the symbolic shortcut during the concrete phase. Students should be able to do it without symbols.

### Step 4: Pictorial Phase Plan

Plan 10–15 minutes:

```
Bridge: "Show me on paper what you did with the blocks. Use a quick drawing."
Modeling: Teacher draws the same problem they modeled concretely; the drawing must mirror the physical move (a slash for trading, an X for grouping, etc.).
Student action: Solve the same type of problem pictorially, no manipulatives.
Common errors: Drawings that don't preserve the structure (e.g., counting circles instead of representing tens).
Bridge: "Where in the picture do you see the tens? Where do you see the ones?"
```

Pictures must be reproducible by students — not teacher art. Provide an example sketch.

### Step 5: Abstract Phase Plan

Plan 10–20 minutes:

```
Bridge: "Now I want to show you the way mathematicians write this — and you'll see it's the same thing you've been doing."
Modeling: Teacher writes the symbolic notation underneath or beside the picture, pointing to the parallel.
Student action: Solve the same type of problem symbolically.
Common errors: Procedural moves disconnected from meaning ("I borrowed because I had to").
Bridge back: "If a 4th grader asked why you crossed out the 4, what would you show them?"
```

The abstract phase explicitly references the concrete and pictorial work. Notation is named as shorthand for the action.

### Step 6: Three-Column Anchor Chart

Output the anchor chart that will live in the room:

```
| Concrete (with blocks) | Pictorial (drawing) | Abstract (numbers) |
|------------------------|---------------------|--------------------|
| [photo or description] | [sketch] | [equation] |
```

One row per worked example. Students return to this chart when stuck.

### Step 7: Differentiation

- **Stuck students:** Pulled back to concrete; cannot leave concrete until they can predict the picture before drawing it
- **Ready-to-move students:** Move to abstract earlier; given prompt to "explain to a partner using only words why this works"
- **ELL support:** Sentence frames: "First I ___. Then I ___. So my answer is ___."
- **IEP / fine-motor:** Pre-cut manipulatives, larger tools, partner record-keeper

### Step 8: Formative Check

Provide three exit-ticket items, one at each level:

1. Concrete: Picture of manipulatives shown — student writes what equation they represent
2. Pictorial: Equation given — student draws the picture
3. Abstract: Symbolic problem — student solves and explains

Students who get only #3 right but not #1 or #2 have procedure without concept — flag for re-teach.

### Step 9: Self-Check

- [ ] Does the pictorial mirror the concrete action, not just decorate it?
- [ ] Does the abstract notation tie to the picture move-for-move?
- [ ] Is the manipulative actually carrying the structure of the concept?
- [ ] Is there an explicit bridge between each pair of phases?
- [ ] Does the exit ticket distinguish concept from procedure?

---

## Output Format

1. Concept and standard
2. Three-row translation table (Step 1)
3. Manipulative justification (Step 2)
4. Concrete phase plan
5. Pictorial phase plan
6. Abstract phase plan
7. Three-column anchor chart
8. Differentiation notes
9. Three-level exit ticket
10. Self-check confirmation

---

## False-Positive Prevention

❌ **DON'T:**
- Use manipulatives as a "fun activity" before getting to the "real math" — that's not CPA
- Let pictures be decorative drawings unrelated to the concrete action
- Move to abstract before students can do concrete without symbols
- Choose manipulatives that don't carry the concept's structure
- Skip the bridges — translation between representations is the lesson

✅ **DO:**
- Name the move-by-move parallel across all three representations
- Spend at least 10 minutes in concrete before introducing the picture
- Make the picture reproducible — students must be able to draw it
- Tie symbolic notation explicitly to physical action
- Pull stuck students back to concrete, not forward to more abstract examples

---

## Quality Indicators

- [ ] Concrete, pictorial, and abstract tell the same mathematical story
- [ ] Manipulative is justified by structural fit
- [ ] Each phase has a bridge to the next
- [ ] Anchor chart shows all three representations side by side
- [ ] Exit ticket separates conceptual from procedural mastery
- [ ] Differentiation includes pulling back, not just pushing forward

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Grade, concept, manipulative, and prior knowledge shape every phase. |
| **ST-02** | Nine sequential phases mirror the CPA sequence with explicit bridges. |
| **DS-01** | Bruner's CPA framework structures the lesson; representations are the unit, not procedures. |
| **OC-01** | Three-row translation table and three-column anchor chart enforce structural parallelism. |
| **QA-02** | Self-check stress-tests whether the three representations actually mirror each other. |
