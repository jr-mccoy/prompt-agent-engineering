---
title: "Sleep Routine and Environment Audit — Timing, Light, Caffeine, Alcohol, and Bedroom for a Healthy Adult"
category: health-wellness/sleep-recovery
description: "Audit a healthy adult's sleep from a one-to-two-week log: wake-time regularity, sleep opportunity, morning and evening light, caffeine and alcohol timing, late meals and training, bedroom environment, wind-down, and naps — then run a two-week experiment on the two or three highest-leverage changes. Routes suspected sleep apnoea, chronic insomnia, and other sleep-disorder signs to a clinician (and insomnia to the CBT-I prompt) before any audit. No sleep aids or supplements."
techniques:
  - QA-08
  - RT-02
  - DS-06
  - QA-04
difficulty: beginner
tags:
  - health-wellness
  - sleep
  - sleep-hygiene
  - circadian-rhythm
  - recovery
  - caffeine
updated: "2026-09-24"
related_prompts:
  - domain-health-wellness/foundations/wellness_readiness_and_red_flag_screen.md
  - domain-psychology/client-self-use/coping-by-concern/clientself_sleep_cbt_i_sleep_restriction_calculator.md
  - domain-health-wellness/foundations/wellness_sustainable_routine_designer.md
---

# Sleep Routine and Environment Audit

**Objective:** Find the two or three things in a healthy adult's routine and bedroom
that are most likely costing them sleep, and test them in a two-week experiment —
after first routing anything that looks like a sleep disorder to a clinician.

> **Readiness gate.** Start from a Readiness Profile
> (`foundations/wellness_readiness_and_red_flag_screen.md`). No profile → ask its
> blocks 1–8 first. URGENT-CARE-NOW, CLINICIAN-FIRST, or OUT-OF-SCOPE → stop and
> restate the route. The profile's *Sleep flags* line is re-checked in step 1 below;
> a flag there sends the person to a clinician before this audit runs.

**When to Use:**
- You sleep "okay" but wake unrefreshed, or your sleep is irregular across the week.
- Training recovery or afternoon energy is suffering and sleep is the suspect.
- You want to know whether caffeine, alcohol, screens, or the bedroom matter *for you*.
- **Not this prompt if** you have trouble sleeping 3+ nights a week for 3+ months with
  daytime impact — that is insomnia, and it has an effective structured treatment:
  see a clinician and
  `domain-psychology/client-self-use/coping-by-concern/clientself_sleep_cbt_i_sleep_restriction_calculator.md`
  (read its safety carve-outs first). Sleep problems driven by low mood or anxiety
  belong in `domain-psychology/client-self-use/`.

## Inputs / Context

1. **Readiness Profile**, including the *Sleep flags* line.
2. **A 7–14 day sleep log:** bedtime, lights-out, rough time to fall asleep, wakings,
   final wake time, time out of bed, naps, and how rested (1–5). Estimates are fine.
3. **Same days:** caffeine (what and when), alcohol (how much and when), last meal time,
   training time, evening screens or work.
4. **Bedroom:** light, noise, temperature, bed and pillow, partner, pets, children.
5. **Fixed constraints:** work start, shifts, caregiving, commute.
6. **Any tracker data** — optional and treated as rough.

## Method

1. **Clinical route first (QA-08).** Any of these → clinician before the audit, stated
   plainly and without diagnosis:
   - Loud snoring with witnessed pauses, gasping, or choking; morning headaches;
     **dozing while driving or in conversation** (and: do not drive drowsy today).
   - Insomnia pattern: 3+ nights a week, 3+ months, with daytime impact → clinician and
     the CBT-I prompt (whose carve-outs include untreated apnoea, bipolar disorder,
     seizures, pregnancy, and safety-sensitive work).
   - An irresistible urge to move the legs in the evening; acting out dreams; sudden
     sleep attacks; sleep problems that began with a new medication.
   - Regular use of sleep medication or alcohol to get to sleep.
   The audit may still run *alongside* a referral for the routine factors, if the person wants.
2. **Summarise the log.** Average time in bed, estimated sleep, wake-time range across
   the week, weekend shift, and the rested score — each with confidence (QA-04).
3. **Audit nine factors (RT-02).** For each: what the log shows, the general guidance,
   and whether it plausibly matters here.

   | Factor | General guidance (healthy adults) |
   |---|---|
   | Wake-time regularity | same wake time within ~30–60 min, weekends included |
   | Sleep opportunity | time in bed that allows 7+ hours of sleep for most adults |
   | Morning light | outdoor light within about an hour of waking |
   | Evening light and screens | dimmer light in the last hour; arousing content matters more than the screen |
   | Caffeine | effects last many hours; many people sleep better with none in the ~8 h before bed |
   | Alcohol | tends to fragment the second half of the night; less and earlier is better |
   | Late meals and training | large meals in the last ~2–3 h and very hard sessions close to bed can delay sleep for some |
   | Bedroom | dark, quiet, and cool (often around 16–19 °C / 60–67 °F), with a comfortable bed |
   | Naps and clock-watching | short (≤ ~30 min) and before mid-afternoon; turn the clock away |

4. **Prioritise (DS-06).** Wake-time regularity and sleep opportunity first — nothing else
   compensates for too little time in bed. Then the largest single deviation in the log.
   Choose two or three changes; never more.
5. **Design the experiment.** Two weeks, the chosen changes only, the same log, and one
   outcome measure (rested score, or estimated time to fall asleep). State what result
   would count as "it helped" before starting.
6. **Handle constraints honestly.** Shift workers get anchors within each shift block and
   a consistent pre-sleep routine; parents of young children get the factors they
   control. Shift-work sleepiness that affects safety → clinician.
7. **Set the review** at two weeks: keep, drop, or swap one change.

## Output Format

```
# Sleep audit — [name]
Readiness: [result] | Clinical route: none | [flag → clinician / CBT-I prompt]

## Your log, summarised  ([n] nights; confidence [H/M/L])
Time in bed ~[h] · estimated sleep ~[h] · wake range [time–time] · weekend shift [h] · rested [avg]/5

## Nine factors
| Factor | Your log | Guidance | Matters here? |
|---|---|---|---|

## The changes (2–3), in priority order
1. [change] — why: [log evidence]

## Two-week experiment
Measure: [...] | Counts as helped if: [...] | Review: [date]

## Not included, on purpose
No sleep aids or supplements (ask a clinician or pharmacist) · no diagnosis
```

## Verification

- [ ] Clinical-route signs were checked before any audit, including drowsy driving.
- [ ] The insomnia pattern routes to a clinician and the CBT-I prompt, with its carve-outs noted.
- [ ] Every factor verdict cites the log.
- [ ] Wake-time regularity and sleep opportunity were considered first.
- [ ] Two or three changes only, with a pre-stated success criterion.
- [ ] No sleep aid, melatonin, or supplement is recommended or dosed.

## False-Positive Prevention

1. **Don't hygiene away a disorder.** Snoring with pauses or daytime dozing is a referral,
   not a blackout-blind problem.
2. **Don't treat trackers as truth.** Consumer sleep-stage estimates are rough; the rested
   score and the log carry more weight, and chasing a tracker score can worsen sleep.
3. **Don't fix everything at once.** Nine changes make the experiment unreadable.
4. **Screens are not automatically the cause.** Look at what the person does on them and
   when; a calm show is not a work inbox.
5. **Weekend lie-ins are a symptom as well as a cause.** A big weekend shift usually means
   weekday sleep opportunity is too short; fix that, not just the weekend.
6. **Don't moralise caffeine or alcohol.** Show the timing against the log and let the
   experiment decide.
7. **Don't recommend melatonin or sleep aids.** Timing and dose questions go to a clinician
   or pharmacist.

## Example Output

Scenario: 34, GO, sleep flags none; 10-night log; strength training 19:30; wakes 06:30
weekdays, ~09:00 weekends; rested 2.5/5; coffee at 07:00, 11:00, and 15:30; phone email in bed.

```
# Sleep audit — Priya
Readiness: GO | Clinical route: none

## Your log, summarised  (10 nights; confidence Medium — estimates)
Time in bed ~7.0 h weekdays · estimated sleep ~6.2 h · wake range 06:30–09:10 · weekend shift 2.5 h · rested 2.5/5

## Nine factors
| Wake regularity  | 06:30 wkdays, ~09:00 wkends | ±30–60 min | yes — 2.5 h shift |
| Sleep opportunity| 23:30–06:30 = 7 h in bed    | allows 7+ h sleep | yes — too short |
| Morning light    | indoors until 09:00          | outdoor within ~1 h | some |
| Evening screens  | work email in bed 3–4 nights | calmer last hour | yes |
| Caffeine         | last cup 15:30, bed 23:30 (8 h) | none ~8 h before bed | borderline |
| Alcohol          | 1 glass wine, 2 nights       | less, earlier | low |
| Late training    | ends 20:15; bed 23:30        | fine for most | no |
| Bedroom          | dark, cool, quiet            | —   | no |
| Naps             | none                         | —   | no |

## The changes, in priority order
1. Lights out 22:45 (not 23:30) → 7.75 h in bed — why: short opportunity is driving the weekend lie-in.
2. Weekend wake by 07:30 — why: 2.5-h shift; the earlier bedtime should make this tolerable.
3. No work email after 22:00; phone charges outside the bedroom — why: 3–4 nights of email in bed.

## Two-week experiment
Measure: rested score | Counts as helped if: average ≥ 3.5/5 in week 2 | Review: 2026-10-08

## Not included, on purpose
No sleep aids or supplements (ask a clinician or pharmacist) · no diagnosis
```

## Techniques Used

- **QA-08 Gate-Based Verification** — the clinical-route screen runs before any audit.
- **RT-02 Multi-Dimensional Analysis Framework** — nine fixed factors against general guidance.
- **DS-06 Prioritization and Severity Guidance** — regularity and opportunity first; 2–3 changes.
- **QA-04 Uncertainty Acknowledgment** — confidence on estimated logs and tracker data.

## Related Prompts

- `domain-health-wellness/foundations/wellness_readiness_and_red_flag_screen.md` — the gate and its sleep flags.
- `domain-psychology/client-self-use/coping-by-concern/clientself_sleep_cbt_i_sleep_restriction_calculator.md` —
  structured treatment for an insomnia pattern, with its own safety carve-outs.
- `domain-health-wellness/foundations/wellness_sustainable_routine_designer.md` — the weekly routine the sleep anchor sits in.
