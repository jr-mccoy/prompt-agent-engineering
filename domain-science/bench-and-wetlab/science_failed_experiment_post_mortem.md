---
title: "Failed-Experiment Post-Mortem"
category: science/bench-and-wetlab
description: "A structured post-mortem that localizes an experimental failure across question, design, protocol, execution, and chance, using control-based diagnosis, and ends in an iterate/redesign/abandon/escalate decision."
techniques:
  - ST-01
  - RT-01
  - RT-03
  - QA-02
  - NE-10
  - CM-02
difficulty: advanced
tags:
  - post-mortem
  - failure-analysis
  - controls
  - confound
  - root-cause
  - reproducibility
  - decision-making
  - calibration
updated: "2026-06-26"
related_prompts:
  - domain-science/methods-foundations/science_replicability_premortem.md
  - domain-science/methods-foundations/science_negative_and_positive_control_designer.md
  - domain-science/bench-and-wetlab/science_lab_notebook_entry_writer.md
---

# Failed-Experiment Post-Mortem

**Objective:** Take a single failed or anomalous experiment and systematically localize the failure to one or more layers — the **question** (untestable/underspecified), the **design** (confounded/underpowered), the **protocol** (wrong method/conditions), the **execution** (operator/reagent/instrument error), or **chance** (true negative / expected variance) — using control-based diagnosis rather than narrative guesswork. Output a layered diagnosis and a defensible next-action decision: iterate, redesign, abandon, or escalate. The analysis must resist the common bias of blaming chance to preserve a favored hypothesis.

**When to use:** After an experiment yields no signal, an implausible result, a control failure, or a result that contradicts a strong prior — and before re-running, modifying the protocol, or abandoning the hypothesis.

**Required inputs:**
- **Discipline.** [user-supplied]
- **Study type.** [user-supplied] (was this pre-specified/confirmatory or exploratory?)
- **The hypothesis/objective tested** and the prediction that failed.
- **Controls run and their outcomes** (positive control, negative control, vehicle, NTC, etc.) — [user-supplied].
- **The observed result** and how it differs from expectation — record exactly what the user reports.

**Optional inputs:**
- Prior runs of the same experiment and their outcomes (replicate history).
- Power/sample-size basis, if any.
- Recent changes (new reagent lot, new operator, instrument service, protocol edit).
- ELN/notebook reference for the run.

**Constraints — Must:**
- Diagnose against the **five layers** explicitly (question → design → protocol → execution → chance) and state evidence for each.
- Use **control outcomes** as the primary localizer (e.g., positive control failing implicates protocol/reagent/execution, not the biology of interest).
- Distinguish **pre-specified vs exploratory** status, because it changes how a "negative" result is interpreted.
- Express conclusions in **calibrated, probability-weighted** language across the candidate causes (NE-10).
- Cross-reference design-level concerns to a replicability premortem and controls-design analysis rather than re-deriving them.
- Adversarially test the most comfortable explanation first (QA-02) — especially any appeal to chance.

**Constraints — Must Not:**
- Do not invent vendor names, catalog/lot numbers, reagent specs, or results/observations. If needed and not supplied, mark `[user-supplied]` and ask; the prompt records what the user supplies, it never fabricates data.
- Do not attribute failure to chance without ruling out positive-control failure and known execution risks.
- Do not recommend re-running an identical protocol when the diagnosis points to design or question layers.
- Do not use promotional language ("novel", "groundbreaking", "first-ever", "gold standard") in drafted text.

**Instructions:**

1. **Restate the failure factually.** Record the hypothesis, the failed prediction, and the observed result using only user-supplied facts; mark gaps `[user-supplied]`.
2. **Read the controls first.** Tabulate each control and its outcome. Use control logic to bound the failure (positive control failed → upstream protocol/reagent/execution; negative control fired → contamination/specificity; all controls fine, only the test arm null → design/question/chance).
3. **Walk the five layers (RT-01).** For each layer, state the specific failure hypotheses and the evidence for/against, drawing on controls, replicate history, and recent changes.
4. **Branch the diagnosis (RT-03).** Where layers are entangled, enumerate the competing explanatory branches and what evidence would distinguish them.
5. **Adversarial check (QA-02).** Attack the explanation that best preserves the favored hypothesis. Explicitly test whether "it was just chance/variance" survives the positive-control and power evidence.
6. **Assign calibrated weights (NE-10).** Give a probability-weighted distribution over the candidate causes, with the assumptions behind each weight.
7. **Decide the next action.** Map the dominant cause(s) to one of iterate (same question, tightened execution), redesign (fix confound/power), abandon (question/hypothesis not supported), or escalate (needs supervisor/collaborator/new method). State the disconfirming evidence that would change the decision.
8. **Capture for the record.** Note what should be logged in the ELN and what to deposit if this informs an Open Science protocol revision.

**Output format (locked):**

```
## Failure Summary (facts only)
- Hypothesis / failed prediction:
- Observed result:
- Pre-specified or exploratory:
- Open items ([user-supplied]):

## Control Readout
| Control | Expected | Observed | Implication |
|---|---|---|---|

## Layered Diagnosis
| Layer | Failure hypotheses | Evidence for | Evidence against | Localized? |
|---|---|---|---|---|
| Question | | | | |
| Design | | | | |
| Protocol | | | | |
| Execution | | | | |
| Chance | | | | |

## Adversarial Check
- Comfortable explanation tested:
- Survives positive-control / power evidence? :

## Probability-Weighted Causes
| Candidate cause | Weight | Key assumption |
|---|---|---|

## Decision
- Action: iterate / redesign / abandon / escalate
- Rationale:
- What would change this decision:

## To Log / Deposit
```

**Reporting-standard alignment:** ARRIVE 2.0 (where in-vivo design is implicated); ALCOA+ for the record of facts; controls-design and replicability-premortem cross-references for design-layer issues.

**Verification checklist (before delivering):**
- [ ] All five layers are addressed with explicit evidence, not skipped.
- [ ] Control outcomes are read before any layer is blamed.
- [ ] A chance attribution is only made after positive-control and power evidence is considered.
- [ ] Pre-specified vs exploratory status is stated and used.
- [ ] Conclusions are probability-weighted, not single-cause certainties.
- [ ] The decision maps to the dominant cause and lists disconfirming evidence.
- [ ] Only user-supplied facts are recorded; no fabricated observations or lot numbers.
- [ ] Banned promotional terms absent.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Chance-blaming bias | "Just biological variance" preserves the pet hypothesis | Require positive-control + power evidence before accepting chance |
| Single-cause tunnel | One clean story for a multi-layer failure | Force all five layers in the table, even when one dominates |
| Re-run reflex | Repeating an identical protocol feels productive | Block iterate when diagnosis localizes to design/question layers |
| Ignored control | Test-arm null read as biology while positive control also failed | Read controls first; positive-control failure overrides biology claims |
| Overconfident verdict | Decisive abandon/confirm from one underpowered run | Calibrate with weights; require disconfirming-evidence statement |
