---
title: "CT Abdomen and Pelvis Report Interpretation"
category: domain-healthcare-clinical/interpretation
description: "Read a CT abdomen/pelvis report by protocol and organ, identify surgical emergencies (perforation, closed-loop obstruction, ischemia, rupture), grade inflammatory processes, and route incidentals to the correct follow-up."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - general-surgery
  - gastroenterology
  - radiology
  - ct-abdomen
  - interpretation
updated: "2026-09-24"
---

## Objective

Read a CT abdomen/pelvis report in clinical context and produce an impression that separates operative emergencies from medical and interventional problems, names the severity class of each inflammatory process, and assigns every incidental a guideline-based disposition. Input is the report or structured findings.

## Inputs

- CT report: protocol (non-contrast stone, portal venous, multiphase, CTA mesenteric), oral contrast yes/no, findings, impression
- Presentation: pain location and timing, peritonitis on exam, vomiting, obstipation, fever, trauma mechanism
- Vitals, lactate, WBC, lipase, LFTs, creatinine, β-hCG where relevant
- Surgical history (adhesions, hernias), anticoagulation, immunosuppression, cancer history
- Prior imaging

## Role

Senior acute care surgeon reading the CT report in the ED.

## Reasoning Steps

1. **Protocol limits.** Non-contrast studies cannot assess bowel wall enhancement, solid-organ injury, or mesenteric vessels. Portal venous phase is not a mesenteric CTA. Absent oral contrast limits leak detection. State the limit when it matters.

2. **Free air and free fluid.** Pneumoperitoneum without recent surgery → perforated viscus until proven otherwise (post-laparotomy free air can persist days). Free fluid: simple (near water) vs high-density (hemoperitoneum ~30–45 HU; clot higher — sentinel clot localizes the source). Free fluid in a male or post-menopausal woman is abnormal.

3. **Bowel.**
   - **Dilation thresholds ("3-6-9"):** small bowel >3 cm, colon >6 cm, cecum >9 cm.
   - **SBO:** single transition point → adhesive; two adjacent transition points, C/U-shaped loop, mesenteric whirl → closed loop (surgical). Strangulation signs: reduced or absent wall enhancement, wall thickening, mesenteric edema, ascites, pneumatosis, portal venous gas → OR.
   - **Mesenteric ischemia:** SMA embolus/thrombus, SMV thrombosis, non-occlusive pattern; pneumatosis + portal venous gas = transmural ischemia.
   - **Appendicitis:** appendix >6 mm, wall enhancement, periappendiceal stranding, appendicolith; perforation/abscess changes management. "Appendix not visualized" is not "normal appendix."
   - **Diverticulitis:** uncomplicated vs complicated (abscess, free perforation, fistula, obstruction). Abscess ≥3–4 cm → percutaneous drainage; purulent or feculent peritonitis → OR.
   - **Colitis:** segmental distribution (watershed → ischemic), pancolitis (C. difficile, IBD), target sign.

4. **Solid organs and pancreas.**
   - **Pancreatitis:** interstitial vs necrotizing; CT in the first 72 h underestimates necrosis. Revised Atlanta collections: acute peripancreatic fluid collection → pseudocyst (>4 weeks, no necrosis); acute necrotic collection → walled-off necrosis (>4 weeks). Gas in necrosis → infected necrosis.
   - **Gallbladder:** CT is less sensitive than ultrasound; many stones are invisible on CT. Emphysematous cholecystitis is a surgical emergency.
   - **Liver:** abscess, portal/hepatic vein thrombosis, cirrhotic morphology.
   - **Trauma:** organ injury grade (AAST) and active contrast extravasation (blush) → IR or OR regardless of grade if unstable.

5. **Genitourinary.** Hydronephrosis + stone size and location: ≤5 mm distal stones usually pass; >10 mm unlikely. Obstructed + infected kidney → emergent decompression (stent or nephrostomy), not a trial of passage. Pyelonephritis with abscess or emphysematous change. Adnexal torsion/mass in women — ultrasound for ovarian flow.

6. **Vascular.** AAA ≥3 cm; repair threshold commonly 5.5 cm in men, lower in women; rupture signs (retroperitoneal hematoma, draped aorta, crescent sign) → vascular surgery emergently.

7. **Incidentals (route, do not chase).** Adrenal nodule ≤10 HU non-contrast → benign adenoma (functional screen if indicated); ≥4 cm or indeterminate → dedicated protocol. Renal cyst → Bosniak class (I–II benign; IIF follow-up; III–IV surgical referral). Pancreatic cyst → dedicated pancreatic cyst pathway. Liver lesion too small to characterize in a low-risk patient → usually no follow-up. Enlarged nodes, bone lesions → oncologic workup.

8. **Pitfalls before signing.** Fat stranding is non-specific; "mild bowel wall thickening" in an under-distended loop is often nothing; a normal CT does not exclude early appendicitis, early ischemia, or cholecystitis; contrast nephropathy fear should not delay a CTA in suspected mesenteric ischemia; incidentals disappear at discharge unless assigned.

## Output Format

```
STUDY: [protocol, oral contrast, quality, limitations]
EMERGENCIES: [free air / closed loop / ischemia / rupture / active bleed — present or absent]
BOWEL: [dilation, transition, wall, appendix, diverticula]
SOLID ORGANS/PANCREAS: [findings, severity class]
GU: [stones, hydronephrosis, adnexa]
VASCULAR: [aorta, mesenteric vessels]
INCIDENTALS: [finding — disposition]

IMPRESSION:
1. [most significant] — [action: OR / IR / admit / discharge]
2. [next] — [action]
3. [incidental] — [follow-up]
```

## Worked Example

**Input:** 71 y/o F, prior hysterectomy and appendectomy. 18 hours of crampy abdominal pain, bilious vomiting, no flatus. HR 108, BP 104/66, T 37.9, abdomen distended with focal RLQ tenderness and guarding. WBC 16.2, lactate 3.1, Cr 1.2, weight 68 kg. CT A/P with IV contrast, no oral: "Dilated small bowel loops up to 4.2 cm. Two adjacent transition points in the right lower quadrant with a C-shaped cluster of fluid-filled loops and swirling of the mesentery. The involved loops show decreased mural enhancement with mesenteric edema. Small volume free fluid. No pneumatosis or portal venous gas. No free air. Colon decompressed."

**Output:**

```
STUDY: Portal venous IV contrast, no oral. Adequate for wall enhancement.
EMERGENCIES: Closed-loop SBO with strangulation signs. No free air, pneumatosis, or portal venous gas yet.
BOWEL: SB dilated to 4.2 cm (>3 cm), two adjacent transition points, mesenteric whirl, reduced wall enhancement, mesenteric edema. Colon decompressed.
SOLID ORGANS/PANCREAS: Not reported abnormal.
GU: Not reported abnormal.
VASCULAR: Not reported abnormal.
INCIDENTALS: None reported.

IMPRESSION:
1. Closed-loop small bowel obstruction with signs of ischemia (reduced enhancement, mesenteric edema, free fluid) in the setting of fever, peritoneal signs, leukocytosis, and lactate 3.1 — this is not a candidate for non-operative management or a water-soluble contrast challenge. Emergent laparotomy/laparoscopy.
   - OR booked now; surgery and anesthesia notified.
   - NPO, NG tube to low intermittent suction.
   - Lactated Ringer's 1 L bolus, then 150 mL/h; reassess perfusion and urine output (Foley).
   - Pre-op antibiotics covering possible bowel necrosis: piperacillin-tazobactam 4.5 g IV (or ceftriaxone 2 g + metronidazole 500 mg IV).
   - Type and screen, BMP, CBC, coags; repeat lactate in 2 h.
   - Hold VTE chemoprophylaxis until post-op plan set.
2. Small free fluid — expected with strangulation; no separate action.
```
