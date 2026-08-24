---
title: "Materials Design-of-Experiments Plan"
category: science/disciplines/materials-engineering
description: "Design a materials / process DOE (factorial, fractional factorial, RSM, Taguchi, definitive-screening, space-filling) with factor selection, alias structure, randomization, and analysis"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - doe
  - design-of-experiments
  - factorial
  - rsm
  - taguchi
  - definitive-screening
  - alias-structure
  - process-development
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/materials-engineering/materials_synthesis_and_characterization_plan.md
  - domain-science/methods-foundations/science_experimental_design_advisor.md
---

# Materials Design-of-Experiments Plan

**Objective:** Design a materials- or process-development DOE that efficiently identifies the dominant factors, their interactions, and their optima for a defined response — using an appropriate design family (full factorial, fractional factorial, Plackett-Burman, definitive-screening, response-surface, Taguchi, mixture, space-filling for computer experiments) with explicit alias structure, randomization, replication, blocking, and a pre-specified analysis plan.

**When to use:** When the user is exploring a process / formulation space and needs to plan experiments at the run-budget level (rather than the lab-protocol level); when transitioning from "tweak one knob at a time" to a structured exploration; when responding to a process-development manager who wants statistically defensible recommendations.

**Required inputs:**
- **Response variable(s).** Property the experiment aims to optimize / characterize, with units and the direction (maximize / minimize / target).
- **Candidate factors.** Process and material variables that may affect the response, with ranges (low / high).
- **Number of runs feasible.** Hard budget cap.
- **Run cost and run duration.** Affects practical replication.
- **Whether factors are continuous, categorical, mixture (sum-to-constant), or hard-to-change.**
- **Prior knowledge.** Suspected main effects, suspected interactions, suspected nonlinearity, prior data (user-supplied).

**Optional inputs:**
- Robustness target (minimize sensitivity to a noise factor).
- Multi-response optimization need.
- Constraint regions in factor space (combinations that are infeasible / unsafe).
- Sequential strategy intent (screening → augment).

**Constraints — Must:**
- Pick the design family based on (i) goal (screening vs. characterization vs. optimization vs. robustness vs. mixture); (ii) run budget; (iii) factor count; (iv) suspected interactions / curvature; (v) prior knowledge.
- For fractional factorial designs, write out the alias / confounding structure explicitly. State which main effects and two-factor interactions are aliased.
- Distinguish randomization from blocking. Randomize run order unless restrictions (hard-to-change factors) demand a split-plot structure. If split-plot, build the design and the analysis as split-plot.
- Include center points for curvature detection (continuous factors) and replicates for pure-error estimation. Typical: 3–5 center points; ≥2 replicates of select corners.
- Pre-specify the analysis model and the model-reduction strategy (significance, AICc, Lenth's method for unreplicated). State whether transformation (Box-Cox) is allowed and the rule.
- For categorical factors: handle level coding and contrast scheme; for mixture: select Scheffé canonical model and constrain the design within the simplex.
- Acknowledge curse of dimensionality: do not propose full factorial for >5 factors without justification.
- Pre-specify what "success" looks like: predicted optimum, prediction uncertainty bound, confirmation-run plan.

**Constraints — Must Not:**
- Do not propose a Taguchi L-array without naming the alias structure and acknowledging two-factor-interaction confounding.
- Do not run a DOE without randomization unless split-plot structure is explicitly chosen and analyzed.
- Do not omit center points where curvature is plausible.
- Do not analyze a DOE with stepwise selection without acknowledging the inflation of effect estimates.
- Do not extend conclusions outside the studied factor range.
- Do not invent variance estimates or prior effect sizes.

**Instructions:**

1. **Goal classification.** Pick one: screening (which factors matter); characterization (model the surface near a point); optimization (find optimum); robust design (minimize sensitivity); mixture (formulation under sum constraint); computer-experiment / surrogate (space-filling).

2. **Factor table.** For each candidate factor: type (continuous / categorical / mixture / noise), range or levels, hard-to-change?, expected linearity, expected interactions, prior data. Mark `[user-supplied]` where missing.

3. **Run-budget vs. design-family matching.**
    - Screening with many factors, small budget → Plackett-Burman, fractional factorial Res III, definitive-screening (DSD).
    - Characterization with ≤4 continuous factors → full factorial 2^k + center points → augment to face-centered or central composite design (CCD) / Box-Behnken (BBD).
    - Optimization → response-surface (CCD / BBD / DSD-augmented).
    - Robust design → inner array (control factors) × outer array (noise factors) per Taguchi.
    - Mixture → Scheffé simplex-lattice or simplex-centroid; with constraints, D-optimal.
    - Computer experiments → Latin hypercube / maximin / Sobol; possibly nested for multi-fidelity.

4. **Resolution and alias structure.** For fractional factorial, state design generator and resolution (III, IV, V). Output the alias table: which main effect / two-factor interaction is confounded with which. Make explicit choices.

5. **Center points and replicates.** Continuous designs: include 3–5 center points to detect curvature and estimate pure error. Replicate selected corners to anchor variance. State count.

6. **Randomization, blocking, split-plot.** Default fully randomized order. If hard-to-change factors exist (oven temperature changed slowly; gas composition; vendor lot), build split-plot and define whole-plot / sub-plot factors. State the analysis as split-plot REML.

7. **Pre-specified analysis.** Linear model with main + selected two-factor interactions + (where relevant) quadratic terms. Effect estimation method (Lenth for unreplicated designs; REML for split-plot; OLS otherwise). Model-reduction rule (significance + AICc, pre-specified, not stepwise after the fact). Transformation allowance.

8. **Confirmation runs.** Plan 3–5 confirmation runs at the predicted optimum (or characterization points). Define success: predicted response within stated CI.

9. **Sequential augmentation.** Plan the next-step augmentation if results suggest curvature, additional factors, or shifted optimum. Avoid running the entire experiment up front.

10. **Reporting.** Output design matrix (run order, factor levels), alias table, planned analysis, confirmation plan. Specify how raw data and analysis code will be archived.

**Output format (locked):**

```
## Goal
- Type (screening / characterization / optimization / robust / mixture / computer):

## Factor table
| Factor | Type | Range / levels | Hard-to-change? | Expected linearity | Expected interactions | Prior data |

## Design family selected
- Family:
- Run count:
- Resolution (if fractional):

## Alias / confounding structure
| Alias chain | Implication |

## Center points and replicates
- Center points:
- Replicated runs:
- Pure-error df:

## Randomization / blocking / split-plot
- Order:
- Blocks:
- Split-plot whole / sub:

## Pre-specified analysis
- Model:
- Effect estimation method:
- Model-reduction rule:
- Transformation rule:

## Confirmation plan
- Confirmation runs:
- Success criterion:

## Sequential augmentation
- Trigger condition:
- Next-step design:

## Design matrix (run order)
| Run | Factor levels | Block |

## Reproducibility
- Software (JMP / Design-Expert / Minitab / R `DoE` / Python `pyDOE` / `pyDOE2`):
- Code / design file committed:
- Data deposit:

## Reporting standard alignment
[ISO / industrial DOE conventions; relevant journal expectations]

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** General DOE conventions (Montgomery; Box-Hunter-Hunter); ISO 16336 for Taguchi-style robust design where used; ASTM E1325 terminology where applicable; journal-specific data-availability statements; FAIR for design files and raw measurement data.

**Verification checklist:**
- [ ] Goal explicit; design family follows from goal + budget + factor count.
- [ ] Factor table covers type / range / hard-to-change.
- [ ] Alias structure written out for fractional designs.
- [ ] Center points and replicates included for continuous designs.
- [ ] Randomization or split-plot structure chosen and matched in analysis plan.
- [ ] Analysis model pre-specified; model-reduction rule explicit.
- [ ] Confirmation run plan present.
- [ ] No invented prior effect sizes or variance estimates.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Aliased interaction misread as main effect | Significant "factor A" is actually A + BC | Alias structure written out |
| OFAT thinking inside DOE | Interactions ignored | Interaction terms in model |
| No center points → undetected curvature | Linear model fits an apparent line through a quadratic | Center points included |
| Unrandomized order with hard-to-change factor | Treated as randomized; SE underestimated | Split-plot explicit |
| Stepwise selection inflation | "Significant" main effect found via stepwise | Pre-specified reduction rule |
| Extrapolation outside range | Optimum predicted beyond explored space | Explicit range constraint |
| Taguchi without confounding awareness | L8 or L16 confounding 2FIs with main effects | Acknowledge + augment if needed |
| Mixture analyzed as factorial | Sum-to-1 constraint violated | Scheffé model |
| No confirmation run | Optimum claimed without verification | Confirmation runs required |
| Invented variance / effect | Plausible-looking RMS error | `[user-supplied]` |
