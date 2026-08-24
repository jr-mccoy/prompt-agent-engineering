---
title: "Strategic Pre-Mortem — Imagine the Strategy Failed at Year Three and Trace Back Why"
category: decision-making/scenario-planning
description: "Run a pre-mortem on an entire strategy at its three-year mark: assume it has clearly failed, then work backward to identify the failure modes that produced it — missed market shifts, capacity gaps, competitive responses, execution breakdowns, and false assumptions about team, market, and technology. Outputs ranked failure modes each paired with a prevention or detection move. Distinct from product/prompt pre-mortems and from systems-intervention pre-mortems; this one operates at the strategy level."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - pre-mortem
  - strategy
  - failure-modes
  - prospective-hindsight
  - strategic-foresight
updated: "2026-05-10"
reasoning:
  styles: [counterfactual, prospective-hindsight, abductive, adversarial]
  stakes: high
  horizon: years
  uncertainty: deep
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: structured
  user_role: [strategist, executive, founder, investor, pm]
  mode: [audit, diagnose, forecast]
related_prompts:
  - domain-decision-making/scenario_robustness_test.md
  - domain-decision-making/scenario_wild_card_injection.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
---

# Strategic Pre-Mortem

**Objective:** Project forward to the strategy's three-year mark, **assume it has clearly and visibly failed**, and work backward to reconstruct the causal story: what went wrong, in what order, and which decisions or assumptions made the failure possible. The output is a ranked set of failure modes, each paired with a specific **prevention** move (stop the cause) or **detection** move (catch it early enough to react). Prospective hindsight — imagining the failure as already real — surfaces risks that forward "what could go wrong?" brainstorming reliably misses.

This pre-mortem operates at the **strategy level** and is deliberately distinct from two neighbors: a product/prompt pre-mortem (does this artifact work as specified?) and a systems-intervention pre-mortem (does this change to a system backfire?). Here the unit of analysis is a multi-year strategy and the failure is strategic: the bet was wrong, the execution didn't land, the world moved.

**When to use:**
- Before committing to a multi-year strategy, while it's still cheap to adjust.
- At a strategy review, to pressure-test a plan that everyone currently believes in.
- After a strategy is set but before major resources are deployed.
- When a strategy feels too clean — no one in the room can articulate how it fails.
- As a companion to a robustness test: the robustness test rates the strategy against scenarios; this finds the internal and execution failures the scenarios don't capture.

**When NOT to use:**
- For evaluating a discrete artifact, prompt, or product spec — use a product/correctness pre-mortem.
- For a single reversible decision — the machinery is too heavy.
- When the strategy is already failing in real time — that's a post-mortem / turnaround, not a pre-mortem.

**Audience:** Strategists, executives, founders, investors, and product leaders responsible for strategies whose failure would be costly and slow to reverse.

---

## Inputs / Context

1. **The strategy.** Its core bet, the few moves it depends on, and what success looks like at year three.
2. **Key assumptions.** What's being assumed about the team, the market, the technology, the competition, and the funding/resource path.
3. **The horizon and milestones.** The three-year endpoint and any interim checkpoints.
4. **What's already known to be hard.** Risks the team has already named (so the pre-mortem can go beyond them).
5. **Decision context.** Whether this is pre-commitment, mid-flight review, or resource-gating.

---

## Constraints

### Must
- Open by **stating the failure as fact**: "It is [date, 3 years out]. The strategy has clearly failed. [One-paragraph description of the visible failure state.]" Write from inside that future.
- Generate failure modes across **all five families**, not just the comfortable ones:
  - **Missed market shift** — demand, customer behavior, or category moved and the strategy didn't.
  - **Internal capacity gap** — the team / capital / infrastructure couldn't deliver what the strategy required.
  - **Competitive response** — a competitor or new entrant did something the strategy didn't anticipate.
  - **Execution failure** — the strategy was right but wasn't executed (slipped timelines, focus loss, organizational friction).
  - **False assumption** — a load-bearing belief about team, market, or technology turned out wrong.
- For each failure mode, specify: the **mechanism** (how it produced failure), an **early signal** (what would have shown it coming), and a **prevent-or-detect** move.
- **Rank** failure modes by a combination of likelihood and how irreversibly they sink the strategy.
- Separate **preventable** failure modes (you can act now to remove the cause) from **detect-only** ones (you can't prevent but can catch early) — these get monitoring, not prevention.
- End by naming the **two or three failure modes most worth acting on before commitment**, and the specific action for each.

### Must Not
- Soften the framing to "risks to watch." The pre-mortem's power comes from asserting the failure as already real, then explaining it. Stay in that stance.
- Stop at the comfortable failure families. Teams over-index on external causes (market, competition) and under-index on internal ones (capacity, execution, their own false assumptions). Force coverage of all five.
- List failure modes without prevention/detection moves. A failure mode with no actionable response is just pessimism.
- Treat every failure as preventable. Some are detect-only; pretending otherwise produces fake contingencies.
- Rank by vividness. The most dramatic failure isn't necessarily the most likely or most lethal; rank by likelihood × irreversibility.

---

## Instructions

### Step 1 — Declare the failure
Write one paragraph from three years in the future: the strategy has failed, here's what that looks like from the outside — the metrics, the market position, the state of the organization. Make it concrete enough to feel real.

### Step 2 — Brainstorm causes within each family
Working backward from the failure, generate candidate causes under each of the five families: missed market shift, internal capacity gap, competitive response, execution failure, false assumption. Aim for 2–4 per family before pruning.

### Step 3 — Trace each mechanism
For each surviving cause, write the causal chain: from the cause, through the intermediate consequences, to the failure state declared in Step 1. A failure mode without a traceable mechanism is speculation.

### Step 4 — Find the early signal
For each: what observable indicator, in year one or two, would have signaled this cause was active? If genuinely none exists, mark it — those are the dangerous silent failures.

### Step 5 — Assign prevent or detect
For each: can the cause be removed now (**prevent**), or only watched for (**detect**)? Prevention moves change the strategy or its setup today; detection moves install a monitored signal with a pre-committed response.

### Step 6 — Rank
Score each failure mode on **likelihood** (over the three years) and **irreversibility** (how completely it sinks the strategy if it lands). Rank by the combination. Put the top handful at the head of the list.

### Step 7 — Reconcile with stated assumptions
For each false-assumption failure mode, point back to the specific input assumption it falsifies. If the team's stated assumptions don't even mention a load-bearing belief that appears here, flag the omission.

### Step 8 — Name the act-now set
Pick the two or three failure modes most worth acting on before commitment. For each, state the concrete change to the strategy, plan, or monitoring that would defuse or surface it — and what it costs.

---

## False-Positive Prevention

1. **Risk-list regression.** Sliding from "it failed, here's why" back into "here are some risks." The asserted-failure stance is the technique; losing it loses the value.
2. **External-cause bias.** Blaming the market and competitors while sparing the team's own execution and assumptions. Force the internal families (capacity, execution, false assumption) to carry their weight.
3. **Mechanism-free modes.** "The team isn't strong enough" with no chain to failure. Every mode needs a traceable cause-to-collapse path.
4. **Prevention theater.** Claiming a failure is preventable when it's structurally outside control. Honest detect-only labeling is better than a fake contingency.
5. **Dramatic-over-likely ranking.** Ranking by how cinematic the failure is rather than likelihood × irreversibility.
6. **Signal omission.** Skipping the early-signal step, which is what makes the pre-mortem operational rather than fatalistic.
7. **Assumption disconnection.** Failure modes that never reconnect to the strategy's stated assumptions. Each false-assumption mode should name the belief it breaks.
8. **Comfortable-count satisficing.** Stopping at three or four obvious modes. Cover all five families before pruning; the unexamined family is usually where the real failure hides.

---

## Output Format

```
# Strategic pre-mortem — [strategy name]

## The failure (asserted, year +3)
> It is [date]. The strategy has clearly failed. [Concrete description of the failure state — metrics, position, org state.]

## Failure modes by family
### Missed market shift
- **[Mode]** — mechanism: [cause → ... → failure] | early signal: [...] / none | prevent or detect: [...]

### Internal capacity gap
- **[Mode]** — mechanism: [...] | early signal: [...] | prevent or detect: [...]

### Competitive response
- **[Mode]** — [...]

### Execution failure
- **[Mode]** — [...]

### False assumption
- **[Mode]** — falsifies stated assumption: [...] | mechanism: [...] | early signal: [...] | prevent or detect: [...]

## Ranked failure modes
| Rank | Failure mode        | Family            | Likelihood | Irreversibility | Prevent/Detect | Move                  |
|------|---------------------|-------------------|------------|-----------------|----------------|-----------------------|
| 1    | [...]               | execution         | high       | high            | prevent        | [action]              |
| 2    | [...]               | false assumption  | medium     | high            | detect         | [monitored signal]    |
| …    |                     |                   |            |                 |                |                       |

## Silent failures (no early signal)
- [Mode] — why it gives no warning, and the standing defense it requires.

## Act-now set (before commitment)
1. [Failure mode] → [concrete change to strategy/plan/monitoring] — cost: [...]
2. [...]
3. [...]
```

---

## Verification

- [ ] Failure asserted as fact at year +3, written from inside that future.
- [ ] Causes generated across all five families (market, capacity, competition, execution, false assumption).
- [ ] Each failure mode has a traceable mechanism.
- [ ] Each has an early signal or an explicit "none" (silent failure).
- [ ] Each labeled prevent or detect, honestly.
- [ ] Failure modes ranked by likelihood × irreversibility, not drama.
- [ ] False-assumption modes reconnected to the strategy's stated assumptions.
- [ ] Act-now set of 2–3 modes named, each with a concrete move and cost.
- [ ] Internal failure families given real weight, not just external ones.
- [ ] No failure mode left without a prevention or detection response.
