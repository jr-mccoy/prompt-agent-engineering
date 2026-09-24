---
title: "Program Progression Review — Read the Training Log for Stalls, Overreaching, and When to Deload"
category: health-wellness/fitness
description: "Review an existing training plan and at least four weeks of log: classify each lift or session as progressing, stalled, or regressing; screen for overreaching and for the few signs that are not training problems at all; walk a stall down a cause tree (adherence, execution, recovery, fuelling, programming); and prescribe exactly one change — often a deload — with a re-review date. Consumes the Readiness Profile."
techniques:
  - RT-10
  - RT-05
  - DS-06
  - QA-04
difficulty: intermediate
tags:
  - health-wellness
  - training-log
  - plateau
  - deload
  - overreaching
  - program-review
  - not-getting-stronger
  - sore-for-days
  - dreading-workouts
  - need-rest-week
updated: "2026-09-24"
related_prompts:
  - domain-health-wellness/fitness/fitness_beginner_training_plan.md
  - domain-health-wellness/fitness/fitness_endurance_event_build_plan.md
  - domain-health-wellness/sleep-recovery/sleep_routine_and_environment_audit.md
---

# Program Progression Review

**Objective:** Turn a plan plus a training log into a verdict per lift or session, a
named cause for any stall, and one change to make next — so the person stops either
grinding through fatigue or abandoning a plan that only needed a deload.

> **Readiness gate.** Start from a Readiness Profile
> (`foundations/wellness_readiness_and_red_flag_screen.md`). No profile → ask its
> blocks 1–8 first. URGENT-CARE-NOW, CLINICIAN-FIRST, or OUT-OF-SCOPE → stop and
> restate the route. An urgent result means contacting the local emergency number now
> (e.g. 911 in the US). GO-WITH-LIMITS → no recommendation may exceed a stated limit.

**When to Use:**
- Week 8 of `fitness_beginner_training_plan.md`, or any plan 4+ weeks in.
- Numbers stopped going up and you cannot tell whether to push, rest, or change plan.
- You feel flat, sore for days, or dread sessions you used to like.
- A build toward an event is falling behind its schedule.
- **Not this prompt if** the problem is pain or an injury (clinician or physiotherapist),
  or you have no log yet — run the plan for four weeks and log it first.

## Inputs / Context

1. **Readiness Profile.**
2. **The plan as written** — sessions, sets, reps, target effort, progression rule.
3. **The log, 4+ weeks** — date, exercise or session, load or pace/distance, reps, RPE.
   Missing weeks are stated, not filled.
4. **Recovery context** for the same weeks: typical sleep, work or life stress (low /
   medium / high), illness, travel.
5. **Optional:** morning resting heart rate if the person already measures it (not
   meaningful on rate-limiting medication), and how sessions *feel* (1–5).

## Method

1. **Non-training red flags first.** Any of these → stop and route, no review:
   chest symptoms, fainting, or unusual breathlessness (re-run the gate); **very dark
   (cola-coloured) urine with severe muscle pain or swelling after a hard session →
   urgent care the same day**; pain that changes movement or has lasted over a week →
   clinician or physiotherapist; eating-guard signals (training to "earn" or "burn off"
   food) → nutrition guard STOP and clinician.
2. **Check the evidence is enough (RT-05, QA-04).** Fewer than 4 weeks, or adherence
   unknown → say what can and cannot be concluded, and at what confidence.
3. **Classify each lift or session.** *Progressing* — load, reps, pace, or distance up
   at the same or lower RPE. *Stalled* — no gain across three consecutive exposures.
   *Regressing* — performance down or RPE up at the same work for 2+ weeks.
4. **Overreaching screen.** Count signals present across the last 2 weeks: regression on
   several lifts at once; soreness lasting beyond ~72 h; sleep worse than baseline; a
   sustained rise in morning resting heart rate against the person's own baseline;
   frequent minor illness; irritability or dread. Two or more with regression → treat
   as overreaching.
5. **Walk the cause tree for each stall (RT-10).** Stop at the first branch that explains it.
   - **Adherence** — fewer than ~80% of planned sessions done? Fix the routine, not the plan.
   - **Execution** — RPE drifting below target, rests cut short, range shortened?
   - **Recovery** — sleep under ~7 h most nights, high stress, recent illness?
   - **Fuelling** — only if the guard is CLEAR: skipped meals around training, very low
     appetite, deliberate restriction? Route to the nutrition prompts; do not set intake here.
   - **Programming** — beginner session-to-session gains naturally slow after roughly
     3–6 months; the rule has outlived its usefulness.
6. **Prescribe exactly one change (DS-06).** In priority order:
   - Overreaching → **deload week**: about half the sets, loads at ~RPE 5–6, same exercises.
   - Recovery cause → protect sleep first; hold loads, no progression, for 2 weeks.
   - Execution cause → reset load ~10% and rebuild with the target RPE enforced.
   - Programming cause → move from session-to-session to weekly progression, or add
     a rep-range step; change one exercise variation at most.
   - Endurance build behind schedule → hold the current week rather than skipping ahead.
7. **Set the re-review** at 2–3 weeks, with the one number that will show whether it worked.

## Output Format

```
# Progression review — [name], weeks [n–n]
Readiness: [result]; limits: [...]
Evidence: [n] weeks logged, adherence [n%], confidence [High / Medium / Low] — [why]

## Red flags
[none | flag → route]

## Verdicts
| Lift / session | Trend | Evidence (first → latest) | Verdict |
|---|---|---|---|

## Overreaching screen
Signals present: [list] ([n] of 6) → [overreaching / not]

## Cause of stall
[branch reached, with the log evidence]

## The one change
[what, for how long, exact numbers]

## Re-review
Date: [..] | Success looks like: [one number]
```

## Verification

- [ ] Red flags were checked before any training analysis.
- [ ] Every verdict cites first and latest log values.
- [ ] Confidence is stated and justified by weeks logged and adherence.
- [ ] Only one change is prescribed.
- [ ] Fuelling was examined only with the nutrition guard CLEAR, and no intake was set.
- [ ] Nothing exceeds a GO-WITH-LIMITS limit.

## False-Positive Prevention

1. **One bad session is not a stall.** Three consecutive exposures, or two weeks of
   regression, before any verdict.
2. **Don't blame the programme first.** Most beginner stalls are adherence, sleep, or
   effort drift; changing the plan hides the real cause.
3. **Don't prescribe a deload for boredom.** A deload answers fatigue; dread without
   performance loss may be a routine or enjoyment problem.
4. **Resting heart rate is personal.** Compare only with the person's own baseline, and
   ignore it on rate-limiting medication.
5. **Don't read fuelling into a guarded profile.** If the nutrition guard is STOP, the
   fuelling branch is not examined; say so.
6. **Don't stack fixes.** A deload plus a new exercise plus more sleep leaves nothing to learn.
7. **Pain is not a stall.** It routes out of this prompt.

## Example Output

Scenario: 34, GO, weeks 1–8 of the beginner plan; slept ~6 h in weeks 6–8 (new project).

```
# Progression review — Priya, weeks 1–8
Readiness: GO; limits: none
Evidence: 8 weeks logged, adherence 22/24 = 92%, confidence Medium — sleep reported, not measured

## Red flags
none

## Verdicts
| Goblet squat | up then flat | 8 kg×12 (wk3) → 14 kg×9, 9, 8 (wk6–8) | stalled |
| DB RDL       | up           | 10 kg×10 → 16 kg×12                 | progressing |
| Incline push-up | down      | 3×12 @ RPE 7 (wk5) → 3×10 @ RPE 9 (wk8) | regressing |
| Row          | flat         | 12 kg×10, 9, 9 (wk6) → 12 kg×10, 9, 9 (wk8) | stalled |

## Overreaching screen
Signals present: regression on 3 lifts, sleep below baseline, soreness ~4 days (3 of 6) → overreaching

## Cause of stall
Recovery branch: adherence 92% and RPE on target through wk5; stall starts with the 6-h sleep weeks.

## The one change
Deload week 9: 2 sets instead of 3, loads at RPE 5–6, same exercises; week 10 resumes the plan as written.
Note (context, not a second change): the 6-h sleep weeks are the likely driver — worth protecting
~7 h if the project allows, but the review tests the deload alone.

## Re-review
Date: week 12 | Success looks like: goblet squat 14 kg × 12, 12, 11 at ≤ RPE 8
```

## Techniques Used

- **RT-10 Troubleshooting Decision Tree** — the ordered cause tree for a stall.
- **RT-05 Evidence-Based Reasoning** — every verdict cites log values.
- **DS-06 Prioritization and Severity Guidance** — red flags, then overreaching, then one change.
- **QA-04 Uncertainty Acknowledgment** — confidence tied to weeks logged and adherence.

## Related Prompts

- `domain-health-wellness/fitness/fitness_beginner_training_plan.md` — the plan most reviews start from.
- `domain-health-wellness/fitness/fitness_endurance_event_build_plan.md` — builds that fall behind.
- `domain-health-wellness/sleep-recovery/sleep_routine_and_environment_audit.md` — when recovery is the branch.
