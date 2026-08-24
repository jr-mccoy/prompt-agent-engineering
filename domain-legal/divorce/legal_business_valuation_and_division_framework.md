---
title: "Business Valuation and Division Framework"
category: legal/divorce
description: "Frame the valuation and division of a closely-held business interest in divorce: select the valuation date and standard of value, choose among asset/income/market approaches, address enterprise vs. personal goodwill under the state's rule, normalize owner compensation and add-backs, apply marketability/minority discounts where allowed, and structure a buyout or offset — producing a valuation-issue memo and an expert-scope checklist."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-05
  - RP-01
  - CM-02
  - QA-01
  - QA-12
difficulty: advanced
tags:
  - legal
  - divorce
  - family-law
  - business-valuation
  - goodwill
  - buyout
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_marital_property_characterization_analysis.md
  - domain-legal/divorce/legal_property_division_and_equalization_proposal.md
  - domain-legal/divorce/legal_hidden_asset_and_dissipation_investigation.md
  - domain-legal/divorce/legal_divorce_tax_consequences_analysis.md
  - domain-legal/corporate-ma/legal_due_diligence_request_list.md
---

**Purpose:** Structure the legal framework for valuing and dividing a closely-held business interest in a divorce — the valuation date, standard of value, approach selection, goodwill treatment, normalization, discounts, and buyout/offset mechanics — and scope the financial expert's work. Output is an issue-framing and expert-scope memo, not a valuation opinion (which requires a qualified appraiser).

**When to use:** A spouse owns or co-owns a business, professional practice, or significant private interest; preparing for a valuation expert engagement; evaluating an opposing expert's report; structuring a buyout in settlement.

---

## Your Input

- **Jurisdiction:** [State; the state's rule on goodwill (enterprise vs. personal), standard of value, and discounts `[CITE: …]`]
- **Property regime:** [Community / equitable distribution]
- **Business facts:** [Entity type, industry, ownership %, owner's role, employee count, revenue/EBITDA history]
- **Valuation date:** [State's prescribed date or the date in dispute]
- **Records available:** [Tax returns, financials, GL, owner comp, buy-sell agreement, prior valuations]
- **Goodwill facts:** [Whether value depends on the owner's personal reputation/skill vs. transferable enterprise value; non-compete feasibility]
- **Normalization items:** [Owner compensation vs. market, perquisites, related-party transactions, non-recurring items]
- **Discount facts:** [Minority interest, lack of marketability, control]
- **Buy-sell / restrictions:** [Transfer restrictions, agreed formula, third-party owners]
- **Division preference:** [Buyout by owner-spouse, offset against other assets, or co-ownership/sale]

---

## Constraints

**Must:**
- Identify the **standard of value** and **valuation date** the state uses for marital business interests `[CITE: …]`.
- Address the state's **goodwill rule** — whether **personal/professional goodwill** is excluded from the marital estate and only **enterprise goodwill** is divisible (this varies sharply by state) `[CITE: …]`.
- Lay out the **three approaches** (asset-based, income/capitalization or DCF, market/comparable) and which fits the business and the standard of value.
- Require **normalization** of owner compensation and **add-backs/adjustments**, and a check for **double-dipping** (counting the same income stream for both business value and spousal support).
- Address **marketability/minority/control discounts** only as the state permits in the marital context `[CITE: …]`.
- Note the role of a **buy-sell agreement** and whether its formula controls or is merely evidence.
- Scope the **financial expert's** engagement and the records needed; mark valuation conclusions as requiring a qualified appraiser `[NEED EXPERT VALUATION]`.
- Propose **buyout/offset** mechanics, including payment terms, security, and tax effects (cross-reference tax analysis).
- Use placeholders `[CITE: ...]`, `[NEED EXPERT VALUATION]`, `[NEED: ...]` for unsupplied authority, values, or facts.

**Must Not:**
- Produce a definitive business value — that requires a qualified valuation expert.
- Treat personal goodwill as divisible where the state excludes it (or vice versa).
- Apply minority/marketability discounts where the state disfavors them in divorce.
- Ignore the double-dip problem when support is also at issue.
- Invent multiples, cap rates, discount percentages, or the state's goodwill rule.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Standard of value & date.** State the standard (fair value/fair market value/intrinsic) and valuation date for the state `[CITE: …]`.
2. **Approach selection.** Evaluate asset, income, and market approaches against the business and the standard of value; recommend a primary approach.
3. **Goodwill analysis.** Apply the state's enterprise vs. personal goodwill rule; assess transferability and non-compete feasibility.
4. **Normalization.** Identify owner-comp adjustments, perquisites, related-party and non-recurring items; flag double-dip risk with support.
5. **Discounts.** Address minority/marketability/control discounts as the state allows.
6. **Buy-sell.** Determine whether the buy-sell formula controls or is evidentiary.
7. **Expert scope.** List the records and analyses the appraiser needs; mark the value `[NEED EXPERT VALUATION]`.
8. **Division mechanics.** Propose buyout (lump/installment, security, interest), offset against other assets, or sale/co-ownership; note tax effects.

---

## Output Format

```markdown
# BUSINESS VALUATION & DIVISION FRAMEWORK — PRIVILEGED WORK PRODUCT
**State:** {…} [CITE: …]   **Standard of value:** {…}   **Valuation date:** {…}   **Regime:** {…}

## 1. Standard of Value & Date
{…} [CITE: …]

## 2. Approach Selection
- Asset-based: {fit} ; Income (DCF/cap): {fit} ; Market/comparable: {fit} ; **Recommended:** {…}

## 3. Goodwill
- State rule: {enterprise divisible / personal excluded} [CITE: …]
- Transferability / non-compete feasibility: {…}

## 4. Normalization & Add-backs
| Item | Reported | Normalized | Basis | Double-dip risk |
|---|---|---|---|---|
| Owner compensation | {$} | {$} | {market} | {yes/no} |

## 5. Discounts
- {Minority / marketability / control}: {allowed? extent?} [CITE: …]

## 6. Buy-Sell Agreement
- Controls / evidentiary only: {…}

## 7. Expert Scope & Records Needed
- [ ] {tax returns} [ ] {financials} [ ] {GL} [ ] {owner comp} [ ] {buy-sell} — Value: [NEED EXPERT VALUATION]

## 8. Division Mechanics
- {Buyout terms / offset / sale}; security: {…}; tax effects: {see tax analysis}
```

---

## Verification

- [ ] Standard of value and valuation date identified for the state.
- [ ] Goodwill analyzed under the state's enterprise vs. personal rule.
- [ ] Valuation approaches evaluated; primary approach recommended.
- [ ] Normalization/add-backs addressed; double-dip risk flagged where support is at issue.
- [ ] Discounts handled per the state's marital-context rule.
- [ ] Buy-sell agreement's role determined.
- [ ] Expert scope and records list provided; value marked as requiring an appraiser.
- [ ] Buyout/offset mechanics with tax effects proposed.
- [ ] No invented multiples, discounts, or the state's goodwill rule.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Stating a definitive business value | Frame the issue; mark value [NEED EXPERT VALUATION] for a qualified appraiser |
| Dividing personal/professional goodwill where the state excludes it | Apply the state's goodwill rule [CITE] before including goodwill |
| Counting business income for value and again for support | Flag and resolve the double-dip problem |
| Applying minority/marketability discounts reflexively | Apply only as the state permits in divorce |
| Treating a buy-sell formula as automatically controlling | Determine whether it controls or is merely evidence |
| Skipping normalization of owner compensation | Adjust owner comp to market and identify perquisites/add-backs |
| Picking an approach that fits the data but not the standard of value | Match approach to the state's standard of value |
| Inventing cap rates or multiples | Leave quantitative inputs to the appraiser; flag them |
| Proposing a buyout with no security or terms | Specify payment terms, interest, and security |
| Ignoring transfer restrictions / third-party owners | Account for buy-sell and co-owner constraints in division |
