---
title: "Full History & Physical Note"
category: domain-healthcare-clinical/workflow
description: "Generate a complete admission H&P from collected clinical data — HPI through assessment and plan by problem — at attending-documentation quality."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - documentation
  - h-and-p
  - admission
  - clinical-notes
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

Produce a complete, admission-quality History & Physical: a narrative HPI that tells the story, a structured review of the supporting data, and an assessment and plan organized by problem with concrete next steps. The note should read as if written by the admitting attending — coherent, prioritized, and clinically reasoned, not a data dump.

## Inputs

- Chief complaint and the elements of the present illness (onset, character, timing, modifiers, associated symptoms, pertinent negatives)
- Past medical/surgical history, medications, allergies, family and social history
- Review of systems
- Vital signs and physical exam findings
- Labs, imaging, and any studies already resulted
- Setting (which service, reason for admission)

## Role

Admitting attending or senior resident writing the H&P that frames the hospitalization.

## Reasoning Steps

1. **Open with a tight one-liner:** age, sex, the pertinent chronic conditions that bear on this admission, and the presenting problem. This is the orienting sentence every reader keys off.

2. **Write the HPI as a narrative,** chronologically, with the OPQRST/relevant elements woven in — not a bulleted symptom list. Include the pertinent positives and the pertinent negatives that shape the differential. The HPI should make the leading diagnosis feel inevitable by the end.

3. **Populate the structured history** (PMH, PSH, meds with doses, allergies with reactions, family history, social history including tobacco/alcohol/substances and functional/living situation). Keep it complete but relevant; flag missing elements rather than inventing them.

4. **Record the ROS** distinguishing pertinent positives/negatives from the rest; do not fabricate a fully negative 14-system review if the data wasn't gathered.

5. **Document vitals and a systematic exam,** general appearance through each system examined. Report only what was examined; don't invent normal findings for systems not assessed.

6. **Summarize the data** — labs, imaging, ECG, with the salient abnormalities highlighted and interpreted, not just listed.

7. **Write the assessment as clinical reasoning,** not a restatement. Lead with a summary statement (problem representation), give the leading diagnosis with supporting and opposing evidence, and the differential ranked with what argues for/against each.

8. **Build the plan by problem.** For each active problem: the working diagnosis, the diagnostic next steps, the therapeutic interventions with named drugs/doses, and the monitoring. Include disposition, code status, VTE prophylaxis, and dispo-relevant items. Don't leave a problem in the assessment without a corresponding plan.

## False-Positive Prevention

❌ **DON'T:**
- Quote a chief complaint in the patient's words, or add sputum colour, onset sequence, exercise tolerance and pertinent negatives that were not in the input, to make the HPI "tell the story".
- Write "ALLERGIES: NKDA" when allergies were not supplied — NKDA is an assertion that someone asked; write `[allergies not obtained]`.
- Add doses and frequencies to MEDICATIONS when the input lists drug names only — the admission reconciliation inherits them.
- Report a severity score or sepsis statement as settled while a component is pending or the criteria set is unnamed — a CURB-65 with BUN pending is "≥ N, incomplete", and "no sepsis" must say which definition (SIRS or Sepsis-3/SOFA) was applied to the supplied vitals and labs.

✅ **DO:**
- Tag every HPI, ROS and exam sentence to the input element it came from; delete or bracket any sentence without a tag before the note is called complete.
- Recompute each score item by item (CURB-65: confusion, BUN > 19 mg/dL [> 7 mmol/L], RR ≥ 30, SBP < 90 or DBP ≤ 60, age ≥ 65) and show which items are scored, unscored or pending.
- Before calling a value "normal" or "not elevated", compare it against the reporting lab's reference range and units if supplied; if not supplied, say so.
- Count problems in ASSESSMENT against `#` headings in PLAN, and check each home medication has an explicit continue/hold decision.

## Output Format

```
CHIEF COMPLAINT: [patient's words / one line]

HPI:
[narrative paragraph(s) — one-liner opener, then the story with pertinent +/-]

PAST MEDICAL HISTORY: [list]
PAST SURGICAL HISTORY: [list]
MEDICATIONS: [drug, dose, frequency]
ALLERGIES: [drug → reaction]
FAMILY HISTORY: [relevant]
SOCIAL HISTORY: [tobacco/alcohol/substances, occupation, living situation, functional status]

REVIEW OF SYSTEMS: [pertinent positives/negatives by system]

VITALS: [T, HR, BP, RR, SpO2]
PHYSICAL EXAM:
- General: ...
- [systems examined]

DATA:
- Labs: [salient values + interpretation]
- Imaging/Studies: [findings]

ASSESSMENT:
[summary statement / problem representation]
[leading diagnosis + supporting/opposing evidence; ranked differential]

PLAN (by problem):
# [Problem 1]
- Dx: [next steps]
- Tx: [drug, dose, route]
- Monitoring: [parameters]
# [Problem 2]
...

Dispo: [level of care]
Code status: [...]
VTE prophylaxis: [...]
```

## Worked Example

**Input:** 68 y/o M, admitted from ED with 3 days of productive cough, fever, dyspnea. Patient: "coughing and short of breath for 3 days." Began with coryza, then yellow-green sputum and right-sided pleuritic chest pain; dyspnea now after one flight of stairs (baseline unlimited). Positive for fever and chills. Denies hemoptysis, orthopnea, PND, leg swelling, chest pressure at rest, abdominal pain, dysuria. PMH COPD, HTN, T2DM. PSH none. Meds: tiotropium 18 mcg inhaled daily, lisinopril 20 mg daily, metformin 1000 mg BID. Allergies: NKDA (confirmed with patient). FHx non-contributory. Current smoker, 40 pack-years; lives with spouse; independent in ADLs. Vitals T 38.9, HR 108, BP 142/84, RR 24, SpO2 88% on RA → 94% on 2L. Exam: ill-appearing, mild respiratory distress, alert and oriented; right basilar crackles, no wheeze at rest, no accessory muscle use; tachycardic, regular, no murmur; no edema. Labs: WBC 16.2 (neutrophil-predominant), lactate 1.8, glucose 244, Cr 1.0 (reference ranges not supplied). BUN not resulted. CXR: right lower lobe consolidation. Procalcitonin elevated. Code status: full code, confirmed with patient.

**Output:**

```
CHIEF COMPLAINT: "Coughing and short of breath for 3 days."

HPI:
68 y/o M with COPD (40 pack-year smoker), HTN, and T2DM presenting with 3 days of productive cough with yellow-green sputum, subjective fevers, and progressive dyspnea. Symptoms began with coryza, then developed pleuritic right-sided chest discomfort and exertional dyspnea limiting him to one flight of stairs (baseline: unlimited). Endorses fever and chills; denies hemoptysis, leg swelling, orthopnea, or chest pressure at rest. In the ED, febrile to 38.9 and hypoxic to 88% on room air, improved to 94% on 2L. The combination of focal consolidation, leukocytosis, fever, and hypoxia is consistent with community-acquired pneumonia superimposed on COPD.

PAST MEDICAL HISTORY: COPD, hypertension, type 2 diabetes mellitus.
PAST SURGICAL HISTORY: None reported.
MEDICATIONS: Tiotropium 18 mcg inhaled daily; lisinopril 20 mg daily; metformin 1000 mg BID.
ALLERGIES: NKDA (confirmed with patient).
FAMILY HISTORY: Non-contributory to current presentation.
SOCIAL HISTORY: 40 pack-year smoker, currently smoking; lives with spouse; independent in ADLs.

REVIEW OF SYSTEMS: Positive for fever, chills, productive cough, dyspnea, pleuritic chest pain. Negative for hemoptysis, orthopnea, PND, leg swelling, abdominal pain, dysuria.

VITALS: T 38.9, HR 108, BP 142/84, RR 24, SpO2 88% RA → 94% on 2L NC.
PHYSICAL EXAM:
- General: Ill-appearing, mild respiratory distress.
- Pulmonary: Right basilar crackles, no wheeze at rest, no accessory muscle use at rest.
- Cardiac: Tachycardic, regular, no murmur.
- Extremities: No edema.

DATA:
- Labs: WBC 16.2 (neutrophil-predominant) — leukocytosis; glucose 244; Cr 1.0 and lactate 1.8 (lab reference ranges not supplied — confirm against reporting lab); BUN not resulted; procalcitonin elevated (supports bacterial etiology).
- Imaging: CXR — right lower lobe consolidation.

ASSESSMENT:
68 y/o M smoker with COPD presenting with fever, focal consolidation, leukocytosis, and hypoxia — community-acquired pneumonia. CURB-65: confusion no (0), BUN not resulted (unscored), RR 24 (≥30 no, 0), BP 142/84 (0), age ≥65 yes (1) → ≥1, incomplete pending BUN; admit appropriate given hypoxia requiring O2. Sepsis screen: meets SIRS criteria (T 38.9, HR 108, RR 24, WBC 16.2) with a suspected pulmonary source; Sepsis-3 SOFA not calculable from supplied data (no ABG/PaO2, platelets or bilirubin) — new hypoxemia requiring O2 may represent respiratory organ dysfunction. Normotensive, lactate 1.8 — no features of septic shock on supplied data. [VERIFY: sepsis definition applied and lactate cutoff against Sepsis-3 / current Surviving Sepsis Campaign guideline and local sepsis protocol.] Hyperglycemia likely stress/illness-related.

PLAN (by problem):
# Community-acquired pneumonia
- Dx: blood cultures x2 before antibiotics, sputum culture, respiratory viral panel, BUN to complete CURB-65, repeat CXR if not improving.
- Tx: ceftriaxone 1 g IV daily + azithromycin 500 mg IV/PO daily (CAP, admitted non-ICU). Reassess de-escalation with cultures.
- Monitoring: continuous pulse oximetry, titrate O2 to SpO2 ≥92%, trend WBC and clinical response.
# COPD
- Continue tiotropium; add scheduled albuterol-ipratropium nebs; assess for need of systemic steroids if bronchospasm/exacerbation features emerge.
# Hyperglycemia / T2DM
- Hold metformin during acute illness; sliding-scale insulin, monitor glucose QID.
# HTN
- Continue lisinopril; monitor in setting of acute illness.

Dispo: Medicine floor with telemetry/continuous pulse ox.
Code status: Full code (confirmed with patient).
VTE prophylaxis: Enoxaparin 40 mg SC daily.
```
