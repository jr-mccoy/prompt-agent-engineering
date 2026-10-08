# Quality Backfill — Corrections Log

**What this is.** While the 2026-10 quality backfill added False-Positive Prevention
sections to existing prompts (see [`COVERAGE_ROADMAP.md`](COVERAGE_ROADMAP.md), *Quality
backfill*), the reviewers who read each file in full flagged content that was wrong in
the prompt itself, mostly in worked examples: arithmetic that did not add up, an example
that broke its own file's rules, a reversed pathway, a dose that disagreed with a
long-standing standard. Those flags were not fixed silently inside the FPP batches. Each
one went through a separate correction pass (batches C-A onward in the roadmap) and is
recorded here so a licensed reviewer can audit every change to clinical teaching
material.

**This log is for a reviewer, not a substitute for one.** Every healthcare-clinical prompt
still carries its *Review status: not yet reviewed by a licensed clinician* line.

## How each flag was decided

| Outcome | Meaning |
|---|---|
| **Rejected** | On reading the file the flag was wrong or the text defensible; nothing changed. |
| **Fixed** (internal) | Arithmetic, unit, count, step-order or self-contradiction errors, recomputed from the file's own data and rules. Where an example's output used values absent from its input, the value was either added to the input or replaced with `[not provided]`. |
| **Fixed** (fact) | Only well-established, uncontroversial facts (a formula with the wrong variable, a pathway in reverse, a drug class mislabelled, a tenfold dose error against a long-standing standard dose). Minimal edit. |
| **`[VERIFY: source]`** | Guideline-dependent, recently changed, contested or jurisdiction-specific claims. The specific number or claim was neutralised and the named source to check was inserted. No replacement value was supplied from memory. |

No new dose, threshold or interval was introduced except to make a worked example agree
with the file's own figures, or to restore a long-standing standard dose; each such case
is named in its row. Perianesthesia prompts follow their toolkit's `SAFETY_PREAMBLE.md`:
corrections there use *per provider order* / *per facility protocol* rather than numbers.
Rows marked **Safety** were errors that could mislead a clinician or learner toward harm.

## Healthcare-clinical

Paths are relative to `domain-healthcare-clinical/` (most sit under `prompts/<area>/`).

| File | Correction | Outcome |
|---|---|---|
| `careplan_hfref_gdmt.md` | ARNI start condition reworded to the label's (no or low-dose ACEi/ARB); example start 24/26 with titration; iron rule "ferritin <100, or 100–299 with TSAT <20%" | Fixed; low-dose ACEi definition `[VERIFY]` |
| `careplan_cirrhosis.md` | Albumin "6–8 g per litre removed"; example's SBP-prophylaxis claim neutralised | Fixed; prophylaxis criteria `[VERIFY]` |
| `careplan_ibd_crohns_uc.md` | Infliximab maintenance 8 → 5 mg/kg q8w (label); HSTCL caveat added for thiopurine + anti-TNF in a young man | Fixed |
| `careplan_gad_panic.md` | Example clonazepam now scheduled, matching step 5 | Fixed |
| `careplan_asthma_stepwise.md` | Action-plan placeholder "reliever >X/day" → `[not provided]` + label check | Fixed |
| `careplan_migraine.md` | ~13 triptan days/month now stated as meeting the ≥10-day overuse threshold | Fixed |
| `careplan_t1dm.md` | Urgent-low alarm per device (fixed at 55 mg/dL on some CGMs); TDD from actual doses, weight estimate only a cross-check | Fixed |
| `careplan_parkinsons.md` | COMT inhibitor with peak-dose dyskinesia now paired with a levodopa reduction | Fixed |
| `careplan_schizophrenia_maintenance.md` | Clozapine REMS statement | `[VERIFY: current label / FDA REMS]` |
| `careplan_post_mi_secondary_prevention.md` | Blanket "beta-blocker ≥1 year" for preserved EF | `[VERIFY: ACC/AHA / ESC]` |
| `medicine_chronic_disease_management_planner.md` | Beta-blocker/COPD conflict narrowed to non-selective agents | Fixed |
| `medicine_geriatric_care_assessment.md` | MMSE 18–23 no longer labelled MCI | Fixed |
| `medicine_chronic_disease_registry_outreach_priority.md` | Sample row interval 7 → ~6 months | Fixed |
| `medicine_care_coordination_transitions.md` | Unsourced adverse-event percentages made qualitative | `[VERIFY: Forster 2003]` |
| `perianesthesia/*` (16 files) | Phase 2 ≠ step-down; Aldrete example scores all five categories; O2 "per order"; impossible causes removed from a hemodynamic sweep; residual NMB replaces hypercarbia as rival hypothesis; recurarization (not re-sedation); NPPE timing; I-PASS label; one-liner keeps "+ sedation"; OIRD wording; laryngospasm readiness; escalation example; capstone checks all five ⚠ domains; unsourced deck card marked unverified | Fixed; bladder on hypotension sweep `[VERIFY]` |
| `interp_abg_acid_base.md` | A–a gradient formula (− PaO2, not − PaCO2); Berlin P/F categories | Fixed; DKA resolution criteria `[VERIFY]` |
| `interp_coagulation_panel.md` | ISTH example arithmetic (total 7) with lab PT range added to the input; FFP volume needs weight | Fixed; vitamin K, protamine window, andexanet `[VERIFY]` |
| `interp_lft_pattern.md` | Late low acetaminophen level explained as elimination | Fixed; King's College lactate criterion `[VERIFY]` |
| `interp_urinalysis_microscopy.md` | Proteus nitrite-positive in both steps; ACE inhibitor needs hCG first | Fixed |
| `interp_cxr_systematic_read.md` | Example input now describes the film; no CT ratio on an AP film; furosemide dose explained | Fixed; dose `[VERIFY]` |
| `interp_cmp_bmp.md` | Tonicity not asserted without osmolality; KDIGO stage 3 wording | Fixed |
| `medicine_lab_diagnostic_interpreter.md` | Pseudothrombocytopenia is an EDTA artifact (heparin → HIT); BNP in CKD/AF is a true elevation | Fixed |
| `interp_cbc_differential.md` | RDW described as supportive, not discriminating | Fixed |
| `patho_fluid_electrolyte_mechanism.md` | Purine order hypoxanthine → xanthine → uric acid | Fixed; TLS targets `[VERIFY]` |
| `patho_pulmonary_physiology.md` | Bohr–Enghoff uses mixed-expired CO2; bosentan/macitentan dual ETA/ETB | Fixed; shunt rule `[VERIFY]` |
| `patho_inflammation_immunology_mechanism.md` | Etanercept is a TNFR2–IgG1 Fc fusion; trial percentages made qualitative | Fixed + `[VERIFY]` |
| `patho_microbial_pathogenesis.md` | PVL forms its own LukS/LukF pore | Fixed; vancomycin monitoring `[VERIFY]` |
| `workup_lymphadenopathy.md` | B-symptom criteria not claimed without baseline weight or measured temperature; allopurinol removed before tissue diagnosis | Fixed; TLS prophylaxis `[VERIFY]` |
| `workup_rash_differential.md` | RMSF centripetal spread; EM minor vs major mucosal involvement | Fixed |
| `workup_joint_pain_arthritis.md` | Lyme arthritis is late disease | Fixed; vancomycin target, HLA-B*5801 populations `[VERIFY]` |
| `medicine_prenatal_risk_stratification.md` | Aspirin dose and accreta level of care | `[VERIFY: USPSTF/ACOG; ACOG/SMFM]` |
| `workup_aki.md` | Metformin restart by eGFR; pre-renal Cr should fall within 24–72 h | Fixed; HRS-AKI criteria `[VERIFY]` |
| `workup_altered_mental_status.md` | CT justified by the file's age rule (no anticoagulant); bolus needs a weight | Fixed; fluid trigger `[VERIFY]` |
| `workup_anemia.md` | Hgb 8.4 is above threshold 8; IRONOUT citation removed | Fixed; MINT/FOCUS `[VERIFY]` |
| `workup_chest_pain.md` | Single troponin below the rule-in value → "suspected NSTEMI pending 1-h hsTn"; "dynamic" needs serial ECGs | Fixed; ADD-RS cutoff `[VERIFY]` |
| `workup_dyspnea.md` | NT-proBNP 450/900/1800 relabelled rule-in | Fixed; rule-out cutoff and diuresis targets `[VERIFY]` |
| `workup_fever_unknown_origin.md` | CRP not graded without units | Fixed; HLH-2004 ferritin `[VERIFY]` |
| `workup_hematuria.md` | Low-risk band <10 pack-years; 30 pack-years is intermediate | Fixed |
| `medicine_incidental_findings_management.md` | "Fleischner 4a" → Lung-RADS 4A | Fixed |
| `medicine_surgical_preoperative_assessment.md` | ACC/AHA (not ACS/AHA); prasugrel 7 d, clopidogrel/ticagrelor 5 d | Fixed; GLP-1 hold, valve bridging, RCRI figures `[VERIFY]` |
| `medicine_em_coding_level_justification.md` | AMA 2021 "Limited" data row | Fixed; consult codes, time table `[VERIFY]` |
| `workflow_care_gap_surfacer.md` | Mammogram 3 yr on a 2-yr interval is overdue | Fixed; RSV eligibility `[VERIFY: ACIP]` |
| `pharm_antidepressant_selection_switching.md` | Retired pregnancy letter categories → label narrative; switch plan on one Day-1 count; selegiline TD tyramine threshold | Fixed |
| `pharm_insulin_regimen_design.md` | RABBIT-2 strata by admission glucose; PLLR wording | Fixed; detemir availability `[VERIFY]` |
| `pharm_iv_to_po_conversion.md` | Metoprolol and levothyroxine IV↔PO ratios no longer stated from memory | `[VERIFY: label]` |
| `pharm_antipsychotic_selection.md` | CAFE citation removed for aripiprazole; clozapine titration reaches target; invented baseline labs → `[not provided]` | Fixed; clozapine REMS `[VERIFY]` |
| `pharm_antiepileptic_selection.md` | Lamotrigine inducer ladder; follow-up visits match titration | Fixed; contraception advice `[VERIFY]` |
| `pharm_antihypertensive_selection.md` | Non-DHP CCB avoidance moved to HFrEF; escalation reaches the dose it cites | Fixed; thiazide claims `[VERIFY]` |
| `pharm_chemotherapy_regimen_explainer.md` | Olanzapine not attributed to NEPA; ranitidine (withdrawn) removed; "diphenhydramine" | Fixed; cetuximab rash rule `[VERIFY]` |
| `pharm_doac_selection_by_profile.md` | Example CrCl recomputed (25, Cockcroft-Gault × 0.85); US vs EU edoxaban criteria separated | Fixed + `[VERIFY]` |
| `pharm_immunosuppression_regimen.md` | BLISS-LN (not NEPTUNE) for belimumab; TMP-SMX/tacrolimus and rotavirus contradictions; HCC surveillance for chronic HBV | Fixed |
| `pharm_inhaler_regimen_asthma_copd.md` | Dupilumab not credited for rhinitis; pMDI default where Turbuhaler isn't marketed | Fixed |
| `pharm_benzodiazepine_taper.md` | Day 1–3 crossover sums to 15 mg diazepam-equivalent | Fixed |
| `medicine_anticoagulation_decision_support.md` | Warfarin pregnancy wording; AF threshold not left unstated | `[VERIFY]` |
| `patho_drug_mechanism_deep_dive.md` | Empagliflozin ~54% urine / ~41% feces; euglycemic DKA on-target; SGLT1 in late proximal tubule (S3) | Fixed |
| `medicine_pediatric_clinical_reasoning.md` | **Safety:** unvaccinated children get a *lower* workup threshold | Fixed; febrile infant pathway, amoxicillin max `[VERIFY: AAP]` |
| `workup_syncope.md` | **Safety:** echo before stress testing (exclude severe AS/HCM); CSRS example re-scored (+2, medium) | Fixed |
| `medicine_addiction_medicine_assessment.md` | **Safety:** precipitated withdrawal follows buprenorphine after recent full agonist; "Disulfiram" | Fixed |
| `workup_hyperkalemia.md` | Example holds metoprolol with HR 52 and conduction delay; hemolysis index "not reported" | Fixed; TTKG cutoff, SZC dose `[VERIFY]` |
| `patho_cardiac_hemodynamics.md` | Pressure-overloaded RV becomes diastole-dependent; raised SvO2 points to a shunt; pulse pressure in AS vs AR; "submassive" PE | Fixed; dobutamine, heparin with alteplase `[VERIFY]` |
| `patho_endocrine_axis_dysfunction.md` | ACTH-dependent Cushing's *syndrome* (pituitary vs ectopic); 6 mm lesion vs "<6 mm" rule | Fixed; assay cutoffs `[VERIFY]` |
| `patho_acid_base_mechanism.md` | Hypokalemia–alkalosis mechanism (intracellular acidosis + H+/K+-ATPase) | Fixed; K replacement rate `[VERIFY]` |
| `patho_disease_mechanism_explainer.md` | Bicarbonate pH threshold | `[VERIFY: ADA]` |
| `patho_oncogenesis_tumor_biology.md` | 2-HG inhibits TET/JmjC demethylases (hypermethylation); HER2CLIMB-04 miscitation removed | Fixed |
| `patho_pharmacodynamics_receptor.md` | Barbiturates allosteric with direct gating at high concentration; ethanol's GABA-A site described as debated | Fixed |
| `patho_genetics_phenotype_mechanism.md` | Ivacaftor variant count | `[VERIFY: label]` |
| `patho_renal_physiology.md` | Gitelman hypocalciuria: both proposed mechanisms given | Fixed |
| `workflow_inbox_message_triage.md` | K 6.5 on two K-retaining drugs → call now, hold both, ED for ECG + repeat (the file's own EMERGENT rule); same-patient check before refill | Fixed; gabapentin renal dose, local K protocol `[VERIFY]` |
| `workflow_longitudinal_chart_summarization.md` | Metformin at eGFR 38 flagged; example input now states the records were pasted | Fixed |
| `workflow_ed_visit_summary_for_pcp.md` | Invented details moved into the input or removed; pending status "not supplied" | Fixed; Fleischner category and interval `[VERIFY]` |
| `workflow_problem_list_builder_from_notes.md` | I13.0 (presumed HTN–HF–CKD link) with coder check; unsupported entries removed | Fixed |
| `workflow_risk_stratification_narrative.md` | LACE C value from Charlson (2, 3 or 5) and totals 11/12/14 | Fixed (reviewer: check the Charlson-to-points conversion) |
| `workflow_specialty_consult_question_composer.md` | Underivable scores and invented vitals/labs → `[not provided]` | Fixed |
| `workflow_post_visit_avs_generator.md` | Glucose-number DKA warning replaced for a patient on dapagliflozin (euglycemic DKA) | Fixed |
| `clinical_decision_support_template.md` | CURB-65 example: only the age point is derivable | Fixed |
| `patient_education_template.md` | Hypoglycemia warning added; health literacy vs reading grade separated | Fixed |
| `psychiatric_assessment_template.md` | Duty-to-warn and crisis lines marked jurisdiction-specific | Fixed |
| `nursing_quick_reference_handbook_creator_prompt.md` | **Safety:** nurse-initiated 30 mL/kg bolus → notify provider, bolus per order/protocol; TJC publishes a Do-Not-Use list, not an approved list; PACU use defers to the SAFETY_PREAMBLE | Fixed |
| `nursing_pacu_prioritization_rule.md` | Complete laryngospasm is Tier 1; pain threshold per protocol; collision rows agree | Fixed |
| `nursing_orientee_pattern_import_check.md` | PACU BP drop: rule out bleeding and volume first | Fixed |
| `nursing_sbar_clinical_escalation.md` | Rapid response callable at any step | Fixed |
| `nursing_preceptor_fumble_postmortem.md` | "Near-miss with patient harm" removed (a near-miss causes no harm) | Fixed |
| `acute_acs_management.md` | STEMI V2–V3 men ≥40 clause; example weight stated | Fixed; primary-PCI heparin regimen `[VERIFY]` |
| `acute_ards_management.md` | Example height 172 cm so PBW 68 kg and tidal volumes agree | Fixed; PEEP-FiO2 table values `[VERIFY: ARDSNet]` |
| `acute_massive_transfusion_protocol.md` | TEG: prolonged K / reduced alpha angle; binder at the greater trochanters; SBP target with possible TBI; fibrinogen 180 vs the <150 trigger | Fixed |
| `acute_mechanical_ventilation_settings.md` | 1:1.5 is not inverse ratio; ECMO pH aligned with EOLIA (<7.25) | Fixed |
| `acute_hhs_protocol.md` | UFH chosen at CrCl ~27 (file's own rule); anion gap 20 worked and explained | Fixed; resolution osmolality, insulin TDD `[VERIFY]` |
| `acute_hypertensive_emergency.md` | Post-thrombectomy BP target | `[VERIFY: AHA/ASA]` |
| `acute_gi_bleed.md` | No INR correction for a cirrhotic variceal bleed; AIMS65 ≤/≥; GBS computed (16); "elderly" removed | Fixed; Baveno VII `[VERIFY]` |
| `acute_stroke_tpa_thrombectomy.md` | BP-TARGET was neutral; later trials showed harm of intensive lowering | Fixed; targets and ASPECTS `[VERIFY]` |
| `acute_severe_hyperkalemia.md` | Type 4 RTA named correctly; example acidosis criterion from step 4 | Fixed; renal-failure insulin regimen `[VERIFY]` |
| `acute_vasopressor_selection.md` | Angiotensin II starting dose 20 ng/kg/min (label) | Fixed; peripheral limits `[VERIFY]` |
| `acute_status_epilepticus.md` | Eclampsia labetalol escalation and MAP floor | `[VERIFY: ACOG]` |
| `medicine_emergency_triage_decision_support.md` | LBBB alone is not a STEMI equivalent (Sgarbossa); ESI resources counted by type | Fixed; qSOFA, door-to-needle `[VERIFY]` |
| `examples/building_anticoagulation_decision_support.md` | COMPASS row not applied to AF; CrCl 15–30 row defers to labels; one Xa-reversal statement; ESC 2024 | Fixed + `[VERIFY]` |
| `careplan_afib.md` | Apixaban dose needs measured creatinine; score version tied to its guideline | Fixed + `[VERIFY]` |
| `pharm_anticoag_periprocedural_bridging.md` | **Safety:** DOAC last dose D−2 (low bleed) / D−3 (high bleed) per PAUSE in steps, Output Format and example; 4 skipped doses for q12h; LMWH last dose ~24 h; andexanet >5 mg threshold; CHA2DS2-VASc recomputed (6); "dabigatran" | Fixed; neuraxial INR, dabigatran neuraxial hold, valve text `[VERIFY: ASRA / CHEST]` |
| `pharm_pediatric_weight_based_dosing.md` | **Safety:** ES-600 escalation 6.25 → 4.1 mL BID (≈89 mg/kg/day); AOM severity by the file's ≥39 °C rule; IV/IO arrest epinephrine max 1 mg; codeine restriction per the 2017 FDA scope | Fixed |
| `pharm_pregnancy_lactation_drug_safety.md` | **Safety:** newborn vitamin K 10 → 1 mg IM; valproate→lamotrigine cross-taper reaches target; NSAID avoidance from 20 weeks | Fixed; peripartum anticoagulant switch `[VERIFY]` |
| `pharm_vancomycin_auc_dosing.md` | **Safety:** example dose now matches its AUC estimate (1000 mg q12h ≈ 505); proportional adjustment lands in range; KDIGO 7-day window; AUC trapezoid term | Fixed |
| `pharm_tdm_interpretation.md` | Digoxin example arithmetic in mg/day; DigiFab vials = body load ÷ 0.5 mg; HFrEF target range | Fixed; AF range `[VERIFY]` |
| `pharm_opioid_equianalgesic_conversion.md` | One conversion throughout (240 MME → 25 µg/h, ≈58% reduction); the file's own 50% criteria applied | Fixed; tramadol factor `[VERIFY: CDC 2022]` |
| `pharm_opioid_taper.md` | Steps within the stated 5–10%; leftover scratch text removed | Fixed |
| `pharm_steroid_taper_design.md` | Taper dates 8 weeks apart; non-overlapping risk classes; REDUCE (COPD); sarilumab is the PMR approval | Fixed + `[VERIFY]` |
| `pharm_adverse_drug_reaction_naranjo.md` | Aztreonam shares its side chain with ceftazidime (a cephalosporin); pending items score 0 (total 4, Possible); item range −1 to +2 | Fixed |
| `medicine_antibiotic_stewardship_advisor.md` | Nitrofurantoin at low GFR: failure *and* toxicity; ciprofloxacin ~70–80% bioavailable; procalcitonin units | Fixed; carbapenem after SJS/TEN/DRESS `[VERIFY]` |
| `pharm_aminoglycoside_dosing.md` | Synergy peak 3–4 mg/L in both places; CrCl weight shown (IBW vs AdjBW) | Fixed; AHA duration `[VERIFY]` |
| `patho_pharmacokinetics_reasoning.md` | **Safety:** AUC24 unit error (≈968, not 40) that had reversed "underdosed"; half-life text; aminoglycoside Vd ~0.25–0.3 L/kg | Fixed; trough target `[VERIFY]` |
| `doc_*` (10 documentation prompts) | Worked-example outputs no longer contain details absent from their inputs; contradictions fixed ("Pending: None" vs pending sputum; afebrile vs Tmax; "present at bedside" vs "supervised"; 14 vs ">12" months); CURB-65 shown item by item | Fixed; sepsis definition and CAP amoxicillin dose `[VERIFY]` |
| `workup_aki.md` | Example stages by creatinine (2.0× → Stage 2); urine-output criterion not applied without weight | Fixed; BUN/Cr flag rejected (58 ÷ 2.8 ≈ 21) |
| `workup_dyspnea.md` | One negative troponin no longer excludes ischemia; serial per assay | Fixed |
| `acute_gi_bleed.md` | Platelet transfusion threshold and example target defer to current guidance | `[VERIFY: ACG/ESGE; Baveno VII/AASLD]` |
| `acute_mechanical_ventilation_settings.md` | PEEP 14 labelled as the step-5 severity band, not an ARDSNet table row | Fixed; PEEP band, PBW and driving-pressure flags rejected (arithmetic correct) |

## Medical education

| File | Correction | Outcome |
|---|---|---|
| `domain-medical-education/profession-specific/allied/prof_rt_clinical_competency.md` | **Safety:** complication data now points to auto-PEEP (symmetric sounds, midline trachea); decompress without waiting for imaging if BP fails or asymmetry appears | Fixed + `[VERIFY: ATLS]` |
| `domain-medical-education/learner-procedures/study_code_leader_rehearsal.md` | **Safety:** audit flags a delayed first shock in monitored VF, epinephrine before the second shock, and the missed compressor swap | Fixed |
| `domain-medical-education/` (12 more learner files) | SIADH urine Na high; NPTE HFrEF teardown; NAPLEX pitfall; NCLEX +/- scoring; DDx scores; Step 1 pass/fail; schedule, spaced-repetition and Anki arithmetic; wellness bands; pre-brief grade scale and bailout service; suture knot row | Fixed + `[VERIFY]` where guideline-dependent |
| `domain-medical-education/` (16 reasoning/rotation/anatomy files) | Word counts, tallies and verdicts recomputed; data leaks removed; morning-report example rebuilt as a coherent CT-negative SAH; anatomy order and levels; urea-cycle table | Fixed; LP-after-CT, sepsis mortality, RUSP `[VERIFY]` |
| `domain-medical-education/` (20 science and OSCE files) | Pedigree priors and symbols; MS-AFP and meningocele; EBV glycoproteins; ceftriaxone covers MSSA; angiotensinogen is hepatic, AT-I plasma; OSCE scorecards matched to transcripts; Mini-Cog total | Fixed; CLSI breakpoints, APL therapy, herb interactions `[VERIFY]` |
| `domain-medical-education/` (9 curriculum, case-writing and assessment files) | Course-map example now has 12 weeks, 4 CLOs and reports unmapped exam items (reflective essay retagged CLO5 → CLO2 — **reviewer to confirm**); microlecture timeline reaches 10:00; virtual-patient outcome paths rebuilt from the path list; remediation standard judged on ≥ 8 of the last 10 cases; progress-test anchor refresh every 3 administrations (the file's retire-after-3 rule); question-bank retire count shown with an unattributed remainder; TBL stipulation moved into the learner stem; grand-rounds title no longer gives away the diagnosis | Fixed; LCME integration element and apixaban dose-reduction criteria `[VERIFY]` |
| `domain-medical-education/` (10 boards, reasoning and simulation files) | Progressive-disclosure model answers no longer use later-stage data; pre-brief lists only the manikin's stated capabilities; Step 1 treated as pass/fail (230 is a practice-form target); compare-contrast false-discriminator count 3 → 2; HPI stage no longer reveals the warfarin history; red-herring bacteriuria no longer credited for treatment; NREMT pupil check earned; COMLEX RA contraindication class made consistent | Fixed; DKA consensus thresholds, pediatric doxycycline age limit, CCTA vs stress test as keyed answer, asymptomatic bacteriuria, OPP contraindication text `[VERIFY]` |
| `domain-medical-education/profession-specific/` (13 dental, EMS, nursing, PA and pharmacy files) | CHA2DS2-VASc spelling; OLMC observation window honoured before refusal; naloxone half-life shorter than the opioid's action; sildenafil named as the nitrate contraindication (critical clue, not distractor); GCS 15 for an oriented patient; Bondy 1983; NGN matrix rows keyed to one hypothesis, matrix-multiple-choice format, no invented pass thresholds; concept-map arrow and PES rule; preceptor gates match the schedule; Benner "competent" is post-orientation; PANCE trap names option B and nitroglycerin removed from the inferior-STEMI key; journal-club rubric scores match anchors | Fixed; BVM rate, ACS SpO2 threshold, ACPE edition, AACP EPA titles, ACH/ACHR definitions, ASHP objective wording, PAEA blueprint, NANDA-I labels `[VERIFY]` |
| `domain-medical-education/` (14 boards, reasoning and profession-specific files, round 2) | Discriminating-fact quotes now verbatim; PANCE pearl 3 is "diagnosis is clinical", EM not taught as a target lesion, Lyme stages correct; submassive PE defined without hypotension; compare-contrast counts exclude the post-hoc treatment row (5/8); COMLEX contraindication classes match the Method and option D now excluded by the stem; EMS run-call quotes no longer contain reviewer text and the CSC window is labelled as not in the supplied protocol; NGN non-discriminating calf row removed (3/5); preceptor gate matches supervised titrations, codes census-dependent with substitute; APPE safety-event trigger added to Method | Fixed; dental INR cut-off and warfarin half-life, pretest-probability tool, neurologic-Lyme route, NANDA-I label, ASHP objective wording `[VERIFY]`; one misattributed flag rejected |
| `domain-medical-education/` (10 educator files, round 2) | Course-map redundancy audit now flags 4 same-Bloom pairs and the untagged progress test; virtual-patient graph, paths and an added N3-blind node agree; integration-audit gap counts recomputed from its heatmap; progress-test anchors all carry forward; question-bank action no longer refreshes retired items and states the export supplied; TBL stem now supports CHA2DS2-VASc 4 / HAS-BLED 3; grand-rounds H-Score marked not computable without Tmax, ferritin claim softened; disclosure distractor at the stage the data appears, model table labelled illustrative; pre-brief names a real limitation, uses "sim pause" and a teach-back; study calendar sums to 42 days with targets recomputed | Fixed; lytic re-key, apixaban dose criteria, Fardet/Eloseily/adult-HLH citations, malaria regimen, recording and grading policy `[VERIFY]` |

## Image generation

| File | Correction | Outcome |
|---|---|---|
| `domain-image-generation/` (2 Nano Banana files) | JSON-schema builder example now obeys its own rules (≤ 3 levels, rule-named keys, no API settings in the schema, every declared variable used); multi-angle composite slot table and prompt number references the same way, side panel has a reference | Fixed |
| `domain-image-generation/healthcare/nursing_badge_buddy_critical_drips.md` | Start/titrate lines carry units from the file's own reference table (titrate units derived from start/max — **reviewer to confirm**); verification checklist added | Fixed; dopamine band units `[VERIFY: institutional drip protocol]` |
| `domain-image-generation/healthcare/nursing_badge_buddy_critical_drips.md` (round 2) | **Safety:** norepinephrine no longer listed as first-line for hypovolemic shock; renal-dose dopamine band removed; dopamine bands moved out of the Start/Titrate/Max columns | Fixed; vasopressin fixed-vs-range, lidocaine bolus rate, BP and MAP targets `[VERIFY]` (must be resolved before printing) |
| `domain-image-generation/nano-banana/nanobana_product_multi_angle_composite.md` (round 2) | `Quality: "high"` removed from prompt text (it is an API parameter) | Fixed |

## Link repair

`related_prompts` entries that still pointed at pre-reorganisation paths (the old flat
`prompts/<file>.md` layout, the retired `learner_*` medical-education names, and the
renamed `visual-planning/` files) were repointed to each file's current location, using
[`REORG_MAP.tsv`](REORG_MAP.tsv) where a file was renamed. Entries whose target no longer
exists anywhere were removed. The counts are in the roadmap's batch table (rows L-1 and L-2).

## Open, not fixed

These are genuine defects that reviewers noticed but nobody had flagged. They were left
as they are because fixing them needs a clinician's judgement, or because they fall
outside this backfill's scope.

### Clinical content (needs a clinician)

| File | Observation |
|---|---|
| `domain-healthcare-clinical/prompts/reasoning/workup_dyspnea.md` | Example lists "B-lines expected", "plethoric IVC expected" and "S3 likely" as findings, against the file's own rule that an unperformed POCUS is not a finding; "BNP 2400 confirms HF" may overstate. |
| `domain-healthcare-clinical/prompts/reasoning/workup_aki.md` | Example uses supplied FeNa/FeUrea although the file's rule says compute from raw values or print "not computable". |
| `domain-healthcare-clinical/prompts/acute-care/acute_mechanical_ventilation_settings.md` | Step 5 still pairs "higher PEEP per ARDSNet table" with severity bands; the example's EOLIA ECMO criteria were not checked. |
| `domain-image-generation/healthcare/nursing_badge_buddy_critical_drips.md` | Dopamine bands and units, vasopressin, lidocaine and BP/MAP targets carry `[VERIFY]` tags that must be resolved against the institutional pump library before the badge is generated, or the tags will print. |
| `domain-medical-education/profession-specific/nursing/prof_rn_clinical_judgment_ngn_drill.md` | The BP row still has two defensible columns (the teardown says "hemorrhage possible"); fixing it means rewriting the case data. |
| `domain-medical-education/learner-clinical-reasoning/reason_compare_contrast_two_diagnoses.md` | Swing features are called "large" with no likelihood ratio or source behind them. |
| `domain-medical-education/profession-specific/ems-paramedic/prof_ems_run_call_critique.md` | "Cortical assessment" and "Glucose check" rows cite requirements absent from the supplied protocol set and feed the 21/24 score. |
| `domain-medical-education/profession-specific/nursing/prof_rn_preceptor_orientation_plan.md` | Other census-dependent counts (1 code as primary RN, 2 CRRT runs, EOL observation) lack an "if available" substitute; one is a gate criterion. |
| `domain-medical-education/profession-specific/pharmacy/prof_pharm_pgy1_residency_eval.md` | R3.2.1 evidence bullets are undated; the "hepatic-adjusted dosing" strength has no evidence. |
| `domain-medical-education/educator-case-writing/case_grand_rounds_case_author.md` | Template row pairs "ferritin > 500" (an HLH-2004-style criterion) with the H-Score; H-Score sensitivity/specificity left under the citation's `[VERIFY]`. |
| `domain-medical-education/educator-case-writing/case_virtual_patient_script_author.md` | N4.B "transfer for cath" is keyed acceptable although on-site cath is available in 60 min. |
| `domain-medical-education/educator-case-writing/case_tbl_application_exercise_author.md` | Option C ("warfarin bridge … not standard in 2025") and the "ACC 2023 AF guideline — verified (limited)" source row are guideline-dependent and unchecked. |
| `domain-medical-education/educator-curriculum-design/curric_vertical_horizontal_integration_audit.md` | The ethics-capacity gaps shown in the heatmap are not carried into the gap summary or plan. |

### Outside this backfill's targets

- **Stale `related_prompts` in 15 non-target domains** (64 entries; most in software-engineering, decision-making, productivity and game-development). These are the same kind of stale link that link-repair parts 1–2 fixed in the target domains, and the same method applies. They were left alone because those domains were outside this backfill, and `domain-science` was explicitly excluded.
- **`category: medicine` in 37 healthcare-clinical prompts**, where their siblings use `domain-healthcare-clinical/<area>`. `category` is a search-indexed field, so normalising it is a routing change and should be measured as one. It was not bundled into this backfill.
