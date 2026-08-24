---
title: "Basel III Capital-Adequacy & RWA Analysis — Methodology Framing"
category: finance/regulatory-compliance
description: "Frame a Basel III capital-adequacy analysis: compute CET1 / Tier 1 / Total capital ratios and leverage ratio, build risk-weighted assets (RWA) across credit, market, and operational risk, and assess buffers and headroom — with auditable formulas, no-fabrication of regulatory minimums, and verify-against-current-source guardrails."
techniques:
  - NE-11
  - DT-02
  - NE-10
  - QA-01
  - CM-02
difficulty: advanced
tags:
  - basel
  - capital-adequacy
  - rwa
  - cet1
  - tier1
  - leverage-ratio
  - prudential
updated: "2026-06-08"
related_prompts:
  - domain-finance/regulatory-compliance/finance_regulatory_requirement_mapper.md
  - domain-finance/risk-management/finance_liquidity_risk_analysis.md
  - domain-finance/risk-management/finance_enterprise_risk_register.md
  - domain-finance/field_guide.md
---

**Informational analysis only — not legal, prudential, or regulatory advice. Basel III/IV standards and their local implementation (specific risk weights, minimum ratios, buffer calibrations, output floors, and effective dates) change and vary by jurisdiction and bank category; confirm all minimums, risk weights, and methodology against current official sources (Basel/BIS standards and the local prudential regulator's rules) and qualified counsel before relying on any output.**

## Objective

Construct an auditable Basel III capital-adequacy analysis: build risk-weighted assets (RWA) across credit, market, and operational risk; compute the regulatory capital ratios (CET1, Tier 1, Total capital) and the leverage ratio; and assess capital against minimums and buffers to determine headroom — with every formula shown and every regulatory minimum/risk-weight/buffer marked for verification against the current local rulebook. This is a methodology-framing and computation tool, not a determination of regulatory capital compliance.

## When to Use

- Internal capital-adequacy assessment (ICAAP-style) and capital planning
- Stress-testing capital ratios under adverse scenarios
- Evaluating the capital impact of a portfolio, acquisition, or business-mix change
- Training/educational framing of the Basel capital stack and RWA build
- Pre-supervisory-review readiness for capital metrics

## Inputs / Context Required

```
<basel_capital_context>
INSTITUTION:
- Bank/entity and jurisdiction; local prudential regulator
- Bank category/approach (standardized vs. internal models; G-SIB/D-SIB status if applicable)
- Reporting date

CAPITAL COMPONENTS (book values, with regulatory adjustments noted):
- Common Equity Tier 1 elements (common shares, retained earnings, AOCI treatment, less regulatory deductions: goodwill/intangibles, DTAs, etc.)
- Additional Tier 1 instruments
- Tier 2 instruments

EXPOSURES FOR RWA:
- Credit risk: on-/off-balance-sheet exposures by asset class, counterparty, rating, collateral/CRM, off-balance-sheet CCFs
- Market risk: trading-book positions by risk factor
- Operational risk: relevant indicator/loss inputs per the applicable approach
- Leverage exposure measure components (on-balance, derivatives, SFTs, off-balance-sheet)

REGULATORY PARAMETERS (user to supply / verify — DO NOT assume):
- Minimum CET1 / Tier 1 / Total ratios [verify against local rule]
- Capital conservation buffer, countercyclical buffer, G-SIB/D-SIB surcharge [verify]
- Leverage ratio minimum [verify]
- Applicable risk weights and any output floor [verify]
</basel_capital_context>
```

## Constraints

### Must
- State the **jurisdiction, prudential regulator, and approach** (standardized vs. internal models).
- Mark **every regulatory minimum, buffer, risk weight, credit-conversion factor, and output floor** as **"[verify against current local Basel implementation]"** — never assert numeric minimums or risk weights as authoritative from memory.
- Show **all formulas** for RWA build and ratio computation (NE-11); every figure must be traceable to inputs.
- Build RWA across **credit, market, and operational risk** separately, then aggregate.
- Apply **regulatory deductions** to capital components and show the bridge from book to regulatory capital.
- Compute **CET1, Tier 1, Total capital ratios** and the **leverage ratio**, and compare each against its (verified) minimum + buffer to derive headroom.
- Run a **buffer/MDA assessment**: state where the entity sits relative to combined buffer requirements (mark MDA mechanics for verification).
- Include **base + adverse scenarios** (NE-10) for capital ratios.
- Verification pass (QA-01): recompute at least one ratio and the credit-RWA subtotal from raw inputs.

### Must Not
- Assert specific Basel minimum ratios, buffer percentages, risk weights, or output-floor levels as authoritative.
- Treat book equity as regulatory capital without deductions and adjustments.
- Present a single point estimate without a stress scenario.
- Conclude the bank "meets/breaches" requirements without the verify-against-current caveat and counsel routing.

## Instructions

**Step 1 — Build regulatory capital from book values (NE-11).**

```
CET1 Capital = Common shares + Retained earnings + Eligible AOCI
              − Regulatory deductions (goodwill, other intangibles, certain DTAs,
                holdings of own/other financial-institution capital, etc.) [verify deduction rules]
Tier 1 Capital = CET1 + Eligible Additional Tier 1 instruments
Total Capital  = Tier 1 + Eligible Tier 2 instruments
```
Show the book-to-regulatory bridge as a table.

**Step 2 — Build credit-risk RWA (DT-02, standardized framing).**

```
For each exposure:
  EAD = On-balance amount + (Off-balance notional × Credit Conversion Factor [verify CCF])
  Risk-weighted amount = EAD_after_CRM × Risk Weight [verify RW by asset class/rating]
Credit RWA = Σ risk-weighted amounts
```
Note credit-risk-mitigation (collateral, guarantees) treatment and mark all risk weights/CCFs "[verify]". If internal models are used, frame PD/LGD/EAD inputs and note model-approval dependency.

**Step 3 — Add market-risk and operational-risk RWA.**
```
Market-risk RWA = (Market-risk capital charge per applicable approach) × 12.5  [verify scalar/approach]
Operational-risk RWA = (Op-risk capital charge per applicable approach) × 12.5 [verify approach inputs]
```
Mark the approach and any indicator/loss-component inputs for verification.

**Step 4 — Aggregate RWA and apply any output floor.**
```
Total RWA = Credit RWA + Market RWA + Operational RWA
If output floor applies: Total RWA = max(Total RWA_internal-models, Floor% × Standardized RWA) [verify floor]
```

**Step 5 — Compute ratios (NE-11).**
```
CET1 Ratio   = CET1 Capital  / Total RWA
Tier 1 Ratio = Tier 1 Capital / Total RWA
Total Ratio  = Total Capital  / Total RWA
Leverage Ratio = Tier 1 Capital / Leverage Exposure Measure   [verify exposure-measure components]
```

**Step 6 — Buffers, headroom, and MDA assessment.**
For each ratio, compare to (verified) minimum + combined buffer requirement (capital conservation + countercyclical + any systemic surcharge):
```
Headroom = Actual Ratio − (Minimum + Combined Buffer)   [all RHS terms verify]
```
State whether the entity is within buffer (potential distribution/MDA constraints — mark MDA mechanics "[verify]") and flag the binding constraint (which ratio is tightest).

**Step 7 — Scenario analysis (NE-10).**
Run base and adverse scenarios (e.g., credit migration increasing RWA, losses reducing CET1, market shock). Show each ratio under each scenario and the year/scenario where headroom is minimized or a buffer is breached.

**Step 8 — Verification (QA-01).**
Recompute the CET1 ratio and the credit-RWA subtotal independently from inputs; confirm the book-to-regulatory capital bridge ties.

## Output Format

### Regulatory Capital Bridge
| Component | Book value | Regulatory adjustments | Regulatory amount |
|---|---|---|---|
| CET1 | | | |
| Additional Tier 1 | | | |
| Tier 2 | | | |
| **Total Capital** | | | |

### RWA Build
| RWA component | Approach | Inputs (verify weights) | RWA |
|---|---|---|---|
| Credit risk | | [verify RW/CCF] | |
| Market risk | | [verify] | |
| Operational risk | | [verify] | |
| Output floor adjustment | | [verify floor] | |
| **Total RWA** | | | |

### Capital Ratios & Headroom
| Ratio | Actual | Minimum (verify) | Combined buffer (verify) | Required total | Headroom | Binding? |
|---|---|---|---|---|---|---|
| CET1 | | | | | | |
| Tier 1 | | | | | | |
| Total capital | | | | | | |
| Leverage | | | n/a | | | |

### Scenario Analysis
| Scenario | CET1 | Tier 1 | Total | Leverage | Min headroom point |
|---|---|---|---|---|---|
| Base | | | | | |
| Adverse | | | | | |

### Verify-Against-Current Instruction
> Confirm all minimum ratios, buffer/surcharge calibrations, risk weights, CCFs, output floor, leverage-exposure definitions, and MDA mechanics against the current Basel standard and local prudential implementation **as of [date]**. Capital-adequacy determinations route to qualified regulatory/prudential counsel.

## Verification

- [ ] Jurisdiction, regulator, and approach (standardized/internal models) stated.
- [ ] Every minimum, buffer, risk weight, CCF, and output floor marked "[verify against current local implementation]".
- [ ] Book-to-regulatory capital bridge shown with deductions.
- [ ] RWA built separately for credit, market, and operational risk, then aggregated.
- [ ] CET1/Tier 1/Total ratios and leverage ratio computed with formulas shown.
- [ ] Headroom computed vs. minimum + combined buffer; binding constraint identified.
- [ ] Base and adverse scenarios run; minimum-headroom point flagged.
- [ ] One ratio and the credit-RWA subtotal independently recomputed (QA-01).

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Asserting Basel minimum ratios or risk weights from memory | All minimums/weights/buffers/floors marked "[verify against current local implementation]" |
| Using book equity as regulatory capital | Regulatory deductions and book-to-regulatory bridge required |
| Single-point capital ratio without stress | Base + adverse scenarios mandatory; minimum-headroom point flagged |
| Precision illusion from a detailed RWA build | Verification pass recomputes a ratio and credit-RWA subtotal; inputs marked for verification |
| Concluding "meets/breaches requirements" definitively | Verify-against-current caveat + counsel routing required; output is methodology framing |
| Ignoring the binding constraint / MDA implications | Headroom table identifies the tightest ratio; buffer/MDA position flagged for verification |
