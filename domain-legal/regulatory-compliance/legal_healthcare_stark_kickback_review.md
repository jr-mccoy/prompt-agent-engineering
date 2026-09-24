---
title: "Stark Law and Anti-Kickback Review — Referral Arrangement Analysis"
category: legal/regulatory-compliance
description: "Attorney-facing review of a proposed or existing healthcare financial arrangement under the physician self-referral law (Stark) and the federal Anti-Kickback Statute — arrangement and referral-flow mapping, element-by-element exception and safe-harbor testing, intent indicators, fair-market-value and commercial-reasonableness support, state-law overlays, and remediation options — distinct from an enterprise compliance-program gap review and from a disclosure decision after a violation is found."
techniques:
  - DT-05
  - DS-32
  - RT-05
  - QA-05
  - QA-12
difficulty: advanced
tags:
  - legal
  - healthcare-regulatory
  - stark-law
  - anti-kickback
  - fraud-and-abuse
  - paying-referring-doctors
  - physician-deal-review
updated: "2026-09-24"
related_prompts:
  - domain-legal/regulatory-compliance/legal_voluntary_disclosure_decision_memo.md
  - domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md
  - domain-legal/regulatory-compliance/legal_internal_investigation_plan.md
---

# Stark Law and Anti-Kickback Review — Referral Arrangement Analysis

> **Scope guard — attorney-facing only.** This prompt is for healthcare regulatory counsel and compliance officers working with counsel. It does not determine fair market value — that requires an independent valuation — and it is not billing or coding advice. A physician or practice owner without counsel should route to `domain-legal/personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md`.

> **No-fabrication rule.** Do not state exception or safe-harbor elements, annual dollar limits (for example on non-monetary compensation or limited remuneration), designated-health-services lists, or penalty amounts from memory — mark each `[VERIFY: current regulation and inflation-adjusted figure]`. Do not invent advisory opinions, case names, or settlement figures; use `[CITE: …]` / `[NEED PIN: …]`.

## When to Use

- A hospital, health system, lab, imaging center, DME supplier, or pharmacy proposes a financial arrangement with physicians or other referral sources (employment, medical directorship, lease, services, joint venture, recruitment, value-based arrangement).
- An existing arrangement has drifted (expired agreement still being paid, rent unchanged for years, compensation that tracks referrals) and counsel needs a risk read.
- Diligence on a target's physician arrangements in a healthcare transaction.

**Not this prompt if:**
- You are assessing the organization's whole compliance program — use `domain-legal/regulatory-compliance/legal_compliance_program_gap_analysis.md`.
- A likely violation has been found and the question is whether and where to self-disclose — use `domain-legal/regulatory-compliance/legal_voluntary_disclosure_decision_memo.md` (this prompt feeds it the violation analysis).
- Facts are unclear and must be established through interviews and documents first — use `domain-legal/regulatory-compliance/legal_internal_investigation_plan.md`.

## Inputs

- **Jurisdiction (required):** Federal programs involved (Medicare, Medicaid, other federal health care programs); the state(s) where services are furnished, for state self-referral, anti-kickback, and fee-splitting laws, some of which apply to all payors `[VERIFY]`.
- **Parties:** Entity and its type; physicians (and immediate family members) and other referral sources; ownership interests.
- **Arrangement documents:** Agreements, amendments, term dates, signatures; compensation formula; space or equipment descriptions.
- **Money and services flow:** Who pays whom, how much, for what, how calculated, and how often; actual payments versus contract terms.
- **Referral flow:** What the physician refers to the entity; which services are designated health services `[VERIFY: current list]`; payor mix.
- **Valuation support:** Independent FMV opinion (date, scope), commercial-reasonableness analysis, time records.
- **Context:** Why the arrangement exists; internal communications about referrals or volume.

## Method

1. **Arrangement map.** Draw each financial relationship (direct or indirect, ownership or compensation) and each referral stream. Identify immediate family members' interests.
2. **Stark screen.** For each relationship: (a) is there a physician referral for designated health services payable by Medicare? (b) is there a financial relationship? If both, the referral is prohibited unless an exception is fully met — intent is irrelevant.
3. **Exception testing, element by element.** Pick the candidate exception(s) (employment, personal services, fair-market-value compensation, office-space or equipment rental, in-office ancillary services, indirect compensation, value-based, and others `[VERIFY: current regulatory text]`). Table each element — writing, signature, term, set-in-advance compensation, fair market value, not determined in any manner that takes into account the volume or value of referrals, commercial reasonableness — against the evidence. One failed element means the exception fails; note any available timing or signature grace provisions `[VERIFY]`.
4. **Anti-Kickback analysis.** Remuneration offered or paid; to induce or reward referrals of federal health care program business; intent evidence. State that courts in several circuits find a violation if one purpose of the payment is to induce referrals `[VERIFY: controlling circuit]`. List intent indicators: compensation tied to referral volume, above-FMV payments, payments for unneeded or undocumented services, selective offers to high referrers, internal statements.
5. **Safe-harbor testing.** Table the elements of the closest safe harbor(s) `[VERIFY: current text]`. Failing a safe harbor does not create a violation; it means the arrangement is judged on its facts and intent.
6. **FMV and commercial reasonableness.** Assess whether the valuation covers the actual arrangement as performed, is current, and uses independent data; assess commercial reasonableness separately (would the arrangement make sense without referrals?).
7. **Other overlays.** State laws; beneficiary-inducement rules if patients receive anything of value; laws specific to labs or treatment facilities `[VERIFY: applicability]`; false-claims consequences of tainted claims `[VERIFY]`; overpayment report-and-return obligations if a violation has occurred `[VERIFY: timing rule]`.
8. **Risk rating and remediation.** Rate each relationship; propose restructuring (fix compensation to FMV, remove referral-sensitive terms, paper the arrangement, document services), and flag past-period exposure for the disclosure analysis.

## Output Format

```markdown
# Stark / AKS Review — {Entity} / {Arrangement}
**Programs:** {…}  |  **States:** {…}  |  **Arrangement period reviewed:** {…}  |  **Privileged & Confidential — Attorney-Client Communication**

## 1. Arrangement and Referral Map
| Relationship | Parties | Direct / indirect | Remuneration | Referral stream (DHS?) |
## 2. Stark Analysis
| Relationship | Financial relationship? | DHS referral? | Candidate exception | Result |
### Exception element table (per relationship)
| Element [VERIFY] | Evidence | Met? |
## 3. Anti-Kickback Analysis
| Relationship | Remuneration | Intent indicators | Closest safe harbor | Elements met / failed | Risk |
## 4. FMV and Commercial Reasonableness
## 5. State-Law and Other Overlays [VERIFY]
## 6. Risk Rating and Remediation
## 7. Past-Period Exposure (hand-off to disclosure analysis)
## 8. Verification Items
```

## Verification

- [ ] Jurisdiction lock: federal programs and each state named; state laws marked `[VERIFY]`.
- [ ] Citation discipline: exception and safe-harbor elements, dollar limits, and penalties are supplied or `[VERIFY]`; no invented advisory opinions or cases.
- [ ] Scope discipline: no FMV number asserted; valuation gaps flagged for an independent appraiser.
- [ ] Stark and AKS analysed separately — strict-liability exception test vs. intent-based analysis.
- [ ] Every exception element tested against evidence of actual practice, not only the contract.
- [ ] Expired, unsigned, or amended-without-writing periods identified by date.
- [ ] Past violations routed to the disclosure analysis, not resolved by prospective restructuring alone.
- [ ] Payor scope checked: federal programs beyond Medicare and any all-payor state laws considered.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Treating the arrangement as safe because the contract looks compliant | Test actual payments and services against the contract terms |
| Merging Stark and AKS into one test | Stark is strict liability with exceptions; AKS turns on intent with voluntary safe harbors |
| "It's FMV because the parties agreed on it" | Require independent, current valuation of the arrangement as performed |
| Concluding a safe-harbor miss is a violation | A miss means facts-and-intent review, not automatic illegality |
| Stating annual dollar limits or penalties as fixed | These are adjusted periodically — `[VERIFY]` |
| Fixing the contract going forward and ignoring the past | Identify past non-compliant periods and route to disclosure and overpayment analysis |
| Limiting the AKS review to Medicare | AKS reaches all federal health care programs; state laws may reach commercial payors `[VERIFY]` |

## Example

**Input (abridged):** Fictional Riverside Imaging Center leases office space to a five-physician orthopedic group that refers MRI studies to Riverside. Lease signed six years ago; rent unchanged; lease expired 14 months ago and the group keeps paying monthly. Riverside also pays the group's lead physician a "medical director" stipend with no time records.

**Output (excerpt):**

> **Stark — lease.** Financial relationship (lease); MRI is imaging, likely a designated health service `[VERIFY: current DHS list]`. Candidate exception: office-space rental. Element "written, signed, term of at least one year" — failed for the 14-month holdover unless a holdover provision applies `[VERIFY: holdover rules]`. Rent at FMV — unknown: six-year-old rent, no current appraisal `[NEED: valuation]`.
>
> **AKS — medical-director stipend.** Payments without time records or deliverables to a high-volume referrer are a recognized intent indicator. The personal-services safe harbor requires a signed writing covering all services, a compensation *methodology* set in advance, consistency with FMV, and compensation not determined by the volume or value of referrals `[VERIFY: current 42 CFR 1001.952(d)]` — likely failed (no time records, no FMV support). Risk: high.
>
> **Remediation.** Sign a new lease at appraised FMV; suspend stipend pending documented duties and valuation; route the holdover period and stipend history to the disclosure analysis.
