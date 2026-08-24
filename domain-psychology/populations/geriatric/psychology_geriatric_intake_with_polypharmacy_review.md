---
title: "Geriatric Intake with Polypharmacy and Falls-Risk Review"
category: psychology/populations/geriatric
description: "Structured biopsychosocial intake for older adults (65+) that integrates a medication / polypharmacy review (Beers Criteria, anticholinergic burden, STOPP/START), falls-risk assessment (Morse, TUG), functional status (Katz ADL, Lawton IADL), cognitive and late-life suicide screens, producing a CPT 90791 intake note with referral hooks."
techniques:
  - ST-04
  - DT-02
  - RT-02
  - CM-02
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - geriatric
  - intake
  - polypharmacy
  - beers-criteria
  - anticholinergic-burden
  - falls-risk
  - functional-status
  - cpt-90791
  - late-life-suicide-risk
  - capacity
updated: "2026-06-08"
related_prompts:
  - domain-psychology/populations/geriatric/psychology_geriatric_depression_vs_dementia_differential.md
  - domain-psychology/populations/geriatric/psychology_geriatric_grief_and_late_life_transitions.md
  - domain-psychology/documentation/psychology_intake_assessment_note.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
---

# Geriatric Intake with Polypharmacy and Falls-Risk Review

## Objective

Produce a complete, age-calibrated biopsychosocial intake record for an older adult (65+) that:

1. Documents presenting concerns, history, and mental status using geriatric-calibrated norms.
2. Integrates a **structured medication review** that screens for polypharmacy, potentially inappropriate medications (Beers Criteria), cumulative anticholinergic burden, and prescribing omissions (STOPP/START) — flagging items for pharmacist/prescriber review rather than independently adjudicating drug interactions.
3. Assesses **falls risk** (Morse Falls Scale structure, Timed Up and Go) and links it to medication and functional findings.
4. Documents **functional status** with named instruments (Katz ADL, Lawton IADL).
5. Includes a **brief cognitive screen** (Mini-Cog / MoCA / MMSE) and a **late-life depression and suicide-risk screen** (GDS-15, Columbia C-SSRS), because suicide risk is elevated in older adults — especially older men.
6. Surfaces capacity and decision-making concerns and routes them to formal capacity evaluation when indicated.
7. Produces a structured note meeting CPT 90791 documentation requirements.

## When to Use

- At initial intake for any client 65 and older presenting for outpatient psychotherapy or psychiatric evaluation.
- When the referral question involves mood, anxiety, cognition, or behavior change in the context of multiple medical conditions and medications.
- When a care-transition (new to a clinic, post-hospitalization, post-move to assisted living) warrants a fresh, consolidated baseline.
- When a collateral informant (spouse, adult child, caregiver) is available to corroborate medication lists and functional status.

## When NOT to Use

- For adults under 65 without a geriatric presentation: use `psychology_intake_assessment_note.md`.
- When the primary question is differentiating depression from dementia: pair with or route to `psychology_geriatric_depression_vs_dementia_differential.md`.
- As a substitute for a pharmacist medication-therapy-management review or a physician medication reconciliation — this prompt **flags** issues for those clinicians; it does not adjudicate drug-drug interactions.
- When acute delirium is suspected: stabilize and obtain medical workup first; an intake conducted during delirium is not a valid baseline.

## Inputs / Context Required

- **Client demographics:** Name/MRN, DOB, age, living situation (independent / with family / assisted living / SNF), primary language, interpreter need, hearing/vision status.
- **Referral information:** Referring provider, reason for referral, records received.
- **Presenting concern:** In the client's own words plus collateral report.
- **Medication list:** ALL prescriptions, OTCs, supplements, PRNs — name, dose, frequency, prescriber, indication, start date. `[clinician input required: source of medication list — pill bottles / pharmacy printout / patient report / EHR reconciliation]`
- **Medical history:** Active conditions, hospitalizations in past 12 months, falls in past 12 months, sensory impairments, pain.
- **Functional baseline:** Self-care and instrumental activities; recent change in function.
- **Collateral informant:** Name, relationship, what they can corroborate.
- **Capacity context:** Any prior capacity question, guardianship/POA status, advance directives.

## Constraints

### Must

- Calibrate MSE, screening thresholds, and diagnostic language to geriatric norms; account for sensory impairment, slowed processing, and education effects.
- Compile a complete medication list (prescription + OTC + supplements + PRN) and **count total agents** to quantify polypharmacy (commonly ≥5 concurrent medications).
- Screen the medication list against **Beers Criteria** (potentially inappropriate medications in older adults) and tally **cumulative anticholinergic burden**; name the specific flagged agents and the concern category.
- Apply **STOPP/START** logic to flag both potentially inappropriate prescriptions (STOPP) and potential prescribing omissions (START).
- Document **falls risk** using Morse Falls Scale domains and, where feasible, a Timed Up and Go (TUG) time; link elevated risk to sedating/orthostatic/anticholinergic medications.
- Document **functional status** with Katz ADL and Lawton IADL, and note any recent functional decline.
- Complete a **cognitive screen** (Mini-Cog / MoCA / MMSE) interpreted against education-adjusted bands without reproducing copyrighted item text.
- Complete a **late-life depression screen (GDS-15)** and a **suicide-risk screen (Columbia C-SSRS)**; document that risk was assessed even when negative.
- Route any medication concern to **pharmacist / prescriber review** and any capacity concern to **formal capacity evaluation** — do not resolve these unilaterally.
- Flag all `[clinician input required: ...]` gaps; do not fabricate medication lists, scores, or functional findings.

### Must Not

- Do not independently adjudicate specific drug-drug interactions or recommend stopping/changing a medication; reference Beers/STOPP/START and route to the prescriber/pharmacist.
- Do not fabricate Beers flags, anticholinergic-burden scores, instrument scores, or falls-history details.
- Do not mark cognition or mood "within normal limits" without a named screen and a behavioral anchor.
- Do not omit the suicide-risk screen; late-life suicide risk (especially older men, recent loss, medical illness, isolation) is elevated and frequently missed.
- Do not document capacity as intact or impaired without the basis (understanding, appreciation, reasoning, expression of a choice); route formal determinations out.

## Geriatric Calibration and Screening Reference

| Domain | Instrument(s) | Structure / Interpretation Note |
|--------|---------------|---------------------------------|
| Polypharmacy | Medication count | ≥5 concurrent agents = polypharmacy; ≥10 = hyperpolypharmacy. Count is a flag, not a diagnosis. |
| Inappropriate meds | Beers Criteria (AGS) | Lists agents to avoid or use with caution in older adults (e.g., certain benzodiazepines, sedative-hypnotics, strong anticholinergics, first-gen antihistamines). Name the flagged agent + concern. |
| Anticholinergic load | Anticholinergic burden tally | Cumulative anticholinergic exposure correlates with cognitive impairment, delirium, and falls. Tally contributing agents; route total to pharmacist. |
| Prescribing review | STOPP/START | STOPP = potentially inappropriate to continue; START = potentially indicated but omitted. |
| Falls risk | Morse Falls Scale; Timed Up and Go (TUG) | Morse domains: fall history, secondary dx, ambulatory aid, IV/heparin lock, gait, mental status. TUG ≥12 sec suggests elevated falls risk. |
| Function (basic) | Katz ADL | Bathing, dressing, toileting, transferring, continence, feeding (independent/dependent per item). |
| Function (instrumental) | Lawton IADL | Telephone, shopping, food prep, housekeeping, laundry, transport, medications, finances. |
| Cognition | Mini-Cog / MoCA / MMSE | Interpret by education-adjusted band; Mini-Cog for rapid screen, MoCA more sensitive to mild impairment. No item text reproduced. |
| Mood | GDS-15 (or GDS-30) | GDS-15: ~0–4 normal, ~5–8 mild, ~9–11 moderate, ~12–15 severe (clinician confirms cutoff/version). Yes/no format suits older adults. |
| Suicide risk | Columbia C-SSRS | Ideation type, intensity, behavior subscale; elevated late-life risk. |

## Instructions

1. **Confirm the medication source and reconcile.** Identify how the medication list was obtained (pill bottles, pharmacy printout, EHR, patient/collateral report) and note discrepancies. Reconciliation quality is itself clinical data.

2. **Conduct the biopsychosocial interview.** Cover presenting concern (client words + collateral), HPI, psychiatric history, medical history (active conditions, recent hospitalizations, pain, sensory status), substance/alcohol use (calibrated to older-adult risk), family and social history, bereavement and role losses, and supports.

3. **Run the medication / polypharmacy review.** Count total agents; flag Beers-listed items by name; tally anticholinergic-burden contributors; apply STOPP/START logic. Document each flag with the concern category and route to pharmacist/prescriber.

4. **Assess falls risk.** Document falls in the past 12 months, gait/balance, assistive devices, orthostatic symptoms; record Morse domains and a TUG time if available. Explicitly link sedating/anticholinergic/orthostatic medications to falls risk.

5. **Document functional status.** Complete Katz ADL and Lawton IADL; note recent decline and its timeline.

6. **Complete cognitive and mood/risk screens.** Administer a cognitive screen (Mini-Cog/MoCA/MMSE), GDS-15, and Columbia C-SSRS; interpret by band; note sensory or language confounds.

7. **Conduct the geriatric-calibrated MSE** and integrate collateral report; flag informant discrepancies.

8. **Surface capacity and safety concerns.** Note any decision-making capacity question, elder-abuse/neglect/financial-exploitation indicators, and route to formal evaluation/reporting hooks as indicated.

9. **Write the Geriatric Intake Note** using the output format below, then **Run verification.**

## Output Format

```
=== GERIATRIC BIOPSYCHOSOCIAL INTAKE NOTE (WITH POLYPHARMACY + FALLS REVIEW) ===

Client: [Initials/MRN]    DOB: [YYYY-MM-DD]    Age: [N]
Date of Service: [YYYY-MM-DD]    Time: [HH:MM–HH:MM]
Clinician: [Name, credentials]
CPT: 90791    Duration: [N minutes]
Living situation: [Independent / With family / Assisted living / SNF / Other]
Sensory status: [Hearing aid(s): Y/N; Vision corrected: Y/N; Accommodations used this visit: ...]
Interpreter: [Yes — language / No]

─────────────────────────────────────────
REFERRAL AND PRESENTING CONCERN
─────────────────────────────────────────
Referred by: [...]    Reason: [...]
Client-reported chief complaint: "[...]"
Collateral-reported concern ([name, relationship]): "[...]"
Duration / onset: [...]

─────────────────────────────────────────
HISTORY OF PRESENTING ILLNESS
─────────────────────────────────────────
[Narrative: onset, course, functional impact; note medical and medication context; identify source for divergent data.]

─────────────────────────────────────────
MEDICATION / POLYPHARMACY REVIEW
─────────────────────────────────────────
Medication list source: [Pill bottles / Pharmacy printout / EHR reconciliation / Patient report / Collateral]    Reconciliation discrepancies: [None / Describe]
Total agents counted: [N]    Polypharmacy: [No / Yes (≥5) / Hyperpolypharmacy (≥10)]

Full list (name | dose | frequency | indication | prescriber):
  1. [...]
  2. [...]
  [clinician input required: complete list]

Beers Criteria flags:
  [Agent] — concern: [e.g., sedative-hypnotic / strong anticholinergic / increased falls or cognitive risk] — action: route to prescriber/pharmacist
  [None identified on review / clinician input required]

Anticholinergic burden:
  Contributing agents: [List]    Tally: [N / not scored]    Concern: [cognitive impairment / delirium / falls — route to pharmacist]

STOPP/START flags:
  STOPP (potentially inappropriate to continue): [Agent — rationale / None noted]
  START (potential omission): [Indicated-but-absent — rationale / None noted]

Medication review disposition: [Referred to pharmacist MTM / Prescriber notified / Pending — clinician input required]

─────────────────────────────────────────
FALLS-RISK ASSESSMENT
─────────────────────────────────────────
Falls in past 12 months: [Number; circumstances; injury]
Gait / balance: [...]    Assistive device: [None / Cane / Walker / Wheelchair]
Orthostatic symptoms: [Reported Y/N]
Morse Falls Scale domains: [Fall history / Secondary dx / Ambulatory aid / IV-lock / Gait / Mental status — score: N / not scored]
Timed Up and Go (TUG): [N seconds — ≥12s = elevated / not performed]
Medication contribution to falls risk: [Sedating/anticholinergic/orthostatic agents linked above: ...]
Falls-risk level: [Low / Moderate / High — rationale]

─────────────────────────────────────────
FUNCTIONAL STATUS
─────────────────────────────────────────
Katz ADL (independent/dependent per item): Bathing [..] Dressing [..] Toileting [..] Transferring [..] Continence [..] Feeding [..]  → Summary: [Independent in N/6]
Lawton IADL: Telephone [..] Shopping [..] Food prep [..] Housekeeping [..] Laundry [..] Transport [..] Medications [..] Finances [..]  → Summary: [Independent in N/8]
Recent functional change: [None / Decline since: ___ — describe]

─────────────────────────────────────────
SUBSTANCE / ALCOHOL USE (older-adult-calibrated)
─────────────────────────────────────────
Alcohol: [Quantity/frequency; interaction-with-meds concern: ...]    Tobacco: [...]    Other: [...]
Screen: [GDS-relevant comorbidity / AUDIT-C if used: score]

─────────────────────────────────────────
COGNITIVE SCREEN
─────────────────────────────────────────
Instrument: [Mini-Cog / MoCA / MMSE]    Score: [N]    Education-adjusted band: [Normal / Borderline / Impaired]
Confounds noted: [Sensory / language / fatigue / acute illness]
Delirium excluded as acute driver: [Yes / Uncertain — workup hook]
Disposition: [No further workup / Refer for full cognitive evaluation / See depression-vs-dementia differential]

─────────────────────────────────────────
MOOD AND SUICIDE-RISK SCREEN
─────────────────────────────────────────
GDS-15: [Score N/15 — band: ...]
Columbia C-SSRS: Ideation type: [...]    Intensity: [...]    Behavior subscale: [...]
Late-life risk amplifiers present: [Recent loss / Isolation / Chronic pain / Functional decline / Firearm or lethal-means access / Male sex]
Risk level: [Low / Moderate / High — rationale]
Action: [Monitor / Safety plan completed / Formal C-SSRS-based assessment / Means-restriction counseling — see risk-crisis prompts]

─────────────────────────────────────────
MENTAL STATUS EXAMINATION (GERIATRIC-CALIBRATED)
─────────────────────────────────────────
Appearance / behavior: [Grooming; psychomotor; cooperation; sensory adaptations]
Speech: [Rate/volume; note hearing-related effects]
Mood / Affect: ["[client words]" / range, congruence]
Thought process / content: [Linear vs. impoverished/perseverative; SI/HI present or absent]
Perception: [Hallucinations present/absent — screen for delirium/charles-bonnet]
Cognition: [Orientation; attention; memory — per screen above]
Insight / Judgment: [...]
Reliability of historian: [Client / Collateral]

─────────────────────────────────────────
CAPACITY AND SAFETY
─────────────────────────────────────────
Decision-making capacity question raised: [No / Yes — domain: medical / financial / independent living]
Capacity basis observed (understanding / appreciation / reasoning / expressing a choice): [...]
Disposition: [No concern / Refer for formal capacity evaluation]
Guardianship / POA / advance directive on file: [...]
Elder abuse / neglect / financial exploitation indicators: [None / Describe — APS reporting hook]

─────────────────────────────────────────
FAMILY / SOCIAL HISTORY AND SUPPORTS
─────────────────────────────────────────
Household / caregivers: [...]    Bereavement / role losses: [...]    Isolation: [...]
Cultural/spiritual context: [...]    Strengths / protective factors: [...]

─────────────────────────────────────────
DIAGNOSTIC IMPRESSIONS
─────────────────────────────────────────
Primary: [DSM-5-TR dx] [ICD-10-CM]
Secondary: [...]
Rule out: [Medication-induced / medical contribution / neurocognitive disorder]
Z-code stressors: [e.g., Z60.2 problems related to living alone; Z63.4 disappearance/death of family member]

─────────────────────────────────────────
FIVE-P FORMULATION
─────────────────────────────────────────
Predisposing / Precipitating / Perpetuating / Protective / Presenting: [...]

─────────────────────────────────────────
TREATMENT RECOMMENDATIONS AND REFERRALS
─────────────────────────────────────────
Modality / level of care: [...]    Frequency: [...]
Medication review referral: [Pharmacist MTM / Prescriber — sent: Y/N]
Falls-prevention referral: [PT / OT / home-safety eval — as indicated]
Cognitive evaluation referral: [If indicated]
Capacity evaluation referral: [If indicated]
Care coordination: [PCP / geriatrician / care manager — ROI status]

─────────────────────────────────────────
BILLING NOTE
─────────────────────────────────────────
CPT: 90791 (Psychiatric Diagnostic Evaluation)    Duration: [N minutes]
Payer: [...]    Authorization: [Not required / Auth # ___]
```

## Verification

- [ ] Living situation, sensory status, and interpreter need documented; MSE calibrated to geriatric norms.
- [ ] Medication list source identified and total agents counted; polypharmacy flagged (≥5 / ≥10).
- [ ] Beers Criteria flags named by agent + concern; anticholinergic burden tallied; STOPP/START applied.
- [ ] Medication concerns routed to pharmacist/prescriber — not unilaterally adjudicated.
- [ ] Falls risk documented (Morse domains and/or TUG) and linked to contributing medications.
- [ ] Functional status documented with Katz ADL and Lawton IADL; recent decline noted.
- [ ] Cognitive screen completed (Mini-Cog/MoCA/MMSE) with education-adjusted interpretation; delirium considered.
- [ ] GDS-15 and Columbia C-SSRS completed; late-life suicide risk assessed even when negative.
- [ ] Capacity question and elder-abuse indicators surfaced with appropriate referral/reporting hooks.
- [ ] No copyrighted instrument item text reproduced; bands referenced only.
- [ ] No fabricated medications, scores, falls history, or interactions; gaps flagged with `[clinician input required: ...]`.
- [ ] CPT 90791 documentation elements present.
