---
title: "Transfer Pricing Position Paper"
category: legal/tax
description: "Transfer pricing position paper for a controlled transaction under IRC §482 and the OECD Transfer Pricing Guidelines — accurate delineation of the transaction and functional analysis, best-method / most-appropriate-method selection with rejected-method reasoning, comparables search and adjustments, arm's-length range and position within it, and documentation for penalty protection — with every regulation cite, threshold, and local-file rule marked for verification."
techniques:
  - RT-02
  - DS-01
  - RT-05
  - QA-04
difficulty: advanced
tags:
  - legal
  - tax
  - transfer-pricing
  - section-482
  - oecd-guidelines
  - international-tax
  - documentation
  - intercompany-charges
updated: "2026-09-24"
reasoning:
  styles: [analytic, comparative, evidential]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: [memo, structured]
  user_role: [lawyer, analyst]
  mode: [assess, document]
related_prompts:
  - domain-legal/tax/legal_tax_research_memo.md
  - domain-legal/tax/legal_rd_credit_position_memo.md
  - domain-finance/valuation/finance_trading_comps_builder.md
  - domain-finance/tax-planning/finance_state_nexus_apportionment_mapper.md
---

# Transfer Pricing Position Paper

**Objective:** Set and defend the arm's-length price for a controlled transaction. The paper accurately delineates the transaction (contract terms, functions, assets, risks and who controls them, economic circumstances), selects the method under the U.S. best-method rule and the OECD most-appropriate-method standard with reasons for rejecting alternatives, documents the comparables search and adjustments, derives the arm's-length range, positions the tested result, and assembles what the documentation must contain for penalty protection and foreign local-file obligations.

**When to use:**
- Establishing pricing for a new intercompany arrangement (services, distribution, licence, cost sharing, financing).
- Annual documentation refresh or a business-model change (principal structure, IP migration).
- Preparing for an examination, a mutual agreement procedure, or an advance pricing agreement request.

**Distinct from:**
- `domain-finance/valuation/finance_trading_comps_builder.md` — market valuation comps; transfer pricing comparables are selected and adjusted for functional comparability and profit-level indicators.
- `domain-finance/tax-planning/finance_state_nexus_apportionment_mapper.md` — U.S. multistate apportionment, not cross-border related-party pricing.
- `legal_tax_research_memo.md` (this folder) — a single tax question; this paper is a method-and-evidence document for a recurring transaction.

**Audience:** International tax counsel and transfer pricing economists preparing documentation for counsel review.

---

## Your Input

- **Transaction:** [Parties (entity, country), type (tangible goods, services, IP licence, cost sharing, loan, guarantee), intercompany agreement terms]
- **Jurisdictions:** [Each tax jurisdiction involved; which is the U.S. side; treaties]
- **Functional facts:** [Who performs DEMPE functions for intangibles, who controls and has financial capacity to bear each risk, who owns what assets — from interviews and org charts]
- **Financials:** [Segmented P&L for the tested party and the transaction, by year]
- **Comparables data:** [Database, search strategy, screens, accepted and rejected companies or agreements]
- **Current method and result:** [Method used, profit-level indicator, tested result]
- **Documentation obligations:** [Master file / local file / country-by-country thresholds in each country — as verified by local advisors, or leave blank for `[VERIFY]`]
- **Controversy status:** [None / under exam / MAP / APA pending]

---

## Constraints

### Must
- **Delineate the actual transaction** from conduct, not just the contract; where conduct diverges from the agreement, state which controls and why.
- Separate **risk assumption** from **risk control** and financial capacity; returns follow functions and control of risk.
- For intangibles, map **DEMPE** functions (development, enhancement, maintenance, protection, exploitation) to entities.
- **Method selection:** evaluate each specified method for the transaction type under the U.S. regulations `[VERIFY: Treas. Reg. §1.482-1 through -9 as applicable]` and the OECD Guidelines `[VERIFY: chapter reference]`; explain rejection of each alternative.
- **Tested party** selection with reasons (least complex, reliable data).
- **Comparables:** search strategy, quantitative and qualitative screens, rejection reasons, and comparability adjustments (working capital, accounting differences).
- **Range and position:** interquartile or full range per the applicable rule `[VERIFY]`, where the tested result falls, and the adjustment point if outside.
- **Penalty protection:** list what contemporaneous documentation must contain and when it must exist `[VERIFY: §6662(e) and Treas. Reg. §1.6662-6]`.
- **Confidence:** state where the position is most exposed (method choice, comparables, characterization) and the likely counter-position of each tax authority.

### Must Not
- Invent regulation paragraph numbers, OECD paragraph numbers, documentation thresholds, penalty rates, or filing deadlines.
- Pick the method that produces the desired result and back-fill the rationale; show rejected methods on their merits.
- Treat a contractual risk allocation as conclusive when the entity lacks people to control the risk.
- Present comparables without disclosing screens and rejections.
- Assume the U.S. and foreign authorities apply identical rules; flag divergence and double-tax risk.

---

## Instructions

1. **Describe the group and transaction.** Value chain, the controlled transaction, contract terms.
2. **Functional analysis.** Functions, assets, risks per entity; risk-control framework; DEMPE for intangibles.
3. **Characterize the entities** (e.g., routine distributor, contract manufacturer, entrepreneur) with the supporting facts.
4. **Method selection.** Evaluate each candidate method; select; document rejections.
5. **Tested party and profit-level indicator.**
6. **Comparables.** Search, screens, accepted set, adjustments.
7. **Arm's-length range and tested result.** Show numbers from inputs; position; adjustment if needed.
8. **Documentation and penalty protection** checklist by jurisdiction.
9. **Risk assessment** — exposed points, each authority's likely challenge, double-tax exposure, and relief routes (MAP, APA) as options.

---

## Output Format

```markdown
# Transfer Pricing Position Paper — {Transaction} — FY {…}
**Jurisdictions:** {…}  |  **Privileged & Confidential — prepared for counsel**

## 1. Executive Summary (method, range, result, position)
## 2. Group and Transaction Overview
## 3. Functional Analysis
| Entity | Functions | Assets | Risks assumed | Control / financial capacity |
### DEMPE Map (if intangibles)
## 4. Entity Characterization
## 5. Method Selection
| Method | Applicability | Reliability considerations | Selected / Rejected — reason |
## 6. Tested Party and PLI
## 7. Comparables
| Step | Criteria | Companies remaining |
| Accepted comparables | PLI (by year) | Adjustments |
## 8. Arm's-Length Range and Result
| Statistic | Value |
## 9. Documentation and Penalty Protection   ([VERIFY] by jurisdiction)
## 10. Risk Assessment and Counter-Positions
```

---

## Worked Example

**Input (abridged):** U.S. parent licenses software IP to an Irish subsidiary that sells into EMEA; Irish entity has a 12-person sales team and no engineering staff; intercompany agreement says the Irish entity bears market and product risk and pays a 20% royalty. Tested result: Irish operating margin 38%. Comparables for distributors show an interquartile operating-margin range of 2.1%–5.4% (from the user's database run).

**Output (excerpt):**

> **Delineation:** The agreement allocates product risk to Ireland, but Ireland has no engineering personnel and no capacity to control development decisions; conduct indicates the U.S. parent controls product risk. Treat Ireland as a limited-risk distributor for pricing purposes; state the contract-vs-conduct divergence explicitly.
>
> **Method selection:** Comparable uncontrolled transaction (CUT) for the royalty — rejected: no licences of comparable software with comparable terms in the dataset. Comparable profits method / TNMM with Ireland as tested party — **selected**: least complex entity, reliable distributor comparables `[VERIFY: §1.482-5 / OECD TNMM chapter reference]`. Profit split — rejected: Ireland makes no unique and valuable contribution.
>
> **Result:** Ireland's 38% margin sits far above the 2.1%–5.4% range → the royalty is understated. Adjusting to the median of the range raises the royalty; the U.S. authority would make this adjustment on exam. Irish authority's likely counter-position: the royalty increase erodes the Irish base — flag double-tax exposure and whether MAP under the treaty is available `[VERIFY: treaty MAP article]`.

---

## Verification

- [ ] Jurisdiction lock: each country named; U.S. regulations and OECD Guidelines distinguished.
- [ ] Transaction delineated from conduct as well as contract.
- [ ] Risk control and financial capacity analyzed; DEMPE mapped where intangibles exist.
- [ ] Every candidate method evaluated with rejection reasons.
- [ ] Comparables screens and rejections disclosed.
- [ ] Range, position, and any adjustment computed from supplied data only.
- [ ] Penalty-protection documentation and local thresholds marked `[VERIFY]`.
- [ ] No regulation, OECD paragraph, threshold, or penalty rate invented.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Accepting the intercompany agreement's risk allocation at face value | Test control and financial capacity; conduct can override contract |
| Method chosen to hit a target result | Evaluate every method on reliability; document rejections |
| Comparables with undisclosed screens | Show the search funnel and rejection reasons |
| Treating a high-margin entity as routine without adjusting | Compare tested result to the range; adjust if outside |
| Assuming identical U.S. and OECD outcomes | Flag divergences and double-tax exposure |
| Stating documentation thresholds from memory | Mark `[VERIFY]` per country; local advisors confirm |
| Ignoring intangibles embedded in services or distribution | Run a DEMPE screen whenever IP is used |
