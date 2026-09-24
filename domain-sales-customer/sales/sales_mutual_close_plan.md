---
title: "Mutual Close Plan — A Buyer-Owned Path from Today to Go-Live, Built Backward from Their Date"
category: sales-customer/sales
description: "Build a mutual action plan the buyer can own and forward internally: work backward from the buyer's own go-live event through every approval, security, legal and procurement step, give each step a named owner on their side and ours with a date, mark the gates that stop the deal, and produce the version to share — distinct from the negotiation close, which handles the final concession rather than the path to signature."
techniques:
  - QA-08
  - DP-07
  - RP-02
  - OC-03
difficulty: intermediate
tags:
  - sales
  - mutual-action-plan
  - close-plan
  - enterprise-sales
  - buyer-enablement
  - deal-execution
updated: "2026-09-24"
related_prompts:
  - domain-sales-customer/sales/sales_deal_qualification_scorecard.md
  - domain-sales-customer/sales/sales_forecast_commit_review.md
  - domain-negotiation/at-the-table/negotiation_closing_and_final_concession.md
---

# Mutual Close Plan

**Objective:** Produce a dated plan, agreed with the buyer, that lists every step
between today and the outcome they care about — with an owner on each side — so
that slippage is visible the week it happens rather than the week the deal was
supposed to close.

**When to Use:**
- The buyer has said yes to the solution and "the process" is now the risk.
- Close dates have slipped before on this deal, or on deals like it.
- The champion needs something to take into rooms you are not in.
- Security review, legal, or procurement is ahead and nobody knows the lead times.
- **Not this prompt if** the remaining issue is price or terms — the final
  concession and the nibble belong to
  `domain-negotiation/at-the-table/negotiation_closing_and_final_concession.md`.
  If you do not yet know who the economic buyer is or what the decision process
  is, you are not ready for a close plan: run
  `sales_deal_qualification_scorecard.md` first. Onboarding after signature
  belongs to `domain-business-strategy/go-to-market/workflow_customer_success_onboarding_plan.md`.

## Inputs / Context

1. **The buyer's event:** the date something must be true for *them* — a season,
   a contract expiry, an audit, a launch. Their words, with who said it.
2. **Decision process** as the buyer described it: steps, approvers, committees.
3. **Paper process:** security questionnaire, DPA, MSA, procurement onboarding,
   PO. Known lead times from the buyer, or `[ASK]`.
4. **People:** champion, economic buyer, legal, security, procurement, IT —
   names where known.
5. **Our side:** AE, SE, legal, deal desk, implementation lead, exec sponsor.
6. **Anything already done** (demo, pilot, reference call) with dates.

## Method

1. **Anchor on the buyer's date, not the quarter.** Start from the event the
   buyer named. If the only date is your quarter-end, stop and say so — the plan
   will be a seller's calendar in a buyer's costume.

2. **Work backward.** From go-live, list what must be done immediately before it
   (implementation kick-off, signature, PO, legal redlines, security sign-off,
   business case approval, evaluation complete). Use the buyer's stated lead
   times; where none is known, use `[ASK — typical: n weeks]` and flag it.

3. **Assign two owners per step.** One on the buyer side, one on ours. A step with
   only our owner is our to-do list, not a mutual plan.

4. **Mark the gates (QA-08).** A gate is a step whose failure stops the plan:
   economic-buyer approval, security pass, budget release. For each gate state
   the pass condition in observable terms ("security questionnaire returned with
   no open high findings"), not "security OK."

5. **Find the slack.** Compare the backward schedule to today. If the plan needs
   more weeks than exist, show the gap and the options: parallelise legal and
   security, phase scope, or move the go-live — decided with the buyer.

6. **Pre-mortem the plan (DP-07).** For the three steps most likely to slip,
   write how it fails ("procurement onboarding needs a W-9 and bank letter we did
   not send"), the early warning, and the move.

7. **Write the buyer-facing version (RP-02).** Plain, neutral, forwardable: the
   buyer's goal in the first line, their language, no internal forecast
   categories, no discount notes, no "we need this by quarter end."

8. **Set the review rhythm.** Who reviews the plan, how often, and what happens
   when a date moves — the plan is updated, not abandoned.

## Output Format

```
# Mutual plan — [Buyer] × [Us] — goal: [buyer's outcome] by [buyer's date]

## Backward schedule
| # | Step | Buyer owner | Our owner | Due | Lead time (source) | Gate? | Status |

## Gates
| Gate | Pass condition (observable) | Decider |

## Feasibility
Weeks needed [n] vs weeks available [n] → [fits | gap of n: options …]

## Pre-mortem (top 3 slip risks)
| Step | How it fails | Early warning | Move |

## Review rhythm

## Buyer-facing version  (forwardable; no internal fields)

## Internal notes  (never shared)
```

## Verification

- [ ] The anchor date is the buyer's event, attributed to a named buyer.
- [ ] Every step has a buyer-side owner, or is explicitly marked ours-only.
- [ ] Every gate has an observable pass condition and a decider.
- [ ] Lead times are sourced or marked `[ASK]`.
- [ ] Weeks-needed recomputed from the schedule.
- [ ] The buyer-facing version contains no forecast, discount, or quota language.

## False-Positive Prevention

1. **A plan the buyer has not seen is not mutual.** If it has not been reviewed
   with the champion, it is a forecast with extra rows.
2. **Our quarter-end is not their deadline.** A plan anchored on it will read as
   pressure and be treated as optional.
3. **"Legal review: 1 week" is usually invented.** Unless the buyer said so,
   mark it `[ASK]`; enterprise legal and security lead times are where plans die.
4. **Signature is not the goal.** A plan that ends at signature optimises our
   event; the buyer's goal is what the product does for them afterwards.
5. **Silent owners are not owners.** A buyer name on a step they have not agreed
   to is a hope.
6. **No manufactured urgency.** Do not add expiring discounts or false scarcity
   to "hold dates." If there is a real constraint on our side (implementation
   capacity), state it as a fact with its date.
7. **Parallelising is not free.** Running legal and security together saves
   weeks only if both teams have capacity; check before promising it.

## Example Output

```
# Mutual plan — Halvorsen Freight × Us — goal: fuel-variance reporting live for
# the Q1 audit (R. Okafor, 09-03) by 2027-01-15

## Backward schedule
| # | Step | Buyer owner | Our owner | Due | Lead time (source) | Gate? | Status |
| 1 | Eval sheet scored, shortlist decided | R. Okafor | AE | 10-03 | — | | done 10-01 |
| 2 | Business case to CFO | R. Okafor | AE + SE | 10-10 | 1 wk (Okafor) | Gate | open |
| 3 | Security questionnaire returned | IT: [ASK name] | SE | 10-24 | [ASK — typical 3 wks] | Gate | not started |
| 4 | MSA + DPA redlines | Legal: [ASK] | Our legal | 10-31 | [ASK] | | not started |
| 5 | Vendor onboarding, PO issued | Procurement | Deal desk | 11-14 | 2 wks (Okafor) | | — |
| 6 | Signature | CFO | AE | 11-14 | — | | — |
| 7 | Implementation kick-off | R. Okafor | Impl. lead | 11-18 | — | | — |
| 8 | Data connected, first report | Fleet analyst | Impl. lead | 12-19 | 4 wks (our std) | Gate | — |
| 9 | Report accepted for audit | R. Okafor | CSM | 01-15 | — | | — |

## Gates
| Gate | Pass condition | Decider |
| 2 | CFO approves spend in writing | CFO |
| 3 | Questionnaire returned, no open high findings | Halvorsen IT lead |
| 8 | Report reconciles to one month of fuel invoices within 2% | R. Okafor |

## Feasibility
Weeks needed from today to step 9: 16. Available: 16. Fits with zero slack;
step 3 is unsourced and could break it.

## Pre-mortem
| Step | How it fails | Early warning | Move |
| 3 | Questionnaire sits in IT queue | No IT owner named by 10-08 | Okafor requests owner; SE offers live review call |
| 4 | Legal starts only after security | Redlines not received by 10-24 | Ask Okafor to send MSA in parallel with step 3 |
| 8 | Fuel-card data export needs vendor ticket | No export sample by 11-25 | Request sample before signature |

## Review rhythm
Tuesday 15-min check with Okafor; any date move updates the plan the same day.

## Buyer-facing version
Goal: fuel-variance reporting ready for your Q1 audit by 15 January.
Steps 1–9 as above, owners and dates, without internal notes.

## Internal notes
Deal CONDITIONAL on qualification scorecard (Paper process 0). This plan is how
that gap closes; if step 3 has no owner by 10-08, the kill signal fires.
CRM close date (10-31) is two weeks earlier than signature (step 6, 11-14) —
move it to 11-14 before the forecast call.
```

## Techniques Used

- **QA-08 Gate-Based Verification** — gates with observable pass conditions.
- **DP-07 Failure Mode Prediction** — pre-mortem on the three likeliest slips.
- **RP-02 Audience-Specific Framing** — a forwardable buyer version separate from internal notes.
- **OC-03 Markdown Table Specification** — the backward schedule as the single source of truth.

## Related Prompts

- `domain-sales-customer/sales/sales_deal_qualification_scorecard.md` — the gaps
  this plan must close.
- `domain-sales-customer/sales/sales_forecast_commit_review.md` — gate status is
  the evidence for a Commit call.
- `domain-negotiation/at-the-table/negotiation_closing_and_final_concession.md` —
  when the last open item is price or terms rather than process.
