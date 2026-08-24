---
title: "Master Services Agreement Drafter"
category: legal/contracts-transactional
description: "Draft a complete Master Services Agreement with standard schedules (SOW form, DPA, SLA, insurance, security) calibrated to the user's posture (buyer or supplier). Output is sectioned, defined-term-consistent, and ready for SOW attachment."
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
  - msa
  - drafting
  - services-agreement
  - first-paper
updated: "2026-05-11"
related_prompts:
  - domain-legal/contracts-transactional/legal_sow_drafter.md
  - domain-legal/contracts-transactional/legal_dpa_gdpr_drafter.md
  - domain-legal/contracts-transactional/legal_contract_review_full_redline.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Draft a Master Services Agreement (MSA) as first paper — the form your side will send to the counterparty. Output is calibrated to posture (buyer/customer or supplier/vendor), governing-law conventions, and any industry overlay. The MSA defines framework terms; each engagement attaches under a separately negotiated SOW.

**When to use:** Standing up a vendor relationship, a customer onboarding template, or a one-off services deal expected to expand. Use the SOW drafter for engagement-specific work scope. Use the targeted clause redline for inbound counter-MSAs.

---

## Your Input

- **Posture:** [Buyer/Customer OR Supplier/Vendor]
- **State of formation / governing law:** [Delaware / California / NY / other]
- **Venue and dispute resolution preference:** [Courts + state, or arbitration body + seat + rules]
- **Counterparty business form and state of formation:** [If known]
- **Services scope category:** [Professional services / managed services / staff augmentation / consulting / development]
- **Term and renewal:** [Initial term length, renewal mechanic preferred]
- **Pricing model:** [T&M / fixed fee / milestone / subscription / hybrid]
- **Payment terms:** [Net 30 / Net 60 / milestones / advance]
- **IP regime:** [Work-for-hire / assignment of deliverables / license-only / background-license-only]
- **Data profile:** [Will counterparty access PII / PHI / regulated data; volume and category]
- **Regulatory overlay:** [HIPAA / GLBA / GDPR / FedRAMP / sector-specific]
- **Insurance requirements:** [Types and limits required of supplier]
- **LoL cap target:** [Multiple of fees / fixed dollar / period for measurement]
- **Indemnity scope:** [IP, data breach, bodily injury, breach of law, third-party-claim only or also direct]
- **Required schedules:** [SOW form / DPA / SLA / Security Addendum / BAA / Insurance / Acceptable Use]

---

## Constraints

**Must:**
- Open with definitions section using consistent capitalization throughout.
- Structure the MSA so it can attach multiple SOWs without amendment.
- Include an **order of precedence** clause governing conflicts between MSA, SOWs, and schedules.
- Calibrate risk allocation (indemnity, LoL, warranties, IP) to posture. Buyer paper protects buyer; supplier paper protects supplier.
- Include schedules as attached exhibits, not external incorporations, unless the schedule is itself a separately negotiated agreement (e.g., DPA).
- Provide a **section-by-section template** in the output covering: Definitions, Services, SOWs, Fees and Payment, Term and Termination, Confidentiality, IP, Data Protection, Warranties and Disclaimers, Indemnification, Limitation of Liability, Insurance, Compliance, General (governing law, venue, assignment, notices, force majeure, integration, severability, counterparts, electronic signature, third-party beneficiaries, no-waiver, survival).
- Use defined terms (e.g., "Effective Date," "Deliverables," "Services," "Confidential Information," "Customer Data," "Background IP," "Foreground IP," "Subcontractor").
- Provide a survival schedule explicitly listing which sections survive termination.
- For buyer paper: include audit rights, step-in rights for critical services, source-code escrow option, MFN if strategically appropriate.
- For supplier paper: include limited warranty with sole-remedy framing, fee acceleration on early termination for convenience, customer obligations as a condition to supplier performance.

**Must Not:**
- Invent statutes or regulatory provisions. Use `[CITE: ...]` if needed.
- Use placeholder text that survives into the output. Replace with `[NEED: ...]` flags.
- Apply mutual / balanced terms when posture is specified. Buyer paper and supplier paper are different documents.
- Include consumer-facing or B2C language; this is a B2B framework agreement.
- Omit DPA / BAA references when the data profile requires them.
- Use generic "consult counsel" disclaimers.
- Include integration clauses that swallow incorporated schedules unintentionally.

---

## Posture Calibration Reference

| Provision | Buyer Posture Default | Supplier Posture Default |
|---|---|---|
| LoL cap | 2× fees in 12 months or higher with carve-outs | 1× fees in 12 months with narrow carve-outs |
| Indemnity scope | Broad: IP, data, breach of law, bodily injury, confidentiality | Narrow: third-party IP claims only |
| Warranties | Express performance warranties + survival of 12 months | Sole-remedy reperformance, disclaim implieds |
| IP — Deliverables | Assigned to customer; supplier license for background IP only | Licensed to customer; supplier retains ownership of all foreground |
| Termination for convenience | Yes, customer right, no wind-down fees beyond fees through termination | Either party, with wind-down fees and termination assistance |
| Audit | Annual + on suspicion, broad scope | Limited to financial records, once per year, on 30-day notice |
| Auto-renewal | None or customer-opt-in | Yes, with reasonable notice period for non-renewal |
| Assignment | Free for customer; supplier consent required | Either party with consent; free to affiliates and on change of control |
| Source-code escrow | Required for critical software | Not required absent specific risk |

---

## Instructions

1. **Frame.** State the parties, effective date, recitals (minimal — recitals are not operative).
2. **Definitions.** Build the defined-term inventory in alphabetical order. Use brackets `{}` for any defined term whose specifics depend on input.
3. **Services.** Establish the framework: services are described in SOWs; SOW form is attached as Exhibit A; SOWs become effective when signed by both parties.
4. **SOWs.** Mechanics: form, signature authority, modification by change order, conflict-resolution with MSA.
5. **Fees and Payment.** Pricing model, invoicing cadence, payment terms, late fees, dispute mechanism, tax allocation, expense reimbursement.
6. **Term and Termination.** Initial term, renewal mechanic, termination for cause (material breach + cure), termination for convenience (posture-dependent), termination for insolvency, effects (transition services, data return, license survival, fee true-up), survival schedule.
7. **Confidentiality.** Definition, exclusions (public, independently developed, lawfully received, compelled disclosure), term, return-or-destroy obligation. Optional residuals clause (supplier-favorable) or its omission (buyer-favorable).
8. **Intellectual Property.** Background IP retention, Foreground IP ownership rule (posture-dependent), license grants, feedback license, restrictions on reverse-engineering, open-source treatment.
9. **Data Protection.** Reference to DPA if applicable; flow-down obligations to subcontractors; data return; breach-notification timeline; cooperation with regulator inquiries.
10. **Warranties.** Express performance warranty, no-conflict warranty, compliance-with-law warranty, anti-corruption warranty, employee-eligibility warranty. Disclaimer of implied warranties (UCC §§ 2-314, 2-315) — calibrated to enforceability under governing law.
11. **Indemnification.** Define indemnified events (posture-driven), procedure (notice, control of defense, cooperation, settlement consent), carve-outs.
12. **Limitation of Liability.** Cap formula, period of measurement, aggregate vs per-claim, carve-outs from cap, exclusion of indirect/consequential damages, carve-backs from consequential exclusion.
13. **Insurance.** Required coverages and limits (CGL, professional liability/E&O, cyber liability, workers' comp, employer's liability, umbrella). Additional insured and waiver of subrogation as required by posture.
14. **Compliance.** Anti-corruption (FCPA / UK Bribery Act), export controls (EAR / ITAR / OFAC sanctions), modern-slavery / human-trafficking compliance, anti-discrimination, accessibility (where applicable).
15. **General.** Governing law (without conflict-of-laws), venue / arbitration, notices (mechanism and addresses), assignment, force majeure, severability, no-waiver, counterparts, electronic signature (E-SIGN / UETA), integration, third-party beneficiaries (typically excluded), publicity restrictions.
16. **Signature block.** Title and authority representation.
17. **Schedules.** Attach Exhibit A (SOW form), and any of DPA, SLA, Security Addendum, BAA, Insurance Schedule, Acceptable Use Policy.

---

## Output Format

```markdown
MASTER SERVICES AGREEMENT

This Master Services Agreement ("Agreement") is entered into as of {Effective Date} (the "Effective Date") by and between {Customer Legal Name}, a {state} {entity type} ("Customer"), and {Supplier Legal Name}, a {state} {entity type} ("Supplier") (each a "Party" and together the "Parties").

RECITALS
A. Customer desires to engage Supplier to provide certain professional services on the terms set forth herein and in one or more Statements of Work attached hereto.
B. Supplier desires to provide such services under those terms.
NOW, THEREFORE, the Parties agree as follows:

1. DEFINITIONS
1.1 "Affiliate" means ...
1.2 "Confidential Information" means ...
1.3 "Customer Data" means ...
1.4 "Deliverables" means ...
1.5 "Foreground IP" means ...
1.6 "Background IP" means ...
1.7 "Services" means ...
1.8 "SOW" means ...
{... etc, alphabetical ...}

2. SERVICES
2.1 Provision of Services. Supplier will provide the Services described in each SOW.
2.2 SOWs. Each SOW is governed by this Agreement and incorporated herein. In the event of conflict between this Agreement and an SOW, this Agreement controls except where the SOW expressly references the conflicting MSA section.
2.3 Subcontractors. {Posture-driven: prior written consent required (buyer) vs notice (supplier)}.

3. FEES AND PAYMENT
3.1 Fees. As stated in each SOW.
3.2 Invoicing. {Cadence, content requirements}.
3.3 Payment. Net {30/60} days from invoice receipt.
3.4 Disputed Amounts. {Mechanism}.
3.5 Taxes. {Allocation}.

4. TERM AND TERMINATION
4.1 Term. Initial term of {duration} from Effective Date.
4.2 Renewal. {Posture-driven mechanic}.
4.3 Termination for Cause. Material breach uncured after {30/60} days' written notice.
4.4 Termination for Convenience. {Posture-driven: customer right vs mutual with wind-down fees}.
4.5 Termination for Insolvency. Either Party may terminate upon the other's bankruptcy, receivership, or assignment for the benefit of creditors.
4.6 Effects of Termination. {Transition services, data return, fee true-up, license survival}.
4.7 Survival. Sections {1, 5, 6, 7, 9, 10, 11, 13} survive termination.

5. CONFIDENTIALITY
{Definition, exclusions, term, return-or-destroy, compelled disclosure}.

6. INTELLECTUAL PROPERTY
6.1 Background IP. Each Party retains all right, title, and interest in its Background IP.
6.2 Foreground IP / Deliverables. {Posture-driven ownership rule}.
6.3 License Grants. {Scope, perpetuity, sublicensability, transferability}.
6.4 Feedback. {License grant for feedback}.
6.5 Open Source. Supplier will identify open-source components in Deliverables and confirm no copyleft contamination of proprietary code.

7. DATA PROTECTION
7.1 DPA. The Data Processing Addendum attached as Exhibit __ governs processing of Personal Data.
7.2 Security. Supplier will maintain administrative, physical, and technical safeguards as set forth in the Security Addendum.
7.3 Breach Notification. {Hours / days}.

8. WARRANTIES AND DISCLAIMERS
8.1 Mutual Warranties. {Authority, no conflict, compliance with law}.
8.2 Supplier Performance Warranty. {Standard of performance, duration, sole remedy}.
8.3 Disclaimer. EXCEPT AS EXPRESSLY SET FORTH HEREIN, THE SERVICES AND DELIVERABLES ARE PROVIDED "AS IS" AND SUPPLIER DISCLAIMS ALL IMPLIED WARRANTIES INCLUDING MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.

9. INDEMNIFICATION
9.1 By Supplier. Supplier will defend and indemnify Customer from third-party Claims arising from {scope}.
9.2 By Customer. Customer will defend and indemnify Supplier from third-party Claims arising from {scope}.
9.3 Procedure. {Notice, control of defense, cooperation, settlement consent}.
9.4 Exclusions. {Customer modifications, combination claims, etc.}.

10. LIMITATION OF LIABILITY
10.1 Cap. EXCEPT FOR EXCLUDED CLAIMS, EACH PARTY'S AGGREGATE LIABILITY UNDER THIS AGREEMENT WILL NOT EXCEED {cap formula}.
10.2 Exclusion of Indirect Damages. NEITHER PARTY WILL BE LIABLE FOR INDIRECT, INCIDENTAL, CONSEQUENTIAL, SPECIAL, OR PUNITIVE DAMAGES, OR LOST PROFITS, REVENUE, OR DATA.
10.3 Excluded Claims. The cap and exclusion do not apply to: {indemnity obligations, confidentiality breach, IP infringement, data breach, gross negligence or willful misconduct, payment obligations}.

11. INSURANCE
{Coverages, limits, additional-insured, waiver-of-subrogation, certificate delivery}.

12. COMPLIANCE
12.1 Anti-Corruption. {FCPA / UK Bribery Act}.
12.2 Export Controls. {EAR / ITAR / OFAC}.
12.3 Modern Slavery. {Where applicable}.

13. GENERAL
13.1 Governing Law. This Agreement is governed by the laws of {state}, without regard to conflict-of-laws principles.
13.2 Venue / Dispute Resolution. {Courts of __ / arbitration body + seat + rules + AAA/JAMS / language / number of arbitrators}.
13.3 Notices. {Mechanism, addresses, effective-on rules}.
13.4 Assignment. {Posture-driven}.
13.5 Force Majeure. {Definition, notice, mitigation, termination right if extended}.
13.6 Severability, No-Waiver, Counterparts, Electronic Signature (E-SIGN/UETA), Integration, Third-Party Beneficiaries (excluded), Publicity, Order of Precedence.

SIGNATURES
{Customer block} | {Supplier block}

EXHIBIT A — FORM OF STATEMENT OF WORK
EXHIBIT B — DATA PROCESSING ADDENDUM (if applicable)
EXHIBIT C — SECURITY ADDENDUM
EXHIBIT D — SERVICE LEVEL AGREEMENT (if applicable)
EXHIBIT E — INSURANCE REQUIREMENTS
EXHIBIT F — BUSINESS ASSOCIATE AGREEMENT (if HIPAA applies)
```

---

## Verification

- [ ] Definitions section is alphabetical, complete, and each defined term used in the body is defined here.
- [ ] Posture calibration applied consistently across indemnity, LoL, IP, warranties, termination, audit.
- [ ] Order of precedence clause present and resolves MSA-vs-SOW conflicts.
- [ ] Survival schedule lists specific sections (not "all relevant provisions").
- [ ] DPA / BAA referenced when data profile requires.
- [ ] Insurance coverages and limits stated, not "reasonable and customary."
- [ ] Governing law and venue specified, without conflict-of-laws.
- [ ] No invented citations or counterparty terms. Placeholders used for unsupplied data.
- [ ] LoL carve-outs match indemnity scope (no orphan carve-outs).
- [ ] All schedules referenced exist or are flagged as `[NEED: ...]`.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| MSA that conflicts with attached SOW form without a precedence clause | Always include an order-of-precedence section; default is MSA controls except where SOW expressly references and overrides |
| "Mutual" indemnity that is asymmetric in risk | Make scope explicitly asymmetric where the risk is asymmetric; pretending symmetry doesn't create it |
| LoL cap stated in body but no carve-outs for indemnity | Indemnity outside the cap is a deliberate choice; either carve out or expressly cap, do not leave silent |
| Auto-renewal in customer paper | Customer paper should not auto-renew or should require affirmative customer opt-in |
| Termination for convenience without wind-down fees in supplier paper | Supplier should include fees-through-termination plus reasonable wind-down for committed resources |
| Implied warranty disclaimer in all-caps but not separately conspicuous as required by UCC | All-caps may not be sufficient in all jurisdictions; verify conspicuousness requirement under governing law |
| BAA omitted in HIPAA-applicable contract | If counterparty is a business associate, BAA is required under HIPAA; flag and attach |
| Source-code escrow omitted for critical operational software | Customer paper should include escrow for software the business depends on; supplier paper need not offer |
| Confidentiality residuals clause silently included in customer paper | Customer paper should not include residuals; if supplier insists, narrow to general skills and ideas, not specific information |
| Governing-law clause without venue clause | Always pair governing law with venue / arbitration seat; otherwise enforcement is uncertain |
| Integration clause swallowing the schedules | Integration clause should expressly state schedules are part of the Agreement |
| Sub-processor approval omitted when DPA is attached | Sub-processor approval flow must be in the DPA, MSA, or both; absent it, GDPR Article 28 compliance is broken |
