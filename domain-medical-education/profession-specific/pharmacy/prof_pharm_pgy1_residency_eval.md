---
title: "PGY1 Pharmacy Residency Evaluation — ASHP Outcomes/Goals/Objectives Quarterly Rating with NI/SP/ACH/ACHR"
category: medical-education/profession-specific/pharmacy
difficulty: advanced
intended_use: model-testing
description: "Author a quarterly preceptor evaluation for a PGY1 pharmacy resident, anchored to ASHP PGY1 educational outcomes (R1 patient-centered care, R2 advancing practice, R3 leadership and management, R4 teaching/education/dissemination, E5 elective). Rate each ASHP-defined goal and objective on the ASHP four-level scale: NI (needs improvement), SP (satisfactory progress), ACH (achieved for residency), ACHR (achieved for residency, repeat needed for sustained competency). Output is a quarterly tool + customized objective set for the rotation + ResiTrak-shape narrative blocks."
techniques:
  - ST-02
  - ST-03
  - DS-01
  - DT-05
  - RT-05
  - QA-16
target_users:
  - pharmacy-resident
  - clinical-educator
  - program-director
  - assessment-faculty
tags:
  - pgy1
  - pharmacy-residency
  - ashp
  - quarterly-evaluation
  - educator-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/profession-specific/pharmacy/prof_pharm_appe_evaluation.md
  - domain-medical-education/profession-specific/pharmacy/prof_pharm_journal_club_critique_rubric.md
---

## Objective

Build a quarterly evaluation tool for a PGY1 pharmacy resident. Each ASHP educational outcome × goal × objective relevant to the rotation is listed with the four-level ASHP rating scale, behavioral evidence, and narrative summary blocks. Output is ResiTrak-shape (matches PharmAcademic field structure) so a residency program director can paste it directly into the system.

## Your Role

Pharmacy residency preceptor / RPD assessment-faculty. You write to ASHP PGY1 standards (current edition) and the standardized goal/objective taxonomy. You assume the preceptor is familiar with the abbreviation conventions (R1.1.1, R1.1.2 etc.) but you make the rating anchors explicit so consistency across preceptors is enforced.

## Inputs

- `learning_experience`: free text (e.g., "internal medicine 6-week longitudinal," "ICU 4-week block," "ambulatory clinic — anticoagulation," "transitions of care," "informatics," "leadership/administration," "research")
- `experience_length_weeks`: integer
- `quarter`: `Q1 | Q2 | Q3 | Q4` (drives expected progression — Q1 should mostly be NI/SP, Q4 should be mostly ACH)
- `objective_subset`: ASHP standardized objectives covered by this experience (free-text list using R/E numbering, e.g., "R1.1.1, R1.1.2, R1.2.1, R1.3.1, R2.1.1, R3.2.1, R4.1.1")
- `evaluation_type`: `formative-quarterly | summative-end-of-experience | summative-end-of-residency`
- `narrative_required`: boolean (default true for summative)
- `customized_objectives_present`: boolean — if program has additional customized objectives beyond ASHP standardized
- `failing_threshold_required`: boolean (default true for summative)

## Method

1. **Lock the framework (CM-02).** ASHP PGY1 outcomes:
   - **R1:** In collaboration with the healthcare team, provide safe and effective patient care…
   - **R2:** Advance the practice and improve patient care.
   - **R3:** Demonstrate leadership and professionalism.
   - **R4:** Teach, educate, and disseminate knowledge.
   - **E5:** Elective outcomes.
   Each outcome breaks into goals (R1.1, R1.2…) and each goal into objectives (R1.1.1, R1.1.2…) at the ABILITY-statement level (cognitive, affective, or psychomotor).

2. **Define rating scale (DS-01 ASHP):**
   - **NI — Needs improvement:** resident requires guidance/intervention beyond preceptor expectation for the level of training.
   - **SP — Satisfactory progress:** resident progressing as expected; competency not yet achieved but trajectory appropriate.
   - **ACH — Achieved for residency:** resident has demonstrated objective at standard expected of a residency-trained pharmacist; no further evaluation of this objective required.
   - **ACHR — Achieved for residency, repeat needed:** demonstrated once but needs repeat opportunities to sustain.
   - **Not applicable / Not observed.**
   *Quarterly progression expectation:* Q1 mostly NI/SP; Q2 mix of SP and earliest ACH/ACHR; Q3 majority ACH; Q4 all required objectives ACH.

3. **Build per-objective evaluation (DT-05).** For each objective in the subset:
   - State the ASHP objective verbatim (or abbreviated reference + paraphrase).
   - Behavioral evidence: 1–3 specific observations from the experience (with date/case identifier).
   - Rating selected.
   - Quarterly trajectory: expected vs actual at this point.

4. **Add narrative summary blocks (RT-05 + QA-16):**
   - **Strengths:** specific behaviors with examples.
   - **Areas for development:** specific behaviors + plan.
   - **Action plan for next quarter:** 2–3 measurable goals.
   - **Resident's self-assessment (separate field):** preceptor-required for summative.

5. **Failing/non-progression threshold.** Name explicitly:
   - End of Q3 with > 25% of required objectives still NI → triggers RAC (residency advisory committee) review.
   - End of residency with any required objective not ACH → does not complete residency on schedule (extension or non-completion per program policy).

## Output Format

```
PGY1 PHARMACY RESIDENCY EVALUATION
Resident: [...]   Learning experience: [...]   Length: [...] wks
Quarter: [...]   Type: [formative-quarterly | summative-end-of-experience | summative-end-of-residency]

>>> RATING SCALE

NI — Needs improvement: [...]
SP — Satisfactory progress: [...]
ACH — Achieved for residency: [...]
ACHR — Achieved for residency, repeat needed: [...]
NA / NO — Not applicable / Not observed

Quarterly progression expectation:
  Q1: mostly NI/SP
  Q2: mix of SP and earliest ACH/ACHR
  Q3: majority ACH
  Q4: all required objectives ACH

>>> OBJECTIVE-BY-OBJECTIVE EVALUATION

═══ R1.1.1 — [verbatim ASHP objective or abbreviated]
  Behavioral evidence:
    • [date] — [specific case/intervention]
    • [date] — [...]
  Rating: ☐NI  ☐SP  ☐ACH  ☐ACHR  ☐NA/NO
  Expected at this quarter: [level]
  Trajectory note: [on-track | ahead | behind]

═══ R1.1.2 — [...]
  [same structure]

[repeat for each objective in subset]

>>> NARRATIVE SUMMARY

Strengths (with specific examples):
  • [...]

Areas for development:
  • [...]

Action plan for next quarter (2–3 measurable goals):
  1. [...]
  2. [...]
  3. [...]

Preceptor's overall progression assessment: ☐On-track ☐Ahead ☐Behind

>>> RESIDENT'S SELF-ASSESSMENT (required for summative)

Resident's self-rating: [...]
Resident's areas they want to develop: [...]
Resident's plan: [...]

>>> CUSTOMIZED OBJECTIVES (if program-specific)

[list with same structure as ASHP standardized objectives]

>>> NON-PROGRESSION TRIGGERS

Triggered if any of:
  • End of Q3 with > 25% of required objectives still rated NI
  • End of residency with any required objective not rated ACH
  • Pattern of professionalism concerns documented across ≥ 2 experiences
  • Documented patient-care error with insufficient self-disclosure or repeated occurrence

>>> SIGNATURES

Resident: __________ Date: ____
Preceptor: __________ Date: ____
RPD (if NI rating present at Q3 or summative): __________ Date: ____
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `learning_experience` | Drives which objectives apply and behavioral anchor specificity |
| `experience_length_weeks` | Adjusts evidence-count expectations |
| `quarter` | Drives expected rating distribution (Q1 vs Q4) |
| `objective_subset` | Selects which ASHP-standardized objectives to evaluate |
| `evaluation_type` | Formative is informational; summative triggers narrative requirement |
| `customized_objectives_present` | Adds program-specific objective block |
| `failing_threshold_required` | Surfaces non-progression triggers |

## Verification Checklist

- [ ] Rating scale lists all 5 options (NI, SP, ACH, ACHR, NA/NO) with one-line definitions.
- [ ] Quarterly progression expectation is named per quarter (not generic).
- [ ] Each objective has behavioral evidence with date/case identifier — not "good job overall."
- [ ] Each objective has expected-vs-actual trajectory note.
- [ ] Action plan items are measurable (2–3 goals named with what + when).
- [ ] Resident self-assessment field is separate and required for summative.
- [ ] Non-progression triggers are criterion-referenced (named percentages / counts).
- [ ] No invented ASHP objectives; uses standardized R/E numbering.
- [ ] No "exceeds expectations" / "meets expectations" generic scale; ASHP four-level scale used.
- [ ] Customized objectives clearly distinguished from ASHP-standardized.

## Worked Example (compact)

**Input:** learning_experience = `internal medicine 6-week block`, experience_length_weeks = 6, quarter = `Q2`, objective_subset = `R1.1.1, R1.1.2, R1.2.1, R1.3.1, R2.1.1, R3.2.1, R4.1.1`, evaluation_type = `summative-end-of-experience`, narrative_required = true, customized_objectives_present = false, failing_threshold_required = true.

**Output (excerpt):**

```
═══ R1.1.1 — Interact effectively with healthcare teams to manage patients' medication therapy.

Behavioral evidence:
  • 10/15 — On AM rounds, identified incorrect renal-adjusted vancomycin trough goal and proposed AUC-targeted re-dosing using institutional protocol; team accepted recommendation.
  • 10/22 — Communicated with hospitalist re: anticoagulation transition for patient with new AF + recent GIB; clearly articulated bleeding-vs-stroke balance and proposed apixaban with reduced dose criteria.
  • 11/05 — On three separate days, proactively flagged drug-drug interactions to nursing prior to administration (warfarin + Bactrim, fluconazole + amiodarone, sevelamer-cipro spacing).

Rating: SP (trending toward ACH)
Expected at Q2: SP
Trajectory note: on-track

═══ R1.1.2 — Interact effectively with patients, family members, and caregivers.

Behavioral evidence:
  • 10/18 — Conducted bedside warfarin teaching for newly diagnosed PE patient; used teach-back; resident self-identified that explanation of dietary K consistency was unclear and re-explained successfully.
  • 11/02 — Difficult conversation with family regarding goals of care and statin discontinuation in hospice candidate; resident appropriately referred to attending and observed.

Rating: SP
Expected at Q2: SP
Trajectory note: on-track

═══ R1.2.1 — Collect information necessary to create an evidence-based assessment of patients.

Behavioral evidence:
  • Consistent independent medication reconciliation across 30+ patients during the experience; only 2 minor documentation gaps noted by preceptor (one missed eye drop; one missed prn opioid).

Rating: ACH
Expected at Q2: SP
Trajectory note: ahead

═══ R3.2.1 — Demonstrate management skills.
  Behavioral evidence:
    • Delegated medication-history-gathering to APPE student with appropriate framing and oversight.
    • Triage of pharmacy interventions across morning rounds (decided which patients to see first based on acuity).
  Rating: SP
  Expected at Q2: NI/SP
  Trajectory note: on-track

>>> NARRATIVE SUMMARY

Strengths:
  • Consistent, accurate medication reconciliation with strong attention to renal- and hepatic-adjusted dosing.
  • Comfortable proposing recommendations on rounds with clear rationale; team trusts input.
  • Strong collaboration with the consult ID pharmacist on antimicrobial de-escalation.

Areas for development:
  • Patient-counseling depth — recommendations land but counseling can feel rushed when census is high.
  • Documentation efficiency — SOAP notes thorough but ~25% over expected length; trim narrative for plan-focused brevity.
  • Difficult conversations (goals-of-care, hospice) — observed only; needs leveled-up participation.

Action plan for next quarter (3 measurable goals):
  1. Lead 2 goals-of-care conversations with attending support by end of Q3.
  2. Reduce average SOAP note length by 25% while maintaining clinical content.
  3. Independently complete one CQI mini-project on transitions-of-care medication reconciliation by end of Q3.

Preceptor's overall progression assessment: ☐On-track ☑On-track  ☐Ahead  ☐Behind
```
