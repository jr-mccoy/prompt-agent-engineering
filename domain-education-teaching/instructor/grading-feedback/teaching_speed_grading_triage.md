---
title: "Speed-Grading Triage"
category: education-teaching/instructor/grading-feedback
description: "Sort a stack of student work into grade-deeply / grade-lightly / grade-quickly piles based on a triage protocol — protecting feedback quality where it matters and reclaiming hours where it doesn't."
techniques:
  - CM-01
  - ST-02
  - OC-01
  - DS-01
  - QA-01
difficulty: intermediate
tags:
  - grading
  - workload
  - triage
  - efficiency
  - feedback
  - sustainable-teaching
updated: "2026-05-09"
related_prompts:
  - domain-education-teaching/instructor/grading-feedback/teaching_essay_feedback_by_rubric.md
  - domain-education-teaching/instructor/grading-feedback/teaching_whole_class_feedback_memo.md
  - domain-education-teaching/instructor/assessment-design/teaching_assessment_rubric_builder.md
---

# Speed-Grading Triage

## Objective

Apply a triage protocol to a stack of student work that decides — paper by paper — whether each gets full feedback, light feedback, or a score-only pass. Output: a sorted plan, time estimate, and per-tier feedback templates so the teacher can finish the stack in a defensible time budget without sacrificing the comments that matter.

## When to Use

- A stack of papers and a finite evening
- After common assessments where some students need feedback and others need a score
- When weekly volume forces a choice
- Returning quizzes vs. unit essays vs. exit tickets — different stakes, different feedback depth
- Recovering from a grading backlog

## When NOT to Use

- High-stakes external assessment requiring uniform feedback (use the assessment's protocol)
- IEP / 504 work that requires individualized response (do not triage)
- Sample so small that triage adds overhead without saving time

---

## Inputs Needed

- **The stack:** [Assignment name, count, type]
- **Rubric:** [...]
- **Time available:** [Total grading minutes you'll spend]
- **Stakes:** [Formative draft / unit summative / quiz / final / exit]
- **What students do with the work next:** [Revise / file / move on / parent conference]
- **Special-population flags:** [IEP/504 students who require full feedback regardless]

---

## Instructions

### Step 1: Decide What Feedback Is For This Assignment

Before triaging, declare the purpose of feedback on this stack:

| Purpose | Feedback depth this implies |
|---------|----------------------------|
| Drive revision (draft) | High — students will use it tomorrow |
| Inform reteach (formative) | Medium — patterns matter more than individual comments |
| Document learning (summative) | Score-focused; comment only where revision is possible |
| Communicate to family / IEP team | Individualized notes for affected students |

This decision sets the ceiling on feedback depth.

### Step 2: First-Pass Sort (≤30 sec per paper)

Skim each paper and sort into three tiers:

| Tier | Definition | Feedback depth |
|------|-----------|---------------|
| **A — Grade Deeply** | Borderline scores, students who will revise, IEP/504 students, work showing significant struggle or significant breakthrough | Full criterion-by-criterion feedback (use `grading_essay_feedback_by_rubric_criterion.md`) |
| **B — Grade Lightly** | Solid mid-range work; clear score; one or two targeted comments would help | Score + 1–2 high-leverage comments |
| **C — Grade Quickly** | Clear high-end or clear low-end where score communicates everything; whole-class memo will cover the rest | Score only or score + a single anchor comment |

Aim for roughly 20% A / 60% B / 20% C unless the stack is unusually distributed.

### Step 3: Time Budget

Apply per-tier defaults:

| Tier | Minutes per paper |
|------|-------------------|
| A | 5–10 |
| B | 2–3 |
| C | 30–60 sec |

Total = ΣΣ. Compare to time available. If over budget:
- Reduce tier A by upgrading borderlines that the whole-class memo can address
- Reduce tier B by collapsing comments to a single high-leverage one
- Add a whole-class memo to cover everything tier C and most tier B (use `grading_whole_class_feedback_memo.md`)

### Step 4: Per-Tier Templates

Provide ready-to-use templates:

**Tier A — full feedback** → invoke `grading_essay_feedback_by_rubric_criterion.md` with the rubric.

**Tier B — light feedback template:**
```
Score: [N]
Working: [1 quoted phrase]
Try next: [1 specific revision move]
```

**Tier C — score-only with anchor comment:**
```
Score: [N]
[Single sentence pointing to the whole-class memo's relevant section, or naming the rubric criterion that drove the score]
```

### Step 5: IEP/504 and Special-Population Override

For any student flagged for individualized feedback (IEP, 504, EL with documented needs), upgrade to Tier A regardless of where they fell in the first-pass sort. List those papers explicitly so they're not missed.

### Step 6: Communication to Students

Tell students how feedback works on this assignment, in advance. Provide a 2-line script:

> "On this assignment, I'm giving full feedback to drafts that are revising. Final scores get a short comment plus the class memo. If you want a longer conversation, sign up for office hours."

This keeps trust while making the triage transparent.

### Step 7: Pile Audit Before You Start Grading

- [ ] Roughly 20/60/20 split or justified deviation
- [ ] All special-population flags upgraded to A
- [ ] Tier C papers will be addressed by the whole-class memo
- [ ] Time budget fits available time with 10% buffer
- [ ] Borderline scores all in tier A (decision will require evidence)

### Step 8: Post-Stack Reflection

After grading, log:

- Did time budget hold?
- Which tier produced the most useful student response (revision, follow-up question)?
- For next stack: which heuristics from this sort should change?

---

## Output Format

1. Feedback purpose statement
2. First-pass sort table (paper IDs by tier)
3. Time budget reconciliation
4. Per-tier feedback templates
5. Special-population upgrade list
6. Student-facing communication script
7. Pile audit checklist
8. Post-stack reflection prompts

---

## False-Positive Prevention

❌ **DON'T:**
- Triage IEP/504 work down — it's an accommodation issue
- Use triage to give vague feedback to weak papers — they often need more, not less
- Skip the whole-class memo if you triaged a lot to tier C — those students still need feedback
- Hide the triage from students — transparency keeps trust
- Triage on demographics — sort on work, not on students

✅ **DO:**
- Declare the feedback purpose first
- Push borderline scores to tier A
- Use the whole-class memo to make tier C defensible
- Tell students how feedback works on this assignment
- Reflect after the stack to refine the heuristics

---

## Quality Indicators

- [ ] Feedback purpose stated up front
- [ ] First-pass sort completed
- [ ] Time budget realistic
- [ ] Per-tier templates ready
- [ ] Special-population upgrades explicit
- [ ] Audit done before grading begins

---

## Techniques Used

| Technique | How It's Applied |
|-----------|-----------------|
| **CM-01** | Stack type, stakes, and time available drive triage decisions. |
| **ST-02** | Sequential sort → budget → template → audit. |
| **OC-01** | Per-tier templates enforce consistent feedback within each tier. |
| **DS-01** | Tiering framework (A/B/C with revision-stakes logic) governs every decision. |
| **QA-01** | Pile audit verifies the triage before time is invested. |
