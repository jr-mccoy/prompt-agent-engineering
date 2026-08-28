---
title: "Math Work Feedback (Process + Answer)"
category: education-teaching/instructor/grading-feedback
description: "Generate feedback on student math work that addresses the process — strategy choice, representation, reasoning, computation — not just the final answer, while pointing the student to the next move without solving the problem for them."
techniques:
  - CM-01  # Context Framing
  - ST-02  # Sequential Steps
  - DS-01  # Framework Application (math discourse + error taxonomy)
  - OC-01  # Output Templates
  - RT-04  # Relational Tone
difficulty: intermediate
tags:
  - grading
  - feedback
  - math
  - process
  - revision
  - middle-school
  - high-school
  - misconceptions
updated: "2026-05-10"
related_prompts:
  - domain-education-teaching/instructor/grading-feedback/teaching_essay_feedback_by_rubric.md
  - domain-education-teaching/learner/math-science/learn_math_error_analyzer.md
  - domain-education-teaching/instructor/response-cycle/teaching_misconception_diagnoser.md
---

# Math Work Feedback (Process + Answer)

## Objective

Produce feedback on a single student's math work that addresses the process — strategy, representation, reasoning, computation — not just whether the answer is right or wrong. Output specifies what's working in the student's reasoning, where the breakdown occurs, and a single next-move prompt that pushes the student forward without solving the problem.

## When to Use

- Returning math work where you want feedback to drive revision
- Conferring prep before a one-on-one with a student
- Calibrating feedback across a class so it follows process, not just answer
- Documenting feedback for portfolio or growth tracking

## When NOT to Use

- Whole-class feedback on patterns across a stack — use `grading_essay_feedback_by_rubric_criterion.md` adapted, or build a whole-class memo
- Coaching a student through their own errors interactively — use `learnmath_error_analyzer_own_work.md`
- Identifying what misconceptions exist in the first place — use `teaching_misconception_diagnoser.md`

---

## Inputs Needed

- **Student's work (full):** [As written, including all marks, scratch, and crossed-out attempts]
- **Problem(s):** [The original problems]
- **Grade / course:** [...]
- **Topic / standard:** [...]
- **Rubric or scoring scheme (if any):** [...]
- **Stage:** [In-class formative / homework return / quiz return / pre-assessment]
- **Feedback length cap:** [Brief / standard / extended]
- **Tone preference:** [Direct / warm / mix — default: direct + warm]

---

## Instructions

### Step 1: Read for Process Before Answer

Look at the student's work as a record of their thinking, not as a producer of an answer. Make notes on:

- What strategy did the student choose? Was it appropriate?
- What representation did they use (equation, diagram, table, words)?
- Where did the work go off-track, if anywhere?
- Did the student check their work? How?
- What does the work reveal about understanding vs. procedure?

### Step 2: Score the Process Components

Score each of these (rubric-style, even informally):

| Component | What it looks at | Score |
|-----------|------------------|-------|
| Strategy | Did they pick a viable approach? |
| Representation | Did they use a useful diagram/equation/table? |
| Reasoning | Is the logic of the steps clear and valid? |
| Computation | Is the arithmetic / algebra correct? |
| Communication | Can someone else follow this? |

A student can have a wrong answer with strong process; a student can have a right answer with weak process. The feedback addresses process explicitly.

### Step 3: Identify the Highest-Leverage Move

Across the components, pick **one** move that would most help this student. Examples:

- "The strategy is sound — the issue is a sign error in line 3"
- "The computation is fine — but the strategy doesn't actually answer the question being asked"
- "There's no representation; drawing a diagram would clarify what's being compared"
- "The work has all the steps but skips the reasoning that ties them together"

### Step 4: Write the Feedback

Use this template:

```
WHAT'S WORKING (1–2 sentences, quote student work):
"When you wrote ___ in step 2, you correctly used ___."

WHERE IT BREAKS (1–2 sentences, locate it):
"In step 4, you wrote ___. Here's where the reasoning shifts: [name what happened]."

YOUR NEXT MOVE (one specific action the student takes):
"Try [specific verb-object move]. Don't redo the whole problem — just fix from step 4 forward."

(Optional question to push thinking):
"Before you redo it: [one diagnostic question]."
```

Hard rules:
- Quote the student's work (line, step, or expression)
- Don't write the corrected work for them
- Don't say "look it up" or "review the chapter" — too vague
- Don't pile on errors — name the one
- Don't praise generically ("nice work!"); name what specifically worked

### Step 5: Differentiate by Process Pattern

Match the next-move language to the process pattern:

| Pattern | Next-move framing |
|---------|-------------------|
| Conceptual gap (wrong strategy) | "Before you compute again, ask: what's the question actually asking? Then choose a strategy that fits." |
| Procedural slip (right strategy, computational error) | "Strategy is good — find the spot where the arithmetic shifts and fix it." |
| Sign / notation error | "Look at line ___ for a sign / notation issue." |
| Skipping a step | "Show me line ___ — what's the move between [previous] and [next]?" |
| No representation | "Try drawing [specific representation type]. What do you see?" |
| Communication problem (right answer, unclear) | "Walk me through how someone else could follow your work — what's missing?" |

### Step 6: Conferring Bridge (Optional)

If you'll see this student in a conference, plan one diagnostic question that surfaces their thinking:

- "Tell me what you tried first — and what made you change?"
- "If your friend looked at this, what would they ask you about?"
- "What did you check, and what didn't you check?"

### Step 7: Self-Check Before Output

- [ ] Did I quote the student's actual work?
- [ ] Did I avoid solving the problem for them?
- [ ] Did I name one highest-leverage move, not several?
- [ ] Is "what's working" specific, not generic?
- [ ] Will the student know what to do next without me re-explaining?

---

## Output Format

1. Process scoring (informal)
2. Identified highest-leverage move
3. Feedback in the four-part template
4. (Optional) Conferring bridge question
5. Self-check confirmation

---

## False-Positive Prevention

❌ **DON'T:**
- Mark only "right" or "wrong" without process feedback
- Solve the problem for the student in feedback
- Give vague "review your notes" advice
- Praise generically without naming what worked
- Pile on every error; pick one

✅ **DO:**
- Read for process before judging the answer
- Quote specific lines / steps from student work
- Name one highest-leverage move
- Make the next move student-executable
- Match feedback to error pattern, not generic comment

---

## Quality Indicators

- [ ] Feedback addresses process, not just answer
- [ ] Specific student work is quoted
- [ ] One highest-leverage move named
- [ ] Next move is verb-first and executable
- [ ] No teacher-rewritten math appears
- [ ] Pattern-matched framing fits the actual error type

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Topic, rubric, and stage anchor feedback depth and tone. |
| **ST-02** | Seven-step sequence: read → score → choose → write → differentiate → bridge → check. |
| **DS-01** | Process taxonomy (strategy / representation / reasoning / computation / communication) frames the feedback. |
| **OC-01** | Four-part feedback template enforces consistent structure across stacks. |
| **RT-04** | Tone preserves student-teacher relationship while delivering specific critique. |
