# Healthcare Clinical Domain Expansion Roadmap (v2)

**Status:** Active
**Replaces:** `_archive/EXPANSION_ROADMAP_v1_safety_framing.md` (archived 2026-05-08)
**Purpose:** Build a deep, real-world clinical prompt library for **model testing and training**. Prompts target the actual reasoning, interpretation, and prescriptive output that healthcare professionals produce in daily workflow.

---

## Framing Change From v1

The v1 roadmap explicitly excluded "direct diagnosis," "treatment recommendations," and "definitive medication dosing." That framing produced prompts that hedged, deferred, and asked clinicians to do the reasoning themselves — useful as decision-support training data but **not useful for testing whether a model can actually do clinical work**.

v2 inverts that: prompts now request the kind of output a senior attending would write for a colleague. No disclaimer headers, no "support not replace" language, no escalation framing baked into the prompt body. The library exists to discriminate model capability on real clinical tasks. Output framing intended for production patient-care deployment is a downstream wrapper concern, not a prompt-authoring concern.

---

## Scope: 9 Lanes, ~140 New Prompts

| # | Lane | Prompts | Subdir |
|---|---|---:|---|
| 1 | Pathophysiology & Mechanism | 15 | `prompts/pathophysiology/` (new) |
| 2 | Diagnostic Interpretation | 22 | `prompts/interpretation/` |
| 3 | Diagnostic Workup by Chief Complaint | 18 | `prompts/reasoning/` |
| 4 | Pharmacology Deep Layer | 22 | `prompts/pharmacology/` |
| 5 | Specialty Care Plans | 25 | `prompts/care-plans/` |
| 6 | Critical & Acute Care | 12 | `prompts/acute-care/` |
| 7 | Specialty-Specific Assessments & Workflows | 18 | `prompts/specialty/` |
| 8 | AI-Native Clinical Workflows | 10 | `prompts/workflow/` |
| 9 | Documentation | 10 | `prompts/workflow/` |

**Net new:** ~152 prompts. **Total target:** ~193 (current 41 + ~152).

---

## Phasing

### Phase 1 — Highest Model-Discrimination Yield (Lanes 1, 2, 4)
~59 prompts. Mechanism reasoning, structured interpretation, and pharmacology are where weak models hallucinate fastest. Highest signal for testing.

### Phase 2 — Reasoning Depth (Lanes 3, 5)
~43 prompts. Workup logic and prescriptive care plans test multi-step clinical reasoning across specialties.

### Phase 3 — Specialty Fidelity (Lanes 6, 7)
~30 prompts. Acute care and specialty depth test edge-case fidelity.

### Phase 4 — Format & Workflow (Lanes 8, 9)
~20 prompts. AI-native workflow tasks and structured documentation.

---

## Lane Detail

### Lane 1 — Pathophysiology & Mechanism (15)
- `patho_disease_mechanism_explainer.md`
- `patho_drug_mechanism_deep_dive.md`
- `patho_lab_abnormality_mechanism_decoder.md`
- `patho_pharmacokinetics_reasoning.md`
- `patho_pharmacodynamics_receptor.md`
- `patho_acid_base_mechanism.md`
- `patho_fluid_electrolyte_mechanism.md`
- `patho_inflammation_immunology_mechanism.md`
- `patho_genetics_phenotype_mechanism.md`
- `patho_microbial_pathogenesis.md`
- `patho_oncogenesis_tumor_biology.md`
- `patho_endocrine_axis_dysfunction.md`
- `patho_cardiac_hemodynamics.md`
- `patho_pulmonary_physiology.md`
- `patho_renal_physiology.md`

### Lane 2 — Diagnostic Interpretation (22)
- `interp_ecg_full_interpretation.md`
- `interp_cxr_systematic_read.md`
- `interp_ct_head.md`
- `interp_ct_chest.md`
- `interp_ct_abdomen_pelvis.md`
- `interp_mri_brain.md`
- `interp_mri_spine.md`
- `interp_echocardiogram_report.md`
- `interp_pft_pulmonary_function.md`
- `interp_abg_acid_base.md`
- `interp_urinalysis_microscopy.md`
- `interp_cbc_differential.md`
- `interp_cmp_bmp.md`
- `interp_coagulation_panel.md`
- `interp_lipid_panel_in_context.md`
- `interp_thyroid_function.md`
- `interp_iron_studies.md`
- `interp_lft_pattern.md`
- `interp_microbiology_culture_sensitivity.md`
- `interp_csf.md`
- `interp_synovial_pleural_ascitic_fluid.md`
- `interp_pathology_report.md`

### Lane 3 — Diagnostic Workup by Chief Complaint (18)
- `workup_chest_pain.md`
- `workup_dyspnea.md`
- `workup_abdominal_pain.md`
- `workup_headache.md`
- `workup_syncope.md`
- `workup_altered_mental_status.md`
- `workup_dizziness_vertigo.md`
- `workup_fever_unknown_origin.md`
- `workup_unintentional_weight_loss.md`
- `workup_lymphadenopathy.md`
- `workup_anemia.md`
- `workup_hyponatremia.md`
- `workup_hyperkalemia.md`
- `workup_aki.md`
- `workup_hematuria.md`
- `workup_jaundice.md`
- `workup_joint_pain_arthritis.md`
- `workup_rash_differential.md`

### Lane 4 — Pharmacology Deep Layer (22)
- `pharm_vancomycin_auc_dosing.md`
- `pharm_aminoglycoside_dosing.md`
- `pharm_iv_to_po_conversion.md`
- `pharm_opioid_equianalgesic_conversion.md`
- `pharm_insulin_regimen_design.md`
- `pharm_anticoag_periprocedural_bridging.md`
- `pharm_doac_selection_by_profile.md`
- `pharm_antihypertensive_selection.md`
- `pharm_antidepressant_selection_switching.md`
- `pharm_antipsychotic_selection.md`
- `pharm_antiepileptic_selection.md`
- `pharm_inhaler_regimen_asthma_copd.md`
- `pharm_steroid_taper_design.md`
- `pharm_benzodiazepine_taper.md`
- `pharm_ssri_snri_taper.md`
- `pharm_opioid_taper.md`
- `pharm_chemotherapy_regimen_explainer.md`
- `pharm_immunosuppression_regimen.md`
- `pharm_pregnancy_lactation_drug_safety.md`
- `pharm_pediatric_weight_based_dosing.md`
- `pharm_tdm_interpretation.md`
- `pharm_adverse_drug_reaction_naranjo.md`

### Lane 5 — Specialty Care Plans (25)
- `careplan_t2dm.md`
- `careplan_t1dm.md`
- `careplan_hfref_gdmt.md`
- `careplan_hfpef.md`
- `careplan_copd_gold.md`
- `careplan_asthma_stepwise.md`
- `careplan_ckd_staged.md`
- `careplan_cirrhosis.md`
- `careplan_afib.md`
- `careplan_post_mi_secondary_prevention.md`
- `careplan_stroke_secondary_prevention.md`
- `careplan_hypertension.md`
- `careplan_hyperlipidemia_ascvd.md`
- `careplan_osteoporosis.md`
- `careplan_mdd.md`
- `careplan_gad_panic.md`
- `careplan_bipolar_maintenance.md`
- `careplan_schizophrenia_maintenance.md`
- `careplan_migraine.md`
- `careplan_chronic_pain_multimodal.md`
- `careplan_hiv_management.md`
- `careplan_hcv_treatment.md`
- `careplan_ibd_crohns_uc.md`
- `careplan_rheumatoid_arthritis.md`
- `careplan_parkinsons.md`

### Lane 6 — Critical & Acute Care (12)
- `acute_vasopressor_selection.md`
- `acute_mechanical_ventilation_settings.md`
- `acute_ards_management.md`
- `acute_dka_protocol.md`
- `acute_hhs_protocol.md`
- `acute_status_epilepticus.md`
- `acute_massive_transfusion_protocol.md`
- `acute_severe_hyperkalemia.md`
- `acute_hypertensive_emergency.md`
- `acute_stroke_tpa_thrombectomy.md`
- `acute_acs_management.md`
- `acute_gi_bleed.md`

### Lane 7 — Specialty Assessments & Workflows (18)
- `specialty_derm_lesion_analysis.md`
- `specialty_red_eye_workup.md`
- `specialty_acute_vision_loss.md`
- `specialty_vertigo_hints_exam.md`
- `specialty_pharyngitis_centor.md`
- `specialty_thyroid_nodule_workup.md`
- `specialty_adrenal_incidentaloma.md`
- `specialty_hypercortisolism_workup.md`
- `specialty_cytopenia_workup.md`
- `specialty_thrombophilia_workup.md`
- `specialty_pancreatitis_severity_management.md`
- `specialty_autoimmune_workup_ana.md`
- `specialty_immunocompromised_fever.md`
- `specialty_hiv_initial_visit_art.md`
- `specialty_solitary_pulmonary_nodule_fleischner.md`
- `specialty_ild_workup.md`
- `specialty_dialysis_modality_decision.md`
- `specialty_drug_allergy_delabeling.md`

### Lane 8 — AI-Native Clinical Workflows (10)
- `workflow_longitudinal_chart_summarization.md`
- `workflow_ed_visit_summary_for_pcp.md`
- `workflow_inbox_message_triage.md`
- `workflow_specialty_consult_question_composer.md`
- `workflow_problem_list_builder_from_notes.md`
- `workflow_pre_visit_summary.md`
- `workflow_post_visit_avs_generator.md`
- `workflow_patient_portal_message_draft.md`
- `workflow_care_gap_surfacer.md`
- `workflow_risk_stratification_narrative.md`

### Lane 9 — Documentation (10)
- `doc_full_hp.md`
- `doc_soap_note.md`
- `doc_discharge_summary.md`
- `doc_operative_note.md`
- `doc_procedure_note.md`
- `doc_code_blue_rrt_note.md`
- `doc_death_note.md`
- `doc_critical_care_daily_note.md`
- `doc_telephone_refill_note.md`
- `doc_consult_note_formal.md`

---

## Authoring Standards

### Frontmatter
Standard repo schema:

```yaml
---
title: "Descriptive Title"
category: domain-healthcare-clinical/<lane-subdir>
description: "One-line purpose statement"
techniques:
  - ST-02
  - ST-03
  - CM-01
  - RT-02
  - RT-05
difficulty: intermediate|advanced
tags:
  - <specialty>
  - <task-type>
updated: "YYYY-MM-DD"
---
```

### Body Sections (Required)
1. **Objective** — what the prompt produces
2. **Inputs / Context** — patient parameters, data, results to be supplied
3. **Reasoning Steps** — explicit multi-step logic the model must execute
4. **Output Format** — structured deliverable (assessment + plan with concrete drug/dose/duration where applicable)
5. **Worked Example** — one fully-worked input → output illustration

### Body Sections (Excluded)
- No "Disclaimers" section
- No "When to Escalate" section in the prompt body (escalation is part of clinical reasoning output, not metaprompt scaffolding)
- No "Limitations of AI" framing
- No GRADE/uncertainty hedging unless the actual clinical task requires confidence calibration (e.g., probability estimation prompts)
- No "consult a licensed professional" boilerplate

### Voice & Stance
The prompt instructs the model to respond as a senior attending in the relevant specialty, writing for a peer colleague. Output should read like a sign-out, a curbside consult, or a chart note — direct, prescriptive, specific. Drug names with doses, durations, monitoring parameters. Differentials with concrete next steps. Not "consider obtaining a CBC" but "draw CBC, BMP, lactate, blood cultures x2 before antibiotics."

### Technique Stack
Default for all Lane 1–9 prompts:
- **ST-02** Sequential Instructions (multi-step clinical logic)
- **ST-03** Output Specification (structured deliverable)
- **CM-01** Context Framing (required patient inputs)
- **RT-02** Role Persona (senior attending in [specialty])
- **RT-05** Evidence-Based (named guidelines, trials, decision rules)

Add as situationally needed:
- **CR-01/02** Chain-of-Thought when mechanism reasoning matters (Lane 1)
- **QA-01** Chain-of-Verification for high-stakes calculations (Lane 4 dosing)
- **DS-02** Decomposition for multi-system care plans (Lane 5)

---

## Naming Conventions (per lane)

| Lane | Prefix | Subdir |
|---|---|---|
| 1 | `patho_` | `prompts/pathophysiology/` |
| 2 | `interp_` | `prompts/interpretation/` |
| 3 | `workup_` | `prompts/reasoning/` |
| 4 | `pharm_` | `prompts/pharmacology/` |
| 5 | `careplan_` | `prompts/care-plans/` |
| 6 | `acute_` | `prompts/acute-care/` |
| 7 | `specialty_` | `prompts/specialty/` |
| 8 | `workflow_` | `prompts/workflow/` |
| 9 | `doc_` | `prompts/workflow/` |

---

## Maintenance Notes

- `PROMPT_INDEX.json` and `PROMPT_INDEX.md` paths for the existing 41 prompts changed during reorganization. Run index regeneration after Phase 1 completion.
- The `field_guide.md` has been updated to remove safety-overlay disclaimers consistent with v2 framing.
- The README still contains v1 framing in places; rewrite scheduled after Phase 1.
