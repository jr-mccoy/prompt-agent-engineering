---
title: "Bid / No-Bid Decision — Hard Gates First, Then Anchored Scores, Expected Value, and a Kill Signal Before You Spend the Estimating Hours"
category: specialized-fields/trades
description: "Decide whether a contractor or trade subcontractor should bid one invitation: pass/fail gates on license, insurance and bonding, crew capacity in the actual work window, cash exposure under the customer's real payment history, and document completeness; then anchored 0–3 scores on fit, competition, margin, relationship and strategic value, an expected-value check against the cost of estimating, and a BID / BID WITH CONDITIONS / NO BID / INSUFFICIENT INFO verdict with a dated kill signal and a ready decline note — distinct from B2B sales deal qualification and from a services practice's ideal-client profile."
techniques:
  - AG-08
  - DP-03
  - NE-11
  - QA-04
difficulty: intermediate
tags:
  - trades
  - construction
  - bidding
  - bid-no-bid
  - subcontractor
  - cash-flow
  - decision
updated: "2026-09-24"
reasoning:
  styles: [evaluative, quantitative, strategic]
  stakes: high
  horizon: weeks
  uncertainty: risk
  evidence_quality: variable
  domain_complexity: regulated
  collaboration: small_team
  output_format: [structured, matrix]
  user_role: [contractor, estimator, business_owner]
  mode: [decide, diagnose]
related_prompts:
  - domain-sales-customer/sales/sales_deal_qualification_scorecard.md
  - domain-business-strategy/client-services/services_ideal_client_and_disqualifiers.md
  - domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md
---

# Bid / No-Bid Decision

**Objective:** Decide, before spending the estimating hours, whether this
invitation to bid is one the business can win, perform, and survive financially —
and if the answer depends on something, name it and the date it must be true by.

**When to Use:**
- A general contractor, property manager or owner has invited you to bid and the
  estimate would take a day or more.
- You win jobs that then hurt: slow pay, wrong crew fit, or a cash hole in month two.
- You bid everything because saying no feels like losing a relationship.
- **Not this prompt if** you are qualifying a B2B software or services deal —
  `domain-sales-customer/sales/sales_deal_qualification_scorecard.md`. If you want
  the standing profile of good and bad clients for a services practice, build it
  with `domain-business-strategy/client-services/services_ideal_client_and_disqualifiers.md`
  and use this prompt per invitation. Once the answer is BID, build the number with
  `trades_bid_estimate_with_contingency.md`. Contract terms (pay-when-paid,
  indemnity, retainage) are flagged here for an attorney; this prompt does not
  judge their enforceability.

## Inputs / Context

1. **The invitation:** scope, drawings/specs status, bid due date, number of bidders
   if known, hard-bid or negotiated.
2. **The customer's record with you:** past jobs, days-to-pay from your own
   receivables, disputes, change-order behaviour. Tag `[our-data]`; hearsay `[heard]`.
3. **Requirements:** license class, insurance limits, bonding, safety or
   prequalification forms.
4. **Your capacity:** crew hours per week and what is already booked in the weeks
   the work would actually happen (from the customer's schedule).
5. **Cash:** cash on hand, credit line available, supplier terms, and the contract's
   payment terms and retainage.
6. **Rough job size:** preliminary labor hours, materials, and target margin.
7. **Estimating cost:** hours to prepare the bid × your estimator's rate.

## Method

1. **Run the hard gates (AG-08).** Each is PASS / FAIL / UNKNOWN, with the evidence:
   - **License, insurance, bonding** — held vs required (certificate, not memory).
   - **Capacity** — `free crew hours/week in the work window ≥ required hours/week`.
   - **Cash** — `peak outlay = costs incurred before the first payment arrives`,
     using the customer's *actual* days-to-pay, not the contract's; compare to
     cash + available credit.
   - **Documents** — enough to price without guessing; if not, can an RFI fix it
     before the due date?
   - **Time** — estimating hours fit before the due date.
   Any FAIL is NO BID unless a named lever turns it to PASS by a date.

2. **Score the soft factors (DP-03), 0–3 with anchors:**

   | Factor | 0 | 3 |
   |---|---|---|
   | Customer payment & conduct | Disputes or >90 days | Paid in terms, fair on changes |
   | Competition | Open hard-bid, many bidders | Negotiated or short list of 2–3 |
   | Crew and skill fit | New work type for you | Done several of these recently |
   | Margin potential | Below your floor | At or above target with room |
   | Document quality | Conceptual only | Complete, coordinated |
   | Strategic value | One-off, no follow-on | Stated follow-on pipeline or a new market you want |
   | Site and access risk | Occupied, restricted, after-hours | Open, straightforward |

   Default thresholds: ≥14 of 21 bid; 10–13 bid only if strategic value is 3;
   < 10 no bid.

3. **Check expected value (NE-11).**
   `EV = P(win) × expected gross margin − cost to bid`. Base `P(win)` is
   `1 ÷ number of bidders`, adjusted for relationship and labelled `[estimate]`.
   A negative EV with passing gates is still a signal to decline or to bid only
   if strategic.

4. **Grade confidence (QA-04).** Which inputs are `[our-data]`, which `[estimate]`,
   and which single unknown would most change the verdict.

5. **Apply the verdict and set the kill signal.**
   - **BID** — all gates PASS, score ≥ threshold, EV > 0.
   - **BID WITH CONDITIONS** — a gate passes only if a named lever is confirmed by
     a date; conditions become bid qualifications or pre-bid questions.
   - **NO BID** — a gate fails with no lever, or score and EV both below bar.
   - **INSUFFICIENT INFO** — two or more gates UNKNOWN; name the one question that
     resolves most.
   The kill signal is one observable event with a date that flips the verdict to NO BID.

6. **Draft the decline note** now, so a NO BID goes out promptly and keeps the relationship.

## Output Format

```
# Bid / no-bid — [job] — invited by [customer] — due [date]

## Gates
| Gate | Required | Ours | Result | Evidence |

## Cash exposure
[schedule of costs vs receipts] Peak outlay $[..] vs available $[..] → [..]
Levers: [..]

## Scores
| Factor | 0–3 | Evidence |
Total [n]/21

## Expected value
P(win) [..] × margin $[..] − bid cost $[..] = $[..]

## Confidence
## Verdict
[BID | BID WITH CONDITIONS | NO BID | INSUFFICIENT INFO] — rule that fired
Conditions: [..] by [date]
Kill signal: [event] by [date] → NO BID

## Pre-bid questions / RFIs
## For attorney review (terms only, no opinion here)
## Decline note (ready)
```

## Verification

- [ ] Every gate cites evidence (certificate, receivables, schedule), not recollection.
- [ ] Peak outlay uses the customer's actual days-to-pay.
- [ ] Capacity is measured in the weeks the work happens, not this week.
- [ ] Score total and EV are recomputed and match.
- [ ] The verdict names the rule that fired and any conditions carry dates.
- [ ] Contract terms are flagged, not interpreted.

## False-Positive Prevention

1. **Invited is not wanted.** Some invitations exist to fill a bid list; a short
   list you are not on is a different job from an open six-bidder hard bid.
2. **Contract payment terms are not payment history.** Use what your receivables
   say this customer actually does.
3. **Backlog today is not capacity in week seven.** Check the weeks on their schedule.
4. **Revenue is not the prize; margin after cash cost is.** A job that needs a
   $107,000 float on a $90,000 line is a loan you are making to the customer.
5. **"Relationship" is not a score of 3 by default.** Score what they have done —
   paid, been fair on changes — not how friendly they are.
6. **Declining is a decision, not a failure.** A prompt, courteous no-bid keeps
   you on the next list more reliably than a late, padded number.
7. **Do not opine on contract clauses.** Pay-when-paid, indemnity and retainage
   terms go to an attorney; this prompt only notes that they are present.

## Example Output

```
# Bid / no-bid — Harbor St dental clinic TI, electrical — invited by Coastline
# Builders — due 2026-10-02 (8 days)

## Gates
| License | Commercial electrical | Held | PASS | License on file, exp. 2027-06 |
| Insurance | $1M/$2M GL + $2M umbrella | Same | PASS | Certificate; confirm additional-insured endorsement with agent |
| Bonding | Not required | — | PASS | ITB p.2 |
| Capacity | Rough-in wks 7–12: 630 hr = 105 hr/wk | 160 hr/wk, 25% booked → 120 free | PASS | GC schedule; our board |
| Cash | Peak outlay ≤ $90,000 | see below | FAIL at current terms | Receivables; supplier terms |
| Documents | Price without guessing | Panel schedules missing | UNKNOWN → RFI | Sheet E-201 |
| Time | 22 hr estimating before 10-02 | Available | PASS | — |

## Cash exposure
Coastline paid our last two invoices in 52 and 61 days [our-data] → first receipt
≈ day 87 of the work. Costs by day 87: materials $52,000 + labor ~80% of $65,100
($52,080) + other $3,000 = ~$107,000. Available: cash $30,000 + line $60,000 =
$90,000 → short ~$17,000.
Levers: (a) GC agrees to 30-day payment → first receipt day 60, costs by then
~$71,300 → PASS; (b) supplier grants net-60 on the $30,000 switchgear → peak
~$77,000 → PASS.

## Scores
| Customer payment & conduct | 2 | Slow (52–61 d) but paid in full; fair on 3 COs |
| Competition | 1 | 6 bidders, hard bid [GC said] |
| Crew and skill fit | 3 | 4 medical/dental TIs in 2 years |
| Margin potential | 2 | 18% target on preliminary takeoff; hard bid squeezes |
| Document quality | 2 | Full set except panel schedules |
| Strategic value | 2 | GC says 3 more medical TIs in 2027 [heard] |
| Site and access risk | 3 | Ground floor, vacant suite |
Total 15/21 (threshold 14)

## Expected value
Base P(win) 1/6 ≈ 17%, adjusted to 20% for relationship [estimate]
Margin: $148,000 − ($52,000 + $65,100 + $4,000) = $26,900
EV = 0.20 × $26,900 − $1,870 (22 hr × $85) = $3,510

## Confidence
Medium. Days-to-pay and capacity are [our-data]; P(win) and the follow-on work
are [estimate]/[heard]. The single unknown that most changes the answer: GC's
answer on payment terms.

## Verdict
BID WITH CONDITIONS — score 15 ≥ 14 and EV > 0, but the cash gate passes only
with lever (a) or (b).
Conditions: lever (a) or (b) confirmed in writing by Tue 09-29 17:00; RFI on panel
schedules answered by 09-30; bid qualifies switchgear lead time (10–12 weeks).
Kill signal: neither lever confirmed by 09-29 17:00 → NO BID; send note below.

## Pre-bid questions / RFIs
To GC (by 09-25): payment terms for subs on this job; stored-materials billing?
RFI (by 09-25): panel schedules for E-201.
To supplier (by 09-25): net-60 on switchgear order?

## For attorney review
Pay-when-paid clause (Subcontract §4.2) and 10% retainage — review before signing
if awarded; not assessed here.

## Decline note (ready)
"Thanks for including us on Harbor Street. We can't give it the attention it
deserves on this schedule and are passing on this one. We'd like to stay on your
list for the 2027 medical work — please keep us in mind."
```

## Techniques Used

- **AG-08 Evidence-Based Decision Gates** — license, capacity, cash and documents pass or fail on evidence.
- **DP-03 Anchored Scoring Scales** — each soft factor scored against stated anchors.
- **NE-11 Embedded Calculation Formulas** — peak outlay and expected value shown and recomputable.
- **QA-04 Uncertainty Acknowledgment** — confidence and the one unknown that swings the verdict.

## Related Prompts

- `domain-sales-customer/sales/sales_deal_qualification_scorecard.md` — the B2B
  sales counterpart, scored on buyer evidence.
- `domain-business-strategy/client-services/services_ideal_client_and_disqualifiers.md` —
  the standing client profile a practice applies to every lead.
- `domain-specialized-fields/trades/trades_bid_estimate_with_contingency.md` —
  builds the number once the verdict is BID.
