---
title: "Economic Scenario Modeler — Internally Consistent Base / Optimistic / Pessimistic / Stress Macro Scenarios"
category: finance/markets-macro
description: "Build a coherent set of macro scenarios (base, optimistic, pessimistic, stress) with internally consistent assumptions across GDP, inflation, policy rates, employment, FX, and credit — then trace implications for sectors, assets, or a specific business decision."
techniques:
  - NE-10
  - NE-11
  - RT-06
  - QA-02
  - QA-04
difficulty: advanced
tags:
  - macro
  - scenario-analysis
  - economic-forecasting
  - stress-testing
  - regime
updated: "2026-06-08"
related_prompts:
  - domain-finance/markets-macro/finance_macro_indicator_dashboard_interpreter.md
  - domain-finance/markets-macro/finance_inflation_regime_analysis.md
  - domain-finance/risk-management/finance_stress_test_scenario_design.md
  - domain-finance/field_guide.md
---

**Informational only — not investment advice. Scenarios are illustrative analytical constructs, not forecasts; all outputs require review by qualified professionals.**

## Objective

Construct four internally consistent macroeconomic scenarios — **base, optimistic, pessimistic, stress** — in which every variable (GDP growth, inflation, policy rate, unemployment, FX, credit spreads, commodity proxy) moves in a way that is mutually coherent, then map the implications to the user's chosen lens (sectors, asset classes, or a specific business/investment decision). The deliverable is a scenario matrix with explicit drivers, transmission logic, and probability commentary — not a single point forecast.

## When to Use

- Annual planning, capital allocation, or budget-setting requiring a macro backdrop
- Stress-testing a portfolio, balance sheet, or business plan against adverse regimes
- Framing an investment thesis or treasury decision against a range of macro paths
- Pre-mortem on a strategic decision exposed to the cycle (e.g., a debt raise, capacity expansion)
- Translating a vague "what if the economy turns" question into a structured set of paths

## Inputs / Context Required

```
<scenario_setup>
Region / economy: (e.g., US, Eurozone, UK, EM aggregate — single economy or block)
Currency & base date: (e.g., USD, as of 2026-06-08)
Horizon: (e.g., 4 quarters, 1–3 years, full cycle)

CURRENT STARTING CONDITIONS — USER MUST SUPPLY (do not assert from memory):
- Real GDP growth (latest print, YoY or annualized):
- Headline & core inflation (latest, YoY):
- Policy rate (current target) and stated central-bank guidance:
- Unemployment rate (latest):
- 10Y govt yield / key spreads (IG, HY) if relevant:
- FX level vs. relevant cross (if relevant):
- Any commodity proxy relevant to the analysis (oil, etc.):
Source & date for each input: (e.g., BLS, BEA, central bank release, Bloomberg snapshot)

ANALYSIS LENS (choose):
[ ] Sector implications  [ ] Asset-class implications  [ ] Specific decision: __________

KNOWN CONSTRAINTS / FOCUS:
- Particular shocks of concern (energy, geopolitical, banking stress, fiscal):
- Any variables that are fixed/exogenous for this exercise:
</scenario_setup>
```

If current starting conditions are not supplied, **stop and request them**. Do not fabricate current macro readings.

## Constraints

### Must
- Anchor every scenario to the user-supplied starting conditions; show the path from "today" to each scenario state.
- Make assumptions internally consistent across variables (NE-10): e.g., a strong-growth scenario cannot simultaneously show falling rates, falling inflation, and rising unemployment without an explicit, stated mechanism.
- State the transmission logic linking variables (RT-06): why a given GDP path implies a given inflation, rate, and labor path.
- Show any quantitative bridge as formula → inputs → result (NE-11).
- Provide a qualitative probability band per scenario (e.g., "more likely / less likely / tail") with reasoning; do not assign false-precision point probabilities unless the user supplies a model basis.
- Include a disconfirming check per scenario: what data print would falsify it.
- Name the regime/recency-bias guardrail explicitly and apply it.

### Must Not
- Assert current rates, inflation, GDP, or central-bank stance from memory — these are user inputs.
- Present a single point forecast labeled as "the outlook."
- Build a scenario where variables contradict (e.g., booming GDP + spiking unemployment) without an explicit stated mechanism.
- Anchor all four scenarios to a small perturbation of the base (the pessimistic/stress cases must explore genuinely different regimes, not base ± 0.5%).
- Imply the stress scenario is "worst possible" — label it as a defined severe-but-plausible construct.

## Instructions

**Step 1 — Lock the starting point.** Restate the user-supplied current readings in a table with source + date. Flag any missing input.

**Step 2 — Define the four scenario narratives.** One-paragraph causal story each:
- **Base:** central tendency given current conditions and stated guidance.
- **Optimistic:** favorable but plausible (e.g., soft landing, productivity surprise, disinflation without recession).
- **Pessimistic:** adverse but orderly (e.g., growth stall, sticky inflation forcing higher-for-longer).
- **Stress:** severe-but-plausible regime break (e.g., stagflationary shock, credit event, sharp recession) — define the trigger.

**Step 3 — Populate the variable matrix.** For each scenario, set values for every variable. Enforce consistency using the transmission relationships:

```
Coherence checks (state the mechanism if a pairing looks unusual):
  Growth ↑  → typically labor tightens (unemployment ↓), inflation pressure ↑ → policy rate ↑ (or higher-for-longer)
  Growth ↓  → unemployment ↑, demand-driven inflation eases; supply shock can break this (stagflation)
  Inflation ↑ persistently → policy rate ↑ → curve dynamics (front-end ↑); growth pressure with a lag
  Risk-off stress → credit spreads ↑, safe-haven FX ↑, equity ↓, policy may cut (demand shock) or be trapped (supply shock)
```

**Step 4 — Quantitative bridges where used.** For any derived figure, show the formula. Examples:

```
Real policy rate            = Nominal policy rate − Expected inflation
Approx. nominal GDP growth  ≈ Real GDP growth + GDP deflator (inflation proxy)
Okun's-law sketch (illustrative): ΔUnemployment ≈ −β × (Real GDP growth − Potential growth)
   [β and potential growth are user/assumption inputs; state them]
```

**Step 5 — Map implications to the chosen lens.** For sectors/assets/decision, state directional impact and the channel (rates, demand, input costs, FX, credit).

**Step 6 — Probability & disconfirmation.** Assign each scenario a likelihood band with reasoning, and one falsifying indicator each.

**Step 7 — Adversarial stress-test (QA-02).** Attack the base case: which single assumption, if wrong, most changes the conclusion? Is the stress scenario actually severe enough, or anchored too close to base?

**Step 8 — Bias guardrail.** Apply recency-bias and regime-blindness checks: are scenarios just an extrapolation of the recent past? Force at least one scenario with a regime different from the trailing 12–24 months.

## Output Format

### Starting Conditions (user-supplied)

| Variable | Current value | Source | As-of date |
|---|---|---|---|
| Real GDP growth | | | |
| Headline / core inflation | | | |
| Policy rate (+ guidance) | | | |
| Unemployment | | | |
| 10Y yield / spreads | | | |
| FX / commodity proxy | | | |

### Scenario Narratives
[One paragraph per scenario — Base / Optimistic / Pessimistic / Stress, each with its causal trigger]

### Scenario Variable Matrix

| Variable | Base | Optimistic | Pessimistic | Stress |
|---|---|---|---|---|
| Real GDP growth | | | | |
| Headline inflation | | | | |
| Core inflation | | | | |
| Policy rate (end-horizon) | | | | |
| Unemployment | | | | |
| 10Y yield | | | | |
| Credit spreads (IG/HY) | | | | |
| FX (relevant cross) | | | | |
| Commodity proxy | | | | |
| **Coherence note** | | | | |

### Implications — [chosen lens]

| Sector / Asset / Decision factor | Base | Optimistic | Pessimistic | Stress | Primary channel |
|---|---|---|---|---|---|

### Probability & Disconfirmation

| Scenario | Likelihood band | Reasoning | Falsifying indicator |
|---|---|---|---|

### Stress-Test & Bias Findings
[Step 7 + Step 8 — most fragile assumption; regime-diversity check]

## Verification

- [ ] All starting conditions are user-supplied with source + date; none asserted from memory.
- [ ] Each scenario's variables are internally consistent; any unusual pairing has a stated mechanism.
- [ ] Transmission logic is explicit, not assumed.
- [ ] Any derived number shows formula → inputs → result.
- [ ] Four distinct regimes are represented; stress and pessimistic are not base ± small delta.
- [ ] Each scenario has a likelihood band and a falsifying indicator.
- [ ] Recency-bias / regime-blindness guardrail applied; at least one non-extrapolative regime present.
- [ ] Implications tie to a stated transmission channel, not asserted directionally.

## False-Positive Prevention

| Overclaim risk | Guardrail |
|---|---|
| Presenting the base case as "the forecast" | Always present four scenarios with likelihood bands; label base as central tendency, not prediction |
| Scenarios are just base ± 0.5% across the board | Require genuinely different regimes; stress must define a trigger and a regime break |
| Internally contradictory scenario (boom + rising unemployment) | Coherence check row mandatory; any unusual pairing requires an explicit mechanism |
| Stating current macro readings from memory | Starting conditions are user inputs with source/date; stop if missing |
| False-precision probabilities | Use likelihood bands with reasoning unless the user supplies a model basis for point probabilities |
| Recency-driven scenario set | Apply regime-blindness guardrail; force ≥1 scenario unlike the trailing 12–24 months |
