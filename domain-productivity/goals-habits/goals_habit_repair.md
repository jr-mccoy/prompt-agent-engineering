---
title: "Habit Repair"
category: productivity/goals-habits
description: "Diagnose why a previously maintained habit broke down and design a specific re-entry smaller than the maintained version."
techniques:
  - ST-01
  - ST-03
  - DS-01
  - CM-02
  - QA-01
  - RT-06
  - AG-11
difficulty: beginner
tags:
  - habits
  - behavior-design
  - habit-repair
  - re-entry
  - diagnosis
updated: "2026-05-12"
related_prompts:
  - domain-productivity/goals-habits/goals_habit_stack_designer.md
  - domain-productivity/goals-habits/goals_personal_tracking_dashboard.md
  - domain-productivity/bottlenecks/bottleneck_procrastination_systems_diagnostic.md
  - domain-personal-development/prompts/agency/agency_habit_loop_repair.md
  - domain-personal-development/prompts/agency/agency_stuck_diagnosis.md
---

# Habit Repair

**Objective:** Diagnose why a habit that was previously maintained has broken down and design a specific re-entry plan. The re-entry version is always smaller than what was maintained — no willpower surges. Produces a diagnosis, a re-entry habit design, a start date, and a 7-day tracking commitment.

**When to use:** When someone was doing a habit consistently, stopped, and hasn't restarted — and the gap has lasted more than a few days. Not for habits that were never properly established (use `goals_habit_stack_designer.md`). Not for habits someone wants to build for the first time.

**Audience:** Anyone who previously maintained a habit and let it lapse — fitness routines, writing practice, meditation, learning habits, journaling. Not for habits abandoned by intentional decision (if the person decided to stop, this is not a repair situation). Not for organizational or team habits.

---

## Inputs Required

1. **The habit.** What was the habit, specifically? How often (daily, weekdays, 3x/week)? How long per session?
2. **How long it was maintained.** Weeks, months, years? A habit maintained for 6 months is different from one maintained for 10 days.
3. **When and how it broke.** What was the specific event or period that disrupted it? Travel, illness, a big work project, a personal event, a schedule change? If it just gradually faded without a clear event, say that — it's its own failure mode.
4. **How long it's been since they last did it.** Days, weeks, months.
5. **What re-starting feels like.** Ask the user to rate re-entry effort on a simple scale: easy (could do it today), effortful (would take some push), or impossible (feels completely blocked right now). This calibrates the re-entry design.

---

## Instructions

### Step 1 — Diagnose the breakdown

Identify which part of the habit loop broke. Choose the primary failure mode:

**Anchor disappeared:** The existing habit the new one was attached to changed or disappeared (e.g., stopped going to the gym where the habit lived, morning routine changed after returning from travel).

**Cue broke:** The trigger that initiated the habit stopped functioning — the environment changed, the reminder was lost, or the cue became associated with something else.

**Routine became too effortful:** The habit grew beyond its sustainable form — escalated duration, added complexity, or the person's life circumstances changed so that the original version became effortful where it once wasn't.

**Identity disruption:** A major life change (new job, move, relationship change, health event) created a gap in identity continuity — the person stopped being "someone who does this."

**Motivation drop:** The person stopped seeing the point. Important note: motivation is a symptom, not a cause. If this is identified, ask what changed — the habit stopped producing a valued outcome, a competing priority grew, or the goal the habit served changed.

**Gradual fade without trigger:** The habit declined slowly over weeks without a discrete event. This usually indicates the habit was never deeply automated — it was maintained by active intention, which eventually depleted.

State the primary diagnosis. If multiple apply, name the primary and secondary.

### Step 2 — Design the re-entry

Re-entry must be smaller than the maintained version — always. No exceptions for enthusiasm or good intentions. The reason: the psychological cost of a lapsed habit includes shame and self-doubt, which raises the activation energy for re-entry. A smaller target reduces that barrier.

**If maintained version was [X], re-entry version is [X ÷ 2] or less.**

Examples:
- Maintained 20-minute runs → Re-entry is a 10-minute walk/jog
- Maintained 500 words/day → Re-entry is 150 words/day or one paragraph
- Maintained daily meditation, 15 minutes → Re-entry is 5 minutes

Additionally:
- Re-anchor to an existing reliable daily behavior (not the same anchor if that anchor broke)
- Re-establish the cue explicitly — don't assume the trigger will reassert itself
- Define the exact context: where, when, what precedes it

### Step 3 — Set a specific start date and anchor

Name the exact day the re-entry begins (not "this week" or "soon" — a specific date). Name the exact anchor the re-entry habit attaches to. These must be specific enough that the person could tell you whether they did them.

### Step 4 — Design the 7-day tracking commitment

Produce a simple 7-day check-in structure. The only questions that matter for the first 7 days:
1. Did the anchor happen? (yes/no)
2. Did the re-entry habit happen after the anchor? (yes/no)
3. Any friction or obstacle? (note it, don't fix it yet — just observe)

The goal of the first 7 days is to get 5–7 successful completions, not to return to full maintained intensity. After 7 days, a reassessment determines whether to stay at re-entry level or begin gradually scaling up.

### Step 5 — Name the re-break risk
Based on the diagnosed failure mode, name the most likely way this re-entry will break again. Not generic — specific to the diagnosis and context. Produce a single pre-planned response: if [specific thing happens], the plan is [specific action, not "try to keep going"].

---

## Constraints

### Must
- Diagnose the failure mode before designing re-entry — not the other way around
- Set re-entry version below the maintained version — no exceptions
- Produce a specific start date (not "this week")
- Name the re-anchor behavior explicitly from the person's actual current routine
- Include a 7-day tracking commitment with defined check-in questions

### Must Not
- Prescribe returning to the full maintained version immediately
- Use motivation or willpower as a re-entry mechanism
- Recommend a tracking app as the solution — produce the tracking design, not the tool
- Leave the re-break risk unnamed
- Suggest starting at the maintained version "just to see if you can"

---

## False-Positive Prevention

1. **Re-entry at maintained intensity:** The most common failure — starting back at the full version because enthusiasm is high at re-entry. High-enthusiasm re-entries almost always lead to re-breaks within 2 weeks. The re-entry version must be structurally smaller.
2. **Motivation diagnosis without root cause:** Identifying "motivation dropped" as the cause without asking what changed to cause it. Motivation is a signal — it points at something else: a changed goal, a changed outcome, a competing priority. Find the underlying cause.
3. **Gradual-fade misdiagnosis:** Treating a gradual fade as an anchor problem when it's actually a sign the habit was never automated — it was maintained by active intention that eventually depleted. The re-entry design must address this by building in a stronger environmental cue, not just re-establishing the old anchor.
4. **Vague start date:** "Starting Monday" or "this week" — not acceptable. The start date must be a specific calendar date that the person commits to.
5. **Re-break risk that's generic:** "You might get busy again" is not a named risk — it's a non-answer. The risk must be specific to the diagnosed failure mode and this person's context.

---

## Output Format

```
HABIT REPAIR PLAN
Habit: [Habit name and original maintained form]
Generated: [Date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DIAGNOSIS

Maintained for:    [Duration]
Broke on/around:   [Specific event or period, or "gradual fade"]
Gap since last done: [Duration]
Re-entry effort felt: [Easy / Effortful / Impossible]

Primary failure mode:   [Anchor disappeared / Cue broke / Routine too effortful /
                         Identity disruption / Motivation drop / Gradual fade]
Secondary (if any):     [Same options]

Diagnosis: [2–3 sentences explaining specifically what broke and why]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RE-ENTRY DESIGN

Maintained version:   [What they were doing — frequency, duration, form]
Re-entry version:     [Reduced form — ≤ half of maintained]

Re-anchor:   [Specific existing daily behavior to attach to]
Cue:         [Explicit transition moment — "immediately after X"]
Context:     [Where and when this happens]

Full sentence: "After I [anchor], I will immediately [re-entry version of habit]."

Start date: [Specific calendar date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

7-DAY TRACKING COMMITMENT (Days 1–7)

Each day, note:
  □ Day [1–7]: Anchor happened? [Y/N] | Habit happened? [Y/N] | Friction noted: ___

Day-7 check-in questions:
  1. How many of 7 days did the habit run? (target: ≥5)
  2. Is the anchor still reliable?
  3. Is the re-entry version too easy, right-sized, or still effortful?
  4. Ready to scale up, or stay at re-entry level for another week?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RE-BREAK RISK

Most likely re-break scenario: [Specific to diagnosis and context]
Pre-planned response:          [Specific action — not "try to keep going"]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Verification

- [ ] Failure mode is diagnosed before the re-entry is designed
- [ ] Re-entry version is explicitly smaller than the maintained version
- [ ] Start date is a specific calendar date — not a week or a general timeframe
- [ ] Re-anchor is a specific existing daily behavior from the user's current routine
- [ ] 7-day tracking structure includes defined yes/no questions (not open-ended journaling)
- [ ] Re-break risk is specific to this person's failure mode — not generic
- [ ] Motivation, if identified, is traced to an underlying cause
- [ ] No tracking app was recommended as the deliverable
