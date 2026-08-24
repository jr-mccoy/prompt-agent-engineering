---
title: "Telemental Health Program Design"
category: psychology/digital-practice
description: "Design a tele-mental-health program covering modality selection, HIPAA-compliant platform requirements, clinical-appropriateness screening, telehealth informed consent, per-location emergency protocols, and PSYPACT licensure compliance."
techniques:
  - NE-02
  - DT-01
  - CM-02
  - ST-04
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - telehealth
  - telemental-health
  - PSYPACT
  - HIPAA
  - informed-consent
  - APA-telepractice
  - ATA-guidelines
  - digital-practice
updated: "2026-06-08"
related_prompts:
  - domain-psychology/practice-operations/psychology_telehealth_state_of_licensure_decision_aid.md
  - domain-psychology/documentation/psychology_telehealth_session_note.md
  - domain-psychology/risk-crisis/psychology_crisis_de_escalation_session_plan.md
  - domain-psychology/digital-practice/psychology_async_messaging_therapy_protocol.md
---

# Telemental Health Program Design

## Objective

Produce a structured tele-mental-health (TMH) program design that specifies: (1) which telehealth modalities the practice will offer and the clinical rationale for each, (2) the technology and platform requirements that satisfy HIPAA and the ATA/APA telepractice standards, (3) the clinical-appropriateness screening that determines who is and is not suitable for telehealth, (4) telehealth-specific informed consent, (5) a per-client-location emergency and safety protocol, (6) licensure and PSYPACT compliance at the point of service, and (7) documentation and equity considerations. The design implements APA Guidelines for the Practice of Telepsychology and the American Telemedicine Association (ATA) best-practice framework. A licensed clinician retains all clinical decision authority; the program defines the operating envelope, not the clinical judgment within it.

## When to Use

- When a practice or clinic is launching telehealth services for the first time and needs a defensible operating framework.
- When an existing telehealth offering grew ad hoc during a public-health emergency and now needs to be formalized for ongoing compliant operation.
- When a multi-state group practice must reconcile telehealth delivery with PSYPACT and counseling-compact obligations.
- When credentialing, accreditation, or a payer audit requires a documented telehealth program with screening and safety protocols.
- When adding a new modality (e.g., phone-only or asynchronous) to an existing synchronous video program.

## Inputs / Context Required

- **Disciplines and licenses in the practice**: psychologists, LCSWs, LPCs, LMFTs, psychiatric prescribers — and the states/jurisdictions in which each is licensed.
- **PSYPACT / compact status**: whether clinicians hold an Authority to Practice Interjurisdictional Telepsychology (APIT) / E.Passport, or Counseling Compact privilege, and which states are members.
- **Client populations served**: presenting problems, typical acuity, age ranges, languages, and any high-risk populations (active suicidality, eating disorders, psychosis, SUD).
- **Geographic footprint**: the states/jurisdictions where clients are physically located at the time of service.
- **Existing technology**: current EHR, video platform, scheduling, and whether Business Associate Agreements (BAAs) are in place.
- **Payer mix**: which payers are reimbursed for telehealth and any modality restrictions (e.g., audio-only coverage limits).
- `[clinician input required: the practice's risk tolerance for serving higher-acuity clients via telehealth and any categorical exclusions the clinical director sets]`
- `[clinician input required: languages and accessibility accommodations the program must support]`

## Constraints

### Must

- Specify each offered modality (synchronous two-way video, audio-only/telephone, asynchronous messaging) with explicit clinical indications and contraindications for each.
- Require a HIPAA-compliant platform with a signed BAA, end-to-end or transport encryption, access controls, and audit logging; name these as non-negotiable platform requirements.
- Include a clinical-appropriateness screen applied before and during telehealth that evaluates acuity, diagnosis, home environment (privacy, safety, presence of others), technology access/literacy, and the client's stated preference.
- Define telehealth-specific informed consent that covers modality limitations, privacy/technology risks, what happens during a technology failure, and the emergency protocol.
- Require verification of the client's physical location at the start of every session (location attestation), because the client's location at the time of service governs which jurisdiction's licensure law applies.
- Specify a per-location emergency protocol: at minimum, the client's current physical address, a local emergency contact, the nearest emergency department, and local crisis resources — collected and updated each session.
- State the risk-escalation pathway explicitly: clinician-this-week / clinician-today / 988 Suicide and Crisis Lifeline / call 911 or go to nearest ED — and tie each tier to a triggering signal.
- Address licensure: the clinician must be licensed (or hold PSYPACT/compact authority) in the jurisdiction where the client is physically located at the time of service.
- Include equity/digital-divide considerations: a fallback plan (audio-only, community access points, device/data assistance) when a client lacks reliable video access.
- Reference correct telehealth claim elements: Place of Service (POS) 02 for telehealth provided other than in the patient's home, POS 10 for telehealth provided in the patient's home, and modifier 95 (synchronous audio-video) or 93 (audio-only), subject to current payer rules.

### Must Not

- Do not present telehealth as universally appropriate; do not omit the contraindication/exclusion logic.
- Do not rely on a consumer videoconferencing tool without a BAA as if it were compliant.
- Do not treat the clinician's licensure state as the governing jurisdiction; the client's physical location at the time of service governs.
- Do not design an emergency protocol that depends on the clinician's local resources rather than resources local to the client.
- Do not position any automated or platform feature (e.g., self-scheduling, chatbot intake) as making clinical decisions; the licensed clinician retains decision authority.
- Do not fabricate specific state statutes, PSYPACT member-state lists, or payer policies; mark jurisdiction- and payer-specific facts as `[verify current ___]`.

## Instructions

1. **Map modalities to clinical indications.** For each modality the practice will offer, state its best-fit use and its contraindications, using the reference table as the anchor.

   | Modality | Strong fit | Weak fit / contraindicated | Key requirement |
   |----------|-----------|----------------------------|-----------------|
   | Synchronous video | Most outpatient therapy; assessment requiring visual cues | Active high-acuity crisis; environments lacking privacy | HIPAA platform + BAA; verified bandwidth |
   | Audio-only / telephone | Continuity when video fails; rural/low-bandwidth; client preference | Initial risk assessment where visual data matters; some payers exclude | Modifier 93; confirm payer coverage |
   | Asynchronous messaging | Skills coaching, between-session support, psychoeducation | Crisis, acute risk, time-sensitive clinical change | Defined response SLA; NOT for emergencies (see sibling protocol) |
   | In-person fallback | High acuity; safety concerns; assessment needs | — | Referral pathway local to client |

2. **Specify platform and technology requirements.** Require: signed BAA with the platform vendor; encryption in transit (and at rest where applicable); unique user authentication and role-based access; audit logging; a documented downtime/technology-failure procedure; and a tested backup channel (e.g., move to phone). List minimum bandwidth guidance and a pre-session tech check.

3. **Build the clinical-appropriateness screen.** Define a pre-enrollment and ongoing screen across five domains: (a) **acuity/risk** — current suicidality, recent hospitalization, acute psychosis, severe SUD withdrawal risk; (b) **diagnosis fit** — presentations that need in-person components; (c) **environment** — private, safe, distraction-free space; who else is present; (d) **technology** — device, connectivity, digital literacy, accessibility needs; (e) **preference/engagement** — client's informed choice. Produce a clear suitable / conditionally-suitable / not-suitable disposition with the human-in-the-loop checkpoint that a licensed clinician signs off on the disposition.

4. **Draft telehealth informed consent elements.** Include: modalities used and their limits; privacy and technology risks; what happens if technology fails (the agreed fallback); recording policy; the emergency protocol and the client's responsibility to provide current location and emergency contact; limits of confidentiality; and consent to the jurisdictional basis of service. Leave clinician/practice-specific language as bracketed slots.

5. **Construct the per-location emergency protocol.** For each session, capture and confirm: client's exact physical address; a named local emergency contact with phone; nearest ED; and local crisis line (alongside 988). Define the escalation ladder and the detection-to-action expectation: a same-session safety assessment for emergent risk; do not defer emergent risk to a future session or to an asynchronous channel.

   | Signal | Tier | Action |
   |--------|------|--------|
   | Passive ideation, no plan/intent, future-oriented | Clinician this week | Safety planning; schedule follow-up; document |
   | Active ideation with plan/intent, able to engage | Clinician today / 988 | Same-session risk assessment; collaborate on means safety; 988 as bridge |
   | Imminent danger / inability to maintain safety | 911 / nearest ED | Direct to local emergency services using client's verified location; warm handoff where possible |

6. **Resolve licensure and PSYPACT at the point of service.** State the rule plainly: service is governed by the jurisdiction where the client is physically located at the time of service. Specify that clinicians may serve a given client only if licensed in that jurisdiction or operating under PSYPACT (APIT/E.Passport) or the relevant compact privilege. Require the location attestation each session and a documented decision when a client travels to a non-covered jurisdiction. Mark member-state and statute specifics as `[verify current ___]`.

7. **Address equity and the digital divide.** Define the fallback hierarchy (video → audio-only → community access point → in-person referral), device/data assistance options, language access, and accessibility accommodations, so that screening out of telehealth does not become screening out of care.

8. **Specify documentation.** Telehealth notes must record: modality used; client's physical location and confirmation of identity; that consent and emergency protocol were addressed; POS (02 or 10) and modifier (95 or 93); and any technology issues. (See the telehealth session note prompt for note-level detail.)

9. **Run verification.**

## Output Format

```
=== TELEMENTAL HEALTH PROGRAM DESIGN ===

PRACTICE CONTEXT
Disciplines / licenses: [___ in states ___]
PSYPACT / compact status: [APIT / E.Passport / Counseling Compact — states] [verify current member list]
Client populations / acuity served: [___]
Jurisdictions where clients are physically located: [___]

────────────────────────────────────────────────────────
1. MODALITIES OFFERED
| Modality | Clinical indication | Contraindication / exclusion | Requirement |
| Synchronous video | [...] | [...] | HIPAA platform + BAA |
| Audio-only | [...] | [...] | Modifier 93; [verify payer coverage] |
| Asynchronous messaging | [...] | NOT for emergencies | Response SLA = [___] |
| In-person fallback | [...] | — | Referral local to client |

────────────────────────────────────────────────────────
2. TECHNOLOGY / PLATFORM REQUIREMENTS
Platform: [Name] — BAA signed: [Y/N]
Encryption: [in transit / at rest] | Access control: [unique auth, RBAC] | Audit logging: [Y/N]
Downtime / failure procedure: "[Fallback channel and steps]"
Pre-session tech check: "[Steps]"

────────────────────────────────────────────────────────
3. CLINICAL-APPROPRIATENESS SCREEN
Acuity/risk: [criteria] | Diagnosis fit: [criteria]
Environment (privacy/safety/others present): [criteria]
Technology (device/connectivity/literacy/accessibility): [criteria]
Preference/engagement: [criteria]
DISPOSITION: [ Suitable / Conditionally suitable: ___ / Not suitable: refer to ___ ]
Human-in-the-loop checkpoint: licensed clinician [name/role] signs off on disposition.

────────────────────────────────────────────────────────
4. TELEHEALTH INFORMED CONSENT — ELEMENTS
[ ] Modalities and limits  [ ] Privacy/technology risks  [ ] Technology-failure fallback
[ ] Recording policy  [ ] Emergency protocol + client location duty  [ ] Confidentiality limits
[ ] Jurisdictional basis of service
Practice-specific language: [clinician input required: ...]

────────────────────────────────────────────────────────
5. PER-LOCATION EMERGENCY PROTOCOL (confirmed each session)
Client physical address: [___]  Local emergency contact: [name / phone]
Nearest ED: [___]  Local crisis line: [___]  (plus 988)
Escalation ladder:
  [Signal] → Clinician this week → [action]
  [Signal] → Clinician today / 988 → [action]
  [Signal] → 911 / nearest ED (client's location) → [action]
Rule: emergent risk handled same-session; never deferred to async channel.

────────────────────────────────────────────────────────
6. LICENSURE / PSYPACT
Governing rule: client's PHYSICAL LOCATION at time of service governs jurisdiction.
Clinician authorized in client's jurisdiction via: [license / APIT / compact] [verify current ___]
Location attestation: collected every session. Travel exception handling: "[___]"

────────────────────────────────────────────────────────
7. EQUITY / DIGITAL DIVIDE
Fallback hierarchy: video → audio-only → community access point → in-person referral
Device/data assistance: [___]  Language access: [___]  Accessibility: [___]

────────────────────────────────────────────────────────
8. DOCUMENTATION STANDARD
Each note records: modality | client location + identity confirmation | consent/emergency addressed |
POS [02 / 10] + modifier [95 / 93] | technology issues.
```

## Verification

- [ ] Each offered modality has explicit clinical indications AND contraindications.
- [ ] Platform requirements name BAA, encryption, access control, audit logging, and a tested failure fallback.
- [ ] Clinical-appropriateness screen covers acuity, diagnosis fit, environment, technology, and preference, ending in a clinician-signed disposition.
- [ ] Telehealth informed consent includes modality limits, technology-failure plan, emergency protocol, and jurisdictional basis.
- [ ] Per-location emergency protocol uses the client's physical location and local resources, with a 988/today/this-week/911 escalation ladder.
- [ ] Licensure section states that the client's physical location at time of service governs jurisdiction; PSYPACT/compact authority addressed; location attestation required each session.
- [ ] Human-in-the-loop checkpoint named; no automated feature positioned as making clinical decisions.
- [ ] Equity/digital-divide fallback hierarchy specified.
- [ ] Documentation standard includes POS (02/10) and modifier (95/93).
- [ ] Jurisdiction- and payer-specific facts marked `[verify current ___]` rather than fabricated.
- [ ] Missing inputs flagged with `[clinician input required]`.
