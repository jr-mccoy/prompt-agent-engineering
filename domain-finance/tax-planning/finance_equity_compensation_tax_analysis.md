---
title: "Equity Compensation Tax Analysis — ISO/NSO/RSU/ESPP Treatment and Exercise/Sale-Timing Scenarios"
category: finance/tax-planning
description: "Analyze the tax treatment of ISOs, NSOs, RSUs, and ESPP across grant/vest/exercise/sale events — including ISO bargain-element AMT, NSO ordinary-income at exercise, RSU vest inclusion, qualifying vs disqualifying dispositions, and 83(b) timing — as scenario comparison, not advice."
techniques:
  - NE-11
  - NE-10
  - QA-01
  - QA-02
  - DT-02
difficulty: advanced
tags:
  - equity-compensation
  - iso
  - nso
  - rsu
  - espp
  - amt
  - 83b
updated: "2026-06-08"
related_prompts:
  - domain-finance/tax-planning/finance_multi_year_tax_projection.md
  - domain-finance/tax-planning/finance_capital_gains_harvesting_analysis.md
  - domain-finance/tax-planning/finance_retirement_account_tax_optimization.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not tax, legal, or accounting advice. Tax rules change and depend on individual circumstances; filing, representation, AMT computation, and reliance decisions must be made with a qualified tax professional (CPA/EA/tax attorney). Verify all rates, AMT exemption/phaseout figures, holding-period rules, and ESPP/ISO limits against current tax law as of the analysis date and the applicable federal and state jurisdiction.**

## Objective

Produce an auditable analysis of an equity-compensation package that (1) classifies each award by type and its taxable events, (2) computes the income and AMT consequences of exercise and sale under multiple timing scenarios, (3) distinguishes qualifying from disqualifying dispositions, and (4) surfaces the AMT/NIIT/concentration risks — so the user and their tax professional can compare timing choices. This prompt analyzes; it does not direct exercises, sales, or filings.

## When to Use

- Deciding whether and when to exercise ISOs (early-exercise + 83(b), exercise-and-hold, or exercise-and-sell).
- Modeling the AMT cost of an ISO exercise before pulling the trigger.
- Planning RSU vest withholding and sell-to-cover vs hold decisions.
- Evaluating ESPP qualifying-disposition holding periods.
- Sequencing a multi-year exercise plan to manage AMT and bracket creep.

## Inputs / Context Required

```
<equity_comp_context>
Jurisdiction: Federal — filing status [single/MFJ/MFS/HoH]; State [name] (note state AMT/conformity varies)
Current-year income (user-supplied; do NOT assume):
  Ordinary taxable income (excl. equity events):  [input]
  Marginal ordinary rate:                          [input current-year figure; verify]
  LTCG breakpoints (0/15/20%):                     [input; verify]
  AMT exemption + phaseout for status:             [input current-year figures; verify]
  NIIT threshold:                                  [input; verify]
Company stock status: private (illiquid) | public (liquid) | tender/secondary available
Current FMV per share (409A or market):
Estimated future FMV scenarios (low/base/high):

AWARDS (repeat per grant):
  Type: ISO | NSO | RSU | ESPP (qualified §423) | RSA
  Grant date / Strike (exercise) price:
  Shares granted / vested / unvested:
  Vesting schedule (cliff + monthly/annual):
  For ISO/NSO: strike price; FMV at grant
  For RSU: vest dates; FMV expected at vest
  For ESPP: offering/purchase dates; discount %; lookback? (yes/no)
  83(b) election filed or available? (only relevant for RSAs / early-exercised options)
HOLDING CONSTRAINTS:
  Blackout windows / 10b5-1 plan / lockup:
  Liquidity to pay exercise cost + tax: [amount available]
</equity_comp_context>
```

## Constraints

### Must
- Map each award type to its **taxable events** (DT-02):
  - **NSO:** ordinary income at exercise = (FMV − strike) × shares (the "spread"); capital gain/loss on later sale from FMV-at-exercise basis.
  - **ISO:** no regular-tax income at exercise, BUT the **bargain element** (FMV − strike) is an **AMT preference item** at exercise. Sale character depends on the qualifying-disposition test.
  - **RSU:** ordinary income at vest = FMV × shares vested (no election available); capital gain/loss from vest-date basis on later sale.
  - **ESPP (§423 qualified):** discount taxation depends on qualifying vs disqualifying disposition and the lookback; ordinary-income portion + capital gain.
  - **RSA / early-exercised options:** 83(b) election within **30 days** shifts ordinary income to grant (low-FMV) date; failure to file means income at vest.
- Apply the **ISO qualifying-disposition test:** hold **> 2 years from grant AND > 1 year from exercise** → entire gain is long-term capital gain (regular tax). A **disqualifying disposition** converts part to ordinary income.
- Compute AMT impact for ISO exercises: show regular taxable income vs AMTI (adding the bargain element), apply AMT exemption/phaseout `[input current-year figures; verify]`, and flag the tentative-minimum-tax vs regular-tax comparison. Note the AMT credit (Form 8801) may recover AMT in later years.
- Run NE-10 scenarios across FMV-at-sale (low/base/high) and timing (exercise-and-hold vs exercise-and-sell vs wait).
- Show formula → inputs → result for every computation.
- Flag NIIT on net investment income above the threshold and concentration risk in employer stock.

### Must Not
- Assert specific current-year AMT exemption, phaseout, NIIT, or bracket figures from memory — require user input or mark `[input current-year figure; verify]`.
- Recommend a specific action ("exercise now," "sell at vest") — present scenarios; the decision routes to the user and their professional.
- Treat the AMT from an ISO exercise as a permanent cost without noting the AMT credit carryforward.
- Ignore that a disqualifying ISO disposition creates ordinary income (W-2 inclusion) in the disposition year.
- Present an exercise plan that ignores the cash needed for both the strike and the tax.

## Instructions

**Step 1 — Classify awards and enumerate taxable events.**
Build a grid: Award → Grant event → Vest event → Exercise event → Sale event, marking which events are taxable and the character.

**Step 2 — NSO / RSU ordinary-income computation.**
```
NSO spread at exercise = (FMV_exercise − Strike) × Shares   → ordinary income (W-2), subject to withholding
RSU income at vest     = FMV_vest × Shares                  → ordinary income (W-2)
Basis going forward    = FMV at the ordinary-income event
Later sale gain/(loss) = (Sale price − Basis) × Shares; LT if held > 1 yr from that event
```

**Step 3 — ISO regular vs AMT path.**
```
Regular tax at exercise: $0 income.
AMT at exercise: Bargain element = (FMV_exercise − Strike) × Shares  → AMT preference (added to AMTI)
AMTI = Regular taxable income + bargain element + other preferences
Tentative Minimum Tax = (AMTI − AMT exemption[phased]) × AMT rate [input; verify]
AMT due = max(0, TMT − Regular tax)
AMT credit generated = AMT paid attributable to deferral items → carries forward (Form 8801)
```

**Step 4 — ISO disposition character.**
```
Qualifying IF: Sale date > 2 yrs from grant AND > 1 yr from exercise.
  Qualifying: entire gain = LT capital gain (regular tax); AMT basis differs from regular basis.
Disqualifying (sold earlier):
  Ordinary income = min(FMV_exercise − Strike, Sale price − Strike) × Shares  (added to W-2)
  Remainder = capital gain/(loss), ST or LT by actual holding period
```

**Step 5 — ESPP (§423) disposition.**
```
Qualifying IF: > 2 yrs from offering/grant date AND > 1 yr from purchase date.
  Ordinary income = min(actual gain, discount measured at grant) ; rest = LT cap gain.
Disqualifying:
  Ordinary income = (FMV_purchase − Purchase price) × Shares ; rest = cap gain ST/LT.
Lookback (if any) measures the discount off the lower of offering-date or purchase-date FMV.
```

**Step 6 — Scenario comparison (NE-10).**

| Scenario | Event | Ordinary income | AMT due | Cap-gain character | NIIT | State | Net after-tax proceeds |
|---|---|---|---|---|---|---|---|
| Exercise-and-hold (ISO) | exercise yr | 0 | [AMT] | LT if qualifying | | | |
| Exercise-and-sell (ISO, disqualifying) | same yr | [spread] | 0 | ST | | | |
| RSU vest + hold | vest | [FMV×sh] | — | LT later | | | |
| NSO exercise + sell | exercise | [spread] | — | — | | | |

**Step 7 — Adversarial stress-test (QA-02).**
- If the private stock later goes to zero, was AMT paid on phantom (illiquid) ISO gains a real cash loss? (AMT-trap risk.)
- Does the exercise push AMTI through the exemption phaseout, raising the effective AMT rate?
- Does a large RSU vest stack with salary to cross the NIIT threshold and a higher bracket?
- Is the user concentration-risk exposed (large % of net worth in one employer's stock)?
- Cash check: can the user fund strike + AMT + withholding without forced selling?
- Recency/anchoring: is the plan built on a peak FMV that may not hold?

## Output Format

```
## Equity Compensation Tax Analysis
Jurisdiction: Federal [status] + State [name] | As of: [date] | Current-year figures: user-supplied/verify

### Award Map & Taxable Events
[Step 1 grid]

### Ordinary-Income Events (NSO/RSU)
[Step 2 calcs]

### ISO Regular vs AMT
[Step 3 computation; AMT due; AMT credit generated]

### Disposition Character (ISO / ESPP)
[Steps 4–5 qualifying vs disqualifying]

### Scenario Comparison
[Step 6 table across timing × FMV scenarios]

### Stress-Test Findings
[Step 7 — AMT-trap, phaseout, NIIT, concentration, cash]

### Items to confirm with your tax professional
[AMT computation; current-year figures; state conformity; 83(b) deadline if applicable]
```

## Verification

- [ ] Each award classified (ISO/NSO/RSU/ESPP/RSA) with its taxable events enumerated.
- [ ] NSO and RSU ordinary income computed with formula and basis-going-forward.
- [ ] ISO bargain element treated as an AMT preference, not regular income at exercise.
- [ ] ISO qualifying test (>2yr grant AND >1yr exercise) applied; disqualifying ordinary-income formula shown.
- [ ] ESPP qualifying/disqualifying and lookback handled.
- [ ] AMT exemption/phaseout/rate marked user-supplied/verify; AMT credit carryforward noted.
- [ ] At least three timing/FMV scenarios compared.
- [ ] NIIT, concentration, and cash-to-pay flags addressed.
- [ ] 83(b) 30-day window noted where RSAs/early-exercise apply.
- [ ] No current-year figure asserted from memory.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Calling ISO exercise "tax-free" | It is tax-free for REGULAR tax only; the bargain element is an AMT preference — always run the AMT path |
| Ignoring the ISO AMT trap on illiquid stock | Stress-test asks: if FMV falls, AMT was paid on phantom gain — flag the cash risk explicitly |
| Treating disqualifying ISO disposition as all capital gain | Disqualifying disposition creates W-2 ordinary income; show the min() formula |
| Assuming 83(b) can be filed late | The election is due within 30 days of grant/early-exercise; flag the hard deadline, route to professional |
| Presenting AMT as permanent | Note the AMT credit (Form 8801) may recover AMT in later regular-tax years |
| Asserting AMT exemption/NIIT/bracket figures | All marked `[input current-year figure; verify with IRS/official source]` |
| Recommending "exercise now" | Output is scenario comparison; the decision and filing route to the user's tax professional |
