---
title: "Modality Selection Decision Aid"
category: psychology/treatment-planning
description: "Match a clinical presentation to the best-fit evidence-based modality — CBT, DBT, ACT, EMDR, psychodynamic, or IFS — using structured decision logic."
techniques:
  - RT-02
  - RT-03
  - DS-02
  - QA-04
  - CM-01
difficulty: advanced
intended_use: model-testing
tags:
  - modality-selection
  - CBT
  - DBT
  - ACT
  - EMDR
  - psychodynamic
  - IFS
  - treatment-planning
  - evidence-based
updated: "2026-06-08"
related_prompts:
  - domain-psychology/treatment-planning/psychology_stepped_care_decision_aid.md
  - domain-psychology/treatment-planning/psychology_golden_thread_writer.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
  - domain-psychology/diagnostic-formulation/psychology_case_conceptualization_framework.md
---

# Modality Selection Decision Aid

## Objective

Apply structured decision logic to match a clinical presentation to the best-fit evidence-based therapy modality. Output a ranked recommendation (first choice, close alternatives) with an explicit rationale anchored to diagnosis, presentation features, evidence base, and practical feasibility. The clinician retains final judgment; this prompt surfaces and organizes the decision-relevant information.

## When to Use

- At treatment initiation when the clinician must choose among several viable modalities.
- When a client has not responded to the current modality and reformulation is under consideration.
- When a training clinician needs to articulate the clinical reasoning behind a modality choice for supervision.
- When the presentation includes comorbidities that complicate a single-modality choice.
- When the client has a strong preference and the clinician needs to evaluate its fit against evidence.

## Inputs / Context Required

- **Primary diagnosis** (DSM-5-TR / ICD-10-CM): including specifiers (e.g., MDD with anxious distress, PTSD with dissociation, BPD).
- **Comorbid diagnoses** (all active): rank-ordered by treatment priority if known.
- **Presenting features** beyond diagnosis: e.g., affect dysregulation severity, dissociation, avoidance profile, relationship pattern, somatic complaints, suicidality level.
- **Symptom severity baselines** (PHQ-9, GAD-7, PCL-5, DAST-10, or equivalent).
- **Prior treatment history**: modalities tried, duration, response or reason for discontinuation.
- **Trauma history**: presence / absence; type (single incident vs. complex / developmental); processing readiness.
- **Client factors**: emotional literacy, distress tolerance, interpersonal functioning, motivation to engage, cultural context, capacity for insight.
- **Practical constraints**: session frequency available (weekly / 2×/week / intensive); clinician competency; whether medication management is concurrent.
- `[clinician input required: any safety profile considerations — active suicidality, ongoing self-harm, eating disorder medical instability — that would modify modality selection]`

## Constraints

### Must

- Evaluate at minimum six modalities: CBT, DBT, ACT, EMDR, psychodynamic therapy (PDT / EFT / BRT), and IFS. Add CPT, PE, schema therapy, or MI if presentation warrants.
- Cite the primary evidence base for each modality in relation to the specific presentation (diagnosis + features), not modality reputation in general.
- Produce a ranked recommendation: **First Choice**, **Close Alternative(s)**, **Consider if [condition]**, **Insufficient evidence or contraindicated for this presentation**.
- For the First Choice, provide: (a) evidence rationale, (b) presentation-match rationale, (c) a specific protocol or treatment manual name, (d) expected session count or course length from the evidence base, (e) any prerequisite skills or stabilization needed before starting.
- Identify contraindications or cautions — not absolute prohibitions — for each modality relative to this presentation.
- Flag presentations for which evidence is sparse and recommend supplementing with supervision or consultation.
- Use `[clinician input required]` for any missing input that would materially change the recommendation.

### Must Not

- Do not present a single modality without acknowledging that alternatives have been evaluated.
- Do not recommend a modality the clinician has flagged as outside their competency without flagging that training or referral would be needed.
- Do not conflate modality selection with level-of-care selection (see `psychology_stepped_care_decision_aid.md`).
- Do not characterize any modality as universally superior; evidence base is population-level and individual variation is the rule.
- Do not fabricate evidence citations; reference named RCTs, meta-analyses, or clinical guidelines by approximate description only ("Cochrane review, 2021" or "APA Division 12 list, 2024 update") and flag if the clinician should verify currency.

## Instructions

1. **Organize the presentation profile**: Compile diagnosis, comorbidities, severity scores, trauma history, and client factors into a structured summary. Identify the primary treatment target (the problem that, if improved, most changes the client's functioning) and secondary targets.

2. **Apply the modality decision matrix**: For each of the six core modalities, evaluate:
   - **Evidence grade** for the primary diagnosis: A (strong RCT + meta-analytic support), B (moderate RCT or guideline support), C (case-series / emerging), or D (no evidence / evidence against).
   - **Presentation-match factors**: Which features of this client's presentation align with the modality's theory of change and mechanism?
   - **Presentation-mismatch or caution factors**: Which features may limit fit, require modification, or indicate a prerequisite stage first?
   - **Practical fit**: Clinician competency, session frequency required, availability of group components.

3. **Apply the trauma overlay** (if trauma history is present):
   - Phase-based model required? (stabilization → processing → integration)
   - Processing readiness: sufficient window of tolerance and distress tolerance for trauma processing?
   - If NOT ready: identify stabilization modality first (DBT skills, ACT, somatic stabilization) before EMDR or PE.
   - Complex / developmental trauma: modify EMDR (AIP extended preparation), consider IFS, CPT, or schema therapy over standard CBT-Trauma.

4. **Apply the affect dysregulation overlay** (if severe dysregulation, impulsivity, or self-harm present):
   - DBT as first choice when affect dysregulation + self-harm + interpersonal chaos meet criteria for BPD or BPD features.
   - ACT when experiential avoidance is the primary mechanism and values work is the lever.
   - IFS when the dysregulation is primarily driven by entrenched part conflicts and the client has capacity for internal observer work.

5. **Rank the modalities**: Assign First Choice, Close Alternative(s), Conditional recommendations, and Insufficient evidence / Contraindicated. Provide a one-paragraph rationale for the First Choice.

6. **Identify the specific protocol**: Name a treatment manual, published protocol, or structured approach (not just the modality umbrella) for the First Choice and primary alternative.

7. **Address the comorbidity sequencing question**: If multiple active diagnoses, recommend a sequencing logic — which modality / problem first, and why. Note when integrated or unified protocols (e.g., Unified Protocol, DBT for MDD+BPD) may be preferable to sequential single-diagnosis treatment.

8. **Flag prerequisite conditions**: What must be in place before the recommended modality starts? (e.g., medical stabilization, safety contract, adequate distress tolerance, medication trial, literacy or language support).

9. **Run verification.**

## Output Format

```
=== MODALITY SELECTION DECISION AID ===

PRESENTATION SUMMARY
Primary diagnosis: [F##.##] [Descriptor + specifiers]
Comorbid diagnoses: [List, rank-ordered by treatment priority]
Primary treatment target: [The problem that most drives functional impairment]
Key severity anchors: [PHQ-9 = X | GAD-7 = X | PCL-5 = X | other]
Trauma history: [None / Single-incident / Complex-developmental / Processing-ready: Y/N]
Affect dysregulation: [Absent / Mild / Moderate / Severe | self-harm: Y/N]
Prior modalities tried: [Modality — duration — response]
Client factors: [Emotional literacy, distress tolerance, motivation, cultural context]

────────────────────────────────────────────────────────
MODALITY DECISION MATRIX

| Modality | Evidence Grade (primary dx) | Presentation Match | Cautions / Mismatches | Practical Fit |
|----------|----------------------------|--------------------|----------------------|---------------|
| CBT | [A/B/C/D] + brief rationale | [List match factors] | [List cautions] | [Fit rating] |
| DBT | [A/B/C/D] + brief rationale | [List match factors] | [List cautions] | [Fit rating] |
| ACT | [A/B/C/D] + brief rationale | [List match factors] | [List cautions] | [Fit rating] |
| EMDR | [A/B/C/D] + brief rationale | [List match factors] | [List cautions] | [Fit rating] |
| Psychodynamic (PDT/EFT/BRT) | [A/B/C/D] + brief rationale | [List match factors] | [List cautions] | [Fit rating] |
| IFS | [A/B/C/D] + brief rationale | [List match factors] | [List cautions] | [Fit rating] |
| [Other if warranted: CPT / PE / Schema / MI / UP] | [...] | [...] | [...] | [...] |

────────────────────────────────────────────────────────
TRAUMA OVERLAY
[If applicable]
Processing readiness: [Yes / No — rationale]
Recommended trauma sequence: [Stabilization phase modality → Processing modality → Integration modality]
Notes on complex trauma modifications: [...]

AFFECT DYSREGULATION OVERLAY
[If applicable]
Severity: [Mild / Moderate / Severe]
Dysregulation-first decision: [DBT / ACT / IFS / Stabilization-first — rationale]

────────────────────────────────────────────────────────
RANKED RECOMMENDATION

★ FIRST CHOICE: [Modality]
  Evidence rationale: [Primary evidence base — named guideline/meta-analysis]
  Presentation-match rationale: [Why this client's profile fits this modality's theory of change]
  Specific protocol / manual: [Name of treatment manual or structured protocol]
  Expected course: [Approximate session count and frequency from evidence base]
  Prerequisites before starting: [Stabilization required / none]

✦ CLOSE ALTERNATIVE: [Modality]
  Rationale: [Why this is a strong second and when to prefer it over First Choice]
  Specific protocol / manual: [Name]
  Prefer this when: [Condition — e.g., client preference, clinician competency, processing not ready]

◦ CONSIDER IF [CONDITION]: [Modality]
  Rationale: [When this becomes the better option]

✕ INSUFFICIENT EVIDENCE / CAUTION FOR THIS PRESENTATION: [Modality or modalities]
  Rationale: [Brief explanation — not "never use" but "evidence does not support for this profile"]

────────────────────────────────────────────────────────
COMORBIDITY SEQUENCING
[If multiple active diagnoses]
Recommended sequence: [Which diagnosis / problem to address first and why]
Integrated/unified protocol option: [If applicable — e.g., Unified Protocol for emotional disorders]
Notes: [clinician input required: ...]

PREREQUISITE CONDITIONS
- [Condition 1 that must be in place before starting First Choice]
- [Condition 2 — e.g., medical clearance, medication stabilized, literacy/language support]
- [clinician input required: ...]
```

## Verification

- [ ] All six core modalities (CBT, DBT, ACT, EMDR, psychodynamic, IFS) evaluated in the matrix.
- [ ] Evidence grade for each modality is presentation-specific, not modality-general reputation.
- [ ] First Choice has: evidence rationale, presentation-match rationale, specific named protocol, expected course length, prerequisites.
- [ ] Ranked tiers all present: First Choice, Close Alternative(s), Conditional, Insufficient evidence / Caution.
- [ ] Trauma overlay applied if trauma history present; processing readiness assessed.
- [ ] Affect dysregulation overlay applied if severe dysregulation or self-harm present.
- [ ] Comorbidity sequencing addressed if multiple active diagnoses.
- [ ] No modality presented as universally superior; individual variation acknowledged.
- [ ] No fabricated evidence citations; references are approximate descriptions.
- [ ] All clinician-judgment inputs flagged with `[clinician input required]`.
- [ ] Recommendation does not conflate modality with level of care.
