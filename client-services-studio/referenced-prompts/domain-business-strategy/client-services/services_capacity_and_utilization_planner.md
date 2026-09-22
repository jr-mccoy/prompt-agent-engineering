---
title: "Capacity and Utilization Planner"
category: client-services/operations
description: "Plan the billable capacity of a services practice — true sellable days after non-billable load, committed versus available capacity, the bench date each open opportunity is racing, and the utilization target that is sustainable rather than theoretical"
techniques:
  - CM-02
  - RT-05
  - OC-03
  - QA-08
  - MP-04
difficulty: intermediate
tags:
  - consulting
  - freelance
  - capacity-planning
  - utilization
  - pipeline
  - bench
  - solo-operator
updated: "2026-09-21"
---

# Capacity and Utilization Planner

**Objective:** Establish how many days you can actually sell, how many are already
committed, when you next run out of committed work (**the bench date**), and whether
the open pipeline can arrive in time to cover it. The output is a capacity picture
that makes the "should I take this?" question answerable with a date rather than a
feeling.

**When to Use:** Use monthly, and whenever an opportunity arrives that would consume
material capacity. It is the numerator behind every pricing and qualification
decision: a thin pipeline is why disqualification rules get overridden.

This is **distinct from** `../go-to-market/workflow_sales_pipeline_risk_assessment.md`,
which audits an open pipeline for stalled deals and winnability in a sales context.
That prompt asks "which deals will close?"; this one asks "will anything close
*before my bench date*, and what do I do if not?" — coupling pipeline to capacity and
to cash arrival. Where that prompt ranks deals, this one ranks them against a
calendar. Run that one first if the question is deal health; run this one if the
question is whether you are about to have an empty month.

All `capacity` and `workload` prompts elsewhere in this repository are GPU, infra,
sprint or study-load planning. None models human billable capacity.

---

## Context Gathering

1. **The raw calendar**
   - "Working days in the period, after holiday and known absence?"
   - "Any fixed commitments that are not client work — teaching, board, care?"

2. **The non-billable load**
   - "Hours a week on sales, proposals, invoicing, admin, bookkeeping?"
   - "Hours on your own learning, content, or tooling?"
   - "Be honest: how much of a 'billable day' is actually billable?"

3. **The commitments**
   - "Which engagements are signed, for how many days, over what window?"
   - "Which retainers reserve capacity whether or not consumed?"
   - "Any commitment that is verbal but real?"

4. **The pipeline**
   - "Open opportunities: size in days, expected start, your honest probability."
   - "For each: what has to happen for it to start, and who has to do it?"

The honest-probability question is the one that determines whether this exercise is
useful. Pipeline optimism is the default failure of every solo practice; if the
numbers come back with four opportunities all at 70%, challenge them against how many
of the last ten at that stage actually closed.

---

## Method

### Step 1 — Compute true sellable capacity

Work down, not up. Start from calendar days and subtract until you reach what can be
invoiced.

```
Calendar days in period
 − weekends, holiday, known absence            = available days
 − non-billable load (sales, admin, finance)   = sellable days
 − reserve for overrun on existing work        = committable days
```

The reserve is not optional. A practice that commits 100% of sellable days has no
capacity for the overrun that will happen, and pays for it out of evenings.
Five to fifteen per cent is the normal range; use your own estimate error from
`../../domain-finance/corporate-finance-fpa/finance_engagement_profitability_postcalc.md`
if you have it.

### Step 2 — Set the utilization target honestly

Utilization is billable days over sellable days. The important point: a sustainable
solo practice does not run at 90%. Sales, admin and recovery are the cost of being
the whole business, and they do not disappear when you are busy.

State the target, and state what it implies for the rate floor — because the rate
floor is computed *from* the utilization assumption. A target you cannot hold
produces a floor that is too low, which is the quiet mechanism by which busy
practices lose money.

### Step 3 — Lay committed work on the calendar and find the bench date

Place every signed commitment and reserved retainer capacity on a timeline. The
**bench date** is the first date after which committed days fall below your target.
It is the single most decision-relevant number this produces: it converts "I should
probably do some business development" into "I have six weeks."

### Step 4 — Race the pipeline against the bench date

For each open opportunity, record size, expected start, honest probability, and
**lead time** — the gap between agreement and first billable day. Lead time is
routinely underestimated: procurement, contracting and onboarding commonly add three
to eight weeks.

An opportunity only covers the bench date if `expected start + lead time ≤ bench
date`. Compute expected covered days as `size × probability` and compare to the gap.

Then state the verdict plainly in one of three forms:

- **Covered** — expected pipeline exceeds the gap with margin. Continue qualifying
  normally; your disqualification rules stay in force.
- **Thin** — pipeline covers the gap only if the optimistic cases land. Begin
  business development now; expect pressure on your rules.
- **Exposed** — no realistic combination covers the gap. Name the decision: accept a
  lower-fit engagement deliberately and on the record, cut cost, or use reserves.

Naming an exposure *in advance* is what allows a below-profile engagement to be a
deliberate commercial choice rather than a rule quietly abandoned.

### Step 5 — Test the next opportunity against capacity

For any specific opportunity, answer four questions before answering the client:

1. Does it fit inside committable days in its window, without touching the reserve?
2. What does it displace? Name the specific work that cannot then be taken.
3. If it overruns by your typical estimate error, what breaks?
4. What does it do to concentration? Cross-check
   `services_client_concentration_risk_check.md`.

---

## Output Format

```markdown
## Capacity — [period]

### Sellable capacity
| Line | Days |
|---|---|
| Calendar | |
| − absence | |
| = available | |
| − non-billable load | |
| = sellable | |
| − overrun reserve ([x]%) | |
| **= committable** | |

**Utilization target:** [x]% — [sustainable because / at risk because]

### Commitments
| Engagement | Days | Window | Type |
|---|---|---|---|

**Bench date: [date]** — [N] weeks out. Gap to cover: [days]

### Pipeline against the bench date
| Opportunity | Days | Prob | Expected start | Lead time | Covers bench? | Expected days |
|---|---|---|---|---|---|---|

**Verdict: [covered / thin / exposed]**
[If thin or exposed: the named decision, and by when it must be made]

### Next-opportunity test
| Question | Answer |
|---|---|
| Fits committable days? | |
| Displaces | |
| Survives typical overrun? | |
| Concentration effect | |
```

---

## Verification

- [ ] Sellable days are derived by subtraction from the calendar, not asserted.
- [ ] Non-billable load is a measured estimate, not a guess of "about a day a week."
- [ ] An overrun reserve exists and is greater than zero.
- [ ] The utilization target is consistent with the one used in the rate-floor model.
- [ ] Every pipeline entry has a lead time, and it is not zero.
- [ ] The verdict is one of the three named states, with a decision attached if not
      "covered."

**False-positive prevention.** The characteristic error is a capacity plan that says
"covered" because probabilities were set by hope. Sanity-check against history: of
your last ten opportunities at the stage these are at, how many closed, and how long
did they take to start? If the plan's implied close rate exceeds your actual one,
the plan is fiction and the bench date is earlier than stated.

The second error is omitting lead time, which makes every opportunity appear to cover
a bench date it will in fact miss by a month. If lead time is unknown, use eight
weeks and mark it assumed.

The third: treating the reserve as available when the month looks thin. The reserve
exists precisely for the month that looks thin. Consuming it converts an overrun into
a missed deadline on work already sold.

---

## Related

- `services_ideal_client_and_disqualifiers.md` — the rules that come under pressure when exposed
- `services_client_concentration_risk_check.md` — the portfolio view of the same commitments
- `../go-to-market/workflow_sales_pipeline_risk_assessment.md` — deal-level pipeline health
- `../../domain-finance/corporate-finance-fpa/finance_services_rate_floor_model.md` — consumes the utilization target
- `../../domain-personal-development/prompts/solo-dev/solo_dev_sustainable_pace_design.md` — whether the target is survivable
