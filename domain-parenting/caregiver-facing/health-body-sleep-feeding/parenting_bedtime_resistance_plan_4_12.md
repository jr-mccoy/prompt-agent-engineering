---
title: "Bedtime Resistance Plan (Ages 4–12) — Find the Driver, Then Fix It: Limit-Setting, Fears, Mistimed Bedtime, Screens, and the Snoring Signs That Go to the Pediatrician"
category: parenting/health-body-sleep-feeding
description: "Diagnose why a 4–12-year-old fights bedtime — limit-testing curtain calls, night-time fears, a bedtime set earlier than the child's body clock, screens and light, sleep-onset dependence on a parent, or an underlying sleep or mental-health problem — then apply the matched evidence-based method (bedtime pass, faded bedtime, check-in fading, worry time) with sleep-need targets, a melatonin caution, and a screen for obstructive sleep apnoea and other medical sleep disorders."
techniques:
  - DP-06
  - IT-23
  - ST-02
  - DS-01
difficulty: intermediate
intended_use: model-testing
tags:
  - parenting
  - health-body-sleep-feeding
  - bedtime-resistance
  - behavioral-insomnia
  - bedtime-pass
  - sleep-hygiene
  - sleep-apnea-screen
  - kid-wont-stay-in-bed
  - bedtime-takes-two-hours
updated: "2026-10-02"
related_prompts:
  - domain-parenting/caregiver-facing/ages-0-3/parenting_sleep_regression_decoder.md
  - domain-parenting/caregiver-facing/ages-4-8/parenting_daily_routine_designer.md
  - domain-parenting/caregiver-facing/ages-4-8/parenting_transitions_and_warnings_protocol.md
---

# Bedtime Resistance Plan (Ages 4–12)

**Objective:** Identify the dominant driver of a school-age child's bedtime
resistance, screen out medical sleep problems, and produce a three-week plan using
the method matched to that driver, with nightly scripts and a sleep log to judge it.

**When to Use:**
- Bedtime takes more than 30–45 minutes of negotiation, curtain calls, or tears.
- A child aged 4–12 leaves the room repeatedly, will only fall asleep with a parent,
  or comes into the parents' bed nightly.
- A child lies awake worrying or is "not tired" at bedtime.
- **Not this prompt if** the child is under 4 or the problem is a sudden change
  around a developmental leap — use
  `domain-parenting/caregiver-facing/ages-0-3/parenting_sleep_regression_decoder.md`.
  If the whole evening routine (homework, dinner, screens) needs rebuilding rather
  than bedtime itself, use
  `domain-parenting/caregiver-facing/ages-4-8/parenting_daily_routine_designer.md`;
  for the hand-off from play to bath to bed, see
  `domain-parenting/caregiver-facing/ages-4-8/parenting_transitions_and_warnings_protocol.md`.

## Safety Block — Medical Sleep Screen

**Raise with the pediatrician before (or alongside) a behavioural plan if:**

- **Snoring ≥3 nights a week**, gasping, pauses in breathing, mouth breathing,
  restless sleep in odd positions (neck extended), night sweats, new bedwetting,
  morning headaches, or daytime sleepiness, hyperactivity, or attention problems —
  possible **obstructive sleep apnoea** (often from enlarged tonsils/adenoids;
  treatable, and it can mimic ADHD).
- Urge to move the legs, "creepy-crawly" feelings in the evening → possible restless
  legs (iron levels can matter).
- Frequent night terrors, sleepwalking that leaves the house or risks injury, or
  episodes with stiffening or jerking (seizure screen).
- Sleep problems with low mood, panic, trauma symptoms, or worries that dominate the
  day → child mental-health assessment.
- **Melatonin:** discuss with the pediatrician before using. Over-the-counter
  products are unregulated in the US and a 2023 analysis found actual doses ranging
  from about 74% to 347% of the label; paediatric ingestion calls have risen sharply.
  It may help with sleep-onset problems in some children (notably autistic children
  under medical guidance) but does not fix limit-setting problems.
- Talk of self-harm → 988 (US) now.

## Inputs / Context

1. **Child:** age, temperament, ADHD/autism/anxiety, medications (stimulants).
2. **Current timeline:** dinner, screens off, routine start, lights out, actual
   sleep onset, night wakings, wake time (weekday vs. weekend).
3. **What happens:** curtain calls (water, toilet, one more hug), leaving the room,
   crying, fear talk, needing a parent present, devices in the room.
4. **Snoring and daytime signs** (Safety Block).
5. **Household:** shared bedroom, shift work, two homes, noise and light.

## Method

1. **Compare sleep need to sleep opportunity (DS-01).** AASM recommended totals:
   ages 3–5, 10–13 hours (including naps); 6–12, 9–12 hours. Calculate time in bed vs.
   actual sleep.
2. **Identify the dominant driver (DP-06)** from the log:
   - **Limit-setting:** stalling and curtain calls, fine once asleep, worse with one
     caregiver than another.
   - **Fears / anxiety:** fear of the dark, intruders, being alone; worry talk at
     lights-out.
   - **Mistimed bedtime:** child is genuinely not sleepy; lies awake 30+ minutes
     calmly; sleeps in on weekends — bedtime is in the body clock's pre-sleep
     "wake maintenance" window.
   - **Sleep-onset association:** can only fall asleep with a parent present or
     specific conditions; wakes and needs them again at night.
   - **Light and screens:** devices within an hour of bed or in the bedroom.
   - **Medical / mental health:** Safety Block positives.
3. **Apply the matched method (IT-23):**
   - **Limit-setting → Bedtime Pass.** One (later zero) card the child can trade
     for one brief out-of-room request; after it's used, calm, boring returns with
     no conversation. Pair with a predictable 20–30 minute routine.
   - **Fears → validate, then build bravery.** Worry time earlier in the evening
     (10 minutes, written down, "put away"); nightlight (dim, warm); a brave-practice
     ladder (parent in the hall → checks every 5, then 10, then 15 minutes);
     avoid monster spray if it confirms monsters exist for that child.
   - **Mistimed bedtime → faded bedtime.** Temporarily set lights-out to when the
     child usually falls asleep, keep wake time fixed, then move bedtime earlier by
     15 minutes every few nights once sleep onset is under 15–20 minutes.
   - **Association → check-in fading / chair method.** Parent's presence fades over
     1–2 weeks (chair by bed → doorway → hall); for night wakings, same response.
   - **Screens → device curfew.** Off 60 minutes before lights-out; charging
     outside the bedroom.
4. **Write the routine and scripts (ST-02).** Same steps nightly; visual chart for
   younger children; one brief warm script for returns ("It's sleep time. I love you.
   See you in the morning.").
5. **Keep wake time consistent** within about an hour on weekends.
6. **Log for three weeks** (lights-out, sleep onset, curtain calls, night wakings).
   Expect an "extinction burst" in nights 2–5.

## Output Format

```
# Bedtime Plan — [child, age]

## Medical sleep screen (each item: present / absent) → outcome
## Sleep need vs. opportunity (hours)
## Dominant driver (evidence) + secondary drivers
## Method selected + rules
## Evening timeline (screens off → routine → lights out → wake time)
## Scripts (first return, repeated returns, fear talk)
## Three-week log + targets
## When to re-check with the pediatrician
```

## Verification

- [ ] Medical screen done; snoring and daytime signs asked about directly.
- [ ] Sleep need compared with the actual schedule.
- [ ] One dominant driver named with evidence from the log.
- [ ] Method matches the driver.
- [ ] Wake time fixed; screen curfew set.
- [ ] Melatonin addressed only as "discuss with the pediatrician."

## False-Positive Prevention

| Misfire | What it looks like | Correction |
|---|---|---|
| Treating fear as defiance | Bedtime Pass for a terrified child | Fear needs validation and bravery steps. |
| Treating a mistimed bedtime as stalling | Fights over a 7:00 lights-out the child can't sleep at | Faded bedtime to actual sleep onset first. |
| Missing apnoea | Behaviour plan for a snoring, inattentive child | Screen and refer. |
| Melatonin as first fix | Gummies for curtain calls | Doesn't address limit-setting; pediatrician first. |
| Quitting during the extinction burst | Abandoning on night 3 | Worse before better is expected. |
| Different rules by caregiver | One parent lies down, the other doesn't | Same plan in both homes and by both adults. |

## Adaptations

- **ADHD / stimulant medication:** check dose timing with the prescriber; delayed
  sleep onset is common; movement before the routine, not during.
- **Autistic child:** visual schedule, sensory adjustments (weighted blanket only if
  age-appropriate and child can remove it), predictable sequence.
- **Shared bedroom:** stagger bedtimes; younger child down first.
- **Two homes:** share the routine card and wake time; accept small differences.

## Example Output

```
# Bedtime Plan — Ava, 7

## Medical screen
Snoring: occasional with colds only. No gasping, daytime sleepiness, or leg
complaints. → behavioural plan.

## Sleep need vs. opportunity
Need 9–12 h. Lights out 7:30, asleep ~9:00, up 6:45 → ~9.75 h sleep.

## Dominant driver
Mistimed bedtime: lies calmly awake 60–90 min, then curtain calls start out
of boredom; sleeps till 8:30 on weekends. Secondary: limit-setting.

## Method
Faded bedtime: lights-out 8:45 for 4 nights, wake 6:45 every day. When sleep
onset <20 min for 3 nights, move to 8:30, then 8:15. Bedtime Pass (1 card)
for the remaining requests.

## Evening timeline
7:45 screens off → 8:15 bath, pyjamas, teeth → 8:30 two books → 8:45 lights out.

## Scripts
Pass used: "You used your pass. Back to bed — I love you." Afterwards:
silent walk back, no eye contact or talk.

## Log + targets (3 weeks)
Sleep onset ≤20 min; curtain calls ≤1; weekend wake ≤7:45.

## Re-check
If snoring becomes regular, or daytime tiredness persists at 3 weeks →
pediatrician.
```

## Techniques Used

- **DP-06 Dominant Driver Identification** — one named driver determines the method.
- **IT-23 Symptom-Based Troubleshooting Organization** — methods indexed by what the parent observes.
- **ST-02 Structured Sequential Instructions** — fixed evening timeline and scripts.
- **DS-01 Framework Application** — AASM sleep-need ranges and behavioural insomnia types.

## Related Prompts

- `domain-parenting/caregiver-facing/ages-0-3/parenting_sleep_regression_decoder.md` — sleep changes under age 4.
- `domain-parenting/caregiver-facing/ages-4-8/parenting_daily_routine_designer.md` — the whole-day routine around bedtime.
- `domain-parenting/caregiver-facing/ages-4-8/parenting_transitions_and_warnings_protocol.md` — handling the switch from play to bed.
