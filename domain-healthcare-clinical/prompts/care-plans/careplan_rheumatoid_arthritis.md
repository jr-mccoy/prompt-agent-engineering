---
title: "Rheumatoid Arthritis Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build a treat-to-target rheumatoid arthritis plan: early DMARD initiation, methotrexate optimization, biologic/JAK escalation, and safety monitoring with named drugs and doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - rheumatology
  - rheumatoid-arthritis
  - dmard
  - care-plan
updated: "2026-06-19"
---

## Objective

Produce a treat-to-target rheumatoid arthritis care plan: start a conventional DMARD early, optimize methotrexate, escalate to biologic or targeted-synthetic DMARD on inadequate response, manage steroids as a bridge only, and install safety monitoring and the health-maintenance bundle. Output is a sequenced DMARD plan with a disease-activity target.

## Inputs

- Diagnosis/activity: disease duration, serology (RF, anti-CCP), inflammatory markers (ESR/CRP), disease-activity score (DAS28/CDAI), joint counts, erosions on imaging
- Prior therapy: csDMARDs/biologics/JAK tried, response, tolerability
- Safety screen: TB (IGRA), HBV/HCV, prior malignancy, infections, cardiovascular/VTE risk (relevant for JAK), pregnancy plans
- Comorbidities, hepatic/renal function, alcohol use (methotrexate), vaccination status

## Role

Rheumatologist managing rheumatoid arthritis.

## Reasoning Steps

1. **Treat early and treat-to-target.** Start a DMARD as soon as RA is diagnosed (window of opportunity); target sustained remission or low disease activity, measured by DAS28/CDAI, with regular reassessment and escalation if target not met.

2. **First-line csDMARD: methotrexate.** Start 10–15 mg weekly, titrate to 20–25 mg weekly (oral or subcutaneous for better absorption/tolerability); **co-prescribe folic acid** 1 mg daily (or 5 mg weekly) to reduce toxicity. Alternatives/components: sulfasalazine, hydroxychloroquine, leflunomide; combination csDMARD (triple therapy) is an option.

3. **Glucocorticoid bridge:** low-dose prednisone or intra-articular steroids only to bridge until DMARD takes effect (DMARDs take 6–12 weeks). Taper off — not for chronic maintenance (long-term steroid toxicity).

4. **Inadequate response to methotrexate at target dose (~3 months):** add/switch to a **biologic or targeted-synthetic DMARD**, usually continuing methotrexate:
   - **TNF inhibitor** (adalimumab, etanercept, infliximab, certolizumab, golimumab) — common first biologic.
   - **Other mechanisms:** abatacept (T-cell costim), tocilizumab/sarilumab (IL-6), rituximab (B-cell; seropositive/specific situations).
   - **JAK inhibitor** (tofacitinib, baricitinib, upadacitinib) — effective oral option; **weigh cardiovascular/VTE/malignancy safety signal**, especially in older patients with CV risk factors (ORAL Surveillance) — prefer a TNF inhibitor in higher-risk patients.

5. **Pre-biologic/JAK screening:** latent TB (IGRA/PPD) and treat if positive before starting; HBV/HCV serologies; update vaccines (live vaccines before immunosuppression); malignancy/infection history.

6. **Cycle/swap** on failure: switch mechanism class (e.g., TNF failure → IL-6 or abatacept or JAK).

7. **Health maintenance:** vaccinations (influenza, pneumococcal, COVID, recombinant zoster, hepatitis B; non-live during immunosuppression), cardiovascular risk management (RA is an independent CV risk amplifier), bone health (steroid + disease), cancer screening, smoking cessation (worsens RA and biologic response), pregnancy-compatible regimen planning (avoid methotrexate/leflunomide — switch and washout).

8. **Monitor:** disease-activity score at each visit (treat-to-target), CBC/LFTs/renal on methotrexate/leflunomide (e.g., q2–4 weeks initially then q8–12 weeks), lipids on tocilizumab/JAK, infection surveillance, TB reactivation vigilance.

## Output Format

```
DIAGNOSIS / SEROLOGY / DISEASE ACTIVITY (DAS28/CDAI) / EROSIONS:
TARGET: remission or low disease activity

INDUCTION / FIRST-LINE:
- Methotrexate: [dose, route, folic acid] (or alternative csDMARD)
- Steroid bridge (taper plan)

ESCALATION (if target not met ~3 mo):
- Biologic/tsDMARD selection + rationale (TNF vs IL-6 vs abatacept vs rituximab vs JAK safety caveat)

PRE-BIOLOGIC/JAK SCREENING:
- TB, HBV/HCV, vaccines

HEALTH MAINTENANCE:
- Vaccines, CV risk, bone, smoking, cancer screening, pregnancy planning

MONITORING:
- DAS28/CDAI cadence, CBC/LFT/renal, lipids if applicable, infection/TB

PITFALLS:
- [delayed DMARD start, chronic steroids, JAK in high CV/VTE risk, skipping TB screen, methotrexate in pregnancy]
```

## Worked Example

**Input:** 46 y/o F, new seropositive RA (RF+, anti-CCP+), symptoms 4 months, DAS28 5.6 (high), CRP elevated, early erosions on hand films. No prior DMARD. TB IGRA negative, HBV/HCV negative. Mild alcohol use. Not pregnant, no immediate plans.

**Output:**

```
DIAGNOSIS / ACTIVITY: seropositive (RF+/CCP+) RA, high disease activity (DAS28 5.6), early erosions — aggressive phenotype, early window.
TARGET: remission (or at least low disease activity) by treat-to-target reassessment.

INDUCTION / FIRST-LINE:
- Methotrexate 15 mg weekly (subcutaneous for absorption/tolerability) titrating to 20–25 mg weekly + folic acid 1 mg daily.
- Counsel alcohol moderation (hepatotoxicity with methotrexate).
- Steroid bridge: low-dose prednisone (e.g., 10 mg taper) or intra-articular steroid for symptom control until methotrexate takes effect (6–12 weeks) — taper off, not maintenance.

ESCALATION (reassess ~3 months):
- If DAS28 not at target on optimized methotrexate → add a TNF inhibitor (e.g., adalimumab) continuing methotrexate.
- Prefer TNF over JAK as the first add-on here per safety (and patient is younger/lower CV risk, but TNF remains the standard first biologic). Other options: IL-6 (tocilizumab), abatacept.

PRE-BIOLOGIC/JAK SCREENING:
- TB IGRA negative, HBV/HCV negative — cleared for future biologic.
- Update vaccines now (recombinant zoster, pneumococcal, influenza, COVID, hepatitis B) before deeper immunosuppression.

HEALTH MAINTENANCE:
- Cardiovascular risk management (RA amplifies CV risk), smoking cessation if applicable, bone health, age-appropriate cancer screening.
- Pregnancy planning: methotrexate is teratogenic — if she plans pregnancy later, switch to a compatible regimen with washout in advance.

MONITORING:
- DAS28/CDAI each visit (escalate if target not met).
- CBC/LFTs/renal q2–4 weeks initially on methotrexate, then q8–12 weeks.
- Infection/TB vigilance once on biologic.

PITFALLS:
- Don't delay DMARD — early aggressive seropositive erosive RA needs prompt methotrexate.
- Steroids are a bridge, not maintenance.
- Plan methotrexate cessation/washout well before any pregnancy.
```
