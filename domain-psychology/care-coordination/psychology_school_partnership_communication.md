---
title: "School-Partnership Communication (Counselor / Teacher / IEP-504 Team)"
category: psychology/care-coordination
description: "Draft a scope-limited communication to a school counselor, teacher, or IEP/504 team conveying only functional/classroom-relevant information and recommended accommodations, with explicit consent/assent framing and a statement of what is NOT disclosed."
techniques:
  - ST-04
  - DT-01
  - CM-02
  - DS-02
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - school-partnership
  - IEP
  - 504-plan
  - accommodations
  - minimum-necessary
  - consent-assent
  - care-coordination
updated: "2026-06-08"
related_prompts:
  - domain-psychology/care-coordination/psychology_referral_letter_generator.md
  - domain-psychology/care-coordination/psychology_warm_handoff_narrative.md
  - domain-psychology/populations/child-adolescent/psychology_school_collaboration_504_iep_input.md
  - domain-psychology/documentation/psychology_collateral_contact_note.md
---

# School-Partnership Communication (Counselor / Teacher / IEP-504 Team)

## Objective

Draft a communication from a behavioral-health clinician to a **school partner** — counselor, teacher, or IEP/504 team — about a minor client that shares **only functional, classroom-relevant information** and **recommended accommodations**, while explicitly stating **what is not being disclosed** (diagnosis details, session content, family information). The communication is bounded by a signed, school-specific **Release of Information** with **guardian consent** and developmentally appropriate **minor assent**, applies HIPAA minimum-necessary, and routes any safety concern through the appropriate channel rather than into a routine accommodations letter.

## When to Use

- Providing clinician input to an IEP or 504 eligibility/review meeting.
- Recommending classroom accommodations that support a child's functioning (e.g., movement breaks, extended time, reduced-stimulation seating, check-in/check-out).
- Coordinating with a school counselor on a shared student's in-school supports.
- Responding to a school's request for information about a student in treatment.
- Translating clinical needs into education-relevant language the team can implement.

## Inputs / Context Required

- **School recipient(s)** and role (counselor / teacher / IEP-504 team) and secure route.
- **Clinician** identity, credentials, license, practice, callback.
- **ROI status**: signed, school-specific release? Scope (what may be shared, with whom)? Expiration? `[clinician input required: ROI specifics if not provided]`.
- **Guardian consent** to communicate with the school, and **minor assent** appropriate to the child's developmental level.
- **Functional / classroom-relevant presentation**: how the concern shows up at school (attention, regulation, transitions, peer interaction, attendance) — not diagnostic detail.
- **Recommended accommodations** the clinician believes support functioning.
- **What is being deliberately withheld**: diagnosis specifics, session content, family/home information.
- **Safety status**: any active risk that requires a separate, urgent channel.
- `[clinician input required: whether the child has expressed preferences about what is shared with the school]`

## Constraints

### Must

- Limit shared content to **functional, classroom-relevant** information: how the concern manifests in the school setting and what helps.
- State **recommended accommodations** in concrete, implementable, education-relevant terms (what staff do, when, how measured).
- Include an explicit **"What is NOT being disclosed"** section naming the categories withheld (specific diagnosis, session content, family/home detail) and why (minimum-necessary, privacy of a minor).
- Document the **consent/assent framing**: guardian consent and the minor's assent at a developmentally appropriate level, plus the ROI scope and expiration.
- Apply **HIPAA minimum-necessary**; share only what the school needs to support the student. (Note: clinician records are HIPAA-covered; the school's educational records are FERPA-covered — they are distinct, and clinical detail should not be embedded into the educational record beyond what is authorized.)
- Provide a **safety carve-out**: if active risk is present, route it through the appropriate urgent/safety channel and do not embed it in a routine accommodations letter; document that the safety concern was handled separately.
- Offer a collaboration / point-of-contact line for the school to follow up within ROI scope.
- Flag missing data as `[clinician input required: ...]`; do not fabricate functional observations or accommodations.

### Must Not

- Do not disclose diagnosis specifics, session content, or family/home information unless explicitly within ROI scope and necessary.
- Do not share information without a signed school-specific ROI and guardian consent (and assent where appropriate).
- Do not embed an active-risk disclosure into a routine accommodations communication.
- Do not write accommodations as vague aspirations ("be more supportive"); make them implementable.
- Do not let clinical (HIPAA) detail flow into the FERPA educational record beyond what is authorized.
- Do not fabricate classroom observations, the child's preferences, or accommodation needs.

## Instructions

1. Confirm the signed, school-specific ROI plus guardian consent and minor assent; record scope and expiration. If absent, halt and flag `[clinician input required: consent/ROI before disclosure]`.
2. Run the safety screen: if active risk exists, route it through the urgent/safety channel and note that it was handled separately — keep it out of this letter.
3. Translate the clinical picture into **functional, classroom-relevant** observations only.
4. Draft concrete, implementable accommodations with the staff action, trigger/timing, and a way to tell if they are working.
5. Write the explicit "What is NOT being disclosed" section and the reason.
6. Document consent/assent framing, ROI scope, and expiration; add the collaboration/point-of-contact line.
7. Run verification.

## Output Format

```
=== SCHOOL-PARTNERSHIP COMMUNICATION ===

DATE: [YYYY-MM-DD]
TO: [School recipient(s), role — counselor / teacher / IEP-504 team]    Route: [secure]
FROM: [Clinician, credentials, license #, practice]    Callback: [phone]
RE: [Student initials]    Grade: [..]    DOB: [YYYY-MM-DD]

PURPOSE: [1 line — e.g., "Clinician input for upcoming 504 review; recommended classroom supports."]

────────────────────────────────────────────────────────
CONSENT / AUTHORIZATION
Guardian consent to communicate with school: [Yes — dated YYYY-MM-DD] / [clinician input required]
Minor assent (developmentally appropriate): [Obtained — describe level / N/A by age]
Signed school-specific ROI: [Yes — scope + expires YYYY-MM-DD] / [clinician input required]
Scope authorized: [What may be shared, with whom]

────────────────────────────────────────────────────────
FUNCTIONAL / CLASSROOM-RELEVANT PICTURE  (no diagnostic detail)
How the concern shows up at school: [Attention / regulation / transitions / peers / attendance — observable terms.]
Strengths to build on: [...]

RECOMMENDED ACCOMMODATIONS  (concrete + implementable)
| Accommodation | What staff do | When/trigger | How to tell it's working |
|---------------|---------------|--------------|--------------------------|
| [e.g., Movement break] | [2-min break on request] | [Signs of dysregulation] | [Fewer escalations/period] |
| [...] | [...] | [...] | [...] |

────────────────────────────────────────────────────────
WHAT IS NOT BEING DISCLOSED  (and why)
- Specific diagnosis / clinical labels — [withheld; minimum-necessary, privacy of a minor].
- Session / therapy content — [withheld].
- Family / home information — [withheld].
[Available on request only within an expanded, signed ROI.]

SAFETY NOTE
[ ] No active safety concern relevant to this communication.
[ ] A safety concern exists and was routed separately through [urgent/safety channel] on [date] — not included here.

COLLABORATION
Point of contact for the team (within ROI scope): [Name, phone, secure route].
Note: Clinical records are HIPAA-covered and distinct from the school's FERPA educational record; clinical detail is not to be entered into the educational record beyond what is authorized.

Signature: ____________________  [Clinician, credentials]  Date: __________
```

## Verification

- [ ] Shared content limited to functional, classroom-relevant information (no diagnostic detail unless ROI-authorized).
- [ ] Recommended accommodations are concrete, implementable, and have a way to gauge effectiveness.
- [ ] Explicit "What is NOT being disclosed" section names withheld categories and the reason.
- [ ] Consent/assent framing documented: guardian consent + developmentally appropriate minor assent.
- [ ] ROI scope and expiration stated; disclosure stays within scope and minimum-necessary.
- [ ] Active risk, if any, routed through the urgent/safety channel and kept out of this routine letter.
- [ ] HIPAA/FERPA distinction noted; clinical detail not embedded into the educational record beyond authorization.
- [ ] Collaboration / point-of-contact line within ROI scope included.
- [ ] No fabricated observations, accommodations, or child preferences.
- [ ] Missing inputs flagged with `[clinician input required]`.
```
