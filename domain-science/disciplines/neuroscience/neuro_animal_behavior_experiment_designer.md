---
title: "Animal Behavior Experiment Designer"
category: science/disciplines/neuroscience
description: "Design a rodent / non-human-primate behavioral experiment with habituation, counterbalancing, blinding, ethologically valid endpoints, and ARRIVE 2.0-aligned reporting"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - QA-02
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - behavior
  - rodent
  - non-human-primate
  - habituation
  - counterbalancing
  - blinding
  - arrive
  - ethology
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/neuroscience/neuro_electrophysiology_protocol_designer.md
  - domain-science/disciplines/neuroscience/neuro_circuit_perturbation_experiment_designer.md
  - domain-science/disciplines/biology/bio_clinical_trial_protocol_outliner.md
---

# Animal Behavior Experiment Designer

**Objective:** Design an animal behavioral experiment (rodent, non-human primate, or other model) with counterbalanced groups, well-defined habituation and handling, blinding of operator and analyst, ethologically valid endpoints, ARRIVE 2.0-aligned reporting, and a pre-specified analysis plan that resists the standard behavioral-neuroscience reviewer critiques.

**When to use:** Before any IACUC submission or pilot cohort, when the user has a behavioral question (cognitive, affective, motor, social, sensory, perceptual, addictive, learning) and needs the design defensible against the field's known reproducibility traps (cage / batch effects, handling stress, sex bias, single-task confounds, p-hacked endpoints).

**Required inputs:**
- **Question.** Phrased as a testable claim with the behavior named.
- **Species, strain / line, sex(es), age, source.** Vendor or colony.
- **Manipulation.** Pharmacological (drug, dose, vehicle, route, timing), genetic (line, induction, control), surgical (lesion, viral, implant), environmental (housing, diet, stress).
- **Behavioral paradigm.** Open field, EPM, NOR, fear conditioning, Morris water maze, T-maze, Barnes, operant 2AFC, lever-press / nose-poke, gnotobiotic / social, prepulse-inhibition, light-dark, sucrose preference, etc. (User names.)
- **Equipment.** Apparatus, video tracking system, ABET / MED-PC, automated scoring software.
- **Throughput.** Cohort size feasible, season constraints, animal-room schedule.

**Optional inputs:**
- Prior effect sizes from same lab or literature (user-supplied).
- Anticipated sex-by-treatment interaction.
- Repeat-testing plan (longitudinal vs. cross-sectional cohorts).
- Microbiome / circadian / pre-clinical phase considerations.

**Constraints — Must:**
- Include both sexes unless biology requires single sex; if single sex, justify and limit the inference. Stratify analysis by sex; do not pool unless interaction is tested and not significant.
- Pre-specify primary behavioral endpoint (single dependent variable, single time-window) before pilot data. Secondaries labeled and non-promotable.
- Plan habituation (to room, handler, apparatus) and handling schedule. State pre-experiment timeline.
- Counterbalance every nuisance factor: cage, litter / dam, time-of-day, apparatus side (left / right chamber), experimenter, order of testing across days, drug-administration order.
- Blind operator (administration and behavioral scoring) and analyst (post-hoc scoring of video; statistical analysis). If automated scoring, validate against blinded manual scoring on a subset.
- Pre-specify exclusion criteria (failure to learn, sickness, surgical complication, dropout, equipment failure). No post-hoc exclusion.
- Specify the unit of analysis: animal (not trial or session) for between-subject claims; trial / session for within-animal repeated-measures.
- Align reporting to ARRIVE 2.0; reference the 3Rs (replacement, reduction, refinement) in justification.

**Constraints — Must Not:**
- Do not propose a single test as proxy for a complex phenotype ("anxiety-like" claim from open field alone).
- Do not pool sexes by default without an interaction test.
- Do not invent drug doses, viral titers, line names, vendor catalog numbers, or behavioral software versions.
- Do not allow the same person to run, score, and analyze the experiment unblinded.
- Do not propose a sample size without an explicit assumption set or marker for `[user-supplied effect-size anchor]`.
- Do not treat trial as the unit of analysis when the question is between-animal.

**Instructions:**

1. **Lock the question and the primary endpoint.** Translate the behavioral claim into a single primary variable with a time-window. Build a small justification: why this variable, why this time-window, what would falsify the claim.

2. **Battery vs. single-task decision.** If the claim is about a construct (anxiety, motivation, learning) rather than a behavior, plan a battery of orthogonal tasks (typically 2–3) with the primary endpoint defined within the battery (e.g., open-field center time *and* light-dark crossings as a convergent measure). Pre-specify the convergence rule. If the claim is about a specific behavior, single-task is acceptable.

3. **Animal cohort design.** Group sizes per cell of the design matrix (e.g., sex × treatment × time). State biological replication unit; state how cage / litter / dam are balanced across treatment (avoid same-cage same-treatment). Specify cohort vs. cohort-replication plan if data come over multiple cohorts.

4. **Pre-registration draft.** Sample-size justification (effect-size anchor `[user-supplied]`; alpha; power; allocation ratio; expected attrition); analysis plan (model + contrasts + post-hoc family-wise control); exclusion criteria; sex stratification rule; convergence rule for batteries.

5. **Handling and habituation.** Timeline before testing: facility acclimation (typically 1–2 weeks); handler habituation (gentle daily handling for 5–7 days); apparatus habituation (per task; e.g., 1–3 short exposures to context before fear conditioning). State scientist time, room conditions (lighting, temperature, humidity), and time-of-day window.

6. **Counterbalancing matrix.** Build the full Latin square or block design showing how cage / sex / treatment / time-of-day / experimenter / apparatus chamber / testing-day-order are crossed. Surface any axis that cannot be crossed and the residual confound.

7. **Blinding.** Specify the blinded role assignments: who codes samples, who runs the experiment, who scores video (manual / automated + manual-validated), who runs the statistical analysis. Specify how blinding is preserved through data-analysis lock and unblinded at the analysis-plan-locked stage.

8. **Manipulation specifics (without inventing values).** For pharmacology: drug, dose, vehicle, route, timing relative to test, half-life consideration, pilot for dose selection. For viral: serotype, promoter, titer, volume, coordinates, recovery, expression-time. For optogenetics: opsin, stimulation parameters (frequency, pulse width, duty cycle, irradiance, total time). Mark all numeric values `[user-supplied]` unless the user has stated them.

9. **Welfare and 3Rs.** Endpoint criteria, humane endpoints, reduction strategy (e.g., within-subject design where appropriate; staged sample size), refinement (enrichment, social housing, low-stress procedures).

10. **Pre-specified analysis plan.** Primary model (mixed-effects with cage as random effect; sex as fixed effect; treatment × sex interaction). Multiple-testing across endpoints (Bonferroni / Holm / hierarchical). Effect-size + CI primary; p-value reported but secondary. Sensitivity analyses (excluding outliers per pre-specified rule; per-cohort).

11. **Reporting block.** Pre-build the ARRIVE 2.0 essential-10 + recommended-set items so the eventual paper has a home for each.

**Output format (locked):**

```
## Question and primary endpoint
- Claim:
- Primary variable + time-window:
- Falsification:

## Battery vs. single-task
- Construct or behavior?
- Tasks selected:
- Convergence rule (if battery):

## Cohort design matrix
| Sex | Treatment | Group | N per cell | Cage balance | Litter balance |

## Pre-registration draft
- Sample-size justification (assumption set):
- Analysis plan:
- Exclusion criteria:
- Sex stratification rule:
- Battery convergence rule:

## Habituation and handling
| Day | Action | Time-of-day | Operator |

## Counterbalancing matrix
| Axis | Crossed with treatment? | Method | Residual confound |

## Blinding plan
| Role | Person / blinded? | Unblinding step |

## Manipulation specifics (marked [user-supplied] for numerics)
- Pharmacology / viral / optogenetic / surgical:

## Welfare and 3Rs
- Endpoint criteria:
- Humane endpoints:
- Reduction / refinement / replacement:

## Pre-specified analysis plan
- Model:
- Random effects:
- Family-wise control:
- Effect-size + CI primary:
- Sensitivity:

## ARRIVE 2.0 pre-build
| Essential-10 item | Where in study it is generated |

## Pitfall register
| Failure mode | Detection | Mitigation |

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** ARRIVE 2.0 (essential-10 + recommended set); STAR Methods (Cell); preregistration on OSF, As.Predicted, or animal-research-specific registries (PCI Registered Reports for animal research where applicable); NIH SABV (consideration of sex as a biological variable); FAIR for raw behavioral data and analysis code.

**Verification checklist:**
- [ ] Primary endpoint and time-window pre-specified.
- [ ] Battery convergence rule (if battery) pre-specified.
- [ ] Both sexes included or single-sex justified.
- [ ] Sample size has an explicit assumption set or `[user-supplied]` marker.
- [ ] Counterbalancing matrix complete; residual confounds named.
- [ ] Blinding plan assigns roles and unblinding step.
- [ ] No invented drug doses, viral titers, line names.
- [ ] Unit of analysis matches between/within question.
- [ ] ARRIVE 2.0 essential-10 mapped.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Single-task construct claim | "Anxiety-like" from open field only | Battery with convergence rule |
| Sex pooling without test | Sexes merged → null result on one masked | Stratify; test interaction |
| Cage / litter confound | Treatment cages clustered | Counterbalancing matrix |
| Post-hoc exclusion | "Failed to learn" defined after seeing data | Exclusion pre-specified |
| Operator unblinded | Same person dispenses and scores | Blinded role assignment |
| Trial as unit | N = trials, not animals | Unit of analysis stated |
| Time-of-day confound | All treatment animals tested AM, controls PM | Time-of-day in counterbalance |
| Invented dose / titer | Plausible-looking concentration | `[user-supplied]` |
| No replication cohort | Single cohort claim | Cohort-replication plan |
| Sample size from convention | "We used N = 10 because we always do" | Power scenarios with assumption |
