---
title: "Derive One or Two Goals From Your Operating Values"
category: personal-development/goals
description: "Take the user's already-surfaced operating values and derive 1–2 concrete, observable goals that close the gap between what they value and what they're actually doing. Defers the values-surfacing itself to identity_values_clarification.md; this prompt only builds the values→action bridge."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DD-02
  - DS-06
difficulty: intermediate
tags:
  - goals
  - values
  - values-to-action
  - derivation
  - alignment
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/identity/identity_values_clarification.md
  - domain-personal-development/prompts/goals/goals_annual_planning_and_theme.md
  - domain-personal-development/prompts/goals/goals_goal_system_designer.md
  - domain-personal-development/prompts/agency/agency_project_ownership_converter.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Derive One or Two Goals From Your Operating Values

**Objective:** Convert 1–2 of the user's operating values into concrete, observable goals that close a specific values-to-action gap — building the bridge from value to behavior, not re-surfacing the values.

**When to use:** You have already identified what you value (via `identity_values_clarification.md` or otherwise) but your calendar and choices don't reflect it, and you want a goal that actually enacts a value rather than a goal chosen for status or habit. Not for figuring out *what* you value in the first place — do that first with `identity_values_clarification.md` — and not for building a full multi-goal system (see `goals_goal_system_designer.md`).

**Audience:** An individual translating their own values into action. Not for prescribing values to someone else, and not clinical. If confronting the values-to-action gap surfaces persistent distress or a sense of a wasted life that won't lift, that is out of scope — see `domain-psychology/`.

---

## Inputs Required

1. **Operating values, already surfaced.** 3–6 values the user has genuinely identified as theirs — ideally the *revealed/operating* values output of `identity_values_clarification.md`, not a generic word list. If the user hasn't done this, stop and route them to that prompt first.
2. **Current enactment evidence.** For each value, how it currently shows up (or doesn't) in the last 30 days — hours, money, decisions. Where is the value already lived, and where is it merely claimed?
3. **The value with the widest gap.** The user's read on which value has the biggest distance between how much it matters and how little it currently shapes their life.
4. **Real weekly capacity.** Discretionary hours per week and rough money available to redirect toward a goal.
5. **Constraints and non-negotiables** that any derived goal must respect (existing commitments, health, relationships).

If input 1 is a list of generic value words with no grounding in the user's actual decisions, refuse and route to `identity_values_clarification.md`. This prompt builds on surfaced values; it does not manufacture them.

---

## Instructions

### Step 1 — Confirm the values are operating values, not aspirations
Check input 1 against input 2. A value that shows up nowhere in 30 days of evidence may be aspirational rather than operating. Flag any such value; do not derive a goal from a value the user only wishes they held (that inverts the whole point — the goal would be borrowed, not owned). Proceed with values that have at least some enactment footprint or a clearly felt, specific pull.

### Step 2 — Locate the widest actionable gap
Take input 3 and confirm or correct it using input 2's evidence: which value has the largest gap between stated importance and current enactment *and* is movable by the user's own action within their capacity (input 4)? A value blocked entirely by factors outside the user's control is not a good goal source this period; note it and pick the widest *actionable* gap.

### Step 3 — Translate the value into an observable behavior
Values are directions; goals are destinations you can watch yourself reach. Using vague-to-concrete translation, convert the chosen value into 1–2 candidate goals stated as observable states or completed actions. Test each candidate: "If I reached this, would an outside observer see the value enacted?" If the goal could be completed while the value stayed unlived, it's the wrong goal — rewrite it.

### Step 4 — Size to capacity and constraints
Fit each candidate goal to input 4's real hours/money and input 5's non-negotiables. A values-derived goal that ignores capacity fails the same way any oversized goal does. If the honest-sized version is small, keep it small — a small enacted value beats a large unlived one.

### Step 5 — Attach the first enacting action
For the chosen goal, specify the first physical, time-bounded action that enacts the value this week — a calendar block, a spending redirect, a conversation, a started artifact. This is where values-to-action gaps usually die; make the first step concrete enough to do without further planning. (Chain to `agency_next_action_spec.md` if the action itself needs decomposition.)

### Step 6 — Output the derivation and its check
Produce the value → gap → goal → first-action chain explicitly so the user can see the derivation, and state what should be observably different in 2 weeks if the value is now actually shaping behavior.

---

## Constraints

### Must
- Build only on surfaced operating values (input 1); route out if they're generic.
- Derive at most 2 goals — ideally 1.
- State every goal as an observable state/action an outsider could verify.
- Size goals to real capacity and constraints.
- Attach a concrete first enacting action for this week.

### Must Not
- Surface or invent values — that belongs to `identity_values_clarification.md`.
- Derive a goal from a value with zero enactment footprint and no specific felt pull.
- Produce a goal that could be completed while the value stayed unlived.
- Output more than 2 goals or a full multi-goal system (route to `goals_goal_system_designer.md`).
- Use aspirational value-words as if they were operating values, or add affirmations.

---

## False-Positive Prevention

1. **Don't derive from an aspirational value.** A value with no footprint in 30 days of evidence is a wish. Deriving a goal from it produces a borrowed goal that won't hold. Flag and skip in Step 1.
2. **Don't accept a goal that leaves the value unlived.** "Read 12 books on generosity" can be completed with zero generosity enacted. The observer test in Step 3 catches this.
3. **Don't pick a gap the user can't move.** The widest gap may be blocked by external factors; derive from the widest *actionable* gap instead.
4. **Don't inflate the goal to match the value's importance.** A deeply held value does not license an oversized goal. Size to capacity; a small enacted value wins.
5. **Don't collapse two values into one muddy goal.** If two values pull toward different goals, derive separately or pick one — don't average them into something that serves neither.
6. **Don't restate the value as the goal.** "Be more present" is a value restated, not a goal. It must become an observable behavior.

---

## Output Format

```
## Values check
Operating values used: [from input 1, confirmed against evidence]
Flagged as aspirational (not used): [any values with no footprint]

## The gap
Widest actionable gap: [value] — matters [high], currently enacted [low], because [evidence from input 2]. Movable by your action: [yes, within capacity].

## Derivation
Value → Goal
[Value] → [observable goal, sized to capacity]
(Optional second: [Value] → [goal])

Observer test: an outsider reaching this goal would see [the value enacted] — passes.

## First enacting action (this week)
[Specific physical, time-bounded action.]

## Two-week check
If this value is now shaping behavior, the following is observably different: [specific observable].
```

---

## Verification

- [ ] Only surfaced operating values used; generic lists routed to `identity_values_clarification.md`.
- [ ] At most 2 goals derived, each observable and outsider-verifiable.
- [ ] The chosen gap is the widest *actionable* one, confirmed against evidence.
- [ ] Each goal passes the observer test (can't be completed while value stays unlived).
- [ ] Goals sized to real capacity and constraints.
- [ ] A concrete first enacting action for this week is attached.
- [ ] No values invented, no aspirational values used, no affirmations.
