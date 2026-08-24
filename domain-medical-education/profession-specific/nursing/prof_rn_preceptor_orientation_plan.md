---
title: "New-Graduate Nurse Preceptor Orientation Plan — Week-by-Week Competency Build with Caseload Progression"
category: medical-education/profession-specific/nursing
difficulty: advanced
intended_use: model-testing
description: "Build a unit-specific 8–16 week new-grad preceptor orientation plan. Each week names: caseload (number of patients + acuity), unit-specific competencies to demonstrate, learning resources, scheduled didactic, milestone assessment (with go/no-go criteria), preceptor:orientee ratio, and explicit escalation criteria. Output is a week-by-week table + competency checklist + go/no-go gate definitions + a separate struggling-orientee branch."
techniques:
  - ST-02
  - ST-03
  - DT-05
  - ED-02
  - NE-02
  - QA-16
target_users:
  - clinical-educator
  - new-graduate-nurse
  - program-director
tags:
  - preceptor
  - new-graduate
  - orientation
  - residency
  - educator-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/profession-specific/nursing/prof_rn_clinical_evaluation_tool.md
  - domain-healthcare-clinical/prompts/nursing/preceptor_orientee_feedback_session.md
  - domain-medical-education/profession-specific/nursing/prof_rn_clinical_judgment_ngn_drill.md
---

## Objective

Build a structured week-by-week new-graduate orientation plan for a specific unit (med-surg / step-down / ICU / ED / OB / NICU / oncology / etc.). Plan defines caseload progression, competency milestones, didactic schedule, gate criteria, and a struggling-orientee escalation branch. Output is a unit-ready document the preceptor and educator can use as the daily working artifact.

## Your Role

Nurse educator / unit-based clinical educator. You build a *unit-specific* plan — generic "be supportive" language is rejected. You enforce caseload progression evidence (Benner novice→competent trajectory) and explicit go/no-go gates so failure isn't a surprise.

## Inputs

- `unit`: free text (e.g., "32-bed med-surg telemetry," "24-bed adult medical ICU," "level III NICU," "level I trauma ED")
- `orientation_length_weeks`: integer 8–16 (med-surg typically 8–12; ICU/ED typically 12–16; specialty/peds 16+)
- `orientee_background`: `new-graduate-nurse | experienced-RN-new-to-specialty | RN-returning-to-bedside`
- `nurse_residency_overlay`: `Vizient/AACN | UHC | program-developed | none`
- `target_full_caseload`: integer (med-surg 5–6; tele 4–5; ICU 1–2; ED varies by acuity)
- `precepted_shifts_per_week`: integer (default 3 for 12-hour shifts)
- `unit_specific_high_acuity_competencies`: free text — list of unit-defining skills (e.g., for ICU: vasoactive titration, mechanical ventilation, CRRT, ICP monitoring; for ED: triage, code response, trauma activation; for OB: external/internal fetal monitoring, second-stage management)
- `gate_structure`: `weekly-gate | biweekly-gate | midpoint-and-end | per-competency`
- `failing_pathway_required`: boolean (default true)

## Method

1. **Lock the trajectory (CM-02).** Anchor the plan in Benner stages: weeks 1–2 = novice (rule-based, observed); weeks 3–6 = advanced beginner (recognizes recurrent patterns); weeks 7+ = competent (consciously plans care for assigned caseload). Caseload doubles roughly every 2–3 weeks until target.

2. **Build week-by-week table (DT-05 + ED-02).** For each week:
   - `Caseload`: number of patients + acuity ceiling.
   - `Preceptor:orientee ratio`: 1:1 → eventually orientee-led with preceptor available.
   - `Unit-specific competencies introduced`: from input list, sequenced low → high acuity.
   - `Required observations`: count + type (e.g., "observe 2 admissions, 1 code response").
   - `Required performances under direct supervision`: count + type (e.g., "perform 3 admissions under direct supervision; titrate norepinephrine ×2 with preceptor verification").
   - `Didactic / class hours scheduled`: topic + hours.
   - `Required documentation/artifact`: shift reflection, dosage cal sheet, scenario debrief.
   - `Self-assessment + preceptor assessment`: structured short form referenced.

3. **Build competency checklist (NE-02).** Master list of unit-defining competencies with three columns: introduced (date) / performed under supervision (date) / performed independently (date). Two preceptor signatures required per competency (one for under-supervision, one for independent).

4. **Build gate criteria (QA-16).** For each gate point in `gate_structure`, name explicit go/no-go criteria. Gate language is criterion-referenced: "By end of week 4, orientee must (a) carry caseload of 3 with appropriate handoff, (b) independently perform initial assessment + documentation within 60 min of shift start, (c) verbalize SBAR for ≥ 2 escalations during the week. Missing any one triggers extended week 4."

5. **Build escalation / struggling-orientee branch.** Define:
   - Trigger criteria (missed gate; safety concern; unprofessional behavior; preceptor request).
   - Step 1: structured preceptor feedback session (cite the existing `preceptor_orientee_feedback_session.md` if relevant).
   - Step 2: educator-led re-baseline + extension plan.
   - Step 3: formal performance improvement plan (PIP) with HR involvement.
   - Step 4: termination / non-progression.
   - Document timing for each step (e.g., Step 1 within 48 hr of trigger; Step 2 within 1 week).

## Output Format

```
NEW-GRAD ORIENTATION PLAN
Unit: [...]   Length: [...] weeks   Orientee background: [...]
Residency overlay: [...]   Target caseload: [...]   Shifts/week: [...]
Gate structure: [...]

>>> WEEK-BY-WEEK TABLE

| Wk | Caseload | Ratio | Competencies introduced | Required obs | Required performance | Didactic | Artifact | Gate? |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 (medium acuity) | 1:1 shadow | unit orientation, EHR, IV pumps, MAR review | 2 admissions | 0 (observe only) | 8h: orientation, EMR, central line care | Shift reflection ×3 | — |
| 2 | 1–2 | 1:1 | core med-surg meds (anticoag, insulin, opioids), patient ed teach-back | 1 code response | 1 admission with full doc | 4h: med-error case studies | Med-pass observation form ×3 | Wk 2 gate |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| [N] | target | 1:1 available | full unit competencies | — | full caseload independent | preceptor-led debriefs | end-of-orientation portfolio | End gate |

>>> UNIT-SPECIFIC COMPETENCY CHECKLIST

| Competency | Introduced (date) | Under supervision (date + preceptor sig) | Independent (date + preceptor sig) |
| [comp 1] | | | |
| [comp 2] | | | |
| ...

(Two signatures required per competency. Independent signature requires ≥ 3 successful performances.)

>>> GATE CRITERIA

═══ Gate 1 (end of week [N])
  Go criteria (ALL required):
    • [...]
    • [...]
  No-go: missing any criterion → trigger extension protocol.

═══ Gate 2 (end of week [N])
  Go criteria: [...]

═══ End-of-orientation gate
  Go criteria: [...]
  No-go: triggers struggling-orientee branch step 2 or higher.

>>> STRUGGLING-ORIENTEE BRANCH

Trigger criteria:
  • Missed gate
  • Safety event (med error / pt harm / near-miss with insufficient self-disclosure)
  • Unprofessional behavior (incivility, dishonesty, repeated tardiness)
  • Preceptor formal request

Step 1 (within 48 hr of trigger): Structured preceptor + orientee feedback session
  • Use SBAR-style write-up of the concern
  • Orientee response and self-assessment
  • Joint re-plan for the next 1–2 weeks
  • Document and forward to educator

Step 2 (within 1 week if Step 1 insufficient): Educator-led re-baseline
  • Reassessment of competency checklist
  • Possible extension of orientation by 2–4 weeks
  • Modified preceptor assignment if needed
  • HR notification

Step 3: Formal PIP
  • HR-led document
  • Defined behavioral targets and review frequency
  • Termination or successful completion endpoint

Step 4: Non-progression / termination per HR/labor policy

>>> SCHEDULED DIDACTIC SUMMARY

| Wk | Topic | Hours | Format |
| 1 | EMR + IV pumps | 8 | hands-on |
| 2 | High-alert meds | 4 | case-based |
| 3 | Stroke protocol | 2 | sim |
| ...

>>> ARTIFACT REQUIREMENTS

End-of-orientation portfolio:
  • Completed competency checklist (all signatures)
  • ≥ 4 shift reflections per Vizient/AACN format
  • ≥ 2 simulation debriefs
  • Final preceptor evaluation (Bondy-style anchored CET)
  • Self-assessment with named growth goals for first 6 months

>>> ROLES + RESPONSIBILITIES

Preceptor: [responsibilities + protected time per shift if any]
Educator: [responsibilities + frequency of touchpoints]
Manager: [responsibilities + escalation receipt]
Orientee: [responsibilities — self-disclosure of difficulties, completion of artifacts on time]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `unit` | Drives competencies, caseload, acuity ceiling |
| `orientation_length_weeks` | Med-surg shorter, specialty longer |
| `orientee_background` | Shortens plan if experienced RN new to unit |
| `nurse_residency_overlay` | Adds residency curriculum requirements |
| `target_full_caseload` | Drives end-state |
| `unit_specific_high_acuity_competencies` | Replaces generic competencies with unit-defining ones |
| `gate_structure` | Weekly vs biweekly vs midpoint-only |
| `failing_pathway_required` | Toggles step 1–4 escalation branch |

## Verification Checklist

- [ ] Each week has *all* columns populated (no "TBD").
- [ ] Caseload progression is gradual (not 1 → full caseload in one jump).
- [ ] Preceptor:orientee ratio drops appropriately (1:1 shadow → 1:1 paired → 1:1 available).
- [ ] Unit-specific competencies are sequenced low → high acuity.
- [ ] Required observations and performances have *counts*, not "as needed."
- [ ] Gate criteria are criterion-referenced (named behaviors / counts), not "preceptor judgment."
- [ ] Struggling-orientee branch has explicit trigger criteria, named steps, and timing.
- [ ] Two-signature rule on competency checklist enforced.
- [ ] Didactic schedule names hours and format.
- [ ] No invented residency policies; named overlay (Vizient/AACN, UHC, program) cited.

## Worked Example (compact)

**Input:** unit = `28-bed adult medical ICU`, orientation_length_weeks = 14, orientee_background = `new-graduate-nurse`, nurse_residency_overlay = `Vizient/AACN`, target_full_caseload = 2 (1:2 ICU ratio), precepted_shifts_per_week = 3, unit_specific_high_acuity_competencies = `vasoactive titration, mechanical ventilation, CRRT setup/management, ICP monitoring, code-team participation, end-of-life withdrawal of life support`, gate_structure = `biweekly-gate`.

**Output (excerpt):**

```
>>> WEEK-BY-WEEK TABLE

| Wk | Caseload | Ratio | Competencies introduced | Obs | Performance | Didactic | Artifact | Gate? |
| 1 | 0 (shadow) | 1:1 shadow | unit/EHR orientation, IV pumps, central lines, A-lines, code cart | 2 codes (any role) | 0 | 8h orientation; 4h code-blue overview | Reflection ×3 | — |
| 2 | 1 (low acuity) | 1:1 | foley/NGT/wound care, basic vent setting interpretation, sedation scales (RASS, CPOT) | 1 vent setup, 2 admissions | 1 admission with preceptor co-doc | 4h: vent fundamentals | Med-pass observation ×3 | Gate 1: end of wk 2 |
| 3–4 | 1 (medium) | 1:1 | low-dose vasopressor monitoring (no titration yet), paralytic safety, ABG interpretation | 2 vent management shifts | 2 admissions independent doc, 1 vasopressor monitoring | 4h: hemodynamics | Vent management worksheet | — |
| 5–6 | 1 (high acuity) OR 2 (low) | 1:1 | vasopressor titration with preceptor verification, ICP basics, sedation titration | 1 CRRT setup observation, 1 ICP setup | 2 vasopressor titrations under direct supervision | 4h: vasoactive lecture; 2h sim | Sim debrief | Gate 2: end of wk 6 |
| 7–8 | 2 (mixed) | 1:1 | CRRT troubleshooting, ECMO awareness, code-team primary RN role | 2 CRRT runs | 1 code as primary RN, 2 admissions independent | 4h: CRRT class | Code reflection | — |
| 9–10 | 2 (full) | 1:1 paired | end-of-life care, family meeting facilitation | 1 EOL withdrawal observation | 1 EOL withdrawal under direct supervision | 4h: EOL/ethics | EOL reflection | Gate 3: end of wk 10 |
| 11–12 | 2 (full) | 1:1 available | charge-nurse shadowing, rapid-response role | — | full caseload independent ×6 shifts | 2h: leadership | Portfolio check-in | — |
| 13–14 | 2 (full) | available on unit | sign-off shifts | — | full caseload independent ×6 with preceptor on unit but not assigned | — | Final portfolio + CET | End-of-orientation gate |

>>> GATE 1 (end of week 2) — Go criteria

  • Independently performs assessment + documentation within 60 min of shift start
  • Verbalizes RASS / CPOT scoring for assigned patient correctly on rounds
  • Demonstrates correct hand hygiene + central-line dressing change technique
  • Identifies code-cart drug locations and verbalizes naloxone/epinephrine dosing
  • Submits 3 shift reflections per Vizient/AACN format
  No-go: extension by 1 week + repeat content.

>>> GATE 3 (end of week 10) — Go criteria

  • Manages 2-patient assignment with appropriate handoff
  • Independently titrates one vasoactive infusion within preceptor verification at start
  • Has performed at least one EOL withdrawal under direct supervision
  • Has participated in 2 codes as primary RN role
  • Verbalizes plan for any unstable patient using SBAR within 5 min of escalation
  No-go: extend by 2–4 weeks + targeted competency repetition; trigger educator review.
```
