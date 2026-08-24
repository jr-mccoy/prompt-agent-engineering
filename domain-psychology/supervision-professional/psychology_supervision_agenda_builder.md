---
title: "Supervision Agenda Builder"
category: psychology/supervision-professional
description: "Build a structured, time-boxed clinical-supervision agenda from a supervisee's caseload that prioritizes high-risk and high-acuity cases, mandated topics, and developmental goals."
techniques:
  - ST-04
  - DT-01
  - RT-02
  - QA-04
  - CM-02
difficulty: intermediate
intended_use: model-testing
tags:
  - clinical-supervision
  - supervision-agenda
  - caseload-review
  - high-acuity
  - developmental-goals
  - discrimination-model
updated: "2026-06-08"
related_prompts:
  - domain-psychology/supervision-professional/psychology_therapeutic_technique_explainer.md
  - domain-psychology/supervision-professional/psychology_parallel_process_detector.md
  - domain-psychology/supervision-professional/psychology_countertransference_reflection_prompt.md
  - domain-psychology/risk-crisis/psychology_tarasoff_duty_to_warn_analysis.md
---

# Supervision Agenda Builder

## Objective

Produce a structured, time-boxed agenda for an individual or group clinical-supervision session, generated from the supervisee's current caseload and developmental plan. The agenda must:

1. Triage the caseload so that high-risk and high-acuity cases are reviewed first and never crowded out by routine business.
2. Cover mandated and standing topics (risk review, mandated-report tracking, missed appointments, documentation backlog, licensure/training requirements).
3. Advance the supervisee's developmental goals, mapped to the discrimination model's three foci (intervention, conceptualization, personalization) and the appropriate IDM (Integrated Developmental Model) stage.
4. Time-box each segment so the session is realistic and closes with a documented supervision record and supervisor co-sign.

## When to Use

- Preparing for a weekly or biweekly individual supervision session with a pre-licensed or trainee supervisee.
- Running group supervision where multiple supervisees' cases compete for limited time.
- A new supervisory relationship where the agenda structure itself models expectations.
- When a supervisee's caseload has grown and high-acuity cases are being missed in unstructured "what's on your mind" supervision.

## Inputs / Context Required

- **Supervisee identity and stage**: discipline, license/trainee status, IDM stage (Level 1 / 2 / 3 / 3i) `[supervisee input required: current developmental stage self-rating]`.
- **Caseload snapshot**: de-identified list of active cases with acuity flags (active SI/HI, recent hospitalization, safety plan in place, mandated report pending, high no-show, treatment-plan overdue).
- **Standing/mandated topics**: pending mandated reports, duty-to-protect situations, documentation overdue, supervision-hour tracking, upcoming evaluations.
- **Developmental goals**: the supervisee's current learning objectives from the supervision contract.
- **Session length**: total minutes available (e.g., 60).
- **Session type**: individual vs. group; in-person vs. telesupervision.
- `[supervisee input required: cases the supervisee specifically wants to bring]`
- `[clinician input required: any supervisor-initiated agenda items, e.g., observed documentation gap]`

## Constraints

### Must

- Triage the caseload into acuity tiers: **Tier 1 (urgent/safety)**, **Tier 2 (elevated/active concern)**, **Tier 3 (routine/maintenance)**; review Tier 1 first.
- Reserve a fixed block for a **standing risk and mandated-topic review** that runs every session regardless of supervisee requests.
- Map at least one agenda item to a stated developmental goal and label the discrimination-model focus (intervention / conceptualization / personalization) and the supervisory role (teacher / counselor / consultant).
- Time-box every segment; the sum of segments must not exceed session length, and include a 5-minute close for documentation and next-step assignment.
- Require de-identified case references (initials/MRN, no full names) within the agenda itself.
- End with a supervision-record line and a supervisor co-sign field.

### Must Not

- Do not place routine cases ahead of any Tier 1 safety case.
- Do not omit the standing risk/mandated-topic block even when the supervisee brings no urgent items.
- Do not over-pack the agenda such that segment minutes exceed available time.
- Do not include client-identifying detail beyond de-identified references.
- Do not fabricate caseload items; flag missing inputs with `[supervisee input required: ...]`.

## Instructions

1. Intake the caseload snapshot and assign each case an acuity tier using the flags provided.
2. Build the standing block first: risk review, mandated-report status, documentation/no-show tracking, hour/eval tracking. Assign it a fixed time-box (typically 10–15 min).
3. Sequence Tier 1 cases next, then Tier 2, then Tier 3 as time allows; assign minutes per case proportional to acuity.
4. For each developmental goal due for attention, attach it to a specific case discussion and label the discrimination-model focus and supervisory role.
5. Add any supervisor-initiated items.
6. Sum the time-boxes; if over budget, defer the lowest-acuity Tier 3 items to a parking lot and note them.
7. Add a 5-minute close: action items, who does what by when, and the supervision-record line.
8. Run verification.

## Output Format

```
=== SUPERVISION SESSION AGENDA ===

SESSION CONTEXT
Supervisee: [Initials, discipline, license/trainee status]   IDM stage: [1 / 2 / 3 / 3i]
Supervisor: [Name, credentials, license #]
Date: [YYYY-MM-DD]   Format: [Individual / Group | In-person / Telesupervision]
Total time: [N min]

────────────────────────────────────────────────────────
CASELOAD TRIAGE
| Case (de-id) | Acuity flags | Tier (1/2/3) |
|--------------|--------------|--------------|
| [Initials/MRN] | [Active SI / safety plan / mandated report / overdue plan / no-show] | [1/2/3] |
| ...          | ...          | ...          |

────────────────────────────────────────────────────────
AGENDA (time-boxed, sequenced)

[00:00–00:__]  STANDING BLOCK — Risk & Mandated Topics ([N] min)
   - Risk review across caseload (any new/changed SI/HI, safety plans)
   - Mandated-report status: [pending / filed / none]
   - Documentation & no-show tracking
   - Supervision hours / evaluation timeline

[__:__–__:__]  TIER 1 — [Case (de-id)] ([N] min)
   Focus: [Discrimination-model focus] | Supervisory role: [Teacher/Counselor/Consultant]
   Goal link: [Developmental goal advanced, if any]
   Key questions: [...]

[__:__–__:__]  TIER 2 — [Case (de-id)] ([N] min)
   ...

[__:__–__:__]  TIER 3 — [Case (de-id)] ([N] min)
   ...

[__:__–__:__]  DEVELOPMENTAL GOAL SEGMENT ([N] min)
   Goal: [Stated goal]   Focus: [intervention/conceptualization/personalization]
   Method: [Live review / role-play / case formulation / process]

[__:__–__:__]  CLOSE & DOCUMENTATION (5 min)
   Action items: [Who / what / by when]
   Parking lot (deferred): [Items]

────────────────────────────────────────────────────────
SUPERVISION RECORD
Topics covered: [...]   Risk items addressed: [...]
Supervisee action items: [...]   Supervisor follow-up: [...]
Supervisee: ____________________  Date: ________
Supervisor co-sign: ____________  Date: ________
```

## Verification

- [ ] Every case assigned an acuity tier; Tier 1 sequenced before Tier 2/3.
- [ ] Standing risk/mandated-topic block present with a fixed time-box.
- [ ] At least one agenda item mapped to a developmental goal with discrimination-model focus and supervisory role labeled.
- [ ] Every segment time-boxed; sum does not exceed total session time.
- [ ] 5-minute close includes action items and a supervision-record line.
- [ ] Case references de-identified (no full names).
- [ ] Supervisor co-sign field present.
- [ ] No routine case sequenced ahead of a Tier 1 safety case.
- [ ] Missing inputs flagged with `[supervisee input required]` / `[clinician input required]`; nothing fabricated.
