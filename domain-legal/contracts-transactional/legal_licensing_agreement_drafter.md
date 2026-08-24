---
title: "IP / Software Licensing Agreement Drafter"
category: legal/contracts-transactional
description: "Draft an IP or software licensing agreement with defined scope (territory, field of use, exclusivity), royalty mechanic, audit rights, sublicense terms, improvements, termination triggers, and survival. Calibrated to licensor or licensee posture."
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
  - contracts
  - licensing
  - royalties
  - field-of-use
  - exclusivity
updated: "2026-05-11"
related_prompts:
  - domain-legal/contracts-transactional/legal_msa_drafter.md
  - domain-legal/contracts-transactional/legal_contract_review_full_redline.md
  - domain-legal/contracts-transactional/legal_negotiation_position_paper.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Draft a licensing agreement granting rights in patents, copyrights, trademarks, trade secrets, or software, with calibrated scope (territory, field of use, exclusivity), royalty mechanism (running royalty, lump sum, minimum guarantees, royalty stacking), audit rights, sublicense terms, improvement ownership, and termination triggers. Posture-calibrated.

**When to use:** Outbound licensing of IP to a partner; inbound licensing from a developer or university; cross-license between parties; software license outside the SaaS subscription model (on-premise, embedded, redistributable). Use the SaaS prompt for hosted-software subscriptions.

---

## Your Input

- **Posture:** [Licensor OR Licensee]
- **State of formation / governing law:** [State; international counterparty?]
- **Type of IP licensed:** [Patent / copyright / software (source / object) / trademark / trade secret / know-how / combination]
- **IP description:** [Patent numbers, copyright registrations, software identifiers, trademark registrations, defined trade secrets]
- **Territory:** [Worldwide / specific countries / specific regions]
- **Field of use:** [Narrow scope (e.g., "for diagnostic applications only"); whether multiple fields can be licensed to different licensees]
- **Exclusivity:** [Exclusive / sole / non-exclusive — defined; carve-outs for licensor's own use]
- **Term:** [Specific term / patent life / copyright life / perpetual with termination triggers]
- **Royalty model:** [Lump sum / running royalty (% of net sales) / per-unit / minimum annual royalty / royalty stacking allowance]
- **Royalty base:** [Net sales — defined; what deducts are permitted (taxes, returns, freight, discounts)]
- **Sublicensing rights:** [Yes / no / with consent / to affiliates only]
- **Improvements ownership:** [Licensor owns / licensee owns / shared / first-refusal license back]
- **Diligence obligations:** [Commercialization milestones; minimum spend; minimum sales]
- **Audit rights:** [Frequency, scope, cost, materiality threshold]
- **Quality control (trademarks):** [Required if trademarks licensed]
- **Termination triggers:** [Breach, insolvency, change of control, patent challenge (no-challenge), minimum performance failure]
- **Survival:** [Confidentiality, payment of accrued royalties, returned-or-destroyed materials, sell-off period]

---

## Constraints

**Must:**
- Define the licensed IP precisely. Patents by number; copyrights by registration or fixation date; software by product name and version; trademarks by registration; trade secrets and know-how by reference to a Schedule.
- Define **scope of license** in three dimensions: (i) what rights (make / have made / use / sell / offer for sale / import / copy / modify / distribute / publicly perform / display / create derivative works), (ii) territory, (iii) field of use, plus (iv) exclusivity.
- Define **exclusivity** with precision: Exclusive (excludes even licensor); Sole (excludes all but licensor); Non-exclusive. Address carve-outs.
- Define **royalty mechanism** with full specificity: base, rate, payment timing, reporting, minimum annual royalty if applicable, royalty stacking allowance, anti-stacking provisions if needed.
- Define **Net Sales** precisely with permitted deductions enumerated.
- Include **audit rights** with scope, frequency, cost-shifting at materiality threshold (e.g., underpayment of 5% or more shifts audit cost to licensee).
- For trademark licenses: include **quality control** provisions sufficient to avoid naked-license risk.
- For exclusive licenses: include **diligence obligations** (commercialization milestones) and consequences of failure (conversion to non-exclusive, termination, fee).
- Specify **improvements** ownership and any grant-back license.
- Include **no-challenge clause** (or reject if licensee posture, as no-challenge clauses limit licensee rights to challenge validity).
- Include **representations and warranties**: licensor owns the IP and has authority to license; freedom-to-operate disclaimers calibrated to posture.
- Address **infringement enforcement**: who has the right to enforce against third-party infringers (typically licensor; licensee may have step-in right for exclusive licenses); cost allocation; recovery sharing.
- Specify **termination effects**: cessation of use, return or destruction of materials, sell-off period for inventory, survival of accrued royalty obligations.
- For software with source code: address **escrow** and triggers for release.

**Must Not:**
- Use "exclusive" and "sole" interchangeably. They mean different things.
- License "all IP" without specifying which IP. Underdefined IP scope is a recipe for disputes.
- Set running royalty rates without considering royalty stacking (cumulative royalties from multiple licenses can exceed product margin).
- Permit sublicensing without flow-down of restrictions.
- Omit quality control for trademark licenses (naked license = abandonment risk).
- Use "best efforts" diligence — replace with specific milestones.
- Invent patent or registration numbers. Use `[NEED: patent number]` placeholders.
- Use generic "consult counsel" disclaimers.

---

## Posture Calibration Reference

| Provision | Licensor Posture Default | Licensee Posture Default |
|---|---|---|
| Scope | Narrow; field-of-use restricted; carve-outs for licensor's own use | Broad; all fields and territories needed |
| Exclusivity | Non-exclusive unless paid for; diligence required for exclusive | Exclusive with carve-outs; longer term |
| Royalty | Higher rate; running royalty preferred; minimum annual royalty | Lower rate; lump sum or per-unit preferred; no minimums |
| Royalty stacking | Anti-stacking provisions to protect rate | Permission for stacking; royalty offset for third-party licenses |
| Audit | Annual + on-demand on suspicion; broad scope; cost shift at low threshold | Annual only; narrow scope; cost shift at higher threshold |
| Diligence | Specific milestones with termination consequence | Loose milestones with cure rights |
| Improvements | Licensor owns; licensee assigns or grants exclusive license back | Licensee owns; grants non-exclusive license back |
| Sublicensing | Consent required; flow-down enforced | Affiliate sublicensing without consent |
| No-challenge | Required; breach triggers termination | Rejected or narrowed |
| Indemnification | Limited; no FTO warranty | Broad IP indemnity from licensor |
| Termination for convenience | Licensor right with notice | Licensee right with notice |
| Sell-off period | None or short | 6–12 months for inventory |
| Source-code escrow (software) | Not provided | Required with broad release triggers |

---

## Instructions

1. **Frame.** Parties; effective date; recitals identifying the IP and the relationship.
2. **Definitions.** Licensed IP, Field of Use, Territory, Net Sales, Royalty, Sublicensee, Affiliate, Improvement, Licensed Product, Licensed Service, Valid Claim (for patent licenses).
3. **License Grant.** Rights bundle, territory, field, exclusivity, term. State whether sublicenseable.
4. **Sublicensing (if permitted).** Conditions: consent (or not), flow-down, notification, royalty pass-through, licensor's audit reach to sublicensees.
5. **Improvements.** Definition; ownership; grant-back; cooperation.
6. **Royalty and Payment.** Rate, base (Net Sales defined), reporting, payment timing, currency, taxes, late fees, minimum annual royalty (if any), royalty stacking treatment.
7. **Records and Audits.** Records retention period; audit scope, frequency, notice, cost (with shift-at-materiality), confidentiality of auditor.
8. **Diligence.** Specific milestones; consequence of failure (conversion to non-exclusive / termination / fee).
9. **Quality Control (trademarks).** Standards, samples, approval, branding guidelines.
10. **Representations and Warranties.** Licensor: ownership and authority. Mutual: no conflict; compliance with law. Disclaimers: no FTO, no warranty of patentability/validity (or affirmative warranties if licensee paid for them).
11. **Infringement.** Enforcement rights (licensor primary, licensee step-in for exclusive); cooperation; cost sharing; recovery distribution.
12. **Indemnification.** Scope; procedure; carve-outs.
13. **Confidentiality.** For know-how and trade-secret components; survival.
14. **Term and Termination.** Term; termination for cause (with cure); termination for insolvency; termination for change of control (optional); no-challenge clause (or omission); termination for diligence failure.
15. **Effects of Termination.** Cessation; return / destruction; sell-off; accrued royalties; survival.
16. **Escrow (software).** Conditions, trustee, release triggers (insolvency, sustained breach, support cessation).
17. **LoL.** Cap; consequential exclusion; carve-outs.
18. **General.** Governing law, venue, force majeure, assignment, notices, integration, severability, counterparts, e-signature, third-party beneficiaries.
19. **Schedules.** Licensed IP (with patent numbers, registrations, software identifiers); Royalty Report Form; Quality Standards; Diligence Milestones.

---

## Output Format

```markdown
LICENSE AGREEMENT

This License Agreement ("Agreement") is entered into as of {Effective Date} by and between {Licensor Legal Name}, a {state} {entity type} ("Licensor"), and {Licensee Legal Name}, a {state} {entity type} ("Licensee").

RECITALS
A. Licensor owns or controls the Licensed IP described in Schedule A.
B. Licensee desires to obtain a license to the Licensed IP for the purposes set forth herein.
NOW, THEREFORE, the Parties agree:

1. DEFINITIONS
1.1 "Licensed IP" means the intellectual property described in Schedule A.
1.2 "Licensed Product" means {definition tied to scope}.
1.3 "Territory" means {countries/regions}.
1.4 "Field of Use" means {specific field}.
1.5 "Net Sales" means the gross amount invoiced by Licensee or its Affiliates for Licensed Products, less the following actual deductions: (a) trade, cash, and quantity discounts taken; (b) sales, use, value-added, and similar taxes collected from purchasers; (c) freight and insurance; (d) returns and allowances. Net Sales does not include sales between Licensee and Affiliates not intended for resale.
1.6 "Valid Claim" means a claim of an issued and unexpired patent that has not been invalidated by a court of competent jurisdiction, abandoned, or disclaimed.
{... additional definitions ...}

2. LICENSE GRANT
2.1 Grant. Subject to this Agreement, Licensor grants to Licensee {an exclusive / a sole / a non-exclusive} license under the Licensed IP to {make, have made, use, sell, offer for sale, and import / copy, modify, distribute, publicly display, create derivative works of} Licensed Products in the Field of Use within the Territory during the Term.
2.2 Exclusivity Carve-Outs. {If exclusive, identify any reserved rights for Licensor's own use, government use, research use, etc.}
2.3 Sublicensing. Licensee {may / may not} grant sublicenses, subject to {prior written consent, not to be unreasonably withheld / notice / no restriction} and the following conditions: (a) sublicensees are bound by written agreements containing terms no less protective than this Agreement; (b) Licensee remains responsible for sublicensee compliance; (c) Licensee provides copies of sublicense agreements to Licensor on request; (d) royalty obligations pass through.

3. IMPROVEMENTS
3.1 Definition. "Improvements" means {modifications, enhancements, or derivative works of the Licensed IP made by either Party during the Term}.
3.2 Ownership. {Licensee / Licensor} owns Improvements it creates.
3.3 Grant-Back. {Licensee / Licensor} grants the other Party a {non-exclusive / exclusive} license to its Improvements {within the existing license scope}.

4. ROYALTIES AND PAYMENT
4.1 Royalty Rate. Licensee will pay Licensor a running royalty of {N}% of Net Sales of Licensed Products.
4.2 Minimum Annual Royalty. {If applicable: $X per year starting in year __, creditable against running royalties earned in that year}.
4.3 Royalty Stacking. {If applicable: licensee may offset up to __% of royalties paid to third parties for licenses necessary to commercialize the Licensed Product, provided that royalties payable to Licensor will not be reduced below __% of Net Sales}.
4.4 Reporting. Within {30 / 45} days after the end of each calendar quarter, Licensee will deliver to Licensor a report in the form of Schedule B showing Net Sales and royalties payable.
4.5 Payment. Royalties are payable within {30 / 45} days of the end of each calendar quarter.
4.6 Currency, Taxes, Late Fees. {Specifics}.

5. RECORDS AND AUDITS
5.1 Records. Licensee will maintain complete and accurate records of Net Sales for {3} years after the end of the relevant period.
5.2 Audit. Licensor may, at its expense, audit such records once per calendar year on {30} days' prior notice, through an independent auditor bound by confidentiality.
5.3 Cost Shift. If the audit reveals an underpayment of {5%} or more for any quarter, Licensee will reimburse Licensor's reasonable audit costs and pay the underpayment plus interest at {prime + 2%}.

6. DILIGENCE
6.1 Milestones. Licensee will achieve the milestones set forth in Schedule C.
6.2 Failure to Meet Milestones. {Licensor may, in its discretion, (a) convert the exclusive license to non-exclusive; (b) terminate the license in the affected Field of Use; or (c) require a milestone-restoration fee}.

7. QUALITY CONTROL (trademarks, if applicable)
{Standards, sample submission, approval, audit rights}

8. REPRESENTATIONS AND WARRANTIES
8.1 Licensor. Licensor represents that (a) it owns or controls the Licensed IP; (b) it has the right to grant the licenses herein; (c) to its knowledge, no third party has asserted that the Licensed IP infringes its rights.
8.2 No FTO Warranty. EXCEPT AS SET FORTH IN SECTION 8.1, LICENSOR MAKES NO WARRANTY THAT THE LICENSED IP IS FREE FROM INFRINGEMENT OF THIRD-PARTY RIGHTS OR IS VALID OR ENFORCEABLE.
8.3 Licensee. Licensee represents that it will comply with applicable law in its exercise of the license.
8.4 Disclaimer. EXCEPT AS EXPRESSLY SET FORTH, LICENSOR DISCLAIMS ALL IMPLIED WARRANTIES INCLUDING MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, AND VALIDITY.

9. INFRINGEMENT BY THIRD PARTIES
9.1 Notice. Each Party will promptly notify the other of any suspected infringement.
9.2 Enforcement. {Licensor has the first right to enforce. For exclusive licenses: if Licensor does not initiate enforcement within {90} days, Licensee may, at its expense, do so in its own name or in Licensor's name with reasonable cooperation}.
9.3 Recoveries. {Allocation}.

10. INDEMNIFICATION
10.1 By Licensor. {Posture-driven: IP indemnity for licensee, or none}.
10.2 By Licensee. Licensee will defend and indemnify Licensor from third-party Claims arising from (a) Licensee's commercialization of Licensed Products; (b) Licensee's modifications; (c) Licensee's product liability or regulatory matters.
10.3 Procedure. {Standard}.

11. CONFIDENTIALITY
{Mutual confidentiality, particularly important for know-how and trade-secret components}

12. TERM AND TERMINATION
12.1 Term. The Term begins on the Effective Date and continues until {patent expiration of the last-to-expire Valid Claim / copyright term / N years / perpetual}.
12.2 Termination for Cause. Either Party may terminate for material breach uncured after {30 / 60} days' written notice.
12.3 Termination for Insolvency. Either Party may terminate upon the other's bankruptcy, receivership, or assignment for the benefit of creditors. {Licensee may elect to retain rights under Section 365(n) of the U.S. Bankruptcy Code}.
12.4 No-Challenge Clause. {Optional: If Licensee challenges the validity or enforceability of any Licensed IP, Licensor may terminate this Agreement}.
12.5 Termination by Licensee. {Optional: Licensee may terminate on {N} days' written notice; any prepaid royalties are non-refundable}.

13. EFFECTS OF TERMINATION
13.1 Cessation. Licensee will cease all use of Licensed IP.
13.2 Return / Destruction. Licensee will return or destroy all materials embodying Licensed IP and certify in writing within {30} days.
13.3 Sell-Off. Licensee may, for {6 / 12} months following termination (other than for cause based on breach by Licensee), sell off inventory of Licensed Products manufactured prior to termination, subject to continued royalty obligations.
13.4 Accrued Royalties. Royalties accrued through termination are payable.
13.5 Survival. Sections {1, 5, 8, 10, 11, 13, 14, 15} survive.

14. ESCROW (software, if applicable)
14.1 Deposit. Licensor will deposit source code and build instructions with {escrow agent} within {30} days of execution and update on each material release.
14.2 Release Triggers. Escrow agent will release the deposit to Licensee upon: (a) Licensor's bankruptcy or insolvency; (b) Licensor's cessation of support; (c) Licensor's uncured material breach of support obligations.
14.3 License upon Release. Upon release, Licensee receives a license to use the deposited materials solely to maintain Licensed Products for internal use.

15. LIMITATION OF LIABILITY
15.1 Cap. {Posture-driven cap}.
15.2 Exclusion. NEITHER PARTY WILL BE LIABLE FOR INDIRECT, INCIDENTAL, CONSEQUENTIAL, SPECIAL, OR PUNITIVE DAMAGES.
15.3 Carve-Outs. {Indemnity obligations, confidentiality, IP infringement (where applicable), gross negligence}.

16. GENERAL
{Governing law, venue, force majeure, assignment, notices, integration, severability, counterparts, e-signature, third-party beneficiaries}

SIGNATURES
{Licensor} | {Licensee}

SCHEDULE A — LICENSED IP
{Patent numbers, copyright registrations, software identifiers, trademark registrations, trade-secret descriptions}

SCHEDULE B — ROYALTY REPORT FORM
{Template}

SCHEDULE C — DILIGENCE MILESTONES
{Milestones with dates and consequences}
```

---

## Verification

- [ ] Licensed IP precisely identified in Schedule A.
- [ ] Scope: rights bundle, territory, field of use, exclusivity — all four dimensions stated.
- [ ] Exclusivity (Exclusive / Sole / Non-exclusive) clearly defined.
- [ ] Net Sales definition includes permitted deductions enumerated.
- [ ] Royalty stacking treatment specified if multiple licenses may apply.
- [ ] Audit cost-shift at materiality threshold specified.
- [ ] Diligence milestones in Schedule C if exclusive license.
- [ ] Quality control included for trademark licenses (no naked license).
- [ ] Improvements ownership and grant-back specified.
- [ ] Termination triggers and effects (cessation, return, sell-off, accrued royalties, survival) specified.
- [ ] No-challenge clause included or expressly omitted per posture.
- [ ] Section 365(n) of Bankruptcy Code addressed for licensee posture.
- [ ] No invented patent numbers or registrations. Placeholders used.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Using "exclusive" and "sole" interchangeably | Exclusive excludes even licensor; Sole excludes all but licensor; define which |
| "Net Sales" undefined or vaguely defined | Always enumerate permitted deductions; otherwise disputes over what counts |
| Running royalty without considering stacking from third-party licenses | Add royalty stacking offset (with floor) or anti-stacking representation as posture dictates |
| Diligence as "commercially reasonable efforts" | Replace with specific milestones (e.g., "first commercial sale within 24 months of regulatory approval"); CRE alone is unenforceable for diligence |
| Trademark license without quality control | Naked license = trademark abandonment; always include quality standards, sample submission, and approval rights |
| Sublicensing without flow-down | Sublicensees not bound by licensee's restrictions create gaps; require flow-down |
| No-challenge clause in licensee paper | Reject or narrow; no-challenge clauses are often unenforceable in licensee jurisdictions and limit licensee defensive options |
| Failing to address Section 365(n) for software / IP licenses | Licensee should preserve right under 11 U.S.C. § 365(n) to retain license rights in licensor's bankruptcy |
| Omitting sell-off period for licensee | Licensee may have inventory at termination; standard sell-off is 6–12 months subject to royalty |
| Audit cost-shift at unrealistic threshold (e.g., 50%) | Standard is 5% underpayment shifts audit cost; higher threshold neuters the audit right |
| Improvements ownership left unspecified | Always specify; otherwise disputes about who can use improvements |
| Source-code escrow without release triggers | Escrow without clear release triggers is useless; specify insolvency, support cessation, sustained breach |
| Licensor IP warranty too broad ("no infringement") | Warrant only what is known and verifiable; FTO disclaimers needed for patents |
| Royalty base = "gross sales" without deductions | Allow standard deductions (taxes, returns, discounts) or licensee economics break |
