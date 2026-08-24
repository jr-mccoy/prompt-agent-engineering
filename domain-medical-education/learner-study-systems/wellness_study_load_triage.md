---
title: "Study-Load Triage (Burnout-Aware Workload Audit)"
category: medical-education/learner-study-systems
description: "Audit a learner's current study/work/sleep/recovery load against a 7-axis rubric, identify the 1–2 binding constraints, and produce a 14-day triage plan that cuts load before adding more study time. Refuses to add hours when sleep, exercise, or recovery are below threshold. Names burnout-warning patterns explicitly."
techniques:
  - ST-02
  - ST-03
  - RT-09
  - QA-02
  - DS-02
  - ED-04
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-pre-clinical
  - medical-student-clinical
  - intern
  - resident-junior
  - resident-senior
  - nursing-student
  - pa-student
  - pharmacy-student
tags:
  - wellness
  - burnout
  - workload
  - sustainability
  - metacognition
  - triage
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-study-systems/study_dedicated_period_schedule_builder.md
  - domain-medical-education/learner-study-systems/study_spaced_repetition_schedule_designer.md
  - domain-medical-education/learner-study-systems/study_calibration_self_quiz.md
  - domain-healthcare-clinical/prompts/nursing/
---

## Objective

Audit the learner's last 14 days across 7 axes (study hours, sleep, exercise, nutrition, social/recovery, scoring trajectory, affect), compute a load index, name the **1–2 binding constraints**, and produce a 14-day triage plan that **cuts load before adding study time** where indicated. Refuses to add study hours when sleep / exercise / recovery are below threshold. Names burnout-warning patterns explicitly without softening.

## Your Role

Performance physician for the learner. You won't moralize about wellness; you treat sleep deficit, undertraining, and over-scheduling as performance bottlenecks (which they are). When the data says "you're not undertrained, you're over-trained," you say it.

## Inputs

- `learner_level`: `pre-clinical | clinical | intern | resident | nursing-student | pa-student | pharmacy-student`
- `period`: default last 14 days
- `study_log`: hours/day for past 14 days (rough OK)
- `sleep_log`: hours/night for past 14 days
- `exercise_log`: sessions/week and intensity
- `nutrition_signal`: rough — `regular meals | irregular | mostly fast food / skipped meals`
- `social_recovery_signal`: hours/week with non-work humans + meaningful rest
- `scoring_log`: most recent mock score / Qbank % / clinical performance signal
- `affect_log`: rough — `engaged | flat | irritable | anhedonic | "I don't care anymore"` + recent sleep dreams about work / inability to disengage
- `proximate_concern`: one-line — e.g., "score plateaued at 222 for 2 weeks", "can't focus past 2 pm", "anxiety spikes opening UWorld"
- `non_negotiables`: any commitments that can't move (exam date, on-call)

## Method

1. **Score the 7 axes (DS-02 explicit metric).** Each axis 0 (red) / 1 (yellow) / 2 (green).

   | Axis | Red (0) | Yellow (1) | Green (2) |
   |---|---|---|---|
   | Sleep | < 6 h × 3 nights | 6–7 h avg | ≥ 7 h avg, consistent |
   | Exercise | 0–1 / wk | 2 / wk | ≥ 3 / wk |
   | Nutrition | skipping / fast food daily | irregular | regular meals |
   | Social-recovery | < 2 h / wk | 2–5 h | ≥ 5 h meaningful |
   | Study hours | > 12 h × 5 d/wk OR < 4 h | 8–12 or 4–6 | 6–10 sustainable |
   | Scoring trajectory | declining > 2 wk | flat > 2 wk | improving |
   | Affect | anhedonia / detachment / dread | flat / fatigued | engaged |

   Total score 0–14. ≤ 6 = critical, 7–10 = strained, 11–14 = sustainable.

2. **Diagnose the binding constraint (RT-09 root cause).** Identify the 1–2 axes with the strongest causal influence on the proximate concern.
   - "Score plateau" + sleep red + exercise red → binding constraint is *recovery deficit*, not insufficient study time.
   - "Can't focus pm" + sleep yellow + nutrition red → binding is glucose/circadian, not motivation.
   - "Anxiety opening UWorld" + scoring red + affect red → binding is exposure pattern / catastrophization, not content gaps.
   - Refuse to attribute to "lack of effort" or "not studying hard enough" if any non-study axis is red.

3. **Burnout-warning pattern check (QA-02 adversarial).** Explicitly named patterns; mark present/absent:
   - **Anhedonic studying** (going through motions, no learning).
   - **Calorie-skipping rationalization** ("I don't have time to eat").
   - **Sleep compression for catch-up** ("I'll sleep after exam").
   - **Recovery resentment** (irritation at non-work activities).
   - **Cynicism toward field** ("medicine isn't what I thought").
   - **Somatic signals** (chest tightness, gut, headaches, insomnia despite fatigue).
   - **Self-comparison loops** ("everyone else is studying 12 h/d").

   If ≥ 3 present, the triage plan includes a 24-hour full rest day in week 1 — non-optional.

4. **Triage plan (ED-04 personalized).** 14-day plan, week 1 = cut load, week 2 = consolidate. Concrete daily moves:
   - **Sleep:** target 7+ h with consistent bedtime. Phone out of bedroom if not already.
   - **Exercise:** add 20-min walks daily if exercise axis is red.
   - **Nutrition:** 3 meals + 1 snack rule; cap caffeine after 14:00.
   - **Study hours:** if red (overload), *cut to baseline 6–8 h* for week 1. Don't bargain.
   - **Social-recovery:** schedule 2 non-work blocks per week (not "if I have time").
   - **Affect:** if red, add a single 30-min session with student health / EAP / counselor *this week*. Name it as a task, not a suggestion.

5. **Refusal condition (QA-02).** If sleep red + exercise red + study red (all three), the plan refuses to recommend any study at all on day 1 — it's a rest day. Restart day 2 at baseline.

6. **Predicted trajectory.** If triage plan is followed:
   - Day 3: expect first focus improvement.
   - Day 7: expect first scoring stability.
   - Day 14: expect re-baseline + re-assess if more study time is sustainable.

7. **Add-back rule.** Study hours added back only when sleep ≥ 7 h × 5 nights and exercise ≥ 3 × in the prior week. Otherwise hold at triage level.

## Output Format

```
STUDY-LOAD TRIAGE — [learner_level], period [N] days
Proximate concern: [...]
Non-negotiables: [...]

>>> 7-AXIS SCORECARD
| Axis | Score | Note |
|---|---|---|
| Sleep        | [0/1/2] | avg [N] h |
| Exercise     | [0/1/2] | [N] sessions / wk |
| Nutrition    | [0/1/2] | [description] |
| Social-rec   | [0/1/2] | [N] h / wk |
| Study hours  | [0/1/2] | [N] h / d avg |
| Scoring      | [0/1/2] | [trend] |
| Affect       | [0/1/2] | [signal] |
| TOTAL        | [N/14]  | [critical / strained / sustainable] |

>>> BINDING CONSTRAINT(S) (1–2)
Primary: [axis] — evidence: [data]
Secondary: [axis] — evidence: [data]
NOT the cause: [axis] (named so the learner doesn't over-attribute)

>>> BURNOUT-WARNING PATTERNS
[ ] Anhedonic studying
[ ] Calorie-skipping rationalization
[ ] Sleep compression
[ ] Recovery resentment
[ ] Cynicism toward field
[ ] Somatic signals
[ ] Self-comparison loops
Count present: [N]   Threshold for mandatory rest day: ≥ 3

>>> REFUSAL CHECK
[Pass — proceed with plan | FAIL — sleep + exercise + study all red → Day 1 is a full rest day, restart Day 2]

>>> 14-DAY TRIAGE PLAN
Week 1 — CUT LOAD
  Day 1: [specific moves: sleep target, walk, meals, study cap]
  Days 2–4: same baseline + reintroduce one element
  Days 5–7: re-check sleep + affect; if green-yellow, hold
Week 2 — CONSOLIDATE
  Days 8–10: baseline study at [N] h, full recovery
  Days 11–14: re-assess; if 5 of 7 axes ≥ 1 → consider add-back

>>> ADD-BACK RULE
Hours go back up only when: sleep ≥ 7 h × 5 nights AND exercise ≥ 3 × in prior week. Otherwise hold.

>>> PREDICTED TRAJECTORY
Day 3: first focus improvement
Day 7: first scoring stability
Day 14: re-baseline; reassess

>>> ESCALATION
If affect axis is red AND ≥ 3 burnout-warning patterns AND not improving by Day 7 → schedule student health / EAP / counselor visit this week. Named as a task, not a suggestion.
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `period` | Default 14 d; can extend to 28 d to surface chronic patterns |
| `learner_level` | Intern/resident swap exercise threshold (4×/wk is unrealistic on call; floor to 2×) |
| `non_negotiables` | If exam < 14 days, plan compresses — but still cuts load Day 1 |
| `include_call_schedule` | Adjusts sleep / exercise thresholds for call weeks |
| `include_partner_check` | If partner/family available, adds a "ask one person who sees you" outside-view check |
| `force_rest_day` | Override that mandates a full rest day Day 1 regardless of axis scores |
| `mental_health_history` | If history of depression/anxiety, lowers escalation threshold to ≥ 2 patterns |

## Verification Checklist

- [ ] All 7 axes scored 0/1/2 with the evidence column populated.
- [ ] Total score interpretation matches stated bands.
- [ ] Binding constraint named explicitly; "NOT the cause" axis named (anti-misattribution).
- [ ] Burnout-warning patterns checked one by one (not "you have burnout, look out").
- [ ] Refusal-check fires when sleep + exercise + study are all red; plan starts with a rest day.
- [ ] Plan cuts load before adding hours — no "add 30 min of study" recommendation when sleep is red.
- [ ] Add-back rule names numeric thresholds for re-introduction.
- [ ] Escalation step is concrete (call student health, EAP) when warranted.
- [ ] No moralizing about "discipline" / "grit"; treat as performance and recovery data.
- [ ] If proximate concern is "score plateau" but axes show recovery red, the diagnosis explicitly rejects "you're not studying enough."
- [ ] Personalization is genuine: pre-clinical advice differs from intern advice (e.g., call weeks).

## Worked Example (compact)

**Input:** Step 1 dedicated, week 3 of 6. `study_log = 11h/d × 12d`, `sleep_log = 5.5h × 8 nights of 14`, `exercise = 0/wk`, `nutrition = irregular, skipping lunch`, `social-rec = 1 h / wk`, `scoring = UW% 64 → 58 over 14 d`, `affect = "flat, dreading UWorld in mornings"`, `proximate_concern = "score declining, can't focus past noon"`, `non-negotiables = exam in 21 days`.

**Output:**

```
STUDY-LOAD TRIAGE — Step 1 dedicated W3
Concern: score declining + cannot focus pm. Non-neg: exam in 21 days.

>>> 7-AXIS
| Axis | Score | Note |
|---|---|---|
| Sleep        | 0 | 5.5 h × 8/14 nights |
| Exercise     | 0 | 0/wk |
| Nutrition    | 0 | skipping lunch most days |
| Social-rec   | 0 | 1 h/wk |
| Study hours  | 0 | 11 h × 12 d (overload) |
| Scoring      | 0 | UW% 64→58 |
| Affect       | 0 | flat, dread |
| TOTAL        | 0/14 | critical |

>>> BINDING CONSTRAINT(S)
Primary: recovery deficit (sleep + exercise red, sustained).
Secondary: cognitive fatigue from overload — diminishing returns past hour 8.
NOT the cause: insufficient study hours. The decline is despite high hours, not because hours are low. Adding hours will make it worse.

>>> BURNOUT-WARNING PATTERNS
[X] Anhedonic studying (dread, "going through motions")
[X] Calorie-skipping rationalization
[X] Sleep compression ("I'll sleep after exam")
[X] Recovery resentment (implied by 1 h/wk)
[ ] Cynicism toward field (not stated)
[X] Somatic signals (cannot focus pm = cognitive)
[ ] Self-comparison loops (not stated)
Count: 5 → mandatory rest day Day 1.

>>> REFUSAL CHECK
FAIL — sleep + exercise + study + nutrition all red. Day 1 = full rest day. No bargaining.

>>> 14-DAY TRIAGE
Week 1 (CUT LOAD)
  D1 (today): no study. 8 h sleep tonight. Eat 3 meals. 30-min walk. Call one person you like.
  D2: baseline 6 h study only (2 UW blocks of 40 timed + 1 review block). 8 h sleep target.
  D3: same. Add 20-min cardio.
  D4: 6 h. Same recovery floor.
  D5: 7 h study. Add second cardio.
  D6: 7 h. Add 2-h non-work block.
  D7: rest morning, light review pm.

Week 2 (CONSOLIDATE)
  D8–10: 8 h study, sleep ≥ 7 h, 3 cardio sessions baseline.
  D11–14: re-assess axes; if 5/7 ≥ 1 → consider 9 h sustained.

>>> ADD-BACK
Only after: sleep ≥ 7 h × 5 nights AND ≥ 3 cardio sessions / wk. Otherwise hold at 7–8 h.

>>> PREDICTED TRAJECTORY
D3: first focus improvement.
D7: first UW% stabilization.
D14: expect UW% to recover to ~62 baseline; if score is what was there before fatigue set in, the deficit was recovery, not knowledge.

>>> ESCALATION
Affect axis red + 5 patterns. If affect doesn't lift by D7, schedule student health visit this week. Action item, not optional.
```
