---
title: "Engagement Profitability Post-Calculation"
category: corporate-finance-fpa/services-practice
description: "Close out a delivered engagement with an estimate-versus-actual reckoning — realised effective rate, where effort went against plan, which decisions caused the variance, and what the estimate error implies for the next quote and for fixed-price eligibility"
techniques:
  - RT-09
  - RT-05
  - QA-01
  - OC-03
  - DD-07
difficulty: intermediate
tags:
  - services-practice
  - profitability
  - estimate-variance
  - realized-margin
  - engagement-review
  - consulting
updated: "2026-09-21"
---

# Engagement Profitability Post-Calculation

**Objective:** Establish what an engagement actually earned — realised effective rate
against the floor, effort by phase against plan, the specific decisions that caused
the variance, and the updated estimate-error figure that the next quote and any
fixed-price decision depend on.

**When to Use:** Run at close-out of every engagement, before the details fade. This
is the prompt that makes every other pricing decision in the practice evidence-based:
the rate floor needs a measured overrun figure, and
`../../domain-business-strategy/client-services/services_productized_offer_designer.md`
cannot compute a coefficient of variation without a history of these.

**Deliberately combines the financial and the retrospective.** The repository already
has four post-mortem prompts — `../../domain-professional-writing/business-writing/business_writing_post_mortem.md`,
`../../domain-negotiation/after-the-deal/negotiation_post_negotiation_debrief.md`,
`../../domain-risk/risk_after_action_review.md`, and
`../../domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md`.
A fifth generic one would be the duplication this repository's structure exists to
prevent. What none of them does is close the financial loop: compute the realised
rate and feed the estimate error forward. That is what this adds, and the qualitative
retrospective should be run with one of the four above rather than repeated here.

This is **distinct from** `finance_budget_variance_investigator.md` (departmental
budget variance in an operating company) and `finance_unit_economics_model.md`
(product CAC/LTV).

---

## Context Gathering

1. **What was sold**
   - "Quoted fee, structure, and the effort estimate behind it."
   - "Scope as written: deliverables, assumptions, exclusions."
   - "Rate floor in force when it was quoted."

2. **What was delivered**
   - "Total hours or days actually spent, by phase where you have it."
   - "Unbilled time: rework, extra meetings, scope absorbed, admin specific to this client."
   - "Anything delivered that was not in scope."

3. **What was paid**
   - "Invoiced total versus quoted. Any write-off or discount?"
   - "Days from final invoice to payment. Any amount still outstanding?"

4. **Direct costs**
   - "Subcontractors, tools bought for this engagement, travel, licences."

5. **The decisions**
   - "Where did it first diverge from plan? What was the decision at that moment?"
   - "What did you agree to that was not in scope, and why?"

The unbilled-time question needs real pressure. It is the number most consistently
under-reported, and it is precisely the number that turns an apparently profitable
engagement into a marginal one.

---

## Method

### Step 1 — Compute the realised effective rate

```
Collected revenue                        R   (invoiced − write-offs − still unpaid)
Direct costs                             C
Net revenue                              Rn = R − C
Total effort, billed and unbilled        E   (days)
Realised effective day rate              Rr = Rn / E
```

Include unbilled effort in `E`. Excluding it produces the rate you wish you had
earned rather than the rate you earned.

Compare `Rr` against the three thresholds from
`finance_services_rate_floor_model.md`: standard, floor, walk-away.

### Step 2 — Decompose the variance

```
Effort variance   = actual effort − estimated effort
Rate variance     = quoted rate − realised rate
Scope variance    = effort on out-of-scope work
Collection variance = invoiced − collected
```

Attribute each to a cause, and be specific. "Scope creep" is not a cause; "agreed to
a second stakeholder review round in week three without a change order" is.

### Step 3 — Locate the divergence point

Name the first moment plan and reality parted, and the decision taken there. Almost
always a decision exists, and almost always it was made in a single message without
deliberation — an agreement to a small extra, an unchallenged assumption, an input
that arrived late and was absorbed rather than escalated.

Classify it:

| Class | Meaning | Fix |
|---|---|---|
| **Estimation** | The work was larger than understood | Better scoping, or a paid discovery phase |
| **Scope control** | Additional work absorbed without a change order | Change-order trigger discipline |
| **Input failure** | Client did not deliver an input on time | Input contract with consequences |
| **Delivery** | Rework, wrong approach, capability gap | Capability or process |
| **Commercial** | Discounted or structured badly at the outset | Pricing discipline |

The class determines what to change. Estimation failures are fixed by scoping; scope
control failures are fixed by change orders; confusing the two leads practices to pad
estimates when the real problem was never saying no mid-engagement.

### Step 4 — Update the estimate-error series

Append this engagement to the running series and recompute:

- Ratio actual/estimated for this engagement
- Median ratio across the series
- Range and coefficient of variation
- **Fixed-price eligibility**: a CV above ~0.40 means this engagement type should not
  be quoted fixed-price (see the productized offer designer); below ~0.25 it can be.

This series is the single most valuable financial artifact a services practice owns,
and it only exists if this prompt is run every time.

### Step 5 — Convert to three forward actions

Not a list of lessons. Three specific changes, each with the artifact it changes:

1. What changes in the **quote** — estimate basis, contingency, structure.
2. What changes in the **scope document** — a new assumption, exclusion or input
   requirement, stated in the words that would have prevented this.
3. What changes in **delivery** — a checkpoint, a checklist, an escalation trigger.

### Step 6 — Decide on the client

State plainly whether you would take this client again, and on what terms. Feed the
answer to `../../domain-business-strategy/client-services/services_ideal_client_and_disqualifiers.md`
— a disqualifier list that is never updated from close-outs is theory.

---

## Output Format

```markdown
## Close-out — [client], [engagement]

### Realised economics
| Line | Value |
|---|---|
| Quoted fee / structure | |
| Invoiced | |
| Write-offs / discounts | |
| Still outstanding | |
| Collected revenue | |
| Direct costs | |
| **Net revenue** | |
| Estimated effort | |
| Billed effort | |
| Unbilled effort | |
| **Total effort** | |
| **Realised effective rate** | |
| Against floor ([x]) | [above standard / above floor / between floor and walk-away / below walk-away] |

### Variance
| Type | Amount | Cause (specific) |
|---|---|---|

### Divergence point
**When:** [date / phase] · **Decision:** [what was decided]
**Class:** [estimation / scope control / input failure / delivery / commercial]

### Estimate-error series
| Engagement | Est | Actual | Ratio |
|---|---|---|---|
Median [x] · Range [x–x] · CV [x] · n = [x]
**Fixed-price eligible for this type:** [yes / with tight inputs / no]

### Three forward actions
1. Quote: ...
2. Scope document: ...
3. Delivery: ...

### Client verdict
[repeat / repeat on different terms: ... / decline] — feeds disqualifier list: [signal]
```

---

## Verification

- [ ] Unbilled effort is included in total effort.
- [ ] Revenue is *collected*, not invoiced; outstanding amounts are excluded, not assumed.
- [ ] Every variance line has a specific decision as its cause, not a category label.
- [ ] The divergence point names an actual moment and an actual decision.
- [ ] The estimate-error series is updated and the CV recomputed.
- [ ] The three actions each name the artifact they change.

**False-positive prevention.** The dominant failure is a close-out that reports the
invoiced figure as revenue and the billed figure as effort, producing a healthy rate
that never existed. Both corrections must be made: collected, not invoiced; total
effort, not billed effort.

The second is attributing variance to the client. Clients request additional work;
that is normal and expected. The variance belongs to whoever agreed to it without a
change order. Attributing it outward produces no forward action, which is why the
same engagement recurs.

The third is running this only on engagements that went badly. The estimate-error
series is only meaningful if every engagement enters it, including the ones that went
well — those are what establish the lower bound of the range.

---

## Related

- `finance_services_rate_floor_model.md` — the thresholds this measures against, and the overrun figure it consumes
- `finance_subcontractor_margin_model.md` — where subcontracted delivery was involved
- `../../domain-business-strategy/client-services/services_productized_offer_designer.md` — consumes the CV
- `../../domain-business-strategy/client-services/services_ideal_client_and_disqualifiers.md` — consumes the client verdict
- `../../domain-risk/risk_after_action_review.md` — the qualitative retrospective to pair with this
