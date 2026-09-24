---
title: "Comparative Market Analysis — Comp Selection, Line-Item Adjustments, and a Reconciled Range Built Only from Sales You Supplied"
category: specialized-fields/real-estate
description: "Build a comparative market analysis for one residential property from sales data the user supplies: screen comps against stated selection rules, adjust each comp line by line toward the subject with a stated rate and source, flag comps whose net or gross adjustments are too large to trust, reconcile a weighted value range, and read actives and pendings as competition rather than value — distinct from listing copy (domain_writing_realtor_listing), from public-equity trading comps, and from a licensed appraisal, which this is not."
techniques:
  - RT-23
  - DS-01
  - NE-11
  - QA-04
difficulty: intermediate
tags:
  - real-estate
  - comparative-market-analysis
  - comps
  - pricing
  - listing-strategy
  - valuation
updated: "2026-09-24"
reasoning:
  styles: [analytic, quantitative, comparative]
  stakes: high
  horizon: days
  uncertainty: risk
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [real_estate_agent, buyer, seller, investor]
  mode: [diagnose, synthesize]
related_prompts:
  - domain-professional-writing/domain-specific/domain_writing_realtor_listing.md
  - domain-specialized-fields/real-estate/realestate_buyer_offer_strategy.md
  - domain-specialized-fields/real-estate/realestate_rental_property_underwriting.md
---

# Comparative Market Analysis

**Objective:** Turn a set of recent sales the user supplies into a defensible value
range for one residential property — every comp screened, every adjustment shown
with its rate and source, and the range reconciled from the comps that needed the
least adjusting.

**When to Use:**
- You are a listing agent setting a list price, or a buyer's agent (or serious
  buyer) deciding what the house is worth before writing an offer.
- A seller has a number in mind and you need to show, line by line, where it comes from.
- You pulled comps from the MLS and want the adjustments checked before they reach a client.
- **Not this prompt if** you need listing copy — use
  `domain-professional-writing/domain-specific/domain_writing_realtor_listing.md`,
  which consumes this range. For income property, value comes from the rent roll —
  use `realestate_rental_property_underwriting.md`. Public-company comparables are
  `domain-finance/valuation/finance_trading_comps_builder.md`. A lender, court or
  tax authority needs a **licensed appraisal**; this output is not one and must not
  be presented as one.

## Inputs / Context

1. **Subject property:** address or area, property type, GLA (above-grade living
   area), beds/baths, year built, lot, garage, condition, notable features.
2. **Closed sales** — ideally from an MLS export: sale price, sale date, GLA, beds,
   baths, garage, lot, condition notes, distance, and **seller concessions**.
3. **Active and pending listings** in the same search, with list price and days on market.
4. **Adjustment rates** you use (per sq ft of GLA, per bath, per garage bay, condition,
   time). If you have none, the prompt proposes rates labelled `[estimate]` with the
   derivation you must confirm.
5. **Purpose:** list-price setting, offer ceiling, or a seller conversation.

If fewer than three closed sales are supplied, stop and say what search to widen
(time, radius, or GLA band) — never fill the gap with remembered or plausible sales.

## Method

1. **Tag every data point by provenance (RT-23).**
   `[MLS]` user's MLS export · `[user]` stated by the user · `[public-record]`
   county record the user pasted · `[estimate]` a rate or figure this prompt
   proposed. No sale enters the analysis without one of the first three tags.

2. **Screen comps against stated rules (DS-01).** Default rules, overridable:
   sold within 6 months; within 1 mile (urban: 0.5); same property type and style;
   GLA within ±20% of subject; arm's-length (exclude estate, foreclosure, family,
   and off-market sales unless the market is dominated by them). Every rejected sale
   is listed with the rule it failed — a comp dropped silently is a thumb on the scale.

3. **Adjust each comp toward the subject.** Comp superior → subtract; comp inferior
   → add. One line per difference: feature, difference, rate, amount, rate source.
   Always check **concessions** (subtract seller-paid concessions from the comp) and
   **time** (apply the market trend per month since sale, only if the user supplied
   a trend).

4. **Compute and police the adjustments (NE-11).**
   - `Adjusted price = sale price + Σ adjustments`
   - `Net % = Σ adjustments ÷ sale price`; `Gross % = Σ |adjustments| ÷ sale price`
   - Flag any comp with net > 15% or gross > 25% as **low-weight**; it is telling
     you it is not comparable.

5. **Reconcile, don't average.** Weight comps by similarity: fewest and smallest
   adjustments, closest, most recent. State each weight and why. Report the
   weighted point value, the full adjusted range, and the **tight range** from the
   best two or three comps.

6. **Read the competition.** Actives and pendings are *not* value evidence — their
   prices are asks. Use them for: months of inventory (actives ÷ monthly sales pace),
   where the subject would sit in the current shelf, and how long overpriced
   listings have sat.

7. **Grade confidence (QA-04).** High: ≥3 comps with gross ≤10%, all `[MLS]`.
   Medium: 3 comps with one low-weight, or a rate is `[estimate]`. Low: any key
   rate is `[estimate]` and comps are thin or old. Name what would raise it.

8. **Translate for purpose.** Listing: a list-price band and the pricing trade-off.
   Buyer: the value range as an input to the offer ceiling, never as the ceiling.

## Output Format

```
# CMA — [subject] — as of [date] — purpose: [list | offer | conversation]

## Subject
[type, GLA, beds/baths, year, lot, garage, condition]

## Comp screen
| Sale | Price | Date | GLA | Dist | Source | Used? | Rule failed |

## Adjustment grid
| Feature | Rate (source) | C1 | C2 | C3 | C4 |
Net adj / Net % / Gross %   Adjusted price   Low-weight?

## Reconciliation
| Comp | Adjusted | Weight | Why |
Weighted point: $[..]   Full range: $[..]–$[..]   Tight range: $[..]–$[..]

## Competition (asks, not value)
Actives: [n, price band, DOM]   Pendings: [n]   Months of inventory: [n]

## Confidence
[High | Medium | Low] — [why] — raise it by: [..]

## Recommendation for purpose
[list band and trade-off | offer-ceiling input]

## Not an appraisal
[one-line statement]
```

## Verification

- [ ] Every sale used carries `[MLS]`, `[user]` or `[public-record]`; none is invented.
- [ ] Every rejected sale names the rule it failed.
- [ ] Each adjustment has a direction consistent with superior → subtract.
- [ ] Adjusted prices, net % and gross % are recomputed from the grid and match.
- [ ] Weights sum to 100%, and the point value is recomputed from them.
- [ ] Concessions and time are either adjusted or explicitly "none supplied".
- [ ] Active list prices appear only in the competition section.

## False-Positive Prevention

1. **Price per square foot is not a CMA.** Multiplying the subject's GLA by an
   area average ignores every feature difference; the grid exists to prevent it.
2. **The GLA rate is not the average $/sq ft.** Marginal square footage is worth a
   fraction of the average (land, kitchen and baths are already paid for). Using
   the full average overstates every size adjustment.
3. **A non-arm's-length sale drags the range.** An estate or foreclosure sale well
   below the cluster is a different transaction, not a signal the market dropped.
4. **Concessions hide in the sale price.** $489,000 with $5,000 seller-paid is a
   $484,000 house; unadjusted, it inflates the range.
5. **An active listing is a hope.** Pricing to the highest active is pricing to
   someone else's unsold ask.
6. **A big adjusted comp is a warning, not a data point.** A comp that needed 25%
   gross adjustment agrees with the answer only because you made it agree.
7. **Remembered or "typical" comps are fabrication.** If the user did not supply
   it, it is not in the grid.
8. **"Market value" language is appraisal language.** Say "indicated range"; the
   word *appraisal* appears only to say this is not one.

## Example Output

```
# CMA — 3-bed ranch, Linden Ave area — as of 2026-09-24 — purpose: offer

## Subject
Single-level ranch, 1,640 sf GLA, 3 bd / 2 ba, 1978, 0.22 ac, 2-car attached,
average condition (original kitchen, roof 2019) [user]

## Comp screen
| C1 | $462,000 | 2026-08-14 | 1,580 | 0.3 mi | [MLS] | Yes | — |
| C2 | $489,000 | 2026-07-02 | 1,720 | 0.5 mi | [MLS] | Yes | — ($5,000 seller concession) |
| C3 | $448,000 | 2026-06-20 | 1,610 | 0.4 mi | [MLS] | Yes | — |
| C4 | $515,000 | 2026-04-10 | 1,900 | 0.8 mi | [MLS] | Yes | — (GLA +16%, at edge) |
| R1 | $395,000 | 2026-07-30 | 1,650 | 0.2 mi | [MLS] | No | Estate sale, as-is — not arm's-length |
| R2 | $505,000 | 2026-08-01 | 1,700 | 1.1 mi | [MLS] | No | Two-storey; beyond radius |

## Adjustment grid
| Feature | Rate (source) | C1 | C2 | C3 | C4 |
| GLA | $110/sf [estimate: ~40% of $285 avg $/sf; confirm by paired sale] | +6,600 | −8,800 | +3,300 | −28,600 |
| Baths | $8,000 per half bath [estimate] | — | — | +8,000 (1.5 ba) | — |
| Garage | $12,000 per bay [user] | — | — | +12,000 (1-car) | — |
| Bedrooms | $5,000 [user] | — | — | — | −5,000 (4 bd) |
| Condition | $20,000 updated kitchen [user] | — | −20,000 | — | — |
| Concession | dollar-for-dollar | — | −5,000 | — | — |
| Time | +0.25%/mo [user: MLS median trend] | +1,155 (1 mo) | +3,668 (3 mo) | +3,360 (3 mo) | +6,438 (5 mo) |
| Net adj | | +7,755 | −30,132 | +26,660 | −27,162 |
| Net / Gross % | | 1.7 / 1.7 | −6.2 / 7.7 | 6.0 / 6.0 | −5.3 / 7.8 |
| Adjusted | | $469,755 | $458,868 | $474,660 | $487,838 |
None exceeds 15% net / 25% gross; C4 down-weighted for size and age of sale.

## Reconciliation
| C1 | $469,755 | 40% | Fewest adjustments, most recent |
| C3 | $474,660 | 25% | Close in GLA; three mechanical adjustments |
| C2 | $458,868 | 20% | Condition adjustment is the largest judgment call |
| C4 | $487,838 | 15% | GLA at edge of band; 5 months old |
Weighted point: $471,516 → $471,500   Full range: $458,900–$487,800
Tight range (C1, C3): $469,800–$474,700

## Competition (asks, not value)
Actives: 3 at $469,000–$499,000, DOM 12–41; the $499,000 listing has sat 41 days.
Pendings: 1 at list $479,900 (sale price unknown — not a comp).
Months of inventory: 6 closed sales in the search in 6 months = 1.0/mo; 3 actives → 3.0 months.

## Confidence
Medium — four arm's-length [MLS] comps, but the GLA and half-bath rates are
[estimate]. Raise it by: one paired-sale check of the GLA rate from the same MLS pull.

## Recommendation for purpose
Indicated value ~$471,500 (tight $469,800–$474,700). Listing is at $479,900 with
3.0 months of inventory: an offer above ~$475,000 is paying for competition, not
value — a decision for realestate_buyer_offer_strategy, with an appraisal likely
near the point value.

## Not an appraisal
An indicated range from user-supplied sales, not a licensed appraisal or a
lender's valuation.
```

## Techniques Used

- **RT-23 Input Provenance Tagging** — every sale and rate carries its source; none is remembered.
- **DS-01 Framework Application** — the sales-comparison grid with explicit screen rules.
- **NE-11 Embedded Calculation Formulas** — adjusted price, net and gross %, weighted point.
- **QA-04 Uncertainty Acknowledgment** — graded confidence and the one datum that raises it.

## Related Prompts

- `domain-professional-writing/domain-specific/domain_writing_realtor_listing.md` —
  the listing copy that follows a list-price decision.
- `domain-specialized-fields/real-estate/realestate_buyer_offer_strategy.md` —
  turns this range into an offer package, escalation cap and appraisal-gap exposure.
- `domain-specialized-fields/real-estate/realestate_rental_property_underwriting.md` —
  for income property, where the rent roll, not comps, drives value.
