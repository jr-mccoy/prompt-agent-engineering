---
title: "Five Cs of Credit Analysis — Capacity, Capital, Conditions, Character, Collateral"
category: finance/credit-lending
description: "Structured 5-Cs creditworthiness assessment that scores each dimension from user-supplied evidence, derives DSCR/leverage support, and produces an internal risk rating on a stated scale — with skeptical default stance and no invented data."
techniques:
  - RT-02
  - DS-02
  - NE-10
  - AG-02
  - NE-11
difficulty: intermediate
tags:
  - credit-analysis
  - five-cs
  - underwriting
  - risk-rating
  - dscr
  - leverage
updated: "2026-06-08"
related_prompts:
  - domain-finance/credit-lending/finance_credit_memo_builder.md
  - domain-finance/credit-lending/finance_debt_capacity_sizing.md
  - domain-finance/financial-statement-analysis/finance_ratio_analysis_engine.md
  - domain-finance/field_guide.md
---

*For informational purposes only. Not financial, credit, or lending advice. All outputs must be reviewed by qualified credit professionals before any lending decision.*

## Objective

Assess a borrower's creditworthiness across the five classic dimensions — Capacity, Capital, Conditions, Character, and Collateral — scoring each from user-supplied evidence, surfacing the supporting cash-flow and leverage arithmetic, and synthesizing an internal risk rating on a stated scale. The analysis defaults to a skeptical stance: claims of strength must be evidenced, and unsupported inputs are flagged rather than credited.

## When to Use

- Pre-screening a new borrower or facility request before drafting a full credit memo
- Annual review of an existing relationship to re-rate risk
- Training or calibration exercises on consistent credit assessment
- Sanity-checking a counterparty's or relationship manager's favorable narrative
- Building the qualitative + quantitative scaffold that feeds a credit memo (`finance_credit_memo_builder.md`)

## Inputs / Context Required

Provide as much as available; the model flags missing items and will not invent them.

**Borrower & facility context**
- Borrower name, entity type, industry / NAICS code, jurisdiction and reporting currency
- Facility requested: amount, purpose, tenor, proposed structure (term / revolver / amortizing)
- Accounting framework (US GAAP / IFRS) and fiscal year end

**Capacity (cash flow / repayment ability)**
- Historical EBITDA / operating cash flow (>=3 years preferred), debt service schedule
- Existing debt balances, interest rates, maturities, lease obligations
- Revenue concentration, contracted vs. discretionary cash flows

**Capital (skin in the game / balance-sheet strength)**
- Equity / net worth, retained earnings, sponsor or owner contribution
- Tangible net worth, intangibles, related-party balances

**Conditions (macro / industry / use of proceeds)**
- Industry outlook, cyclicality, regulatory exposure, supplier/customer dependency
- Use of proceeds and sensitivity to rate / demand shocks

**Character (willingness / track record)**
- Payment history, prior defaults, management tenure and reputation, audit quality
- Litigation, covenant breaches, related-party governance concerns

**Collateral (secondary repayment / LGD support)**
- Asset type, appraised / book value, lien position, advance rate, liquidation discount

**Rating context**
- Internal rating scale to use (e.g., 1-10 internal grades, or Pass/Special Mention/Substandard). If none supplied, the model uses a generic 1-5 scale and labels it `[ASSUMED SCALE]`.

## Constraints

### Must
- Default to a skeptical stance (AG-02): treat each strength claim as a hypothesis requiring supporting evidence; weight unevidenced claims at zero.
- Score each C on the stated scale with an explicit evidence citation for the score.
- Show repayment-capacity arithmetic (DSCR, leverage) with formula -> inputs -> result.
- Flag every input that is assumed or missing with `[ASSUMED]` / `[MISSING]`.
- State the rating scale used and never map to an external agency rating.
- Name the bias pitfalls relevant to credit (anchoring on a sponsor narrative, optimism on projections, recency on a recent good quarter) and run a disconfirming check.

### Must Not
- Invent financial figures, payment histories, collateral values, or industry data.
- Map the internal score to a named agency rating (e.g., "equivalent to BBB").
- Treat collateral as a substitute for capacity — collateral mitigates loss given default, not probability of repayment from cash flow.
- Credit a "strong management" or "good relationship" claim without documented evidence.
- Present a single favorable C as sufficient for approval.

## Instructions

1. **Parse inputs and build an evidence register.** For each of the five Cs, list the data points provided and annotate the source. Flag missing or assumed items explicitly.

2. **Compute the Capacity arithmetic.** Capacity is the primary C; quantify repayment ability:
```
DSCR = (EBITDA - Cash Taxes - Maintenance Capex) / (Interest + Scheduled Principal)
   (state which numerator definition is used; CFADS variants must be labeled)

FCCR = (EBITDA - Unfinanced Capex - Cash Taxes) / (Interest + Principal + Rents)

Leverage = Total Debt / EBITDA
Pro-forma Leverage = (Existing Debt + New Facility) / EBITDA

Interest Coverage = EBIT / Interest Expense
```
Show each formula, substitute the supplied values, and report the result to two decimals.

3. **Score each C on the stated scale.** For each dimension assign a score (e.g., 1 = strong ... 5 = weak on a 1-5 scale; mirror the user's scale direction) and a one-line evidence-based justification. Capacity score must reference the DSCR/leverage outputs.

4. **Apply the skeptical disconfirming check.** For each C scored as "strong," ask: what evidence would contradict this, and is it present or absent? For Capacity, stress EBITDA -15% / -30% and recompute DSCR.

5. **Weight and synthesize.** Combine the five scores into an overall internal rating. State the weighting used (default: Capacity highest weight; if user supplies weights, use them). Capacity weakness cannot be fully offset by Collateral strength — note this asymmetry.

6. **Identify the binding constraint.** Name the single dimension that most limits the credit and the specific evidence that would be required to upgrade it.

7. **Run base / downside / severe stress on Capacity.** Recompute DSCR and leverage under three internally consistent macro/operating scenarios.

## Output Format

### Evidence Register
| Dimension | Data Provided | Source | Missing / Assumed |
|---|---|---|---|
| Capacity | ... | ... | [MISSING/ASSUMED flags] |
| Capital | ... | ... | ... |
| Conditions | ... | ... | ... |
| Character | ... | ... | ... |
| Collateral | ... | ... | ... |

### Capacity Arithmetic
```
DSCR        = [numerator] / [denominator] = X.XXx
FCCR        = ... = X.XXx
Leverage    = Total Debt / EBITDA = X.Xx
Pro-forma Leverage = (Existing + New) / EBITDA = X.Xx
Interest Coverage = EBIT / Interest = X.Xx
```

### Five-Cs Scorecard (scale: [state scale])
| C | Score | Evidence-Based Justification | Disconfirming Check Result |
|---|---|---|---|
| Capacity | [x] | references DSCR/leverage | ... |
| Capital | [x] | ... | ... |
| Conditions | [x] | ... | ... |
| Character | [x] | ... | ... |
| Collateral | [x] | advance rate / lien | ... |
| **Overall internal rating** | **[x]** | weighting: [state] | binding constraint: [name] |

### Capacity Stress (base / downside / severe)
| Metric | Base | Downside (EBITDA -15%) | Severe (EBITDA -30%) |
|---|---|---|---|
| EBITDA | | | |
| DSCR | X.XXx | X.XXx | X.XXx |
| Leverage | X.Xx | X.Xx | X.Xx |
| Interest Coverage | X.Xx | X.Xx | X.Xx |

### Binding Constraint & Upgrade Path
- **Binding constraint:** [dimension] — [evidence].
- **To upgrade:** [specific evidence or structural change required].

## Verification

- [ ] Each C is scored on the explicitly stated scale; no external agency rating is referenced.
- [ ] Capacity arithmetic shows formula -> inputs -> result for DSCR, FCCR, and leverage.
- [ ] Every missing or assumed input is flagged `[MISSING]` / `[ASSUMED]`.
- [ ] No financial figure, payment history, or collateral value was invented.
- [ ] Disconfirming check is documented for each "strong" score.
- [ ] Capacity downside and severe scenarios are recomputed and internally consistent.
- [ ] Collateral strength is not used to offset a Capacity weakness in the synthesis.
- [ ] The binding constraint and its upgrade path are named.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Approving on collateral strength while cash flow is weak | Collateral scored separately; synthesis states it mitigates LGD, not repayment capacity |
| Crediting "strong management / good relationship" without evidence | Unevidenced character claims weighted zero and flagged |
| Anchoring on a sponsor's optimistic projection | Capacity stressed -15%/-30%; base case must survive downside |
| Treating one strong C as approval | Overall rating requires all five; binding constraint surfaced explicitly |
| Mapping internal score to an agency grade | Output uses only the stated internal scale; agency mapping prohibited |
| Single good recent quarter driving the score | Full-cycle / multi-year capacity required; recency bias named |
| Inventing an industry outlook for Conditions | Conditions scored only from supplied data; absence flagged, not filled |
