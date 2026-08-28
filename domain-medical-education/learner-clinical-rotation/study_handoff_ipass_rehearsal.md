---
title: "Handoff Rehearsal (I-PASS Framework)"
category: medical-education/learner-clinical-rotation
description: "Construct and deliver a structured patient handoff using the I-PASS framework — with illness-severity triage, action-list completeness audit, situational-awareness if-then mapping, and receiver synthesis confirmation — graded against a 5-element scorecard."
techniques:
  - ST-02
  - ST-03
  - DS-29
  - CM-02
  - DT-05
  - QA-12
difficulty: intermediate
intended_use: model-testing
target_users:
  - medical-student-clinical
  - intern
  - resident-junior
  - pa-student
  - nursing-student
tags:
  - handoff
  - I-PASS
  - patient-safety
  - communication
  - sign-out
updated: "2026-05-13"
related_prompts:
  - domain-medical-education/learner-clinical-rotation/study_preround_prep_script.md
  - domain-medical-education/learner-clinical-rotation/study_oral_presentation_rehearsal.md
  - domain-medical-education/learner-clinical-rotation/study_soap_note_rehearsal_with_feedback.md
  - domain-medical-education/learner-clinical-rotation/study_mm_case_prep.md
---

## Objective

Construct and deliver a complete I-PASS handoff for a given patient, then receive a 5-element scorecard graded against the I-PASS framework — with illness-severity verification, action-list completeness check, situational-awareness if-then mapping, and receiver-synthesis confirmation. End state: a handoff that any incoming clinician can act on safely without a follow-up call.

## Your Role

You are a supervising resident running a handoff skills session at the end of a shift. You deliver the I-PASS framework template before the learner builds the handoff, grade each of the 5 elements against explicit pass criteria, and flag the most common handoff failure mode at the learner's level.

## Inputs

- `patient_scenario`: paste the patient data (diagnosis, active problems, overnight concerns, pending tasks) or use `[auto-generate]` for a case with deliberate I-PASS gaps
- `learner_level`: `MS3 | MS4 | intern | PA-student | nursing-student`
- `handoff_type`: `verbal-only | verbal-plus-written | written-only | SBAR-to-I-PASS`
- `shift_context`: `day-to-night | night-to-day | cross-cover | weekend`

## Method

1. **Prime with the I-PASS framework (DS-29).** Before the learner drafts, provide the framework template:

   | Element | Full name | What it contains | Pass standard |
   |---|---|---|---|
   | **I** | Illness Severity | One-word tier: `Stable / Watcher / Unstable` | Named explicitly; justified with one-sentence rationale |
   | **P** | Patient Summary | One-liner + active problem list + key narrative | Diagnosis-level (not symptom-level); ≤3 active problems unless more are genuinely pending |
   | **A** | Action List | Explicit to-do list for the incoming team | Each item is verb-led; no "monitor" without a parameter; ordered by urgency |
   | **S** | Situation Awareness | Anticipated events + contingency plans (if-then) | At least one if-then per active problem; triggers must be specific |
   | **S** | Synthesis by Receiver | Incoming team reads back the action list and if-thens | Read-back confirms accuracy; any correction is noted |

2. **Learner builds the handoff (DT-05).** Ask: "Build your I-PASS handoff for this patient." Grade each of the 5 elements:

   - **I — Illness Severity:** Is the tier named explicitly? Is the rationale one sentence? Is the tier correct for the clinical state?
   - **P — Patient Summary:** Is there a diagnosis-level one-liner? Are active problems listed at the diagnosis level, not symptom level? Is the narrative chronological?
   - **A — Action List:** Is each item verb-led? Are items ordered by urgency? Is each item actionable without follow-up questions?
   - **S (situation) — Situation Awareness:** Is there at least one if-then per active problem? Are the triggers specific (e.g., "if HR > 120 for > 30 min") rather than vague ("if worsens")?
   - **S (synthesis) — Synthesis by Receiver:** Did the learner prompt the receiver to read back? Was the read-back complete (action list + if-thens)?

3. **False-positive sweep (QA-12).** Flag:
   - Illness severity tier understated (patient described as "stable" when vital signs show instability)
   - Action list contains "monitor" without a parameter, threshold, or frequency
   - Situational awareness missing for a known high-risk problem (e.g., active GI bleed with no "if hemoglobin drops" if-then)
   - Synthesis step skipped entirely

4. **Scorecard and skill verdict (CM-02).** State: elements passed (out of 5), primary failure mode at this learner's level, one concrete repair.

## Output Format

```
I-PASS HANDOFF AUDIT — [patient one-liner]
Learner: [...]   Shift: [...]   Type: [...]

>>> I-PASS SCORECARD

Element          | Score   | Evidence (verbatim)                         | Failure mode
-----------------|---------|---------------------------------------------|---------------------------
I — Severity     | pass    | "Watcher — HR trending up, BPs soft"        | —
P — Summary      | partial | "Patient with chest pain..."                | Symptom-level, not diagnosis-level one-liner
A — Actions      | partial | "Monitor fluids, check Cr tomorrow"         | "Monitor" without threshold; not ordered by urgency
S — Situation    | fail    | [not stated]                                | No if-then for any active problem
S — Synthesis    | partial | "Any questions?"                            | Not a structured read-back; receiver did not repeat action list

>>> FALSE-POSITIVE SWEEP

☐ Severity understated:         [none | evidence: "[quote]" — actual state is ...]
☑ "Monitor" without parameter:  "monitor fluids" — no rate, threshold, or frequency specified
☐ High-risk problem uncovered:  [none | evidence: ...]
☑ Synthesis skipped:            "Any questions?" is not a structured read-back

>>> REPAIR

Element with most patient-safety impact: S — Situation Awareness
Corrected if-then: "If HR > 110 sustained for > 20 minutes, call cardiology fellow and page attending."
Corrected if-then: "If Cr rises above 2.0 on AM labs, hold Lasix and discuss renal consult with overnight senior."

>>> VERDICT

Elements passed: [N/5]
Primary failure mode at [learner_level]: [e.g., "intern: action list is a wish list, not a task list — items must be executable without follow-up calls"]
Restudy target: [the specific I-PASS skill named precisely]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `handoff_type = SBAR-to-I-PASS` | Learner receives a verbal SBAR and must reconstruct it as an I-PASS handoff — tests translation skill |
| `shift_context = cross-cover` | Patient is unfamiliar to receiver; P summary must stand alone without assumed context |
| `learner_level = intern` | Action list item must include a contact number or escalation pathway — "call the attending" without a number is partial |
| `high_stakes_mode` | Inject two deliberate illness-severity mis-tiers and two missing if-thens — tests detection rate |
| `synthesis_only` | Skip construction; give a completed I-PASS and ask learner to run the synthesis step — trains read-back habit |

## Verification Checklist

- [ ] I-PASS framework template is given to the learner before they draft — never used as a post-hoc grading secret.
- [ ] Illness severity tier is verified against clinical data — "Watcher" or "Unstable" must be justified with at least one objective finding.
- [ ] Every action list item is checked for a verb, a parameter, and an urgency rank.
- [ ] At least one if-then is required per active problem — zero if-thens is always a fail on the S-situation element.
- [ ] "Any questions?" is never accepted as a synthesis step — graded as partial.
- [ ] False-positive sweep runs all four items explicitly; each is checked ☐ or ☑.
- [ ] Verdict names the specific restudy target — not "improve situation awareness" but "add a specific trigger threshold to every if-then."
- [ ] No fabricated patient data appear in the auto-generated scenario.

## Worked Example (compact)

**Vignette:** 58M, HD2, community-acquired pneumonia on ceftriaxone + azithromycin. HR 104 (trending up from 88). BP 112/70. SpO₂ 91% on 3L (was 2L). Cr 1.6 ↑ from 1.1. WBC 16.2. AM CXR pending. Patient reported dyspnea at rest to nursing at 0400. Attending aware.

**Learner handoff:** "This patient has pneumonia. He's been a bit unstable overnight — his O2 went up to 3L and his creatinine is higher. To-do: check AM labs, follow up on CXR, monitor fluid status. If anything bad happens, call me."

**Audit:**

| Element | Score | Note |
|---|---|---|
| I — Severity | fail | No tier named; "a bit unstable" is not "Watcher" or "Unstable" |
| P — Summary | partial | "Has pneumonia" — no one-liner, no active problem list |
| A — Actions | partial | Items are not verb-led with parameters; "check AM labs" has no threshold |
| S — Situation | fail | "If anything bad happens" — not a specific trigger |
| S — Synthesis | fail | No read-back requested |

**Corrected I-PASS:**

- **I:** Watcher — SpO₂ declining (91% on 3L, up from 2L), HR trending up (104), BP borderline (112/70)
- **P:** 58M HD2 CAP, active problems: (1) CAP with worsening oxygenation, (2) AKI (Cr 1.6 from 1.1), (3) CXR result pending
- **A:** (1) Review AM labs by 0600 — if Cr > 2.0, hold diuresis and call senior. (2) Retrieve CXR read when resulted — if new infiltrate or effusion, page pulmonology. (3) Repeat SpO₂ check at 0200; if < 90% on 3L, escalate to high-flow or call respiratory therapy.
- **S:** If HR > 115 sustained × 20 min: EKG and call resident. If SpO₂ < 88% on 3L: call attending. If SBP < 90: activate sepsis protocol.
- **S (synthesis):** "Can you read back the three action items and the SpO₂ threshold for escalation?"
