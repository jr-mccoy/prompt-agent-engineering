---
title: "Numerical Convergence Audit (Grid / Time-Step / Mesh Refinement)"
category: science/computational
description: "Design and report a systematic refinement study that computes observed order of convergence, applies Richardson extrapolation and the Grid Convergence Index, and sets a pre-specified discretization-error criterion before production runs."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - convergence-study
  - grid-convergence-index
  - richardson-extrapolation
  - mesh-refinement
  - discretization-error
  - asymptotic-range
  - solution-verification
  - numerical-uncertainty
updated: "2026-06-26"
related_prompts:
  - domain-science/computational/science_simulation_validation_protocol.md
  - domain-science/computational/science_computational_reproducibility_environment.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
  - domain-science/disciplines/chemistry/chem_computational_chemistry_validation_protocol.md
---

# Numerical Convergence Audit (Grid / Time-Step / Mesh Refinement)

**Objective:** Produce a quantitative refinement study that estimates the discretization error in a simulation's quantity of interest (QoI). Systematically refine the relevant discretization parameter(s) — grid spacing, mesh density, time-step, or analogous resolution — over at least three levels, compute the *observed* order of convergence, apply **Richardson extrapolation** and the **Grid Convergence Index (GCI)** to estimate the error and a numerical uncertainty band, and verify the solution is in the **asymptotic range** of convergence. The deliverable replaces "it ran" and "it looked converged" with a numerical error estimate and a pre-specified acceptance criterion.

**When to use:** As the solution-verification step of a V&V effort, before any production simulation campaign whose QoI accuracy matters, or when reviewing a study that reports results from a single resolution.

**Required inputs:**
- **Discipline.** [user-supplied] (e.g., CFD, structural FEM, MD, reservoir simulation)
- **Study type.** [user-supplied — typically `computational/simulation`]
- **Discretization parameter(s).** What is being refined (grid spacing h, mesh element count, Δt, particle count, etc.).
- **Quantity of interest (QoI).** The scalar output whose discretization error is being estimated (a field requires a defined norm).
- **Refinement levels.** At least three (coarse, medium, fine) with their resolutions and the **refinement ratio** r between them. Mark `[user-supplied]` if not yet chosen.

**Optional inputs:**
- Theoretical order of accuracy of the scheme (used as a sanity check against the observed order).
- Target tolerance / acceptable discretization error for the QoI.
- Whether refinement is uniform (constant r) or non-uniform.
- Compute budget (constrains how fine the finest level can be).

**Constraints — Must:**
- Use **at least three** systematically refined levels — three is the minimum to compute an observed order and a GCI; two levels cannot establish convergence behavior.
- Compute the **observed (apparent) order of convergence** from the three QoI values and the refinement ratio, and compare it to the scheme's theoretical order.
- Apply **Richardson extrapolation** to estimate the zero-discretization-error QoI value, and report a **Grid Convergence Index (GCI)** (Roache) as the numerical uncertainty band, with a safety factor stated.
- Perform an **asymptotic-range check**: verify the convergence ratio is consistent with monotonic convergence in the asymptotic regime (e.g., the ratio of successive GCIs ≈ 1). State explicitly if the solution is *not* in the asymptotic range.
- Set the **convergence/acceptance criterion before production runs** (pre-specified), and keep it distinct from any after-the-fact observation.
- Report the refinement as a table: level → resolution → QoI → ratio → GCI.

**Constraints — Must Not:**
- Do not invent citations, DOIs, tool version numbers, benchmark values, or convergence thresholds. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not claim convergence from a single resolution or a single refinement step.
- Do not report Richardson-extrapolated values or GCI when the solution is outside the asymptotic range without flagging that the estimate is unreliable there.
- Do not silently treat oscillatory or non-monotonic convergence as monotonic — diagnose and report it.
- Do not use promotional language ("novel", "groundbreaking", "first-ever", "gold standard") in the drafted report.

**Instructions:**

1. **Fix the QoI and the refinement design.** State the QoI (and norm, if a field), the discretization parameter, the three-or-more resolutions, and the refinement ratio r. Confirm refinement is systematic (geometrically self-similar where possible).
2. **Pre-specify the criterion.** Before running production, state the acceptable discretization error (e.g., "GCI on the fine grid ≤ 2% of QoI"). Record it as pre-specified.
3. **Run the levels and record QoIs.** Tabulate the QoI at each level. Keep all other parameters fixed so only resolution varies.
4. **Compute observed order of convergence.** From the three QoI values and r, compute the apparent order p. Compare to the theoretical order; a large mismatch signals under-resolution, a bug, or being outside the asymptotic range.
5. **Richardson-extrapolate.** Estimate the continuum (zero-error) QoI value using the observed order and the finest grids.
6. **Compute GCI.** Report GCI between the medium/fine pair (and coarse/medium) using Roache's formulation with an explicit safety factor; interpret GCI as the numerical uncertainty band on the QoI.
7. **Asymptotic-range check.** Verify that GCI_coarse/medium ≈ r^p · GCI_medium/fine (ratio near 1). Report monotonic vs. oscillatory vs. divergent behavior. If not asymptotic, recommend further refinement before trusting the estimates.
8. **Self-check and report.** Confirm units, that finer grids reduce error, and that the extrapolated value is bracketed sensibly. Deliver the table plus the verdict against the pre-specified criterion.

**Output format (locked):**

```
## Convergence Audit Scope
- Discipline / study type:
- Discretization parameter & QoI (norm if field):
- Refinement ratio r:
- Pre-specified acceptance criterion:
- Theoretical order of scheme [user-supplied if unknown]:

## Refinement Table
| Level | Resolution (h / N / Δt) | QoI | Ratio to next | GCI (%) |
|-------|-------------------------|-----|---------------|---------|
| Coarse |  |  |  |  |
| Medium |  |  |  |  |
| Fine   |  |  | — |  |

## Convergence Estimates
- Observed order of convergence p:
- Theoretical order (comparison):
- Richardson-extrapolated QoI value:
- GCI (fine) with safety factor:
- Numerical uncertainty band on QoI:

## Asymptotic-Range Check
- GCI ratio (≈1 expected):
- Convergence behavior (monotonic / oscillatory / divergent):
- In asymptotic range? (yes/no — if no, estimates are unreliable):

## Verdict
- Meets pre-specified criterion? (pass/fail):
- Recommendation (production-ready resolution / refine further):
```

**Reporting-standard alignment:** Roache Grid Convergence Index and Richardson extrapolation; consistent with ASME V&V 20 / AIAA G-077 solution-verification practice for estimating discretization (numerical) uncertainty.

**Verification checklist (before delivering):**
- [ ] At least three systematically refined levels are used.
- [ ] Observed order of convergence is computed and compared to the theoretical order.
- [ ] Richardson extrapolation gives a continuum estimate.
- [ ] GCI is reported with an explicit safety factor and interpreted as a numerical uncertainty band.
- [ ] Asymptotic-range check is performed and its result stated (not assumed).
- [ ] Convergence behavior (monotonic/oscillatory/divergent) is diagnosed.
- [ ] The acceptance criterion was pre-specified, not chosen after seeing results.
- [ ] No fabricated thresholds, benchmark values, or version numbers; unknowns marked `[user-supplied]`.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Single-resolution claim | "It ran and the answer looks reasonable" | Require ≥3 levels and a computed error estimate |
| Two-level illusion | Two grids agree, assumed converged | Three levels minimum to get observed order + GCI |
| Outside asymptotic range | Richardson value reported but order is nonsensical | Asymptotic-range check gate before trusting extrapolation |
| Oscillatory convergence | Non-monotonic QoI averaged into "agreement" | Diagnose monotonic vs. oscillatory; report explicitly |
| Theoretical-order assumption | GCI computed using assumed order, not observed | Compute observed order; use it (and compare) |
| Post-hoc criterion | Threshold chosen to make the fine grid pass | Pre-specify the criterion before production runs |
