# `domain-science/bench-and-wetlab/`

The bench / wet-lab practice layer for the experimental scientist: drafting and troubleshooting protocols, reagent and buffer math, cell / animal / human-subjects protocols, biosafety, sample custody, lab-notebook discipline, and reagent validation. Composes on top of [`../methods-foundations/`](../methods-foundations/) (controls, power, reproducibility) and routes oversight matters to the relevant committee.

**Scope & safety:** these are legitimate bench-practice aids. They identify hazards at the class level and route to the official SDS, institutional EHS, and the IACUC / IRB / IBC / biosafety officer — they never grant approval, assert hazard facts from memory, or provide operational uplift for creating or enhancing a hazard. Dual-use concerns route to [`../ethics-integrity/science_dual_use_research_assessment.md`](../ethics-integrity/science_dual_use_research_assessment.md).

## Map (Phase 2B — 12 prompts)

### Protocols & lab math

| File | Coverage |
|---|---|
| [`science_lab_protocol_drafter.md`](science_lab_protocol_drafter.md) | STAR-Methods-style protocol: materials, numbered steps with critical timing/temp, controls, hazard/PPE routed to SDS, expected readout |
| [`science_lab_protocol_optimizer.md`](science_lab_protocol_optimizer.md) | 5-Whys troubleshooting of a failed protocol; ranked cause→diagnostic→fix; one-variable-at-a-time discipline |
| [`science_reagent_and_supply_calculator.md`](science_reagent_and_supply_calculator.md) | Molarity / dilution / serial-dilution / %w-v with shown unit-checking and dimensional analysis |
| [`science_buffer_recipe_designer.md`](science_buffer_recipe_designer.md) | Buffer by pH vs pKa (Henderson-Hasselbalch), ionic strength, downstream-assay compatibility |

### Oversight-committee protocols & biosafety

| File | Coverage |
|---|---|
| [`science_cell_culture_protocol_designer.md`](science_cell_culture_protocol_designer.md) | Line-specific media/passaging, STR authentication + mycoplasma cadence (NIH rigor), QC log |
| [`science_animal_protocol_iacuc_drafter.md`](science_animal_protocol_iacuc_drafter.md) | IACUC scaffold aligned to ARRIVE 2.0 + the 3Rs; humane endpoints; sample-size justification |
| [`science_human_subjects_irb_protocol_drafter.md`](science_human_subjects_irb_protocol_drafter.md) | IRB scaffold: risk-benefit, consent/assent, vulnerable populations, data security (Belmont/Common Rule) |
| [`science_biosafety_risk_assessment.md`](science_biosafety_risk_assessment.md) | Risk-group / BSL-ABSL determination logic + IBC submission scaffold; dual-use screen pointer (governance level only) |

### Records, rigor & validation

| File | Coverage |
|---|---|
| [`science_sample_logging_chain_of_custody_designer.md`](science_sample_logging_chain_of_custody_designer.md) | Unique sample-ID schema, freezer location model, ELN linkage, retention/destruction (ALCOA+) |
| [`science_failed_experiment_post_mortem.md`](science_failed_experiment_post_mortem.md) | Layered diagnosis: question vs design vs protocol vs execution vs chance; next-action decision |
| [`science_lab_notebook_entry_writer.md`](science_lab_notebook_entry_writer.md) | ELN entry recording only user-supplied facts; deviations logged; observation-vs-inference separated (ALCOA+) |
| [`science_reagent_validation_workflow.md`](science_reagent_validation_workflow.md) | Antibody multi-pillar validation, primer specificity, cell-line authentication — reproducibility-critical, pre-use |

## Floor (per [`../README.md`](../README.md))

Every prompt requires discipline + study type; forbids fabricated vendor / catalog / lot / reagent / hazard / regulatory facts (`[user-supplied]`, routed to SDS / EHS / IACUC / IRB / IBC); locks the output format; names the relevant standard (STAR Methods, ARRIVE 2.0, the 3Rs, Belmont/Common Rule, NIH authentication & rigor guidance, ALCOA+); keeps controls and sample-size justification first-class; defaults to the Open Science branch (protocol deposit, authenticated lines, FAIR sample metadata) with consent/biosafety/proprietary constraints named as the non-default exception; and ends with a verification checklist + false-positive matrix. The notebook and post-mortem prompts never fabricate observations.

See [`../EXPANSION_ROADMAP.md`](../EXPANSION_ROADMAP.md) for the remaining phases and build order.
