---
title: "CPT (Cognitive Processing Therapy) Session Protocol"
category: psychology/modalities/cpt
description: "Generate a Cognitive Processing Therapy (Resick) session plan within the 12-session PTSD protocol: Impact Statement, Stuck Point Log, ABC sheets, Challenging Questions and Challenging Beliefs Worksheets, and the five themes (Safety, Trust, Power/Control, Esteem, Intimacy)."
techniques:
  - ST-04
  - RT-02
  - DT-02
  - ED-04
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - CPT
  - cognitive-processing-therapy
  - PTSD
  - Resick
  - stuck-points
  - challenging-beliefs-worksheet
  - five-themes
  - assimilation-accommodation
intended_use: model-testing
updated: "2026-06-08"
related_prompts:
  - domain-psychology/modalities/emdr-trauma/psychology_prolonged_exposure_session_plan.md
  - domain-psychology/modalities/cbt/psychology_cbt_thought_record_drafter.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
  - domain-psychology/modalities/grief-therapy/psychology_prolonged_grief_therapy_protocol.md
---

# CPT (Cognitive Processing Therapy) Session Protocol

## Objective

Generate a single Cognitive Processing Therapy (CPT; Resick, Monson, Chard) session plan placed within the standard 12-session PTSD protocol, or a multi-session protocol map. The plan ties the session number to its manualized content (psychoeducation, Impact Statement, ABC sheets, Stuck Point Log development, Challenging Questions Worksheet, Patterns of Problematic Thinking, Challenging Beliefs Worksheets across the five themes), specifies the CPT vs. CPT+A variant, captures stuck points, and assigns practice (homework) between sessions. Output includes a structured Stuck Point Log and a per-session protocol map.

## When to Use

- DSM-5-TR PTSD confirmed, ideally with a PCL-5 baseline and weekly PCL-5 monitoring.
- Adults with single-incident or chronic trauma; CPT is trauma-focused and present-oriented around stuck points (over-generalized maladaptive beliefs), not narrative exposure per se.
- Either variant: **CPT** (no written account) or **CPT+A** (includes a written trauma account read aloud in sessions 4–5).
- Telehealth: CPT delivers well via telehealth with worksheets shared on-screen or in advance.
- Mid-protocol sessions where stuck points and worksheets are being developed and challenged.
- Not for clients with active psychosis, imminent suicide risk, or severe dissociation requiring stabilization-first; not a substitute for crisis intervention, medication management, or a comprehensive trauma assessment.

## Inputs / Context

- Baseline and weekly PCL-5 (and PHQ-9 / GAD-7 if tracked) with trajectory.
- Variant decision: CPT vs. CPT+A (with rationale).
- Index trauma and any additional traumas; current "worst" event the protocol is anchored to.
- Impact Statement content (session 1 assignment): client's stated reasons the trauma happened and how it changed beliefs about self, others, world.
- Existing Stuck Point Log entries and their theme classification.
- Which worksheet the client is currently practicing (ABC → Challenging Questions → Patterns of Problematic Thinking → Challenging Beliefs Worksheet).
- Homework status from prior session.
- Risk and safety plan; substance use status.
- Modality (in-person / telehealth) and cultural / developmental considerations.

## Constraints

### Must

- Confirm the **weekly PCL-5** at session start and chart the trajectory.
- Map each session to its **manualized content** (see protocol map below): Sessions 1 (psychoed + Impact Statement assignment), 2 (Impact Statement read + first stuck points + ABC sheets), 3 (ABC review), 4–5 (in CPT+A, trauma account written and read; in CPT, Challenging Questions introduced), 6–7 (Challenging Questions + Patterns of Problematic Thinking), 8–11 (Challenging Beliefs Worksheets across the five themes), 12 (revised Impact Statement + relapse/recovery review).
- Identify, label, and log **stuck points** as specific, distorted, over-generalized belief statements ("It was my fault," "I can't trust anyone"), not emotions or facts.
- Classify each belief as **assimilated** (altering the memory to fit prior beliefs — e.g., self-blame / hindsight bias / undoing), **over-accommodated** (extreme present/future beliefs — e.g., "the world is completely dangerous"), or **accommodated** (balanced, realistic — the target outcome).
- Address the **five themes** in order as worksheets progress: **Safety, Trust, Power/Control, Esteem, Intimacy** (self and others within each).
- Use **Socratic dialogue** to challenge stuck points (CPT does not dispute by lecturing; the client generates evidence via the worksheet questions).
- Assign **practice assignments** between sessions tied to the current worksheet and theme.
- **Risk re-screen** at session start (suicidality; substance use; PTSD cluster check); include a **consultation / co-sign line** for high-acuity trauma per setting policy.
- For dissociation: ground first, then resume worksheet/account work; if persistent, pause and reformulate.

### Must Not

- Do not log emotions, facts, or events as stuck points; stuck points are **belief statements**.
- Do not deliver CPT as exposure: CPT+A uses the account to surface stuck points, not for habituation/SUDS tracking (that is PE lineage).
- Do not skip the Impact Statement or the revised Impact Statement at session 12.
- Do not dispute beliefs by argument; use the Socratic worksheet questions so the client generates balanced alternatives.
- Do not advance to Challenging Beliefs Worksheets before the client can use Challenging Questions and recognize Patterns of Problematic Thinking.
- Do not conduct trauma-focused work without an active safety plan and risk-monitoring cadence.
- Do not skip the weekly PCL-5 or the trajectory review.

## Instructions

1. PCL-5 check-in and trajectory chart; homework review.
2. Risk re-screen (Columbia or comparable); substance use status.
3. Confirm session number and pull the manualized content for that session from the protocol map.
4. Review or develop the **Impact Statement** (sessions 1–2) or the **revised Impact Statement** (session 12).
5. Surface and label new **stuck points**; add to the Stuck Point Log with theme + assimilation/over-accommodation classification.
6. Work the **current worksheet** (ABC → Challenging Questions → Patterns of Problematic Thinking → Challenging Beliefs Worksheet) via Socratic dialogue; in CPT+A sessions 4–5, the written account is read aloud and mined for stuck points.
7. Move beliefs toward **accommodated** (balanced) alternatives the client generates.
8. Assign practice tied to the current worksheet and theme.
9. Update safety plan; document trajectory, stuck points, theme, variant, and consultation items.

## Output Format

```
=== CPT SESSION PLAN / NOTE ===
Client: [Initials/MRN]    Session #: [N of 12]    Date: [YYYY-MM-DD]    Variant: [CPT / CPT+A]
Index trauma: [Brief tag]
PCL-5 today: [N] (baseline [N]; last week [N]; trend ↑/↓/=)    PHQ-9: [N]    GAD-7: [N]

OPENING (5–10 min)
- PCL-5 review and trajectory: [...]
- Homework review: [Worksheet/account completed Y/N; quality]
- Risk re-screen: [Columbia or comparable; SI; means access]
- AOD status: [...]

IMPACT STATEMENT (sessions 1–2; revised session 12)
- Reasons client believes the trauma happened: [...]
- Beliefs about self / others / world it created: [...]
- Revised statement shifts (session 12): [...]

STUCK POINT LOG (running)
| # | Stuck point (belief statement)        | Theme              | Type (assim/over-accom/accom) | Status        |
|---|---------------------------------------|--------------------|-------------------------------|---------------|
| 1 | [e.g., "It was my fault"]             | [Safety/Trust/...] | [Assimilated]                 | [Active]      |
| 2 | [e.g., "I can't trust anyone"]        | [Trust]            | [Over-accommodated]           | [In progress] |
| 3 | [...]                                  | [...]              | [...]                         | [...]         |

WORKSHEET WORK THIS SESSION
- Current worksheet: [ABC / Challenging Questions / Patterns of Problematic Thinking / Challenging Beliefs Worksheet]
- Theme in focus: [Safety / Trust / Power-Control / Esteem / Intimacy — self and/or others]
- Stuck point(s) challenged: [#s from log]
- Socratic questions used: [...]
- Patterns of Problematic Thinking identified: [e.g., jumping to conclusions, over-generalizing, mind reading]
- Balanced (accommodated) alternative the client generated: [...]
- CPT+A account (sessions 4–5): [Read aloud Y/N; new stuck points surfaced]

PROTOCOL MAP (orientation)
- S1: Psychoed on PTSD + CPT; assign Impact Statement
- S2: Read Impact Statement; first stuck points; ABC sheets
- S3: ABC review; build Stuck Point Log
- S4–5: CPT+A — written account read; CPT — Challenging Questions introduced
- S6–7: Challenging Questions + Patterns of Problematic Thinking
- S8: Safety  | S9: Trust  | S10: Power/Control  | S11: Esteem
- S12: Intimacy + revised Impact Statement + relapse/recovery review

PRACTICE ASSIGNMENT (homework)
- Worksheet: [Which; how many stuck points]
- Theme focus: [...]
- Account task (CPT+A): [...]

RISK / SAFETY
- Suicidality: [...]    Means access: [...]
- Substance use: [...]
- Safety plan adequacy: [...]
- Between-session check-in: [Y/N — when]

DOCUMENTATION
- Note type / billing: [90834 / 90837]
- Trajectory observation: [...]
- Reformulation flag: [Y/N — what triggered]
- Consultation / supervision / co-sign (high-acuity trauma): [Name; date]
- Next session: [Date / planned theme]
```

## Verification

- [ ] Weekly PCL-5 captured and trajectory charted.
- [ ] Session content matches the manualized 12-session protocol map.
- [ ] Variant (CPT vs. CPT+A) stated; account handled correctly for the variant.
- [ ] Stuck Point Log entries are belief statements, not emotions/facts.
- [ ] Each stuck point classified as assimilated / over-accommodated / accommodated.
- [ ] Worksheet progression respected (ABC → CQ → Patterns → Challenging Beliefs Worksheet).
- [ ] Five themes addressed in order across the worksheet phase.
- [ ] Stuck points challenged Socratically, not by argument.
- [ ] Impact Statement assigned (S1) and revised (S12).
- [ ] Risk re-screen and safety plan check at session start.
- [ ] Consultation / co-sign line present for high-acuity trauma.
- [ ] No fabricated PCL-5 scores, stuck points, or client content.
