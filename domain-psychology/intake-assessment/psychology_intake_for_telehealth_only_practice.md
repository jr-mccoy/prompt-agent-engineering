---
title: "Telehealth-Only Practice Intake Protocol"
category: psychology/intake-assessment
description: "Structured intake protocol for practices delivering care exclusively via telehealth, covering location attestation, platform verification, interstate licensure, safety and escalation planning, technology-fail contingency, and documentation requirements specific to synchronous audio-video encounters."
techniques:
  - ST-04
  - DT-02
  - CM-01
  - CM-02
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - telehealth
  - intake
  - location-attestation
  - interstate-licensure
  - escalation-plan
  - cpt-90791
  - cpt-90792
  - pos-10
  - modifier-95
updated: "2026-06-08"
related_prompts:
  - domain-psychology/documentation/psychology_intake_assessment_note.md
  - domain-psychology/documentation/psychology_telehealth_session_note.md
  - domain-psychology/intake-assessment/psychology_re_intake_after_lapse_protocol.md
  - domain-psychology/risk-crisis/psychology_crisis_de_escalation_session_plan.md
---

# Telehealth-Only Practice Intake Protocol

## Objective

Produce a complete intake record for a practice that delivers care exclusively or primarily via synchronous audio-video telehealth that:

1. Verifies and documents the client's physical location at the time of the encounter (state-level and street address) for licensure compliance.
2. Confirms the clinician holds an active license or compact privilege in the client's state of physical location.
3. Establishes a individualized safety and escalation plan before or during the initial encounter — including local emergency contacts, nearest emergency department, and a technology-fail protocol.
4. Documents platform standards (HIPAA-compliant video, audio backup) and verifiable client identity.
5. Screens for presentations that exceed telehealth safety thresholds and require in-person referral or co-located backup.
6. Produces a telehealth-adapted biopsychosocial intake note meeting CPT 90791 / 90792 documentation requirements with POS 10 (Telehealth Provided in Patient's Home) and modifier 95 (Synchronous Telemedicine Service).

## When to Use

- At intake for any client being onboarded into a telehealth-only or telehealth-primary outpatient practice.
- When a client who was previously seen in-person transitions to telehealth-only care and requires a telehealth-specific intake or re-consent.
- When a client presents from a state different from their state of record, requiring fresh licensure attestation.
- When the practice operates under a state telehealth compact (PSYPACT, LCSW Compact, or similar) and must document compact authority.

## Inputs / Context Required

- **Client demographics:** Name, date of birth, physical address at time of this encounter, email, phone.
- **Clinician licensure:** Active license numbers, states licensed, compact memberships (PSYPACT authority to practice interjurisdictional telepsychology — ATP, or equivalent).
- **Platform used:** HIPAA-compliant video platform name, backup audio line (phone number or secondary platform).
- **Chief complaint and referral reason:** What the client is seeking; who referred.
- **Prior mental health records:** Available, requested, or unavailable.
- **Emergency contacts:** At least one emergency contact with name, relationship, phone.
- **Client's nearest emergency department:** Name and address — collected before or at the start of the encounter.
- **Insurance and billing authorization:** Payer, telehealth coverage confirmed (parity state or verified), preauthorization if required.
- **Screening instruments completed:** PHQ-9, GAD-7, and any other measures administered before or during intake.

## Constraints

### Must

- Document the client's physical location (state + street address or city/county at minimum) at the time of each encounter — this is required for licensure compliance and billing.
- Confirm clinician licensure authority for the client's state before the encounter proceeds; if not licensed in the client's state, halt and refer — document the referral.
- Complete the Safety and Escalation Plan before any clinical assessment begins or within the first 15 minutes of the encounter; do not defer this to a future session.
- Verify client identity at the start of the encounter (government-issued ID viewed via video, or identity verification policy applied per practice standard).
- Screen explicitly for presentations that exceed telehealth safety thresholds and document the screening result and clinical rationale for proceeding or referring.
- Document technology-fail contingency: if audio-video connection drops, the plan for how the encounter continues (phone, reschedule, or escalate if mid-crisis).
- Obtain and document telehealth-specific informed consent separate from general consent — covering limits of confidentiality unique to telehealth, technology risks, location privacy, and recording policy.
- Note wherever MSE is adapted or limited by the telehealth medium (e.g., "gait could not be assessed"; "fine motor and grooming partially observable via video").
- Flag gaps with `[clinician input required: ...]`.

### Must Not

- Do not proceed with the clinical intake if licensure in the client's state cannot be confirmed — refer immediately.
- Do not use audio-only (phone) as the sole modality for an initial intake without documenting explicit clinical and regulatory rationale; POS 10 + modifier 95 requires synchronous audio-video.
- Do not defer the Safety and Escalation Plan to "later in treatment" — it is a precondition of telehealth intake.
- Do not fabricate licensure authority, license numbers, compact privileges, or emergency resources — flag all as `[clinician input required]`.
- Do not treat telehealth as equivalent to in-person when documenting MSE domains that are genuinely limited by the medium.
- Do not present clinician estimates as instrument scores; administer or collect instruments before documenting results.

## Instructions

1. **Open the encounter with identity verification and location attestation.** Confirm the client's name and DOB against the chart. Ask the client to confirm their current physical location (state + address) on video. Document exactly.

2. **Verify clinician licensure authority.** Confirm the clinician holds an active license or compact privilege (e.g., PSYPACT ATP) in the client's state of physical location. If yes, document license number and authority type. If no, halt — provide referral and document.

3. **Confirm platform and identity.** Verify the HIPAA-compliant video platform is in use. Have the client show government-issued ID via camera (or apply practice's identity verification protocol). Document.

4. **Obtain telehealth-specific informed consent.** Confirm the client has received, reviewed, and signed the telehealth consent form (or obtain verbal consent documented per practice policy). Note key elements covered: technology risks, location privacy, recording policy, limits of confidentiality, emergency procedures.

5. **Complete the Safety and Escalation Plan.** Collect and document: (a) nearest emergency department — name and address; (b) local emergency services — 911 confirmed reachable; (c) emergency contact name, relationship, phone; (d) technology-fail protocol — what happens if connection drops; (e) explicit agreement on how client will access emergency services if clinician loses contact during a crisis.

6. **Screen for telehealth safety thresholds.** Determine whether the client's presentation is appropriate for telehealth-only care using the criteria below. Document the screening result and clinical rationale.

7. **Conduct the biopsychosocial intake.** Follow the standard intake domains, noting MSE adaptations for telehealth. Administer or review screening instruments.

8. **Write the Telehealth Intake Note** using the output format below.

9. **Run verification.**

## Telehealth Safety Threshold Screening

The following presentations warrant in-person evaluation or co-located clinical backup rather than telehealth-only intake. Document each as PRESENT / ABSENT / UNCLEAR and provide clinical rationale for the disposition.

| Threshold Criterion | Screen Result | Disposition |
|---------------------|---------------|-------------|
| Active suicidal ideation with plan or intent | [PRESENT / ABSENT / UNCLEAR] | If present → in-person or ED referral; telehealth intake contraindicated |
| Active homicidal ideation with identified target | [PRESENT / ABSENT / UNCLEAR] | If present → in-person, ED, or duty-to-protect protocol |
| Active psychosis with command hallucinations or disorganized behavior | [PRESENT / ABSENT / UNCLEAR] | If present → in-person or higher level of care |
| Active alcohol or substance withdrawal with autonomic instability | [PRESENT / ABSENT / UNCLEAR] | If present → ED referral; CIWA-Ar cannot be adequately assessed via telehealth |
| Moderate–severe eating disorder with medical instability | [PRESENT / ABSENT / UNCLEAR] | If present → medical and in-person coordination required |
| Client in unsafe environment (DV, human trafficking, unable to speak privately) | [PRESENT / ABSENT / UNCLEAR] | If present → safety planning required before proceeding; may need to defer |
| Unable to consent or participate meaningfully (cognitive, acute intoxication) | [PRESENT / ABSENT / UNCLEAR] | If present → defer intake; refer to appropriate level of care |

Overall telehealth appropriateness: [Appropriate for telehealth intake / Requires in-person evaluation — see disposition above]
Clinical rationale: [clinician input required]

## Output Format

```
=== TELEHEALTH INTAKE NOTE ===

Client: [Initials/MRN]    Date of Service: [YYYY-MM-DD]    Time: [HH:MM–HH:MM]
Clinician: [Name, credentials, license #]

Platform: [HIPAA-compliant video platform name]
Backup modality: [Phone number / secondary platform]
Place of Service: POS 10 (Telehealth Provided in Patient's Home)
Billing modifier: 95 (Synchronous Telemedicine Service)

─────────────────────────────────────────
LOCATION ATTESTATION AND LICENSURE
─────────────────────────────────────────
Client physical location at time of encounter:
  State: [State]
  City / Address: [City, or street address per practice policy]
  Client self-reported: [Yes — stated on video]

Clinician licensure authority for client's state:
  License type: [In-state license / Compact privilege — specify compact (e.g., PSYPACT ATP)]
  License / Authority number: [clinician input required]
  Expiration date: [YYYY-MM-DD]
  Licensure confirmed: [Yes / No — if No: intake halted; referral provided to: ...]

─────────────────────────────────────────
IDENTITY VERIFICATION
─────────────────────────────────────────
Method used: [Government-issued ID viewed via video / Practice alternative protocol — describe]
Identity confirmed: [Yes / No]
Client name confirmed: [Yes]    DOB confirmed: [Yes]

─────────────────────────────────────────
TELEHEALTH INFORMED CONSENT
─────────────────────────────────────────
Consent form provided: [Yes — date sent / date signed: YYYY-MM-DD]
Verbal consent obtained and documented: [Yes / No — if verbal, document: clinician attests client verbally agreed on video MM/DD/YYYY]
Key elements reviewed with client:
  Technology risks (connection failure, data interception): [Confirmed reviewed]
  Location privacy (third parties in client's environment): [Confirmed reviewed]
  Recording policy: [No recording / Recording requires written consent — policy confirmed]
  Limits of confidentiality unique to telehealth: [Confirmed reviewed]
  Emergency procedures if clinician loses contact: [Confirmed reviewed]

─────────────────────────────────────────
SAFETY AND ESCALATION PLAN
─────────────────────────────────────────
[This section must be completed before or within the first 15 minutes of the encounter.]

Client's nearest emergency department:
  Name: [clinician input required]
  Address: [clinician input required]

Local emergency services: 911 confirmed reachable from client's location: [Yes / No — if No: document alternative]

Emergency contact:
  Name: [clinician input required]    Relationship: [clinician input required]
  Phone: [clinician input required]
  Authorized to contact in crisis: [Yes — per ROI / Yes — per verbal agreement documented here]

Technology-fail protocol:
  If audio-video drops mid-session: [Client will call clinician at: (phone number) / Clinician will call client at: (phone number) within (X) minutes]
  If connection cannot be restored: [Session concluded; clinician will attempt contact by phone; escalate to emergency contact if client is in distress]
  If connection drops during active crisis: [Clinician will call client's phone immediately; if no answer within (X) minutes, clinician will call 911 and provide client's physical address]

Crisis agreement documented:
  Client understands how to access emergency services (911, nearest ED) without clinician contact: [Yes — confirmed on video]
  988 Suicide and Crisis Lifeline provided: [Yes / Not indicated at this time]

Telehealth Safety Threshold Screening result: [Appropriate for telehealth intake / Referral required — see clinical rationale in Threshold Screening section]

─────────────────────────────────────────
IDENTIFYING INFORMATION
─────────────────────────────────────────
Name: [Initials]    DOB: [YYYY-MM-DD]    Age: [N]    Gender identity: [...]
Pronouns: [...]    Primary language: [...]    Interpreter needed: [Yes / No]
Living situation: [Alone / With (relationship) / Other]
Employment / school status: [...]
Referral source: [...]

─────────────────────────────────────────
CHIEF COMPLAINT
─────────────────────────────────────────
In client's words: "[...]"
Presenting concern(s): [...]
Duration and onset: [...]
Precipitating or proximal stressors: [...]

─────────────────────────────────────────
HISTORY OF PRESENTING ILLNESS
─────────────────────────────────────────
[Narrative: symptom onset and timeline, prior episode history relevant to current episode, treatment-seeking trajectory, what has changed prompting this intake. For telehealth-specific intake: include how the client came to seek telehealth specifically — prior in-person treatment, geographic access barriers, scheduling, preference, provider availability.]

─────────────────────────────────────────
PSYCHIATRIC HISTORY SUMMARY
─────────────────────────────────────────
Prior diagnoses: [List with approximate onset dates]
Prior outpatient treatment: [Providers, modalities, approximate dates, response — from client self-report or records]
Prior psychiatric hospitalizations: [Voluntary / involuntary; dates; reasons — or None reported]
Prior medication trials: [List; see full Psychiatric History if compiled separately]
Prior suicide attempts or self-harm history: [Yes — describe / No]

─────────────────────────────────────────
SUBSTANCE USE HISTORY SUMMARY
─────────────────────────────────────────
[Summary; see full Substance Use History module if compiled separately]
Current alcohol use: [Frequency, quantity, AUDIT-C if administered: score X/12]
Current substance use: [Substance, frequency, quantity]
Prior SUD treatment: [Yes — describe / No]
Withdrawal risk: [None identified / Low / Moderate — clinical rationale / High — in-person required]

─────────────────────────────────────────
MEDICAL HISTORY SUMMARY
─────────────────────────────────────────
Active medical conditions: [List]
Current medications (all): [List with dose, frequency, prescriber]
Known allergies or adverse drug reactions: [List / None reported]
Primary care provider: [Name / None — unestablished]
Last physical exam: [Date / Unknown]
Medical clearance obtained or pending: [clinician input required]

─────────────────────────────────────────
SOCIAL AND FAMILY HISTORY
─────────────────────────────────────────
Social supports: [...]
Relationship status and living arrangement: [...]
Cultural background and relevant identity factors: [...]
Family psychiatric history: [...]
Current stressors: [...]
Strengths and protective factors: [...]

─────────────────────────────────────────
MENTAL STATUS EXAMINATION (TELEHEALTH-ADAPTED)
─────────────────────────────────────────
[Note: MSE conducted via synchronous audio-video. Domains limited by the medium are flagged.]

Appearance: [Dress, grooming, hygiene as observable via video; note: "full body posture and gait not assessed via video"]
Behavior: [Cooperation, eye contact with camera, psychomotor activity as observable; note limitations]
Speech: [Rate, rhythm, volume, latency, articulation — assessed via audio; note: "volume assessment affected by client microphone/speaker setup if applicable"]
Mood: [Client-reported — quote directly]
Affect: [Range: ___; Intensity: ___; Quality: ___; Congruence with mood: ___]
Thought process: [...]
Thought content: [SI: [present / absent — current ideation, plan, intent, access to means]; HI: [present / absent]; Delusions: [present — describe / absent]; Obsessions: [present — describe / absent]; Other: [...]]
Perceptual disturbances: [Hallucinations: [present — describe / absent]; Illusions: [present / absent]]
Cognition: [Orientation x4 confirmed; Concentration as observed; Memory limitations noted; Formal cognitive screen: [not administered / MMSE / MoCA — score X if administered — note: validated in-person; telehealth adaptation limitations apply]]
Insight: [Good / Fair / Poor]
Judgment: [Good / Fair / Poor]
Reliability of historian: [Good / Fair / Limited — rationale]

Note on telehealth MSE limitations: [List any domains where the telehealth medium limited assessment — e.g., "Fine motor coordination, gait, and body habitus below the waist not directly observed. Affect intensity assessment may be influenced by video compression and lighting. Client's home environment visible — note: [describe relevant environmental observations or None notable]."]

─────────────────────────────────────────
SCREENING INSTRUMENTS
─────────────────────────────────────────
[Document instrument, administration method, date, and score. Note whether administered prior to session (patient portal / e-intake) or during session via screen share or verbal administration.]

PHQ-9: [Score: X/27; Severity band: ___; Item 9 (SI screen): [0/1/2/3]; Date: YYYY-MM-DD; Method: [e-intake / in-session]]
GAD-7: [Score: X/21; Severity band: ___; Date: YYYY-MM-DD; Method: [...]]
[Other instruments as applicable: PCL-5, AUDIT, DAST-10, MDQ, etc.]

─────────────────────────────────────────
RISK ASSESSMENT SUMMARY
─────────────────────────────────────────
[See C-SSRS or full risk assessment if compiled separately. Required at every intake regardless of presenting concern.]
Current suicidal ideation: [Present / Absent]
Current homicidal ideation: [Present / Absent]
Current self-harm: [Present / Absent]
Risk level: [Low / Moderate / High — clinical rationale]
Protective factors: [...]
Risk mitigation: [Safety plan location — see Safety and Escalation Plan above / Additional safety planning: ...]

Telehealth-specific risk consideration: [Does the client's risk profile require in-person or higher level of care? Yes — referral initiated / No — telehealth appropriate with safety plan in place]

─────────────────────────────────────────
DIAGNOSTIC IMPRESSIONS
─────────────────────────────────────────
Primary: [DSM-5-TR diagnosis] [ICD-10-CM code]
Secondary: [DSM-5-TR diagnosis] [ICD-10-CM code]
Rule out: [...]
Deferred: [...]
Principal concern(s) guiding treatment: [...]

─────────────────────────────────────────
FIVE-P FORMULATION SUMMARY
─────────────────────────────────────────
Predisposing: [...]
Precipitating: [...]
Perpetuating: [...]
Protective: [...]
Presenting: [...]

─────────────────────────────────────────
TREATMENT RECOMMENDATIONS
─────────────────────────────────────────
Level of care: [Telehealth outpatient — individual / group / both]
Frequency: [Weekly / Biweekly / Other]
Modality fit: [Rationale for telehealth as appropriate modality for this client, diagnosis, and goals]
Referrals: [Psychiatry / PCP / Specialist / None at this time]
Barriers to telehealth participation identified: [Technology access / Quiet private space / Time zone / Other / None identified]
Plan to address barriers: [...]

─────────────────────────────────────────
TELEHEALTH TECHNOLOGY AND ENVIRONMENT
─────────────────────────────────────────
Client's technology: [Laptop / Desktop / Tablet / Phone — client-reported]
Connection quality during this encounter: [Good / Fair / Poor — describe any interruptions]
Client privacy during this encounter: [Client confirmed private space / Third party visible — note: [describe]; session adapted by: [...]]
Clinician location: [Clinician's licensed office / Other — describe]

─────────────────────────────────────────
BILLING NOTE
─────────────────────────────────────────
CPT: [90791 (Psychiatric Diagnostic Evaluation) | 90792 (with medical services)]
Place of Service: POS 10 (Telehealth Provided in Patient's Home)
Modifier: 95 (Synchronous Telemedicine Service)
Duration: [N minutes]
Payer telehealth coverage confirmed: [Yes — parity state / Yes — verified with payer / No — self-pay / Pending]
Preauthorization: [Not required / Obtained — auth #: ___ / Pending]
Note: POS 10 is appropriate when the patient is in their home. If client is not in their home (e.g., in a telehealth-equipped clinic site), POS 02 applies. Confirm POS with billing team if client location varies.
```

## Verification

- [ ] Client physical location (state + address or city) documented at time of encounter.
- [ ] Clinician licensure authority for client's state confirmed and documented with license/compact number.
- [ ] If licensure not confirmed: intake halted and referral documented.
- [ ] Identity verification method documented and identity confirmed.
- [ ] Telehealth-specific informed consent documented (signed form date or verbal attestation).
- [ ] Safety and Escalation Plan completed: nearest ED, emergency contact, 911 confirmation, technology-fail protocol, crisis agreement.
- [ ] Telehealth Safety Threshold Screening documented for each criterion (PRESENT / ABSENT / UNCLEAR) with disposition.
- [ ] MSE notes telehealth-medium limitations explicitly; no domain left blank or marked "WNL" without behavioral anchor.
- [ ] Thought Content explicitly addresses SI and HI (present or absent).
- [ ] Risk assessment completed and telehealth-specific risk disposition documented.
- [ ] Diagnostic impressions include ICD-10-CM codes.
- [ ] Billing section documents CPT, POS 10, modifier 95, and payer coverage confirmation.
- [ ] Gaps flagged with `[clinician input required: ...]`.
- [ ] No fabricated license numbers, emergency resources, or instrument scores.
