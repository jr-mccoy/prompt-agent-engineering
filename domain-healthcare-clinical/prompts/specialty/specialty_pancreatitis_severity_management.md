---
title: "Acute Pancreatitis Severity and Management"
category: domain-healthcare-clinical/specialty
description: "Confirm acute pancreatitis, grade severity with the revised Atlanta classification and BISAP, find the etiology, and write the fluid, analgesia, nutrition, ERCP, antibiotic, and cholecystectomy plan through local complications."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - gastroenterology
  - pancreatitis
  - hospital-medicine
  - specialty-assessment
updated: "2026-09-24"
---

## Objective

Manage acute pancreatitis from admission through complications: confirm the diagnosis, predict and then classify severity, establish etiology, and write concrete orders for resuscitation, analgesia, feeding, and etiology-directed intervention, plus the plan for collections and necrosis. Distinct from `reasoning/workup_abdominal_pain.md`, which reaches a diagnosis from the chief complaint — this prompt starts once pancreatitis is on the table and carries it through severity and management.

## Inputs

- Symptoms and timing: onset of epigastric pain, radiation to back, vomiting, hours since onset
- Vitals: HR, BP, RR, SpO₂, temperature, urine output, mental status
- Labs: lipase (and/or amylase), CBC with hematocrit, BMP including BUN and creatinine, calcium, glucose, LFTs (ALT, AST, alkaline phosphatase, bilirubin), triglycerides, lactate, ABG or PaO₂ if hypoxemic; repeat values at 24–48 h
- Imaging: right upper quadrant ultrasound; CT or MRI if done (timing and findings)
- Etiology history: alcohol quantity, gallstones, recent ERCP, medications, prior episodes, family history, hypercalcemia, trauma
- Comorbidities: cardiac, renal, pulmonary disease, obesity

## Role

Senior attending gastroenterologist writing the admission plan and daily reassessment for a hospitalist colleague.

## Reasoning Steps

1. **Confirm the diagnosis — 2 of 3:** typical epigastric pain; lipase or amylase >3× upper limit of normal; characteristic imaging. Do not image on day 1 if two criteria are met; CT is for diagnostic doubt or for deterioration after 72 h.

2. **Predict severity at admission.**
   - **BISAP** (1 point each, first 24 h): BUN >25 mg/dL; impaired mental status; SIRS (≥2 criteria); age >60; pleural effusion on imaging. Score ≥3 marks substantially higher mortality.
   - SIRS persisting >48 h, rising BUN or hematocrit at 24 h, and obesity also signal a worse course.
   - Lipase magnitude does not predict severity. Do not trend it.

3. **Classify severity by the revised Atlanta classification (2012)** — this is a classification, finalized once the 48-hour course is known.
   - **Mild:** no organ failure, no local or systemic complications.
   - **Moderately severe:** transient organ failure (resolves within 48 h) and/or local complications and/or exacerbation of comorbid disease.
   - **Severe:** persistent organ failure >48 h (single or multiple).
   - Organ failure = modified Marshall score ≥2 in respiratory (PaO₂/FiO₂ ≤300), renal (creatinine ≥1.9 mg/dL), or cardiovascular (SBP <90 not fluid-responsive).

4. **Name the local complication type** when imaging exists: acute peripancreatic fluid collection (interstitial, <4 weeks) → pseudocyst (>4 weeks, encapsulated); acute necrotic collection (necrotizing, <4 weeks) → walled-off necrosis (>4 weeks). Also portal/splenic vein thrombosis and pseudoaneurysm.

5. **Establish etiology** — it drives the definitive intervention.
   - Gallstones: RUQ ultrasound on everyone. ALT >150 IU/L early supports a biliary cause.
   - Alcohol: quantity and pattern.
   - Triglycerides: >1000 mg/dL is causative; draw early (they fall with fasting).
   - Calcium, medications, post-ERCP, trauma. If none after the first episode: EUS or MRCP for microlithiasis or neoplasm, especially over 40.

6. **Resuscitate with a moderate, goal-directed strategy.** Lactated Ringer's. If hypovolemic, 10 mL/kg bolus, then ~1.5 mL/kg/h; without hypovolemia, no bolus. Reassess at 3, 12, 24, 48, and 72 h (HR, MAP, urine output ≥0.5 mL/kg/h, BUN, hematocrit). Stop or reduce once targets are met and oral intake resumes. Aggressive high-volume resuscitation raises fluid-overload risk without benefit (WATERFALL). Watch lungs and abdominal compartment pressure.

7. **Analgesia.** Opioids are appropriate (e.g., hydromorphone 0.2–0.5 mg IV q2–3h PRN or PCA); multimodal with acetaminophen. NSAIDs only if renal function is normal and there is no AKI risk.

8. **Nutrition.** Mild: oral low-fat solid diet as soon as pain allows, usually within 24 h. No mandatory "NPO until lipase normalizes." If oral intake is not tolerated by ~72 h, or in severe disease: enteral feeding (nasogastric is acceptable; nasojejunal if not tolerated) over parenteral.

9. **Biliary intervention.**
   - ERCP within 24 h for concurrent cholangitis.
   - Persistent biliary obstruction without cholangitis: MRCP or EUS first, ERCP if a stone is confirmed.
   - No urgent ERCP for gallstone pancreatitis without cholangitis or obstruction.
   - Cholecystectomy in the same admission for mild gallstone pancreatitis (PONCHO). In necrotizing pancreatitis, defer until collections resolve or are managed, usually >6 weeks.

10. **Antibiotics.** No prophylactic antibiotics, including for sterile necrosis. Treat extra-pancreatic infection (cholangitis, pneumonia, UTI, bacteremia). Suspect infected necrosis when a patient deteriorates after 7–10 days or CT shows gas in the collection. Use antibiotics that penetrate necrosis (a carbapenem such as meropenem 1 g IV q8h, or a fluoroquinolone plus metronidazole).

11. **Necrosis and collections.** Step-up approach: antibiotics first, then drainage, then necrosectomy. Delay intervention until walled off (≥4 weeks) when possible; endoscopic transluminal drainage is preferred over open surgery. Asymptomatic pseudocysts and sterile necrosis need no drainage regardless of size.

12. **Etiology-specific therapy.** Hypertriglyceridemia: insulin infusion (with dextrose if glucose normal) to drive TG <500 mg/dL; plasmapheresis in selected severe cases; long-term fibrate and diet. Alcohol: brief intervention, withdrawal prophylaxis, and referral. Hypercalcemia: treat the cause.

13. **Verify.** Check the revised Atlanta grade against organ-failure duration, not admission impression. Check the fluid orders against reassessment triggers. Confirm etiology workup is complete before discharge (ultrasound, TG, calcium) and the cholecystectomy plan is booked for biliary cases.

## Output Format

```
DIAGNOSIS: [criteria met]

SEVERITY:
- Predicted (admission): BISAP [n] — [components]; SIRS [present/absent]; BUN/Hct trend
- Revised Atlanta: [mild / moderately severe / severe] — [basis; provisional until 48 h]
- Local complications: [type per Atlanta, or none]

ETIOLOGY: [most likely + supporting data; pending tests]

ORDERS:
- Fluids: [LR rate/bolus, reassessment times, stop criteria]
- Analgesia: [agents, doses]
- Nutrition: [oral diet start or enteral route]
- Biliary: [ERCP yes/no + timing; cholecystectomy timing]
- Antibiotics: [none / indication-specific]
- Monitoring: [vitals, UO, labs, level of care]

COMPLICATION PLAN: [collection/necrosis surveillance and triggers for CT and intervention]

PITFALLS:
- [trending lipase, over-resuscitation, prophylactic antibiotics, early ERCP without cholangitis, missed TG]
```

## Worked Example

**Input:** 68 y/o F, 10 h of epigastric pain radiating to the back, vomiting. HR 112, BP 104/62, RR 22, T 37.6°C, SpO₂ 94% RA, alert. Lipase 4,800 (ULN 60). WBC 15.8, Hct 47%, BUN 29, creatinine 1.1, calcium 8.6, ALT 310, AST 240, alk phos 180, bilirubin 1.6, TG 140. No alcohol. RUQ US: gallbladder with multiple stones, CBD 5 mm. CXR: small left pleural effusion. Weight 70 kg.

**Output:**

```
DIAGNOSIS: Acute pancreatitis — typical pain + lipase 80× ULN. No CT needed now.

SEVERITY:
- Predicted: BISAP 4 (BUN 29, SIRS — HR 112/RR 22/WBC 15.8, age 68, pleural effusion). High-risk: step-down unit.
- Revised Atlanta: provisional. No organ failure yet (SBP >90, creatinine 1.1). Grade finalizes at 48 h.
- Local complications: not assessed; CT only if not improving at 72–96 h.

ETIOLOGY: Biliary — cholelithiasis, ALT 310 in a gallstone patient. TG and calcium exclude those causes.

ORDERS:
- Fluids: hypovolemic (tachycardic, Hct 47%). LR 700 mL (10 mL/kg) bolus, then LR 105 mL/h (1.5 mL/kg/h). Reassess at 3, 12, 24, 48, 72 h: HR <100, MAP ≥65, UO ≥0.5 mL/kg/h, falling BUN/Hct. Reduce when targets met; stop at 48 h if tolerating oral intake. Hold for new hypoxemia or crackles.
- Analgesia: hydromorphone 0.4 mg IV q3h PRN + acetaminophen 1 g IV/PO q8h (max 3 g/day given LFTs).
- Nutrition: low-fat oral diet as pain allows; if not eating by 72 h, NG enteral feeding.
- Biliary: no ERCP now — no cholangitis (afebrile, bilirubin 1.6, no duct dilation). Repeat LFTs at 24 h. If bilirubin rises or CBD dilates → MRCP/EUS, then ERCP for a retained stone. If fever + rising bilirubin/hypotension → ERCP within 24 h.
- Cholecystectomy: same admission once clinically improving, if the course stays mild or moderately severe without necrosis.
- Antibiotics: none. SIRS here is pancreatic inflammation, not infection.
- Monitoring: vitals q2h, strict I/O, SpO₂ continuous; BMP, CBC, LFTs at 12 and 24 h.

COMPLICATION PLAN: If SIRS persists >48 h or organ failure develops → contrast CT at 72–96 h for necrosis. Clinical deterioration at day 7–10 → CT for gas/infected necrosis → meropenem 1 g IV q8h and step-up drainage once walled off.

PITFALLS:
- Do not trend lipase.
- Avoid high-volume resuscitation; her effusion and age raise overload risk.
- No prophylactic antibiotics; no ERCP without cholangitis or proven obstruction.
- Do not discharge without booked cholecystectomy.
```
