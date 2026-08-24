---
title: "Reframe Skill Gaps as Separate from Project Goals"
category: personal-development/agency
description: "Separate a stated skill gap from the project the user is trying to ship, so learning doesn't silently become a substitute for shipping — and the real minimum needed is isolated and bounded."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - agency
  - skill-gap
  - learning
  - avoidance
  - project-execution
updated: "2026-04-20"
related_prompts:
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-personal-development/prompts/agency/agency_planning_masquerade_detector.md
  - domain-personal-development/prompts/goals/goals_decompose_learning_task.md
---

# Reframe Skill Gaps as Separate from Project Goals

**Objective:** When a user says "I can't ship X until I learn Y," test the claim. Separate Y (the skill) from X (the project). Identify the smallest slice of Y that's actually required to ship X, move it into a bounded parallel track, and restart the project with the minimum-viable knowledge.

**When to use:** The user says they need to "learn Rust," "get better at design," "understand marketing," or "learn AI" before they can ship their thing. They've been in the learning phase for weeks or months. The project has not advanced.

**Audience:** An individual who is motivated, not lazy — often highly motivated, which is how they got into the learning-trap in the first place.

---

## Inputs Required

1. **The project.** What X is, and what "shipped" looks like concretely.
2. **The stated skill gap.** Y — how the user describes it.
3. **What the user has already done toward learning Y.** Courses, books, tutorials, hours, recent artifacts.
4. **What specifically, in the project, the user believes requires Y.** Best honest guess.
5. **The user's fallback posture if Y never got closed.** Would they still want to build X?

If (4) is vague ("just all of it"), that's a finding — flag it.

---

## Instructions

### Step 1 — Separate Y into subsets

Break Y into three layers, sized to the specific project X:

- **Critical subset:** The narrow slice of Y that must be known to ship X at the ship-floor level. Usually very small (e.g., "the difference between async and sync in one language"), not the whole topic.
- **Useful-but-deferrable subset:** Y-things that would make X better but aren't required to ship. These can be learned after the first ship.
- **Orthogonal subset:** Y-things the user currently lumps under Y but that are not actually on the path to X at all. Adjacent interests, not prerequisites.

Name each layer with specifics. "Async in one language" not "concurrency." "Typography rules for body text in long-form essays" not "design."

### Step 2 — Test whether the project actually needs Y

For the "critical subset," run three tests:

- **Existence test:** Do other people ship X-class things without deep Y? If yes, Y may not be required; strictly the critical subset is.
- **Substitution test:** Can a library, template, tool, or partial-knowledge fallback cover the critical subset without deep understanding? Often yes.
- **Post-ship test:** Can the critical subset be learned while shipping the project, inside the project, not before?

Report the results. If all three tests show Y is weaker-than-claimed a prerequisite, call that out plainly.

### Step 3 — Identify what the user can ship now

Write a short paragraph describing a version of X that can ship with the user's current knowledge. This may be:

- X with a smaller feature set.
- X using a more familiar tool.
- X at a lower level of polish that still counts as shipped.

This is not a suggestion to abandon ambition; it's the minimum version that starts the feedback loop. Later versions can incorporate more Y.

### Step 4 — Move learning into a parallel track

Reshape Y into a bounded side-track that runs alongside project work, not blocking it:

- **Minimum session size.** E.g., 30 minutes.
- **Maximum weekly time.** Capped so it can't swallow project hours.
- **Scope.** Only the critical subset at first. Defer the rest.
- **Termination condition.** When the critical subset is covered, the side-track closes or moves to the useful-but-deferrable subset.

Learning in a bounded side-track ≠ learning as the project. Be explicit about the boundary.

### Step 5 — Name the avoidance risk if present

One of two things is true:

- **A. Y is genuinely a narrow prerequisite.** Then Step 4's side-track works, and the user should ship a smaller X in parallel.
- **B. Y is being used as avoidance** — the user's momentum drops every time shipping comes close, and returns when a new learning path opens. If the user's inventory shows this pattern (repeated learning dives with no shipping), name it directly and recommend running `agency_planning_masquerade_detector.md` or `agency_stuck_diagnosis.md`.

Don't default to (B); only claim it if the evidence supports it.

### Step 6 — Restart the project

Give the user one concrete action to restart the project this session. Not "think about the smaller version." Open the file, make the first change. See `agency_next_action_spec.md` if a fuller spec is needed.

---

## Constraints

### Must
- Split Y into critical / useful / orthogonal subsets with specifics.
- Run all three tests on the critical subset.
- Propose a version of X that can ship with current knowledge.
- Bound the learning side-track in time and scope.
- Name the avoidance risk only when evidence supports it.

### Must Not
- Recommend the user learn Y deeply before starting X.
- Pretend Y doesn't matter — the critical subset is real.
- Suggest a full curriculum. This prompt isn't a learning plan; it's a reframe.
- Blanket-label the user as avoiding; distinguish case (A) from case (B).
- Recommend they lower ambition permanently. The small X is a restart, not the ceiling.

---

## False-Positive Prevention

1. **Don't minimize real prerequisites.** Some skills really are required. Surgery without anatomy doesn't work. Run the three tests honestly rather than assuming Y is always inflated.
2. **Don't inflate the critical subset.** When in doubt, shrink it. Users can always add learning later; un-learning weeks spent on non-essentials is costly.
3. **Don't substitute one big learning plan for another.** The learning side-track must be smaller than the project hours, not equal to them.
4. **Don't accuse the user of avoidance without evidence.** Use case (B) only when repeated learning-pivots with no shipping are visible.
5. **Don't equate the smaller-X with the final ambition.** Be explicit that the smaller ship is the first draft of a longer arc.

---

## Output Format

```
# Skill-gap reframe: [Y] for [X]

## Y decomposed
- Critical subset: [specific]
- Useful-but-deferrable: [specific]
- Orthogonal: [specific]

## Tests on critical subset
- Existence: [do others ship X-class without deep Y?]
- Substitution: [is there a library/tool/template substitute?]
- Post-ship: [can critical subset be learned during X?]

## Smaller X that can ship now
[One paragraph describing the minimum shippable version with current knowledge.]

## Learning side-track
- Min session: [size]
- Max weekly time: [cap]
- Scope: critical subset first
- Termination: [when]

## Avoidance risk
- Case (A) genuine prerequisite — [evidence]
- Case (B) avoidance pattern — [evidence if present, "not supported" if not]

## Restart action (this session)
[One concrete physical-motion action on the project.]

## Uncertainty
[Anything the inputs didn't resolve.]
```

---

## Verification

- [ ] Critical subset is genuinely narrow, not the whole field.
- [ ] All three tests were run.
- [ ] A version of X is proposed that can ship with current knowledge.
- [ ] Learning side-track is capped.
- [ ] Avoidance claim is evidence-based or not made.
- [ ] Restart action is a concrete physical motion, not a reflection.
