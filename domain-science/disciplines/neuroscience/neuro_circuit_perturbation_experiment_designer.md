---
title: "Circuit Perturbation Experiment Designer"
category: science/disciplines/neuroscience
description: "Design a circuit-perturbation experiment (optogenetic / chemogenetic / lesion / pharmacological) with logic-of-causal-inference, controls, off-target audits, and dose-response"
techniques:
  - ST-01
  - ST-03
  - RT-03
  - CM-02
  - DS-02
  - QA-02
difficulty: advanced
tags:
  - optogenetics
  - chemogenetics
  - dreadds
  - lesion
  - causality
  - circuit
  - off-target
  - dose-response
updated: "2026-05-19"
related_prompts:
  - domain-science/disciplines/neuroscience/neuro_electrophysiology_protocol_designer.md
  - domain-science/disciplines/neuroscience/neuro_animal_behavior_experiment_designer.md
---

# Circuit Perturbation Experiment Designer

**Objective:** Design a circuit-perturbation experiment (optogenetic activation / inhibition, chemogenetic / DREADDs, focal pharmacology, lesion, electrical microstimulation) that supports a defensible causal claim about a circuit's role — with proper controls for the perturbation tool itself, off-target effects, temporal specificity, dose-response, and a behavioral / electrophysiological readout matched to the claim.

**When to use:** When the user wants to make a causal claim about a circuit (e.g., "activity in pathway A is necessary for behavior B"; "stimulating cell type C produces phenotype D"). Equally useful for triaging existing perturbation data whose claim might outrun the controls.

**Required inputs:**
- **Causal claim.** Necessity, sufficiency, or both, written as a single sentence.
- **Circuit / cell type / projection.** Target region + cell-type marker + projection origin / target (for axon-terminal manipulation).
- **Tool family.** Optogenetic (ChR2 / ChRmine / iC++ / NpHR / GtACR / soma-targeted variants); chemogenetic (DREADDs hM3Dq / hM4Di / KORD / others); pharmacological (NMDA / AMPA / GABA / muscarinic / nicotinic agonists / antagonists); lesion (electrolytic / excitotoxic / genetic / aspiration); electrical microstim.
- **Readout.** Behavioral (which task), physiological (which recording), imaging (which signal), molecular.
- **Timescale.** Acute (ms–s), short-term (min–hr), chronic (days–weeks).
- **Animal model + genetic targeting strategy.** Cre line + viral approach, or other targeting.

**Optional inputs:**
- Closed-loop intent (real-time triggering on a neural signal).
- Pilot data.
- Constraints (no surgical implant, no tethering, behavioral apparatus access).

**Constraints — Must:**
- Distinguish necessity (loss-of-function) from sufficiency (gain-of-function). Each requires different controls; do not conflate.
- Pre-specify the *intended* perturbation effect: cell-type-specific or projection-specific or terminal-specific. State how the targeting strategy supports the claim.
- For every active manipulation, include the matched inactive control: opsin-negative + light; CNO / DCZ + opsin-negative animals (or vehicle in opsin-positive); vehicle-injected; sham surgery; opsin-only-no-light; off-target-region perturbation.
- Audit off-target effects: light-induced heating (Stujenske et al.-style); CNO / DCZ off-target binding and pharmacokinetics; viral leakage to neighboring regions; spread of pharmacology; axon-of-passage effects in lesion.
- For optogenetics: report opsin, expression strategy, wavelength, irradiance at tissue (in mW/mm²), pulse parameters, total light exposure, baseline / on / off comparisons; histological verification of expression spread.
- For chemogenetics: justify ligand choice; report dose, route, vehicle, time-to-onset, duration; control for non-DREADD ligand effects.
- Dose-response or strength-response curve where feasible: at least three levels of perturbation strength (intensity, frequency, dose) to demonstrate the effect scales sensibly.
- Recovery / reversibility: where claim implies reversibility (e.g., optogenetic), include the off-period as a within-subject control.
- Histology: post-hoc verification of expression / electrode placement / lesion extent on every animal. Animals failing verification are excluded per a pre-specified rule.
- Align reporting to ARRIVE 2.0 for animal handling and to community conventions for opsin / DREADD reporting (e.g., reporting irradiance at tissue, not laser output).

**Constraints — Must Not:**
- Do not invent opsin / DREADD variants, viral titers, or ligand doses.
- Do not propose a "necessity" claim from gain-of-function data alone (or vice versa).
- Do not use only opsin-negative + no-light as the only control (must include light delivered to opsin-negative animals to control for heating / direct stimulation).
- Do not interpret CNO-only effects as DREADD-mediated without an opsin-negative + CNO comparison.
- Do not silently exclude animals failing histology after seeing the result.
- Do not pool animals with substantially different expression / placement / dose.

**Instructions:**

1. **Restate the claim and pick the perturbation tool.** Necessity vs. sufficiency. Tool matched to timescale and reversibility requirement (optogenetic for ms; DREADDs for hours; lesion for permanent).

2. **Targeting strategy.** Cre line × viral approach × promoter × serotype × titer × volume × coordinates → expected cell-type and projection coverage. Specify off-target risk (leakage, projection of passage, neighboring region). Mark numeric values `[user-supplied]`.

3. **Control matrix.** Build the full control set:
    - Opsin / DREADD-negative animals receiving light / ligand.
    - Opsin / DREADD-positive animals receiving no light / vehicle.
    - Off-target region perturbation (parallel circuit not expected to drive readout).
    - Ligand-only control for chemogenetics (CNO / DCZ alone in non-DREADD animals).
    - Yoked / sham-surgery controls where surgery itself could affect behavior.

4. **Perturbation parameters.** Optogenetics: wavelength, irradiance at tissue (mW/mm² estimated from fiber, tissue, depth), pulse width, frequency, duty cycle, total exposure, on / off scheduling. Chemogenetics: ligand, dose, vehicle, route, time-of-administration relative to test, expected occupancy timeline. Pharmacology: drug, concentration, volume, infusion rate, diffusion estimate, dummy-cannula control. Lesion: method (electrolytic / NMDA / 6-OHDA / DREADD-toxin / saporin), expected spread, time-to-test.

5. **Readout matched to claim.** Behavioral assay sensitive to the predicted direction; physiological recording during perturbation to confirm circuit-level effect; ideally both. State how the readout would distinguish circuit-specific effect from general motor / motivational / sensory confound.

6. **Off-target audit.** For each perturbation:
    - Optogenetics: heating estimate per parameters; opsin-negative + light arm.
    - Chemogenetics: CNO-only arm; report DCZ alternative if relevant.
    - Pharmacology: diffusion estimate; cannula-misplacement audit; saline control.
    - Lesion: axon-of-passage; neighboring-region damage; cell-type non-specificity.
7. **Dose-response.** Three or more levels of intensity / frequency / dose, randomized across sessions or animals where feasible. State the predicted shape (saturating, monotonic, U-shape) and what the result would look like if the claim is wrong.

8. **Within-subject structure.** Where possible, use the same animal across on / off / off-target / sham conditions (counterbalanced). State the unit-of-analysis (animal for between-subjects necessity claims).

9. **Histology and inclusion / exclusion.** Post-hoc verification of expression spread, fiber tip placement, electrode placement, lesion extent. Inclusion criteria pre-specified. Animals failing histology are excluded by rule, not by data.

10. **Pre-specified analysis.** Mixed-effects model with subject as random effect, condition as fixed effect, baseline as covariate. Effect-size + CI primary. Multiple-comparisons across conditions. Sensitivity analyses (excluding animals at expression-spread extremes).

11. **Reporting.** ARRIVE 2.0 + perturbation-specific reporting (irradiance at tissue; ligand dose / route / time; cannula coordinates; histological figures); deposit raw behavioral / physiological data with metadata; histological images archived.

**Output format (locked):**

```
## Claim and tool
- Claim type (necessity / sufficiency / both):
- Tool:
- Justification:

## Targeting strategy
- Cre line / promoter:
- Viral approach / serotype / titer / volume / coordinates:
- Expected coverage:
- Off-target risk:

## Control matrix
| Control arm | What it controls for |

## Perturbation parameters (marked [user-supplied] where numeric)
- Optogenetics / Chemogenetics / Pharmacology / Lesion:

## Readout
- Behavioral assay:
- Physiological recording (if applicable):
- Confound-distinction logic:

## Off-target audit
| Risk | Diagnostic / control arm |

## Dose-response
| Level | Parameter value | Animals per level | Predicted shape |

## Within-subject structure
- Counterbalancing:
- Unit of analysis:

## Histology and inclusion criteria
- Verification target:
- Inclusion criteria:
- Pre-specified exclusion rule:

## Pre-specified analysis
- Model:
- Random / fixed effects:
- Multiple-comparisons:
- Sensitivity:

## Reporting
- ARRIVE 2.0 mapping:
- Irradiance / dose-route reporting:
- Histology figure plan:
- Data deposit:

## Open questions for the user
[gaps marked [user-supplied]]
```

**Reporting-standard alignment:** ARRIVE 2.0; community standards for opsin reporting (irradiance at tissue, not laser output; expression spread reported); chemogenetic reporting (ligand, dose, route, vehicle, control-group CNO administration); for circuit claims, dual-direction logic (necessity + sufficiency) per current best practice in systems neuroscience.

**Verification checklist:**
- [ ] Necessity vs. sufficiency claim explicit; control matrix matches.
- [ ] Control matrix includes opsin-negative + light AND opsin-positive + no-light arms.
- [ ] CNO-only arm present for chemogenetic experiments.
- [ ] Off-target audit specifies diagnostic per risk.
- [ ] Dose-response at ≥3 levels planned.
- [ ] Histology verification pre-specified; exclusion rule pre-specified.
- [ ] Irradiance reported at tissue, not at laser output.
- [ ] No invented viral titers / ligand doses.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Heating mistaken for opsin effect | High-power light in opsin-negative animals not run | Opsin-neg + light control |
| CNO off-target effect | Vehicle CNO causes behavioral change | CNO-only arm in non-DREADD animals |
| Expression leakage to neighbors | "Region X drives behavior" but expression in X+neighbor | Histology + off-target arm |
| Axon-of-passage in lesion | Fiber-of-passage damage misattributed | Lesion-method choice and audit |
| Saturating dose response | Single intensity hides U-shape | ≥3 levels |
| Necessity from sufficiency | "Activating X drives Y → X is necessary" | Necessity claim requires loss-of-function |
| Post-hoc histology exclusion | Animals failing histology removed only when convenient | Pre-specified rule |
| Pooling expression extremes | Wide expression variation pooled | Sensitivity excluding extremes |
| Invented viral titer / ligand dose | Plausible-looking 1e12 vg/mL or 1 mg/kg CNO | `[user-supplied]` |
| Irradiance at laser, not tissue | "10 mW" laser output reported as stimulation | Tissue-level irradiance reported |
