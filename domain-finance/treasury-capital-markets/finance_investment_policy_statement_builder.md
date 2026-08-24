---
title: "Investment Policy Statement Builder — Objectives, Constraints, Eligible Instruments, and Limits"
category: finance/treasury-capital-markets
description: "Build a corporate or institutional investment policy statement covering objectives (safety/liquidity/yield), eligible instruments, credit/maturity/concentration limits, benchmarks, and governance."
techniques:
  - NE-11
  - DS-02
  - QA-01
  - RT-03
  - DS-06
difficulty: intermediate
tags:
  - investment-policy
  - ips
  - cash-investment
  - liquidity-management
  - governance
updated: "2026-06-08"
related_prompts:
  - domain-finance/treasury-capital-markets/finance_cash_flow_forecasting_model.md
  - domain-finance/treasury-capital-markets/finance_bank_relationship_rfp_framework.md
  - domain-finance/risk-management/finance_liquidity_risk_analysis.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, or hedge-accounting advice.**

## Objective

Build an investment policy statement (IPS) for a corporate or institutional cash/short-term portfolio that codifies the objective hierarchy (safety → liquidity → yield), defines eligible instruments and prohibited investments, sets credit-quality, maturity, and concentration limits, names benchmarks, and establishes governance and reporting — producing a document a treasury committee or board can adopt.

---

## When to Use

- Drafting a first IPS for a treasury function or refreshing an outdated one.
- Codifying limits after a near-miss (e.g., concentration or credit event).
- Aligning a portfolio to a corporate cash strategy with liquidity tranching.
- Preparing for an audit or board governance review of treasury investments.
- **Do not use** to recommend specific securities to buy, to set an endowment/pension long-horizon asset allocation (different objective set), or to give investment advice.

---

## Inputs / Context Required

```
<ips_inputs>
Organization / fund:
Type:                              Corporate treasury | Foundation/endowment short-term | Government/municipal | Other
Reporting currency:                [CCY]
Jurisdiction / regulatory regime:  [e.g., state investment statutes, prospectus rules — verify as of date]

PORTFOLIO PROFILE
- Total investable cash (approx.):
- Liquidity tranching needs (operating / reserve / strategic):
- Typical horizon by tranche:
- Risk tolerance / objective priority (rank: safety, liquidity, yield):
- Current holdings (if refreshing):

CONSTRAINTS
- Permitted instrument universe (or "advise standard"):
- Minimum credit quality (e.g., A-1/P-1 short-term; investment grade):
- Maturity limits (max maturity, weighted avg maturity):
- Concentration limits (per issuer, per sector, per instrument type):
- ESG / exclusion screens (if any):
- Benchmark preference (if any):

GOVERNANCE
- Approval authority structure:
- Reporting cadence to committee/board:
- Exception/escalation process:
</ips_inputs>
```

---

## Constraints

### Must
- Lead with the **objective hierarchy** in priority order: **Safety of principal → Liquidity → Yield** (the standard corporate cash priority); state it explicitly and let limits flow from it (RT-03 tradeoff).
- Use **liquidity tranching**: Operating (immediate), Reserve (near-term), Strategic (longer) — each with its own maturity and instrument profile.
- Define **eligible instruments** AND **prohibited investments** explicitly.
- Set quantified **limits**: minimum credit quality, max maturity / weighted-average maturity (WAM), and per-issuer / per-sector concentration caps.
  - `Issuer concentration = Holdings in issuer ÷ Total portfolio ≤ limit`
  - `WAM = Σ (weight_i × days-to-maturity_i)` ≤ stated maximum.
- Name a **benchmark** per tranche (e.g., a money-market index or T-bill yield) for performance evaluation.
- Specify **governance**: authorities, reporting cadence, exception process, periodic review date.
- Reference regulation/credit-rating frameworks **generically** (e.g., NRSRO short-term ratings) without inventing specific thresholds the user did not supply; note "verify applicable statutes/regulations as of [date]."
- Trace every limit to a stated input or label it a recommended default to be ratified.

### Must Not
- Recommend specific securities or issuers to purchase.
- Place yield above safety/liquidity in the objective hierarchy for an operating cash portfolio.
- Invent regulatory limits, rating thresholds, or required reserve rules.
- Omit prohibited-investment and concentration sections.
- Present limits as final without a board/committee ratification step.

---

## Instructions

1. **State purpose and scope.** Define which assets the IPS governs and the entity adopting it.

2. **Set the objective hierarchy (RT-03).** Rank safety, liquidity, yield. For operating cash, safety and liquidity precede yield; state the tradeoff and why.

3. **Define liquidity tranches.**
   ```
   Operating tranche:  immediate needs; max maturity short (e.g., ≤ 90 days); highest liquidity instruments
   Reserve tranche:    near-term needs; intermediate maturity; high-grade instruments
   Strategic tranche:  excess cash; longer maturity within policy; still high grade
   ```
   Size each tranche from the cash-forecast inputs.

4. **Specify eligible instruments per tranche** (e.g., government bills, agency, high-grade CP, bank deposits/CDs, money-market funds, repo) — only those the user permits or standard defaults flagged for ratification.

5. **List prohibited investments** (e.g., equities, below-investment-grade, structured/leveraged products, derivatives for speculation, illiquid private instruments) unless explicitly permitted.

6. **Set quantified limits (NE-11).**
   ```
   Minimum credit quality: [short-term rating floor / IG floor]
   Max maturity (per tranche) and portfolio WAM cap
   Per-issuer concentration cap (ex-government): e.g., ≤ X% (recommended default; ratify)
   Per-sector / per-instrument-type caps
   ```

7. **Name benchmarks and performance evaluation** per tranche; define how yield is measured net of any fees and risk-adjusted.

8. **Define governance (DS-06).** Approval authorities by size, reporting cadence (holdings, compliance with limits, exceptions), exception/escalation process, and a periodic IPS review date.

9. **Compliance monitoring.** Specify how limit breaches are detected and remediated (e.g., monthly limit check, cure period).

10. **Verification (QA-01).** Confirm objective hierarchy ordering, that every limit is quantified, and that prohibited/concentration sections are present.

---

## Output Format

```
## Investment Policy Statement — [Organization]
Currency: [CCY] | Adopting body: [committee/board] | Effective: [date] | Review: [date]
Data: user-supplied; defaults flagged for ratification. Verify applicable statutes as of [date].

### 1. Purpose & Scope
[Assets governed; entity; relationship to cash strategy]

### 2. Objective Hierarchy (priority order)
1. Safety of principal
2. Liquidity
3. Yield (subject to 1 and 2)

### 3. Liquidity Tranches (illustrative sizing)
| Tranche   | Purpose            | Size  | Max maturity | Instruments |
|-----------|--------------------|-------|--------------|-------------|
| Operating | Immediate needs    | 40%   | ≤ 90 days    | Govt bills, MMFs, deposits |
| Reserve   | Near-term needs    | 35%   | ≤ 1 year     | Agency, high-grade CP, CDs |
| Strategic | Excess cash        | 25%   | ≤ 3 years    | Govt/agency, high-grade corp |

### 4. Eligible Instruments
[List per tranche]

### 5. Prohibited Investments
[Equities, below-IG, leveraged/structured products, speculative derivatives, illiquid private, etc.]

### 6. Limits (quantified)
| Limit                    | Setting (illustrative; ratify) |
|--------------------------|--------------------------------|
| Min short-term rating    | A-1 / P-1 (or as supplied) |
| Min long-term rating     | A− / A3 (or as supplied) |
| Max single maturity      | per tranche above |
| Portfolio WAM cap        | ≤ 365 days (illustrative) |
| Per-issuer cap (ex-govt) | ≤ 5% of portfolio (illustrative) |
| Per-sector cap           | ≤ 25% (illustrative) |
| MMF per-fund cap         | ≤ 10% (illustrative) |

### 7. Benchmarks
| Tranche   | Benchmark (example) |
|-----------|---------------------|
| Operating | 3-month T-bill / MMF index |
| Reserve   | 1-year T-bill index |
| Strategic | 1–3 year govt index |

### 8. Governance
| Element            | Setting |
|--------------------|---------|
| Approval authority | <[X]: treasurer; ≥[X]: CFO; ≥[Y]: committee |
| Reporting cadence  | Monthly holdings + limit-compliance report |
| Exception process  | Documented, time-bound cure, escalation to committee |
| IPS review         | Annual (or on material change) |

### 9. Compliance Monitoring
[Limit-check frequency; breach remediation; cure period]
```

---

## Verification

- [ ] Objective hierarchy ordered safety → liquidity → yield (for operating cash).
- [ ] Liquidity tranches defined with maturity and instrument profiles.
- [ ] Eligible AND prohibited instruments both specified.
- [ ] Every limit quantified (credit floor, maturity, WAM, concentration).
- [ ] Benchmarks named per tranche.
- [ ] Governance: authorities, reporting, exception process, review date all present.
- [ ] No specific securities recommended; no invented regulatory thresholds.
- [ ] Defaults flagged for ratification; statutes flagged to verify as of date.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Putting yield ahead of safety/liquidity | Objective hierarchy fixed for operating cash; yield is subordinate |
| Recommending specific securities | IPS sets the framework, not buy lists |
| Inventing regulatory/rating limits | Use supplied limits or flag defaults for ratification; verify statutes |
| Omitting concentration/prohibited sections | Both are mandatory sections |
| Treating limits as final | Require committee/board ratification before adoption |
| Vague "high quality" language | Quantify with explicit rating floors and caps |
