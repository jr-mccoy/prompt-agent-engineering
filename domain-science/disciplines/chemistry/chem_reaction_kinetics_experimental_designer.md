---
title: "Reaction Kinetics Experimental Designer"
category: science/disciplines/chemistry
description: "Design a kinetics experiment that returns a defensible rate law: order in each component, temperature dependence, mechanistic discriminators, and sensible fit strategy"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - kinetics
  - rate-law
  - mechanism
  - eyring
  - arrhenius
  - rpkinetic-analysis
  - vtna
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/chemistry/chem_synthesis_route_critique.md
  - domain-science/methods-foundations/science_experimental_design_advisor.md
---

# Reaction Kinetics Experimental Designer

**Objective:** Design a kinetics experiment that yields a defensible rate law — order in each component, rate constant with uncertainty, activation parameters (Arrhenius / Eyring), and a discrimination among competing mechanisms — using methods modern enough for a contemporary mechanistic paper (RPKA / VTNA + classical pseudo-first-order experiments + isotope effects + cross-over).

**When to use:** When a synthetic reaction has been demonstrated to work and the user now wants to understand it (order in catalyst, substrate, oxidant; turnover-limiting step; on-cycle vs. off-cycle catalyst resting state; reversibility of a step). Also useful when a kinetic claim is being made in a paper draft and the user needs to audit whether the data actually support it.

**Required inputs:**
- **Transformation** as substrate → product, with all named reagents and the suspected role (substrate, catalyst, oxidant, base, reductant, additive).
- **Question.** Order determination, rate constant, activation parameters, mechanistic discrimination, identification of resting state, isotope effect, off-cycle pathway test.
- **Monitoring method available.** In-situ IR (ReactIR), in-situ NMR (NMR tube or flow), GC / GC-MS, HPLC, UV-Vis, calorimetry (RC1 / heat-flow), MS, sampling and quench.
- **Time / concentration regime.** Approximate half-life or expected time to completion; concentration range accessible.
- **Temperature range available.** Glassware + bath ranges.

**Optional inputs:**
- Suspected mechanism(s) and the discriminating prediction of each.
- Existing kinetics data (yield-vs-time curves, partial orders).
- Sensitivity of substrate / product to the monitoring method.

**Constraints — Must:**
- Distinguish between *initial rate* methods (multiple separate runs), *graphical / pseudo-first-order* methods (one run with most components in excess), and *modern progress-curve* methods (RPKA / VTNA). Pick the method matched to the question and to the monitoring instrument.
- Require at least two orthogonal experiments per order determined (e.g., different-excess + same-excess for catalyst deactivation; VTNA + initial-rate for substrate).
- Distinguish *kinetic order* from *stoichiometric coefficient*. They are not the same.
- For activation parameters, require ≥4 temperatures spanning a meaningful range (typically ≥30 K) and report ΔH‡ / ΔS‡ from Eyring (not just Arrhenius Ea), with covariance-aware uncertainty.
- For isotope effects, distinguish primary vs. secondary; specify whether the experiment is competition (intermolecular) or parallel (intramolecular) and what each tells you.
- For mechanism discrimination, list each candidate mechanism's *unique* prediction and design the discriminator experiment.

**Constraints — Must Not:**
- Do not propose a single in-situ NMR run as proof of overall order in two components.
- Do not propose Arrhenius without verifying linearity across temperatures (curved plots imply changing mechanism).
- Do not fit a multi-parameter mechanistic model to noisy yield-vs-time data without identifiability analysis.
- Do not invent activation parameters, rate constants, or isotope effects.
- Do not call a Hammett or LFER plot "evidence" without ≥5 substrates and a residual analysis.

**Instructions:**

1. **Lock the kinetic question.** Output it as one of: order in [component]; rate constant; activation parameters; mechanism discrimination (Mechanism A vs. B); resting state ID; pre-equilibrium vs. rate-limiting bond formation; off-cycle pathway test. Multiple questions are allowed but must be ranked.

2. **Pick monitoring method matched to the chemistry.** Build a small table: ReactIR / NMR / GC / HPLC / UV-Vis / calorimetry against (time resolution, concentration sensitivity, selectivity in mixture, interference with the reaction). Pick one primary and one confirmatory.

3. **Pick kinetic-method family.** From {initial-rate-with-variation, pseudo-first-order with excess components, VTNA / RPKA on progress curves, stopped-flow for fast steps, isotope-effect (KIE / EIE), Hammett / LFER, competition, cross-over, mercury / poisoning, in-flask / out-of-flask interconversion}. Match to question.

4. **Concentration / temperature design.** For order determination: at least four substrate concentrations spanning ≥5× range; at least three catalyst loadings; same-excess and different-excess runs. For Eyring: at least four temperatures spanning ≥30 K, ideally five. For KIE: paired runs with H vs. D, with separate plus competition experiments.

5. **Mechanism-discriminator experiments.** For each candidate mechanism, list its *unique* prediction (e.g., turnover-limiting C–H cleavage predicts large primary KIE; rate-limiting oxidative addition predicts saturation kinetics in catalyst; bimetallic mechanism predicts non-first-order in catalyst). Design one experiment per discriminator.

6. **Data acquisition and quality.** Per-run: pre-equilibration time, sampling cadence, total monitoring time relative to half-life (≥3 half-lives for good fit), internal standard for quantification, baseline / drift control, calibration.

7. **Fit strategy and uncertainty.** Specify the model fit at each stage: linear fit (e.g., ln[A] vs. t for first-order), VTNA overlay assessment, Eyring fit with ΔH‡ / ΔS‡ covariance, Hammett fit with ρ and σ. Specify whether weighted or unweighted; whether covariance reported; whether residual plot is required and what passing looks like.

8. **Pitfalls and validation.** Enumerate: product inhibition, catalyst deactivation, induction periods, mass-transfer limitation, autocatalysis, heterogeneous artifact, solvent / atmosphere drift, instrument baseline drift. Specify the diagnostic for each.

9. **Reproducibility unit.** Number of independent runs per condition (typically ≥3); independent batch of catalyst / substrate if possible; freshness of reagents; environment control (Schlenk / glovebox if needed).

**Output format (locked):**

```
## Kinetic question (ranked)
| Rank | Question | Why this question |

## Monitoring method
| Method | Time res | Conc sens | Selectivity | Interference | Primary? |

## Kinetic-method family
- Primary:
- Confirmatory:
- Why matched:

## Concentration / temperature design
| Variable | Levels | Range | Rationale |

## Mechanism discriminators
| Candidate mechanism | Unique prediction | Discriminator experiment | Expected sign |

## Per-run acquisition spec
- Half-lives monitored:
- Sampling cadence:
- Internal standard:
- Pre-equilibration:

## Fit strategy
| Stage | Model | Weighted? | Uncertainty reporting | Residual check |

## Pitfall register
| Pitfall | Diagnostic | Mitigation |

## Reproducibility
- Independent runs per condition:
- Independent batches:
- Atmosphere / glovebox?

## Reporting standard alignment
[journal-specific kinetic-reporting expectations; ACS / RSC / Wiley]

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** Modern mechanistic-kinetics practice (Blackmond RPKA; Burés VTNA): in-situ progress-curve overlays with same-excess / different-excess; Eyring rather than Arrhenius alone; covariance-aware uncertainty; KIE with explicit competition vs. parallel framing; Hammett with residual analysis.

**Verification checklist:**
- [ ] Kinetic question lockedified, ranked if multiple.
- [ ] Monitoring method and kinetic-method family matched.
- [ ] ≥4 substrate concentrations spanning ≥5× for order determination.
- [ ] ≥4 temperatures spanning ≥30 K for Eyring.
- [ ] Mechanism-discriminator unique predictions named per candidate.
- [ ] Fit strategy specifies covariance-aware uncertainty and residual check.
- [ ] Pitfall register includes product inhibition, induction, mass-transfer, deactivation.
- [ ] ≥3 independent runs per condition specified.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Order from one excess run | "First order in substrate — log-linear plot" | Different-excess + same-excess required |
| Arrhenius linearity assumed | Curved Eyring across mechanism crossover | ≥4 T points, residual check |
| KIE direction misread | Inverse secondary KIE called "primary" | Competition / parallel framing explicit |
| Hammett from 3 substrates | ρ reported on 3 points | ≥5 substrates with residuals |
| Product inhibition masquerading as decay | Rate constant "falls" mid-run | Diagnostic in pitfall register |
| Mass-transfer artifact | Apparent rate independent of catalyst | Stirring rate / particle-size test |
| Heterogeneous artifact in "homogeneous" catalysis | Hg or PPh3 poisoning would have killed it | Poisoning / filtration test required |
| Multi-parameter overfit | Mechanistic model with 5 params from 12 points | Identifiability analysis required |
| Invented Eyring numbers | Plausible ΔH‡ / ΔS‡ in output | All numbers from user data or `[user-supplied]` |
