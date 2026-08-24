---
title: "Care Gap Surfacer"
category: domain-healthcare-clinical/workflow
description: "Scan a patient's chart against evidence-based screening, immunization, and chronic-disease monitoring schedules to surface every open care gap with the action that closes it."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - workflow
  - care-gaps
  - preventive-care
  - quality
updated: "2026-06-19"
---

## Objective

Compare a patient's record against the applicable preventive-care and chronic-disease monitoring standards and output a complete, prioritized list of open care gaps, each paired with the specific action that closes it. The deliverable is what a panel-management or pre-visit-planning workflow needs: not "the patient is overdue for things" but "order a FIT kit, give the RSV vaccine, draw a urine ACR, schedule a DXA — here's why and when each was due."

## Inputs

- Patient demographics (age, sex, relevant risk factors: smoking, family history)
- Active problem list and current medications
- Dates of prior screenings, immunizations, and monitoring labs (or "unknown/not in chart")
- Applicable guideline set (default: USPSTF for screening, ACIP for immunizations, condition-specific society guidelines for disease monitoring)
- Any patient-specific factors that modify standard recommendations (life expectancy, prior abnormal results changing the interval, patient preference/declines)

## Role

Primary care attending running the panel-management pass that catches what reactive visits miss.

## Reasoning Steps

1. **Build the applicable schedule from the patient's profile,** not a generic checklist. Age and sex set the baseline (mammography, colorectal, cervical, AAA, bone density, lung CT eligibility). Risk factors add to it (smoking → lung CT; family history → earlier/more frequent). Conditions add monitoring (diabetes → A1c, retinal, foot, ACR; CKD → eGFR/lytes; on a DMARD → interval CBC/LFTs).

2. **For each applicable item, compare last-done date to the recommended interval** and classify: due now, overdue, up to date, or not applicable. State the interval source so the recommendation is auditable.

3. **Account for interval modifiers.** A prior abnormal result often shortens the interval (3-year colonoscopy after a polyp, not 10). Certain conditions change the rule (no routine cervical screening after appropriate hysterectomy; intensified monitoring on a new nephrotoxic drug). Apply the right rule, not the population default.

4. **Cover the three gap classes:** (a) **screening** (cancer, AAA, osteoporosis, depression, etc.); (b) **immunizations** (influenza, pneumococcal, RSV, shingles, Tdap, COVID, hepatitis where indicated); (c) **chronic-disease monitoring** (the labs/exams each active condition obligates at its interval).

5. **Don't fabricate or assume completion.** If a date is unknown/not in the chart, list it as a gap to confirm rather than guessing it's done. Missing data is itself a gap.

6. **Respect appropriateness, not just eligibility.** Flag where a guideline default may not apply — limited life expectancy, patient who has declined, screening that exceeds the upper age limit. Surface these as "consider whether still indicated," not blind orders.

7. **Prioritize and make each gap actionable.** Rank by clinical impact (an overdue diabetic eye exam in poorly controlled diabetes outranks a slightly-overdue Tdap). For each gap, give the closing action: the order, the referral, the vaccine, the lab.

## Output Format

```
PATIENT PROFILE: [age, sex, conditions, key risk factors driving the schedule]

OPEN CARE GAPS (prioritized):

SCREENING:
- [test] — Last: [date/unknown] | Due: [interval + guideline] | Status: [overdue/due] → ACTION: [order]

IMMUNIZATIONS:
- [vaccine] — Status: [due/unknown] → ACTION: [give/order]

CHRONIC-DISEASE MONITORING:
- [condition → test] — Last: [date] | Interval: [source] | Status → ACTION: [order]

CONSIDER WHETHER STILL INDICATED:
- [items where guideline default may not apply: age, life expectancy, declined]

UP TO DATE (no action):
- [brief list]

GAPS DUE TO MISSING DATA (confirm):
- [items with no date in chart]
```

## Worked Example

**Input:** 67 y/o F. Conditions: T2DM (A1c 8.3, suboptimal control), HTN, former smoker (25 pack-years, quit 5 yr ago). Chart dates: colonoscopy 11 years ago (normal), mammogram 3 years ago (normal), last diabetic retinal exam unknown, foot exam at last visit, urine ACR 14 months ago, A1c 6 months ago, influenza vaccine last fall, pneumococcal/RSV/shingles status unknown, DXA never done. USPSTF/ACIP defaults.

**Output:**

```
PATIENT PROFILE: 67 y/o F with T2DM (suboptimally controlled), HTN, former smoker (25 pack-years, quit 5 yr) — schedule driven by age, sex, diabetes, and smoking history.

OPEN CARE GAPS (prioritized):

SCREENING:
- Diabetic retinal exam — Last: unknown | Due: annual (ADA, more important with A1c 8.3) | Status: overdue/unconfirmed → ACTION: order/refer ophthalmology, confirm prior.
- Colorectal cancer — Last: colonoscopy 11 yr ago (normal) | Due: 10-yr interval → overdue → ACTION: order colonoscopy or FIT.
- Lung cancer (low-dose CT) — Meets USPSTF criteria (age 50–80, 20+ pack-years, quit <15 yr) | Status: due → ACTION: order LDCT, counsel.
- Mammography — Last: 3 yr ago | Due: biennial (USPSTF) → due/slightly overdue → ACTION: order screening mammogram.
- Osteoporosis (DXA) — Never done; recommended for women ≥65 | Status: due → ACTION: order DXA.

IMMUNIZATIONS:
- Pneumococcal — Status: unknown → ACTION: confirm; give age-/condition-appropriate series if not documented.
- RSV — Age-eligible (≥60, shared decision) → ACTION: offer.
- Shingles (RZV) — Age ≥50, status unknown → ACTION: confirm/give 2-dose series.
- Influenza — up to date (last fall) → confirm current season.
- Tdap/Td — confirm last booster within 10 yr.

CHRONIC-DISEASE MONITORING:
- T2DM → A1c — Last: 6 mo ago; with A1c 8.3, recheck at 3 mo until controlled → ACTION: order A1c now.
- T2DM/HTN → urine ACR + eGFR/CMP — Last ACR 14 mo ago | annual minimum → overdue → ACTION: order ACR + CMP.
- Diabetic foot exam — done last visit → up to date.

CONSIDER WHETHER STILL INDICATED: None limited by age/life expectancy at 67 with good functional status — all above are appropriate.

UP TO DATE (no action): Diabetic foot exam; influenza (confirm current season).

GAPS DUE TO MISSING DATA (confirm): Retinal exam date, pneumococcal/RSV/shingles/Tdap status — all listed as gaps to confirm rather than assume complete.
```
