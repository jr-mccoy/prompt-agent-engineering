---
title: "Accretion / Dilution Analysis — Financing Mix, Pro-Forma EPS, and Breakeven Synergies"
category: finance/mergers-acquisitions
description: "Build an auditable accretion/dilution analysis: pro-forma EPS across cash/stock/debt financing mixes, exchange-ratio and ownership math, the breakeven synergy required to neutralize dilution, and a sensitivity grid that exposes the deal's true EPS impact."
techniques:
  - NE-11
  - NE-10
  - QA-01
  - QA-02
  - DS-02
difficulty: advanced
tags:
  - accretion-dilution
  - pro-forma-eps
  - exchange-ratio
  - breakeven-synergy
  - m-and-a
  - deal-financing
updated: "2026-06-08"
related_prompts:
  - domain-finance/mergers-acquisitions/finance_ma_deal_model_builder.md
  - domain-finance/mergers-acquisitions/finance_synergy_estimation_framework.md
  - domain-finance/mergers-acquisitions/finance_deal_financing_structure_analysis.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. All outputs must be reviewed by qualified finance professionals before use in any transaction or decision.**

## Objective

Construct an auditable accretion/dilution analysis that quantifies the impact of an acquisition on the acquirer's earnings per share (EPS) under cash, stock, and mixed financing, with all formulas shown. Solve for the breakeven synergy that neutralizes dilution, present a sensitivity grid across purchase price and financing mix, and stress-test the result against the consensus pitfall that "accretive = value-creating."

## When to Use

- Screening whether a proposed acquisition is accretive or dilutive to the acquirer's EPS in Year 1 and beyond
- Comparing all-cash, all-stock, and mixed financing on EPS impact before negotiating consideration
- Determining the minimum synergy required to make a dilutive stock deal neutral
- Preparing board or investment-committee materials that must show EPS impact transparently
- Pressure-testing a target's asking price against the EPS the acquirer can defend

## Inputs / Context Required

**Acquirer (standalone)**
- Net income (LTM or NTM); state which
- Diluted shares outstanding
- Share price (and date)
- Marginal tax rate; accounting framework (US GAAP / IFRS)
- Pre-tax cost of incremental debt (rate + base rate, dated)
- After-tax yield on cash being used (foregone interest)

**Target (standalone)**
- Net income (LTM or NTM, matched to acquirer basis)
- Offer price per share or total equity purchase price
- Existing net debt assumed/refinanced
- Diluted shares outstanding (for exchange-ratio context)

**Deal terms**
- Consideration mix: % cash / % stock / % new debt
- Control premium offered (% over unaffected price)
- Expected pre-tax run-rate synergies (and phase-in, if modeled)
- New intangible amortization from purchase accounting (if estimable; non-cash, tax treatment stated)
- Transaction and financing fees

## Constraints

### Must
- Show pro-forma EPS as: `Pro-Forma EPS = Pro-Forma Net Income ÷ Pro-Forma Diluted Shares`, with each component built up from inputs.
- Build the financing-cost bridge explicitly: forgone interest on cash (after-tax), new debt interest (after-tax), and new shares issued from stock consideration.
- Compute the exchange ratio and resulting ownership split when stock is used.
- Solve for breakeven pre-tax synergies that make accretion/dilution exactly zero.
- Present base/upside/downside cases with internally consistent net-income, synergy, and rate assumptions (NE-10).
- State whether figures are LTM or NTM and keep acquirer and target on the same basis.
- Flag intangible amortization and its tax treatment; show EPS both including and excluding non-cash purchase-accounting amortization if material.

### Must Not
- Conclude "accretive therefore value-creating" — accretion is an EPS-mechanics outcome, not a value test.
- Mix LTM target earnings with NTM acquirer earnings without flagging the mismatch.
- Omit forgone interest on cash consideration (using cash is not free).
- Present a single financing mix without showing the EPS sensitivity to the cash/stock/debt split.
- Ignore the control premium when assessing whether projected synergies can justify the price paid.

## Instructions

**Step 1 — Establish standalone baselines**

```
Acquirer standalone EPS = Acquirer Net Income ÷ Acquirer Diluted Shares
Target equity purchase price = Offer Price/Share × Target Diluted Shares
  (or stated total equity value)
Control premium % = (Offer Price − Unaffected Price) ÷ Unaffected Price
```

**Step 2 — Determine consideration and new shares issued**

```
Cash consideration  = % cash  × Equity Purchase Price
Debt-funded portion = % debt  × Equity Purchase Price   (new borrowing)
Stock consideration = % stock × Equity Purchase Price

New acquirer shares issued = Stock Consideration ÷ Acquirer Share Price
Exchange Ratio (per target share) = (Offer Price/Share × % stock) ÷ Acquirer Share Price
Pro-forma ownership: target holders = New Shares ÷ (Acquirer Shares + New Shares)
```

**Step 3 — Build the pro-forma net income bridge**

```
+ Acquirer standalone net income
+ Target standalone net income
+ After-tax run-rate synergies        = Pre-tax synergies × (1 − tax rate)
− After-tax new debt interest         = Debt-funded portion × cost of debt × (1 − tax rate)
− After-tax forgone interest on cash  = Cash consideration × cash yield × (1 − tax rate)
− After-tax incremental intangible amortization (if any; state if non-deductible)
= Pro-Forma Net Income
```

**Step 4 — Compute pro-forma EPS and accretion/dilution**

```
Pro-Forma Diluted Shares = Acquirer Diluted Shares + New Shares Issued
Pro-Forma EPS            = Pro-Forma Net Income ÷ Pro-Forma Diluted Shares

Accretion/(Dilution) $   = Pro-Forma EPS − Acquirer Standalone EPS
Accretion/(Dilution) %   = (Pro-Forma EPS ÷ Acquirer Standalone EPS) − 1
```

**Step 5 — Solve for breakeven synergies**

Set Pro-Forma EPS equal to standalone EPS and solve for required pre-tax synergies:

```
Breakeven Pre-Tax Synergies =
  [ (Standalone EPS × Pro-Forma Diluted Shares) − Pro-Forma NI excl. synergies ]
  ÷ (1 − tax rate)

Interpretation: synergies above this make the deal accretive; below, dilutive.
Compare breakeven synergies to management's claimed run-rate synergies.
```

**Step 6 — Sensitivity grid (NE-10)**

Vary financing mix and purchase price; report accretion/(dilution) %:

| Financing mix ↓ / Offer price → | −10% | Base | +10% | +20% |
|---|---|---|---|---|
| 100% cash/debt | | | | |
| 50% stock / 50% cash | | | | |
| 100% stock | | | | |

**Step 7 — Adversarial stress-test (QA-02)**

- Does the deal flip from accretive to dilutive under the downside synergy case?
- What share-price decline in the acquirer makes a stock deal cross to dilutive (more shares issued at lower price)?
- Is accretion driven by cheap debt rather than operating logic? Recompute at +100bps cost of debt.
- Does Year 1 accretion mask Year 1 dilution once full intangible amortization phases in?

## Output Format

### Standalone Baselines
[Step 1 outputs]

### Consideration & Ownership
[Step 2 outputs — cash/debt/stock, new shares, exchange ratio, pro-forma ownership %]

### Pro-Forma Net Income Bridge
| Line item | Amount | Note |
|---|---|---|
| Acquirer net income | | |
| + Target net income | | |
| + After-tax synergies | | |
| − After-tax new debt interest | | |
| − After-tax forgone cash interest | | |
| − After-tax intangible amortization | | |
| = Pro-Forma Net Income | | |

### EPS Impact
| Metric | Standalone | Pro-Forma | Δ ($) | Δ (%) |
|---|---|---|---|---|
| Diluted EPS | | | | |

### Breakeven Synergy
[Step 5 result vs. management claim]

### Sensitivity Grid
[Step 6 table]

### Stress-Test Summary
[Step 7 findings]

## Verification

- [ ] Acquirer and target earnings are on the same basis (both LTM or both NTM); basis stated.
- [ ] Forgone interest on cash consideration is included (after-tax).
- [ ] New debt interest and new shares issued are both reflected in the bridge.
- [ ] Exchange ratio and pro-forma ownership split are shown when stock is used.
- [ ] Breakeven synergy is solved and compared against management's claimed synergies.
- [ ] Sensitivity grid covers ≥3 financing mixes and ≥3 price points.
- [ ] At least one case in the grid shows dilution (if all are accretive, the price range is too narrow — widen it).
- [ ] Intangible amortization treatment (deductible vs. not) is stated.
- [ ] Tax rate applied consistently to synergies, interest, and amortization.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| "Accretive, therefore the deal creates value" | State explicitly that accretion is an EPS-mechanics result; value creation requires synergies > premium paid, tested separately |
| Accretion driven entirely by cheap debt | Recompute at +100bps cost of debt; flag if accretion disappears |
| Using cash as if it were free | Forgone after-tax interest on cash consideration is a mandatory line in the bridge |
| Mismatched earnings basis inflating accretion | Acquirer and target must both be LTM or both NTM; flag any mismatch |
| Year-1 accretion that reverses on full amortization phase-in | Show EPS impact across Year 1–3 and with full intangible amortization loaded |
| Stock-deal accretion that ignores acquirer share-price risk | Stress acquirer share price down; more shares issued at a lower price can flip the deal to dilutive |
