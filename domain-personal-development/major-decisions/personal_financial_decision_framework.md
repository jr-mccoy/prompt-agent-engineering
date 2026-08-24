---
title: "Personal Financial Decision Framework — What It Optimizes, Tail Risk, Irreversibility, and Fee-Only Smell Test"
category: personal-development/major-decisions
description: "Framework for evaluating a major personal financial decision: mortgage sizing, leverage, asset allocation shift, large purchase financing, early retirement feasibility, business loan, equity vs. cash compensation, investment concentration. Forces clarity on what the decision actually optimizes (not just return), the time horizon, tax implications, tail-risk scenarios, and irreversibility. Ends with the fee-only advisor smell test: would a fiduciary with no stake in the outcome make this same recommendation?"
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
  - personal-decisions
  - financial
  - tradeoffs
  - risk
  - decision-quality
updated: "2026-05-11"
reasoning:
  styles: [analytic, bayesian, systems, counterfactual]
  stakes: high
  horizon: years
  uncertainty: risk
  evidence_quality: moderate
  domain_complexity: cross_domain
  collaboration: solo_or_pair
  output_format: structured
  user_role: [individual, couple, household]
  mode: [decide, audit, diagnose]
related_prompts:
  - domain-personal-development/major-decisions/personal_relocation_decision.md
  - domain-personal-development/major-decisions/personal_major_purchase_research.md
  - domain-personal-development/major-decisions/personal_career_offer_evaluation.md
  - domain-decision-making/tradeoff_reversibility_stakes_grid.md
  - domain-decision-making/decisioning_regret_minimization.md
  - domain-decision-making/documentation/decisiondoc_options_memo.md
---

# Personal Financial Decision Framework

**Objective:** Structure the analysis of a major personal financial decision — one large enough that a wrong answer has multi-year consequences. Walks through what the decision is actually optimizing (which is rarely just expected return), the relevant time horizon, tax implications, tail-risk scenarios, irreversibility analysis, and comparison to the base case. Ends with a specific adversarial check: would a fee-only fiduciary with no stake in the outcome recommend this? The prompt is compatible with any major financial decision; it forces the structure the decision deserves rather than the structure that's comfortable.

**When to use:**
- Deciding how much mortgage to take on.
- Evaluating leverage on any asset class.
- Making a significant shift in asset allocation.
- Deciding between equity compensation and cash compensation.
- Evaluating investment concentration in a single company, sector, or asset.
- Early retirement or FIRE feasibility analysis.
- Business loan or self-funding a venture.
- Any financial decision where the downside scenario would be materially painful.

**When NOT to use:**
- Routine budget decisions or purchases not requiring multi-year analysis.
- The decision is primarily non-financial (use the relevant domain prompt for the primary dimension).
- Decisions below your personal "I can absorb this if wrong" threshold.

**Audience:** Individuals or couples making a financial decision large enough that a structured analysis changes the expected outcome.

---

## Inputs / Context

1. **The decision.** What specifically is being considered, including the full set of options.
2. **Current financial state.** Income, assets, liabilities, liquidity, existing obligations.
3. **Time horizon.** When the decision's consequences play out. For leverage or concentration: when do you need to be whole again?
4. **What you're trying to optimize.** This is the most important input and the one most often unstated. Candidates: expected return, risk-adjusted return, peace of mind, optionality, life fit, financial independence, capital preservation.
5. **Tax situation.** Filing status, marginal rate, capital gains situation, relevant account types.

---

## Constraints

### Must
- Clarify what the decision is optimizing before evaluating options. A decision that's optimal for expected return may be suboptimal for peace of mind, liquidity, or optionality — and the right objective changes the analysis.
- Model the base case explicitly — what happens if you do nothing?
- Compute scenarios: expected case, pessimistic case, tail case (the bad outcome that's unlikely but possible and survivable vs. not).
- Assess irreversibility: what's the cost and path of reversing this decision if it goes wrong?
- Apply the fee-only smell test: would a fiduciary advisor with no commission or product stake make this recommendation?
- Surface tax implications — many financial decisions look different pre- and post-tax.
- Explicitly address concentration and correlation risk if relevant.

### Must Not
- Reduce the decision to expected-value calculation alone. Expected value is necessary but not sufficient; variance, liquidity, and tail risk matter at the individual level in ways they don't at the portfolio level.
- Assume financial decisions exist in isolation from life decisions. A mortgage that's optimal financially but requires both partners to stay in current jobs for 10 years is a life decision too.
- Let the person recommending the transaction (broker, lender, advisor with AUM fee) define the analysis. They have incentives; model the decision from your position, not theirs.
- Treat leverage as just "amplified return." Leverage also amplifies loss and adds liquidity constraint. Walk both directions.
- Skip the tail scenario because it's uncomfortable to contemplate.

---

## Instructions

### Step 1 — Clarify what you're optimizing
Write it down: "This decision is being optimized for ___." Options:
- Expected return (probability-weighted average outcome)
- Risk-adjusted return (Sharpe-like: return per unit of risk you're bearing)
- Liquidity (maintaining access to capital)
- Peace of mind (reduced anxiety, simpler sleep)
- Optionality (preserving future choices)
- Life fit (allows the lifestyle you want regardless of financial optimality)
- Financial independence (reaching a number at which work becomes optional)
- Capital preservation (avoiding permanent loss of capital)

If you're optimizing for more than one, rank them. Conflicts between objectives are where decisions get hard.

### Step 2 — Model the base case
What happens if you make no change? Model forward:
- Financial state in 3 years.
- Financial state in 10 years.
- What the base case preserves (optionality, liquidity) and what it gives up (return, compounding, opportunity).

### Step 3 — Model the decision scenarios
For each option under consideration:
- **Expected case:** what happens if things go roughly as planned?
- **Pessimistic case:** what happens if the investment underperforms, rates move against you, income drops, or the market turns?
- **Tail case:** what happens in the worst plausible scenario? Can you survive it? How does it compare to your base case?

For each scenario, trace: portfolio impact, liquidity impact, lifestyle impact, reversibility.

### Step 4 — Assess irreversibility
- What's the cost (financial, time, opportunity) of unwinding this decision if it goes wrong?
- At what point does the decision become difficult to reverse? (6 months? 2 years? 10 years?)
- What are the reversal options and their costs?

Decisions with low reversal cost deserve less caution than decisions that lock you in.

### Step 5 — Tax analysis
- What are the tax implications of the decision as structured?
- Is there a tax-equivalent option that achieves similar expected return at lower tax drag?
- What's the after-tax expected return vs. the pre-tax expected return?
- Capital gains implications if applicable (short-term vs. long-term, tax-loss harvesting opportunity, wash-sale).
- For equity compensation: tax treatment of stock options or RSUs at grant, vest, and exercise.

### Step 6 — Concentration and correlation risk
- Does this decision increase concentration in a single asset, company, sector, or geography?
- How correlated is this decision with your existing assets and income? (Company stock + salary from same company = double concentration; a home in the same city where you're employed = correlated risk.)
- What's the plan if the concentrated asset declines significantly?

### Step 7 — Leverage analysis (if applicable)
If the decision involves leverage (mortgage, margin, business loan):
- What's the maximum drawdown you can sustain before a margin call or forced sale?
- What does debt service look like under the pessimistic income scenario?
- What's the interest rate risk if rates move adversely?
- At what income or asset level does leverage become unserviceable?

### Step 8 — Fee-only smell test
Before finalizing the analysis, ask:
- A fee-only fiduciary financial advisor — someone paid by the hour, with no commission, no AUM fee, no product to sell — is looking at this recommendation. Would they make the same recommendation?
- If the answer is "probably not" or "I'm not sure," what's driving the gap? Is it a genuine optimization for your specific situation, or is it a rationalization?
- Is the person currently recommending this action compensated in any way that aligns with you proceeding?

### Step 9 — Decision and documentation
- Recommended option with rationale anchored to: objective, expected case, tail case, reversibility.
- What new information would change the recommendation?
- Tripwires: if [condition], then [action] — pre-commit to the trigger, not the in-the-moment judgment.
- Calibration anchor: what you're choosing and why, written in one sentence today.

---

## False-Positive Prevention

1. **Expected-value reductionism.** At the individual level, variance matters enormously. Two decisions with the same expected value can have wildly different tails; optimize for the one you can survive.
2. **Leverage asymmetry blindness.** Leverage amplifies gains in discussion and losses in reality. Walk the downside scenario explicitly.
3. **Advisor incentive blindness.** The person recommending the transaction is often compensated on the transaction. Their analysis is not independent.
4. **Tax-drag omission.** Pre-tax returns are not the returns you keep. Model after-tax.
5. **Reversibility overconfidence.** "I can always sell" is sometimes true (liquid asset) and sometimes not (illiquid investment, mortgage in a down market, business loan).
6. **Concentration normalization.** Heavy concentration in company stock is common; that makes it normal, not safe. Correlation with your employment income is a double exposure.
7. **Base-case skip.** The "do nothing" option is almost always available and often undervalued. Model it explicitly before evaluating any action.
8. **Tail scenario avoidance.** Contemplating the tail scenario is uncomfortable; skipping it makes the analysis feel cleaner and more optimistic. The tail scenario is the most important scenario for irreversible decisions.
9. **Peace-of-mind invisibility.** A financially optimal decision that causes persistent anxiety has a hidden cost. Peace of mind has real value; quantify it honestly.

---

## Output Format

```
# Financial decision — [what's being decided]

## What this decision optimizes
Primary objective: [...]
Secondary objectives (ranked): [...]
Objective conflicts: [where they pull in different directions]

## Base case (do nothing)
- 3-year financial state: [...]
- 10-year financial state: [...]
- What base case preserves: [...]
- What base case gives up: [...]

## Scenario analysis per option
| Option       | Expected case outcome | Pessimistic case outcome | Tail case outcome | Survivable? |
|--------------|-----------------------|--------------------------|-------------------|-------------|
| [Option A]   |                       |                          |                   |             |
| [Option B]   |                       |                          |                   |             |
| Base case    |                       |                          |                   |             |

## Irreversibility
| Option     | Reversal cost (financial) | Reversal cost (time) | Locks in by (date) | Reversal options |
|------------|--------------------------|----------------------|--------------------|------------------|
| [Option A] |                          |                      |                    |                  |

## Tax analysis
- Pre-tax expected return: [...]
- After-tax expected return: [...]
- Tax-equivalent alternatives: [...]
- Capital gains / option / RSU considerations: [...]

## Concentration and correlation
- New concentration created: [asset / company / sector / geography]
- Correlation with existing assets / income: [high / moderate / low — specifics]
- Plan if concentrated asset declines 50%: [...]

## Leverage analysis (if applicable)
- Max sustainable drawdown before crisis: [...]
- Debt service at pessimistic income: [...]
- Interest rate stress test: [...]

## Fee-only smell test
- Would a fee-only fiduciary recommend this? [yes / no / uncertain — why]
- Who is recommending this and what's their compensation structure? [...]
- Gap from independent recommendation: [if any]

## Decision
- Recommended option: [...]
- Rationale: [objective-anchored, tail-tested]
- Tripwire: if [condition] within [time], [action]
- What would change this: [...]
- Calibration anchor (write down today): "I am choosing [option] to optimize [objective], accepting the tail risk that [named scenario], with the tripwire that [condition triggers re-evaluation]."
```

---

## Verification

- [ ] Optimization objective stated explicitly (not assumed to be "expected return").
- [ ] Base case modeled at 3 and 10 years.
- [ ] Three scenarios per option: expected, pessimistic, tail.
- [ ] Tail survivability assessed explicitly.
- [ ] Irreversibility assessed with reversal cost and lock-in point.
- [ ] Tax analysis includes after-tax returns.
- [ ] Concentration and correlation with existing assets assessed.
- [ ] Leverage downside walked (if applicable).
- [ ] Fee-only smell test applied.
- [ ] Decision includes tripwire and calibration anchor.
