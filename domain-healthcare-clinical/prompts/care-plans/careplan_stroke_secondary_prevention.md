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

## False-Positive Prevention

❌ **DON'T:**
- Assign a TOAST mechanism (or "cryptogenic/ESUS") while vessel imaging, echocardiography or cardiac monitoring is still pending — mark it "provisional" and keep the AF-surveillance line.
- Call a carotid stenosis "symptomatic" without matching its side to the infarct territory, or quote a percentage without the method (NASCET-equivalent on CTA/angiography vs duplex velocity band).
- Start short-course DAPT for a "minor stroke" with NIHSS >3, or for a TIA whose ABCD2 was never calculated.
- Write an anticoagulation start day from the 1-3-6-12 rule without the infarct-size category and the haemorrhagic-transformation result from imaging; newer trial data (ELAN, TIMING) support earlier DOAC starts `[VERIFY: current guideline]`.
- Assume clopidogrel response when CYP2C19 loss-of-function status is known — CHANCE-2 used ticagrelor-aspirin in carriers `[VERIFY]`.

✅ **DO:**
- Recompute ABCD2 from the input and show the sum: age ≥60 (1); BP ≥140/90 (1); unilateral weakness (2) or speech disturbance without weakness (1); duration ≥60 min (2) or 10–59 min (1); diabetes (1).
- Date every time-limited line: DAPT start date + 21 (or 90) days = the stated stop date; CEA target date within 14 days of the event date in the input.
- Trace each target (BP, LDL) to the guideline or trial it comes from and to the patient's current value, so the gap is a computed number, not a restated goal.

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
