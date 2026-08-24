---
title: "After-Visit Summary Generator"
category: domain-healthcare-clinical/workflow
description: "Translate a clinical encounter into a patient-facing after-visit summary at the right reading level — what we found, what changed, what to do, and when to come back."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
difficulty: intermediate
tags:
  - workflow
  - patient-education
  - after-visit-summary
  - health-literacy
updated: "2026-06-19"
---

## Objective

Convert the clinical content of a visit into an after-visit summary (AVS) the patient can actually understand and act on: a plain-language recap of what was discussed, what medications changed, what they need to do, what's been ordered, and when to follow up or seek urgent care. The summary must be accurate to the clinical plan, written at an accessible reading level, and free of jargon — while preserving the specifics (drug names, doses, dates) the patient needs.

## Inputs

- The encounter's assessment and plan (diagnoses addressed, decisions made)
- Medication changes (started, stopped, dose-changed) with the patient-facing reason
- Orders placed: labs, imaging, referrals
- Follow-up interval and any conditional follow-up ("sooner if...")
- Patient factors: preferred language, health-literacy considerations, target reading level (default ~6th–8th grade)
- Specific self-care or monitoring instructions (home BP, glucose logging, wound care)

## Role

The clinician writing the takeaway the patient will actually read at home — clear, warm, specific, and safe.

## Reasoning Steps

1. **Lead with what happened in one or two plain sentences.** "We talked about your blood pressure and diabetes today. Your numbers have improved." Orient before detail.

2. **Translate each diagnosis into plain language** without dumbing it down to the point of inaccuracy. "Your kidneys are working at a reduced level (stage 3 kidney disease)" — name it, explain it, keep the medical term in parentheses so it carries forward to other clinicians.

3. **Make medication changes unmistakable.** State exactly what changed, the new instruction, and why, in patient terms. "STOP taking lisinopril. START taking losartan 50 mg, one pill every morning. We changed this because lisinopril was giving you a cough." Bold or separate the action verbs (START/STOP/CHANGE) so they can't be missed.

4. **List what to do, as concrete tasks.** Get the blood test before your next visit. Check your blood pressure at home twice a week and write it down. Schedule the mammogram. Each item is an action the patient can complete and check off.

5. **State what was ordered and what happens next** — which labs, which referrals, who will call them, and what to do if they don't hear back. Closing the loop is a patient-safety function, not just courtesy.

6. **Give clear follow-up and return precautions.** When to come back, and the specific symptoms that mean "don't wait — call or go to the ER." Make the urgent symptoms concrete and tied to their conditions.

7. **Control reading level and tone.** Short sentences, common words, no unexplained abbreviations, active voice, second person. Respect the patient — accessible is not condescending. Honor language and literacy inputs.

8. **Stay faithful to the clinical plan.** Do not soften a serious finding into vagueness, and do not introduce instructions the encounter didn't include. If the plan is serious, the summary should be clear about it without inducing panic.

## Output Format

```
WHAT WE DID TODAY:
[1–2 plain sentences]

WHAT WE TALKED ABOUT (your health conditions):
- [condition in plain language (medical term)] — [one line on where it stands]

YOUR MEDICINE CHANGES:
- START / STOP / CHANGE: [drug, dose, how to take it] — [plain reason]
- (Medicines that stay the same: [brief list])

WHAT YOU NEED TO DO:
1. [concrete task]
2. ...

TESTS AND REFERRALS WE ORDERED:
- [test/referral] — [who follows up, what to expect]

YOUR NEXT VISIT:
- [when] — [purpose]

CALL US OR GO TO THE ER IF:
- [specific warning symptoms tied to their conditions]

QUESTIONS? [how to reach the office]
```

## Worked Example

**Input:** Visit per the pre-visit example. Plan: A1c improved to 7.2; continue meds. Switched lisinopril → losartan 50 mg daily due to cough. Ordered colonoscopy and mammogram referrals, low-dose chest CT for lung screening. Diabetic foot exam normal. Recheck in 3 months with labs first. Target ~7th-grade reading level, English.

**Output:**

```
WHAT WE DID TODAY:
We checked on your diabetes and blood pressure. Your diabetes numbers have improved, and your foot exam was normal. We also set up some routine cancer screening tests.

WHAT WE TALKED ABOUT (your health conditions):
- Diabetes (type 2) — Your 3-month average sugar (A1c) went down to 7.2. This is good progress. Keep going.
- High blood pressure — Still being treated. We changed one of your medicines (see below).

YOUR MEDICINE CHANGES:
- STOP: lisinopril. You no longer need to take this.
- START: losartan 50 mg. Take 1 pill every morning. We switched you because lisinopril was causing your cough. Losartan treats your blood pressure the same way but should not cause the cough.
- Medicines that stay the same: metformin, dapagliflozin, and atorvastatin — keep taking these as before.

WHAT YOU NEED TO DO:
1. Get your blood tests done at the lab before your next visit (about 3 months from now).
2. Watch for any new cough or swelling after starting losartan, and let us know.
3. Schedule your colonoscopy — our office will help set this up.
4. Schedule your mammogram.
5. Schedule your lung scan (a low-dose CT). This is recommended because of your past smoking.

TESTS AND REFERRALS WE ORDERED:
- Colonoscopy, mammogram, and a low-dose chest CT for lung cancer screening. Our staff will call you to schedule. If you don't hear from us in 1 week, please call.
- Blood work (A1c, kidney function, cholesterol) — do this before your next visit.

YOUR NEXT VISIT:
- In about 3 months, to recheck your diabetes and blood pressure and review your test results.

CALL US OR GO TO THE ER IF:
- You feel dizzy or faint, especially when standing up.
- Your blood sugar is very high (over 300) with nausea or trouble breathing.
- You have swelling of your face, lips, or tongue, or trouble breathing after the new medicine — go to the ER.
- You have a fall or new chest pain.

QUESTIONS? Call the office at [number] or send us a message through the patient portal.
```
