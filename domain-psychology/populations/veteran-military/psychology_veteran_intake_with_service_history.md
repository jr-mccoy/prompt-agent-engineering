---
title: "Veteran Intake with Service History"
category: psychology/populations/veteran-military
description: "Service-history-informed biopsychosocial intake for veterans and active/reserve service members that captures military service context, combat and trauma exposure, MST screening, and elevated suicide risk, producing a CPT 90791 intake note."
techniques:
  - ST-04
  - DT-02
  - RT-02
  - CM-02
  - QA-04
difficulty: intermediate
intended_use: model-testing
tags:
  - veteran
  - military
  - service-history
  - intake
  - combat-exposure
  - MST
  - suicide-risk
  - cpt-90791
  - VA
  - PTSD
updated: "2026-06-08"
related_prompts:
  - domain-psychology/populations/veteran-military/psychology_combat_trauma_formulation.md
  - domain-psychology/populations/veteran-military/psychology_military_sexual_trauma_aware_protocol.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
  - domain-psychology/documentation/psychology_intake_assessment_note.md
---

# Veteran Intake with Service History

## Objective

Produce a complete, service-history-informed biopsychosocial intake record for a veteran, active-duty, National Guard, or Reserve service member that:

1. Captures military service context as a core clinical domain: branch, era of service, Military Occupational Specialty (MOS/rating/AFSC), rank, deployments, combat exposure, and discharge status/character of service.
2. Documents VA enrollment, service-connected disability status, and eligibility for VA care (including free MST-related care).
3. Screens systematically for the signature post-deployment conditions: PTSD, depression, hazardous alcohol use, TBI history, and chronic pain.
4. Conducts universal Military Sexual Trauma (MST) screening for all genders, with a warm hand-off to a focused protocol when positive.
5. Administers a mandatory suicide-risk screen with lethal-means (firearm) counseling, given the elevated suicide risk in this population, and documents the Veterans Crisis Line escalation pathway.
6. Produces a structured intake note meeting CPT 90791 documentation requirements.

## When to Use

- At initial intake for any veteran, active-duty, Guard, or Reserve service member presenting for outpatient mental health care, in VA, DoD, community-care, or private settings.
- When a community clinician receives a referral from VA Community Care, Vet Centers, or a Veteran Service Organization and needs a service-informed intake structure.
- For re-intake when a veteran returns to care after a gap, a new deployment, a transition out of service, or a change in service-connection status.

## When NOT to Use

- For a routine adult intake where the client has no military affiliation: use `psychology_intake_assessment_note.md`.
- As a standalone combat-trauma case formulation: when combat trauma or moral injury is the focus, pair with `psychology_combat_trauma_formulation.md`.
- As a focused MST engagement protocol: when MST screening is positive or MST is the presenting concern, route to `psychology_military_sexual_trauma_aware_protocol.md`.
- As a structured suicide-risk assessment instrument: a positive screen here routes to `psychology_columbia_suicide_risk_assessment.md`.

## Inputs / Context Required

- **Client demographics:** Name/initials, DOB, age, gender identity, pronouns, race/ethnicity as client identifies, primary language, relationship and housing status.
- **Military service summary (if available):** DD-214 or service record, branch, component (active/Guard/Reserve), era, MOS, rank at separation, deployments, awards, character of discharge.
- **VA/benefits context:** VA enrollment status, assigned VA facility/Vet Center, service-connected conditions and combined rating, current VA or DoD providers.
- **Referral information:** Source, reason, any records received.
- **Prior records:** Prior mental health and substance treatment, TBI/polytrauma evaluations, C&P (Compensation & Pension) exam findings if shared by client.
- **Consent:** Standard informed consent; releases of information for VA, Vet Center, command, or collateral contacts as applicable.
- `[clinician input required: any command-notification, fitness-for-duty, or security-clearance reporting obligations relevant to active-duty/Guard/Reserve status]`

## Constraints

### Must

- Document military service history as a required clinical domain — not optional background — including branch, era, MOS, deployments, combat exposure, and character of discharge.
- Use the Combat Exposure Scale (CES) framing to characterize combat exposure severity rather than a single yes/no item.
- Conduct universal MST screening using the VA's two-item MST clinical reminder framing for every client regardless of gender; document the screen result even when negative.
- Administer the PC-PTSD-5 as the brief screen and, when positive or trauma is endorsed, the PCL-5; administer PHQ-9 and AUDIT-C at every veteran intake.
- Conduct a mandatory suicide-risk screen and, if positive, complete a Columbia C-SSRS and lethal-means (firearm) counseling; document the Veterans Crisis Line pathway (988 then Press 1) in the safety plan.
- Document VA enrollment and service-connection status because they determine care eligibility, including the rule that MST-related care is free at VA regardless of service-connection or discharge status.
- Screen for TBI history (deployment blast exposure, loss of consciousness) and chronic pain, given high comorbidity with post-deployment mental health conditions.
- Flag all `[clinician input required: ...]` gaps; do not fabricate service records, deployment dates, ratings, or instrument scores.

### Must Not

- Do not omit the MST screen for male clients; MST affects men and women, and under-screening men is a known failure mode.
- Do not equate a less-than-honorable discharge with ineligibility for care; document character of discharge factually and note that MST-related and certain other VA care can be available regardless.
- Do not skip the firearm-access and lethal-means inquiry; veteran suicide deaths disproportionately involve firearms.
- Do not assume combat exposure from branch or MOS, or assume its absence from a support role; ask directly and characterize with the CES.
- Do not fabricate a DD-214, C&P findings, deployment history, or service-connection percentages; mark unknowns as such.

## Service-Context Reference Overlay

| Domain | What to capture | Why it is clinically load-bearing |
|--------|-----------------|-----------------------------------|
| Era of service | Vietnam, Gulf War, OEF/OIF/OND, post-9/11 Guard/Reserve, peacetime | Anchors likely exposures (Agent Orange, burn pits, blast), cohort norms, and benefit eligibility windows |
| Branch + component | Army/Navy/USAF/USMC/USCG/USSF; active vs. Guard/Reserve | Reserve/Guard carry civilian-life disruption and weaker unit support post-deployment |
| MOS / rating / AFSC | Job specialty | Maps occupational exposures (combat arms, medic, EOD, mortuary affairs, drone/ISR moral strain) |
| Deployments | Number, location, dates, role | Dose-response relationship with PTSD; multiple deployments raise risk |
| Combat exposure (CES) | Firefights, casualties, IEDs, handling remains | Severity grading; informs combat-trauma formulation referral |
| Character of discharge | Honorable / General / OTH / BCD / Dishonorable | Affects benefits; OTH veterans face elevated risk and access barriers; MST care still available |
| Service-connection | Conditions + combined % rating | Affects care eligibility, financial context, and disability-system stressors |

## Instructions

1. **Pre-intake setup.** Review available records (DD-214, prior evaluations, referral). Identify component status and any active-duty/Guard/Reserve reporting obligations. Confirm consent and applicable releases.

2. **Open and orient.** Introduce the structure of the intake, explain confidentiality and its limits (including any command, fitness-for-duty, or mandated-reporting obligations relevant to the client's status), and acknowledge military service.

3. **Elicit service history.** Cover branch, component, era, MOS, rank, deployments, awards, and character of discharge. Characterize combat exposure using the Combat Exposure Scale framing.

4. **Document VA/benefits context.** Enrollment, facility, service-connected conditions and rating, current VA/DoD providers, and any C&P involvement.

5. **Screen post-deployment conditions.** Administer PC-PTSD-5, PHQ-9, AUDIT-C; administer PCL-5 if PTSD screen positive or trauma endorsed. Screen TBI history and chronic pain.

6. **Conduct universal MST screen.** Use the VA two-item MST framing for every client. If positive, proceed sensitively and route to the MST-aware protocol; document warm hand-off.

7. **Conduct suicide-risk screen with lethal-means counseling.** Screen for SI/behavior; if positive, complete Columbia C-SSRS, conduct firearm/lethal-means counseling, and document the Veterans Crisis Line pathway and safety plan.

8. **Complete biopsychosocial domains.** Psychiatric, substance, medical, family/social, and military-to-civilian transition functioning.

9. **Write the Veteran Intake Note** using the output format below.

10. **Run verification.**

## Output Format

```
=== VETERAN BIOPSYCHOSOCIAL INTAKE NOTE ===

Client: [Initials/MRN]   DOB: [YYYY-MM-DD]   Age: [N]   Gender/Pronouns: [...]
Date of Service: [YYYY-MM-DD]   Time: [HH:MM–HH:MM]
Clinician: [Name, credentials]
CPT: 90791   Duration: [N minutes]   Setting: [VA / DoD / Vet Center / Community Care / Private]

─────────────────────────────────────────
CONSENT AND REPORTING CONTEXT
─────────────────────────────────────────
Informed consent obtained: [Yes — date/method]
Confidentiality limits reviewed: [Yes — including: ...]
Active-duty/Guard/Reserve reporting obligations: [None / Command notification: ... / Fitness-for-duty: ... / Security clearance: ...] [clinician input required: ...]
Releases of information: [VA / Vet Center / Command / PCP / Collateral — obtained / pending]

─────────────────────────────────────────
MILITARY SERVICE HISTORY
─────────────────────────────────────────
Branch: [Army / Navy / Air Force / Marine Corps / Coast Guard / Space Force]
Component: [Active duty / National Guard / Reserve / Veteran (separated)]
Era of service: [Vietnam / Gulf War / OEF / OIF / OND / Post-9/11 / Peacetime / Other]
Years of service: [Entry – Separation]   Rank at separation: [...]
MOS / Rating / AFSC: [Code + description]
Deployments: [Number; locations; dates; role] [clinician input required if record unavailable]
Awards / commendations relevant to exposure (e.g., CAB/CIB, Purple Heart): [...]
Character of discharge: [Honorable / General (Under Honorable) / OTH / BCD / Dishonorable / Still serving]
Source of service data: [DD-214 reviewed / Client self-report / Records pending]

COMBAT EXPOSURE (Combat Exposure Scale framing):
  Exposure to firefights / enemy fire: [None / Some / Frequent]
  Witnessed casualties / death: [None / Some / Frequent]
  IED / blast / mortar exposure: [None / Some / Frequent]
  Handling of human remains: [Yes / No]
  CES severity estimate: [None / Light / Moderate / Heavy / Extreme]
  Refer for combat-trauma formulation: [Yes → psychology_combat_trauma_formulation.md / No]

─────────────────────────────────────────
VA / BENEFITS CONTEXT
─────────────────────────────────────────
VA enrolled: [Yes — facility: ... / No / Eligibility unknown]
Vet Center engaged: [Yes — location / No]
Service-connected conditions: [List]   Combined rating: [__% / None / Pending]
C&P (Compensation & Pension) exam history: [Completed: ... / Pending / N/A]
Current VA/DoD providers: [...]
Eligibility note: MST-related mental health care is available free at VA regardless of service-connection or character of discharge. [Confirmed applicable: Yes / N/A]

─────────────────────────────────────────
REFERRAL AND PRESENTING CONCERN
─────────────────────────────────────────
Referred by: [...]   Reason: [...]
Chief complaint (client's words): "[...]"
History of presenting illness: [Narrative — onset, course, functional impact; link to deployment/transition timeline where relevant]

─────────────────────────────────────────
POST-DEPLOYMENT SCREENING
─────────────────────────────────────────
PC-PTSD-5: [Score: N/5; Positive (≥3): Yes/No]
PCL-5 (if indicated): [Score: N/80; Provisional PTSD threshold (≥31–33): Yes/No]
PHQ-9: [Score: N/27; Severity band: ___; Item 9 (SI): 0/1/2/3]
AUDIT-C: [Score: N/12; Positive (M ≥4 / F ≥3): Yes/No]
TBI history screen: [Blast/impact exposure: Y/N; LOC/AOC/PTA: ...; Prior TBI eval: ...]
Chronic pain: [Present — location/severity / Absent]

─────────────────────────────────────────
MILITARY SEXUAL TRAUMA (MST) UNIVERSAL SCREEN
─────────────────────────────────────────
[VA two-item MST clinical reminder framing — administered to ALL clients regardless of gender.]
Item 1 (unwanted sexual attention/harassment during service): [Yes / No / Declined]
Item 2 (sexual assault/coerced sexual contact during service): [Yes / No / Declined]
MST screen result: [Negative / Positive]
If Positive: warm hand-off to MST-aware protocol documented: [Yes → psychology_military_sexual_trauma_aware_protocol.md]
Client informed MST-related care is free at VA regardless of service-connection/discharge: [Yes / N/A]

─────────────────────────────────────────
SUICIDE RISK SCREEN AND LETHAL-MEANS COUNSELING
─────────────────────────────────────────
[Mandatory — veteran population carries elevated suicide risk.]
Current SI: [Present — type, plan, intent / Absent]
Prior attempts: [Yes — describe / No]
Columbia C-SSRS completed: [Yes — most severe ideation: ___; behavior: ___ / Not indicated by negative screen]
Firearm access: [Yes — number/storage / No]   Other lethal means: [...]
Lethal-means (firearm) counseling provided: [Yes — safe storage / temporary off-site / locking device discussed]
Risk level: [Low / Moderate / High — rationale]
Veterans Crisis Line provided (988 then Press 1; text 838255; chat): [Yes]
Safety plan completed: [Yes — copy provided / Not indicated]
Escalation pathway if risk elevates: [Veterans Crisis Line → ED → VA same-day mental health → ...]

─────────────────────────────────────────
PSYCHIATRIC, SUBSTANCE, AND MEDICAL HISTORY
─────────────────────────────────────────
Prior diagnoses / treatment: [...]
Prior inpatient/residential: [...]
Substance use history: [Alcohol, cannabis, opioids (incl. service-related pain pathway), stimulants, tobacco]
Current medications: [Name, dose, prescriber]
Medical conditions / exposures (burn pit, Agent Orange, blast): [...]
Sleep / nightmares: [...]

─────────────────────────────────────────
FAMILY, SOCIAL, AND TRANSITION FUNCTIONING
─────────────────────────────────────────
Relationship / family status: [...]
Housing stability: [Stable / At risk / Homeless — VA HUD-VASH/SSVF referral: Y/N]
Employment / education (incl. GI Bill, VR&E): [...]
Military-to-civilian transition stressors: [Identity/purpose loss, unit/social support loss, ...]
Legal / financial: [...]
Strengths and protective factors: [...]

─────────────────────────────────────────
MENTAL STATUS EXAMINATION
─────────────────────────────────────────
[Appearance, Behavior, Speech, Mood, Affect, Thought Process, Thought Content (SI/HI explicit), Perception, Cognition, Insight, Judgment]

─────────────────────────────────────────
DIAGNOSTIC IMPRESSIONS
─────────────────────────────────────────
Primary: [DSM-5-TR] [ICD-10-CM]
Secondary: [...]
Z-code stressors: [e.g., Z65.4 victim of crime/terrorism; Z56.9 occupational stress; Z59.0 homelessness — as applicable]
Rule out / Deferred: [...]

─────────────────────────────────────────
FORMULATION (5-P)
─────────────────────────────────────────
Predisposing / Precipitating / Perpetuating / Protective / Presenting: [...]
Service-context contribution: [...]

─────────────────────────────────────────
TREATMENT RECOMMENDATIONS
─────────────────────────────────────────
Level of care: [...]
Recommended modality (referenced, not delivered here): [CPT / PE / EMDR for PTSD — note evidence-based options; selection per modality decision aid]
Referrals: [VA/Vet Center, MST coordinator, TBI/polytrauma, pain, SUD, housing, VR&E]
Risk-reassessment hook: [Re-screen SI and firearm access at each visit; sooner if [trigger]]

─────────────────────────────────────────
BILLING NOTE
─────────────────────────────────────────
CPT: 90791 (Psychiatric Diagnostic Evaluation)   Duration: [N minutes]
Payer: [VA / TRICARE / Community Care auth / Commercial]   Authorization: [Not required / Auth #___]
```

## Verification

- [ ] Military service history documented as a required domain (branch, component, era, MOS, deployments, discharge).
- [ ] Combat exposure characterized using the Combat Exposure Scale framing, not a single yes/no.
- [ ] VA enrollment and service-connection status documented; MST-care eligibility note included.
- [ ] PC-PTSD-5, PHQ-9, and AUDIT-C administered; PCL-5 administered if PTSD screen positive.
- [ ] TBI history and chronic pain screened.
- [ ] Universal MST screen administered for this client regardless of gender; result documented even if negative.
- [ ] Positive MST screen triggers warm hand-off to the MST-aware protocol.
- [ ] Mandatory suicide-risk screen completed; firearm/lethal-means counseling documented.
- [ ] Veterans Crisis Line pathway (988 then Press 1) documented in safety planning.
- [ ] Positive suicide screen routes to Columbia C-SSRS.
- [ ] MSE Thought Content addresses SI and HI explicitly.
- [ ] Diagnostic impressions include ICD-10-CM codes and relevant Z-codes.
- [ ] Risk-reassessment hook specified.
- [ ] Gaps flagged with `[clinician input required: ...]`; no fabricated service records or scores.
