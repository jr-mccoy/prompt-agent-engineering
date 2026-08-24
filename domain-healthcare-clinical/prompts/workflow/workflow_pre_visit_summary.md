---
title: "Pre-Visit Planning Summary"
category: domain-healthcare-clinical/workflow
description: "Build a pre-visit summary that tells the clinician what to accomplish at the upcoming appointment: what's due, what's unresolved, and what data to have in hand before walking in."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - workflow
  - pre-visit-planning
  - primary-care
  - care-gaps
updated: "2026-06-19"
---

## Objective

Produce a pre-visit summary that lets a clinician walk into an appointment already knowing the agenda: the chronic conditions due for review, the open loops from last visit, the care gaps to close, the labs that should be drawn (ideally before the visit), and the patient-reported reason for coming. The goal is to convert a reactive visit into a planned one — nothing important deferred to "next time" because no one remembered it.

## Inputs

- Visit type and interval since last visit (annual wellness, chronic-disease follow-up, problem-focused)
- Active problem list and current medications
- Last visit's plan and any deferred items
- Most recent labs/vitals and what's overdue
- Care gaps: screenings, immunizations, chronic-disease monitoring intervals
- Patient-reported reason for the visit, if scheduled with one
- Pending results or specialist notes received since last visit

## Role

Primary care attending doing the night-before chart review that makes the next day's visit efficient and complete.

## Reasoning Steps

1. **Anchor on the visit's purpose and interval.** A 3-month diabetes follow-up has a different agenda than a Medicare annual wellness visit. State why the patient is coming and what the visit type obligates you to cover.

2. **Pull last visit's plan forward.** What was deferred, what was started and needs reassessment, what the patient was told to do (med titration, lifestyle change, get a study). The single most common failure mode is losing the thread between visits.

3. **For each active chronic problem, state where it stands and what this visit should do.** Is it controlled? When was it last objectively assessed? Is a med titration or monitoring lab due? Give the clinician the trajectory and the next action, not just the diagnosis.

4. **Order labs to be drawn before the visit where possible.** A1c, lipid panel, CMP, INR, TSH, drug levels due now — flag them so they're resulted in time to act on during the visit rather than triggering a callback. List exactly what's due based on the condition-specific monitoring interval.

5. **Surface care gaps.** Screenings overdue (colorectal, mammography, cervical, lung, AAA, bone density), immunizations due, condition-specific monitoring (diabetic eye/foot exam, ACR, CKD labs). Map each gap to the action that closes it.

6. **Reconcile medications** — flag refills coming due, anything that needs monitoring, and any high-risk combination or recent change to revisit.

7. **Integrate new information received since last visit** — ED visits, specialist recommendations, abnormal results — and turn each into an agenda item.

8. **Produce a ranked agenda** so that if the visit runs short, the highest-yield items are covered first. Do not pad with items the record doesn't support; if data is missing to plan an item, say what to obtain.

## Output Format

```
VISIT: [type, date, interval since last] | PATIENT-REPORTED REASON: [if any]

ONE-LINER: [age, sex, key active problems]

CARRY-FORWARD FROM LAST VISIT:
- [deferred items, started-and-needs-reassessment, patient action items]

CHRONIC PROBLEM AGENDA:
- [problem] — [current status + last objective data] → THIS VISIT: [action]

LABS DUE (order before visit if possible):
- [test + why/interval]

CARE GAPS TO CLOSE:
- [screening/immunization/monitoring + action]

MEDICATION REVIEW:
- [refills due, monitoring needed, changes to revisit]

NEW SINCE LAST VISIT:
- [ED visits, specialist input, abnormal results → agenda item]

RANKED VISIT AGENDA:
1. [highest-yield item]
2. ...

DATA NEEDED TO COMPLETE PLANNING: [anything missing from the chart]
```

## Worked Example

**Input:** 67 y/o F, 6-month follow-up for T2DM and HTN. Last visit: started on dapagliflozin, told to get retinal screen, A1c was 8.3. Since then: ED visit 2 months ago for a fall, no fracture. Last colonoscopy 11 years ago. Mammogram 3 years ago. Smoker, quit 5 years ago, 25 pack-years. On metformin, dapagliflozin, lisinopril, atorvastatin.

**Output:**

```
VISIT: T2DM + HTN follow-up, 6-month interval | PATIENT-REPORTED REASON: routine follow-up.

ONE-LINER: 67 y/o F with T2DM and HTN, former smoker (25 pack-years), recent mechanical fall.

CARRY-FORWARD FROM LAST VISIT:
- Dapagliflozin started — assess tolerance, BP/volume effect, recheck renal function and glucose response.
- Diabetic retinal screen was ordered last visit — confirm done; if not, re-order (overdue).
- A1c was 8.3 — reassess response to the regimen change.

CHRONIC PROBLEM AGENDA:
- T2DM — A1c 8.3 six months ago, dapagliflozin added → THIS VISIT: review repeat A1c (order pre-visit), titrate if still above goal, confirm retinal + foot exam done.
- HTN — on lisinopril → THIS VISIT: review home/clinic BP; note SGLT2i may have lowered it; check orthostatics given recent fall.

LABS DUE (order before visit):
- A1c (due, regimen changed).
- CMP/eGFR + urine ACR (diabetic + on SGLT2i and ACEi — monitor renal function and albuminuria).
- Lipid panel (annual on statin).

CARE GAPS TO CLOSE:
- Colorectal screening OVERDUE (colonoscopy 11 yr ago) → order colonoscopy or FIT.
- Mammography due (3 yr since last) → order screening mammogram.
- Lung cancer screening — meets criteria (25 pack-years, quit <15 yr ago, age 67) → order low-dose chest CT, counsel.
- Diabetic foot exam this visit; confirm retinal screen.
- Bone density — given age 67 + recent fall, screen DXA if not done.
- Immunizations: confirm pneumococcal, annual influenza, RSV (age-eligible), shingles status.

MEDICATION REVIEW:
- Confirm dapagliflozin tolerance (genital infections, volume); ensure metformin appropriate at current eGFR (check pre-visit labs).
- Refills: review all four for 90-day continuation.

NEW SINCE LAST VISIT:
- ED visit 2 months ago for a fall, no fracture → THIS VISIT: falls assessment (orthostatics, gait, med review for hypotension/hypoglycemia risk, vision, home hazards). The recent SGLT2i and ACEi raise orthostatic-fall relevance.

RANKED VISIT AGENDA:
1. Falls assessment + orthostatics (safety, recent event).
2. Diabetes control: A1c review, retinal/foot exam, titration.
3. Renal/albuminuria monitoring on SGLT2i + ACEi.
4. Close overdue cancer screenings (colorectal, mammogram, lung CT).
5. Immunization catch-up, DXA, med refills.

DATA NEEDED TO COMPLETE PLANNING: Confirm whether the previously ordered retinal screen was completed; obtain ED records from the fall if not already in chart.
```
