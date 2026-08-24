---
title: "Substance Use Disclosure Rehearsal — Screening, Brief Intervention, Stigma-Resistant Language"
category: medical-education/learner-osce-skills
description: "Rehearse an encounter where substance use is the focus or surfaces incidentally. SP holds defined use pattern, stage of change, and disclosure threshold (will disclose more honestly if learner avoids stigmatizing language and uses validated tool framing). Scorecard evaluates SBIRT structure (Screen, Brief Intervention, Refer to Treatment), validated-tool use (AUDIT-C, DAST-10, NIDA Quick Screen, CRAFFT for adolescents), stigma-resistant language, and a workable disclosure of accurate quantity/frequency."
techniques:
  - RP-01
  - RP-04
  - ST-02
  - CM-02
  - DT-05
  - NE-04
difficulty: advanced
intended_use: model-testing
target_users:
  - medical-student-clinical
  - pa-student
  - nursing-student
  - intern
  - resident-junior
  - resident-senior
  - fellow
tags:
  - osce
  - substance-use
  - sbirt
  - stigma
  - communication
  - learner-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/learner-osce-skills/osce_motivational_interviewing_rehearsal.md
  - domain-medical-education/learner-osce-skills/osce_history_taking_rehearsal.md
  - domain-medical-education/learner-osce-skills/osce_difficult_conversation_anger_grief.md
---

## Objective

Drill a focused encounter where alcohol or other substance use is screened, discussed, and (when indicated) followed by a brief intervention with a referral plan. Output: encounter transcript + scorecard against SBIRT, validated-tool use, stigma-resistant language audit, accuracy of disclosed quantity/frequency, and MI-consistent brief intervention.

## Your Role

You are *both* the SP and the rater. As SP: hold a defined use pattern in your head; respond to stigmatizing language with under-disclosure or partial disclosure (lower the quantity); respond to validated, neutral framing with truthful disclosure. As rater: at end of station, score the rubric and report what *would have* been disclosed with optimal language ("if you had asked using the AUDIT-C framing, the truthful answer is X").

## Inputs

- `substance_focus`: `alcohol | tobacco/nicotine | cannabis | opioids-rx | opioids-illicit | stimulants | benzos-rx | benzos-illicit | poly-substance` (or free text)
- `actual_use_pattern`: detailed truthful pattern — frequency, quantity, route, duration, last use (e.g., "alcohol — 5 nights/week, 5 drinks/night, no morning use, last drink 12h ago")
- `stage_of_change`: `precontemplation | contemplation | preparation | action | maintenance`
- `disclosure_threshold`: `low | medium | high` — how easily SP discloses fully (low = only with optimal language)
- `setting_and_pretext`: free text (e.g., "annual wellness," "ED visit for trauma after fall," "prenatal first visit," "preop clearance")
- `learner_level`: `MS3 | MS4 | pa-student | nursing-student | intern | resident-junior | resident-senior | fellow`
- `withdrawal_risk_present`: `none | possible-mild | possible-severe (delirium-tremens, opioid withdrawal in pregnancy, benzo withdrawal)`
- `station_minutes`: integer (default 10)

## Method

1. **Lock the case (CM-02).** Privately commit to: truthful pattern, withdrawal risk if any, social context, prior treatment history.

2. **Open the station.** SP opens in setting role. Wait.

3. **Run SBIRT expectations (the answer key).**
   - **Screen:** open the topic with a normalizing pre-statement ("I ask everyone about alcohol and other substances — it helps me take better care of you"). Then a validated tool (AUDIT-C, NIDA Quick Screen, CRAFFT for adolescents, AUDIT or DAST-10 if positive screen).
   - **Quantify** with a *neutral* framing: "how many days per week do you have any alcohol?" then "on a typical drinking day, how many standard drinks?" Avoid "do you drink?" / "how much?" without anchoring to a standard drink definition.
   - **Brief Intervention** (if positive): feedback (compare to low-risk drinking limits or to risk profile), responsibility (decision is patient's), advice ("as your doctor I would recommend..."), menu of options (cut down vs quit; meds; counseling), empathy, self-efficacy (FRAMES).
   - **Refer to Treatment:** appropriate level (outpatient counseling, MAT initiation, intensive outpatient, withdrawal management) and named follow-up.
   - **Withdrawal risk:** if applicable, screened (CIWA-Ar awareness, last use timing, history of seizures/DTs).

4. **Run stigma-resistant language audit (NE-04).**
   - "Substance use disorder" rather than "abuse," "addict," "junkie," "alcoholic" (unless patient self-identifies).
   - "Person with opioid use disorder" rather than "opioid abuser."
   - "Positive / negative" toxicology rather than "clean / dirty."
   - "In recovery" / "not in recovery" rather than "still using."
   - No moralizing tone ("you really should know better").

5. **Disclosure response rule.** SP discloses fully when language is neutral and validated; partially when language is stigmatizing or judgmental; under-discloses or shuts down when shame is invoked. At end of station, report what would have been disclosed with optimal language.

6. **End and score (DT-05).**

## Output Format

```
OSCE STATION — Substance Use
Substance focus: [...]   Setting: [...]   Learner level: [...]   Station: [...] min
Stage of change: [...]   Withdrawal risk: [...]

>>> ENCOUNTER TRANSCRIPT

[turn-by-turn]

>>> SCORECARD — Screen

[ ✓ / ✗ ] Normalizing pre-statement
[ ✓ / ✗ ] Validated tool used (name it)
[ ✓ / ✗ ] Standard-drink definition or substance-specific quantification anchored
[ ✓ / ~ / ✗ ] Frequency probed neutrally (days/week)
[ ✓ / ~ / ✗ ] Quantity probed neutrally (units/day)

>>> SCORECARD — Brief Intervention (if positive screen)

[ ✓ / ~ / ✗ ] Feedback against guideline / risk
[ ✓ / ~ / ✗ ] Responsibility framing (decision is patient's)
[ ✓ / ~ / ✗ ] Advice ("as your doctor, I'd recommend...")
[ ✓ / ~ / ✗ ] Menu of options (cut down vs quit; meds; counseling)
[ ✓ / ~ / ✗ ] Empathy + self-efficacy
[ ✓ / ✗ ] Withdrawal risk screened (when applicable)

>>> SCORECARD — Refer to Treatment

[ n/a / ✓ / ~ / ✗ ] Appropriate level named
[ n/a / ✓ / ✗ ] Specific resource / referral routed (not "look up local AA")
[ n/a / ✓ / ✗ ] Named follow-up

>>> SCORECARD — Language audit (verbatim count)

[ count ] Stigmatizing terms used: ["abuse", "clean", "addict", "alcoholic" (non-self-applied), "junkie", "dirty UDS"]
[ count ] Moralizing / shaming phrases
[ count ] Person-first language used
[ count ] Use-disorder framing ("alcohol use disorder, mild/moderate/severe")

>>> SCORECARD — Disclosure accuracy

Disclosed quantity:        [...]
Truthful quantity (locked): [...]
Gap:                       [accurate / under-disclosed by ~N units / refused]
What would have been disclosed with optimal language: [...]

>>> COACHING (one paragraph)

Single highest-yield improvement: [...]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `substance_focus` | Drives validated tool + intervention options |
| `actual_use_pattern` | Locks the truthful answer |
| `disclosure_threshold` | How forgiving the SP is of imperfect language |
| `withdrawal_risk_present` | Adds CIWA-Ar / opioid withdrawal scaffolding |
| `setting_and_pretext` | Annual / ED / prenatal / pre-op |
| `adolescent_overlay` | Use CRAFFT; confidentiality limits |
| `pregnancy_overlay` | Heightened stakes + different referral pathway (MAT in pregnancy) |
| `prior_treatment_history` | Affects readiness + intervention shape |

## Verification Checklist

- [ ] Validated tool named explicitly when used; not "I asked about drinking."
- [ ] Standard-drink definition or substance equivalent anchored before quantification.
- [ ] Stigma audit done from verbatim transcript, not impression.
- [ ] Disclosure-accuracy gap reported as a number, with the "optimal-language" counterfactual.
- [ ] Brief Intervention scored against FRAMES elements separately.
- [ ] Withdrawal risk scored `n/a` if not applicable.
- [ ] Referral level matches severity; no overshoot (residential for a low-AUDIT score) or undershoot (handouts for severe disorder).
- [ ] No invented MAT regimens, named treatment programs, or quantitative outcomes.
- [ ] Coaching names ONE improvement.

## Worked Example (compact)

**Input:** substance_focus = `alcohol`, actual_use_pattern = `4–5 days/week, 4–5 standard drinks/day, no morning use, last drink 18h ago`, stage = `contemplation`, disclosure_threshold = `medium`, setting = `annual wellness`, learner_level = `intern`, withdrawal_risk = `none`, station_minutes = 10.

**Output (excerpt):**

```
Learner: "Mr. Petrov — at every wellness visit I ask everyone about alcohol and other substances. It helps me give better care. A standard drink is 12 ounces of beer, 5 ounces of wine, or 1.5 ounces of hard liquor. In the past year, how many days per week do you have any alcohol?"
SP: "Most weeks, four or five days."
Learner: "And on a day when you do drink, how many standard drinks would you say?"
SP: "Maybe four. Sometimes five if I'm out with friends."
[learner notes 4–5 days × 4–5 drinks = positive AUDIT-C]
Learner: "I appreciate you being direct. Where you're at — that's above the limit we consider low-risk for men, which is up to 14 drinks a week or 4 in a day. I'm not telling you that to worry you; I want to be honest with you about the data so you can make a decision that fits your life. What's your sense of where you'd want to be with this?"
SP: "Honestly — I've been thinking about it. My doctor before you didn't seem to care."
Learner: "There are a few directions people go — some cut back, some take a break, some quit entirely; we can also use medication that takes the edge off cravings. Where do you want to start? Anything you've tried before that worked or didn't?"
[...]

>>> SCORECARD — Screen

[✓] Normalizing pre-statement
[✓] AUDIT-C framing (not named explicitly but used)
[✓] Standard-drink anchored
[✓] Frequency neutral
[✓] Quantity neutral

>>> SCORECARD — Brief Intervention

[✓] Feedback against limit (14/week, 4/day for men)
[✓] Responsibility ("your decision," "fit your life")
[✓] Advice (offered without sermon)
[✓] Menu (cut back / break / quit / medication)
[✓] Empathy + self-efficacy
[n/a] Withdrawal risk (not applicable)

>>> SCORECARD — Refer to Treatment

[~] Appropriate level named (not yet specific in this excerpt)
[~] Resource not yet routed
[~] Follow-up not yet scheduled

>>> SCORECARD — Language audit

[0] Stigmatizing terms
[0] Moralizing
[multiple] Person-first / neutral language
[0] Use-disorder framing — neither stigmatizing nor (yet) diagnostic

>>> SCORECARD — Disclosure accuracy

Disclosed: 4–5 days/week, 4–5 drinks/day
Truthful: 4–5 days/week, 4–5 drinks/day
Gap: accurate
Counterfactual: n/a — disclosed accurately with optimal language

>>> COACHING

Single highest-yield improvement: close with a *specific* next step. The intervention was clean — name a target (e.g., 2 alcohol-free days/week for 2 weeks), a check-in (phone or portal at 2 weeks), and a medication option ready if he wants (naltrexone). "Where do you want to start?" is an open prompt, not a plan.
```
