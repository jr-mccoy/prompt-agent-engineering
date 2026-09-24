---
title: "Sustainable Wellness Routine — One Week That Holds Training, Eating Rhythm, and Sleep Together"
category: health-wellness/foundations
description: "Fit movement, an eating rhythm, and a sleep anchor into one weekly routine sized to the person's measured capacity: a minimum-viable week that survives a bad week, a standard week, recovery placed on purpose, and a disruption protocol for travel, illness, and crunch periods. Consumes the Readiness Profile; distinct from single-habit design."
techniques:
  - ST-44
  - DS-26
  - ED-04
  - QA-13
difficulty: beginner
tags:
  - health-wellness
  - routine-design
  - weekly-schedule
  - consistency
  - recovery
  - minimum-viable-week
  - keep-falling-off
  - no-spare-time
  - irregular-schedule
updated: "2026-09-24"
related_prompts:
  - domain-health-wellness/foundations/wellness_readiness_and_red_flag_screen.md
  - domain-personal-development/prompts/habits/habits_habit_design_blueprint.md
  - domain-health-wellness/sleep-recovery/sleep_routine_and_environment_audit.md
---

# Sustainable Wellness Routine

**Objective:** Produce one weekly routine that holds training sessions, a regular
eating rhythm, and a fixed sleep anchor inside the hours the person actually has — with
a minimum-viable version that still runs in a bad week.

> **Readiness gate.** Start from a Readiness Profile
> (`foundations/wellness_readiness_and_red_flag_screen.md`). No profile → ask its
> blocks 1–8 first. URGENT-CARE-NOW, CLINICIAN-FIRST, or OUT-OF-SCOPE → stop and
> restate the route. An urgent result means contacting the local emergency number now
> (e.g. 911 in the US). GO-WITH-LIMITS → every limit binds this routine.

**When to Use:**
- You have tried to "get healthy" all at once and it collapsed by week three.
- Training, meals, and sleep each work on paper but fight each other for the same evening.
- Your schedule is irregular (shifts, caregiving, travel) and a fixed plan keeps breaking.
- **Not this prompt if** you want to engineer *one* behaviour's cue and reward — that is
  `domain-personal-development/prompts/habits/habits_habit_design_blueprint.md`. If the
  goal is mood rather than physical health, use
  `domain-psychology/client-self-use/habit-lifestyle/clientself_exercise_as_antidepressant_plan.md`.

## Inputs / Context

1. **Readiness Profile** (or the gate answers).
2. **A real week, logged or recalled:** wake time, work blocks, commute, caregiving,
   fixed commitments, when you currently eat, when you currently sleep.
3. **Hours genuinely available** for training, measured against that week — not hoped for.
4. **What you enjoy or can tolerate** (ED-04): kinds of movement, foods, times of day.
5. **What broke last time**, if anything.
6. **Known disruptions** in the next 3 months: travel, deadlines, shift changes.

## Method

1. **Fix the sleep anchor first.** Choose one wake time held within ~30–60 minutes on
   all seven days where life allows; place bedtime from the sleep need the person
   reports (most adults need 7+ hours). Training and meals fit around this — never the
   reverse, because the routine that steals sleep is the one that collapses.
2. **Set defaults for everything unstated (DS-26).**

   | Parameter | Default | Change when |
   |---|---|---|
   | Training sessions/week | 3 (2 strength-focused, 1 aerobic) | capacity or profile says otherwise |
   | Session length | 30–45 min | measured capacity is less |
   | Hard days in a row | never 2 | experienced and recovering well |
   | Eating rhythm | 3 meals ± 1 planned snack at consistent times | shift work, cultural pattern, clinician advice |
   | Rest days | at least 1 full, 1 light (walk, mobility) | always keep at least 1 |
   | Last hard session | ≥2–3 h before bedtime | it demonstrably does not affect sleep |

3. **Build three tiers (ST-44).** Each must work alone.
   - **Minimum-viable week** — the floor for a bad week: e.g. two 20-minute sessions,
     the wake anchor, and one planned meal a day. Designed to take ≤25% of capacity.
   - **Standard week** — the default, at ≤75% of measured capacity. The 25% slack is
     what absorbs a late meeting without the week failing.
   - **Full week** — only for weeks that open clear; never the plan of record.
4. **Place recovery on purpose.** Put the rest day after the hardest session, not
   wherever the calendar is empty. Pair a light day with the busiest workday.
5. **Hand off the parts.** Session content → `fitness/fitness_beginner_training_plan.md`
   or the endurance build; meal content → `nutrition/nutrition_meal_structure_planner.md`
   (only if the nutrition guard is CLEAR); sleep detail → the sleep audit. This prompt
   owns *when*, not *what*.
6. **Write the disruption protocol (QA-13).** For each known disruption type: which tier
   to drop to, what is kept no matter what (the wake anchor and one session), and the
   rule for coming back (resume at the standard week; do not "make up" missed sessions).
7. **Set the review.** One 10-minute check every 2 weeks: which tier actually ran, and
   whether the standard week needs shrinking. Shrink before you quit.

## Output Format

```
# Weekly routine — [name]
Readiness: [gate result]; limits: [...]

## Anchors
Wake: [time] (all days ±[n] min) | Bedtime target: [time] | Eating times: [...]

## Standard week  ([n] h of [n] h available = [%])
| Day | Morning | Midday | Evening | Type (hard / light / rest) |
|---|---|---|---|---|

## Minimum-viable week  (≤25% of capacity)
[bullets]

## Full week (only when the week opens clear)
[bullets]

## Disruption protocol
| Disruption | Drop to | Never drop | Return rule |
|---|---|---|---|

## Hand-offs
Sessions → [prompt] | Meals → [prompt or "nutrition guard STOP — not run"] | Sleep → [prompt]

## Review
Every [2] weeks: [questions]
```

## Verification

- [ ] The standard week uses ≤75% of measured capacity, and the percentage is shown.
- [ ] The minimum-viable week is genuinely small enough for the worst week named.
- [ ] No two hard days are adjacent unless the profile supports it.
- [ ] The wake anchor is protected in every tier and every disruption.
- [ ] Every GO-WITH-LIMITS limit is visibly applied.
- [ ] Meal hand-off respects the nutrition guard status.

## False-Positive Prevention

1. **Aspirational capacity is not capacity.** "I could train at 5 a.m." is a guess until
   the logged week shows it; build from the log.
2. **Don't make the full week the plan.** A routine that only works in a perfect week
   has a failure date, not a schedule.
3. **Missed sessions are not debt.** Doubling up to catch up is how beginners get hurt
   and how routines end.
4. **Don't stack every change at once.** If the person is starting from nothing, the
   standard week may add movement first and eating rhythm a fortnight later — say so.
5. **Don't borrow sleep to fund training.** A 5 a.m. session that costs an hour of
   sleep is a net loss for most of what the person wants.
6. **Culture and shifts are inputs, not deviations.** A night-shift worker's "morning"
   and a fasting period's meal times are designed around, not corrected.

## Example Output

Scenario: 38, GO, two children, hybrid job, measured ~4 h/week free for exercise,
previous plan (6 sessions/week) collapsed in week 2.

```
# Weekly routine — Sam
Readiness: GO; limits: none

## Anchors
Wake: 06:30 (all days ±30 min) | Bedtime target: 22:45 | Eating: 07:00, 12:30, 18:30

## Standard week  (3.0 h of 4 h available = 75%)
| Day | Morning | Midday | Evening | Type |
| Mon | —            | 30-min walk      | —                      | light |
| Tue | —            | —                | 45-min strength A (19:30) | hard |
| Wed | —            | —                | —                      | rest |
| Thu | —            | —                | 45-min strength B (19:30) | hard |
| Fri | —            | 30-min walk      | —                      | light |
| Sat | 30-min easy run/walk (08:00) | — | —                     | moderate |
| Sun | —            | —                | —                      | rest |

## Minimum-viable week  (40 min ≈ 17%)
- Strength A (20-min version) Tue, 20-min walk Sat; wake anchor held.

## Full week
- Add a 30-min mobility session Sun; only if Mon–Wed ran as planned.

## Disruption protocol
| Disruption | Drop to | Never drop | Return rule |
| Child sick | minimum-viable | wake anchor | resume standard next Monday |
| Work travel | minimum-viable (hotel-room strength A) | 1 session | no make-up sessions |

## Hand-offs
Sessions → fitness_beginner_training_plan | Meals → nutrition_meal_structure_planner | Sleep → sleep_routine_and_environment_audit

## Review
Every 2 weeks: Which tier ran? If standard ran <2 of 2 weeks, cut Sat to 20 min.
```

## Techniques Used

- **ST-44 Progressive Complexity Scaffolding** — minimum-viable, standard, and full weeks,
  each independently workable.
- **DS-26 Safe Defaults Pattern** — a default for every unstated parameter, with when to change it.
- **ED-04 Personalization Hooks** — built from the person's enjoyed activities, foods, and times.
- **QA-13 Failure Recovery Specification** — the disruption protocol and return rule.

## Related Prompts

- `domain-health-wellness/foundations/wellness_readiness_and_red_flag_screen.md` — the gate this consumes.
- `domain-personal-development/prompts/habits/habits_habit_design_blueprint.md` — engineering one
  behaviour inside this routine.
- `domain-health-wellness/sleep-recovery/sleep_routine_and_environment_audit.md` — the sleep anchor in depth.
