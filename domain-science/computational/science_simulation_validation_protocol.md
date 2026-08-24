---
title: "Simulation Validation Protocol (MD / FEM / CFD / ABM)"
category: science/computational
description: "Build a verification-and-validation (V&V) plan for a numerical simulation that separates code verification, solution verification, and validation-against-reality with quantified discrepancy metrics."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - simulation
  - verification-validation
  - code-verification
  - solution-verification
  - uncertainty-quantification
  - sensitivity-analysis
  - method-of-manufactured-solutions
  - validation-metric
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_numerical_convergence_audit.md
  - domain-science/computational/science_computational_reproducibility_environment.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
  - domain-science/disciplines/chemistry/chem_computational_chemistry_validation_protocol.md
---

# Simulation Validation Protocol (MD / FEM / CFD / ABM)

**Objective:** Produce a structured V&V plan for a computational simulation (molecular dynamics, finite-element, computational fluid dynamics, agent-based, or similar) that cleanly separates the three distinct questions — *are the equations solved correctly?* (code verification), *how large is the discretization/iterative/round-off error in this run?* (solution verification), and *does the model match physical reality?* (validation). The plan must quantify discrepancies with explicit validation metrics rather than asserting plausibility. The point is to make "the simulation is trustworthy" a falsifiable, evidence-backed claim, not an impression.

**When to use:** Before a simulation campaign is used to support a scientific or engineering conclusion, before publishing simulation results, or when reviewing a simulation study whose credibility is in question.

**Required inputs:**
- **Discipline.** [user-supplied] (e.g., structural mechanics, fluid dynamics, materials/MD, epidemiology/ABM)
- **Study type.** [user-supplied — typically `computational/simulation`; note if it also feeds a downstream experimental or observational claim]
- **Solver / framework.** Name and (if relevant) configuration of the simulation code. Mark version as `[user-supplied]` if not given — do not assume.
- **Quantities of interest (QoIs).** The specific scalar/field outputs whose accuracy must be established (e.g., drag coefficient, peak stress, diffusion coefficient, infection-peak timing).
- **Reality reference.** What ground truth exists: analytic solution, manufactured solution, benchmark case, prior experiment, or field data. Mark `[user-supplied]` if none yet exists.

**Optional inputs:**
- Governing equations / model assumptions and their stated domain of validity.
- Known calibration parameters and the data used to tune them.
- Available compute budget (caps how many V&V runs are feasible).
- Required confidence / tolerance for the QoI (e.g., "drag within 5%").
- Stakes and intended use (regulatory submission vs. exploratory study).

**Constraints — Must:**
- Structure the plan on the V&V hierarchy: (1) **code verification**, (2) **solution verification**, (3) **validation**. Keep them separate — never let one substitute for another.
- Align terminology and structure with **ASME V&V 10/20** and **AIAA G-077** conventions for verification and validation of computational simulations; name the standard where a step maps to it.
- For code verification, prefer **order-of-accuracy** tests via the **method of manufactured solutions (MMS)** or comparison to an exact analytic solution; report observed vs. theoretical order of convergence.
- For solution verification, require quantified discretization error (delegate the refinement study to the numerical convergence audit) plus iterative-convergence and round-off considerations.
- For validation, define an explicit **validation metric** (a quantified discrepancy between simulation and reference with its uncertainty), not a qualitative "good agreement."
- Distinguish **calibration data** from **validation data** — validation must use data not used to tune the model.
- Include **uncertainty quantification (UQ)** of inputs and a **sensitivity analysis** (e.g., Morris screening then Sobol indices) so that QoI uncertainty is attributed to its sources.
- Preserve the **pre-specified vs. exploratory** distinction: state which acceptance thresholds and reference cases were fixed before runs vs. chosen after seeing results.

**Constraints — Must Not:**
- Do not invent citations, DOIs, tool version numbers, benchmark values, or convergence thresholds. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not treat a result that "looks physical" or "looks smooth" as validated — visual plausibility is not a validation metric.
- Do not validate a model on the same data used to calibrate it.
- Do not report agreement without an associated uncertainty band on both the simulation and the reference.
- Do not use promotional language ("novel", "groundbreaking", "first-ever", "gold standard") in the drafted plan; describe what is established and at what confidence.

**Instructions:**

1. **Frame the claim and QoIs.** Restate the scientific/engineering claim the simulation is meant to support, list the QoIs, and record the required tolerance for each. A V&V plan is scoped to specific QoIs, not "the model" in the abstract.
2. **Code verification — solve the equations right.** Specify order-of-accuracy tests: design a manufactured solution (or use an exact analytic case), run at multiple resolutions, and compare the *observed* order of convergence against the solver's *theoretical* order. A mismatch signals a code/implementation bug, independent of physics.
3. **Solution verification — bound the numerical error of this run.** Hand the discretization-error estimate to a formal refinement study (grid/mesh/time-step) and report the discretization, iterative-convergence, and round-off contributions. Carry forward a numerical uncertainty band on each QoI.
4. **Separate calibration from validation.** Document which parameters were tuned, on what data, and confirm the validation reference is independent. Flag any leakage where validation data influenced the model.
5. **Define validation metrics.** For each QoI, specify the discrepancy measure between simulation and reference, with combined uncertainty from numerical error, input uncertainty, and reference/experimental uncertainty. State the acceptance criterion (pre-specified where possible).
6. **Quantify input uncertainty (UQ).** Identify uncertain inputs (material properties, boundary/initial conditions, rate constants, behavioral rules) and propagate them to QoI uncertainty using an appropriate method; note whether aleatory and epistemic uncertainty are kept separate.
7. **Run sensitivity analysis.** Use a screening method (e.g., Morris) to rank inputs cheaply, then variance-based indices (e.g., Sobol) on the dominant inputs, to attribute QoI variance and reveal which inputs most need better characterization.
8. **Assess and report adequacy.** Compare validation-metric results to acceptance criteria, state the model's demonstrated **domain of applicability** (the conditions under which it is validated), and flag extrapolation beyond it as unvalidated.
9. **Adversarial self-check.** Ask: what would make this conclusion wrong? Confounded calibration, an under-resolved mesh masquerading as agreement, a sensitivity-dominant input left uncharacterized, or a reference dataset with its own unstated error.

**Output format (locked):**

```
## V&V Scope
- Discipline / study type:
- Solver (+ version [user-supplied if unknown]):
- QoIs and required tolerances:
- Claim the simulation must support:

## 1. Code Verification (solving the equations right)
| QoI / test case | Method (MMS / analytic) | Theoretical order | Observed order | Verdict |
|---|---|---|---|---|

## 2. Solution Verification (numerical error of the run)
- Discretization error estimate (→ convergence audit):
- Iterative-convergence criterion:
- Round-off / precision notes:
- Numerical uncertainty band per QoI:

## 3. Validation (matching reality)
- Calibration data vs. validation data (independence confirmed?):
| QoI | Sim value ± U_num ± U_input | Reference value ± U_ref | Validation metric | Acceptance criterion (pre-specified?) | Pass/Fail |
|---|---|---|---|---|---|

## Uncertainty Quantification & Sensitivity
- Uncertain inputs and propagation method:
- Screening (Morris) ranking:
- Variance-based (Sobol) indices for dominant inputs:

## Domain of Applicability & Limitations
- Validated regime:
- Known extrapolation risks:
- Pre-specified vs. exploratory choices:
```

**Reporting-standard alignment:** ASME V&V 10 (computational solid mechanics) / V&V 20 (CFD & heat transfer), AIAA G-077 (CFD verification & validation). UQ/sensitivity framing follows standard variance-based (Sobol) and screening (Morris) methods.

**Verification checklist (before delivering):**
- [ ] Code, solution, and validation are kept as three distinct activities — none substitutes for another.
- [ ] Code verification reports observed vs. theoretical order of accuracy (MMS or analytic).
- [ ] Solution verification carries a numerical uncertainty band into validation, not just "it converged."
- [ ] Calibration and validation data are confirmed independent.
- [ ] Each validation comparison uses a quantified metric with uncertainty on both sides.
- [ ] UQ propagates input uncertainty; sensitivity analysis attributes QoI variance.
- [ ] Validated domain of applicability is stated; extrapolation is flagged.
- [ ] No fabricated benchmark values, thresholds, or version numbers; unknowns marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Plausibility bias | Smooth, physical-looking field assumed correct | Require a quantified validation metric vs. an independent reference |
| Calibration leakage | "Excellent agreement" because the model was tuned on that data | Confirm validation data independence before reporting agreement |
| Under-resolution masking error | Coarse mesh happens to match experiment by cancellation | Require solution verification (refinement study) before validation |
| Order-of-accuracy unverified | Code runs and is "stable" but solves the wrong equations | MMS/analytic order test as a precondition to validation |
| Unattributed uncertainty | Single number reported with no band | UQ + sensitivity; report QoI ± combined uncertainty |
| Silent extrapolation | Validated at low Re / small system, applied far outside | State and enforce the validated domain of applicability |
