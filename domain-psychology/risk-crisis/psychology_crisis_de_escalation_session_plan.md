---
title: "In-Session Crisis De-Escalation and Disposition Plan"
category: psychology/risk-crisis
description: "Build a real-time, in-session crisis plan when acute risk emerges mid-encounter: rapid risk re-stratification, agreed-upon safety actions before the client leaves, contingency tree if the client refuses, and post-session follow-through."
techniques:
  - ST-04
  - DT-02
  - NE-01
  - NE-07
  - RT-03
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - in-session-crisis
  - rapid-stratification
  - agitation-management
  - refusal-contingency
  - warm-handoff
  - post-session-followup
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
  - domain-psychology/risk-crisis/psychology_stanley_brown_safety_plan.md
  - domain-psychology/risk-crisis/psychology_civil_commitment_narrative.md
---

# In-Session Crisis De-Escalation and Disposition Plan

## Objective

Generate a real-time plan for the clinician when acute risk emerges *during* a session and a disposition decision must be reached *before the client leaves the room (or the call)*. The output must:

1. Stabilize affect first (de-escalation before assessment when agitation is high).
2. Rapidly re-stratify risk using condensed C-SSRS / homicidal-ideation criteria.
3. Reach a **disposition decision in the room**: outpatient with agreed safety actions, escalated outpatient with same-day follow-up, mobile crisis dispatch, ED with transport, voluntary admission, involuntary hold.
4. Specify **what must be true before the client leaves the encounter** (means restriction action, support contact, transport arranged, warm handoff completed).
5. Provide a **contingency tree** for client refusal of recommended disposition.
6. Specify **post-session follow-through** within hours of the encounter.

This is for in-session use, not for after-hours phone crises (separate workflow).

## When to Use

- Mid-session disclosure of imminent SI / SA preparatory acts.
- Mid-session HI with identifiable target.
- Acute agitation, dissociation, psychotic decompensation in session.
- Telehealth session where risk emerges and physical proximity is not available.
- Re-assessment when prior session's risk stratification is contradicted by current presentation.

## Inputs / Context

- Current session metadata: date, time, modality (in-person / telehealth), location.
- Trigger: what was said or observed in the last 0–30 minutes.
- Client's current state: agitation level, dissociation, intoxication, psychotic features.
- Prior risk stratification on file (if any) and how it differs from now.
- Means access (firearms, medications, vehicle, other).
- Identified support persons currently reachable (in waiting room, by phone, at home).
- Available resources: in-clinic psychiatrist / on-call MD, mobile crisis team in catchment, nearest ED, transport options (family, EMS, law enforcement, ride share rarely appropriate for active risk).
- Telehealth-specific: client's exact location, local emergency-services number, ability/willingness to dispatch crisis services to client's address.

## Constraints

### Must

- Output the following labeled sections in order: **Trigger and Initial Stabilization**, **Rapid Risk Re-Stratification**, **Disposition Decision Tree**, **What Must Be True Before Client Leaves**, **Refusal Contingency Tree**, **Communication and Warm Handoff**, **Post-Session Follow-Through**, **Documentation Plan**, **Linked Records**.
- Initial Stabilization must address agitation / dissociation first when present (grounding, slowing pace, validating, removing stimulus, offering water, breathing) before deepening risk inquiry. A flooded client cannot collaborate on disposition.
- Rapid Risk Re-Stratification uses condensed criteria: ideation severity & intensity (now), behavior (preparatory acts, attempt today), means (access right now), intent (current); plus dynamic factors (intoxication, psychosis, agitation) and protective factors (alliance, support).
- Disposition Decision Tree presents options ordered by restrictiveness, with the in-room criteria for each.
- "What Must Be True Before Client Leaves" lists concrete prerequisites (means restriction action initiated, support person contacted, transport confirmed, warm handoff completed).
- Refusal Contingency Tree maps client refusal to next step (negotiate intermediate step, contact supports, escalate to involuntary hold, contact law enforcement for telehealth dispatch).
- Telehealth-specific elements: confirm client's exact location at time of risk emergence, identify local emergency services, plan for dispatch if client disengages.
- Communication / Warm Handoff: whoever the client is going to next (ED, mobile crisis, family, identified clinician) is contacted by the current clinician, with content of the handoff specified.
- Post-Session Follow-Through has time-bounded actions within 4, 24, and 48 hours.
- Documentation plan specifies what gets written when (real-time bullet points, full note within 24 h, linked safety plan, linked Columbia, civil-commitment narrative if applicable).

### Must Not

- Do not deepen risk inquiry while the client is acutely flooded; stabilize first.
- Do not allow a client to leave with active SI / plan / means access without an agreed disposition and the prerequisite actions completed.
- Do not assume telehealth risk is manageable from a distance; document the dispatch plan and use it.
- Do not delegate the disposition decision to "we'll follow up tomorrow" if risk is acute.
- Do not skip warm handoff; transfer of care requires direct communication.
- Do not allow client refusal to terminate the safety process; document refusal and escalate per contingency tree.
- Do not fabricate; flag missing inputs.

## Instructions

1. Document the trigger and current state.
2. Stabilize: name agitation level; apply grounding / pacing / validation / environmental adjustment as needed.
3. Once collaboratively engaged, run rapid risk re-stratification.
4. Identify disposition options from least to most restrictive that match the stratification.
5. Engage the client in selecting the least-restrictive viable option; document the selection.
6. List the prerequisites that must be true before the client leaves; act on them in session (call support, initiate means restriction, arrange transport, confirm bed, complete warm handoff).
7. If client refuses, walk the contingency tree.
8. Document time-bounded post-session follow-through (4 h / 24 h / 48 h).
9. Document linked records.
10. Run verification.

## Output Format

```
=== IN-SESSION CRISIS DE-ESCALATION AND DISPOSITION PLAN ===

TRIGGER AND INITIAL STABILIZATION
Encounter: [Date / time / modality / location]
Trigger: [What was said / observed in last 0–30 min — verbatim where possible]
Current state on a 0–10 agitation/dissociation scale: [N]
Stabilization actions taken in real time:
- [Specific grounding: e.g., 5-4-3-2-1; cold water; breath pacing; standing up; moving to quieter room]
- [Pacing adjustment: slow, short sentences, validation]
- [Environmental adjustment: lower lights, remove stimulus, offer water]
- [Telehealth-specific: confirmed client's exact location, asked client to remain on line, identified anyone else in client's environment]
Result: [Agitation reduced from N to N over [time]; client able to collaborate / partially / not yet]

RAPID RISK RE-STRATIFICATION (condensed)
Ideation severity now: [Wish to be dead / Non-specific active SI / SI with method / SI with some intent / SI with specific plan + intent]
Verbatim: "[client's words]"
Intensity: frequency [now / today / past 24 h]; controllability [...]; deterrents [named]
Behavior: preparatory acts today / attempt today / aborted today / NSSI today: [Y/N specifics]
Means access right now: [Firearms / medications / other — present / removed]
Intent now: [Egodystonic / egosyntonic / unclear; client's stated reason]

For HI scenarios:
Identifiable target: [Yes / No]; plan / means / preparatory acts; egodystonic vs egosyntonic; duty-to-protect triggered Y/N — see linked Tarasoff prompt.

Dynamic factors right now: [Intoxication / psychosis / agitation / sleep deprivation / acute loss / recent ED]
Protective factors right now: [Alliance / specific reasons for living / accessible support]

Stratification (this moment): [Low / Moderate / High] with rationale.
Imminent risk (next hours): [Yes / No].

DISPOSITION DECISION TREE (least to most restrictive)
1. Outpatient with safety-plan refresh and same-day support contact: [Match? Y/N — criteria: low-moderate risk, no plan/intent/means, alliance intact, support reachable in next hours]
2. Outpatient with same-day clinician check-in (4 h) plus support involvement: [Match? Y/N — criteria: moderate risk, ambivalence intact, means restriction in motion]
3. Mobile crisis dispatch / urgent psychiatric appointment within 24 h: [Match? Y/N — criteria: moderate-high risk requiring more contact than weekly]
4. ED for evaluation: [Match? Y/N — criteria: high acute risk, intent without plan execution, need for medical clearance]
5. Voluntary inpatient admission: [Match? Y/N — criteria: high acute risk, plan + intent + means present or prior attempt this episode, voluntary acceptance]
6. Involuntary hold: [Match? Y/N — see linked civil-commitment narrative if selected]

Selected disposition: [...]
Client engagement with selection: [Agrees / agrees with reservations / disagrees]

WHAT MUST BE TRUE BEFORE CLIENT LEAVES
- [Means-restriction action initiated: e.g., "Brother John called and en route to retrieve firearms" or "Pharmacy called for 7-day fill" or "Lockbox key transferred to partner"]
- [Support person contacted: name, time, content of contact]
- [Transport arranged: family / EMS / law enforcement / mobile crisis / clinician arranged with destination and ETA]
- [Bed confirmed (if admission): receiving facility name, intake clinician, ETA]
- [Warm handoff completed: receiving party briefed]
- [Updated safety plan in client's hand / phone / portal]
- [Crisis resources reviewed and rehearsed]
- [Telehealth: client to remain on line until in-person resource arrives or risk reduced; dispatch readiness confirmed]

REFUSAL CONTINGENCY TREE
If client refuses recommended disposition:
- Step 1 — Negotiate intermediate option: [Specific offer one step less restrictive that still addresses risk; document client response]
- Step 2 — Engage support: [Bring identified support into the conversation in person or by phone; with consent or emergency exception]
- Step 3 — Reassess capacity to consent: [If lacking, initiate involuntary process per state statute — see linked civil-commitment narrative]
- Step 4 — Escalate: [Mobile crisis to current location / law enforcement welfare check / emergency dispatch for telehealth]
- Step 5 — Document: [Refusal, escalation actions, time-stamps, supervisor consultation]

COMMUNICATION AND WARM HANDOFF
- Receiving party: [Name, role, agency, contact]
- Time of warm handoff: [HH:MM]
- Content shared (with consent or emergency exception): [Risk summary, current presentation, means status, support involvement, current medications, allergies, medical issues, transport ETA]
- Receiving party's plan: [What they will do next; how clinician follows up]
- ROI status: [Signed / emergency exception cited]

POST-SESSION FOLLOW-THROUGH
Within 4 hours:
- [Confirm arrival at destination — call ED / family / mobile crisis]
- [Confirm means-restriction follow-through — text / photo / call]
- [Brief supervisor / on-call]
Within 24 hours:
- [Document full progress note (linked safety plan, Columbia, civil-commitment narrative if applicable)]
- [Coordinate with prescriber / PCP]
- [Establish next contact with client (in-person at receiving facility / phone / next session)]
- [Family check-in if consented]
Within 48 hours:
- [Re-stratify risk with current information]
- [Risk-management debrief if escalated to ED / hold / law enforcement]
- [Plan revision if treatment plan needs update]

DOCUMENTATION PLAN
- Real-time bullet points captured during stabilization and disposition.
- Full progress note completed within 24 h.
- Linked: Columbia (date), Stanley-Brown plan (date or new), lethal-means counseling (date or new), Tarasoff analysis (if applicable), civil-commitment narrative (if applicable).
- Telehealth-specific attestations preserved if applicable.

LINKED RECORDS
- Linked Columbia: [Date]
- Linked safety plan: [Date or "new today"]
- Linked Tarasoff analysis: [Date if applicable]
- Linked civil-commitment narrative: [Date if applicable]
- Linked progress note: [Date]

Clinician: __________________  Date/Time: ___________
Supervisor / on-call: ________  Date/Time: ___________
```

## Verification

- [ ] Trigger and initial-state agitation rated; stabilization actions documented before deeper inquiry.
- [ ] Rapid re-stratification covers ideation severity, intensity, behavior, means, intent, dynamic and protective factors.
- [ ] Disposition Decision Tree presents options least-to-most restrictive with match criteria.
- [ ] Selected disposition documented with client's engagement status.
- [ ] "What Must Be True Before Client Leaves" lists concrete prerequisites that were acted on in session (means action, support contact, transport, bed, warm handoff, updated plan).
- [ ] Refusal Contingency Tree maps refusal to specific escalation steps.
- [ ] Telehealth-specific elements (location, dispatch readiness, stay-on-line plan) present if applicable.
- [ ] Warm handoff completed with content shared and ROI/emergency-exception cited.
- [ ] Post-session follow-through actions time-bounded at 4 h / 24 h / 48 h.
- [ ] Documentation plan specifies real-time bullets + full note within 24 h + linked records.
- [ ] No client allowed to leave with unresolved acute risk and no agreed disposition.
- [ ] No deferral of decision to "next time" when risk is acute.
- [ ] Gaps flagged; nothing fabricated.
