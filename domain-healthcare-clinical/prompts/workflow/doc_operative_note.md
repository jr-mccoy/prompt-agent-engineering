---
title: "Operative Note"
category: domain-healthcare-clinical/workflow
description: "Generate a complete operative note — preop/postop diagnosis, procedure, findings, technique, specimens, EBL, and disposition — to surgical documentation standard."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: advanced
tags:
  - documentation
  - operative-note
  - surgery
  - clinical-notes
updated: "2026-06-19"
---

## Objective

Produce a complete operative note documenting a surgical procedure to the standard required for the medical record and billing: the required header elements, the intraoperative findings, a stepwise account of the technique, and the immediate disposition. The note must contain every mandated field and accurately reflect what was done.

## Inputs

- Preoperative and postoperative diagnoses
- Procedure(s) performed
- Surgeon, assistants, anesthesia type
- Indication for surgery
- Intraoperative findings
- Step-by-step description of the procedure as performed
- Specimens removed, implants/devices placed
- Estimated blood loss, fluids, drains, counts
- Complications (or explicitly none)
- Patient condition and disposition at end of case

## Role

Operating surgeon dictating the operative note immediately after the case.

## Reasoning Steps

1. **Complete the required header fields** — pre- and postoperative diagnoses (note when they differ and why), procedure(s) performed, surgeon and assistants, anesthesia type. These are mandatory and frequently audited.

2. **State the indication** — a concise sentence on why the operation was done, tying to the diagnosis and any informed-consent context.

3. **Document the findings** — what was actually seen intraoperatively. Findings often justify the procedure and any intraoperative decision-making (e.g., conversion from laparoscopic to open).

4. **Describe the technique stepwise,** in the sequence performed: positioning, prep/drape, incision/access, the key operative steps, hemostasis, closure, and dressings. Be specific enough that another surgeon could follow what was done; include suture types, device sizes, and energy modalities where they matter.

5. **Record specimens and implants** — what was sent to pathology, what was implanted (with type/size/serial where applicable). This is both a clinical and medicolegal requirement.

6. **Document the safety/accounting elements:** estimated blood loss, IV fluids, urine output, drains placed, and that instrument/sponge/needle counts were correct (or the action taken if not).

7. **State complications explicitly** — including "none." A note that omits the complication field is incomplete.

8. **Close with patient condition and disposition** — tolerated the procedure, extubated/condition, transferred to PACU/ICU. Do not embellish or document steps not performed; the note must match the operation.

## Output Format

```
PREOPERATIVE DIAGNOSIS:
POSTOPERATIVE DIAGNOSIS: [note if changed + why]
PROCEDURE(S) PERFORMED:
SURGEON: / ASSISTANT(S):
ANESTHESIA:
INDICATION:

FINDINGS:
[intraoperative findings]

DESCRIPTION OF PROCEDURE:
[stepwise: positioning → prep/drape → access/incision → operative steps → hemostasis → closure → dressing]

SPECIMENS: [sent to pathology]
IMPLANTS/DEVICES: [type/size/serial]
ESTIMATED BLOOD LOSS:
FLUIDS / URINE OUTPUT:
DRAINS:
COUNTS: [sponge/instrument/needle — correct?]
COMPLICATIONS: [none / describe]

DISPOSITION: [patient condition, extubation, transfer location]
```

## Worked Example

**Input:** Laparoscopic cholecystectomy. Preop dx: acute cholecystitis. Postop dx: same. Surgeon Dr. X, assist resident. General anesthesia. Indication: ultrasound-confirmed cholecystitis with gallstones, failed medical management. Findings: distended, inflamed gallbladder with stones, no CBD dilation, critical view of safety achieved. Technique: 4-port laparoscopic, cystic duct and artery clipped and divided, gallbladder dissected from liver bed, removed via umbilical port. EBL minimal (<25 mL). No drains. Counts correct. No complications. Specimen gallbladder to path.

**Output:**

```
PREOPERATIVE DIAGNOSIS: Acute cholecystitis with cholelithiasis.
POSTOPERATIVE DIAGNOSIS: Same.
PROCEDURE(S) PERFORMED: Laparoscopic cholecystectomy.
SURGEON: Dr. X / ASSISTANT(S): Surgical resident.
ANESTHESIA: General endotracheal.
INDICATION: Patient with ultrasound-confirmed acute cholecystitis and cholelithiasis, failed conservative management. Risks, benefits, and alternatives discussed; informed consent obtained.

FINDINGS:
Distended, acutely inflamed gallbladder containing multiple stones. No common bile duct dilation. Critical view of safety was clearly achieved prior to division of any structures. No evidence of bile duct injury or aberrant anatomy.

DESCRIPTION OF PROCEDURE:
The patient was identified, brought to the OR, and placed supine. A surgical time-out was performed confirming patient, procedure, and site. General anesthesia was induced. The abdomen was prepped and draped in standard sterile fashion. Pneumoperitoneum was established via the umbilical port using standard technique, and a 4-port laparoscopic approach was established under direct visualization. The gallbladder was retracted cephalad. The hepatocystic triangle was dissected and the critical view of safety was obtained, clearly identifying the cystic duct and cystic artery. Both were doubly clipped and divided. The gallbladder was dissected free from the liver bed using electrocautery, with attention to hemostasis. The gallbladder was placed in a retrieval bag and removed through the umbilical port. Hemostasis of the liver bed was confirmed. The ports were removed under direct visualization, pneumoperitoneum was released, and the fascial defect at the umbilicus was closed. Skin incisions were closed and sterile dressings applied.

SPECIMENS: Gallbladder sent to pathology.
IMPLANTS/DEVICES: None.
ESTIMATED BLOOD LOSS: Minimal (<25 mL).
FLUIDS / URINE OUTPUT: Per anesthesia record; adequate.
DRAINS: None.
COUNTS: Sponge, instrument, and needle counts correct x2.
COMPLICATIONS: None.

DISPOSITION: Patient tolerated the procedure well, was extubated in the operating room, and transferred to the PACU in stable condition.
```
