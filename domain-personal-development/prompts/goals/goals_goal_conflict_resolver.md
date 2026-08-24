---
title: "Resolve Two Goals Competing for the Same Finite Resource"
category: personal-development/goals
description: "When two or more real goals compete for the same finite resource (time, money, energy, or attention), surface the true conflict, quantify the shared scarce resource, and force a decision: rank one above the other or sequence them — not a fantasy of doing both."
techniques:
  - ST-01
  - ST-02
  - RT-05
  - DS-06
  - CM-02
difficulty: intermediate
tags:
  - goals
  - goal-conflict
  - prioritization
  - trade-offs
  - sequencing
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/goals/goals_anti_goals_avoidance_list.md
  - domain-personal-development/prompts/goals/goals_scope_right_sizer.md
  - domain-personal-development/prompts/goals/goals_progress_stall_diagnostic.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
---

# Resolve Two Goals Competing for the Same Finite Resource

**Objective:** Identify the single scarce resource two or more goals are fighting over, quantify the fight, and force one decision — rank or sequence — instead of pretending both can run at full intensity.

**When to use:** You are stalled on two goals at once and suspect they're undermining each other; you keep switching between them without finishing either; you have a "do both" plan that quietly assumes more time/money/energy than exists. Not for a single stuck goal with no competitor (see `goals_progress_stall_diagnostic.md`) or for a goal that is simply mis-sized (see `goals_scope_right_sizer.md`).

**Audience:** An individual resolving their own competing goals. Not for mediating between other people's goals, and not clinical. If the conflict is driven by a relationship dynamic that feels persistently distressing, that is out of scope — see `domain-psychology/`.

---

## Inputs Required

1. **The competing goals.** 2–4 goals the user believes are in conflict, each stated as an observable outcome with a rough horizon.
2. **The suspected shared resource.** The user's guess at what they're fighting over: time, money, energy, or attention. (Confirmed or corrected in Step 1.)
3. **Real weekly budget of each resource.** Discretionary hours per week, discretionary dollars per month, and a rough energy read (how many genuinely focused blocks per week the user has). Numbers, not "some."
4. **What each goal currently consumes** of that resource, best estimate.
5. **Each goal's cost of delay.** For each goal: what specifically gets worse, and how fast, if it waits 3–6 months. Required — this is what separates rank from sequence.
6. **Any hard deadline or external dependency** on either goal.

If the user supplies only "I want to do both and can't," refuse to proceed until inputs 3, 4, and 5 are filled. The conflict cannot be resolved without the numbers.

---

## Instructions

### Step 1 — Confirm the true scarce resource
Goals often appear to conflict over time when they actually conflict over energy or attention (two goals fit the calendar but both need the same 2 fresh morning blocks). Using inputs 3 and 4, identify which single resource is actually binding. Name it. If two resources bind at once, name the tighter one and note the second.

### Step 2 — Quantify the overrun
Sum what the goals demand of the binding resource (input 4) against what exists (input 3). State the gap as a number: "the two goals demand ~18 focused blocks/week; you have ~9." If there is no overrun, the goals are not actually in conflict — say so and stop; the real problem is elsewhere (route to `goals_progress_stall_diagnostic.md`).

### Step 3 — Separate rank from sequence using cost of delay
Apply this fixed decision rule to input 5:

| Situation | Decision |
|---|---|
| One goal's cost of delay is steep and time-sensitive; the other's is shallow or flat | **Sequence** — run the steep one now, the shallow one after |
| Both have steep, time-sensitive costs of delay and a hard deadline (input 6) collides | **Rank** — one wins the resource; the other is deliberately reduced or dropped this period |
| Both costs of delay are shallow | **Sequence** — pick either order; the conflict is smaller than it feels |
| The goals share a deadline and neither can move | **Rank** — split is fantasy; forcing both fails both |

### Step 4 — Name what running both actually costs
Make the "do both" option concrete: at the current split, project where each goal lands in 3 months given the Step 2 overrun. This is usually "both half-done, neither shipped." State it plainly so the decision has a real alternative to beat.

### Step 5 — Force one decision
Output either a **rank** (Goal A gets N units of the binding resource, Goal B gets what remains or is paused) or a **sequence** (Goal A now through [trigger/date], then Goal B). Not both goals at full intensity. Attach the specific resource reallocation — the calendar block, the dollar amount, the attention rule — that makes the decision real this week.

### Step 6 — Set the reconsideration trigger
State the one observable condition under which this decision should be revisited (the sequenced goal's cost of delay crossing a threshold, the deadline moving, the binding resource expanding). One trigger, not "check in periodically."

---

## Constraints

### Must
- Identify a single binding resource and quantify the overrun as a number.
- Use cost of delay (input 5) to choose between rank and sequence via the fixed rule.
- Make the "do both" cost concrete before recommending against it.
- Output exactly one decision (rank OR sequence) with a this-week reallocation.
- Set one observable reconsideration trigger.

### Must Not
- Recommend "just balance both" or a 50/50 split when Step 2 shows an overrun.
- Add a third goal or a new time-management system as the answer.
- Moralize about which goal is more worthy — decide on delay cost and resource fit, not virtue.
- Leave the decision as "it's up to you" — force the call from the evidence.
- Recommend generic productivity hacks in place of a resource decision.

---

## False-Positive Prevention

1. **Don't accept the user's named resource without checking.** The stated conflict (time) is frequently a proxy for the real one (fresh-attention blocks). Verify against inputs 3–4 in Step 1.
2. **Don't call it a conflict when there's no overrun.** If demand fits supply, the stall has another cause — route out rather than manufacturing a trade-off.
3. **Don't default to rank because it feels decisive.** Sequencing preserves both goals when only one is time-sensitive; only rank when delay costs collide.
4. **Don't let "do both" stay abstract.** An unquantified "I'll fit both in" always beats a concrete decision in the user's head. Force the 3-month projection.
5. **Don't sequence around a fantasy trigger.** "When things calm down" is not a trigger. Use an observable date or measurable condition.
6. **Don't mistake a mis-sized single goal for a conflict.** If one goal is simply too big for the whole budget regardless of the other, the tool is `goals_scope_right_sizer.md`.

---

## Output Format

```
## The real conflict
Binding resource: [time / money / energy / attention] (second, if any: [x])
Overrun: goals demand ~[N] of [resource]/[period]; you have ~[M]. Gap: [number].

## Cost of delay
| Goal | Cost of delay | Time-sensitive? | Hard deadline? |
|---|---|---|---|
| A | ... | yes/no | ... |
| B | ... | yes/no | ... |

## What "do both" actually costs
At the current split, in 3 months: [concrete projection — usually both half-done].

## Decision (one)
[RANK: Goal A gets [N units]; Goal B [reduced/paused].]
   — or —
[SEQUENCE: Goal A now through [trigger/date], then Goal B.]

This-week reallocation: [specific block / dollar / attention rule].

## Reconsider when
[One observable trigger].
```

---

## Verification

- [ ] A single binding resource named and the overrun stated as a number.
- [ ] Rank-vs-sequence chosen via the fixed cost-of-delay rule, not preference.
- [ ] The "do both" alternative made concrete with a 3-month projection.
- [ ] Exactly one decision output, with a this-week reallocation.
- [ ] One observable reconsideration trigger, not "check in later."
- [ ] No 50/50 split recommended against a documented overrun.
- [ ] No moralizing about goal worthiness; no generic productivity advice.
