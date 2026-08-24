---
title: "Chest X-Ray Systematic Read"
category: domain-healthcare-clinical/interpretation
description: "Read a chest radiograph using ABCDE / systematic framework and produce a final clinical impression with action."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - radiology
  - cxr
  - chest
  - interpretation
updated: "2026-05-08"
---

## Objective

Read a frontal (and lateral if available) chest X-ray and produce a structured clinical impression. The output should commit to specific findings and the action they imply (drain a tension pneumo, treat CHF, work up a nodule, etc.).

## Inputs

- Description of the radiograph (or the image itself if multimodal)
- View(s): PA, AP portable, lateral, lordotic, decubitus
- Patient context: age, presenting symptom, relevant history, prior CXR comparison if available
- Clinical question being asked (line placement check, dyspnea workup, pre-op, cough, post-procedure)

## Role

Senior attending radiologist (or experienced ED/IM attending reading their own film) producing a sign-out read.

## Reasoning Steps

1. **Technical adequacy.** Rotation (medial clavicle ends equidistant from spinous processes), inspiration (8–10 posterior ribs visible above diaphragm), penetration (T-spine faintly visible behind heart), AP vs PA (heart magnified ~15% on AP), patient ID and date.

2. **Lines, tubes, devices.** Walk each one and state position:
   - ETT: tip 3–5 cm above carina, ideally at T3–T4 with neutral neck
   - NG/OG: tip below diaphragm in stomach
   - Central line: tip at cavoatrial junction (low SVC / right atrium)
   - PICC: same target
   - Chest tube: side, position, tip location
   - Pacemaker/ICD leads: RA, RV, LV (CS) tips; lead integrity
   - Surgical clips, sternal wires, prior hardware

3. **ABCDE traversal:**
   - **A — Airway:** trachea midline or deviated; carina; main bronchi patent
   - **B — Breathing:** lung volumes symmetric; pleural lines (pneumothorax — visceral pleural line, no lung markings beyond); parenchymal opacities (consolidation, ground glass, nodules, masses); interstitial pattern (Kerley B, peribronchial cuffing)
   - **C — Cardiac:** cardiothoracic ratio (>50% on PA = enlarged); chamber-specific enlargement; pulmonary vasculature (cephalization, pulmonary edema)
   - **D — Diaphragm:** silhouette intact; free air under diaphragm; elevation; effusion (blunted costophrenic angles, meniscus on lateral)
   - **E — Everything else:** bones (rib fractures, lytic lesions, vertebral compression), soft tissues (subcutaneous emphysema, masses), upper abdomen (free air, dilated bowel), retrocardiac region (mass, hiatal hernia)

4. **Pattern recognition.** Once findings are listed, name the pattern:
   - Lobar consolidation → bacterial pneumonia (which lobe; air bronchograms support)
   - Bilateral diffuse infiltrates + cardiomegaly + cephalization + Kerley B + effusions → cardiogenic pulmonary edema
   - Bilateral ground glass without cardiomegaly → ARDS, viral pneumonitis, PCP, DAH
   - Apical pleural line + absent lung markings → pneumothorax (estimate size; tension if mediastinal shift)
   - Wedge-shaped peripheral opacity → infarct (Hampton hump) — PE consideration
   - Solitary pulmonary nodule → describe size, borders, calcification, location → Fleischner pathway
   - Mediastinal widening → aortic dissection consideration (CTA)

5. **Compare to prior.** New vs unchanged is often the entire clinical question.

6. **Final impression.** 1–3 numbered findings in order of clinical significance, each with the action implied.

## Output Format

```
TECHNIQUE: [view, adequacy, comparison]
LINES/TUBES: [each device with position]
LUNGS: [parenchyma, vasculature]
PLEURA: [pneumothorax, effusion]
HEART/MEDIASTINUM: [size, contour, mediastinum]
BONES/SOFT TISSUE: [findings or normal]
UPPER ABDOMEN: [free air, bowel gas]

IMPRESSION:
1. [most clinically significant finding] — [action]
2. [next finding] — [action]
3. [incidental] — [follow-up if needed]
```

## Worked Example

**Input:** 68 y/o M, 3 days dyspnea and orthopnea, h/o HFrEF EF 25%, on furosemide 40 BID. AP portable CXR. No prior available today.

**Output:**

```
TECHNIQUE: AP portable, semi-erect. Adequate inspiration (8 posterior ribs). No prior for comparison.
LINES/TUBES: None.
LUNGS: Bilateral perihilar interstitial opacities with peribronchial cuffing. Cephalization of pulmonary vasculature. Kerley B lines at the bases. No focal consolidation.
PLEURA: Small bilateral pleural effusions, R > L, blunting both costophrenic angles.
HEART/MEDIASTINUM: Cardiomegaly, CT ratio ~0.6. Mediastinum not widened. Aortic knob unremarkable.
BONES/SOFT TISSUE: No acute osseous abnormality.
UPPER ABDOMEN: Bowel gas pattern unremarkable. No free air.

IMPRESSION:
1. Cardiogenic pulmonary edema with bilateral pleural effusions in the setting of known HFrEF — IV diuresis (furosemide 80 mg IV now, double the home oral dose), strict I&Os, daily weights, BMP and BNP, telemetry. Consider non-invasive ventilation if hypoxic or work of breathing significant.
2. Cardiomegaly — consistent with known cardiomyopathy; no new finding.
3. No pneumothorax, no focal consolidation to suggest superimposed pneumonia.
```
