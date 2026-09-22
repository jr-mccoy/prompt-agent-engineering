---
title: "North-Star Metric Definition — One Number, Its Inputs, and What It Will Corrupt"
category: product-management/prompts
description: "Define a product north-star metric: a candidate set tested against five criteria, the input metrics that decompose it, a counter-metric for the behaviour it will distort, an explicit statement of what it excludes, and the instrumentation needed to compute it. Refuses vanity metrics, metrics that cannot be moved by the product team, and metrics shipped without a counter-metric."
techniques:
  - CM-02
  - RT-05
  - QA-04
  - QA-18
  - OC-03
difficulty: intermediate
tags:
  - metrics
  - north-star
  - product-analytics
  - counter-metrics
  - goodharts-law
updated: "2026-09-22"
related_prompts:
  - domain-product-management/prompts/product_opportunity_solution_tree.md
  - domain-AI-ML/problem-framing-scoping/mlframe_success_metric_selection.md
  - domain-business-strategy/startup/solo_dev_metrics_dashboard.md
---

# North-Star Metric Definition

**Objective:** Choose one product metric that represents delivered customer value,
decompose it into the inputs teams can act on, pair it with a **counter-metric** for the
behaviour it will inevitably distort, state what it deliberately excludes, and specify
the instrumentation required to compute it. Vanity metrics, metrics outside the product
team's influence, and metrics without a counter-metric are refused.

**When to Use:**
- Teams are optimising different numbers and the results conflict.
- Your headline metric is signups, page views or registered users.
- You need a root for an opportunity solution tree, or a target for a quarter.
- A metric is being gamed and you need to name what is happening.

**When NOT to use:**
- You are selecting a metric for a **machine-learning** system — that is
  `../../domain-AI-ML/problem-framing-scoping/mlframe_success_metric_selection.md`, which
  handles offline/online divergence, label quality and proxy risk in model evaluation. A
  platform-neutral product north-star is a different object.
- You need a dashboard built — that is
  `../../domain-business-strategy/startup/solo_dev_metrics_dashboard.md`.
- You need OKRs cascaded across an organisation — that is org scope, and
  `../../domain-presentations/board-decks/boarddeck_okr_cascade.md` renders the slide.
- You need the event taxonomy and tracking plan — that is
  `../../domain-agentic-resources/skills/marketing/analytics-tracking/`.

---

## Context Gathering

1. **The product's value exchange**
   - "What does a customer get from this product that they would miss if it vanished?"
   - "What do they have to do to get it?"
   - "When does a new customer first get it? How long does that take?"

2. **Current measurement**
   - "What is the headline number today, and who looks at it?"
   - "What is instrumented, and how reliably?"
   - "What has been gamed before?"

3. **The business model**
   - "How does customer value become revenue, and with what lag?"
   - "Is this transactional, subscription, marketplace, ad-supported, usage-based?"

4. **Scope of control**
   - "Which teams would be accountable for this number?"
   - "What else moves it that they do not control — seasonality, sales, pricing,
     partnerships?"

---

## Method

### Step 1 — Generate candidates from the value exchange

Three to five candidates, each expressed as a rate or a count of a **customer action
that represents received value**, not an action that represents intent.

| Product type | Weak candidate | Stronger candidate |
|---|---|---|
| Collaboration tool | Registered users | Weekly active *teams* with ≥3 members posting |
| Marketplace | Listings created | Completed transactions with both sides rated |
| Analytics product | Dashboards created | Dashboards viewed ≥3×/week by someone who did not build them |
| Learning product | Courses started | Learners completing a module and starting the next |
| Messaging | Messages sent | Conversations with a reply within 24h |

The pattern: the stronger candidate counts the moment the customer **got** something,
usually involves a second party or a repeat, and is harder to inflate.

### Step 2 — Test each candidate against five criteria

| Criterion | The question |
|---|---|
| **Represents value received** | Does moving it mean customers got more of what they came for — or only that they did more clicking? |
| **Movable by the product team** | Can the teams who will be held to it actually change it within a quarter? |
| **Leading, not lagging** | Does it move before revenue does? Revenue itself is an outcome, not a north star |
| **Computable now, or soon** | Is the instrumentation there? What is missing? |
| **Hard to game** | What is the cheapest way to move this number without helping a customer? |

Score each candidate against all five and show the table. A candidate failing
"movable" is the commonest trap: it is often the most meaningful number and it belongs
on the business dashboard, not as the product team's north star, because holding a team
to a number they cannot move produces cynicism rather than focus.

### Step 3 — Decompose into input metrics

The north star is for alignment; the inputs are for action. Decompose so the parts
relate to the whole by a stated arithmetic — usually multiplicatively.

```
North star = (reach) × (activation rate) × (frequency) × (breadth)
```

Each input gets an owning team. Three to five inputs. If teams cannot point at which
input they move, the decomposition is not yet usable.

State the relationship explicitly, because an unstated one invites double-counting when
two teams both claim the same movement.

### Step 4 — Define the counter-metric

**Every north star will be gamed. The counter-metric is how you find out.**

Answer step 2's gaming question, then choose a metric that moves in the wrong direction
if that happens:

| North star | Cheapest way to game it | Counter-metric |
|---|---|---|
| Weekly active teams | Nag emails driving hollow logins | Session depth; 8-week retention of newly active teams |
| Completed transactions | Pushing low-quality matches through | Dispute and refund rate; repeat-purchase rate |
| Dashboards viewed | Auto-opening dashboards on login | Views from a deliberate navigation; unique viewers |
| Module completions | Trivially easy modules | Assessment pass rate at the *next* module |
| Conversations with a reply | Auto-replies, bots | Human reply rate; conversation length |

A north star shipped without a counter-metric is an instruction to optimise a proxy, and
the optimisation will be found within two quarters. Define it now, publish it beside the
north star, and review them together.

### Step 5 — State what it excludes

Write down what this metric deliberately does not capture, so nobody has to discover it
by being punished. Common exclusions: the value delivered to non-users who benefit
indirectly, the quality of the experience for a small high-value segment, long-horizon
trust effects, and work whose payoff sits beyond the measurement window.

Naming exclusions is what allows a team to argue for work the north star would not
reward. Without it, the metric quietly becomes the whole strategy.

### Step 6 — Specify the instrumentation and the review cadence

- The exact event or query definition, unambiguously enough that two analysts compute
  the same number.
- What is missing today and who will add it.
- The reporting cadence, and — separately — the cadence for reviewing whether the
  **metric itself** is still the right one. Annually is typical. A north star that
  outlives its product stage is the most expensive kind of wrong.

---

## Output Format

```markdown
## North-star metric — [product]

### Value exchange
Customers come for [value]. They get it when [moment]. Typical time to first value: [x].

### Candidates
| Candidate | Value received | Movable by team | Leading | Computable | Hard to game |
|---|---|---|---|---|---|

### Chosen
**[Metric]** — precise definition:
> [unambiguous enough that two analysts agree]

Current value [x] · target [x] by [date] · owner [role] · cadence [x]

**Rejected, and why**
| Candidate | Failed on | Where it belongs instead |
|---|---|---|

### Inputs
```
North star = [input A] × [input B] × [input C]
```
| Input | Definition | Owning team | Current |
|---|---|---|---|

### Counter-metric
**Cheapest way to game the north star:** [the honest answer]
**Counter-metric:** [metric] — moves adversely if that happens
**Reviewed:** together with the north star, same cadence

### What this deliberately excludes
- [exclusion] — work serving it is justified on [other grounds]

### Instrumentation
| Needed | Exists? | Owner | By when |
|---|---|---|---|

### Metric review
Next review of whether this is still the right metric: [date]
```

---

## Verification

- [ ] Three to five candidates, each tested against all five criteria in a visible table
- [ ] The chosen metric counts value received, not intent
- [ ] The chosen metric is movable by the teams accountable for it
- [ ] The definition is unambiguous enough for two analysts to agree
- [ ] Inputs decompose the north star by a stated arithmetic relationship
- [ ] Every input has an owning team
- [ ] The gaming question is answered honestly, and a counter-metric is defined
- [ ] The counter-metric is published and reviewed alongside the north star
- [ ] Exclusions are written down
- [ ] Missing instrumentation is named with an owner and a date
- [ ] A date is set for reviewing the metric itself

**False-positive prevention.** The dominant failure is a metric that measures effort
rather than value — sessions, clicks, time in app, items created. Those rise when the
product becomes *harder*, which is the wrong direction, and they rise when marketing
spends more, which is not the product team's doing. Ask what the customer received; if
the answer is "they used the product", the metric is measuring activity.

The second failure is shipping without a counter-metric because gaming feels like
something other teams do. It is not a question of integrity: a team told to move a
number will find the cheapest path to moving it, which is what incentives do. The
counter-metric makes the cheap path visible rather than forbidden.

The third is a north star the team cannot move. Revenue, NPS and total customers are all
meaningful and all substantially outside a product team's quarterly control. They belong
on the business dashboard. Holding a team to them produces either cynicism or the
gaming above.

The fourth is an ambiguous definition. "Weekly active teams" splits three ways on the
first analyst question — does a team with one active member count, does a weekend count,
does an API call count? Write the definition so the answers are already in it.

---

## Related

- `product_opportunity_solution_tree.md` — takes this metric as its root
- `product_launch_readiness_gate.md` — checks the metric is instrumented before launch
- `../../domain-AI-ML/problem-framing-scoping/mlframe_success_metric_selection.md` — the ML-system counterpart
- `../../domain-business-strategy/startup/solo_dev_metrics_dashboard.md` — where it gets displayed
- `../../domain-agentic-resources/skills/marketing/analytics-tracking/` — the event taxonomy
