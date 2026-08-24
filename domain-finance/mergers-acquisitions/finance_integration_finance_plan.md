---
title: "Post-Close Integration Finance Plan — Day-1 Readiness, Synergy Tracking, and Reporting"
category: finance/mergers-acquisitions
description: "Build the finance workstream plan for post-close integration: Day-1 financial readiness (close, treasury, controls), a synergy-tracking baseline and capture ledger, combined reporting and chart-of-accounts mapping, and integration-cost budgeting against the deal thesis."
techniques:
  - DT-01
  - ST-02
  - DS-02
  - NE-11
  - DS-06
difficulty: intermediate
tags:
  - integration
  - post-merger-integration
  - synergy-tracking
  - day-1-readiness
  - reporting
  - m-and-a
updated: "2026-06-08"
related_prompts:
  - domain-finance/mergers-acquisitions/finance_synergy_estimation_framework.md
  - domain-finance/mergers-acquisitions/finance_deal_post_mortem_review.md
  - domain-finance/mergers-acquisitions/finance_ma_deal_model_builder.md
  - domain-finance/field_guide.md
---

**Informational only — not investment, accounting, or legal advice. Integration planning should involve the deal team, controllers, tax, and treasury professionals.**

## Objective

Produce the finance-function integration plan that turns a closed deal into a controllable combined entity: Day-1 financial readiness (close calendar, treasury/cash, controls, payroll), a synergy-tracking baseline and capture ledger that ties to the underwritten synergy case, combined management reporting with a chart-of-accounts mapping, and an integration-cost budget tracked against the deal thesis — sequenced by phase with owners and milestones.

## When to Use

- Planning the finance workstream for a closing or recently closed acquisition
- Standing up Day-1 financial reporting, treasury, and controls for the combined entity
- Building the synergy-capture tracking system that proves (or disproves) the deal thesis
- Mapping two charts of accounts into one combined reporting structure
- Governing integration spend against budget and the underwritten synergy plan

## Inputs / Context Required

- Deal close date; legal/operating structure (merge entities, hold separate, carve-out)
- Underwritten synergy case (run-rate, phase-in, by category) — ideally from the synergy-estimation prompt
- Both companies' close calendars, ERP/GL systems, chart of accounts, and reporting cadence
- Treasury setup: bank accounts, cash pooling, debt facilities, FX exposures
- Integration budget (costs-to-achieve) and any TSAs (transitional services agreements)
- Key controls/SOX or audit requirements; tax/entity considerations affecting reporting
- Accounting framework (US GAAP / IFRS); reporting currency

## Constraints

### Must
- Sequence the plan by phase with owners, dependencies, and milestones (DT-01): Pre-Day-1 → Day-1 → First close (Month 1) → First 100 days → Run-rate.
- Define Day-1 financial readiness as a checklist (ST-02): ability to close the books, run payroll, pay vendors, collect cash, access banking, and produce a combined flash report.
- Build a synergy-tracking baseline (NE-11, DS-02): lock the pre-deal cost/revenue baseline so captured synergies are measured against it, not against a moving budget.
  - `Synergy Captured_t = Baseline run-rate − Actual run-rate (cost) or Actual − Baseline (revenue), net of dis-synergy`
  - Track gross capture, net-of-cost-to-achieve, and run-rate vs. underwritten target.
- Map the two charts of accounts into a combined structure; flag accounts that cannot be cleanly mapped.
- Budget integration costs (costs-to-achieve) by category and track actual vs. budget; prioritize initiatives by net value and effort (DS-06).
- State the cadence and owner of combined management reporting (flash, monthly, board).

### Must Not
- Measure synergies against a budget that already includes them (circular) — measure against a locked pre-deal baseline.
- Present a synergy-capture number without netting costs-to-achieve and dis-synergies.
- Assume Day-1 reporting works without an explicit readiness checklist and contingency.
- Treat integration costs as open-ended; they must be budgeted and tracked.
- Ignore TSAs and the cliff when transitional services end.

## Instructions

**Step 1 — Phase plan (DT-01)**

| Phase | Window | Key finance objectives | Owner | Milestone/gate |
|---|---|---|---|---|
| Pre-Day-1 | before close | banking, GL access, opening BS, comms | | readiness sign-off |
| Day-1 | close date | payroll, payments, cash visibility | | Day-1 operational |
| First close | Month 1 | combined flash, opening balance sheet | | first combined close |
| First 100 days | Q1 | synergy quick wins, COA mapping, controls | | tracking live |
| Run-rate | by Year 1–2 | full synergy run-rate, single ERP | | run-rate achieved |

**Step 2 — Day-1 financial readiness checklist (ST-02)**

```
[ ] Bank accounts mapped; signatories and cash pooling in place
[ ] GL/ERP access; opening balance sheet booked (links to PPA)
[ ] Payroll continuity for both workforces
[ ] AP/AR continuity — vendors paid, customers billed and collected
[ ] Combined flash report defined (revenue, cash, key KPIs)
[ ] Controls/authority matrix for the combined entity
[ ] TSA scope and end-dates documented; dependencies flagged
```

**Step 3 — Synergy-tracking baseline and capture ledger (NE-11, DS-02)**

```
Lock baseline (pre-deal run-rate by cost/revenue category).
For each initiative:
  Synergy Captured_t = (Baseline − Actual) [cost]  or  (Actual − Baseline) [revenue]
  Net Captured_t = Captured_t − Costs-to-achieve_t − Dis-synergy_t
  Run-rate captured vs. underwritten run-rate target (% of plan)
Status: Identified → Validated → In-flight → Realized (run-rate locked)
```

**Step 4 — Chart-of-accounts mapping**

Map source-A and source-B accounts to the combined structure; flag unmapped/ambiguous accounts and the policy decision needed (e.g., harmonizing capitalization thresholds, revenue-recognition policy alignment).

**Step 5 — Integration-cost budget and prioritization (DS-06)**

```
Budget costs-to-achieve by category (severance, systems, advisory, retention).
Track Actual vs. Budget each period; flag variances.
Prioritize initiatives by net value ÷ effort; sequence quick wins first.
```

**Step 6 — Reporting cadence**

Define flash (weekly/daily early), monthly close, and board reporting; name owners; specify the synergy dashboard that ties to the deal thesis.

## Output Format

### Phase Plan
[Step 1 table]

### Day-1 Readiness Checklist
[Step 2 checklist with status]

### Synergy-Tracking Ledger

| Initiative | Category | Baseline | Actual | Gross Captured | Costs-to-Achieve | Net Captured | % of Plan | Status |
|---|---|---|---|---|---|---|---|---|

### Chart-of-Accounts Mapping
[Step 4 — mapping table + unmapped/policy flags]

### Integration-Cost Budget

| Category | Budget | Actual to date | Variance | Owner |
|---|---|---|---|---|

### Reporting Cadence
[Step 6 — flash/monthly/board cadence, owners, dashboard definition]

## Verification

- [ ] Plan sequenced by phase with owners, dependencies, and milestones.
- [ ] Day-1 readiness checklist covers close, treasury, payroll, AP/AR, controls, TSAs.
- [ ] Synergy baseline locked pre-deal; capture measured against baseline, not budget.
- [ ] Captured synergies netted of costs-to-achieve and dis-synergies.
- [ ] Captured run-rate compared to the underwritten target (% of plan).
- [ ] Chart-of-accounts mapping complete; unmapped accounts and policy decisions flagged.
- [ ] Integration costs budgeted and tracked actual vs. budget.
- [ ] Reporting cadence and owners defined; synergy dashboard ties to the thesis.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Synergies measured against a budget that already contains them | Lock a pre-deal baseline; capture is measured against the baseline |
| Gross synergy capture overstated | Net of costs-to-achieve and dis-synergies; report net and % of plan |
| Day-1 assumed operational without proof | Explicit readiness checklist with status and contingency required |
| Integration costs running open-ended | Budget by category and track actual vs. budget with variance flags |
| TSA cliff ignored | Document TSA scope and end-dates; flag dependencies at expiry |
| "On track" claimed without a baseline tie | Synergy dashboard must reconcile to the underwritten deal thesis |
