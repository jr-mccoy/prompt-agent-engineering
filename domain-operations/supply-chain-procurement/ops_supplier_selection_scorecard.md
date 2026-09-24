---
title: "Supplier Selection Scorecard — Weighted Criteria, Total Cost of Ownership, Supply Risk, and the Dual-Sourcing Call"
category: operations/supply-chain-procurement
description: "Choose among competing suppliers for a recurring material or service: fix weighted criteria and anchored 1–5 scales before scoring, compute landed total cost of ownership rather than unit price, score supply risk explicitly, test whether the winner survives a change in weights, and decide single, dual, or split sourcing with the premium stated."
techniques:
  - DP-03
  - RT-02
  - NE-11
  - QA-02
difficulty: intermediate
tags:
  - supplier-selection
  - sourcing
  - total-cost-of-ownership
  - weighted-scorecard
  - dual-sourcing
  - supply-risk
updated: "2026-09-24"
related_prompts:
  - domain-operations/supply-chain-procurement/ops_rfp_procurement_package.md
  - domain-operations/supply-chain-procurement/ops_inventory_reorder_policy.md
  - domain-business-strategy/research/research_vendor_evaluation.md
---

# Supplier Selection Scorecard

**Objective:** Produce a defensible supplier choice for a recurring purchase — a
weighted scorecard on anchored scales, a TCO comparison that reveals what unit price
hides, an explicit supply-risk view, a sensitivity test, and a sourcing split with its
cost.

**When to Use:**
- Two or more suppliers can provide the same part, material, or recurring service,
  and the cheapest quote is not obviously the best.
- A single-source supplier has failed you once and you are considering a second.
- The choice must be explained to finance, quality, or an auditor.
- You have RFP responses and need to turn them into a decision.
- **Not this prompt if** you are deciding whether to buy **one product or software
  vendor** for a specific situation — use
  `domain-business-strategy/research/research_vendor_evaluation.md`. If the decision is
  made and you are negotiating terms, use
  `domain-negotiation/contexts/negotiation_vendor_procurement_buyside.md`. For a bank
  relationship, use
  `domain-finance/treasury-capital-markets/finance_bank_relationship_rfp_framework.md`.

## Inputs / Context

1. **What is being sourced**: spec, annual volume, criticality to operations.
2. **Candidate suppliers** and their quotes: unit price, MOQ, lead time, terms,
   Incoterms/freight basis.
3. **Performance evidence**: sample or trial defect rates, on-time delivery history,
   references, audit results.
4. **Cost drivers beyond price**: freight, duties, inspection, defect handling cost
   per unit, carrying cost rate, admin/onboarding.
5. **Risk information**: financial health, number of plants, geography, capacity
   headroom, dependence on you (your share of their revenue).
6. **Your priorities**, before looking at the quotes.

## Method

1. **Fix criteria, weights, and anchors first (DP-03).** Choose 4–6 criteria that
   matter for *this* item. Assign weights summing to 100%. Write a 1–5 anchor for each
   score level in observable terms ("5 = on-time ≥98% over 6 months of history").
   Record them before scoring; weights set after seeing scores are reverse-engineered.
2. **Build landed TCO per unit (NE-11).**
   `TCO = price + freight/duty + (defect rate × cost per defect) + carrying cost
   (from MOQ and lead-time-driven stock) + admin/onboarding amortized`.
   Show each component; multiply by annual volume.
3. **Score each supplier on each criterion (RT-02)** against the anchors, with the
   evidence cited. Cost scores come from TCO, not unit price.
4. **Assess supply risk explicitly.** Single site, single geography, thin finances,
   capacity already committed, sub-tier dependence. Risk is a criterion *and* an
   input to the sourcing decision.
5. **Sensitivity test (QA-02).** Shift the top two weights by ±10 points. If the
   winner changes, or the margin is within ~0.2 on a 5-point scale, treat it as a tie
   and decide on sourcing strategy and risk, not the decimal.
6. **Decide the sourcing split.** Single source (simplest, most leverage per unit),
   dual source (primary/secondary share), or split award. State the premium of
   dual-sourcing in currency and what it buys (qualified backup, competitive tension).
7. **Qualification gates.** What must be true before first order: sample approval,
   quality agreement, capacity confirmation. Safety-critical or regulated items
   require qualification by the qualified quality/regulatory owner.

## Output Format

```
# Supplier selection — [item]   Annual volume: [..]   Criticality: [..]

## Criteria and anchors (fixed before scoring, date: [..])
| Criterion | Weight | 1 = | 3 = | 5 = |

## TCO per unit
| Component | Supplier A | Supplier B | Supplier C |
Annual TCO: [..]

## Scorecard
| Criterion | Weight | A | B | C | Evidence |
Weighted total: A [..]  B [..]  C [..]

## Supply risk
| Supplier | Key risks | Mitigation |

## Sensitivity
[weight changes tested → winner stable? margin?]

## Sourcing decision
[single | dual (share) | split] — premium: [..]/yr — buys: [...]

## Qualification gates before first PO
```

## Verification

- [ ] Weights sum to 100% and are dated before scoring.
- [ ] Every score level has an observable anchor.
- [ ] TCO components are shown and multiply correctly to annual.
- [ ] Cost scores are based on TCO, not unit price.
- [ ] Each score cites evidence; missing evidence is scored conservatively and flagged.
- [ ] Sensitivity test is reported with the margin.
- [ ] Dual-sourcing premium is stated in currency.

## False-Positive Prevention

1. **Unit price as cost.** The lowest quote often carries higher freight, larger
   MOQs, longer lead times (more safety stock), or more defects.
2. **Weights tuned to a favourite.** Weights set after reading proposals tend to
   produce the answer someone wanted. Fix and date them first.
3. **Precision from soft scores.** A 4.35 vs 4.25 difference on judgment scores is
   noise. Say "tie" and decide on risk and strategy.
4. **Supplier-reported quality as measured.** A quoted "99.8% quality" is a claim;
   your trial or incoming inspection data is evidence. Label which is which.
5. **Ignoring your share of their business.** Being 40% of a small supplier's revenue
   is a risk to both parties.
6. **Dual-sourcing as free insurance.** It costs volume leverage, qualification
   effort, and a price premium; state it.
7. **Unqualified approval of regulated items.** Food-contact, medical, aerospace, or
   safety components need formal qualification by the responsible quality function.

## Example Output

```
# Supplier selection — Corrugated shipping cartons (non-food-contact)
Annual volume: 600,000   Criticality: high (no ship without carton)

## Criteria and anchors (fixed 2 Sep)
| TCO        | 35% | >10% above lowest | 5–10% above | ≤2% above lowest (5); 2–5% (4) |
| Quality    | 25% | defect >3%       | 1–2%        | ≤0.5% on trial lot            |
| Delivery   | 20% | LT >6 wk / OTD <90% | LT 3–4 wk | LT ≤2 wk and OTD ≥98%       |
| Risk       | 10% | single site, weak finances | single site, stable | 2+ sites, stable |
| Service    | 10% | no VMI, slow response | responsive | VMI + 24 h response        |

## TCO per unit
| Component            | A      | B       | C       |
| Price                | 0.420  | 0.380   | 0.450   |
| Freight              | 0.030  | 0.060   | 0.020   |
| Defects (rate×$0.50) | 0.005 (1%) | 0.0125 (2.5%) | 0.0025 (0.5%) |
| Carrying (MOQ/LT)    | 0.010  | 0.025   | 0.008   |
| TCO                  | 0.465  | 0.4775  | 0.4805  |
Annual TCO: A $279,000   B $286,500   C $288,300   (B: lowest price, not lowest cost)

## Scorecard
| TCO      | 35% | 5 | 4 (+2.7%) | 4 (+3.3%) | TCO table |
| Quality  | 25% | 4 | 3         | 5         | trial lots of 2,000 |
| Delivery | 20% | 4 | 2         | 5         | 6 mo OTD history; B LT 6 wk |
| Risk     | 10% | 3 | 3         | 4         | C has 2 plants |
| Service  | 10% | 4 | 3         | 3         | references |
Weighted total: A 4.25   B 3.15   C 4.35

## Supply risk
A: single plant 80 miles away; B: long lead time, 30% of its capacity would be ours;
C: two plants, stable financials.

## Sensitivity
Base: C +0.10. TCO 45% (−5 Risk, −5 Service): A 4.40, C 4.40 → tie.
TCO 25% / Quality 35%: C 4.45, A 4.15. Margin is small and weight-dependent → no
robust winner on score alone; decide on risk and sourcing. B last in every test.

## Sourcing decision
Dual: C primary 65%, A secondary 35%. Blended TCO 0.4751 → $285,045/yr vs single-A
$279,000 → premium $6,045/yr buys a qualified backup and ongoing price tension.

## Qualification gates before first PO
Approved samples at both; quality agreement with defect chargeback; capacity
confirmation for 100% volume at either supplier within 4 weeks' notice.
```

## Techniques Used

- **DP-03 Anchored Scoring Scales** — observable anchors fixed before scoring.
- **RT-02 Multi-Dimensional Analysis Framework** — cost, quality, delivery, risk, service scored separately.
- **NE-11 Embedded Calculation Formulas** — landed TCO and blended dual-source cost.
- **QA-02 Adversarial Stress-Test** — weight sensitivity to expose a false winner.

## Related Prompts

- `ops_rfp_procurement_package.md` — running the competitive process that produces the bids.
- `ops_inventory_reorder_policy.md` — how the chosen lead time and MOQ set stock levels.
- `domain-business-strategy/research/research_vendor_evaluation.md` — single product/vendor decisions.
- `domain-negotiation/contexts/negotiation_vendor_procurement_buyside.md` — negotiating terms after selection.
