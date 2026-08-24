---
title: "CBT-I — Provider Sleep Protocol (Sleep Restriction, Stimulus Control, Titration)"
category: psychology/specialty-clinical
description: "Generate a CBT-I session plan that computes prescribed time-in-bed from sleep-diary data, applies stimulus control, and titrates by sleep efficiency."
techniques:
  - ST-04
  - RT-02
  - DS-02
  - NE-02
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - cbt-i
  - insomnia
  - sleep-restriction
  - stimulus-control
  - sleep-efficiency
  - spielman-3p
intended_use: model-testing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/specialty-clinical/psychology_insomnia_comorbid_with_pain_or_ptsd.md
  - domain-psychology/client-self-use/coping-by-concern/clientself_sleep_cbt_i_sleep_restriction_calculator.md
  - domain-psychology/treatment-planning/psychology_relapse_prevention_plan_designer.md
---

# CBT-I — Provider Sleep Protocol (Sleep Restriction, Stimulus Control, Titration)

## Objective
Generate a single CBT-I (Cognitive Behavioral Therapy for Insomnia) session plan within the manualized 4–8 session protocol described by Edinger & Carney (*Overcoming Insomnia*) and Perlis et al. (*Cognitive Behavioral Treatment of Insomnia: A Session-by-Session Guide*), grounded in Spielman's 3P (predisposing/precipitating/perpetuating) model. The plan derives quantitative parameters from a 1–2 week prospective sleep diary — total sleep time (TST), time in bed (TIB), and sleep efficiency (SE = TST/TIB) — and operationalizes the active ingredients: **sleep restriction therapy** (set prescribed TIB near average TST to consolidate sleep, then titrate), **stimulus control** (Bootzin's rules to re-pair bed with sleep), sleep-hygiene correction (necessary but not sufficient), cognitive restructuring of dysfunctional beliefs about sleep, and relapse prevention. The Insomnia Severity Index (ISI) and ongoing diary anchor outcome monitoring. The clinical frame is data-driven and protocol-faithful; the prescribed schedule comes from the diary, not from preference.

## When to Use
- Chronic insomnia disorder (≥3 nights/week, ≥3 months) confirmed, with a completed prospective sleep diary.
- Session 2+ where the diary supports computing a sleep-restriction prescription.
- Titration sessions adjusting TIB based on the prior week's SE.
- Comorbid insomnia where CBT-I is delivered alongside treatment of the comorbidity.
- Not appropriate before a screen for untreated obstructive sleep apnea, bipolar disorder, seizure disorder, or occupational driving hazards — sleep restriction can destabilize bipolar disorder and the transient sleepiness it induces is dangerous for drivers and untreated OSA; coordinate/screen first.

## Inputs / Context
- 1–2 weeks of prospective sleep-diary data: bedtime, lights-out, sleep-onset latency, wake after sleep onset (WASO), final wake, rise time → TST, TIB, SE.
- ISI score and trajectory; insomnia subtype (onset / maintenance / mixed / early-morning).
- Dysfunctional beliefs about sleep (catastrophizing daytime impact, unrealistic sleep-need expectations).
- Substances affecting sleep (caffeine, alcohol, nicotine), hypnotic use, shift schedule.
- `[clinician input required: screen results for OSA, restless legs, bipolar disorder, seizure disorder, and any occupational driving/safety-sensitive duties]`
- `[clinician input required: the average TST from the diary used to set the initial TIB prescription]`
- `[clinician input required: comorbid conditions and any coordination needed (e.g., chronic pain, PTSD, prescriber)]`

## Constraints

### Must
- Compute the prescribed TIB from the diary's **average TST** (not from desired sleep), and set a fixed rise time.
- Hold a **TIB floor of about 5 hours** — do not prescribe below ~5h even if average TST is lower; document the floor.
- Titrate by sleep efficiency: when SE ≥ ~85–90% over the week, increase TIB by ~15–20 min; when SE < ~80–85%, decrease TIB by ~15 min (or hold), per protocol thresholds.
- Specify stimulus-control (Bootzin) rules explicitly: bed only for sleep (and sex); out of bed if awake ~15–20 min and not sleepy; return only when sleepy; fixed rise time; no daytime naps.
- Treat sleep hygiene as necessary-not-sufficient; do not present it as the primary intervention.
- Warn about and document the expected transient daytime sleepiness during restriction and its safety implications for driving/safety-sensitive work.
- State the CPT code and a coordination/risk hook for bipolar or untreated OSA.

### Must Not
- Must not prescribe TIB below the ~5-hour floor.
- Must not initiate sleep restriction without the bipolar/OSA/seizure/occupational-safety screen.
- Must not set the prescription from the patient's desired sleep duration rather than measured TST.
- Must not present sleep hygiene as sufficient treatment or substitute it for restriction + stimulus control.
- Must not fabricate diary values, SE percentages, or ISI scores — all derive from the diary and instrument.

## Instructions
1. Confirm the diary covers ≥1 week and complete the OSA/bipolar/seizure/occupational-safety screen; if any flag, switch output to a coordination note and stop or modify.
2. Compute average TST, TIB, and SE from the diary; record the arithmetic.
3. Set the prescription: fixed rise time; TIB = average TST (≥5h floor); derive prescribed bedtime.
4. Apply the titration rule from last week's SE if this is a follow-up (increase/decrease/hold by the stated thresholds).
5. Specify the full stimulus-control rule set.
6. Add cognitive restructuring for one identified dysfunctional sleep belief.
7. Document the daytime-sleepiness safety warning and any driving/occupational precaution.
8. Assign the next diary, the schedule, and a single behavioral target.
9. Complete the outcome/risk block, billing, and coordination line.

## Output Format
```
=== CBT-I SESSION PLAN ===
Patient: [initials]    Session #: [n] of [4-8]    Date: [date]
Insomnia subtype: [onset/maintenance/mixed/early-morning]    ISI (latest): [score]
Safety screen: OSA [ ]  Bipolar [ ]  Seizure [ ]  Safety-sensitive driving/work [ ]

--- DIARY-DERIVED PARAMETERS ---
Avg TST: [h:mm]    Avg TIB: [h:mm]    Sleep efficiency (SE = TST/TIB): [%]
(Show arithmetic: TST [min] / TIB [min] = SE)

--- SLEEP-RESTRICTION PRESCRIPTION ---
Fixed rise time: [time]    Prescribed TIB: [h:mm] (>= 5h floor: [Y])
Prescribed bedtime/earliest-to-bed: [time]
Titration applied (from last week SE): [+15-20 min / -15 min / hold — rule cited]

--- STIMULUS CONTROL (Bootzin) ---
- Bed for sleep (and sex) only
- Out of bed if awake ~15-20 min and not sleepy; return when sleepy
- Fixed rise time every day
- No daytime naps
- [patient-specific notes]

--- COGNITIVE WORK ---
Dysfunctional belief targeted: "[verbatim]"    Restructuring: [plan]

--- SLEEP HYGIENE (necessary, not sufficient) ---
Corrections: [caffeine/alcohol/light/screens as relevant]

--- SAFETY WARNING ---
Transient daytime sleepiness expected during restriction.
Driving / safety-sensitive precaution: [specific]

--- HOMEWORK ---
Adhere to schedule + stimulus-control rules; complete sleep diary nightly.
Single behavioral target: [specific]

--- OUTCOME / RISK ---
Risk/coordination: [bipolar destabilization or untreated OSA -> coordinate; prescriber]
Disposition: [continue / titrate / coordinate]

--- BILLING ---
CPT: [90834 (45 min) | 90837 (60 min) | 96158 (health-behavior intervention, initial 30 min)]
Clinician: ______________  Co-sign (if high-acuity comorbidity): ______________
```

## Verification
- [ ] Prescribed TIB is computed from measured average TST, not desired sleep.
- [ ] TIB floor of ~5 hours is respected and documented.
- [ ] SE is calculated with arithmetic shown; titration follows the stated SE thresholds.
- [ ] Full Bootzin stimulus-control rule set is specified.
- [ ] Sleep hygiene is framed as necessary-not-sufficient, not the primary intervention.
- [ ] OSA/bipolar/seizure/occupational-safety screen completed before initiating restriction.
- [ ] Daytime-sleepiness safety warning and driving precaution documented.
- [ ] CPT and coordination/risk hook present.
- [ ] No fabricated diary values, SE percentages, or ISI scores — all derive from the diary and instrument.
