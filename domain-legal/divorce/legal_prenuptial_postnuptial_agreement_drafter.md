---
title: "Prenuptial / Postnuptial Agreement Drafter"
category: legal/divorce
description: "Draft a premarital (prenuptial) or marital (postnuptial) agreement under the controlling state's framework (UPAA/UPMAA or state-specific law): recitals and full financial disclosure schedules, separate vs. marital property definitions, treatment of appreciation and income, spousal-support waiver or terms (with enforceability caveats), estate/death provisions, and the procedural safeguards (independent counsel, voluntariness, time to review) that make it enforceable."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - divorce
  - family-law
  - prenuptial
  - postnuptial
  - marital-agreement
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_prenup_postnup_enforceability_analysis.md
  - domain-legal/divorce/legal_marital_property_characterization_analysis.md
  - domain-legal/divorce/legal_marital_settlement_agreement_drafter.md
  - domain-legal/divorce/legal_spousal_support_alimony_analysis.md
  - domain-legal/contracts-transactional/legal_nda_mutual_drafter.md
---

**Purpose:** Draft a prenuptial or postnuptial agreement that defines property and support rights and is structured to withstand a later enforceability challenge — with full disclosure, clear definitions, and the procedural safeguards the state requires. Output is a full agreement plus disclosure schedules, not a memo.

**When to use:** Engaged or married parties defining separate property, income, appreciation, and support; protecting a business, premarital assets, or children of a prior marriage; converting an informal understanding into an enforceable agreement.

---

## Your Input

- **Jurisdiction:** [State; whether it follows UPAA/UPMAA or state-specific law; the state's enforceability requirements `[CITE: …]`]
- **Agreement type:** [Prenuptial (premarital) / postnuptial (marital)]
- **Parties & timing:** [Names; wedding date if prenup; how far in advance the agreement is being signed]
- **Each party's finances:** [Assets, debts, income — for the disclosure schedules]
- **Separate-property goals:** [Premarital assets, business, inheritance, gifts to keep separate]
- **Appreciation/income treatment:** [Whether appreciation of and income from separate property stays separate]
- **Support terms:** [Waiver, cap, or formula for spousal support — note enforceability limits]
- **Estate provisions:** [Waiver of elective share/death rights; coordination with wills/trusts]
- **Counsel:** [Whether each party has or will have independent counsel]

---

## Constraints

**Must:**
- Identify the state's framework (**UPAA/UPMAA or state law**) and the **enforceability requirements** — voluntariness, **full and fair financial disclosure (or knowing waiver)**, no unconscionability, and any **independent-counsel/time-to-review** expectations `[CITE: …]`.
- Attach **disclosure schedules** for each party (assets, debts, income) and recite the disclosure and the right to independent counsel.
- Define **separate vs. marital property** clearly, including the treatment of **appreciation and income** from separate property and **commingling/transmutation** rules the parties choose.
- Address **spousal support** with an explicit caveat that **support waivers face heightened scrutiny** and may be unenforceable if unconscionable at enforcement (state-dependent); never waive **child support** (it cannot be bargained away).
- Address **estate/death rights** (elective share waiver) where intended, coordinated with estate documents.
- Build in **procedural safeguards**: signing well in advance (for prenups), voluntariness recital, separate counsel, and absence of duress.
- Note **postnuptial-specific** concerns (consideration, heightened scrutiny in some states).
- Use placeholders `[CITE: ...]`, `[NEED: ...]` for unsupplied authority, schedules, or facts.

**Must Not:**
- Purport to waive or limit **child support or custody** rights — they cannot be contracted away.
- Omit the financial-disclosure schedules or the disclosure recital.
- Present a spousal-support waiver as certainly enforceable.
- Invent the state's enforceability standard or case law.
- Draft a same-day, no-counsel prenup without flagging the duress/voluntariness risk.
- Insert generic "consult counsel" disclaimers (but DO require independent counsel as a substantive safeguard).

---

## Instructions

1. **Framework & requirements.** State the governing framework and enforceability requirements `[CITE: …]`.
2. **Recitals & disclosure.** Parties, purpose, disclosure exchange, independent counsel, voluntariness, timing.
3. **Property definitions.** Define separate and marital property; treatment of appreciation, income, commingling, and transmutation.
4. **Property on dissolution/death.** State how property is divided on divorce and what each waives at death (elective share).
5. **Spousal support.** State the support term/waiver with the enforceability caveat; expressly exclude child support.
6. **Procedural safeguards.** Recite voluntariness, counsel, time to review, and absence of duress; for prenups, the signing-in-advance fact.
7. **Disclosure schedules.** Attach each party's asset/debt/income schedule.
8. **General provisions.** Governing law, severability, amendment (in writing), execution formalities (notarization/acknowledgment).

---

## Output Format

```markdown
{PRENUPTIAL / POSTNUPTIAL} AGREEMENT

This Agreement is entered into by {Party A} and {Party B}{, who intend to marry on {date} / who are married}.

RECITALS
A. Each party has made full and fair disclosure of assets, debts, and income as set forth in Schedules A and B.
B. Each party {has been represented by independent counsel / has had the opportunity to obtain independent counsel and {did/declined}}.
C. Each party enters this Agreement voluntarily, free of duress, with adequate time to review.

1. GOVERNING FRAMEWORK. This Agreement is governed by {State} {UPAA/UPMAA/state law} [CITE: …].
2. SEPARATE PROPERTY. {Definitions; premarital assets; business; inheritance/gifts}. Appreciation of and income from separate property {remains separate / …}.
3. MARITAL PROPERTY. {Definition; what the parties choose to treat as marital}.
4. ON DISSOLUTION. Property shall be divided as follows: {…}.
5. ON DEATH. Each party {waives/retains} elective-share and other death rights as follows: {…} (coordinate with estate documents).
6. SPOUSAL SUPPORT. {Waiver / cap / formula}. The parties acknowledge that support provisions are subject to {State}'s review and may be unenforceable if unconscionable at the time of enforcement [CITE: …]. This Agreement does NOT affect child support, which cannot be waived.
7. SAFEGUARDS. {Voluntariness; counsel; time to review; for prenup, executed {N} days before the wedding}.
8. GENERAL. Amendment only in a signed writing; governing law {State}; severability; execution with {notarization/acknowledgment}.

Schedule A — {Party A} assets/debts/income.
Schedule B — {Party B} assets/debts/income.
{Signatures; acknowledgments}
```

---

## Verification

- [ ] Governing framework (UPAA/UPMAA/state) and enforceability requirements stated.
- [ ] Disclosure schedules attached and disclosure/counsel/voluntariness recited.
- [ ] Separate vs. marital property defined, including appreciation/income/commingling treatment.
- [ ] Dissolution and death (elective-share) provisions addressed where intended.
- [ ] Spousal-support term includes the enforceability caveat; child support expressly excluded from waiver.
- [ ] Procedural safeguards recited (timing, counsel, no duress).
- [ ] Execution formalities (notarization/acknowledgment) included.
- [ ] No attempt to waive child support/custody; no invented standards or case law.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Waiving or limiting child support/custody | These cannot be contracted away; exclude them expressly |
| Omitting the financial-disclosure schedules | Attach Schedules A/B; inadequate disclosure is a leading invalidity ground |
| Presenting a support waiver as ironclad | Add the unconscionability/heightened-scrutiny caveat (state-dependent) |
| Drafting a same-day, no-counsel prenup silently | Flag the voluntariness/duress risk; build in time and independent counsel |
| Treating a postnup like a prenup | Address consideration and the heightened scrutiny some states apply to postnups |
| Ambiguous separate vs. marital definitions | Define categories and the treatment of appreciation, income, and commingling |
| Inventing the state's enforceability test | Use [CITE]/[NEED] placeholders for the UPAA/UPMAA or state standard |
| Ignoring elective-share/death coordination | Coordinate waivers with wills/trusts |
| No amendment-in-writing or execution formalities | Require signed-writing amendments and notarization/acknowledgment |
| Assuming the agreement is portable across states | Note choice-of-law and that another state may apply its own enforceability rules |
