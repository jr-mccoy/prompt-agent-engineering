---
title: "Deliberate Practice Designer — A Focused Loop for One Specific Sub-Skill"
category: learning/practice
description: "Design a deliberate-practice loop for a single, narrow sub-skill. Unlike a curriculum (broad), this is the focused rep loop. Forces narrowness (deliberate practice requires a specific sub-skill, not a domain), designs one time-bounded rep, builds in an immediate-feedback mechanism (without feedback, repetition is not deliberate), sets rep volume and cadence, names the failure mode where reps degrade into rote, and sets the progression criteria for when the rep gets harder. Output: a practice spec plus a 4-week ramp."
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
  - deliberate-practice
  - feedback
  - skill-acquisition
  - reps
updated: "2026-06-18"
reasoning:
  styles: [analytic, systems, empirical]
  stakes: moderate
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: single_domain
  collaboration: solo_or_pair
  output_format: [spec, structured]
  user_role: [individual, learner, professional]
  mode: [plan, rehearse]
related_prompts:
  - domain-learning/learning_curriculum_designer.md
  - domain-learning/learning_skill_gap_to_curriculum.md
  - domain-personal-development/prompts/agency/agency_foundation_session.md
---

# Deliberate Practice Designer — A Focused Loop for One Specific Sub-Skill

**Objective:** Design a deliberate-practice loop for one narrow sub-skill. Deliberate practice is not "doing the activity a lot" — it is repeated, focused work on a specific sub-skill at the edge of current ability, with immediate feedback, sustained until the sub-skill improves. The two things that turn ordinary practice into deliberate practice are **narrowness** (you practice "writing concrete opening sentences," not "writing") and **feedback** (a rep without feedback is just a rep; you can't correct what you can't see). This prompt forces both, designs the single time-bounded rep, sets the volume and cadence, names where the loop will degrade into mindless rote, and defines when the rep should get harder. The output is a practice spec and a 4-week ramp.

**When to use:**
- A learner has identified a specific weakness (writing tight paragraphs, debugging methodically, handling objections on sales calls, painting faces, sight-reading, giving feedback) and wants to drill it.
- They can carve out short, regular practice sessions.
- Feedback is available — self-graded against a rubric, from a tool, or from a person.

**When NOT to use:**
- The goal is broad domain competence — use `learning_curriculum_designer.md`.
- No feedback mechanism is possible at all; without feedback this loop won't work, so first solve the feedback problem.
- The sub-skill is still too vague to name precisely — narrow it first (the prompt will push on this, but if it can't be narrowed, the learner isn't ready).

**Audience:** Self-directed learners and professionals who want to deliberately improve one specific, nameable sub-skill.

---

## Inputs / Context

1. **The skill, as the user states it.** Probably too broad; we'll narrow it.
2. **Why this sub-skill.** What it unlocks, where the current weakness shows up.
3. **Current performance.** What a current rep looks like and where it falls short.
4. **Feedback options.** What feedback is available — a rubric, a tool, a mentor, a recording, a metric.
5. **Time per session and sessions per week.** Realistic.
6. **Edge.** What's just beyond current ability — the zone where practice should sit.

---

## Constraints

### Must
- **Narrow the skill** to one specific sub-skill. "Get better at writing" → "open paragraphs with a concrete image or claim rather than a throat-clearing generality." If it can't be narrowed to something rep-able, say so.
- Design **one rep**: what the learner does in a single, time-bounded repetition (e.g., "write 5 opening sentences for a given topic in 10 minutes"). Reps are short and specific.
- Build an **immediate-feedback mechanism** into every rep. Specify exactly how the learner sees whether the rep was good: a rubric to self-grade against, a model answer to compare to, a tool's output, a metric, a person. No feedback = not deliberate.
- Set **rep volume and cadence**: reps per session, sessions per week. Enough volume to matter, not so much that it degrades.
- Name the **degradation failure mode** — the point where reps go on autopilot and stop being deliberate — and the countermeasure.
- Set **progression criteria**: the observable signal that the current rep is mastered and should get harder, plus how it gets harder (more constraint, less time, higher difficulty, novel context).

### Must Not
- Practice the whole domain. Breadth defeats the purpose; deliberate practice is narrow by definition.
- Design a rep with no feedback. Repetition without feedback ingrains errors as readily as it ingrains skill.
- Set the difficulty at comfort level. If the reps feel easy, they're not at the edge and won't drive improvement.
- Set rep volume so high that focus collapses; quality of attention beats quantity once focus breaks.
- Leave progression undefined, so the learner drills the same easy rep forever and plateaus.

---

## Instructions

### Step 1 — Narrow the sub-skill
Take the stated skill and cut it down to one specific, observable sub-skill that can be practiced in short reps. State it as a behavior, not a quality. If you can't get it narrow enough to rep, name what's blocking that and stop here.

### Step 2 — Specify the rep
Define one repetition precisely: the prompt/input, the action, the time bound, and the output. A rep should be small enough to do many times in a session.

### Step 3 — Build the feedback mechanism
Specify exactly how the learner gets feedback on each rep, immediately. Options in rough order of preference: a person who can critique; a tool/metric that scores; a model/exemplar to compare against; a rubric to self-grade. Write the actual rubric or comparison criteria if self-graded. State the feedback latency (immediate is the target).

### Step 4 — Set volume and cadence
Reps per session and sessions per week, calibrated to the time budget and to sustaining focus. Note the point at which adding reps stops helping.

### Step 5 — Find the edge
Confirm the rep sits just beyond current comfort. If current performance is already fine at this difficulty, raise it now. Describe what "at the edge" feels like here (some failure, some strain) so the learner can self-check.

### Step 6 — Name the degradation mode
Every practice loop decays into rote eventually — the learner stops attending and just goes through motions. Name how that shows up for *this* rep (e.g., reusing the same sentence pattern, stopping reading the feedback) and the countermeasure (vary the input, raise difficulty, add a constraint, take a real break).

### Step 7 — Set progression criteria
Define the observable signal that the current rep is owned (e.g., "8/10 reps clear the rubric two sessions running") and specify the next, harder version of the rep. Chain at least 3 progression levels for the ramp.

### Step 8 — Build the 4-week ramp
Lay out 4 weeks: which progression level each week, volume, the feedback in use, and a weekly check. Week 4 ends with an assessment of whether the sub-skill has measurably improved.

### Step 9 — Verify and output
Run the checklist; deliver the spec and ramp.

---

## False-Positive Prevention

1. **Too-broad target.** "Practice writing." Not rep-able, not deliberate. Force a specific sub-skill stated as a behavior.
2. **Feedback-free reps.** Designing the rep but no way to see if it was good. This is the central failure; without immediate feedback the loop ingrains errors. Build the mechanism explicitly.
3. **Comfort-zone difficulty.** Reps that feel easy. No strain, no growth. Keep it at the edge; raise difficulty when reps stop failing.
4. **Volume over quality.** Cramming so many reps that attention collapses and the practice goes rote. Cap volume at sustained-focus level.
5. **Rote drift unaddressed.** Ignoring that every loop degrades. Name the degradation mode and its countermeasure up front.
6. **Frozen difficulty.** Drilling the same rep forever with no progression, producing a plateau. Define progression criteria and the next-harder rep.
7. **Self-grading without a rubric.** "I'll just tell if it's good." Vague self-assessment isn't feedback. Write the rubric or comparison.
8. **Activity mistaken for practice.** Doing the real task and calling it practice. Real performance isn't deliberate practice; the isolated, feedback-tight rep is.

---

## Output Format

```
# Deliberate Practice Spec — [narrow sub-skill]

## The sub-skill (behavior, not quality)
[Specific, observable, rep-able.]

## Why it matters
[What it unlocks / where the weakness shows.]

## The rep
- Input/prompt: [...]
- Action: [...]
- Time bound: [...]
- Output: [...]

## Feedback mechanism (immediate)
- Type: [person / tool / exemplar / rubric]
- How seen each rep: [...]
- Rubric or comparison (if self-graded):
  - [criterion 1]
  - [criterion 2]
- Latency: [immediate target]

## Volume & cadence
- Reps/session: [...]
- Sessions/week: [...]
- Volume ceiling (focus collapse point): [...]

## Edge check
- At the edge because: [some failure expected at this difficulty]

## Degradation mode & countermeasure
- Degrades when: [...]
- Countermeasure: [...]

## Progression ladder
| Level | Rep difficulty | Mastery signal to advance |
|-------|----------------|---------------------------|
| 1 | | |
| 2 | | |
| 3 | | |

## 4-week ramp
| Week | Progression level | Volume | Feedback in use | Weekly check |
|------|-------------------|--------|-----------------|--------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | Assessment | | | Measurably improved? |
```

---

## Verification

- [ ] The sub-skill is narrow, observable, and stated as a behavior.
- [ ] One rep is specified with input, action, time bound, and output.
- [ ] Every rep has an immediate feedback mechanism; a rubric is written if self-graded.
- [ ] Volume and cadence respect a focus ceiling.
- [ ] The rep is confirmed to sit at the edge of current ability.
- [ ] A degradation mode and countermeasure are named.
- [ ] Progression criteria are observable and chain at least 3 levels.
- [ ] The 4-week ramp ends with a measurable-improvement assessment.
- [ ] No feedback-free reps and no whole-domain practice survive.
