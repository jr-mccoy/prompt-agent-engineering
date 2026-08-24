---
title: "Bank Relationship RFP Framework — Banking-Services RFP Structure and Evaluation Scorecard"
category: finance/treasury-capital-markets
description: "Structure a banking-services RFP and a weighted relationship-evaluation framework covering services, pricing, credit support, technology, service quality, and counterparty strength."
techniques:
  - NE-11
  - DS-02
  - RT-03
  - QA-01
  - DS-06
difficulty: beginner
tags:
  - bank-rfp
  - banking-services
  - vendor-evaluation
  - treasury
  - relationship-management
updated: "2026-06-08"
related_prompts:
  - domain-finance/treasury-capital-markets/finance_investment_policy_statement_builder.md
  - domain-finance/treasury-capital-markets/finance_capital_raise_readiness_assessment.md
  - domain-finance/treasury-capital-markets/finance_treasury_hedging_program_design.md
  - domain-finance/field_guide.md
---

**Informational only — not financial, investment, or hedge-accounting advice.**

## Objective

Structure a banking-services RFP and an accompanying weighted evaluation scorecard so a treasury team can compare banking partners on a like-for-like basis across the dimensions that matter — services and coverage, pricing/fees, credit support, technology/integration, service quality, and counterparty strength — and reach a defensible, documented selection.

---

## When to Use

- Running a periodic banking RFP or consolidating/diversifying the bank panel.
- Selecting a primary operating bank or adding a credit/cash-management provider.
- Benchmarking incumbent pricing and service before a renewal.
- Documenting a defensible selection rationale for governance/audit.
- **Do not use** to negotiate a specific credit facility's terms (use `finance_debt_issuance_analysis.md`) or to set investment policy (use `finance_investment_policy_statement_builder.md`).

---

## Inputs / Context Required

```
<bank_rfp_inputs>
Organization:
Currency / regions of operation:    [CCY; countries needing coverage]
Jurisdiction(s):                    [regulatory/KYC considerations — verify as of date]

NEEDS
- Services required (cash management, payments, FX, trade finance, credit/RCF, custody, card, payroll):
- Transaction volumes / value (by service, monthly):
- Account structure needs (multi-entity, multi-currency, pooling/sweeping):
- Technology needs (ERP/TMS integration, APIs, host-to-host, portals):
- Credit needs (committed facility size, ancillary-business expectations):
- Service-level expectations (coverage model, response times):

EVALUATION
- Decision criteria & relative importance (or "advise standard weights"):
- Incumbent provider(s) and current pricing (for benchmarking):
- Number of banks to invite:
- Counterparty constraints (min rating, geographic, regulatory):

GOVERNANCE
- Decision authority / committee:
- Timeline:
</bank_rfp_inputs>
```

---

## Constraints

### Must
- Produce two artifacts: (1) a structured **RFP question set** by section, and (2) a **weighted evaluation scorecard** (RT-03 tradeoff across competing criteria).
- Define **weights** that sum to 100% across the evaluation dimensions; tie weights to stated needs.
  - `Weighted score = Σ (dimension score × dimension weight)`
- Require **comparable pricing** (a standardized pro-forma fee schedule / RFP pricing grid) so banks quote like-for-like; compute an estimated annual cost from stated volumes.
  - `Estimated annual cost = Σ (unit price × annual volume)` per service.
- Include **counterparty strength** as a scored dimension (credit rating, capitalization) — referencing rating frameworks generically without inventing grades.
- Include **technology/integration** and **service-quality** as explicit dimensions, not afterthoughts.
- Define **governance**: scoring panel, conflict handling, documentation of rationale (DS-06).
- Flag currency/jurisdiction coverage and "verify regulatory/KYC requirements in each region as of [date]."

### Must Not
- Score on price alone; relationship value spans service, credit, technology, and resilience.
- Invent bank ratings, fee benchmarks, or capabilities.
- Let weights be undocumented or fail to sum to 100%.
- Compare quotes that are not on a standardized pricing grid.
- Omit counterparty strength / concentration considerations.

### Notes
- Counterparty concentration matters: over-reliance on one bank for both operating and credit services is a resilience risk; reflect it in scoring.

---

## Instructions

1. **Define needs and required services.** From inputs, list the services, volumes, regions, and technology requirements that the RFP must cover.

2. **Build the RFP question set by section:**
   - **Services & coverage:** capabilities by service, geographic reach, relationship/coverage model.
   - **Pricing:** standardized fee grid (per-item, monthly maintenance, FX spreads, facility fees) — require quotes on the supplied volume profile.
   - **Credit support:** appetite, committed-facility terms, ancillary expectations.
   - **Technology & integration:** ERP/TMS connectivity, APIs, portals, security/SOC reports.
   - **Service quality:** SLAs, escalation, references, implementation/onboarding plan.
   - **Counterparty strength & risk:** ratings, capital, business continuity, regulatory standing.

3. **Set evaluation weights (RT-03).** Assign weights summing to 100% reflecting priorities (e.g., a credit-dependent borrower weights credit support higher; a payments-heavy operator weights technology/pricing).

4. **Standardize pricing for comparison (NE-11).**
   ```
   Estimated annual cost (per bank) = Σ over services (Unit price × Annual volume)
   Normalize FX/credit pricing to comparable bases (e.g., spread in bps on stated notional).
   ```

5. **Score and aggregate.**
   ```
   Dimension score (1–5) per bank, per dimension
   Weighted total = Σ (dimension score × weight)
   ```
   Combine the weighted qualitative score with the estimated-cost comparison; do not collapse to price alone.

6. **Assess concentration/resilience.** Flag if the leading proposal concentrates both operating and credit relationships in one counterparty; consider a panel split.

7. **Governance (DS-06).** Define the scoring panel, how conflicts are handled, and how the selection rationale is documented for audit.

8. **Verification (QA-01).** Confirm weights sum to 100%, pricing is on a like-for-like grid, and counterparty strength is scored. Confirm no fabricated ratings or benchmarks.

---

## Output Format

```
## Banking-Services RFP & Evaluation Framework — [Organization]
Currency: [CCY] | Regions: [list] | Prepared: [date] | Data: user-supplied
(All figures illustrative unless traced to an input; verify regional KYC/regulation as of date)

### Part A — RFP Question Set (by section)
1. Services & Coverage
   - [Capabilities by service; geographic reach; coverage model questions]
2. Pricing (standardized grid — quote on our volumes)
   | Service        | Unit | Our annual volume | Bank unit price | Annual cost |
   |----------------|------|-------------------|-----------------|-------------|
   | ACH / payments | item | 120,000           | [quote]         | [calc]      |
   | Wires          | item | 6,000             | [quote]         | [calc]      |
   | FX spot        | bps  | $200M notional    | [quote]         | [calc]      |
   | RCF commitment | bps  | $100M             | [quote]         | [calc]      |
3. Credit Support  [appetite, facility terms, ancillary]
4. Technology & Integration  [ERP/TMS, APIs, security/SOC]
5. Service Quality  [SLAs, escalation, references, onboarding]
6. Counterparty Strength  [ratings, capital, BCP, regulatory]

### Part B — Weighted Evaluation Scorecard (illustrative weights)
| Dimension              | Weight | Bank A | Bank B | Bank C |
|------------------------|--------|--------|--------|--------|
| Services & coverage    | 20%    | 4      | 3      | 5      |
| Pricing (cost)         | 25%    | 3      | 5      | 4      |
| Credit support         | 20%    | 5      | 3      | 4      |
| Technology/integration | 15%    | 4      | 4      | 3      |
| Service quality        | 10%    | 4      | 3      | 4      |
| Counterparty strength  | 10%    | 5      | 4      | 4      |
| **Weighted total**     | 100%   | **4.0**| **3.9**| **4.1**|

### Estimated Annual Cost Comparison (illustrative)
| Bank   | Estimated annual cost | Note |
|--------|-----------------------|------|
| Bank A | $640k                 | premium service |
| Bank B | $510k                 | lowest cost |
| Bank C | $590k                 | best coverage |

### Concentration / Resilience Note
[Flag if winner holds both operating + credit; consider panel split]

### Recommendation & Rationale
Selected: [Bank] — highest weighted score balancing [credit/coverage] against cost; concentration
managed by [retaining a secondary bank for X]. Rationale documented for governance.
```

---

## Verification

- [ ] RFP covers all six sections (services, pricing, credit, technology, service, counterparty).
- [ ] Evaluation weights sum to 100% and reflect stated priorities.
- [ ] Pricing requested on a standardized grid; annual cost computed from stated volumes.
- [ ] Counterparty strength scored; no fabricated ratings.
- [ ] Weighted total combined with cost — not price-only selection.
- [ ] Concentration/resilience considered.
- [ ] Governance (panel, conflicts, documentation) defined.
- [ ] Regional KYC/regulatory coverage flagged to verify.

---

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Selecting on price alone | Weighted scorecard across six dimensions; cost is one input |
| Inventing bank ratings or fee benchmarks | Use only supplied/quoted data; rating frameworks referenced generically |
| Undocumented or non-100% weights | Weights must sum to 100% and tie to stated needs |
| Comparing non-comparable quotes | Standardized pricing grid on the same volume profile |
| Ignoring counterparty concentration | Resilience note + scored counterparty-strength dimension |
| Skipping selection rationale | Document the weighted rationale for governance/audit |
