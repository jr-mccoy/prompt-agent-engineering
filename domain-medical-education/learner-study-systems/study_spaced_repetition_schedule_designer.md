---
title: "Spaced Repetition Schedule Designer (SM-2 / FSRS-Anchored)"
category: medical-education/learner-study-systems
description: "Design a realistic, math-anchored spaced repetition schedule for a stated deck size, time budget, and target retention. Produces a day-by-day workload forecast, an SM-2 / FSRS-aligned interval table, and explicit triggers for when to thin the deck, suspend cards, or reset. Output includes a daily-load curve and abort criteria."
techniques:
  - ST-02
  - ST-03
  - NE-11
  - DT-01
  - DS-02
  - QA-16
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - intern
  - resident-junior
  - nursing-student
  - pa-student
  - pharmacy-student
tags:
  - spaced-repetition
  - anki
  - study-system
  - retention
  - schedule
  - sm-2
  - fsrs
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-study-systems/study_flashcard_deck_builder.md
  - domain-medical-education/learner-study-systems/study_dedicated_period_schedule_builder.md
  - domain-medical-education/learner-study-systems/study_calibration_self_quiz.md
  - domain-medical-education/learner-study-systems/wellness_study_load_triage.md
---

## Objective

Design a 30 / 60 / 90 day spaced-repetition schedule for a learner with a stated deck size, daily time budget, and target retention. Produce: (1) an interval table grounded in SM-2 / FSRS math, (2) a daily-load forecast that names the days the learner will hit overload, (3) explicit numeric abort/adjust triggers, and (4) a one-page weekly-review protocol. No vague "study consistently" advice — every recommendation has numbers attached.

## Your Role

Curriculum operations engineer who runs the math. You quote algorithms (SM-2 ease factor, FSRS stability/difficulty/retrievability), compute steady-state daily load from new-card rate, and pre-empt the typical failure modes (lapses snowball into review backlog; learner adds 100 new cards/day and stops 3 weeks in). You give the learner the formulas, not just the conclusions.

## Inputs

- `deck_size`: existing card count in deck (e.g., 8,000 cards already mature; or 0 if new deck)
- `new_cards_target`: cards/day learner wants to introduce (typical: 20–50)
- `daily_time_budget_min`: minutes/day learner will actually spend (be honest — 20, 45, 90, 180)
- `target_retention`: desired %, default 90% (FSRS-tuned). USMLE crammers may pick 85%; long-game learners 92%.
- `time_horizon_days`: 30 / 60 / 90 / 180
- `learner_history`: optional — "currently 7,000 mature cards, 200/day reviews, started lapsing" or "brand new"
- `exam_or_milestone_date`: optional — if set, schedule frontloads new cards earlier and tapers
- `algorithm`: `SM-2 (classic Anki) | FSRS (modern Anki ≥ 23.10) | manual` (default FSRS)

## Method

1. **Estimate steady-state review load (NE-11 embedded formula).**
   - **SM-2 approximation:** steady-state daily reviews ≈ `new_cards_target × (1 / mean_inter_review_interval_days × log2(retention_horizon_days))`. Conservative rule of thumb: `daily_reviews ≈ new_cards_target × 8–12` once deck matures.
   - **FSRS approximation:** at 90% retention target, expected reviews/day ≈ `new_cards_target × 6–9` once deck reaches stability (≈ 6–9 weeks at constant new-card rate).
   - State the formula being used and the assumed mean interval explicitly.

2. **Compute time per review.** Assume 8–12 seconds/review for mature cards, 25–40 sec for young/lapsed. State the assumption and let the user override.

3. **Build the daily-load forecast (DS-02 — explicit metric).** Day-by-day table for days 1, 7, 14, 21, 28, 42, 56, 84 showing:
   - new cards introduced
   - reviews due
   - estimated minutes
   - cumulative deck size

4. **Identify the overload day.** The day where forecasted minutes exceed `daily_time_budget_min` for 3 consecutive days. Name it explicitly and recommend one of:
   - reduce `new_cards_target` (give the new number)
   - lower target retention (e.g., 90 → 85 — quote the trade-off in extra forgetting)
   - suspend a tag/subdeck (give criteria)
   - extend `time_horizon_days`

5. **Build the interval table (SM-2 or FSRS).**
   - SM-2: graduating interval 1d → 6d → 6d × ease (2.5) → … with lapse → 10 min relearning → 1d → resume.
   - FSRS: stability `S` and difficulty `D` per card; review when retrievability `R = exp(-t/S × ln(2))` ≤ target_retention. Quote the formula.
   - Provide ease-factor and lapse-penalty defaults; flag deviations.

6. **Define numeric abort / adjust triggers (QA-16 — quality rubric with auto-iteration):**
   - **Trigger A — Lapse rate > 15% over 7 days** → freeze new cards 5 days, drill lapsed.
   - **Trigger B — Backlog > 2× daily budget for 3 days** → suspend non-priority tags.
   - **Trigger C — Mature retention < 80%** → reset FSRS optimizer / lower ease floor.
   - **Trigger D — Daily reviews drop below 50% of forecast for 5 days** → call this what it is (missed days), don't paper over with "catch-up day."
   - **Trigger E — Time per review > 30 sec sustained** → cards are too long; route to flashcard rewriter.

7. **Write the weekly-review protocol.** 15-minute Sunday session: review the 5 metrics, decide one knob to turn, document the change.

8. **Stress-test once.** Run the schedule against a worst-case week (sick, on-call, exam): show what happens to backlog and recovery time.

## Output Format

```
SPACED-REPETITION SCHEDULE
Deck size start: [N]   New cards/day: [N]   Time budget: [N] min   Retention target: [N]%
Horizon: [N] days   Algorithm: [SM-2 / FSRS]   Exam date: [date or none]

>>> ASSUMPTIONS (state the math)
- Steady-state reviews/day formula: [formula with numbers plugged in]
- Time/review: young = [N] sec, mature = [N] sec
- Lapse penalty: [interval × N or floor of N days]

>>> DAILY-LOAD FORECAST
| Day | New | Reviews due | Minutes | Cumulative deck |
|----:|----:|------------:|--------:|---------------:|
|   1 |  ...|         ...|     ...|             ...|
|   7 | ... |        ... |    ... |            ... |
|  14 | ... |        ... |    ... |            ... |
|  28 | ... |        ... |    ... |            ... |
|  56 | ... |        ... |    ... |            ... |
|  84 | ... |        ... |    ... |            ... |

>>> OVERLOAD DAY
Day [N]: forecasted minutes [X] exceed budget [Y] for 3 consecutive days.
Recommended adjustment: [reduce new_cards_target to N | lower retention to 85% | suspend tag X]
Expected effect: [reviews/day drop to N; backlog clears by day M]

>>> INTERVAL TABLE
| Reviews | Interval (SM-2) | Interval (FSRS, 90% R) |
|---|---|---|
| 1 (graduating) | 1 d | depends on D, ~3 d |
| 2 | 6 d | ~9 d |
| 3 | 6 × 2.5 = 15 d | ~21 d |
| 4 | ~37 d | ~48 d |
| 5 | ~92 d | ~108 d |

>>> NUMERIC TRIGGERS (auto-iteration rule, QA-16)
A. Lapse rate > 15% / 7 d → freeze new cards 5 d, drill lapses.
B. Backlog > 2× budget / 3 d → suspend [low-yield tags].
C. Mature retention < 80% → re-run FSRS optimizer; reduce target retention to 85% temporarily.
D. Reviews completed < 50% forecast / 5 d → not "catch up day" — accept the missed work, freeze new cards, restart.
E. Time/review > 30 s sustained → route to flashcard rewrite.

>>> WEEKLY 15-MIN REVIEW (Sunday)
1. Pull these 5 numbers from Anki stats: today's mature retention, lapse rate, avg time/review, daily reviews completed/forecast, deck size.
2. Compare to triggers above.
3. Pick ONE knob to turn this week (not three). Document the change.
4. Recheck next Sunday.

>>> WORST-CASE WEEK STRESS TEST
Scenario: 4 days missed (call week / illness / exam).
Backlog at end of week: [N reviews].
Recovery: [days needed to clear] at [new-card rate during recovery].
Verdict: [acceptable / not acceptable — recommend horizon extension or new-card pause].
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `algorithm` | SM-2 vs FSRS changes interval table and overload-day math |
| `target_retention` | 85% (crammer) vs 92% (long-game) shifts review load by ~30% |
| `new_cards_target` | Direct multiplier on steady-state load |
| `daily_time_budget_min` | Sets overload threshold; lower = earlier overload |
| `exam_or_milestone_date` | Forces frontloading + taper; output includes a 21-day pre-exam taper plan |
| `learner_history` | If lapsing already, plan starts with a 5-day freeze and re-baseline |
| `include_subdeck_priority` | Sorts which tags get suspended first |

## Verification Checklist

- [ ] Formula for steady-state reviews shown with numbers plugged in (no hand-waving).
- [ ] Overload day is named with a specific day number, not "eventually you'll run out of time."
- [ ] Daily-load forecast includes days 1, 7, 14, 28, 56, 84 (or comparable for a shorter horizon).
- [ ] Interval table grounded in stated algorithm; deviations flagged.
- [ ] All 5 numeric triggers stated with thresholds (not vague "if struggling").
- [ ] Weekly review names the 5 specific stats to pull from Anki (not "review your stats").
- [ ] Worst-case week stress test included with concrete backlog and recovery numbers.
- [ ] No "just be consistent" filler. Every recommendation has a number or a formula.
- [ ] If the time budget is mathematically incompatible with the new-card rate, the prompt says so and refuses to recommend the schedule.

## Worked Example (compact)

**Input:** `deck_size = 4000 mature`, `new_cards_target = 30/day`, `daily_time_budget_min = 60`, `target_retention = 90%`, `time_horizon_days = 60`, `algorithm = FSRS`, `exam_or_milestone_date = none`.

**Output:**

```
SPACED-REPETITION SCHEDULE
Deck start: 4,000 mature   New: 30/day   Budget: 60 min   Retention: 90%   Horizon: 60 d   Algo: FSRS

>>> ASSUMPTIONS
- Steady-state reviews/day ≈ new × 7 (FSRS at 90% R, mature deck) = 30 × 7 = 210 reviews/day
- Time/review: young 30 s, mature 10 s. Mix at day 30 ≈ 60% mature → avg 18 s.
- Lapse penalty: FSRS default; lapsed card S resets to ~50% of pre-lapse.

>>> DAILY-LOAD FORECAST
| Day | New | Reviews due | Minutes | Cumulative |
|----:|----:|---:|---:|---:|
|   1 |  30 |  60 |  25 |  4,030 |
|   7 |  30 | 120 |  46 |  4,210 |
|  14 |  30 | 170 |  58 |  4,420 |
|  21 |  30 | 195 |  64 |  4,630 |
|  28 |  30 | 210 |  66 |  4,840 |
|  42 |  30 | 215 |  65 |  5,260 |
|  60 |  30 | 220 |  64 |  5,800 |

>>> OVERLOAD DAY
Day 19: forecasted minutes 62 exceed budget 60 for 3 consecutive days (days 19, 20, 21).
Recommended: reduce new_cards_target from 30 → 25.
Expected: steady-state reviews drop to ~175/day, minutes settle ~52, backlog risk gone.

>>> INTERVAL TABLE
| Reviews | SM-2 | FSRS (90% R) |
|---|---|---|
| 1 | 1 d | ~3 d |
| 2 | 6 d | ~9 d |
| 3 | 15 d | ~21 d |
| 4 | 37 d | ~48 d |
| 5 | 92 d | ~108 d |

>>> TRIGGERS
A. Lapse > 15%/wk → freeze new 5 d.
B. Backlog > 120 reviews × 3 d → suspend "low-yield" tag.
C. Mature R < 80% → re-optimize FSRS, drop target to 85% for 2 wk.
D. Reviews done < 105/d × 5 d → accept missed work, freeze new, restart.
E. Time/review > 30 s sustained → route 50+ slow cards to rewrite.

>>> WEEKLY 15-MIN REVIEW (Sunday)
Pull: mature retention, lapse rate, time/review, completed/forecast, deck size.
Pick one knob this week.

>>> WORST-CASE WEEK
Miss 4 days at day 21: backlog = 800 reviews.
Recovery: 5 days at 0 new + 250 reviews/day. Verdict: acceptable; freeze new, don't add catch-up tag.
```
