---
title: "Workflow: STEM Problem Solving"
category: education-teaching/learner/guides/college-students
description: "Per-problem chain for math, physics, chemistry, engineering: decode the problem, Socratic step-by-step (no final answer given by AI), error analysis on your work, concept map for the unit. Builds skill instead of getting the answer."
techniques:
  - CM-01
  - DT-01
  - NE-02
  - RP-02
  - ST-02
difficulty: intermediate
tags:
  - education
  - college
  - undergraduate
  - workflow-chain
updated: "2026-05-13"
related_prompts:
  - domain-education-teaching/learner/guides/college-students/learn_workflow_office_hours_and_class_discussion.md
  - domain-education-teaching/learner/guides/college-students/learn_workflow_cross_domain_kit.md
  - domain-education-teaching/learner/guides/college-students/learn_workflow_research_paper_full_arc.md
audience: college-students
chain_length: 4
estimated_time: "20-60 min per problem"
status: active
---

# Workflow: STEM Problem Solving

## Who This Is For

- Undergrad in math, physics, chemistry, engineering, or quantitative social science working through problem sets
- Stuck on a specific problem and tempted to look up the answer
- Wants to build durable skill, not just finish the assignment

If you genuinely just need the answer for a take-home graded problem set, this workflow will refuse to give it to you — by design. That's a feature, not a bug. If your problem is "I don't understand the unit," see step 4 (concept map). If your problem is "I have 6 hours of work in a 2-hour window," that's a scheduling problem, not a STEM problem — run [`../../../../domain-productivity/deep-work/deepwork_calendar_audit.md`](../../../../domain-productivity/deep-work/deepwork_calendar_audit.md).

## What You'll Have at the End

- A solution you arrived at yourself (or a clear understanding of where you're blocked)
- Identified the type of error or misconception if you got it wrong
- A concept map showing how this problem connects to the rest of the unit

## What You Need to Bring

- The problem statement
- Your work so far (even just notes about what you tried)
- The relevant textbook / lecture notes for the unit
- 20–60 minutes per problem (depending on difficulty and how stuck you are)

## The Chain

### Step 1 — Decode the problem

**Prompt:** [`../../math-science/learn_word_problem_decoder.md`](../../math-science/learn_word_problem_decoder.md)

**Input:** the problem statement

**What you'll get:** guided identification of what's being asked, what's given, what strategy might fit — through questions, not answers

**Carry forward:** clear understanding of the problem before you attempt a solution

**Skip if:** the problem is a straightforward "compute X" with no ambiguity. Decoding is mostly valuable for word problems and multi-step problems.

**Time:** 5–15 min

---

### Step 2 — Socratic step-by-step

**Prompt:** [`../../math-science/learn_math_socratic_solver.md`](../../math-science/learn_math_socratic_solver.md)

**Input:** decoded problem + your current attempt or block

**What you'll get:** stepping-stone questions that move you toward the solution — AI does not compute, does not give intermediate values, does not state the answer

**Carry forward:** your worked solution

**Time:** 15–30 min for moderate problems

**The friction is the point.** If the AI gave you the next step, you'd learn the answer; with the question approach, you learn the method. The method generalizes; the answer doesn't.

---

### Step 3 — Error analysis (if you got it wrong)

**Prompt:** [`../../math-science/learn_math_error_analyzer.md`](../../math-science/learn_math_error_analyzer.md)

**Input:** your wrong answer + the correct answer + your work

**What you'll get:** the prompt helps you locate, classify, and plan the fix — was it a procedural error, a misconception, a transcription mistake, a strategy choice, or a time-pressure slip

**Carry forward:** an entry in your mistake log

**Skip if:** you got it right.

**Time:** 10–15 min

**This is the highest-leverage step for long-term learning.** Categorizing errors prevents re-making them. A mistake that gets classified is a mistake that gets fixed; a mistake that doesn't is a mistake that repeats on the exam.

---

### Step 4 — Concept map (after several problems in a unit)

**Prompt:** [`../../math-science/learn_science_concept_map_builder.md`](../../math-science/learn_science_concept_map_builder.md)

**Input:** the key terms from the unit, your sense of how they connect

**What you'll get:** Socratic questions about the relationships between concepts — you draw the map

**Carry forward:** a concept map that shows how this unit's pieces fit together

**When to run this:** after 5–10 problems in a single unit, or before the exam on a unit you've been studying.

**Time:** 30–45 min per unit

## Per-Problem Time Budget

| Problem type | Steps | Time |
|--------------|-------|------|
| Routine practice problem | 2 only | 10–20 min |
| Multi-step word problem | 1, 2, 3 (if wrong) | 20–45 min |
| Hard / novel problem | 1, 2 with multiple Socratic passes, 3 | 30–60 min |
| End-of-unit concept check | 4 (concept map) | 30–45 min |

## When to Use Direct Mode Instead

The Socratic prompts above are designed for skill-building. There are three legitimate situations where direct-mode (just give me the answer / formula / definition) is the right tool:

1. **Looking up a formula or constant** you already understand. ("What's the speed of light in vacuum?" — direct mode.)
2. **Understanding a concept you'll never be tested on** (the prereq from a course you're not taking; background context). Direct explanation is fine.
3. **Diagnostic time-pressure check** during exam practice: if you can't make progress in 5 minutes on a problem, look at the solution, study it, then re-solve from scratch from memory.

In all other cases (graded problem sets, exam study, skill you'll actually need), stay Socratic. See [`../shared/learn_socratic_vs_direct_decision.md`](../shared/learn_socratic_vs_direct_decision.md).

## Common Failure Modes

| Failure | What to do |
|---------|-----------|
| **"Just tell me the answer."** | The prompt refuses. If you're truly out of time, step away and ask the professor or TA. Pasting an answer you don't understand is worse than leaving the problem blank. |
| **Got "AI" to give the answer by rephrasing.** | You won't be able to do the next problem either. Re-engage with step 1. |
| **Stuck mid-problem and the Socratic questions feel unhelpful.** | Means you're missing a prerequisite. Run step 4 (concept map) on the unit; the missing piece will likely surface. Or check the textbook section the problem is from — there's usually a worked example. |
| **Got it right but couldn't explain why.** | Run [`../../memory-and-recall/learn_feynman_teach_back_coach.md`](../../memory-and-recall/learn_feynman_teach_back_coach.md) on the problem. If you can't teach the solution, you don't yet own it. |
| **Spending 90+ minutes per problem.** | Either the problem is genuinely above your level (talk to TA), or you're missing prerequisites. Don't burn an evening on one problem; move on, learn the unit, return. |
| **Test scores low despite good problem-set scores.** | Almost certainly an error-classification gap. Run step 3 on every wrong test answer. Patterns will emerge. |

## Building the Mistake Log

Step 3 is most valuable if its output goes somewhere you'll see again. One workable system:

- One page per unit in a dedicated notebook
- Each entry: problem (or summary), my wrong answer, correct answer, error category, what I'll do differently
- Review the log at the start of each study session for that unit
- Run [`../../self-assessment/learn_mistake_log_reviewer.md`](../../self-assessment/learn_mistake_log_reviewer.md) before midterms and finals

## Lab Reports (Special Case)

For lab courses, problem-solving is paired with lab report writing. Use [`../../math-science/learn_lab_report_scaffold.md`](../../math-science/learn_lab_report_scaffold.md) for the report; this workflow handles the underlying problem-solving.

For experimental design and data interpretation:
- [`../../math-science/learn_experimental_design_helper.md`](../../math-science/learn_experimental_design_helper.md)
- [`../../math-science/learn_science_data_interpreter.md`](../../math-science/learn_science_data_interpreter.md)

---

*Part of [`GUIDE.md`](GUIDE.md). For exam prep that uses STEM mistake logs, see [`learn_workflow_exam_prep_finals_week.md`](learn_workflow_exam_prep_finals_week.md).*
