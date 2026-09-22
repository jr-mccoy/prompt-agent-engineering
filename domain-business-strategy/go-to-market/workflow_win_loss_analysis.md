---
title: "Win/Loss Analysis — Interviews With the Buyer, Not the Seller's Account of Them"
category: business-strategy/go-to-market
description: "Run win/loss analysis that produces decisions: buyers interviewed by someone who was not on the deal, wins interviewed as rigorously as losses, the stated reason separated from the deciding reason, CRM loss codes treated as hypotheses rather than data, findings aggregated before action, and routing to whoever can actually fix each cause."
techniques:
  - RT-09
  - RT-05
  - CM-01
  - QA-04
  - OC-03
difficulty: intermediate
tags:
  - win-loss
  - sales-effectiveness
  - competitive-intelligence
  - buyer-research
  - go-to-market
updated: "2026-09-22"
related_prompts:
  - domain-business-strategy/go-to-market/workflow_sales_pipeline_risk_assessment.md
  - domain-business-strategy/research/research_competitive_landscape.md
  - domain-product-management/prompts/product_competitor_feature_teardown.md
---

# Win/Loss Analysis

**Objective:** Find out why deals were actually won and lost, from the **buyer**, and
convert it into changes someone owns. Output: interviews run by someone who was not on
the deal, wins examined as rigorously as losses, the stated reason distinguished from the
deciding reason, CRM loss codes treated as hypotheses, findings aggregated across deals
before anything changes, and each cause routed to the function that can fix it.

**When to Use:**
- Win rate is falling and the CRM says "price" on most losses.
- Sales, product and marketing each have a different theory about why deals are lost.
- A competitor is beating you and you only know the seller's account of why.
- You are about to change pricing, packaging or positioning and want evidence first.

**When NOT to use:**
- You need to audit the **open** pipeline for stalled deals, single-threading and
  winnability — that is `workflow_sales_pipeline_risk_assessment.md`, which looks
  forward at live opportunities. This looks backward at closed ones.
- You need a feature-by-feature comparison against named competitors — that is
  `../../domain-product-management/prompts/product_competitor_feature_teardown.md`.
- You need the market and competitor landscape — that is
  `../research/research_competitive_landscape.md` and
  `../../domain-agentic-resources/skills/marketing/competitor-profiling/`.
- You need customer research for product discovery among *existing* users — that is
  `../../domain-agentic-resources/skills/marketing/customer-research/`.
- You need to know why a *customer left* rather than never bought — that is churn, and
  `../../domain-agentic-resources/skills/marketing/churn-prevention/` plus
  `workflow_cs_account_health.md`.

---

## Context Gathering

1. **The deals**
   - "Closed-won and closed-lost in the last two to four quarters, with value, segment,
     competitor and recorded loss reason."
   - "Which had a competitive evaluation, and which were no-decision?"
   - "Sales cycle length for each, and where each stalled."

2. **What is recorded today**
   - "What loss reasons does the CRM offer? Who picks them, and when?"
   - "What proportion are 'price' or 'no budget'?"

3. **Access**
   - "Can you reach the buyers? Who has the relationship?"
   - "Is there anyone on the team who was not involved in these deals and could
     interview?"

4. **The competing theories**
   - "What does sales say the problem is? Product? Marketing? Leadership?"
   - Record these before interviewing — they are the hypotheses this tests, and writing
     them down first prevents the analysis quietly confirming whoever commissioned it.

The CRM question usually reveals the core problem. Loss reasons are typically selected by
the losing seller, from a short list, at the moment of losing — which makes "price" the
socially cheapest available answer. Treat the field as a hypothesis set, never as data.

---

## Method

### Step 1 — Interview wins as rigorously as losses

**The most common structural error is analysing only losses.** It produces a list of
deficiencies with no sense of what actually drives a yes, and it systematically
over-weights whatever losing buyers mention.

Wins tell you what to protect, which competitor claims did not land, and what nearly went
wrong. Interview both, in similar numbers.

### Step 2 — Have someone who was not on the deal do the interview

A buyer will not tell the seller that the seller was the reason. They will say price, or
timing, because those are kind and unarguable.

Use someone independent: a researcher, a product manager, a third party, or a colleague
from another team. If the organisation is too small for that, use written questions and
say plainly who will read the answers — and expect the ceiling on candour that implies.

Never let the account owner sit in.

### Step 3 — Separate the stated reason from the deciding reason

Two questions, in this order, and the gap between them is where the finding lives:

- **"What was the main reason you chose [X]?"** — the stated reason. Usually price,
  features, or timing.
- **"When did you actually decide? What was happening then?"** — the deciding moment.
  Frequently weeks before the stated reason came up, and frequently about something else:
  a slow response, a demo that did not show their use case, a champion who lost internal
  support, a security review that stalled.

Then the diagnostic follow-ups:

| Question | What it surfaces |
|---|---|
| "Who else was involved in the decision, and what did each of them care about?" | Whether you were single-threaded — usually the real cause |
| "What did you look at, in what order?" | Whether you were in the evaluation early or validating someone else's choice |
| "What did our competitor say about us?" | Competitive claims you may not know are being made |
| "What would we have had to do differently?" | Asked without defending |
| "What was confusing or slow in dealing with us?" | Process friction, which is cheap to fix and invisible internally |
| "Was price the reason, or was value the reason?" | The distinction that price-coded losses hide |

The last one matters. "Too expensive" almost always means the value case was not made,
not that the number was wrong — and those have opposite remedies. Discounting a
value-case failure trains the market to wait for discounts and fixes nothing.

### Step 4 — Classify the deciding cause, and keep no-decision separate

| Cause | Owned by | Fixable by |
|---|---|---|
| Value not established | Marketing / sales enablement | Positioning, proof, ROI case |
| Product gap — genuine | Product | Roadmap |
| Product gap — perceived | Marketing | Messaging, demo, documentation |
| Process friction | Sales ops | Cycle, security review, procurement paperwork |
| Wrong fit — should not have been in pipeline | Sales / marketing | Qualification, targeting |
| Single-threaded | Sales | Multi-threading discipline |
| Champion lost internal support | Sales | Building the internal business case with them |
| Competitor genuinely better for this buyer | Strategy | Segment choice, or accept it |
| Timing / budget disappeared | Nobody | Genuinely not winnable |
| Price above their ceiling at any value | Pricing / segment | Packaging or segment fit |

**Keep no-decision losses separate from competitive losses.** They have entirely
different causes: a buyer who chose a competitor rejected your offering, while a buyer who
did nothing failed to build an internal case. Merging them produces an average that
describes neither, and no-decision is frequently the largest bucket and the most
addressable.

Also flag **wrong-fit** losses distinctly. A high wrong-fit rate is not a sales problem;
it is a qualification or targeting problem, and the fix is upstream in
`../../domain-agentic-resources/skills/marketing/revops/` and the ICP.

### Step 5 — Aggregate before acting

**One lost deal is an anecdote.** A buyer's account is retrospective, partial, and
reconstructed after the fact, and sellers will bring you the one interview that supports
their existing theory.

Act when a cause appears across independent deals. Count by cause, by segment, and by
competitor, and weight by deal value — five small losses to process friction and one
large loss to a product gap are different problems.

| Cause | Deals | Value | Segment concentration | Competitor concentration | Threshold met? |
|---|---|---|---|---|---|

Then test the hypotheses recorded in step 1 explicitly: what sales believed, what product
believed, what the CRM said. Naming which theories the evidence did not support is the
most useful output the exercise produces, and the reason to write the theories down
beforehand.

### Step 6 — Route each cause to whoever can fix it, with an owner

A win/loss report with no owners changes nothing.

| Finding | Evidence | Route to | Owner | Action | By when |
|---|---|---|---|---|---|

Then close the loop: tell the sales team what the analysis found, including where their
theory was wrong and where it was right. A win/loss programme that collects from sellers
and reports only upward stops getting honest input within two cycles.

### Step 7 — Make it continuous

A one-off study ages out in two quarters. Interview a fixed proportion of closed deals —
all above a value threshold, a sample below — on a standing cadence, and re-aggregate
quarterly. The trend matters more than any single quarter's ranking.

---

## Output Format

```markdown
## Win/loss analysis — [period]

### Sample
| | Won | Lost — competitive | Lost — no decision | Total closed |
|---|---|---|---|---|
| Deals | | | | |
| Interviewed | | | | |
| Value | | | | |

**Interviewer:** [name] — *not on any of these deals*
**Hypotheses recorded before interviewing:** sales said [x] · product said [x] · CRM said [x]

### Per deal
| Deal | Outcome | CRM reason | Stated reason | **Deciding reason** | Decided when | Cause |
|---|---|---|---|---|---|---|

### Aggregated causes
| Cause | Deals | Value | Segment | Competitor | Threshold met? |
|---|---|---|---|---|---|

**Competitive losses vs no-decision, kept separate:** [counts]
**Wrong-fit rate:** [x]% → upstream qualification issue if elevated

### Hypotheses tested
| Theory | Held up? | Evidence |
|---|---|---|

### Competitive claims we did not know about
| Competitor | Claim | True? | Response |
|---|---|---|---|

### What wins look like
[what buyers who chose us said was decisive — the thing to protect]

### Actions
| Finding | Evidence | Route to | Owner | Action | By when |
|---|---|---|---|---|---|

### Reported back to sales on
[date] — including where their theory was not supported
```

---

## Verification

- [ ] Wins interviewed in similar numbers to losses
- [ ] The interviewer was not involved in any of the deals
- [ ] The account owner did not attend the interviews
- [ ] Stated reason and deciding reason are recorded separately for every deal
- [ ] "When did you decide?" was asked in every interview
- [ ] CRM loss codes are treated as hypotheses and compared against interview findings
- [ ] Competitive losses and no-decision losses are kept in separate buckets
- [ ] Wrong-fit losses are flagged and routed upstream to qualification
- [ ] Causes are aggregated by count, value, segment and competitor before any action
- [ ] The pre-recorded hypotheses are each explicitly tested
- [ ] Every finding has a route, an owner and a date
- [ ] Findings were reported back to the sales team
- [ ] A standing cadence is set, not a one-off study

**False-positive prevention.** The dominant failure is believing "price". It is the
socially cheapest answer for a buyer, the least blameworthy for a seller, and the default
in most CRM pick-lists — so it is over-represented at every layer. The separating
question is whether price or *value* was the issue: a buyer who says "too expensive"
almost always means the case was not made. Discounting in response trains the market and
fixes nothing.

The second failure is analysing only losses. It yields a deficiency list with no sense of
what drives a yes, and over-weights whatever losing buyers happened to mention. Wins
identify what to protect — and a change that fixes a loss cause while damaging a win
driver is a net loss you will not detect.

The third is letting the seller interview their own buyer. The buyer will be kind, and
the resulting report will confirm the seller's existing theory. Independence is not
optional here; it is the whole method.

The fourth is acting on one articulate loss. The buyer's account is retrospective and
partial, and sellers preferentially surface the interview that supports their view. Set a
threshold and hold it.

The fifth is merging no-decision with competitive loss. They share nothing causally — one
buyer rejected your offering, the other failed to build an internal case — and the
merged average recommends fixing neither.

---

## Related

- `workflow_sales_pipeline_risk_assessment.md` — the forward-looking counterpart, on open deals
- `../research/research_competitive_landscape.md` — the market view
- `../../domain-product-management/prompts/product_competitor_feature_teardown.md` — feature-level comparison
- `../../domain-agentic-resources/skills/marketing/sales-enablement/` — where value-case findings are fixed
- `../../domain-agentic-resources/skills/marketing/revops/` — where wrong-fit and qualification findings are fixed
- `workflow_cs_account_health.md` — post-sale health, a different question
