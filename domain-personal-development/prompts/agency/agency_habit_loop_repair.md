---
title: "Repair Broken Consistency in a Personal Habit Loop"
category: personal-development/agency
description: "Diagnose why a personal habit the user had been keeping has broken down, choose a repair action sized to the break, and restart without requiring a motivational speech or a new tracking app."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - QA-01
difficulty: beginner
tags:
  - agency
  - habits
  - consistency
  - repair
  - restart
updated: "2026-04-20"
related_prompts:
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
  - domain-personal-development/prompts/agency/agency_rapid_start_mode.md
  - domain-personal-development/prompts/goals/goals_goal_system_designer.md
---

# Repair Broken Consistency in a Personal Habit Loop

**Objective:** When a habit the user had running (daily writing, daily training, weekly review, language practice, meditation, any repeatable self-directed behavior) breaks, diagnose the cause, pick a repair move proportional to the break, and restart without redesigning the habit from scratch.

**When to use:** The user had a habit. They miss it. They can tell you when it broke but not exactly why. They're tempted to either give up on it or design a whole new system — this prompt argues for repair over rebuild.

**Audience:** An individual who has already done the work of building the habit once. The prompt assumes that, not a blank-slate beginner.

---

## Inputs Required

1. **The habit.** What it was, at what cadence, for how long before it broke.
2. **When it broke.** Approximate date or event.
3. **What was happening in life around the break.** Travel, illness, deadline, family, move, seasonal change.
4. **How many attempts to restart the user has made since the break** and what happened to them.
5. **What the user has told themselves about why it broke.** Verbatim.

If the habit only ran a couple of weeks before breaking, it's not a repair problem — it's a design problem; flag that and point to `goals_goal_system_designer.md`.

---

## Instructions

### Step 1 — Size the break

Classify:

- **Hairline:** Missed 1–3 sessions, within a cadence that allowed missing without derailing. Not really broken.
- **Crack:** Missed a chunk (a week, a month), can resume at previous intensity if restarted in a small way.
- **Fracture:** Longer break (1–3 months) or multiple failed restarts. Will need a modified restart, not a resume at full intensity.
- **Reset-class:** Long absence, life structure has changed, old habit design no longer fits. Rebuild, don't repair.

Pick one. The repair move depends on this.

### Step 2 — Identify what broke the habit

Classify the break cause into one of:

- **Context change.** The cue, environment, time-slot, or companion is gone (moved house, new schedule, travel, kid born).
- **Overload.** Life filled up and the habit lost its slot.
- **Scale mismatch.** The habit was sized to high-energy weeks and didn't have a small-version for low-energy weeks.
- **Boredom/decay.** The habit was doing its job but the user lost interest; the purpose got fuzzy.
- **Purpose expired.** The habit's original goal is now achieved or no longer relevant.
- **No-obvious-cause.** Sometimes things drop. Say so rather than inventing a cause.

Pick one. Justify briefly from the user's words.

### Step 3 — Match the repair to the size of the break

| Break size | Repair move |
|---|---|
| Hairline | Do today's session. No meta-work. |
| Crack | Resume at a reduced scale for one week (half the duration, half the difficulty), then return to full. |
| Fracture | Modified restart: smaller scale, different cue, explicit 2-week ramp. Accept it feels awkward. |
| Reset-class | Rebuild — but first, confirm the user actually wants this habit or just the identity of having it. |

Deliver one specific repair move. Not a plan.

### Step 4 — Adjust the design to the break cause

For each break cause, a targeted fix:

- **Context change:** Rebind the habit to a new cue that exists in the new environment.
- **Overload:** Define a minimum-viable version that fits the most overloaded realistic week. The minimum is the real commitment.
- **Scale mismatch:** Explicitly design a floor-version and a target-version. Floor counts as keeping the habit.
- **Boredom/decay:** Reconnect the habit to its purpose, or change the form. If the purpose no longer exists, be honest — the habit may have expired.
- **Purpose expired:** Don't repair. Let it go cleanly, or replace it with the current purpose's habit.
- **No-obvious-cause:** Treat as crack or fracture based on size; don't dig further.

### Step 5 — Define "kept" vs "missed"

Write explicit rules:

- What counts as doing the habit today? (Floor-version.)
- What counts as missing? (e.g., "a full day passed with nothing done" vs "didn't do the full target version").
- What's the make-up rule for missed days? (Often none — the right rule is "don't miss twice in a row" rather than "catch up.")

Writing these rules prevents the silent drift where a missed day becomes two becomes permanent break.

### Step 6 — Identify tomorrow's action

The user's next move is not a plan; it's the first instance of the repaired habit. State the exact time, place, and what the minimum completed version looks like.

---

## Constraints

### Must
- Classify the break size from the fixed set.
- Classify the break cause from the fixed set.
- Size the repair to the break — hairline gets "do today's," not "redesign."
- Define what counts as kept vs missed.
- Give tomorrow's specific instance.

### Must Not
- Recommend a new tracking app, system, or framework.
- Moralize or shame.
- Treat every break as a reset-class problem.
- Design a 30-day or 90-day challenge as the repair.
- Claim the habit will "definitely stick this time." It might not. That's fine.

---

## False-Positive Prevention

1. **Don't over-repair hairline breaks.** Skipping two yoga sessions doesn't require a "restart" ceremony; it requires doing today's session.
2. **Don't confuse loss-of-purpose with failure of will.** Sometimes the habit served something that's now handled. Letting it go is the right move.
3. **Don't repair habits the user has outgrown.** Ask once whether the habit is still wanted, not just habitual-ly missed.
4. **Don't require motivation.** Motivation-based repairs fail on the next low-motivation day. The floor-version is what actually sustains.
5. **Don't add new habits during repair.** The user wants this one back, not three new ones.

---

## Output Format

```
# Habit repair: [habit name]

## Break sizing
[Hairline / Crack / Fracture / Reset-class] — [one-sentence justification]

## Break cause
[Category] — [brief justification from user's words]

## Repair move
[One specific action sized to the break.]

## Design adjustment
[Targeted fix for the identified cause.]

## Kept vs missed (explicit)
- Kept: [floor-version definition]
- Missed: [what counts as missing]
- Make-up rule: [usually none]
- Two-in-a-row rule: [how handled]

## Tomorrow's instance
- When: [specific time]
- Where: [specific place]
- What counts as done: [floor-version]

## Wanted-or-habitual check
[Brief note on whether the user still wants the habit or is chasing the identity of having had it.]
```

---

## Verification

- [ ] Break size and cause came from the fixed taxonomies.
- [ ] Repair move is sized to the break (not a full rebuild on a hairline).
- [ ] Floor-version and target-version are distinct.
- [ ] Make-up rule is defined.
- [ ] Tomorrow's instance is time- and place-specific.
- [ ] No new tracking apps, frameworks, or 30-day challenges.
