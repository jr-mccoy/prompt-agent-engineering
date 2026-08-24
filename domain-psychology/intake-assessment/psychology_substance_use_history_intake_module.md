---
title: "Substance Use History Intake Module"
category: psychology/intake-assessment
description: "Per-substance history intake module with AUDIT and DAST-10 scoring interpretation, withdrawal risk screening, and ASAM criteria framing for level-of-care determination."
techniques:
  - ST-04
  - DT-02
  - CM-02
  - QA-04
  - RT-02
difficulty: intermediate
intended_use: model-testing
tags:
  - substance-use
  - AUDIT
  - DAST-10
  - ASAM
  - SUD
  - withdrawal
  - DSM-5-TR
  - level-of-care
  - intake
  - cpt-90791
  - cpt-90792
updated: "2026-06-08"
related_prompts:
  - domain-psychology/documentation/psychology_intake_assessment_note.md
  - domain-psychology/intake-assessment/psychology_screening_battery_interpreter.md
  - domain-psychology/intake-assessment/psychology_psychiatric_history_compiler.md
  - domain-psychology/risk-crisis/psychology_columbia_suicide_risk_assessment.md
---

# Substance Use History Intake Module

## Objective

Compile a per-substance history that:

1. Covers each substance class individually: alcohol, cannabis, stimulants, opioids, benzodiazepines/sedatives, cocaine/crack, hallucinogens, inhalants, and other/polydrug.
2. Incorporates AUDIT score interpretation (if administered) and DAST-10 interpretation (if administered), cross-referenced with clinical interview findings.
3. Screens for withdrawal risk with clinical urgency flags for alcohol and benzodiazepine withdrawal (the two life-threatening withdrawal syndromes).
4. Maps the presentation to DSM-5-TR Substance Use Disorder criteria (mild / moderate / severe) for each applicable substance.
5. Applies the ASAM (American Society of Addiction Medicine) six-dimension criteria framework to support level-of-care determination.
6. Produces a Substance Use History section ready for insertion into the 90791/90792 biopsychosocial intake note.

## When to Use

- At any psychiatric or behavioral health intake where substance use history is a required assessment domain — which includes all intakes per Joint Commission and CARF standards.
- When AUDIT Zone II–IV (8+) or DAST-10 ≥ 3 was obtained on screening.
- When the chief complaint or referral source indicates SUD, withdrawal, or co-occurring concerns.
- As a standalone SUD evaluation supplement when a prior intake note lacked structured substance use documentation.

## Inputs / Context Required

Provide available data for each substance class. Mark substances as "denied" or "not assessed" rather than leaving blank — this distinction matters for documentation completeness.

- **Per substance:**
  - Age of first use.
  - Current use frequency and quantity (standard drinks/day or week, grams, mg, times per week).
  - Route of administration (oral, inhaled, smoked, intranasal, injected).
  - Last use date and amount.
  - Longest period of abstinence and circumstances.
  - Context of heaviest use (triggered by stress, trauma, mood episode, social context).
  - Tolerance: need for markedly increased amounts to achieve same effect, or diminished effect with same amount.
  - Withdrawal history: prior withdrawal symptoms, prior withdrawal complications (seizures, delirium tremens, autonomic instability).
  - Prior SUD treatment: detox, MAT, IOP/PHP, residential, AA/NA/SMART, medication (naltrexone, buprenorphine, methadone, acamprosate, disulfiram — with dates and compliance).
  - Perceived control: client's assessment of ability to cut down or stop.
  - Impact on functioning: work, relationships, legal, financial, health.

- **AUDIT score** (0–40): Full 10-item if available. Note if AUDIT-C (3-item) was substituted.
- **DAST-10 score** (0–10): For non-alcohol substances.
- **IV drug use history:** If any injection use, date of most recent injection, sharing paraphernalia, HIV/HCV testing recency.
- **Overdose history:** Substances involved, year, whether Narcan was used, hospitalization.
- **Family history of SUD.**

## Constraints

### Must

- Complete a per-substance table for each substance class; mark "denied" explicitly — do not leave cells blank.
- Interpret AUDIT scores using validated Zone categories: Zone I (0–7, low risk), Zone II (8–15, hazardous), Zone III (16–19, harmful), Zone IV (20–40, dependence likely). Note whether the 10-item AUDIT or AUDIT-C was used; do not apply AUDIT-C cutoffs to AUDIT-10 bands.
- Interpret DAST-10 scores using validated severity levels: 0 (no problem), 1–2 (low), 3–5 (moderate), 6–8 (substantial), 9–10 (severe).
- Screen explicitly for alcohol and benzodiazepine/sedative-hypnotic withdrawal risk; flag CIWA-Ar (Clinical Institute Withdrawal Assessment for Alcohol) level urgency if current daily or near-daily use with abrupt reduction. These two syndromes carry seizure and mortality risk.
- Apply DSM-5-TR SUD criteria for each substance where use is present: 2–3 of 11 criteria = mild; 4–5 = moderate; 6+ = severe. List which criteria are met or endorsed.
- Apply the ASAM six-dimension framework for level-of-care narrative: Dimension 1 (Acute Intoxication / Withdrawal Potential), Dimension 2 (Biomedical), Dimension 3 (Emotional/Behavioral/Cognitive), Dimension 4 (Readiness to Change), Dimension 5 (Relapse/Continued Use Potential), Dimension 6 (Recovery/Living Environment).
- Note IV drug use with HIV/HCV risk assessment if relevant.
- Note any overdose history with clinical detail.

### Must Not

- Do not use the term "drug abuse" (per DSM-5-TR revision to "substance use disorder"); use SUD or substance use.
- Do not present AUDIT or DAST-10 scores as diagnoses — they are screening tools flagging probable clinical range, not DSM criteria.
- Do not assume route of administration; document what the client reported.
- Do not omit the withdrawal risk screen for alcohol and benzodiazepines; the omission carries clinical risk.
- Do not apply adult norms to adolescent substance use inquiry without noting age-adjusted developmental context.
- Do not fabricate; flag gaps.

## Instructions

1. **Complete the per-substance table.** For each substance class, document the variables listed above. Mark each substance as: never used / used in past (specify most recent year) / current use.

2. **Interpret AUDIT and DAST-10.** Apply validated bands. Note discrepancies between self-report and screening score (e.g., client minimizing on interview vs. AUDIT Zone III suggesting probable dependence).

3. **Screen for withdrawal risk.** For alcohol: estimate average daily consumption, date of last drink, and any history of seizures, DTs, or prior complicated withdrawal → assess CIWA-Ar urgency tier. For benzodiazepines: dosage, frequency, duration of use, prescription vs. non-prescription. If withdrawal risk is present, generate a clinical urgency flag.

4. **Apply DSM-5-TR SUD criteria.** For each substance where use is current or recent, enumerate which of the 11 criteria are met. Determine severity (mild / moderate / severe). Include ICD-10 code if determinable.

5. **Complete ASAM six-dimension narrative.** Each dimension should have a brief entry based on the history gathered; gaps flagged.

6. **Compute SUD treatment history summary.** Note what has been tried, what worked, and clinical factors relevant to current LOC determination.

7. **List action items.** Include withdrawal medically supervised detox urgency (if applicable), MAT consideration, and LOC recommendation.

8. **Run verification.**

## Output Format

```
=== SUBSTANCE USE HISTORY ===

Client: [Initials/MRN]    Date of Service: [YYYY-MM-DD]
AUDIT Administered: [Yes — score X / No]    DAST-10 Administered: [Yes — score X / No]
CPT: [90791 | 90792]

─────────────────────────────────────────
PER-SUBSTANCE TABLE
─────────────────────────────────────────
| Substance       | Status        | Age 1st Use | Current Freq/Qty | Route     | Last Use   | Withdrawal Hx | Prior Tx |
|-----------------|---------------|-------------|------------------|-----------|------------|---------------|----------|
| Alcohol         | [Current / Past / Denied] | [X] | [X drinks/day]  | [Oral]    | [YYYY-MM-DD] | [Y/N — complications] | [Y/N] |
| Cannabis        | [...]         | [...]       | [...]            | [Smoked / vaped / edible] | [...] | [Y/N] | [Y/N] |
| Stimulants (Rx ADHD) | [...]  | [...]       | [...]            | [Oral]    | [...]      | [Y/N]         | [Y/N] |
| Stimulants (illicit: methamphetamine, cocaine powder) | [...] | [...] | [...] | [...] | [...] | [Y/N] | [Y/N] |
| Crack / cocaine | [...]         | [...]       | [...]            | [Smoked / intranasal / IV] | [...] | [Y/N] | [Y/N] |
| Opioids (Rx)    | [...]         | [...]       | [mg/day — medication name] | [Oral] | [...] | [Y/N] | [Y/N] |
| Opioids (illicit: heroin, fentanyl, pills) | [...] | [...] | [...] | [Oral / intranasal / IV] | [...] | [Y/N] | [Y/N] |
| Benzodiazepines / sedative-hypnotics | [...] | [...] | [Rx: mg/day / Non-Rx] | [Oral] | [...] | [Y/N — seizures / DTs] | [Y/N] |
| Hallucinogens   | [...]         | [...]       | [...]            | [Oral / inhaled] | [...] | [N/A]  | [Y/N] |
| MDMA / ecstasy  | [...]         | [...]       | [...]            | [Oral]    | [...]      | [N/A]         | [Y/N] |
| Inhalants       | [...]         | [...]       | [...]            | [Inhaled] | [...]      | [N/A]         | [Y/N] |
| Other / polydrug | [...]        | [...]       | [...]            | [...]     | [...]      | [Y/N]         | [Y/N] |

IV Drug Use History: [Never / Past — last injection: date / Current — date, paraphernalia sharing Y/N]
HIV/HCV Testing: [Date of most recent test / Not tested — recommend]
Overdose History: [None / Year, substances, Narcan used Y/N, hospitalized Y/N]
Family SUD History: [...]

─────────────────────────────────────────
AUDIT INTERPRETATION
─────────────────────────────────────────
Form used: [AUDIT-10 / AUDIT-C — note if substituted]
Score: [X]
Zone: [Zone I (0–7): Low risk / Zone II (8–15): Hazardous use /
Zone III (16–19): Harmful use / Zone IV (20–40): Probable dependence]
Clinical interpretation: [One sentence — align with interview report; note any discrepancy]
AUDIT-C (if substituted): [Score X — cutoffs: ≥ 3 women / ≥ 4 men positive screen for hazardous use]

─────────────────────────────────────────
DAST-10 INTERPRETATION
─────────────────────────────────────────
Score: [X / 10]
Severity: [0: No problem / 1–2: Low / 3–5: Moderate / 6–8: Substantial / 9–10: Severe]
Clinical interpretation: [One sentence — align with per-substance interview data]

─────────────────────────────────────────
⚠️ WITHDRAWAL RISK SCREEN
─────────────────────────────────────────
ALCOHOL WITHDRAWAL RISK:
  Daily / near-daily use with abrupt cessation or reduction: [Yes / No]
  Last drink: [Date and time]
  History of complicated withdrawal (seizures, DTs, autonomic instability): [Yes / No]
  CIWA-Ar urgency tier: [Low — monitor outpatient / Moderate — medical monitoring warranted /
  High — medically supervised detox required / Emergent — acute medical evaluation now]
  Action: [Medically supervised detox referral / CIWA-Ar formal assessment / Monitor /
  Not indicated]

BENZODIAZEPINE / SEDATIVE-HYPNOTIC WITHDRAWAL RISK:
  Daily use > 4 weeks with abrupt cessation risk: [Yes / No]
  Current dose and medication: [...]
  History of benzo withdrawal complications: [Yes / No]
  Action: [Taper planning / Medically supervised detox / Prescriber consultation / Not indicated]

OPIOID WITHDRAWAL RISK (COWS consideration):
  Physical dependence indicators: [Yes / No]
  COWS assessment indicated: [Yes / No]
  MAT consideration: [Buprenorphine / Methadone / Extended-release naltrexone — note eligibility]

─────────────────────────────────────────
DSM-5-TR SUD CRITERIA SUMMARY
─────────────────────────────────────────
[For each primary substance:]

[Substance Name] Use Disorder:
  DSM-5-TR Criteria endorsed (of 11):
  1. Taking in larger amounts / longer than intended: [Yes / No]
  2. Persistent desire or unsuccessful efforts to cut down: [Yes / No]
  3. Great deal of time obtaining / using / recovering: [Yes / No]
  4. Craving: [Yes / No]
  5. Failure to fulfill major role obligations: [Yes / No]
  6. Continued use despite social / interpersonal problems: [Yes / No]
  7. Important activities given up: [Yes / No]
  8. Use in physically hazardous situations: [Yes / No]
  9. Continued use despite known physical / psychological problem: [Yes / No]
  10. Tolerance: [Yes / No]
  11. Withdrawal: [Yes / No]
  Total criteria met: [X / 11]
  Severity: [Mild (2–3) / Moderate (4–5) / Severe (6–11)]
  Provisional ICD-10: [F1X.XX]

─────────────────────────────────────────
ASAM SIX-DIMENSION NARRATIVE
─────────────────────────────────────────
Dimension 1 — Acute Intoxication / Withdrawal Potential:
  [Current intoxication status; withdrawal risk tier per screen above; medical urgency]

Dimension 2 — Biomedical Conditions and Complications:
  [Medical conditions affected by substance use; IV-associated infections; hepatic/cardiac/
  neurological complications; pregnancy; pain]

Dimension 3 — Emotional, Behavioral, and Cognitive Conditions:
  [Co-occurring psychiatric diagnoses; cognitive impact of substance use; behavioral patterns;
  emotional dysregulation driven by use]

Dimension 4 — Readiness to Change:
  [Client's stage (precontemplation / contemplation / preparation / action / maintenance);
  motivation level; expressed goals for substance use]

Dimension 5 — Relapse, Continued Use, or Continued Problem Potential:
  [Triggers identified; prior relapse patterns; high-risk situations; protective factors;
  longest sobriety and what sustained it]

Dimension 6 — Recovery and Living Environment:
  [Housing stability; supportive vs. using-peer social network; employment;
  family/community support; access to recovery resources]

─────────────────────────────────────────
LEVEL-OF-CARE INDICATION
─────────────────────────────────────────
Recommended LOC based on ASAM criteria: [Outpatient (Level 1) / Intensive Outpatient (Level 2.1) /
Partial Hospitalization (Level 2.5) / Residential (Levels 3.1–3.7) /
Medically Managed Residential (Level 4) / Medically supervised detox]
Rationale: [Which ASAM dimensions drive the recommendation]
Immediate action items:
1. [Highest urgency — withdrawal / medical / safety]
2. [MAT evaluation if indicated]
3. [LOC placement coordination]
4. [...]

─────────────────────────────────────────
BILLING NOTE
─────────────────────────────────────────
SUD history documented as part of CPT [90791 | 90792].
AUDIT and DAST-10 scores documented in Outcome Measures section.
Medical necessity statement: [One sentence connecting SUD findings to diagnosis and LOC need].
```

## Verification

- [ ] Per-substance table complete with all substance classes listed — "denied" explicit, no blanks.
- [ ] AUDIT interpreted using validated Zone categories; form (AUDIT-10 vs. AUDIT-C) specified.
- [ ] DAST-10 interpreted using validated severity levels.
- [ ] Alcohol withdrawal risk screen completed with CIWA-Ar urgency tier noted.
- [ ] Benzodiazepine/sedative withdrawal risk screen completed.
- [ ] Opioid withdrawal screen and MAT consideration noted if relevant.
- [ ] DSM-5-TR SUD criteria enumerated for each primary substance with severity and ICD-10 code.
- [ ] ASAM six-dimension narrative present for all six dimensions.
- [ ] Level-of-care recommendation with ASAM rationale included.
- [ ] IV drug use and HIV/HCV testing status documented if applicable.
- [ ] Overdose history documented (present or absent).
- [ ] AUDIT and DAST-10 not used as diagnoses — screening vs. diagnosis distinction maintained.
- [ ] Gaps flagged with `[clinician input required: ...]`.
