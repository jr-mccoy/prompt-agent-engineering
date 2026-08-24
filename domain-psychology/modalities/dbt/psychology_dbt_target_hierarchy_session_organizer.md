---
title: "DBT Target Hierarchy Session Organizer"
category: psychology/modalities/dbt
description: "Apply Linehan's stage-1 target hierarchy (life-threatening → therapy-interfering → quality-of-life → skills) to organize a single 50-minute DBT individual session with time blocks, agenda priority, and consultation-team flags."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - DBT
  - target-hierarchy
  - session-agenda
  - Linehan
  - stage-1
  - therapy-interfering-behavior
intended_use: model-testing
updated: "2026-05-19"
related_prompts:
  - domain-psychology/modalities/dbt/psychology_dbt_diary_card_analyzer.md
  - domain-psychology/modalities/dbt/psychology_dbt_chain_analysis.md
  - domain-psychology/modalities/dbt/psychology_dbt_emotion_regulation_module_lesson.md
---

# DBT Target Hierarchy Session Organizer

## Objective

Organize a 50-minute DBT individual session using Linehan's stage-1 target hierarchy: (1) life-threatening behaviors, (2) therapy-interfering behaviors (TIB), (3) quality-of-life-interfering behaviors, (4) skill deficits. The output is a time-blocked agenda with explicit prioritization rationale, planned interventions per item (chain analysis, skill coaching, behavioral analysis), and consultation-team flags.

## When to Use

- Standard adherent DBT, stage 1 (severe behavioral dyscontrol).
- Following a diary-card review.
- When the session has multiple competing demands and the agenda is contested.
- When supervision or consultation-team review of a clinician's adherence is at stake.
- Telehealth sessions with the same structure.
- Not for DBT-informed therapy without target hierarchy or for stages 2–4 where target structure shifts.

## Inputs / Context

- Completed diary-card review for the past week (output of the diary-card analyzer).
- Client's stage of DBT and current treatment contract.
- Prior session's agenda and homework follow-through.
- Active life-threatening risk status (Columbia/SafeT, prior chains).
- Active TIB pattern (missed sessions, dropped group, fees, lateness).
- Client's QOL targets in the current contract (work, relationships, housing, school, eating, sleep).
- Skill modules currently being taught in group.
- Session length and modality.

## Constraints

### Must

- Order the agenda strictly: **Level 1 → Level 2 → Level 3 → Level 4**. A Level-1 item present at any intensity preempts.
- For Level-1 items (suicide/NSSI/serious AOD/imminent harm): schedule a **chain analysis** and a **solution analysis**, plus a risk re-screen.
- For Level-2 items (TIB): name explicitly and apportion meaningful time. If client wants to skip the TIB discussion, that is itself TIB and is itself agenda-worthy.
- For Level-3 items: prioritize by client preference among QOL items, but cap time to leave room for Level 4.
- For Level-4 items: skills generalization, coaching, in-session rehearsal.
- Allocate time **in minutes**, not vague segments.
- Leave a 3–5 minute buffer for diary-card capture and homework setting at the end.
- Identify any **consultation-team items** that this session generates.
- When two Level-1 items compete (e.g., suicide ideation + active substance use), order by acuity / lethality and document the rationale.
- Use the **dialectical stance**: validate the client's preferred agenda even while applying hierarchy.

### Must Not

- Do not let client preference override Level-1 items.
- Do not skip TIB to keep the alliance; that is itself iatrogenic.
- Do not let Level-3 items consume all session time when Level-1 or Level-2 items are present.
- Do not assign chain analyses without time to do them.
- Do not skip the homework / skills hand-off at the end.
- Do not let new in-session content (e.g., a fresh disclosure of NSSI) be ignored; if it crosses Level-1 threshold, re-rank.
- Do not fabricate agenda items not supported by the diary card or in-session disclosures.

## Instructions

1. Open the session: 2-minute orientation, "What's on the diary card we should address first?"
2. Apply target hierarchy from the diary-card analyzer output.
3. Set the agenda visibly with the client (whiteboard / shared screen / paper).
4. Assign time blocks per item; sum to session length minus buffer.
5. Begin with Level-1 work; conduct chain analysis if behavior occurred or was very close to occurring.
6. Address TIB; do not collapse into Level-3.
7. Move to Level-3 by client priority among QOL options.
8. Close with Level-4 skills practice, homework, diary-card hand-off.
9. Identify consultation-team items.
10. Schedule next session.

## Output Format

```
=== DBT SESSION AGENDA (Target Hierarchy Organizer) ===
Client: [Initials/MRN]    Session #: [N]    Date: [YYYY-MM-DD]    Length: [50 min]    Modality: [...]
Stage: [1]    Contract targets active: [...]
Source diary card / review: [Date]

LEVEL 1 — LIFE-THREATENING BEHAVIORS
Items present: [list, with severity]
Block(s): [N min] — Intervention: [chain analysis + solution analysis + risk re-screen]
Rationale: [Why this item is Level 1, why this severity ordering]
Risk re-screen: [Y; tool used: Columbia; outcome]

LEVEL 2 — THERAPY-INTERFERING BEHAVIORS
Items present: [missed session; late; card incomplete; fees; refused homework]
Block: [N min] — Intervention: [behavioral analysis of TIB; problem-solving with client commitment]

LEVEL 3 — QUALITY-OF-LIFE-INTERFERING BEHAVIORS
Client-priority items: [Top 1–2 items]
Block: [N min] — Intervention: [skill application, behavioral chain on QOL pattern, validation+problem-solving]

LEVEL 4 — SKILLS GENERALIZATION
Block: [N min] — Intervention: [Coaching on current group module; in-session rehearsal; cue planning]

BUFFER (closing)
Block: [3–5 min] — Diary-card hand-off, homework set, next-session date.

DIALECTICAL STANCE / VALIDATION NOTES
- Client preferred topic: [...]
- Validation provided: [...]
- Reason for ordering: [...]

CONSULTATION-TEAM ITEMS
- [Item to bring this week's team meeting]

HOMEWORK
- Diary card daily
- Skills practice: [Specific module/skill, daily cadence]
- Chain analyses to complete: [Y/N — what targets]
- Coaching-call use plan: [...]

DOCUMENTATION
- Note type / billing code: [90834 / 90837 per length]
- Risk stratification at session: [Low / Moderate / High; rationale]
- Coordination needed (group leader, psychiatrist, PCP): [...]
- Next session: [Date]
```

## Verification

- [ ] Agenda ordered strictly: Level 1 → 2 → 3 → 4.
- [ ] Level-1 item gets chain analysis + risk re-screen.
- [ ] TIB addressed; not skipped for alliance.
- [ ] Time blocks in minutes; sum to session length minus buffer.
- [ ] Closing buffer for diary card and homework.
- [ ] Consultation-team items flagged.
- [ ] Dialectical stance / validation captured.
- [ ] Risk stratification documented.
- [ ] Homework includes diary card and named skills practice.
- [ ] Re-ordering rationale present when multiple Level-1 items compete.
- [ ] No fabricated agenda items.
