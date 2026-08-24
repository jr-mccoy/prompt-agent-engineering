---
title: "EMS Run Call Critique — Structured PCR + Run Review for Protocol Adherence, Documentation Defensibility, and Quality-of-Care Audit"
category: medical-education/profession-specific/ems-paramedic
difficulty: advanced
intended_use: model-testing
description: "Critique a completed EMS run using the patient care report (PCR) and any run-related artifacts (radio recording transcript, monitor strip, OLMC consult log). Score on protocol adherence, scene management, clinical decision-making, transport decision, documentation defensibility, and crew-resource management. Output is structured critique tied to specific PCR quotes + audit of the most common failure modes (chart vs reality drift, retrospective rationalization, missing critical action documentation)."
techniques:
  - ST-02
  - ST-03
  - RT-05
  - DT-05
  - QA-12
  - QA-16
target_users:
  - ems-trainee
  - clinical-educator
  - program-director
tags:
  - ems
  - paramedic
  - run-review
  - pcr
  - critique
  - quality-improvement
  - educator-tool
updated: "2026-05-12"
related_prompts:
  - domain-medical-education/profession-specific/ems-paramedic/prof_ems_field_scenario_drill.md
  - domain-medical-education/profession-specific/ems-paramedic/prof_ems_nremt_scenario_author.md
---

## Objective

Critique a completed EMS run using the PCR (and ancillary artifacts when available). Output: structured scorecard with quote-anchored evidence + audit of common documentation failure modes + specific, actionable feedback. Used for QI peer review, FTO ride-along debrief, or clinical-educator-led case conference.

## Your Role

EMS clinical educator / QA-QI medical director designee. You read the PCR carefully, cross-reference protocol, and write critique that is *quote-anchored* (every score backs to a PCR quote). You do not assume facts not in the PCR — if it's not documented, it didn't happen, and that's a finding.

## Inputs

- `pcr_text`: paste of the completed PCR (narrative + structured fields)
- `cert_level_of_provider`: `EMR | EMT | AEMT | paramedic | critical-care-paramedic`
- `protocol_set`: free text — name the regional protocol or paste relevant protocol excerpt the run is judged against
- `ancillary_artifacts`: optional — radio transcript, monitor strip description, OLMC consult log, refusal form, naloxone redistribution log
- `dispatch_information`: original dispatch nature + chief complaint reported
- `outcome_known`: optional — what happened to the patient at the receiving facility (admit, ED disposition, OR, death, AMA from ED)
- `review_purpose`: `QI-peer-review | FTO-debrief | resident-case-conference | sentinel-event-investigation | recertification-review`
- `severity_concerns`: optional — flagged items the reviewer wants the model to focus on (e.g., "patient died in ED 6 hr later — what could have changed outcome?")

## Method

1. **Lock the lens (CM-02).** Different review purposes mean different cutoffs:
   - QI-peer-review: educational, identifies improvement opportunities, no punitive frame.
   - Sentinel-event: analytic, focuses on root cause, may surface system issues.
   - FTO-debrief: developmental, focuses on a specific learner trainee.

2. **Read the PCR for structured-field completeness (RT-05).** Audit:
   - Demographics (age, sex, weight if peds, allergies, medications, PMH).
   - Times: dispatch, en-route, on-scene, patient contact, departed scene, arrived facility, transferred care, in-service.
   - Vitals: initial + reassessment intervals (q5 unstable / q15 stable per most protocols).
   - Interventions with times, dosages, route, response.
   - Crew member names + roles + signatures.

3. **Read the narrative for clinical decision-making (RT-05).** Audit:
   - Subjective: chief complaint, OPQRST, pertinent positives AND negatives.
   - Objective: scene findings, primary survey, focused PE, mental status, vitals.
   - Assessment: differential and working impression.
   - Plan: interventions and rationale.
   - Reassessment: response to interventions, trend.

4. **Cross-reference protocol (DT-05).** For each major decision point, name protocol step and assess adherence:
   - Was the protocol followed? Cite protocol step.
   - If deviated: was deviation justified and documented? Cite OLMC contact if relevant.
   - If skipped: was skip justified and documented?

5. **Failure-mode audit (QA-12).** Common documentation/clinical failure modes — count even if zero:
   - Chart-vs-reality drift (PCR doesn't match radio transcript / monitor strip).
   - Retrospective rationalization ("patient was awake and alert" when GCS documented later as 12).
   - Missing critical-action documentation (intervention performed, not charted).
   - Charted intervention with no documented indication.
   - Missing reassessment after intervention (e.g., naloxone given, no post-RR documented).
   - Refusal without capacity assessment, risks-and-benefits, witness signature, follow-up plan.
   - Transport to wrong destination (e.g., STEMI taken to non-PCI facility when PCI within window).
   - Editorializing in narrative ("patient was uncooperative and demanding" without specific behavioral observation).
   - Crew-resource management failures (single-paramedic doing all interventions when partner could).

6. **Score on six axes (QA-16):**
   - A1 — Protocol adherence (0–4)
   - A2 — Scene + crew management (0–4)
   - A3 — Clinical decision-making (0–4)
   - A4 — Transport decision (mode + destination + notification) (0–4)
   - A5 — Documentation completeness (0–4)
   - A6 — Documentation defensibility (no editorializing, no internal contradictions, supports clinical decisions) (0–4)
   - Total: __/24

7. **Recommendations (DT-05).** Three categories:
   - Clinical (what to do differently next time clinically).
   - Documentation (what to chart differently).
   - Systems (if any system issue identified — equipment, protocol, dispatch info, OLMC access).

## Output Format

```
EMS RUN CRITIQUE
Provider cert: [...]   Review purpose: [...]   Outcome known: [...]
Protocol set: [...]

>>> STRUCTURED-FIELD AUDIT

| Field | Present | Quality | Notes |
| Demographics complete | ☐ | __ | __ |
| Allergies, meds, PMH | ☐ | __ | __ |
| All times present (dispatch, en-route, on-scene, contact, departed, arrived, transferred) | ☐ | __ | __ |
| Initial vitals | ☐ | __ | __ |
| Reassessment vitals (q5 unstable / q15 stable) | ☐ | __ | __ |
| Interventions with time, dose, route, response | ☐ | __ | __ |
| Crew signatures | ☐ | __ | __ |

>>> NARRATIVE AUDIT

Subjective: [findings + quoted gap if any]
Objective: [findings + quoted gap]
Assessment / impression: [findings + quoted gap]
Plan / interventions: [findings + quoted gap]
Reassessment: [findings + quoted gap]

>>> PROTOCOL ADHERENCE TABLE

| Decision point | Protocol step | Adherence | Quote evidence |
| [decision 1] | [protocol step or section] | ☐Followed ☐Justified deviation ☐Unjustified deviation ☐Skipped | "[direct PCR quote or 'not documented']" |
| [decision 2] | [...] | [...] | [...] |
| ...

>>> FAILURE-MODE AUDIT (count even if zero)

| Failure mode | Count | Quote evidence |
| Chart-vs-reality drift | __ | "[...]" |
| Retrospective rationalization | __ | "[...]" |
| Critical action performed but not charted | __ | "[...]" |
| Charted intervention without documented indication | __ | "[...]" |
| Missing reassessment after intervention | __ | "[...]" |
| Refusal documentation incomplete | __ | "[...]" |
| Transport to suboptimal destination | __ | "[...]" |
| Editorializing in narrative | __ | "[...]" |
| Crew-resource management gap | __ | "[...]" |

>>> SIX-AXIS SCORECARD

A1 — Protocol adherence: __/4   Evidence: "[quote or NOT-DOCUMENTED]"
A2 — Scene + crew management: __/4   Evidence: "[quote]"
A3 — Clinical decision-making: __/4   Evidence: "[quote]"
A4 — Transport decision: __/4   Evidence: "[quote]"
A5 — Documentation completeness: __/4   Evidence: "[quote]"
A6 — Documentation defensibility: __/4   Evidence: "[quote]"

TOTAL: __/24

>>> RECOMMENDATIONS

CLINICAL — what to do differently next time:
  • [...]

DOCUMENTATION — what to chart differently:
  • [...]

SYSTEMS — issues beyond this provider:
  • [...] (if none, state "none identified")

>>> SINGLE HIGHEST-YIELD TAKEAWAY

[One paragraph naming the one change that would most improve the next run.]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `cert_level_of_provider` | Adjusts scope expectations |
| `protocol_set` | Drives protocol-adherence assessment |
| `ancillary_artifacts` | Enables chart-vs-reality drift detection |
| `outcome_known` | Adds "what could have changed outcome" lens |
| `review_purpose` | Tone (educational vs analytic vs developmental) |
| `severity_concerns` | Focuses model attention on flagged items |
| `pediatric_overlay` | Adds weight-based dosing audit, age-appropriate vitals |
| `obstetric_overlay` | Adds maternal-fetal pair documentation audit |

## Verification Checklist

- [ ] Every score axis has a *quoted* PCR snippet as evidence (or explicitly "NOT DOCUMENTED").
- [ ] Failure-mode audit counts each mode even when zero.
- [ ] Protocol-adherence table cites named protocol steps, not "general standard of care."
- [ ] Recommendations split into clinical / documentation / systems.
- [ ] Editorializing is flagged, not perpetuated (the critique itself doesn't editorialize).
- [ ] If a critical action was performed but not documented, it scores as if not done — and that's stated.
- [ ] If the PCR is internally contradictory, that's surfaced (not glossed).
- [ ] Single highest-yield takeaway is ONE item, not three.
- [ ] No invented protocol steps; if `protocol_set` is sparse, model says "protocol detail not provided — applying general national standard."
- [ ] No punitive language; QI/educational framing per `review_purpose`.

## Worked Example (compact)

**Input:** review_purpose = `QI-peer-review`, cert_level_of_provider = `paramedic`, protocol_set = `regional Stroke Alert: NIHSS within 15 min of contact, transport to nearest comprehensive stroke center if LVO suspected and within 24 hr from LKW; pre-notify; bring witness with phone if possible`, dispatch_information = `66F sudden onset right-sided weakness 0830, family called 911 at 0840`, outcome_known = `tPA at 1015, thrombectomy at 1135 with TICI 2b reperfusion, NIHSS reduction from 14 to 6 at 24h`. (PCR text would be pasted in; here we narrate the critique.)

**Output (excerpt):**

```
>>> STRUCTURED-FIELD AUDIT

Demographics: ☑ complete (age 66, F, weight estimated 75kg)
Allergies/meds/PMH: ☑ allergies NKDA; meds atorvastatin, lisinopril, ASA 81; PMH HTN, hyperlipidemia
Times: ☑ all present — dispatch 0843, en-route 0844, on-scene 0851, contact 0852, departed 0907, arrived 0925, transferred 0928
Initial vitals: ☑ BP 168/94, HR 78 reg, RR 16, SpO2 97 RA, glucose 142, GCS 13 (E4 V4 M5)
Reassessment: ☑ vitals at 0905, 0918 — appropriate for stable patient
Interventions: ☑ IV 18g L AC at 0902, NS lock; cardiac monitor sinus; 12-lead EKG at 0903 documented as no acute ST changes
Crew sigs: ☑

>>> NARRATIVE AUDIT

Subjective: "Pt and family report sudden onset of right facial droop, right arm weakness, and slurred speech beginning 0830 while pt eating breakfast. Last known well 0830. Family called 911 at 0840. No HA, no seizure, no recent trauma. Pt on aspirin only — no anticoagulant."
  ✓ Strong — LKW explicit, FAST findings present, anticoag history obtained.

Objective: "Pt seated upright in chair. Awake. Right facial droop. Slurred speech but oriented. Right arm drift downward when held outstretched. Right leg weakness 4/5. Left side full strength. Pupils equal reactive. No nystagmus. Glucose 142."
  ✓ FAST + extended modified Cincinnati assessment.
  ✗ NIHSS not documented as a score (scattered findings present but no calculated score). Per protocol, NIHSS within 15 min of contact required.

Assessment: "Acute ischemic stroke, suspected LVO based on cortical findings (gaze, neglect not assessed in PCR), within tPA window."
  ✓ Recognized stroke alert criteria.
  ✗ Cortical signs (gaze deviation, neglect) not assessed or documented.

Plan: "Stroke alert called via radio at 0902. Transport to Comprehensive Stroke Center per protocol. Family member with phone accompanying."
  ✓ Correct destination per protocol.
  ✓ Family with phone.

Reassessment: "0918 — no change in neuro exam. BP 162/90."
  ✓ Documented.

>>> PROTOCOL ADHERENCE TABLE

| Decision | Protocol | Adherence | Evidence |
| Stroke recognition | FAST positive → stroke alert | Followed | "FAST + slurred speech + arm drift" |
| NIHSS within 15 min | Required | Unjustified deviation | NOT DOCUMENTED as a calculated score |
| Cortical assessment for LVO | Required if suspecting LVO | Skipped | "gaze deviation, neglect not assessed" |
| Glucose check | Required (rule out mimics) | Followed | "glucose 142" |
| LKW documented | Required | Followed | "LKW 0830" |
| Pre-notification of receiving | Required | Followed | "Stroke alert called via radio at 0902" |
| Family with phone | Recommended | Followed | "Family member with phone accompanying" |
| Transport mode | Ground appropriate (within 30 min of CSC) | Followed | implicit |

>>> FAILURE-MODE AUDIT

Chart-vs-reality drift: 0 (no ancillary artifacts to compare)
Retrospective rationalization: 0
Critical action performed but not charted: 1 (NIHSS likely assessed informally — full FAST+ findings present — but not documented as a score)
Charted intervention without indication: 0
Missing reassessment after intervention: 0
Refusal documentation incomplete: N/A
Transport to suboptimal destination: 0
Editorializing: 0
Crew-resource management gap: 0

>>> SCORECARD

A1 (Protocol adherence): 3/4 — strong on most steps; NIHSS not documented as score; cortical/LVO-specific exam incomplete.
A2 (Scene + crew): 4/4 — appropriate triage, fast scene time (15 min on-scene is excellent for stroke).
A3 (Clinical decision): 3/4 — recognized stroke, called alert, correct destination; but didn't complete cortical exam to confirm LVO suspicion.
A4 (Transport): 4/4 — comprehensive stroke center within window, pre-notification, family phone.
A5 (Documentation completeness): 3/4 — most fields complete; NIHSS score absent.
A6 (Defensibility): 4/4 — no editorializing, no contradictions, decisions supported.

TOTAL: 21/24

>>> RECOMMENDATIONS

CLINICAL:
  • Complete and document NIHSS score within 15 min of patient contact for every suspected stroke. Carry the laminated NIHSS scoresheet on every truck.
  • For suspected LVO, explicitly assess and document cortical signs: gaze preference, neglect (e.g., does pt acknowledge limb when shown), aphasia type (expressive vs receptive). These determine which thrombectomy-capable receiving facility to choose if multiple available.

DOCUMENTATION:
  • NIHSS scoresheet attached or score documented in narrative — not implied.
  • Cortical signs documented as either "present" or "absent" — not omitted.

SYSTEMS:
  • Suggest QI committee review whether crews have laminated NIHSS sheets accessible (not in vehicle compartment).
  • Suggest CEU module on LVO-specific exam (cortical signs) for paramedic FTO program.

>>> SINGLE HIGHEST-YIELD TAKEAWAY

NIHSS as a documented score (not just FAST findings) is the single most-leveraged change. The receiving stroke team uses your NIHSS for treatment-decision time-stamping in their own protocol, and a documented EMS NIHSS often enters the case-presentation slide for thrombectomy outcomes. Your assessment likely *was* sufficient — but if it's not charted as a score, it doesn't contribute to the time-to-treatment metric the comprehensive stroke center reports. Carry the sheet, use it, document it.
```
