---
title: "Financial Due Diligence Workstream — QoE, Net Debt, and Working-Capital Target"
category: finance/mergers-acquisitions
description: "Run the buy-side financial due diligence workstream: normalize EBITDA (quality of earnings), build the net-debt and debt-like-items schedule, set the normalized working-capital peg, and surface findings that feed the purchase agreement's price-adjustment mechanics."
techniques:
  - DT-02
  - ST-02
  - NE-11
  - QA-02
  - DS-06
difficulty: advanced
tags:
  - financial-due-diligence
  - quality-of-earnings
  - net-debt
  - working-capital-peg
  - debt-like-items
  - m-and-a
updated: "2026-06-08"
related_prompts:
  - domain-finance/financial-statement-analysis/finance_quality_of_earnings_review.md
  - domain-finance/mergers-acquisitions/finance_purchase_price_allocation.md
  - domain-finance/mergers-acquisitions/finance_ma_deal_model_builder.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance and legal professionals before use in any transaction or decision.**

## Objective

Execute the buy-side financial due diligence (FDD) workstream that produces the three numbers a purchase agreement turns on: (1) normalized/quality-of-earnings (QoE) EBITDA, (2) the net-debt and debt-like-items schedule used to bridge enterprise value to equity value, and (3) the normalized working-capital target ("peg") that governs the closing adjustment — each built bottom-up with adjustments evidenced and quantified, and findings prioritized by deal impact.

## When to Use

- Buy-side diligence on an acquisition prior to signing or before finalizing price mechanics
- Validating a seller-prepared QoE or rebuilding an independent view
- Setting or negotiating the net-debt definition and working-capital peg in the SPA
- Identifying earnings-quality, balance-sheet, and proof-of-cash red flags that change price or structure
- Preparing the diligence findings memo for an investment committee

## Inputs / Context Required

- Target financials: monthly/quarterly P&L (3 years), balance sheet, cash flow; trial balance if available
- Accounting framework (US GAAP / IFRS); revenue recognition policy; audit status (audited/reviewed/compiled)
- Management adjustments/add-backs already proposed (the seller's QoE bridge, if any)
- Debt schedule, lease obligations, and off-balance-sheet commitments
- Working-capital components by month (AR, inventory, AP, accruals) for ≥24 months
- Deal context: enterprise value/offer, signing/closing timeline, key value-driver assumptions

## Constraints

### Must
- Build the QoE EBITDA bridge bottom-up; every add-back/deduction tagged as non-recurring, out-of-period, pro-forma, or accounting-driven, with $ and evidence (NE-11, DT-02).
- Separately classify each add-back's quality: hard (contracted/one-time, well-evidenced) vs. soft (run-rate/judgmental); report adjusted EBITDA on a hard-only and a full basis.
- Build the net-debt schedule and a **debt-like items** list (e.g., unfunded pensions, deferred/earnout consideration, accrued bonuses, capital leases, factored receivables, customer deposits, unpaid capex, tax liabilities).
- Set the working-capital peg from a normalized trailing-twelve-month (TTM) average, adjusted for seasonality and one-offs: show the monthly series and the average used.
- Run a proof-of-cash: reconcile reported EBITDA to operating cash flow to bank statements; flag gaps.
- Prioritize findings by deal impact (DS-06): price (EV multiple × EBITDA delta), bridge (net-debt/peg delta), or structural (indemnity/escrow/closing-condition).
- Quantify the price impact of EBITDA adjustments: `ΔPrice ≈ EBITDA adjustment × EV/EBITDA multiple`.

### Must Not
- Accept management add-backs without independent evidence; soft add-backs must be flagged and stress-tested.
- Conflate net debt with debt-like items silently — list debt-like items separately so the SPA definition is explicit.
- Set the working-capital peg from a single month or a cherry-picked period.
- Present an adjusted EBITDA without showing the bridge from reported/statutory EBITDA.
- Ignore the EBITDA-to-cash gap (a clean P&L with poor cash conversion is a red flag).

## Instructions

**Step 1 — Quality-of-earnings EBITDA bridge (DT-02, NE-11)**

```
Reported EBITDA (statutory)
  ± Out-of-period items (revenue/cost in wrong period)
  + Non-recurring costs (litigation, restructuring, one-time fees) [evidence each]
  + Owner/related-party normalizations (above-market comp, personal expenses)
  ± Accounting-policy adjustments (revenue recognition, capitalization vs. expense)
  − Pro-forma run-rate items only if contractually supported
= Adjusted EBITDA (full)
  of which Hard add-backs vs. Soft add-backs (report both subtotals)

Price impact of each adjustment = Adjustment $ × EV/EBITDA multiple
```

**Step 2 — Proof-of-cash and earnings-quality checks**

```
Reconcile: Adjusted EBITDA → CFO → cash movements per bank statements
EBITDA-to-cash conversion = CFO ÷ Adjusted EBITDA  [persistently < ~0.7 → investigate]
Flag: rising DSO, channel stuffing, capitalized costs that should be expensed,
      revenue pulled forward, deferred-revenue trends.
```

**Step 3 — Net debt and debt-like items schedule**

```
Net Debt = Total Interest-Bearing Debt + Finance Leases − Cash & Equivalents (less restricted/trapped cash)

Debt-like items (added to net debt in the equity bridge), each evidenced:
  + Unfunded pension / post-employment obligations
  + Deferred/earnout/contingent consideration
  + Accrued but unpaid bonuses / management fees
  + Unpaid/deferred capex and overdue payables beyond normal terms
  + Customer deposits / deferred revenue with cash-cost to fulfill
  + Unprovided tax liabilities; factored/securitized receivables

Equity Value = Enterprise Value − Net Debt − Debt-like items + Surplus assets
```

**Step 4 — Working-capital peg (NWC target)**

```
NWC = (AR + Inventory + other current assets) − (AP + accruals + other current liabilities)
   (exclude cash and debt items — those sit in net debt)

Normalize the monthly NWC series: remove one-offs, adjust for seasonality.
Peg = TTM average normalized NWC (or business-appropriate basis; state it)

Closing adjustment = Actual NWC at close − Peg
  (above peg → price up to seller; below peg → price down to buyer)
```

**Step 5 — Findings prioritization (DS-06)**

Classify each finding: Price | Bridge | Structural; quantify $ impact; rate severity High/Med/Low.

**Step 6 — Adversarial stress-test (QA-02)**
- Recompute adjusted EBITDA on a hard-add-back-only basis: how much price evaporates?
- Are any add-backs actually recurring (e.g., "one-time" costs that appear every year)? Re-test the trailing 3 years.
- Does the peg understate true working-capital need (seller drained WC pre-sale)? Check AP stretch and inventory run-down near the measurement date.
- Name the confirmation-bias risk (accepting the seller's bridge); require an independent rebuild as the disconfirming check.

## Output Format

### QoE EBITDA Bridge

| Adjustment | $ | Type (NR/OOP/PF/Acctg) | Quality (Hard/Soft) | Evidence | Price impact (× multiple) |
|---|---|---|---|---|---|
| Reported EBITDA | | — | — | — | — |
| ... | | | | | |
| Adjusted EBITDA (full) | | | | | |
| Adjusted EBITDA (hard only) | | | | | |

### Proof-of-Cash
[Step 2 — EBITDA→CFO→cash reconciliation; conversion ratio; flags]

### Net Debt & Debt-Like Items

| Item | $ | Evidence | Included in SPA net-debt def? |
|---|---|---|---|
| Total debt + finance leases | | | |
| Less: cash (ex-restricted) | | | |
| Debt-like: [each] | | | |
| **Net debt for equity bridge** | | | |

### Working-Capital Peg
[Step 4 — monthly normalized NWC series, seasonality note, peg value, basis]

### Prioritized Findings

| Finding | Bucket (Price/Bridge/Structural) | $ Impact | Severity |
|---|---|---|---|

### Stress-Test Summary
[Step 6 findings]

## Verification

- [ ] Adjusted EBITDA shown as a bridge from reported/statutory, every line evidenced.
- [ ] Hard vs. soft add-backs subtotaled separately.
- [ ] Price impact of EBITDA adjustments quantified at the deal multiple.
- [ ] Proof-of-cash reconciliation performed; conversion ratio reported.
- [ ] Net debt and debt-like items listed separately with evidence.
- [ ] Working-capital peg built from a normalized TTM series, not a single period.
- [ ] Findings classified Price/Bridge/Structural and quantified.
- [ ] Seller add-backs independently tested over the trailing 3 years for recurrence.
- [ ] Restricted/trapped cash excluded from net-debt cash.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Accepting seller's adjusted EBITDA at face value | Independent bottom-up rebuild required; hard-only EBITDA reported alongside full |
| "One-time" costs that recur annually | Trailing-3-year recurrence test on every non-recurring add-back |
| Net-debt definition that quietly omits debt-like items | Explicit debt-like-items list mapped to the SPA definition |
| Peg set from a favorable single month | Normalized TTM series shown; seasonality adjustment required |
| Clean P&L masking poor cash conversion | Proof-of-cash mandatory; flag conversion persistently below ~0.7 |
| Seller draining working capital pre-close | Check AP stretch/inventory run-down near measurement date; adjust peg basis |
