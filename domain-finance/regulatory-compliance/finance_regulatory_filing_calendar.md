---
title: "Regulatory Filing Calendar Builder — Filings, Owners, and Deadlines"
category: finance/regulatory-compliance
description: "Build a regulatory filing calendar that lists each periodic and event-driven filing with its regulator, frequency, owner, preparer/reviewer/approver, lead-time milestones, and deadline — with no-fabrication of deadlines and verify-against-current-source guardrails."
techniques:
  - ST-02
  - DT-02
  - OC-01
  - CM-02
  - NE-06
difficulty: beginner
tags:
  - filing-calendar
  - deadlines
  - regulatory-filings
  - compliance-calendar
  - owners
updated: "2026-06-08"
related_prompts:
  - domain-finance/regulatory-compliance/finance_regulatory_requirement_mapper.md
  - domain-finance/regulatory-compliance/finance_compliance_gap_analysis.md
  - domain-finance/accounting-controllership/finance_audit_pbc_preparation.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not legal or compliance advice. Filing requirements, forms, frequencies, and deadlines change and vary by jurisdiction, entity type, and filer status; confirm every form, frequency, and deadline against current official sources (the relevant regulator's filing instructions) and qualified counsel before relying on this calendar.**

## Objective

Produce a regulatory filing calendar that captures, for each required filing, the regulator, form/report, frequency, due date (and any lead-time milestones), the accountable owner, and the preparer/reviewer/approver chain — so filings are tracked and not missed. Every deadline and form name is a placeholder to be verified against the current official source; this tool organizes and schedules, it does not establish what is legally required.

## When to Use

- Building a compliance calendar for a new entity, registration, or jurisdiction
- Annual refresh of an existing filing calendar
- Onboarding a new compliance/finance owner who needs the full filing inventory
- After a missed/late filing, to harden lead-time milestones and ownership

## Inputs / Context Required

```
<filing_calendar_context>
ENTITY / SCOPE:
- Legal entity(ies), registration/license types, filer status
- Regulator(s) and jurisdiction(s)

FILINGS (user-supplied or from the requirement map):
- Filing/report name and regulator
- Frequency (annual, semi-annual, quarterly, monthly, event-driven)
- Known due date or due-date rule (verify against current source)
- Any dependencies (e.g., requires audited financials first)

OPERATING CONTEXT:
- Fiscal year end
- Available owners/preparers/reviewers/approvers
- Standard lead time needed to prepare each filing
- Calendar year(s) to build: __________
- Date prepared: __________
</filing_calendar_context>
```

## Constraints

### Must
- State the **regulator and jurisdiction** for every filing.
- Mark every **due date, deadline rule, and form name** as **"[verify against current {regulator} filing instructions]"** — never assert a specific deadline or form number as authoritative from memory.
- Assign a single accountable **owner** plus the **preparer / reviewer / approver** chain for each filing.
- Add **lead-time milestones** (start, internal draft, review, approval) backward from each (verified) deadline.
- Flag **dependencies** (filings that require a prior deliverable, e.g., audited statements) and **event-driven filings** (triggered by a transaction/event rather than the calendar).
- Note **filing-period / business-day conventions** (e.g., "deadline rolls to next business day if it falls on a weekend/holiday — verify") rather than assuming a fixed date.
- Run a **completeness self-audit (NE-06)**: which registrations, jurisdictions, or event-driven triggers might have filings not yet on the calendar?

### Must Not
- Assert specific filing deadlines, form numbers, or frequencies as authoritative.
- Omit the owner or the verification placeholder for any filing.
- Treat event-driven filings as if they were periodic (or omit them entirely).
- Imply the calendar is exhaustive or constitutes legal confirmation of obligations.

## Instructions

**Step 1 — Inventory filings (DT-02).**
List every periodic and event-driven filing in scope, grouped by regulator. For each, capture frequency and the due-date rule. Mark forms/deadlines "[verify against current filing instructions]".

**Step 2 — Anchor deadlines to the fiscal calendar (ST-02).**
For periodic filings, translate the (verified) due-date rule into calendar dates for the target year(s), noting business-day/holiday roll conventions. Keep dates as "[verify]" anchored values, not asserted facts.

**Step 3 — Add lead-time milestones.**
For each filing, schedule backward from the deadline: data-ready → first draft → review → approval → submit. Use the institution's standard lead time per filing.

**Step 4 — Assign ownership chain.**
Assign owner (accountable), preparer, reviewer, approver for each filing. No filing may lack an accountable owner.

**Step 5 — Flag dependencies and event-driven filings.**
Mark filings that depend on a prior deliverable. List event-driven filings with their **trigger** and the (verified) post-event deadline window.

**Step 6 — Completeness self-audit (NE-06).**
List registrations/jurisdictions/event triggers that may generate filings not yet captured. Name the **scope-omission** and **over-reliance-on-prior-year-calendar** pitfalls and require a disconfirming check: "What new registration, product, jurisdiction, or transaction this year creates a filing not on last year's calendar?"

## Output Format

### Periodic Filing Calendar

| # | Filing/Form (verify) | Regulator / Jurisdiction | Frequency | Deadline (verify) | Lead-time start | Owner | Preparer | Reviewer | Approver | Dependency |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [verify form] | | Quarterly | [verify deadline] | | | | | | |

### Event-Driven Filing Register

| # | Filing (verify) | Trigger event | Post-event deadline window (verify) | Owner | Notes |
|---|---|---|---|---|---|

### Lead-Time Milestone View (per filing)

| Filing | Data-ready | Draft | Review | Approval | Submit (deadline, verify) |
|---|---|---|---|---|---|

### Completeness Self-Audit
- Registrations/jurisdictions possibly missing filings: …
- Event triggers not yet mapped to filings: …
- Disconfirming check (new items this year): …

### Verify-Against-Current Instruction
> Confirm every form name, frequency, deadline, and business-day convention against the current official filing instructions for each regulator **as of [date prepared]**. Deadlines and forms change; this calendar must be re-verified before each filing cycle. Obligation determinations route to qualified compliance/legal counsel.

## Verification

- [ ] Every filing has a regulator and jurisdiction.
- [ ] Every deadline and form name is marked "[verify against current filing instructions]".
- [ ] Every filing has an accountable owner and a preparer/reviewer/approver chain.
- [ ] Lead-time milestones scheduled backward from each deadline.
- [ ] Dependencies flagged; event-driven filings listed with triggers and windows.
- [ ] Business-day/holiday roll conventions noted, not assumed.
- [ ] Completeness self-audit lists possibly missing filings and a disconfirming check.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Asserting a specific deadline or form number | All deadlines/forms marked "[verify against current filing instructions]" |
| Calendar appears complete = all obligations covered | Completeness self-audit forces a review of registrations, jurisdictions, and event triggers |
| Over-reliance on last year's calendar | Disconfirming check required for new registrations/products/jurisdictions/transactions |
| Filing with no clear owner | Every filing requires an accountable owner; preparer/reviewer/approver chain mandatory |
| Event-driven filings forgotten | Separate event-driven register with explicit triggers and post-event windows |
| Fixed date assumed without business-day roll | Business-day/holiday conventions noted and marked for verification |
