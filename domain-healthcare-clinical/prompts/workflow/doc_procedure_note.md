---
title: "Bedside Procedure Note"
category: domain-healthcare-clinical/workflow
description: "Generate a bedside/clinic procedure note — indication, consent, time-out, technique, specimens, complications, and post-procedure plan — for procedures like central lines, LP, thoracentesis, paracentesis, and intubation."
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate
tags:
  - documentation
  - procedure-note
  - bedside-procedures
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

Produce a procedure note for a bedside or clinic procedure that documents indication, consent, the safety time-out, the technique as performed, any specimens, immediate complications, and the post-procedure plan including confirmatory studies. The note must include the elements required for the record and for billing, and accurately reflect what was done.

## Inputs

- Procedure performed and the indication
- Consent obtained (and from whom; or emergent/implied)
- Operator and supervising attending
- Anesthesia/sedation used (local, moderate sedation)
- Technique details: approach, site, ultrasound guidance, attempts, devices/catheters used
- Specimens obtained (fluid studies, cultures)
- Estimated blood loss, complications (or none)
- Confirmatory study (e.g., post-line CXR) and immediate patient status

## Role

Proceduralist documenting immediately after a bedside procedure.

## Reasoning Steps

1. **Document indication and consent.** State why the procedure was indicated and that informed consent was obtained (risks/benefits/alternatives discussed) — or that it was emergent with implied consent. This is mandatory.

2. **Record the time-out and universal precautions** — patient, procedure, site verified; sterile technique. For invasive procedures this is an audited safety element.

3. **State operator, supervision, and anesthesia/sedation.** If moderate sedation was used, note the agents and that monitoring was in place.

4. **Describe the technique with the specifics that matter:** site and approach, ultrasound guidance if used, number of attempts, catheter/needle type and size, depth, and confirmation of correct placement (blood return, CSF flow, wire-in-vein on US). Document attempts honestly.

5. **Record specimens and what was sent** — fluid appearance, volume removed, and the studies/cultures sent.

6. **Document complications explicitly, including none,** and immediate management of any that occurred (e.g., held pressure, aspirated air).

7. **State the confirmatory plan and immediate status** — post-line CXR ordered/reviewed, patient tolerated procedure, hemodynamics. For central lines, the line is not "usable" until placement is confirmed and pneumothorax excluded where applicable; document that.

8. **Don't fabricate.** Attempts, EBL, and complications must match reality; the note is a medicolegal record.

## False-Positive Prevention

❌ **DON'T:**
- Add the anesthetic concentration, antiseptic agent, anatomic landmarks, "all ports aspirated and flushed", "no arterial puncture" or "hemodynamics unchanged" when the operator did not report them.
- Write "attending present at bedside" when the input says only "supervised" or "aware" — physical presence is a teaching-physician and billing claim.
- State catheter depth at the skin, needle gauge or volume removed from typical values — these are read later to judge malposition and re-accumulation.

✅ **DO:**
- Check the confirmation chain for the procedure type: central line — the venous-confirmation method (ultrasound wire-in-vein, manometry or blood gas) and whether the CXR is ordered or reviewed with tip position; thoracentesis/paracentesis — volume removed; LP — opening pressure with patient position.
- Count specimens and match each to a study sent; a fluid study listed without an order, or an order without a specimen, is flagged.
- When the confirmatory study is ordered but not yet reviewed, state the device's usability as pending and carry the study as an open result for handoff.
- Match CONSENT to the input exactly (informed vs emergent/implied) and record the reason implied consent applied.

## Output Format

```
PROCEDURE:
INDICATION:
CONSENT: [informed / emergent-implied; from whom]
OPERATOR: / SUPERVISING ATTENDING:
ANESTHESIA/SEDATION:
TIME-OUT: [performed — patient/procedure/site verified]

TECHNIQUE:
[site/approach, US guidance, attempts, device type/size, placement confirmation, sterile technique]

SPECIMENS: [fluid appearance/volume, studies/cultures sent]
ESTIMATED BLOOD LOSS:
COMPLICATIONS: [none / describe + management]

CONFIRMATION & POST-PROCEDURE:
- [confirmatory study ordered/reviewed]
- [patient status, immediate plan]
```

## Worked Example

**Input:** Right internal jugular central venous catheter placement. Indication: need for vasopressors in septic shock, poor peripheral access. Consent: emergent, implied (patient obtunded), attending aware. Operator resident, supervised by ICU attending. Time-out performed (patient, procedure, right IJ site). Local 1% lidocaine. Full sterile barrier precautions (cap, mask, sterile gown and gloves, full-body drape); chlorhexidine prep, allowed to dry. Ultrasound-guided: right IJ patent, compressible, lateral to carotid. Single attempt, dark non-pulsatile venous blood return, wire visualized in vein, wire removed intact; triple-lumen catheter; all ports aspirated and flushed. Catheter secured, sterile dressing; depth at skin not recorded. EBL minimal. No complications — no arterial puncture, no air aspiration. Hemodynamics unchanged during procedure. Post-line CXR ordered.

**Output:**

```
PROCEDURE: Right internal jugular central venous catheter (triple-lumen) placement.
INDICATION: Septic shock requiring central access for vasopressor administration; inadequate peripheral access.
CONSENT: Emergent procedure; patient obtunded — implied consent. Attending of record aware and supervising.
OPERATOR: Resident / SUPERVISING ATTENDING: ICU attending (supervising; physical presence not documented).
ANESTHESIA/SEDATION: Local 1% lidocaine at the insertion site.
TIME-OUT: Performed — patient identity, procedure, and site (right IJ) verified prior to start.

TECHNIQUE:
Full sterile barrier precautions were used (cap, mask, sterile gown and gloves, full-body drape). The right neck was prepped with chlorhexidine and allowed to dry. Under real-time ultrasound guidance, the right internal jugular vein was identified, patent, and compressible, lateral to the carotid artery. The vein was accessed on the first attempt with the introducer needle, with return of non-pulsatile dark venous blood. The guidewire was advanced with the wire visualized within the vein by ultrasound. The needle was removed, the tract dilated, and a triple-lumen catheter advanced over the wire; the wire was removed in its entirety. All ports aspirated blood and flushed without resistance. The catheter was secured (depth at skin not recorded) and a sterile dressing applied.

SPECIMENS: None.
ESTIMATED BLOOD LOSS: Minimal.
COMPLICATIONS: None. No arterial puncture, no aspiration of air.

CONFIRMATION & POST-PROCEDURE:
- Portable chest X-ray ordered to confirm catheter tip position and exclude pneumothorax prior to use for any infusion not already running.
- Catheter not to be used for central infusions until placement is confirmed on imaging.
- Patient tolerated the procedure; hemodynamics unchanged during the procedure.
```
