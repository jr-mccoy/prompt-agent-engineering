---
title: "Monte Carlo Risk Quantification — Ranges In, a Loss Exceedance Curve Out, and No Fake Precision"
category: risk/quantification
description: "Quantify a small set of operational, project or enterprise risks by simulation: elicit calibrated ranges instead of point scores, choose distributions that fit the shape of each loss, model correlation through shared drivers, run the simulation in named software with a seed, read the loss exceedance curve against appetite, run a sensitivity check on the inputs that drive the tail, and explain the result to a non-quant in plain frequencies; distinct from `domain-finance/risk-management/finance_market_risk_var_stress.md` (market VaR on a trading portfolio) and `domain-finance/personal-finance-planning/finance_monte_carlo_withdrawal_analysis.md` (retirement withdrawals)."
techniques:
  - NE-10
  - NE-11
  - RT-23
  - QA-04
  - NE-13
difficulty: advanced
tags:
  - monte-carlo
  - risk-quantification
  - loss-exceedance-curve
  - calibrated-estimation
  - uncertainty
  - enterprise-risk
updated: "2026-09-24"
reasoning:
  styles: [probabilistic, quantitative, evidential]
  stakes: high
  horizon: months
  uncertainty: risk
  evidence_quality: sparse
  domain_complexity: cross_domain
  collaboration: small_team
  output_format: [structured, chart_spec]
  user_role: [risk-lead, analyst, finance, executive, operator]
  mode: [forecast, decide, explain]
related_prompts:
  - domain-finance/risk-management/finance_market_risk_var_stress.md
  - domain-risk/risk_register_builder.md
  - domain-risk/risk_appetite_statement.md
---

# Monte Carlo Risk Quantification

**Objective:** Replace "likelihood 3 × impact 4 = 12" with a statement a decision-maker can
use — "in about one year in eight, these risks together cost us more than $1M" — built from
ranges the estimators actually believe, simulated transparently, and explained without
pretending to more precision than the inputs carry.

**When to Use:**
- A register's top risks are competing for one budget and ordinal scores cannot say whether
  a $150k mitigation is worth it.
- The board or an insurer asks "how much could we lose in a bad year?"
- Two risks look similar on a heat map but one has a much fatter tail.
- You need to show the effect of a mitigation as a shift in a curve, not a change of colour.

**Not this prompt if:**
- The exposure is a traded portfolio and the question is market VaR — `domain-finance/risk-management/finance_market_risk_var_stress.md`.
- It is a household retirement plan — `domain-finance/personal-finance-planning/finance_monte_carlo_withdrawal_analysis.md`.
- You have not yet identified the risks — `risk_register_builder.md` first.
- No one can give even a rough range for a risk. Model the risks you can range, and list the
  rest separately; do not fill gaps with invented numbers.

## Inputs / Context

1. **The 3–10 risks** to quantify, each with a clear event definition and a one-year horizon (or state another).
2. **Estimators:** the people who know each risk, and whether they have had calibration practice.
3. **Evidence per risk:** internal loss history, near-misses, industry data, insurer or peer benchmarks.
4. **Shared drivers:** conditions that would make several risks likelier at once (a downturn, a key supplier, one IT platform).
5. **Appetite:** the loss level and probability the organisation says it tolerates.
6. **The tool** that will run the simulation (spreadsheet with a Monte Carlo add-in, R, Python). This prompt specifies the model; the tool computes it.

## Method

1. **Define each event so it can be counted.** "Ransomware causing more than 24 hours of
   outage in the next 12 months", not "cyber risk".

2. **Elicit ranges, and tag their source (RT-23).** For each risk: annual probability (or
   frequency) and a 90% interval for the loss if it happens. Tag every number: loss history /
   benchmark / estimator judgement. Ask estimators for the interval they would bet on at 9:1,
   and challenge any interval narrower than the evidence supports.

3. **Choose a shape per input (NE-11).** Loss severity: lognormal fitted to the 90% interval
   (skewed, never negative). Occurrence: Bernoulli for once-a-year events, Poisson for events
   that can recur. Bounded quantities (durations, percentages): PERT or triangular. Write each
   choice and parameters as a formula.

4. **Model correlation through drivers (NE-10).** Prefer an explicit shared driver ("in a
   downturn year, client loss and supplier failure both become likelier") over a correlation
   coefficient no one can estimate. Keep each risk's overall probability unchanged when you add
   the driver, so you change the joint behaviour, not the averages.

5. **Specify the run.** Iterations (10,000 minimum; 100,000 if the tail matters), random seed,
   software and version. Output: annual loss per iteration, summed across risks.

6. **Read the outputs.** Expected annual loss; probability of any loss; the loss exceedance curve
   (probability that annual loss exceeds each amount); the 90th, 95th and 99th percentiles.
   Compare to appetite: where does the curve cross the tolerance line?

7. **Test sensitivity (QA-04).** Re-run with each key input at its plausible alternative. Report
   which input moves the tail most — that is where better evidence or mitigation pays.

8. **Translate for the non-quant (NE-13).** Frequencies, not decimals ("about one year in
   eight"); round to two significant figures; state what is and is not included; say which input
   the answer depends on most.

## Output Format

```
# Risk quantification — [scope], [horizon], run [date]
Software: [tool, version] · Iterations: [n] · Seed: [n]

## Inputs
| Risk | Event definition | Annual probability | Loss if it occurs (90% interval) | Distribution | Source tag |
Shared drivers: [driver — which risks — how probabilities change — marginals preserved?]

## Results
Expected annual loss: [$] (by risk: ...)
Chance of any loss in a year: [%]
Loss exceedance: P(> $A) = [..] · P(> $B) = [..] · P(> $C) = [..]
Percentiles: 90th [$] · 95th [$] · 99th [$]
Against appetite: [where the curve crosses tolerance]

## Sensitivity
| Input changed | From → to | Effect on tail |

## Plain-language summary (for [audience])
[3–5 sentences, frequencies, rounded]

## Not in this model
[risks without ranges, excluded loss types, horizon limits]
```

## Verification

- [ ] Every event defined so an occurrence can be counted within the horizon.
- [ ] Every input is a range with a source tag; no point estimates standing in for uncertainty.
- [ ] Distribution and parameters stated as formulas for every input.
- [ ] Correlation modelled explicitly, with marginal probabilities preserved, or its absence stated.
- [ ] Software, iterations and seed recorded so the run is reproducible.
- [ ] Expected loss by risk sums to the total (analytic check against the simulated mean).
- [ ] Sensitivity names the input that drives the tail.
- [ ] Summary uses rounded frequencies and lists what is excluded.

## False-Positive Prevention

1. **Precision theatre.** "$347,697" from inputs that are guesses to ±50% is false. Round to two
   significant figures and say why.
2. **Narrow intervals.** Uncalibrated estimators give ranges that are too tight; an interval that
   would surprise no one is not a 90% interval. Widen, or record the calibration gap.
3. **Invented inputs.** When no one can range a risk, list it under "not in this model" rather than
   inserting a number to complete the table.
4. **Normal distributions for losses.** Losses are skewed and non-negative; a normal curve puts
   probability on negative losses and understates the tail.
5. **Correlation by assertion.** A coefficient of 0.4 no one can justify is decoration; name the
   shared driver or say you assumed independence.
6. **Expected loss as the answer.** The average hides the tail the decision is usually about. Lead
   with the exceedance curve.
7. **The model computed here.** This prompt specifies the model; the numbers come from the named
   tool's run, with its seed, not from mental arithmetic.

## Example Output

```
# Risk quantification — 120-person distributor, next 12 months, run 2026-09-20
Software: Python 3.12 (standard library random) · Iterations: 100,000 · Seed: 42

## Inputs
| R1 Ransomware | Outage > 24h | 0.15 | $200k–$2.5M | lognormal | benchmark + IT Lead judgement |
| R2 Key client loss | Top-5 client leaves | 0.20 | $400k–$1.5M | lognormal | 8-year client history |
| R3 Supplier failure | Primary supplier stops > 2 weeks | 0.10 | $100k–$900k | lognormal | Ops judgement |
Shared driver: downturn year (probability 0.20) → R2 0.60 / R3 0.35; otherwise R2 0.10 / R3 0.0375
(marginals preserved: 0.2×0.60 + 0.8×0.10 = 0.20; 0.2×0.35 + 0.8×0.0375 = 0.10)

## Results
Expected annual loss: about $350k (R1 $142k + R2 $168k + R3 $38k = $348k analytic; simulated $348k)
Chance of any loss in a year: 37%
Loss exceedance: P(> $500k) 27% · P(> $1M) 13% · P(> $2M) 2.5% · P(> $3M) 0.7%
Percentiles: 90th $1.1M · 95th $1.5M · 99th $2.7M
Against appetite (no more than 5% chance of losing > $1.5M): just over — 95th percentile ≈ $1.55M; the R1 mitigation below brings it to ≈ $1.36M

## Sensitivity
| Downturn correlation | independent → shared driver | 95th: $1.50M → $1.55M (small) |
| R1 upper bound | $2.5M → $1.5M (tested restores, faster recovery) | P(> $2M): 2.5% → 1.3%; 99th: $2.7M → $2.1M |

## Plain-language summary (for the board)
In roughly two years out of three, none of these three events happens. In about one year in eight,
together they cost more than $1M; in about one year in forty, more than $2M. The bad-year figure
depends mostly on how long a ransomware outage would last, so proving we can restore quickly
moves the tail more than anything else modelled.

## Not in this model
Regulatory fines (no one could range them); reputational effects beyond lost revenue; multi-year effects.
```

## Techniques Used

- **NE-10 Probability-Weighted Scenarios** — shared-driver correlation with preserved marginals.
- **NE-11 Embedded Calculation Formulas** — distributions and parameters written as formulas.
- **RT-23 Input Provenance Tagging** — every range tagged to its source.
- **QA-04 Uncertainty Acknowledgment** — sensitivity, rounding and an explicit exclusions list.
- **NE-13 Technical-to-Business Translation** — frequencies a board can act on.

## Related Prompts

- `domain-finance/risk-management/finance_market_risk_var_stress.md` — market VaR and stress tests for trading exposures.
- `domain-risk/risk_register_builder.md` — the risks and owners this quantifies.
- `domain-risk/risk_appetite_statement.md` — the tolerance line the exceedance curve is read against.
- `domain-risk/risk_tail_risk_scan.md` — the risks that belong under "not in this model".
