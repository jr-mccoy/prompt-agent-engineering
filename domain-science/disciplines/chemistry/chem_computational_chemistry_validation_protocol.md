---
title: "Computational Chemistry Validation Protocol"
category: science/disciplines/chemistry
description: "Validate a computational chemistry workflow: method / basis selection, benchmarking against experiment or higher theory, basis-set and method-sensitivity, error budget"
techniques:
  - ST-01
  - ST-03
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - dft
  - computational-chemistry
  - benchmarking
  - method-validation
  - basis-set
  - error-budget
  - solvation
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/chemistry/chem_reaction_kinetics_experimental_designer.md
  - domain-science/methods-foundations/science_experimental_design_advisor.md
---

# Computational Chemistry Validation Protocol

**Objective:** Validate a planned computational chemistry workflow (DFT, post-HF, MP2 / CCSD(T), QM/MM, semi-empirical, ML-potential, force-field MD) for the user's specific question, by pinning method / basis / corrections to a benchmark, surfacing sensitivities, and producing an itemized error budget that the eventual paper can be defended against.

**When to use:** Before production runs, when a computational study is being scoped or revised, or when a manuscript reviewer has asked for evidence that the method choice supports the claim. Use also when adopting a new method in the group.

**Required inputs:**
- **Property to compute.** Geometry, vibrational frequency, energetics (relative / absolute / activation), thermochemistry, redox potential, pKa, NMR shielding / coupling, excitation energy, charge transfer, magnetic property, binding free energy, reaction barrier.
- **System class.** Main-group small molecule; transition-metal complex (open-shell? heavy-atom?); organic with significant dispersion; weakly bound non-covalent complex; charged species; periodic / solid; biomolecular complex with explicit / implicit solvent.
- **Target accuracy** linked to the experimental claim (e.g., "ΔG‡ to ±1 kcal/mol to discriminate competing TSs"; "TD-DFT excitation within 0.3 eV of experiment"; "geometry r.m.s.d. < 0.02 Å vs. crystal").
- **Computational budget** (cores, wall time, memory) and what is already in-house (Gaussian / ORCA / Q-Chem / Psi4 / Turbomole / CFOUR / NWChem / OpenMM / AMBER / GROMACS / GPAW / VASP / Quantum ESPRESSO).

**Optional inputs:**
- Existing experimental anchors (user-supplied).
- Prior computational work on the same family.
- Reviewer concerns to address.

**Constraints — Must:**
- Pin method and basis to the property and system class. Use literature-validated combinations explicitly (named) and state the validation regime they were tested on. Do not extrapolate beyond.
- Test method / basis / dispersion / solvation / relativistic-correction sensitivity *before* production runs. The sensitivity panel is part of the protocol, not an afterthought.
- Distinguish *single-reference* from *multi-reference* problems. For open-shell TMs, transition states, biradicals, near-degeneracies, require a single-reference diagnostic (T1 / D1 / M / FOD) and switch families if it fails.
- Itemize the error budget: method error + basis-set incompleteness + dispersion + solvation + thermochemistry approximation + harmonic / anharmonic + relativistic / SO + numerical (grid, SCF threshold). Each item has a numerical magnitude or `[benchmark required]`.
- For TDDFT, distinguish charge-transfer / Rydberg / valence excitations and gate functional choice on diagnostic (e.g., Λ index, M diagnostic).
- For thermochemistry, specify the partition-function approximation (rigid-rotor harmonic-oscillator vs. quasi-RRHO, low-frequency mode treatment, standard state, temperature, concentration corrections).

**Constraints — Must Not:**
- Do not propose B3LYP for problems known to fail it (non-covalent, charge transfer, open-shell TM low-spin / high-spin) without explicit dispersion correction or a switch to a validated functional.
- Do not benchmark on the same data the method will be applied to. Benchmark on a held-out analogous set.
- Do not report relative energies without specifying the reference (single-point at optimized geometry vs. fully optimized vs. ZPE/thermal corrections at consistent level).
- Do not invent reference values, benchmark dataset names, or method-validation papers.
- Do not propose ML-potential production runs without out-of-distribution diagnostics on the actual chemical space.
- Do not silently use default convergence / integration grids for systems known to need tighter settings.

**Instructions:**

1. **Restate property + accuracy target.** Property name; experimental anchor (if any); accuracy needed for the scientific claim; system class. If the claim does not constrain the accuracy target, ask.

2. **Single- vs. multi-reference diagnostic plan.** Specify the diagnostic computation (T1 from CCSD; D1; M from CASSCF; FOD from finite-temperature DFT). Specify the threshold above which the system is multireference (T1 > 0.02 for closed-shell; > 0.045 for TM as a common rule, with caveats). State what method family the protocol switches to if the diagnostic fails (CASSCF / NEVPT2 / DMRG / DLPNO-CCSD(T) / multireference perturbation).

3. **Method / basis sensitivity panel (pre-production).** Plan a small grid of single-point calculations on 3–5 representative systems (different sizes / charge states / spin states / structural motifs that span the target chemistry):
    - Two density-functional families (e.g., a hybrid GGA with dispersion + a range-separated hybrid) plus a wavefunction reference (DLPNO-CCSD(T) where feasible, MP2 / SCS-MP2 otherwise).
    - Two basis sets: production basis vs. one step larger (e.g., def2-TZVP vs. def2-QZVPP), and the CBS-limit estimate.
    - Dispersion: with and without (D3(BJ) / D4 / VV10 / nonlocal).
    - Solvation: gas-phase vs. implicit (CPCM / SMD / COSMO-RS) vs. explicit-shell if relevant.
    - Relativistic: scalar (DKH / X2C / ZORA) for heavy atoms; SO for actinides / lanthanides / heavy-element spectra.
    - Numerical: tight SCF and tight integration grid as the default.
4. **Benchmark against experiment or higher theory.** Identify 3–5 anchor data points from experiment (user-supplied) or from a higher-theory dataset (e.g., GMTKN family for main-group; MOR41 for TM bond energies; S66x8 for non-covalent; MOBH35 for TM barriers — named by user, not invented). Report MAE / RMSE / max-error on the anchor set per method-basis-correction combination.

5. **Pick production setup.** From the sensitivity panel + benchmark, pick the cheapest setup that meets the accuracy target. State the rationale and the cost ratio vs. the most-accurate panel entry.

6. **Itemized error budget.** Build a table summing the contributions: method-vs-experiment MAE, basis incompleteness (production vs. CBS), dispersion (D-correction value), solvation (implicit-vs-explicit shift), thermochemistry (RRHO vs. quasi-RRHO; standard-state correction), harmonic-vs-anharmonic, relativistic / SO (where applicable), numerical convergence (SCF / grid / k-point). Sum into a worst-case and a likely error band.

7. **Geometry and stationary-point validation.** Frequency analysis at the level of optimization (number of imaginary frequencies as expected); IRC to verify TS connectivity; conformer search (CREST / metadynamics / systematic) to avoid local-minimum bias.

8. **Reproducibility artifacts.** Specify input-file / log / coordinate / output-archive policy; pin software version, compiler, libraries (BLAS / LAPACK); commit input templates; deposit final coordinates and key outputs to Zenodo / Materials Cloud / ioChem-BD; report all relevant settings in the SI per ACS / RSC conventions.

9. **Pitfalls and detection.** Multireference miss; spin-contamination > 0.1 above pure value for restricted-open systems; broken-symmetry energies misused; SCF convergence onto excited state; implicit-solvation failure for charged TS / strongly H-bonded; basis-set superposition error not corrected for non-covalent.

10. **ML-potential / force-field caveats (if used).** Out-of-distribution diagnostics: per-frame uncertainty from ensemble; force / energy MAE on a held-out QM set drawn from production trajectories; rerun on QM where uncertainty exceeds threshold.

**Output format (locked):**

```
## Property and accuracy target
- Property:
- System class:
- Accuracy required:
- Experimental anchor available?

## Reference / multireference diagnostic
- Diagnostic + threshold:
- Switch plan if multireference:

## Sensitivity panel (pre-production)
| Axis | Levels | Representative systems | Cost | Notes |
| Functional family | | | | |
| Basis set | | | | |
| Dispersion | | | | |
| Solvation | | | | |
| Relativistic | | | | |
| Numerical (grid / SCF) | | | | |

## Benchmark
| Anchor | Reference value source | Method-basis | Result | Error |

## Production setup (locked)
- Method:
- Basis:
- Dispersion:
- Solvation:
- Relativistic:
- Grid / SCF thresholds:

## Error budget
| Source | Estimated magnitude | Direction |
| Sum | likely band: ±x; worst case: ±y |

## Geometry and stationary points
- Opt level + frequency confirmation:
- IRC plan:
- Conformer search:

## Reproducibility artifacts
- Software / version / libraries:
- Input templates committed:
- Coordinate / output archive:
- SI reporting block:

## Pitfall register
| Pitfall | Detection | Mitigation |

## ML-potential / force-field validation (if applicable)
- Out-of-distribution diagnostic:
- QM re-spotting strategy:

## Open questions for the user
[gaps marked [benchmark required] or [user-supplied]]
```

**Reporting-standard alignment:** Community computational-chemistry benchmark sets (GMTKN, S22 / S66, MOBH35, MOR41 — named by user, not invented); ACS / RSC SI conventions for computational details (method, basis, dispersion, solvation, software version, coordinates); FAIR4Chem and ioChem-BD for data deposit.

**Verification checklist:**
- [ ] Accuracy target is tied to the experimental claim.
- [ ] Multireference diagnostic specified.
- [ ] Sensitivity panel covers all six axes (functional / basis / dispersion / solvation / relativistic / numerical).
- [ ] Benchmark anchor is named (user-supplied) and not invented.
- [ ] Error budget itemized with magnitudes.
- [ ] Production setup is chosen from the panel + benchmark, not a priori.
- [ ] IRC / frequency / conformer-search plan specified.
- [ ] Reproducibility artifacts named (software version, input templates, deposit).

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Multireference miss | DFT energy on a strongly correlated TS | Diagnostic step required |
| Basis-set false convergence | Result agrees with experiment at small basis only | Basis ladder + CBS estimate |
| Dispersion drift | Functional without D-correction on stacking / binding | D-correction axis enforced |
| Solvation mismatch | Implicit solvent on charge-localized TS | Implicit / explicit comparison if charged |
| Wrong stationary point | Saddle with 2 imaginary frequencies labeled TS | Frequency analysis required |
| Conformer-blindness | Lowest local min reported as "the" structure | Conformer-search plan |
| Benchmark-on-the-test | Method fit on same data it will be applied to | Held-out anchor set |
| ML-potential extrapolation | Force-field-style MD on chemistry outside training | OOD diagnostic + QM re-spot |
| Invented reference value | Plausible-looking experimental ΔH | `[user-supplied]` if not anchored |
| Default-grid blindness | Tight TS energy on default grid | Tight grid + SCF as default |
