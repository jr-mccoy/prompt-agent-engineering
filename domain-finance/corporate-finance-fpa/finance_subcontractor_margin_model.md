---
title: "Subcontractor Margin Model"
category: corporate-finance-fpa/services-practice
description: "Model the economics of delivering client work through subcontractors — gross and net margin after management load, payment-timing exposure from pay-when-paid mismatch, the utilization break-even on a bench, and the margin floor below which subcontracting transfers risk without reward"
techniques:
  - RT-05
  - CM-02
  - OC-03
  - QA-08
  - MP-04
difficulty: advanced
tags:
  - services-practice
  - subcontracting
  - margin
  - working-capital
  - bench-risk
  - consulting
  - solo-operator
updated: "2026-09-21"
---

# Subcontractor Margin Model

**Objective:** Model what a practice actually earns when client work is delivered by
someone else: gross margin, margin net of the management load, the working-capital
exposure created by paying before being paid, and the utilization break-even on any
guaranteed commitment. The output is a margin floor and a maximum safe commitment.

**When to Use:** Use before agreeing a subcontract rate, before guaranteeing a
subcontractor minimum hours, and when deciding whether to scale a practice by adding
people rather than raising rates.

This is **distinct from** `../../domain-legal/employment-labor/solo_dev_contractor_management.md`,
which covers the management and legal side — when to outsource, writing scopes of
work, IP assignment, payment structures, quality control and 1099 treatment. That
prompt handles the relationship; this one handles the arithmetic, which that prompt
does not attempt. It is also distinct from the proposed flow-down review in
`../../domain-legal/contracts-transactional/legal_subcontractor_flow_down_check.md`,
which checks whether contractual obligations pass through correctly.

**Scope note.** As with `finance_services_rate_floor_model.md`, this is the
small-practice exception to this domain's institution-grade framing, following the
precedent of the two existing `solo_dev_*` finance prompts.

---

## Context Gathering

1. **The rates**
   - "What do you bill the client, per day or hour?"
   - "What do you pay the subcontractor?"
   - "Is either rate fixed for a term, or does it move?"

2. **The management load**
   - "Hours you spend per subcontractor-day on briefing, review, rework and client
     communication."
   - "Who fixes it when the work is not acceptable — you or them, and at whose cost?"
   - "What is your own rate? That is the opportunity cost of those hours."

3. **The payment timing**
   - "Client payment terms, and their actual behaviour — not the contract."
   - "Subcontractor payment terms. Do you pay on invoice or on client payment?"
   - "Is there a pay-when-paid clause, and is it enforceable in your jurisdiction?"

4. **The commitment**
   - "Have you guaranteed minimum hours or a retainer to the subcontractor?"
   - "If the client engagement ends, what do you still owe?"

5. **The risk**
   - "If the subcontractor's work is rejected, who bears the cost of redoing it?"
   - "Is your liability to the client capped at what you can recover from them?"

---

## Method

### Step 1 — Gross margin, per unit

```
Client rate                      Rc
Subcontractor rate               Rs
Gross margin                     Rc − Rs
Gross margin %                   (Rc − Rs) / Rc
```

This is the number people quote and the number that misleads, because it ignores the
cost of the work you still do.

### Step 2 — Load the management cost

```
Management hours per subcontractor-day    Hm
Your own effective rate per hour          Ro   (from the rate floor model)
Management cost per day                   Cm = Hm × Ro
Net margin per day                        Rc − Rs − Cm
Net margin %                              (Rc − Rs − Cm) / Rc
```

`Ro` should be your **floor** rate, not your walk-away rate: the hours spent managing
a subcontractor are hours not spent on billable delivery, so their opportunity cost
is what that time would otherwise have earned at your standard basis.

A common result is that a 30% gross margin becomes a 5–10% net margin once two hours
per day of review are priced in. That is the finding this model exists to produce.

### Step 3 — Compute the working-capital exposure

The structural risk of subcontracting is paying out before being paid in.

```
Client days-to-pay (actual)      Dc
Subcontractor days-to-pay        Ds
Funding gap (days)               Dg = Dc − Ds
Peak exposure                    Rs × subcontractor-days in flight × (Dg / period)
```

State the peak exposure in money and compare it to available cash. A practice with
£40k of peak exposure and £15k of cash is not running a margin business; it is
running a credit business with a margin attached, and a single late-paying client
breaks it.

Where a pay-when-paid clause exists, check whether it is enforceable in the relevant
jurisdiction before relying on it — in several it is unenforceable or narrowly
construed, and the practice pays regardless. This is a question for a lawyer, not an
assumption.

### Step 4 — Compute the break-even on any guaranteed commitment

If minimum hours or a retainer have been guaranteed:

```
Guaranteed cost per period       Cg
Net margin per billed day        Mn
Break-even billed days           Cg / Mn
Break-even utilization           (Cg / Mn) / days available in period
```

Above that utilization the commitment earns; below it, the bench is funded from
margin earned elsewhere. State the break-even utilization explicitly, because a
guarantee is a fixed cost in a business whose revenue is not fixed.

### Step 5 — Set the margin floor and the maximum commitment

- **Margin floor** — the net margin below which subcontracting is not worth doing.
  It must at minimum compensate for: the delivery risk you retain, the liability you
  carry to the client for someone else's work, the working-capital funding, and the
  management time. Practices commonly find the floor sits at 25–35% net, well above
  the gross margin that felt acceptable.
- **Maximum commitment** — the largest guarantee whose break-even utilization you can
  cover from committed work alone, not from pipeline. Guarantees covered by pipeline
  are guarantees covered by hope.

### Step 6 — Name the risk transfer, honestly

State in one line what you are being paid to absorb. If the net margin does not
exceed the margin floor, the arrangement transfers risk to you without compensating
for it, and the honest options are to raise the client rate, lower the subcontractor
rate, reduce the management load through better briefing, or introduce the
subcontractor to the client directly for a referral fee.

---

## Output Format

```markdown
## Subcontractor economics — [engagement / subcontractor]

### Per-day margin
| Line | Value |
|---|---|
| Client rate | |
| Subcontractor rate | |
| Gross margin | / [x]% |
| Management hours per day | |
| Your rate (floor basis) | |
| Management cost | |
| **Net margin** | / [x]% |

### Working capital
| Line | Value |
|---|---|
| Client days-to-pay (actual) | |
| Subcontractor days-to-pay | |
| **Funding gap** | [days] |
| Days in flight | |
| **Peak exposure** | [money] |
| Available cash | |
| Pay-when-paid clause | [present / absent] — enforceability [confirmed / unverified] |

### Guaranteed commitment
| Line | Value |
|---|---|
| Guarantee per period | |
| Break-even billed days | |
| **Break-even utilization** | [x]% |
| Covered by committed work? | [yes / no — pipeline-dependent] |

### Verdict
- Margin floor: [x]% — actual [x]% → [clears / fails]
- Maximum safe commitment: [x]
- What you are paid to absorb: [one line]
- If it fails: [raise client rate / lower sub rate / cut management load / refer out]
```

---

## Verification

- [ ] Management cost is priced at your floor rate, not omitted and not at cost.
- [ ] Client days-to-pay uses observed behaviour, not contractual terms.
- [ ] Peak exposure is compared to actual available cash.
- [ ] Any pay-when-paid reliance is flagged as requiring legal confirmation.
- [ ] Break-even utilization on guarantees is stated and tested against *committed*
      work, not pipeline.
- [ ] The margin floor accounts for retained liability, not only for time.

**False-positive prevention.** The characteristic error is judging the arrangement on
gross margin. Gross margin ignores the two costs that decide the outcome — your
review time and the funding gap — and a 30% gross margin business routinely nets
under 10%. Always compute net.

The second error is treating a guarantee as low-risk because the current engagement
covers it. Guarantees outlive engagements; that is what makes them guarantees. Test
the break-even against what is contractually committed beyond the current client.

The third is assuming a pay-when-paid clause protects you. Its enforceability varies
by jurisdiction and is frequently limited. Model the exposure as though you must pay
regardless, then treat any protection as upside.

**This is not legal or tax advice.** Worker-classification, flow-down enforceability
and pay-when-paid treatment are jurisdiction-specific. Confirm with a lawyer and an
accountant before relying on any of them.

---

## Related

- `finance_services_rate_floor_model.md` — supplies your own rate for the opportunity cost
- `finance_engagement_profitability_postcalc.md` — whether the modelled margin was realised
- `../../domain-legal/employment-labor/solo_dev_contractor_management.md` — the relationship and legal side
- `../../domain-legal/contracts-transactional/legal_subcontractor_flow_down_check.md` — obligation pass-through
- `../../domain-business-strategy/client-services/services_capacity_and_utilization_planner.md` — whether subcontracting is the right answer to a capacity constraint
