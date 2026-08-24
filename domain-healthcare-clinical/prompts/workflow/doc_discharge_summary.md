---
title: "Discharge Summary"
category: domain-healthcare-clinical/workflow
description: "Generate a complete discharge summary — hospital course by problem, discharge medications with changes, follow-up, pending results, and patient instructions — that safely closes the admission."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - documentation
  - discharge-summary
  - care-transitions
  - clinical-notes
updated: "2026-06-19"
---

## Objective

Produce a discharge summary that closes the hospitalization safely: a coherent hospital course, an explicit reconciliation of what changed about the medications, the follow-up plan with owners, the results still pending at discharge, and clear patient instructions. The summary is the primary handoff to the next clinician — its highest job is to ensure nothing falls through the cracks after the patient leaves.

## Inputs

- Admission diagnosis and discharge diagnosis(es)
- Hospital course: the key events, treatments, procedures, consults, and the patient's response
- Discharge medication list and how it differs from the admission list (started, stopped, changed)
- Pending results at discharge (cultures, final reads, biopsies)
- Follow-up appointments and referrals
- Discharge condition, functional status, and disposition (home, SNF, etc.)
- Pertinent discharge labs/vitals

## Role

Attending or senior resident writing the discharge summary the receiving clinician will rely on.

## Reasoning Steps

1. **State admission and discharge diagnoses up front,** clearly distinguished. The discharge diagnosis is what was actually found, which may differ from the admitting impression.

2. **Write the hospital course by problem,** in narrative form — what was the problem, what was done, how did the patient respond, what's the status at discharge. Include procedures, significant consults and their recommendations, and complications. Keep it proportional: the principal problem gets the detail; minor issues get a line.

3. **Reconcile medications explicitly.** This is the highest-risk section. List discharge meds, and for each change from baseline, state it and why: "Stopped lisinopril (AKI); started amlodipine 5 mg." "Warfarin held; bridging with enoxaparin, see plan." The receiving clinician and pharmacist depend on this being unambiguous.

4. **Itemize pending results with an owner and a plan.** A culture or biopsy pending at discharge is the canonical dropped result. State what's pending, who will follow it up, and what to do with the result.

5. **Lay out the follow-up plan:** which appointments are scheduled (with whom, when), which referrals were placed, and what each follow-up needs to accomplish. Flag time-sensitive follow-up.

6. **Capture discharge condition and disposition** — functional status, where the patient is going, services arranged (home health, PT, DME, oxygen).

7. **Include patient-facing instructions and warning signs** — activity, diet, wound care, and the specific symptoms that should prompt return.

8. **Don't fabricate course or results.** If something is uncertain or wasn't resolved, say so. The summary must reflect what actually happened.

## Output Format

```
ADMISSION DATE / DISCHARGE DATE:
ADMISSION DIAGNOSIS:
DISCHARGE DIAGNOSIS(ES):

HOSPITAL COURSE (by problem):
# [Principal problem]: [what, treatment, response, status at d/c]
# [Secondary problems]: ...
Procedures: [list]
Consults: [service + key recommendation]

DISCHARGE MEDICATIONS (with changes flagged):
- [drug, dose, frequency]
- CHANGES: STARTED [..], STOPPED [.. + reason], CHANGED [.. + reason]

PENDING RESULTS AT DISCHARGE (with owner):
- [test — expected back — who follows up — action]

FOLLOW-UP:
- [appointment/referral — with whom — when — purpose]

DISCHARGE CONDITION / DISPOSITION:
- [functional status, destination, services arranged]

DISCHARGE LABS/VITALS (pertinent):

PATIENT INSTRUCTIONS:
- Activity/diet/wound care: [...]
- Return precautions: [specific warning symptoms]
```

## Worked Example

**Input:** CAP patient, ready for discharge HD4. Admitted for CAP/COPD, culture-confirmed pneumococcal pneumonia, treated with ceftriaxone+azithromycin, narrowed to oral amoxicillin, clinically resolved, off O2. Metformin held during admission, resumed. Blood cultures finalized no growth; sputum final pending speciation confirmation already known. Follow-up PCP 1 week. Lives home with spouse, independent.

**Output:**

```
ADMISSION DATE / DISCHARGE DATE: [admit] / [discharge, HD4]
ADMISSION DIAGNOSIS: Community-acquired pneumonia with hypoxia, COPD.
DISCHARGE DIAGNOSIS(ES): Pneumococcal community-acquired pneumonia (Streptococcus pneumoniae), resolved; COPD; type 2 diabetes mellitus; hypertension.

HOSPITAL COURSE (by problem):
# Community-acquired pneumonia: Presented with fever, cough, and hypoxia (88% RA); CXR showed RLL consolidation; WBC 16.2; procalcitonin elevated. Started on ceftriaxone + azithromycin. Blood cultures no growth; sputum culture grew S. pneumoniae sensitive to ceftriaxone. Azithromycin discontinued; transitioned to oral amoxicillin to complete a 7-day total course. Afebrile by HD2, weaned to room air by HD3, WBC normalized to 9.8. Resolved at discharge.
# COPD: No acute exacerbation requiring steroids; continued maintenance tiotropium with PRN nebs.
# T2DM: Metformin held during acute illness, managed with sliding-scale insulin; metformin resumed at discharge with stable glucoses.
# HTN: Continued home lisinopril, controlled throughout.
Procedures: None.
Consults: None.

DISCHARGE MEDICATIONS (with changes flagged):
- Amoxicillin 875 mg PO BID to complete through [date] (7-day total course) — STARTED for pneumonia.
- Tiotropium 18 mcg inhaled daily — continued.
- Lisinopril 20 mg daily — continued.
- Metformin 1000 mg BID — RESUMED (held inpatient during acute illness).
- CHANGES: STARTED amoxicillin (finish course); ceftriaxone/azithromycin were inpatient only and STOPPED at discharge; metformin resumed.

PENDING RESULTS AT DISCHARGE (with owner): None — blood cultures finalized (no growth), sputum culture finalized (S. pneumoniae, sensitivities reported). No open results.

FOLLOW-UP:
- PCP in 1 week — confirm clinical resolution, repeat exam, ensure antibiotic course completed; address tobacco cessation and pneumococcal/influenza vaccination status.
- Recommend outpatient pneumococcal and seasonal influenza vaccination if not up to date.

DISCHARGE CONDITION / DISPOSITION:
- Stable, ambulatory, off oxygen, independent in ADLs. Discharged home with spouse. No home services required.

DISCHARGE LABS/VITALS: Afebrile, SpO2 95% RA, WBC 9.8, glucose stable on resumed metformin.

PATIENT INSTRUCTIONS:
- Activity: resume as tolerated. Diet: regular/diabetic. Finish all antibiotic doses.
- Return precautions: return or call for recurrent fever, worsening cough or shortness of breath, chest pain, or inability to keep oral medications down. Strongly advised smoking cessation.
```
