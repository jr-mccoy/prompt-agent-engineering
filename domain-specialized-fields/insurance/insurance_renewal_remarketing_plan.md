---
title: "Broker Renewal and Remarketing Plan — Renewal Outlook, the Remarket-or-Renew Decision, Market Approach, and a Backward-Scheduled Timeline"
category: specialized-fields/insurance
description: "For a commercial insurance broker planning a client's renewal: build the renewal outlook from exposure change, loss development and market conditions as probability-weighted scenarios, decide whether to renew with the incumbent, remarket selectively, or go to full market (with the cost of market fatigue and incumbent relationship stated), choose which markets see which lines, and schedule backward from the effective date with client decision points — distinct from assembling the submission itself and from the client's own coverage-gap review (finance_business_insurance_coverage_review)."
techniques:
  - NE-10
  - NE-11
  - DP-07
  - NE-17
difficulty: intermediate
tags:
  - insurance-renewal
  - remarketing
  - insurance-broker
  - market-strategy
  - commercial-insurance
  - renewal-timeline
  - premium-going-up
  - shop-insurance-at-renewal
  - stay-with-current-insurer
updated: "2026-10-02"
reasoning:
  styles: [strategic, quantitative, procedural]
  stakes: high
  horizon: months
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [insurance_broker, account_executive, account_manager]
  mode: [plan, decide, communicate]
related_prompts:
  - domain-specialized-fields/insurance/insurance_commercial_submission_builder.md
  - domain-specialized-fields/insurance/insurance_underwriting_risk_assessment.md
  - domain-professional-writing/domain-specific/domain_writing_insurance_comparison.md
---

# Broker Renewal and Remarketing Plan

**Objective:** Give the client a renewal they can budget for and a broker team a plan
they can execute: what the renewal is likely to cost and why, whether testing the
market is worth what it costs, which markets see which lines, and a dated timeline
that leaves time for the client to decide before the policy lapses.

**When to Use:**
- 120–150 days before a commercial renewal, at the stewardship or pre-renewal meeting.
- The incumbent has signalled a large increase, reduced capacity or new restrictions.
- The client has asked "should we shop this?" and you need a reasoned answer.
- Losses, a change in operations or a hard market make the outcome uncertain.
- **Not this prompt if** you are assembling the underwriting submission itself —
  `domain-specialized-fields/insurance/insurance_commercial_submission_builder.md`.
  Presenting received quotes to the client as a comparison document is
  `domain-professional-writing/domain-specific/domain_writing_insurance_comparison.md`.
  A business owner reviewing whether its cover fits its exposures is
  `domain-finance/risk-management/finance_business_insurance_coverage_review.md`.
  This prompt does not forecast specific carriers' rates from memory: market
  conditions come from the user's own market intelligence.

## Inputs / Context

1. **Expiring program**: lines, carriers, limits, retentions, premiums, effective date,
   any multi-year or minimum-premium terms.
2. **Change since last year**: exposures (revenue, payroll, TIV, vehicles), new
   operations or locations, contracts requiring new cover.
3. **Losses**: current loss runs and large-loss status.
4. **Market intelligence** the broker has: incumbent's renewal indication, rate trends
   by line from the broker's own placements or market surveys, appetite changes.
5. **Client priorities**: budget ceiling, retention tolerance, relationship with the
   incumbent, claims-service history, desire for stability.
6. **Previous marketing history**: which markets saw the account and when, and their
   responses (declined, quoted, terms).

All market figures are tagged `[broker data]`, `[market survey]`, `[incumbent
indication]` or `[estimate]`.

## Method

1. **Renewal outlook (NE-10, NE-11).** Per line:
   `Renewal premium ≈ expiring × (current exposure / prior exposure) × (1 + rate change)`.
   Build three scenarios — favourable, expected, adverse — with probabilities that sum
   to 100% and a weighted expected premium; explain what drives each (loss
   development, market trend, a large loss, capacity).
2. **Remarket-or-renew decision.** Compare:
   - **Renew with incumbent** — when the indication is within the expected range,
     service is good and the account was marketed recently.
   - **Selective remarketing** — specific lines or 2–4 targeted markets, when one
     line is out of line or a capacity gap has appeared.
   - **Full marketing** — when the incumbent has non-renewed, restricted terms
     materially, or the outlook is far above the market.
   State expected saving or improvement, and the costs: broker and client time,
   underwriter fatigue if the account is shown every year, risk of the incumbent
   hardening, and the loss of continuity credit on long-tail lines.
3. **Failure modes before choosing (DP-07).** For the chosen route, how it goes
   wrong: markets decline late, the incumbent withdraws its indication, the
   submission is incomplete, the client decides after the binding deadline.
4. **Market approach.** Which markets per line and why (appetite, class, capacity,
   claims reputation); lead and excess structure for umbrella towers; which markets
   are reserved for later years to avoid fatigue.
5. **Backward timeline.** From effective date: bind (−5 days), client decision
   (−10 to −14), proposal (−21), quotes due (−30 to −35), submission to market
   (−60 to −75 for complex accounts), data collection (−90 to −120), pre-renewal
   meeting (−120 to −150). Adjust for line complexity and any notice periods the
   policy or local rules require.
6. **Client decision close (NE-17).** The decisions the client must make, by date:
   retention changes, limit changes, budget approval, go/no-go on remarketing.

## Output Format

```
# Renewal plan — [client]   Effective: [..]   Expiring premium: [..]

## Changes since last year
| Item | Prior | Current | Effect on premium |

## Renewal outlook
| Line | Expiring | Favourable (p) | Expected (p) | Adverse (p) | Weighted |
Drivers: [..]

## Decision: renew / selective remarket / full market
Expected benefit: [..]   Costs and risks: [..]   Why not the alternatives: [..]

## Failure modes and mitigations

## Market approach
| Line | Incumbent | Markets approached | Why | Reserved for later |

## Timeline (backward from effective date)
| Date | Day | Milestone | Owner |

## Client decisions needed
| Decision | Options | Needed by |
```

## Verification

- [ ] Scenario probabilities sum to 100% and the weighted premium recomputes.
- [ ] Exposure change and rate change are shown separately.
- [ ] Every market-trend figure carries a source tag; none is recalled as fact.
- [ ] The decision states its cost and the reason the alternatives were not chosen.
- [ ] The timeline runs backward from the effective date and includes client decision dates.
- [ ] Markets shown in the last two years are noted to manage fatigue.

## False-Positive Prevention

1. **Rate change as premium change.** A flat premium on 15% more exposure is a rate
   decrease; report both.
2. **Shopping as free.** Every remarketing costs time and goodwill; markets that
   decline the same account each year stop looking at it.
3. **Incumbent indication as final.** Early indications move once updated losses
   arrive; treat as one scenario input.
4. **Market averages as this account.** Survey rate trends describe a portfolio;
   this account's losses and class may differ.
5. **Late start.** Complex accounts that go to market 30 days out get fewer and
   worse quotes; the timeline is the plan.
6. **Price over continuity.** Moving long-tail lines (e.g. claims-made liability)
   can create gaps in prior-acts coverage; flag for the client and specialist review.

## Example Output

```
# Renewal plan — Harbor Fabrication LLC   Effective: 1 Jan 2027
Expiring premium: $412k (property $138k, GL $96k, auto $44k, WC $118k, umbrella $16k)

## Changes since last year
| Sales | $18.2 M | $21.5 M | GL exposure +18% |
| Payroll | $4.1 M | $4.6 M | WC exposure +12% |
| Vehicles | 9 | 11 | auto +22% |
| TIV | $13.0 M | $16.8 M (Plant 1 appraisal) | property exposure +29% |

## Renewal outlook
| WC | $118k | $125k (25%) | $140k (50%) | $160k (25%) | $141k |
| Property | $138k | $172k (30%) | $185k (50%) | $205k (20%) | $185k |
| GL+auto+umb | $156k | $170k (30%) | $182k (50%) | $195k (20%) | $181k |
Weighted total ≈ $507k (+23%), of which ~20 pts exposure, ~3 pts rate.
Drivers: TIV correction; incumbent WC indication +19% after the 2024 large loss
[incumbent indication]; property rates in this class flat to +5% [broker data].

## Decision: selective remarketing (WC and property only)
GL/auto/umbrella: incumbent indication +16% on +18–22% exposure → renew.
WC: 3 markets with fabrication appetite; expected saving $10–20k if the 2024
loss is accepted as remediated. Property: 2 markets for Plant 2 (unsprinklered).
Not full market: account last fully marketed in 2025; reshowing all lines risks fatigue.

## Failure modes
2022 WC loss run missing → markets wait → request now, due 25 Oct.
Incumbent withdraws package credit if WC moves → ask incumbent to quote
monoline and package both.

## Timeline
| 2 Oct | −91 | Pre-renewal meeting; data request (late vs −120 target → compressed) | AE / client |
| 25 Oct | −68 | Data complete; submission finalised | AM |
| 1 Nov | −61 | WC and property to market | AE |
| 1 Dec | −31 | Quotes due | markets |
| 10 Dec | −22 | Proposal to client | AE |
| 18 Dec | −14 | Client decision | client CFO |
| 26 Dec | −6 | Bind; certificates issued | AM |

## Client decisions needed
| WC retention: guaranteed cost vs $25k deductible | quote both | 18 Dec |
| Budget approval at ~$507k expected ($467–560k scenario range) | — | 15 Nov |
```

## Techniques Used

- **NE-10 Probability-Weighted Scenarios** — favourable / expected / adverse renewal outcomes with weights.
- **NE-11 Embedded Calculation Formulas** — premium separated into exposure and rate change and recomputed per line.
- **DP-07 Failure Mode Prediction** — how the chosen marketing route fails, with mitigations, before committing.
- **NE-17 Call-to-Action Mandatory Close** — client decisions listed with options and dates.

## Related Prompts

- `domain-specialized-fields/insurance/insurance_commercial_submission_builder.md` — the submission the remarketed lines go out on.
- `domain-specialized-fields/insurance/insurance_underwriting_risk_assessment.md` — how each market will assess the account.
- `domain-professional-writing/domain-specific/domain_writing_insurance_comparison.md` — presenting the quotes to the client.
