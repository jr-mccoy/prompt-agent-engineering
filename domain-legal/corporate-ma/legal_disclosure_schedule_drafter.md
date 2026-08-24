---
title: "Disclosure Schedule Drafter"
category: legal/corporate-ma
description: "Draft a seller's disclosure schedule structured to the representations and warranties of the definitive agreement, with cross-reference table, exception conventions (general vs. specific), bring-down logic, and treatment under materiality-scrape and anti-sandbagging provisions."
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
  - disclosure-schedule
  - representations-warranties
  - sell-side
updated: "2026-05-11"
related_prompts:
  - domain-legal/corporate-ma/legal_due_diligence_findings_memo.md
  - domain-legal/corporate-ma/legal_due_diligence_request_list.md
  - domain-legal/corporate-ma/legal_board_resolution_drafter.md
  - domain-legal/research/legal_research_memo_irac.md
---

**Purpose:** Produce a disclosure schedule that mirrors the structure of the reps and warranties, lists each exception under the section it modifies, and includes a cross-reference table mapping every disclosed item to every rep it may qualify. Built to survive a buyer challenge that an exception was not "fairly disclosed."

**When to use:** Sell-side disclosure-schedule preparation between signing and closing (for bring-down) or during negotiation of the definitive agreement; buy-side review of seller-prepared schedules; supplemental disclosure between signing and closing.

---

## Your Input

- **Deal structure:** [Asset / stock / forward merger / reverse triangular merger / 338(h)(10) / F-reorg]
- **Governing law:** [Default: Delaware]
- **Target state of formation/incorporation:** [State]
- **Industry:** [Industry]
- **Posture:** Seller (drafter) — list each rep the buyer will request and the schedule structure
- **Section numbering of the reps in the definitive agreement:** [E.g., Article III, §§3.1–3.25; provide the rep map]
- **Materiality scrape:** [Yes / no — affects how aggressively exceptions are drafted]
- **Sandbagging treatment:** [Pro-sandbagging / anti-sandbagging / silent (Delaware default = pro-sandbagging)]
- **"Fairly disclosed" or "deemed disclosed across all reps" general disclosure language:** [Include / exclude — typically negotiated]
- **Bring-down standard:** [Bring-down at closing of all reps with "MAE" qualifier on non-fundamental reps / dual standard / no bring-down]
- **R&W insurance:** [Bound / not — affects scope of permissible exceptions]
- **Documents to incorporate by reference:** [VDR index ranges, attached documents]
- **Specific items to disclose (per rep):** [Bullet list keyed to rep numbers]

---

## Constraints

**Must:**
- Mirror the rep numbering exactly. Section 3.1 of the schedule corresponds to Section 3.1 of the agreement. Empty sections still appear with "None."
- For each disclosed item, identify (a) the rep it modifies, (b) the specific factual disclosure, (c) any cross-references to other reps it may also qualify (via the cross-reference table).
- Include a **cross-reference table** at the front mapping each disclosure to every rep it qualifies — this defeats a later buyer argument that the disclosure was not "fairly disclosed" against a different rep.
- Honor the agreement's "fairly disclosed" / "deemed cross-disclosure" convention. If the agreement permits cross-disclosure only where reasonable on its face, cross-list explicitly.
- Use precise language: include dates, parties, dollar amounts, document references — vague disclosures may not satisfy "fairly disclosed" standards.
- For each schedule item, identify any supporting document in the VDR by VDR reference number.
- Flag items that may breach a rep absent disclosure (so the schedule cures the breach) vs. items disclosed for informational/transparency purposes.
- Include the Schedule of Definitions section (capitalized terms with meanings from the agreement).
- Address bring-down: if any disclosed item could change between signing and closing, flag for supplemental disclosure procedure.

**Must Not:**
- Invent transactions, contracts, dates, or counterparties. Use `[NEED: ...]` placeholders and an open-items list.
- Drop boilerplate "all matters of public record are hereby disclosed" without specificity — buyers reject as not fairly disclosed.
- Use a single "global" disclosure section without per-rep mirroring.
- Include items that are not actually exceptions to a rep (clutters the schedule and creates ambiguity).
- Disclose privileged matters without privilege protocol consideration.
- Make disclosures so vague they fail the "fairly disclosed" standard (e.g., "various contracts" without identification).
- Omit "consult counsel" disclaimers? — there are none to include; substantive disclosures only.

---

## Instructions

1. **Cover page.** Title, deal name, target, buyer, date of agreement (signing), bring-down date if applicable, version, confidentiality legend.
2. **Introduction / interpretation.**
   - Defined terms inherit from the agreement.
   - Disclosure schedule organized by section corresponding to the reps.
   - Cross-disclosure rule restated (matches the agreement's negotiated convention).
   - Documents incorporated by reference identified by VDR section.
   - Bring-down convention.
3. **Cross-reference table.** Three columns: Disclosure Item Number | Schedule Section(s) Modified | Brief Description. Drives "fairly disclosed" defense.
4. **Schedules, mirroring rep structure.** For each rep section:
   - Schedule heading mirroring rep heading.
   - "None" if no exceptions.
   - Per-item disclosure with date, parties, dollar amount, document reference.
5. **Common schedules.** Typical buy-side reps trigger the following disclosure schedules (adjust to actual rep list):
   - Organization & Qualification (foreign qualifications)
   - Subsidiaries
   - Capitalization (current and historical issuances, outstanding options/warrants/SAFEs, voting agreements, ROFR/co-sale, drag-along)
   - No Conflicts / Required Consents (anti-assignment provisions, change-of-control triggers, regulatory consents — critical for asset deals and stock deals with COC clauses)
   - Financial Statements (deviations from GAAP, restatements)
   - No Undisclosed Liabilities
   - Absence of Changes (since reference date — restricts ordinary course)
   - Material Contracts (list with COC and assignment status)
   - Real Property (owned, leased, landlord consents)
   - Intellectual Property (registered IP, material licenses in/out, chain-of-title issues, OSS, joint ownership)
   - IT, Privacy, Cybersecurity (breaches, incidents, vendor DPAs, regulatory inquiries)
   - Employees & Benefits (key employees, employment agreements, restrictive covenants, ERISA plans, §280G payments, §409A items, independent contractors, union/CBA)
   - Tax (audits, NOLs, §382 limits, transfer pricing, sales-tax nexus, §1202 status if relevant)
   - Litigation (pending and threatened)
   - Compliance with Laws / Permits / Licenses
   - Environmental
   - Insurance (policies and claims)
   - Customers & Suppliers (top N concentration, loss of relationships)
   - Affiliate Transactions
   - Brokers / Finders
6. **Bring-down supplement protocol.** Procedure for adding supplemental disclosures between signing and closing; specify whether such supplements (a) cure the rep, (b) trigger walk-right, (c) waive indemnity claims (typically not — pro-sandbagging governs).
7. **Open items log.** Disclosures not yet finalized, target completion date, owner.

---

## Output Format

```markdown
# DISCLOSURE SCHEDULE
to the
[STOCK PURCHASE / ASSET PURCHASE / MERGER] AGREEMENT
by and among
[BUYER], [TARGET], and [SELLERS]
dated as of [DATE]

**Privileged & Confidential — Attorney Work Product**

## INTRODUCTION
This Disclosure Schedule (the "Schedule") is delivered pursuant to and forms a part of the [Agreement Name] dated [date] (the "Agreement"). Capitalized terms used and not otherwise defined herein have the meanings ascribed to them in the Agreement. Section headings correspond to the section numbers of Article [III] of the Agreement.

Headings and section numbers are for convenience. Disclosure of any matter under any section shall be deemed disclosed against any other representation, warranty, or covenant of Seller [to the extent the relevance of such matter is reasonably apparent on its face / only as expressly cross-referenced] (matching the Agreement's negotiated convention).

Disclosure of any matter herein shall not be deemed an admission that such matter is required to be disclosed, is material, or constitutes a breach absent such disclosure.

Documents referenced herein and made available in the Data Room (the "VDR") at the locations indicated are incorporated by reference.

## CROSS-REFERENCE TABLE
| Disclosure Item | Schedule Section(s) Modified | Brief Description |
|---|---|---|
| 1 | §3.4 (No Conflicts), §3.10 (Material Contracts) | Anti-assignment clause in [Top Customer] MSA dated [date]; requires consent |
| 2 | §3.13 (IP), §3.10 (Material Contracts) | Joint development agreement with [Counterparty] dated [date]; joint ownership of [field] |
| 3 | §3.15 (Employees), §3.17 (Tax) | §280G parachute payments to [N] executives; calculations at [VDR ref] |
{...}

## SCHEDULE 3.1 — ORGANIZATION AND QUALIFICATION
[State of foreign qualification 1]; [State of foreign qualification 2]
[Or "None" if none beyond state of formation]

## SCHEDULE 3.2 — SUBSIDIARIES
| Subsidiary | Jurisdiction | % Ownership |
|---|---|---|
| [Sub 1] | [State] | 100% |

## SCHEDULE 3.3 — CAPITALIZATION
[Current cap table at VDR §2.1]
[Outstanding options, warrants, SAFEs, convertible notes at VDR §2.3]
[Voting agreement, ROFR/co-sale, drag-along at VDR §2.4]
[Historical issuances since [date] at VDR §2.5]

## SCHEDULE 3.4 — NO CONFLICTS / REQUIRED CONSENTS
| Contract / Permit | Counterparty | Trigger | Consent Required? | Notice Period | Status |
|---|---|---|---|---|---|
| [Contract] | [Party] | Anti-assignment (asset deal) / Change-of-control (stock deal) | Yes | [N] days | Outreach commenced [date] |
{...}

## SCHEDULE 3.5 — FINANCIAL STATEMENTS
[Deviations from GAAP; restatements; significant accounting policies]

## SCHEDULE 3.6 — NO UNDISCLOSED LIABILITIES
[Identified items above the threshold]

## SCHEDULE 3.7 — ABSENCE OF CHANGES (since [reference date])
[Items outside ordinary course]

## SCHEDULE 3.10 — MATERIAL CONTRACTS
[List of all material contracts with date, parties, COC and assignment status, term, renewal mechanics]

## SCHEDULE 3.13 — INTELLECTUAL PROPERTY
[Registered IP by type — patents, trademarks, copyrights, domains]
[Inbound material licenses]
[Outbound material licenses]
[Joint ownership / joint development]
[OSS bill of materials and policy]
[Chain-of-title exceptions (missing IP assignments) — flag for indemnity]

## SCHEDULE 3.14 — IT / PRIVACY / CYBERSECURITY
[Historical breaches and incidents; regulatory inquiries; pen-test material findings; vendor DPA exceptions]

## SCHEDULE 3.15 — EMPLOYEES & BENEFITS
[Key employees]
[Employment agreements and restrictive covenants by employee]
[ERISA plans and 5500s at VDR §5.2]
[§280G parachute analysis at VDR §5.4 — quantify aggregate exposure]
[§409A items at VDR §5.5]
[Independent contractor classifications subject to challenge]
[Union / CBA]

## SCHEDULE 3.17 — TAX
[Open audits and contested matters]
[NOLs and §382 limitations]
[Transfer pricing studies / agreements]
[Sales-and-use tax nexus exposure]
[§1202 QSBS qualification status if relevant — original-issue date, gross-asset cap compliance, qualified trade or business status]

## SCHEDULE 3.18 — LITIGATION
[Pending and threatened, with case caption, court, status, exposure]

## SCHEDULE 3.20 — ENVIRONMENTAL
[Phase I findings; Phase II if any; permits; notices of violation]

## SCHEDULE 3.22 — INSURANCE
[Policy schedule; claims history]

## SCHEDULE 3.24 — CUSTOMERS AND SUPPLIERS
[Top N customers and suppliers by revenue / spend; any loss or material reduction]

## SCHEDULE 3.25 — AFFILIATE TRANSACTIONS
[All transactions between target and affiliates / management / equity holders]

## SCHEDULE 3.26 — BROKERS / FINDERS
[Engagement letter and fee at VDR §X]

## BRING-DOWN SUPPLEMENT PROTOCOL
Between signing and closing, Seller shall deliver supplemental disclosures of matters arising after signing within [N] business days. Supplemental disclosures (i) do not cure a breach of any representation as of signing for purposes of indemnification (pro-sandbagging) and (ii) [trigger / do not trigger] Buyer's walk-right depending on materiality and the closing condition framework in §[X].

## OPEN ITEMS
| Item | Section | Target Completion | Owner |
|---|---|---|---|
```

---

## Verification

- [ ] Disclosure schedule mirrors the rep numbering exactly.
- [ ] Cross-reference table is present and lists every multi-rep disclosure.
- [ ] Each disclosure is specific (date, parties, amount, VDR reference) — no vague catch-alls.
- [ ] Cross-disclosure language matches the negotiated convention in the agreement ("reasonably apparent on its face" vs. "expressly cross-referenced").
- [ ] Bring-down protocol addressed with sandbagging interaction explicitly stated.
- [ ] Empty sections show "None" rather than being omitted.
- [ ] §280G, §409A, §1202 disclosures included if applicable to deal facts.
- [ ] Chain-of-title IP exceptions identified for buyer-side indemnity tracking.
- [ ] Anti-assignment / change-of-control inventory in Schedule 3.4 with consent status.
- [ ] No invented contracts, counterparties, dates, or amounts; placeholders for unknowns.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| "All matters of record are hereby disclosed" boilerplate | Buyers reject as failing "fairly disclosed" standard; itemize specifically |
| Disclosing only under one rep when item qualifies multiple reps | Use the cross-reference table; restate per rep if "expressly cross-referenced" convention applies |
| Vague disclosures like "various IP licenses" | Identify by counterparty, date, and VDR reference |
| Missing anti-assignment / COC inventory | Schedule 3.4 is one of the most contentious — every contract with an anti-assignment clause (asset deal) or COC trigger (stock deal / merger) must be listed |
| Disclosing items that aren't exceptions to a rep | Disclosing for "transparency" clutters the schedule and creates ambiguity; if the rep is not breached, disclosure may signal otherwise |
| Treating the cross-disclosure rule as the same in all agreements | Negotiated provision — varies between "reasonably apparent on its face" (seller-favorable) and "expressly cross-referenced" (buyer-favorable); draft to the agreement |
| Assuming supplemental disclosures cure pre-signing breaches | Under Delaware-default pro-sandbagging, post-signing disclosures do not cure pre-signing reps; pro-rate indemnity accordingly |
| Disclosing privileged investigation findings | Privilege protocol must be in place; coordinate with counsel before disclosure |
| Listing §280G payments without aggregate exposure quantification | The buyer needs the gross-up exposure number to size the special indemnity; quantify or cross-reference VDR |
| Skipping §1202 disclosure when seller is rolling equity | Seller's QSBS status is material to seller's economics; buyer-side structuring (e.g., F-reorg before stock deal) may preserve or impair |
| Listing material contracts without COC and assignment status | Buyer needs the COC and assignment status to plan consent procurement and condition-precedent drafting |
| Disclosure schedule misaligned with bring-down standard | If reps bring down at closing without MAE qualifier, exceptions must be drafted so disclosed items don't trigger failure of closing condition |
