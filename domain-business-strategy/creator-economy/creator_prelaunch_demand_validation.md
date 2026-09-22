---
title: "Pre-Launch Demand Validation — Presell, Smoke Test, Paid Waitlist, and What Each One Proves"
category: business-strategy/creator-economy
description: "Test whether anyone will pay before building an information product: pick the instrument that matches the claim, set the kill number before running it, separate interest from commitment, and handle refunds and obligations honestly when the answer is no."
techniques:
  - RT-05
  - DS-06
  - DT-01
  - QA-04
  - OC-03
difficulty: intermediate
tags:
  - demand-validation
  - presell
  - smoke-test
  - waitlist
  - creator-economy
  - info-product
updated: "2026-09-22"
related_prompts:
  - domain-business-strategy/creator-economy/creator_list_growth_plan.md
  - domain-education-teaching/instructor/independent-course-creator/teaching_expertise_to_teachable_scope.md
  - domain-idea-to-product/stage-2-problem-validation/validation_customer_discovery_interview_protocol.md
---

# Pre-Launch Demand Validation

**Objective:** Decide whether to build an information product by getting
evidence that costs the buyer something — with the kill number written down
before the test runs, and the refund and obligation consequences of every
outcome settled in advance.

**When to Use:**
- You are about to spend six weeks building a course, cohort or paid community.
- A survey said people are interested and you want to know what that is worth.
- You want to run a presell, a smoke test or a paid waitlist and need to know
  which one answers your actual question.
- The audience is small and you cannot afford to spend it on the wrong offer.

**When NOT to use:**
- You need to interview people about a problem, before any offer exists —
  `domain-idea-to-product/stage-2-problem-validation/validation_customer_discovery_interview_protocol.md`
  owns discovery interviews.
- You need the launch itself — `skills/marketing/launch-strategy/` owns the five
  phases including Early Access.
- You need to scope what you would teach —
  `domain-education-teaching/instructor/independent-course-creator/teaching_expertise_to_teachable_scope.md`.
- You need pricing method — one-time digital-product pricing is a configuration
  of `skills/marketing/pricing-strategy/`, not a separate discipline.

## Inputs / Context

1. **The offer, in one sentence**, including the price. A validation test with no
   price tests nothing.
2. **The audience you can reach**, honestly: list size, delivered reach, and
   how much of it you are willing to spend on this.
3. **What you would build**, and the hours it costs. This sets what the test has
   to be worth.
4. **What you would do if the answer is no.** If the answer is "build it
   anyway", stop — you are not validating, you are seeking permission.
5. **Whether you can deliver** if it works, on the promised date.

## Method

1. **State the claim the test must support (RT-05).**
   Not "is there demand" but something falsifiable: *"At least N people from my
   list of M will pay £P before [date] for [offer] delivered by [date]."*

2. **Pick the instrument that matches the claim (DT-01).**

   | Instrument | What the buyer gives up | What it proves | What it cannot prove |
   |---|---|---|---|
   | Survey / interest form | nothing | that the topic is legible | that anyone will pay |
   | Free waitlist | an email address | mild interest, and list growth | willingness to pay |
   | **Paid waitlist / deposit** | a small refundable sum | commitment, at a lower threshold than full price | that they will pay the full price |
   | **Smoke test** (a real sales page, checkout disabled at the last step) | intent, and their time | that the offer converts from a page | that they would have completed payment |
   | **Presell** (full price, money taken, product not built) | the full price | willingness to pay, unambiguously | that you can deliver |

   A paid waitlist is an *instrument*, not a separate idea: it is the low-friction
   version of a presell, and it belongs here rather than in its own prompt.

3. **Set the kill number before running it (DS-06).**
   Three numbers, written down now:
   - **Go**: at or above this, build it.
   - **Kill**: at or below this, do not, and say what you do instead.
   - **Murky**: between them — and what you will do, decided now, because the
     murky band is where projects get built on a feeling.

   Derive them from arithmetic, not from a round number: what conversion rate
   would the launch need, and does this test clear it at the same rate?

4. **Handle the money honestly before you take any (OC-03).**
   - Presell: state the delivery date and what happens if you miss it. A presell
     with no refund policy is a promise you have not priced.
   - Smoke test: what the buyer sees at the last step matters. "Not available
     yet — here is what happens next" is honest; a fake error is not, and it is
     the thing that costs an audience.
   - Paid waitlist: whether the deposit applies to the price, and how it is
     refunded if you do not build.

5. **Read the result against the claim, not against your hopes (QA-04).**
   Report: who bought, from which part of the audience, and what the conversion
   rate was against *reach delivered*, not list size. Then state explicitly
   which of the three bands you landed in and what you are doing.

## Output Format

```
# Demand validation — [offer]

## Claim
At least [N] of [M] reachable people will [action] by [date] for [price].

## Instrument
Chosen: [presell | smoke test | paid waitlist]
Because the claim requires proving: [...]
What this instrument cannot prove: [...]

## Kill numbers (set before running)
| Band | Threshold | Action |
|---|---|---|
| Go | ≥ [n] | build, starting [date] |
| Murky | [n]–[n] | [decided now] |
| Kill | ≤ [n] | [what you do instead] |

Derivation: [the arithmetic, not the round number]

## Money and obligation
- Taken: [amount, when]
- Delivery promise: [what, by when]
- If missed: [refund terms]
- What the buyer sees at the last step: [exact wording]

## Result
| Reach delivered | Actions | Rate | Band |
|---|---|---|---|

Who bought: [which part of the audience]
Decision: [build / do not build / the murky action decided in advance]

## What this did NOT establish
- [the instrument's stated limit]
- [anything about a different audience, price or date]
```

## Verification

- [ ] The claim is falsifiable and names a number, a price and a date.
- [ ] The instrument's limits are stated, not just its result.
- [ ] Go / murky / kill thresholds were written **before** the test ran.
- [ ] The murky action is decided in advance.
- [ ] Refund and delivery terms exist before money is taken.
- [ ] The rate is computed against reach delivered, not list size.
- [ ] "What this did not establish" is filled in.

## False-Positive Prevention

1. **Interest is not demand.** A survey, a free waitlist and a lot of replies
   cost the respondent nothing. If the instrument takes nothing from the buyer,
   it has not tested willingness to pay, and the output must say so.
2. **A kill number set afterwards is not a kill number.** Written before, or the
   result will be interpreted to mean whatever you wanted.
3. **The murky band is where bad projects are born.** Decide it in advance or it
   resolves to "build it" every time.
4. **A smoke test that lies costs more than it proves.** A fake error message or
   a dead checkout teaches your audience that your links do not work. State the
   exact last-step wording in the plan.
5. **Presell revenue is a liability, not a win.** You owe a product. Count it as
   an obligation with a date, and price the refund risk.
6. **Do not extrapolate a launch from a test at a different price.** A deposit
   converting at 4% says nothing about a full-price launch converting at 4%.
7. **A small audience is not a failed test.** If reach was too small for the
   claim to be decidable either way, the result is "undecided" and the next step
   is `creator_list_growth_plan.md`, not building on a hunch.

## Related

- `creator_list_growth_plan.md` — when the honest answer is "not enough reach yet".
- `domain-education-teaching/instructor/independent-course-creator/teaching_expertise_to_teachable_scope.md`
  — what would actually be taught, before you sell it.
- `domain-agentic-resources/skills/marketing/launch-strategy/` — the launch, once
  the answer is yes.
- `domain-agentic-resources/skills/marketing/pricing-strategy/` — the price the
  test uses.
