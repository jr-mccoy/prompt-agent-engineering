---
title: "Chest Pain Diagnostic Workup"
category: domain-healthcare-clinical/reasoning
description: "Risk-stratify and work up undifferentiated chest pain across cardiac, pulmonary, GI, MSK, and dissection etiologies with named decision rules and disposition logic."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - cardiology
  - emergency-medicine
  - diagnostic-workup
  - chest-pain
updated: "2026-05-08"
---

## Objective

Work up undifferentiated chest pain in an adult patient: rule out the five life-threats (ACS, aortic dissection, PE, tension pneumothorax, esophageal rupture), risk-stratify with named decision rules, order the right tests in the right sequence, and disposition.

## Inputs

- Pain character: onset (sudden vs gradual), quality (pressure/tearing/sharp/burning), location, radiation, duration, exertional vs rest, pleuritic, positional
- Associated symptoms: dyspnea, diaphoresis, nausea, syncope, hemoptysis, fever
- Vitals (both arms BP if dissection considered), SpO2
- Risk factors: ASCVD risk (age, sex, HTN, DM, smoking, FHx, lipids), prior CAD/PCI/CABG, recent immobility/surgery/malignancy/estrogen, connective tissue disease, cocaine
- ECG (ideally within 10 minutes of arrival)
- Initial troponin (high-sensitivity preferred); CXR; basic labs
- Exam: equal pulses/BP both arms, JVD, murmurs, lung exam, leg exam (DVT)

## Reasoning Steps

1. **Life-threat sweep first.** Before pattern-matching to a benign cause, run the five killers:
   - **ACS:** pressure/squeezing, exertional, radiation, diaphoresis, dyspnea — ECG + troponin.
   - **Aortic dissection:** sudden tearing pain radiating to back, BP differential >20 mmHg between arms, pulse deficit, new AI murmur, neurologic deficit, syncope. Mediastinal widening on CXR (only ~60% sensitive).
   - **PE:** pleuritic pain, dyspnea, tachycardia, hypoxia, unilateral leg swelling. Risk factors: recent surgery/immobility, malignancy, estrogen, prior VTE.
   - **Tension pneumothorax:** sudden pleuritic pain, dyspnea, hypotension, tracheal deviation, absent breath sounds — clinical diagnosis, do not wait for CXR; needle decompression.
   - **Esophageal rupture (Boerhaave):** vomiting then severe chest/upper-abdominal pain, subcutaneous emphysema, mediastinal air on CXR/CT.

2. **ECG immediately (≤10 min).**
   - STEMI criteria → cath lab activation. ST depression V1–V3 with tall R → posterior MI (do V7–V9). New LBBB with concerning picture → Sgarbossa. Wellens (biphasic/deeply inverted T V2–V3 in pain-free state) → proximal LAD lesion. De Winter T waves → STEMI-equivalent.
   - Sinus tachycardia, S1Q3T3, T-wave inversion V1–V4, RBBB → consider PE.
   - Diffuse ST elevation with PR depression → pericarditis.
   - Low voltage with electrical alternans → tamponade.
   - Always compare to prior if available.

3. **Apply HEART score for ED chest pain risk stratification.**
   - History (slightly/moderately/highly suspicious), ECG (normal/non-specific repol/significant ST deviation), Age (<45/45–64/≥65), Risk factors (0/1–2/≥3 or known atherosclerotic disease), Troponin (normal/1–3× ULN/>3× ULN). Score 0–10.
   - **0–3 low risk:** ~2% MACE at 6 weeks; consider discharge with outpatient follow-up if shared decision; serial troponins if hsTn protocol.
   - **4–6 moderate:** observation, serial troponins (0/1-h or 0/3-h hsTn algorithm), stress test or CTCA before discharge.
   - **≥7 high:** admit, cardiology consult, early invasive strategy if ACS confirmed.

4. **High-sensitivity troponin algorithms.**
   - **ESC 0/1-h algorithm (hs-cTnT):** rule-out if initial <5 ng/L AND symptom onset >3 h, OR if 0-h <12 ng/L and 1-h delta <3 ng/L. Rule-in if 0-h ≥52 ng/L OR delta ≥5 ng/L. Observation in between.
   - Repeat hsTn at 3 h if borderline. Single elevated hsTn does not diagnose ACS — requires rise/fall pattern with clinical context.
   - Type 2 MI from demand (sepsis, anemia, tachyarrhythmia, hypotension) does not always need cath; treat trigger.

5. **PE workup: Wells + PERC + d-dimer pathway.**
   - **PERC** (rule-out criteria for low-pretest probability only): age <50, HR <100, SpO2 ≥95%, no hemoptysis, no estrogen, no prior DVT/PE, no recent surgery/trauma, no unilateral leg swelling. All 8 negative + low pretest → PE excluded without further workup.
   - **Wells score:** clinical signs DVT (3), PE most likely diagnosis (3), HR >100 (1.5), immobilization/surgery 4 wks (1.5), prior DVT/PE (1.5), hemoptysis (1), malignancy (1). ≤4 PE unlikely; >4 PE likely.
   - **YEARS algorithm** simplifies: clinical signs DVT, hemoptysis, PE most likely. If 0 criteria, d-dimer cutoff <1000 ng/mL excludes; if ≥1, cutoff <500.
   - **Age-adjusted d-dimer:** age × 10 ng/mL FEU for patients >50.
   - PE likely or d-dimer positive → CTPA. V/Q scan if pregnancy or contrast contraindicated.

6. **Aortic dissection: ADD-RS + d-dimer.**
   - **Aortic Dissection Detection Risk Score (ADD-RS):** 0–3 categories (predisposing conditions, pain features, exam features). 0 = low; 1 = intermediate; ≥2 = high.
   - ADD-RS 0 + d-dimer <500 ng/mL FEU = sensitive rule-out (ADvISED study).
   - ADD-RS ≥1 or any clinical concern → CTA chest/abdomen/pelvis (or TEE if unstable). Type A → emergent surgery; Type B → BP and HR control (esmolol or labetalol IV, target SBP 100–120 and HR <60), ICU.

7. **Ancillary patterns.**
   - **Pericarditis:** sharp pleuritic chest pain, worse supine, better leaning forward, friction rub, diffuse ST elevation with PR depression. NSAIDs (ibuprofen 600–800 mg TID × 1–2 weeks) + colchicine 0.5–0.6 mg BID × 3 months. Echo to evaluate for effusion/tamponade.
   - **Tamponade:** Beck triad (hypotension, JVD, muffled heart sounds), pulsus paradoxus >10 mmHg, low voltage and electrical alternans on ECG. Echo confirms; pericardiocentesis if hemodynamic compromise.
   - **Pneumonia:** fever, productive cough, focal crackles, infiltrate on CXR. Treat per CAP guidelines.
   - **GERD / esophageal spasm:** burning, postprandial, supine, responds to antacid; do not anchor here until cardiac excluded in older or higher-risk patients.
   - **MSK / costochondritis:** reproducible with palpation, recent exertion or cough; diagnosis of exclusion in higher-risk patients.
   - **Cocaine chest pain:** treat ACS but avoid beta-blockers acutely (unopposed alpha vasoconstriction); benzodiazepines, NTG, calcium channel blockers; ECG/troponin standard rule-out.
   - **Herpes zoster:** unilateral dermatomal pain preceding rash by days; high suspicion in immunocompromised.

8. **Disposition.**
   - Life-threat confirmed → appropriate emergent management and admission (cath lab, OR, ICU).
   - Low-risk HEART (0–3) with negative serial hsTn → discharge with PCP follow-up 24–72 h, outpatient stress or CTCA if indicated.
   - Moderate HEART → observation unit, serial troponin, stress or CTCA before discharge.
   - High HEART or positive troponin → admit, cardiology, treat as NSTEMI pathway.
   - Document specific reasoning if discharging chest pain.

## Output Format

```
LIFE-THREAT SCREEN:
- ACS: [excluded/active workup/confirmed]
- Dissection: [ADD-RS, plan]
- PE: [Wells/PERC/d-dimer/CTPA plan]
- Pneumothorax: [excluded/management]
- Esophageal rupture: [excluded/active workup]

ECG INTERPRETATION:
- Rhythm, axis, intervals, ischemic changes
- Comparison to prior

INITIAL LABS / IMAGING:
- hsTn 0-h: [value], plan for serial timing
- CXR: [findings]
- D-dimer: [if indicated, value, age-adjusted cutoff]
- Other: [BMP, lactate, BNP, etc.]

RISK STRATIFICATION:
- HEART score: [breakdown, total, risk tier]
- Wells / PERC / ADD-RS as applicable

WORKING DIFFERENTIAL:
1. [most likely with reasoning]
2. [second]
3. [third]

PLAN:
- Immediate: [meds, monitoring, consults]
- Disposition: [discharge / obs / admit / cath lab]
- Follow-up testing: [stress, CTCA, echo, pulm CT]
- Patient instructions if discharged
```

## Worked Example

**Input:** 62 y/o F, HTN, DM, dyslipidemia, smoker, presents with 2 hours of substernal pressure radiating to left arm, diaphoresis, nausea. BP 148/86 R arm, 142/84 L arm. HR 96. SpO2 96%. ECG: 1 mm ST depression V4–V6 with T-wave flattening. Initial hs-cTnT 28 ng/L (ULN 14). CXR clear.

**Output:**

```
LIFE-THREAT SCREEN:
- ACS: active workup — pressure pain with radiation, diaphoresis, dynamic ECG changes, elevated hsTn. Most likely NSTEMI.
- Dissection: ADD-RS 0 (no predisposing condition, no tearing, no pulse/BP differential). Low concern; no CTA at this time.
- PE: no pleuritic component, no hypoxia, no tachycardia >100, no risk factors elicited; PERC negative if confirmed (need to verify no estrogen, no recent surgery). PE not pursued unless clinical evolution.
- Pneumothorax: clear CXR, normal breath sounds.
- Esophageal rupture: no preceding emesis, no subcutaneous emphysema.

ECG INTERPRETATION:
- Sinus rhythm, normal axis, normal intervals.
- 1 mm ST depression V4–V6 with T-wave flattening — suggests subendocardial ischemia, likely lateral/anterolateral.
- No ST elevation; no Sgarbossa criteria.
- Compare to prior if available; serial ECGs q15–30 min while symptomatic.

INITIAL LABS / IMAGING:
- hs-cTnT 0-h: 28 ng/L (elevated, 2× ULN). Repeat at 1 h (ESC 0/1-h algorithm) — delta ≥5 ng/L = rule-in NSTEMI.
- CXR: clear, no widened mediastinum, no pneumothorax.
- BMP, CBC, lipid panel, lactate. BNP if heart failure features.
- D-dimer not indicated (PE pretest low and ACS already established).

RISK STRATIFICATION:
- HEART: History 2 (highly suspicious), ECG 2 (significant ST deviation), Age 1 (45–64), Risk factors 2 (≥3: HTN, DM, smoking, dyslipidemia), Troponin 1 (1–3× ULN). Total 8 = HIGH RISK.
- This is NSTEMI by current data.

WORKING DIFFERENTIAL:
1. NSTEMI (most likely) — typical presentation, dynamic ECG, elevated hsTn, multiple risk factors.
2. Unstable angina — less likely now that hsTn elevated.
3. Type 2 MI from demand — possible but no obvious trigger (no sepsis, anemia, tachyarrhythmia).

PLAN:
- Aspirin 325 mg chewed PO now.
- P2Y12 inhibitor — defer until coronary anatomy known if cath within 24 h, or load with clopidogrel 600 mg if cath delayed (institutional preference; ticagrelor 180 mg also acceptable).
- Anticoagulation: enoxaparin 1 mg/kg SC q12h (CrCl appears normal — verify) OR UFH bolus + infusion if invasive imminent.
- Atorvastatin 80 mg PO load.
- Metoprolol tartrate 12.5–25 mg PO once stable, no contraindications (no shock, no severe asthma, no high-degree block).
- Sublingual NTG 0.4 mg q5 min × 3 for active pain; IV NTG infusion if persistent.
- Continuous telemetry, repeat ECG q15 min while symptomatic, repeat hsTn at 1 h.
- Cardiology consult — early invasive strategy (within 24 h) given GRACE likely >140, dynamic ECG, hsTn rise.
- Disposition: admit to telemetry/CCU pending cath.
- Echocardiogram before or after cath for EF.
- Initiate secondary prevention discussion (DAPT, statin, BB, ACE/ARB, smoking cessation, cardiac rehab, BP/DM/lipid optimization) prior to discharge.
```
