---
title: "Month-End Close Checklist Builder — Owners, Dependencies, and SLAs"
category: finance/accounting-controllership
description: "Generate a sequenced month-end close checklist with task owners, upstream/downstream dependencies, day-of-close timing, and SLAs — converting an ad hoc close into a controlled, repeatable, auditable process."
techniques:
  - ST-02
  - DT-02
  - NE-06
  - DS-06
  - QA-01
difficulty: beginner
tags:
  - month-end-close
  - close-calendar
  - controllership
  - dependencies
  - sla
  - process-design
updated: "2026-06-08"
related_prompts:
  - domain-finance/accounting-controllership/finance_account_reconciliation_protocol.md
  - domain-finance/accounting-controllership/finance_journal_entry_review_protocol.md
  - domain-finance/accounting-controllership/finance_management_reporting_kpi_pack.md
  - domain-finance/field_guide.md
---

**Informational only — not accounting, audit, or tax advice. Verify all standard references against current authoritative guidance (FASB ASC / IASB IFRS).**

## Objective

Produce a structured, day-numbered month-end close checklist that assigns an owner and reviewer to every task, maps the dependency chain (what must finish before each task can start), assigns a target completion day and SLA, and flags the critical path — turning a fragile, tribal-knowledge close into a controlled and repeatable process that survives staff turnover and audit scrutiny.

---

## When to Use

- Standing up a close calendar for the first time, or replacing a spreadsheet that lives in one person's head.
- Diagnosing why the close runs late: identifying bottlenecks, serial dependencies, and single points of failure.
- Onboarding a new controller, accounting manager, or staff accountant who needs the close documented.
- Preparing for an audit or SOX walkthrough where the close process must be demonstrable.
- **Do not use** as a substitute for an ERP-integrated close-management tool's actual task status, or to certify that the close was performed correctly — this produces the plan and the control structure, not evidence of execution.

---

## Inputs / Context Required

```
<close_context>
Entity / consolidation scope:
Accounting framework: US GAAP | IFRS
ERP / GL system (e.g., NetSuite, SAP, Oracle, QuickBooks):
Target close length (business days, e.g., "Day 5 close"):
Reporting cadence: monthly | quarterly close embedded | both

TEAM (roles available to assign):
- Controller / accounting manager:
- Staff / senior accountants (count and specialties, e.g., AR, AP, payroll, inventory):
- FP&A / reporting:
- External providers (outsourced payroll, tax, etc.):

KNOWN CLOSE ACTIVITIES (list what you do today; leave blank to use standard set):
- Sub-ledger cutoffs (AR, AP, payroll, inventory, fixed assets):
- Accruals / deferrals routinely booked:
- Intercompany / consolidation steps:
- Reconciliations performed:
- Reporting deliverables and recipients:

PAIN POINTS (optional):
- Where does the close currently slip?
- Any recurring late inputs from outside the team?
</close_context>
```

---

## Constraints

### Must
- Sequence tasks by **dependency**, not alphabetically — every task lists its predecessor(s) so the critical path is visible.
- Assign exactly one **accountable owner** and one **reviewer** to each task (segregation of preparer and reviewer).
- Number each task by **close day** (Day −2 pre-close through Day N final), and assign an **SLA** (target completion time on that day).
- Group tasks into standard close phases: **Pre-close / cutoff → Sub-ledger close → Journal entries (accruals, deferrals, allocations) → Reconciliations → Intercompany & consolidation → Review & analytics → Reporting & sign-off**.
- Identify the **critical path** explicitly: the longest dependency chain that determines minimum close length.
- Flag tasks that depend on **external inputs** (bank statements, payroll provider, tax) as schedule risks.
- Include a **close sign-off / certification** gate as the final task.
- Mark which tasks are **SOX-relevant key controls** if the entity is in scope (note "if applicable").

### Must Not
- Invent the team's actual headcount, ERP, or activities not supplied — if inputs are blank, use a clearly-labeled standard template and state the assumption.
- Assign the same person as both preparer and reviewer of the same task.
- Present the checklist as evidence the close was completed — it is a plan, not a status report.
- Fabricate specific SLA times as if they were the entity's policy; present SLAs as recommended targets the user confirms.
- Collapse dependent tasks into the same day where one genuinely cannot start until another finishes.

---

## Instructions

1. **Define the close window.** From the target close length, lay out the day grid (Day −2, −1, 0/Day 1, …, Day N). Day 1 is typically the first business day after period end.

2. **Enumerate tasks by phase.** Walk the seven phases in order. For each supplied or standard activity, create one task line.

3. **Map dependencies.** For each task, record predecessor(s). Use this dependency logic:

```
Cutoff (AR/AP/payroll/inventory)  →  Sub-ledger close
Sub-ledger close                  →  Accrual & deferral JEs
Accruals / deferrals / allocations →  Account reconciliations
Reconciliations                   →  Intercompany & consolidation
Consolidation                     →  Flux / variance analytics
Analytics clean                   →  Reporting package
Reporting reviewed                →  Close sign-off / certification
```

4. **Identify the critical path.** Trace the longest unbroken predecessor chain. The sum of its task durations is the floor on close length — shortening the close means attacking this chain (parallelize, pre-close, or automate).

5. **Assign owners and reviewers.** One accountable owner; a different reviewer. Never the same person for both on a given task.

6. **Set SLAs.** Assign a target day and time of day. Tasks waiting on external inputs get a "ready-by" dependency note and an escalation contact.

7. **Tag controls.** If SOX-relevant, mark key controls (e.g., reconciliations, JE review, management review of flux) and note frequency = monthly.

8. **Verification pass (QA-01).** Confirm no task precedes its predecessor in day-order; confirm every task has owner ≠ reviewer; confirm the sign-off gate is last.

---

## Output Format

```
## Month-End Close Checklist — [Entity]
Framework: [US GAAP / IFRS] | ERP: [system] | Target: Day [N] close
Prepared: [date] | Status: PLAN (not execution evidence)

### Critical Path (close-length driver)
Cutoff → Sub-ledger close → Accruals → Reconciliations → Consolidation → Reporting → Sign-off
Estimated minimum close length: Day [N]  (illustrative)

### Close Calendar
| # | Day | Phase | Task | Owner | Reviewer | Predecessor(s) | SLA (target) | Key Control? |
|---|-----|-------|------|-------|----------|----------------|--------------|--------------|
| 1 | D−1 | Cutoff | Communicate AP cutoff; final invoices in | AP Accountant | Controller | — | D−1 5:00pm | No |
| 2 | D1 | Sub-ledger | Close AR sub-ledger; post final cash receipts | AR Accountant | Acct Mgr | #1 | D1 noon | No |
| 3 | D1 | Sub-ledger | Close AP / run accrual of unvouchered receipts | AP Accountant | Acct Mgr | #1 | D1 3:00pm | No |
| 4 | D2 | Journal entries | Book payroll accrual | Staff Acct | Acct Mgr | #2,#3 | D2 noon | Yes |
| 5 | D2 | Journal entries | Book prepaid amortization / deferrals | Staff Acct | Acct Mgr | #3 | D2 3:00pm | Yes |
| 6 | D2 | Journal entries | Run depreciation; post FA roll-forward | Staff Acct | Acct Mgr | #3 | D2 4:00pm | Yes |
| 7 | D3 | Reconciliations | Reconcile all balance-sheet accounts (see protocol) | Assigned owners | Controller | #4,#5,#6 | D3 EOD | Yes (key) |
| 8 | D3 | Intercompany | Match & eliminate IC; settle imbalances | Acct Mgr | Controller | #7 | D3 EOD | Yes |
| 9 | D4 | Consolidation | Run consolidation; FX translation if applicable | Acct Mgr | Controller | #8 | D4 noon | Yes |
| 10| D4 | Analytics | Prepare flux/variance vs prior & budget; explain >threshold | FP&A | Controller | #9 | D4 4:00pm | Yes (mgmt review) |
| 11| D5 | Reporting | Draft management reporting package | FP&A | Controller | #10 | D5 noon | No |
| 12| D5 | Sign-off | Controller close certification & lock GL period | Controller | CFO | #11 | D5 EOD | Yes |

### External-Input Schedule Risks
| Input | Provider | Needed by | Escalation contact |
|-------|----------|-----------|--------------------|
| Bank statements | [Bank] | D1 am | [name] |
| Payroll register | [Provider] | D1 | [name] |

### Open Decisions / Confirmations Needed from User
- Confirm recommended SLAs match policy.
- Confirm SOX scope tags (which tasks are key controls).
```
*All days, names, and SLAs above are illustrative until confirmed against the entity's actual team and policy.*

---

## Verification

- [ ] Every task has a predecessor mapping (or "—" for true starts) and appears after its predecessor in day-order.
- [ ] Every task has one owner and a different reviewer.
- [ ] The seven close phases are present and in order.
- [ ] The critical path is identified and the minimum close length is stated.
- [ ] External-input dependencies are flagged with a ready-by time and escalation contact.
- [ ] A final close sign-off / period-lock task exists as the last item.
- [ ] SOX key-control tags applied (or "if applicable" noted) where the entity is in scope.
- [ ] No supplied figures or team facts were invented; assumptions labeled.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Presenting the checklist as proof the close happened | Label output "PLAN (not execution evidence)"; status comes from the close tool, not this artifact |
| Inventing the team's ERP, headcount, or SLAs | Use a clearly-labeled standard template when inputs are blank; mark SLAs as recommended targets to confirm |
| Same person preparing and reviewing a task (SoD gap) | Enforce owner ≠ reviewer on every line; reject any task that violates it |
| Hiding the real bottleneck by parallelizing dependent tasks on paper | Respect true predecessor logic; tasks that genuinely block each other cannot share a day |
| Applying GAAP-specific steps to an IFRS filer or vice versa | Confirm framework; e.g., consolidation/FX and lease steps differ — do not assume US GAAP defaults for an IFRS entity |
| Treating SOX key-control tags as authoritative | Tags are recommendations to confirm with the entity's control owner / external auditor |
