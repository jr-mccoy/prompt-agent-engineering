---
title: "Rule 45 Subpoena Drafter"
category: legal/discovery
description: "Draft a nonparty subpoena (documents, testimony, or inspection) under Rule 45 or a state analog — issuing court, place of compliance, narrowly tailored requests, prior notice to parties, fee tender, and a burden-and-privacy screen — distinct from the regulatory subpoena/CID response strategy, which is for the recipient."
techniques:
  - DS-33
  - CM-02
  - QA-08
  - ST-03
difficulty: intermediate
tags:
  - legal
  - discovery
  - subpoena
  - rule-45
  - third-party-discovery
  - get-records-from-someone-not-in-the-case
  - subpoena-a-witness
updated: "2026-09-24"
related_prompts:
  - domain-legal/regulatory-compliance/legal_subpoena_or_cid_response_strategy.md
  - domain-legal/discovery/legal_document_request_drafter.md
  - domain-legal/ethics-professional-conduct/legal_sanctions_risk_premortem.md
---

# Rule 45 Subpoena Drafter

**Objective:** Produce a subpoena that a nonparty can comply with and a court will enforce: issued from the right court, commanding compliance at a lawful place, describing documents precisely, accompanied by the notices and tenders the rule requires, and screened for undue burden and statutory privacy barriers before it goes out.

> **Scope guard — attorney-facing.** For counsel of record issuing a subpoena in a pending case (in many jurisdictions an attorney may sign as an officer of the court `[VERIFY]`). It does not draft a response to a subpoena. A self-represented party should route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`, because court-clerk issuance rules for unrepresented parties differ.

## When to Use

- You need documents, electronically stored information, testimony, or an inspection from a person or entity that is not a party.
- A 30(b)(6) deposition of a nonparty organization requires a subpoena to accompany the notice.
- A state-court case needs discovery from an out-of-state nonparty (interstate subpoena procedure applies).

**Not this prompt if:**
- You received a subpoena or CID and must respond — use `domain-legal/regulatory-compliance/legal_subpoena_or_cid_response_strategy.md`.
- The target is a party — use `domain-legal/discovery/legal_document_request_drafter.md` (Rule 34) instead of a subpoena.
- You are moving to quash or modify a subpoena someone served — use `domain-legal/discovery/legal_motion_for_protective_order_drafter.md`.

## Inputs

- **Jurisdiction (required):** Court where the action is pending, the court (if different) for the place of compliance, and the governing rule (FRCP 45 or state analog). For a state case with an out-of-state nonparty, the compliance state and whether it has adopted an interstate-deposition act `[VERIFY]`.
- **Case caption and docket number.**
- **Recipient:** Name, type (individual, business, government agency, communications provider, health-care provider, financial institution), and address of residence, employment, or regular business.
- **What you need and why:** The facts each category of documents or testimony will prove.
- **Command type:** Produce documents/ESI, testify at deposition, testify at hearing/trial, permit inspection.
- **Compliance logistics:** Proposed date, place, format of production (native, PDF, load file), and whether production by mail/electronic delivery in lieu of appearance is acceptable.
- **Protective order status:** Whether a protective order is entered and whether the recipient's materials will be confidential.

## Method

**Ground rules:** Do not state the geographic compliance limit, objection deadline, witness-fee amount, or notice period as fact unless supplied — use `[VERIFY: …]`. Do not name privacy statutes' requirements beyond identifying that they may apply `[VERIFY: statute and its process requirements]`. Use `[CITE: …]` for any case authority.

1. **Confirm a subpoena is the right tool.** Party → Rule 34/30. Nonparty → subpoena. Government agency → check for agency-specific regulations governing employee testimony and records `[VERIFY: agency regulations]`.
2. **Identify the issuing court and place of compliance.** State which court issues the subpoena and where compliance occurs, and check the place against the rule's geographic limits `[VERIFY: FRCP 45(c) or analog]`. If the recipient is outside the limit, propose electronic production or a compliant location.
3. **Screen for statutory barriers.** Flag categories where a subpoena alone may be insufficient or where special notice/consent is required: stored electronic communications content, protected health information, financial records, education records, substance-use treatment records, tax returns `[VERIFY: each statute's requirement]`. Recommend alternatives (party consent/authorization, a court order, targeting the account holder).
4. **Draft requests narrowly.** Each request: a defined category, a date range, and a link to a need. Prefer "documents sufficient to show" for background facts. Avoid requesting what a party can produce more easily.
5. **Run the undue-burden check.** For each request, estimate burden on the recipient and note the issuing attorney's duty to take reasonable steps to avoid undue burden or expense `[VERIFY: FRCP 45(d)(1) or analog]`; offer cost-sharing or phased production where burden is real.
6. **Draft the subpoena.** Use the court's required form if one exists `[VERIFY: form number/version]`; include the command, schedule of requests, definitions and instructions (short), production format, and the text of the rule provisions the forum requires on the face of the subpoena `[VERIFY]`.
7. **Prepare the notices and tenders.** Prior notice and a copy to all parties before serving a documents subpoena `[VERIFY: FRCP 45(a)(4) timing]`; witness attendance fee and mileage tender for testimony `[VERIFY: amount]`; a cover letter to the recipient offering a contact and a reasonable extension process.
8. **Draft the service and follow-up plan.** Method of service, proof of service, calendar for the recipient's objection window `[VERIFY]`, and a meet-and-confer path before any motion to compel compliance in the court for the place of compliance `[VERIFY]`.

## Output Format

```markdown
# Subpoena Package — {Caption} — Recipient: {Name}

## 1. Tool and Forum Check
- Recipient status: nonparty ✔ | Issuing court: {…} | Place of compliance: {…} — within limit? {Y/N/[VERIFY]}
- Statutory-barrier screen: | Category | Possible barrier | Alternative |

## 2. Subpoena (draft on required form [VERIFY form])
- Command: {produce | testify | inspect}
- Date / time / place: {…}
### Schedule A — Definitions and Instructions (short)
### Schedule B — Documents to Be Produced
| # | Request | Date range | Need served |

## 3. Burden Screen
| Request # | Recipient burden (L/M/H) | Mitigation offered |

## 4. Notice to Parties (draft) and Timing
## 5. Fee / Mileage Tender (testimony only) [VERIFY amount]
## 6. Cover Letter to Recipient
## 7. Service and Follow-Up Calendar
| Event | Date | Rule basis [VERIFY] |
## 8. Verification Items
```

## Verification

- [ ] Jurisdiction lock: issuing court, compliance court, and rule identified for the stated forum; interstate procedure addressed if applicable.
- [ ] Citation discipline: no invented deadlines, fee amounts, distance limits, or case law; placeholders used.
- [ ] Scope discipline: the package issues a subpoena; it does not direct the recipient's response or advise the recipient.
- [ ] Recipient is not a party (or the reason for subpoenaing a party is stated and flagged).
- [ ] Place of compliance checked against the geographic limit.
- [ ] Statutory privacy barriers screened for every category of records.
- [ ] Each request has a date range and a stated need; burden mitigation offered where burden is medium or high.
- [ ] Prior notice to parties drafted and scheduled before service.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Using a subpoena to get party documents | Route to Rule 34; subpoenaing a party to evade discovery limits draws objections |
| Commanding appearance at counsel's office across the country | Check the geographic limit; offer electronic production |
| Subpoenaing a provider for message *content* or a clinic for records without the statutory process | Run the statutory-barrier screen; propose consent or court order |
| "All documents relating to" with no date range | Category + date range + need for every request |
| Skipping prior notice to other parties | Draft the notice and calendar it before service |
| Stating the objection deadline from memory | Calendar it as `[VERIFY]` from the rule text |

## Example

**Input sketch:** Federal case in the Northern District; plaintiff Brindle Logistics (fictional) alleges defendant diverted customers. Need: nonparty freight broker Castellan Freight's load records showing shipments booked for three named customers, 2024–2025. Castellan is headquartered 400 miles from the courthouse.

**Output (abridged):**

> **Forum check.** Issuing court: the Northern District (where the action is pending). Place of compliance: Castellan's headquarters city or electronic production to counsel — the courthouse is likely outside the geographic limit `[VERIFY: FRCP 45(c)(2)(A)]`. Any motion to compel compliance would be filed in the district where compliance is required `[VERIFY]`.
>
> **Schedule B, Request 1.** "Documents sufficient to show, for each load booked between January 1, 2024 and December 31, 2025 for Marrow Foods, Tillery Paper, or Aster Glassworks: booking date, booking agent, origin, destination, and the carrier assigned." Need served: proves diversion of the named customers' shipments.
>
> **Burden screen.** Request 1 — Medium (TMS export). Mitigation: accept a native export of the listed fields; no email search.
>
> **Statutory screen.** None of the categories involve communications content, health, or financial-institution records.
