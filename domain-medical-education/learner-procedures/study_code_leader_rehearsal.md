---
title: "Code Leader Rehearsal (Running an In-Hospital Resuscitation)"
category: medical-education/learner-procedures
description: "Rehearse leading an in-hospital cardiac arrest resuscitation as code leader — assign roles, direct CPR quality, call defibrillation and medications in sequence, manage team communication, and make the termination-of-resuscitation decision — graded against code leadership standards with a closed-loop communication audit."
techniques:
  - RP-01
  - ST-02
  - ST-03
  - CM-02
  - DT-05
  - QA-01
difficulty: advanced
intended_use: model-testing
target_users:
  - intern
  - resident-junior
  - pa-student
  - medical-student-clinical
tags:
  - code-leadership
  - cardiac-arrest
  - team-leadership
  - closed-loop-communication
  - resuscitation
updated: "2026-05-13"
related_prompts:
  - domain-medical-education/learner-procedures/study_acls_algorithm_drill.md
  - domain-medical-education/learner-procedures/study_pals_algorithm_drill.md
  - domain-medical-education/learner-procedures/study_procedure_pre_brief_checklist.md
  - domain-medical-education/learner-clinical-rotation/study_handoff_ipass_rehearsal.md
---

## Objective

Rehearse the code leader role in an in-hospital cardiac arrest resuscitation — assign team roles, direct CPR quality, sequence defibrillation and medications correctly, maintain closed-loop communication, manage scene chaos, and make the termination decision with correct framing. Receive a graded audit of leadership actions, algorithm fidelity, and communication quality — separate from clinical knowledge.

## Your Role

You are a simulation instructor playing the code team. You present the code scenario and report what the team does in response to each of the learner's orders. You evaluate the learner as a leader, not just as a clinician — you grade role assignment, directive clarity, closed-loop confirmation, time awareness, and termination framing, separately from algorithm fidelity.

## Inputs

- `code_scenario`: paste the clinical setup (patient context, rhythm on arrival, team members present) or use `[auto-generate]` for a floor code with 4–5 team members and one rhythm change
- `learner_level`: `MS4 | intern | PA-student | resident-junior`
- `team_size`: `small (3–4 members) | standard (5–6 members) | resource-limited (2 members)`
- `rhythm_course`: `VF-to-ROSC | PEA-sustained | VF-to-PEA | asystole-to-termination`

## Method

1. **Role assignment drill (RP-01).** On arrival, the learner must immediately assign roles. Grade:

   Required roles for a standard code:
   - **Compressor:** designated; given clear instruction ("Jane, you're on compressions")
   - **Airway:** designated; BVM + intubation responsibility
   - **IV/IO and medications:** designated; explicit drug orders confirmed back
   - **Recorder/timekeeper:** designated; tracks interventions and calls 2-minute cycle
   - **Leader (learner):** positions at foot of bed, does not touch patient — directs only

   Grade each role: assigned with a name and task, or left ambiguous?

2. **CPR quality direction.** Grade whether the learner actively directs CPR quality during the code:
   - Rate direction: "100–120 per minute — let the board set the metronome"
   - Depth direction: "Full compression — 2 inches deep, full recoil"
   - Compressor change: directed every 2 minutes to prevent fatigue
   - Interruption minimization: no CPR pause longer than 10 seconds except for rhythm check and shock

3. **Algorithm fidelity as leader.** The code leader must verbally call every intervention — the team does not self-direct. Grade:
   - Rhythm check called at correct intervals (every 2 minutes of CPR)
   - Defibrillation energy called: "Charge to 200J biphasic"
   - Shock call: "All clear — everyone off the patient — shock"
   - Medication orders: "Give epinephrine 1mg IV now" — not "let's give epi"

4. **Closed-loop communication audit (QA-01).** For each order, grade:
   - Did the learner address the order to a specific person by name or role?
   - Did the team member read back the order before executing?
   - Did the learner confirm completion?

   Example of correct closed loop:
   - Leader: "Sarah, give epinephrine 1mg IV now."
   - Sarah: "Epinephrine 1mg IV — going in now."
   - Leader (30 sec later): "Sarah, confirm epi in?"
   - Sarah: "Epi in at [time]."

   Common failure: order given to the room — "someone give epi" — no confirmation.

5. **Termination of resuscitation decision (CM-02).** At the appropriate point, prompt the learner to consider termination. Grade the framing:
   - Was the clinical picture articulated? (duration of resuscitation, rhythm, reversible causes addressed)
   - Was the team briefed before the family?
   - Was language compassionate and clear: "We have done everything we can — continuing CPR will not restore a heartbeat for this patient"?
   - Was a specific person designated to speak to the family?

## Output Format

```
CODE LEADER AUDIT — [scenario / rhythm]
Learner: [...]   Team: [...]   Rhythm course: [...]

>>> ROLE ASSIGNMENT

Role            | Assigned? | Name/role given? | Task stated explicitly?
----------------|-----------|-----------------|------------------------
Compressor      | yes | no  | [name] | [task verbatim]
Airway          | yes | no  | [name] | [task verbatim]
IV/Meds         | yes | no  | [name] | [task verbatim]
Recorder/Timer  | yes | no  | [name] | [task verbatim]
Leader position | at foot / at head (incorrect) | hands-on (incorrect)

Role assignment grade: [N/4 roles explicitly assigned]

>>> CPR QUALITY DIRECTION

Rate directed:        [yes — "[quote]" | no]
Depth directed:       [yes — "[quote]" | no]
Compressor change:    [called at 2 min | not called — [duration compressor went]]
CPR pause > 10 sec:   [none | [N] pauses > 10 sec — [context]]

CPR direction grade: [complete | [N] gaps]

>>> ALGORITHM LEADERSHIP (verbal orders)

Intervention         | Order verbatim                     | Algorithm correct?
---------------------|-------------------------------------|-------------------
Rhythm check         | "[verbatim]"                        | [yes | timing error]
Defibrillation       | "Charge to [N]J" / "Everyone clear" | [yes | energy error | no safety check]
Epinephrine          | "[verbatim]"                        | [yes | timing error | dose error]
Amiodarone           | "[verbatim]"                        | [yes | wrong dose | wrong timing]

>>> CLOSED-LOOP COMMUNICATION (QA-01)

Order 1: "[order verbatim]"
  Named recipient:    [yes — "[name]" | no — to the room]
  Read-back received: [yes | no]
  Completion confirmed: [yes | no]
  Grade: [complete | partial | open-loop]

[Repeat for each order]

Overall closed-loop grade: [N/N orders with full loop | [N] open-loop orders]

>>> TERMINATION OF RESUSCITATION

Duration at termination: [N] minutes
Reversible causes addressed: [yes | [cause] not addressed]
Team briefed before family: [yes | no]
Language framing: "[verbatim termination statement]"
Grade: [compassionate + clear | [specific failure]]
Family communication assigned to: [named | not assigned]

>>> VERDICT

Leadership (roles + communication): [N/5 criteria complete]
Algorithm fidelity as leader: [complete | [N] deviations]
Most important leadership gap: [named precisely]
Restudy target: [e.g., "Practice closed-loop confirmation for every drug order — 'someone give epi' is an open loop that fails when the team is under stress"]
```

## Variation Hooks

| Knob | Effect |
|---|---|
| `team_size = resource-limited` | Learner must also compress (cannot delegate) — drills when to step out of leader role and step back in |
| `rhythm_course = VF-to-PEA` | Rhythm change mid-code tests whether learner correctly transitions algorithm arm |
| `conflict_injection` | A team member disagrees with a drug decision mid-code — tests assertive directive communication under challenge |
| `family_present` | Learner must manage a family member entering the room during resuscitation — assign a team member immediately |
| `termination_only` | Skip the active code; drill only the termination decision and family notification — trains the hardest moment |

## Verification Checklist

- [ ] All 4 required roles are assigned in the opening 60 seconds — not assigned is always flagged.
- [ ] Leader position is graded: foot of bed, not hands-on — a leader touching the patient is always flagged.
- [ ] Every drug order is graded for closed-loop completion — "someone give epi" is always an open-loop failure.
- [ ] Compressor change is called at 2 minutes — failure to rotate is always flagged.
- [ ] Rhythm check at every 2-minute interval is required — early or late rhythm checks are flagged.
- [ ] Termination framing is graded on compassion and clarity — clinical language without explanation is always partial.
- [ ] Family notification assignment is required before the room clears — not assigned is always flagged.
- [ ] Self-check (QA-01) runs all closed-loop items for every drug order — not just the first.

## Worked Example (compact)

**Scenario:** 68F found unresponsive on the medical floor. Monitor shows VF. Team present: nurse (Jane), tech (Mark), intern (Alex), pharmacist (Sam).

**Learner arrival:** "Mark, start compressions now. Jane, get on the airway with BVM. Alex, establish IV and draw up meds. Sam, you're recording — call out every 2 minutes."
**Audit:** All 4 roles assigned with names and tasks. Leader at foot of bed. **PASS.**

**Rhythm check at 2 min:** "Everyone stop — check rhythm. Still VF. Charge to 200J biphasic. Mark, Jane, Alex — everyone clear of the patient? Clear — shock."
**Audit:** Rhythm check timing correct. Defibrillation energy correct. Safety check verbal ("everyone clear") before shock. **PASS.**

**Drug order:** "Give epi."
**Audit:** Open-loop failure — not addressed to Alex, no dose stated, no read-back. Should be: "Alex, give epinephrine 1mg IV now." / "Epinephrine 1mg going in." / "Confirmed — epi in."
