---
title: "Naturalization Eligibility Analysis"
category: legal/immigration
description: "Attorney-facing N-400 eligibility and risk analysis — lawful-admission validity, statutory period of residence, continuous residence and trip-by-trip absence analysis, physical presence, state/district residence, good moral character (statutory bars and discretionary factors), English and civics, and attachment — with a mandatory removability screen before filing and every period, bar, and test version marked for verification."
techniques:
  - RT-02
  - CM-02
  - QA-04
  - QA-01
difficulty: advanced
tags:
  - legal
  - immigration
  - naturalization
  - n-400
  - good-moral-character
  - continuous-residence
  - removability-screen
  - becoming-citizen
updated: "2026-09-24"
reasoning:
  styles: [analytic, protective, systematic]
  stakes: critical
  horizon: weeks
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: regulated
  collaboration: solo_or_team
  output_format: [structured, matrix]
  user_role: [lawyer]
  mode: [assess, audit]
related_prompts:
  - domain-legal/immigration/legal_i589_asylum_declaration_framework.md
  - domain-legal/immigration/legal_eb1_extraordinary_ability_petition.md
  - domain-legal/client-intake-communications/legal_new_matter_intake_summary.md
  - domain-legal/research/legal_statutory_interpretation.md
---

# Naturalization Eligibility Analysis

**Objective:** Tell counsel whether a lawful permanent resident client is eligible to file for naturalization now, when they will become eligible if not, and — before anything else — whether filing would expose the client to removal. The analysis starts with a removability and admission-validity screen, then tests each statutory requirement against documented facts: the applicable residence period, continuous residence trip by trip, physical presence, state or district residence, good moral character during the statutory period (bars and discretion), English and civics, and attachment to the Constitution. Every period, bar, and test version is marked for verification.

> **Scope guard — attorney-facing only.** For immigration counsel or accredited representatives. It does not advise an individual whether to apply. If the person running it is the applicant, stop and route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md` — filing without a removability screen can put permanent residence at risk.

**When to use:**
- Intake for a naturalization matter.
- Re-evaluation after travel, an arrest or charge, a tax problem, or a change in marital status.
- Preparing for the interview after an application is filed.

**Distinct from:**
- `domain-legal/client-intake-communications/legal_new_matter_intake_summary.md` — generic intake; this is the substantive eligibility and risk analysis.
- Removal-defense and crimmigration analysis — this prompt flags criminal and fraud issues for specialist review; it does not decide immigration consequences of convictions.
- Derivative and acquired citizenship (through parents) — a different analysis; flag if the facts suggest the client may already be a citizen.

**Audience:** Immigration attorneys and supervised legal staff.

---

## Your Input

- **Admission to LPR status:** [Date, category, how obtained (consular / adjustment), any conditional residence and removal-of-conditions status]
- **Basis for filing:** [General residence period / spouse of U.S. citizen / military / other — with marital facts if spousal]
- **Travel history:** [Every trip outside the U.S. in the statutory period with departure and return dates — from passport stamps, travel records, or a records request]
- **Residence history:** [Addresses and dates; current state or USCIS district and time there]
- **Criminal history:** [Every arrest, citation, charge, and disposition anywhere, including expunged or sealed records]
- **Other GMC facts:** [Tax filing history, child support, selective service registration (if applicable), voting or claims to citizenship, false testimony, public benefits, immigration history issues]
- **English / civics:** [Language ability; age and years as LPR for exemptions; disability waiver facts]
- **Current rules you have verified:** [Statutory periods, early-filing window, civics test version in use, current policy guidance — or leave blank for `[VERIFY]`]

---

## Constraints

### Must
- Run the **removability and admission screen first**: Was LPR status lawfully obtained (fraud, ineligibility at adjustment, conditional status unresolved)? Does any criminal, immigration, or false-claim history make the client removable? If any flag appears, **stop the eligibility analysis at "Refer for specialist review before filing."**
- Identify the **statutory residence period** that applies `[VERIFY: INA §316(a), §319(a), military provisions]` and the earliest filing date including any early-filing window `[VERIFY]`.
- Analyze **continuous residence trip by trip**: absences over the thresholds that create a rebuttable presumption of a break or break continuity outright `[VERIFY: 8 CFR 316.5(c)]`, with rebuttal evidence (kept job, home, taxes, family) and any preservation filing.
- Compute **physical presence** days from the travel log; show the arithmetic `[VERIFY: required fraction of period]`.
- Test **state / district residence** duration `[VERIFY]`.
- Separate **good moral character** into statutory bars `[VERIFY: INA §101(f); 8 CFR 316.10]`, regulatory bars, and discretionary factors, limited to the statutory period but noting conduct outside it that may be considered.
- Flag **English and civics** requirements, exemptions, and the test version in use `[VERIFY: current test version]`.
- Present a **status**: Eligible now / Eligible on {date} / Not eligible / Refer before filing.

### Must Not
- Compute periods or thresholds without the `[VERIFY]` tag unless the user supplied verified rules.
- Treat expunged, sealed, or dismissed matters as irrelevant — disclosure obligations and immigration consequences differ from criminal-law effects; flag for specialist review.
- Decide the immigration consequences of any criminal disposition; refer.
- Assume travel dates from memory or estimates when records can be obtained; mark estimates as such.
- Communicate with the client or recommend filing without counsel's review of the screen.

---

## Instructions

1. **Removability and admission screen** → proceed or refer.
2. **Basis and statutory period** → earliest filing date.
3. **Travel log** → trip-by-trip continuous-residence analysis with presumption and rebuttal evidence.
4. **Physical presence** arithmetic.
5. **State / district residence.**
6. **Good moral character** → bars, then discretionary factors; statutory-period dates stated.
7. **English and civics** → requirement, exemption, accommodation.
8. **Attachment / oath** issues (e.g., oath modifications).
9. **Status and next steps** → documents to gather, records requests, and timing.

---

## Output Format

```markdown
# Naturalization Eligibility Analysis — {Client initials} — A-{…}
**LPR since:** {date}  |  **Basis:** {…}  |  **Prepared:** {date}  |  **Attorney Work Product**

## 0. Removability and Admission Screen
| Issue | Facts | Flag (Yes / No / Unknown) | Action |
**Screen result:** {Proceed / Refer for specialist review before filing}

## 1. Statutory Period and Earliest Filing Date   [VERIFY]
## 2. Continuous Residence
| Trip | Depart | Return | Days out | Threshold implicated [VERIFY] | Rebuttal evidence |
## 3. Physical Presence
{days in U.S. / days required — arithmetic}
## 4. State / District Residence
## 5. Good Moral Character
| Category | Facts | Bar or discretionary | Within statutory period? | Assessment |
## 6. English and Civics
## 7. Attachment / Oath
## 8. Status: {Eligible now / Eligible on {date} / Not eligible / Refer before filing}
## 9. Next Steps and Documents
```

---

## Worked Example

**Input (abridged):** LPR since 2021-02-15 (adjustment through employment). Basis: general residence period. Travel: 2022 trip of 7 months (kept U.S. job remotely, apartment, filed resident tax returns); four short trips totaling 50 days. One 2023 arrest for driving with a suspended licence, dismissed. No tax issues. Resident in current state since 2019.

**Output (excerpt):**

> **0. Screen:** Adjustment facts appear regular. 2023 arrest, dismissed — disclosure required on the application regardless of dismissal; immigration consequences appear low on these facts but confirm with certified disposition. **Proceed**, with certified disposition obtained before filing.
>
> **1. Period:** If the general period is five years `[VERIFY: §316(a)]`, the client completes five years as an LPR on 2026-02-15, with an early-filing window before that date `[VERIFY: early-filing rule]`. The continuous-residence, physical-presence, and good-moral-character periods are measured as **the 5 years before filing on {filing date}** — not from the LPR date — so every count below is recomputed once the filing date is fixed, and the travel log must cover that whole window.
>
> **2. Continuous residence:** 7-month trip exceeds the six-month threshold that raises a rebuttable presumption of a break but is under one year `[VERIFY: 8 CFR 316.5(c)(1)]`. Rebuttal evidence: continued U.S. employment, retained apartment, resident tax filings — **likely rebuttable**; gather employer letter, lease, and returns.
>
> **3. Physical presence:** ~213 days (7-month trip) + 50 days = ~263 days abroad of ~1,826 in the 5 years before filing on {filing date} (assuming all listed trips fall in that window) → ~1,563 days present, above half (~913) `[VERIFY: fraction]`; replace estimates with records.
>
> **8. Status:** Eligible now (period has run as of the prepared date), subject to verification of rebuttal evidence and certified disposition.

---

## Verification

- [ ] Jurisdiction lock: federal naturalization law; USCIS district identified.
- [ ] Removability and admission screen completed first; referral triggered where flagged.
- [ ] Statutory period and earliest filing date computed and tagged `[VERIFY]`.
- [ ] Every trip analyzed; presumptions and rebuttal evidence stated.
- [ ] Physical presence arithmetic shown.
- [ ] GMC separated into bars and discretionary factors with period dates.
- [ ] English / civics requirement and test version tagged `[VERIFY]`.
- [ ] No immigration consequences of criminal dispositions decided; no advice to the client.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Starting with eligibility instead of the removability screen | Screen first; filing can expose a removable LPR |
| Treating expunged or dismissed matters as non-disclosable | Disclosure and immigration effects differ; flag and obtain dispositions |
| Collapsing continuous residence and physical presence | They are separate tests with separate arithmetic |
| Treating a 6–12 month absence as an automatic break | It raises a rebuttable presumption; analyze rebuttal evidence |
| Using estimated travel dates as final | Replace with records; mark estimates |
| Ignoring whether the client may already be a citizen by derivation | Flag parental-citizenship facts for separate analysis |
| Stating periods, fractions, or test versions from memory | Tag `[VERIFY]` unless supplied |
