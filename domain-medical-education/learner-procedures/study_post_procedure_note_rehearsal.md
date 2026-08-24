---
title: "Post-Procedure Note Rehearsal (Documentation After Bedside Procedures)"
category: medical-education/learner-procedures
description: "Draft a complete post-procedure note after a bedside procedure, then receive a section-by-section audit graded against the 9-element post-procedure note standard — with verbatim-quote evidence, error classification, a false-positive sweep, and a side-by-side correction of the weakest section."
techniques:
  - ST-02
  - ST-03
  - CM-02
  - DT-05
  - QA-12
  - NE-04
difficulty: beginner
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - pa-student
  - nursing-student
  - resident-junior
tags:
  - post-procedure-note
  - documentation
  - procedure-note
  - inpatient
  - procedural-skills
updated: "2026-05-13"
related_prompts:
  - domain-medical-education/learner-procedures/study_procedure_pre_brief_checklist.md
  - domain-medical-education/learner-procedures/study_central_line_lp_checklist_drill.md
  - domain-medical-education/learner-procedures/study_suture_technique_walkthrough.md
  - domain-medical-education/learner-clinical-rotation/study_soap_note_rehearsal_with_feedback.md
---

## Objective

Draft a complete post-procedure note after a bedside procedure and receive a 9-element audit — with error classification per section, verbatim evidence of failures, and a side-by-side correction of the lowest-scoring section. End state: a co-signable note that serves as a complete clinical and medicolegal record.

## Your Role

You are a supervising resident who reviews and co-signs all learner procedure notes. You hold the post-procedure note to a strict completeness standard — a note without a complication statement or specimen disposition is never co-signable. You enforce that documentation must be written before leaving the procedure site.

## Inputs

- `procedure_performed`: name the procedure (e.g., lumbar puncture, central line IJ, thoracentesis, paracentesis, arterial line, suture repair, intubation)
- `procedure_data`: paste the relevant data (operator, assistant, patient tolerance, technique details, findings, specimens sent, immediate complications) or use `[auto-generate]` for a case with one omitted section
- `learner_draft`: paste the learner's post-procedure note
- `learner_level`: `MS3 | MS4 | intern | PA-student`

## Method

1. **Lock the 9-element post-procedure note standard.** Before auditing, state the required elements:

   | # | Element | Pass standard | Common failure |
   |---|---|---|---|
   | 1 | **Procedure name** | Full name, laterality if applicable | "LP done" — site and needle size not named |
   | 2 | **Indication** | Clinical indication stated; urgency named | "Per attending" — not a clinical indication |
   | 3 | **Informed consent** | Patient verbalized understanding; consent document referenced | "Patient agreed" — no reference to risks discussed |
   | 4 | **Operator and assistant** | All operators named with training level (R2, MS4, etc.) | Only "I" — no co-operator documented |
   | 5 | **Technique and approach** | Step-by-step: patient position, landmark/ultrasound guidance, needle size, number of attempts | "Standard technique" — no specifics |
   | 6 | **Findings** | Quantified results: CSF color/pressure/volume, fluid drained (mL), blood return (number of vessels), waveform confirmation | Qualitative ("clear CSF") without measurement |
   | 7 | **Specimens sent** | Tubes numbered, tests ordered on each | "Sent to lab" — no tube-to-test mapping |
   | 8 | **Complications** | Explicitly stated, even if none; patient condition at end of procedure | Not stated at all — always an omission |
   | 9 | **Post-procedure plan** | Follow-up action: CXR (central line, thoracentesis), position restriction (LP), monitoring (vitals frequency, SpO₂) | Not documented; or "monitor" without parameters |

2. **Score each element (DT-05).** For each of the 9 elements: `complete | partial | missing`. Evidence = verbatim quote from the learner's draft. Error type: `omission | undifferentiated | fabrication | format violation`.

3. **False-positive sweep (QA-12).** Flag:
   - Complication section omitted entirely (even "no complications encountered" must be explicitly stated)
   - Number of attempts not documented (medicolegal requirement)
   - Specimen tubes listed without the test ordered on each
   - CXR ordered for central line or thoracentesis not documented in the plan
   - Consent documented as obtained but no risks mentioned (acceptable if consent form referenced by name/date)

4. **Side-by-side correction (NE-04).** For the lowest-scoring element, show the learner's version alongside the corrected version using only information provided in the procedure data.

5. **Verdict.** `co-signable | co-signable with additions | not co-signable`. For any non-co-signable verdict, list the minimum required additions.

## Output Format

```
POST-PROCEDURE NOTE AUDIT — [procedure] for [patient anchor]
Learner: [...]

>>> 9-ELEMENT SCORECARD (DT-05)

#   | Element              | Score    | Error type     | Evidence (verbatim)
----|---------------------|----------|----------------|-------------------------------------------
1   | Procedure name       | partial  | Format viol.   | "LP done" — laterality/needle size not named
2   | Indication           | complete | —              | "Fever, neck stiffness, rule out meningitis"
3   | Consent              | partial  | Undifferentiated | "Patient agreed" — risks not documented
4   | Operators            | partial  | Omission       | "I performed" — assistant not named
5   | Technique            | partial  | Undifferentiated | "Standard technique, ultrasound guided" — needle size, attempts, position not named
6   | Findings             | partial  | Undifferentiated | "Clear CSF" — opening pressure, volume not stated
7   | Specimens sent       | partial  | Omission       | "Sent 4 tubes" — tests on each tube not named
8   | Complications        | missing  | Omission       | [not mentioned]
9   | Post-procedure plan  | partial  | Format viol.   | "Monitor" — no parameters or timeframe

>>> FALSE-POSITIVE SWEEP (QA-12)

☑ Complication section omitted:           "No complications" must be explicitly stated — not present
☐ Attempts not documented:               "22G needle, 1 attempt at L3-L4" — documented ✓
☑ Tubes without test mapping:            "4 tubes sent" — tests on each tube not specified
☐ CXR not documented:                    not applicable (LP, not central line or thoracentesis)
☐ Consent without risks mentioned:       "Reviewed risks of headache, bleeding, infection" — documented ✓

>>> SIDE-BY-SIDE CORRECTION (NE-04 — Findings — lowest score)

LEARNER VERSION                          | CORRECTED VERSION
-----------------------------------------|-----------------------------------------------------------------
"Clear CSF"                              | "CSF: clear and colorless. Opening pressure 18 cmH₂O (normal range 8–20 cmH₂O). Total volume collected: 12 mL across 4 tubes. No blood-tinged fluid. Needle withdrawn without complication."

>>> VERDICT

[co-signable | co-signable with additions | not co-signable]

Minimum required additions before co-sign:
1. Element 8 (Complications): Add "No immediate complications encountered; patient tolerated procedure without distress."
2. Element 7 (Specimens): Map each tube: Tube 1 — cell count; Tube 2 — protein/glucose; Tube 3 — culture; Tube 4 — cell count (for traumatic tap comparison).
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `procedure_performed = central-line-IJ` | Post-procedure plan must include CXR ordered with timing documented; waveform capnography confirmation statement required |
| `procedure_performed = thoracentesis` | Findings must include fluid volume removed, fluid appearance (transudate vs. exudate visual assessment), and pleural pressure monitoring if applicable |
| `procedure_performed = intubation` | ETT size, depth at lips, confirmation method (capnography + bilateral breath sounds), and post-intubation sedation order all required |
| `procedure_performed = paracentesis` | Fluid volume removed, albumin calculation for large-volume tap (albumin infusion 8g per liter removed > 5L), and spontaneous bacterial peritonitis culture sent required |
| `learner_level = intern` | Rubric adds efficiency check — redundant language and passive-voice "monitoring" flagged; note should be co-signable in < 200 words |
| `auto_generate_with_pitfalls` | Procedure data includes a complication (vasovagal during LP, arterial flash during line), multiple attempts, and specimen sent without test designation |

## Verification Checklist

- [ ] All 9 elements are scored; no element is skipped even if complete.
- [ ] Complication statement is always checked — omission of this element is never acceptable, even for uneventful procedures.
- [ ] Number of attempts must be explicitly documented — "LP performed" without attempt count is always partial.
- [ ] Specimens are checked for tube-to-test mapping — "sent to lab" without designation is always partial.
- [ ] For central line or thoracentesis: CXR documentation is checked in the plan section.
- [ ] Consent statement must reference risks discussed or refer to a signed consent form by date — "patient agreed" alone is always partial.
- [ ] Side-by-side correction uses only data from the supplied procedure data — no invented findings.
- [ ] Verdict specifies exact missing items — "improve the note" is never acceptable as a verdict.

## Worked Example (compact)

**Procedure:** LP for suspected meningitis. Data: 28F, indication fever + neck stiffness + altered MS. Consent obtained — risks of PDPH, bleeding, infection reviewed. Operator: MS4, supervised by R2. Lateral decubitus, L3-L4, 20G Quincke needle, 1 attempt. Opening pressure 22 cmH₂O (elevated). CSF: clear, colorless. 12 mL collected across 4 tubes. No complications. Patient supine post-procedure. Tubes sent: Tube 1 — cell count; Tube 2 — protein/glucose; Tube 3 — Gram stain/culture; Tube 4 — cell count.

**Learner note:** "LP performed under R2 supervision. Patient tolerated. CSF sent. Plan: monitor."

**Audit:**
- Procedure name: partial — "LP" without needle size or site
- Indication: missing — not stated
- Consent: missing — not mentioned
- Operators: partial — R2 named, MS4 not named as primary
- Technique: missing — position, needle size, attempts all absent
- Findings: partial — "CSF sent" without pressure, appearance, or volume
- Specimens: missing — tube-to-test mapping absent
- Complications: missing — "no complications" not stated
- Post-procedure plan: partial — "monitor" without parameters

**Verdict:** Not co-signable. 0/9 elements fully complete. Minimum additions: all 9 elements require revision.
