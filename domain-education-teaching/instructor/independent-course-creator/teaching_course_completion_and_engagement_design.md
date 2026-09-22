---
title: "Course Completion and Engagement Design"
category: education-teaching/instructor/independent-course-creator
description: "Design an independent course so learners finish it: find where they actually stop rather than where you assume, distinguish a design problem from a motivation problem, build the smallest intervention that removes the blockage, and measure completion honestly against who started."
techniques:
  - DS-06
  - RT-05
  - DT-01
  - QA-04
  - OC-03
difficulty: intermediate
tags:
  - course-creation
  - completion
  - retention
  - engagement
  - independent-instructor
  - learner-success
updated: "2026-09-22"
related_prompts:
  - domain-education-teaching/instructor/independent-course-creator/teaching_cohort_vs_self_paced_decision.md
  - domain-education-teaching/instructor/independent-course-creator/teaching_expertise_to_teachable_scope.md
  - domain-education-teaching/program/evaluation-analytics/program_early_warning_system_designer.md
---

# Course Completion and Engagement Design

**Objective:** Raise the number of learners who acquire the capability, by
locating where they stop, deciding whether that is design or motivation, and
building the smallest thing that removes it.

**This gap is pre-sanctioned by the domain's own roadmap.**
`EXPANSION_ROADMAP.md` records, under Deferred, that `program/` has no
student-success or retention track. The nearest existing prompts —
`program/evaluation-analytics/program_early_warning_system_designer.md` and
`program_continuous_improvement_cycle.md` — are institutional: they assume an
LMS, a cohort of hundreds and a committee. This is the independent-instructor
version.

**When to Use:**
- A course sells and most buyers never finish it.
- You are about to add gamification, streaks or badges and want to know whether
  the problem is motivation at all.
- A cohort loses people at the same point every run.
- You need a completion number you can state honestly.

**When NOT to use:**
- You need an institutional early-warning system across a programme —
  `program_early_warning_system_designer.md`.
- You need to design a lesson or a microlearning module —
  `instructor/higher-ed-corporate/teaching_microlearning_module.md` and
  `instructor/lesson-planning/`.
- The capability itself is wrong for the mode — go back to
  `teaching_cohort_vs_self_paced_decision.md`; no engagement design rescues a
  feedback-dependent capability delivered with no feedback.

## Inputs / Context

1. **Where learners actually stop**, per module or per week. Real data, however
   thin. If you do not have it, collecting it is step 1 and everything else waits.
2. **The course structure** — modules, what each asks the learner to do, and
   how long each takes.
3. **The mode** — cohort, self-paced or hybrid, and its bounds.
4. **What happens when someone stalls today.** Usually nothing; say so.
5. **Instructor hours available for support.**
6. **What "completion" means here** — finished the material, or acquired the
   capability. These are different numbers and the second one matters.

## Method

1. **Find the stall point before theorising (DS-06).**
   Plot starts and completions per module. Two patterns, with different causes:
   - **A cliff** at one module: that module is the problem. Something in it is
     too hard, too long, too vague, or requires something the learner does not
     have.
   - **A slope** from the start: the problem is the entry, the promise, or the
     mode — people who never really started.

   Diagnosing a cliff as a slope produces motivational emails aimed at people
   who are stuck on a specific thing.

2. **Classify the blockage (DT-01).**

   | Type | Signal | Fix |
   |---|---|---|
   | Design | everyone stops at the same place | fix that module |
   | Prerequisite | some learners stop early, and share a background | state the entry requirement |
   | Feedback | learners produce work and hear nothing | add a bounded feedback loop |
   | Friction | the next step is unclear or effortful | remove the step, not the content |
   | Motivation | dispersed stalls, no shared point | accountability structure |

   **Most "motivation problems" are design problems.** Motivation is the
   residual after the other four are excluded, not the first explanation.

3. **Build the smallest intervention (RT-05).**
   Per blockage, the cheapest thing that removes it. Ranked by cost to you:
   - splitting an over-long module;
   - a worked example of the thing they are stuck on;
   - a stated entry requirement that stops the wrong learners enrolling;
   - a checkpoint artifact someone actually looks at;
   - a scheduled deadline;
   - and only then, accountability mechanics.

   Gamification is the last resort, not the first. It raises activity, which is
   not the same as the capability, and it is easy to mistake one for the other.

4. **Set the intervention's own success test (QA-04).**
   What completion rate at that module, by when, would say it worked. Otherwise
   you will keep the intervention because you built it.

5. **Measure completion honestly (OC-03).**
   Report against **everyone who started**, including people who never opened
   module one. Rates computed over "active learners" are the number people
   publish and the number that means least. State both if you must, and lead
   with the honest one.

   Then report the capability number separately: of those who completed, how
   many can now do the thing. That number is usually smaller, and it is the one
   the course exists for.

## Output Format

```
# Completion design — [course]

## Where learners stop
| Module | Started | Completed | Drop |
|---|---|---|---|

Pattern: [cliff at module N | slope from the start]

## Blockage classification
| Stall point | Type | Evidence | Fix |
|---|---|---|---|

Motivation was concluded only after excluding: [the four other types]

## Interventions, cheapest first
| # | Intervention | Cost to instructor | Blockage it removes | Success test |
|---|---|---|---|---|

Not doing: [what you considered and rejected, and why]

## Honest measurement
Completion, of everyone who started: [n]%
Completion, of those who opened module one: [n]%
Acquired the capability, of those who completed: [n] — measured by [...]

## Review
Revisit when: [observable condition]

## Open questions
- [unresolved, and what it blocks]
```

## Verification

- [ ] Stall points come from data, not assumption.
- [ ] The pattern is identified as cliff or slope before any fix is proposed.
- [ ] Motivation was concluded only after excluding the other four types.
- [ ] Interventions are ranked cheapest-first and each has a success test.
- [ ] Completion is reported against everyone who started.
- [ ] The capability number is reported separately from the completion number.

## False-Positive Prevention

1. **"Learners are not motivated" is the last explanation, not the first.** It is
   also the only one that blames the learner, which is why it is reached for.
   Exclude design, prerequisite, feedback and friction first.
2. **Activity is not learning.** Streaks, badges and check-ins raise activity
   metrics reliably and capability unreliably. If you add them, keep measuring
   the capability separately or you will not notice the difference.
3. **Completion over "active learners" is a vanity number.** It excludes exactly
   the people who dropped out hardest.
4. **A cliff is one module's problem.** Course-wide interventions aimed at a
   cliff cost everyone and help nobody.
5. **Do not add content to fix a stall.** A learner stuck at module four is not
   helped by a fifth module. Usually the fix is subtraction.
6. **Deadlines work and have a cost.** They raise completion and exclude learners
   whose lives do not fit them. State the trade rather than treating the
   improvement as free.
7. **Small numbers are still evidence, and they are still small.** Twelve
   learners tell you where the cliff is; they do not support a rate you quote.

## Related

- `teaching_cohort_vs_self_paced_decision.md` — when the mode is the cause.
- `teaching_expertise_to_teachable_scope.md` — when the scope is the cause.
- `domain-education-teaching/program/evaluation-analytics/program_early_warning_system_designer.md`
  — the institutional version, for programmes with an LMS and a committee.
