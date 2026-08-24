---
title: "BIRP-Format Progress Note Drafter"
category: psychology/documentation
description: "Draft a BIRP-format (Behavior / Intervention / Response / Plan) progress note common in CMH, SUD, and case-management settings."
techniques:
  - ST-04
  - DT-02
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - progress-note
  - birp
  - community-mental-health
  - substance-use-documentation
  - case-management
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/documentation/psychology_soap_progress_note.md
  - domain-psychology/documentation/psychology_dap_progress_note.md
  - domain-psychology/documentation/psychology_girp_progress_note.md
  - domain-psychology/documentation/psychology_pirp_progress_note.md
---

# BIRP-Format Progress Note Drafter

## Objective

Produce a complete BIRP progress note (**Behavior / Intervention / Response / Plan**) suitable for community mental health, SUD, ACT-team, ICM/PSR, and similar settings where state Medicaid or grant funders typically require BIRP.

The note must:

1. Open with observable, behavioral data (not interpretation) in **Behavior**.
2. Document each intervention with the evidence-based technique name and the goal it serves in **Intervention**.
3. Document the client's specific, observable **Response** to each intervention.
4. Specify next steps in **Plan**.
5. Survive a Medicaid / state audit: every intervention must be tied to a treatment-plan goal, every billed minute must be accounted for, and medical necessity must be evident.

## When to Use

- Community mental health, ACT, ICM, PSR, IOP/PHP, MAT clinic, or SUD outpatient settings.
- Funder requires BIRP (e.g., state Medicaid carve-out).
- Group / collateral / case-management encounters that benefit from behavior-first structuring.

## Inputs / Context

- Session metadata: date, start/stop time, duration, modality, location, CPT/HCPCS code, ICD-10, treatment-plan goal(s) worked, place of service.
- Treatment-plan goals (as currently written) and which were addressed today.
- Raw session content with what was observed (Behavior), what the clinician did (Intervention), how the client responded (Response).
- Risk indicators present and actions taken.
- MSE observations, measures administered.
- Substance-use status this session (last-use date, intoxication/withdrawal signs, drug-screen results if any).

## Constraints

### Must

- Output four labeled sections in order: **Behavior**, **Intervention**, **Response**, **Plan**.
- **Behavior** contains observable data only — appearance, presentation, statements (in quotes when possible), MSE, measure scores, substance-use status. No clinical interpretation in this section.
- **Intervention** lists each technique by evidence-based name (e.g., "Stage-2 MI: elaboration of change talk and double-sided reflection of ambivalence about cannabis use") and tags it to the treatment-plan goal it serves (e.g., `[Goal #2]`).
- **Response** documents the client's specific, observable response to each intervention — not "client engaged well," but "client identified 3 personal reasons to reduce use without prompting and committed to logging cravings on the printed sheet."
- **Plan** specifies next session, homework, coordination, medication discussion, safety actions, and clinician follow-up tasks.
- Risk content (SI / HI / NSSI / substance / abuse) appears in Behavior with what was observed/reported, in Intervention with what the clinician did about it, and in Plan with what happens next.
- Time in/time out and total minutes consistent with billed code.

### Must Not

- Do not put clinical interpretation in Behavior (e.g., "client appears resistant" — instead: "client crossed arms, declined to discuss cannabis use stating 'that's not why I'm here'").
- Do not list interventions without specifying the goal each serves.
- Do not write generic responses ("client tolerated session well"); specify the observable response.
- Do not omit substance-use status in SUD settings, even if "denied use since last session."
- Do not fabricate; flag gaps as `[clinician input required: ...]`.

## Instructions

1. Identify missing inputs and either request them or mark as bracketed prompts.
2. Draft **Behavior**: appearance, behavior in session, statements, MSE, measure scores, risk indicators as observed/reported, substance status. Use direct quotes liberally.
3. Draft **Intervention**: bulleted list, each item naming the technique and tagging the goal it serves (`[Goal #N]`).
4. Draft **Response**: bulleted list paralleling the Intervention list, with one observable response per intervention.
5. Draft **Plan**: next session date/frequency, homework with measurable terms, coordination contacts, medication coordination, safety actions and follow-through, clinician's own tasks.
6. Append billing block: code, units/minutes, place of service, medical-necessity sentence.
7. Run verification.

## Output Format

```
=== PROGRESS NOTE (BIRP) ===

Client: [Initials/MRN]    DOB: [age, gender, pronouns]
Date of Service: [YYYY-MM-DD]    Time In/Out: [HH:MM–HH:MM]    Duration: [N min]
Place of Service: [POS code + descriptor]    Modality: [in-person | telehealth-video | telehealth-audio-only]
Code(s) billed: [CPT/HCPCS]    ICD-10: [codes]
Treatment-plan goals addressed: [Goal #X, Goal #Y]

BEHAVIOR
[Appearance, hygiene, dress.]
[Behavior in session: engagement, eye contact, motor activity, cooperation.]
[Statements in client's own words, quoted: "..."]
[MSE elements observed: speech, mood (quoted), affect, thought process, thought content, cognition, insight, judgment.]
[Outcome measures: PHQ-9 = X (prior X / YYYY-MM-DD); GAD-7 = X; AUDIT = X; etc.]
[Risk indicators as observed/reported: SI/HI/NSSI status in client's language.]
[Substance-use status: last use [date], reported quantity/frequency, intoxication / withdrawal signs observed, drug-screen results if collected.]

INTERVENTION
- [Named technique #1 — concrete description] [Goal #X]
- [Named technique #2 — concrete description] [Goal #Y]
- [Risk-related action if any: safety plan reviewed, means restriction discussed, warm handoff to crisis team, ROI executed for collateral.]

RESPONSE
- [Observable response to Intervention #1: what client said, did, demonstrated.]
- [Observable response to Intervention #2: ...]
- [Response to risk-related action if applicable.]

PLAN
- Next session: [date / frequency].
- Homework: [specific, measurable, with review point].
- Coordination: [collateral contacts, referrals, with dates and ROI status].
- Medication: [coordination notes; client to discuss with prescriber re ...].
- Safety: [safety plan status; means restriction; emergency contacts].
- Clinician follow-up: [tasks with target dates].

BILLING
[Code] x [units/minutes], POS [##]. Medical necessity: [one sentence tied to active diagnosis and goal].

Clinician: [name, credentials, license #, signature, date/time]
```

## Verification

- [ ] Four sections present and correctly ordered.
- [ ] Behavior contains only observable data (zero interpretation).
- [ ] Each Intervention has a named technique and a Goal tag.
- [ ] Each Intervention has a corresponding observable Response.
- [ ] Risk reassessed in Behavior and acted on (or noted "no action indicated") in Intervention.
- [ ] Substance-use status documented if applicable to the population.
- [ ] Time in/out, total minutes, and billed code consistent.
- [ ] Plan items specific and measurable.
- [ ] All gaps flagged; nothing fabricated.
