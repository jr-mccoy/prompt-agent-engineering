# Toolkit Crosswalk — Library Drill ↔ Clinical Source of Truth

**The boundary made concrete.** This library authors the **learner's side** (drills, primers, rehearsals, self-assessment, the progression spine). It does **not** re-state clinical content — doses, thresholds, complication scaffolds, drug monographs, population specifics, curriculum design, and the preceptor's evaluation lifecycle all live in the **educator toolkit** (`domain-healthcare-clinical/prompts/perianesthesia/`) or in the **nursing seed prompts** (`domain-healthcare-clinical/prompts/nursing/`). This document is the single map from each learner prompt to the artifact that supplies its clinical facts.

> **Non-auto-resolving.** These are **documented cross-references**, not live/auto-resolving links (per `BUILD_PLAN.md` §4a). The toolkit is deliberately standalone and portable; nothing here creates a runtime dependency. A learner follows a path by hand, or pastes the relevant facility/toolkit material into the drill.
>
> **The rule this enforces (`BUILD_PLAN.md` §1):** *if a clinical fact, dose, threshold, complication scaffold, or drug monograph is needed by a learner drill, the drill points here* — it does not restate clinical content. One source of truth; low authoring cost; no drift.

**Path conventions in this file:**
- `toolkit:` → `domain-healthcare-clinical/prompts/perianesthesia/clinical-and-educator/<file>.md` (or `domain-agentic-resources/skills/non-coding/healthcare/<dir>/` for skills)
- `seed:` → `domain-healthcare-clinical/prompts/nursing/<file>.md`
- `(pending W4)` → a toolkit **Wave-4** artifact planned but not yet built; per `BUILD_PLAN.md` §7 option (b) the library drill points at the `pacu_complication_deep_dive` generator (or the relevant baked complication file) until it ships, then the link upgrades. No blocking.

---

## Seed-prompt anchors (the Stage-1 backbone)

The 10 nursing seed prompts are **adopted by reference**, never moved (other repo routing points at them — `BUILD_PLAN.md` §9.5). The library's reference-bridge prompts adapt them for learner self-operation.

| Seed prompt (`seed:`) | Library prompt(s) that anchor on it |
|---|---|
| `nursing_pacu_shift_structure.md` | `stage-1-orientation/pacu_orient_shift_structure_card.md` |
| `nursing_pacu_prioritization_rule.md` | `stage-1-orientation/pacu_orient_prioritization_rule_drill.md` · `stage-2-independence/pacu_indep_two_patient_prioritization_stress_drill.md` |
| `nursing_orientee_pattern_import_check.md` | `stage-1-orientation/pacu_orient_pattern_import_check.md` |
| `nursing_sbar_clinical_escalation.md` | `stage-1-orientation/pacu_orient_outbound_sbar_report_rehearsal.md` · `stage-2-independence/pacu_indep_escalation_decision_drill.md` |
| `nursing_medication_administration_safety.md` | `stage-1-orientation/pacu_orient_medication_safety_selfcheck_drill.md` |
| `nursing_clinical_assessment_framework.md` | `stage-2-independence/pacu_indep_charting_under_load_rehearsal.md` |
| `nursing_preceptor_daily_debrief.md` | `stage-1-orientation/pacu_orient_daily_debrief_selfprep.md` |
| `nursing_preceptor_fumble_postmortem.md` | *(preceptor-side; mirrored by learner self-prep — no direct library anchor)* |
| `nursing_preceptor_independence_rubric.md` | *(preceptor-side; mirrored self-side by the Stage-2 readiness prompts)* |
| `nursing_quick_reference_handbook_creator_prompt.md` | *(analog of `stage-3-independent-practice/pacu_solo_personal_reference_builder.md`)* |

---

## Stage 0 — Foundations → clinical source

| Library prompt | Clinical source of truth |
|---|---|
| `pacu_foundations_what_is_pacu.md` | toolkit: `pacu_orientation_first_day_packet` |
| `pacu_foundations_anesthesia_types_primer.md` | toolkit: `pacu_medication_profile` · `pacu_drug_*` reference set |
| `pacu_foundations_emergence_respiratory_physiology.md` | toolkit: `pacu_negative_pressure_pulmonary_edema` · `pacu_opioid_induced_respiratory_depression` |
| `pacu_foundations_anesthesia_pharmacology_map.md` | toolkit: `pacu_medication_profile` · `pacu_drug_analgesics_reference` · `pacu_drug_antiemetics_reference` · `pacu_drug_naloxone` · `pacu_drug_flumazenil` · `pacu_drug_neostigmine_glycopyrrolate` · `pacu_drug_sugammadex` · `pacu_drug_vasopressors_reference` (Drug Monograph Library) |
| `pacu_foundations_hemodynamics_of_emergence.md` | toolkit: `pacu_post_op_hypertension` · `pacu_dysrhythmia_recognition` |
| `pacu_foundations_pain_ponv_thermoreg_basics.md` | toolkit: `pacu_hypothermia_shivering` · `pacu_drug_antiemetics_reference` |
| `pacu_foundations_monitoring_and_scores_primer.md` | toolkit: `pacu_competency_self_assessment` · `pacu_aldrete_padss_scoring_explainer` (pending W4) |
| `pacu_foundations_vocabulary_acronym_builder.md` | toolkit: `pacu_topic_primer` |
| `pacu_foundations_week1_expectations_map.md` | toolkit: `pacu_orientation_first_week_plan` |
| `pacu_foundations_pre_reading_planner.md` | toolkit: `pacu_orientee_topic_self_study_planner` |
| `pacu_foundations_transfer_from_prior_unit_bridge.md` | toolkit: `pacu_background_specific_pathway_adapter` |
| `pacu_foundations_starter_concept_map.md` | toolkit: `pacu_topic_primer` |

## Stage 1 — Orientation → clinical source

| Library prompt | Clinical source of truth |
|---|---|
| `pacu_orient_shift_structure_card.md` | seed: `nursing_pacu_shift_structure` |
| `pacu_orient_prioritization_rule_drill.md` | seed: `nursing_pacu_prioritization_rule` |
| `pacu_orient_inbound_handoff_receiving_rehearsal.md` | toolkit: `pacu_handoff_script` |
| `pacu_orient_outbound_sbar_report_rehearsal.md` | seed: `nursing_sbar_clinical_escalation` · toolkit: `pacu_handoff_script` |
| `pacu_orient_recovery_one_liner_drill.md` | toolkit: `pacu_handoff_script` |
| `pacu_orient_normal_vs_deviation_drill.md` | toolkit: `pacu_red_flag_card` · Complication Library (`pacu_complication_deep_dive`) |
| `pacu_orient_recovery_deviation_script_builder.md` | toolkit: `pacu_complication_deep_dive` (+ baked complication files: `pacu_bronchospasm`, `pacu_aspiration`, `pacu_delayed_emergence`, etc.) |
| `pacu_orient_ngn_clinical_judgment_drill.md` | toolkit: `pacu_unfolding_case_study` |
| `pacu_orient_respiratory_event_recognition_drill.md` | toolkit: `pacu_bronchospasm` · `pacu_negative_pressure_pulmonary_edema` · `pacu_opioid_induced_respiratory_depression` |
| `pacu_orient_hemodynamic_event_recognition_drill.md` | toolkit: `pacu_post_op_hypertension` · `pacu_dysrhythmia_recognition` · `pacu_drug_vasopressors_reference` |
| `pacu_orient_abg_in_recovery_drill.md` *(scope banner)* | toolkit: `pacu_opioid_induced_respiratory_depression` · clinical substrate: `domain-healthcare-clinical/prompts/interpretation/interp_abg_acid_base.md` (nurse-scoped) |
| `pacu_orient_rhythm_recognition_drill.md` *(scope banner)* | toolkit: `pacu_dysrhythmia_recognition` · clinical substrate: `interpretation/interp_ecg_full_interpretation.md` (nurse-scoped) |
| `pacu_orient_aldrete_padss_scoring_practice.md` | toolkit: `pacu_aldrete_score_visual_meta` · `pacu_aldrete_padss_scoring_explainer` (pending W4) |
| `pacu_orient_medication_safety_selfcheck_drill.md` | seed: `nursing_medication_administration_safety` · Drug Monograph Library |
| `pacu_orient_pattern_import_check.md` | seed: `nursing_orientee_pattern_import_check` · toolkit: `pacu_background_specific_pathway_adapter` |
| `pacu_orient_reflective_journal.md` | toolkit: `pacu_orientee_reflective_journal_prompts` |
| `pacu_orient_question_log_and_spaced_review.md` | toolkit: `pacu_orientee_question_log_builder` |
| `pacu_orient_daily_debrief_selfprep.md` | seed: `nursing_preceptor_daily_debrief` · toolkit: `pacu_preceptor_debrief` |

## Stage 2 — Independence → clinical source

| Library prompt | Clinical source of truth |
|---|---|
| `pacu_indep_run_bay_solo_simulation.md` | toolkit: `pacu_emergency_drill_designer` · `pacu_simulation_scenario_builder` |
| `pacu_indep_two_patient_prioritization_stress_drill.md` | seed: `nursing_pacu_prioritization_rule` |
| `pacu_indep_deteriorating_patient_walkthrough.md` | toolkit: `pacu_complication_deep_dive` · `pacu_last_recognition_response` |
| `pacu_indep_emergency_response_rehearsal_last.md` | toolkit: `pacu_last_recognition_response` |
| `pacu_indep_emergency_response_rehearsal_airway.md` | toolkit: `pacu_negative_pressure_pulmonary_edema` · `pacu_bronchospasm` · `pacu_airway_management_teaching` (pending W4) |
| `pacu_indep_emergency_response_rehearsal_oird.md` | toolkit: `pacu_opioid_induced_respiratory_depression` · `pacu_drug_naloxone` |
| `pacu_indep_escalation_decision_drill.md` | seed: `nursing_sbar_clinical_escalation` · toolkit: `pacu_escalation_who_to_call_meta` |
| `pacu_indep_confidence_calibration_selfquiz.md` | toolkit: `pacu_competency_self_assessment` |
| `pacu_indep_signoff_readiness_self_capstone.md` | toolkit: `pacu_orientee_evaluation_meta_prompt` · `pacu_competency_self_assessment` |
| `pacu_indep_cueing_decay_self_tracker.md` | toolkit: `pacu_orientation_skill_acquisition_timeline` |
| `pacu_indep_charting_under_load_rehearsal.md` | seed: `nursing_clinical_assessment_framework` · clinical substrate: `workflow/doc_soap_note.md`, `doc_code_blue_rrt_note.md` |
| `pacu_indep_prep_for_signoff_conversation.md` | toolkit: `pacu_preceptor_approach_guide` · `pacu_competency_self_assessment` |

## Stage 3 — Independent Practice + Certification → clinical source

| Library prompt | Clinical source of truth |
|---|---|
| `pacu_solo_new_pattern_capture_log.md` | toolkit: `pacu_orientee_question_log_builder` |
| `pacu_solo_near_miss_good_catch_reflection.md` | toolkit: `pacu_simulation_debrief_facilitator` |
| `pacu_solo_personal_reference_builder.md` | toolkit skill: `pacu-quick-reference-author` · seed: `nursing_quick_reference_handbook_creator_prompt` |
| `pacu_solo_monthly_growth_review.md` | toolkit: `pacu_orientee_reflective_journal_prompts` |
| `pacu_cert_capa_cpan_readiness_bridge.md` | toolkit: `pacu_capa_cpan_blueprint_aligned_study_plan` · `pacu_capa_cpan_practice_question_generator` · `pacu_capa_cpan_test_strategy_coach` · `pacu_capa_cpan_final_week_review` · `pacu_capa_cpan_weak_area_diagnostic` |
| `pacu_cert_spaced_repetition_deck_builder.md` | toolkit skill: `pacu-flashcard-deck-builder` · toolkit: `pacu_quick_quiz_generator` |
| `pacu_cert_weak_area_self_diagnostic.md` | toolkit: `pacu_capa_cpan_weak_area_diagnostic` |
| `pacu_maint_annual_competency_refresh_planner.md` | toolkit: `pacu_orientation_simulation_calendar_designer` · `pacu_emergency_drill_designer` |

## Stage 4 — Growth & Advanced → clinical source

| Library prompt | Clinical source of truth |
|---|---|
| `pacu_adv_high_acuity_recovery_reasoning.md` | toolkit: `pacu_cardiac_recovery_considerations` · `pacu_complication_deep_dive` |
| `pacu_adv_difficult_airway_recovery.md` *(scope banner)* | toolkit: `pacu_negative_pressure_pulmonary_edema` · `pacu_airway_management_teaching` (pending W4) |
| `pacu_adv_malignant_hyperthermia_recognition.md` *(scope banner)* | toolkit: `pacu_complication_deep_dive` · `pacu_emergency_drill_designer` |
| `pacu_adv_hemodynamic_instability_reasoning.md` *(scope banner)* | toolkit: `pacu_drug_vasopressors_reference` · `pacu_cardiac_recovery_considerations` |
| `pacu_adv_regional_neuraxial_advanced.md` *(scope banner)* | toolkit: `pacu_complication_deep_dive` · `pacu_dermatome_block_level_meta` · `pacu_regional_neuraxial_assessment` (pending W4) |
| `pacu_adv_complex_population_mastery.md` | toolkit: `pacu_pediatric_considerations` · `pacu_geriatric_considerations` · `pacu_obstetric_considerations` · `pacu_bariatric_osa_considerations` · `pacu_cardiac_recovery_considerations` (Population-Specialty Library) |
| `pacu_adv_ambulatory_fast_track_mastery.md` | toolkit: `pacu_ambulatory_day_surgery_considerations` |
| `pacu_grow_becoming_preceptor_self_prep.md` | toolkit: `pacu_preceptor_approach_guide` · `pacu_preceptor_debrief` (the suite they will operate) |
| `pacu_grow_teaching_recovery_concept.md` | toolkit skill: `pacu-in-depth-explainer` · toolkit: `pacu_topic_primer` |
| `pacu_grow_debrief_junior_after_event.md` | toolkit: `pacu_simulation_debrief_facilitator` · `pacu_preceptor_debrief` |
| `pacu_grow_charge_resource_nurse_readiness.md` | toolkit: `pacu_orientation_curriculum_audit` · `pacu_preceptor_calibration_facilitator` |
| `pacu_grow_code_rrt_participation_growth.md` *(scope banner)* | toolkit: `pacu_emergency_drill_designer` · `pacu_last_recognition_response` |
| `pacu_grow_journal_club_participation.md` | toolkit: `pacu_orientation_journal_club_facilitator` |
| `pacu_grow_evidence_appraisal_for_practice.md` | — (epistemic; no toolkit xref — learner supplies real sources) |
| `pacu_grow_qi_project_starter.md` | — (routes to facility QI/governance; baseline numbers from facility data only) |
| `pacu_grow_professional_development_plan.md` | toolkit: `pacu_orientee_weekly_learning_plan` |

---

## Spine → source architecture

The three spine prompts and two maps are built from **education-design** donors (not clinical content), so they carry no toolkit clinical xref:

| Spine artifact | Design donor |
|---|---|
| `COMPETENCY_PROGRESSION_MAP.md` | `domain-education-teaching/program/curriculum-design/program_progression_map_designer.md` · `teaching_competency_framework_designer.md` · `teaching_milestone_alignment_designer.md` |
| `TOOLKIT_CROSSWALK.md` (this file) | toolkit's `pacu_aspan_competency_domain_crosswalk` concept |
| `spine/pacu_self_assessment_blueprint.md` | `teaching_assessment_blueprint_builder.md` · `teaching_competency_assessment_evidence_design.md` |
| `spine/pacu_growth_remediation_pathway.md` | `teaching_remediation_pathway_designer.md` |
| `spine/pacu_learning_objectives_by_stage.md` | `teaching_learning_objectives_writer_blooms.md` · `teaching_blooms_taxonomy_calibrator.md` |

---

## Pending upgrades (toolkit Wave 4)

Four `see_also_toolkit` targets are toolkit Wave-4 artifacts planned but not yet built. Per `BUILD_PLAN.md` §7 option (b), the affected library drills point at the `pacu_complication_deep_dive` generator (or a baked complication file) today and upgrade the link when the toolkit ships them — **no blocking**.

| Pending toolkit artifact | Library prompts awaiting the upgrade |
|---|---|
| `pacu_aldrete_padss_scoring_explainer` | `pacu_foundations_monitoring_and_scores_primer.md` · `pacu_orient_aldrete_padss_scoring_practice.md` |
| `pacu_airway_management_teaching` | `pacu_indep_emergency_response_rehearsal_airway.md` · `pacu_adv_difficult_airway_recovery.md` |
| `pacu_regional_neuraxial_assessment` | `pacu_adv_regional_neuraxial_advanced.md` |
| `pacu_aspan_competency_domain_crosswalk` | *(superseded by this file + `COMPETENCY_PROGRESSION_MAP.md`)* |

> A few library prompts reference toolkit `*_meta` visual/planning artifacts (`pacu_aldrete_score_visual_meta`, `pacu_dermatome_block_level_meta`, `pacu_escalation_who_to_call_meta`, `pacu_handoff_sbar_visual_meta`) named in `BUILD_PLAN.md` §6. Where a named meta-artifact is not present in the current toolkit build, treat it as a planned visual companion; the library drill stands alone until it lands (same non-blocking rule).

---

*Spine artifact — the boundary made concrete. When in doubt about where a clinical fact belongs: it belongs to the toolkit or facility material, and the drill points here. This library owns the learner's side and the connective progression — one source of truth, no duplication (`BUILD_PLAN.md` §1, §10).*
