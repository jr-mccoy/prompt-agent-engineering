---
title: "Endurance Event Build Plan — Base, Build, Taper for a First 5K, 10K, Half Marathon, or Century Ride"
category: health-wellness/fitness
description: "Plan a first endurance event from the person's current base to the start line: a feasibility check of weeks available against weeks needed, base-build-peak-taper phases with gates between them, ramp limits on weekly volume and the long session, cutback weeks, a missed-week and illness protocol, and the injury signs that end running for now. Consumes the Readiness Profile; no rehabilitation, no race-day heroics."
techniques:
  - DT-01
  - DS-02
  - QA-08
  - QA-13
difficulty: intermediate
tags:
  - health-wellness
  - endurance
  - running
  - cycling
  - taper
  - injury-prevention
  - event-training
updated: "2026-09-24"
related_prompts:
  - domain-health-wellness/foundations/wellness_readiness_and_red_flag_screen.md
  - domain-health-wellness/fitness/fitness_program_progression_review.md
  - domain-health-wellness/nutrition/nutrition_meal_structure_planner.md
---

# Endurance Event Build Plan

**Objective:** Get a healthy adult to the start line of a first 5K, 10K, half marathon,
or century ride uninjured, by building from their real current base with ramp limits
they can see and gates they must pass between phases.

> **Readiness gate.** Start from a Readiness Profile
> (`foundations/wellness_readiness_and_red_flag_screen.md`). No profile → ask its
> blocks 1–8 first. URGENT-CARE-NOW, CLINICIAN-FIRST, or OUT-OF-SCOPE → stop and
> restate the route. GO-WITH-LIMITS → intensity caps bind every session; a first
> half marathon or century under limits needs the clinician's explicit agreement.

**When to Use:**
- You have entered, or want to enter, a first event with a date.
- You run or ride casually and want a plan that does not end in shin pain at week five.
- You want to know honestly whether the date you picked is realistic.
- **Not this prompt if** you have no base at all and no event (start with
  `fitness/fitness_beginner_training_plan.md`), you are returning from an injury
  (clinician or physiotherapist), or you are chasing a time at your fifth marathon —
  this is first-event planning.

## Inputs / Context

1. **Readiness Profile.**
2. **Event:** type, distance, date, terrain or elevation, expected weather.
3. **Current base, last 4 weeks:** sessions per week, weekly distance or time, longest
   single session, and whether any of it hurt.
4. **Days and minutes available** per week; which day can hold the long session.
5. **Goal:** finish comfortably (default), finish with walk breaks, or a target time.

## Method

1. **Feasibility check (QA-08).** Compare weeks available with common coaching practice
   for a first event, from a base of regular easy activity:

   | Event | Typical build | Longest session before taper |
   |---|---|---|
   | 5K | 8–10 weeks (run/walk from little running) | ~5 km continuous or run/walk |
   | 10K | 10–12 weeks from running 20–30 min comfortably | ~10–12 km |
   | Half marathon | 12–16 weeks from ~15–20 km/week | ~16–19 km |
   | Century ride | 12–16 weeks from ~2–3 h riding/week | ~120–135 km (75–85 mi) |

   Short of time → offer, in order: a shorter distance on the same date, run/walk the
   event, or a later event. Never compress the ramp to fit the date.
2. **Break the build into phases (DT-01).**
   - **Base** — easy volume only; most sessions conversational; builds the habit and tissue tolerance.
   - **Build** — one quality session a week (steady tempo or short intervals), long session grows.
   - **Peak** — 1–2 weeks with the longest session and event-pace practice.
   - **Taper** — ~1 week for 5K/10K, ~2 weeks for half marathon or century: cut volume by
     roughly 40–60%, keep a little intensity, sleep more.
3. **Set ramp limits (DS-02).** Show them on the plan.
   - Weekly volume up by roughly **10% at most** — a conservative heuristic; the evidence
     for the exact number is weak, but large sudden jumps are the pattern to avoid.
   - Long run grows by ≤ ~1–1.5 km a week and stays under about half of weekly running
     volume; long ride grows by ≤ ~15–20 min a week.
   - A **cutback week** every 3rd or 4th week (~20–30% less volume); the week after it
     returns to the last full week's volume, not above it.
   - Never raise volume and intensity in the same week.
   - ~80% of weekly time easy; quality sessions never on consecutive days.
4. **Add strength twice a week** (short full-body sessions from the beginner plan) in
   base and build; once a week in peak; none in the final taper week.
5. **Gate each phase (QA-08).** Base → build only if ≥80% of base sessions were done and
   nothing hurts. Build → peak only if the long session is on schedule. A failed gate
   repeats the last week; it does not skip ahead.
6. **Write the missed-week and illness protocol (QA-13).** Fever, chest symptoms, or
   breathlessness → no training until well; if those occurred during training, re-run
   the gate. Missed 1 week → repeat the previous week. Missed 2+ → step back two weeks.
   Lost more than a quarter of the remaining build → redo the feasibility check.
7. **State the injury stops.** Pain that changes your stride or pedalling; pain on a
   specific spot of bone that worsens with impact; swelling; pain that is worse the
   morning after → stop that activity and see a clinician or physiotherapist. Do not
   "run through" these to protect the date.
8. **Hand off fuelling** for sessions over ~90 minutes to
   `nutrition/nutrition_meal_structure_planner.md` — only if the nutrition guard is CLEAR.

## Output Format

```
# Build plan — [event], [date]
Readiness: [result]; limits: [...]
Feasibility: [n] weeks available vs [n] typical → [on track | adjusted: ...]

## Ramp limits
[volume cap, long-session cap, cutback pattern, intensity rule]

## Phases and gates
| Phase | Weeks | Focus | Gate to pass |
|---|---|---|---|

## Week-by-week
| Wk | Phase | Sessions (easy / quality / long) | Weekly volume | Long session | Change vs last week |
|---|---|---|---|---|---|

## Missed-week and illness protocol
[rules]

## Injury stops
[signs → action]

## Hand-offs
Fuelling → [prompt or "nutrition guard STOP"] | Stalls → fitness_program_progression_review
```

## Verification

- [ ] Feasibility was checked before any week was written.
- [ ] No week's volume exceeds the previous by more than the stated cap (cutback rebounds excepted).
- [ ] Cutback weeks recur every 3–4 weeks.
- [ ] No week raises volume and intensity together.
- [ ] Every phase has a gate, and failing it repeats rather than skips.
- [ ] Injury stops route to a clinician or physiotherapist.

## False-Positive Prevention

1. **The date is not the constraint; the ramp is.** Compressing the build to fit an
   entry is the commonest route to a first-event injury.
2. **Don't present "10%" as science.** It is a conservative heuristic; say so.
3. **Easy means easy.** Beginners run their easy days too hard; give the talk test, not a pace.
4. **A cutback week is training, not failure.** Don't let the person "use it" to catch up.
5. **Don't write a time goal into a first half or century** unless the person asks, and
   then as a range with "finish healthy" ranked first.
6. **Bone-spot pain is not soreness.** Route it out; do not suggest shoes or stretches instead.
7. **Don't carry heart-rate zones onto rate-limiting medication.** Use RPE and the talk test.

## Example Output

Scenario: 41, GO, running 3–4×/week, ~20 km/week, longest 8 km, no pain. Half marathon
in 16 weeks; goal "finish without walking"; long day Sunday.

```
# Build plan — half marathon, 2027-01-17
Readiness: GO; limits: none
Feasibility: 16 weeks available vs 12–16 typical; base 20 km/week (top of ~15–20) → on track.

## Ramp limits
Weekly volume +10% max; long run +1–1.5 km/week and < half of weekly km; cutback every
4th week (−25%), then back to the last full week; volume and intensity never rise together.

## Phases and gates
| Base  | 1–4   | easy volume, 3–4 runs + 2 strength | ≥80% done, no pain |
| Build | 5–12  | +1 tempo/week, long run grows      | long run ≥ 15 km by wk 11 |
| Peak  | 13–14 | 16–18 km long run, race-pace segments | long run done, no pain |
| Taper | 15–16 | volume −45%, short race-pace strides | — |

## Week-by-week (excerpt)
| 1  | Base  | 3 easy + long   | 20 km   | 8 km    | current base |
| 2  | Base  | 3 easy + long   | 22 km   | 9 km    | +10% |
| 3  | Base  | 3 easy + long   | 24.2 km | 10 km   | +10% |
| 4  | Base  | 3 easy + long   | 18 km   | 7 km    | cutback |
| 5  | Build | 2 easy + tempo + long | 24.2 km | 10 km | tempo added, volume = wk 3 |
| 11 | Build | 2 easy + tempo + long | 35.4 km | 15 km | +10% |
| 12 | Build | 2 easy + tempo + long | 26.5 km | 11 km | cutback |
| 14 | Peak  | 2 easy + pace + long  | 38.9 km | 18 km  | peak (46% of week) |
| 15 | Taper | 3 easy + long   | 21 km   | 10 km   | −46% |
| 16 | Taper | 3 short easy    | 10 km + race | race | race week |

## Missed-week and illness protocol
Flu in wk 7 (fever): no running until well; repeat wk 6. If wks 7–8 both missed: step back to wk 5.

## Injury stops
Pain on one spot of the shin that worsens with each run → stop running, see a physio.

## Hand-offs
Fuelling for 90+ min runs (from wk 11) → nutrition_meal_structure_planner | Stalls → progression review
```

## Techniques Used

- **DT-01 Hierarchical Task Breakdown** — event → phases → weeks → sessions.
- **DS-02 Metric Specification** — visible caps on weekly volume, long session, and cutbacks.
- **QA-08 Gate-Based Verification** — feasibility gate and phase gates that repeat rather than skip.
- **QA-13 Failure Recovery Specification** — the missed-week, illness, and injury protocol.

## Related Prompts

- `domain-health-wellness/foundations/wellness_readiness_and_red_flag_screen.md` — the gate.
- `domain-health-wellness/fitness/fitness_program_progression_review.md` — when the build falls behind.
- `domain-health-wellness/nutrition/nutrition_meal_structure_planner.md` — fuelling around long sessions.
