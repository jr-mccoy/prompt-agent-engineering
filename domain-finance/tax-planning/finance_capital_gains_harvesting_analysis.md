---
title: "Capital Gains/Loss Harvesting Analysis — Wash-Sale, Bracket, and Holding-Period Awareness"
category: finance/tax-planning
description: "Analyze tax-loss and tax-gain harvesting opportunities across a portfolio with wash-sale 30-day window logic, short- vs long-term character separation, bracket-fill and 0% LTCG-bracket awareness, and NIIT/AMT interaction checks — framed as scenario comparison, not advice."
techniques:
  - NE-11
  - NE-10
  - QA-01
  - QA-02
  - DS-02
difficulty: intermediate
tags:
  - tax-loss-harvesting
  - capital-gains
  - wash-sale
  - bracket-management
  - niit
updated: "2026-06-08"
related_prompts:
  - domain-finance/tax-planning/finance_multi_year_tax_projection.md
  - domain-finance/tax-planning/finance_charitable_giving_tax_strategy.md
  - domain-finance/personal-finance-planning/finance_tax_aware_withdrawal_sequencing.md
  - domain-finance/investing-research/finance_position_sizing_framework.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not tax, legal, or accounting advice. Tax rules change and depend on individual circumstances; filing, representation, and reliance decisions must be made with a qualified tax professional (CPA/EA/tax attorney). Verify all rates, brackets, thresholds, and the wash-sale rule against current tax law as of the analysis date and the applicable federal and state jurisdiction.**

## Objective

Produce an auditable harvesting analysis that identifies candidate lots for tax-loss or tax-gain harvesting, computes the realized-character impact (short-term vs long-term), screens each candidate against the wash-sale window, and projects the after-tax effect under multiple income/bracket scenarios — so the user and their tax professional can compare options. This prompt analyzes; it does not direct trades or filings.

## When to Use

- Year-end review of a taxable brokerage account for loss-harvesting candidates.
- Evaluating gain-harvesting in a low-income year (e.g., a gap year, early retirement, or business-loss year) to use the 0% LTCG bracket.
- Rebalancing a concentrated position while managing the realized-gain tax cost.
- Offsetting a large realized gain elsewhere (e.g., from an M&A event or RSU vest).
- Pre-checking trades against the wash-sale rule before a tax professional finalizes.

## Inputs / Context Required

```
<harvesting_context>
Jurisdiction:
  Federal — filing status: single | MFJ | MFS | HoH
  State — name + does state tax capital gains as ordinary income? (many do; some have no income tax)
Current-year income picture (user-supplied; do NOT assume):
  Ordinary taxable income (pre-cap-gains):     [input current-year figure]
  Filing status:                                [input]
  Marginal ordinary bracket %:                  [input current-year figure; verify with IRS/official source]
  LTCG bracket breakpoints (0% / 15% / 20%):    [input current-year thresholds; verify]
  NIIT threshold for filing status:             [input current-year figure; verify — applies to MAGI over threshold]
  AMT exposure flag:                            yes | no | unknown
Realized YTD: short-term gain/(loss): __  long-term gain/(loss): __
Carryforward losses from prior years: short-term __  long-term __

PORTFOLIO LOTS (repeat per lot):
  Security / ticker:
  Account (must be TAXABLE — exclude IRA/401k):
  Acquisition date:           (drives short vs long term, > 1 year = long-term)
  Cost basis:
  Current market value:
  Unrealized gain/(loss):     = Market value − Cost basis
  Recent purchases of same/substantially identical security in last 30 days? (wash-sale flag)
  Replacement security candidate (to maintain market exposure):

CONSTRAINTS:
  Target realized loss to harvest (if offsetting a known gain): __
  Positions the user will NOT sell (tax-lot lock):
</harvesting_context>
```

## Constraints

### Must
- Separate every candidate into **short-term** (held ≤ 1 year) and **long-term** (held > 1 year) — character drives the rate and the netting order.
- Apply the IRS netting order: ST losses first offset ST gains; LT losses offset LT gains; net ST and net LT are then combined; net capital loss is deductible against ordinary income only up to the annual cap **[input current-year ordinary-offset cap; verify — historically $3,000 / $1,500 MFS]**, with the remainder carried forward.
- Screen every loss-harvest candidate against the **wash-sale rule**: a loss is disallowed if a substantially identical security is purchased within **30 days before or after** the sale (a 61-day window centered on the trade). Flag any buy in IRAs or by a spouse — those trigger wash-sale too.
- Show formula → inputs → result for every tax computation.
- Run scenarios (NE-10) across at least: current-bracket case, a higher-income case (bunched income), and a lower-income case (0% LTCG harvest opportunity).
- Flag NIIT and AMT interactions where realized gains push MAGI over the NIIT threshold or where harvesting interacts with AMT.
- State that wash-sale, basis, and bracket figures must be confirmed by a tax professional before any trade.

### Must Not
- Assert specific current-year bracket figures, LTCG breakpoints, NIIT thresholds, or the ordinary-offset cap from memory — require user input or mark `[input current-year figure; verify]`.
- Recommend a specific trade ("sell X now") — present candidates and after-tax scenarios; the decision routes to the user and their professional.
- Ignore the wash-sale window or treat a "similar" ETF swap as automatically safe — substantially-identical determination is a professional judgment.
- Net short-term and long-term incorrectly (e.g., applying LTCG rates to short-term gains, which are taxed as ordinary income).
- Treat tax savings as pure gain without accounting for basis reset (harvesting a loss lowers future basis, deferring — not eliminating — tax unless stepped up at death or given to charity).

## Instructions

**Step 1 — Classify lots by holding period and character.**
```
For each lot:
  Holding period = Analysis date − Acquisition date
  Character = LONG if holding period > 1 year, else SHORT
  Unrealized G/(L) = Market value − Cost basis
Sort: loss-harvest candidates (unrealized loss) and gain-harvest candidates (unrealized gain) separately.
```

**Step 2 — Wash-sale screen (loss candidates only).**
```
For each loss candidate:
  Window = [Sale date − 30 days, Sale date + 30 days]
  Disallowed IF substantially identical security purchased in Window
       in ANY account (incl. IRA, spouse) — including dividend reinvestment.
  If disallowed: loss is deferred; disallowed loss adds to basis of replacement shares.
  Mitigation note: a non-substantially-identical replacement maintains exposure without triggering
       wash-sale — but "substantially identical" is a facts-and-circumstances call for the professional.
Output: PASS / FLAG per candidate.
```

**Step 3 — Apply IRS netting and compute usable loss.**
```
Net ST = (ST realized YTD + ST carryforward) + Σ harvested ST losses
Net LT = (LT realized YTD + LT carryforward) + Σ harvested LT losses
Combine: net ST and net LT.
If net capital loss < 0:
  Ordinary offset this year = min(|net capital loss|, [current-year cap; verify])
  Carryforward = |net capital loss| − ordinary offset
```

**Step 4 — Bracket-fill / gain-harvest logic (for low-income scenarios).**
```
0% LTCG room = max(0, LTCG 0%-bracket ceiling [input; verify] − ordinary taxable income)
Gain that can be harvested at 0% LTCG = min(0% room, available unrealized LT gains)
NOTE: realized LT gains stack ON TOP of ordinary income and can push later dollars into 15%/20%
      and over the NIIT threshold — compute the marginal effect, not just the headline 0%.
```

**Step 5 — After-tax impact per scenario (NE-10).**

| Scenario | Ordinary income | Harvested ST loss used | Harvested LT loss used | Gain harvested @0% | Est. federal tax delta | NIIT delta | State tax delta | Net after-tax benefit |
|---|---|---|---|---|---|---|---|---|
| Current bracket | | | | | | | | |
| Higher-income (bunched) | | | | | | | | |
| Lower-income (0% harvest) | | | | | | | | |

```
Tax delta from loss harvest ≈ Usable loss × Marginal rate on the income it offsets
  (ordinary rate up to the cap; otherwise the capital-gains rate of the gains it nets against)
Basis-reset cost note: future tax on the now-lower-basis replacement is deferred tax, not avoided.
```

**Step 6 — Adversarial stress-test (QA-02).**
- Does any harvest push MAGI over the NIIT threshold, adding the NIIT surtax to all net investment income?
- Does gain-harvesting at "0%" actually cost 15%/20% on the marginal dollars once gains stack on ordinary income?
- Is the user anchored on the headline tax saving while ignoring the deferred-tax basis reset?
- Would a wash-sale flagged buy in a spouse's IRA silently disallow the loss?
- In AMT years, does the loss provide less benefit than at the regular marginal rate?
- Transaction costs and bid-ask spread: do they erode the tax benefit on small lots?

## Output Format

```
## Capital Gains/Loss Harvesting Analysis
Jurisdiction: Federal [status] + State [name] | As of: [date] | Data: user-supplied
Current-year figures: user-supplied / flagged for verification

### Lot Classification
[table: lot, account, holding period, character, unrealized G/(L)]

### Wash-Sale Screen
[table: candidate, sale date, 30-day window, PASS/FLAG, note]

### Netting Result
[ST net, LT net, combined, ordinary offset (capped), carryforward]

### Bracket / 0% Harvest Room (if low-income scenario)
[0% room, harvestable gain, marginal-stacking note]

### After-Tax Scenario Comparison
[Step 5 table]

### Stress-Test Findings
[Step 6 bullets — including NIIT/AMT/basis-reset flags]

### Items to confirm with your tax professional
[wash-sale substantially-identical calls; current-year figures; state treatment]
```

## Verification

- [ ] Every lot classified short vs long term using the >1-year rule.
- [ ] Wash-sale 30-day-before-and-after window applied to all loss candidates, including IRA/spouse buys and dividend reinvestment.
- [ ] IRS netting order applied (ST→ST, LT→LT, then combine); ordinary-offset cap marked as user-supplied/verify.
- [ ] No current-year bracket, breakpoint, NIIT, or cap figure asserted from memory.
- [ ] At least three income scenarios computed (current, higher, lower).
- [ ] NIIT and AMT interactions flagged where applicable.
- [ ] Basis-reset / deferred-tax note included (not presented as permanent savings).
- [ ] State capital-gains treatment addressed.
- [ ] Output frames candidates and scenarios, not a directive to trade.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Presenting harvested losses as permanent tax savings | Show basis reset: lower replacement basis defers tax; only step-up at death or charitable gift removes it — state this explicitly |
| Treating an ETF/fund swap as automatically wash-sale-safe | "Substantially identical" is a facts call; flag for the professional, do not clear it |
| Applying LTCG rates to short-term gains | Short-term gains are ordinary-rate; character separation is mandatory before any rate is applied |
| "0% gain harvest" ignoring marginal stacking | Gains stack on ordinary income; compute the marginal rate on each tranche and any NIIT crossing |
| Missing a wash-sale trigger in an IRA or spouse account | Screen explicitly states IRA and spouse purchases trigger the rule; require those accounts in inputs |
| Asserting current bracket/NIIT thresholds | All such figures marked `[input current-year figure; verify with IRS/official source]` |
| Anchoring on headline rate while ignoring AMT/state | Stress-test requires an AMT-year and a state-tax check before claiming a benefit |
