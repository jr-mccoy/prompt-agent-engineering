# Psychology Library — Remaining Prompts Roadmap

**Status as of 2026-06-08:** **124 prompts** in the psychology library (96 prior + Wave 3's 28 just authored). The domain was promoted from `domain-specialized-fields/psychology/` to top-level `domain-psychology/` on 2026-06-08.

### Build status (reconciled 2026-06-08)

| Wave | Theme | Planned | Built | Status |
|------|-------|---------|-------|--------|
| W1 | Documentation & note formats | 15 | 15 | ✅ complete |
| W2 | Risk & crisis | 10 | 10 | ✅ complete |
| **W4** | **Modalities** (CBT 7, DBT 5, ACT 4, EMDR 5, IFS 3, MI 4, schema/psychodynamic 3) | 31 | 31 | ✅ **complete** (was listed as "future wave" in PROMPT_INDEX) |
| W5 | Client self-use core | 30 | 30 | ✅ complete |
| — | Pre-existing relocated | ~10 | ~10 | ✅ |
| **W3** | **Intake / formulation / treatment-planning depth** | 28 | 28 | ✅ **complete** (intake 12, diagnostic-formulation 8, treatment-planning 8) |
| **W6** | **Populations** (child/adolescent 6, perinatal 3, geriatric 3, LGBTQ+ 3, neurodivergent adult 4, SMI 4, veteran 3, cross-population 4) | 30 | 30 | ✅ **complete** |
| **W7** | **Prescriber / care-coord / supervision+ / MBC / practice-ops+** | 30 | 30 | ✅ **complete** (built 2026-06-08: prescriber 8, care-coord 5, supervision+ 8, MBC 4, practice-ops+ 5) |
| **W8** | **Client self-use: pre-therapy / relational / grief-loss / identity-transitions / crisis-self-triage / communication-system / habit-lifestyle / psychoeducation-self** | 41 | 41 | ✅ **complete** (built 2026-06-08) |
| **W9** | **Specialty clinical verticals** (CBT-E, FBT, OCD-ERP, CBT-I, ACT-pain, sex therapy, behavioral addiction, IPSRT, hoarding, comorbid insomnia, SSD, chronic-illness adjustment) | 12 | 12 | ✅ **complete** (built 2026-06-08) |
| **W10** | **Additional modalities** (CPT, prolonged-grief therapy, SFBT, narrative, sensorimotor/somatic, polyvagal, BPT/PCIT, group-curriculum, EFT-individual, ACT-group) | 10 | 10 | ✅ **complete** (built 2026-06-08) |
| **W11** | **Assessment & psychological testing** (battery selection, neuropsych screening, ADHD/autism battery design, personality integration, PROM selection, capacity, forensic framing, feedback session, integrated report) | 10 | 10 | ✅ **complete** (built 2026-06-08) |
| **W12** | **Couples / family / systems depth + digital practice** (EFT-couples, Gottman, IFS-couples, structural, Bowenian genogram, discernment counseling; tele-mental-health, AI-augmented ops, digital phenotyping, async messaging) | 10 | 10 | ✅ **complete** (built 2026-06-08: family-couples-systems 6, digital-practice 4) |

**Remaining on the original plan:** none — **Wave 8 is built**, completing the original **~210**-prompt plan (Waves 1–8 done). Waves 9–13 below are the net-new extension to the revised **~260** target.

**Net-new (this refresh):** Waves 9–13 ≈ **52 prompts** extend the library to a revised target of **~260**. These cover specialty clinical verticals, additional evidence-based modalities, psychological testing, systems/digital practice, and client-self-use specialty tools that the original 8-wave plan did not address. They are enumerated after Wave 8.

This document enumerates every planned remaining prompt with:
- target subdirectory
- proposed filename
- 1-line objective
- difficulty tag
- whether it requires clinician sign-off note (for self-administered tools that should be reviewed before use)

Prompts can be added in any order; the wave grouping is for batch-authoring efficiency, not dependency.

---

## Wave 3 — Intake / Formulation / Treatment-Planning Depth (~28 prompts) ✅ COMPLETE (built 2026-06-08)

These deepen the clinical-reasoning layer that Wave 1's documentation skeletons currently delegate to bracketed `[clinician input required]` slots.

### `intake-assessment/` (12 new)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_screening_battery_interpreter.md` | Compile and interpret a screening battery (PHQ-9 + GAD-7 + PCL-5 + AUDIT + C-SSRS) at intake with clinician framing | intermediate |
| `psychology_mental_status_exam_compiler.md` | Compile a structured MSE from interview observations (descriptive, not "WNL") | intermediate |
| `psychology_cultural_formulation_interview_drafter.md` | DSM-5 Cultural Formulation Interview structured drafter | advanced |
| `psychology_developmental_history_compiler.md` | Compile prenatal → milestone → school → adolescence history for adult intake | intermediate |
| `psychology_trauma_history_intake_module.md` | Trauma-history module that respects pacing and doesn't push detail | advanced |
| `psychology_substance_use_history_intake_module.md` | Per-substance history with AUDIT/DAST scoring and ASAM criteria framing | intermediate |
| `psychology_psychiatric_history_compiler.md` | Prior diagnoses / providers / meds / hospitalizations / longest stability | intermediate |
| `psychology_medical_history_for_psych_intake.md` | Medical history with attention to psychotropic-relevant labs and conditions | intermediate |
| `psychology_collateral_information_interview_protocol.md` | Structured collateral interview with ROI scope adherence | intermediate |
| `psychology_re_intake_after_lapse_protocol.md` | Re-intake after long lapse — what to update vs re-do | intermediate |
| `psychology_intake_for_telehealth_only_practice.md` | Telehealth-specific intake with location attestation, escalation plan | intermediate |
| `psychology_pediatric_intake_with_caregiver.md` | Child / adolescent intake with both child and caregiver inputs | advanced |

### `diagnostic-formulation/` (8 new)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_dsm5_differential_generator.md` | Generate ICD-10/DSM-5-TR differential with confirm/refute criteria per dx | advanced |
| `psychology_icd10_crosswalk_assistant.md` | DSM-5-TR to ICD-10-CM code crosswalk for billing | beginner |
| `psychology_provisional_vs_rule_out_decision_aid.md` | When to assign provisional vs rule-out vs deferred | intermediate |
| `psychology_comorbidity_mapping.md` | Common comorbidity patterns (depression+anxiety, PTSD+SUD, BPD+MDD) and treatment implications | advanced |
| `psychology_normal_reaction_vs_disorder_reasoner.md` | When does grief / acute stress / life-stage transition cross into disorder | advanced |
| `psychology_malingering_vs_genuine_distress_framework.md` | Forensic-aware framework for evaluating credibility without dismissing | advanced |
| `psychology_personality_disorder_dimensional_formulation.md` | Dimensional (DSM-5 Section III alt) PD formulation | advanced |
| `psychology_diagnostic_disclosure_conversation_planner.md` | How to share a diagnosis with a client without flattening them | intermediate |

### `treatment-planning/` (8 new)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_smart_treatment_goal_generator.md` | Convert problem statement into SMART goals with measurement | intermediate |
| `psychology_golden_thread_writer.md` | Walk problem → goal → SMART objective → intervention → measurement chain | intermediate |
| `psychology_modality_selection_decision_aid.md` | CBT vs DBT vs ACT vs EMDR vs psychodynamic vs IFS — match to presentation | advanced |
| `psychology_stepped_care_decision_aid.md` | Outpatient → IOP → PHP → residential → inpatient — when to step | advanced |
| `psychology_measurement_based_care_plan.md` | Build a measurement-based care plan with cadence and instruments | intermediate |
| `psychology_treatment_resistance_reformulation.md` | When the plan isn't working, how to reformulate without abandoning | advanced |
| `psychology_relapse_prevention_plan_designer.md` | End-of-treatment relapse prevention plan with warning signs and supports | intermediate |
| `psychology_referral_decision_aid_within_episode.md` | When to refer out for adjunct care while continuing primary | intermediate |

---

## Wave 4 — Modality Interventions (~30 prompts) ✅ COMPLETE (built 2026; 31 prompts on disk)

> Retained below for reference. All files in this wave now exist under `modalities/`.

### `modalities/cbt/` (6 new — adds to existing cognitive-distortion-identifier)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_cbt_thought_record_drafter.md` | Structured 7-column thought record with cognitive restructuring | intermediate |
| `psychology_cbt_behavioral_experiment_designer.md` | Design behavioral experiment to test a specific belief | intermediate |
| `psychology_cbt_panic_protocol_session_plan.md` | CBT-Panic session plan with interoceptive exposure | advanced |
| `psychology_cbt_social_anxiety_protocol_session_plan.md` | CBT-SA session plan with video-feedback and dropping safety behaviors | advanced |
| `psychology_cbt_specific_phobia_one_session_treatment.md` | One-session in-vivo exposure protocol | advanced |
| `psychology_cbt_relapse_prevention_module.md` | End-of-CBT relapse prevention with personal manual | intermediate |

### `modalities/dbt/` (5)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_dbt_diary_card_analyzer.md` | Process a week of diary cards: target hierarchy review, skill use, urges | intermediate |
| `psychology_dbt_chain_analysis.md` | Behavior chain analysis with vulnerability factors, prompting events, links, consequences | advanced |
| `psychology_dbt_skills_coaching_call_simulator.md` | Telephone skills coaching call within DBT framework | advanced |
| `psychology_dbt_target_hierarchy_session_organizer.md` | Apply life-threatening / TIB / QOL / skills target hierarchy to session agenda | intermediate |
| `psychology_dbt_emotion_regulation_module_lesson.md` | Lesson plan for an emotion regulation skills module | intermediate |

### `modalities/act/` (4)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_act_values_card_sort.md` | Facilitated values clarification with card sort | intermediate |
| `psychology_act_defusion_exercise_selector.md` | Match defusion exercise to client's specific cognitive fusion pattern | intermediate |
| `psychology_act_matrix_session_facilitator.md` | ACT matrix with toward/away moves, mental events vs sensory | intermediate |
| `psychology_act_committed_action_planner.md` | Convert values into committed-action plan with workability check | intermediate |

### `modalities/emdr-trauma/` (5)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_emdr_target_sequence_organizer.md` | Past / present / future target sequence with cluster mapping | advanced |
| `psychology_emdr_aip_case_formulation.md` | Adaptive Information Processing-based formulation | advanced |
| `psychology_emdr_blocked_processing_troubleshooter.md` | Identify blocking belief / feeder memory / cognitive interweave needed | advanced |
| `psychology_emdr_phase_2_resourcing_protocol.md` | Resource development & installation before processing | advanced |
| `psychology_prolonged_exposure_session_plan.md` | PE imaginal + in-vivo exposure session plan | advanced |

### `modalities/ifs-parts/` (3)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_ifs_parts_mapping.md` | Map manager / firefighter / exile parts and Self qualities | advanced |
| `psychology_ifs_unburdening_session_structure.md` | Phased unburdening session for an exile | advanced |
| `psychology_ifs_polarized_parts_resolution.md` | Work with polarized parts (e.g., critic ↔ rebellious teen) | advanced |

### `modalities/motivational-interviewing/` (4)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_mi_decisional_balance_facilitator.md` | Decisional balance for ambivalent change topic | intermediate |
| `psychology_mi_change_talk_coder.md` | Code session transcript for DARN-CAT change talk | intermediate |
| `psychology_mi_oars_response_generator.md` | Generate Open question / Affirmation / Reflection / Summary responses | intermediate |
| `psychology_mi_ambivalence_map.md` | Two-column ambivalence map with double-sided reflections | intermediate |

### `modalities/schema-psychodynamic/` (3)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_schema_mode_mapper.md` | Map active schema modes (vulnerable child, punitive parent, healthy adult) | advanced |
| `psychology_psychodynamic_transference_focused_formulation.md` | TFP-style object-relations formulation | advanced |
| `psychology_psychodynamic_session_process_note.md` | Process-focused note capturing transference, defenses, enactments | advanced |

---

## Wave 6 — Populations (~30 prompts) ✅ COMPLETE (built 2026-06-08)

> All files in this wave now exist under `populations/`. The four cross-population files are placed in `populations/cross-population/`.

### `populations/child-adolescent/` (6)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_child_play_therapy_session_note.md` | Play therapy session note with developmental framing | intermediate |
| `psychology_adolescent_intake_with_developmental_lens.md` | Adolescent intake covering identity, peer, family, school, risk | advanced |
| `psychology_pediatric_anxiety_protocol_session_plan.md` | Coping-Cat / Cool-Kids style session plan | intermediate |
| `psychology_adolescent_dbt_skills_module.md` | Age-adapted DBT skills module for teens | intermediate |
| `psychology_school_collaboration_504_iep_input.md` | Mental-health input for 504/IEP meeting | intermediate |
| `psychology_pediatric_safety_planning_with_caregiver.md` | Safety planning with both teen and caregiver | advanced |

### `populations/perinatal/` (3)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_perinatal_mood_anxiety_screen_interpretation.md` | EPDS / PHQ-9 / GAD-7 in perinatal population with cutoffs | intermediate |
| `psychology_perinatal_treatment_options_with_pregnancy_lactation.md` | Therapy and medication considerations across pregnancy / lactation | advanced |
| `psychology_postpartum_psychosis_recognition_and_referral.md` | Recognition, urgency, and disposition for postpartum psychosis | advanced |

### `populations/geriatric/` (3)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_geriatric_depression_vs_dementia_differential.md` | Pseudodementia vs early dementia screening framework | advanced |
| `psychology_geriatric_intake_with_polypharmacy_review.md` | Geriatric intake including medication review and falls risk | intermediate |
| `psychology_geriatric_grief_and_late_life_transitions.md` | Late-life grief, identity, role-loss work | intermediate |

### `populations/lgbtq-affirmative/` (3)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_lgbtq_affirmative_intake_module.md` | Identity-affirmative intake with minority-stress framing | intermediate |
| `psychology_gender_affirming_letter_drafter.md` | Letter for gender-affirming care per WPATH framework | advanced |
| `psychology_minority_stress_formulation.md` | Meyer's minority-stress model applied to case formulation | intermediate |

### `populations/neurodivergent-adult/` (4)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_adult_autism_assessment_intake_module.md` | Adult-autism assessment intake with masking-aware questions | advanced |
| `psychology_adult_adhd_assessment_intake_module.md` | Adult-ADHD assessment intake with executive-function-history | intermediate |
| `psychology_pda_pathological_demand_avoidance_framework.md` | PDA-aware approach to demand-avoidance presentations | advanced |
| `psychology_neurodivergent_affirming_treatment_planning.md` | Treatment planning that doesn't pathologize neurotype | intermediate |

### `populations/severe-mental-illness/` (4)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_first_episode_psychosis_intake.md` | First-episode psychosis intake with CHR / FEP differentiation | advanced |
| `psychology_smi_recovery_oriented_treatment_plan.md` | Recovery-oriented plan: housing, work, social, symptom | advanced |
| `psychology_assertive_community_treatment_engagement_plan.md` | ACT-team engagement and outreach plan | advanced |
| `psychology_smi_med_adherence_motivational_plan.md` | Adherence work using MI for clients on antipsychotics / mood stabilizers | intermediate |

### `populations/veteran-military/` (3)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_veteran_intake_with_service_history.md` | Service-history-informed intake | intermediate |
| `psychology_combat_trauma_formulation.md` | Combat-trauma formulation including moral injury | advanced |
| `psychology_military_sexual_trauma_aware_protocol.md` | MST-aware engagement and treatment planning | advanced |

### Cross-population (4)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_couples_therapy_intake_eft_or_gottman.md` | Couples intake using EFT or Gottman frame | advanced |
| `psychology_family_therapy_intake_systemic.md` | Family-systems intake with genogram and presenting-problem mapping | advanced |
| `psychology_group_therapy_member_screening.md` | Group-therapy member screening for fit | intermediate |
| `psychology_grief_complicated_vs_normal_assessment.md` | Prolonged Grief Disorder vs normal grief assessment | advanced |

---

## Wave 7 — Psychiatric Prescriber, Care Coordination, Supervision, Practice Operations (30 prompts) ✅ COMPLETE (built 2026-06-08)

### `psychiatric-prescriber/` (8)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_initial_psych_eval_drafter.md` | Initial psychiatric evaluation note (90792) | advanced |
| `psychology_med_management_progress_note.md` | E&M-style med management note | intermediate |
| `psychology_depression_med_algorithm_reasoner.md` | First-line / next-step / augmentation reasoning for depression | advanced |
| `psychology_anxiety_med_algorithm_reasoner.md` | First-line / next-step reasoning for anxiety disorders | advanced |
| `psychology_bipolar_med_algorithm_reasoner.md` | Mood stabilizer / antipsychotic / antidepressant reasoning across bipolar phases | advanced |
| `psychology_adhd_med_algorithm_reasoner.md` | Stimulant / non-stimulant reasoning, monitoring, diversion-risk | advanced |
| `psychology_psychotropic_taper_plan.md` | Taper plan for SSRI / benzo / antipsychotic / mood stabilizer | advanced |
| `psychology_controlled_substance_agreement_drafter.md` | Controlled-substance agreement (stimulant or benzo) for the chart | intermediate |

### `care-coordination/` (5)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_referral_letter_generator.md` | Referral letter to specialist with ROI scope | intermediate |
| `psychology_warm_handoff_narrative.md` | Warm-handoff narrative for transfer of care | intermediate |
| `psychology_pcp_communication_note.md` | PCP communication note with relevant clinical and med info | intermediate |
| `psychology_integrated_care_huddle_brief.md` | Integrated-care daily huddle brief on shared patients | intermediate |
| `psychology_school_partnership_communication.md` | School-partnership communication with appropriate scope | intermediate |

### `supervision-professional/` (8 — adds to existing therapeutic-technique-explainer)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_supervision_agenda_builder.md` | Build a supervision agenda from the supervisee's caseload | intermediate |
| `psychology_parallel_process_detector.md` | Detect parallel-process dynamics in supervision | advanced |
| `psychology_countertransference_reflection_prompt.md` | Structured countertransference reflection | intermediate |
| `psychology_clinical_vignette_teaching_case_generator.md` | Generate teaching case from a real vignette (de-identified) | intermediate |
| `psychology_ethics_consultation_walkthrough.md` | Structured ethics-consultation walkthrough | advanced |
| `psychology_scope_of_practice_decision_aid.md` | Scope-of-practice analysis when ambiguity arises | advanced |
| `psychology_dual_relationship_analyzer.md` | Dual-relationship / boundary-crossing analysis | advanced |
| `psychology_board_exam_vignette_study_tool.md` | Generate board-style vignettes with answer reasoning | intermediate |

### `measurement-based-care/` (4)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_outcome_monitoring_dashboard_interpreter.md` | Interpret a panel-level outcome dashboard | intermediate |
| `psychology_individual_rom_trajectory_analyzer.md` | Analyze an individual's ROM trajectory and treatment response | intermediate |
| `psychology_treatment_non_response_decision_tree.md` | Decision tree when client isn't responding | advanced |
| `psychology_mbc_implementation_plan_for_practice.md` | MBC implementation plan for a practice / clinic | intermediate |

### `practice-operations/` (5 — adds to existing informed-consent-template-builder)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_missed_appointment_policy_letter.md` | No-show / late-cancel policy letter | beginner |
| `psychology_telehealth_state_of_licensure_decision_aid.md` | Telehealth across-state-lines decision aid (PSYPACT, exceptions) | intermediate |
| `psychology_insurance_verification_intake_protocol.md` | Insurance verification structured protocol | beginner |
| `psychology_superbill_generator.md` | Superbill with codes and modifiers for client out-of-network claim | beginner |
| `psychology_records_request_response_decision_aid.md` | How to respond to records requests (subpoena vs court order vs HIPAA request) | advanced |

---

## Wave 8 — Identity / Grief / Relational / Crisis-Self / System-Navigation (41 prompts) ✅ COMPLETE (built 2026-06-08)

### `client-self-use/pre-therapy/` (5)

| File | Objective | Difficulty |
|------|-----------|------------|
| `clientself_do_i_need_therapy_decision_aid.md` | Self-decision aid for whether to start therapy | beginner |
| `clientself_modality_fit_selector.md` | Match modality (CBT / DBT / EMDR / psychodynamic / IFS) to my needs | intermediate |
| `clientself_finding_a_therapist_search_criteria.md` | Build search criteria + therapist-interview questions | beginner |
| `clientself_insurance_eap_sliding_scale_navigation.md` | How to find affordable therapy (insurance, EAP, sliding-scale, training clinics) | beginner |
| `clientself_culturally_affirming_therapist_screening.md` | Screen for cultural / identity fit with prospective therapists | intermediate |

### `client-self-use/relational/` (7)

| File | Objective | Difficulty |
|------|-----------|------------|
| `clientself_boundary_setting_script.md` | Build a specific boundary-setting script with anticipated pushback | intermediate |
| `clientself_repair_conversation_drafter.md` | Draft an apology / repair conversation that doesn't over- or under-own | intermediate |
| `clientself_is_this_relationship_healthy_check.md` | Pattern-check across multiple relationship dimensions | intermediate |
| `clientself_attachment_style_self_reflection.md` | Attachment-style reflection without typing-as-destiny | beginner |
| `clientself_conflict_postmortem.md` | After-conflict reflection: what each person was protecting | intermediate |
| `clientself_navigating_estrangement.md` | Working with family / parental estrangement (initiating, holding, repairing) | advanced |
| `clientself_friendship_end_conversation.md` | Drafting a friendship-end or hibernation conversation | intermediate |

### `client-self-use/grief-loss/` (5)

| File | Objective | Difficulty |
|------|-----------|------------|
| `clientself_grief_continuing_bonds_journaling.md` | Continuing-bonds journal prompts (vs stages-based) | beginner |
| `clientself_anniversary_reaction_plan.md` | Pre-plan for an anniversary / death-day / season | beginner |
| `clientself_complicated_vs_normal_grief_reflection.md` | Self-reflection on whether grief has crossed into prolonged grief | intermediate |
| `clientself_pet_loss_script.md` | Pet-loss reflection and ritual script | beginner |
| `clientself_ambiguous_loss_framework.md` | Boss's ambiguous-loss framework for living-but-lost (dementia, addiction, estrangement) | intermediate |

### `client-self-use/identity-transitions/` (6)

| File | Objective | Difficulty |
|------|-----------|------------|
| `clientself_coming_out_planning.md` | Planning a coming-out conversation (gender / sexuality / identity) | intermediate |
| `clientself_gender_identity_exploration_journal.md` | Structured exploration journal without rushing | intermediate |
| `clientself_religious_deconstruction_support.md` | Working through religious deconstruction with grief and integrity | advanced |
| `clientself_divorce_separation_emotional_plan.md` | Emotional plan for divorce / separation distinct from logistics | intermediate |
| `clientself_retirement_identity_reframe.md` | Working with identity loss in retirement | intermediate |
| `clientself_post_diagnosis_adjustment.md` | Adjustment to chronic illness / neurodivergence diagnosis | intermediate |

### `client-self-use/crisis-self-triage/` (4)

| File | Objective | Difficulty |
|------|-----------|------------|
| `clientself_am_i_in_crisis_self_triage.md` | Self-triage for whether to call clinician, crisis line, or ED | intermediate |
| `clientself_post_ed_discharge_self_plan.md` | Personal plan for the first 72 hours after ED discharge | advanced |
| `clientself_supporting_loved_one_in_crisis.md` | What to do when someone I love is in suicidal crisis | intermediate |
| `clientself_after_suicide_loss_support.md` | Initial support framework after losing someone to suicide | advanced |

### `client-self-use/communication-system/` (5)

| File | Objective | Difficulty |
|------|-----------|------------|
| `clientself_writing_to_therapist_about_concerns.md` | Drafting a between-session message to therapist about a concern | beginner |
| `clientself_requesting_records.md` | Requesting clinical records (HIPAA framework) | beginner |
| `clientself_complaint_to_licensing_board.md` | Drafting a complaint to a state licensing board | intermediate |
| `clientself_inpatient_self_advocacy.md` | Self-advocacy on an inpatient unit | advanced |
| `clientself_workplace_accommodations_request.md` | Drafting an ADA-style workplace accommodations request for mental health | intermediate |

### `client-self-use/habit-lifestyle/` (4)

| File | Objective | Difficulty |
|------|-----------|------------|
| `clientself_sustainable_habit_designer.md` | Habit design with explicit relapse planning | intermediate |
| `clientself_screen_time_phone_relationship_audit.md` | Honest audit of phone / screen relationship without moralizing | beginner |
| `clientself_alcohol_use_re_evaluation.md` | DrinkLessUK-style re-evaluation of alcohol use | intermediate |
| `clientself_exercise_as_antidepressant_plan.md` | Exercise-as-antidepressant plan with behavioral-activation overlap | beginner |

### `client-self-use/psychoeducation-self/` (5)

| File | Objective | Difficulty |
|------|-----------|------------|
| `clientself_explain_my_diagnosis_to_me.md` | Plain-language explanation of a diagnosis I was given | beginner |
| `clientself_explain_my_partner_diagnosis.md` | Understanding a partner's diagnosis to support without taking it on | intermediate |
| `clientself_what_to_expect_first_psychiatry_appointment.md` | What to expect at a first psychiatric appointment | beginner |
| `clientself_what_to_expect_neuropsych_eval.md` | What to expect from a neuropsych evaluation | beginner |
| `clientself_my_med_was_just_prescribed_questions.md` | Questions to ask about a newly-prescribed psychotropic | beginner |

---

## Wave 9 — Specialty Clinical Verticals (provider) (~12) ✅ COMPLETE (built 2026-06-08)

Disorder-specific protocols the modality directories do not cover. Each anchors to a manualized/evidence-based protocol so output can be checked. All 12 files now exist under `specialty-clinical/`.

### `specialty-clinical/` (12)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_eating_disorder_cbt_e_protocol.md` | CBT-E session protocol with regular-eating and weight-monitoring structure | advanced |
| `psychology_eating_disorder_fbt_phase_planner.md` | Family-Based Treatment phase planner for adolescent eating disorders | advanced |
| `psychology_ocd_erp_provider_protocol.md` | Provider-side ERP protocol with hierarchy, response-prevention, mental-compulsion handling | advanced |
| `psychology_cbt_i_provider_sleep_protocol.md` | Provider CBT-I protocol (sleep restriction, stimulus control, titration) | intermediate |
| `psychology_health_psych_chronic_pain_act_protocol.md` | ACT-for-chronic-pain session protocol with values and acceptance focus | advanced |
| `psychology_sex_therapy_assessment_and_plan.md` | Sex-therapy assessment and intervention plan (PLISSIT-aware) | advanced |
| `psychology_behavioral_addiction_protocol.md` | Gambling / gaming / behavioral-addiction CBT protocol | intermediate |
| `psychology_bipolar_ipsrt_protocol.md` | Interpersonal & Social Rhythm Therapy protocol for bipolar | advanced |
| `psychology_hoarding_disorder_protocol.md` | Hoarding-disorder CBT protocol with sorting/discarding structure | advanced |
| `psychology_insomnia_comorbid_with_pain_or_ptsd.md` | CBT-I adapted for comorbid pain / PTSD with safety carve-outs | advanced |
| `psychology_somatic_symptom_disorder_protocol.md` | Somatic-symptom-disorder reattribution and CBT protocol | advanced |
| `psychology_chronic_illness_adjustment_protocol.md` | Adjustment-to-chronic-illness intervention plan | intermediate |

---

## Wave 10 — Additional Modalities (~10) ✅ COMPLETE (built 2026-06-08)

Evidence-based approaches not represented in Wave 4. All 10 files now exist under `modalities/` in the new subdirs named below.

### `modalities/` (new subdirs) (10)

| File | Subdir | Objective | Difficulty |
|------|--------|-----------|------------|
| `psychology_cpt_cognitive_processing_therapy_protocol.md` | `cpt/` | CPT (cognitive processing therapy) session protocol with stuck-point log | advanced |
| `psychology_prolonged_grief_therapy_protocol.md` | `grief-therapy/` | PGT protocol distinct from generic grief support | advanced |
| `psychology_sfbt_session_structure.md` | `sfbt/` | Solution-focused brief-therapy session structure with scaling/miracle question | intermediate |
| `psychology_narrative_therapy_externalizing_session.md` | `narrative/` | Narrative-therapy externalizing-conversation session | intermediate |
| `psychology_somatic_sensorimotor_session_plan.md` | `somatic/` | Sensorimotor/somatic session plan with window-of-tolerance tracking | advanced |
| `psychology_polyvagal_informed_stabilization_plan.md` | `somatic/` | Polyvagal-informed stabilization and regulation plan | intermediate |
| `psychology_behavioral_parent_training_module.md` | `behavioral-parent-training/` | BPT / PCIT-style parent-training module | intermediate |
| `psychology_group_therapy_curriculum_builder.md` | `group/` | Build a structured group-therapy curriculum (process or psychoeducational) | intermediate |
| `psychology_eft_individual_emotion_focused_session.md` | `eft-individual/` | Emotion-Focused Therapy (individual) session with emotion-deepening | advanced |
| `psychology_acceptance_commitment_group_protocol.md` | `act/` | ACT group protocol (adds to existing ACT set) | intermediate |

---

## Wave 11 — Assessment & Psychological Testing (~10) ✅ COMPLETE (built 2026-06-08)

Test selection and interpretation scaffolds. **⚠️ Authoring caution:** do not reproduce copyrighted instrument item content; reference instruments by name and interpret bands/structure only. All 10 files now exist under `assessment-testing/`; every file references instruments by name and interprets bands/structure only (no item content), is referral-aware with stated scope and referral thresholds, and carries a copyright Must-Not.

### `assessment-testing/` (10)

| File | Objective | Difficulty |
|------|-----------|------------|
| `psychology_test_battery_selection_aid.md` | Select an assessment battery matched to referral question | advanced |
| `psychology_neuropsych_screening_interpretation.md` | Interpret cognitive-screening results into a clinical read (referral-aware) | advanced |
| `psychology_adhd_testing_battery_design.md` | Design an adult/child ADHD testing battery with multi-source data | intermediate |
| `psychology_autism_testing_battery_design.md` | Design an autism assessment battery (masking-aware, multi-informant) | advanced |
| `psychology_personality_assessment_integration.md` | Integrate multi-method personality assessment into a coherent formulation | advanced |
| `psychology_prom_measure_selection_aid.md` | Select patient-reported outcome measures for a presentation/setting | intermediate |
| `psychology_capacity_evaluation_scaffold.md` | Decisional-capacity evaluation scaffold (medical/financial) | advanced |
| `psychology_forensic_evaluation_framing.md` | Forensic-evaluation framing (referral question, role boundaries, limits) | advanced |
| `psychology_feedback_session_planner.md` | Therapeutic-assessment feedback-session planner | intermediate |
| `psychology_integrated_assessment_report_writer.md` | Write an integrated assessment report from multi-source findings | advanced |

---

## Wave 12 — Couples / Family / Systems Depth + Digital Practice (~10) ✅ COMPLETE (built 2026-06-08)

Goes beyond the Wave 6 cross-population stubs. All 10 files now exist under `family-couples-systems/` (6) and `digital-practice/` (4). Systems prompts anchor to named models (EFT three-stage/nine-step, Gottman Method, IFIO/IFS-couples, Minuchin structural, Bowen genogram, Doherty discernment); digital-practice prompts each carry clinical-oversight guardrails, safety/risk routing, and licensure/PSYPACT considerations.

### `family-couples-systems/` (6) and `digital-practice/` (4)

| File | Subdir | Objective | Difficulty |
|------|--------|-----------|------------|
| `psychology_eft_couples_full_arc_planner.md` | `family-couples-systems/` | EFT-couples full three-stage arc planner | advanced |
| `psychology_gottman_intervention_planner.md` | `family-couples-systems/` | Gottman-method intervention planner from assessment | advanced |
| `psychology_ifs_couples_session_structure.md` | `family-couples-systems/` | IFS-informed couples session structure | advanced |
| `psychology_structural_family_therapy_session.md` | `family-couples-systems/` | Structural family-therapy session (boundaries, enactments) | advanced |
| `psychology_bowenian_genogram_formulation.md` | `family-couples-systems/` | Bowenian multigenerational genogram formulation | advanced |
| `psychology_discernment_counseling_protocol.md` | `family-couples-systems/` | Discernment-counseling protocol for mixed-agenda couples | advanced |
| `psychology_telemental_health_program_design.md` | `digital-practice/` | Design a tele-mental-health program (modality, safety, tech, licensure) | intermediate |
| `psychology_ai_augmented_practice_ops_design.md` | `digital-practice/` | Design AI-augmented practice operations with clinical-oversight guardrails | intermediate |
| `psychology_digital_phenotyping_data_interpreter.md` | `digital-practice/` | Interpret passive/app-collected behavioral data into clinical signal | advanced |
| `psychology_async_messaging_therapy_protocol.md` | `digital-practice/` | Asynchronous-messaging therapy protocol with risk routing | intermediate |

---

## Wave 13 — Client Self-Use Specialty (~10)

Population/condition-specific self-tools with strong clinician-handoff for anything not self-administrable.

### `client-self-use/specialty/` (10)

| File | Objective | Difficulty |
|------|-----------|------------|
| `clientself_eating_self_monitoring_with_handoff.md` | Eating self-monitoring tool with mandatory clinician handoff and risk routing | advanced |
| `clientself_ocd_self_erp_prep_with_therapist.md` | OCD self-ERP preparation for therapist review (not self-administration) | advanced |
| `clientself_chronic_pain_self_management_plan.md` | Chronic-pain self-management plan (pacing, ACT-overlay, flare plan) | intermediate |
| `clientself_caregiver_burnout_plan.md` | Caregiver-burnout assessment and sustainable-support plan | intermediate |
| `clientself_perinatal_self_screen_and_plan.md` | Perinatal mood/anxiety self-screen with clear escalation thresholds | advanced |
| `clientself_mens_mental_health_engagement.md` | Men's-mental-health engagement tool lowering help-seeking barriers | intermediate |
| `clientself_faith_integrated_coping_plan.md` | Faith/values-integrated coping plan (tradition-neutral) | intermediate |
| `clientself_neurodivergent_self_advocacy_toolkit.md` | Neurodivergent self-advocacy and accommodation toolkit | intermediate |
| `clientself_postpartum_partner_support_guide.md` | Guide for a partner supporting someone postpartum (recognition + action) | intermediate |
| `clientself_chronic_illness_mental_health_plan.md` | Mental-health plan alongside a chronic-illness diagnosis | intermediate |

---

## Cross-Wave Conventions (apply to all remaining prompts)

- **Frontmatter:** `intended_use: model-testing`; standard `title`, `category`, `description`, `techniques`, `difficulty`, `tags`, `updated`, `related_prompts`.
- **No boilerplate disclaimers in prompt body.** Constraints focus on documentation accuracy, format fidelity, and named-instrument scoring.
- **Provider-side prompts:** include billing block (CPT/HCPCS) where applicable; include risk-reassessment hook where applicable; include supervisor / co-sign line for high-acuity content.
- **Client-side prompts:** include "bring this to my therapist" handoff for tools that should not be self-administered (exposure design, ERP design, sleep restriction in safety-carve-out populations).
- **Risk routing:** every client-side prompt includes a clear escalation pathway (clinician this week / today / 988 / ED).
- **Safety carve-outs:** prompts targeting self-administered behavior change (BA, sleep restriction, ERP, exposure, accommodation reduction) include explicit do-not-use conditions.

---

## Authoring Order Recommendation

If batching, suggested order:

1. **Wave 3 (intake/formulation/treatment-planning depth)** — fills the bracketed-input slots in Wave 1's documentation skeletons; highest yield for clinician-side testing.
2. **Wave 7 prescriber + supervision** — completes the provider-side workflow corpus.
3. **Wave 4 modalities** — long but highly testable: each modality has manualized protocols models can be checked against.
4. **Wave 6 populations** — tests cultural / developmental / population adaptation.
5. **Wave 8 client-side identity / grief / relational / crisis-self / system-navigation** — completes user-facing surface; pairs with Wave 5.

Each wave can be authored independently in any order — there are no hard dependencies, only thematic groupings.

---

## Sizing Estimate

| Wave | Prompts | Avg. lines/prompt | Approx. total lines | Status |
|------|---------|-------------------|---------------------|--------|
| 3    | 28      | 220               | ~6,200              | ✅ built |
| 4    | 31      | 200               | ~6,200              | ✅ built |
| 6    | 30      | 200               | ~6,000              | ✅ built |
| 7    | 30      | 220               | ~5,700              | ✅ built |
| 8    | 30      | 130               | ~3,900              | not started |
| **Original plan remaining** | **~114** | — | **~21,800 lines** | |
| 9 (specialty clinical) | 12 | 220 | ~2,600 | ✅ built |
| 10 (modalities) | 10 | 200 | ~2,000 | ✅ built |
| 11 (assessment/testing) | 10 | 220 | ~2,200 | ✅ built |
| 12 (systems/digital) | 10 | 210 | ~2,100 | ✅ built |
| 13 (client-self specialty) | 10 | 140 | ~1,400 | net-new |
| **Net-new total** | **52** | — | **~10,300 lines** | |
| **All remaining → ~260 target** | **~166** | — | **~32,100 lines** | |

For comparison: Waves 1+2 = ~4,700 lines; Wave 4 = ~6,200 lines; Wave 5 = ~3,400 lines (all built).

---

*Last updated: 2026-05-08*
