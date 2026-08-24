---
title: "Skill Gap to Curriculum — Translate a Concrete Gap Into a Sequenced Plan"
category: learning/planning
description: "Translate a real skill gap — something you need to do for a job, project, or goal that you currently can't — into a sequenced learning plan. Names the gap precisely as an observable behavior or output (not 'be better at X'), assesses its depth, surfaces the prerequisite gaps the user is usually skipping, picks the right learning mode (study / deliberate practice / apprenticeship / just doing), designs the smallest loop that closes the gap, and attaches a milestone and a check. Counters the most common mistake: trying to learn at level 3 while level 2 is missing."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - RT-11
  - QA-01
difficulty: intermediate
tags:
  - learning
  - skill-gap
  - prerequisites
  - learning-mode
  - sequencing
updated: "2026-06-18"
reasoning:
  styles: [analytic, systems, strategic]
  stakes: moderate
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: variable
  collaboration: solo
  output_format: [structured, ranked_list]
  user_role: [individual, learner, professional, founder]
  mode: [diagnose, plan]
related_prompts:
  - domain-learning/learning_curriculum_designer.md
  - domain-learning/learning_deliberate_practice_designer.md
  - domain-personal-development/prompts/agency/agency_skill_gap_reframe.md
---

# Skill Gap to Curriculum — Translate a Concrete Gap Into a Sequenced Plan

**Objective:** Take a real, specific skill gap — a thing the user needs to do (for a job, project, or goal) that they currently cannot — and turn it into the smallest sequenced plan that closes it. The work this prompt does that learners usually skip: it forces the gap to be named as an **observable behavior or output** rather than a vague label; it assesses the gap's **depth** so the plan isn't over- or under-built; it surfaces the **prerequisite gaps** the user is silently skipping (most failed self-learning is someone trying to learn level 3 while level 2 is missing); it picks the **right mode** for closing the gap (study, deliberate practice, apprenticeship, or just doing the thing badly until it isn't), since the wrong mode wastes the most time; and it attaches a **milestone and a check** so "done" is verifiable. This is the front-end diagnostic that decides whether you need a curriculum, a practice loop, a mentor, or just to start shipping.

**When to use:**
- A specific thing is blocking a job, project, or goal because the user can't yet do it.
- The user is about to pour weeks into "learning X" and wants to make sure they're learning the right X in the right way.
- The user keeps bouncing off a topic and suspects a missing prerequisite.

**When NOT to use:**
- The gap is already well-understood and clearly needs a broad curriculum — go straight to `learning_curriculum_designer.md`.
- The "gap" is motivation or follow-through, not skill — use the agency prompts in `domain-personal-development/prompts/agency/`.
- The gap is a single narrow sub-skill needing reps — go straight to `learning_deliberate_practice_designer.md`.

**Audience:** Professionals, founders, and self-directed learners facing a concrete capability gap and choosing how to close it.

---

## Inputs / Context

1. **The gap, as stated.** What the user can't currently do. (Probably vague; we'll sharpen it.)
2. **Why it matters now.** The job, project, or goal it's blocking, and the deadline if any.
3. **Current ability near the gap.** What the user *can* do that's adjacent — reveals depth and prerequisites.
4. **Time and access.** Hours available; access to mentors, communities, real work to practice on.
5. **What they've tried.** Prior attempts to close it and where they stalled (often reveals a missing prerequisite).

---

## Constraints

### Must
- Restate the gap as an **observable behavior or output**: "design a normalized schema for a 3-table app and write the migrations," not "be better at databases." If it can't be made observable, that's the first fix.
- Assess the gap's **depth**: intro / intermediate / advanced — relative to the user's current adjacent ability, not in the abstract.
- Surface **prerequisite gaps**: the things that must be solid before the target gap is learnable. Explicitly check whether the user is trying to learn at level 3 with level 2 missing; if so, the plan starts at level 2.
- Choose the **learning mode** deliberately, with a reason:
  - **Study (curriculum)** when the gap is conceptual/knowledge-shaped.
  - **Deliberate practice** when it's a specific skill needing feedback-tight reps.
  - **Apprenticeship** when it's tacit and best absorbed from someone better.
  - **Doing (ship it badly)** when the gap is closed mainly by reps on real output and the cost of bad output is low.
- Design the **smallest loop** that produces the gap-closing skill — the minimum viable learning intervention, not a maximal program.
- Attach a **milestone** (the observable thing that proves the gap is closing) and a **check** (the yes/no test).

### Must Not
- Accept a vague gap label. "Improve at communication" is not a gap; it's a category.
- Plan to learn the target while a prerequisite is missing. That's the dominant failure; check prerequisites first.
- Default to "take a course" for every gap. Mode choice is where most time is saved or wasted.
- Over-build the plan. A small loop that ships beats a comprehensive program that stalls.
- Define success as effort ("studied for three weeks") instead of the observable milestone.

---

## Instructions

### Step 1 — Sharpen the gap to an observable
Rewrite the stated gap as a behavior or output you could watch the user perform or produce. If the user can't make it observable, work with them until they can; the rest of the plan depends on it.

### Step 2 — Assess depth
Place the gap at intro / intermediate / advanced relative to the user's current adjacent ability (Input 3). The same nominal skill is a different gap for a beginner than for someone with adjacent experience.

### Step 3 — Surface prerequisite gaps
List what must be solid before the target gap is learnable. For each, check the user's current state. The key move: detect the level-3-while-level-2-is-missing pattern. If a prerequisite is missing, the plan's first loop targets *it*, not the original gap. Often the prior-attempts input (Input 5) reveals exactly which prerequisite was missing.

### Step 4 — Choose the learning mode
Decide study / deliberate practice / apprenticeship / doing, with a one-line reason tied to the gap's nature. Most gaps are a sequence of modes (e.g., a little study to get the vocabulary, then doing on real output). State the primary mode and any secondary.

### Step 5 — Design the smallest closing loop
Define the minimum loop that closes the (possibly-prerequisite-first) gap: what the user does, how they get feedback, and how the loop repeats. If study mode, hand off to `learning_curriculum_designer.md` with the now-sharpened target. If practice mode, hand off to `learning_deliberate_practice_designer.md`. If apprenticeship, specify whom and how to get reps with them. If doing, specify the real thing to ship and how to ship it badly fast.

### Step 6 — Set the milestone and check
Milestone: the observable artifact or behavior that shows the gap is closing (not closed — closing). Check: the yes/no test for whether the milestone is hit, with a date.

### Step 7 — Set a redirect
If the check fails, what changes — usually that a deeper prerequisite was missed, or the mode was wrong. State the redirect (drop a level, switch modes, get a mentor) rather than "try harder."

### Step 8 — Verify and output
Run the checklist; deliver the gap-specific plan with milestone and check.

---

## False-Positive Prevention

1. **Vague gap.** "Get better at X." Not actionable, not checkable. Force an observable behavior or output.
2. **Prerequisite skip.** Planning to learn the target while a foundation is missing — the dominant cause of stalled self-learning. Check prerequisites and start there if needed.
3. **Course-by-default.** Reaching for a course for every gap. A skill gap often needs reps or a mentor, not a curriculum; choose the mode by the gap's nature.
4. **Over-building.** Designing a 12-week program when a two-week doing-loop would close the gap. Smallest loop first.
5. **Mode mismatch.** Studying a gap that only closes through doing, or just-doing a gap that needs conceptual grounding first. Match mode to gap.
6. **Effort-as-success.** Defining done as time spent rather than the observable milestone. Hours aren't the deliverable.
7. **Depth misread.** Treating an intermediate's gap like a beginner's (boring, wasteful) or a beginner's like an intermediate's (overwhelming, stalls). Assess depth relative to current ability.
8. **No redirect.** A check with no consequence when it fails. Specify the redirect — usually a missed prerequisite or wrong mode.

---

## Output Format

```
# Skill-Gap Plan — [the gap]

## Gap (observable)
[Behavior or output you could watch the user perform/produce.]
- Stated as: "[original vague version]" → sharpened above.

## Depth
[Intro / intermediate / advanced], relative to current adjacent ability: [...]

## Prerequisite check
| Prerequisite | Solid? | If not → plan starts here |
|--------------|--------|---------------------------|
| [...] | yes/no | |
Level-3-while-2-missing detected? [yes/no] → first loop targets: [...]

## Learning mode
- Primary: [study / deliberate practice / apprenticeship / doing] — because [...]
- Secondary (if any): [...]
- Hand-off: [learning_curriculum_designer.md / learning_deliberate_practice_designer.md / mentor plan / ship-it plan]

## Smallest closing loop
- What the user does: [...]
- Feedback: [...]
- Repeat: [cadence]

## Milestone & check
- Milestone (gap closing): [observable artifact/behavior]
- Check (yes/no): [...] by [date]

## Redirect if the check fails
[Drop a level / switch modes / get a mentor — not "try harder."]
```

---

## Verification

- [ ] The gap is restated as an observable behavior or output.
- [ ] Depth is assessed relative to current adjacent ability.
- [ ] Prerequisites are checked, and the level-3-while-2-missing pattern is explicitly tested.
- [ ] The learning mode is chosen with a reason, not defaulted to "take a course."
- [ ] The plan is the smallest loop that closes the gap, not a maximal program.
- [ ] A milestone (gap closing) and a dated yes/no check are attached.
- [ ] A redirect is specified for check failure (deeper prerequisite or wrong mode).
- [ ] Success is the observable milestone, not effort or time spent.
