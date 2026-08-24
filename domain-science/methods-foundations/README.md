# `domain-science/methods-foundations/`

The reusable scientific-methodology layer for the working scientist. These prompts cover the research lifecycle *before and around* discipline-specific execution — refining the question, pre-specifying the design and analysis, justifying sample size, controlling confounds, and auditing for replicability and reproducibility. The discipline modules in [`../disciplines/`](../disciplines/) and the statistics / bench / computational phases compose on top of this layer.

**Convention:** anything that applies across disciplines lives here. A prompt moves to `disciplines/` only when a generic counterpart would lose force.

## Map (Phase 2A — 14 prompts + 3 relocated Phase 1 prompts)

### Question, pre-specification & reporting

| File | Coverage |
|---|---|
| [`science_research_question_refiner.md`](science_research_question_refiner.md) | Vague curiosity → specific, testable, scoped question (FINER / PICO, feasibility + falsifiability check) |
| [`science_preregistration_drafter.md`](science_preregistration_drafter.md) | OSF-style preregistration: hypotheses, design, sampling, analysis plan, confirmatory/exploratory split, deviations clause |
| [`science_registered_report_stage1_drafter.md`](science_registered_report_stage1_drafter.md) | Stage-1 Registered Report skeleton with study-design table and outcome-neutral quality checks |
| [`science_methods_section_drafter.md`](science_methods_section_drafter.md) | IMRaD methods section, skeleton-first, bound to the right reporting checklist (CONSORT / STROBE / PRISMA / ARRIVE 2.0 / …) |

### Design rigor

| File | Coverage |
|---|---|
| [`science_methodology_decision_tree.md`](science_methodology_decision_tree.md) | Route to RCT vs quasi-experiment vs observational vs simulation, with the load-bearing assumption each buys |
| [`science_qualitative_vs_quantitative_decision.md`](science_qualitative_vs_quantitative_decision.md) | Match paradigm to question; surface mixed-methods designs |
| [`science_power_and_sample_size_calculator.md`](science_power_and_sample_size_calculator.md) | Frequentist + Bayesian power, three scenarios, sensitivity grid, assumptions surfaced |
| [`science_pilot_study_designer.md`](science_pilot_study_designer.md) | Feasibility-objective pilot with go/no-go progression criteria; what a pilot can and cannot tell you |
| [`science_negative_and_positive_control_designer.md`](science_negative_and_positive_control_designer.md) | Control selection logic: each control → what it isolates → what its failure means |
| [`science_blinding_and_randomization_protocol.md`](science_blinding_and_randomization_protocol.md) | Sequence generation, allocation concealment (kept distinct from blinding), blinding levels, unblinding contingencies |

### Validity, confounds & integrity of the finding

| File | Coverage |
|---|---|
| [`science_confound_and_bias_audit.md`](science_confound_and_bias_audit.md) | Working bias taxonomy → ranked bias register with design-stage vs analysis-stage mitigations (DAG-based) |
| [`science_threats_to_validity_walkthrough.md`](science_threats_to_validity_walkthrough.md) | Cook & Campbell four-validity audit applied to one named design |
| [`science_replicability_premortem.md`](science_replicability_premortem.md) | "Assume an independent direct replication failed — why?" ranked risk register + pre-publication robustness checks |
| [`science_reproducibility_self_audit.md`](science_reproducibility_self_audit.md) | FAIR-aligned data / code / environment / documentation audit (same data + code → same result) |

### Relocated Phase 1 prompts

| File | Coverage |
|---|---|
| [`science_experimental_design_advisor.md`](science_experimental_design_advisor.md) | Propose 2–4 designs under constraints; controls, randomization, power, confounds |
| [`science_hypothesis_generator.md`](science_hypothesis_generator.md) | Testable hypotheses with predictions and falsification criteria |
| [`science_literature_review_synthesizer.md`](science_literature_review_synthesizer.md) | Extract methods, findings, contradictions, gaps across supplied papers |

> The three Phase 1 prompts predate the current structural floor (they lack the Required-inputs / verification-checklist / false-positive-matrix sections). They are functionally sound and were relocated here when Phase 2A shipped; a future pass may upgrade them to the floor.

## Floor (per [`../README.md`](../README.md))

Every Phase 2A prompt:
- requires the user to state discipline + study type
- forbids fabricated citations, DOIs, datasets, effect sizes, prior-study parameters, and instrument/vendor specs (gaps marked `[user-supplied]`)
- locks the output format (tables / structured sections)
- names the relevant reporting standard explicitly (OSF prereg, Registered Reports, CONSORT, STROBE, PRISMA, ARRIVE 2.0, STARD, SPIRIT, TRIPOD, COREQ/SRQR, FAIR, Cook & Campbell)
- preserves the pre-specified vs exploratory distinction wherever analysis or interpretation is touched
- defaults to the Open Science branch; names closed-data handling as the non-default exception
- ends with a verification checklist + false-positive matrix

See [`../EXPANSION_ROADMAP.md`](../EXPANSION_ROADMAP.md) for the remaining phases (2B–2L) and the build order.
