---
title: "Launch Readiness Gate — Cross-Functional, With a Real No Available"
category: product-management/prompts
description: "Run the cross-functional gate before a product launch: readiness assessed per function with a named owner and an evidence requirement, blockers separated from risks, a go/no-go/go-with-conditions decision with a named decider, rollback criteria fixed in advance, and the first-week watch list. Refuses gates where every function self-reports green with no evidence and gates with no available no."
techniques:
  - ST-02
  - QA-08
  - CM-02
  - DD-07
  - OC-03
difficulty: intermediate
tags:
  - launch
  - go-no-go
  - readiness
  - cross-functional
  - rollback
updated: "2026-09-22"
related_prompts:
  - domain-product-management/prompts/product_north_star_metric_definition.md
  - domain-product-management/prompts/product_feature_sunset_decision.md
  - domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md
---

# Launch Readiness Gate

**Objective:** Run the **cross-functional** decision meeting before a launch: per-function
readiness with a named owner and required evidence, blockers distinguished from accepted
risks, a decision of go / no-go / go-with-conditions made by one named person, rollback
criteria agreed *before* launch, and a first-week watch list. Gates where every function
self-reports green with no evidence, and gates with no available "no", are refused.

**When to Use:**
- A launch date is near and you need to decide whether to hold it.
- Launches keep surprising support, sales or legal.
- The last launch went badly and nobody had agreed in advance what would trigger a
  rollback.

**When NOT to use:**
- You need the **engineering** definition of done for the work itself — that is
  `../../domain-engineering-workflows/done-definition/` and
  `workflow_definition_of_done_builder.md`. Engineering DoD asks "is the code
  complete?"; this gate asks "is the **organisation** ready for customers to have it?"
- You need the go-to-market plan — messaging, channels, launch sequence, Product Hunt,
  beta and waitlist mechanics — that is
  `../../domain-agentic-resources/skills/marketing/launch-strategy/`, which explicitly
  covers beta launch, early access and waitlists. This gate consumes its output as one
  function's readiness rather than replacing it.
- You need the release engineering pipeline — route to
  `../../domain-agentic-resources/skills/cicd-automation/deployment-pipeline-design/`.
- You are retiring something — the mirror case is
  `product_feature_sunset_decision.md`.

---

## Context Gathering

1. **The launch**
   - "What is launching, to whom, on what date, and is the date committed externally?"
   - "Is this a full release, a staged rollout, or a limited availability?"
   - "What is the blast radius if it goes wrong — all customers, one segment, new
     signups only?"

2. **The functions involved**
   - "Which functions are affected: engineering, support, sales, CS, marketing, legal,
     finance, security, ops?"
   - "Who owns readiness for each, by name?"

3. **The instrumentation**
   - "How will you know within 24 hours whether it is working?" (from
     `product_north_star_metric_definition.md` and the tracking plan)
   - "What would you see if it were failing quietly?"

4. **The escape route**
   - "Can this be rolled back? How long does it take? Has it been tested?"
   - "Is there a data migration that makes rollback lossy?"

The quiet-failure question is the one most gates omit. Loud failures get noticed; the
expensive ones are the launches that work technically and lose a conversion step nobody
was watching.

---

## Method

### Step 1 — Assess per function, with an owner and required evidence

Not a single checklist. Each affected function has a named owner who states readiness
**and supplies the evidence for it.** "Green" without evidence is an opinion, and the
whole purpose of the gate is to make it something else.

| Function | Owner | Ready? | Evidence required | Evidence supplied |
|---|---|---|---|---|
| Engineering | | | Tests passing, error budget headroom, load tested at [x] | |
| Support | | | Macros written, staff briefed, expected volume estimated | |
| Sales | | | Can describe it, knows the price, knows who it is not for | |
| Customer success | | | Affected accounts identified and contacted | |
| Marketing | | | Assets ready, copy approved, timing agreed | |
| Legal / privacy | | | Terms reviewed, data-processing position confirmed | |
| Finance / billing | | | Pricing configured, invoicing tested, revenue recognition clear | |
| Security | | | Review complete, findings closed or accepted | |
| Ops / infra | | | Capacity, alerting, on-call rota covers launch window | |
| Analytics | | | Events instrumented **and verified firing in production** | |

The analytics row is the one most often waved through, and it is the one that makes
everything after launch decidable. Instrumented-but-unverified is not ready: verify the
events fire in production before the gate, not after the launch.

Omit functions genuinely not affected — but say which and why, because "we didn't think
legal was involved" is a common post-mortem line.

### Step 2 — Separate blockers from accepted risks

Two categories, and the distinction must be explicit:

- **Blocker** — launch cannot proceed. Needs an owner and a resolution date.
- **Accepted risk** — known, launching anyway, with a named accepter, a stated
  consequence and a mitigation.

| # | Item | Blocker or risk | Owner / accepter | Consequence if it bites | Mitigation |
|---|---|---|---|---|---|

Writing down an accepted risk with a name against it is what makes acceptance real. Most
bad launches had the risk identified and nobody recorded as accepting it, which is how
it becomes a surprise in the post-mortem.

### Step 3 — Fix rollback criteria before launching

Decided now, not during the incident. Judgement degrades under pressure and sunk cost
rises by the hour.

| Signal | Threshold | Within | Action |
|---|---|---|---|
| Error rate | | 1h | Roll back |
| [North-star input] | drops >x% | 24h | Hold rollout, investigate |
| Support volume | >x tickets/h on this topic | 4h | Hold rollout |
| [Quiet-failure signal] | | 24h | Investigate before proceeding |

Also record: **how long a rollback takes, whether it has been tested, and whether it is
lossy.** An untested rollback plan is a hope. If a data migration makes rollback lossy,
say so — it raises the bar on the decision, and that is the correct effect.

### Step 4 — Name one decider and give them a real no

One named person decides. Not consensus: a committee needing unanimity defaults to the
most confident voice, and a committee needing a majority diffuses accountability until
nobody owns the outcome.

Three available decisions, and the second must be genuinely available:

- **Go** — launch as planned.
- **No-go** — hold. State what has to be true to revisit, and when.
- **Go with conditions** — launch to a reduced audience, with a named condition for
  widening.

**If the launch cannot be stopped, this is not a gate.** A meeting held after the date
is externally committed and the marketing has shipped is a briefing wearing a gate's
name. That is sometimes the real situation; say so, and run it as a risk review instead
of pretending a decision is available.

### Step 5 — Build the first-week watch list

Who watches what, when, and what they do:

| Metric | Owner | Cadence | Expected | Escalate if |
|---|---|---|---|---|

Include the quiet-failure signals from context gathering. Assign an owner to each — an
unowned dashboard is not monitoring — and set a review point (48 hours and one week are
typical) at which someone decides to widen, hold or revert.

### Step 6 — Record the decision

Date, decider, decision, conditions, accepted risks with accepters, rollback criteria,
and the watch list. This record is what makes the post-mortem informative: it shows what
was known, who decided, and which risk was accepted rather than missed.

---

## Output Format

```markdown
## Launch readiness — [what], [date]

**Scope:** [audience] · **Blast radius:** [x] · **Date externally committed:** [y/n]
**Decider:** [name, role]

### Is a no available?
[yes / no — if no, this is a risk review, not a gate. Say so.]

### Readiness by function
| Function | Owner | Ready? | Evidence required | Evidence supplied |
|---|---|---|---|---|

**Functions deemed not affected:** [list, with why]

### Blockers and accepted risks
| # | Item | Blocker / risk | Owner or accepter | Consequence | Mitigation | Resolution date |
|---|---|---|---|---|---|---|

### Rollback
| Signal | Threshold | Within | Action |
|---|---|---|---|

Rollback takes [x] · tested [y/n, date] · lossy [y/n — if yes, what is lost]

### Decision
**GO / NO-GO / GO WITH CONDITIONS** — [date], by [name]
Conditions: [x] · Widen when: [x]
If no-go: revisit when [x], by [date]

### First-week watch
| Metric | Owner | Cadence | Expected | Escalate if |
|---|---|---|---|---|

Review points: 48h [owner] · 1 week [owner]
```

---

## Verification

- [ ] Every affected function has a named owner and supplied evidence, not a self-reported colour
- [ ] Functions deemed unaffected are listed with reasons
- [ ] Analytics events are verified firing in production, not merely instrumented
- [ ] Blockers and accepted risks are separated, and every accepted risk has a named accepter
- [ ] Rollback criteria are agreed before launch, with thresholds and time windows
- [ ] Rollback duration is known, the plan has been tested, and lossiness is stated
- [ ] One named decider, with three genuinely available decisions
- [ ] If no is unavailable, the document says so and is relabelled a risk review
- [ ] Every watch-list metric has an owner and an escalation threshold
- [ ] At least one quiet-failure signal is on the watch list
- [ ] The decision is recorded with date, decider and accepted risks

**False-positive prevention.** The dominant failure is the all-green gate: every function
reports ready, nobody supplies evidence, and the launch surprises support within two
hours. The evidence column is the fix, and it has to be enforced — "yes, we're ready" is
not evidence, and the gate's owner has to be willing to say so in the meeting.

The second failure is the ceremonial gate, held after the date is committed and the
announcement scheduled. Everyone present understands no is unavailable, so concerns go
unraised and the meeting produces false confidence. If that is the situation, name it and
convert the meeting into a risk review with rollback criteria — which is genuinely
useful — rather than recording a decision that was never available.

The third is deciding rollback criteria during the incident. At hour three of a bad
launch, with the announcement live and the team tired, the threshold that gets chosen is
the one that avoids reverting. Fix the numbers while nothing is on fire.

The fourth is treating instrumentation as done when the events are written. Events that
do not fire, fire twice, or fire with a null property are the normal state before
verification, and a launch you cannot measure is one you cannot decide about on day two.

---

## Related

- `product_north_star_metric_definition.md` — supplies the signals and the counter-metric
- `product_feature_sunset_decision.md` — the mirror gate at the other end of the lifecycle
- `../../domain-engineering-workflows/workflows/workflow_definition_of_done_builder.md` — the engineering DoD this gate sits above
- `../../domain-agentic-resources/skills/marketing/launch-strategy/` — the GTM plan, consumed as one function's readiness
- `../../domain-risk/risk_after_action_review.md` — the post-launch retrospective this record feeds
