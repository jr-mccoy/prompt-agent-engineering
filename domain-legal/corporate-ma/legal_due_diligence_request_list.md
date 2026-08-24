---
title: "Buy-Side Due Diligence Request List"
category: legal/corporate-ma
description: "Produce a buy-side legal due diligence request list tailored to deal structure (asset / stock / merger), target industry, governing law, and the buyer's red-flag focus areas — organized by classic DD categories with priority and rationale per request."
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
  - m-and-a
  - corporate
  - due-diligence
  - buy-side
  - checklist
updated: "2026-05-11"
related_prompts:
  - domain-legal/corporate-ma/legal_due_diligence_findings_memo.md
  - domain-legal/corporate-ma/legal_disclosure_schedule_drafter.md
  - domain-legal/contracts-transactional/legal_msa_drafter.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Generate a buy-side DD request list sized to the deal — not a generic template. Each category includes deal-structure-specific requests, industry overlays, red-flag-driven questions, and priority tier. Output is ready to deliver to seller's counsel via VDR index.

**When to use:** Kickoff of buy-side diligence after LOI/term sheet; updating an existing list mid-diligence; preparing a Phase 2 supplemental request list after initial review.

---

## Your Input

- **Deal structure:** [Asset purchase / stock purchase / forward merger / reverse triangular merger / forward triangular merger / §338(h)(10) election / §336(e) election / F-reorganization]
- **Governing law of definitive agreement:** [Default: Delaware; specify if otherwise]
- **Target state of formation/incorporation:** [e.g., Delaware C-corp, California LLC]
- **Target jurisdictions of operation:** [States and foreign countries]
- **Industry:** [Specify — SaaS, healthcare, manufacturing, FinTech, defense, life sciences, consumer, etc.]
- **Posture:** Buyer
- **Approximate deal value and consideration mix:** [Cash / stock / earnout / rollover equity / seller note]
- **R&W insurance status:** [Pursuing / not pursuing — affects scope and underwriter requirements]
- **Buyer's red-flag focus areas:** [e.g., IP ownership chain, cybersecurity, customer concentration, regulatory licensure, ITAR/EAR, FCPA, wage-and-hour, ERISA]
- **Timing:** [Sign-to-close window; HSR / CFIUS / foreign clearance expected]
- **Target's prior M&A or financing history:** [If known — affects cap table, prior reps survival, drag-along complexity]
- **Known issues from LOI diligence or management presentations:** [List]

---

## Constraints

**Must:**
- Organize requests under the 12 classic DD categories in fixed order: Corporate, Capitalization, Material Contracts, IP, Employment & Benefits, Litigation, Regulatory & Compliance, Tax, Real Estate, Environmental, IT / Privacy / Cybersecurity, Insurance.
- Tailor each category's questions to the deal structure: an asset deal requires the assignment-and-consent inventory; a stock deal requires complete cap table history; a merger requires charter/bylaws and stockholder approval mechanics.
- Mark each request with priority: **P1 (deal-critical / gating)**, **P2 (material to value / reps)**, **P3 (confirmatory)**.
- For each request, include a short **rationale** tying it to a specific risk, rep, or deal-structure requirement.
- Include industry-specific overlays (e.g., HIPAA BAAs for healthcare; FDA correspondence for life sciences; PCI for payments; CMMC/DFARS for defense; SOC 2 for SaaS).
- Flag requests that are R&W-insurance underwriting requirements when R&W is in play.
- Use VDR-style numbering (1.1, 1.2, 2.1, etc.).

**Must Not:**
- Invent statutes, regulations, contract names, or facts about the target. Use `[NEED: ...]` placeholders for target-specific facts and `[CITE: ...]` for regulatory provisions not confirmed.
- Produce a generic checklist that ignores the deal structure (asset vs. stock vs. merger drives substantially different requests).
- Include "consult counsel" disclaimers — the list is the work product.
- Combine unrelated requests into a single line.
- Skip the rationale — every request must justify its inclusion.
- Demand documents that are facially irrelevant to the deal structure (e.g., requesting full subsidiary minute books in a single-entity asset deal without subsidiaries).

---

## Instructions

1. **Header block.** Project code name, target legal name, buyer legal name, deal structure, governing law, date, version.
2. **Instructions to seller.** Format expectations (VDR upload by request number), privilege protocol, redaction conventions, rolling production, written responses for "none" or "not applicable" answers.
3. **Section 1 — Corporate.** Formation documents, good standing, foreign qualifications, minute books, organizational chart, subsidiary list, prior name changes, prior reorganizations.
4. **Section 2 — Capitalization.** Cap table (current and historical), equity issuance documents, option plans, warrants, convertible notes, SAFEs, §409A valuations, stockholder agreements, voting agreements, ROFR/co-sale, drag-along, prior round documents.
5. **Section 3 — Material Contracts.** Top customers and suppliers (by revenue/spend), change-of-control and assignment provisions, MFN clauses, exclusivity, non-compete, most-favored-customer, take-or-pay, government contracts (FAR/DFARS flowdowns), distribution and reseller agreements.
6. **Section 4 — Intellectual Property.** Patents (issued, pending, abandoned), trademarks, copyrights, domain names, IP assignment agreements from all employees and contractors (chain-of-title), open-source usage and OSS policy, inbound/outbound licenses, joint development agreements, trade secret protections.
7. **Section 5 — Employment & Benefits.** Employee census, offer letters, restrictive covenants, independent contractor classification, ERISA plans, 5500s, COBRA, §280G parachute analysis if change-of-control accelerates equity, §409A compliance for deferred comp, wage-and-hour audits, I-9 / E-Verify, OSHA, union/CBAs.
8. **Section 6 — Litigation.** Pending, threatened, settled (last 5 years), demand letters, government investigations, subpoenas, internal investigations, whistleblower complaints, EEOC charges.
9. **Section 7 — Regulatory & Compliance.** Industry licenses and permits, FCPA / anti-corruption policy and incidents, OFAC / sanctions screening, export controls (ITAR/EAR), antitrust history, CFIUS notification analysis, foreign investment.
10. **Section 8 — Tax.** Federal/state/foreign returns (last 5 years), audits, nexus analysis, sales-and-use tax compliance (post-Wayfair), R&D credits, NOLs and §382 limitations, transfer pricing, §280G if applicable, §1202 QSBS status if relevant to seller consideration.
11. **Section 9 — Real Estate.** Owned property, leases, landlord consents (critical for asset deal / stock deal with anti-assignment clauses), environmental Phase I/II.
12. **Section 10 — Environmental.** Phase I ESAs, Phase II if any, CERCLA/RCRA exposure, environmental permits, notices of violation, hazardous materials handling.
13. **Section 11 — IT / Privacy / Cybersecurity.** Privacy policies, data maps, DPAs, GDPR/CCPA compliance, breach history, SOC 2 / ISO 27001 / HITRUST reports, pen test results, incident response plan, cyber insurance.
14. **Section 12 — Insurance.** Schedule of policies, claims history, D&O tail availability, R&W underwriting submission status if applicable.
15. **Industry overlay.** Append an industry-specific addendum (HIPAA, FDA, FERC, banking, defense, etc.) keyed off the input.
16. **Red-flag-driven supplemental.** Append targeted questions for each red-flag area in the input.

---

## Output Format

```markdown
# Buy-Side Legal Due Diligence Request List
**Project:** [CODE NAME]
**Target:** [TARGET LEGAL NAME], a [STATE] [ENTITY TYPE]
**Buyer:** [BUYER LEGAL NAME]
**Deal Structure:** [Asset / Stock / Merger — specify subtype]
**Governing Law (Definitive Agreement):** [State]
**Date:** [Date]   **Version:** 1.0

## Instructions to Seller
- Upload responsive documents to the VDR indexed by request number.
- For "none" or "not applicable," provide a written confirmation in the response log.
- Identify any privileged documents on a privilege log; do not upload without prior counsel-to-counsel discussion.
- Production is rolling; flag any documents requiring a clean-team protocol.

## 1. Corporate Organization
| # | Request | Priority | Rationale |
|---|---|---|---|
| 1.1 | Certificate of incorporation/formation, all amendments, restated certificate | P1 | Confirms entity existence, authorized capital; required for charter rep |
| 1.2 | Bylaws / operating agreement / LLC agreement, all amendments | P1 | Governs internal approvals; required for authorization rep |
| 1.3 | Good standing certificates from state of formation and each foreign qualification | P1 | Required for [closing deliverable / R&W underwriter] |
| 1.4 | Organizational chart including all subsidiaries, joint ventures, branches | P1 | Scopes the deal perimeter |
| 1.5 | Minute books and written consents (board and stockholder) since [date] | P2 | Confirms authorization history; identifies prior approvals affecting current deal |
{...continue}

## 2. Capitalization
| # | Request | Priority | Rationale |
|---|---|---|---|
| 2.1 | Current cap table with fully-diluted ownership, including options, warrants, SAFEs, notes, RSUs | P1 | Drives purchase price allocation and per-share consideration |
| 2.2 | Historical cap table at each financing round | P2 | Reconciles current cap table; identifies prior round overhang |
| 2.3 | All equity issuance documents (subscription agreements, board approvals, §409A valuations) | P1 | Supports valid issuance rep; identifies §409A exposure |
| 2.4 | Stockholders' agreement, voting agreement, ROFR/co-sale, drag-along | P1 | Required to plan stockholder consent / drag mechanics |
| 2.5 | All option/equity incentive plans, forms of award, individual grant agreements | P1 | Drives §280G analysis and treatment-of-equity provisions |
{...continue}

## 3. Material Contracts
{table — tailored to deal structure: assignment / consent inventory required for asset deal and for stock deal where change-of-control triggers apply}

## 4. Intellectual Property
{table — emphasize chain-of-title: IP assignments from all employees and contractors; OSS}

## 5. Employment & Benefits
{table — including §280G parachute calculation if equity accelerates; §409A audit of deferred comp}

## 6. Litigation
{table}

## 7. Regulatory & Compliance
{table — including CFIUS analysis if buyer is foreign or target has critical-tech / sensitive data}

## 8. Tax
{table — including §382 NOL limitation analysis; §1202 QSBS status if seller is taking stock and intends to preserve QSBS holding period}

## 9. Real Estate
{table}

## 10. Environmental
{table}

## 11. IT / Privacy / Cybersecurity
{table}

## 12. Insurance
{table}

## Industry Overlay — [Industry]
{appended category-specific requests}

## Red-Flag Supplemental
{appended requests targeted at buyer-identified focus areas}

## R&W Insurance Underwriter Requirements
{if applicable — additional items typical for underwriter scoping call}
```

---

## Verification

- [ ] Every request includes priority tier and rationale.
- [ ] Deal-structure-specific requests included (assignment/consent inventory for asset deals; cap table history for stock deals; charter and stockholder approval mechanics for mergers).
- [ ] All 12 classic categories present and in fixed order.
- [ ] Industry overlay tailored to specified industry.
- [ ] Red-flag supplemental responsive to each buyer-identified focus area.
- [ ] No invented statutes, regulations, or target-specific facts; placeholders used where appropriate.
- [ ] §280G, §409A, §1202, §382, CFIUS, HSR considerations flagged where input warrants.
- [ ] R&W underwriter items separated if R&W is in play.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Generic checklist that doesn't reflect deal structure | Asset deal → assignment/consent inventory is P1; stock deal → cap table history and §382 analysis are P1; merger → charter, bylaws, stockholder vote mechanics |
| Requesting subsidiary minute books when target has no subsidiaries | Verify org chart input first; suppress requests that don't apply |
| Treating §280G as a tax-only item | §280G parachute analysis belongs in Employment & Benefits because it gates equity acceleration and tax gross-ups, not just tax compliance |
| Skipping IP chain-of-title | All employee and contractor IP assignments must be requested; missing assignments are the most common IP rep breach |
| Treating OSS as cosmetic | Request the OSS bill of materials and policy — copyleft contamination is a deal-killer in SaaS / software acquisitions |
| Asking for "all contracts" without thresholds | Define materiality (revenue threshold, term, change-of-control trigger) — broad requests delay production and yield noise |
| Skipping CFIUS analysis when buyer is foreign-owned or target has critical tech / sensitive personal data | Add CFIUS-specific requests: data types, foreign personnel access, government contracts, critical technologies under 31 C.F.R. Part 800 [CITE: confirm] |
| Skipping wage-and-hour audit | Most-litigated employment area; request exempt/non-exempt classifications, off-the-clock policies, meal/rest period compliance in applicable states |
| Demanding privileged documents in initial production | Privilege log protocol must be established before production to avoid waiver |
| Treating R&W underwriter as identical to buyer counsel scope | Underwriters require specific items (cyber pen test, IP search, wage-and-hour audit, customer calls) — list separately |
