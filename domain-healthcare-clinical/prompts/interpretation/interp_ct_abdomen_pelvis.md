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
  - belly-pain
  - bowel-blockage
  - unexpected-scan-finding
updated: "2026-09-24"
related_prompts:
  - domain-healthcare-clinical/prompts/reasoning/workup_abdominal_pain.md
  - domain-healthcare-clinical/prompts/specialty/specialty_pancreatitis_severity_management.md
  - domain-healthcare-clinical/prompts/reasoning/medicine_incidental_findings_management.md
---

## Objective

Read a CT abdomen/pelvis report in clinical context and produce an impression that separates operative emergencies from medical and interventional problems, names the severity class of each inflammatory process, and assigns every incidental a guideline-based disposition. Input is the report or structured findings.

Decision support for a licensed clinician: confirm antibiotic and fluid doses, renal adjustment and thresholds against the current guideline and local formulary; the operative decision belongs to the surgeon. A patient with peritonitis, shock, or rising lactate is escalated now, not after this output.

## When to Use

- An ED or inpatient CT abdomen/pelvis report is back and the question is whether it shows a surgical emergency.
- Deciding operative vs interventional vs medical management for obstruction, appendicitis, diverticulitis, pancreatitis, or an obstructed infected kidney.
- Giving every adrenal, renal, pancreatic, liver, or aortic incidental a follow-up and an owner before discharge.

**Not this prompt if:**

- There is no imaging yet and the abdominal pain is being worked up → `domain-healthcare-clinical/prompts/reasoning/workup_abdominal_pain.md`.
- An adrenal mass needs its full biochemical workup → `domain-healthcare-clinical/prompts/specialty/specialty_adrenal_incidentaloma.md`.
- Pancreatitis severity scoring and management beyond the CT read → `domain-healthcare-clinical/prompts/specialty/specialty_pancreatitis_severity_management.md`.

## Inputs

- CT report: protocol (non-contrast stone, portal venous, multiphase, CTA mesenteric), oral contrast yes/no, findings, impression
- Presentation: pain location and timing, peritonitis on exam, vomiting, obstipation, fever, trauma mechanism
- Vitals, lactate, WBC, lipase, LFTs, creatinine, β-hCG where relevant
- Surgical history (adhesions, hernias), anticoagulation, immunosuppression, cancer history
- Prior imaging

## Role

Senior acute care surgeon supporting the treating clinician; reads the CT report in the ED.

## Reasoning Steps

1. **Stop and escalate first if:** hemodynamic instability, peritonitis, free air, suspected closed-loop obstruction or mesenteric ischemia, rupture signs on an aneurysm, active contrast extravasation, or an obstructed infected kidney — call surgery, vascular, IR, or urology now and resuscitate in parallel; the rest of the read does not delay that call. Then **protocol limits.** Non-contrast studies cannot assess bowel wall enhancement, solid-organ injury, or mesenteric vessels. Portal venous phase is not a mesenteric CTA. Absent oral contrast limits leak detection. State the limit when it matters.

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

## Verification

- [ ] Protocol limits (contrast phase, oral contrast) stated wherever they weaken a negative finding.
- [ ] Each emergency (free air, closed loop, ischemia, rupture, active bleed) explicitly declared present or absent before routine findings.
- [ ] Each impression item traced to a report phrase plus the vitals and labs that support it — including whether a temperature actually meets the fever threshold.
- [ ] Thresholds named with their source classification (Revised Atlanta, Bosniak, AAST, aneurysm repair guideline), and antibiotic doses checked against weight, renal function, and local formulary.
- [ ] Every incidental leaves with a named follow-up, interval, and owner.
- [ ] States what would change the plan (exam change, repeat lactate, dedicated imaging).

## False-Positive Prevention

- **Physiologic pelvic free fluid in a menstruating woman called pathologic.** Small volumes are normal in reproductive-age women; the abnormal-fluid rule applies to men and post-menopausal women.
- **Ileus or pseudo-obstruction called mechanical SBO because the report names a "transition".** Require a true caliber change with decompressed distal bowel and a fitting clinical picture.
- **An incidental named as the cause of the pain.** Simple renal cysts, cholelithiasis without inflammation, and diverticulosis without diverticulitis are common background findings.
- **An appendix >6 mm called appendicitis on diameter alone.** Normal appendices can exceed 6 mm; require wall enhancement, periappendiceal stranding, or a fitting exam.
- **Expected post-operative free air or post-procedure change called a perforation or leak** without the interval since surgery and the clinical trend.

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
1. Closed-loop small bowel obstruction with signs of ischemia (reduced enhancement, mesenteric edema, free fluid) in the setting of a low-grade temperature (37.9 °C, below the 38.0 °C fever threshold), peritoneal signs, leukocytosis, and lactate 3.1 — this is not a candidate for non-operative management or a water-soluble contrast challenge. Emergent laparotomy/laparoscopy.
   - Recommend emergent surgical review now; the surgeon decides on and books the operation. Notify anesthesia per local pathway.
   - NPO, NG tube to low intermittent suction.
   - Lactated Ringer's 1 L bolus, then 150 mL/h; reassess perfusion and urine output (Foley).
   - Pre-op antibiotics covering possible bowel necrosis: piperacillin-tazobactam 4.5 g IV (or ceftriaxone 2 g + metronidazole 500 mg IV).
   - Type and screen, BMP, CBC, coags; repeat lactate in 2 h.
   - Hold VTE chemoprophylaxis until post-op plan set.
2. Small free fluid — expected with strangulation; no separate action.
```
