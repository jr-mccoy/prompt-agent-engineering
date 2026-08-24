# Domain-Science Expansion Roadmap

**Status as of 2026-06-26:** Phase 1 (3 prompts, originally authored in `domain-specialized-fields/science/`) migrated to top-level `domain-science/` and **relocated into `methods-foundations/`**. **Phase 2J shipped (24 prompts across 6 discipline sub-clusters).** **Phase 2A shipped (14 prompts in `methods-foundations/`).** **Phase 2D shipped (12 prompts in `statistics/`).** **Phase 2E shipped (14 prompts in `writing-communication/`).** **Phase 2H shipped (8 prompts in `ethics-integrity/`).** **Phase 2C shipped (14 prompts in `computational/`).** **Phase 2B shipped (12 prompts in `bench-and-wetlab/`).** **Phase 2F shipped (6 prompts in `peer-review/`).** **Phase 2G shipped (10 prompts in `grants-funding/`).** **Phase 2I shipped (10 prompts in `lab-operations-mentorship/`).** **Phase 2K shipped (8 prompts in `public-engagement/`).** **Phase 2L shipped (6 prompts in `teaching-research-methods/`).** ✅ **The Phase 2 roadmap is fully built — all 12 subdirectories shipped (141 prompts total).**

**Filing convention:** `science_{specific_function}.md` inside the relevant subdirectory. **All prompts follow the floor specified in [`README.md`](README.md):** required discipline + study-type inputs, no-fabrication clause, locked output format, reporting-standard alignment where applicable, pre-specification bias, verification checklist, false-positive matrix, calibrated uncertainty, Open Science default.

**Scope discipline.** This roadmap is intentionally finite. Prompts that would duplicate `domain-research-academic/`, `domain-healthcare-clinical/`, `domain-education-teaching/`, or `domain-software-engineering/` are excluded; the boundary table in `README.md` is the authoritative split. Where a prompt sits at a boundary, the rule is: scientific judgment specific to bench / field / instrument / discipline lives here.

---

## Phase 1 — Shipped (3 prompts, at directory root)

| File | Description |
|---|---|
| `science_experimental_design_advisor.md` | Designs under stated constraints; controls, randomization, power, confounds |
| `science_hypothesis_generator.md` | Testable hypotheses with predictions and falsification criteria |
| `science_literature_review_synthesizer.md` | Extract methods, findings, contradictions, gaps across supplied papers |

**✓ Relocated 2026-06-26:** these three moved into `methods-foundations/` when Phase 2A shipped; all `related_prompts` references in the `disciplines/` tree and `README.md` were rewritten to the new paths. (`PROMPT_INDEX.json` / `PROMPT_INDEX.md` do not yet index `domain-science/` at all — neither Phase 1, 2A, nor 2J — so no index entries needed updating; a future pass should index the whole domain.)

---

## Phase 2 — Planned subdirectories and prompts

The ordering below reflects build priority. Phase 2A is the foundation everything else composes on; 2B–2D cover execution and analysis; 2E–2G cover dissemination and resourcing; 2H–2K cover the surrounding professional context.

### Phase 2A — Methods & Research-Lifecycle Foundations (`methods-foundations/`, 14 prompts) — ✓ COMPLETE (shipped 2026-06-26)

The reusable scientific-methodology layer that the discipline-specific phases build on. Aligned to NIH Rigor & Reproducibility, OSF preregistration, Registered Reports, and Cook & Campbell threats-to-validity. **All 14 prompts shipped 2026-06-26**, plus the 3 relocated Phase 1 prompts. See [`methods-foundations/README.md`](methods-foundations/README.md).

| File | Description |
|---|---|
| `science_research_question_refiner.md` | Convert vague curiosity into a specific, testable, scoped question with feasibility check |
| `science_preregistration_drafter.md` | OSF-style preregistration with hypotheses, design, analysis plan, deviations clause |
| `science_registered_report_stage1_drafter.md` | Stage-1 Registered Report draft: introduction, methods, analysis, sampling plan, pilot data |
| `science_power_and_sample_size_calculator.md` | Frequentist and Bayesian power options, with assumptions surfaced and sensitivity analysis |
| `science_pilot_study_designer.md` | Pilot design to derisk a full study: what the pilot can and cannot tell you |
| `science_negative_and_positive_control_designer.md` | Sham, vehicle, positive, negative controls — selection logic per design |
| `science_blinding_and_randomization_protocol.md` | Allocation, sequence generation, blinding levels, breakdown contingencies |
| `science_confound_and_bias_audit.md` | Systematic threats to internal, external, construct, and statistical conclusion validity |
| `science_replicability_premortem.md` | Pre-publication audit: what would cause a direct replication to fail? |
| `science_reproducibility_self_audit.md` | FAIR-aligned self-audit: data, code, environment, documentation |
| `science_methodology_decision_tree.md` | When to use RCT vs. quasi-experiment vs. observational vs. simulation, with assumptions |
| `science_methods_section_drafter.md` | IMRaD-aligned methods section with reporting-standard-specific checklists |
| `science_threats_to_validity_walkthrough.md` | Cook-Campbell four-validity audit applied to a specific design |
| `science_qualitative_vs_quantitative_decision.md` | Match the methodology to the question; surfaces mixed-methods options |

### Phase 2B — Bench / Wet Lab Practice (`bench-and-wetlab/`, 12 prompts) — ✓ COMPLETE (shipped 2026-06-26)

For experimental scientists running protocols at the bench or in the field. Aligned to ARRIVE 2.0 (animal), STAR Methods (general), ALCOA+ data integrity, and standard biosafety/IBC norms. **All 12 prompts shipped 2026-06-26.** The IACUC / IRB / biosafety prompts draft and route to the empowered committee — they never grant approval; the biosafety prompt is governance/containment-level only (no operational uplift) and points dual-use concerns to `ethics-integrity/science_dual_use_research_assessment.md`. See [`bench-and-wetlab/README.md`](bench-and-wetlab/README.md).

| File | Description |
|---|---|
| `science_lab_protocol_drafter.md` | Step-by-step protocol with reagents, equipment, hazards, controls, expected outcomes |
| `science_lab_protocol_optimizer.md` | Troubleshooting walk for a failed protocol: 5-Whys against likely failure modes |
| `science_reagent_and_supply_calculator.md` | Molarity, dilutions, serial dilutions, stock prep with unit-checking |
| `science_buffer_recipe_designer.md` | Buffer selection by pH, ionic strength, compatibility with downstream assay |
| `science_cell_culture_protocol_designer.md` | Line-specific media, passaging, mycoplasma testing, authentication (NIH guidance) |
| `science_animal_protocol_iacuc_drafter.md` | IACUC protocol aligned to ARRIVE 2.0; 3Rs justification, endpoints, statistical justification |
| `science_human_subjects_irb_protocol_drafter.md` | IRB protocol with risk-benefit, consent, data security, vulnerable-population handling |
| `science_sample_logging_chain_of_custody_designer.md` | Sample ID schema, freezer location, ELN linking, retention/destruction policy |
| `science_failed_experiment_post_mortem.md` | Structured post-mortem distinguishing bad luck, bad protocol, bad question |
| `science_lab_notebook_entry_writer.md` | ELN-compatible entry: hypothesis, method, observations, interpretation, next step |
| `science_reagent_validation_workflow.md` | Antibody validation, primer specificity, cell-line authentication |
| `science_biosafety_risk_assessment.md` | BSL/ABSL determination, dual-use review, IBC submission scaffold |

### Phase 2C — Computational & Dry Lab (`computational/`, 14 prompts) — ✓ COMPLETE (shipped 2026-06-26)

For computational scientists, bioinformaticians, simulation researchers, and ML-for-science practitioners. Aligned to The Turing Way, rOpenSci packaging, FAIR / FAIR4RS principles, ASME V&V, and the ML-for-science leakage/pitfalls literature (Kapoor–Narayanan, REFORMS). **All 14 prompts shipped 2026-06-26.** `science_open_source_research_software_repo_layout.md` is the bridge to `domain-software-engineering/`. See [`computational/README.md`](computational/README.md).

| File | Description |
|---|---|
| `science_bioinformatics_pipeline_designer.md` | Pipeline architecture with QC gates, version pinning, containerization, test data |
| `science_genomics_qc_protocol.md` | Per-stage QC: read-level, alignment, variant, sample-level; thresholds and remediation |
| `science_single_cell_analysis_plan.md` | scRNA-seq plan: QC, normalization, batch, clustering, annotation, validation |
| `science_proteomics_analysis_plan.md` | DDA / DIA workflow, FDR control, missing-data strategy, post-translational handling |
| `science_simulation_validation_protocol.md` | MD / FEM / CFD / ABM validation: convergence, V&V, sensitivity, ground-truth comparison |
| `science_numerical_convergence_audit.md` | Grid / time-step / mesh refinement study with quantitative convergence criteria |
| `science_computational_reproducibility_environment.md` | Docker / Nix / renv / conda-lock + CI to make a study computationally reproducible |
| `science_data_management_plan_drafter.md` | NIH / NSF / Wellcome / ERC DMP aligned to DMPTool prompts; storage, sharing, preservation |
| `science_data_dictionary_designer.md` | Variable-level dictionary with units, allowed values, missingness codes, provenance |
| `science_metadata_schema_builder.md` | Discipline-appropriate schema (MIBBI family, Dublin Core, schema.org) with mapping |
| `science_synthetic_data_generator_design.md` | Surrogate data preserving structure for sharing or testing without disclosure risk |
| `science_ml_for_science_validation_audit.md` | Audit for data leakage, label leakage, distribution shift, evaluation-set contamination |
| `science_ml_for_science_benchmark_design.md` | Benchmark with held-out distribution, calibrated baselines, ablations, error analysis |
| `science_open_source_research_software_repo_layout.md` | rOpenSci-aligned layout: tests, CI, docs, citation file, release tags, archive (Zenodo) |

### Phase 2D — Statistical Analysis & Interpretation (`statistics/`, 12 prompts) — ✓ COMPLETE (shipped 2026-06-26)

Aligned to ASA statement on p-values, transparent reporting, and pre-specified analysis culture. **All 12 prompts shipped 2026-06-26.** See [`statistics/README.md`](statistics/README.md).

| File | Description |
|---|---|
| `science_statistical_test_selector.md` | Match test to design / distribution / hypothesis; surface assumption checks |
| `science_effect_size_and_uncertainty_reporter.md` | Effect sizes with appropriate intervals; reporting style for the target journal |
| `science_multiple_comparisons_strategy.md` | FDR vs. FWER vs. hierarchical decisions, with cost-of-error framing |
| `science_pre_specified_analysis_plan.md` | Lock the primary, secondary, and exploratory analyses before data lock |
| `science_bayesian_analysis_plan.md` | Prior selection, sensitivity analysis, decision rules, posterior summaries |
| `science_mixed_models_design.md` | Fixed vs. random effects, nested vs. crossed, singularity diagnosis, REML/ML choice |
| `science_survival_analysis_design.md` | Censoring handling, proportional-hazards assessment, competing risks |
| `science_causal_inference_design.md` | DAG, identification strategy, instruments / regression discontinuity / DiD selection |
| `science_meta_analysis_protocol.md` | PRISMA-aligned meta-analysis: search, screen, extract, synthesize, bias, sensitivity |
| `science_statistical_results_interpreter.md` | Calibrated interpretation: avoid p-only spin, surface what is and is not supported |
| `science_outlier_handling_decision.md` | Pre-specified outlier rules with rationale; document robustness checks |
| `science_p_hacking_self_check.md` | Garden-of-forking-paths audit: how many degrees of freedom were taken? |

### Phase 2E — Scientific Writing & Communication (`writing-communication/`, 14 prompts) — ✓ COMPLETE (shipped 2026-06-26)

For producing manuscripts, abstracts, figures, and lay summaries. Format-locked, no rhetorical inflation, fully aligned to target-journal norms when the journal is supplied. **All 14 prompts shipped 2026-06-26.** See [`writing-communication/README.md`](writing-communication/README.md).

| File | Description |
|---|---|
| `science_imrad_paper_drafter.md` | Skeleton-first IMRaD draft from results + key claims; structural critique afterward |
| `science_abstract_compressor.md` | Structured or unstructured abstract calibrated to discipline conventions and word limits |
| `science_journal_target_selector.md` | Match manuscript to candidate journals on scope, audience, OA policy, decision time |
| `science_cover_letter_to_editor.md` | Cover letter with significance framing, scope fit, suggested handling editors |
| `science_response_to_reviewers.md` | Point-by-point response with traceable changes; distinguishes acceded vs. argued |
| `science_appeal_to_editor_after_rejection.md` | Appeal letter — when warranted vs. when not; tone and evidence calibration |
| `science_figure_first_paper_skeleton.md` | Figure-first outlining: lock figures, then results, then discussion |
| `science_figure_legend_drafter.md` | Self-contained legend; species/sample-size/statistics/scale-bar/error-bar conventions |
| `science_figure_design_critique.md` | Color-blind safety, chart-junk audit, encoding choices, accessibility |
| `science_table_design_critique.md` | Significant-figure discipline, units, missingness convention, footnote economy |
| `science_conference_abstract_drafter.md` | Oral / poster abstract with submission-portal-aware structure |
| `science_poster_designer.md` | Three-zone print poster: question-method-finding scan path; hand-off to image-gen domain |
| `science_preprint_release_plan.md` | Server selection (bioRxiv / arXiv / SSRN / ChemRxiv / EarthArXiv), license, versioning |
| `science_lay_summary_translator.md` | Plain-language summary calibrated to a stated audience without overclaiming |

### Phase 2F — Peer Review (`peer-review/`, 6 prompts) — ✓ COMPLETE (shipped 2026-06-26)

For scientists serving as reviewers and editors. Aligned to COPE peer-review guidance. **All 6 prompts shipped 2026-06-26.** Every criticism is evidence-based and located; honest error is assumed over misconduct (suspected misconduct routes via `ethics-integrity/`, not accused). See [`peer-review/README.md`](peer-review/README.md).

| File | Description |
|---|---|
| `science_peer_review_drafter.md` | Structured review: summary, strengths, major concerns, minor concerns, recommendation |
| `science_peer_review_self_check.md` | Bias and scope audit before submitting; evidentiary basis for each criticism |
| `science_editorial_decision_drafter.md` | Decision letter synthesizing reviewer disagreement with editor's own assessment |
| `science_review_disagreement_arbitration_memo.md` | Third-reviewer or AE memo when two reviewers strongly disagree |
| `science_post_publication_critique_drafter.md` | PubPeer-style critique with evidence, calibration, no ad hominem |
| `science_review_for_replication_or_robustness.md` | Specialized review lens for replication studies and robustness audits |

### Phase 2G — Funding & Grants (`grants-funding/`, 10 prompts) — ✓ COMPLETE (shipped 2026-06-26)

Aligned to NIH, NSF, ERC, Wellcome, and major foundation conventions. Each prompt asks for the specific program before drafting and drafts from the user's own science — never inventing preliminary data, impact figures, collaborators, costs, or funder-specific rules (all `[user-supplied]`/verify). **All 10 prompts shipped 2026-06-26.** See [`grants-funding/README.md`](grants-funding/README.md).

| File | Description |
|---|---|
| `science_specific_aims_drafter.md` | NIH-style one-page Specific Aims with significance, premise, aims, payoff |
| `science_nih_r01_outline_drafter.md` | R01 outline: Significance, Innovation, Approach with rigor/reproducibility blocks |
| `science_nsf_proposal_outliner.md` | NSF heuristics: Intellectual Merit + Broader Impacts woven through, not bolted on |
| `science_erc_grant_outliner.md` | ERC Starting / Consolidator / Advanced — high-risk-high-gain framing, PI scientific identity |
| `science_grant_significance_section_drafter.md` | Significance with gap framing and quantitative impact rationale |
| `science_grant_innovation_section_drafter.md` | Innovation framed against the state of the art with specific delta claims |
| `science_grant_approach_section_drafter.md` | Approach with timelines, milestones, pitfalls + alternatives, rigor language |
| `science_grant_resubmission_response.md` | Response-to-summary-statement with revisions traced and crosswalked |
| `science_grant_budget_justification_drafter.md` | Budget justification by category with effort allocation rationale |
| `science_letter_of_support_drafter.md` | Collaborator / chair / institutional letters with specific commitments, not boilerplate |

### Phase 2H — Research Ethics & Integrity (`ethics-integrity/`, 8 prompts) — ✓ COMPLETE (shipped 2026-06-26)

Aligned to ICMJE, CRediT, WHO research-ethics guidance, and the dual-use research framework. **All 8 prompts shipped 2026-06-26.** Convention: these prompts structure / disclose / self-audit and route formal matters to the institution / IBC / DURC committee / editor / COPE — they never adjudicate. The dual-use prompt is governance-level only (no operational detail). See [`ethics-integrity/README.md`](ethics-integrity/README.md).

| File | Description |
|---|---|
| `science_authorship_and_credit_resolver.md` | CRediT-taxonomy walkthrough resolving disputed contribution assignments |
| `science_conflict_of_interest_disclosure_drafter.md` | COI disclosure for manuscript, grant, IRB; financial and non-financial |
| `science_dual_use_research_assessment.md` | DURC self-screen against community-of-concern criteria; mitigation options |
| `science_responsible_ai_use_in_research_audit.md` | LLM-in-research disclosure; what is and is not acceptable per current consensus |
| `science_misconduct_self_audit.md` | Pre-submission self-audit for fabrication / falsification / plagiarism risk |
| `science_image_integrity_self_check.md` | Western blot / microscopy / gel-image integrity audit against community norms |
| `science_retraction_or_correction_decision_walkthrough.md` | When error becomes retraction; correction-letter vs. retraction-notice path |
| `science_open_science_practices_self_audit.md` | FAIR / CARE / TRUST audit before submission and at study close |

### Phase 2I — Lab Operations & Mentorship (`lab-operations-mentorship/`, 10 prompts) — ✓ COMPLETE (shipped 2026-06-26)

For PIs and senior postdocs managing groups, trainees, and timelines. Trainee dignity + psychological safety are first-class; well-being concerns route to professional support (not clinical tools). **All 10 prompts shipped 2026-06-26.** See [`lab-operations-mentorship/README.md`](lab-operations-mentorship/README.md).

| File | Description |
|---|---|
| `science_individual_development_plan_drafter.md` | NIH-style IDP for a trainee; skills, milestones, career options, advisor compact |
| `science_lab_meeting_agenda_designer.md` | Rotating lab meeting that surfaces stuck projects without humiliating trainees |
| `science_one_on_one_mentorship_session_plan.md` | Structured 1:1 with research, career, and well-being checkpoints |
| `science_lab_onboarding_packet_designer.md` | New-trainee packet: safety, software, conventions, expectations, mentoring compact |
| `science_thesis_committee_meeting_prep.md` | Pre-committee prep document for the student; chair, advisor, and external roles |
| `science_qualifying_exam_question_bank.md` | Field-specific qual question bank with model answers and grading rubric |
| `science_postdoc_to_pi_transition_plan.md` | Independent-research statement, startup negotiation, lab-launch operations |
| `science_lab_culture_charter.md` | Norms on attribution, hours, conflict, mental health, mistake disclosure |
| `science_undergraduate_research_mentoring_plan.md` | Semester / summer plan with appropriate scaffolding and ownership |
| `science_research_internship_project_scope.md` | 8–12 week project with realistic outputs and a clear what-success-looks-like |

### Phase 2J — Discipline-Specific Modules (`disciplines/`, 24 prompts across 6 sub-subdirectories) — ✓ COMPLETE (shipped 2026-05-19)

Selective: only where a discipline-specific prompt would differ materially from the general-purpose Phase 2A–D prompts. **All 24 prompts shipped 2026-05-19.** See [`disciplines/README.md`](disciplines/README.md) for the cluster map.

#### `disciplines/biology/` (5)
- `bio_genomics_study_design.md` — power, multiple testing, ancestry, batch
- `bio_microscopy_experiment_design.md` — modality choice, controls, sampling, quantification
- `bio_clinical_trial_protocol_outliner.md` — CONSORT/SPIRIT-aligned protocol scaffold
- `bio_omics_study_metadata_planner.md` — MIxS / MIAME-aligned metadata up front
- `bio_field_ecology_study_designer.md` — replication units, pseudo-replication, BACI designs

#### `disciplines/chemistry/` (4)
- `chem_synthesis_route_critique.md` — retrosynthesis review with green-chemistry lens
- `chem_characterization_battery_designer.md` — NMR / MS / IR / XRD / EA per compound class
- `chem_reaction_kinetics_experimental_designer.md` — order, rate-law, temperature, fit strategy
- `chem_computational_chemistry_validation_protocol.md` — method/basis/benchmarking discipline

#### `disciplines/physics-astronomy/` (4)
- `physics_observable_and_measurement_chain_designer.md` — from signal to publishable claim
- `physics_systematic_uncertainty_budget_drafter.md` — itemized systematics with propagation
- `astro_observing_proposal_drafter.md` — telescope-time proposal: target, exposure, cadence
- `astro_data_reduction_pipeline_protocol.md` — calibration, reduction, validation, archiving

#### `disciplines/earth-climate/` (4)
- `earth_field_campaign_designer.md` — siting, sensor placement, calibration, sampling strategy
- `climate_model_intercomparison_plan.md` — ensemble selection, baseline, signal-to-noise
- `earth_remote_sensing_validation_plan.md` — ground-truth, scale, retrieval-error budget |
- `earth_geochronology_age_model_designer.md` — sample selection, dating methods, uncertainty

#### `disciplines/neuroscience/` (4)
- `neuro_animal_behavior_experiment_designer.md` — counterbalancing, habituation, blinding |
- `neuro_imaging_analysis_plan.md` — fMRI / EEG / MEG preregistered pipeline |
- `neuro_electrophysiology_protocol_designer.md` — recording config, controls, artifact rejection |
- `neuro_circuit_perturbation_experiment_designer.md` — optogenetic / chemogenetic / lesion logic

#### `disciplines/materials-engineering/` (3)
- `materials_synthesis_and_characterization_plan.md` — synthesis → characterization → property mapping |
- `materials_failure_analysis_protocol.md` — failure-mode investigation: visual → fractography → root cause |
- `materials_doe_plan.md` — design of experiments (factorial, RSM, Taguchi) for materials process

### Phase 2K — Public Engagement & Science Communication (`public-engagement/`, 8 prompts) — ✓ COMPLETE (shipped 2026-06-26)

For scientists communicating beyond academic peers. Core theme: overclaim avoidance — calibrated certainty, primary-source links, no fabricated findings, fair representation of others' views, inoculation-based misinformation response. **All 8 prompts shipped 2026-06-26.** See [`public-engagement/README.md`](public-engagement/README.md).

| File | Description |
|---|---|
| `science_press_release_drafter.md` | Institutional press release calibrated against overclaim risk |
| `science_media_interview_prep.md` | Q&A bank with bridge phrases, traps, and visual-language alternatives |
| `science_op_ed_drafter.md` | Op-ed translating a finding into a policy-relevant claim with clear evidence chain |
| `science_policy_brief_drafter.md` | 2-page brief for a non-scientist policymaker; options not advocacy |
| `science_congressional_or_parliamentary_testimony_prep.md` | Testimony with five-minute opening + Q&A bank for a hostile jurisdiction |
| `science_social_media_thread_drafter.md` | Thread with calibrated certainty, primary-source links, and overclaim-avoidance |
| `science_explainer_for_general_audience.md` | Explainer that builds intuition without metaphor-induced false confidence |
| `science_misinformation_response_drafter.md` | Response to public misinformation, applying inoculation principles |

### Phase 2L — Teaching Lab & Research-Method Skills (`teaching-research-methods/`, 6 prompts) — ✓ COMPLETE (shipped 2026-06-26)

For scientists who also teach research practice — distinct from the K-12/HE pedagogy in `domain-education-teaching/` because the subject matter is research craft itself. **All 6 prompts shipped 2026-06-26 — completing the Phase 2 roadmap.** See [`teaching-research-methods/README.md`](teaching-research-methods/README.md).

| File | Description |
|---|---|
| `science_undergraduate_lab_course_designer.md` | Authentic-research lab course: open question, real measurement, calibrated rubric |
| `science_research_methods_syllabus_designer.md` | Semester research-methods syllabus aligned to discipline + Open Science |
| `science_journal_club_facilitation_guide.md` | Paper selection, pre-read questions, in-room facilitation, follow-up |
| `science_code_review_for_science_software.md` | Science-specific code review: correctness, reproducibility, numerical stability |
| `science_data_analysis_workshop_designer.md` | Carpentries-style hands-on workshop with assessment and post-workshop scaffolding |
| `science_reproducibility_workshop_designer.md` | One-day workshop converting a paper into a fully reproducible artifact |

---

## Totals and sequencing

| Phase | Subdirectory | Count |
|---|---|---|
| 1 (shipped, relocated into 2A) | `methods-foundations/` | 3 |
| 2A ✓ | `methods-foundations/` | 14 |
| 2B ✓ | `bench-and-wetlab/` | 12 |
| 2C ✓ | `computational/` | 14 |
| 2D ✓ | `statistics/` | 12 |
| 2E ✓ | `writing-communication/` | 14 |
| 2F ✓ | `peer-review/` | 6 |
| 2G ✓ | `grants-funding/` | 10 |
| 2H ✓ | `ethics-integrity/` | 8 |
| 2I ✓ | `lab-operations-mentorship/` | 10 |
| 2J ✓ | `disciplines/` (6 sub-subdirs) | 24 |
| 2K ✓ | `public-engagement/` | 8 |
| 2L ✓ | `teaching-research-methods/` | 6 |
| **Total planned (Phase 1 + 2)** | | **141** |

**Recommended build order:** 2A → 2D → 2E → 2H → 2C → 2B → 2F → 2G → 2I → 2J → 2K → 2L. Rationale: methods, statistics, writing, and integrity together cover the highest-frequency working-scientist needs; computational and bench come next; the remaining phases address specialized contexts and roles.

---

## Cross-cutting conventions for every Phase 2 prompt

1. **First input always asks for discipline + study type.** No discipline-agnostic outputs where discipline matters.
2. **No invented citations, vendor catalog numbers, instrument specs, grant program names, or DOIs.** If the user does not supply, the prompt either asks or marks `[user-supplied]`.
3. **Reporting-standard alignment.** Where a community standard exists, the prompt cites it by name in the instruction body. (CONSORT, STROBE, PRISMA, ARRIVE 2.0, SPIRIT, STARD, COREQ, SQUIRE, CHEERS, TRIPOD, MIBBI family, STAR Methods, FAIR, CARE, TRUST, CRediT.)
4. **Pre-specification vs. exploratory distinction is preserved.** Any prompt producing or modifying an analysis plan, results section, or interpretation flags which claims are pre-specified.
5. **Calibrated language defaults.** Drafted text avoids "novel," "groundbreaking," "first-ever," "the gold standard"; substitutes specific, falsifiable claims.
6. **Open Science is the default branch.** Closed-data / proprietary-instrument / IP-restricted paths are accommodated but explicitly named as the non-default branch.
7. **Reviewer / editor / IRB / IACUC / IBC / funder framing.** Where output will be read by a gatekeeper, the prompt names that audience and shapes the output to their evaluation criteria, not generic prose.
8. **Verification checklist + false-positive matrix at the bottom of every prompt.**

---

## Open Science source standards relied on

Listed in `README.md` under "Reputable open resources." Each Phase 2 prompt will cite the specific standard(s) it aligns to in its instruction body so users can verify directly against the source.

---

## Open questions for the maintainer

These are deferred decisions that should be made before Phase 2 build begins:

1. **`disciplines/` subdirectory scope.** The current plan covers six disciplinary clusters (biology, chemistry, physics-astronomy, earth-climate, neuroscience, materials-engineering). Should we add **psychology / cognitive science**? (Possible overlap with `domain-psychology/` and `domain-research-academic/`.) **Should we add social-science quantitative methods**, or leave that to `domain-research-academic/`?
2. **Clinical trials.** Where do CONSORT / SPIRIT clinical-trial protocol prompts live — here in `disciplines/biology/` or in `domain-healthcare-clinical/`? Recommendation: trial-design **methodology** here; clinical-practice-side trial **execution** in healthcare-clinical.
3. **Lab software.** Computational-research software craft is in scope here; general-purpose code quality is `domain-software-engineering/`. The proposed `science_open_source_research_software_repo_layout.md` is the planned bridge. Confirm this is the only cross-domain prompt needed, vs. building a small `disciplines/research-software-engineering/` set.
4. **AI/ML-for-science weight.** Phase 2C has two ML-for-science prompts and Phase 2H has one responsible-AI-use prompt. Given the rate of change in this area, should there be a dedicated `ml-for-science/` subdirectory (~6 prompts) instead? Recommendation: defer until after 2A–2D ship, then re-scope based on observed usage.
5. **CLAUDE.md update.** ✓ **Done 2026-06-26 (when Phase 2A shipped).** Root `CLAUDE.md` now lists `domain-science/` in both the Category Mapping section (a "Science" block after "Research & Academic," with the boundary note vs `domain-research-academic/`) and the Quick Reference table. Update these again as later phases (2B–2L) ship.
