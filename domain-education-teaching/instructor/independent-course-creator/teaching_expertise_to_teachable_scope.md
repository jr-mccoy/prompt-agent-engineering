---
title: "Expertise to Teachable Scope"
category: education-teaching/instructor/independent-course-creator
description: "Turn tacit expertise into a scope a stranger will pay to acquire: surface what you do that you have stopped noticing, name the one capability a learner leaves with, cut everything that is context rather than capability, and hand the result to a course designer rather than designing the course here."
techniques:
  - RT-05
  - DT-01
  - CM-02
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - course-creation
  - expertise-elicitation
  - scoping
  - independent-instructor
  - curriculum
  - tacit-knowledge
updated: "2026-09-22"
related_prompts:
  - domain-education-teaching/program/curriculum-design/program_course_design_he.md
  - domain-education-teaching/instructor/independent-course-creator/teaching_cohort_vs_self_paced_decision.md
  - domain-business-strategy/creator-economy/creator_prelaunch_demand_validation.md
---

# Expertise to Teachable Scope

**Objective:** Convert what a practitioner knows into a single named capability
a learner can leave with, scoped tightly enough to design against — then hand
off to course design rather than doing it here.

**This prompt deliberately builds only the front half.**
`program/curriculum-design/program_course_design_he.md` already claims course
design, redesign, syllabus creation, constructive alignment, intended learning
outcomes and modality conversion. A second course designer would collide with it
head-on. This one stops at the scope and names the handoff.

**When to Use:**
- A practitioner wants to teach what they do and cannot say where to start.
- A course outline keeps growing because everything feels necessary.
- You have a topic and need a *capability* — the difference between "SQL" and
  "can find the query that is slowing down a report".
- Someone has years of experience and produces a table of contents that looks
  like a textbook's.

**When NOT to use:**
- You are designing the course: modules, alignment, assessment, syllabus — that
  is `program_course_design_he.md`, and this prompt's output is its input.
- You are writing a lesson — `instructor/lesson-planning/` and
  `teaching_microlearning_module.md` own that.
- You are writing learning objectives with Bloom's and ABCD —
  `program/curriculum-design/program_learning_objectives_writer_blooms.md`.
- You are writing the sales page — that is a copywriting job.

## Inputs / Context

The practitioner supplies:

1. **What they actually do**, in the last month, with specifics. Not their job
   title — three real pieces of work.
2. **What people ask them for.** Repeated questions are the most reliable
   signal available and cost nothing to collect.
3. **What they see that others miss** in their domain — the judgement call, the
   thing they notice first, the mistake they can spot at a glance.
4. **Who the learner is**, and crucially what the learner can already do.
5. **What the learner wants to be able to do afterwards**, in their own words if
   you have them.
6. **Constraints** — how much the practitioner can teach, and by when.

## Method

1. **Elicit the tacit layer (RT-05).**
   Expertise becomes invisible to the person who has it. Work the three real
   pieces of work:
   - What did you decide that you did not deliberate about?
   - What would a competent beginner have done instead, and what would it have
     cost them?
   - Where did you *not* do the obvious thing, and why?

   The answers are the course. The things they can already articulate are
   usually the things already on the internet.

2. **Name one capability, in the learner's verbs (CM-02).**
   Form: *"After this, [learner] can [observable action] in [situation],
   without [the support they needed before]."*
   One. If there is an "and", there are two courses or one that will not finish.

3. **Separate capability from context (DT-01).**

   | Category | Test | Where it goes |
   |---|---|---|
   | Capability | the learner does it, and you could watch them | in scope |
   | Context | useful background, does not change what they can do | a reading list |
   | Prerequisite | they must already have it | stated entry requirement |
   | Adjacent | a different capability | a different course, or nothing |

   Most over-scoped courses are 70% context. Context is what the expert enjoys
   teaching and the learner skips.

4. **Cut to what fits the practitioner's real hours (DS-06).**
   Hours to build, hours to deliver, hours to support. If the scope does not fit,
   cut *capability breadth*, never depth — a narrow capability taught properly
   sells; a broad one taught thinly is a YouTube playlist with a price.

5. **State the entry requirement honestly.**
   What the learner must already be able to do. A course that is unclear about
   this sells to people who will not finish, and non-completion is expensive in
   refunds and reputation.

6. **Verify the scope is teachable (QA-01).**
   - Could you assess the capability? If you cannot describe how you would know
     the learner has it, it is not a capability yet.
   - Could a learner acquire it in the stated hours?
   - Does anything in scope fail the capability test in step 3?

## Output Format

```
# Teachable scope — [working title]

## The capability
After this, [learner] can [observable action] in [situation], without [prior support].

## What the expert knows that they had stopped noticing
| Decision made without deliberating | What a beginner would do instead | What that costs |
|---|---|---|

## In scope / out of scope
| Item | Capability / Context / Prerequisite / Adjacent | Verdict |
|---|---|---|

## Entry requirement
The learner must already be able to: [...]
This course is wrong for: [who, specifically]

## Size
| Build hrs | Delivery hrs | Support hrs | Available | Fits? |
|---|---|---|---|---|

If it does not fit, what was cut (breadth, not depth): [...]

## How you would know they have it
[the assessment, in one sentence — not designed here, but nameable]

## Handoff
Design the course with `program/curriculum-design/program_course_design_he.md`,
supplying: the capability, the entry requirement, the in-scope list, the hours.
Decide delivery mode first with `teaching_cohort_vs_self_paced_decision.md`.

## Open questions
- [unresolved, and what it blocks]
```

## Verification

- [ ] Exactly one capability, stated in the learner's observable verbs.
- [ ] The tacit-layer table has at least three rows with real decisions in them.
- [ ] Every scope item is classified, and the context items are out.
- [ ] The entry requirement names who this course is wrong for.
- [ ] Hours fit; if they did not, breadth was cut rather than depth.
- [ ] The assessment is nameable in one sentence.
- [ ] The handoff to `program_course_design_he.md` is explicit.

## False-Positive Prevention

1. **A topic is not a capability.** "Advanced SQL" is a topic. "Can find the
   query slowing down a report" is a capability. If it does not contain a verb
   the learner performs, keep going.
2. **The articulable part is usually the commodity.** What the expert can already
   explain fluently is generally what is already written down somewhere. The
   valuable material is what they had to be asked about twice.
3. **Do not design the course here.** Modules, sequencing, assessment design and
   alignment belong to `program_course_design_he.md`. Producing a module list
   here duplicates it and produces a worse one.
4. **Cutting depth is the wrong cut.** A thin broad course competes with free
   content and loses. A narrow deep one does not.
5. **An unstated entry requirement is a refund.** Learners who cannot follow
   blame the course, and they are half right.
6. **"Everything I know" is not a scope.** If the expert cannot name something
   they are deliberately leaving out, the scoping has not happened yet.

## Related

- `domain-education-teaching/program/curriculum-design/program_course_design_he.md`
  — the course design this hands off to.
- `teaching_cohort_vs_self_paced_decision.md` — delivery mode, decided before design.
- `domain-business-strategy/creator-economy/creator_prelaunch_demand_validation.md`
  — whether anyone will pay for the capability, before it is built.
