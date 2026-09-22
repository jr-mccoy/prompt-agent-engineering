---
title: "Client Concentration Risk Check"
category: client-services/risk
description: "Measure and act on revenue concentration in a services practice — share by client, effective notice period, replacement time, and the compound exposure where one client is simultaneously the largest, the reference, and the referral source"
techniques:
  - RT-05
  - CM-02
  - OC-03
  - QA-08
  - NE-27
difficulty: intermediate
tags:
  - consulting
  - freelance
  - concentration-risk
  - revenue-risk
  - client-portfolio
  - solo-operator
updated: "2026-09-21"
---

# Client Concentration Risk Check

**Objective:** Measure how exposed a services practice is to the loss of any single
client — by revenue share, by capacity share, by effective notice, and by replacement
time — and convert the measurement into a limit with a named action when breached.

**When to Use:** Use quarterly, and before accepting any engagement that would grow
an existing client materially. It is the portfolio-level counterpart to the
single-client rule in `services_ideal_client_and_disqualifiers.md`.

This is **distinct from** `../../domain-finance/risk-management/finance_counterparty_risk_assessment.md`,
which assesses institutional credit exposure — counterparty default probability,
netting, wrong-way risk, collateral. This one measures *revenue* dependence in a
one-person or small practice, where the exposure is not that the client fails to pay
but that the client leaves and the practice has no bench. It is also narrower than
`../../domain-risk/risk_register_builder.md`, which is generic risk machinery; this
supplies the specific metric that machinery would otherwise lack.

---

## Context Gathering

1. **The revenue split**
   - "Revenue by client over the last twelve months, and forecast for the next twelve."
   - "Which are recurring, which are project-based?"
   - "Any client that is really several under one name, or several that are really
     one buyer?"

2. **The terms**
   - "Notice period on each engagement, in each direction."
   - "Which could end at the completion of current work, with no notice needed?"

3. **The replacement path**
   - "How long, historically, from deciding to find work to first billable day?"
   - "Where did your last three clients come from?"

4. **The compound exposures**
   - "Is your largest client also your main reference? Your main referral source?"
   - "Does any client's work make up most of your public portfolio?"
   - "Is the relationship with the company, or with one person inside it?"

The last question matters more than its length suggests. A large client held by a
single internal sponsor is a sponsor-sized risk, not a company-sized one, and
sponsors move.

---

## Method

### Step 1 — Measure share, three ways

Compute each, because they diverge and the divergence is informative:

- **Revenue share** — last twelve months and forward twelve.
- **Capacity share** — proportion of committable days held. A retainer that reserves
  capacity it does not consume is a larger capacity risk than a revenue risk.
- **Margin share** — proportion of contribution after delivery cost. A large client
  on a discounted rate can be a small margin contributor, which changes the answer.

Add the **Herfindahl index** — the sum of squared shares — as a single portfolio
number. Below ~0.15 is diversified; above ~0.25 is concentrated; above ~0.40 the
practice is effectively a dependent supplier to one buyer.

### Step 2 — Convert share into time at risk

Share alone understates the exposure. The number that matters is how long you are
exposed if the largest client leaves:

```
Exposure window = replacement lead time − effective notice
```

where effective notice is the *shorter* of the contractual notice and the natural end
of current work. A 90-day notice period on an engagement that completes in three
weeks provides three weeks of notice, not ninety days.

A positive exposure window is months of reduced revenue that must be covered by
reserves. State it in months and in money.

### Step 3 — Check the compound exposures

Concentration is worse than its number when one client holds several roles at once.
Score each:

| Role | Held by largest client? | If they leave |
|---|---|---|
| Largest revenue | | |
| Primary reference | | Pipeline conversion falls at the same moment revenue does |
| Referral source | | The replacement path closes as you need it |
| Portfolio centrepiece | | Positioning must be rebuilt |
| Capability anchor | | Your stated specialism loses its evidence |

Two or more roles in one client is a materially different risk from the revenue share
alone, because the failures correlate: you lose the income and the means of replacing
it in the same week.

### Step 4 — Set the limit and the action

A limit without a pre-agreed action is a number you will rationalise past. Write both:

- **Limit** — the share above which the next engagement with that client requires a
  deliberate decision. Common practice is 30–40% for an established practice with
  reserves; lower where reserves are thin.
- **Action on breach** — one of: decline the increment; accept with a compensating
  action (a business-development block booked in the same period, an extended notice
  clause, a deposit); or accept deliberately, recorded with a review date.

The third option is legitimate. A deliberate, dated, recorded acceptance of
concentration is a commercial decision; drifting past the limit without noticing is
not.

### Step 5 — Name the reduction path

If already over the limit, concentration reduces in only three ways: grow other
clients, reduce the large one, or extend the notice and build reserves to cover the
exposure window. Name which, with a date. "Diversify" is not a plan.

---

## Output Format

```markdown
## Concentration — [practice], [date]

### Shares
| Client | Revenue % (L12M) | Revenue % (F12M) | Capacity % | Margin % | Recurring? |
|---|---|---|---|---|---|

**Herfindahl index:** [x] — [diversified / concentrated / dependent]

### Exposure on largest client
| | |
|---|---|
| Contractual notice | |
| Natural end of current work | |
| **Effective notice** | |
| Replacement lead time | |
| **Exposure window** | [months] |
| Revenue at risk in that window | [amount] |
| Reserves cover | [months] |

### Compound exposure
| Role | Held? | Consequence |
|---|---|---|
**Roles held by largest client: [n]**

### Limit and action
- Limit: [x]% of [measure]
- Current: [x]% — [within / breached]
- Action: [decline / accept with compensation / accept deliberately, review [date]]

### Reduction path (if over)
[grow / reduce / extend-and-reserve] — by [date], measured by [metric]
```

---

## Verification

- [ ] Share is computed three ways, and divergences are noted rather than averaged.
- [ ] Effective notice uses the shorter of contractual notice and natural work end.
- [ ] The exposure window is expressed in both months and money, and compared to reserves.
- [ ] Compound roles are checked, not just revenue share.
- [ ] The limit has a named action; "monitor" is not an action.
- [ ] If over the limit, the reduction path names a mechanism and a date.

**False-positive prevention.** The most common error is reassurance from a long
contractual notice period. Notice only protects you if the engagement would otherwise
continue; on project work that is finishing anyway, the notice clause is inert.
Always compute effective notice.

The second is treating a group of related entities as separate clients. If one buyer,
one budget or one sponsor controls several engagements, they are one client for this
purpose. Concentration measured against the paying entity rather than the deciding
person systematically understates risk.

The third is measuring only revenue. A retainer holding 40% of capacity at 15% of
revenue is a capacity emergency disguised as a small account.

---

## Related

- `services_ideal_client_and_disqualifiers.md` — the per-opportunity concentration rule
- `services_capacity_and_utilization_planner.md` — the capacity-share input and the bench date
- `services_retainer_design_and_ceiling.md` — where single-client drift originates
- `../../domain-risk/risk_register_builder.md` — logging this alongside other practice risks
