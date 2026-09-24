---
title: "CT Chest Report Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Read a CT chest or CTPA report by protocol, then commit to action on PE with RV strain, parenchymal patterns, pleura, mediastinum, aorta, and Fleischner-tracked nodules and incidentals."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - pulmonology
  - radiology
  - ct-chest
  - pulmonary-embolism
  - interpretation
  - blood-clot-in-lung
  - spot-on-lung
  - short-of-breath
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/interpretation/interp_cxr_systematic_read.md
  - domain-healthcare-clinical/prompts/pharmacology/pharm_doac_selection_by_profile.md
  - domain-healthcare-clinical/prompts/specialty/specialty_solitary_pulmonary_nodule_fleischner.md
---

## Objective

Read a CT chest report — routine contrast, non-contrast, CT pulmonary angiogram, HRCT, low-dose screening, or CTA aorta — and produce an impression that states what the protocol can answer, classifies each finding, risk-stratifies acute findings, and closes the loop on every incidental with a named follow-up. Input is the report or structured findings, not pixels.

Decision support for a licensed clinician: confirm anticoagulant and thrombolytic doses, renal adjustment and thresholds against the current guideline and local formulary. A hypotensive or deteriorating patient is escalated now, not after this output.

## When to Use

- A CTPA shows pulmonary embolism and the risk class and first-hour plan need committing.
- A routine, HRCT, or CTA chest report needs its parenchymal, pleural, mediastinal, or aortic findings turned into action.
- A nodule or other incidental needs a guideline interval and an owner before discharge.

**Not this prompt if:**

- The nodule is the whole question (malignancy risk, PET or biopsy decision) → `domain-healthcare-clinical/prompts/specialty/specialty_solitary_pulmonary_nodule_fleischner.md`.
- The study is a chest radiograph → `domain-healthcare-clinical/prompts/interpretation/interp_cxr_systematic_read.md`.
- The interstitial lung disease workup beyond the CT pattern → `domain-healthcare-clinical/prompts/specialty/specialty_ild_workup.md`.

## Inputs

- CT report: protocol, contrast phase, findings, impression, comparison
- Clinical question (PE, dyspnea, pneumonia, cancer staging, ILD, trauma, screening)
- Vitals, SpO2, troponin, BNP/NT-proBNP, lactate if acute
- Smoking history (pack-years, quit date), prior malignancy, immunosuppression, age
- Prior chest imaging

## Role

Senior pulmonary/critical care attending supporting the treating clinician; reads the CT report with the chart open.

## Reasoning Steps

1. **Stop and escalate first if:** PE with hypotension or shock (high-risk — reperfusion decision now), Stanford A dissection, tension pneumothorax, or massive hemoptysis — call the responsible team now and continue the read in parallel. Then **protocol determines what is excluded.** Non-contrast CT cannot exclude PE. Routine venous-phase contrast is suboptimal for PE. CTPA is not a gated aortic study — a "no dissection" read on CTPA is limited. Screening low-dose CT uses Lung-RADS, not Fleischner. Note motion, contrast bolus timing, and transient-interruption artifact that can mimic or hide filling defects.

2. **Pulmonary embolism.**
   - Location and burden: saddle, main, lobar, segmental, subsegmental; unilateral vs bilateral.
   - RV strain on CT: RV:LV diameter ratio >1.0, septal flattening/bowing, contrast reflux into IVC/hepatic veins.
   - Risk-stratify with the whole picture (2019 ESC acute PE guideline): hemodynamic instability → high-risk (massive); normotensive with RV dysfunction + positive troponin → intermediate-high; one of the two, or sPESI ≥1 without RV dysfunction and without troponin rise → intermediate-low; neither + sPESI 0 → low risk (outpatient candidate).
   - Isolated subsegmental PE without DVT in a low-risk patient: management individualized; confirm it is real (artifact is common at this level).

3. **Parenchymal patterns.**
   - Lobar/segmental consolidation with air bronchograms → bacterial pneumonia; cavitation → S. aureus, Klebsiella, anaerobes/aspiration, TB, fungal, septic emboli, squamous cell carcinoma.
   - Tree-in-bud → infectious bronchiolitis, aspiration, endobronchial TB/NTM spread.
   - Diffuse ground glass → edema, viral/PJP pneumonia, DAH, drug pneumonitis, ARDS; crazy paving adds alveolar proteinosis, PJP, DAH.
   - Basal, subpleural reticulation with honeycombing and traction bronchiectasis → UIP pattern (IPF if no exposure/CTD cause).
   - Mosaic attenuation → small-airways disease (air trapping on expiratory images) vs chronic thromboembolic disease.
   - Emphysema: centrilobular (smoking), panlobular lower-lobe (A1AT deficiency), paraseptal.

4. **Nodules — Fleischner 2017 (incidental, age ≥35, no known cancer, not immunocompromised).**
   - Solid, single: <6 mm → no routine follow-up (low risk) or optional CT at 12 months (high risk); 6–8 mm → low risk: CT at 6–12 months, then consider CT at 18–24 months; high risk: CT at 6–12 months, then CT at 18–24 months; >8 mm → CT at 3 months, PET/CT, or tissue sampling.
   - Pure ground-glass ≥6 mm → CT at 6–12 months, then every 2 years to 5 years.
   - Part-solid ≥6 mm → CT at 3–6 months; persistent with solid component ≥6 mm is highly suspicious.
   - Upper-lobe location, spiculation, emphysema, and smoking history raise risk.

5. **Pleura.** Effusion size and whether loculated; split-pleura sign → empyema; pleural nodularity/thickening >1 cm or mediastinal pleural involvement → malignancy; pneumothorax size and tension signs.

6. **Mediastinum, hila, aorta, heart.** Nodes >1 cm short axis are enlarged (reactive nodes are common in pneumonia and HF). Aortic dissection: Stanford A (ascending) → cardiothoracic surgery emergently; B → medical/endovascular. Aneurysm diameter against current aortic guideline repair thresholds. Pericardial effusion. Coronary artery calcification → statin/ASCVD risk discussion even on a non-gated study.

7. **Upper abdomen and bones.** Adrenal nodule ≤10 HU on non-contrast = lipid-rich adenoma; liver lesions; lytic/blastic bone lesions; vertebral compression fractures (osteoporosis workup).

8. **Pitfalls before signing.** Dependent atelectasis read as consolidation; mixing artifact read as PE; "nodule — clinical correlation" never ordered; acute findings crowding out incidentals that then get lost at discharge. Every incidental leaves with a named interval and an owner.

## Output Format

```
STUDY: [protocol, contrast phase, quality, comparison, what it cannot answer]
VESSELS: [PE location/burden, RV:LV, reflux; aorta]
LUNGS: [pattern, distribution, nodules with size/type]
PLEURA: [effusion, pneumothorax, thickening]
MEDIASTINUM/HEART: [nodes, pericardium, coronary calcium]
UPPER ABDOMEN/BONES: [findings]

IMPRESSION:
1. [acute finding + risk stratum] — [action with doses]
2. [next finding] — [action]
3. [incidental] — [guideline follow-up interval and owner]
```

## Verification

- [ ] The protocol's blind spots are stated (non-contrast for PE, CTPA for the aorta, low-dose screening CT read with Lung-RADS).
- [ ] PE risk class derived from hemodynamics, RV findings, troponin, and sPESI per the 2019 ESC acute PE guideline, with each criterion named from the input.
- [ ] Heparin and thrombolytic doses checked against weight, renal function, bleeding risk, and the local nomogram.
- [ ] Each nodule follow-up uses the correct Fleischner 2017 arm (size, solid vs subsolid, single vs multiple, low vs high risk) and names an owner.
- [ ] Each impression item traced to a report phrase and a clinical value.
- [ ] States what would change the risk class or plan (echo, repeat troponin, BP trend, comparison imaging).

## False-Positive Prevention

- **Fleischner applied where it does not belong.** It excludes age <35, known cancer, immunosuppression, and screening CT; using it there over- or under-calls follow-up.
- **Reactive mediastinal nodes in pneumonia or heart failure called malignant adenopathy.** Size >1 cm short axis alone does not establish malignancy.
- **CT RV:LV >1.0 alone called intermediate-high risk.** That class needs both RV dysfunction and a positive troponin in a normotensive patient.
- **Typical perifissural (intrapulmonary lymph node) nodules put on a cancer follow-up pathway.** Smooth, triangular or lentiform fissural nodules usually need no follow-up.

## Worked Example

**Input:** 58 y/o M, 3 days progressive dyspnea after a long-haul flight. HR 112, BP 118/76, SpO2 91% on 4 L, weight 90 kg, Cr 0.9. hs-troponin elevated at 2× URL, NT-proBNP 1,850. 35 pack-year smoker, quit 2 years ago. CTPA report: "Bilateral filling defects in the right and left lower lobe pulmonary arteries extending into segmental branches. RV:LV ratio 1.3 with flattening of the interventricular septum and reflux of contrast into the IVC. 7 mm solid nodule in the right upper lobe, smooth margins. Mild centrilobular emphysema. No effusion."

**Output:**

```
STUDY: CTPA, diagnostic quality for PE to segmental level. No prior.
VESSELS: Bilateral lobar and segmental PE. CT RV strain: RV:LV 1.3, septal flattening, IVC reflux.
LUNGS: 7 mm solid RUL nodule, smooth; mild centrilobular emphysema.
PLEURA: No effusion or pneumothorax.
MEDIASTINUM/HEART: RV dilatation as above.
UPPER ABDOMEN/BONES: Not reported abnormal.

IMPRESSION:
1. Intermediate-high risk PE (normotensive, RV dysfunction on CT, positive troponin).
   - Unfractionated heparin (keeps the lysis/catheter option open): 80 units/kg IV bolus (7,200 units), then 18 units/kg/h (1,620 units/h), titrate to anti-Xa or aPTT nomogram.
   - Activate PE response team; ICU or step-down with continuous monitoring.
   - Rescue plan documented now: if SBP <90 for 15 min or vasopressor need → alteplase 100 mg IV over 2 h (stop heparin during infusion), or catheter-directed therapy if bleeding risk prohibits.
   - Bedside echo to confirm RV function; bilateral lower-extremity dopplers.
   - Avoid large fluid boluses (worsens RV dilation); low threshold for norepinephrine if pressure falls.
   - Transition to DOAC once stable 24–48 h without escalation; provoked (travel) — 3 months minimum, reassess.
2. 7 mm solid RUL nodule in a high-risk patient (35 pack-years, upper lobe, emphysema) — Fleischner 2017 high-risk arm: CT chest at 6–12 months, then CT at 18–24 months. Also meets lung cancer screening criteria; enroll after the interval CT. Write in discharge summary with PCP as owner.
3. Centrilobular emphysema — spirometry once recovered from PE; smoking abstinence reinforced.
```
