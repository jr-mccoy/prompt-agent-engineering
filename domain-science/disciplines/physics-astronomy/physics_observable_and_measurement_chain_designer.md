---
title: "Observable and Measurement-Chain Designer"
category: science/disciplines/physics-astronomy
description: "Trace the chain from a physical observable to a publishable claim: definition, signal model, detector response, calibration, reduction, statistical inference, and what the chain can and cannot conclude"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - physics
  - observable
  - measurement
  - calibration
  - detector-response
  - inference-chain
  - signal-model
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/physics-astronomy/physics_systematic_uncertainty_budget_drafter.md
  - domain-science/methods-foundations/science_experimental_design_advisor.md
---

# Observable and Measurement-Chain Designer

**Objective:** Trace, end-to-end, the chain from a physical observable to a publishable claim — from the operational definition of the observable through the signal model, detector response, calibration / unfolding, reduction, statistical inference, and finally the form of the claim and what the chain can and cannot support. The goal is to expose silent steps that often collapse later under scrutiny.

**When to use:** When designing a new measurement (HEP analysis, condensed-matter transport, optics / quantum-optics, gravitational-wave search, precision metrology, dark-matter direct detection); when a measurement gives a number that "looks right" but the user is uneasy about what it actually means; when reviewing a colleague's analysis where the claim might outrun the chain.

**Required inputs:**
- **The claim.** Written as a single sentence with the observable, the value, the uncertainty form (stat / syst), and the inference (cross section / coupling / mass / phase / asymmetry / rate / coefficient).
- **The observable.** Operational definition — what is *actually* measured at the detector.
- **The signal model.** What process produces the observable; theoretical inputs; what is fixed vs. profiled vs. left free.
- **Detector / apparatus.** What records the observable; resolution; efficiency; acceptance; known biases.
- **Calibration path.** How raw recorded data become physical quantities.
- **Reduction pipeline.** From recorded data to the analyzed quantity (selection cuts, unfolding, vetoes, fits, blind / unblind protocol).
- **Statistical framework.** Frequentist, Bayesian, profile-likelihood, CLs, Feldman-Cousins, hypothesis-test, parameter-estimation.

**Optional inputs:**
- Known prior measurements (user-supplied).
- Theoretical predictions to compare to.
- Blinding plan.
- Combination plans with other experiments.

**Constraints — Must:**
- Make every step in the chain explicit. Forbid silent steps — anything implicit becomes a row in the table.
- Distinguish three claim grammars: *measurement of a parameter* (value ± stat ± syst), *test of a hypothesis* (p-value / significance), and *limit-setting* (upper / lower bound at stated CL). The chain depends on which grammar.
- Distinguish efficiency, acceptance, and selection. They are not interchangeable.
- Distinguish detector resolution from unfolding regularization — unfolding can hide bias if the regularization is mis-set.
- Require a closure / null test: measurement applied to a known-answer case (control region; simulation injection; known calibrator) and the answer recovered within stated uncertainty.
- Require a blinding strategy if the analysis is hypothesis-test or limit-setting on a novel signal: define the analysis box before unblinding, lock cuts, record any post-unblinding change.
- Align reporting to the field's expectations: HEP-style (CMS / ATLAS / LHCb analysis notes); astrophysics (full systematics table per major journal); metrology (CIPM / BIPM uncertainty notation; GUM expanded uncertainty with coverage factor).

**Constraints — Must Not:**
- Do not let the signal model and the background model share the same systematic without correlation accounting.
- Do not invent past measurement values, theoretical predictions, calibration constants, or systematic magnitudes.
- Do not collapse stat and syst into a single error bar without justification.
- Do not interpret a p-value as evidence of magnitude.
- Do not apply Feldman-Cousins or CLs without naming the test statistic and the null model.
- Do not unblind before the analysis is frozen.

**Instructions:**

1. **Lock the claim grammar.** Pick *measurement* vs. *hypothesis test* vs. *limit*. Write the claim sentence in canonical form. State what value of the observable would *not* support the claim — the falsification condition.

2. **Operationalize the observable.** Define it at the detector level: event count in fiducial region; transition rate; phase; absorption coefficient; voltage trace amplitude. Make the unit explicit.

3. **Signal model.** Write the parametric form: signal rate as a function of the parameter of interest (POI) plus nuisance parameters. State theoretical input source (user-supplied citation; if absent, mark `[theory input required]`).

4. **Background / null model.** Same level of detail. Distinguish irreducible (physics) from reducible (mismodeling / impurity / cosmic). Specify how each component is constrained — from data control region, from auxiliary measurement, from simulation, from theory.

5. **Detector response.** Resolution function (Gaussian / Voigt / detector-specific); efficiency vs. observable; acceptance vs. observable; known systematic biases. Specify how the response is itself calibrated and how its uncertainty propagates.

6. **Calibration chain.** Trace raw → physical: ADC → time / voltage / charge → energy / wavelength / position / momentum. Per step: calibration source (in-situ source / external standard / known transition / cosmic), traceability (NIST / BIPM / known physics), stability monitoring, residual uncertainty.

7. **Reduction pipeline.** Selection cuts (and the order applied); vetoes; corrections (PU, alignment, livetime, dead time, atmospheric, instrumental); unfolding (matrix-inversion / Bayesian / SVD / regularized) with regularization strength chosen by closure test on a held-out injection.

8. **Statistical framework.** Likelihood form; profile-likelihood vs. Bayesian; nuisance-parameter treatment (constrained vs. free); coverage diagnostics (toy-MC coverage at the stated CL); look-elsewhere effect if scanning.

9. **Closure and null tests.** Define one or more known-answer tests and the success criterion (recovered value within stated uncertainty; bias < x% of stat uncertainty).

10. **Blinding plan (if needed).** Define the box; lock cuts pre-unblinding; pre-register on a collaboration / public repository if appropriate; log any post-unblinding change with reason.

11. **Claim audit.** Re-read the claim sentence. For each clause, identify which row in the chain supports it and which row could undermine it. If any clause is unsupported, flag it.

**Output format (locked):**

```
## Claim grammar
- Type (measurement / hypothesis / limit):
- Claim sentence:
- Falsification condition:

## Observable (operational definition)
- Detector-level quantity:
- Units:

## Signal model
- Parametric form:
- POI:
- Nuisance parameters:
- Theory input source:

## Background / null model
| Component | Type (irreducible / reducible) | Constraint source |

## Detector response
| Property | Form | Calibration source | Residual uncertainty |

## Calibration chain
| Step | Input | Output | Source / traceability | Stability monitor | Residual uncertainty |

## Reduction pipeline
1. Selection cuts (in order):
2. Vetoes:
3. Corrections:
4. Unfolding (method + regularization + closure on injection):

## Statistical framework
- Likelihood:
- Nuisance treatment:
- Test statistic:
- Coverage diagnostic:
- LEE handling:

## Closure / null tests
| Test | Known answer | Recovered | Pass criterion |

## Blinding plan (if applicable)
- Box definition:
- Cuts locked at:
- Post-unblinding change log:

## Claim audit
| Clause of claim | Supported by row(s) | Risk row |

## Open questions for the user
[gaps marked [theory input required] or [user-supplied]]
```

**Reporting-standard alignment:** CMS / ATLAS / LHCb analysis-note conventions for HEP; astrophysics-journal systematic-table conventions; GUM (Guide to the Expression of Uncertainty in Measurement) and CIPM / BIPM coverage-factor notation for precision metrology; PDG (Particle Data Group) reporting conventions for HEP measurements.

**Verification checklist:**
- [ ] Claim grammar locked; falsification condition stated.
- [ ] Observable defined operationally with units.
- [ ] Signal and background models both fully specified.
- [ ] Detector response with calibration uncertainty propagated.
- [ ] Calibration chain traceable to a standard.
- [ ] Reduction pipeline lists cuts in order, regularization choice justified by closure.
- [ ] Statistical framework names test statistic and coverage diagnostic.
- [ ] Closure / null test with pass criterion specified.
- [ ] Blinding plan present (if hypothesis-test or limit).
- [ ] Claim audit: every clause traces to a row.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Silent step | "Then we apply the standard correction" — what correction? | Every step explicit as a row |
| Efficiency / acceptance / selection conflation | "70% efficiency" really means 70% of selection × acceptance | Three separately named |
| Unfolding regularization bias | Choose regularization that gives "nice" answer | Closure on injection; held-out criterion |
| Stat + syst collapsed | Single error bar without decomposition | Stat / syst separately reported |
| p-value as effect size | "5σ evidence" → "large effect" | Claim-grammar lock |
| Calibration drift unmonitored | Constants from year 1 used for year 5 | Stability monitor required |
| Look-elsewhere effect ignored | Scan over many bins → spurious peak | LEE step required |
| Unblinding leakage | Cut moved after seeing the box | Post-unblinding log mandatory |
| Invented theory input | Plausible-looking branching ratio | `[theory input required]` |
| Combined uncertainty without correlation | Two systematics added in quadrature when correlated | Correlation accounted in propagation |
