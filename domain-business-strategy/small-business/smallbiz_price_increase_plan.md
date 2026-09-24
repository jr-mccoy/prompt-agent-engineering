---
title: "Price Increase Plan — How Much, How Many Customers You Can Afford to Lose, and How to Tell Them"
category: business-strategy/small-business
description: "Plan a price increase for a local shop, trades business or freelance practice — the price needed to recover documented cost increases, the break-even customer loss at the new price, sequencing by customer segment, notice and wording, staff answers to pushback, and a rollback trigger watched for eight weeks; distinct from services_pricing_model_selector (choosing a billing structure for consulting work), monetization_pricing_strategy (app and SaaS tiers) and advocacy_price_increase_retention_request (the customer's side of the same letter)."
techniques:
  - NE-11
  - RT-05
  - DP-11
  - NE-23
  - QA-02
difficulty: intermediate
tags:
  - small-business
  - pricing
  - price-increase
  - customer-communication
  - margins
  - retention
updated: "2026-09-24"
related_prompts:
  - domain-business-strategy/client-services/services_pricing_model_selector.md
  - domain-business-strategy/startup/monetization_pricing_strategy.md
  - domain-written-advocacy/accounts-and-billing/advocacy_price_increase_retention_request.md
---

# Price Increase Plan

**Objective:** Give a small-business owner a price increase they can defend with their
own numbers — the size that restores margin, the number of customers they could lose
and still be better off, the order in which customers see it, the words they will
hear, and the signal that would make them pause.

**When to Use:**
- Costs have risen and prices have not, and the margin is visibly thinner.
- You have not raised prices in two or more years and are nervous about regulars.
- You are fully booked with a waitlist — demand is telling you something.

**Not this prompt if:**
- You are choosing *how* to charge for consulting or freelance work (hourly, day
  rate, fixed, retainer) — `domain-business-strategy/client-services/services_pricing_model_selector.md`
  and the rate floor in `domain-finance/corporate-finance-fpa/finance_services_rate_floor_model.md`.
- You are pricing an app or SaaS product with tiers and trials —
  `domain-business-strategy/startup/monetization_pricing_strategy.md`.
- You are the customer writing to ask for a better rate —
  `domain-written-advocacy/accounts-and-billing/advocacy_price_increase_retention_request.md`.

## Inputs

1. Current prices for your main products or services, and monthly volume of each.
2. Variable cost per unit (materials, direct labour share) — now and a year ago.
3. Fixed cost changes (rent, insurance, software) with amounts.
4. Customer mix: new vs regular; any prepaid packages, contracts or memberships.
5. Demand signals: waitlist, booking lead time, how often customers mention price.
6. What nearby competitors charge, if you know — marked with how you know.

## Method

1. **Document the reason (RT-05).** List each cost change with its source (invoice,
   lease, wage rate). The increase must be explainable in one honest sentence.

2. **Price to stand still (NE-11).**
   `monthly squeeze = volume × (old contribution − current contribution) + fixed-cost increase`
   `price to stand still = old price + squeeze ÷ volume`
   Round up to a price that reads naturally.

3. **Break-even customer loss at the proposed price.**
   `max volume loss = increase % ÷ (current contribution margin % + increase %)`
   Compare with a realistic loss estimate from your own signals. If your realistic
   loss is well under the break-even, the increase is safe even if you are wrong by a
   margin.

4. **Stress-test (QA-02).** Re-run profit at 2×, and at the break-even, of your
   expected loss. State the monthly result at each.

5. **Sequence by segment (DP-11).**
   - **New customers first:** the new price from day one — a low-risk test of demand.
   - **Regulars next:** after notice (commonly four to six weeks), in person where
     possible, then in writing.
   - **Prepaid, contracted or member customers:** honour existing terms until they end;
     check contract and notice terms, and any legal notice requirements, with an adviser.

6. **Write the words (NE-23).** A notice (short, dated, one reason, thanks), a
   counter or front-desk line, and answers to the three most likely objections —
   "why?", "that's a lot", "I'll go elsewhere". No apology spiral, no discount-on-demand.

7. **Watch and set a rollback trigger.** Weekly for eight weeks: bookings, new-customer
   conversion, regulars' rebook rate. Name the threshold that pauses the plan.

## Output Format

```
# Price increase plan — [business], effective [dates]

## Why (documented)
| Cost change | Amount | Source |

## The numbers
Squeeze: … | Price to stand still: … | Proposed: … (+x%)
Break-even loss: … | Realistic loss estimate: … (basis)

## Stress test
| Volume loss | Monthly contribution | vs today |

## Rollout
| Segment | New price from | How told | Notice |

## Notice text / Counter line / Objection answers
## Watch list and rollback trigger
| Metric | Baseline | Pause if |
## Flags for qualified review
```

## Verification

- [ ] Every cost change has a source.
- [ ] Break-even loss is computed from contribution margin, not revenue.
- [ ] The stress test includes a case at 2× expected loss.
- [ ] Prepaid and contracted customers are handled on their existing terms.
- [ ] A numeric rollback trigger is set before launch.

## False-Positive Prevention

1. **Matching competitors is not a reason.** Your costs and your demand are; a
   competitor's price is context, marked with how you know it.
2. **Revenue margin is not contribution margin.** Break-even loss must use price
   minus variable cost; using revenue overstates how many customers you can lose.
3. **Don't raise prices on people who prepaid.** Honour packages, memberships and
   quotes already given until they end.
4. **Small, frequent is not always better than one clear step.** Several increases a
   year train customers to notice; choose deliberately and say why.
5. **No surprise at the till.** A regular discovering the new price at checkout is
   the worst version of this plan.
6. **Do not invent the loss estimate.** Base it on waitlist, lead times and past
   price reactions — or mark it `[estimate]` and lean on the break-even.
7. **Dual failure:** under-raising to avoid discomfort, then raising again in six
   months, costs more goodwill than one adequate increase.

## Example Output

```
# Price increase plan — Muddy Paws Grooming, new customers 1 Nov; regulars 1 Jan 2027

## Why (documented)
| Cost change | Amount | Source |
| Groomer wage | +$1.50/hr → +$1.50 per groom | Payroll, Jul 2026 |
| Shampoo and supplies | +$0.50 per groom | Supplier invoices |
| Rent | +$240/month | Lease renewal |

## The numbers
Standard groom $60; variable cost $24 → $26; contribution $36 → $34 (56.7%).
Volume 320 grooms/month.
Squeeze: 320 × $2 + $240 = $880/month → stand still at $60 + $2.75 = $62.75.
Proposed: $68 (+13.3%) — contribution $42.
Break-even loss: 13.3% ÷ (56.7% + 13.3%) = 19.0% → can lose 61 of 320 grooms.
Today's contribution: 320 × $34 = $10,880/month.
Realistic loss estimate: 5% — 3-week waitlist; 2 of ~300 regulars left after the
2023 increase [estimate from owner's records].

## Stress test
| Volume loss | Grooms | Contribution | vs today |
| 5% | 304 | $12,768 | +$1,888 |
| 10% (2×) | 288 | $12,096 | +$1,216 |
| 19% (break-even) | 259 | $10,878 | ≈ $0 |

## Rollout
| Segment | New price from | How told | Notice |
| New customers | 1 Nov 2026 | Website and booking page | — |
| Regulars | 1 Jan 2027 | In person at pickup, then card + email | 6 weeks (from 20 Nov) |
| 10-groom prepaid packages (38 open) | When package used up | Note on package card | — |

## Notice text
"From 1 January our standard groom will be $68. Our costs — especially what we pay
our groomers — have risen, and we want to keep paying them well. Thank you for
trusting us with your dog. — Priya"

## Objection answers
"Why?" → "Mostly groomer pay; we raised it in July." / "That's a lot." → "It's our
first change since 2023; a bath-and-tidy is still $45." / "I'll go elsewhere." →
"I understand — we'd miss you and Bella. Your next groom is at the old price if
already booked."

## Watch list and rollback trigger
| Metric | Baseline | Pause if |
| New-customer bookings/week | 11 | < 7 for 3 weeks |
| Regulars' rebook rate | 82% | < 70% for 4 weeks |

## Flags for qualified review
Written terms on prepaid packages and any notice rules for them — check with an adviser.
```

## Techniques Used

- **NE-11 Embedded Calculation Formulas:** squeeze, stand-still price, break-even loss.
- **RT-05 Evidence-Based Reasoning:** every cost change traced to a source.
- **DP-11 Safe Experiment Design:** new customers see the price first.
- **NE-23 Objection Pre-emption:** answers written before the counter conversation.
- **QA-02 Adversarial Stress-Test:** profit at 2× expected loss and at break-even.

## Related Prompts

- `domain-business-strategy/client-services/services_pricing_model_selector.md` — billing structure for services
- `domain-business-strategy/startup/monetization_pricing_strategy.md` — app and SaaS pricing
- `domain-written-advocacy/accounts-and-billing/advocacy_price_increase_retention_request.md` — the customer's side
