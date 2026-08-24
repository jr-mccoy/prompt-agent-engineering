---
title: "Robustness Test — Rate a Strategy Across All Scenarios and Find the Performance-vs-Floor Frontier"
category: decision-making/scenario-planning
description: "Test one strategy against every scenario in a set, rating effectiveness in each as strong / acceptable / weak / catastrophic, then propose modifications that lift weak and catastrophic cells to acceptable even at the cost of peak performance in the favored scenario. Surfaces the robustness frontier: the explicit tradeoff between maximizing performance in the expected future and raising the worst-case floor across all futures."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: advanced
tags:
  - robustness
  - stress-test
  - minimax
  - scenario-planning
  - strategy-evaluation
updated: "2026-05-10"
reasoning:
  styles: [scenario, strategic, minimax, dialectical]
  stakes: high
  horizon: years
  uncertainty: deep
  evidence_quality: variable
  domain_complexity: cross_domain
  collaboration: solo_or_team
  output_format: structured
  user_role: [strategist, executive, founder, investor, policy, planner]
  mode: [audit, decide, synthesize]
related_prompts:
  - domain-decision-making/scenario_two_by_two_matrix.md
  - domain-decision-making/scenario_strategic_pre_mortem.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
---

# Robustness Test

**Objective:** Take one strategy and run it against every scenario in a set (the four from a 2x2 matrix, or N scenarios from any source). Rate the strategy's effectiveness in each scenario on a four-level scale — **strong / acceptable / weak / catastrophic** — then identify where the strategy is fragile and propose **robustness modifications**: changes that lift weak and catastrophic cells to at least acceptable, accepting that this may shave peak performance in the favored scenario. The headline output is the **robustness frontier** — the explicit tradeoff between maximizing the expected case and raising the worst case across all cases.

A strategy optimized for the single most-likely scenario is, by construction, fragile in the others. Robustness analysis asks a different question than "what's the best strategy if my forecast is right?" It asks "what strategy do I least regret if I'm wrong about which future arrives?" The answer usually trades a little expected-case performance for a much higher floor.

**When to use:**
- After building a scenario set, to evaluate whether a candidate strategy holds across futures.
- Comparing a high-peak/high-variance strategy against a flatter, more robust one.
- Decisions under deep uncertainty where the cost of being wrong about the future is severe.
- Stress-testing an investment thesis, policy, or product strategy against multiple worlds.
- As the converging step after a 2x2 matrix and a strategic pre-mortem.

**When NOT to use:**
- The future is forecastable and one scenario dominates probability — optimize for it.
- No scenario set exists — build one first.
- The decision is small or reversible, where worst-case floor barely matters.

**Audience:** Strategists, executives, founders, investors, policy designers, and planners choosing strategy under deep uncertainty about which future will arrive.

---

## Inputs / Context

1. **The strategy under test.** The single strategy being evaluated (and, optionally, alternatives to compare).
2. **The scenario set.** The N scenarios to test against, each with enough description to judge how the strategy fares.
3. **Scenario probabilities (if available).** Rough likelihoods — used to weight, never to dismiss low-probability/high-impact scenarios.
4. **What "effectiveness" means here.** The outcome the strategy is trying to produce (revenue, survival, market position, mission impact), so ratings are anchored to something concrete.
5. **Acceptable-floor definition.** The minimum outcome below which a result counts as failure — the line between "weak" and "catastrophic."

---

## Constraints

### Must
- Rate the strategy in **every** scenario on the four-level scale, with a one-line justification per cell:
  - **Strong** — strategy thrives; outcome well above target.
  - **Acceptable** — strategy holds; outcome at or modestly below target, survivable.
  - **Weak** — strategy underperforms; outcome meaningfully below target but not fatal.
  - **Catastrophic** — strategy fails; outcome below the survival floor.
- Anchor ratings to the stated effectiveness outcome and the acceptable-floor definition, not to vibes.
- Identify every **catastrophic** cell as a fragility that must be addressed (a single catastrophic scenario can justify abandoning an otherwise strong strategy).
- For each weak or catastrophic cell, propose a **robustness modification** that would raise it to at least acceptable, and state its **cost** — specifically what it sacrifices in the strong/favored scenarios.
- Surface the **robustness frontier** explicitly: characterize the tradeoff between the original strategy (high peak, low floor) and the modified strategy (lower peak, higher floor), and state which side of the frontier the decision should sit on given the stakes and the cost of being wrong.
- Compute and report a **floor** (worst rating across scenarios) and a **probability-weighted expectation** (if probabilities given) for both the original and modified strategy, so the tradeoff is quantified, not just described.

### Must Not
- Average the scenarios into a single score that hides a catastrophic cell. A catastrophic worst case is a property of its own; it does not get diluted by strong cells.
- Rate by preference for the expected scenario. The favored scenario's strong rating is not evidence about the others.
- Propose modifications with no stated cost. Every robustness gain is paid for somewhere — usually in peak performance; name the price.
- Confuse robustness with mediocrity. The goal is raising the floor at minimal cost to the peak, not flattening everything to bland safety.
- Drop low-probability catastrophic scenarios. Those are precisely the ones robustness analysis exists to catch.
- Recommend the robust strategy reflexively. If the cost of robustness is high and the catastrophic scenario is genuinely remote and survivable, the high-peak strategy may be correct — make the frontier choice explicit either way.

---

## Instructions

### Step 1 — Anchor the effectiveness scale
State what outcome counts as the strategy working, and where the survival floor sits (the weak/catastrophic boundary). All ratings reference this.

### Step 2 — Rate every cell
For each scenario, rate the strategy strong / acceptable / weak / catastrophic, with a one-line mechanism for the rating: *why* the strategy lands there in that world.

### Step 3 — Compute floor and expectation
- **Floor:** the worst rating across scenarios — the strategy is only as robust as its weakest cell.
- **Expectation:** if probabilities are given, the probability-weighted outcome. Report both; the gap between them is the fragility signal.

### Step 4 — Flag fragility
List every catastrophic cell and every weak cell. Catastrophic cells are mandatory to address; weak cells are addressed if the cost is reasonable.

### Step 5 — Design robustness modifications
For each fragile cell, propose a change to the strategy that would raise it to at least acceptable. For each modification, state:
- What it changes about the strategy.
- Which fragile cell(s) it lifts and to what level.
- **What it costs** in the strong/favored scenarios (the peak it gives up).
- Any cells it might *worsen* (modifications can have side effects).

### Step 6 — Re-rate under the modified strategy
Produce the full scenario rating for the modified strategy, and recompute floor and expectation. Now you have two rows: original and modified.

### Step 7 — Characterize the frontier
State the tradeoff plainly: original strategy = [peak], [floor]; modified strategy = [lower peak], [higher floor]. Describe the frontier — how much peak is given up per unit of floor gained.

### Step 8 — Make the frontier choice
Recommend where on the frontier to sit, justified by: the stakes (can the organization survive the catastrophic cell?), the cost of being wrong about the favored scenario, and the probability mass on the fragile scenarios. State the recommendation as a deliberate position on the frontier, not a default.

---

## False-Positive Prevention

1. **Catastrophe averaging.** Rolling a catastrophic cell into a mean that looks fine. The floor is reported separately and a catastrophic worst case is never diluted by strong cells.
2. **Favored-scenario halo.** Letting the strategy's strength in the expected world inflate its ratings elsewhere. Rate each cell on its own world's mechanics.
3. **Costless robustness.** Proposing modifications as pure upgrades. Every floor-raising move costs peak performance somewhere; if it doesn't, the original ratings were probably wrong.
4. **Robustness-as-blandness.** Flattening the strategy to be mediocre everywhere. The target is a higher floor at minimal peak cost, not uniform safety.
5. **Low-probability dismissal.** Excusing a catastrophic cell because the scenario is unlikely. Low-probability/high-impact is the whole reason for the test.
6. **Side-effect blindness.** Modifications that fix one cell and quietly break another. Re-rate the full set after each modification.
7. **Reflexive robust recommendation.** Always choosing the robust strategy. If catastrophe is remote and survivable and the robustness cost is high, the high-peak strategy can be right — make the frontier choice, don't default.
8. **Unanchored ratings.** Strong/weak with no reference to a defined outcome or floor. Anchor the scale in Step 1 and hold every rating to it.

---

## Output Format

```
# Robustness test — [strategy] against [scenario set]

## Effectiveness anchor
- **Working means:** [outcome that counts as success]
- **Survival floor (weak/catastrophic line):** [...]

## Original strategy — scenario ratings
| Scenario | Prob | Rating        | Mechanism (why it lands here)        |
|----------|------|---------------|--------------------------------------|
| [A]      | [..] | strong        | [...]                                |
| [B]      | [..] | acceptable    | [...]                                |
| [C]      | [..] | weak          | [...]                                |
| [D]      | [..] | catastrophic  | [...]                                |
- **Floor:** [worst rating]   **Prob-weighted expectation:** [...]

## Fragility
- Catastrophic cells (must address): [...]
- Weak cells (address if affordable): [...]

## Robustness modifications
| Modification        | Lifts cell(s)        | To level    | Cost in favored scenario | Side effects        |
|---------------------|----------------------|-------------|--------------------------|---------------------|
| [change]            | C, D                 | acceptable  | A drops strong→acceptable| [none / B → weak]   |
| [...]               |                      |             |                          |                     |

## Modified strategy — scenario ratings
| Scenario | Prob | Rating      | Mechanism                  |
|----------|------|-------------|----------------------------|
| [A]      | [..] | acceptable  | [...]                      |
| [B]      | [..] | acceptable  | [...]                      |
| [C]      | [..] | acceptable  | [...]                      |
| [D]      | [..] | acceptable  | [...]                      |
- **Floor:** [worst rating]   **Prob-weighted expectation:** [...]

## Robustness frontier
- Original: peak [..], floor [..]
- Modified: peak [..], floor [..]
- Tradeoff: [how much peak given up per unit of floor gained]

## Frontier choice (recommendation)
- **Sit at:** [original | modified | intermediate]
- **Because:** [stakes / survivability of catastrophic cell / cost of being wrong / probability mass on fragile scenarios]
```

---

## Verification

- [ ] Effectiveness outcome and survival floor anchored before rating.
- [ ] Every scenario rated strong/acceptable/weak/catastrophic with a mechanism.
- [ ] Floor reported separately from probability-weighted expectation.
- [ ] Every catastrophic cell flagged as mandatory to address.
- [ ] Each robustness modification states what it lifts, to what level, and its peak cost.
- [ ] Modifications re-rated across the full scenario set (side effects caught).
- [ ] Both original and modified strategy report floor and expectation.
- [ ] Robustness frontier characterized as an explicit peak-vs-floor tradeoff.
- [ ] Frontier choice recommended deliberately, not defaulted to "robust."
- [ ] No catastrophic cell averaged away or dismissed for low probability.
