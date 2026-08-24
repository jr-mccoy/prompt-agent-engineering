---
title: "SaaS Subscription Agreement Drafter"
category: legal/contracts-transactional
description: "Draft a SaaS subscription agreement with usage metrics, SLA framework, security and data protection, customer data ownership, termination assistance, data portability, IP and acceptable-use restrictions. Calibrated to vendor-favorable or customer-favorable posture."
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
  - saas
  - subscription
  - sla
  - data-portability
updated: "2026-05-11"
related_prompts:
  - domain-legal/contracts-transactional/legal_dpa_gdpr_drafter.md
  - domain-legal/contracts-transactional/legal_msa_drafter.md
  - domain-legal/contracts-transactional/legal_contract_review_full_redline.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Draft a SaaS subscription agreement governing access to a hosted software service. Covers subscription model, usage metrics, service levels, customer data ownership and security, IP and AUP restrictions, fees and renewal, termination and data portability. Posture-calibrated for vendor or customer.

**When to use:** Vendor first paper for a SaaS offering; customer first paper for procurement; replacement of an expiring SaaS subscription. Use the DPA drafter alongside for GDPR overlay; use the MSA drafter when the relationship includes professional services.

---

## Your Input

- **Posture:** [Vendor/Licensor OR Customer/Subscriber]
- **State of formation / governing law:** [Delaware / California / New York / other]
- **Venue / dispute resolution:** [Courts + state, or arbitration body + seat + rules]
- **Service description:** [What the SaaS does, modules, target users]
- **Subscription metric:** [Named user / authorized user / concurrent user / device / transaction / data volume / API call / tiered]
- **Subscription tier(s):** [Pricing model, included quotas, overage mechanic]
- **Term and renewal:** [Initial term, renewal mechanic, non-renewal notice window]
- **SLA framework:** [Uptime target, response/restoration times for severity tiers, exclusions, credits, escalation, repeat-failure right]
- **Data sensitivity profile:** [PII / PHI / financial / regulated; volume; categories]
- **Regulatory overlay:** [HIPAA, GDPR, GLBA, FedRAMP, SOC 2, ISO 27001, PCI-DSS]
- **Data location and residency:** [US / EU / multi-region / customer choice]
- **Subprocessors:** [Approved list / general authorization]
- **Acceptable use:** [Restrictions on benchmarking, reverse engineering, competitor use, prohibited content]
- **Support model:** [Tier, hours, channels, response times]
- **Professional services:** [Included onboarding, paid implementation, training]
- **Termination assistance and data export:** [Format, period, fees]

---

## Constraints

**Must:**
- Open with a subscription grant defining scope: license type (subscription, not perpetual), scope (internal business purposes, identified users / scope), restrictions.
- Define **Customer Data** clearly and confirm **customer ownership** (vendor receives only the licenses needed to provide the service).
- Define **Usage Metrics** precisely — disputes over how users / transactions are counted are common.
- Include a **subscription tier / quota mechanism** with overage handling (auto-true-up, blocking, or notification).
- Include an **SLA**: uptime metric (definition of "available"), measurement window, exclusions (planned maintenance, customer's environment, force majeure, third-party causes), credits (typically 10% / 25% / 50% of monthly fees in tiered fashion), repeat-failure termination right (e.g., 3 months of credits in 12 months = customer termination right without penalty).
- Include **acceptable use** restrictions and consequences (suspension, termination, indemnification by customer for violations).
- Include **data security** by reference to a Security Addendum + minimum measures in the body.
- Include **data protection** by reference to the DPA (if applicable).
- Include **termination assistance**: customer right to export data in standard format for a defined period (30–90 days post-termination); cooperation in transition; treatment of customer data on termination (deletion with certification).
- Include **fees and renewal**: subscription fees, payment terms, auto-renewal mechanic with non-renewal notice window, price-increase cap at renewal.
- Include **IP**: vendor owns the service; customer owns customer data; mutual license grants narrowly scoped.
- Include **warranties**: vendor warrants service will perform in material conformity with documentation; sole remedy reperformance + credit + termination right.
- Include **indemnification**: vendor IP indemnity with standard carve-outs; customer indemnity for AUP violations and customer-data content.
- Include **LoL**: cap (typically 12 months fees), carve-outs (indemnity, confidentiality, data breach, AUP violations, gross negligence).

**Must Not:**
- Grant a perpetual license — SaaS is subscription-based; service ends at termination.
- Claim ownership of customer data in vendor paper — customer always owns its data.
- Use undefined SLA terms ("commercially reasonable uptime"). Always specify percentage and measurement.
- Omit termination assistance — customer needs an exit; absent provision, customer is locked in.
- Auto-renew with no non-renewal notice window or with a window so short it is impractical.
- Invent regulatory certifications (SOC 2, FedRAMP) — use `[NEED: ...]` to confirm.
- Use generic "industry standard" without specifying the standard.
- Embed generic disclaimers.

---

## Posture Calibration Reference

| Provision | Customer Posture Default | Vendor Posture Default |
|---|---|---|
| License scope | Internal business use; affiliates included; reasonable user changes | Internal use; named entity only; user changes require approval |
| Usage overage | Notification + 30 days to true up; no service interruption | Auto-billed at list rate; right to suspend on persistent overage |
| Uptime target | 99.9% or higher with tiered credits | 99.5% with capped credits |
| SLA exclusions | Narrow: planned maintenance with notice, customer's network | Broad: planned + emergency maintenance, third-party causes, customer environment |
| Termination assistance period | 90 days minimum, no fee | 30 days included, additional at hourly rate |
| Data export format | Industry-standard (JSON, CSV, SQL dump) + API access | CSV export only |
| Auto-renewal | 30-day non-renewal window with 60-day price-change notice | Auto-renew with 60-day window; market-rate pricing at renewal |
| Price increase at renewal | Capped at CPI or 5% | List-price at renewal |
| Source-code escrow | Required for critical use cases | Not offered |
| Customer data deletion | Certification within 30 days of termination | Certification within 60–90 days; reasonable backup carve-out |
| Warranty | Performance + security warranty | Performance only, sole-remedy reperformance |

---

## Instructions

1. **Frame.** Parties, effective date, scope of agreement.
2. **Definitions.** Including: Authorized User, Customer Data, Documentation, Order Form, Service, Subscription Term, Usage Metric.
3. **Order Forms.** Mechanic for ordering subscription tiers; signature authority; integration with this agreement.
4. **Subscription Grant.** Scope (internal business purposes), authorized users, term-limited license, prohibited uses (resale, benchmarking absent consent, competitor use, reverse engineering, derivative works, removal of proprietary notices).
5. **Usage Metrics and Overage.** Definition of metric, measurement, overage notification, true-up.
6. **Fees and Payment.** Subscription fees per Order Form, payment terms, late fees, disputed-amount mechanism, taxes.
7. **Term and Renewal.** Initial Subscription Term per Order Form; renewal mechanic; non-renewal notice; price increases.
8. **Service Levels.** Uptime metric (definition), measurement window, exclusions, credits (tiered), credit claim mechanism, escalation, repeat-failure termination right.
9. **Support.** Tiers, hours, channels, response targets.
10. **Customer Data.** Customer ownership; license to vendor (limited to providing service); customer responsibility for accuracy and lawfulness.
11. **Data Security.** Reference Security Addendum; minimum measures; certifications (SOC 2 / ISO 27001 / FedRAMP) by reference.
12. **Data Protection.** Reference DPA where applicable.
13. **Acceptable Use Policy.** Restrictions, suspension right, customer indemnification for AUP violations.
14. **IP.** Vendor owns the service; customer owns customer data; feedback license.
15. **Warranties.** Vendor performance warranty; sole-remedy reperformance + credit + termination; disclaimer of implieds.
16. **Indemnification.** Vendor IP indemnity (carve-outs: customer modifications, combinations, customer-supplied content); customer indemnity for AUP and customer-data content.
17. **LoL.** Cap, carve-outs from cap, exclusion of indirect/consequential damages with carve-backs.
18. **Confidentiality.** Mutual.
19. **Termination.** For cause (material breach + cure), insolvency, AUP violation. Effects: cease service, fee true-up, data export.
20. **Termination Assistance and Data Export.** Period, format, fees, certification of deletion.
21. **General.** Governing law, venue, force majeure, assignment, notices, integration, severability, counterparts, electronic signature, third-party beneficiaries (typically excluded), publicity (with consent), audit (license compliance, narrow).
22. **Signatures and Order Form.**

---

## Output Format

```markdown
SAAS SUBSCRIPTION AGREEMENT

This SaaS Subscription Agreement ("Agreement") is entered into as of {Effective Date} by and between {Vendor Legal Name}, a {state} {entity type} ("Vendor"), and {Customer Legal Name}, a {state} {entity type} ("Customer").

1. DEFINITIONS
{Including: Authorized User, Customer Data, Documentation, Order Form, Service, Subscription Term, Usage Metric}

2. ORDER FORMS
Customer may subscribe to the Service by executing one or more Order Forms referencing this Agreement. Each Order Form is incorporated herein.

3. SUBSCRIPTION GRANT
3.1 Grant. Subject to this Agreement and payment of fees, Vendor grants Customer a non-exclusive, non-transferable, non-sublicensable subscription to access and use the Service for Customer's internal business purposes during the Subscription Term, limited to the Usage Metric in the Order Form.
3.2 Authorized Users. Customer may permit access by Authorized Users as defined in the Order Form. Customer is responsible for Authorized Users' compliance.
3.3 Restrictions. Customer will not (a) resell or sublicense the Service; (b) reverse engineer or attempt to derive source code, except as permitted by applicable law; (c) use the Service to develop a competing product; (d) benchmark the Service for publication without Vendor's prior written consent; (e) remove proprietary notices; (f) violate the Acceptable Use Policy (Annex __).

4. USAGE METRICS AND OVERAGE
4.1 Metric. The Service is subscribed by {Usage Metric}.
4.2 Measurement. Vendor will measure usage via {mechanism}.
4.3 Overage. {Posture-driven: notification with 30-day true-up vs auto-billing at list rate}.

5. FEES AND PAYMENT
5.1 Fees. As set forth in each Order Form.
5.2 Invoicing and Payment. {Cadence, terms}.
5.3 Disputed Amounts. {Mechanism}.
5.4 Taxes. {Allocation}.
5.5 Late Fees. {Posture-driven}.

6. TERM AND RENEWAL
6.1 Initial Subscription Term. As set forth in each Order Form.
6.2 Renewal. The Subscription Term will renew for successive {12-month / equal} periods unless either Party gives written notice of non-renewal at least {30 / 60} days before the end of the then-current term.
6.3 Price Changes. Vendor may increase fees at renewal by providing at least {60} days' prior notice; increases capped at {CPI / 5% / list rate}.

7. SERVICE LEVELS
7.1 Uptime Commitment. Vendor will use commercially reasonable efforts to make the Service "Available" at least {99.9%} of the time during each calendar month ("Service Level"), measured as set forth in Annex __ (Service Level Agreement).
7.2 Service Credits. If Vendor fails to meet the Service Level, Customer will be entitled to Service Credits as set forth in Annex __.
7.3 Exclusions. Service Level calculations exclude {scheduled maintenance with notice; emergency maintenance; force majeure; Customer's network or environment; Customer's misuse}.
7.4 Repeat Failure. If Vendor fails to meet the Service Level for {3 months in any rolling 12-month period}, Customer may terminate the affected Order Form for cause and receive a pro-rata refund of pre-paid unused fees.

8. SUPPORT
{Tier, hours, channels, response targets}

9. CUSTOMER DATA
9.1 Ownership. As between the Parties, Customer owns all Customer Data.
9.2 License to Vendor. Customer grants Vendor a limited, non-exclusive license to host, transmit, process, and display Customer Data solely to provide the Service and as authorized by this Agreement.
9.3 Customer Responsibility. Customer is responsible for the accuracy, legality, and lawful basis of Customer Data, and for obtaining necessary consents.

10. SECURITY
10.1 Measures. Vendor will maintain administrative, physical, and technical safeguards as described in Annex __ (Security).
10.2 Certifications. Vendor will maintain {SOC 2 Type II / ISO 27001 / FedRAMP} certification during the Term and will make audit reports available to Customer under NDA.

11. DATA PROTECTION
The Data Processing Addendum attached as Annex __ governs processing of Personal Data.

12. ACCEPTABLE USE
Customer will comply with the Acceptable Use Policy attached as Annex __. Vendor may suspend the Service for material AUP violation upon notice; Customer will indemnify Vendor for AUP violations and Customer-supplied content.

13. INTELLECTUAL PROPERTY
13.1 Vendor IP. Vendor and its licensors own the Service, Documentation, and all related intellectual property.
13.2 Customer Data. Customer retains ownership of Customer Data.
13.3 Feedback. Customer grants Vendor a perpetual, irrevocable, royalty-free license to use feedback provided by Customer to improve the Service, without obligation.

14. WARRANTIES
14.1 Performance. Vendor warrants that the Service will perform materially in accordance with the Documentation during the Subscription Term. Customer's sole remedy is reperformance and, if Vendor cannot reperform within {30 days}, a refund of pre-paid unused fees and right to terminate.
14.2 Mutual. Each Party warrants authority, no conflict, and compliance with law.
14.3 Disclaimer. EXCEPT AS EXPRESSLY SET FORTH, THE SERVICE IS PROVIDED "AS IS" AND VENDOR DISCLAIMS ALL IMPLIED WARRANTIES INCLUDING MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.

15. INDEMNIFICATION
15.1 By Vendor. Vendor will defend and indemnify Customer from third-party Claims that the Service infringes a valid {US / specified} patent, copyright, trademark, or trade secret. If the Service becomes the subject of an infringement claim, Vendor may, at its option, (a) modify the Service to be non-infringing; (b) procure rights for Customer to continue using; or (c) terminate the affected subscription and refund pre-paid unused fees.
15.2 By Customer. Customer will defend and indemnify Vendor from third-party Claims arising from (a) AUP violations; (b) Customer Data content; (c) Customer's combination of the Service with Customer-supplied or third-party materials.
15.3 Procedure. {Notice, control of defense, cooperation, settlement consent}.
15.4 Exclusions to Vendor Indemnity. Vendor has no obligation for Claims arising from (a) modifications to the Service not made by Vendor; (b) combination with Customer or third-party materials; (c) Customer's use outside the Documentation; (d) Customer's failure to use a non-infringing update made available at no additional charge.

16. LIMITATION OF LIABILITY
16.1 Cap. EXCEPT FOR EXCLUDED CLAIMS, EACH PARTY'S AGGREGATE LIABILITY UNDER THIS AGREEMENT WILL NOT EXCEED {fees paid by Customer in the 12 months preceding the Claim}.
16.2 Exclusion of Indirect Damages. NEITHER PARTY WILL BE LIABLE FOR INDIRECT, INCIDENTAL, CONSEQUENTIAL, SPECIAL, OR PUNITIVE DAMAGES, OR LOST PROFITS, REVENUE, OR DATA.
16.3 Excluded Claims. The cap and exclusion do not apply to: {indemnity obligations, confidentiality breach, data breach, AUP violations, gross negligence or willful misconduct, payment obligations}.

17. CONFIDENTIALITY
Mutual confidentiality obligations apply per Annex __.

18. TERMINATION
18.1 For Cause. Either Party may terminate for material breach uncured after {30 / 60} days' written notice.
18.2 For Insolvency. Either Party may terminate upon the other's bankruptcy, receivership, or assignment for the benefit of creditors.
18.3 For AUP Violation. Vendor may terminate for material AUP violation.
18.4 Effect. Upon termination: (a) Customer's access to the Service ends; (b) Customer pays fees accrued through termination; (c) Customer may export Customer Data per Section 19; (d) Vendor will delete Customer Data per Section 19.

19. TERMINATION ASSISTANCE AND DATA EXPORT
19.1 Export Period. For {30 / 60 / 90} days following termination, Vendor will make Customer Data available for export in {industry-standard formats / specified format} at {no additional charge / hourly rate}.
19.2 Deletion. Within {30 / 60 / 90} days after the end of the Export Period, Vendor will delete Customer Data from its systems, subject to reasonable backup retention for the period not exceeding {N} months, and will provide written certification.
19.3 Continued Confidentiality. Vendor's confidentiality obligations continue with respect to retained backups.

20. GENERAL
20.1 Governing Law and Venue. {State; courts or arbitration}.
20.2 Assignment. {Posture-driven}.
20.3 Force Majeure. {Definition; payment, confidentiality, and security not excused}.
20.4 Notices, Severability, No-Waiver, Counterparts, Electronic Signature, Integration, Third-Party Beneficiaries (excluded), Publicity (consent required), Audit (license compliance, narrow).

SIGNATURES
{Vendor} | {Customer}

ANNEXES
A — Service Level Agreement
B — Security Measures
C — Data Processing Addendum
D — Acceptable Use Policy
E — Order Form (form)
```

---

## Verification

- [ ] Subscription (not perpetual) license framing throughout.
- [ ] Customer Data ownership stated affirmatively.
- [ ] SLA includes uptime metric, measurement, exclusions, credits, and repeat-failure termination right.
- [ ] Usage metric defined with overage mechanic.
- [ ] Renewal mechanic with non-renewal window and price-increase cap (per posture).
- [ ] Termination assistance period and data export format specified.
- [ ] Data deletion certification mechanism with backup carve-out.
- [ ] Indemnity carve-outs match the actual risk profile (vendor IP indemnity has standard exclusions).
- [ ] LoL carve-outs match the indemnity scope (no orphan carve-outs).
- [ ] DPA / Security Addendum / AUP referenced and identified as annexes.
- [ ] No invented certifications. Placeholders for unconfirmed items.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Granting a perpetual license in a SaaS contract | SaaS is subscription only; service access ends at termination |
| Claiming ownership of customer data in vendor paper | Customer always owns its data; vendor receives a service-license only |
| "Commercially reasonable" uptime with no number | Specify percentage and measurement window; otherwise SLA is unenforceable |
| SLA credits as sole remedy with no termination right | Customer should have termination right for repeat or material failures beyond credits |
| Auto-renewal with no non-renewal notice or with a window the customer cannot operate (e.g., 7 days) | Standard is 30–60 days; specify and confirm operability |
| Termination assistance absent from vendor paper | Customer needs an exit; absent provision, customer is captive; add 30-day minimum |
| Data export only via CSV when customer needs API or SQL | Specify the format; tailor to data complexity |
| Indemnification of vendor for "all customer use" | Customer indemnity must be limited to AUP, content, and customer-supplied materials — not general use |
| LoL cap that swallows data-breach exposure | Data breach should be carved out from the cap or have a separate cap commensurate with exposure |
| Suspension right without notice | Suspension for AUP violation should include notice and cure where possible, except for critical security or legal issues |
| Confusing the SLA service-credit cap with the LoL cap | Service credits are a remedy floor; not a substitute for the overall LoL cap |
| No mention of data residency when customer requires EU-only | Specify residency commitment and consequence of breach |
| Vendor claiming feedback license with derivative rights | Feedback license should be perpetual + royalty-free, but limited to improving the Service — not creating derivative products competing with the customer's business |
