---
title: "Property Division and Equalization Proposal"
category: legal/divorce
description: "Build a marital-estate division proposal: a schedule allocating each characterized asset and debt between the parties, computing each side's net allocation, and proposing an equalization payment or offsetting transfer to reach the target split — community equal-division or equitable-distribution factor-based — with tax-basis and liquidity notes and a settlement-vs-litigation comparison."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - CM-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - legal
  - divorce
  - family-law
  - property-division
  - equalization
  - equitable-distribution
updated: "2026-06-01"
related_prompts:
  - domain-legal/divorce/legal_marital_property_characterization_analysis.md
  - domain-legal/divorce/legal_financial_affidavit_and_disclosure_builder.md
  - domain-legal/divorce/legal_retirement_division_and_qdro_framework.md
  - domain-legal/divorce/legal_divorce_tax_consequences_analysis.md
  - domain-legal/divorce/legal_marital_settlement_agreement_drafter.md
---

**Purpose:** Convert a completed characterization and valuation into a concrete division: allocate each asset and debt, total each party's net, and propose an equalization payment or offsetting transfers to reach the target split under the state's regime. Output is a division schedule and proposal memo to support negotiation or trial — not a final order.

**When to use:** After characterization and valuation; preparing a settlement proposal or MSA property terms; preparing the property issue for a settlement conference or trial; evaluating the other side's proposal.

---

## Your Input

- **Jurisdiction & regime:** [State; community (presumptive equal) or equitable distribution (factor-based)]
- **Division standard:** [Equal division, or the state's equitable-distribution factors `[NEED FACTOR LIST: …]`]
- **Characterized inventory:** [Each marital/community asset and debt with confirmed value]
- **Separate property:** [Items confirmed separate, to be set aside to the owner]
- **Liquidity/tax notes:** [Which assets are liquid; tax basis; built-in gain; penalties for early access]
- **Non-divisible considerations:** [Items that cannot be split (residence, business, pension) and need offset]
- **Party preferences:** [Who wants the house, business, retirement; ability to refinance/buy out]
- **Reimbursement/equitable claims:** [From the characterization analysis]
- **Target split:** [50/50, or the equitable target with justification]

---

## Constraints

**Must:**
- State the **division standard** for the state — presumptive equal split (community) or **factor-based equitable distribution** `[NEED FACTOR LIST: …]` — and apply it.
- Use only **confirmed values** from valuation/disclosure; flag any unvalued item `[NEED VALUATION: …]`.
- Allocate **each asset and debt**, compute **each party's net allocation**, and compute the **equalization payment** needed to hit the target.
- Account for **tax basis, built-in gain, and liquidity** — a dollar of pre-tax retirement is not a dollar of home equity; note after-tax/effective values where material.
- For **indivisible assets** (residence, business, pension), propose buyout/offset mechanics, including financing/refinance feasibility.
- Separate **confirmed separate property** set-asides from the marital division.
- Provide a **settlement-vs-litigation comparison** noting the range of likely outcomes and the cost/risk of trial.
- Use placeholders `[CITE: ...]`, `[NEED FACTOR LIST: ...]`, `[NEED VALUATION: ...]` for unsupplied authority or values.

**Must Not:**
- Apply equal division in an equitable-distribution state, or ignore the factors.
- Treat pre-tax and after-tax dollars as equivalent.
- Invent values, the factor list, or tax rates.
- Allocate an indivisible asset without an offset or buyout mechanism.
- Present a single number as the only outcome where the law is discretionary.
- Insert generic "consult counsel" disclaimers.

---

## Instructions

1. **Division standard.** State equal-division or the equitable-distribution factors and the target split with justification.
2. **Build the schedule.** Two columns (Party A / Party B); list every marital asset and debt with value; allocate each.
3. **Net each side.** Total assets minus debts for each party.
4. **Tax/liquidity adjustment.** Note where after-tax or liquidity-adjusted values change the real split; show adjusted nets if material.
5. **Equalization.** Compute the payment or offsetting transfer to reach the target; identify the source of the payment.
6. **Indivisible assets.** Propose buyout/refinance/sale mechanics for the home, business, and pension (cross-reference QDRO framework).
7. **Separate property.** Set aside confirmed separate property to the owner.
8. **Settlement vs. litigation.** Compare the proposal to the likely litigated range; note cost and risk.

---

## Output Format

```markdown
# PROPERTY DIVISION PROPOSAL — Case No. {____}
**State / regime:** {…}   **Standard:** {equal / equitable factors [NEED FACTOR LIST]}   **Target:** {50/50 or {%} with justification}

## A. Division Schedule (marital/community estate)
| Asset/Debt | Value | Tax basis / note | To Party A | To Party B |
|---|---|---|---|---|
| {Residence equity} | {$} | {basis/gain} | {$} | |
| {Retirement (pre-tax)} | {$} | {after-tax ≈ $} | | {$} |
| {Debt} | ({$}) | | ({$}) | |
| **Net allocation** | | | **{$}** | **{$}** |

## B. Tax/Liquidity-Adjusted Nets (if material)
- Party A effective: {$} ; Party B effective: {$}

## C. Equalization
- To reach {target}, Party {X} pays Party {Y} {$}, sourced from {…}.

## D. Indivisible Assets
- Residence: {buyout/refinance/sale} — feasibility: {…}
- Business: {buyout/offset} — see valuation framework
- Pension/retirement: {QDRO/offset} — see QDRO framework

## E. Separate Property Set Aside
- To Party A: {…} ; To Party B: {…}

## F. Settlement vs. Litigation
- Likely litigated range: {…} ; trial cost/risk: {…} ; recommendation: {…}
```

---

## Verification

- [ ] Division standard correct for the state; factors applied where equitable distribution governs.
- [ ] Every marital asset and debt allocated; each party's net computed.
- [ ] Confirmed values used; unvalued items flagged.
- [ ] Tax basis/liquidity reflected; pre-tax vs. after-tax not treated as equal.
- [ ] Equalization payment computed with a funding source.
- [ ] Indivisible assets handled with buyout/offset mechanics.
- [ ] Separate property set aside to the owner.
- [ ] Settlement-vs-litigation comparison included with a range.
- [ ] No invented values, factor lists, or tax rates.

---

## False-Positive Prevention

| Failure mode | Correction |
|---|---|
| Splitting 50/50 in an equitable-distribution state | Apply the state's factors and justify the target split [NEED FACTOR LIST] |
| Treating $1 of 401(k) as equal to $1 of home equity | Adjust for tax and liquidity; show effective values |
| Allocating the house or business with no buyout/offset | Provide refinance/buyout/sale mechanics and feasibility |
| Using estimated values as final | Flag [NEED VALUATION]; use confirmed values only |
| Presenting one number where the law is discretionary | Show the likely litigated range and trial risk |
| Folding separate property into the divisible estate | Set aside confirmed separate property to the owner |
| Ignoring reimbursement/equitable claims from characterization | Carry those claims into the net allocations |
| Equalization payment with no identified source | Identify how the paying party funds it |
| Inventing tax rates or built-in gain | Flag tax items for the tax-consequences analysis |
| Ignoring debt allocation | Allocate debts as well as assets in each party's net |
