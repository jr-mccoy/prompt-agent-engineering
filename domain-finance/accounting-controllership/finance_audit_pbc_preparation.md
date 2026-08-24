---
title: "Audit PBC Preparation — Request List and Supporting-Schedule Package"
category: finance/accounting-controllership
description: "Prepare an audit Prepared-By-Client (PBC) list and supporting-schedule package: map requests to significant accounts and assertions, build tie-out-ready schedules that agree to the trial balance, assign owners and due dates, and pre-empt common auditor follow-ups."
techniques:
  - ST-02
  - DS-06
  - NE-06
  - QA-01
  - DT-02
difficulty: intermediate
tags:
  - audit-pbc
  - audit-prep
  - supporting-schedules
  - tie-out
  - trial-balance
  - documentation
updated: "2026-06-08"
related_prompts:
  - domain-finance/accounting-controllership/finance_account_reconciliation_protocol.md
  - domain-finance/accounting-controllership/finance_month_end_close_checklist.md
  - domain-finance/accounting-controllership/finance_technical_accounting_memo_writer.md
  - domain-finance/field_guide.md
---

**Informational only — not accounting, audit, or tax advice. Verify all standard references against current authoritative guidance (FASB ASC / IASB IFRS).**

## Objective

Produce an organized audit Prepared-By-Client (PBC) package: a request list mapped to significant accounts and financial-statement assertions, a set of supporting schedules that tie to the trial balance, clear ownership and due dates, and a pre-emptive set of explanations for the follow-ups auditors typically raise — so the audit runs efficiently and management's schedules are tie-out-ready on day one of fieldwork.

---

## When to Use

- Preparing for an interim or year-end financial-statement audit or review.
- Responding to an auditor's PBC / open-items list and converting it into an owned, scheduled work plan.
- Building reusable supporting schedules (roll-forwards, agings, reconciliations) that agree to the GL.
- Reducing audit friction by anticipating common auditor questions before they're asked.
- **Do not use** to assert that schedules are "audit-proof" or that the audit will be clean — this organizes and substantiates management's support; the audit conclusion is the auditor's.

---

## Inputs / Context Required

```
<pbc_context>
Entity / framework: US GAAP | IFRS
Audit type: full audit | review | interim | single-area:
Period under audit:
Auditor (firm) and known focus areas (if any):

FINANCIALS:
- Trial balance / financial statements for the period:
- Prior-year audited figures (for roll-forwards / comparatives):

SIGNIFICANT ACCOUNTS / AREAS in scope:
- [e.g., revenue, AR/allowance, inventory, fixed assets, debt, leases, equity, accruals, tax]

REQUEST LIST (if auditor already sent one — paste it):

TEAM:
- Owners available to prepare schedules:
- Document repository / data-room location:
</pbc_context>
```

---

## Constraints

### Must
- Map each PBC request to the **significant account/disclosure** and the **assertion(s)** it supports (existence, completeness, accuracy/valuation, rights/obligations, cutoff, presentation).
- Specify, for each request, the **deliverable form**: roll-forward, aging, reconciliation, detail listing, contract/agreement, memo, confirmation support.
- Require every numeric schedule to **tie to the trial balance** — state the tie-out point (schedule total = GL/TB balance) and include a tie-out reference.
- Assign each item an **owner**, a **due date** (sequenced before fieldwork), and a **status**.
- Order requests by **audit phase**: planning/PBC-1 (TB, policies, org docs) → interim/controls → substantive (account schedules) → completion (subsequent events, reps, disclosures).
- Build **standard supporting schedules** correctly:
  - Roll-forward: `Beginning + Additions − Disposals/Reductions ± Adjustments = Ending` (ties to TB).
  - Aging: buckets summing to the GL balance.
  - Reconciliation: GL vs independent source (link to the reconciliation protocol).
- **Pre-empt common follow-ups** (DT-02): for each area, list the typical auditor question and the explanation/support to have ready (e.g., unusual fluctuations, large/round entries, related-party items, estimates and their methodology).
- Track **open items** and a **single source of truth** for delivered documents (no duplicate/version confusion).

### Must Not
- Invent trial-balance figures, prior-year balances, or schedule contents not supplied.
- Provide a schedule whose total does not reconcile to the TB without flagging the difference.
- Assert the audit outcome or that schedules guarantee a clean opinion.
- Mix periods or use unaudited figures where audited comparatives are required without noting it.
- Omit the assertion mapping — a PBC list with no assertion linkage is just a document dump.
- Hand over draft/uncontrolled versions as the audit support.

---

## Instructions

1. **Anchor to the trial balance.** Confirm the TB total and the significant accounts; comparatives sourced from prior-year audited figures.

2. **Translate / build the request list.** If the auditor sent a list, map each item; otherwise generate a standard list by significant account. For each request, set deliverable form, account, assertion(s), owner, due date.

3. **Sequence by phase.** Group into planning, interim/controls, substantive, completion; due dates ladder up to fieldwork start.

4. **Design supporting schedules.** For each numeric area, specify the schedule structure and the **tie-out point** to the TB. Build roll-forwards/agings/recs with the formulas above.

5. **Pre-empt follow-ups.** For each significant area, list the likely auditor inquiry and the ready explanation/support (estimate methodology, fluctuation drivers, large-entry support, related-party disclosure).

6. **Assign and track.** Owner + due date + status per item; maintain an open-items log and a controlled document index.

7. **Verification (QA-01).** Confirm every request maps to an account + assertion; confirm every numeric schedule states its TB tie-out; confirm owners and due dates are set and sequenced before fieldwork.

---

## Output Format

```
## Audit PBC Package — [Entity], [Period]
Framework: [US GAAP/IFRS] | Audit type: [__] | Fieldwork start: [date]
Status: PREPARATION (management support; audit conclusion is the auditor's)

### TB Anchor
Total assets per TB: [illustrative] 50,000,000  (schedules tie to this TB)

### PBC Request List
| # | Phase | Request | Account / disclosure | Assertion(s) | Deliverable form | Owner | Due | Status | Doc ref |
|---|-------|---------|----------------------|--------------|------------------|-------|-----|--------|---------|
| 1 | Planning | Final TB + mapping to FS | All | Presentation | TB export | Controller | T−10 | Done | TB-01 |
| 2 | Substantive | AR aging + allowance support | AR / Allowance | Existence, Valuation | Aging + memo | AR Lead | T−5 | In prog | AR-01 |
| 3 | Substantive | Fixed-asset roll-forward | PP&E | Completeness, Valuation | Roll-forward | Staff Acct | T−5 | Open | FA-01 |
| 4 | Substantive | Debt schedule + agreements | Debt | Rights/Oblig, Accuracy | Schedule + contracts | Treasury | T−5 | Open | DT-01 |
| 5 | Completion | Subsequent-events memo | Disclosures | Presentation | Memo | Controller | T+5 | Open | SE-01 |

### Supporting Schedule Specs (tie-out ready)
| Schedule | Structure | Tie-out point |
|----------|-----------|---------------|
| FA roll-forward | Beg + Additions − Disposals + Depr = End | End = PP&E net per TB |
| AR aging | Current/30/60/90+ buckets | Sum = AR per TB |
| Debt schedule | Per-facility principal + accrued interest | Total = debt per TB |

### Pre-Empted Auditor Follow-Ups
| Area | Likely question | Ready explanation / support |
|------|-----------------|------------------------------|
| Allowance for credit losses | How is the estimate derived? | CECL/ECL methodology memo + historical loss rates |
| Revenue cutoff | Sales near period-end real? | Cutoff testing support; shipping/acceptance docs |
| Large/round JEs | Support for top-side entries | JE support package (link to JE review) |

### Open Items Log
| # | Item | Blocker | Owner | Target |
|---|------|---------|-------|--------|
| 3 | FA roll-forward | Awaiting disposal detail | Staff Acct | T−4 |
```
*All figures illustrative until populated from the entity's records.*

---

## Verification

- [ ] Every PBC request maps to a significant account/disclosure and assertion(s).
- [ ] Each request specifies deliverable form, owner, due date, status, doc reference.
- [ ] Requests sequenced by audit phase; due dates ladder before fieldwork.
- [ ] Every numeric schedule states its trial-balance tie-out point.
- [ ] Roll-forwards/agings/recs use correct structure and foot to the TB.
- [ ] Common auditor follow-ups pre-empted with ready support.
- [ ] Open-items log and controlled document index maintained.
- [ ] No invented TB, prior-year, or schedule figures.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Implying the audit will be clean / schedules are "audit-proof" | Label PREPARATION; the audit conclusion is the auditor's, not management's |
| Schedule total that doesn't tie to the TB | Every numeric schedule must state its TB tie-out; flag any difference rather than hide it |
| PBC list as a document dump with no assertion linkage | Map every request to account + assertion(s) |
| Handing over uncontrolled draft versions | Maintain a single controlled document index; deliver final versions only |
| Using unaudited figures where audited comparatives are required | Source comparatives from prior-year audited figures; note any unaudited data |
| Inventing schedule contents to fill the template | Use only supplied data; missing items go to the open-items log |
