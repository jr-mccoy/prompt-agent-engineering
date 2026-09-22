---
title: "Risk Appetite Statement — The Thresholds the Register and the Heat Map Presuppose"
category: risk
description: "Write the risk appetite statement the other risk instruments already assume: appetite stated per risk category rather than as one sentence, quantified tolerance limits where a number exists, the trade-off each appetite implies stated out loud, escalation triggers when a limit is breached, and a review cadence. Refuses single-sentence appetites, appetites with no stated trade-off, and limits nobody monitors."
techniques:
  - CM-02
  - CM-09
  - RT-05
  - QA-08
  - OC-03
difficulty: advanced
tags:
  - risk-appetite
  - risk-tolerance
  - governance
  - escalation
  - thresholds
updated: "2026-09-22"
related_prompts:
  - domain-risk/risk_register_builder.md
  - domain-risk/risk_heat_map.md
  - domain-decision-making/decisioning_escalation_decision_tree.md
---

# Risk Appetite Statement

**Objective:** Write the statement that every other instrument in this domain already
presupposes. `risk_register_builder` ranks risks against an implied threshold;
`risk_heat_map` asks whether the top three mitigations are actually happening; both
assume somebody has decided how much risk is acceptable and in which categories.
Usually nobody has, and the threshold is whatever the most risk-averse person in the
room felt that day.

Output: appetite per category, quantified tolerance limits where a number exists, the
**trade-off each appetite implies** stated explicitly, escalation triggers on breach,
and a review cadence. Single-sentence appetites, appetites with no stated trade-off, and
limits nobody monitors are refused.

**When to Use:**
- You have a risk register and no basis for deciding which entries are acceptable.
- Two managers disagree about whether a risk needs mitigating and there is no referee.
- A board, investor, insurer or auditor has asked for one.
- The organisation is systematically over-cautious in one area and reckless in another,
  and nobody has noticed because there is no stated position.

**When NOT to use:**
- You need the register itself — that is `risk_register_builder.md`. Build the appetite
  first if you can; retrofit it if the register already exists.
- You need to visualise and re-rank existing risks — that is `risk_heat_map.md`.
- You need an **enterprise** risk register in a regulated financial institution — that
  is `../domain-finance/risk-management/finance_enterprise_risk_register.md`, with
  `finance_operational_risk_rcsa.md` for the control self-assessment.
- You need scenario planning or stress testing — this domain routes those out by name:
  `../domain-decision-making/scenario_two_by_two_matrix.md` and siblings, or
  `../domain-finance/risk-management/finance_stress_test_scenario_design.md`.
- You need personal risk tolerance for investing — that is
  `../domain-finance/personal-finance-planning/finance_asset_allocation_glidepath.md`.

---

## Context Gathering

1. **What the organisation is for**
   - "What is the mission or the commercial objective? Appetite is only meaningful
     relative to something you are trying to achieve."
   - "What stage are you at — survival, growth, scale, steady state?"

2. **Where risk currently lands**
   - "Name a risk you have deliberately accepted in the last year. Who decided?"
   - "Name one you refused. Who decided?"
   - "Was either decision written down?"

3. **Categories that matter here**
   - "Which of these are live for you: financial, operational, safety, legal and
     regulatory, reputational, security and data, people, strategic, third-party?"
   - "Which one would end the organisation if it went badly?"

4. **Capacity, as distinct from appetite**
   - "How much loss could you absorb without existential consequence — cash, time,
     reputation?"
   - "What is insured? What is not?"

The distinction in the last group is the one that makes the document honest. **Capacity**
is how much you can survive; **appetite** is how much you choose to take. Appetite
exceeding capacity is not a bold position, it is an arithmetic error, and the statement
should refuse to record it.

---

## Method

### Step 1 — Refuse the single sentence

"We have a moderate appetite for risk" is the standard output and it is useless: it
cannot adjudicate anything, and every party reads their own preference into it.

Appetite is **different per category**, and the differences are the substance. A
well-run organisation is typically near-zero on safety and regulatory, deliberately high
on product experimentation, and moderate on financial — and saying so resolves arguments
that a single sentence leaves open.

### Step 2 — State appetite per category on a scale with meanings

Use four or five levels and define each in behavioural terms, so that two people
classify the same proposal the same way.

| Level | What it means in practice |
|---|---|
| **Averse** | We will not accept this risk. We forgo the opportunity, and we accept the cost of doing so |
| **Cautious** | Accept only with strong controls, senior approval, and a tested reversal path |
| **Measured** | Accept where the expected benefit is documented and the downside is bounded |
| **Open** | Accept readily; this is where we expect to learn and occasionally lose |

Then per category:

| Category | Appetite | Why | What this means we will do | What it means we will not do |
|---|---|---|---|---|
| Safety / physical harm | | | | |
| Legal and regulatory | | | | |
| Security and data | | | | |
| Financial | | | | |
| Operational and delivery | | | | |
| Reputational | | | | |
| People | | | | |
| Strategic / product | | | | |
| Third-party dependency | | | | |

The last two columns are what make it a decision rather than a sentiment. "Open
appetite on product experimentation" means we will ship things that fail and not punish
the team for it — write that down, because the appetite is disbelieved until the
consequence is stated.

### Step 3 — Quantify tolerance where a number exists

Appetite is a direction; **tolerance is the limit.** Where a number can exist, state it.

| Category | Tolerance limit | Measured by | Monitored by | Frequency |
|---|---|---|---|---|
| Financial | Single loss ≤ [x]; annual aggregate ≤ [y] | | | |
| Operational | Availability ≥ [x]%; error budget [y] | | | |
| Security | No unpatched critical beyond [x] days | | | |
| Third-party | No single supplier above [x]% of [capability] | | | |
| People | Key-person coverage: no single point beyond [x] | | | |
| Financial (concentration) | No client above [x]% of revenue | | | |

Two rules:

- **A limit with no monitor is not a limit.** If nobody measures it on a cadence, the
  row is aspiration and should say so rather than sitting in a table implying control.
- **Where no meaningful number exists, say so** rather than inventing one. Reputational
  risk rarely quantifies well; an honest qualitative statement with named examples beats
  a fabricated threshold.

Cross-check the limits against existing instruments: the concentration limit should match
`../domain-business-strategy/client-services/services_client_concentration_risk_check.md`,
and the third-party limits should be consistent with what
`risk_dependency_chain_audit.md` has already found.

### Step 4 — State the trade-off each appetite buys

Every appetite has a cost, and stating it is what stops the document being a list of
virtues.

| Appetite | What it buys | What it costs |
|---|---|---|
| Averse on regulatory | Predictability, licence retention | Slower entry to regulated markets; some opportunities forgone entirely |
| Open on product experimentation | Learning rate, occasional large win | Visible failures; support load; some customer frustration |
| Cautious on financial | Survivability | Slower growth than a competitor willing to take the risk |

An appetite statement in which everything is prudent and nothing is forgone has not been
written honestly. If no cost can be named for a category, the appetite in that category
is probably not a real position.

### Step 5 — Set escalation triggers on breach

A limit needs a consequence, or the first breach establishes that breaches are fine.

| Category | Approaching limit ([x]% of it) | Limit breached |
|---|---|---|
| | Notify [role]; review at [forum] | Escalate to [role] within [time]; [specific action] |

The approaching-limit column is the useful one. A breach is a failure; an approach is a
decision point with time to act, and it is where the statement earns its keep.
Cross-reference `../domain-decision-making/decisioning_escalation_decision_tree.md`,
which owns the escalation pathway shape.

### Step 6 — Set the review cadence and the ratifier

- **Who ratifies this** — a named person or body. An unratified appetite statement is one
  person's opinion in a table.
- **Review cadence** — annually, and on any material change: stage change, new market,
  new regulation, a significant loss event.
- **Where it is visible** — a statement nobody can find will not be used when the
  decision it exists for arrives.

---

## Output Format

```markdown
## Risk appetite statement — [organisation], [date]

**Ratified by:** [name / body] on [date] · **Next review:** [date] or on [triggers]
**Objective this appetite serves:** [one sentence]

### Capacity, before appetite
| | |
|---|---|
| Absorbable single loss without existential consequence | |
| Absorbable annual aggregate | |
| Insured / uninsured | |
**Appetite must not exceed capacity in any category.** [confirmed]

### Appetite by category
| Category | Appetite | Why | We will | We will not |
|---|---|---|---|---|

### Tolerance limits
| Category | Limit | Measured by | Monitored by | Frequency |
|---|---|---|---|---|
**Unquantifiable categories:** [named, with a qualitative statement and examples]
**Unmonitored limits:** [named as aspiration, not control]

### What each appetite costs
| Appetite | Buys | Costs |
|---|---|---|

### Escalation
| Category | Approaching limit | Breached |
|---|---|---|

### Consistency check against existing instruments
| Instrument | Agrees? |
|---|---|
| `risk_register_builder.md` rankings | |
| `risk_dependency_chain_audit.md` findings | |
| Client-concentration limit | |
```

---

## Verification

- [ ] Appetite is stated per category, not as one sentence
- [ ] Each level on the scale is defined in behavioural terms
- [ ] Every category has both a "we will" and a "we will not"
- [ ] Capacity is stated and appetite does not exceed it anywhere
- [ ] Tolerance limits are quantified where a number meaningfully exists
- [ ] Unquantifiable categories say so rather than carrying an invented number
- [ ] Every limit names a monitor and a frequency, or is labelled aspiration
- [ ] Every appetite has a stated cost
- [ ] Escalation has both an approaching-limit and a breached row
- [ ] A named person or body has ratified it
- [ ] Limits are checked for consistency against the register and the dependency audit

**False-positive prevention.** The dominant failure is the appetite statement in which
every category is prudent and nothing is given up. It reads well, satisfies whoever asked
for it, and adjudicates nothing — because an organisation averse to every category has
simply declined to choose. Force the cost column: if no cost can be named for a
category, the appetite there is decoration.

The second failure is uniform appetite across categories. Genuine positions differ
sharply — near-zero on safety, open on experimentation — and a flat "moderate" across the
board is the single-sentence failure in table form.

The third is limits nobody monitors. A table of thresholds with no owner and no cadence
creates the appearance of control and, worse, a record that the organisation knew the
limit and did not watch it. Label those rows aspiration, or assign the monitor.

The fourth is appetite exceeding capacity. An organisation with three months of runway
cannot have a genuinely open appetite for financial risk; writing one down does not
create the capacity, it just documents that the arithmetic was not done. Capacity is
computed first for exactly this reason.

---

## Related

- `risk_register_builder.md` — ranks risks against the thresholds this sets
- `risk_heat_map.md` — the visual re-ranking, which needs a line to rank against
- `risk_dependency_chain_audit.md` — supplies the third-party and key-person limits
- `risk_business_continuity_plan.md` — what happens when a limit is breached materially
- `../domain-decision-making/decisioning_escalation_decision_tree.md` — the escalation pathway
- `../domain-business-strategy/client-services/services_client_concentration_risk_check.md` — the concentration limit in a services practice
