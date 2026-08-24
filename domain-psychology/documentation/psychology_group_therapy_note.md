---
title: "Group Therapy Progress Note Drafter"
category: psychology/documentation
description: "Draft a group psychotherapy progress note that documents group census, theme, individual participation per member, group process, safety, and plan, billable per-member."
techniques:
  - ST-04
  - DT-02
  - DS-04
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - group-therapy
  - cpt-90853
  - cpt-90849
  - group-process
  - per-member-note
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/documentation/psychology_birp_progress_note.md
  - domain-psychology/documentation/psychology_dap_progress_note.md
---

# Group Therapy Progress Note Drafter

## Objective

Generate group-therapy progress notes that satisfy two requirements simultaneously:

1. A **session-level group note** documenting the group itself: roster, theme/curriculum, group process, leader interventions, group response, safety events.
2. A **per-member individual note** for each participant tied to that member's treatment-plan goals, suitable for billing **CPT 90853** (group psychotherapy, non-family) or **90849** (multiple-family group). Each member's note must stand alone for audit.

## When to Use

- Outpatient or program-based group therapy (DBT skills group, CBT group, SUD process group, IOP group, MFT, psychoeducation group, support group with clinical leadership).
- Manualized curricula (DBT skills, Seeking Safety, IPT, etc.) that require module/topic documentation.
- Multi-family groups requiring 90849 billing.

## Inputs / Context

- Group metadata: date, start/stop time, duration, modality (in-person / telehealth), location, group type, curriculum/module covered today, leader(s), co-leader(s).
- Roster: members present (initials/MRN), absent, late arrivals, early departures.
- Theme / topic / module covered.
- Leader interventions delivered (named techniques, didactic content, structured exercises).
- Group process: dynamics, alliance, conflict, cohesion, subgroup formation, scapegoating, silences.
- Per-member: presentation, participation, content shared, skills practiced, response, risk indicators, ties to that member's treatment-plan goals.
- Safety events during group (disclosure of risk, intoxication, aggression, etc.).
- Outcome measures collected at group entry/exit (BPRS-G, GCQ, or program-specific).
- Treatment-plan goals each member is working.

## Constraints

### Must

- Output two parts: **(A) Group-Level Note** and **(B) Per-Member Notes** (one block per attending member).
- Group-Level Note has: Group metadata, Roster, Theme/Module, Leader Interventions, Group Process Observations, Safety Events, Plan for Next Group.
- Per-Member Note has: Member identifiers, Presentation, Participation, Skills Practiced / Content Engaged, Response, Risk Reassessment, Tie to Treatment-Plan Goal(s), CPT and time.
- Each member's note must stand alone — an auditor reading only that member's note must see what they did, what they got, and how it tied to their goals.
- Each member's note is tagged to ≥ 1 treatment-plan goal.
- Risk reassessed for each member.
- Group leaders' and co-leaders' signatures present.

### Must Not

- Do not paste identical text into every member's note. Each is individualized.
- Do not name other group members in any one member's note (confidentiality).
- Do not omit a member's note because they were quiet — document quiet/withdrawn participation as observed.
- Do not bill CPT 90853 for unstructured drop-in support without therapeutic intervention.
- Do not fabricate; flag missing inputs.

## Instructions

1. Compile group-level metadata, roster, theme.
2. Write Group-Level Note: leader interventions named, group process observations, safety events, plan.
3. For each attending member, write a per-member note pulling only that member's data.
4. Tag each member's note to that member's treatment-plan goal(s).
5. Reassess risk per member.
6. Apply correct CPT (90853 vs 90849) and document time.
7. Run verification.

## Output Format

```
=== GROUP THERAPY PROGRESS NOTE ===

PART A — GROUP-LEVEL NOTE

Group: [Name / type, e.g., "DBT Skills — Distress Tolerance Module"]
Date: [YYYY-MM-DD]    Time: [HH:MM–HH:MM]    Duration: [N min]
Modality: [In-person / Telehealth]    Location: [...]
Leader: [Name, credentials]    Co-leader: [Name, credentials]
Curriculum / Module: [...]
Theme / Topic this session: [...]

ROSTER
Present: [Initials/MRN x N]
Absent: [Initials/MRN x N — reason if known]
Late arrival: [Initials/MRN — time]
Early departure: [Initials/MRN — time, reason]

LEADER INTERVENTIONS
- [Named technique #1 — concrete description.]
- [Didactic content delivered — topic + key teaching points.]
- [Structured exercise / role-play / chain analysis demo / etc.]
- [Process intervention if applicable — naming a dynamic, redirecting, supporting cohesion.]

GROUP PROCESS OBSERVATIONS
[Dynamics, alliance, conflict, cohesion, subgroup formation, scapegoating, silences, depth of disclosures, leader's countertransference notes.]

SAFETY EVENTS
[Any risk content disclosed in group, intoxication, aggression, walkouts, ED transfer, contact with crisis line during/after group. If none: "No safety events; SI/HI/NSSI status will be addressed per-member."]

PLAN FOR NEXT GROUP
- Module / topic next session: [...]
- Outreach to absent members: [Yes / No, by whom]
- Leader supervision items: [...]


PART B — PER-MEMBER NOTES

────────────────────────────────────
Member: [Initials/MRN]    DOB: [age, gender, pronouns]
Treatment-plan goals addressed: [Goal #X label, Goal #Y label]
ICD-10 (this member): [...]
CPT: [90853 / 90849]    Time: [HH:MM–HH:MM]    Duration: [N min]

PRESENTATION
[Appearance, behavior in group, mood (quoted), affect, MSE elements as observable. Substance status if relevant.]

PARTICIPATION
[Frequency / depth of contributions; engagement with material; response to leader prompts; interaction with peers (without naming peers).]

SKILLS PRACTICED / CONTENT ENGAGED
- [Specific skill or content, tied to today's module — what this member did with it.]
- [...]

RESPONSE
[Observable response: insight statements, skill rehearsal performance, distress reduction, homework receptivity, in-group skill use during dysregulation.]

RISK REASSESSMENT
SI: [denied / endorsed — details]; HI: [...]; NSSI: [...]; substance: [...]; protective factors: [...]; risk this session: [low/moderate/high]; safety actions if any: [...].

TIE TO TREATMENT-PLAN GOAL(S)
Goal #X: [How today's group activity addresses this goal; specific evidence from this member's participation.]
Goal #Y: [...]

PLAN FOR THIS MEMBER
- Continue group: [Yes / No / step up / step down with rationale]
- Homework: [specific to this member's goal]
- Individual session follow-up: [Yes / No, with whom, by when]
- Coordination: [if applicable]

Leader: [signature, date/time]
Co-leader: [signature, date/time]

────────────────────────────────────
[Repeat per attending member.]
```

## Verification

- [ ] Group-Level Note and one Per-Member Note per attending member.
- [ ] Per-Member Notes are individualized; no copy-paste; no other members named.
- [ ] Each Per-Member Note tied to ≥ 1 treatment-plan goal.
- [ ] Risk reassessed per member.
- [ ] CPT (90853 vs 90849) chosen correctly for population.
- [ ] Time and duration consistent.
- [ ] Safety events section present (or explicit "none").
- [ ] Outreach plan for absent members specified.
- [ ] Leader and co-leader signatures present.
- [ ] Gaps flagged; nothing fabricated.
