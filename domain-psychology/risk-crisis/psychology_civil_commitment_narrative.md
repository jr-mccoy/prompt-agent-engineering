---
title: "Civil Commitment / Involuntary Hold Narrative"
category: psychology/risk-crisis
description: "Draft an involuntary-hold narrative (e.g., 5150 / state equivalent) that documents danger to self / danger to others / grave disability with specific behavioral evidence and least-restrictive-alternative reasoning suitable for review by a hearing officer."
techniques:
  - ST-04
  - DT-02
  - RT-05
  - QA-04
  - CM-02
  - DS-04
difficulty: advanced
tags:
  - civil-commitment
  - involuntary-hold
  - 5150
  - danger-to-self
  - danger-to-others
  - grave-disability
  - least-restrictive-alternative
  - probable-cause
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
  - domain-psychology/risk-crisis/psychology_homicidal_ideation_triage.md
  - domain-psychology/risk-crisis/psychology_tarasoff_duty_to_warn_analysis.md
---

# Civil Commitment / Involuntary Hold Narrative

## Objective

Draft a narrative supporting initiation of an involuntary psychiatric hold. The narrative must:

1. Identify the **statutory category** invoked: typically **danger to self (DTS)**, **danger to others (DTO)**, or **grave disability (GD)** (some states call this "unable to provide for basic needs"). Specific terminology and durations vary (e.g., California 5150 = 72-hour hold; Florida Baker Act; New York 9.39; Washington ITA).
2. Document **specific, observable behavioral evidence** supporting the criterion — not conclusions.
3. Document the **least-restrictive-alternative analysis** (what was tried or considered, why outpatient or voluntary admission is insufficient).
4. Document the clinician's **statutory authority** to initiate the hold (peace officer, designated mental-health professional, physician, in some states LCSW or LPC with state-specific designation).
5. Be written so that a reviewing officer (probable-cause hearing, judicial review) can find probable cause from the facts.

This is a generic template; the clinician must adapt to their state's statutory language, forms, and authority chain.

## When to Use

- After a suicide-risk assessment supports imminent risk and outpatient management is insufficient.
- After a homicidal-ideation triage with active duty-to-protect concerns and dispositional need for inpatient containment.
- For grave disability — psychotic decompensation with inability to maintain food / shelter / medical needs, or severe mania, or florid catatonia.
- When voluntary admission has been offered and declined, or is not feasible.

## Inputs / Context

- State statute being invoked (clinician must confirm exact code and form).
- Clinician's statutory authority (license type with designation, agency authorization, peace-officer involvement).
- Linked Columbia or homicidal-ideation triage with date.
- Specific verbatim client statements supporting the criterion.
- Specific observed behaviors supporting the criterion (within the past 24–72 h typically; statutes vary).
- Mental status data points.
- Voluntary admission offer status: offered / declined / not feasible / unable to consent.
- Means access; recent acts (preparatory, attempts, NSSI).
- Substance use / intoxication.
- Failure of less-restrictive alternatives: outpatient intensification, mobile crisis, partial hospital, voluntary admission.
- Family / supports' availability and willingness to maintain safety.
- Medical clearance status (most facilities require medical clearance prior to psychiatric admission).
- Client's current capacity to consent and to participate in the decision.

## Constraints

### Must

- Output the following labeled sections in order: **Encounter Metadata**, **Statutory Authority and Category**, **Specific Behavioral Evidence**, **Mental Status**, **Substance and Medical Status**, **Voluntary Admission Analysis**, **Least-Restrictive-Alternative Analysis**, **Capacity to Consent**, **Family / Support Availability**, **Probable-Cause Statement**, **Disposition and Transport**, **Notifications**, **Clinician Statement and Signature**, **Limits and Disclaimer**.
- The Specific Behavioral Evidence section uses **observable** behavior and **verbatim statements**, with timestamps where possible. Avoid conclusions ("client was suicidal") in favor of evidence ("client said at 14:32, 'I'm going to drive my car into a bridge tonight,' had a written note in their pocket dated today, and refused to surrender it").
- The Least-Restrictive-Alternative Analysis explicitly considers and rejects each less-restrictive option (outpatient intensification, mobile crisis, partial hospital, voluntary admission, family-supervised home) with specific reasoning.
- The Probable-Cause Statement is a narrative paragraph (4–8 sentences) integrating the evidence so that a reviewing officer can make a probable-cause finding.
- Capacity to Consent is documented separately; if the hold is partly because client lacks capacity to make the admission decision, that is stated.
- Family / support availability is documented; the absence of available family for supervised home management is part of LRA analysis.
- Medical clearance status documented (most psych admissions require medical clearance from ED).
- Notifications: who has been or will be notified (family per consent or per emergency exception, agency, transport).
- Clinician's statutory authority cited: license, any required designation (e.g., "Designated 5150 Mental Health Professional, Los Angeles County, ID #...").
- Disclaimer that statutes vary materially by state and the clinician must use the correct state form.

### Must Not

- Do not substitute conclusions for evidence ("client was psychotic" — instead: specific observed thought disorder, delusional content, command AH, behavioral disorganization).
- Do not invoke a category not supported by the evidence (e.g., GD where DTS is more appropriate, or DTO without an identifiable threat).
- Do not bypass voluntary-admission analysis when voluntary admission was feasible.
- Do not omit least-restrictive-alternative analysis; this is often the section that fails on review.
- Do not initiate a hold without statutory authority or, when authority is lacking, without engaging the appropriate authorized professional (peace officer, designated MHP, ED physician).
- Do not delay transport while perfecting the narrative; document at the earliest safe moment.
- Do not fabricate; flag missing inputs.

## Instructions

1. Compile encounter metadata.
2. State statutory authority and category invoked: DTS / DTO / GD or combination.
3. Document specific behavioral evidence with timestamps and verbatim statements.
4. Document mental status, substance status, medical status.
5. Document voluntary-admission analysis: offered? declined? not feasible? rationale.
6. Document least-restrictive-alternative analysis: each option considered, why insufficient.
7. Document capacity to consent.
8. Document family / support availability.
9. Compose probable-cause statement integrating the evidence.
10. Document disposition and transport plan; medical clearance.
11. Document notifications.
12. Sign with statutory authority cited.
13. Append disclaimer.
14. Run verification.

## Output Format

```
=== CIVIL COMMITMENT / INVOLUNTARY HOLD NARRATIVE ===

ENCOUNTER METADATA
Client: [Initials/MRN]    DOB: [age, gender, pronouns]
Date: [YYYY-MM-DD]    Time: [HH:MM]    Setting: [ED / Outpatient / Inpatient / Mobile crisis / Telehealth (with caveats)]
Clinician: [Name, credentials, license #, statutory designation]
Linked assessments:
- Suicide risk (Columbia): [Date]
- Homicidal ideation triage: [Date if applicable]
- Tarasoff / duty-to-protect analysis: [Date if applicable]

STATUTORY AUTHORITY AND CATEGORY
State: [...]    Statute / form: [State code; form number; e.g., "California Welfare & Institutions Code 5150; LPS Form"]
Authority: [Designated Mental Health Professional / Peace officer / Physician / Other state-specific designation]
Category invoked: [Danger to Self / Danger to Others / Grave Disability / Combination — specify which]
Hold duration authorized by statute: [e.g., 72 hours]

SPECIFIC BEHAVIORAL EVIDENCE
For the category invoked, observable, time-stamped, verbatim where possible:

Danger to Self:
- [HH:MM — Specific statement: "..."]
- [HH:MM — Observed behavior: e.g., "Found in possession of [item], with note dated today, refused to surrender"]
- [Recent attempt or preparatory acts within statutory window]
- [Means access; recent reduction or escalation]

Danger to Others:
- [HH:MM — Specific statement: "..."]
- [Identifiable target; means; preparatory acts; agitation]
- [Linked Tarasoff analysis if separate]

Grave Disability:
- [Inability to provide for food: specific evidence]
- [Inability to provide for shelter: specific evidence]
- [Inability to provide for medical needs given psychiatric state: specific evidence]
- [Behavioral disorganization documented]

MENTAL STATUS
[Appearance, behavior, agitation, speech, mood (quoted), affect, thought process (specific — looseness, tangentiality, blocking), thought content (delusions with content, AH/VH with content, command AH if any), cognition, insight, judgment.]

SUBSTANCE AND MEDICAL STATUS
- Intoxication / withdrawal status: [...]
- Active medical issues: [...]
- Medication adherence: [...]
- Medical clearance status (for psychiatric admission): [Obtained / Pending / Required at receiving facility]

VOLUNTARY ADMISSION ANALYSIS
- Voluntary admission offered: [Yes / No — if not offered, rationale: clinically inappropriate / client lacks capacity / safety risk in attempting]
- Client's response to offer: [Accepted / Declined / Unable to engage with offer / Withdrew acceptance]
- If declined: client's stated reason: [...]
- Is voluntary admission a feasible alternative now? [Yes / No — rationale]

LEAST-RESTRICTIVE-ALTERNATIVE ANALYSIS
Each option considered:
1. Outpatient intensification (increased session frequency, daily check-ins): [Considered — Insufficient because: ...]
2. Mobile crisis dispatch / wraparound: [Considered — Insufficient because: ...]
3. Partial hospital / IOP: [Considered — Insufficient because: ...]
4. Voluntary admission: [See above]
5. Family-supervised home with means restriction and intensified follow-up: [Considered — Insufficient because: family unavailable / unwilling / unable / safety risk to family]
6. Other state-specific options: [...]

Conclusion: Inpatient hospitalization on involuntary basis is the least restrictive alternative that adequately addresses the safety concern.

CAPACITY TO CONSENT
- Capacity to consent to or refuse psychiatric hospitalization at this time: [Present / Impaired / Absent]
- Evidence: [Specific cognitive / psychotic / acute distress evidence; ability to articulate risks/benefits/alternatives]
- Implication for the hold: [Hold initiated due to acute risk regardless of capacity / Hold initiated partly because client lacks capacity to consent]

FAMILY / SUPPORT AVAILABILITY
- Family / partner / supports identified: [Names, relationships]
- Willingness to provide supervised safety at home: [Yes / No / Unable]
- Capability (means access controlled, 24/7 supervision feasible, safety plan workable): [Yes / No]
- ROI status: [...]

PROBABLE-CAUSE STATEMENT
[A narrative paragraph (4–8 sentences) integrating the evidence so a reviewing officer can find probable cause that the client meets the statutory category and that less-restrictive alternatives are insufficient. Use specific evidence; preserve verbatim statements; tie evidence to the elements of the statute.]

DISPOSITION AND TRANSPORT
- Receiving facility: [Name, address]
- Bed availability confirmed: [Yes / No / Pending]
- Medical clearance: [Obtained / Pending at ED / Required en route]
- Transport: [EMS / Law enforcement transport (per state rules) / Mobile crisis transport / Family transport contraindicated when?]
- ETA to receiving facility: [...]
- Time of decision: [HH:MM]    Time of transport initiated: [HH:MM]

NOTIFICATIONS
- Family / emergency contact: [Name, time, content — per consent or emergency exception]
- Receiving facility intake clinician: [Name, time]
- Outpatient provider continuity (PCP, prescriber, therapist): [Name, time]
- Agency risk management / supervisor: [Name, time]
- Law enforcement (if involved in transport): [Agency, officer name, badge, time]

CLINICIAN STATEMENT AND SIGNATURE
I, [Name, credentials, license #, statutory designation], am authorized under [State statute] to initiate this involuntary psychiatric hold. Based on the specific behavioral evidence and analysis documented above, I have probable cause to believe the client meets the criterion of [DTS / DTO / GD] and that less restrictive alternatives are insufficient. The hold is initiated at [HH:MM YYYY-MM-DD].

Signature: __________________  Date/Time: ___________
Supervisor / co-signing physician (per state rule): __________________  Date/Time: ___________

LIMITS AND DISCLAIMER
This is a generic narrative template. State statutes vary materially in:
- Who is authorized to initiate the hold
- The duration and structure of the hold (72 hours, longer holds, judicial vs administrative)
- The categories named and their definitions
- The forms required and their language
- The procedures for transport and review
The clinician must use the correct state form and statutory language; this template supplements but does not replace the official form.
```

## Verification

- [ ] All labeled sections present and in order.
- [ ] Statutory authority and category cited; state form referenced.
- [ ] Specific behavioral evidence is observable, time-stamped, with verbatim quotes — not conclusions.
- [ ] Mental status documented in detail (not "WNL").
- [ ] Substance and medical status documented; medical clearance status explicit.
- [ ] Voluntary admission analysis explicit (offered? response? feasible alternative?).
- [ ] Least-restrictive-alternative analysis considers ≥ 5 options with rationale why each is insufficient.
- [ ] Capacity to consent documented separately.
- [ ] Family / support availability documented.
- [ ] Probable-cause statement is an integrative narrative.
- [ ] Disposition / transport / medical-clearance documented.
- [ ] Notifications documented with time.
- [ ] Clinician statement cites statutory authority.
- [ ] Disclaimer about state variation present.
- [ ] No conclusions substituted for evidence; no LRA analysis omitted; no statutory category invoked without supporting evidence.
- [ ] Gaps flagged; nothing fabricated.
