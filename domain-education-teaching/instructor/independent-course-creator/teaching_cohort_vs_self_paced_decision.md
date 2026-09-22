---
title: "Cohort vs Self-Paced Decision"
category: education-teaching/instructor/independent-course-creator
description: "Decide whether an independent course runs as a live cohort, self-paced, or a hybrid — by matching the learning mechanism the capability actually needs against the instructor hours each mode consumes per learner, rather than by which model is currently fashionable."
techniques:
  - DT-01
  - DS-06
  - RT-05
  - CM-02
  - QA-04
difficulty: intermediate
tags:
  - course-creation
  - cohort
  - self-paced
  - delivery-mode
  - independent-instructor
  - instructional-design
updated: "2026-09-22"
related_prompts:
  - domain-education-teaching/instructor/independent-course-creator/teaching_expertise_to_teachable_scope.md
  - domain-education-teaching/instructor/independent-course-creator/teaching_course_completion_and_engagement_design.md
  - domain-education-teaching/program/curriculum-design/program_course_design_he.md
---

# Cohort vs Self-Paced Decision

**Objective:** Choose a delivery mode from two facts — what the capability
requires in order to be learned, and how many instructor hours per learner each
mode costs — and state what the choice gives up.

**When to Use:**
- The scope is settled and the mode is not.
- You are drawn to cohorts for the completion rates and have not priced the
  hours.
- You are drawn to self-paced for the margin and have not asked whether the
  capability can be acquired without feedback.
- A course exists in one mode and is not working, and you suspect the mode.

**When NOT to use:**
- This is a semester course and the question is in-person to online, with
  faculty workload — `instructor/higher-ed-corporate/teaching_online_course_conversion.md`
  owns that, in a semester frame.
- The question is lesson-level blended or HyFlex design —
  `instructor/ed-tech/teaching_blended_hyflex_lesson_designer.md`.
- The scope is not settled — `teaching_expertise_to_teachable_scope.md` first.
  Choosing a mode for an unscoped course decides nothing.

## Inputs / Context

1. **The capability** from scoping, in the learner's observable verbs.
2. **How that capability is actually acquired.** Be specific: by watching, by
   doing with feedback, by doing repeatedly, by being unstuck at the right
   moment, by working with others.
3. **Instructor hours available per week**, and for how many weeks.
4. **Expected enrolment**, and whether it recurs.
5. **The learners' constraints** — time zones, schedules, whether they can
   commit to a fixed hour.
6. **Price**, and what it implies about contact.

## Method

1. **Name the learning mechanism the capability needs (DT-01).**
   This is the decisive input, and it is the one usually skipped.

   | If the capability is acquired by… | The mode must supply |
   |---|---|
   | knowing something | content; self-paced is sufficient |
   | doing it once, correctly | worked examples and a checkable artifact |
   | doing it with feedback | a feedback loop; someone must look |
   | judgement under ambiguity | exposure to others' attempts and reasoning |
   | sustained practice | accountability over time |

   A capability needing feedback, delivered self-paced with no feedback loop,
   does not produce the capability. That is an instructional failure, not a
   marketing one, and no amount of engagement design fixes it.

2. **Cost each mode in instructor hours per learner (DS-06).**

   | Mode | Build | Per cohort | Per learner | Scales by |
   |---|---|---|---|---|
   | Self-paced | high | none | ~0 live, plus support | content, once |
   | Cohort | medium | live hours × sessions | feedback hours | your calendar |
   | Hybrid | high | fewer live hours | bounded feedback | the bound you enforce |

   Compute it: at enrolment N, mode M costs H hours. Compare against hours
   available. Most cohort plans fail here and only discover it mid-run.

3. **Find the hybrid honestly, if there is one.**
   Hybrid means self-paced content plus a *bounded* live or feedback element —
   bounded meaning a stated number of hours, a stated response time, and a stated
   limit. An unbounded hybrid is a cohort with worse economics: you carry the
   feedback load without the cohort's schedule to contain it.

4. **State what the choice gives up (RT-05).**
   - Self-paced gives up feedback, peer learning and the schedule that produces
     completion.
   - Cohort gives up asynchronous access, scale, and revenue between runs.
   - Hybrid gives up simplicity, and fails when the bound is not enforced.

   A decision with nothing given up has not been made.

5. **Set the review condition (QA-04).**
   An observable that would change the decision: completion below X, feedback
   hours exceeding the budget by Y, enrolment below the cohort minimum.

## Output Format

```
# Delivery mode — [course]

## The capability and how it is acquired
Capability: [from scoping]
Acquired by: [mechanism]
Therefore the mode must supply: [...]

## Hours
| Mode | Build hrs | Hrs per cohort | Hrs per learner | At N=[n], total | Fits [available]? |
|---|---|---|---|---|---|

## Decision
Mode: [self-paced | cohort | hybrid]
Because: [the mechanism], and the hours [do/do not] permit the alternative.

If hybrid — the bounds:
- Live hours: [n], on [schedule]
- Feedback: [what, within what response time]
- Hard limit: [the thing you will refuse, and how you will say it]

## What this gives up
- [...]
- [...]

## Review condition
Revisit when: [observable], not on a date.

## Open questions
- [unresolved, and what it blocks]
```

## Verification

- [ ] The learning mechanism is named before the mode is chosen.
- [ ] Hours per learner are computed at a stated enrolment and compared with
      hours available.
- [ ] If hybrid, all three bounds are stated, including what will be refused.
- [ ] What the choice gives up is written down.
- [ ] The review condition is observable.

## False-Positive Prevention

1. **Do not pick the mode first and justify it.** Cohorts are fashionable and
   self-paced is profitable; neither is a reason. The mechanism decides.
2. **Self-paced delivery of a feedback-dependent capability is a design defect.**
   Learners will not complete it, and the cause is not motivation. Either add a
   feedback loop or change the capability.
3. **Unbounded hybrid is the worst of both.** If the bound is not stated and
   enforceable, price it as a cohort.
4. **Cohort hours do not fall with experience as fast as people expect.**
   Feedback is per learner, every run.
5. **A completion rate is not a mode comparison.** Cohorts complete better partly
   through selection — people who commit to a schedule are different people.
   Do not attribute the whole gap to the mode.
6. **Do not decide before the scope exists.** Mode for an unscoped course is a
   preference, and it will be revisited the moment the scope lands.

## Related

- `teaching_expertise_to_teachable_scope.md` — the scope this decides for.
- `teaching_course_completion_and_engagement_design.md` — making the chosen mode
  actually finish.
- `domain-education-teaching/program/curriculum-design/program_course_design_he.md`
  — designing the course once the mode is fixed.
