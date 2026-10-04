---
title: "Underwriter Risk Assessment of a Commercial Submission — Risk Quality, Pricing Adequacy Signals, Terms and Conditions, and Referral Triggers"
category: specialized-fields/insurance
description: "For a commercial lines underwriter evaluating a broker's submission: check completeness and appetite first, score risk quality on anchored scales (operations, management and controls, loss experience, property COPE, exposure trend), compute burning cost and loss-ratio signals against the indicated premium, propose terms, conditions, subjectivities and retentions tied to specific findings, and list the referral triggers that take the file beyond the underwriter's authority — distinct from a broker assembling the submission and from a lender's credit memo."
techniques:
  - DP-03
  - NE-11
  - DD-05
  - QA-02
difficulty: advanced
tags:
  - underwriting
  - commercial-insurance
  - risk-selection
  - pricing-adequacy
  - burning-cost
  - referral-authority
  - should-we-quote-this-risk
  - review-insurance-submission
updated: "2026-10-02"
reasoning:
  styles: [analytic, quantitative, adversarial, evaluative]
  stakes: high
  horizon: weeks
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [underwriter, underwriting_assistant, portfolio_manager]
  mode: [evaluate, decide]
related_prompts:
  - domain-specialized-fields/insurance/insurance_commercial_submission_builder.md
  - domain-specialized-fields/insurance/insurance_renewal_remarketing_plan.md
  - domain-finance/credit-lending/finance_credit_memo_builder.md
---

# Underwriter Risk Assessment of a Commercial Submission

**Objective:** Turn a broker's submission into an underwriting decision an authority
holder can sign: is it in appetite, how good is the risk, is the indicated premium
plausibly adequate given the losses, what terms make it acceptable, and what has to
be referred — with every judgment tied to evidence in the file.

**When to Use:**
- A new-business or renewal submission has landed and you must decide decline /
  quote / refer and on what terms.
- You are preparing a referral to a senior underwriter or an underwriting committee.
- A peer review or audit needs the rationale behind a quote written down.
- **Not this prompt if** you are the **broker** assembling the file —
  `domain-specialized-fields/insurance/insurance_commercial_submission_builder.md`.
  A lender's credit decision on the same business is
  `domain-finance/credit-lending/finance_credit_memo_builder.md`; it scores
  repayment capacity, not insurable hazard. A consumer comparing quotes is
  `domain-professional-writing/domain-specific/domain_writing_insurance_comparison.md`.
  This prompt does not set filed rates or replace the carrier's rating plan,
  underwriting guidelines or authority letter; it applies them.

## Inputs / Context

1. **The submission**: applications, exposures, loss runs (with valuation dates),
   COPE schedule, narrative, expiring program.
2. **Your guidelines**: appetite by class and hazard grade, prohibited classes,
   limit and retention authority, mandatory referral list, required inspections.
3. **Rating output**: the indicated premium from the carrier's rating plan, and any
   schedule-rating range (credits/debits) available.
4. **Third-party data** the user supplies: inspection reports, motor vehicle
   records, financial ratings, catastrophe-model output.
5. **Portfolio context**: aggregation in the zone or class, line size, reinsurance limits.

All figures carry the submission's source tag or `[NOT PROVIDED]`. Guidelines and
authority come from the user; none are assumed.

## Method

1. **Gate: completeness and appetite.** Prohibited class, hazard grade outside
   appetite, limits above authority, or a missing item the guidelines make
   mandatory (e.g. 5 years of loss runs) → stop and state decline or "awaiting
   information", with the specific item.
2. **Score risk quality on anchored scales (DP-03).** 1–5 per dimension, anchors
   written before scoring:
   - **Operations hazard** (class, processes, products, contracts).
   - **Management and controls** (safety programme, fleet controls, contractual
     risk transfer, maintenance) — evidence, not adjectives.
   - **Loss experience** (frequency trend, severity, large losses and corrective action).
   - **Property COPE** (construction, occupancy, protection, exposure; valuation credibility).
   - **Exposure trend** (growth, new operations, geographic change).
3. **Pricing adequacy signals (NE-11).**
   `Burning cost = Σ trended, developed incurred (in layer) / Σ exposure` per year;
   `Expected loss = burning cost × current exposure`;
   `Indicated loss ratio = expected loss / proposed premium`.
   Compare with the target loss ratio from the user's guidelines. Without supplied
   development and trend factors, show the unadjusted figures and say they
   understate recent years.
4. **Stress the view (QA-02).** What if the large loss recurs? What if the stale
   values are 25% light? What if exposure growth outpaces the revenue figure?
   Report the premium or terms that would still be adequate.
5. **Terms tied to findings.** Each condition answers a specific weakness:
   higher retention for frequency; a sublimit or exclusion for a specific hazard;
   protective-safeguards warranty where sprinklers carry the rating; subjectivities
   (inspection within 60 days, updated appraisal) with dates.
6. **Referral triggers (DD-05).** List every item outside authority or on the
   mandatory referral list, and anything requiring judgment beyond guidelines
   (unusual contract liability, a catastrophe-exposed aggregation). The authority
   holder decides; the assessment prepares the case.
7. **Decision.** Decline / quote as requested / quote with modified terms / refer —
   with the 2–3 reasons that decided it.

## Output Format

```
# Underwriting assessment — [insured]   Line(s): [..]   Broker: [..]   Eff.: [..]

## Gate
Appetite: [in / out — why]   Authority: [within / exceeds — item]   Missing: [..]

## Risk quality
| Dimension | Score 1–5 | Anchor met | Evidence (source) |

## Pricing adequacy
| Year | Exposure | Incurred | Burning cost | Note |
Expected loss [..]  Proposed premium [..]  Indicated LR [..] vs target [..]

## Stress tests
| Scenario | Effect on expected loss | Adequate premium / term |

## Proposed terms, conditions and subjectivities
| Term | Finding it addresses |

## Referral triggers
## Decision and reasons
```

## Verification

- [ ] The gate is applied before any scoring; out-of-appetite files stop there.
- [ ] Every score cites evidence and the anchor it meets.
- [ ] Burning cost and indicated loss ratio recompute from the rows.
- [ ] Immature years and missing development factors are stated.
- [ ] Every term or condition names the finding it addresses.
- [ ] Every item outside authority is listed as a referral, not decided.

## False-Positive Prevention

1. **Narrative as evidence.** "Strong safety culture" with no programme, dates or
   results scores as unknown, not as good.
2. **Immature years look clean.** The last 1–2 years will develop; a burning cost
   that excludes development understates expected loss.
3. **One large loss as the trend.** A single shock loss with credible corrective
   action is different from rising frequency; score frequency and severity apart.
4. **Rate-to-exposure blind spot.** A premium that rose 8% while exposure rose 18%
   is a rate cut.
5. **Conditions that do not bite.** A warranty the insured cannot meet, or a
   subjectivity with no date, adds no protection and invites disputes at claim time.
6. **Authority creep.** Quoting just above limit authority "because it's a good
   risk" is a referral item, whatever the merits.

## Example Output

```
# Underwriting assessment — Harbor Fabrication LLC   Line: workers' compensation
Broker: Coastline Risk Partners   Eff.: 1 Jan 2027

## Gate
Appetite: class 3632 = hazard group C, in appetite [guidelines].
Authority: premium within $250k authority. Missing: 2022 loss run → subjectivity.

## Risk quality
| Operations hazard | 3 | metal fab, press brakes, welding | submission |
| Management/controls | 4 | interlocks + monthly lockout audit since 2024 | narrative + loss trend |
| Loss experience | 3 | freq. 1.5→0.9–1.1; one $247k loss with corrective action | loss run 30 Sep 2026 |
| Exposure trend | 2 | payroll +12%, new trailer-frame work, 6 new welders | exposure summary |
Unweighted mean 3.0 → standard risk with a growth concern.

## Pricing adequacy
| 2023 | $4.1 M | $48k | $1.17 / $100 payroll |
| 2024 | $4.3 M | $247k | $5.74 |
| 2025 | $4.5 M | $43k | $0.96 |
3-yr burning cost (unadjusted): $338k / $12.9 M = $2.62 per $100.
Expected loss: $4.6 M × $2.62 = $120.5k. Proposed premium $131k →
indicated LR 92% vs target 65% → inadequate.
Excluding the 2024 large loss and loading a 1-in-10 shock of $150k/10 = $15k/yr:
($91k / $12.9 M) × $4.6 M = $32.4k + $15k = $47.4k → indicated LR 36%.
Truth lies between; base view sits near the high end until 2022 is seen.

## Stress tests
| Base: 3-yr unadjusted burning cost | $120.5k | ~$185k at 65% LR |
| 2024-type loss once per 5 yrs ($32.4k + $49.4k) | $81.8k | ~$126k at 65% LR |
| New welders at 1.5 freq. in yr 1 | +$9k [estimate] | supports a debit |
$150k sits between: indicated LR 80% on the base view, 55% on the 1-in-5 view.

## Proposed terms
| $150k quote with 5% schedule debit | growth and new operations |
| Loss-control visit within 60 days | new trailer-frame line |
| Subjectivity: 2022 loss run within 30 days | 5-yr history incomplete |

## Referral triggers
None on authority. Note for portfolio: second fabrication risk in this county.

## Decision
Quote with modified terms ($150k, debit, visit, subjectivity). Reasons: controls
credible after 2024; expected loss sensitive to one large loss; growth unproven.
```

## Techniques Used

- **DP-03 Anchored Scoring Scales** — risk-quality anchors written before scoring and cited per score.
- **NE-11 Embedded Calculation Formulas** — burning cost, expected loss and indicated loss ratio shown step by step.
- **DD-05 Human Review Flags** — referral triggers routed to the authority holder rather than decided.
- **QA-02 Adversarial Stress-Test** — large-loss recurrence and growth scenarios tested against the premium.

## Related Prompts

- `domain-specialized-fields/insurance/insurance_commercial_submission_builder.md` — the broker's side of the file this assessment reads.
- `domain-specialized-fields/insurance/insurance_renewal_remarketing_plan.md` — how the broker responds to this quote at renewal.
- `domain-finance/credit-lending/finance_credit_memo_builder.md` — the parallel lender decision on repayment capacity.
