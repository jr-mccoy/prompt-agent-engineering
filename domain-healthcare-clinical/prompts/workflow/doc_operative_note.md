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

## False-Positive Prevention

❌ **DON'T:**
- Expand the dictated technique into standard steps the surgeon did not state — time-out, retrieval bag, "doubly clipped", energy device, fascial closure — each is a claim about what was done in this operation.
- Upgrade terse inputs into fuller claims: "general anesthesia" → "general endotracheal", "counts correct" → "correct ×2", or an unstated "extubated in the OR, to PACU stable".
- Add negative findings ("no bile duct injury", "no aberrant anatomy") or "informed consent obtained" that the input does not contain — both carry medicolegal weight.
- Fill FLUIDS / URINE OUTPUT with "adequate"; write `[per anesthesia record — value not provided]`.

✅ **DO:**
- Audit the mandated fields one by one — pre/post-op diagnosis, procedure, surgeon/assistants, anesthesia, indication, findings, specimens, implants, EBL, fluids/UOP, drains, counts, complications, disposition — and confirm each is either sourced from the input or explicitly marked not provided.
- Check that the PROCEDURE(S) PERFORMED line matches the DESCRIPTION exactly (e.g., "with cholangiogram" only if a cholangiogram step is described), because the coder assigns CPT from it — the note never states a code itself.
- Copy implant type, size, lot and serial exactly as supplied, and when pre- and post-op diagnoses or the approach differ, confirm a FINDINGS sentence explains why.

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

**Input:** Laparoscopic cholecystectomy. Preop dx: acute cholecystitis. Postop dx: same. Surgeon Dr. X, assist resident. General endotracheal anesthesia. Indication: ultrasound-confirmed cholecystitis with gallstones, failed medical management; informed consent (risks, benefits, alternatives) obtained and on chart. Findings: distended, inflamed gallbladder with multiple stones, no CBD dilation, normal biliary anatomy, critical view of safety achieved before dividing any structure, no bile duct injury. Technique: supine; time-out performed; prepped and draped sterile; pneumoperitoneum via umbilical port, 4-port laparoscopic under direct vision; gallbladder retracted cephalad, hepatocystic triangle dissected to critical view; cystic duct and artery each doubly clipped and divided; gallbladder dissected from liver bed with electrocautery, liver bed hemostatic; removed in retrieval bag via umbilical port; ports removed under vision, umbilical fascia closed, skin closed, sterile dressings. EBL minimal (<25 mL). Fluids/UOP not dictated (on anesthesia record). No drains. Counts correct x2. No complications. Specimen gallbladder to path. Extubated in OR, to PACU stable.

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
The patient was placed supine. A surgical time-out was performed. General endotracheal anesthesia was induced. The abdomen was prepped and draped in standard sterile fashion. Pneumoperitoneum was established via the umbilical port, and a 4-port laparoscopic approach was established under direct visualization. The gallbladder was retracted cephalad. The hepatocystic triangle was dissected and the critical view of safety was obtained, clearly identifying the cystic duct and cystic artery. Both were doubly clipped and divided. The gallbladder was dissected free from the liver bed using electrocautery; the liver bed was hemostatic. The gallbladder was placed in a retrieval bag and removed through the umbilical port. The ports were removed under direct visualization and the umbilical fascia was closed. Skin incisions were closed and sterile dressings applied.

SPECIMENS: Gallbladder sent to pathology.
IMPLANTS/DEVICES: None.
ESTIMATED BLOOD LOSS: Minimal (<25 mL).
FLUIDS / URINE OUTPUT: [per anesthesia record — value not provided].
DRAINS: None.
COUNTS: Sponge, instrument, and needle counts correct x2.
COMPLICATIONS: None.

DISPOSITION: Patient tolerated the procedure well, was extubated in the operating room, and transferred to the PACU in stable condition.
```
