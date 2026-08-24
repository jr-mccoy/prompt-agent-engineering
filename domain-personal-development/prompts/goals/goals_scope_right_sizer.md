---
title: "Right-Size a Goal That's Too Big to Start or Too Small to Pull"
category: personal-development/goals
description: "Calibrate a goal that never gets started (too big) or generates no traction (too small) to the right size for the user's real weekly capacity and horizon. Diagnoses the sizing fault, then rewrites the goal to a size the user will actually start and sustain."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-20
difficulty: intermediate
tags:
  - goals
  - scope
  - right-sizing
  - capacity
  - calibration
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/goals/goals_progress_stall_diagnostic.md
  - domain-personal-development/prompts/goals/goals_goal_conflict_resolver.md
  - domain-personal-development/prompts/goals/goals_skill_breakdown_blueprint.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
  - domain-personal-development/prompts/agency/agency_project_ownership_converter.md
---

# Right-Size a Goal That's Too Big to Start or Too Small to Pull

**Objective:** Diagnose whether a goal is oversized (never starts) or undersized (no traction), then rewrite it to the one size that fits the user's real weekly capacity and horizon — a size they will actually begin and sustain.

**When to use:** A goal keeps intimidating you into not starting; or a goal is so small it generates no momentum and you keep dropping it; or a `goals_progress_stall_diagnostic.md` run pointed to "wrong size." Not for a goal that's the right size but blocked by a competing goal (see `goals_goal_conflict_resolver.md`) or by a missing next action alone (see `agency_next_action_spec.md`).

**Audience:** An individual re-sizing their own goal. Not for scoping work assigned to someone else, and not clinical. If the inability to start persists across most goals and areas of life and comes with distress, that pattern is beyond a sizing tool — see `domain-psychology/`.

---

## Inputs Required

1. **The goal as currently stated**, with its current implied horizon (weeks/months).
2. **The sizing symptom.** Which is happening: (a) never starts / keeps getting deferred / feels overwhelming, or (b) starts easily but generates no traction, gets forgotten, feels not worth tracking.
3. **Real weekly capacity for this goal.** Honest discretionary hours per week available *specifically for this goal* after existing commitments — a number, and how reliably it appears.
4. **Horizon.** How long the user is genuinely willing to sustain effort on this before needing a visible result.
5. **The smallest version that would still matter**, in the user's own words — and the largest version they're secretly hoping for.
6. **Track record on similar goals.** How past goals of this type went — completed, abandoned, and at roughly what size.

If input 3 is "as much as it takes" or otherwise unquantified, refuse and ask for a real number. Sizing against imagined capacity reproduces the original fault.

---

## Instructions

### Step 1 — Confirm the sizing fault and rule out impostors
From input 2, name the fault: **oversized** or **undersized**. Then rule out the two things that masquerade as sizing problems:
- If the goal never starts but the real reason is a competing goal eating the capacity → it's a conflict, route to `goals_goal_conflict_resolver.md`.
- If the goal never starts but the real reason is no atomic next action → route to `agency_next_action_spec.md`.
Only proceed if the fault is genuinely size: the goal's *magnitude relative to capacity* is what breaks it.

### Step 2 — Compute the capacity-horizon envelope
Multiply input 3 (reliable weekly hours) by input 4 (horizon) to get the realistic total effort available before a result is needed. This is the envelope the goal must fit. State it as a number (e.g., "~6 reliable hrs/week × 10 weeks ≈ 60 hours of real work").

### Step 3 — Run the dual-failure sizing test
Test the current goal against both failure modes at once:
- **Too big:** Does completing it plausibly exceed the Step 2 envelope? Does the first meaningful milestone sit more than ~1–2 weeks out? Either makes it oversized.
- **Too small:** Would completing it change nothing the user would notice or track? Does it fail to build toward anything? Either makes it undersized.
A well-sized goal fails *neither* test. State the result for both explicitly.

### Step 4 — Rewrite to the fitting size
Rewrite the goal to fit the envelope:
- **If oversized:** carve out the largest coherent chunk that fits the envelope and delivers a visible result — a real milestone, not a fragment. The rest becomes a *later* goal, explicitly parked (route to `goals_skill_breakdown_blueprint.md` if it's a skill needing decomposition). Anchor to input 5's "smallest version that still matters" as the floor.
- **If undersized:** raise the goal to the smallest version that produces noticeable traction and builds toward the larger hope in input 5 — enough that progress is worth tracking and generates pull.
Cross-check the rewrite against input 6: if the new size matches a size the user has abandoned before, adjust once more toward the size they've historically completed.

### Step 5 — Set the first-milestone timing
Specify when the first visible milestone lands under the new size — for an oversized rewrite this should be within ~1–2 weeks. If it can't be, the goal is still too big; carve again. This near milestone is what makes the goal startable.

### Step 6 — Output the resize and its traction check
Produce the before/after goal statement and state what should be observably true within 1–2 weeks that proves the new size took (started and produced a first result). Name the single sign that it's *still* mis-sized so the user can catch a bad resize early.

---

## Constraints

### Must
- Name the fault as oversized or undersized and rule out the two impostor causes.
- Compute the capacity-horizon envelope as a number.
- Run the dual-failure test and report both results.
- Rewrite to a size that fails neither test and fits the envelope.
- Cross-check the new size against the user's completion track record.
- Set a near first milestone (≤ ~2 weeks for oversized rewrites) and a traction check.

### Must Not
- Resize against unquantified or fantasy capacity.
- Shrink an oversized goal into a meaningless fragment (below input 5's floor).
- Inflate an undersized goal past the envelope just to feel ambitious.
- Return two sizes and ask the user to pick — deliver one.
- Moralize about the user's difficulty starting or finishing.
- Recommend a generic "break it into steps" without fitting the envelope.

---

## False-Positive Prevention

1. **Don't treat every "won't start" as oversized.** A competing goal or a missing next action produces the same symptom. Rule them out in Step 1 before resizing.
2. **Don't shrink into a fragment.** An oversized goal cut below the "smallest version that still matters" (input 5) trades one failure for another — now it's undersized. Hold the floor.
3. **Don't inflate for ambition's sake.** An undersized goal raised past the real envelope becomes oversized. Raise only to the traction threshold, not to the secret hope.
4. **Don't size to peak-week capacity.** Use *reliable* weekly hours (input 3), not the one good week. Reliability, not maximum, sets the envelope.
5. **Don't ignore the track record.** A rewrite that lands at a size the user has repeatedly abandoned will be abandoned again regardless of the math. Weight input 6.
6. **Don't confuse a distant milestone with a sized goal.** If the first visible result is 6 weeks out, the goal is still too big even if the total fits the horizon — startability needs a near win.

---

## Output Format

```
## Sizing fault
Fault: [oversized / undersized]
Impostor causes ruled out: [conflict? next-action? — results]

## Capacity-horizon envelope
~[N] reliable hrs/week × [horizon] ≈ [total hours of real work available].

## Dual-failure test (current goal)
Too big? [yes/no — why]
Too small? [yes/no — why]

## Resize
Before: [current goal]
After: [rewritten goal, fits envelope, above the "still matters" floor, matched to completion track record]
Parked for later (if oversized): [the carved-off remainder].

## First milestone
Visible result by [date, ≤ ~2 weeks if oversized]: [what lands].

## Traction check (1–2 weeks)
Proof the size took: [observable — started + first result].
Sign it's still mis-sized: [one early warning].
```

---

## Verification

- [ ] Fault named as oversized/undersized; conflict and next-action impostors ruled out.
- [ ] Capacity-horizon envelope computed as a number from reliable (not peak) hours.
- [ ] Dual-failure test run with both results reported.
- [ ] One rewritten goal that fails neither test and respects the input-5 floor.
- [ ] New size cross-checked against the completion track record (input 6).
- [ ] A first visible milestone ≤ ~2 weeks (for oversized) and a traction check with early-warning sign.
- [ ] One size delivered, not a menu; no moralizing; no generic "break it into steps."
