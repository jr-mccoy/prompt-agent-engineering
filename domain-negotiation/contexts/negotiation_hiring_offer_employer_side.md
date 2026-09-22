---
title: "Hiring Offer — Employer Side"
category: negotiation/contexts
description: "Negotiate a hiring offer from the employer's seat: the band position decided before the call, the package levers ranked by cost-to-you against value-to-them, an explicit walk-away, the internal-equity constraint that outranks winning this candidate, handling a competing offer without bidding against an unverifiable number, and a close that does not start the relationship with resentment."
techniques:
  - CM-02
  - MP-10
  - RT-05
  - QA-04
  - OC-03
difficulty: intermediate
tags:
  - hiring
  - offer-negotiation
  - employer-side
  - compensation
  - internal-equity
updated: "2026-09-22"
related_prompts:
  - domain-negotiation/contexts/negotiation_salary_raise_promotion.md
  - domain-negotiation/preparation/negotiation_package_trade_design.md
  - domain-hr-management/people-ops/hr_compensation_banding.md
---

# Hiring Offer — Employer Side

**Objective:** Run the offer conversation from the employer's seat: band position decided
and justified **before** the call, package levers ranked by cost-to-you against
value-to-them, a stated walk-away, the internal-equity constraint made explicit as
something that outranks winning this candidate, a method for handling a competing offer
that does not involve bidding against a number you cannot see, and a close that does not
begin the employment relationship with a grievance.

This is the **mirror** of `negotiation_salary_raise_promotion.md`, which holds the
candidate's and the employee's seat. Same ceremony, opposite side of the table, different
constraints — you are negotiating against a band you must defend to the people already
inside it.

**When to Use:**
- A candidate has passed the loop and you are making or revising an offer.
- A candidate has countered and you need to decide what to move.
- A candidate has a competing offer.
- You are about to break a band to win someone and want to see the cost first.

**When NOT to use:**
- You hold the candidate's seat — that is
  `negotiation_salary_raise_promotion.md`.
- You are designing the band structure itself — that is
  `../../domain-hr-management/people-ops/hr_compensation_banding.md`. Do that first; this
  prompt negotiates within bands and cannot substitute for having them.
- You are negotiating a **separation** package — that is
  `../../domain-legal/employment-labor/legal_employment_offer_and_separation_package.md`.
- You are negotiating a contractor rate — route to
  `../../domain-finance/corporate-finance-fpa/finance_subcontractor_margin_model.md` for
  the economics and `../contexts/negotiation_vendor_procurement_buyside.md` for the
  conversation.
- You need general offer-design mechanics rather than this context — see
  `../preparation/negotiation_opening_offer_design.md` and
  `../preparation/negotiation_package_trade_design.md`, which this prompt applies rather
  than repeats.

---

## Context Gathering

1. **Your position**
   - "The band for this level: minimum, midpoint, maximum." (from
     `hr_compensation_banding.md`)
   - "Where do current holders of this level sit, and what did the most recent hire get?"
   - "What is your approval authority, and whose sign-off is needed above it?"
     (`../at-the-table/negotiation_authority_mandate_limits.md` owns this discipline)

2. **The candidate**
   - "What did the loop conclude — hire, hire at a different level, or hire with
     reservations?"
   - "What have they said about compensation, timing, and what matters to them?"
   - "What do you know about their current situation — commute, flexibility, equity they
     would forfeit, notice period?"

3. **The alternatives, both ways**
   - "Who else is in the pipeline for this role, and how far along?"
   - "What does it cost you to keep looking — time, vacancy cost, the work not getting
     done?"
   - "What is their alternative, as far as you actually know?"

4. **The levers**
   - "Which of these can you actually move: base, bonus, equity, start date, title,
     level, signing payment, relocation, learning budget, remote arrangement, extra
     leave, review timing?"

The vacancy-cost question is the one employers most often skip, and it is what makes the
walk-away honest. If the role being empty for another two months costs more than the
gap you are arguing about, that is worth knowing before you refuse it.

---

## Method

### Step 1 — Decide the band position before the conversation

Write it down first: minimum, target, and maximum for **this candidate**, with the
justification for each against the band. Deciding while talking to a specific person is
how bands become decorative, and how the person hired last quarter ends up underpaid by
comparison.

| | Figure | Justification against the band |
|---|---|---|
| Opening | | |
| Target | | |
| Maximum | | |
| **Walk-away** | | |

The walk-away is the number above which you would rather keep looking. It follows from
the vacancy cost and the pipeline, not from irritation.

### Step 2 — Make internal equity an explicit constraint

**This is the constraint that outranks winning this candidate, and it is the one most
often sacrificed in the moment.**

Before moving above target, check: what does this do to the people already at this level?
Pay transparency legislation, published ranges and simple conversation mean compression
is discovered. The cost of breaking a band is not the increment to one person — it is the
increment plus the corrections you will owe everyone it compresses, plus the credibility
of the band structure itself.

| If we offer [x] | Who becomes compressed | Cost to correct | Total real cost |
|---|---|---|---|

Run that table before agreeing anything above target. It frequently converts an
apparently small concession into a five-figure decision, which is the honest arithmetic.

If you break the band deliberately, record why — a genuinely scarce skill, a market that
has moved, a level mis-set. That record is what you will need at the next review, and it
should trigger a band review rather than remaining an exception.

### Step 3 — Rank the levers by cost to you against value to them

Not everything costs the same, and base salary is the most expensive lever because it
compounds through every future increase, every bonus percentage, and every pension
contribution.

| Lever | Cost to you | Typical value to them | Sets a precedent? |
|---|---|---|---|
| Base salary | High — compounds and sets internal comparators | High | Yes, strongly |
| Signing payment | One-off; can be clawback-protected | High if replacing forfeited equity | Weakly |
| Equity | Dilutive but not cash; long payoff | Varies enormously by stage and literacy | Moderate |
| Bonus target | Variable; conditional | Moderate | Moderate |
| Start date flexibility | Usually free | Sometimes decisive | No |
| Extra leave | Low cash cost | High for some, irrelevant for others | Moderate |
| Remote or hybrid arrangement | Low, if the policy allows | Frequently the highest-value lever | Yes, if outside policy |
| Title | Free in cash; expensive if the level is wrong | Varies | Yes — and levelling errors are costly |
| Learning or equipment budget | Low | Moderate | No |
| Early review date | Free now, commits later | High for someone taking a below-target base | Moderate |

Two notes. **Title is not free** if it implies a level the person is not at — you have
bought agreement now and created a levelling problem, a compression problem and a
promotion problem later. And the **early review date** is the most under-used lever:
"below target now, with a formal review at six months against these criteria" is honest,
cheap, and genuinely attractive to a candidate who believes they will exceed the bar —
provided you put the criteria in writing and honour the date.

Use `../preparation/negotiation_package_trade_design.md` to build the trades.

### Step 4 — Handle the competing offer without bidding blind

You cannot verify a competing offer and should not demand proof. Three legitimate
responses:

- **Ask what would make the decision easy**, rather than asking for the number. The
  answer is often not the number, and is often something cheap.
- **Compete on the dimension you can win.** If their alternative pays more, do not try to
  match it — name what you offer that it does not: scope, the specific work, the team,
  flexibility, the trajectory.
- **State your position once and hold it.** "This is the top of the band for this level.
  I would rather be honest than start you here and have you find out in six months that
  the band has a ceiling."

What to avoid: the escalating counter. Bidding against an unverifiable number teaches the
candidate that your first offer was not real, and it produces the hire who arrives
believing the process was a game — which shapes how they negotiate everything afterwards.

If they choose the other offer, say so gracefully and leave the door open. People come
back, and they talk.

### Step 5 — Close in a way the relationship survives

The offer conversation is the first management interaction of the employment, and the
candidate reads it as a preview. Three things to do:

- **Explain the basis, not just the number.** "This is at the midpoint of the band for
  this level, which is where we place someone with your scope; here is what moves
  someone within it." A candidate who understands the structure negotiates less and
  trusts it more.
- **Say what is fixed and why.** Honesty about a constraint is respected; vagueness about
  it is read as tactics.
- **Do not win the last point you could have conceded.** Extracting a final small
  concession from someone who is about to join you is a bad trade: you gain a fraction of
  a percent and start the relationship with them feeling squeezed.

And put it in writing the same day, matching exactly what was said. A written offer that
differs from the conversation is the fastest way to lose someone at the last step.

### Step 6 — Record it for the band

Every negotiated offer is band data. Record the opening, the close, what moved, and why —
feeding `hr_compensation_banding.md`'s compression audit. Offers negotiated without a
record are how a band structure drifts into fiction.

---

## Output Format

```markdown
## Offer negotiation — [candidate], [role], [level]

### Decided before the call
| | Figure | Justification against the band |
|---|---|---|
| Opening | | |
| Target | | |
| Maximum | | |
| **Walk-away** | | |

Band: min [x] / mid [x] / max [x] · Current holders at this level: [x]
Approval authority: mine to [x]; above that [who]
Vacancy cost per month: [x] · Pipeline alternatives: [x]

### Internal equity check
| If we offer | Who becomes compressed | Cost to correct | Total real cost |
|---|---|---|---|
**Verdict:** [within band / breaking band deliberately because ... → triggers band review]

### Levers, ranked
| Lever | Available? | Cost to us | Expected value to them | Precedent |
|---|---|---|---|---|

**Offer first:** [the cheap, high-value levers]
**Hold:** [base above target]

### Competing offer
Claimed: [what they said] · Verification: **not requested**
Response: [what would make the decision easy / compete on our dimension / hold and explain]

### Close
Basis explained: [how the number was arrived at]
Fixed and why: [x]
Written offer sent: [date — matching the conversation exactly]

### Recorded for the band
Opened [x] · closed [x] · moved on [levers] · reason [x] → `hr_compensation_banding.md`
```

---

## Verification

- [ ] Opening, target, maximum and walk-away were written down before the conversation
- [ ] Each figure is justified against the published band
- [ ] The walk-away follows from vacancy cost and pipeline, not from irritation
- [ ] The internal-equity table was run before offering above target
- [ ] Any band break is deliberate, recorded with a reason, and triggers a band review
- [ ] Levers are ranked by cost to you against value to them
- [ ] Title is not being used to substitute for money at a level the candidate is not at
- [ ] No escalating counter against an unverifiable competing offer
- [ ] No proof of a competing offer was demanded
- [ ] The basis of the number was explained, not just the number
- [ ] No final small concession was extracted from someone about to join
- [ ] Written offer matches the conversation and went out the same day
- [ ] The outcome was recorded as band data

**False-positive prevention.** The dominant failure is the escalating counter. It feels
like winning the candidate and it does three things: teaches them the first offer was
theatre, breaks the band for everyone already inside it, and starts the relationship on
the premise that pressure works. Decide the maximum before the call and hold it — and if
you find yourself above it, stop and run the internal-equity table rather than
continuing.

The second failure is treating internal equity as a soft concern. It is the hardest
constraint in the conversation, because the cost of breaking it is not the increment to
this person — it is that increment plus every correction it triggers plus the credibility
of the structure. Compute it.

The third is title inflation as a cash substitute. It resolves today's conversation by
creating a levelling error, and levelling errors surface at the first review, the first
promotion cycle and the first time two people compare notes.

The fourth is asking for proof of a competing offer. It signals distrust at the moment
you are asking someone to trust you, it is usually unverifiable anyway, and it changes
nothing about what you can offer.

The fifth is a written offer that differs from the conversation — a different bonus
basis, a start date nobody agreed, a clause not mentioned. It reads as bad faith even
when it is administrative error, and it is the most avoidable way to lose a candidate at
the final step.

---

## Related

- `negotiation_salary_raise_promotion.md` — the candidate's and employee's seat; the mirror of this
- `../preparation/negotiation_package_trade_design.md` — building the trades
- `../preparation/negotiation_opening_offer_design.md` — general opening-offer mechanics
- `../at-the-table/negotiation_authority_mandate_limits.md` — knowing and stating your mandate
- `../../domain-hr-management/people-ops/hr_compensation_banding.md` — the band this negotiates within, and the audit this feeds
- `../../domain-hr-management/hiring/hr_sourcing_outreach.md` — where the range was first disclosed
