---
title: "Entity Structure Tax Comparison — C-Corp vs. S-Corp vs. LLC vs. Partnership"
category: finance/tax-planning
description: "Compare entity structures (C-corporation, S-corporation, multi-member LLC, partnership, sole proprietorship) on tax outcomes — entity-level tax, pass-through treatment, self-employment tax, QBI, double-taxation, payroll/distribution mix, and basis — across multiple income and distribution scenarios."
techniques:
  - NE-11
  - NE-10
  - QA-02
  - DS-02
  - RT-02
difficulty: advanced
tags:
  - entity-selection
  - c-corp
  - s-corp
  - llc
  - partnership
  - pass-through
  - self-employment-tax
  - qbi
updated: "2026-06-08"
related_prompts:
  - domain-finance/tax-planning/finance_multi_year_tax_projection.md
  - domain-finance/tax-planning/finance_state_nexus_apportionment_mapper.md
  - domain-finance/corporate-finance-fpa/finance_capital_allocation_framework.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not tax, legal, or accounting advice. Tax rules change and depend on individual circumstances; entity formation, election filings (e.g., Form 2553, Form 8832), and reliance decisions must be made with a qualified tax professional (CPA / EA / tax attorney).**

**Verify all figures against current tax law as of the date of use and the applicable federal and state jurisdiction. Brackets, rates, QBI thresholds, SE-tax wage bases, and entity-level tax rates change annually and vary by state.**

## Objective

Produce an auditable, scenario-based comparison of entity structures on after-tax cash to owner(s), showing the formula chain for each tax layer (entity-level, owner-level, self-employment/payroll, QBI deduction, state) so an owner and their tax professional can see *why* one structure produces more after-tax cash under a given set of facts — not a blanket "choose X" recommendation.

## When to Use

- A founder or owner is choosing an initial entity structure or considering a conversion/election.
- Modeling the trade-off between S-corp payroll-vs-distribution splits and C-corp retention.
- Comparing pass-through (LLC/partnership/S-corp) self-employment tax exposure.
- Evaluating whether double taxation of a C-corp is offset by a lower entity rate and retained-earnings reinvestment.
- Preparing an options memo for review by counsel/CPA before an election deadline.

## Inputs / Context Required

```
<entity_comparison_inputs>
Business profile:
- Industry; is it a "specified service trade or business" (SSTB) for QBI? [yes/no/unsure]
- Owner count and ownership %; any non-resident or entity owners (affects S-corp eligibility)
- Expected annual net business income (pre-owner-comp), 3 scenarios: low / base / high
- Reasonable compensation estimate for owner labor (for S-corp/C-corp): $______
- Cash the owner needs to draw vs. cash to retain/reinvest in the business
- State(s) of operation and owner residence (note state entity-level taxes, PTET elections)

Owner tax profile:
- Filing status; other household income (stacks on top of pass-through income)
- Marginal ordinary rate, qualified-dividend/LTCG rate [input current-year figures; verify]
- Applicability of NIIT (3.8%) and Additional Medicare (0.9%) [verify thresholds]

Current-year tax parameters (USER-SUPPLIED — do not assume):
- Federal ordinary brackets: [input; verify with IRS]
- C-corp flat rate: [input current-year rate; verify]
- Qualified dividend / LTCG rate(s): [input; verify]
- SE tax: Social Security wage base ___, SS rate ___, Medicare rate ___ [input; verify]
- QBI deduction %, taxable-income thresholds, phase-in range [input; verify]
- Applicable state rates / PTET parameters [input; verify]
</entity_comparison_inputs>
```

## Constraints

### Must
- Show the formula for every tax layer; never present an after-tax number without its derivation (NE-11).
- Run the low / base / high income scenarios for every entity (NE-10); structures can reverse ranking by income level.
- Separate the three tax layers explicitly: (1) entity-level tax, (2) owner-level tax on distributions/dividends, (3) employment tax (SE tax or FICA on wages).
- Treat owner compensation consistently: S-corp/C-corp pay W-2 wages (FICA), LLC/partnership owners pay SE tax on distributive share of active income.
- Apply the QBI deduction only to eligible pass-through income, respecting SSTB status and taxable-income thresholds/phase-ins as user-supplied figures.
- State a jurisdiction flag and note state-level entity taxes (franchise tax, gross-receipts tax, PTET) materially change results.
- Identify the breakeven income level (if any) where the ranking of two structures flips.

### Must Not
- Assert specific current-year brackets, the C-corp rate, the SS wage base, or QBI thresholds from memory — require user input or mark `[input; verify]`.
- Recommend an election or formation ("you should elect S-corp") — frame as scenario outcomes routed to a professional.
- Ignore self-employment tax on LLC/partnership active income or assume all S-corp income escapes employment tax.
- Treat retained C-corp earnings as tax-free to the owner (a second tax applies on distribution or sale).
- Ignore "reasonable compensation" risk for S-corps (understated wages are an IRS audit target).

## Instructions

**Step 1 — Lay out the four-to-five candidate structures and eligibility gates.**

| Structure | Entity-level tax? | Owner active income tax | Eligibility note |
|---|---|---|---|
| Sole prop / SMLLC (default) | No | SE tax on net SE income | Single owner |
| Partnership / MMLLC (default) | No | SE tax on distributive share (general/active) | ≥2 owners |
| S-corp (election) | No (mostly) | FICA on W-2 wages only; distributions not SE-taxed | ≤100 eligible owners, US individuals, one class of stock |
| C-corp | Yes (entity rate) | Dividends taxed at owner level | No eligibility limits |

Flag any structure the inputs disqualify (e.g., non-resident owner → no S-corp).

**Step 2 — Compute the pass-through (SE-tax) path for sole prop / partnership / LLC.**

```
Net SE income          = Net business income allocable to active owner
SE tax base            = Net SE income × 92.35%
SE tax                 = (SS portion: min(base, SS wage base) × SS rate)
                         + (Medicare portion: base × Medicare rate)
                         + (Additional Medicare 0.9% on wages+SE over threshold) [verify]
1/2 SE tax deduction   = SE tax × 50%   (above-the-line)
QBI-eligible income    = Net business income − 1/2 SE tax deduction (subject to SSTB/threshold limits)
QBI deduction          = min(QBI% × QBI income, QBI% × (taxable income − net cap gain)) [verify]
Taxable ordinary income= Other income + (net business income − 1/2 SE tax − QBI deduction)
Federal income tax     = apply brackets [input; verify]
NIIT                   = generally N/A on active SE income (verify passive vs. active)
After-tax cash to owner= Net business income − SE tax − Federal income tax − State tax
```

**Step 3 — Compute the S-corp path (wage + distribution split).**

```
Reasonable W-2 wages   = [user estimate of owner labor value]
FICA on wages          = wages × (SS+Medicare employer+employee portions) [verify]
                         (note: employer half is a business deduction)
Pass-through income    = Net business income − wages − employer payroll taxes
QBI-eligible income    = pass-through income (S-corp QBI excludes W-2 wages) [verify SSTB/thresholds]
QBI deduction          = min(QBI% × QBI income, taxable-income limit) [verify]
Owner taxable income   = other income + wages + (pass-through − QBI deduction)
Federal income tax     = apply brackets
Employment-tax savings = SE-tax-path employment tax − FICA on wages only
After-tax cash to owner= Net business income − total FICA − Federal income tax − State tax
```
Stress the *reasonable compensation* constraint: artificially low wages inflate savings but raise audit risk — show savings at the user's stated wage AND at a higher "defensible wage" sensitivity.

**Step 4 — Compute the C-corp path (entity tax + dividend on distribution).**

```
Owner W-2 wages        = [user estimate]  (deductible to corp; FICA applies)
Corporate taxable income = Net business income − wages − employer payroll tax
Corporate tax          = corporate taxable income × C-corp rate [input; verify]
Retained earnings      = after-tax corporate income retained (no second tax until distributed/sold)
If distributed as dividend:
  Dividend tax         = dividend × qualified-dividend rate [input; verify] + NIIT if applicable
  Total tax on distributed $ = corporate tax + dividend tax  (double taxation)
After-tax cash if fully distributed = wages-after-tax + dividend-after-tax
After-tax cash if fully retained    = wages-after-tax only (defer 2nd layer; note future tax)
```

**Step 5 — Build the comparison matrix across the three income scenarios.** For each scenario × structure, report: total tax (all layers), effective tax rate, after-tax cash to owner if cash is fully drawn, and after-tax owner value if cash is retained/reinvested.

**Step 6 — Find the breakeven and run the adversarial stress-test (QA-02).**
- At what net income does S-corp employment-tax savings exceed its added payroll/admin cost?
- At what reinvestment horizon does C-corp deferral beat pass-through, after the eventual second tax?
- What happens if the QBI deduction phases out (income above threshold or SSTB)? Re-rank.
- What if the owner's state has no PTET / a high franchise or gross-receipts tax? Re-rank.
- What if "reasonable compensation" must rise (IRS challenge)? Recompute S-corp savings.

## Output Format

### Candidate Structures & Eligibility
[Step 1 table with disqualifications flagged]

### Tax-Layer Derivations
[Steps 2–4 formula chains for base scenario, fully shown]

### Comparison Matrix

| Scenario | Structure | Entity tax | Employment tax | Owner income tax | Total tax | Effective rate | After-tax cash (drawn) | After-tax value (retained) |
|---|---|---|---|---|---|---|---|---|
| Low | Sole prop / LLC | | | | | | | |
| Low | S-corp | | | | | | | |
| Low | C-corp | | | | | | | |
| Base | … | | | | | | | |
| High | … | | | | | | | |

### Breakeven & Stress-Test
[Step 6 findings — breakeven income, QBI phase-out re-rank, reasonable-comp sensitivity, state-tax sensitivity]

### Key Drivers (3–5 bullets)
[Plain-language explanation of what actually moves the ranking for these facts]

## Verification

- [ ] Every after-tax figure traces to a shown formula with stated inputs.
- [ ] All current-year parameters are user-supplied or marked `[input; verify]` — none asserted from memory.
- [ ] SE tax modeled for LLC/partnership active income; FICA modeled for S-corp/C-corp wages.
- [ ] QBI deduction respects SSTB status and taxable-income thresholds.
- [ ] C-corp shows BOTH retained and fully-distributed (double-tax) cases.
- [ ] All three income scenarios run for every structure.
- [ ] Breakeven income identified; ranking flip noted if it exists.
- [ ] Reasonable-compensation sensitivity shown for S-corp.
- [ ] State entity taxes / PTET flagged with jurisdiction.
- [ ] Disclaimer present; election/filing routed to professional.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| "S-corp always saves on taxes" | Savings depend on income level and reasonable comp; show breakeven and the defensible-wage sensitivity, and note added payroll/admin cost |
| Treating retained C-corp earnings as escaping tax | Always model the second (dividend/sale) layer; retained ≠ tax-free, only deferred |
| Ignoring SE tax on LLC/partnership active income | SE tax applies to active distributive share; model it explicitly |
| Anchoring on headline entity rate | Compare full stack (entity + employment + owner) effective rates, not the entity rate alone |
| Assuming QBI applies fully | QBI is limited by SSTB status, W-2/UBIA limits, and taxable-income thresholds — apply the limits and show the phase-out re-rank |
| Ignoring state tax | State entity taxes, franchise/gross-receipts taxes, and PTET can reverse the federal ranking; require jurisdiction input |
| Presenting a single recommendation | Output is a scenario comparison routed to a CPA/attorney for the actual election decision |
