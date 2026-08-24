---
title: PACU Orientee Remediation Plan
category: pacu/preceptor-evaluation
task_type: CREATE
audience: PACU preceptor, educator, or nurse manager building a structured remediation plan for an orientee not meeting competency by target date
updated: "2026-04-16"
tags:
  - pacu
  - preceptor-evaluation
  - remediation
  - orientee
  - gap-closure
techniques:
  - ST-01
  - ST-02
  - RT-02
  - QA-02
  - ED-02
  - DS-06
difficulty: advanced
related_prompts:
  - prompts/pacu_preceptor_writing_orientee_evaluation.md
  - prompts/pacu_preceptor_difficult_conversation_guide.md
  - prompts/pacu_preceptor_approach_guide.md
  - prompts/pacu_orientee_evaluation_meta_prompt.md
  - prompts/pacu_preceptor_debrief.md
  - prompts/pacu_preceptor_calibration_facilitator.md
references:
  - ASPAN Standards of Perianesthesia Nursing Practice
  - Drain's PeriAnesthesia Nursing Practice (7th ed.)
  - ASPAN Core Curriculum for PeriAnesthesia Nursing Practice
---

# PACU Orientee Remediation Plan

> Safety reminder: A remediation plan is an educational intervention — it does **not** substitute for a patient-safety event report, medication-error report, or formal HR disciplinary process. Escalate those in parallel through facility channels.

## Objective

Produce a structured **PACU orientee remediation plan** when a specific competency is not being met by the target phase date. Output names the gap, a focused practice plan, a reassessment date, and the escalation pathway by role if the gap persists.

## When to use

- A `pacu_preceptor_writing_orientee_evaluation.md` draft reaches an **Extend** or **Remediation** disposition on one or more competencies.
- A calibration session (`pacu_preceptor_calibration_facilitator.md`) concludes the orientee is not on track for sign-off at the current phase.
- The primary preceptor has already delivered the concern verbally in a debrief **and** in a planned 1:1 (see `pacu_preceptor_difficult_conversation_guide.md`). This remediation plan is written **after** those conversations, not as a surprise.

## When not to use

- For general performance management of established staff — defer to facility HR tooling.
- To document a patient-safety event — file the facility's event report in parallel; this plan does not replace it.
- To bypass a difficult conversation — run `pacu_preceptor_difficult_conversation_guide.md` first.

## Inputs

- **Orientee identifier:** {{initials}}
- **Phase / current week:** {{...}}
- **Primary preceptor and secondary preceptors:** {{roles, not names, if sharing with orientee}}
- **Specific competency gap(s):** {{name using the scaffold from `pacu_orientee_evaluation_meta_prompt.md` — e.g., "Hemodynamic assessment & intervention — currently 'With Direction' against Week 6–10 target of 'With Cues' or better"}}
- **Evidence base:** {{reference the evidence grid from `pacu_preceptor_approach_guide.md` — shift dates, observed behaviors}}
- **Prior debrief / 1:1 delivery dates:** {{confirm the concern has already been raised — no-surprises principle}}
- **Target reassessment date:** {{calendar date + number of shifts allocated}}
- **Facility constraints:** orientation program policy on remediation, maximum extension period, HR involvement trigger.

## Audience / Scope

- **Primary user:** Preceptor or educator authoring the plan.
- **Signatories:** Orientee, primary preceptor, educator or nurse manager (per facility protocol).
- **Scope:** Phase 1 PACU orientation only. Post-orientation performance management is out of scope.

## Output requirements

```markdown
# PACU Orientee Remediation Plan — {Initials} — {Phase} — {Date}

> Safety reminder: Educational remediation plan. Does not substitute for patient-safety event reports, medication-error reports, or formal HR processes — those escalate through facility channels in parallel.

> This plan is drafted **after** verbal delivery of the concern in a prior debrief and/or planned 1:1. Nothing in this document should be new information to the orientee.

## 1. Named Gap(s)
For each competency not meeting phase target:

### {Competency name — from scaffold}
- **Current sign-off level:** {Independent / With Cues / With Direction / Not Yet}
- **Phase target:** {Independent / With Cues / With Direction / Not Yet}
- **Observable behavior gap:** {specific — e.g., "Does not verbalize a two-item differential before completing the full PACU checklist when a vital drifts outside expected range. Observed shifts: 03/18, 03/25, 04/02."}
- **Impact:** {what's at risk for the patient, team, or handoff if unaddressed}
- **Prior delivery of this concern to orientee:** debrief dates + 1:1 date.

## 2. Focused Practice Plan (per gap)
For each gap:

- **Practice behavior (specific, observable):** {what the orientee will do differently on each shift}
- **Preceptor cueing plan:** {what the primary preceptor will actively observe for and how they will cue — without taking over}
- **Simulated practice (if available):** {reference `pacu-case-scenario-writer` skill output for targeted scenarios; NOT a substitute for bedside practice}
- **Supporting review:**
  - ASPAN *Standards of Perianesthesia Nursing Practice*, {section}
  - *Drain's PeriAnesthesia Nursing*, {chapter}
  - `/corecurriculum/` {module}
  - Facility orientation program resources: {per facility protocol}

## 3. Reassessment
- **Target date:** {calendar date}
- **Number of shifts allocated:** {e.g., "4 shifts across 2 weeks"}
- **Reassessment method:** {direct preceptor observation + second preceptor's 360 via `pacu_peer_preceptor_360_feedback.md` + case-scenario sign-off}
- **Reassessment criteria (observable):** {e.g., "In 3 of 4 shifts, orientee verbalizes a two-item differential before completing the PACU checklist when any vital drifts outside expected range, without preceptor cueing."}

## 4. Escalation Pathway (by role, not name)
If reassessment criteria are not met:
- **Next:** Preceptor escalates to {educator / nurse manager — per facility protocol} for a joint review.
- **Then:** Decision is made per facility orientation program policy — further extension, role reassignment, or end of orientation.
- **At any time** if a patient-safety event occurs, file the facility's event report and notify {charge nurse / nurse manager / rapid response as applicable} per facility protocol. The remediation plan does not substitute.

## 5. Support Available to Orientee
- Access to additional simulated practice (scenarios, flashcards, quizzes) via the toolkit.
- Facility EAP contact: {{per facility protocol}} (for personal or well-being concerns — not documented here).
- Identified mentor or resource nurse (by role): {{charge / lead preceptor / educator — per facility protocol}}.
- Right to request a second preceptor for the reassessment period (per facility policy).

## 6. Non-Negotiable Expectations During Remediation
- Orientee continues to call by role (charge / CRNA / anesthesiologist on call / rapid response) for any red-flag trigger. Remediation **does not change escalation expectations**.
- All documentation must remain accurate and timely. Late charting trends are themselves a competency concern.
- Medication-administration safety steps (rights of medication administration, independent double-check per facility protocol) remain mandatory.
- Patient confidentiality is unaffected — no orientee-specific case details leave the PACU team.

## 7. Signatures and Acknowledgment
- Orientee: ______________________  Date: __________
- Primary preceptor: ______________________  Date: __________
- Educator / nurse manager: ______________________  Date: __________

> Orientee signature acknowledges receipt and understanding of the plan. It does not require agreement with every observation; the orientee may attach a written response.

## Sources / reference
- ASPAN *Standards of Perianesthesia Nursing Practice*, {relevant sections}
- *Drain's PeriAnesthesia Nursing*, {relevant chapters}
- Facility orientation program remediation policy: {{per facility protocol}}.
```

## Must / Must not

**Must:**
- Name every gap as an **observable behavior**, anchored to specific shift dates.
- Confirm the concern has been delivered verbally before this plan is written (no-surprises principle).
- Set a specific reassessment date, number of shifts, and observable criteria for meeting the target.
- Name escalation partners by role, never by name.
- State clearly that the plan does **not** substitute for patient-safety event reports, medication-error reports, or formal HR processes.
- Label as a draft the preceptor/educator edits before signatures are obtained.
- Keep escalation expectations unchanged during remediation — the orientee still calls for red-flag triggers.

**Must not:**
- Use personality labels ("slow learner," "defensive," "not a good fit," "shy"). Describe observable behavior.
- Reference age, race, sex, disability, religion, national origin, pregnancy, or other protected characteristics.
- Speculate about medical, mental-health, or family circumstances. Refer to facility EAP as a resource, do not document the reason.
- Reference license pathway (BSN/ASN/LPN-bridge) or prior unit as a cause of the gap.
- Include patient-identifying information (MRN, full name, date of birth, room number).
- Substitute this plan for a patient-safety event report or medication-error report.
- Invent facility policies, extension timelines, supply specifics, or escalation phone numbers — defer to `{{per facility protocol}}`.
- Document medication errors that have not been reported through the facility's incident-reporting system.
- Skip the reassessment method or criteria — "we'll see how it goes" is not a plan.
- Use the plan to bypass the difficult-conversation step (`pacu_preceptor_difficult_conversation_guide.md` runs first or in parallel).

## Quality signals

- Every gap names a behavior a second preceptor could observe and agree on.
- Reassessment criteria are specific enough that two preceptors would reach the same verdict.
- The plan explicitly acknowledges what it does **not** replace (safety reports, HR processes).
- The orientee has received verbal delivery of every concern before signing.
- Escalation expectations are unchanged during remediation.

## Self-check

- [ ] Every gap is an observable behavior, not a trait or personality label.
- [ ] Gaps are anchored to specific shift dates from the evidence grid.
- [ ] No-surprises principle is confirmed — prior debrief and 1:1 dates recorded.
- [ ] Reassessment date, number of shifts, and observable criteria are specific.
- [ ] Escalation pathway names roles, not people.
- [ ] Plan explicitly disclaims that it does not replace patient-safety reports or formal HR processes.
- [ ] No protected-characteristic references; no medical / family speculation.
- [ ] No patient-identifying information.
- [ ] No invented facility policies, timelines, or protocols.
- [ ] Signatures section includes orientee, primary preceptor, educator/manager.
- [ ] Safety reminder present.

## Verification

Before circulating the draft plan for signatures, verify:

- [ ] Every named gap is an **observable behavior** (verb the preceptor can witness), not a trait.
- [ ] Every gap cites at least two shift dates from the evidence grid — not a single incident.
- [ ] Prior debrief and 1:1 dates are recorded confirming the no-surprises principle.
- [ ] Reassessment criteria are specific enough that two different preceptors would reach the same verdict.
- [ ] Escalation pathway explicitly states: "if patient-safety event occurs during remediation, file the facility's event report in parallel — this plan does not substitute."
- [ ] Escalation expectations during remediation are **unchanged** from normal orientation (orientee still calls for red-flag triggers).

## False-Positive Prevention

Do **not** fabricate:

- **No invented shift dates, case details, vitals, or observations.** Every gap anchor must come from the evidence grid.
- **No invented facility orientation program policies** — maximum extension length, specific remediation plan forms, HR triggers. State "per facility orientation program."
- **No invented escalation pager numbers or phone lines.** Role only.
- **No personality labels** ("slow learner," "defensive," "not a good fit"). Translate to observable behavior.
- **No references to age, race, sex, disability, religion, national origin, pregnancy, license pathway, or prior unit as cause of the gap.**
- **No speculation about medical, mental-health, or family circumstances.** EAP by role only; do not document reason.
- **No invented pharmacy specifics or equipment specifics** in the practice plan.
- **No documentation of patient-safety events in this plan** — event reports go through the facility's separate channel.
- **No patient-identifying information** (MRN, full name, full DOB, room number).
- **No substitution of this plan for the difficult-conversation step** — that runs first (or in parallel).

## Worked Example

<details>
<summary>Example: One named gap + focused practice plan + reassessment criteria (click to expand)</summary>

```markdown
### Hemodynamic assessment & intervention
- **Current sign-off level:** With Direction
- **Phase target (Week 10):** With Cues or better
- **Observable behavior gap:** Does not verbalize a two-item differential before completing the PACU admission checklist when any vital drifts outside expected range. Observed shifts: 03/18, 03/25, 04/02, 04/09.
- **Impact:** Cue-recognition lags 2–5 minutes behind the pattern; escalation timing trails what the trend already shows.
- **Prior delivery of this concern to orientee:** Debrief on 03/18, 03/25, 04/02; planned 1:1 conversation 04/10 using `pacu_preceptor_difficult_conversation_guide.md`.

### Focused Practice Plan
- **Practice behavior:** When any vital drifts outside expected range during admission, verbalize a two-item differential before completing the rest of the checklist.
- **Preceptor cueing plan:** Primary preceptor observes silently; does not cue unless patient safety requires it; documents whether orientee verbalized before or after cue.
- **Simulated practice:** One `pacu_unfolding_case_study.md` scenario per week, focused on post-spinal and post-volume-loss hypotension.
- **Supporting review:** Drain's Ch. on Cardiovascular Assessment in PACU; ASPAN Core Curriculum hemodynamics module.

### Reassessment
- **Target date:** 2026-05-08.
- **Number of shifts allocated:** 4 shifts across 2 weeks.
- **Reassessment method:** Direct primary preceptor observation + one 360 submission via `pacu_peer_preceptor_360_feedback.md` + one simulated case sign-off.
- **Reassessment criteria:** In 3 of 4 shifts, orientee verbalizes a two-item differential before completing admission checklist when any vital drifts outside expected range, without preceptor cueing. Simulated case: same behavior demonstrated on at least one post-spinal scenario.
```

Notes: gap is observable (verb "verbalizes"), anchored to 4 specific shifts, no-surprises principle documented, reassessment criterion is specific enough for inter-rater agreement, facility-specific details deferred to policy.
</details>
