---
title: "Diagnose Why a Goal Isn't Moving and Prescribe One Unblock"
category: personal-development/goals
description: "For a goal that has stopped moving, classify the stall against a fixed 6-cause taxonomy (wrong goal / wrong size / no next action / capacity / motivation / hidden conflict) using the user's evidence, then prescribe the single unblock move that fits the diagnosed cause."
techniques:
  - ST-01
  - ST-02
  - RT-09
  - DS-01
  - QA-12
difficulty: intermediate
tags:
  - goals
  - stall-diagnosis
  - unblocking
  - root-cause
  - progress
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-personal-development/prompts/goals/goals_scope_right_sizer.md
  - domain-personal-development/prompts/goals/goals_goal_conflict_resolver.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
  - domain-personal-development/prompts/resilience/resilience_motivation_diagnosis.md
---

# Diagnose Why a Goal Isn't Moving and Prescribe One Unblock

**Objective:** Classify why a specific goal has stalled against a fixed 6-cause taxonomy, name the single dominant cause from the user's evidence, and prescribe exactly one unblock move — not a checklist of possible fixes.

**When to use:** A goal you still care about has produced no visible progress for weeks; you keep meaning to work on it and don't; you can't tell whether the problem is the goal, the plan, or you. Not for a goal you've decided to drop, and not for pure in-the-session execution paralysis on a task (see `agency_stuck_diagnosis.md`, which this cross-links).

**Audience:** An individual diagnosing their own stalled goal. Not for evaluating someone else's progress, and not clinical. If the stall coincides with persistent low mood, loss of interest across most of life, or exhaustion that rest doesn't fix, that pattern is beyond a goal diagnostic — see `domain-psychology/` and a licensed professional.

---

## Inputs Required

1. **The stalled goal.** Stated as an observable outcome, with when it was set and when progress last happened.
2. **The stall window.** How long it's been stuck, and what "stuck" looks like concretely (no action taken? action taken but no result? repeated restarts?).
3. **Last 3 attempts to move it.** For each: what the user actually did or tried to do, and what stopped them — as specifically as possible.
4. **Current next action, as the user understands it.** The literal next thing they believe they need to do. If they can't state one, note that.
5. **Competing demands.** What else is drawing on the same time/energy right now.
6. **Honest interest read.** On a plain 1–5, how much the user actually wants this goal now vs. when they set it — and why, in one line.

If the user supplies only "I'm not making progress" with no detail on inputs 3, 4, and 6, refuse and ask. The cause cannot be found without the attempt history and the interest read.

---

## Instructions

### Step 1 — Classify the stall against the fixed taxonomy
Map the evidence to exactly one dominant cause. All six are distinct; do not blend them:

| # | Cause | Signature in the evidence | Primary unblock family |
|---|---|---|---|
| 1 | Wrong goal | Interest read (input 6) has genuinely dropped; the goal no longer serves a current value | Drop, downgrade, or re-derive it |
| 2 | Wrong size | Every attempt stalls at the same overwhelmed/underwhelmed point; goal too big to start or too small to pull | Re-size it |
| 3 | No next action | User can't state a concrete next step (input 4), or the "next step" is actually a project | Decompose to one atomic action |
| 4 | Capacity | Real interest and clear next step, but no time/energy exists for it (input 5 saturates the budget) | Free capacity or sequence |
| 5 | Motivation | Interest is real but activation keeps failing at the same emotional point (dread, avoidance) | Address the activation barrier |
| 6 | Hidden conflict | A second goal or unnamed cost is silently competing; progress here means loss elsewhere | Surface and resolve the conflict |

State the dominant cause in one sentence, citing which inputs point to it. If two causes seem present, name the *upstream* one — the one that, if fixed, dissolves the other (e.g., a "no next action" that's really a "wrong size").

### Step 2 — Rule out the two most common misdiagnoses
Before finalizing, actively check:
- Is a claimed "motivation" (5) actually a "wrong goal" (1)? If the interest read is genuinely low, it's cause 1, not a willpower problem.
- Is a claimed "capacity" (4) actually a "hidden conflict" (6)? If time exists but keeps going elsewhere by choice, it's a conflict, not a shortage.

Correct the classification if either check fires.

### Step 3 — Prescribe the one unblock move
From the diagnosed cause's unblock family, prescribe a single, physical, time-bounded move — and route to the matching sibling prompt where one exists:
- Cause 1 → decide: drop / downgrade / re-derive (route to `goals_values_to_goals_derivation.md` if re-deriving).
- Cause 2 → route to `goals_scope_right_sizer.md`.
- Cause 3 → route to `agency_next_action_spec.md`; specify the atomic action here.
- Cause 4 → free a specific block or sequence behind another goal.
- Cause 5 → route to `resilience_motivation_diagnosis.md` or `agency_stuck_diagnosis.md`; name the smallest activation step.
- Cause 6 → route to `goals_goal_conflict_resolver.md`.

One move. Not "here are options for each cause."

### Step 4 — Set the movement check
State what should be observably true within one week if the diagnosis was correct and the move worked. If that observable doesn't appear, the diagnosis was wrong — name the second-most-likely cause to try next.

---

## Constraints

### Must
- Assign exactly one dominant cause from the fixed 6-type taxonomy.
- Cite specific inputs supporting the classification.
- Run the two misdiagnosis checks in Step 2.
- Prescribe exactly one unblock move, physical and time-bounded, with a route to the matching sibling prompt.
- Set a one-week observable movement check and name the fallback cause.

### Must Not
- Return more than one cause as "the answer," or a menu of fixes.
- Diagnose "motivation" when the interest read is genuinely low (that's wrong goal).
- Treat dropping the goal as failure — for cause 1 it's the correct move.
- Add a new productivity system or tool as the unblock.
- Moralize about the stall or attribute it to a character flaw.
- Cross the line into diagnosing depression, ADHD, or other conditions.

---

## False-Positive Prevention

1. **Don't default to "motivation."** It's the flattering cause (implies the goal is right, only willpower failed). Only assign it when interest is genuinely present and the failure is at the activation point — otherwise it masks wrong-goal or wrong-size.
2. **Don't accept the user's stated next action at face value.** A "next action" that is really a multi-step project is a cause-3 (no atomic next action) in disguise — the plan feels ready but isn't.
3. **Don't call it capacity when time exists but goes elsewhere.** A budget spent by choice on other things is a hidden conflict, not a shortage.
4. **Don't diagnose the goal as wrong just because it's hard.** A steep but still-wanted goal is size or motivation, not wrong goal. Use the interest read, not the difficulty.
5. **Don't stack causes.** Naming three causes is the same as naming none. Find the upstream one.
6. **Don't medicalize a stall.** A single stuck goal is not evidence of a disorder; keep the diagnosis at the goal level and route persistent cross-life patterns to `domain-psychology/`.

---

## Output Format

```
## Stall diagnosis
Dominant cause: [#N — name] (upstream of: [other cause, if relevant])
Evidence: [specific inputs pointing here].

## Misdiagnosis checks
Motivation-vs-wrong-goal: [result]
Capacity-vs-hidden-conflict: [result]

## The one unblock move
[Single physical, time-bounded move.] → routed to: [sibling prompt, if any].

## One-week movement check
If the diagnosis is right, by [date] you'll observe: [specific observable].
If that doesn't appear, next-most-likely cause to try: [#N — name].
```

---

## Verification

- [ ] Exactly one dominant cause assigned from the fixed 6-type taxonomy.
- [ ] Classification cites specific inputs.
- [ ] Both misdiagnosis checks (Step 2) were run and reported.
- [ ] Exactly one unblock move, physical and time-bounded, with a sibling-prompt route.
- [ ] A one-week observable movement check plus a named fallback cause.
- [ ] "Motivation" not assigned where the interest read is genuinely low.
- [ ] No menu of fixes, no new systems, no moralizing, no clinical diagnosis.
