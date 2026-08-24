---
title: "Telehealth Session Progress Note Drafter"
category: psychology/documentation
description: "Draft a telehealth-specific psychotherapy progress note covering location attestation, identity verification, environment/privacy adequacy, technology functioning, telehealth modifier/POS, and standard clinical content."
techniques:
  - ST-04
  - DT-02
  - QA-04
  - CM-02
difficulty: intermediate
tags:
  - telehealth
  - place-of-service
  - modifier-93
  - modifier-95
  - state-of-licensure
  - audio-only
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/documentation/psychology_soap_progress_note.md
  - domain-psychology/documentation/psychology_dap_progress_note.md
  - domain-psychology/practice-operations
---

# Telehealth Session Progress Note Drafter

## Objective

Produce a telehealth-specific psychotherapy progress note layered on top of a base format (SOAP / DAP / BIRP / GIRP / PIRP). The note must:

1. Document location of clinician and client at time of service, including state.
2. Document identity verification (especially first encounter or address change).
3. Document environment / privacy adequacy on both sides.
4. Document technology platform, audio/video status, and any disruptions.
5. Document telehealth-specific consent reaffirmation when required.
6. Use the correct **Place of Service (POS)** code and **modifier** (95 for synchronous video, 93 for audio-only where allowed) so the claim is payable.
7. Include all standard clinical content from the chosen base format.

## When to Use

- Any synchronous telehealth session: video, audio-only, or video with audio fallback.
- Telehealth-specific elements are required regardless of the base note format the clinician uses.
- Useful when an EHR doesn't auto-populate telehealth fields.

## Inputs / Context

- Base format selected (SOAP / DAP / BIRP / GIRP / PIRP).
- Session metadata: date, start/stop time, duration.
- Clinician location (full address or city + state); state of licensure used for this session.
- Client location at time of service (full address or city + state); attest that client is in a state where clinician is licensed (or a state with a temporary practice exception).
- Modality: synchronous video / audio-only / video with brief audio-only fallback.
- Platform name (HIPAA-compliant; document platform).
- Identity verification method (visual recognition, ID check, knowledge-based).
- Client environment and privacy attestation (alone, on headphones, who else is in the home, ability to speak freely).
- Clinician environment and privacy attestation.
- Technology disruptions (drop-outs, video off, audio static, reconnects); whether they materially affected care.
- Telehealth consent on file: signed-on date, scope, and whether reaffirmed today (especially after pause in care or modality change).
- Emergency contact and current local emergency-services number for client's location.
- Standard clinical content (per base format).

## Constraints

### Must

- Output a header **Telehealth Attestations** block before the chosen base-format note body.
- Telehealth Attestations include: clinician location + state of licensure; client location + state attested by client; identity verification method; consent on file (date) and reaffirmed-today status; platform; modality; audio/video status; disruptions; environment / privacy attestation both sides; emergency-services number for client's location; client's identified emergency contact.
- Use correct POS: **POS 10** for telehealth provided in patient's home, **POS 02** for telehealth provided other than in patient's home (per current Medicare rules).
- Use correct modifier: **95** for synchronous audiovisual; **93** for audio-only when payer allows; document audio-only justification when used.
- Include all elements of the chosen base format below the attestations.
- Explicitly document that the clinician confirmed client is in a state where clinician holds licensure (or temporary practice authority).
- Document plan for managing acute risk remotely (local emergency services, identified support person, ability to dispatch).

### Must Not

- Do not bill telehealth without the correct POS and modifier; correct documentation must support the claim.
- Do not use audio-only if the payer does not allow it; document medical necessity for audio-only when used (lack of broadband, accessibility, client preference with rationale).
- Do not skip identity verification on first encounter or after address change.
- Do not skip a client location attestation; "client at home" is insufficient — state matters for licensure.
- Do not fabricate; flag missing items.

## Instructions

1. Compile the Telehealth Attestations block.
2. Document POS, modifier, and audio-only justification if relevant.
3. Document risk-management plan specific to remote setting (local 911, identified support person at the client's location, ability/willingness to dispatch crisis services to client's address if needed).
4. Use the chosen base format (SOAP / DAP / BIRP / GIRP / PIRP) for the clinical body.
5. In Plan, note any telehealth-specific elements (e.g., next session in-person if rapport / risk requires).
6. Run verification.

## Output Format

```
=== TELEHEALTH SESSION PROGRESS NOTE ===

TELEHEALTH ATTESTATIONS
Date: [YYYY-MM-DD]    Time In/Out: [HH:MM–HH:MM]    Duration: [N min]
Base note format: [SOAP / DAP / BIRP / GIRP / PIRP]

Clinician location: [Address or city + state]
State of licensure used today: [State] (license #: [...])

Client location: [Address or city + state, as attested by client]
State of licensure: [State] is one in which clinician holds [active license / temporary practice authority / interjurisdictional compact (e.g., PSYPACT)]: [Yes / No — if No, document basis].

Modality: [Synchronous audiovisual / Audio-only / Audio-only with brief video fallback]
Audio-only justification (if applicable): [Lack of broadband / Accessibility / Client preference with rationale / Other]
Platform: [HIPAA-compliant platform name]
Audio status: [Working / Intermittent / Failed]
Video status: [Working / Intermittent / Off — with reason]
Disruptions: [None / Brief drop-outs at HH:MM, reconnect duration N sec, no material impact / Material impact: ...]

Identity verification: [Visual recognition (continuing client) / Photo ID check / Knowledge-based / Other]
Telehealth consent on file: signed [YYYY-MM-DD]    Reaffirmed today: [Yes / No / Not required — first session was today]

Environment / privacy:
- Clinician side: [Private office / home office, door closed, no overheard conversation possible.]
- Client side: [Client attests to being alone / with [identified person, role], headphones, able to speak freely / privacy concerns noted: ...]

Emergency-services number for client's current location: [911 / local equivalent]
Client's emergency contact: [Name, relationship, phone, on file: Yes / No]
Client's nearest ED: [Name, address — known to clinician]

Risk-management plan for remote setting: [Local 911 ready to dispatch if needed; identified support person at location is [name, relationship]; client agrees to remain on line until safety established if acute crisis emerges; client agreed [Yes / No].]

POS: [10 (patient's home) / 02 (other than home)]    Modifier: [95 / 93]
CPT: [...]    ICD-10: [...]    Treatment-plan goals: [Goal #X, #Y]

═══════════════════════════════════════════════════════════
[BASE-FORMAT NOTE BODY — exactly as specified by the chosen format. Include all required sections (e.g., for SOAP: Subjective / Objective / Assessment / Plan; for BIRP: Behavior / Intervention / Response / Plan; etc.).]
═══════════════════════════════════════════════════════════

BILLING
CPT [#####] x 1, [N] minutes face-to-face. POS [10 / 02], Modifier [95 / 93].
Medical necessity: [one-sentence justification].

Clinician: [name, credentials, license #, signature, date/time]
```

## Verification

- [ ] Telehealth Attestations block present before base-format body.
- [ ] Clinician location AND state of licensure used today documented.
- [ ] Client location AND attestation that clinician is licensed in that state (or has compact / temporary authority) documented.
- [ ] Identity verification method documented.
- [ ] Telehealth consent date documented and "reaffirmed today" status explicit.
- [ ] Platform, audio/video status, disruptions documented.
- [ ] Audio-only sessions include payer-eligible justification.
- [ ] Environment / privacy attestation for both sides.
- [ ] Emergency-services number, emergency contact, and nearest ED documented.
- [ ] Risk-management plan for remote setting present (especially if any risk indicators).
- [ ] POS (10 vs 02) and modifier (95 vs 93) correctly chosen.
- [ ] All required elements of the chosen base format are present in the body.
- [ ] Gaps flagged; nothing fabricated.
