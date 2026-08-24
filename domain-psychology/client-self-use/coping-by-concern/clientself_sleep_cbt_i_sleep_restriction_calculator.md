---
title: "CBT-I Sleep Restriction Calculator (Client-Side)"
category: psychology/client-self-use/coping-by-concern
description: "Help a client implement the sleep restriction component of CBT-I (Cognitive Behavioral Therapy for Insomnia) — calculate sleep window, set bedtime/wake time, manage daytime sleepiness, and titrate."
techniques:
  - ST-04
  - DT-02
  - DS-02
  - QA-04
difficulty: intermediate
tags:
  - client-self-use
  - insomnia
  - cbt-i
  - sleep-restriction
  - sleep-efficiency
intended_use: model-testing
updated: "2026-05-08"
---

# CBT-I Sleep Restriction Calculator (Client-Side)

## Objective

Help a client implement sleep restriction (the most powerful component of CBT-I) safely and correctly: calculate the prescribed sleep window from a sleep diary, set a bedtime / rise-time pair, manage transient daytime sleepiness, and titrate weekly based on sleep efficiency.

## When to Use

- Chronic insomnia (≥ 3 months, ≥ 3 nights/week with onset, maintenance, or early-morning-waking).
- Already attempting sleep hygiene with limited success.
- Working with a clinician on CBT-I who wants the client to come prepared.
- Without a clinician but motivated to attempt the protocol.

## When NOT to Use (safety carve-outs)

- Bipolar disorder (sleep restriction can trigger mania).
- Active SI (severe sleep deprivation worsens risk).
- Untreated sleep apnea (restriction without CPAP is contraindicated).
- Seizure disorder (sleep restriction can lower threshold).
- Occupational driving / safety-sensitive work without time-off cushion (transient daytime sleepiness affects safety).
- Pregnancy (titration parameters differ).

## Inputs / Context

- 1–2 weeks of sleep diary: time to bed, time to fall asleep, awakenings (count + duration), final wake time, time out of bed, daytime naps.
- Current bedtime / wake time pattern.
- Mandatory wake time (work, kids, alarm).
- Whether client has a CPAP / sleep apnea has been ruled out.
- Whether bipolar / SI / seizure / pregnancy contraindications apply.
- Caffeine, alcohol, screen, exercise patterns.

## Constraints

### Must

- Output sections: **Safety Check**, **Sleep Diary Summary**, **Calculate Total Sleep Time and Sleep Efficiency**, **Prescribed Sleep Window**, **Bedtime / Rise Time**, **Titration Rules (week by week)**, **What to Expect (transient daytime sleepiness)**, **What NOT to Do**, **When to Stop or Reach Clinician**.
- Calculation:
  - Average Total Sleep Time (TST) = mean of nightly sleep across the diary.
  - Average Time in Bed (TIB) = mean of nightly time in bed.
  - Sleep Efficiency (SE) = TST / TIB × 100.
  - Prescribed Sleep Window = TST (rounded up to nearest 15 min); minimum window = 5 hours (do not go below — even with poor sleep, do not prescribe < 5 h).
- Titration: each week, if SE ≥ 85% → expand window 15 min; SE 80–85% → hold; SE < 80% → contract 15 min.
- Wake time is fixed first; bedtime moves to create the window.

### Must Not

- Don't prescribe a window < 5 hours.
- Don't apply with any safety carve-out present.
- Don't mix with sleep medication titration (clinician decision).
- Don't use during a mood episode.

## Instructions

1. Run safety check; if any contraindication, redirect to clinician.
2. Summarize the sleep diary.
3. Compute TST and SE.
4. Calculate prescribed window.
5. Set wake time (fixed) and bedtime (window-derived).
6. Provide titration rules.
7. Set expectations and danger flags.

## Output Format

```
=== CBT-I SLEEP RESTRICTION — WEEK 1 PRESCRIPTION ===

SAFETY CHECK
Bipolar / cycling mood: [No / Yes — STOP, do not implement; coordinate with prescriber]
Active SI: [No / Yes — STOP; risk-assess and reach clinician]
Untreated sleep apnea: [No / On CPAP / Yes untreated — STOP; treat apnea first]
Seizure disorder: [No / Yes — STOP, coordinate]
Pregnancy: [No / Yes — coordinate]
Safety-sensitive driving / work without cushion: [No / Yes — coordinate timing]

If any STOP above → don't proceed. Reach a CBT-I-trained clinician.

SLEEP DIARY SUMMARY (1–2 weeks)
Average bedtime: [...]
Average sleep onset latency: [N min]
Average # awakenings / night: [N]
Average duration of awakenings: [N min total]
Average final wake time: [...]
Average naps: [N min]

CALCULATE
Average Time in Bed (TIB) per night: [N hours]
Average Total Sleep Time (TST) per night: [N hours]
Sleep Efficiency (SE) = TST / TIB × 100 = [N%]

PRESCRIBED SLEEP WINDOW
Window = TST rounded up to nearest 15 min, minimum 5 hours
Prescribed window = [N hours, N min]

BEDTIME / RISE TIME
Mandatory wake time (fixed): [...]
Bedtime (count back the window from wake time): [...]

I do NOT get into bed before this bedtime, even if I'm sleepy.
I get OUT of bed at the wake time, every day, including weekends.
No naps in week 1.

TITRATION (weekly, after 7 nights):
- If SE ≥ 85% → expand window by 15 min (move bedtime earlier; keep wake time fixed)
- If SE 80–85% → hold for another week
- If SE < 80% → contract window by 15 min (move bedtime later); never below 5 hours

WHAT TO EXPECT (transient daytime sleepiness)
- Days 3–10 will likely be the hardest — sleepy in the day, harder to work.
- This is the protocol working. Sleep drive needs to build to break the insomnia loop.
- By week 2, sleep onset typically improves; by week 3–4, sleep is consolidating.
- Drowsy driving is the highest risk during this phase. If feeling unsafe behind the wheel, do not drive.

WHAT NOT TO DO
- Do not get into bed early "just to rest."
- Do not nap (week 1).
- Do not lie awake in bed > 20 min — get up, do something dim and quiet, return when sleepy.
- Do not catch up on weekends — fixed wake time.
- Do not drink alcohol to sleep — alcohol fragments sleep and tanks SE.
- Do not start or change sleep medication without prescriber.

WHEN TO STOP OR REACH CLINICIAN
- Daytime sleepiness affecting driving safety
- Mood deterioration (depression / hypomania) — bipolar contraindication
- Worsening SI
- Onset of new physical symptoms
- After 4 weeks if no improvement → reach a CBT-I-trained clinician

This is one component of CBT-I. The full protocol also includes stimulus control, cognitive restructuring around sleep, and relaxation. Sleep restriction is the most powerful single component.
```

## Verification

- [ ] Safety check executed; STOP triggered if any contraindication.
- [ ] Sleep diary summarized.
- [ ] TST and SE calculated.
- [ ] Prescribed window ≥ 5 hours.
- [ ] Wake time fixed; bedtime derived.
- [ ] Titration rules clear.
- [ ] Transient sleepiness expectations set.
- [ ] Driving-safety flag.
- [ ] What-not-to-do explicit.
- [ ] Escalation triggers present.
