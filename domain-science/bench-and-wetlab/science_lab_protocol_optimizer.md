---
title: "Lab Protocol Optimizer (Failure Troubleshooting)"
category: science/bench-and-wetlab
description: "Structured troubleshooting of a failed wet-lab protocol: build a failure-mode taxonomy for the assay class, run 5-Whys per symptom, and produce a ranked diagnosis-and-experiment table under one-variable-at-a-time discipline."
techniques:
  - ST-01
  - RT-01
  - RT-03
  - QA-02
  - NE-10
difficulty: advanced
tags:
  - troubleshooting
  - failure-mode-analysis
  - five-whys
  - wet-lab
  - controls
  - root-cause
  - bench-practice
  - reproducibility
updated: "2026-06-26"
related_prompts:
  - domain-science/bench-and-wetlab/science_lab_protocol_drafter.md
  - domain-science/bench-and-wetlab/science_reagent_and_supply_calculator.md
  - domain-science/bench-and-wetlab/science_buffer_recipe_designer.md
  - domain-science/methods-foundations/science_negative_and_positive_control_designer.md
  - domain-science/methods-foundations/science_reproducibility_self_audit.md
---

# Lab Protocol Optimizer (Failure Troubleshooting)

**Objective:** Take a protocol that failed or under-performed and systematically localize the cause. Build a failure-mode taxonomy for the assay class, run a 5-Whys chain per observed symptom, and emit a ranked hypothesis table mapping likely cause → diagnostic test → corrective fix → confirmation criterion. Enforce one-variable-at-a-time change discipline and a positive control to isolate where in the workflow the failure lives.

**When to use:** A run produced no signal, high background, irreproducibility, off-target results, or a quantitative miss, and you need a disciplined diagnostic plan rather than ad-hoc tweaking. Use before re-running, so each re-run tests a single hypothesis.

**Required inputs:**
- **Discipline.** <e.g., molecular biology, biochemistry, cell biology, microbiology>
- **Study type.** <experimental / method-development / QC validation>
- **Assay/technique that failed.** <e.g., Western blot, qPCR, transfection, ELISA, PCR>
- **Observed symptom(s).** <no signal, high background, smearing, low yield, Cq drift, etc.>
- **What was expected vs observed.** <the readout gap, quantitative if possible>

**Optional inputs:**
- The protocol version that was run (point to `science_lab_protocol_drafter.md`)
- Which controls were included and how they behaved
- Recent changes (new lot, new operator, new instrument, new buffer)
- Replicate structure and whether failure was consistent or sporadic

**Constraints — Must:**
- Build a **failure-mode taxonomy partitioned by cause class**: reagent, sample, operator/technique, instrument, protocol/parameter, and biology — so no class is overlooked.
- Run a **5-Whys chain per distinct symptom**, stopping at a testable root-cause hypothesis (not a guess).
- Use **Tree-of-Thoughts branching (RT-03)** to keep competing root causes alive until a diagnostic discriminates them.
- Produce a **ranked diagnosis-and-experiment table**; ranking reflects prior likelihood and ease of test.
- Enforce **one-variable-at-a-time (OVAT)** change discipline; each proposed re-run changes exactly one factor.
- Require a **positive control** (and the relevant negative/vehicle controls) to localize whether failure is upstream (reagents/sample) or downstream (detection/instrument); cross-reference `science_negative_and_positive_control_designer.md`.
- Express residual uncertainty with **probability-weighted language (NE-10)** when multiple causes remain plausible.

**Constraints — Must Not:**
- Do not invent vendor names, catalog/lot numbers, reagent specifications, or hazard/SDS data. If needed and not supplied, mark `[user-supplied]` and ask; route all safety/hazard facts to the official SDS and institutional EHS.
- Do not recommend changing multiple variables at once "to save time."
- Do not assert that a specific lot/reagent is degraded or hazardous from memory; flag it as a hypothesis to test, with SDS for any handling.
- Do not use promotional language ("novel," "groundbreaking," "first-ever," "gold standard") in the drafted output.
- Do not conclude root cause without a confirming diagnostic.

**Instructions:**

1. **Restate the failure precisely.** Capture discipline, study type, assay, the expected-vs-observed gap, and how controls behaved. A failing positive control vs a failing sample-only result points to different cause classes.
2. **Build the assay-class failure taxonomy.** Enumerate plausible failure modes grouped by the six cause classes (reagent / sample / operator / instrument / protocol / biology) specific to this assay.
3. **Run 5-Whys per symptom.** For each distinct symptom, ask "why" iteratively until you reach a testable mechanistic hypothesis, not a restatement.
4. **Branch competing causes (ToT).** Where 5-Whys yields more than one viable root, keep each branch and identify the diagnostic that discriminates them.
5. **Localize with a positive control.** Specify a positive control (and negatives/vehicle) whose behavior splits upstream vs downstream failure; state what each control outcome would mean.
6. **Rank hypotheses.** Order by prior likelihood × ease/cost of the diagnostic; assign probability-weighted confidence where causes remain ambiguous.
7. **Design OVAT diagnostics.** For each ranked cause, define the single-variable test, the predicted result if the cause is real, and the confirmation criterion. Defer any concentration/buffer changes to `science_reagent_and_supply_calculator.md` / `science_buffer_recipe_designer.md`.
8. **Emit the diagnosis-and-experiment table** and a recommended testing order.
9. **Self-check adversarially.** Stress-test the plan (QA-02): does any proposed change confound interpretation? Is any control missing? Revise before delivering.

**Output format (locked):**

```
## Failure Summary
Discipline: <...> | Study type: <...> | Assay: <...>
Expected vs Observed: <...> | Control behavior: <...>

## Failure-Mode Taxonomy (by cause class)
- Reagent: <...>
- Sample: <...>
- Operator/Technique: <...>
- Instrument: <...>
- Protocol/Parameter: <...>
- Biology: <...>

## 5-Whys (per symptom)
Symptom: <...>
  Why1 → Why2 → Why3 → Why4 → Why5 → Root hypothesis: <testable>

## Localization Control
- Positive control: <...> → if it <fails/passes>, failure is <upstream/downstream>
- Negative / vehicle: <...>

## Ranked Diagnosis & Experiment Plan (OVAT)
| Rank | Likely cause | Prob. | Single-variable diagnostic | Predicted result if true | Fix | Confirm by |
|---|---|---|---|---|---|---|
| 1 | <...> | <~%> | <one change> | <...> | <...> | <...> |

## Recommended Testing Order & Notes
- <ordered next runs; one variable each>
```

**Reporting-standard alignment:** STAR Methods troubleshooting conventions; protocols.io versioning for revised protocols; good-documentation / ELN practice for logging each OVAT change; reproducibility self-audit (`science_reproducibility_self_audit.md`).

**Verification checklist (before delivering):**
- [ ] Discipline and study type captured first.
- [ ] Taxonomy covers all six cause classes for this assay.
- [ ] A 5-Whys chain exists for each distinct symptom and ends in a testable hypothesis.
- [ ] Competing root causes are kept distinct with a discriminating diagnostic.
- [ ] A positive control localizes upstream vs downstream failure.
- [ ] Every proposed diagnostic changes exactly one variable (OVAT).
- [ ] Hypotheses ranked with probability-weighted confidence where ambiguous.
- [ ] No invented reagent/lot/hazard facts; lot degradation framed as a hypothesis to test.

**False-positive matrix:**

| Risk | What "looks right but isn't" | Guardrail |
|---|---|---|
| Premature root cause | A confident single-cause conclusion with no confirming test | Require a diagnostic + confirmation criterion before concluding |
| Multi-variable change | "Increase template AND anneal temp AND cycles" in one re-run | Enforce OVAT; one variable per proposed run |
| Missing localization | Jumping to reagents without a positive control | Mandate a positive control to split upstream/downstream |
| Blaming a lot from memory | "Your enzyme lot is bad" asserted, not tested | Frame as hypothesis; verify with fresh-aliquot/positive-control test |
| Taxonomy gap | Ignoring operator or biology causes, only chasing reagents | Six-class taxonomy gate forces full coverage |
