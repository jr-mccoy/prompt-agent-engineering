---
title: "Death Note / Pronouncement"
category: domain-healthcare-clinical/workflow
description: "Generate a death note documenting the pronouncement — absence of vital signs examined, time of death, events leading up, family and attending notification, and autopsy/organ-donation disposition."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - documentation
  - death-note
  - pronouncement
  - end-of-life
updated: "2026-10-06"
---

> **Medical disclaimer — read before use.** This prompt is a decision-support and
> teaching aid for **licensed clinicians**. It is **not medical advice** and is not for
> patients to diagnose or treat themselves. Drug doses, thresholds and guideline
> references in it and in its worked example may be incomplete, outdated or wrong:
> verify each one against the current guideline, the product label and your local
> formulary, and follow your institution's protocols. It does not replace examination
> or clinical judgment. **Medical emergency: call your local emergency number (911 in
> the US).**
>
> **Review status:** AI-assisted content, reviewed by AI only (2026-10-06);
> **not yet reviewed by a licensed clinician.**

## Objective

Produce a death note that documents a pronouncement to the required standard: the examination confirming absence of vital signs, the time of death, a brief account of the terminal events and the patient's condition leading up to it, and the required notifications and disposition items (attending, family, medical examiner/coroner referral if applicable, autopsy discussion, organ/tissue donation). The note is a legal record and must be precise and factual.

## Inputs

- Patient and the clinical context (admitting/terminal diagnosis, code status — DNR/DNAR vs. full code, comfort care)
- Circumstances of death (expected/comfort care vs. failed resuscitation)
- Time the clinician was called and time of examination
- Examination findings confirming death
- Time of death pronounced
- Notifications made (attending, family, who was present)
- Medical examiner/coroner reportability, autopsy discussion, organ/tissue donation referral status

## Role

Clinician performing and documenting the pronouncement.

## Reasoning Steps

1. **State the context briefly.** Who the patient was, the terminal diagnosis, and the code status/goals (e.g., comfort-focused care with DNR, or post-failed-resuscitation). One or two sentences orient the reader to whether this death was expected.

2. **Document the call and the examination.** Time called to evaluate, time of examination at bedside.

3. **Record the pronouncement exam explicitly** — the findings that confirm death: unresponsive to verbal and tactile/noxious stimulus, no spontaneous respirations observed over an adequate period, no heart sounds on auscultation, no palpable pulses, pupils fixed and non-reactive. These specific findings are the substance of a valid pronouncement.

4. **State the time of death** clearly (the time of pronouncement, per institutional convention).

5. **Summarize the terminal events** proportionate to the situation — for an expected comfort-care death, the trajectory and that the patient appeared comfortable; for an arrest, reference the resuscitation event/note and that efforts were terminated.

6. **Document notifications:** attending physician notified (time), family notified or present at bedside, and the chaplain/support if involved. This is both a courtesy and a required element.

7. **Address disposition items:** whether the case is reportable to the medical examiner/coroner (unexpected, unnatural, or statutorily required deaths), whether autopsy was discussed with the family and their decision, and whether the organ/tissue donation organization was notified (often required by regulation regardless of candidacy).

8. **Remain factual and respectful.** No speculation about cause beyond what is known; the note records the pronouncement and process, not a forensic conclusion.

## False-Positive Prevention

❌ **DON'T:**
- Fill the "[period]" of observation with a customary duration, name pulse sites (carotid, femoral) or add "bilaterally" to the pupil finding when the input gives no such detail — the pronouncement examination is the legal substance of the note.
- Record a notification time ("attending notified at 14:40"), a chaplain visit or an autopsy conversation that the input does not contain.
- Default "Medical examiner/coroner: Not reportable" because the death was expected — reportability follows jurisdiction-specific criteria (recent fall or fracture, surgery within a statutory window, injury, custody); check the input for them or write `[confirm against local ME criteria]`.
- Use the time the nurse called or the time of examination as TIME OF DEATH when the input gives a separate pronouncement time.

✅ **DO:**
- Reconcile the clock times in order — called ≤ examined ≤ pronounced ≤ notifications — each traced to the input; an out-of-order sequence is flagged to the clinician, not smoothed.
- Check that DISPOSITION answers all three items (ME/coroner, autopsy, organ/tissue donation agency) with the source of each answer; an absent one reads `[not documented]`.
- Confirm the code status in CONTEXT matches the input (DNR/comfort care vs full code after failed resuscitation); after a failed resuscitation, reference the code note's time and do not re-narrate the arrest.

## Output Format

```
DEATH NOTE

CONTEXT: [patient, terminal diagnosis, code status/goals — expected vs. resuscitation]

CALLED TO EVALUATE: [time] | EXAMINED: [time]

PRONOUNCEMENT EXAMINATION:
- Unresponsive to verbal and tactile/noxious stimuli.
- No spontaneous respirations over [period] of observation.
- No heart sounds on auscultation; no palpable central pulses over [period].
- Pupils fixed and non-reactive.

TIME OF DEATH: [time]

TERMINAL EVENTS: [brief account; reference code note if applicable]

NOTIFICATIONS:
- Attending physician: [name, time notified]
- Family: [notified/present, who]
- Spiritual care/support: [if involved]

DISPOSITION:
- Medical examiner/coroner: [reportable? referred? case number if applicable]
- Autopsy: [discussed with family — decision]
- Organ/tissue donation: [organization notified per protocol — status]
```

## Worked Example

**Input:** 84 y/o F with metastatic pancreatic cancer, transitioned to comfort-focused care 3 days ago, DNR/DNAR. On a morphine infusion for comfort; per nursing, declining over the past days and appearing comfortable without distress. Family at bedside. Nurse called clinician at 14:32 reporting patient appeared to have stopped breathing. No resuscitation attempted (DNR). Examined at 14:35. Found unresponsive, no respirations over 2 minutes, no heart sounds or pulses over 1 minute, pupils fixed. Pronounced 14:37. Attending notified at 14:40. Family present. Death expected/natural from known terminal illness — not ME-reportable. Autopsy declined by family. Organ procurement organization notified per hospital policy; not a donation candidate given metastatic malignancy.

**Output:**

```
DEATH NOTE

CONTEXT: 84 y/o F with metastatic pancreatic cancer, transitioned to comfort-focused care 3 days prior with DNR/DNAR status, on a morphine infusion for symptom control. Death was anticipated as a natural progression of her terminal illness.

CALLED TO EVALUATE: 14:32 | EXAMINED: 14:35.

PRONOUNCEMENT EXAMINATION:
- Unresponsive to verbal and tactile/noxious stimuli.
- No spontaneous respirations observed over 2 minutes of observation.
- No heart sounds on auscultation; no palpable pulses over 1 minute [pulse sites not recorded].
- Pupils fixed.

TIME OF DEATH: 14:37.

TERMINAL EVENTS: Patient had been declining over the preceding days on comfort-focused care, appearing comfortable without signs of distress on the morphine infusion. She became unresponsive and apneic, with the nurse summoning the clinician at 14:32. No resuscitative measures were undertaken, consistent with her DNR/DNAR status and goals of care.

NOTIFICATIONS:
- Attending physician notified at 14:40.
- Family was present at the bedside at the time of death.
- Spiritual care: [not documented].

DISPOSITION:
- Medical examiner/coroner: Not reportable per clinician (input) — expected natural death from a known terminal illness [confirm against local ME criteria].
- Autopsy: Discussed with family; declined.
- Organ/tissue donation: Organ procurement organization notified per hospital policy; patient not a candidate given metastatic malignancy.
```
