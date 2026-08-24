---
title: "Ischemic Stroke Secondary Prevention Care Plan"
category: domain-healthcare-clinical/care-plans
description: "Build an ischemic stroke / TIA secondary prevention plan by mechanism: antithrombotic selection, BP and lipid targets, and etiology-specific therapy with named drugs and doses."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
  - DS-02
difficulty: advanced
tags:
  - neurology
  - stroke
  - secondary-prevention
  - care-plan
updated: "2026-06-19"
---

## Objective

Produce an ischemic stroke / TIA secondary prevention plan organized by stroke mechanism: antithrombotic strategy (antiplatelet vs anticoagulation), BP and LDL targets, and etiology-specific interventions (carotid revascularization, PFO, AF). Output is a mechanism-driven prevention plan.

## Inputs

- Event: ischemic stroke vs TIA, severity (NIHSS), territory, imaging (infarct size, hemorrhagic transformation)
- Mechanism workup: cardioembolic (AF, low EF, valve), large-artery atherosclerosis (carotid/intracranial stenosis), small-vessel/lacunar, cryptogenic/ESUS, PFO, dissection, hypercoagulable
- Risk factors: BP, LDL, diabetes, smoking, prior events, AF
- Bleeding risk, current antithrombotics, renal/hepatic function

## Role

Vascular neurologist or internist managing stroke secondary prevention.

## Reasoning Steps

1. **Define mechanism — it drives antithrombotic choice.** Complete workup: vessel imaging (CTA/MRA carotid + intracranial), cardiac monitoring (telemetry → extended/loop for cryptogenic to detect AF), echo (± bubble study for PFO), labs.

2. **Antithrombotic by mechanism:**
   - **Non-cardioembolic (atherosclerotic/lacunar):** antiplatelet. Aspirin 81 mg, or clopidogrel 75, or aspirin-dipyridamole.
   - **Minor stroke (NIHSS ≤3) or high-risk TIA (ABCD2 ≥4):** short-course DAPT — aspirin + clopidogrel for 21 days (CHANCE/POINT), then single agent. Ticagrelor + aspirin alternative (THALES). Do not continue DAPT long-term (bleeding).
   - **Symptomatic intracranial stenosis (70–99%):** aspirin + clopidogrel × 90 days + aggressive risk-factor control (SAMMPRIS); stenting not superior.
   - **Cardioembolic (AF):** anticoagulation — DOAC preferred (apixaban, etc.), warfarin for mechanical valve/significant MS. Timing by infarct size ("1-3-6-12 day" rule): start sooner for TIA/small, delay 1–2 weeks for large infarcts (hemorrhagic transformation risk).

3. **BP control:** target <130/80 long-term; initiate/intensify after the acute period. Thiazide + ACEi/ARB favored (PROGRESS).

4. **Lipids:** high-intensity statin (atorvastatin 80); target LDL <70 (SPARCL/Treat Stroke to Target — <70 superior). Add ezetimibe/PCSK9i to reach goal.

5. **Etiology-specific:**
   - **Carotid stenosis 70–99% symptomatic:** CEA (or CAS) within 2 weeks if non-disabling stroke. 50–69%: individualize.
   - **PFO** in cryptogenic stroke, age <60, no other cause: closure + antiplatelet (RESPECT/CLOSE).
   - **Dissection:** antiplatelet or anticoagulation × 3–6 months.

6. **Risk factors:** diabetes control (consider pioglitazone in insulin-resistant non-diabetic stroke — IRIS; or GLP-1/SGLT2i), smoking cessation, OSA screening, weight, activity, alcohol.

7. **Monitor:** BP log, lipids, bleeding, AF surveillance if cryptogenic, carotid follow-up, medication adherence.

## Output Format

```
EVENT / SEVERITY / TERRITORY:
MECHANISM (with workup status):

ANTITHROMBOTIC:
- [agent(s), dose, duration, mechanism rationale]
- DAPT short course if minor stroke/high-risk TIA
- Anticoagulation timing if cardioembolic

BP TARGET / AGENTS:
LIPID TARGET / STATIN:

ETIOLOGY-SPECIFIC:
- Carotid revascularization / PFO closure / dissection

RISK FACTORS:
- Diabetes, smoking, OSA, lifestyle

MONITORING:
- BP, lipids, AF surveillance, bleeding, adherence

PITFALLS:
- [long-term DAPT bleeding, anticoagulation timing by infarct size, missing AF in cryptogenic, delayed carotid surgery]
```

## Worked Example

**Input:** 68 y/o M, minor ischemic stroke (NIHSS 2), left MCA territory, small cortical infarct, no hemorrhagic transformation. CTA: 80% symptomatic left ICA stenosis. BP 156/90, LDL 118, statin-naive, sinus rhythm on telemetry, diabetic.

**Output:**

```
EVENT / SEVERITY / TERRITORY: minor ischemic stroke, NIHSS 2, left MCA, small infarct.
MECHANISM: large-artery atherosclerosis — symptomatic 80% left ICA stenosis. (Telemetry sinus; complete AF surveillance but mechanism here is carotid.)

ANTITHROMBOTIC:
- Minor stroke → short-course DAPT: aspirin 81 mg + clopidogrel 75 mg × 21 days (load clopidogrel 300–600), then single antiplatelet (clopidogrel 75 or aspirin 81) long-term.
- No anticoagulation (not cardioembolic; sinus rhythm).

BP TARGET / AGENTS: <130/80. Initiate after acute period: chlorthalidone + lisinopril (or ARB); avoid aggressive lowering in the first 24–48 h with critical stenosis.

LIPID TARGET / STATIN: atorvastatin 80 mg; LDL goal <70. Recheck 4–6 wk; add ezetimibe if above goal.

ETIOLOGY-SPECIFIC:
- Symptomatic 80% ICA stenosis, non-disabling stroke → carotid endarterectomy (or stenting) within 2 weeks — do not delay.

RISK FACTORS:
- Diabetes optimization (consider GLP-1/SGLT2i); smoking cessation if applicable; OSA screen; lifestyle.

MONITORING:
- BP log, lipids, bleeding on DAPT (stop at 21 days), post-CEA surveillance, adherence.

PITFALLS:
- Do not continue DAPT beyond 21 days (bleeding without benefit).
- Refer for CEA urgently (≤2 wk) — the stenosis is the lesion.
- Statin target is <70 for stroke (lower than primary prevention).
```
