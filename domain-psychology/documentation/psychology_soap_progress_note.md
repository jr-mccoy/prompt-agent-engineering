---
title: "SOAP-Format Psychotherapy Progress Note Drafter"
category: psychology/documentation
description: "Convert raw session notes into a clinically defensible SOAP-format individual psychotherapy progress note that supports the billed CPT code."
techniques:
  - ST-04
  - DT-02
  - QA-04
  - CM-02
  - DS-04
difficulty: intermediate
tags:
  - progress-note
  - soap
  - psychotherapy-documentation
  - cpt-90834
  - cpt-90837
  - golden-thread
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/documentation/psychology_dap_progress_note.md
  - domain-psychology/documentation/psychology_birp_progress_note.md
  - domain-psychology/documentation/psychology_intake_assessment_note.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
---

# SOAP-Format Psychotherapy Progress Note Drafter

## Objective

Convert a clinician's raw session shorthand into a complete SOAP-format individual psychotherapy progress note that:

1. Is structurally faithful to the SOAP format (Subjective / Objective / Assessment / Plan).
2. Justifies the billed CPT code (typically **90832** ~30 min, **90834** ~45 min, **90837** ~60 min, with **+90785** for interactive complexity, **+90833 / +90836 / +90838** for E&M add-ons).
3. Maintains the **golden thread**: presenting problem → treatment-plan goal → in-session intervention → measurable response → next-session plan.
4. Includes risk reassessment, medication / substance check, and any safety actions taken.

## When to Use

- After an outpatient individual psychotherapy session when the EHR uses or accepts SOAP.
- When auditing a clinician's prior note for SOAP-format completeness.
- When a payer requires structured SOAP documentation for utilization review.
- For training models on format-faithful clinical writing.

## Inputs / Context

Provide the following. If anything is missing, ask before drafting.

- **Session metadata:** date, start/stop time, duration in minutes, modality (in-person / telehealth-video / telehealth-audio-only), location of clinician, location of client, CPT code billed, ICD-10 codes addressed, treatment-plan goals being worked.
- **Client identifiers:** initials or MRN, age, gender, pronouns, relevant cultural / linguistic context.
- **Session content (raw notes):** what was discussed, what the clinician did (interventions, by name and dose), how the client responded, any homework reviewed or assigned.
- **Risk indicators present this session:** SI / HI / NSSI / substance use / psychosis / abuse disclosures, plus what was assessed and any actions taken.
- **Mental status data points** the clinician observed (appearance, behavior, speech, mood, affect, thought process, thought content, cognition, insight, judgment).
- **Outcome measures** administered this session and scores (PHQ-9, GAD-7, PCL-5, etc.).

## Constraints

### Must

- Output the four canonical SOAP sections in order, each with a clear heading: **Subjective**, **Objective**, **Assessment**, **Plan**.
- Place client-reported content (verbatim or paraphrased quotes, self-reported symptoms, life events) in **Subjective**.
- Place clinician-observed and measured data (MSE, vitals if relevant, test scores, behavior in session) in **Objective**.
- In **Assessment**, document clinical reasoning: progress vs treatment-plan goals, current diagnostic impression, response to intervention, risk formulation.
- In **Plan**, document next session plan, frequency, homework assigned, referrals, medication coordination, and any safety follow-through.
- Name interventions by their evidence-based label (e.g., "cognitive restructuring of automatic thought," "interoceptive exposure with diaphragmatic breathing," "DBT TIPP skill rehearsal," "behavioral activation activity scheduling," "MI reflection of change talk"). Do not write "talked about it" or "supportive listening" without further specification.
- Document risk reassessment every session, even when low: explicitly state SI/HI/NSSI status with current/denied language and the basis for the conclusion.
- Tie at least one in-session intervention to a numbered/lettered treatment-plan goal so the golden thread is visible.
- Justify session length: for 90837, demonstrate medical necessity for the extended session (complexity, crisis content, exposure session, family involvement, etc.).

### Must Not

- Do not invent content the clinician did not provide. If a SOAP section has no source data, write `[clinician input required: <what is missing>]`.
- Do not soften or omit risk content that was disclosed. If the client reported SI, document it with severity, frequency, plan, intent, means, and protective factors.
- Do not include client identifiers beyond what the clinician provides, and never insert generic placeholder names ("John Doe") — leave fields the clinician must populate as bracketed prompts.
- Do not editorialize ("the client seemed to really benefit from..."). Use observable, behavioral language.
- Do not duplicate Subjective content into Objective — keep the source-of-evidence distinction clean.

## Instructions

1. **Parse inputs and identify gaps.** List any missing items from the Inputs section before drafting. If the clinician proceeds without them, mark each gap as a bracketed prompt in the output.
2. **Draft Subjective.** Lead with the client's stated agenda or chief complaint *for this session* (not the original referral problem). Include sleep, appetite, substance use, medication adherence, side effects, and interpersonal stressors as the client reported them. Use one direct quote when it captures the session's emotional core.
3. **Draft Objective.** Compose a session-specific MSE paragraph. Include outcome-measure scores with comparison to prior administration if available. Note attendance, punctuality, telehealth environment if applicable.
4. **Draft Assessment.** Begin with the active diagnoses (ICD-10 with descriptors). Then write 3–6 sentences covering: progress on treatment-plan goals, response to today's interventions, current symptom severity, and updated risk formulation. State clinical impression of trajectory (improving / stable / worsening / acute change).
5. **Draft Plan.** Include: next appointment date/frequency, homework assigned (specific and measurable), referrals or coordination needed, medication communication, safety plan status (reviewed / updated / not indicated), and clinician's own follow-up tasks.
6. **Append billing block.** State the CPT code, time in/out, total minutes, modality, and one-sentence medical-necessity justification.
7. **Run the verification checklist** before delivering.

## Output Format

```
=== PROGRESS NOTE (SOAP) ===

Client: [Initials/MRN]    DOB: [age, gender, pronouns]
Date of Service: [YYYY-MM-DD]    Time In/Out: [HH:MM – HH:MM]    Duration: [N min]
Modality: [in-person | telehealth-video | telehealth-audio-only]
Clinician location: [...]    Client location: [...]
CPT: [code]    ICD-10: [codes addressed this session]
Treatment-plan goals addressed: [Goal #1 short label; Goal #3 short label]

SUBJECTIVE
[Client's stated agenda for the session.]
[Reported symptoms since last session, with frequency / intensity / duration.]
[Sleep, appetite, energy, concentration, anhedonia/interest, anxiety, irritability, substance use.]
[Medication adherence and side effects (if applicable).]
[Interpersonal / occupational / situational stressors.]
[One direct quote when illustrative: "..."]
[Self-reported risk: SI/HI/NSSI status as client described it.]

OBJECTIVE
[MSE paragraph: appearance, behavior, speech, mood (client-stated, in quotes), affect (clinician-observed), thought process, thought content, cognition, insight, judgment.]
[Outcome measures: PHQ-9 = X (prior X on YYYY-MM-DD), GAD-7 = X, ...]
[Clinician-observed engagement: e.g., "Engaged actively; tearful when discussing X; used grounding skill spontaneously when dysregulated."]

ASSESSMENT
Active diagnoses: [F##.# Description; F##.# Description].
[3–6 sentences: progress vs treatment-plan goals, response to today's interventions named explicitly, current severity, risk formulation, trajectory impression.]
Risk: SI [denied/passive/active with/without plan/intent/means]; HI [denied/...]; NSSI [denied/...]; protective factors [...]; risk level this session [low/moderate/high]; safety plan [reviewed/updated/not indicated].

PLAN
- Next session: [date or interval], [frequency rationale if changing].
- Continue: [modality / modules being worked].
- Homework assigned: [specific, measurable, with review at next session].
- Coordination: [PCP / psychiatry / school / family / case manager], with date and method.
- Medication: [no change / awaiting prescriber response / client to discuss with prescriber re X].
- Safety: [safety plan status; means restriction status; emergency contacts confirmed].
- Clinician follow-up: [tasks owned by the clinician with target dates].

BILLING
CPT [#####] x 1, [N] minutes face-to-face. [+90785 if interactive complexity, with reason.]
Medical necessity: [one-sentence justification tied to active diagnosis and treatment-plan goal].

Clinician: [name, credentials, license #, signature, date/time]
```

## Verification

Before delivering, confirm:

- [ ] All four SOAP sections present and non-empty (or have bracketed clinician-input prompts).
- [ ] No content from the clinician's raw notes is missing from the appropriate section.
- [ ] At least one named, evidence-based intervention appears in Assessment or Plan and is tied to a treatment-plan goal.
- [ ] Risk explicitly reassessed (SI / HI / NSSI), even if low or denied.
- [ ] CPT code, duration, and medical-necessity sentence are consistent with each other (e.g., 90837 has ≥53 min and a complexity rationale).
- [ ] Subjective vs Objective separation is clean — no observed data in Subjective, no client-reported data in Objective.
- [ ] Outcome-measure scores include a prior comparator when available.
- [ ] No invented content; all gaps flagged as bracketed prompts.
- [ ] Telehealth-specific elements present if modality is telehealth (locations, environment adequacy, identity verification reaffirmation if first session of episode).
