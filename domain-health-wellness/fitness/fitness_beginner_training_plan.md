---
title: "Beginner Training Plan — Eight Weeks of Full-Body Strength and Aerobic Work With Explicit Progression Rules"
category: health-wellness/fitness
description: "Build an eight-week beginner plan for a healthy adult: full-body strength two to three times a week across six movement patterns, aerobic work framed against public-health activity guidance, effort set by RPE and reps in reserve, a double-progression rule for adding load, a pain-versus-soreness stop rule, and form learned from a qualified coach rather than from text. Consumes the Readiness Profile; no rehabilitation."
techniques:
  - DS-02
  - DS-26
  - OC-09
  - QA-01
difficulty: beginner
tags:
  - health-wellness
  - strength-training
  - beginner
  - progressive-overload
  - rpe
  - aerobic-fitness
  - start-exercising
  - lifting-weights
  - weight-training
  - returning-to-exercise
updated: "2026-09-24"
related_prompts:
  - domain-health-wellness/foundations/wellness_readiness_and_red_flag_screen.md
  - domain-health-wellness/fitness/fitness_program_progression_review.md
  - domain-psychology/client-self-use/habit-lifestyle/clientself_exercise_as_antidepressant_plan.md
---

# Beginner Training Plan

**Objective:** Give a healthy adult who is new to (or returning to) structured training
an eight-week plan they can run without guessing: what to do each session, how hard,
when to add load, and when to stop an exercise.

> **Readiness gate.** Start from a Readiness Profile
> (`foundations/wellness_readiness_and_red_flag_screen.md`). No profile → ask its
> blocks 1–8 first. URGENT-CARE-NOW, CLINICIAN-FIRST, or OUT-OF-SCOPE → stop and
> restate the route. GO-WITH-LIMITS → every limit binds this plan (for example an RPE
> ceiling, or effort rating instead of heart rate on rate-limiting medication).

**When to Use:**
- You have never followed a structured plan, or it has been a year or more.
- You want strength *and* general fitness, not a single sport.
- You have 2–4 sessions a week and a gym, home dumbbells, or only bodyweight.
- **Not this prompt if** you are rehabilitating an injury or managing a diagnosed
  condition (clinician or physiotherapist), training for a dated event
  (`fitness/fitness_endurance_event_build_plan.md`), or exercising primarily for mood
  (`domain-psychology/client-self-use/habit-lifestyle/clientself_exercise_as_antidepressant_plan.md`).

## Inputs / Context

1. **Readiness Profile** — gate result, limits, starting point, capacity.
2. **Sessions per week and minutes each**, from the profile or the routine designer.
3. **Equipment:** gym, dumbbells (which weights), bands, bodyweight only.
4. **Goal in their words**, and one thing they would enjoy doing.
5. **Movement history:** any exercise that already feels uncomfortable (not injury — that
   routes back to the gate).

## Method

1. **State what this plan can and cannot do (OC-09).** Can: session structure, effort,
   progression, stop rules. Cannot: teach technique reliably in text, assess pain, or
   rehabilitate. Recommend one or two sessions with a qualified coach or trainer in the
   first fortnight, or filming a set and comparing it with a reputable demonstration.
2. **Anchor to general guidance, not a prescription.** Widely cited public-health
   guidance for adults is roughly 150–300 minutes of moderate aerobic activity (or
   75–150 vigorous) per week plus muscle-strengthening on 2+ days. Beginners build
   *toward* it; anything above zero counts.
3. **Pick the structure from capacity (DS-26).**

   | Sessions/week | Default structure |
   |---|---|
   | 2 | Full-body A and B, aerobic on other days as walks |
   | 3 | Full-body A / B / A, then B / A / B the next week; 1 aerobic session |
   | 4 | Full-body A / B + 2 aerobic sessions |

   Each full-body session covers six patterns: **squat, hinge, push, pull, single-leg or
   carry, trunk.** Choose the easiest variation the person can do with control
   (e.g. box squat → goblet squat; hip bridge → dumbbell Romanian deadlift).
4. **Set effort with numbers (DS-02).**
   - **RPE 1–10**, with **reps in reserve (RIR)**: RPE 7 ≈ 3 reps left in the tank.
   - Weeks 1–2: 2 sets, RPE 5–6 — technique weeks. Weeks 3–8: 2–3 sets of 8–12 reps at RPE 6–8.
   - Rest 60–90 s on small exercises, 2–3 min on squat and hinge.
   - Aerobic: "talk test" — moderate means you can speak in sentences but not sing.
   - GO-WITH-LIMITS: cap at the limit given (default RPE 6), no maximal attempts.
5. **Write the progression rule (double progression).** When every set reaches the top of
   the rep range at or below the target RPE, add the smallest available load (the next
   dumbbell, or roughly 2.5–5%) and return to the bottom of the range. Bodyweight moves
   progress by leverage, range, or tempo. One variable changes at a time.
6. **Write the stop rule.** Muscle soreness 24–72 h after a new session is expected.
   **Sharp pain, joint pain during a rep, pain that changes how you move, or anything
   that worsens across sessions → stop that exercise, swap to a pain-free variation,
   and if it persists beyond a week or recurs, see a clinician or physiotherapist.**
   Any gate-block-1 or block-2 symptom during exercise → stop and re-run the gate.
7. **Lay out eight weeks** with a lighter week 5 or 6 if the person feels run-down,
   then hand to `fitness_program_progression_review.md` at week 8.
8. **Self-verify (QA-01)** against the checklist below before output.

## Output Format

```
# 8-week beginner plan — [name]
Readiness: [result]; limits applied: [...]
What this plan can't do: [one line]; coaching recommendation: [...]

## Weekly structure
[sessions/week, days, which session on which day]

## Session A / Session B
| Pattern | Exercise (easiest → next) | Sets × reps | RPE | Rest | Coach cue to check |
|---|---|---|---|---|---|

## Aerobic
[type, minutes, talk-test intensity, weekly total vs. guidance]

## Progression rule
[double progression, with the actual increments available]

## Stop rule
[soreness vs. pain; swap; when to see a clinician; gate re-run]

## Weeks 1–8
| Week | Sets | RPE | Aerobic min | Note |
|---|---|---|---|---|

## Log template
Date | Exercise | Load | Reps per set | RPE | Pain (Y/N, where)
```

## Verification

- [ ] Every limit from the profile is visible in the RPE column or exercise choice.
- [ ] All six patterns appear in each full-body session.
- [ ] Weeks 1–2 are technique weeks at RPE 5–6.
- [ ] The progression rule names a real increment for the person's equipment.
- [ ] The stop rule separates soreness from pain and names where persistent pain goes.
- [ ] No exercise is prescribed as treatment for a condition or injury.

## False-Positive Prevention

1. **Text is not coaching.** Give at most two check-cues per exercise and route
   technique to a qualified coach; do not write a paragraph of biomechanics.
2. **Don't prescribe to failure.** Beginners get nearly all of the benefit at RPE 6–8;
   failure sets add injury risk and soreness that end week-one enthusiasm.
3. **Don't progress two things at once.** Adding load and a set in the same week hides
   which change caused a stall or a tweak.
4. **Heart-rate zones are not universal.** On rate-limiting medication, or without a
   measured maximum, use RPE and the talk test.
5. **"No pain, no gain" is not a rule.** Joint pain is a stop signal, not a toughness test.
6. **Don't write a weight-loss plan here.** If the goal is body composition, the plan is
   the same; eating goes to the nutrition prompts, and only if the guard is CLEAR.
7. **Bodyweight-only is not second-class.** Progress by leverage; don't tell the person
   they need a gym.

## Example Output

Scenario: 34, GO, 3 sessions × 45 min, dumbbells 4–16 kg in 2 kg steps, goal "feel strong
and stop getting out of breath on stairs".

```
# 8-week beginner plan — Priya
Readiness: GO; limits applied: none
What this plan can't do: teach technique from text; coaching: one trainer session in week 1, film week-3 goblet squat.

## Weekly structure
Mon A · Wed B · Fri A (next week B/A/B) · Sat 30-min brisk walk

## Session A
| Pattern | Exercise | Sets × reps | RPE | Rest | Coach cue |
| Squat | Goblet squat (box squat if depth is hard) | 3 × 8–12 | 6–8 | 2 min | heels down; knees track toes |
| Hinge | DB Romanian deadlift | 3 × 8–12 | 6–8 | 2 min | hips back; neutral back |
| Push | Incline push-up | 3 × 8–12 | 6–8 | 90 s | body in one line |
| Pull | One-arm DB row | 3 × 8–12/side | 6–8 | 90 s | elbow to hip |
| Single-leg | Split squat, bodyweight | 2 × 8/side | 6–7 | 60 s | front heel planted |
| Trunk | Dead bug | 2 × 8/side | 6 | 60 s | low back stays down |
(Session B: DB bench/floor press, band pull-apart, hip bridge, reverse lunge, farmer carry, side plank.)

## Aerobic
Sat 30 min + 10-min walk after Mon/Wed/Fri ≈ 60 min/week; building to 150 by week 8.

## Progression rule
All 3 sets hit 12 reps at ≤ RPE 8 → next dumbbell (+2 kg), back to 8 reps.

## Stop rule
Sore quads for 2 days: expected. Knee pain during split squats: swap to box step-up; if still present in a week, see a physio.

## Weeks 1–8
| 1–2 | 2 sets | 5–6 | 60 | learn the moves |
| 3–4 | 3 sets | 6–7 | 90 | start progressing load |
| 5   | 3 sets | 7–8 | 110 | lighter week if run-down |
| 6–8 | 3 sets | 7–8 | 150 | week 8 → progression review |
```

## Techniques Used

- **DS-02 Metric Specification** — RPE, RIR, rep ranges, and a numeric progression trigger.
- **DS-26 Safe Defaults Pattern** — a default structure for every session count.
- **OC-09 Capability Boundary Specification** — what text can and cannot do for technique and pain.
- **QA-01 Self-Verification** — checklist pass before output.

## Related Prompts

- `domain-health-wellness/foundations/wellness_readiness_and_red_flag_screen.md` — the gate.
- `domain-health-wellness/fitness/fitness_program_progression_review.md` — the week-8 review.
- `domain-psychology/client-self-use/habit-lifestyle/clientself_exercise_as_antidepressant_plan.md` —
  movement for mood rather than fitness.
