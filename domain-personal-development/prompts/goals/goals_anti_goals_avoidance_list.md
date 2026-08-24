---
title: "Define Anti-Goals and Failure States to Protect the Real Goals"
category: personal-development/goals
description: "Define what the user will deliberately NOT pursue this period and the concrete failure states to avoid, then convert each into a guardrail that protects the keystone goals. Outputs an anti-goal list, the failure states, and one tripwire per failure state."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-12
difficulty: intermediate
tags:
  - goals
  - anti-goals
  - failure-states
  - guardrails
  - focus
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/goals/goals_annual_planning_and_theme.md
  - domain-personal-development/prompts/goals/goals_goal_conflict_resolver.md
  - domain-personal-development/prompts/goals/goals_progress_stall_diagnostic.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
---

# Define Anti-Goals and Failure States to Protect the Real Goals

**Objective:** Produce an explicit list of what the user will deliberately not pursue this period, the specific failure states they must avoid, and one tripwire per failure state — so the real goals are protected by named boundaries rather than left exposed to drift.

**When to use:** You have keystone goals set but keep getting pulled off them by shiny opportunities; you tend to over-commit and finish nothing; you want to make a period's *no* list as deliberate as its *yes* list. Best run right after `goals_annual_planning_and_theme.md`. Not for resolving a live conflict between two goals you're already committed to (see `goals_goal_conflict_resolver.md`).

**Audience:** An individual defining their own boundaries. Not for imposing limits on someone else, and not clinical. If the pattern of over-commitment is tied to persistent anxiety or an inability to say no that feels compulsive, that is beyond this prompt — see `domain-psychology/`.

---

## Inputs Required

1. **This period's keystone goals.** The 2–3 outcomes the anti-goals exist to protect (from `goals_annual_planning_and_theme.md` or supplied directly).
2. **The recurring distraction pattern.** 4–8 real examples from the last period of things that pulled the user off their goals: opportunities said yes to, projects picked up mid-stream, commitments that quietly grew, rabbit holes. Each with rough time/energy cost.
3. **Known temptations for the coming period.** Specific things the user can already predict will tempt them (a side project, a new tool to learn, a role someone keeps offering).
4. **Failure states from history.** 2–4 end-states the user has actually reached before and does not want again (e.g., "three projects at 60%, none shipped"; "burned out by month 4"; "money spent on tools instead of the goal").
5. **The user's typical rationalization** for taking on the thing they shouldn't ("but it's related to my goal," "it's only a small commitment").

If inputs 2 and 4 are empty or purely hypothetical, refuse and ask for real history. Anti-goals built from imagined temptations miss the actual leaks.

---

## Instructions

### Step 1 — Extract the leak pattern from history
From input 2, identify how the user actually loses focus. Classify each example against this fixed taxonomy and note which types dominate:

| Leak type | Signature |
|---|---|
| Adjacent-opportunity | "It's related to my goal, so it counts" (it doesn't) |
| Novelty-pull | A new tool/idea/skill more exciting than the current work |
| Scope-creep | A committed thing quietly grew past its original size |
| People-pleasing yes | Said yes to protect a relationship, not to serve a goal |
| Optimization detour | Polishing/researching in place of doing |
| Rescue-reflex | Picked up someone else's dropped ball |

### Step 2 — Write the anti-goals
For each dominant leak type and each item in input 3, write an explicit anti-goal: a specific thing the user will *not* pursue this period, stated as plainly as a goal. Anti-goals are concrete ("I will not start a second newsletter") not vague ("I'll avoid distractions"). Each anti-goal must trace to either a historical leak (input 2) or a predicted temptation (input 3).

### Step 3 — Name the failure states as observable end-states
Take input 4 and sharpen each into an observable state with an early marker — not just "burnout" but "by month 4, working weekends and dreading the goal." For each failure state, name the one measurable sign that it is beginning, drawn from history.

### Step 4 — Convert each failure state into one tripwire
A tripwire is a pre-committed rule that fires on the early marker, before the failure state fully arrives. One per failure state. Format: "IF [observable early marker] THEN [specific corrective action]." Example: "IF I have two goals both under 50% at end of month 2 THEN one gets paused, chosen by cost of delay." The corrective action must be physical and immediate, not "reflect on whether to continue."

### Step 5 — Pre-empt the rationalization
Take input 5 (the user's typical justification) and write the counter-rule that neutralizes it in advance — the sentence the user commits to now so the in-the-moment rationalization doesn't win. One counter-rule, aimed at their specific rationalization.

### Step 6 — Produce the single protective boundary
Of everything above, name the **one** anti-goal or tripwire that protects the most goal-capacity — the boundary that, if held, saves the most focused time/energy for the keystone goals. This is the one to actually enforce; the rest are backup.

---

## Constraints

### Must
- Trace every anti-goal to a historical leak or a predicted temptation.
- Classify leaks against the fixed 6-type taxonomy.
- Give each failure state an observable early marker and exactly one tripwire.
- Write a counter-rule targeting the user's specific rationalization.
- End with one primary protective boundary to enforce.

### Must Not
- Produce vague anti-goals ("avoid distractions," "stay focused") — they must name specific things not to pursue.
- List failure states without early markers — an unobservable failure state can't be caught.
- Write tripwires whose action is reflection rather than a physical move.
- Moralize about the user's leaks or call over-commitment a character flaw.
- Recommend a generic "just say no more" mindset in place of named boundaries.

---

## False-Positive Prevention

1. **Don't disguise a real goal as an anti-goal.** If the "thing not to pursue" is actually one of the keystone goals under stress, that's a conflict — route to `goals_goal_conflict_resolver.md`, don't ban it.
2. **Don't accept "related to my goal" as license.** The adjacent-opportunity leak is the most common and the most self-justifying. Anti-goals must specifically catch it.
3. **Don't confuse a failure state with a bad day.** A failure state is a durable end-state reached over weeks, not a single rough afternoon. Set markers accordingly.
4. **Don't set a tripwire on an unobservable feeling.** "IF I feel unfocused" fires constantly and means nothing. Tie the marker to a countable signal.
5. **Don't over-list.** Twenty anti-goals is a resolution list inverted. Keep to what history and prediction actually support, and name one primary boundary.
6. **Don't ban novelty categorically.** The goal is protecting keystone capacity, not eliminating all new interests — target the specific leaks, not curiosity itself.

---

## Output Format

```
## Your leak pattern (from history)
Dominant leak types: [from taxonomy, with cited examples]

## Anti-goals this period (what you will NOT pursue)
1. [Specific thing not to pursue] — traces to: [historical leak / predicted temptation]
2. ...

## Failure states to avoid
| Failure state (observable end-state) | Early marker | Tripwire (IF marker THEN action) |
|---|---|---|
| ... | ... | IF ... THEN ... |

## Rationalization counter-rule
Your typical justification: "[input 5]"
Counter-rule you commit to now: [one sentence].

## The one boundary to actually enforce
[The single anti-goal or tripwire protecting the most goal-capacity, and why.]
```

---

## Verification

- [ ] Every anti-goal traces to a historical leak or predicted temptation.
- [ ] Leaks classified against the fixed 6-type taxonomy.
- [ ] Each failure state has an observable early marker and exactly one tripwire.
- [ ] Every tripwire action is physical and immediate, not reflective.
- [ ] A counter-rule targets the user's specific rationalization.
- [ ] Exactly one primary protective boundary named.
- [ ] No vague anti-goals, no moralizing, no "just say no" advice.
