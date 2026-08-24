---
title: "Convert a Vague Intention Into Precise If-Then Implementation Intentions"
category: personal-development/habits
description: "Take a fuzzy intention ('I'll exercise more', 'I should reply faster') and translate it into one or more precise if-then implementation intentions anchored to a specific cue, time, and location, plus coping if-thens for the predictable obstacles."
techniques:
  - ST-01
  - ST-02
  - DD-02
  - CM-02
  - QA-12
difficulty: beginner
tags:
  - habits
  - implementation-intentions
  - if-then-planning
  - cue-specification
  - behavior-change
updated: "2026-07-23"
related_prompts:
  - domain-personal-development/prompts/habits/habits_habit_design_blueprint.md
  - domain-personal-development/prompts/habits/habits_identity_based_habit_designer.md
  - domain-personal-development/prompts/habits/habits_environment_design_for_habits.md
  - domain-personal-development/prompts/habits/habits_temptation_bundling_designer.md
  - domain-personal-development/prompts/agency/agency_habit_loop_repair.md
---

# Convert a Vague Intention Into Precise If-Then Implementation Intentions

**Objective:** Translate a vague goal intention into one or more implementation intentions in strict "when [cue], I will [action] [at location]" form — each anchored to a cue that reliably fires — plus a coping if-then for every predictable obstacle, so the behavior is triggered by the situation instead of by remembering or feeling like it.

**When to use:** The user keeps *meaning* to do something and not doing it, or has a goal intention ("get healthier," "network more") with no trigger attached. Use as a focused follow-on when a habit blueprint needs its cues tightened. Not for this: building the whole cue-routine-reward loop or sizing a floor — that is `habits_habit_design_blueprint.md`; this prompt only manufactures the if-then triggers.

**Audience:** An individual doing this for themselves. Not for assessing someone else, not clinical. If the intention is tied to acute distress ("I need this or I'll fall apart"), planning is not mental-health care — see `domain-psychology/` and a licensed professional.

---

## Inputs Required

1. **The vague intention.** In the user's own words ("I want to exercise more," "I should read instead of scroll at night").
2. **The concrete behavior** they believe fulfills it, as an action, not an outcome. If they only have an outcome, ask them to name one action.
3. **Candidate cues.** The times, preceding actions, or places in their day this could attach to. Pulled from their real daily rhythm.
4. **The two or three most likely obstacles.** What actually derails them — a competing pull, a bad mood, a schedule collision, forgetting.
5. **The worst realistic day**, so the cue and action can be tested against it.

If the user offers only the vague intention with no candidate action or no real cues, refuse to fabricate a schedule. Ask for one concrete action and at least two real anchors in their day. An implementation intention with an invented cue is guesswork.

---

## Instructions

### Step 1 — Translate the intention from vague to concrete (DD-02)

Rewrite input 1 as a specific, observable action. "Exercise more" → "do 10 squats." "Reply faster" → "clear the inbox to zero." Strip every comparative ("more," "better," "less") and every outcome word until what remains is a single physical action a camera could record.

### Step 2 — Pick and grade the cue

An implementation intention is only as reliable as its cue. Grade each candidate cue from input 3:

| Cue type | Example | Reliability |
|---|---|---|
| **Preceding action** | "after I pour my morning coffee" | Strongest — it already fires daily and carries its own trigger. |
| **Location** | "when I sit down at my desk" | Strong if the place is daily and singular. |
| **Time** | "at 7:00am" | Only if that clock slot is genuinely stable for this user. |
| **Emotional/state** | "when I feel anxious" | Weak — states are unreliable triggers; use only for coping if-thens, never as the primary cue. |

Choose the strongest available cue. Prefer a preceding action anchored to something that happens on the worst day too.

### Step 3 — Write the primary implementation intention

Produce one sentence in the exact locked form — no softening, no "try to":

> **"When [specific cue], I will [concrete action] [in/at specific location]."**

If the behavior needs to happen more than once a day or in more than one context, write one implementation intention per context (up to three). Do not write a single vague sentence to cover them all.

### Step 4 — Write a coping if-then for each obstacle

For every obstacle in input 4, write a second-order if-then that pre-decides the response before the moment arrives:

> **"If [specific obstacle], then I will [pre-decided response]."**

The response must be concrete and available in the moment — a fallback action, a shrink-to-floor, or a specific re-trigger. "Then I will try harder" is not a coping plan.

### Step 5 — Stress-test against the worst day and lock the set

Re-read input 5. Confirm the primary cue still fires and the action still runs on a bad day; if not, return to Step 2 for a more reliable cue or a smaller action. Then output the final set: primary intention(s) + coping if-thens, as a short rehearsable script the user can read aloud once. End with the single first firing to expect.

---

## Constraints

### Must
- Rewrite the intention into one camera-observable action before writing any if-then.
- Grade the cue and choose the strongest reliably-firing one.
- Write every implementation intention in the exact "when [cue], I will [action] [at location]" form.
- Write one coping if-then per stated obstacle, each with a concrete in-the-moment response.
- Test the primary cue and action against the worst realistic day.

### Must Not
- Leave any comparative or outcome word ("more," "better," "healthier") in the final action.
- Anchor the primary intention to an emotional state.
- Produce a single vague sentence for a multi-context behavior — write one per context.
- Recommend an app, reminder-tool subscription, or notification system as the trigger.
- Moralize about willpower or discipline.
- Provide clinical framing; route distress to `domain-psychology/`.

---

## False-Positive Prevention

1. **Don't let an outcome pose as an action.** "When I wake, I will be more disciplined" has no observable behavior. Force a physical action.
2. **Don't anchor to an unreliable cue.** A time cue for someone with chaotic mornings, or a mood cue, will silently never fire. Grade the cue honestly.
3. **Don't skip the location.** "I will read" is weaker than "I will read in the armchair by the lamp." The physical slot is part of the trigger.
4. **Don't write toothless coping plans.** "If I'm tired, then I'll do it anyway" is not a plan. The response must be a specific, smaller, available action.
5. **Don't over-produce.** Ten if-thens for one behavior is a to-do list, not a trigger set. Cap primary intentions at three contexts.
6. **Don't confuse this with loop design.** If the behavior has no reward and no floor logic, if-thens alone won't sustain it — route to `habits_habit_design_blueprint.md`.

---

## Output Format

```
## Concrete action
Vague intention: [input 1] → observable action: [camera-recordable behavior]

## Cue grade
| Candidate cue | Type | Reliability | Chosen? |
|---|---|---|---|
| ... | Preceding action / Location / Time / State | ... | ... |

## Implementation intention(s)
1. "When [cue], I will [action] at [location]."
2. [only if a second context genuinely exists]

## Coping if-thens (one per obstacle)
- "If [obstacle 1], then I will [pre-decided concrete response]."
- "If [obstacle 2], then I will [...]."

## Worst-day check
On a [worst-day] day, the primary cue still fires and the action still runs because [reason].

## Rehearsal script
[The full set written as 2–4 sentences to read aloud once.]

Next action: expect the first firing at [next time the cue occurs]; run it once and note yes/no.
```

---

## Verification

- [ ] The intention was rewritten into a single camera-observable action with no comparative/outcome words.
- [ ] The cue was graded and the strongest reliably-firing one chosen (not an emotional state).
- [ ] Every implementation intention is in exact "when [cue], I will [action] [at location]" form.
- [ ] Each stated obstacle has a coping if-then with a concrete in-the-moment response.
- [ ] The primary cue and action were tested against the worst realistic day.
- [ ] No more than three primary intentions; no app/notification prescribed as the trigger.
- [ ] No willpower moralizing, no clinical framing.
