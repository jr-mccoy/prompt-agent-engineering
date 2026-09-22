---
title: "List Growth Plan — Channel Mix, Honest Rates, and the Arithmetic That Ends the Argument"
category: business-strategy/creator-economy
description: "Plan audience growth as arithmetic rather than hope: a channel mix costed in hours, a conversion rate per channel taken from your own data or marked as an assumption, compounding versus one-off sources separated, and a stated point at which a channel gets cut."
techniques:
  - DS-06
  - RT-05
  - CM-02
  - DT-01
  - QA-04
difficulty: intermediate
tags:
  - audience-growth
  - newsletter
  - channel-mix
  - cross-promotion
  - creator-economy
  - subscriber-acquisition
updated: "2026-09-22"
related_prompts:
  - domain-business-strategy/creator-economy/creator_newsletter_positioning_and_cadence.md
  - domain-business-strategy/creator-economy/creator_platform_choice_owned_vs_rented.md
  - domain-business-strategy/creator-economy/creator_prelaunch_demand_validation.md
---

# List Growth Plan

**Objective:** Turn "I need more subscribers" into a costed plan: which channels,
how many hours each, what each is assumed to produce, which of them compound,
and the number at which each gets cut.

**When to Use:**
- You have a newsletter or audience and no plan for growing it beyond posting.
- You are spending hours on channels and cannot say which one works.
- You are considering cross-promotion, referrals, or paid acquisition and need
  to compare them against each other rather than against zero.
- Growth has stalled and you need to know whether it is the offer, the channel,
  or the rate.

**When NOT to use:**
- You need the *lead magnet* itself — its offer, format and promise. That is
  `domain-agentic-resources/skills/marketing/lead-magnets/`, which owns the
  offer and explicitly hands the follow-up sequence to `email-sequence/`.
- You need the nurture sequence — `skills/marketing/email-sequence/`.
- You need to define what the newsletter *is* first —
  `creator_newsletter_positioning_and_cadence.md`. Growing a list with no
  promise produces subscribers who do not open.
- You are running paid acquisition on ad platforms — `skills/marketing/paid-ads/`
  owns targeting and budget split across five platforms.

## Inputs / Context

1. **Current list size and the last three months of net growth**, including
   unsubscribes. Net, not gross.
2. **Where current subscribers came from**, to whatever accuracy exists. "I
   don't know" is a finding, and step 1 addresses it.
3. **Hours per week available for growth**, separate from hours for writing.
4. **Existing surfaces** — a podcast, a talk, a repo, clients, a day job
   audience, an employer's platform.
5. **Any real conversion data**: visits to subscribers, a past cross-promotion,
   a referral experiment.
6. **What the list is for**, from the positioning work. A list for a paid
   product and a list for inbound consulting want different people.
7. **Constraints** — budget, anonymity, employer restrictions, platform bans.

## Method

1. **Establish the baseline, including attribution you do not have.**
   Net growth per month for three months, and the share of new subscribers whose
   source is unknown. If most sources are unknown, the first action is
   attribution, not growth — every later number is otherwise unfalsifiable.

2. **Separate compounding from one-off sources (DT-01).**

   | Type | Behaviour | Examples |
   |---|---|---|
   | Compounding | keeps producing without further hours | search, an evergreen artifact, a referral loop, a directory listing |
   | One-off | produces once, per unit of effort | a guest post, a podcast appearance, a launch, a talk |
   | Borrowed | produces while someone else's audience allows it | cross-promotion, a feature, a repost |

   A plan made entirely of one-off sources is a treadmill, and it will read as
   growth right up until you stop.

3. **Cost each channel in hours, then in subscribers per hour (DS-06).**
   For each channel: hours to set up, hours per week to maintain, expected
   subscribers, and — stated explicitly — whether that expectation comes from
   **your own data**, **a comparable you can name**, or **an assumption**.
   Mark assumptions. Most of them will be wrong, and the marked ones are the
   ones you can fix.

4. **Project three cases, and label them (QA-04).**
   Pessimistic, base, optimistic — each as arithmetic from the per-channel
   numbers, not as a growth-rate curve. State which inputs the spread is most
   sensitive to.

5. **Set a cut line per channel before you start (RT-05).**
   For each: how long it runs, what it must produce by then, and what happens if
   it does not. A channel with no cut line runs forever on the strength of the
   effort already spent.

6. **Sequence by compounding first, then by subscribers per hour.**
   Compounding channels are worth starting early even when their early rate is
   poor, because their rate is the only one that improves without you.

## Output Format

```
# List growth plan — [list name]

## Baseline
| Month | Gross adds | Unsubs | Net | Unknown-source share |
|---|---|---|---|---|

Attribution verdict: [adequate | the first action is attribution, because ...]

## Channel mix
| Channel | Type | Setup hrs | Hrs/week | Expected subs/mo | Basis | Cut line |
|---|---|---|---|---|---|---|
| ... | compounding/one-off/borrowed | | | | own data / named comparable / ASSUMPTION | by [date], ≥ [n] |

Total weekly hours: [n] — against [n] available.

## Three cases
| Case | 90-day net | Driven mostly by |
|---|---|---|
| Pessimistic | | |
| Base | | |
| Optimistic | | |

Most sensitive input: [which, and what a 50% error does to the base case]

## Sequence
1. [channel] — start now because [compounding / highest subs-per-hour]
2. ...

## What gets stopped
[what you are currently doing that this plan does not include, and why]

## Assumptions to convert into data
- [assumption] — cheapest way to test it: [...]
```

## Verification

- [ ] Baseline is **net**, including unsubscribes.
- [ ] Unknown-source share is stated, and drives the plan if it is large.
- [ ] Every channel is typed compounding / one-off / borrowed.
- [ ] Every expected rate is labelled own data, named comparable, or ASSUMPTION.
- [ ] Total weekly hours do not exceed hours available.
- [ ] Every channel has a cut line with a date and a number, set in advance.
- [ ] The plan names what gets **stopped**, not only what gets started.

## False-Positive Prevention

1. **Gross growth hides a leaking list.** A list adding 200 and losing 180 is
   not growing at 200. Always net.
2. **An unlabelled rate becomes a fact by Tuesday.** Anything not measured is
   an assumption and must be written as one; the labels are the difference
   between a plan and a forecast.
3. **Borrowed reach is not yours.** Cross-promotion and platform features work
   until the other party stops. Count them as borrowed, and never build the base
   case on them.
4. **A channel with no cut line never gets cut.** Sunk effort makes the decision
   for you later; make it now, in writing, with a date.
5. **Subscriber count is not the goal unless the list is the product.** If the
   list exists for a product or for inbound work, a smaller list of the right
   readers outperforms a larger one, and the plan should say which you are
   optimising.
6. **Do not compare your rate to a published benchmark.** Benchmarks come from
   lists with different offers, sizes and sources. Your own three months, however
   thin, is better evidence about you than someone else's average.

## Related

- `creator_newsletter_positioning_and_cadence.md` — the promise people subscribe to.
- `creator_platform_choice_owned_vs_rented.md` — where the audience actually lives.
- `domain-agentic-resources/skills/marketing/lead-magnets/` — the offer itself.
- `domain-agentic-resources/skills/marketing/referral-program/` — referral and
  affiliate mechanics, including the distinction between them.
