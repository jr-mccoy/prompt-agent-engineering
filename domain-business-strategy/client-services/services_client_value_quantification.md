---
title: "Client Value Quantification"
category: client-services/pricing
description: "Build the client-side economic model for an engagement — what the problem costs them per month, what a fix is worth, and which number they already track — producing the defensible value figure that anchors a price, with the attribution weaknesses stated"
techniques:
  - RT-05
  - CM-01
  - QA-01
  - OC-03
  - ED-05
difficulty: advanced
tags:
  - consulting
  - freelance
  - value-pricing
  - roi
  - business-case
  - anchoring
  - solo-operator
updated: "2026-09-21"
---

# Client Value Quantification

**Objective:** Build the **client's** economic model for the problem you would solve:
what it costs them now, per unit time; what a fix is worth; which of those numbers
they already track and would accept. The output is a defensible value figure with its
assumptions and attribution weaknesses exposed — the input a price anchors to.

**When to Use:** Use between discovery and pricing, when the engagement has a
plausible economic case and the client has not made it themselves. Its output feeds
`services_pricing_model_selector.md` as the ceiling.

This is **distinct from** `../../domain-personal-development/prompts/solo-dev/solo_dev_pricing_value_confidence.md`,
which operates at **self** scope: it produces *your* defensible number and the
confidence to hold it. This one operates on **the client's books** — it models their
cost of the problem, independent of what you charge, and is usable even when you
decide to bill a day rate. One is about your nerve; this is about their arithmetic.

---

## Context Gathering

Most of this comes from the client during discovery. Where it does not, the model
must mark the number as assumed and show the swing.

1. **The cost of the current state**
   - "How often does [the problem] happen? Over what period?"
   - "When it happens, who gets involved and for how long?"
   - "What does it stop from happening?"
   - "Has anyone put a number on it? Where did that number come from?"

2. **The numbers they already track**
   - "What goes on the dashboard your sponsor looks at?"
   - "Which of those has a target attached?"
   - "Who owns that number?"

3. **The counterfactual**
   - "If you do nothing for twelve months, what happens?"
   - "What else are you doing that could move the same number?"
   - "What have you already tried, and what did it cost?"

A client who cannot answer the counterfactual has not made the case internally, which
means your engagement will be competing for budget against projects that have. That
is a qualification signal as much as a pricing one.

---

## Method

### Step 1 — Pick the value mechanism, and pick one

Every services engagement creates value through one dominant mechanism. Model the
dominant one; mention the others as unquantified upside.

| Mechanism | Unit of measure | Typical evidence |
|---|---|---|
| **Cost avoided** | Incidents × cost per incident | Support tickets, outage minutes, rework hours |
| **Time recovered** | Hours × loaded rate × frequency | Process timings, headcount on the task |
| **Revenue enabled** | Deals or units × margin | Pipeline held up, launch date moved |
| **Risk reduced** | Probability × impact | Audit findings, contractual penalties, insurance |
| **Decision improved** | Size of the decision × error rate | Capital being committed on a shaky basis |

Stacking mechanisms inflates the number and destroys its credibility. One mechanism,
well evidenced, beats four stacked.

### Step 2 — Build the model at three settings

Never produce a single number. Produce three, and be explicit about the source of
each input:

| Input | Conservative | Expected | Optimistic | Source |
|---|---|---|---|---|

Mark every input as **client-stated**, **observed**, **industry reference class**, or
**assumed**. The proportion of assumed inputs is the credibility of the model. If
more than a third are assumed, the honest output is "we do not yet know enough to
value this" — which is itself a finding worth delivering.

### Step 3 — State attribution honestly

Attribution is where value cases die in front of a CFO. Answer three questions in
writing:

- **What else moves this number?** List every other factor. If seasonality alone can
  swing it more than your engagement would, say so.
- **How would anyone know it was you?** Name the measurement design — before/after,
  held-out comparison, or none.
- **What is the baseline, and is it recorded now?** A baseline measured after the
  fact is not a baseline. If it is not recorded, recording it becomes deliverable
  one.

### Step 4 — Convert to the client's own units

Translate into the unit the sponsor is accountable for. A number expressed as
"£180k/year of avoided rework" is weaker than "2.3 engineers of capacity returned"
if the sponsor is fighting for headcount. Same arithmetic, different decision.

### Step 5 — Derive the pricing band, and stop

The band is a ratio of the conservative figure, not the expected one. State the
conventional ranges and the reason:

- Fee at 10–20% of conservative annual value: an easy internal case, low scrutiny.
- Fee at 20–35%: defensible, expect the model to be examined.
- Fee above 35% of conservative value: requires the optimistic case to be believed,
  which means you are now selling the model rather than the work.

Then stop. This prompt produces the ceiling and its evidence. The structure is
`services_pricing_model_selector.md`; the floor is the rate-floor model.

---

## Output Format

```markdown
## Value case — [client], [problem]

**Dominant mechanism:** [one]
**Sponsor's own metric:** [name] — owned by [role]

### Model
| Input | Conservative | Expected | Optimistic | Source |
|---|---|---|---|---|
| **Annual value** | | | | |

**Input quality:** [n] client-stated, [n] observed, [n] reference class, [n] assumed

### Attribution
- Also moves this number: [list]
- Measurement design: [before/after | held-out | none]
- Baseline: [recorded / not recorded — if not, becomes deliverable 1]

### In the sponsor's units
[restatement]

### Pricing band
Conservative annual value [X] → fee band [0.10X – 0.35X]
Above [0.35X] requires [which optimistic assumption] to be accepted.

### Weakest link
[the single assumption that, if wrong, collapses the case]
```

---

## Verification

- [ ] Exactly one dominant mechanism is modelled.
- [ ] Every input carries a source label; the assumed count is stated.
- [ ] The conservative column uses the client's own pessimism, not yours.
- [ ] Attribution names at least two other factors that move the same number.
- [ ] The pricing band derives from the conservative column.
- [ ] The weakest link is named and is a real threat, not a token caveat.

**False-positive prevention.** The characteristic failure is a value case that is
arithmetically impressive and commercially useless because every input was supplied
by the person who wants the project approved. Check the provenance column: if the
large inputs are all client-stated and none is observed or referenced, the model is
circular — it proves what the sponsor already wanted.

The second failure is annualising a one-off. A migration that saves 400 hours saves
them once. Multiplying by twelve produces a number no finance function will accept
and costs you the credibility of the whole proposal. Where a benefit recurs, say why
it recurs.

The third: presenting the expected case as the case. Lead with conservative. A fee
that is defensible against the conservative figure survives scrutiny; one that needs
the optimistic figure does not survive the first CFO question.

---

## Related

- `services_pricing_model_selector.md` — turning this ceiling into a charging structure
- `../../domain-finance/corporate-finance-fpa/finance_services_rate_floor_model.md` — the floor
- `../../domain-personal-development/prompts/solo-dev/solo_dev_pricing_value_confidence.md` — the self-scope counterpart
- `../../domain-reasoning-craft/forecasting/forecasting_base_rate_establishment.md` — reference-class inputs
