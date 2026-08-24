---
title: "DBT Skills Coaching Call Simulator"
category: psychology/modalities/dbt
description: "Simulate and structure a DBT phone-coaching call (24/7 between-session contact for skills, not therapy) within Linehan's contract: in-the-moment skill selection, brief, time-limited, not problem-solving."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - DBT
  - phone-coaching
  - skills-coaching
  - Linehan
  - between-session-contact
  - therapy-interfering-behavior
intended_use: model-testing
updated: "2026-05-19"
related_prompts:
  - domain-psychology/modalities/dbt/psychology_dbt_diary_card_analyzer.md
  - domain-psychology/modalities/dbt/psychology_dbt_target_hierarchy_session_organizer.md
  - domain-psychology/risk-crisis/psychology_crisis_de_escalation_session_plan.md
---

# DBT Skills Coaching Call Simulator

## Objective

Produce a structured DBT skills-coaching call: a brief (3–15 minute), in-the-moment, skill-focused phone or text contact with a DBT client between sessions. The call's purpose is to **coach a skill the client already knows**, **not** to provide therapy, problem-solving, or crisis management. The output is a call-flow template plus a record-keeping note documenting the call.

## When to Use

- Standard adherent DBT, individual therapist's 24/7 phone-coaching contract.
- Client is having an urge (suicide, NSSI, substance, binge, rage outburst) and is calling for skills help **before** acting.
- Client wants to repair a recent interpersonal rupture (DEAR MAN application).
- Client wants generalization help with a skill assigned for homework.
- Telehealth equivalent: secure messaging or video coaching contact.
- Not appropriate when the call is for: extended therapy content, emotional venting, problem-solving the underlying issue, or for any reason after the client has acted on a life-threatening urge (then the 24-hour rule applies — no coaching call after self-harm).

## Inputs / Context

- Client's name and identifier; consent for coaching calls; coaching-call contract on file.
- Time of call; expected duration.
- Client's stated reason for calling.
- Recent diary-card data and target hierarchy status.
- Skills client has been taught (mindfulness, distress tolerance, emotion regulation, interpersonal effectiveness — which modules, when).
- Current risk plan and safety plan.
- 24-hour rule status: did the client engage in life-threatening behavior in the last 24 hours? (If yes, route to risk plan, not coaching.)
- Therapist's availability window and back-up coverage.

## Constraints

### Must

- Time-limit the call (3–15 minutes default); set the limit at the start.
- Establish the call's purpose: "Which skill are we working on?"
- Apply the **24-hour rule**: if the client has engaged in life-threatening behavior in the prior 24 hours (NSSI, suicide attempt, substance overdose), do not coach skills; route to medical / safety plan and schedule next session. Document this.
- Coach a **specific** skill the client already knows; do not introduce new skills mid-call.
- Use behavioral specifics: "Right now, put cold water on your face for 30 seconds. I'll wait."
- For interpersonal coaching: walk through DEAR MAN / GIVE / FAST steps for the specific upcoming interaction.
- Validate briefly; do not therapize the underlying issue.
- Plan a check-back (text/voicemail) within the contract window if appropriate.
- Document the call in the chart same day; classify as TIB-prevention or skills-generalization.
- If the client is in active crisis with imminent risk, exit coaching frame and apply risk plan / Stanley-Brown.

### Must Not

- Do not coach after life-threatening behavior in the prior 24 hours (24-hour rule).
- Do not extend the call indefinitely; structure beats duration.
- Do not introduce new skills the client has not been taught.
- Do not problem-solve the underlying conflict; coach the skill, save the problem for the session.
- Do not provide unlimited reassurance; reassurance becomes reinforcing.
- Do not let the call drift into venting; redirect to skill use.
- Do not skip documentation; an undocumented coaching call is a missed teaching opportunity and a record gap.
- Do not allow coaching to substitute for the session.

## Instructions

1. **Frame the call (30 seconds):** "What's the urge? What skill do you want to work on? I have about 10 minutes."
2. **Check the 24-hour rule.** If the client has engaged in life-threatening behavior since the last contact, exit coaching, switch to risk plan, schedule.
3. **Quick orientation:** brief validation (1–2 sentences), no therapizing.
4. **Skill selection:** with the client, pick **one** skill they know.
5. **In-moment instruction:** behavior-specific, with timing. E.g., "Hold the ice cube to the back of your neck for 30 seconds; tell me when you start."
6. **Walk through application:** observe the behavior; check effectiveness; choose a next skill if the first didn't move the urge.
7. **Plan the next 30–60 minutes:** specific actions, distraction or task, who they'll call next, when they'll text the therapist.
8. **End:** confirm session time; set check-back if appropriate.
9. **Document** the call: reason, skill coached, outcome, plan, time spent.

## Output Format

```
=== DBT COACHING CALL — SIMULATION / RECORD ===
Client: [Initials/MRN]    Date/Time: [YYYY-MM-DD HH:MM]    Channel: [Phone / secure msg / video]
Duration: [N min]    Therapist: [Name]
Coaching-call contract in chart: [Y]
24-hour rule check: [Client has not engaged in LTB in prior 24 hr / Client has — coaching not provided]

CALL FRAME
"What's the urge?" Client: "[verbatim or summary]"
"What skill?" Client: "[verbatim or summary]"
Time-limit set: [N min]

VALIDATION (brief, 1–2 sentences)
"[verbatim]"

SKILL COACHED
- Skill name: [e.g., TIPP — Temperature]
- Procedure: [Cold water 30s; ice cube 30s to back of neck; etc.]
- Timing: [Start time, end time]
- Effectiveness check (urge 0–100): pre [N] → post [N]
- Backup skill if not effective: [Name]

NEXT 30–60 MINUTES
- Specific actions: [...]
- Distraction / task: [...]
- Next contact: [Whom / when]
- Therapist check-back: [Y/N — when]

EXIT FRAME
- Session reminder: [Date/time]
- Diary-card capture: [Reminded]
- If urge re-escalates: [Plan — call back, 988, ED]

RECORD-KEEPING NOTE
- Coaching call placed: [Y]
- Skill coached: [...]
- Outcome: [...]
- Classification: [Skills generalization / TIB prevention / risk-adjacent]
- Time spent: [N min]
- Risk re-screen during call: [Y/N — result]
- Consultation-team flag: [If repeated coaching for same target without movement]

EXIT TO RISK PLAN (if applicable)
- Reason: [Imminent risk; LTB in prior 24 hr]
- Action: [Stanley-Brown plan activated; ED; mobile crisis; 988]
- Continuity: [...]
```

## Verification

- [ ] Time limit set at start.
- [ ] 24-hour rule checked and applied.
- [ ] One specific skill coached; not new content.
- [ ] Behavior-specific in-moment instruction with timing.
- [ ] Urge pre/post rating captured.
- [ ] Next 30–60 minutes planned with specific actions.
- [ ] Call documented same day.
- [ ] Validation present but brief; no extended therapizing.
- [ ] Exit-to-risk plan path described.
- [ ] No new skills introduced mid-call.
- [ ] Coaching not provided after LTB in prior 24 hours.
