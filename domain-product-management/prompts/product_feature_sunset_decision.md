---
title: "Feature Sunset Decision — Evidence, Affected Users, Migration Path, and a Reversibility Check"
category: product-management/prompts
description: "Decide whether to remove a feature and how: usage evidence with the long-tail dependants identified, true carrying cost including what the feature blocks, contractual and accessibility obligations checked, a migration path for every affected segment, a communication timeline, and a stated point of no return. Refuses sunsets based on aggregate usage alone or with no migration path for dependent users."
techniques:
  - RT-05
  - CM-02
  - QA-04
  - QA-08
  - OC-03
difficulty: advanced
tags:
  - deprecation
  - sunset
  - product-lifecycle
  - migration
  - reversibility
updated: "2026-09-22"
related_prompts:
  - domain-product-management/prompts/product_north_star_metric_definition.md
  - domain-decision-making/decisioning_opportunity_sunk_cost_audit.md
  - domain-product-management/prompts/product_launch_readiness_gate.md
---

# Feature Sunset Decision

**Objective:** Decide whether a feature should be removed, and if so, how — from usage
evidence that identifies the **long-tail dependants** rather than stopping at an
aggregate, a carrying cost that includes what the feature blocks, a check of contractual
and accessibility obligations, a migration path per affected segment, a communication
timeline, and an explicit point of no return. Sunsets justified by low aggregate usage
alone, or with no migration path for dependent users, are refused.

**When to Use:**
- A feature has low usage and high maintenance cost and someone has proposed removing it.
- A rewrite or migration forces a keep-or-drop decision on old functionality.
- Two features overlap and one should go.
- Support burden or security exposure is concentrated in one old surface.

**When NOT to use:**
- You are deciding whether to *stop investing* while leaving it running — that is a
  roadmap decision, `product_planning_coding_roadmap.md`.
- You are retiring an **ML model** — that is
  `../../domain-AI-ML/production-monitoring/mlmonitor_model_portfolio_health_review.md`.
- You are auditing whether to abandon a *project* on sunk-cost grounds — that is
  `../../domain-decision-making/decisioning_opportunity_sunk_cost_audit.md`, which this
  prompt cross-references for the reasoning-hygiene half.
- You are shutting down an entire product or company — larger decision, different
  obligations, take advice.

---

## Context Gathering

1. **Usage, disaggregated**
   - "Monthly active users of the feature — and the distribution, not the total."
   - "Who are the heaviest 20 users? What accounts are they on? What is their value?"
   - "Is usage declining, flat, or seasonal? Over what window?"
   - "Is it used more by any single segment, region, or accessibility need?"

2. **Cost of carrying it**
   - "Engineering time in the last four quarters — maintenance, incidents, security
     patching."
   - "Does it block anything? A framework upgrade, a schema change, a rewrite?"
   - "Support ticket volume attributable to it."
   - "Infrastructure cost, if separable."

3. **Obligations**
   - "Is it named in any contract, SLA, order form or public commitment?"
   - "Is it part of an accessibility path — is it how some users accomplish the task at
     all?"
   - "Any regulatory or records-retention dependency?"
   - "Is it in a public API, or does anything integrate with it?"

4. **Alternatives**
   - "Is there another way in the product to accomplish the same thing? Is it as good?"
   - "What will the heaviest users do on the day it is gone?"

---

## Method

### Step 1 — Disaggregate the usage before anything else

**This is the step that prevents the characteristic mistake.** A feature used by 0.3% of
users can be load-bearing for the three accounts that constitute a quarter of revenue,
or the only route by which screen-reader users complete a core task. An aggregate
percentage hides exactly the information the decision needs.

| Cut | What to look for |
|---|---|
| By account value | Is any large account a heavy user? |
| By tenure | Is it used mostly by long-tenured customers who rely on it? |
| By segment / role | Is it concentrated in one job function? |
| By accessibility path | Is it how anyone accomplishes the task at all? |
| By frequency per user | A few users using it daily differs from many using it once |
| By integration | Does anything machine-consume it? |

Then name the dependants explicitly — the accounts, not the percentage. If they cannot
be named, the instrumentation is insufficient and the decision is premature.

### Step 2 — Compute the true carrying cost

Include the item most sunset cases omit: **what its existence prevents.**

| Cost | Value | Basis |
|---|---|---|
| Maintenance engineering (last 4 quarters) | | |
| Incidents attributable | | |
| Support tickets | | |
| Infrastructure | | |
| **Blocks** — the upgrade, migration or simplification it prevents | | |
| Security surface | | |
| Cognitive cost — does it confuse users of the newer path? | | |

A feature that is cheap to run and blocks nothing has a weak case for removal even at
low usage. A feature that is cheap to run and blocks a framework upgrade the whole
platform needs has a strong one. The blocking row usually decides it.

### Step 3 — Check the obligations, and stop if any bind

Four hard checks. Any of them can convert a product decision into a legal or compliance
one:

- **Contractual.** Named in a contract, order form, SLA or public roadmap commitment?
  Removing it may be a breach. Route to
  `../../domain-legal/contracts-transactional/legal_contract_review_full_redline.md` and
  take advice.
- **Accessibility.** If this is the only path by which some users complete the task, its
  removal may be a regression against accessibility obligations, not merely a product
  change. Check against
  `../../domain-agentic-resources/skills/accessibility/wcag-audit-patterns/`.
- **Regulatory or records.** Does anything require the data or the capability to remain
  reachable for a retention period?
- **Public API.** A documented endpoint carries a different deprecation contract from an
  internal UI affordance, usually including a stated notice period.

**This is not legal advice.** Where a check binds, the decision is no longer solely the
product team's.

### Step 4 — Design a migration path per segment

Not one path. For each dependant group identified in step 1:

| Segment | What they use it for | Where they go instead | Gap | Who helps them |
|---|---|---|---|---|

The **gap** column is the honest one. If a segment's replacement is worse, say how, and
decide whether that is acceptable — sometimes it is. A segment with no replacement and
no gap-closing work is a segment you are choosing to lose, and that should be a stated
decision with a number attached, not an oversight discovered at cutover.

A feature with dependent users and no migration path for any of them is refused here.
Either build the path, or make losing them an explicit priced decision.

### Step 5 — Choose the sunset mechanism

Ordered by user cost:

| Mechanism | When it fits |
|---|---|
| **Hide from new users, keep for existing** | Cheap, removes discovery cost, does not reduce maintenance. Good interim |
| **Read-only** | Data stays reachable; writes stop. Often right where records obligations apply |
| **Deprecate with a date** | Announced, notice period, then removed. The standard path |
| **Hard removal** | Only for security necessity or genuinely zero dependants |
| **Extract and hand over** | Open-source it, or hand it to the accounts that need it. Rare; occasionally elegant |

### Step 6 — Build the communication timeline and name the point of no return

| When | Who is told | Channel | Message |
|---|---|---|---|
| T−[n] | Heaviest users, individually, by a human | | |
| T−[n] | All affected users | in-product + email | |
| T−[n] | Support, sales, CS teams — *before* customers | | |
| T−[n] | Public changelog / docs | | |
| T | Removal | | |
| T+[n] | Data export remains available until | | |

Telling internal teams before customers is not politeness; a support agent who learns
about a removal from a customer cannot help them.

Then the **point of no return**: the date after which reversing costs more than
continuing. State it, and state what a rollback costs before and after. This is what
keeps the decision reversible while it still is, and it is the check that
`../../domain-decision-making/tradeoff_reversibility_stakes_grid.md` formalises.

### Step 7 — Define what would reverse it

Before starting, write down the signal that would stop the sunset: a named account
escalating, a usage spike, a dependency discovered, migration completion below a
threshold by a date. Deciding this in advance prevents both kinds of error — pressing on
through real evidence, and abandoning the plan at the first complaint.

---

## Output Format

```markdown
## Sunset decision — [feature]

### Usage, disaggregated
| Cut | Finding |
|---|---|
| Total MAU / % of base | |
| By account value | |
| By tenure | |
| By segment | |
| Accessibility path? | |
| Machine-consumed? | |

**Named dependants:** [accounts/users, explicitly — not a percentage]

### Carrying cost
| Cost | Value | Basis |
|---|---|---|
| **What it blocks** | | |

### Obligations
| Check | Result | Binding? | Route to |
|---|---|---|---|
| Contractual | | | |
| Accessibility | | | |
| Regulatory / records | | | |
| Public API | | | |

### Decision
**[Sunset via mechanism] / [Keep] / [Blocked pending obligation review]**
Because: [reason referencing cost, blocking, and dependants]

### Migration
| Segment | Uses it for | Goes to | Gap | Helped by |
|---|---|---|---|---|

**Segments with no path:** [named, with the decision to lose them priced]

### Timeline
| When | Who | Channel | Message |
|---|---|---|---|

**Point of no return:** [date] · rollback cost before [x] / after [x]

### What would reverse this
- [signal] → [action]
```

---

## Verification

- [ ] Usage is disaggregated across at least the six cuts, not reported as a total
- [ ] Dependants are named as accounts or users, not as a percentage
- [ ] Carrying cost includes what the feature blocks
- [ ] All four obligation checks are run and recorded
- [ ] Any binding obligation has stopped the decision and routed it
- [ ] Every dependant segment has a migration path, or an explicit priced decision to lose it
- [ ] The gap in each replacement path is stated honestly
- [ ] Internal teams are told before customers in the timeline
- [ ] Heaviest users are contacted individually by a human
- [ ] A point of no return is named, with rollback costs on both sides
- [ ] Reversal signals are written down before the sunset starts

**False-positive prevention.** The dominant failure is deciding from an aggregate. "Used
by 0.4% of users" is the sentence that precedes most bad sunsets, because it is
compatible with the feature being essential to your three largest accounts, the only
accessible route to a core task, or the integration point for a partner's product.
Disaggregate first; if the dependants cannot be named, the instrumentation is
insufficient and the decision is premature.

The second failure is an incomplete cost picture in either direction — building a case
purely from maintenance hours when the real argument is the migration it unblocks, or
keeping something because removal seems risky when it is quietly blocking a platform
upgrade. The blocking row is usually decisive; fill it in honestly.

The third is a single migration path for heterogeneous users. The power user with a
twelve-step workflow and the occasional user who clicked it once need different things,
and a generic "use the new dashboard instead" serves neither.

The fourth is skipping the accessibility check because the feature looks legacy. Older
surfaces are disproportionately the ones that work well with assistive technology,
precisely because they are simpler. If it is anyone's only route, removal is a
regression with obligations attached, not a cleanup.

---

## Related

- `product_north_star_metric_definition.md` — whether the feature moves anything that matters
- `product_launch_readiness_gate.md` — the mirror gate, at the other end of the lifecycle
- `../../domain-decision-making/decisioning_opportunity_sunk_cost_audit.md` — reasoning hygiene on abandonment
- `../../domain-decision-making/tradeoff_reversibility_stakes_grid.md` — formalising the point of no return
- `../../domain-legal/contracts-transactional/legal_contract_review_full_redline.md` — if a contractual obligation binds
