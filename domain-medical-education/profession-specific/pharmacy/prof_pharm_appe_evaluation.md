---
title: "APPE Rotation Evaluation Tool — PPCP Anchored to ACPE/EPA Outcomes for PharmD Final Year"
category: medical-education/profession-specific/pharmacy
difficulty: advanced
intended_use: model-testing
description: "Author a preceptor evaluation tool for an Advanced Pharmacy Practice Experience (APPE) rotation. Anchored in the Pharmacist's Patient Care Process (PPCP: collect / assess / plan / implement / follow-up monitor & evaluate) crossed with ACPE Standards 2016 educational outcomes (foundational knowledge, essentials for practice and care, approach to practice and care, personal and professional development) and AACP/PharmD-EPA expectations. Output is a one-page tool + rotation-specific competency matrix + entrustment ratings."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - DT-05
  - CM-02
  - QA-16
target_users:
  - pharmacy-student
  - clinical-educator
  - program-director
  - assessment-faculty
tags:
  - appe
  - pharmd
  - ppcp
  - acpe
  - rotation-evaluation
  - educator-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/profession-specific/pharmacy/prof_pharm_pgy1_residency_eval.md
  - domain-medical-education/profession-specific/pharmacy/prof_pharm_journal_club_critique_rubric.md
  - domain-medical-education/profession-specific/pa/prof_pa_clinical_year_evaluation_tool.md
---

## Objective

Build a preceptor-facing evaluation tool for an APPE rotation (typically 5–6 weeks). Score the student against PPCP × ACPE outcomes with rotation-specific behavioral anchors at each entrustment level. Output is a one-page tool + completion sign-off + remediation triggers.

## Your Role

PharmD assessment-faculty / experiential-education coordinator. You write to ACPE Standards 2016 and the PharmD-EPA framework (Core EPAs for new pharmacy graduates: collect drug-related information, evaluate drug-related needs, design and adjust regimens, manage transitions of care, education, immunization administration, identify drug-related problems, manage adherence, document care, supervise pharmacy operations and personnel, fulfill workflow). Preceptors are practicing pharmacists who may be community, hospital, or specialty — clarity prioritized over jargon.

## Inputs

- `rotation_type`: free text (e.g., "ambulatory care — primary care clinic," "hospital internal medicine," "ICU," "infectious disease," "oncology infusion," "community pharmacy," "managed care," "specialty: anticoagulation clinic," "informatics," "academia/teaching")
- `rotation_length_weeks`: integer (typically 5–6)
- `is_required_or_elective`: `required-core | elective`
- `appe_year_position`: integer 1–8 (which APPE in the sequence — 1st has lower expectations than 6th)
- `entrustment_scale`: `5-level-Chen | 4-level | program-defined` (default 5-level Chen for pharmacy: Observe / Co-activity / Direct Supervision / Indirect Supervision / Practice Independently)
- `epa_set`: subset of the 15 PharmD Core EPAs the rotation actively assesses
- `setting_constraints`: `inpatient | outpatient | community | virtual | hybrid`
- `failing_threshold_required`: boolean (default true)

## Method

1. **Lock the framework (CM-02).** Anchor on PPCP as the workflow and ACPE/EPA as the outcomes. Build a matrix: PPCP step (rows) × competency domain (columns).

2. **Define entrustment scale (DS-01 Chen-style for pharmacy):**
   - **O — Observe only:** student observes; preceptor performs.
   - **CON — Co-activity:** student performs concurrently with preceptor (e.g., joint medication reconciliation).
   - **DS — Direct supervision:** student performs; preceptor in the room.
   - **IS — Indirect supervision:** student performs; preceptor available, reviews after.
   - **PI — Practice independently (rotation-context):** student performs; preceptor reviews documentation only.

3. **Build PPCP-anchored matrix (DT-05).** For each PPCP step, write rotation-specific behavioral anchors at each entrustment level:
   - **Collect:** medication reconciliation, history-taking from patient and EHR, lab/vital integration.
   - **Assess:** drug-related problem (DRP) identification using a named taxonomy (PCNE, DOTx.MED, Cipolle/Strand).
   - **Plan:** SOAP plan with rationale and monitoring parameters.
   - **Implement:** order/recommend/educate; include pharmacist-led interventions appropriate to the setting (anticoag adjustment per protocol, vancomycin dosing, immunization).
   - **Follow-up monitor & evaluate:** efficacy + safety endpoints, with named timeframes.

4. **EPA logbook overlay.** For each EPA the rotation assesses, count documented entrustment ratings (e.g., "EPA: collect drug-related information — minimum 5 documented patient encounters at IS level by end of rotation").

5. **Add narrative blocks (QA-16):**
   - Strengths (specific behaviors).
   - Areas for growth (specific behaviors).
   - Plan for improvement (only required if any rating is O at end OR DS in a core PPCP step).
   - Single highest-yield growth target for next rotation.

6. **Failing/remediation threshold.** Name explicitly:
   - End-of-rotation O rating in any PPCP step → fail.
   - Failure to meet minimum EPA documentation → incomplete with make-up plan.
   - Documented professionalism concern → committee review.

## Output Format

```
APPE ROTATION EVALUATION
Rotation: [...]   Length: [...] wks   APPE position: [...] of 8   Type: [required | elective]
Setting: [...]   PPCP × EPA framework

>>> ENTRUSTMENT SCALE

O — Observe only: [...]
CON — Co-activity: [...]
DS — Direct supervision: [...]
IS — Indirect supervision: [...]
PI — Practice independently (rotation-context only): [...]

>>> PPCP-ANCHORED COMPETENCY MATRIX

═══ COLLECT (gathers drug-related information)
  Rotation-specific anchors:
    O: [...]
    CON: [...]
    DS: [...]
    IS: [...]
    PI: [...]
  Mid-rotation expected: [level]    End-of-rotation expected: [level]
  Rating: ☐O ☐CON ☐DS ☐IS ☐PI
  Specific evidence: __________

═══ ASSESS (identifies and prioritizes DRPs)
  [same structure]

═══ PLAN (develops evidence-based care plan)
  [same structure]

═══ IMPLEMENT (executes plan; recommends, orders within scope, educates)
  [same structure]

═══ FOLLOW-UP / MONITOR & EVALUATE (measures effect and adjusts)
  [same structure]

═══ INTERPROFESSIONAL COMMUNICATION (verbal + documented)
  [rotation-specific anchors]

═══ PROFESSIONALISM
  [rotation-specific anchors]

>>> EPA LOGBOOK SUMMARY

| EPA (subset assessed this rotation) | Min documented | Encounters logged | Highest entrustment achieved |
| [EPA 1] | __ | __ | __ |
| [EPA 2] | __ | __ | __ |
| ...

Logbook complete: ☐ Yes ☐ No → Make-up plan: __________

>>> EVALUATOR COMMENTARY

Strengths (specific behaviors observed, with date):
  • [...]

Areas for growth (specific behaviors to develop):
  • [...]

Plan for improvement (REQUIRED if any rating is O at end OR DS in core PPCP step):
  Concern: [...]
  Targeted behaviors next rotation: [...]
  Resources: [...]

Single highest-yield growth target for next rotation:
  [...]

>>> FAILING / REMEDIATION TRIGGERS

Triggered if any of:
  • End-of-rotation "O" rating in any PPCP step
  • Failure to log minimum EPA encounters
  • Documented professionalism concern
  • Safety event with insufficient self-disclosure

>>> SIGNATURES

Student: __________ Date: ____
Preceptor: __________ Date: ____
Experiential coordinator (if remediation triggered): __________ Date: ____
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `rotation_type` | Drives behavioral anchors (anticoag clinic emphasizes plan + monitor; ICU emphasizes collect + assess complexity; community emphasizes implement + adherence) |
| `rotation_length_weeks` | Adjusts expected end-rotation entrustment level |
| `appe_year_position` | Earlier APPEs have lower expected entrustment |
| `entrustment_scale` | 5-level Chen vs 4-level vs program-defined |
| `epa_set` | Selects which EPAs to log on this rotation |
| `setting_constraints` | Adjusts which interventions are within rotation scope |
| `failing_threshold_required` | Toggles the explicit failing threshold block |

## Verification Checklist

- [ ] Entrustment scale has 5 named levels with one-line definitions.
- [ ] Every PPCP step has a rotation-specific anchor at *each* entrustment level.
- [ ] Anchors are *behavioral and observable*, not affective.
- [ ] Mid-rotation expected level differs from end-of-rotation expected level.
- [ ] EPA logbook lists EPAs with required minimum documentation.
- [ ] Plan-for-improvement is conditionally required, not always.
- [ ] Failing triggers are criterion-referenced.
- [ ] DRP taxonomy is named (PCNE / DOTx.MED / Cipolle/Strand) — not "drug-related problems" generically.
- [ ] No invented program policies; ACPE/EPA framework cited.

## Worked Example (compact)

**Input:** rotation_type = `hospital internal medicine`, rotation_length_weeks = 5, is_required_or_elective = `required-core`, appe_year_position = 4, entrustment_scale = `5-level-Chen`, epa_set = `[collect drug-related info, evaluate drug-related needs, design/adjust regimens, identify and prioritize DRPs, document care]`, setting_constraints = `inpatient`, failing_threshold_required = true.

**Output (excerpt):**

```
═══ COLLECT

Rotation-specific anchors (inpatient internal medicine):
  O: Observes preceptor's medication reconciliation; takes notes.
  CON: Reviews EHR med list with preceptor; jointly clarifies discrepancies with patient.
  DS: Independently performs medication reconciliation on assigned patient; preceptor verifies before next step.
  IS: Performs med rec across assigned panel (3–5 patients); presents discrepancies and resolution plan to preceptor.
  PI: Manages med rec for full assigned team; flags only complex/ambiguous cases for preceptor.

Mid-rotation expected: DS    End-of-rotation expected: IS
Rating: ☐O ☐CON ☐DS ☐IS ☐PI

═══ ASSESS

Rotation-specific anchors (DRP identification using PCNE taxonomy):
  O: Verbalizes existence of a DRP after preceptor names it.
  CON: Identifies 1 DRP with preceptor prompting; classifies per PCNE with preceptor verification.
  DS: Independently identifies 2–3 DRPs per patient; classifies per PCNE; prioritizes with preceptor input.
  IS: Independently identifies and prioritizes DRPs across panel; recommends interventions; preceptor reviews documentation.
  PI: Routinely identifies subtle DRPs (e.g., overlap of QT-prolonging agents, renal-adjusted dose missed in transitions); preceptor signs off without revision.

Mid-rotation expected: DS    End-of-rotation expected: IS

═══ PLAN

Rotation-specific anchors (vancomycin dosing per institutional AUC-based protocol; aminoglycoside extended-interval; warfarin-to-DOAC transition):
  O: Listens to preceptor's recommendation rationale.
  CON: Drafts plan with preceptor's stepwise guidance.
  DS: Independently designs vanco initial regimen using AUC-based protocol; preceptor verifies before order.
  IS: Independently designs vanco + aminoglycoside + warfarin reversal plans; documents rationale; preceptor reviews.
  PI: Routinely designs and documents complex regimen plans across multiple disease states; preceptor concurs without revision.

Mid-rotation expected: DS    End-of-rotation expected: IS

═══ IMPLEMENT
[etc.]

>>> EPA LOGBOOK SUMMARY

| EPA | Min | Logged | Highest entrustment |
| Collect drug-related information | 10 patients | __ | __ |
| Evaluate drug-related needs | 10 patients | __ | __ |
| Design and adjust regimens | 5 complex regimens | __ | __ |
| Identify and prioritize DRPs | 15 DRPs documented | __ | __ |
| Document care (SOAP) | 8 notes | __ | __ |

>>> FAILING TRIGGERS

  • End-of-rotation "O" in any PPCP step
  • EPA logbook < 80% of required minimum at end of rotation
  • Documented professionalism concern
  • ≥ 1 documented patient-care error caught by preceptor with insufficient self-disclosure
  • Failed final case presentation (separate rubric)
```
