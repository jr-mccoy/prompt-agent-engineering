---
title: "Negative and Positive Control Designer"
category: science/methods-foundations
description: "Select and justify negative, vehicle/sham, positive, internal, and batch controls for a specific experimental design, keyed to the artifact each control rules out."
techniques:
  - ST-01
  - ST-03
  - RT-01
  - QA-01
  - CM-02
  - DS-02
difficulty: advanced
tags:
  - controls
  - negative-control
  - positive-control
  - vehicle-control
  - sham
  - batch-effects
  - arrive
  - star-methods
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_experimental_design_advisor.md
  - domain-science/methods-foundations/science_blinding_and_randomization_protocol.md
  - domain-science/methods-foundations/science_confound_and_bias_audit.md
  - domain-science/methods-foundations/science_threats_to_validity_walkthrough.md
---

# Negative and Positive Control Designer

**Objective:** Design the full control set for a specific experiment so every observed effect can be attributed to the intended manipulation rather than a reagent, instrument, batch, or expectancy artifact. Map each control to the precise alternative explanation it isolates, and state what a control failure would mean for interpretation. Output a control matrix and reporting-aligned justification.

**When to use:** You have a defined manipulation and readout but have not yet locked which negative, positive, vehicle/sham, internal, loading, and batch controls are required — or a reviewer has flagged inadequate controls.

**Required inputs:**
- **Discipline.** <field — e.g., molecular biology, pharmacology, behavioral neuroscience, analytical chemistry>
- **Study type.** <observational / experimental / computational / in vitro / in vivo / ex vivo>
- **Manipulation.** What is applied/perturbed (drug, gene edit, antibody, stimulus, algorithm).
- **Primary readout(s).** What is measured and on what instrument/assay.
- **Experimental unit and N.** Cell well, animal, subject, sample; replication structure.

**Optional inputs:**
- Known reference compounds/conditions with established effect direction.
- Reagent identities (antibody clone, vector, vehicle solvent) — supply or mark `[user-supplied]`.
- Batch/run structure (plates, sessions, lots, operators).
- Detection limits, dynamic range, or expected effect magnitude.

**Constraints — Must:**
- Ask for discipline and study type before designing.
- For every control, state the specific alternative explanation it rules out (reagent artifact, off-target, expectancy, instrument drift, batch, loading, carryover).
- Distinguish pre-specified controls (in the protocol) from any exploratory controls added post hoc.
- Name reporting expectations explicitly: ARRIVE 2.0 (in vivo animal), STAR Methods (cell/molecular), and MIQE where qPCR is used.
- Specify the experimental unit at which each control is randomized/applied.

**Constraints — Must Not:**
- Do not invent citations, DOIs, effect sizes, or instrument/vendor specs. If needed and not supplied, mark `[user-supplied]` and ask.
- Do not assert a reference compound's effect direction/magnitude unless supplied; mark `[user-supplied]`.
- Do not use "novel", "groundbreaking", "first-ever", or "gold standard"; describe controls by function.
- Do not treat technical replicates as biological replicates, or a single positive control as sufficient validation of a full assay.

**Instructions:**

1. **Restate the causal claim.** Write the one-sentence claim the experiment must support, and name the readout-to-manipulation link that controls must protect.
2. **Enumerate alternative explanations.** List every non-target reason the readout could change: reagent/vehicle effect, off-target binding, expectancy/handling, instrument drift, batch/lot, loading/normalization, carryover, plate-position effects.
3. **Select negative controls.** Map alternatives to: no-treatment/baseline (spontaneous level), vehicle/sham (carrier or procedure without active agent), isotype/IgG (antibody specificity), scrambled/non-targeting (sequence-based perturbations), untransfected/empty-vector (delivery artifact). State which apply and which are not needed, with reasons.
4. **Select positive controls.** Choose a known-effect reference that should move the readout in a defined direction, and/or a spike-in/recovery standard for quantitative assays. Mark effect direction/magnitude `[user-supplied]` if not provided.
5. **Specify internal, loading, and normalization controls.** Housekeeping/reference signals, input normalization, internal standards, and run-order controls that detect drift within a batch.
6. **Specify batch and technical controls.** Define batch structure, inter-plate calibrators, technical replicates, and how batch is balanced or blocked against condition.
7. **Define pass/fail criteria.** For each control, state the expected result and the threshold that constitutes a failure, before data collection.
8. **State failure interpretation.** For each control, write what a failure means (invalidates run, indicates off-target, indicates drift) and the resulting action (discard, repeat, re-normalize).
9. **Align to reporting standard.** Map the control set onto ARRIVE 2.0 / STAR Methods / MIQE items and flag any unmet expectation.

**Output format (locked):**

```
## Causal claim under protection
[one sentence]

## Alternative explanations to be ruled out
- [explanation] → addressed by [control or "UNADDRESSED"]

## Control matrix
| Control | Type (neg/pos/internal/batch) | What it isolates | Applied at unit | Expected result | Failure means | Action on failure |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

## Pre-specified vs exploratory
- Pre-specified: [...]
- Exploratory (post hoc, flagged): [...]

## Reporting-standard alignment
- Standard: [ARRIVE 2.0 / STAR Methods / MIQE]
- Met: [...]
- Gaps / [user-supplied]: [...]

## Open residual confounds
[controls that do NOT rule out X — defer to confound audit]
```

**Reporting-standard alignment:** ARRIVE 2.0 (in vivo animal experiments — control groups, randomization context), STAR Methods (cell/molecular reagent and validation reporting), MIQE (qPCR controls). Name only the standard(s) relevant to the supplied study type.

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured before any control was proposed.
- [ ] Every observed-effect alternative explanation maps to a control or is flagged UNADDRESSED.
- [ ] Negative controls cover reagent/vehicle, specificity, and delivery artifacts as applicable.
- [ ] At least one positive control or spike-in establishes assay sensitivity; effect direction marked `[user-supplied]` if not given.
- [ ] Internal/loading/normalization and batch controls are specified, not assumed.
- [ ] Pass/fail thresholds are pre-specified, not derived from the data.
- [ ] Technical vs biological replication is not conflated.
- [ ] No fabricated reference effects, vendor specs, or citations; unknowns marked `[user-supplied]`.
- [ ] Banned hype language absent.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Vehicle confusion | "Untreated" baseline presented as the negative control when the vehicle solvent itself is bioactive | Require a vehicle/sham arm distinct from no-treatment whenever a carrier is used |
| Positive-control theater | A positive control that works once is treated as validating every plate/run | Require the positive control on every batch with a pre-set pass threshold |
| Specificity gap | An antibody/probe result with no isotype/non-targeting control read as on-target | Flag specificity UNADDRESSED until isotype/scrambled control is included |
| Replicate inflation | Technical replicates counted toward N, making controls look adequately powered | Force explicit biological-vs-technical labeling at the experimental unit |
| Batch masquerade | Condition effect that is actually a plate/lot/operator effect | Require batch balanced/blocked against condition and an inter-batch calibrator |
