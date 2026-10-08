---
title: "Founder Investor Update — Stable Metric Definitions, Bad News Up Top, Runway With Committed Costs"
category: professional-writing/domain-specific
description: "Write a founder's monthly or quarterly update to existing investors: metrics on definitions held constant from the last update (with any change restated), the period's worst news in the first lines, runway computed on burn that includes committed hires, a check against what the last update promised, and asks specific enough to act on. Distinct from a fundraising pitch to new investors and from a board deck."
techniques:
  - DS-02
  - NE-11
  - DS-06
  - NE-17
difficulty: intermediate
tags:
  - founder
  - investor-update
  - monthly-investor-update
  - quarterly-investor-letter
  - startup-runway
  - shareholder-update
  - startup-metrics
updated: "2026-10-06"
related_prompts:
  - domain-presentations/narrative-delivery/presentation_investor_pitch_narrative.md
  - domain-finance/treasury-capital-markets/finance_liquidity_runway_covenant_analysis.md
  - domain-professional-writing/business-writing/business_writing_status_report.md
  - domain-presentations/powerpoint_board_deck.md
---

# Founder Investor Update

**Objective:** Produce a periodic update that existing investors can compare line for
line with the last one, that states the period's bad news before its wins, that shows
runway on the burn the company has actually committed to, and that ends in asks an
investor can act on that week.

**When to Use:**
- You send a monthly or quarterly update to the investors already on your cap table.
- Something went wrong this period and you need to say it without either burying it or
  setting off alarm.
- A metric's definition changed (you started counting signed contracts, switched
  retention basis) and the update must stay comparable.
- You want investors' help and keep getting "let me know how I can help".
- **Not this prompt if** you are raising from new investors — use
  `domain-presentations/narrative-delivery/presentation_investor_pitch_narrative.md`. A
  board meeting pack with decisions for directors is
  `domain-presentations/powerpoint_board_deck.md`. If the question is the runway
  analysis itself (scenarios, covenants, minimum cash), do it first with
  `domain-finance/treasury-capital-markets/finance_liquidity_runway_covenant_analysis.md`
  and bring the result here.

**Audience:** Existing investors, from lead partners who read every line and compare it
with the last update, to small angels who read the first three lines. They want to know
whether the company is on track, whether runway has changed, what the founder is worried
about, and how they can help.

## Inputs / Context

Paste source material inside named tags and refer to it by name, e.g.
`<last_update>`, `<metrics>`, `<financials>`.

1. **Headline metrics** `<metrics>` — revenue or ARR, growth, retention, customers, the
   company's key KPIs, each with its definition.
2. **Last update** `<last_update>` — the previous update's metrics, definitions, and what
   it said the company would do next.
3. **Financials** `<financials>` — cash at period end, monthly net burn for the period,
   and committed costs not yet in the burn (signed offers, contracts, price increases).
4. **Wins this period** — product, customers, team, financing.
5. **Challenges** — what is hard right now, what it costs, what you are doing.
6. **Key learnings** — what you found out that changes what you do.
7. **Asks** — introductions, advice, expertise; who you want and why.
8. **Next 30/90 days** — focus and milestones.
9. **Constraints** — customer names you may or may not disclose; anything under NDA;
   whether the update also goes to prospective investors.

## Method

1. **Hold definitions steady (DS-02).**
   - Compare each metric's definition with `<last_update>`. Where it changed, report this
     period on both bases, restate the prior period on the new basis, and say why it
     changed in one line.
   - Keep the comparison period the same length (quarter vs quarter, month vs month).
2. **Compute runway on committed burn (NE-11).**
   - Committed net burn = current monthly net burn + monthly cost of signed hires and
     contracts not yet in it.
   - Runway (months) = cash ÷ committed net burn; show the current-burn figure beside it.
   - Cash-out date = period end + runway; raise-by date = cash-out − the fundraising
     lead time the founder supplies. State that revenue is held flat unless the founder
     provides a forecast.
3. **Score the last update's promises.** Each "next 90 days" item from `<last_update>`:
   done, partly, missed — with one line on why.
4. **Order by severity (DS-06).**
   - The most material negative development (lost large customer, runway shortening,
     key departure, missed target) appears in the TL;DR's first lines, with its number.
   - Then metrics, then wins, then challenges with the plan for each.
5. **Write challenges as what, impact, plan, and what would make it worse.** No
   adjectives in place of numbers.
6. **Make asks specific (NE-17).** Each ask names the kind of person or company, why,
   and what a good outcome is — something an investor can forward in one step.
7. **Verify before sending.** Every metric matches `<metrics>`; growth rates recompute;
   runway recomputes from cash and burn; no customer is named who has not agreed
   (`[VERIFY: permission to name]`); projections are labelled as projections. If the
   update will reach prospective investors, flag it for counsel review
   (`[VERIFY: securities counsel]`) rather than editing it here.

## Output Format

```
Subject: [Company] [period] update — [one-line headline including the bad news if any]

## TL;DR
- [most material negative development, with number]
- [headline progress, with number]
- [runway: months on committed burn; raise-by date]
- [top ask]

## Metrics
| Metric | Definition | Last period | This period | Change |
[Definition changes: what changed, why, prior restated]

## Cash and runway
Cash [..]  Net burn [..]/mo  Committed additions [..]/mo  Committed burn [..]/mo
Runway [..] months (current burn: [..])  Cash-out [..]  Raise-by [..]

## What we said last time
| Commitment | Result | Note |

## Wins
## Challenges   [what — impact — plan — what would make it worse]
## Learnings
## Asks         [numbered, specific]
## Next 30 / 90 days
```

## Verification

- [ ] Each metric's definition matches the last update, or the change is stated with the
      prior period restated.
- [ ] Growth rates recompute from the two periods shown.
- [ ] Runway uses burn including committed hires and contracts; both figures shown.
- [ ] The most material negative development is in the TL;DR's first lines.
- [ ] Every commitment from the last update is reported.
- [ ] Each ask names a type of person or company and the outcome wanted.
- [ ] Named customers have permission; projections are labelled.

## False-Positive Prevention

1. **A metric whose definition moved.** Last quarter's "ARR" included signed contracts
   not yet live; this quarter's does not (or the reverse). Retention switches from gross
   to net, revenue becomes ARR. The update looks fine and is not comparable. Show both
   bases and restate the prior period.
2. **Bad news under the wins.** The churned largest customer appears in paragraph six
   after three wins. Investors who find it there trust the next update less. It goes in
   the TL;DR with its ARR.
3. **Runway on today's burn.** Cash ÷ current burn ignores the three offers already
   signed. Investors will compute the committed figure at the next update and see the
   runway "drop" without warning. Use committed burn.
4. **Growth from a convenient base.** Month-over-month growth from a dip month, or a
   quarter compared with a shorter period, flatters the rate. Compare like-length
   periods and the same months used last time.
5. **Last update's promises dropped.** A "next 90 days" item that was missed and never
   mentioned again is noticed by the investor who reads both. Report every one.
6. **Asks too vague to act on.** "Intros to potential customers" produces nothing.
   "VPs of Finance at freight brokers with 200+ trucks running NetSuite" can be
   forwarded in a minute.
7. **Customer names without permission.** Logos in a win list are often under NDA, and
   updates get forwarded. Name only with permission; otherwise describe ("a top-20
   US freight broker").

## Example Output

```
Subject: Tallyhaul Q3 2026 update — largest customer churned; ARR $1.61M; 14.8 months runway

## TL;DR
- Lost our largest customer (Brightline Freight, $96k ARR) to an in-house build; gross
  retention fell from 91% to 86%. Cause and fix below.
- ARR $1.61M on a live-subscriptions basis, +13.4% on Q2 restated; 68 paying customers.
- 14.8 months runway on committed burn (3 hires signed); raise-by June 2027.
- Ask: intros to VPs of Finance at freight brokers with 200+ trucks on NetSuite.

## Metrics
| Metric | Definition | Q2 | Q3 | Change |
| ARR | Live paying subscriptions × 12; excludes signed-not-live and onboarding fees | $1.42M (restated) | $1.61M | +13.4% |
| Signed, not yet live | Contracted ARR awaiting go-live | $0.13M | $0.22M | +$0.09M |
| Net revenue retention | Trailing 12 mo, ARR basis | 104% | 98% | −6 pts |
| Gross revenue retention | Trailing 12 mo, ARR basis | 91% | 86% | −5 pts |
| Paying customers | Logos with a live paid subscription | 61 | 68 | +7 |
Definition change: the Q2 update reported ARR $1.55M, which included $0.13M signed but
not live. From Q3, ARR is live only and signed-not-live is reported separately; Q2 is
restated to $1.42M. On the old basis Q3 would be $1.83M (+18.1% on $1.55M). Growth
check: 1.61 ÷ 1.42 = 1.134; 1.83 ÷ 1.55 = 1.181.

## Cash and runway
Cash $3.90M (30 Sep)   Net burn $205k/mo (Q3 avg)   Committed additions $58k/mo
(3 signed hires, all started by 1 Dec)   Committed burn $263k/mo
Runway 3.90 ÷ 0.263 = 14.8 months (current burn: 3.90 ÷ 0.205 = 19.0)
Cash-out ≈ late Dec 2027   Raise-by June 2027 (6-month raise lead time, our assumption)
Revenue held flat; no growth assumed in these figures.

## What we said last time
| Commitment                         | Result  | Note |
| Ship multi-carrier invoice matching | Done    | Live 12 Aug; used by 41 customers |
| Hire Head of Sales                 | Missed  | Two finalists; offer expected October |
| Reach 70 paying customers          | Missed  | 68; two deals slipped into October |

## Wins
- Multi-carrier matching: customers using it reconcile invoices in a median 2 days,
  down from 6 (product analytics).
- Seven net new customers, including two top-50 US freight brokers [VERIFY: permission
  to name].
- Signed-not-live grew to $0.22M; both large contracts go live in Q4.

## Challenges
Brightline churn — What: built reconciliation in-house after we could not parse a
carrier invoice format they rely on. Impact: −$96k ARR; drives the GRR drop. Plan:
format support ships in November; we reviewed the 9 customers with similar volume and
3 ($140k ARR) use the same format — each has a founder call this month. Worse if: any
of the 3 renews before November.
Head of Sales hire slipped a quarter — Impact: founder still runs every deal over
$30k, which caps new pipeline. Plan: offer in October; interim sales advisor 1 day/week.

## Learnings
Large customers churn on format coverage, not price: none of our last four losses cited
price. We now track format coverage by customer volume weekly.

## Asks
1. Intros to VPs of Finance at freight brokers with 200+ trucks running NetSuite — our
   best-retaining segment.
2. 30 minutes with anyone who has hired a first Head of Sales at a vertical SaaS company
   under $3M ARR — on calibrating the scorecard before our final interviews.
3. Feedback on the 9-customer retention review — is there a churn signal we are missing?

## Next 30 / 90 days
30: Head of Sales offer; founder calls with the 3 at-risk accounts.
90: carrier-format support live; both signed contracts live (+$0.22M ARR); GRR back
above 90% on the trailing-12 basis [projection].
```

## Techniques Used

- **DS-02 Metric Specification** — each metric defined, held constant across updates, and
  restated when its basis changes.
- **NE-11 Embedded Calculation Formulas** — committed burn, runway, cash-out and raise-by
  date, and growth recomputed on both bases.
- **DS-06 Prioritization and Severity Guidance** — the most material negative development
  leads the TL;DR.
- **NE-17 Call-to-Action Mandatory Close** — numbered asks, each specific enough to forward.

## Related Prompts

- `domain-presentations/narrative-delivery/presentation_investor_pitch_narrative.md` — the
  fundraising narrative for the raise this update's raise-by date points to.
- `domain-finance/treasury-capital-markets/finance_liquidity_runway_covenant_analysis.md` —
  the full runway analysis behind the cash section.
- `domain-professional-writing/business-writing/business_writing_status_report.md` — status
  reporting with the same bad-news-plainly discipline, for internal stakeholders.
- `domain-presentations/powerpoint_board_deck.md` — the board meeting deck, where
  decisions are asked of directors.
