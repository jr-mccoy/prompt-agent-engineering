---
title: "Homicidal Ideation Triage and Documentation"
category: psychology/risk-crisis
description: "Conduct and document a structured homicidal-ideation triage covering target identifiability, plan, means, intent, ideation type (egodystonic vs egosyntonic), risk stratification, and disposition including duty-to-protect analysis."
techniques:
  - ST-04
  - DT-02
  - RT-02
  - RT-05
  - QA-04
  - CM-02
difficulty: advanced
tags:
  - homicidal-ideation
  - violence-risk
  - duty-to-protect
  - tarasoff
  - hcr-20
  - egodystonic-vs-egosyntonic
intended_use: model-testing
updated: "2026-05-08"
related_prompts:
  - domain-psychology/risk-crisis/psychology_tarasoff_duty_to_warn_analysis.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
---

# Homicidal Ideation Triage and Documentation

## Objective

Produce a structured assessment of homicidal ideation (HI) when raised in clinical encounter, intake, or post-incident contact. The output must:

1. Distinguish **identifiable target(s)** from **non-specific anger / vengeance ideation**.
2. Walk plan, means, intent, and timeline (analogous to suicide-risk specifics, but with separate considerations).
3. Differentiate **egodystonic** intrusive HI (often OCD-spectrum or trauma-driven) from **egosyntonic** HI (anger-congruent, plan-supportive).
4. Synthesize static / dynamic / protective factors using a violence-risk frame (drawing on HCR-20 V3 or comparable).
5. Produce stratification (low / moderate / high) and disposition (outpatient management / increased contact / mobile crisis / ED / law enforcement notification / Tarasoff-style warning / civil commitment).
6. Trigger a separate **duty-to-protect analysis** when criteria are met.

This is a triage-and-documentation prompt; full violence risk assessment with structured tools (HCR-20 V3, VRAG, START) is a longer process and is referenced rather than executed here.

## When to Use

- Any disclosure or screening positive for HI.
- Anger-driven ideation that names or implies a target.
- Recent forensic event (assault, domestic violence, stalking).
- Intrusive violent thoughts that distress the client (consider OCD differential).
- Pre-discharge from ED / inpatient / forensic units.

## Inputs / Context

- Client identifiers, age, current setting.
- Trigger that raised concern (client disclosure, collateral report, screening).
- Specific HI content: targets (named, identifiable, generic), thoughts/images/urges/plans/preparatory acts, weapons/means access, timeline.
- Client's stated intent and confidence (egodystonic vs egosyntonic; ego-alien intrusive vs anger-congruent).
- History of violence: prior physical violence, domestic violence, weapons charges, court orders against client, incarceration, juvenile history, fire-setting, animal cruelty.
- Co-occurring SI (often co-present in homicide-suicide).
- Substance use / intoxication.
- Psychotic symptoms, command AH directing violence, paranoia about target.
- Identifiable target's current accessibility, relationship, and any pattern of stalking.
- Static factors (HCR-20 H items) and dynamic factors (HCR-20 C items) and risk-management factors (R items).
- Mental status; current medication adherence.
- Collateral information (police reports, prior provider, family) with ROI.

## Constraints

### Must

- Output the following labeled sections in order: **Encounter Metadata**, **Trigger / Source**, **HI Content**, **Target Identifiability**, **Plan / Means / Preparatory Acts**, **Intent and Egodystonic vs Egosyntonic Type**, **Co-Occurring SI**, **History of Violence**, **Psychotic / Command Phenomena**, **Static / Dynamic / Risk-Management Factors**, **Protective Factors**, **Mental Status**, **Risk Stratification**, **Imminence Decision**, **Duty-to-Protect Analysis** (separate prompt referenced if triggered), **Disposition**, **What Would Change This Stratification**, **Clinical Reasoning Summary**, **Signatures**.
- Distinguish **egodystonic** ("I'm horrified by these thoughts; I'd never act on them") from **egosyntonic** ("I'd be justified; I've been planning when") with explicit client-language quotes.
- For any identifiable target: name, relationship, accessibility, pattern of approach (calls, drives by, social media contact), prior violence toward that target.
- For any plan: specifics (where, when, how), means access (firearms, vehicle weaponization, knives, chemicals), preparatory acts (reconnaissance, weapon acquisition, threats made).
- Risk stratification follows a violence-risk frame, not a suicide-risk frame; static / dynamic / risk-management factors named.
- Duty-to-protect analysis is triggered when: identifiable victim + serious threat of harm + perceived foreseeability — at which point the **separate Tarasoff/duty-to-protect prompt** is referenced.
- Disposition selected from: Outpatient with safety contracting (rare and case-specific) / Outpatient with increased contact / Mobile crisis / ED for evaluation / Law-enforcement notification under duty-to-protect / Civil commitment initiation.
- Document who was contacted and when (target if duty triggers, law enforcement, on-call psychiatry).
- Co-occurring SI evaluated in parallel (homicide-suicide risk).

### Must Not

- Do not collapse target into "people in general" without exploring whether anyone is identifiable.
- Do not treat egodystonic intrusive thoughts (consistent with OCD spectrum) as homicidal ideation requiring duty-to-protect; document the differential.
- Do not omit history of violence or fire-setting / animal cruelty when relevant.
- Do not skip command-AH inquiry when psychotic symptoms are present.
- Do not delegate the duty-to-protect decision to a future visit; document decision-time.
- Do not breach confidentiality before duty criteria are met; conversely, do not fail to act when they are.
- Do not fabricate; flag missing inputs.

## Instructions

1. Compile encounter metadata and trigger.
2. Document HI content in client's own words (quotes preferred).
3. Determine target identifiability: named individual / identifiable group / generic anger.
4. Walk plan, means, preparatory acts, timeline.
5. Categorize ideation: egodystonic intrusive vs egosyntonic anger-congruent (or unclear).
6. Document co-occurring SI and intoxication.
7. Compile violence history: physical violence, DV, weapons, court orders, juvenile.
8. Document psychotic / command phenomena.
9. Apply static / dynamic / risk-management factors per HCR-20 frame (named or descriptive).
10. Document protective factors (treatment alliance, support, no weapons access, no prior violence, ego-dystonia).
11. Compile mental status.
12. Stratify risk; decide imminence; select disposition.
13. Determine whether duty-to-protect analysis is triggered and reference the separate prompt for that determination if so.
14. Document time-stamped contacts (target, law enforcement, on-call psychiatry, ED).
15. State what would change the stratification.
16. Write clinical reasoning summary.
17. Run verification.

## Output Format

```
=== HOMICIDAL IDEATION TRIAGE ===

ENCOUNTER METADATA
Client: [Initials/MRN]    DOB: [age, gender, pronouns]
Date: [YYYY-MM-DD]    Time: [HH:MM]    Setting: [Outpatient / ED / Inpatient / Mobile crisis / Telehealth]
Clinician: [Name, credentials, license #]
On-call / Supervisor: [Name, credentials]

TRIGGER / SOURCE
[Client disclosure / collateral / screening tool / forensic event — what raised concern.]

HI CONTENT
Client's own words: "[quote]"
[Description of thoughts, images, urges; frequency; duration; controllability.]

TARGET IDENTIFIABILITY
Type: [Named individual / Identifiable group (e.g., "people who work in my office") / Generic anger / Mixed]
For named/identifiable target(s):
- Name(s) / role: [...]
- Relationship: [...]
- Current accessibility: [Lives with / works with / can locate / has restraining order / no current contact]
- Pattern of approach: [None / passing thoughts / driving by / messaging / following / direct contact]

PLAN / MEANS / PREPARATORY ACTS
Plan specifics: [Where, when, how — or "no plan, just thoughts"]
Means access:
- Firearms: [...]
- Vehicle: [...]
- Knives / sharps: [...]
- Other: [chemicals, blunt objects, etc.]
Preparatory acts: [Reconnaissance / weapon acquisition / threats issued (verbal, written, online) / final preparations / none]

INTENT AND EGODYSTONIC VS EGOSYNTONIC TYPE
Type: [Egodystonic / Egosyntonic / Unclear / Mixed]
Quoted evidence: "[client's words]"
Differential considerations: [OCD intrusive harm thoughts vs anger-congruent ideation; PTSD-related re-experiencing; psychotic command; antisocial / sadistic ideation]

CO-OCCURRING SI
[Linked Columbia assessment date, current SI status. Homicide-suicide risk consideration if both present.]

HISTORY OF VIOLENCE
- Physical violence (lifetime; recent): [Specifics: dates, severity, victim, charges]
- Domestic violence: [Specifics; current orders of protection]
- Weapons-related charges: [...]
- Incarceration / juvenile history: [...]
- Fire-setting / animal cruelty (especially adolescent): [...]

PSYCHOTIC / COMMAND PHENOMENA
- Active psychosis: [Yes / No]
- Command AH directing violence: [Yes / No — content / loudness / how recent]
- Paranoid beliefs about target: [...]
- Medication adherence: [...]

STATIC / DYNAMIC / RISK-MANAGEMENT FACTORS (HCR-20 frame)
Static (H): [Prior violence; young age at first violent act; relationship instability; employment instability; substance use disorder; major mental disorder; psychopathy features; early maladjustment; personality disorder; prior supervision failure]
Dynamic (C): [Insight problems; negative attitudes; active major mental disorder symptoms; impulsivity; treatment non-adherence]
Risk management (R): [Plan / future destabilizers / non-compliance with intervention plan / stress / lack of supports / future exposure to victim]

PROTECTIVE FACTORS
[Treatment alliance; engagement; absence of means; absence of prior violence; ego-dystonia; family supervision; meaningful future-oriented commitments.]

MENTAL STATUS
[Appearance, behavior, agitation, speech, mood (quoted), affect, thought process, thought content, cognition, insight, judgment.]

RISK STRATIFICATION
Chronic risk: [Low / Moderate / High] — Rationale: [...]
Acute risk: [Low / Moderate / High] — Rationale: [...]
Overall: [Low / Moderate / High]

IMMINENCE DECISION
Imminent risk (next hours-to-days): [Yes / No]
Rationale: [Specific factors — identifiable target + means + plan + intent + agitation; or absence thereof]

DUTY-TO-PROTECT ANALYSIS
Triggered: [Yes / No]
Criteria considered: [Identifiable victim + serious threat of harm + perceived foreseeability]
[If triggered, see separate Tarasoff / duty-to-protect prompt for the formal analysis. Briefly: state-specific framework applied; options considered (warn, hospitalize, treat differently); decision; time and method of any warning made.]

DISPOSITION
Selected: [Outpatient with increased contact / Mobile crisis / ED / Voluntary inpatient / Involuntary hold / Law-enforcement notification under duty-to-protect / Combination]
Time of decision: [HH:MM]
Contacts made:
- [Target — if duty applied — time, method, content of warning]
- [Law enforcement — agency, time, content]
- [On-call psychiatry / supervisor — time, content]
- [Emergency contact — time, content]

WHAT WOULD CHANGE THIS STRATIFICATION
Up: [Acquiring firearm; making contact with target; resumed substance use; psychotic decompensation; loss of supports; specific date approach.]
Down: [Treatment engagement; means restriction verified; target accessibility eliminated; sobriety; psychiatric stabilization.]

CLINICAL REASONING SUMMARY
[3–6 sentences integrating data into stratification, imminence, disposition, and rationale.]

SIGNATURES
Clinician: __________________  Date/Time: ___________
On-call / Supervisor (required for High acute, duty-to-protect, or involuntary hold): __________  Date/Time: ___________
```

## Verification

- [ ] All labeled sections present and in order.
- [ ] Target identifiability explicitly classified.
- [ ] Plan / means / preparatory acts documented.
- [ ] Egodystonic vs egosyntonic explicitly classified with quoted evidence.
- [ ] Co-occurring SI evaluated.
- [ ] Violence history documented.
- [ ] Psychotic / command phenomena addressed.
- [ ] HCR-20 frame applied (or named alternative).
- [ ] Risk stratified for chronic and acute, plus overall.
- [ ] Imminence decided.
- [ ] Duty-to-protect analysis flagged Yes/No; separate prompt referenced if Yes.
- [ ] Disposition selected with time and contacts.
- [ ] What-would-change-stratification documented.
- [ ] Supervisor sign-off for High acute, duty-to-protect, or involuntary actions.
- [ ] Gaps flagged; nothing fabricated.
