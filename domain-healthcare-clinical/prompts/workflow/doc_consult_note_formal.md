---
title: "Formal Consultation Note"
category: domain-healthcare-clinical/workflow
description: "Generate a specialist consultation note that answers the referring question — focused history and exam, data review, specialty assessment, and explicit recommendations the primary team can act on."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - documentation
  - consult-note
  - specialty
  - clinical-notes
updated: "2026-06-19"
---

## Objective

Produce a specialist consultation note that does the consultant's core job: answer the referring clinician's question and give explicit, actionable recommendations. Unlike an H&P, a consult note is anchored on the reason for consultation and tailored to a specialty lens. Its most important section is the recommendations — numbered, specific, and executable by the primary team.

## Inputs

- The reason for consultation / question asked, and the requesting service
- Focused history relevant to the consult question
- Pertinent exam findings (focused to the specialty)
- Relevant labs, imaging, and prior workup
- The specialty being consulted (defines the lens and the differential)
- Any specialty-specific scoring or risk assessment the question requires

## Role

Consulting specialist attending writing the note the primary team will act on.

## Reasoning Steps

1. **Restate the reason for consultation up front,** naming the requesting service and the specific question. The whole note is organized to answer it. "Consulted by Medicine for evaluation of new-onset atrial fibrillation and rate-vs-rhythm strategy."

2. **Give a focused history,** curated to the question — the relevant present illness and the specialty-relevant background. A cardiology consult for AFib needs the palpitation history, prior cardiac history, and thromboembolic risk factors, not the full social history.

3. **Document the focused, specialty-relevant exam** — the findings that bear on the question and the differential.

4. **Review and interpret the pertinent data** through the specialty lens — the ECG read by cardiology, the imaging interpreted for the specialty question, relevant labs.

5. **Write a specialty assessment** that demonstrates the reasoning: the consultant's impression, the differential within the specialty's domain, and any risk stratification using the appropriate validated tool (CHA2DS2-VASc, etc.). This is the value the consultant adds.

6. **Write numbered, explicit recommendations** — the deliverable. Each recommendation is a specific action: the drug and dose to start/stop, the study to order, the threshold to act on, the follow-up. "Recommend rate control with metoprolol 25 mg PO BID, titrate to HR <110; start anticoagulation with apixaban 5 mg BID given CHA2DS2-VASc 4" — not "consider rate control and anticoagulation."

7. **State what the consultant will do vs. what the primary team should do,** and the follow-up plan (will continue to follow, sign-off, available for questions). Clarify ownership to prevent gaps.

8. **Answer the question that was asked.** If the question is unanswerable as posed or the consult reveals a different priority, say so explicitly and reframe — don't silently answer a different question.

## Output Format

```
CONSULTATION NOTE — [Specialty]
REASON FOR CONSULTATION: [requesting service + specific question]

FOCUSED HISTORY:
[present illness + specialty-relevant background, curated to the question]

FOCUSED EXAM:
[specialty-relevant findings]

DATA REVIEWED:
[ECG/imaging/labs interpreted through the specialty lens]

ASSESSMENT (specialty):
[impression, differential within specialty domain, risk stratification with named tool]

RECOMMENDATIONS:
1. [specific action — drug/dose/study/threshold]
2. ...

FOLLOW-UP / OWNERSHIP:
- [consultant will follow / sign off]; [what primary team owns]; [availability]
```

## Worked Example

**Input:** Cardiology consulted by Medicine. 72 y/o M admitted for pneumonia, found to have new-onset atrial fibrillation with RVR (HR 130s) on telemetry, now 110s after initial metoprolol. Question: rate vs. rhythm strategy and anticoagulation. History: palpitations x2 days, no prior AFib, HTN, diabetes, prior TIA 3 years ago. No prior cardiac history, no chest pain. Exam: irregularly irregular, no murmur, no heart failure signs. ECG: AFib, no pre-excitation, no ischemia. Echo (today): EF 55%, mild LA enlargement, no valvular disease. CHA2DS2-VASc: HTN(1), DM(1), age 65-74(1), prior TIA(2) = 5.

**Output:**

```
CONSULTATION NOTE — Cardiology
REASON FOR CONSULTATION: Consulted by Medicine for new-onset atrial fibrillation with rapid ventricular response in the setting of pneumonia — rate-vs-rhythm strategy and anticoagulation recommendations.

FOCUSED HISTORY:
72 y/o M admitted with community-acquired pneumonia, now with new-onset atrial fibrillation. Reports 2 days of palpitations, no prior documented AFib. No chest pain, dyspnea beyond his pneumonia, syncope, or prior cardiac history. PMH notable for hypertension, type 2 diabetes, and a TIA 3 years ago (relevant to thromboembolic risk). The AFib is most likely precipitated by the acute infection/inflammatory state.

FOCUSED EXAM:
Irregularly irregular rhythm, rate ~110 after initial beta-blockade. No murmurs, no S3, JVP not elevated, lungs with pneumonia findings, no peripheral edema — no signs of decompensated heart failure.

DATA REVIEWED:
- ECG: Atrial fibrillation, ventricular rate ~110s, no pre-excitation/delta wave, no acute ischemic changes.
- Echocardiogram (today): EF 55% (preserved), mild left atrial enlargement, no significant valvular disease, no thrombus reported.
- Labs: electrolytes, thyroid function (recommend TSH if not done), within acceptable range.

ASSESSMENT (Cardiology):
New-onset atrial fibrillation, most likely secondary to the acute illness (pneumonia) — a common reversible precipitant. Hemodynamically stable, no pre-excitation, preserved EF, no decompensated heart failure. For a stable patient with likely illness-triggered AFib, a rate-control strategy is preferred initially; rhythm control is not urgently indicated and many patients convert as the acute illness resolves. Thromboembolic risk is high: CHA2DS2-VASc = 5 (HTN 1, DM 1, age 65–74 1, prior TIA 2) — anticoagulation is clearly indicated regardless of rate/rhythm strategy.

RECOMMENDATIONS:
1. Rate control: metoprolol tartrate 25 mg PO BID, titrate to a resting HR <110; transition to metoprolol succinate once stable. Avoid AV-nodal blockade pitfalls — no contraindication here (preserved EF, no pre-excitation).
2. Anticoagulation: start apixaban 5 mg PO BID (CHA2DS2-VASc 5; high stroke risk, prior TIA). No mechanical valve or severe mitral stenosis, so a DOAC is appropriate over warfarin. Confirm renal function and weight for dosing.
3. Treat the precipitant: full treatment of pneumonia; correct hypoxia, electrolytes (keep K >4, Mg >2).
4. Obtain TSH to exclude thyrotoxic contribution if not already done.
5. No urgent cardioversion indicated (stable, AFib >48h/unknown duration, anticoagulation just starting). If rhythm control is later pursued, anticoagulate ≥3 weeks first or perform TEE-guided cardioversion.
6. Outpatient cardiology follow-up after discharge to reassess rhythm once the acute illness resolves and to decide on long-term rate/rhythm strategy.

FOLLOW-UP / OWNERSHIP:
- Cardiology will continue to follow during this admission for rate control and anticoagulation titration. Primary team to implement orders above, monitor telemetry and HR, and ensure renal-appropriate DOAC dosing. Available for any questions or hemodynamic change.
```
