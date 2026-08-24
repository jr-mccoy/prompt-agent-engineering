---
title: "Acute Ischemic Stroke: tPA and Thrombectomy Decision"
category: domain-healthcare-clinical/acute-care
description: "Run the acute ischemic stroke workflow: NIHSS, time windows, eligibility for IV thrombolysis (alteplase or tenecteplase) and endovascular thrombectomy, and BP management."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - neurology
  - stroke
  - thrombolysis
  - thrombectomy
  - critical-care
updated: "2026-05-08"
---

## Objective

For a patient with suspected acute ischemic stroke, decide on IV thrombolysis (alteplase or tenecteplase) and/or endovascular thrombectomy with named eligibility criteria, time windows, dose, and concurrent BP and supportive management.

## Inputs

- Last known well (LKW) time and time of presentation
- NIHSS score
- Imaging: non-contrast CT head (rule out hemorrhage), CT angiography head/neck (large vessel occlusion?), CT perfusion or MRI for late-window selection
- Vital signs: BP, glucose, temp, SpO2, HR, rhythm
- Medications: anticoagulants (warfarin INR, DOAC and last dose), antiplatelets, recent thrombolytic, recent surgery
- Comorbidities: prior stroke/ICH, recent GI bleed, severe HTN, pregnancy
- Wake-up stroke or unwitnessed onset features

## Reasoning Steps

1. **Door-to-needle / door-to-puncture matters.**
   - Goal door-to-needle ≤45 min, door-to-CT ≤25 min, door-to-puncture (LVO) ≤90 min.
   - Time is brain — 1.9 million neurons lost per minute in untreated LVO.

2. **Initial actions in parallel (first 10 min).**
   - Stroke alert, neurology / stroke team activation.
   - Vitals, glucose fingerstick (treat hypoglycemia immediately — can mimic stroke).
   - IV access ×2.
   - NIHSS by stroke team or trained provider.
   - Non-contrast CT head — rule out hemorrhage, look for early ischemic changes (ASPECTS).
   - CT angiography head/neck if LVO suspected (LVO suggested by NIHSS ≥6, gaze deviation, hemiplegia, aphasia, neglect — not all required).
   - Labs: CBC, BMP, troponin, INR/PTT, glucose, type and screen, pregnancy if applicable.
   - ECG.

3. **Determine time window.**
   - **0–4.5 hours from LKW:** standard IV thrombolysis window.
   - **4.5–9 hours OR wake-up / unknown onset:** thrombolysis possible if MRI DWI/FLAIR mismatch (WAKE-UP, EXTEND) or CT perfusion mismatch (EXTEND).
   - **0–6 hours with LVO:** standard thrombectomy window.
   - **6–24 hours with LVO:** thrombectomy if perfusion-imaging mismatch (DAWN, DEFUSE-3) — small core, large penumbra.

4. **IV thrombolysis eligibility.**
   - **Inclusion:** disabling stroke (NIHSS typically ≥4, but can be lower for disabling deficit), age ≥18, within window.
   - **Absolute exclusions:**
     - Hemorrhage on imaging
     - Severe head trauma in past 3 months
     - Ischemic stroke in past 3 months
     - Suspected SAH
     - Recent intracranial / intraspinal surgery in past 3 months
     - History of intracranial hemorrhage
     - Active internal bleeding
     - Aortic dissection
     - Intracranial neoplasm with hemorrhagic potential
     - Platelets <100, INR >1.7, aPTT >40, coagulopathy
     - Therapeutic LMWH within 24 h
     - DOAC within 48 h (unless specific reversal possible) — newer evidence supports tPA after dabigatran reversal with idarucizumab; emerging data on Xa-inhibitor reversal
     - BP >185/110 (must be lowered before tPA — see step 5)
     - Glucose <50 (treat first; if symptoms persist after correction, can reassess)
     - GI bleed in past 21 days
   - **Relative considerations:** age >80, NIHSS >25 (very large stroke, more hemorrhage risk), prior stroke + diabetes, recent surgery (10–14 days), pregnancy (case-by-case, often given), seizure at onset (if deficit clearly stroke not postictal).

5. **BP management for thrombolysis.**
   - Pre-tPA: must be ≤185/110.
     - Labetalol 10–20 mg IV bolus, may repeat once.
     - Nicardipine infusion 5 mg/h, titrate up by 2.5 mg/h q5–15 min (max 15 mg/h).
     - Clevidipine infusion 1–2 mg/h titrated.
   - During and after tPA (first 24 h): keep BP <180/105.
   - Post-thrombectomy: BP target individualized; in successful recanalization, lower targets (e.g., <140/90) may improve outcomes (BP-TARGET trial showed benefit of <130 SBP post-thrombectomy in some analyses). In unsuccessful recanalization or large established infarct, allow permissive hypertension (<180/105).

6. **Thrombolytic dose.**
   - **Alteplase 0.9 mg/kg IV (max 90 mg).** 10% as bolus over 1 min, remainder over 60 min.
   - **Tenecteplase 0.25 mg/kg IV bolus (max 25 mg)** — single bolus, increasingly preferred (non-inferior or superior in LVO; faster administration; AcT and EXTEND-IA TNK trials).

7. **Thrombectomy eligibility (LVO).**
   - **Standard window (0–6 h):** ICA, M1, basilar, sometimes M2 with disabling deficit. ASPECTS ≥6 on CT. Pre-stroke mRS 0–1.
   - **Late window (6–24 h):** DAWN/DEFUSE-3 criteria — perfusion mismatch (small core, large penumbra). Core typically <70 mL, mismatch ratio >1.8.
   - Both tPA and thrombectomy can be done together (do not skip tPA waiting for thrombectomy if both indicated and time permits).

8. **Post-treatment monitoring.**
   - ICU or stroke unit.
   - Neuro checks q15 min × 2 h, q30 min × 6 h, q1h × 16 h.
   - BP per protocol.
   - 24-hour CT or MRI to assess for hemorrhagic transformation.
   - No antithrombotics for 24 hours after tPA; restart aspirin after 24-h imaging confirms no hemorrhage.
   - No central lines, NG tubes, arterial lines for 24 h after tPA unless absolutely necessary.

9. **Etiology workup (concurrent and post-acute).**
   - ECG and telemetry × 24 h minimum (atrial fibrillation).
   - Echo: TTE for LV thrombus, valvular disease, EF, PFO bubble study if cryptogenic in young patient.
   - Carotid imaging if anterior circulation: CTA, MRA, or duplex.
   - Lipid panel, HbA1c, smoking status, BP.
   - Cryptogenic + young: hypercoagulability workup, autoimmune, drug screen, prolonged cardiac monitoring (e.g., implantable loop recorder).

10. **Secondary prevention initiated by 48 h.**
    - Antiplatelet (aspirin 81 mg or clopidogrel 75 mg) for non-cardioembolic stroke; dual antiplatelet (DAPT) for 21–90 days for minor stroke or TIA (CHANCE/POINT).
    - Anticoagulation for cardioembolic (AFib): DOAC preferred unless mechanical valve or moderate-severe MS (warfarin). Timing of initiation: 1–14 days post-stroke depending on infarct size and risk.
    - Statin: high-intensity (atorvastatin 80 or rosuvastatin 40).
    - BP control: ACE/ARB or CCB; goal long-term <130/80.
    - Smoking cessation, glycemic control, sleep apnea screen.

## Output Format

```
PRESENTATION: NIHSS [score], deficits [list]
LKW: [time]
TIME FROM LKW: [hours]
IMAGING: [CT findings, LVO yes/no, ASPECTS, perfusion mismatch if late]

ELIGIBILITY:
- IV thrombolysis: [eligible/not, reason]
- Thrombectomy: [eligible/not, reason]

BP MANAGEMENT:
- Pre-thrombolysis target: ≤185/110
- [agent, dose if BP elevated]

THROMBOLYTIC:
- [drug, dose, timing]

THROMBECTOMY:
- [indicated, vessel, target time]

MONITORING:
- Stroke unit / ICU
- Neuro checks per protocol
- 24-h imaging

CONCURRENT:
- Etiology workup [list]
- Secondary prevention plan

CONTRAINDICATIONS / PITFALLS:
- [issues identified, accommodations]
```

## Worked Example

**Input:** 72 y/o F, presenting 90 minutes after sudden onset of right hemiplegia, expressive aphasia, and left gaze preference. NIHSS 18. BP 192/108, glucose 142, HR 86 sinus. CT head: no hemorrhage, ASPECTS 9, hyperdense MCA sign on left. CTA: left M1 occlusion. PMH: HTN, AFib on apixaban — last dose was 36 hours ago.

**Output:**

```
PRESENTATION: NIHSS 18 — moderate-to-severe stroke. Right hemiplegia, expressive aphasia, left gaze preference (left hemispheric / dominant hemisphere stroke).
LKW: 90 min before arrival.
TIME FROM LKW: 1.5 hours — well within standard windows for both tPA (0–4.5 h) and thrombectomy (0–6 h).
IMAGING: Non-contrast CT — no hemorrhage, ASPECTS 9 (large salvageable territory), hyperdense MCA. CTA — left M1 occlusion. Confirmed LVO.

ELIGIBILITY:
- IV thrombolysis: complicated by apixaban exposure 36 hours ago. Within standard exclusion of "DOAC within 48 hours" — but specific apixaban reversal (andexanet alfa) before tPA carries unproven risk-benefit; many centers proceed to thrombectomy without tPA in this scenario. Some centers measure anti-Xa (drug-calibrated for apixaban) and proceed with tPA if level low — this is institutional. Default decision: skip tPA, proceed directly to thrombectomy (given LVO, this is the higher-yield intervention regardless).
- Thrombectomy: indicated. Left M1 occlusion, NIHSS 18, ASPECTS 9, within 6-h window, pre-stroke functional status independent (assumed).

BP MANAGEMENT:
- BP 192/108 — would block tPA (>185/110). For thrombectomy, do not over-correct because some perfusion is being maintained by collaterals; aim 140–180 systolic pre-procedure. Post-recanalization, lower target (<140 SBP) per BP-TARGET-style protocols.
- Labetalol 10 mg IV now, may repeat. Or nicardipine infusion at 5 mg/h titrated.
- Avoid dropping too fast; target SBP 160–180 for now.

THROMBOLYTIC:
- Skipped due to recent DOAC exposure (apixaban 36 h ago). Document the discussion.
- If center has andexanet and protocols, reversal followed by tPA is an option; coordinate with neurology and pharmacy.

THROMBECTOMY:
- Activate neurointerventional team immediately.
- Door-to-puncture goal ≤90 min.
- Anesthesia: conscious sedation preferred over GA where possible (less BP variability, better outcomes in some studies). General anesthesia for combative patients or compromised airway.
- Maintain SBP 140–180 during procedure; avoid hypotension.

MONITORING (post-procedure):
- Neuro ICU.
- Neuro checks q15 min × 2 h, then q30 min × 6 h, q1h × 16 h.
- 24-hour CT or MRI to assess hemorrhagic transformation.
- BP target post-recanalization: <140/90 if recanalization successful (TICI 2b-3); if unsuccessful, allow permissive HTN <180/105.

CONCURRENT:
- Etiology: known AFib on apixaban. Restart anticoagulation timing depends on infarct size — typically 4–14 days for moderate/large infarct. Bridge with aspirin 81 mg starting 24 h post-procedure if no hemorrhage on imaging.
- TTE for LV thrombus and structural disease.
- Lipid panel, HbA1c, ASCVD risk.
- Reinforce DOAC adherence — apixaban gap likely contributed.
- Statin: atorvastatin 80 mg daily starting now.
- Antiplatelet: aspirin 81 mg starting 24 h post-procedure once imaging stable; transition or layer with apixaban per neurology recommendation.

CONTRAINDICATIONS / PITFALLS:
- DOAC within 48 h is the key obstacle for tPA in this case — proceeding to thrombectomy alone is reasonable.
- Failure to control BP pre-procedure → procedural risk.
- Over-aggressive BP lowering → hypoperfusion and infarct expansion.
- Missing reversal opportunity if center has andexanet protocol.
- Post-procedure: avoid central lines, NG, art lines if alternatives available; monitor groin access site; femoral hematoma is a common and important complication.
```
