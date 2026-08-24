---
title: "Referral Decision Aid — Within Episode"
category: psychology/treatment-planning
description: "Determine when to refer out for adjunct care (psychiatry, specialist therapy, medical, peer support) while continuing the primary treatment relationship."
techniques:
  - DT-01
  - RT-02
  - QA-04
  - CM-01
  - DS-02
difficulty: intermediate
intended_use: model-testing
tags:
  - referral
  - adjunct-care
  - care-coordination
  - psychiatry
  - treatment-planning
  - within-episode
updated: "2026-06-08"
related_prompts:
  - domain-psychology/treatment-planning/psychology_modality_selection_decision_aid.md
  - domain-psychology/treatment-planning/psychology_stepped_care_decision_aid.md
  - domain-psychology/treatment-planning/psychology_treatment_resistance_reformulation.md
  - domain-psychology/documentation/psychology_initial_treatment_plan.md
---

# Referral Decision Aid — Within Episode

## Objective

Determine whether and to whom the clinician should refer for adjunct services during an active treatment episode, without transferring primary care or severing the therapeutic relationship. The decision aid produces: (1) a referral decision across seven adjunct-care domains, (2) a clinical rationale for each referral or non-referral, (3) a coordination-of-care plan that defines each provider's role and communication protocol, and (4) documentation language for the treatment plan and progress notes.

This prompt addresses mid-episode referrals to supplementary services, not transfer-of-care decisions or level-of-care escalation (see `psychology_stepped_care_decision_aid.md`).

## When to Use

- When a new clinical concern has emerged mid-treatment that is outside the primary clinician's scope of practice or competency.
- When the primary diagnosis requires concurrent medication management that the primary clinician cannot provide.
- When a specialized treatment protocol (e.g., EMDR for a specific trauma, CPT, PE, ERP for OCD, CBT-I, DBT skills group) would augment the primary individual work.
- When physical symptoms suggest a medical evaluation is warranted before or alongside psychological treatment.
- When peer support, community support, or group care would meaningfully supplement individual sessions.
- When a domestic violence, substance use, legal, housing, or financial concern requires a specialized provider or case manager.
- When the clinician is unsure whether a referral is indicated and wants to organize the decision systematically.

## Inputs / Context Required

- **Current treatment status**: diagnosis, current modality, session number, progress summary, outcome measure scores.
- **New or unaddressed clinical concern**: the specific need or gap that is prompting the referral question.
- **Clinician's scope and competency boundaries**: which adjunct services the primary clinician cannot provide.
- **Client's current functioning and capacity**: can the client manage multiple concurrent providers? Is coordination likely to help or overwhelm?
- **Insurance / financial access**: what adjunct services are accessible given the client's coverage and resources.
- **Geographic / telehealth access**: what is realistically available locally or via telehealth.
- **Client's stated preferences**: has the client expressed openness to, or reluctance about, adjunct services?
- `[clinician input required: current medication status and last prescriber contact if psychiatry referral is under consideration]`
- `[clinician input required: any active safety or legal concerns that affect referral urgency or mandatory notification]`

## Constraints

### Must

- Evaluate at minimum seven adjunct-care domains: psychiatric / medication management; specialist psychotherapy; medical / primary care; substance use treatment; peer support / community; case management / social services; group therapy.
- For each domain, produce a clear **Refer / Monitor / Not indicated** decision with a one-sentence rationale.
- For all referrals, specify: urgency (routine / within 2 weeks / urgent within 48–72 hours / emergent), referral type (general vs. specific specialty), communication protocol with the primary clinician, and ROI requirement.
- Define each provider's lane in a brief role-boundary statement to prevent overlap, duplication, or splitting.
- Include a coordination protocol: how and when the primary clinician will communicate with each adjunct provider (written communication frequency, shared documentation, co-case-conference if applicable).
- Include a splitting-risk assessment: for clients with complex trauma, personality pathology, or strong transference reactions, note the specific risk that multiple providers could be played against each other and the mitigation plan.
- Write a treatment-plan addendum paragraph suitable for insertion into the existing plan to document the new referral and its rationale.

### Must Not

- Do not recommend adjunct services the client has no realistic access to without suggesting accessible alternatives.
- Do not refer to a specialty for a concern the primary clinician is competent to address — scope clarity is required.
- Do not frame all concerns as referral-worthy; "Monitor / Not indicated" is a clinical decision that must be documented.
- Do not omit ROI considerations; information sharing with any external provider requires documented informed consent.
- Do not recommend concurrent therapists working in competing theoretical frames without a coordination plan that manages the conflict.
- Do not fabricate referral resources; leave specific provider names blank and use `[clinician input required: identify local or telehealth-accessible referral in this specialty]`.

## Instructions

1. **Summarize the current treatment arc**: State the primary diagnosis, modality, current progress, and the specific gap or new concern that triggered the referral review.

2. **Apply the seven-domain decision matrix**: For each of the seven adjunct-care domains, evaluate:
   - **Is this need present and clinically significant?**
   - **Is it within the primary clinician's scope / competency to address?**
   - **Would an adjunct provider materially improve outcomes?**
   - **Is it accessible to this client?**

   Then assign: **Refer** (with urgency), **Monitor** (no referral now; review at next session), or **Not indicated**.

3. **Write role-boundary statements for each referral**: Define what each provider will and will not do in this episode. Example: "Psychiatric prescriber: evaluate for and manage psychotropic medications; not conducting psychotherapy. Primary clinician retains therapeutic relationship and communicates with prescriber monthly."

4. **Assess splitting risk** (mandatory if personality disorder or complex trauma is in the formulation):
   - Rate splitting risk: High / Moderate / Low.
   - Specify the coordination protocol designed to prevent or manage splitting (e.g., regular case conferences, explicit communication agreement, shared formulation document sent to all providers).

5. **Build the coordination-of-care plan**: For each active provider in the episode (including newly referred), specify:
   - Role
   - Communication method (written note, phone, EHR, secure messaging)
   - Frequency of communication
   - ROI status (current / needs renewal)
   - Who initiates communication after each contact

6. **Set referral urgency for each domain**:
   - **Emergent** (within 24 hours): active suicidal ideation with plan and means, acute psychosis, medical emergency, imminent safety risk.
   - **Urgent** (within 48–72 hours): moderate suicidal ideation without clear plan; new symptoms suggesting medical cause; substance withdrawal concern.
   - **Priority** (within 2 weeks): medication evaluation for new or worsening symptoms; first-episode psychosis stable enough for outpatient initiation; domestic violence safety planning.
   - **Routine** (within 30 days): adjunct group, peer support, specialist modality, case management for ongoing functional needs.

7. **Write the treatment-plan addendum paragraph**: Document the referral decision in language suitable for insertion into the active treatment plan. Include: reason for referral, provider role, communication protocol, and date initiated.

8. **Run verification.**

## Output Format

```
=== REFERRAL DECISION AID — WITHIN EPISODE ===

CURRENT TREATMENT SUMMARY
Primary diagnosis: [F##.##] [Descriptor]
Modality / frequency: [e.g., Individual CBT, weekly]
Session number: [N]     Progress: [Improving / Plateauing / Deteriorating]
Outcome measures: [Instrument = score (baseline = X)]
Gap / new concern prompting referral review: [Specific description]

────────────────────────────────────────────────────────
SEVEN-DOMAIN REFERRAL DECISION MATRIX

| Domain | Decision | Urgency | Rationale |
|--------|----------|---------|-----------|
| 1. Psychiatric / Medication Management | [Refer / Monitor / Not indicated] | [Urgency level] | [1-sentence rationale] |
| 2. Specialist Psychotherapy | [Refer / Monitor / Not indicated] | [Urgency level] | [1-sentence rationale] |
| 3. Medical / Primary Care | [Refer / Monitor / Not indicated] | [Urgency level] | [1-sentence rationale] |
| 4. Substance Use Treatment | [Refer / Monitor / Not indicated] | [Urgency level] | [1-sentence rationale] |
| 5. Peer Support / Community Resource | [Refer / Monitor / Not indicated] | [Urgency level] | [1-sentence rationale] |
| 6. Case Management / Social Services | [Refer / Monitor / Not indicated] | [Urgency level] | [1-sentence rationale] |
| 7. Group Therapy | [Refer / Monitor / Not indicated] | [Urgency level] | [1-sentence rationale] |

────────────────────────────────────────────────────────
ROLE-BOUNDARY STATEMENTS (for each Refer decision)

Domain [#] — [Specialty]:
  Provider role: [What this provider will do in this episode]
  Primary clinician retains: [What the primary clinician continues to own]
  Exclusion: [What this provider will NOT do — prevents overlap or splitting]

Domain [#] — [Specialty]:
  [same structure]

────────────────────────────────────────────────────────
SPLITTING RISK ASSESSMENT

Risk level: [High / Moderate / Low]
Rationale: [Brief — why this client / formulation presents splitting risk or not]

If High or Moderate:
  Coordination protocol: [Specific plan — e.g., "Monthly case conference; shared formulation
  document sent to all providers at treatment initiation and updated at 90-day reviews;
  explicit 'no triangulation' agreement in consent forms."]
  Early signs of splitting to monitor: [e.g., "Client reports one provider said X that contradicts
  another provider's guidance; idealization/devaluation shifts across providers."]

────────────────────────────────────────────────────────
COORDINATION-OF-CARE PLAN

| Provider | Role | Communication Method | Frequency | ROI Status | Who Initiates |
|----------|------|---------------------|-----------|------------|---------------|
| Primary clinician | [Role] | — | — | — | — |
| [Referral 1] | [Role] | [Written / phone / EHR] | [Monthly / as needed] | [Current / Needed] | [Primary clinician / mutual] |
| [Referral 2] | [Role] | [...] | [...] | [...] | [...] |
| [PCP / other existing] | [Role] | [...] | [...] | [...] | [...] |

[clinician input required: ROI forms needed before information sharing with any new provider]

────────────────────────────────────────────────────────
REFERRAL URGENCY SUMMARY

Emergent (today / 24 hrs): [None / Specify]
Urgent (48–72 hours): [None / Specify]
Priority (within 2 weeks): [None / Specify]
Routine (within 30 days): [List domains where referral is indicated]

────────────────────────────────────────────────────────
TREATMENT-PLAN ADDENDUM

[Paragraph for insertion into active treatment plan:]
"Effective [YYYY-MM-DD], the following adjunct referral(s) have been initiated: [Domain — Provider role
— rationale in clinical language]. The primary therapeutic relationship and treatment goals remain
unchanged. Communication protocol: [Brief description]. ROI for information sharing: [obtained /
pending / not required]. Role boundaries have been clarified with [provider(s)] to prevent
duplication and support coordination."
```

## Verification

- [ ] All seven adjunct-care domains evaluated with an explicit decision (Refer / Monitor / Not indicated).
- [ ] Each referral includes urgency classification; emergent and urgent referrals do not default to "routine."
- [ ] Role-boundary statement present for each Refer decision.
- [ ] Splitting risk assessed; coordination protocol specified if High or Moderate.
- [ ] Coordination-of-care plan completed for all active and newly referred providers.
- [ ] ROI status documented for all providers with whom information will be shared.
- [ ] Treatment-plan addendum paragraph drafted in chartable language.
- [ ] Referrals not recommended for concerns the primary clinician is competent to address.
- [ ] Access and feasibility considered; inaccessible referrals flagged with accessible alternatives.
- [ ] Client preference documented or flagged as requiring discussion.
- [ ] Nothing fabricated; specific provider names left blank with `[clinician input required]`.
