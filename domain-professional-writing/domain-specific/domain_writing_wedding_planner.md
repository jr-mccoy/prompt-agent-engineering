---
title: "Wedding Planner Client Proposal — Defined Services, a Budget That Adds Up, Vision as Decisions"
category: professional-writing/domain-specific
description: "Write a wedding planner's proposal to a couple: their vision translated into concrete decisions, services defined tightly enough to prevent scope disputes (what 'day-of' covers, who pays vendors, overtime), a category budget recomputed against their total with a contingency, and the planner's fee and payment schedule. Distinct from general services proposals (business_writing_client_engagement_proposal) and from drafting the contract itself (legal_sow_drafter)."
techniques:
  - DD-02
  - CM-03
  - NE-11
  - QA-20
difficulty: intermediate
tags:
  - wedding-planner
  - wedding-proposal
  - event-planning-proposal
  - day-of-coordination
  - wedding-budget
  - write-a-proposal-for-a-couple
updated: "2026-10-06"
related_prompts:
  - domain-professional-writing/business-writing/business_writing_client_engagement_proposal.md
  - domain-legal/contracts-transactional/legal_sow_drafter.md
  - domain-legal/contracts-transactional/legal_payment_terms_and_late_fee_review.md
---

# Wedding Planner Client Proposal

**Objective:** Give a couple a proposal they can say yes to with no surprises later: their
vision shown as decisions, every service bounded in hours and responsibilities, a budget
whose categories sum to their number, and a fee schedule that matches the contract.

**When to Use:**
- After a consultation, when a couple has shared date, venue, guest count, budget, and
  what they want the day to feel like.
- Converting a package menu (full planning, partial planning, day-of coordination) into a
  proposal for one specific wedding.
- A past client disputed what "day-of" included, or expected you to pay vendors, and you
  want the next proposal to close those gaps.
- The couple's budget and guest count look inconsistent and you need to show them the
  arithmetic kindly.
- **Not this prompt if** you are writing a proposal for a non-wedding professional
  service with no event budget — use
  `domain-professional-writing/business-writing/business_writing_client_engagement_proposal.md`.
  For the services agreement itself, use
  `domain-legal/contracts-transactional/legal_sow_drafter.md` and have the contract
  reviewed; this proposal must match it, not replace it.

**Audience:** The couple, often reading together and sometimes with a parent who is
contributing money. They need to feel understood and to see exactly what they are buying,
what it costs, and what remains theirs to do. A family member paying a share will read the
budget table first.

## Inputs / Context

Paste source material inside named tags and refer to it by tag name:

1. **Wedding details** — date, venue (and rain plan), guest count, total budget and
   whether it includes your fee.
2. **Couple's vision** in `<consult_notes>` — their words for style and feel, their top
   priorities, what they do not care about.
3. **Your approach** — how you run planning and the day: meetings, tools, team size.
4. **Services included** — the stub's field, plus your package definitions in
   `<package_terms>`: start date of service, meetings, on-site hours, staff count, setup
   limits, overtime rate and increment, travel, what is excluded.
5. **Budget working numbers** in `<budget_draft>` — category estimates, quotes already
   received, vendors already booked.
6. **Investment** — your fee, payment schedule, retainer terms, cancellation terms as
   written in your contract template `<contract_terms>`.
7. **Venue constraints** in `<venue_terms>` (optional) — included items, end time,
   load-out, vendor restrictions.

## Method

1. **Translate the vision into decisions (DD-02).** For each phrase the couple used,
   write the decision it implies, the date it gets made, and what it costs or protects.
   "Relaxed" might mean no receiving line and family-style dinner; "everyone dancing"
   might mean dinner ends by a set time. A vision section that only repeats their
   adjectives has not done the work.
2. **Bound every service (CM-03).** For each service state: what you do, start and end
   (date or time), how many meetings or hours, how many staff, and what is excluded.
   Name the three dispute points explicitly:
   - **"Day-of"**: when your involvement starts (often weeks before), on-site hours,
     rehearsal, and what happens at the end of the night.
   - **Vendor payments**: who pays vendors, whether you ever hold the couple's money,
     and who delivers final payments and gratuities on the day.
   - **Overtime**: rate per staff member, increment, and who on the day can approve it.
3. **Recompute the budget (NE-11).** Sum `<budget_draft>`; per-guest lines are
   guest count × rate. Compare to the stated total. If it is over, or has no contingency,
   show the gap and a rebalancing that protects the couple's top priorities and trims
   what they said matters less. Mark estimates `[estimate]` and booked amounts
   `[contracted]`; taxes and service charges come from vendor quotes or are
   `[VERIFY: vendor quote]`.
4. **Build the timeline.** Planning milestones from signing to the wedding, plus a
   day-of outline that shows the vision decisions in time.
5. **Match the money to the contract.** Fee, payment dates, and amounts sum to the fee;
   retainer and cancellation wording comes from `<contract_terms>`, not from memory
   `[VERIFY: your contract template and local consumer rules on deposits]`.
6. **Verify before output.** Recompute every total, check each service has a start, an
   end, and an exclusion, and check every vision phrase maps to a decision.

## Output Format

```
## Your wedding as we heard it
| You said | What we'll decide | When | Budget effect |

## How we'll work
## Services
| Service | Included | Not included |
   Day-of definition | Vendor payments | Overtime

## Budget
| Category | Your draft | Proposed | Basis |
Totals and arithmetic; gap; contingency

## Planning timeline and wedding-day outline
## Investment
Fee | payment schedule (sums to fee) | overtime | travel

## Next steps
```

## Verification

- [ ] Every vision phrase from `<consult_notes>` maps to a decision with a date.
- [ ] "Day-of" has a start date, on-site hours, staff count, and an end-of-night rule.
- [ ] The proposal states who pays vendors and that the planner does or does not hold funds.
- [ ] Overtime rate, increment, and approver are stated.
- [ ] Budget categories sum to the stated total, including the planner's fee if the couple's total includes it, with a contingency line.
- [ ] Per-guest lines equal guest count × rate.
- [ ] Payment schedule sums to the fee; dates are consistent with the wedding date.

## False-Positive Prevention

1. **Vision mirrored, not planned.** "You dream of a relaxed, joyful garden celebration"
   feels attentive and tells the couple nothing they did not say; each phrase needs a
   decision attached.
2. **"Day-of coordination" taken at its name.** Couples read it as one day; planners
   run it from weeks out. Without start date and hours, the first 6-week call or the 11 pm
   overrun becomes a dispute.
3. **Silence on vendor payments.** If the proposal does not say the couple pays vendors
   directly, someone will expect the planner to carry a balance or hand over cash, and
   holding client funds creates obligations the planner did not price.
4. **A budget that only adds up per line.** Each estimate can be reasonable while the
   sum overshoots the total by thousands; the couple discovers it at the last deposit.
5. **The fee outside the total.** If the couple's number is "all-in", leaving the planner
   fee out of the budget table hides a gap the size of the fee.
6. **Zero contingency presented as a balanced budget.** Weather, a guest-count creep of
   ten, or a vendor service charge consumes it; a budget at exactly the total with no
   buffer is already over.
7. **Cutting what the couple protected.** A rebalancing that trims food when they said
   food matters most is arithmetic without listening; cut from what they ranked lowest.

## Dual-Failure Prevention (QA-20)

- **Harmful:** a proposal that signs off on an over-budget plan or vague services, so
  the couple overspends or argues with the planner the week of the wedding.
- **Unhelpful:** a proposal so full of contract language, caveats, and "subject to vendor
  availability" that the couple cannot see their plan, or one that lists the budget gap
  and leaves them to solve it alone.
- **Bar:** the couple can read the budget total, see what was cut and why, and say what
  happens at 10:30 pm on the day and who pays the DJ.

## Example Output

Scenario: Jordan Ellis and Aisha Rahman, Saturday 18 September 2027, Willow Creek Farm (lawn
ceremony; barn reception; barn is the rain plan), 140 guests, $48,000 all-in including planner
fee. `<consult_notes>`: "relaxed garden party, not stuffy", "the food has to be great", "we want
everyone dancing", "photos that feel like us"; florals "nice but not essential". Planner: Field
& Fern Events, partial-planning package, $4,800. `<package_terms>`: service starts at signing;
3 planning meetings; venue walkthrough; 1-hour rehearsal; on-site 11:00–23:00 with lead plus one
assistant; overtime $95/h per staff member in 30-minute increments; up to 2 hours placing
couple-supplied décor; travel within 40 miles included. `<venue_terms>`: music ends 22:00;
vendor load-out by 23:00.

```
## Your wedding as we heard it
| You said                     | What we'll decide                                  | When     | Budget effect |
| "relaxed garden party"       | Lawn ceremony, no receiving line, family-style dinner (caterer confirms barn table space for 140 [VERIFY: venue floor plan]) | Jun 2027 | within catering line |
| "the food has to be great"   | Tasting with caterer; catering line protected in rebalance | Jun 2027 | $15,400 kept |
| "everyone dancing"           | Dinner service ends 19:45; DJ planning call; dance floor sized by rental company for 140 [VERIFY: rental sizing] | Aug 2027 | within music/rentals |
| "photos that feel like us"   | First look 15:00 so cocktail hour isn't spent on portraits; photography protected | Jul 2027 | $4,800 kept |

## How we'll work
Three planning meetings (June, July, August), a shared budget tracker and vendor contact
sheet, venue walkthrough in August, rehearsal on Friday 17 September.

## Services
| Service           | Included                                          | Not included |
| Vendor sourcing   | Referrals and booking support for unbooked vendors | Negotiating on your behalf without your sign-off |
| Budget            | Tracker, payment-due reminders 7 days ahead       | Paying vendors or holding your funds |
| Timeline          | Wedding-day run sheet sent to all vendors 14 days out | — |
| Day-of            | See definition below                              | Guest RSVP tracking; DIY assembly; cleaning |
Day-of definition: our involvement runs from signing; final vendor confirmations begin six
weeks out (7 Aug). On the day, lead planner and one assistant on site 11:00–23:00: vendor
arrivals, placing your décor (up to 2 hours), ceremony cueing, reception flow, supervising
load-out to the venue's 23:00 deadline.
Vendor payments: you pay every vendor directly. We remind you 7 days before each due date.
On the day we hand over sealed final-payment and gratuity envelopes that you prepare; we never
hold or transfer your money.
Overtime: $95 per hour per staff member, in 30-minute increments, approved on the day by
the contact you name (e.g. Aisha's sister).

## Budget  (all-in total $48,000)
| Category              | Your draft | Proposed | Basis |
| Venue                 |  9,500 |  9,500 | [contracted] |
| Catering & bar        | 15,400 | 15,400 | 140 × $110 incl. service charge & tax per caterer's sample quote [VERIFY: final quote] |
| Photography           |  4,800 |  4,800 | [contracted] |
| Florals & décor       |  4,200 |  2,900 | seasonal stems; ceremony arch moved to reception |
| Music (DJ + ceremony) |  2,200 |  2,200 | [estimate] |
| Rentals & lighting    |  2,600 |  2,000 | venue's farm tables; no linen upgrade |
| Attire & beauty       |  3,500 |  3,500 | yours to set |
| Cake                  |    900 |    500 | 2-tier cutting cake + kitchen sheet cake [estimate] |
| Stationery & postage  |    700 |    400 | digital save-the-dates |
| Officiant             |    500 |    500 | [estimate] |
| Planner fee           |  4,800 |  4,800 | this proposal |
| Contingency           |      0 |  1,500 | ~3% buffer |
| **Total**             | **49,100** | **48,000** | |
Your draft sums to $49,100 — $1,100 over, with no contingency. Proposed: florals −1,300,
rentals −600, cake −400, stationery −300 = −2,600 → 46,500 + 1,500 contingency = 48,000.
Food and photography, your two priorities, are unchanged.

## Planning timeline and wedding-day outline
17 May sign · Jun tasting + meeting 1 · Jul photo plan + meeting 2 · 7 Aug final
confirmations begin · Aug walkthrough + meeting 3 · 4 Sep run sheet to vendors · 17 Sep rehearsal.
Day: 15:00 first look · 16:30 ceremony · 17:00 cocktail hour, lawn games · 18:15 dinner,
family-style · 19:45 dancing · 22:00 music ends (venue rule) · 23:00 load-out complete.

## Investment
Partial planning: $4,800 (in the budget table above). Payments: 30% at signing 17 May 2027
($1,440); 40% on 20 June 2027, 90 days out ($1,920); 30% on 4 September 2027, 14 days out
($1,440); 1,440 + 1,920 + 1,440 = 4,800. Overtime as above; travel included (venue within 40
miles). Retainer and cancellation terms as in the enclosed agreement [VERIFY: contract template].

## Next steps
Tell us whether the proposed budget column works or which line you'd rather trim; we'll send
the agreement with these services and dates written in.
```

## Techniques Used

- **DD-02 Vague-to-Concrete Translation** — each vision phrase becomes a dated decision with its budget effect.
- **CM-03 Scope Definition** — every service carries included/excluded columns, with day-of, vendor payments, and overtime defined explicitly.
- **NE-11 Embedded Calculation Formulas** — per-guest lines, category totals, the rebalancing, and the payment schedule are recomputed and shown.
- **QA-20 Dual-Failure Quality Test** — the proposal is checked against both an over-budget, vague plan and an over-caveated one that leaves the couple to solve the gap.

## Related Prompts

- `domain-professional-writing/business-writing/business_writing_client_engagement_proposal.md` — general professional-services proposals.
- `domain-legal/contracts-transactional/legal_sow_drafter.md` — turn these service definitions into contract scope.
- `domain-legal/contracts-transactional/legal_payment_terms_and_late_fee_review.md` — review retainer, payment, and late-fee terms from the planner's side.
