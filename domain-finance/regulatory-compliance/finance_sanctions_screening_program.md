---
title: "Sanctions Screening Program Designer — Lists, Matching, and Escalation Workflow"
category: finance/regulatory-compliance
description: "Design a sanctions-screening program: list sourcing and coverage (OFAC/UN/EU/UK and applicable lists), customer and transaction screening logic, name-matching and fuzzy-match tuning, alert triage and escalation to a blocking/rejection decision, and governance/testing — with no-fabrication and verify-against-current-source guardrails."
techniques:
  - ST-02
  - DT-02
  - CM-02
  - DS-06
  - NE-06
difficulty: intermediate
tags:
  - sanctions
  - screening
  - ofac
  - watchlist
  - name-matching
  - escalation
  - blocking
updated: "2026-06-08"
related_prompts:
  - domain-finance/regulatory-compliance/finance_aml_kyc_program_designer.md
  - domain-finance/regulatory-compliance/finance_regulatory_requirement_mapper.md
  - domain-finance/risk-management/finance_operational_risk_rcsa.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not legal or compliance advice. Sanctions regimes (e.g., OFAC, UN, EU, UK/OFSI and other national lists), list contents, blocking/rejection obligations, and reporting requirements change frequently and vary by jurisdiction; confirm all lists, obligations, and reporting deadlines against current official sources (OFAC, EU, UK/OFSI, UN, applicable national authority) and qualified counsel before implementation. Sanctions compliance is strict-liability in many regimes — currency of lists is critical.**

## Objective

Design a sanctions-screening program covering: (1) list sourcing and coverage, (2) what is screened (customers/related parties and transactions/payments) and when, (3) name- and entity-matching logic and fuzzy-match calibration, (4) alert triage, investigation, and escalation to a documented true-match / false-positive / blocking-or-rejection decision, and (5) governance, testing, and recordkeeping. The output is a design framework; specific list obligations and reporting steps are placeholders for verification against current official sources.

## When to Use

- Standing up or remediating a sanctions-screening capability (bank, payments, fintech, BD, fund)
- Tuning a screening system generating excessive false positives or missing matches
- Extending screening to a new product, payment rail, counterparty type, or jurisdiction
- Pre-exam readiness or response to a screening-related finding

## Inputs / Context Required

```
<sanctions_screening_context>
INSTITUTION:
- Entity type and jurisdiction(s) — home and host
- Applicable sanctions authorities/regimes (OFAC, EU, UK/OFSI, UN, national)
- Products, payment rails, and counterparty types (incl. correspondent, cross-border)

SCREENING SCOPE:
- What is screened today: customers, beneficial owners, related parties, counterparties, transactions/payments, free-text payment fields
- Screening points: onboarding, periodic re-screen, real-time payment screening, list-update re-screen
- Current system/tool and matching configuration (if any)

CURRENT STATE (if remediating):
- False-positive volumes, backlog, known gaps, prior findings

CONSTRAINTS:
- Risk appetite, resourcing, SLAs for payment holds
- Date of this design: __________
</sanctions_screening_context>
```

## Constraints

### Must
- State the **applicable sanctions authorities and jurisdictions**; obligations and lists differ across regimes.
- Mark every reference to a specific list, blocking/rejection obligation, reporting form, or deadline as **"[verify against current {authority} requirements]"** — never assert list contents or reporting deadlines as authoritative from memory.
- Address **list coverage and update frequency** (lists change frequently; stale lists are a primary failure mode) and require a list-update re-screen process.
- Define **what is screened** (customers, beneficial owners, related parties, counterparties, and transaction/payment fields including free-text) and **at which points** (onboarding, periodic, real-time, on list update).
- Specify **matching logic**: exact, alias, transliteration, and **fuzzy-match** thresholds — with explicit tuning to balance false negatives (miss a true match) against false positives, treating **false-negative risk as the dominant risk**.
- Define the **alert workflow**: generation → triage → investigation → decision (true match / false positive / requires escalation) → **blocking or rejection action** → reporting, with documentation at each stage.
- Prioritize by **severity (DS-06)**: potential true matches and screening failures are highest priority.
- Include **governance, independent testing (including list-coverage and matching-effectiveness testing), training, and recordkeeping** (mark retention for verification).
- Run a **coverage self-audit (NE-06)**: which screening points, data fields, or counterparty types are not screened? Where could a true match slip through?

### Must Not
- Assert specific list contents, blocking/rejection rules, or reporting deadlines as authoritative.
- Optimize purely for false-positive reduction at the expense of false-negative risk (under-tuning fuzzy matching to cut alert volume is a critical failure).
- Treat onboarding screening as sufficient without list-update re-screening and transaction screening.
- Provide a definitive determination that a specific party/transaction is or is not a sanctions match — escalate to governance/counsel.

## Instructions

**Step 1 — List sourcing and coverage (DT-02).**
Identify required lists per regime (mark each "[verify against current {authority} list]"), the source-of-record, and the **update frequency and re-screen trigger**. Confirm consolidated vs. regime-specific list handling and any sectoral/embargo dimensions.

**Step 2 — Define screening scope and points (ST-02).**

| Screened item | Onboarding | Periodic re-screen | List-update re-screen | Real-time (payments) |
|---|---|---|---|---|
| Customers / beneficial owners | | | | |
| Related parties / counterparties | | | | |
| Transactions / payment fields (incl. free-text) | | | | |

Flag any cell that is currently "no" as a potential gap.

**Step 3 — Matching logic and tuning.**
Define matching methods (exact, alias/AKA, transliteration/script variants, fuzzy/phonetic) and threshold settings. State the tuning philosophy:
```
Tune to minimize FALSE NEGATIVES first (a missed true match is the critical failure),
then reduce false positives through better data quality, secondary scoring, and
disposition rules — NOT by loosening match sensitivity below a defensible threshold.
```
Require documentation of threshold rationale and periodic effectiveness testing.

**Step 4 — Alert triage and escalation workflow (DS-06).**

| Stage | Action | Decision criteria | Owner | Documentation | Timing/SLA |
|---|---|---|---|---|---|
| Alert generation | System hit | Match score ≥ threshold | System | Alert record | Real-time/batch |
| Level-1 triage | Clear obvious false positives | Documented disposition rules | Analyst | Disposition note | Within SLA |
| Investigation | Resolve potential true match | Identity/data corroboration | Senior analyst | Investigation file | Hold maintained |
| Escalation | Refer unresolved/true match | Governance + counsel | Sanctions officer | Decision memo | Per obligation [verify] |
| Action | Block / reject / release | Per regime obligation [verify] | Sanctions officer | Action + reporting record | Per deadline [verify] |

Maintain the payment hold while a potential true match is unresolved; do not release on SLA pressure alone.

**Step 5 — Governance, testing, training, recordkeeping.**
Define ownership, independent testing (list-coverage completeness, matching effectiveness, alert-handling quality), role-based training, and recordkeeping/retention (mark retention "[verify]").

**Step 6 — Coverage self-audit (NE-06 / QA-02).**
List screening points, data fields, counterparty types, or list categories not covered. Name the **checkbox-compliance illusion** (alerts cleared ≠ no true match) and the **false-negative blind spot**; require a disconfirming check: "If a true match existed in [unscreened field / counterparty type], would this program catch it?"

## Output Format

### List Coverage
| Regime/authority | Required lists (verify) | Source-of-record | Update frequency | Re-screen trigger |
|---|---|---|---|---|

### Screening Scope Matrix
[Step 2 table]

### Matching Configuration
- Methods, thresholds, tuning rationale, effectiveness-testing plan.

### Alert & Escalation Workflow
[Step 4 table]

### Governance, Testing, Recordkeeping
| Component | Scope | Cadence | Retention (verify) | Owner |
|---|---|---|---|---|

### Coverage Self-Audit
- Unscreened points/fields/counterparty types: …
- False-negative disconfirming check: …

### Verify-Against-Current Instruction
> Confirm all applicable lists, list-update cadence, blocking/rejection obligations, reporting forms and deadlines, and retention periods against current official sources (OFAC/EU/UK-OFSI/UN/national authority) **as of [date]**. Lists change frequently — re-verification is continuous. Match determinations and reporting route through governance and qualified compliance/legal counsel.

## Verification

- [ ] Applicable sanctions authorities and jurisdictions stated.
- [ ] All lists, obligations, forms, and deadlines marked "[verify against current requirements]".
- [ ] List coverage includes update frequency and a list-update re-screen trigger.
- [ ] Screening scope covers customers, related parties, counterparties, and transaction/free-text fields across the relevant screening points.
- [ ] Matching logic documented with false-negative-first tuning philosophy.
- [ ] Alert → triage → investigation → escalation → block/reject → report workflow defined with owners and documentation.
- [ ] Governance, independent testing, training, recordkeeping included.
- [ ] Coverage self-audit identifies gaps and includes a false-negative disconfirming check.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Asserting list contents or reporting deadlines from memory | All marked "[verify against current authority requirements]" |
| Tuning to cut alert volume at the cost of missed matches | False-negative-first tuning philosophy mandated; threshold rationale documented and tested |
| Checkbox illusion (alerts cleared = compliant) | Disconfirming check: would a true match in an unscreened field/counterparty be caught? |
| Onboarding-only screening | List-update re-screen and transaction screening required; scope matrix flags "no" cells as gaps |
| Releasing a held payment under SLA pressure | Hold maintained until potential true match resolved; release criteria are evidentiary, not time-based |
| Concluding a party "is/ is not" a match definitively | Match determinations escalate to governance/counsel; documentation required |
