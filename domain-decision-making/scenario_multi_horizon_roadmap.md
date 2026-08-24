---
title: "Multi-Horizon Roadmap — Three Horizons of Now, Next, and Later with a Resource-Balance Check"
category: decision-making/scenario-planning
description: "Build a three-horizons roadmap (defend the core / build adjacencies / create future options) that names what gets resourced, what gets monitored, and the kill criterion at each horizon, then forces an honest reconciliation between actual time-and-budget allocation and stated strategy. Counters the failure where organizations over-fund the present and starve the future (or chase the future and neglect the engine paying for it)."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - three-horizons
  - roadmap
  - portfolio
  - resource-allocation
  - strategic-foresight
updated: "2026-05-10"
reasoning:
  styles: [strategic, systems, portfolio, temporal]
  stakes: high
  horizon: years
  uncertainty: ambiguity
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: structured
  user_role: [strategist, executive, founder, pm, investor, planner]
  mode: [plan, synthesize, audit]
related_prompts:
  - domain-decision-making/scenario_backcasting.md
  - domain-decision-making/scenario_two_by_two_matrix.md
  - domain-decision-making/tradeoff_multi_criteria_decision_analysis.md
---

# Multi-Horizon Roadmap

**Objective:** Lay a strategy across three time horizons — Horizon 1 (defend and extend the core, months to a year), Horizon 2 (build emerging adjacencies, 1–3 years), Horizon 3 (create viable options for future opportunities, 3+ years) — and for each horizon specify what gets resourced, what gets monitored, and the kill criterion. The exercise's hard output is the **resource-balance check**: a comparison of where time and money actually go against what the stated strategy claims to prioritize. Most roadmaps drift; this one forces the drift into the open.

Based on the three-horizons frame (McKinsey). The common failure modes are asymmetric: incumbents over-invest in H1 and starve H3 until disruption arrives; early-stage or founder-led organizations over-invest in H3 (the exciting future) and neglect the H1 engine that funds everything. This prompt is designed to surface which way you're tilted.

**When to use:**
- Annual or multi-year strategic planning across a portfolio of initiatives.
- Diagnosing whether the organization is investing for the future or coasting on the core.
- Reconciling an inspiring strategy deck with the actual budget and headcount.
- Founder / leadership debates about how much to spend on the current product vs. the next one.
- Translating a vision into a sequenced, resourced plan.

**When NOT to use:**
- Single-initiative decisions — there's no portfolio to balance across horizons.
- Pure crisis triage — when survival is at stake, H1 is the only horizon that matters.
- The organization is too early to have a defensible core (pre-product). Plan the core first.

**Audience:** Executives, strategists, founders, product leaders, investors, and planners responsible for allocating finite resources across competing time horizons.

---

## Inputs / Context

1. **The strategy or vision.** The stated direction the roadmap is meant to execute.
2. **Current initiative portfolio.** What's being worked on now, with rough effort/spend on each if known.
3. **Resource envelope.** Total time, budget, headcount available (even approximate).
4. **The core business / engine.** What currently generates revenue, users, or mission impact.
5. **Time-allocation reality (if available).** Where leadership attention and budget actually go today — needed for the balance check.

---

## Constraints

### Must
- Assign every current and proposed initiative to a horizon:
  - **H1 — defend and extend the core** (months–1 year): protect and grow what works now.
  - **H2 — build emerging adjacencies** (1–3 years): scaling bets that aren't yet the engine but plausibly could be.
  - **H3 — create future options** (3+ years): cheap, optional bets on opportunities that may or may not materialize.
- For each horizon, specify three things:
  - **Resourced:** what gets real time/budget/headcount.
  - **Monitored:** what's watched but not yet funded (signals that would promote it to "resourced").
  - **Kill criterion:** the condition under which initiatives in this horizon are stopped or demoted.
- Produce an explicit **target allocation** across the three horizons (e.g., 70/20/10 of discretionary resource) and justify it against the strategy.
- Run the **resource-balance check**: compare *actual* allocation to *target* and to *stated strategy*. Name the gap and its direction (over-investing the present vs. the future).
- Treat H3 as **options, not commitments**. H3 bets should be individually cheap and killable; the value is optionality, not the expected return of any single bet.

### Must Not
- Let every initiative claim H2. The "innovation theater" failure is reclassifying core maintenance as a growth bet. Be strict: H1 protects the engine, H2 is genuinely new adjacency.
- Resource H3 like H1. Future options are deliberately under-funded relative to their excitement; over-funding an unproven bet drains the core.
- Skip kill criteria. A horizon without kill criteria becomes a graveyard of zombie initiatives.
- Produce a target allocation and then ignore the actual. The balance check — actual vs. target — is the deliverable.
- Confuse horizons with project size. A small project can be H3 (a cheap option) and a large project can be H1 (defending the core). Horizon is about time-to-payoff and certainty, not budget.

---

## Instructions

### Step 1 — Identify the core (H1 anchor)
Name the engine: what currently produces the revenue, users, or mission outcomes that fund everything else. H1 is whatever defends and extends this.

### Step 2 — Classify the portfolio
Place each current and proposed initiative into H1, H2, or H3. For borderline cases, classify by **time-to-payoff and certainty**: near-term + high-certainty = H1; medium-term + plausible = H2; long-term + speculative = H3.

### Step 3 — Define each horizon's three lists
For H1, H2, H3 in turn:
- **Resourced:** the funded initiatives and their purpose.
- **Monitored:** unfunded watch-items and the signal that would promote each.
- **Kill criterion:** the explicit stop/demote condition.

### Step 4 — Set the target allocation
Propose a split of discretionary resource (time, budget, headcount) across the three horizons. Justify it from the strategy and the organization's stage. State the reasoning — e.g., a disrupted incumbent needs more H3 than a 70/20/10; a cash-strapped startup may need 85/15/0 until the core is safe.

### Step 5 — Measure the actual allocation
Estimate where time and money *actually* go today. Use the input data; if unavailable, estimate from the portfolio and flag it as an estimate to confirm.

### Step 6 — Run the balance check
Lay actual against target against stated strategy in one view. Name:
- The **direction of drift** (over-investing present or future).
- The **magnitude** (rough percentage points off target).
- The **specific reallocation** that would close the gap — what to defund and what to fund.

### Step 7 — Sequence the promotions
Identify which H3 options and H2 bets are closest to graduating, and the signpost that would trigger promotion to the next horizon (and the resource it would draw).

### Step 8 — State the one decision
Name the single highest-leverage reallocation decision the balance check surfaced, and what it costs to make it.

---

## False-Positive Prevention

1. **H2 inflation.** Reclassifying routine core maintenance as a growth adjacency to look innovative. H1 work stays H1; only genuinely new adjacencies are H2.
2. **H3 over-funding.** Pouring real budget into speculative future bets and starving the engine. H3 bets are cheap options; if one needs H1-scale resourcing, it's been promoted to H2 and should be judged as such.
3. **Allocation-without-check.** Stating a clean target (70/20/10) and never comparing it to reality. The actual-vs-target gap is the finding.
4. **Kill-criterion absence.** Horizons without stop conditions accumulate zombies. Every horizon gets explicit kill criteria.
5. **Size-horizon conflation.** Assuming big projects are near-horizon and small ones are far. Horizon is time-to-payoff and certainty, not budget.
6. **Optimism in the actuals.** Estimating actual allocation to match the desired target. Estimate from where attention and money visibly go, not from intentions.
7. **Strategy-deck mismatch ignored.** A strategy that says "we're betting on the future" paired with a 95/5/0 actual allocation is incoherent — name the incoherence rather than smoothing it.
8. **Monitor-list dumping.** Parking everything inconvenient in "monitored" to avoid deciding. Each monitored item needs a concrete promotion signal, or it's just deferred indefinitely.

---

## Output Format

```
# Three-horizons roadmap — [strategy / org]

## Core engine (H1 anchor)
> [What funds everything; what H1 defends]

## Horizon classification
| Initiative            | Horizon | Time-to-payoff | Certainty | Rationale            |
|-----------------------|---------|----------------|-----------|----------------------|
| [...]                 | H1      | <1yr           | high      | [...]                |
| [...]                 | H2      | 1–3yr          | plausible | [...]                |
| [...]                 | H3      | 3yr+           | speculative | [...]              |

## Horizon 1 — defend and extend the core
- **Resourced:** [...]
- **Monitored:** [item] — promote if [signal]
- **Kill criterion:** [...]

## Horizon 2 — build emerging adjacencies
- **Resourced:** [...]
- **Monitored:** [item] — promote if [signal]
- **Kill criterion:** [...]

## Horizon 3 — create future options
- **Resourced (cheap, optional):** [...]
- **Monitored:** [item] — promote if [signal]
- **Kill criterion:** [...]

## Resource-balance check
| Horizon | Target % | Actual % (est.) | Stated-strategy implies | Gap        |
|---------|----------|-----------------|-------------------------|------------|
| H1      | [..]     | [..]            | [..]                    | [+/- pts]  |
| H2      | [..]     | [..]            | [..]                    | [+/- pts]  |
| H3      | [..]     | [..]            | [..]                    | [+/- pts]  |

- **Direction of drift:** [over-investing present | over-investing future]
- **Magnitude:** [rough pts off target]
- **Reallocation to close the gap:** defund [...], fund [...]

## Promotion pipeline
- [H3 option] closest to graduating — trigger: [signpost], draws: [resource]
- [H2 bet] closest to becoming core — trigger: [signpost]

## The one decision
- [Highest-leverage reallocation] — cost to make it: [...]
```

---

## Verification

- [ ] Core engine named and H1 anchored to defending it.
- [ ] Every initiative classified H1/H2/H3 by time-to-payoff and certainty, not size.
- [ ] Each horizon has resourced / monitored / kill-criterion specified.
- [ ] Target allocation across horizons stated and justified from strategy + stage.
- [ ] Actual allocation estimated (and flagged if estimated).
- [ ] Balance check names drift direction, magnitude, and a concrete reallocation.
- [ ] H3 treated as cheap options, not funded like the core.
- [ ] No core maintenance smuggled into H2.
- [ ] Monitored items each have a promotion signal.
- [ ] Single highest-leverage reallocation decision named with its cost.
