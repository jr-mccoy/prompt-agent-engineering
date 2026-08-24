---
title: "Pediatric Safety Planning with Caregiver"
category: psychology/populations/child-adolescent
description: "Dyadic Stanley-Brown–adapted safety plan built with both the youth and caregiver, integrating Columbia C-SSRS risk stratification, developmentally calibrated warning signs and coping steps, caregiver-led means restriction, and a documented risk-reassessment loop."
techniques:
  - ST-04
  - RT-02
  - RT-04
  - CM-02
  - QA-04
  - DS-02
difficulty: advanced
intended_use: model-testing
tags:
  - safety-planning
  - stanley-brown
  - columbia-cssrs
  - suicide-prevention
  - means-restriction
  - caregiver
  - youth
  - risk-reassessment
updated: "2026-06-08"
related_prompts:
  - domain-psychology/risk-crisis/psychology_stanley_brown_safety_plan.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
  - domain-psychology/populations/child-adolescent/psychology_adolescent_intake_with_developmental_lens.md
  - domain-psychology/populations/child-adolescent/psychology_adolescent_dbt_skills_module.md
---

# Pediatric Safety Planning with Caregiver

## Objective

Build a developmentally calibrated, dyadic Stanley-Brown Safety Planning Intervention (SPI) for a youth at risk for suicide, completed with both the youth and at least one caregiver. The plan:

1. Anchors to a current Columbia C-SSRS (Adolescent) risk stratification and disposition decision.
2. Completes the six Stanley-Brown steps with youth-generated, age-appropriate content: warning signs, internal coping, social distractions/settings, people to ask for help, professionals/agencies, and means restriction.
3. Splits the dyad's roles: the youth co-authors the plan; the caregiver owns lethal-means restriction and emergency access, and learns how to support without surveillance that backfires.
4. Documents confidentiality handling — what must be shared with the caregiver for safety versus what remains private.
5. Establishes a concrete risk-reassessment loop and follow-up (caring contacts, next appointment, escalation triggers).
6. Provides copies to youth and caregiver and documents the encounter.

## When to Use

- After a Columbia C-SSRS or clinical assessment identifies suicidal ideation, a recent attempt, or elevated risk in a youth (typically ages 10–17), when outpatient safety planning is the appropriate disposition.
- At hospital discharge / ED follow-up, post-attempt re-engagement, or when ideation emerges in ongoing treatment.
- Whenever a caregiver can and should be engaged in means restriction and monitoring.

## When NOT to Use

- When the youth requires immediate higher level of care (active intent + plan + means, inability to maintain safety): arrange emergency evaluation/hospitalization first; safety planning does not substitute for crisis stabilization.
- For adults 18+: use the standard `psychology_stanley_brown_safety_plan.md`.
- When no caregiver is available — adapt with the available protective adult and document the limitation; do not omit means-restriction planning.

## Inputs / Context Required

- **Youth:** Initials/MRN, age, developmental stage, diagnosis, presenting risk.
- **Risk assessment:** Current Columbia C-SSRS (Adolescent) findings — ideation type/severity, behavior, intent, plan, access to means.
- **Caregiver:** Name(s), relationship, legal authority, capacity/willingness to restrict means and monitor.
- **Home means inventory:** Firearms, medications, sharps, other lethal means accessible in the home.
- **Supports:** Trusted people, settings, and professional/crisis contacts (incl. 988).
- **Disposition context:** Outpatient vs. step-down from ED/inpatient; current treatment.
- `[clinician input required: any disclosure the youth made privately (e.g., abuse, means access) that bears on safety and requires confidentiality/mandated-reporter analysis]`

## Constraints

### Must

- Complete or reference a current Columbia C-SSRS (Adolescent) before finalizing the plan; document risk level and disposition.
- Use youth-generated content in the youth's own words for warning signs and coping steps; calibrate to developmental stage.
- Complete all six Stanley-Brown steps; means restriction is mandatory and caregiver-owned.
- Conduct caregiver lethal-means counseling: secure/remove firearms, lock and limit medications, restrict other identified means; document the agreed actions and timeline.
- Manage confidentiality explicitly: certain content (intent, plan, means access, recent attempt) must be shared with the caregiver for safety; document what was shared and what private content was protected and why.
- Establish a risk-reassessment loop: explicit triggers for escalation, 988/crisis access, caring-contact/follow-up timing, and next appointment.
- Provide copies to youth and caregiver; document the encounter and a mandated-reporter screen if abuse/neglect surfaced.
- Flag gaps with `[clinician input required: ...]`; do not fabricate means inventory or supports.

### Must Not

- Do not finalize an outpatient safety plan when criteria for emergency evaluation are met; escalate first.
- Do not write warning signs/coping steps for the youth in the clinician's words — they must be the youth's.
- Do not rely on monitoring/surveillance in place of actual means restriction.
- Do not share the youth's private, non-safety-relevant content with the caregiver; protect it and document the boundary.
- Do not omit means-restriction planning even when a caregiver is reluctant — document the barrier and the plan to address it.
- Do not fabricate the means inventory, supports, or caregiver agreement.

## Developmental & Dyadic Calibration Reference

| Element | Younger (≈10–13) | Older (≈14–17) |
|---------|------------------|-----------------|
| Warning signs | Concrete, body/behavior cues ("tummy hurts," "want to hide") | Cognitive/emotional cues, situational triggers |
| Internal coping | Simple, sensory, brief; caregiver may prompt | Self-initiated skills (DBT TIPP/distraction), autonomy emphasized |
| Help-seeking | Heavily caregiver-mediated | Balance autonomy with reachable adults; peer-to-adult bridge |
| Means restriction | Fully caregiver-owned | Caregiver-owned; youth informed and collaborating |
| Confidentiality | Limited privacy; most shared with caregiver | Protect non-safety private content; share safety-critical content |

## Instructions

1. **Confirm disposition.** Review the Columbia C-SSRS; if emergency criteria are met, escalate and stop here. Otherwise proceed with outpatient safety planning.
2. **Set the dyadic frame.** Explain to youth and caregiver how the plan is built together, each person's role, and the confidentiality boundary.
3. **Step 1 — Warning signs (youth-generated, age-calibrated).**
4. **Step 2 — Internal coping strategies** the youth can use alone.
5. **Step 3 — Social distractions** (people and settings that help take the youth's mind off the crisis).
6. **Step 4 — People to ask for help** (trusted adults/peers), with caregiver as a named front-line contact.
7. **Step 5 — Professionals and agencies**, including 988 and local crisis services.
8. **Step 6 — Means restriction (caregiver-owned):** conduct lethal-means counseling; document firearms, medications, and other means actions and timeline.
9. **Confidentiality handling:** document what was shared with the caregiver for safety and what private content was protected; complete a mandated-reporter screen if indicated.
10. **Risk-reassessment loop:** define escalation triggers, follow-up/caring-contact timing, and next appointment.
11. **Distribute and document.** Provide copies; write the encounter note.
12. **Run verification.**

## Output Format

```
=== PEDIATRIC DYADIC SAFETY PLAN (Stanley-Brown adapted) ===

Youth: [Initials/MRN]    Age: [N]    Stage: [...]    Dx: [DSM-5-TR + ICD-10-CM]
Caregiver(s) present: [Name(s), relationship, legal authority]
Date/Time: [YYYY-MM-DD HH:MM]    Clinician: [Name, credentials]    Setting/disposition: [Outpatient / ED follow-up / post-discharge]

─────────────────────────────────────────
RISK STRATIFICATION (Columbia C-SSRS – Adolescent)
─────────────────────────────────────────
Ideation type / most severe: [...]    Plan: [Y/N]    Intent: [Y/N]
Behavior (lifetime/recent): [...]    Access to means: [...]
Protective factors: [...]
Risk level: [Low / Moderate / High — rationale]
Disposition decision: [Outpatient safety plan appropriate / Escalated to emergency eval — STOP]

─────────────────────────────────────────
CONFIDENTIALITY FRAME (explained to youth & caregiver)
─────────────────────────────────────────
Shared with caregiver for safety: [Intent / plan / means access / recent attempt — as applicable]
Protected (non-safety private content): [...] — boundary explained: [Yes]
Mandated-reporter screen (if abuse/neglect surfaced): [Not triggered / Triggered — consultation, report (agency, date/time, #)]

─────────────────────────────────────────
STEP 1 — WARNING SIGNS (youth's own words)
─────────────────────────────────────────
- "[...]"  - "[...]"  - "[...]"

─────────────────────────────────────────
STEP 2 — INTERNAL COPING STRATEGIES (do alone)
─────────────────────────────────────────
- [...]  - [...]  - [...]

─────────────────────────────────────────
STEP 3 — SOCIAL DISTRACTIONS (people / settings)
─────────────────────────────────────────
People: [...]    Settings: [...]

─────────────────────────────────────────
STEP 4 — PEOPLE TO ASK FOR HELP
─────────────────────────────────────────
Caregiver (front-line): [Name — phone]
Other trusted adults/peers: [Name — phone]

─────────────────────────────────────────
STEP 5 — PROFESSIONALS & AGENCIES
─────────────────────────────────────────
Clinician/on-call: [Name — phone]
988 Suicide & Crisis Lifeline: call/text 988    Crisis Text Line: text HOME to 741741
Local crisis/mobile team: [...]    Nearest ED: [...]

─────────────────────────────────────────
STEP 6 — MEANS RESTRICTION (caregiver-owned)
─────────────────────────────────────────
Firearms in home: [None / Present — action: removed from home / locked, ammo separated; owner: ...; timeline: ...]
Medications: [Lock box / removed / dispensed by caregiver; specific meds: ...; timeline: ...]
Other means (sharps, ligature, etc.): [Identified: ...; action: ...]
Caregiver agreement obtained: [Yes — specifics] / Barrier: [...] — plan to resolve: [...]
Means-restriction verified at follow-up: [Plan to confirm at ...]

─────────────────────────────────────────
RISK-REASSESSMENT LOOP & FOLLOW-UP
─────────────────────────────────────────
Escalation triggers (when to call 988 / go to ED): [...]
Caring contact / check-in: [Method, timing]
Next appointment: [Date/time]
Reassess risk at: [Next contact / if [trigger]]
Coordination: [School (with ROI) / PCP / psychiatry / crisis team]

─────────────────────────────────────────
DISTRIBUTION & DOCUMENTATION
─────────────────────────────────────────
Copies provided to: [Youth: Y/N] [Caregiver: Y/N] [Stored in chart: Y/N]
Encounter documented; risk assessment and safety plan filed.
```

## Verification

- [ ] Current Columbia C-SSRS (Adolescent) completed/referenced; risk level and disposition documented.
- [ ] Emergency criteria checked; escalation performed first if met (no outpatient plan substituted for crisis care).
- [ ] All six Stanley-Brown steps completed.
- [ ] Warning signs and coping steps are youth-generated and developmentally calibrated.
- [ ] Means restriction completed and caregiver-owned; firearms, medications, and other means addressed with timeline.
- [ ] Caregiver lethal-means counseling documented; reluctance/barriers handled, not omitted.
- [ ] Confidentiality boundary documented: safety-critical content shared, private content protected.
- [ ] Mandated-reporter screen documented if abuse/neglect surfaced.
- [ ] 988 and crisis resources included.
- [ ] Risk-reassessment loop with escalation triggers, follow-up, and next appointment specified.
- [ ] Copies provided to youth and caregiver and stored in chart.
- [ ] Gaps flagged with `[clinician input required: ...]`; no fabricated means inventory or supports.
