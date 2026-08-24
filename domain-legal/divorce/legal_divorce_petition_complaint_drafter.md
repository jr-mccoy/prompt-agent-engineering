---
title: "Divorce Petition / Complaint Drafter"
category: legal/divorce
description: "Draft a petition (complaint) for dissolution of marriage with caption, residency and subject-matter jurisdiction allegations, grounds (no-fault and/or fault), identification of marital and separate property and debts, child and custody allegations with UCCJEA pleading, and a prayer for relief — sized to the controlling state's dissolution statute and local court rules."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - legal
  - divorce
  - family-law
  - petition
  - pleading
  - dissolution
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_divorce_intake_and_case_assessment.md
  - domain-legal/divorce/legal_divorce_response_and_counterpetition_drafter.md
  - domain-legal/divorce/legal_temporary_orders_pendente_lite_motion.md
  - domain-legal/custody/legal_uccjea_jurisdiction_analysis.md
  - domain-legal/litigation/legal_complaint_drafter.md
---

**Purpose:** Draft a filing-ready petition/complaint for dissolution that establishes the court's jurisdiction, pleads residency and grounds, identifies the estate and the children, and states the relief requested. Output is a captioned pleading conformed to the controlling state and local rules — not a memo.

**When to use:** Initiating a dissolution, legal separation, or annulment; converting a legal separation to dissolution; drafting after intake and conflict clearance.

---

## Your Input

- **Jurisdiction:** [State; county; specific court (e.g., Superior Court, Family Division); local rule set]
- **Property regime:** [Community-property / equitable-distribution state]
- **Relief type:** [Dissolution / legal separation / annulment]
- **Petitioner / Respondent:** [Names, residence addresses (or confidential-address request if DV), service info]
- **Residency facts:** [Durational residency satisfied by which party; dates]
- **Marriage facts:** [Date and place of marriage; date of separation if pleaded]
- **Grounds:** [No-fault language used in the state; fault grounds if pleaded and supported]
- **Children:** [Names, ages, current residence, existing orders; UCCJEA residence history for past 5 years]
- **Property & debts:** [Items to be characterized and divided; what is alleged separate]
- **Relief requested:** [Dissolution; property division; spousal support; child custody and support; name restoration; attorney's fees; other]
- **Required attachments:** [State-mandated forms — UCCJEA declaration, summons, confidential information sheet, fee waiver]

---

## Constraints

**Must:**
- Use the **controlling state's caption and pleading format** and the state's statutory grounds language; do not import another state's terms.
- Plead **residency/durational jurisdiction** with the qualifying party and dates `[CITE: …]`.
- Plead **subject-matter and personal jurisdiction** over the respondent (service, long-arm, or appearance).
- For children, include the **UCCJEA allegations** (residence history, other proceedings, persons claiming custody) required to invoke custody jurisdiction.
- Identify property and debts at the level the state requires (some require itemization; some allow general allegation with later disclosure); allege which property is **separate**.
- State a **prayer for relief** that requests every form of relief the petitioner may want; relief not requested may be unavailable.
- Note any **mandatory attachments and service requirements** for the jurisdiction.
- Where a party requests address confidentiality (DV), use the state's confidential-address procedure.
- Use placeholders `[CITE: ...]`, `[NEED: ...]` for any statute, residency period, grounds text, or fact not supplied.

**Must Not:**
- Invent statutory grounds language, residency periods, code section numbers, dates, or property values.
- Plead fault grounds without a supplied factual basis, or where the state is pure no-fault.
- Omit UCCJEA allegations when children are involved (it can defeat custody jurisdiction).
- Disclose a protected party's address where confidentiality applies.
- Over-plead specific dollar values that will bind the petitioner before disclosure; allege division/valuation "to be determined."
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Caption & parties.** Court, county, case-number placeholder, party designations (Petitioner/Respondent or Plaintiff/Defendant per the state), attorney block.
2. **Jurisdiction & residency.** Allege the durational residency met by the qualifying party with dates `[CITE: …]`; allege the basis for personal jurisdiction over the respondent.
3. **Marriage facts.** Date and place of marriage; date of separation if the state recognizes it.
4. **Grounds.** State the no-fault ground in the state's exact statutory phrasing; add fault grounds only if supplied and supported.
5. **Children & UCCJEA.** Allege children, residence history for the UCCJEA lookback, other custody proceedings, and persons with custody claims; request custody/parenting orders.
6. **Property & debts.** Allege existence of marital/community and separate property and debts at the required level; reserve characterization, valuation, and division for disclosure/trial.
7. **Support.** Allege grounds for spousal support and child support as applicable.
8. **Prayer for relief.** Enumerate all relief requested.
9. **Verification & signature.** Add the state-required verification/declaration and attorney signature block.
10. **Attachments checklist.** List mandatory forms and the service plan.

---

## Output Format

```markdown
{STATE} {COURT}, COUNTY OF {COUNTY}, {FAMILY DIVISION}

In re the Marriage of:
{PETITIONER},        Petitioner,                Case No. ____________
   and
{RESPONDENT},        Respondent.                PETITION FOR {DISSOLUTION OF MARRIAGE / LEGAL SEPARATION / ANNULMENT}

Petitioner alleges:

1. RESIDENCY & JURISDICTION. {Party} has been a resident of {State} for {period} and of {County} for {period} preceding filing, satisfying {statute [CITE: …]}. The Court has jurisdiction over the subject matter and over Respondent by {service / appearance / long-arm}.

2. MARRIAGE. The parties were married on {date} at {place}. The parties separated on {date}. [if recognized]

3. GROUNDS. {Statutory no-fault ground in state's exact language} [CITE: …]. {Fault ground + factual basis, if pleaded.}

4. CHILDREN & UCCJEA. The following minor children were born of/adopted into the marriage: {name, DOB}. UCCJEA: the children have resided at {addresses, dates, persons} during the past five years; {no other / the following} custody proceeding exists. Petitioner requests {legal/physical custody and parenting time} per the children's best interests.

5. PROPERTY & DEBTS. The parties have acquired {community/marital} property and debts subject to division, and Petitioner asserts the following is separate property: {…}. Characterization, valuation, and division are reserved for disclosure and determination by the Court.

6. SUPPORT. Petitioner {requests / reserves the right to request} spousal support and child support as provided by law [CITE: …].

WHEREFORE, Petitioner prays the Court:
   a. Dissolve the marriage / grant legal separation / annul;
   b. Divide marital/community property and debts and confirm separate property;
   c. Award spousal support as appropriate;
   d. Enter custody and parenting-time orders in the children's best interests;
   e. Order child support per guideline [NEED GUIDELINE: …];
   f. Restore {Petitioner}'s former name to {name};
   g. Award attorney's fees and costs as provided by law;
   h. Grant such other relief as the Court deems just.

{Verification / declaration under penalty of perjury as required by {State}}
{Attorney name, bar no., firm, contact}   /   {Self-represented, if applicable}

Attachments: {Summons; UCCJEA declaration; Confidential information sheet; [DV confidential address request]; Fee waiver [if applicable]}
```

---

## Verification

- [ ] Caption and party designations conform to the state/court.
- [ ] Residency/durational requirement pleaded with qualifying party and dates [CITE].
- [ ] Personal and subject-matter jurisdiction alleged.
- [ ] Grounds use the state's exact statutory language; fault pleaded only if supported.
- [ ] UCCJEA allegations present and complete when children are involved.
- [ ] Property/debt allegations at the state-required level; separate property asserted; values not prematurely bound.
- [ ] Prayer for relief requests all desired relief (including name restoration and fees).
- [ ] Verification/declaration and signature block included; mandatory attachments listed.
- [ ] Confidential-address procedure used where a DV party requires it.
- [ ] No invented statutes, residency periods, grounds text, dates, or values.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Importing another state's grounds language or "complaint" vs. "petition" terminology | Use the controlling state's exact pleading nomenclature and statutory grounds |
| Pleading fault in a pure no-fault state, or fault without a factual basis | Use the state's no-fault ground; plead fault only where available and supported |
| Omitting UCCJEA allegations with minor children | Include residence history, other proceedings, and custody claimants to invoke custody jurisdiction |
| Reciting specific asset values that will bind the petitioner pre-disclosure | Reserve characterization/valuation/division for disclosure and trial |
| Forgetting to request name restoration, fees, or support in the prayer | Enumerate all relief; unrequested relief may be waived |
| Disclosing a DV party's residential address | Use the state's confidential-address request procedure |
| Inventing the residency period or code section | Use [CITE]/[NEED] placeholders for unsupplied statutory references |
| Filing without the state's mandatory attachments (UCCJEA declaration, summons) | List and attach all required forms; confirm service method |
| Alleging jurisdiction over respondent without a basis | Plead service, appearance, or long-arm grounds |
| Treating legal separation and dissolution prayers identically | Tailor the relief and grounds to the relief type selected |
