---
title: "Estate Tax Planning Memo — Exposure Analysis with Lifetime Gifting, GST, Portability and Valuation Strategies"
category: legal/trusts-estates
description: "Write an attorney's estate-tax planning memo: build the gross-estate picture by asset and title, compute projected federal and state estate-tax exposure under explicitly labelled and verified assumptions (exclusion amount, rates, growth, order of deaths), then compare strategies — marital and credit-shelter or disclaimer planning, portability, annual-exclusion and lifetime gifting, GST allocation and dynasty trusts, SLATs, GRATs, ILITs, entity valuation discounts, charitable split-interest trusts — each with its tax effect, income-tax basis trade-off, control and liquidity cost, and legal risk. Every exemption amount, rate and deadline is supplied by the user or marked for verification. Distinct from a client-side financial beneficiary review."
techniques:
  - RT-02
  - DS-02
  - QA-04
  - QA-05
  - QA-01
difficulty: advanced
tags:
  - legal
  - trusts-estates
  - estate-tax
  - gift-tax
  - gst
  - portability
  - lifetime-gifting
  - valuation
  - wealthy-client
updated: "2026-09-24"
reasoning:
  styles: [analytic, quantitative, comparative, strategic]
  stakes: high
  horizon: years
  uncertainty: risk
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: small_team
  output_format: [memo, matrix]
  user_role: [attorney, tax_adviser, wealth_planner]
  mode: [diagnose, decide, plan]
related_prompts:
  - domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md
  - domain-legal/trusts-estates/legal_revocable_trust_drafter.md
  - domain-legal/corporate-ma/legal_409a_or_qsbs_issue_spotter.md
  - domain-legal/research/legal_research_memo_irac.md
---

## Objective

Give the attorney a planning memo that (1) quantifies projected estate-tax exposure
under stated, verified assumptions and at least two sensitivity cases, (2) compares
candidate strategies on the same scale — tax saved, income-tax basis cost, loss of
control or access, liquidity, cost and legal risk — and (3) recommends a sequenced
plan with the documents it requires. It is a planning memo, not a tax opinion.

## When to Use

- A client's estate may exceed, or may grow to exceed, the federal and/or state
  exclusion amount.
- Exclusion-amount changes, a liquidity event (business sale, inheritance), a death of
  a spouse (portability decision), or a move between states.
- Before drafting a will or revocable trust, to decide whether tax sub-trusts are needed.

**Distinct from:**
- `domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md` — a
  consumer-side review of existing documents and designations that flags "tax
  exposure" and routes to an attorney; this memo is that attorney's analysis.
- `domain-legal/corporate-ma/legal_409a_or_qsbs_issue_spotter.md` — QSBS per-issuer
  cap stacking via non-grantor trusts is analysed there in a deal context; cross-refer
  if the estate holds founder stock.
- `domain-legal/trusts-estates/legal_revocable_trust_drafter.md` — implements the
  sub-trust structure this memo selects.

## Your Input

- **Jurisdiction (required):** domicile and every state where real or tangible property
  is located (state estate/inheritance tax exposure).
- **Client(s):** ages, marital status, citizenship of each spouse (non-citizen spouse
  changes marital-deduction planning `[VERIFY]`), health if relevant to horizon.
- **Balance sheet:** each asset with value, basis, title and beneficiary designation;
  liabilities; life insurance ownership and death benefit.
- **Prior taxable gifts** and GST allocations (prior gift-tax returns).
- **Current-law parameters (required or `[VERIFY]`):** federal basic exclusion amount,
  annual exclusion, GST exemption, top rate, state exemption and rates, portability
  and election deadlines. If not supplied, the memo uses labelled placeholders.
- **Goals and constraints:** need for access to gifted assets, charitable intent,
  family governance, liquidity needs, risk tolerance.

## Constraints

**Must:**
- Show every tax computation with its inputs, and label each parameter as
  **SUPPLIED** or **ASSUMED — [VERIFY]**.
- Run a base case and at least two sensitivities (e.g. order of deaths reversed;
  asset growth at a higher rate; lower exclusion amount).
- For each strategy report: estate-tax effect, gift-tax use, GST effect, loss of
  step-up in basis (income-tax cost), control/access given up, liquidity impact,
  implementation cost, and principal legal risks (e.g. step-transaction, valuation
  challenge, reciprocal-trust doctrine, inclusion by retained interest) `[CITE]`.
- Separate federal and state analyses; state exemption and portability rules often
  differ `[VERIFY]`.
- End with a sequenced plan and an open-items list.

**Must Not:**
- State exclusion amounts, annual exclusions, rates, sunset or indexing rules,
  filing deadlines, Code sections, regulations, rulings or cases as fact unless
  supplied — use `[VERIFY: …]` and `[CITE: …]`.
- Present a strategy's tax saving without its basis cost and access cost.
- Recommend a valuation discount percentage; discounts come from a qualified appraisal.
- Deliver a tax opinion or guarantee outcomes.

## Method

1. **Balance sheet by title.** Probate, trust, joint, beneficiary-designated, and
   entity-held assets; include life insurance owned by the insured.
2. **Parameters table.** Each law parameter, value, SUPPLIED / ASSUMED, source.
3. **Base-case exposure.** Federal and state, first and second death, current structure.
4. **Sensitivities.** At least two; show which assumption drives the result.
5. **Strategy screen.** Filter the catalogue (marital/credit-shelter, disclaimer
   planning, portability, annual-exclusion gifts, lifetime exclusion gifts, GST
   allocation/dynasty trust, SLAT, GRAT, ILIT, family entity with appraisal, CRT/CLAT,
   state-residency planning) against goals and constraints; drop the ones that fail
   and say why.
6. **Strategy comparison matrix.** Common metrics for survivors of the screen.
7. **Recommendation.** Sequence, documents, filings, professionals needed (appraiser,
   CPA), and triggers to revisit.
8. **Open items and verification list.**

## Output Format

```markdown
# Estate Tax Planning Memo — [Client(s)]
**Domicile:** [state] · **Other situs states:** [ ] · **Date:** [ ]
**Privileged & Confidential — Attorney–Client Communication / Work Product**
**Scope:** planning analysis, not a tax opinion.

## 1. Summary and recommendation (≤ 1 page)
## 2. Balance sheet by title
| Asset | Value | Basis | Title / designation | In gross estate? |
## 3. Parameters
| Parameter | Value | SUPPLIED / ASSUMED [VERIFY] | Source |
## 4. Exposure — base case and sensitivities
| Case | Federal tax | State tax | Total | Driver |
## 5. Strategy screen (dropped strategies and reasons)
## 6. Strategy comparison
| Strategy | Est. tax saved | Basis cost | Access given up | Liquidity | Cost | Legal risks |
## 7. Sequenced plan
## 8. Open items / verification
```

## Worked Example

**Input (abridged):** Married couple, both U.S. citizens, ages 66 and 64; combined
net estate $26M (closely held operating company $12M with basis $1M, brokerage $7M,
residence $3M, life insurance $4M death benefit owned by husband). Domicile state has
no estate tax `[VERIFY]`; vacation home in a state that does `[VERIFY]`. User did not
supply current-law parameters.

**Parameters:**

| Parameter | Value | Status |
|---|---|---|
| Federal basic exclusion per person | $15.0M | **ASSUMED for illustration — [VERIFY: amount in effect for year of death and indexing]** |
| Top federal rate on excess | 40% | **ASSUMED — [VERIFY]** |
| Portability available to survivor | Yes, if timely election | **[VERIFY: election mechanics and deadline]** |

**Base case (husband dies first; everything to wife; portability elected; no growth):**
Wife's estate $26M − (her $15.0M + ported $15.0M) = no federal tax on these assumptions.

**Sensitivity A (portability not elected):** $26M − $15.0M = $11.0M × 40% =
**$4.4M** federal tax. Driver: a missed election, not the plan.

**Sensitivity B (6% annual growth, second death in 20 years):** $26M × 1.06²⁰ ≈
$83.4M; less $30.0M exclusions (ported amount does not grow `[VERIFY]`; survivor's
own may be indexed `[VERIFY]` — held flat here for conservatism) = $53.4M × 40% ≈
**$21.4M**. Driver: growth after the first death.

**Strategy comparison (excerpt):**

| Strategy | Est. tax saved (Sens. B) | Basis cost | Access given up | Legal risks |
|---|---|---|---|---|
| Credit-shelter trust at first death instead of portability only | Freezes ~$15M plus its growth outside wife's estate | Loses second step-up on sheltered assets | Wife as beneficiary under HEMS — modest | GST not portable `[VERIFY]` — allocate GST to the shelter trust |
| ILIT holding the $4M policy | $4M × 40% = $1.6M | None (insurance) | Husband gives up ownership | Transfer of existing policy: inclusion if death within a look-back period `[VERIFY/CITE]` |
| Gift of non-voting company shares to GST dynasty trust, appraised | Removes future growth of gifted shares | Low basis ($1M on $12M) carries over — significant income-tax cost on a later sale | Loss of the value; voting retained | Valuation challenge; appraisal required — no discount assumed here |

**Recommendation line:** "Portability alone leaves $21M of modelled exposure in
Sensitivity B; move the policy to an ILIT now, add a credit-shelter/disclaimer trust
to both revocable trusts, and obtain a qualified appraisal before any business-interest
gift."

## Verification

- [ ] Every parameter is SUPPLIED or ASSUMED with `[VERIFY]`; none asserted from memory.
- [ ] Computations show inputs and arithmetic; results reproduce.
- [ ] Base case plus at least two sensitivities; driver of each identified.
- [ ] Federal and state analysed separately, including out-of-state real property.
- [ ] Every strategy shows tax saved alongside basis cost, access cost and legal risk.
- [ ] Portability, GST and step-up interactions addressed.
- [ ] No valuation-discount percentage assumed without appraisal.
- [ ] Memo scoped as planning, not a tax opinion; citations are placeholders.

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Quoting this year's exclusion amount from memory | Use the user's figure or a labelled ASSUMED value with `[VERIFY]` |
| "No tax" conclusion from a static snapshot | Always run growth and order-of-deaths sensitivities |
| Treating portability as a complete plan | Show what portability does not do: shelter growth, GST, or some state exemptions `[VERIFY]` |
| Reporting tax saved without the lost step-up | Put basis cost in the same row; for low-basis assets it can exceed the estate-tax saving |
| Plugging a discount percentage | Discounts come only from a qualified appraisal; show results undiscounted |
| Forgetting life insurance owned by the insured | Include the death benefit in the gross estate and consider an ILIT |
| Ignoring a second state's estate tax on real property | Test situs states separately `[VERIFY]` |
| Citing Code sections or cases unverified | Use `[CITE: …]`; this is a planning memo, not an opinion |

## Related

- `domain-legal/trusts-estates/legal_revocable_trust_drafter.md` — implementing sub-trusts and disclaimer planning
- `domain-legal/trusts-estates/legal_will_drafter.md` — tax-apportionment and survivorship clauses
- `domain-legal/trusts-estates/legal_trust_modification_or_decanting_analysis.md` — fixing tax problems in existing irrevocable trusts
- `domain-legal/corporate-ma/legal_409a_or_qsbs_issue_spotter.md` — QSBS and founder-stock interactions
- `domain-finance/personal-finance-planning/finance_estate_beneficiary_review.md` — client-side review feeding the balance sheet
