---
title: "Owned vs Rented — Deciding Where an Audience Lives, and What Each Choice Costs"
category: business-strategy/creator-economy
description: "A decision prompt for where a creator's audience should live: applies the existing ORB framework and platform selection guide to one situation, prices the switching cost of each option, names the failure each choice exposes you to, and produces a defensible decision with a review trigger."
techniques:
  - DT-01
  - RT-05
  - DS-06
  - CM-02
  - QA-04
difficulty: intermediate
tags:
  - platform-risk
  - owned-audience
  - decision
  - creator-economy
  - distribution
  - switching-cost
updated: "2026-09-22"
related_prompts:
  - domain-business-strategy/creator-economy/creator_list_growth_plan.md
  - domain-business-strategy/creator-economy/creator_community_operations.md
  - domain-risk/risk_dependency_chain_audit.md
---

# Owned vs Rented

**Objective:** Decide where an audience lives, with the switching cost of each
option priced and the specific failure each choice exposes you to named — and a
trigger that says when to revisit.

**This prompt decides; it does not invent frameworks.** Two already exist and
must be **cited rather than restated**:

- **ORB (Owned / Rented / Borrowed)** —
  `domain-agentic-resources/skills/marketing/launch-strategy/`, "The ORB
  Framework". Use its definitions.
- **Platform Selection Guide** —
  `domain-agentic-resources/skills/marketing/community-marketing/`. Use its
  per-platform characteristics.

If this prompt's output restates either, it has done the wrong job.

**When to Use:**
- You are choosing where to build: email, a platform, a community host, a site.
- One platform is producing most of your reach and you want the exposure priced.
- You are considering moving, and need the cost of moving rather than the
  attraction of the destination.
- An algorithm change or a policy change just cost you reach.

**When NOT to use:**
- You need launch-channel planning — `skills/marketing/launch-strategy/` owns
  the five phases and the ORB application to a launch.
- You need to compare community platforms feature by feature —
  `skills/marketing/community-marketing/`'s Platform Selection Guide.
- You need a general single-point-of-failure audit across a whole business —
  `domain-risk/risk_dependency_chain_audit.md` owns blast radius × replacement
  difficulty.
- You need paid-channel targeting — `skills/marketing/paid-ads/`.

## Inputs / Context

1. **Where the audience is now**, by size and by *reach actually delivered*, not
   follower count.
2. **Which surfaces produce what** — reach, subscribers, revenue, inbound.
3. **What you would lose tomorrow** if each surface disappeared, in concrete
   terms: revenue, inbound, the work itself.
4. **Effort per surface per week.**
5. **What the audience is for** — product, services, a body of work.
6. **Constraints** — anonymity, employer rules, budget, technical skill, the
   audience's own habits.
7. **Any prior incident**: a ban, a reach collapse, a policy change.

## Method

1. **Classify every surface with ORB, citing the framework (DT-01).**
   Owned: you hold the contact and can leave. Rented: you hold an account on
   someone else's terms. Borrowed: someone else's audience, at their discretion.
   Most creators misclassify one surface here — a hosted newsletter platform with
   exportable addresses is owned; the same platform's recommendation network is
   borrowed.

2. **Price the switching cost of each surface (DS-06).**
   Not "could I move" but what moving costs:
   - what fraction of the audience follows (state the basis — a comparable, a
     past move, or an assumption);
   - hours to migrate;
   - what breaks (archives, search, links, integrations);
   - what is unrecoverable.
   A surface with an unpriced switching cost is being treated as owned whether or
   not it is.

3. **Name the failure each choice exposes you to (RT-05).**
   For each option, the specific bad day: a ban with no appeal, an algorithm
   change, a pricing change, a platform closing, a deliverability collapse,
   your own inbox provider deciding you are spam. Owned is not riskless — it is
   a *different* risk, and a plan that treats email as safe has stopped thinking.

4. **Decide, and state what the decision is not.**
   One primary surface, an explicit second, and everything else demoted. Say
   which surfaces you are choosing to under-invest in; a decision that adds a
   platform without dropping one is an hours problem disguised as a strategy.

5. **Set a review trigger (QA-04).**
   Not a date — an observable: reach on the primary surface falls below X for
   two consecutive months, a policy change, the second surface overtakes the
   first. A calendar review gets skipped; a trigger fires.

## Output Format

```
# Where the audience lives — decision

## Surfaces today
| Surface | ORB class (per launch-strategy) | Audience | Reach delivered | Effort/wk | Produces |
|---|---|---|---|---|---|

Misclassification found: [which surface was being treated as owned and is not]

## Switching cost
| Surface | % who follow | Basis | Hours | What breaks | Unrecoverable |
|---|---|---|---|---|---|

## The failure each option exposes you to
| Option | The bad day | Likelihood basis | What it costs |
|---|---|---|---|

## Decision
Primary: [surface] — because [...]
Second: [surface] — role: [...]
Demoted / dropped: [surfaces], and the hours that frees: [n]

What this decision is NOT: [the thing someone would wrongly read into it]

## Review trigger
Revisit when: [observable condition], not on a date.

## Open questions
- [unresolved, and what it blocks]
```

## Verification

- [ ] ORB is cited, not restated; the same for the Platform Selection Guide.
- [ ] Every surface is classified, and any misclassification is called out.
- [ ] Switching cost is priced for every surface, with the basis of the
      follow-rate labelled.
- [ ] The failure mode of the *owned* option is named, not just the rented ones.
- [ ] The decision names what is dropped and the hours it frees.
- [ ] The review trigger is observable, not a date.

## False-Positive Prevention

1. **Owned is not safe, it is differently exposed.** Deliverability, provider
   policy and list decay are real. A plan that stops analysing once it reaches
   email has found a conclusion, not an answer.
2. **Follower count is not reach.** Classify and decide on delivered reach;
   follower counts are the number platforms show you because it flatters.
3. **"Exportable" is not "owned".** An exportable list you have never exported,
   into a destination you have not chosen, has an unpriced switching cost.
4. **Do not add a platform without dropping one.** Hours are the binding
   constraint, and a strategy that ignores them is a wish list.
5. **A past incident is evidence; a feared one is an assumption.** Label which
   is which in the likelihood column.
6. **Do not restate ORB or the platform guide.** If the output would stand alone
   without them, this prompt has duplicated two existing resources — the defect
   the repository's structure exists to prevent.

## Related

- `domain-agentic-resources/skills/marketing/launch-strategy/` — ORB, and its
  use in a launch.
- `domain-agentic-resources/skills/marketing/community-marketing/` — the
  Platform Selection Guide.
- `domain-risk/risk_dependency_chain_audit.md` — the general version of this,
  across a whole business.
- `creator_community_operations.md` — once you have chosen where a community lives.
