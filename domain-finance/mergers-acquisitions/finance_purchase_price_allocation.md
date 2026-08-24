---
title: "Purchase Price Allocation — Intangibles, Step-Up, Deferred Tax, and Goodwill Waterfall"
category: finance/mergers-acquisitions
description: "Allocate purchase consideration to identifiable assets and liabilities at fair value: build the consideration-transferred bridge, the asset step-up and intangible schedule with useful lives, the deferred-tax effect, and the goodwill residual — feeding pro-forma D&A and the merger model."
techniques:
  - NE-11
  - ST-02
  - DS-02
  - QA-01
  - QA-04
difficulty: advanced
tags:
  - purchase-price-allocation
  - ppa
  - goodwill
  - intangibles
  - deferred-tax
  - asset-step-up
updated: "2026-06-08"
related_prompts:
  - domain-finance/mergers-acquisitions/finance_ma_deal_model_builder.md
  - domain-finance/mergers-acquisitions/finance_financial_due_diligence_workstream.md
  - domain-finance/mergers-acquisitions/finance_earnout_structuring_analysis.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice and not accounting or tax advice. PPA for financial reporting requires a qualified valuation specialist and auditor; this prompt structures the modeling logic only.**

## Objective

Build the purchase price allocation (PPA) logic used in a merger model: bridge from offer price to total consideration transferred, fair-value the acquired net identifiable assets (including intangible step-ups and useful lives), compute the deferred-tax liability/asset arising from book-vs-tax basis differences, and solve goodwill as the residual — then translate the result into the incremental D&A and balance-sheet entries that flow to the pro-forma statements.

## When to Use

- Producing the PPA inputs (goodwill, intangibles, step-up D&A, DTL) for a merger or accretion/dilution model
- Estimating how much of a deal's purchase price lands in amortizing intangibles vs. non-amortizing goodwill
- Assessing the EPS drag from intangible amortization and the deferred-tax mechanics of a stock vs. asset deal
- Diligence on a seller's preliminary PPA, or scenario analysis on step-up assumptions
- Note: financial-reporting PPA under ASC 805 / IFRS 3 requires a third-party valuation; this is a modeling aid

## Inputs / Context Required

- Equity purchase price / offer; form of deal (stock purchase vs. asset purchase / 338(h)(10) election) — drives tax-basis treatment
- Target balance sheet: book values of assets and liabilities at close
- Fair-value estimates (or assumptions) for: PP&E, inventory, identifiable intangibles (customer relationships, technology/IP, trademarks/brands, non-competes, backlog), and assumed liabilities
- Useful-life assumptions per intangible class; amortization method (straight-line default)
- Tax rate; whether step-up is tax-deductible (asset deal / 338 election) or not (typical stock deal)
- Accounting framework (US GAAP ASC 805 / IFRS 3)
- Existing goodwill/intangibles on target books (eliminated and replaced)

## Constraints

### Must
- Compute consideration transferred including the fair value of any contingent consideration/earnout and equity issued (NE-11).
- Fair-value each acquired asset and liability; show book value, fair-value adjustment (step-up/(down)), and fair value (DS-02).
- Schedule identifiable intangibles separately with useful life and annual amortization: `Annual Amort_i = FV Intangible_i ÷ Useful Life_i`.
- Compute the deferred tax on book-vs-tax basis differences: in a non-deductible stock deal, `DTL = Σ taxable step-up × tax rate`; state when step-up is deductible (no DTL, tax-amortizable goodwill).
- Solve goodwill as a residual: `Goodwill = Consideration − Fair Value of Net Identifiable Assets`; goodwill cannot be negative without triggering a bargain-purchase gain (flag it).
- Translate to pro-forma impact: incremental D&A, the DTL on the balance sheet, and how amortization unwinds the DTL over time.
- State confidence/uncertainty on fair-value inputs (QA-04); these are estimates pending a formal valuation.

### Must Not
- Plug goodwill without first fair-valuing identifiable intangibles (under-allocating to intangibles overstates goodwill and hides EPS drag).
- Omit the deferred-tax liability in a non-deductible step-up — this both understates goodwill and misstates the balance sheet.
- Amortize goodwill (US GAAP: goodwill is tested for impairment, not amortized; IFRS 3 likewise — note jurisdiction/private-company alternatives if relevant).
- Carry over the target's existing goodwill/intangibles; they are replaced.
- Present a negative goodwill residual as ordinary; it signals a bargain purchase (gain to income) and requires re-checking fair values.

## Instructions

**Step 1 — Consideration transferred**

```
Consideration = Cash paid + Fair value of equity issued
              + Fair value of contingent consideration (earnout, at fair value)
              + Assumed debt-like obligations (if part of consideration)
   (Transaction costs are expensed under ASC 805 / IFRS 3 — not part of consideration; state treatment.)
```

**Step 2 — Fair-value the acquired balance sheet (DS-02)**

| Asset/Liability | Book Value | FV Adjustment (step-up/(down)) | Fair Value |
|---|---|---|---|
| Cash | | — | |
| AR | | | |
| Inventory | | +step-up | |
| PP&E | | +step-up | |
| Identifiable intangibles (new) | 0 | + recognized FV | |
| Existing goodwill/intangibles | (eliminate) | | 0 |
| Assumed liabilities | | | |
| Deferred tax (Step 4) | | | |
| **Net Identifiable Assets (FV)** | | | |

**Step 3 — Intangible amortization schedule**

```
For each intangible class i: Annual Amort_i = FV Intangible_i ÷ Useful Life_i (years)
Total incremental intangible amortization (Year t) = Σ Annual Amort_i (while life remains)
  (trademarks may be indefinite-lived → not amortized but impairment-tested; flag if so)
```

**Step 4 — Deferred tax on step-up**

```
Non-deductible step-up (typical stock deal):
  DTL = (Σ book step-ups on assets − step-downs) × tax rate
  Goodwill is grossed up because the DTL increases net identifiable liabilities.
  DTL unwinds as step-up assets are depreciated/amortized (deferred tax benefit each year).

Tax-deductible step-up (asset deal / 338(h)(10)):
  No DTL on step-up; tax basis = book basis; goodwill is tax-amortizable (typically 15 yrs in US).
```

**Step 5 — Goodwill residual (QA-01)**

```
Goodwill = Consideration − Net Identifiable Assets at Fair Value (incl. DTL)
Check: Goodwill ≥ 0. If negative → bargain purchase gain → re-verify fair values before booking gain.
```

**Step 6 — Pro-forma impact translation**

```
Incremental pre-tax D&A_t = intangible amortization_t + incremental PP&E depreciation from step-up_t
After-tax EPS drag_t = Incremental D&A_t × (1 − tax rate) ÷ pro-forma shares
Balance sheet: add goodwill, new intangibles, stepped-up PP&E, DTL; eliminate target equity & old goodwill.
```

**Step 7 — Sensitivity & uncertainty (QA-04)**

- Vary the intangible/goodwill split (e.g., 30% vs. 50% of excess to intangibles): show the EPS-drag range.
- Vary useful lives (±2 years) on the largest intangible.
- State which inputs are estimates pending a formal valuation and the confidence level of each.

## Output Format

### Consideration Transferred
[Step 1 buildup]

### Fair-Value Allocation
[Step 2 table]

### Intangible & D&A Schedule

| Intangible | Fair Value | Useful Life | Annual Amort. |
|---|---|---|---|
| Customer relationships | | | |
| Technology/IP | | | |
| Trademarks/brands | | | |
| Non-compete / backlog | | | |
| **Total** | | | |

### Deferred Tax
[Step 4 — DTL (or none, with rationale) and unwind logic]

### Goodwill Residual
[Step 5 — calculation and non-negativity check]

### Pro-Forma Impact

| Metric | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Incremental D&A | | | |
| After-tax EPS drag | | | |
| DTL balance | | | |

### Sensitivity & Uncertainty
[Step 7 — intangible/goodwill split range, useful-life sensitivity, confidence flags]

## Verification

- [ ] Consideration includes equity issued and contingent consideration at fair value; transaction costs expensed (stated).
- [ ] Each asset/liability shows book value, FV adjustment, and fair value.
- [ ] Identifiable intangibles fair-valued before goodwill is solved.
- [ ] Useful lives stated; indefinite-lived intangibles flagged as non-amortizing.
- [ ] Deferred tax computed correctly for the deal form (non-deductible vs. deductible step-up).
- [ ] Goodwill solved as residual and is non-negative (bargain purchase flagged if not).
- [ ] Goodwill is not amortized (US GAAP/IFRS); impairment-tested instead.
- [ ] Target's existing goodwill/intangibles eliminated.
- [ ] Pro-forma incremental D&A and EPS drag computed; DTL unwind shown.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Plugging goodwill to minimize visible EPS drag | Identifiable intangibles must be fair-valued first; sensitivity on the intangible/goodwill split required |
| Omitting the DTL on non-deductible step-up | DTL computed explicitly; it grosses up goodwill and must appear on the balance sheet |
| Amortizing goodwill | Goodwill is impairment-tested, not amortized; only identifiable intangibles amortize |
| Treating step-up as tax-deductible by default | Deal form (stock vs. asset/338) drives deductibility; state it and tax the step-up accordingly |
| Negative goodwill booked silently | Bargain-purchase residual triggers a re-check of fair values and a gain-to-income flag |
| Presenting fair values as precise | These are estimates pending a formal ASC 805/IFRS 3 valuation; confidence flagged per input |
