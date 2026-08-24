# Legal: Practitioner Prompt Library

Prompts for the actual day-to-day work of attorneys, paralegals, in-house counsel, legal operations, contract managers, and compliance professionals.

## Scope

This domain covers professional legal workflows: legal research, case analysis, contract review and drafting, redlining, discovery, deposition preparation, litigation strategy, regulatory compliance, risk assessment, due diligence, privilege review, client intake, matter summaries, legal memoranda, issue spotting, statutory interpretation, precedent comparison, and jurisdiction-specific analysis.

Prompts are written for sophisticated users who already know what they need. They omit generic "consult a licensed attorney" boilerplate and refusal hedging — those add no signal. Substantive guardrails (do not invent citations, do not assume the wrong jurisdiction, do not collapse fact-specific analysis) are encoded as testable constraints inside each prompt.

**Two exceptions: `family-self-advocacy/` and `personal-self-advocacy/`.** These two subsections *invert* this convention. They are written for **laypeople handling their own side** — self-represented or self-organizing litigants, not practitioners — and therefore carry a strong, load-bearing not-legal-advice boundary, a mandatory Safety Block, and explicit refusal of legal advice, strategy, citation, legal conclusions, and outcome prediction (those are routed to the user's attorney or the relevant authority). They *organize, document, and prepare* the user's own information — and, where a channel is designed for non-lawyers, help draft the user's own factual account/letter — for handoff to counsel or a channel; they do not generate court filings or authority. `family-self-advocacy/` covers **divorce and custody**; `personal-self-advocacy/` covers **non-family personal legal matters** (workplace, harassment/stalking, defamation, IP theft, consumer/scams, landlord–tenant, identity theft, debt collection, small claims). See [`family-self-advocacy/README.md`](family-self-advocacy/README.md) and [`personal-self-advocacy/README.md`](personal-self-advocacy/README.md).

## Directory Map (Phase 1 + Phase 2A + Family Law)

```
domain-legal/
├── divorce/                       Dissolution intake, petitions/responses, temporary orders,
│                                  financial disclosure, property characterization/division,
│                                  business valuation, retirement/QDRO, hidden-asset/dissipation,
│                                  tax, alimony, MSA, prenup/postnup (+ enforceability),
│                                  mediation prep + mediation brief + post-mediation term sheet/MOU,
│                                  discovery, trial prep, post-judgment, DV protective order
├── custody/                       Best-interests analysis, UCCJEA jurisdiction, custody
│                                  petitions/emergency motions, parenting plans + holiday
│                                  schedules, high-conflict provisions, child support,
│                                  modification, relocation/move-away, custody-evaluation
│                                  and GAL-report response, third-party/grandparent,
│                                  supervised visitation, enforcement/contempt, trial prep,
│                                  paternity/parentage, settlement/mediation prep, custody
│                                  mediation brief, mediation impasse/package strategy
├── family-self-advocacy/          LITIGANT-FACING (layperson, inverts the attorney convention):
│                                  organize-your-own-side prep for divorce/custody — case
│                                  chronology, evidence/exhibit index, communication/incident
│                                  records, financial-disclosure organizer, asset/debt inventory,
│                                  budget, allegation-response, hearing/deposition/custody-eval/
│                                  mediation prep, post-mediation follow-up + agreement review,
│                                  best-interests self-map, attorney handoff brief
├── personal-self-advocacy/         LITIGANT-FACING (layperson, inverts the attorney convention):
│                                  organize-your-own-side prep for NON-FAMILY personal legal
│                                  matters — workplace, harassment/stalking, defamation/reputation,
│                                  IP theft, consumer/scams, landlord–tenant, identity theft,
│                                  debt collection, small claims. Cross-cutting anchors (router,
│                                  incident record, evidence preservation, chronology, handoff
│                                  brief, consultation questions) + matter-specific documentation
│                                  organizers, logs, and self-submit narrative preparers (HR
│                                  complaint, police account, DMCA notice, FTC/agency report,
│                                  dispute letters). Not legal advice.
├── research/                      Issue spotting, IRAC memos, statutory interpretation,
│                                  case briefs, precedent comparison, jurisdiction splits
├── litigation/                    Complaints, answers, dispositive motions, case strategy,
│                                  settlement valuation, jury instructions, MILs, trial themes, budgets
├── discovery/                     RFPs, interrogatories, responses, privilege logs/protocols,
│                                  meet-and-confer, custodian interviews, review taxonomies
├── depositions/                   Fact-witness outlines, 30(b)(6) outlines, deposition
│                                  summaries, witness prep, expert deposition prep
├── contracts-transactional/       Contract review/redline, risk heatmaps, MSA/SOW/NDA/DPA/SaaS/
│                                  license drafting, term-sheet translation, clause library,
│                                  negotiation position papers
├── corporate-ma/                  DD request lists, findings memos, disclosure schedules,
│                                  board resolutions, §409A/QSBS spotters, post-closing integration
├── employment-labor/              Offer/separation, workplace investigations, PIP/termination
│                                  risk, wage-hour classification, non-compete enforceability,
│                                  EEOC position statements
├── ip/                            Patent claim charts, trademark clearance, fair-use analysis,
│                                  DMCA takedown/counter-notice, OSS license compatibility
├── client-intake-communications/  Matter intake, engagement letters, demand letters,
│                                  client status updates
└── in-house-legalops/             Executive matter summaries, legal-spend anomalies,
                                   contract playbooks, intake triage, board legal updates
```

**Family law (delivered):** the planned Phase 2C `family/` set was built out as two dedicated, comprehensive subsections — `divorce/` (22 prompts) and `custody/` (20 prompts) — rather than a single five-prompt `family/` directory. The build folds in prenuptial/postnuptial drafting and enforceability, a DV protective-order petition, child-support calculation, and paternity/parentage establishment. A 2026-06-10 expansion added a full mediation set: divorce settlement/mediation prep, divorce and custody mediation brief drafters, a custody mediation impasse/package-strategy prompt, and a post-mediation term sheet/MOU drafter (plus two litigant-facing post-mediation organizers in `family-self-advocacy/`).

Phase 2B will add: regulatory-compliance, privacy-data, ethics-professional-conduct. Remaining Phase 2C: bankruptcy, tax, immigration, criminal, appellate, real estate, T&E. Phase 3: cross-cutting (litigation hold, 30(b)(6) notice, subpoenas, settlement, mediation, fee petitions, post-trial motions) + field guide. Phase 4: specialized topics.

## How These Prompts Are Built

Every prompt includes:
- **Required jurisdiction input** — federal/state/circuit. Doctrine and procedure diverge sharply by jurisdiction; outputs without it are unreliable.
- **Required governing law / venue / posture input** for litigation work; **required governing law + state of formation** for transactional work.
- **No-fabrication clause** — explicit instruction not to invent case names, statutory citations, regulatory provisions, or quoted text. If a citation is not supplied or knowable from the input, the model must say so rather than fill the gap.
- **Locked output format** — memo headers, motion captions, redline conventions, table schemas — so outputs are immediately usable in a docket or matter file.
- **Verification block** — a self-check covering jurisdiction lock, citation discipline, scope discipline, privilege/work-product handling.
- **False-positive matrix** — common model failure modes for that task (e.g., conflating Rule 12(b)(6) with Rule 56 standards; confusing "objection" with "general objection"; treating Restatements as primary authority).

## Conventions

- **File naming:** `legal_{specific_function}.md`
- **Citation format:** Bluebook by default; user can override (ALWD, state-specific).
- **Difficulty tags:** beginner (intake letter, demand letter), intermediate (MTD brief, fact-witness deposition outline), advanced (multi-jurisdiction split analysis, complex DD findings memo, expert deposition Daubert outline).
- **Practice-area neutrality:** Prompts are not bound to civil vs. criminal vs. transactional unless the task type requires it. The user supplies practice-area context.

## What These Prompts Are Not

- They are not a substitute for the user's own jurisdictional knowledge. They generate scaffolding, structure, and first drafts — not authority.
- They do not perform live legal research against a database. If the user does not supply authority, the prompt will tell the user to supply it rather than invent it.
- They are not configured for any specific e-discovery, contract lifecycle, or DMS platform. Outputs are platform-neutral.

## Routing (for Claude)

| User says | Use |
|---|---|
| "Spot the issues in this fact pattern" | `research/legal_issue_spotter_from_facts.md` |
| "Write me a research memo on X" | `research/legal_research_memo_irac.md` |
| "What does this statute mean as applied to..." | `research/legal_statutory_interpretation.md` |
| "Brief this case" / "summarize this opinion" | `research/legal_case_brief_generator.md` |
| "Compare these three cases" | `research/legal_precedent_comparison_table.md` |
| "Is there a circuit/state split on this?" | `research/legal_jurisdiction_split_analysis.md` |
| "Draft a complaint" | `litigation/legal_complaint_drafter.md` |
| "Draft an answer with affirmative defenses" | `litigation/legal_answer_with_affirmative_defenses.md` |
| "Draft a 12(b)(6) motion" | `litigation/legal_motion_to_dismiss_12b6.md` |
| "Draft an MSJ" / "Rule 56 motion" | `litigation/legal_motion_for_summary_judgment.md` |
| "Assess the case" / "where do we stand" | `litigation/legal_case_strategy_assessment.md` |
| "What's this case worth in settlement?" | `litigation/legal_settlement_value_range_analysis.md` |
| "Draft jury instructions" | `litigation/legal_jury_instruction_drafter.md` |
| "Draft document requests" / RFPs | `discovery/legal_document_request_drafter.md` |
| "Draft interrogatories" | `discovery/legal_interrogatory_drafter.md` |
| "Draft responses and objections" | `discovery/legal_discovery_response_objections.md` |
| "Build a privilege log" | `discovery/legal_privilege_log_generator.md` |
| "Write a meet-and-confer letter" | `discovery/legal_meet_and_confer_letter.md` |
| "Interview a custodian for ESI sources" | `discovery/legal_ediscovery_custodian_interview.md` |
| "Design a doc-review coding taxonomy" | `discovery/legal_document_review_coding_taxonomy.md` |
| "Outline a fact witness deposition" | `depositions/legal_deposition_outline_witness.md` |
| "Outline a 30(b)(6) deposition" | `depositions/legal_deposition_outline_30b6.md` |
| "Summarize this deposition transcript" | `depositions/legal_deposition_summary.md` |
| "Prep my witness for deposition" | `depositions/legal_deposition_witness_prep_script.md` |
| "Prep to depose an expert (Daubert focus)" | `depositions/legal_expert_deposition_prep.md` |
| "Draft a set of motions in limine" | `litigation/legal_motion_in_limine_set.md` |
| "Build a phased litigation budget" | `litigation/legal_litigation_budget_phase_estimator.md` |
| "Design a trial theme / narrative arc" | `litigation/legal_trial_theme_and_narrative_designer.md` |
| "Design a privilege review protocol (TAR/sampling)" | `discovery/legal_privilege_review_protocol.md` |
| "Full contract redline + issues memo" | `contracts-transactional/legal_contract_review_full_redline.md` |
| "Targeted redline (indemnity, LoL, IP, warranties, termination)" | `contracts-transactional/legal_contract_clause_redline_targeted.md` |
| "Contract risk heatmap" | `contracts-transactional/legal_contract_risk_heatmap.md` |
| "Draft an MSA" | `contracts-transactional/legal_msa_drafter.md` |
| "Draft a SOW" | `contracts-transactional/legal_sow_drafter.md` |
| "Draft a mutual NDA" | `contracts-transactional/legal_nda_mutual_drafter.md` |
| "Draft a GDPR DPA (with SCCs)" | `contracts-transactional/legal_dpa_gdpr_drafter.md` |
| "Draft a SaaS subscription agreement" | `contracts-transactional/legal_saas_subscription_agreement_drafter.md` |
| "Draft a licensing agreement" | `contracts-transactional/legal_licensing_agreement_drafter.md` |
| "Turn a term sheet into a first draft" | `contracts-transactional/legal_term_sheet_to_definitive_translator.md` |
| "Extract a clause library from executed contracts" | `contracts-transactional/legal_clause_library_extractor.md` |
| "Internal negotiation position paper" | `contracts-transactional/legal_negotiation_position_paper.md` |
| "Buy-side DD request list" | `corporate-ma/legal_due_diligence_request_list.md` |
| "Buy-side DD findings memo" | `corporate-ma/legal_due_diligence_findings_memo.md` |
| "Draft a disclosure schedule" | `corporate-ma/legal_disclosure_schedule_drafter.md` |
| "Draft board resolutions for a transaction" | `corporate-ma/legal_board_resolution_drafter.md` |
| "§409A or QSBS issue-spot in a deal" | `corporate-ma/legal_409a_or_qsbs_issue_spotter.md` |
| "Post-closing legal integration checklist" | `corporate-ma/legal_post_closing_integration_legal_checklist.md` |
| "Offer + IP + restrictive-covenant + separation set" | `employment-labor/legal_employment_offer_and_separation_package.md` |
| "Plan + report a workplace investigation" | `employment-labor/legal_workplace_investigation_plan_and_report.md` |
| "Pre-termination / PIP risk review" | `employment-labor/legal_pip_and_termination_risk_review.md` |
| "Wage-hour / contractor classification" | `employment-labor/legal_wage_hour_classification_analysis.md` |
| "Multi-state non-compete enforceability" | `employment-labor/legal_non_compete_enforceability_analysis.md` |
| "Draft an EEOC position statement" | `employment-labor/legal_eeoc_position_statement_drafter.md` |
| "Element-by-element patent claim chart" | `ip/legal_patent_claim_chart.md` |
| "Trademark clearance (knockout + full)" | `ip/legal_trademark_clearance_analysis.md` |
| "Copyright fair-use four-factor analysis" | `ip/legal_copyright_fair_use_analysis.md` |
| "DMCA takedown / counter-notice" | `ip/legal_dmca_takedown_and_counter_notice.md` |
| "OSS license compatibility review" | `ip/legal_open_source_license_compatibility_review.md` |
| "New matter intake summary" | `client-intake-communications/legal_new_matter_intake_summary.md` |
| "Draft an engagement letter" | `client-intake-communications/legal_engagement_letter_drafter.md` |
| "Draft a pre-litigation demand letter" | `client-intake-communications/legal_demand_letter_drafter.md` |
| "Client-facing matter status update" | `client-intake-communications/legal_client_status_update_memo.md` |
| "One-page executive matter summary" | `in-house-legalops/legal_matter_summary_for_executive.md` |
| "Outside-counsel invoice anomaly review" | `in-house-legalops/legal_legal_spend_anomaly_analyzer.md` |
| "Build a contract-type playbook" | `in-house-legalops/legal_playbook_builder_for_contract_type.md` |
| "Legal intake triage / routing" | `in-house-legalops/legal_legal_intake_triage_router.md` |
| "Quarterly board legal update" | `in-house-legalops/legal_board_legal_update_brief.md` |
| **Divorce / dissolution** | |
| "Divorce intake / case assessment" | `divorce/legal_divorce_intake_and_case_assessment.md` |
| "Draft a divorce petition / complaint" | `divorce/legal_divorce_petition_complaint_drafter.md` |
| "Draft a response / counterpetition" | `divorce/legal_divorce_response_and_counterpetition_drafter.md` |
| "Temporary / pendente lite orders motion" | `divorce/legal_temporary_orders_pendente_lite_motion.md` |
| "Financial affidavit / disclosure" | `divorce/legal_financial_affidavit_and_disclosure_builder.md` |
| "Characterize property (marital vs. separate)" | `divorce/legal_marital_property_characterization_analysis.md` |
| "Property division / equalization proposal" | `divorce/legal_property_division_and_equalization_proposal.md` |
| "Value & divide a business in divorce" | `divorce/legal_business_valuation_and_division_framework.md` |
| "Divide retirement / QDRO" | `divorce/legal_retirement_division_and_qdro_framework.md` |
| "Find hidden assets / prove dissipation" | `divorce/legal_hidden_asset_and_dissipation_investigation.md` |
| "Divorce tax consequences" | `divorce/legal_divorce_tax_consequences_analysis.md` |
| "Spousal support / alimony analysis" | `divorce/legal_spousal_support_alimony_analysis.md` |
| "Draft a marital settlement agreement (MSA)" | `divorce/legal_marital_settlement_agreement_drafter.md` |
| "Draft a prenup / postnup" | `divorce/legal_prenuptial_postnuptial_agreement_drafter.md` |
| "Is the prenup/postnup enforceable?" | `divorce/legal_prenup_postnup_enforceability_analysis.md` |
| "Prep for divorce mediation / financial settlement" | `divorce/legal_divorce_settlement_and_mediation_prep.md` |
| "Draft a divorce mediation brief / statement" | `divorce/legal_divorce_mediation_brief_drafter.md` |
| "Memorialize a mediated deal (term sheet / MOU)" | `divorce/legal_post_mediation_term_sheet_and_mou_drafter.md` |
| "Divorce discovery plan / requests" | `divorce/legal_divorce_discovery_plan_and_requests.md` |
| "Divorce trial prep / proposed findings" | `divorce/legal_divorce_trial_prep_and_findings_plan.md` |
| "Post-judgment modification / enforcement" | `divorce/legal_divorce_postjudgment_modification_and_enforcement.md` |
| "DV protective / restraining order petition" | `divorce/legal_domestic_violence_protective_order_petition.md` |
| **Custody / parenting** | |
| "Best-interests custody analysis" | `custody/legal_custody_best_interests_analysis.md` |
| "UCCJEA / which state has jurisdiction" | `custody/legal_uccjea_jurisdiction_analysis.md` |
| "Draft a custody petition / motion" | `custody/legal_custody_petition_or_motion_drafter.md` |
| "Emergency / temporary custody motion" | `custody/legal_temporary_and_emergency_custody_motion.md` |
| "Draft a parenting plan" | `custody/legal_parenting_plan_drafter.md` |
| "Build a holiday / vacation schedule" | `custody/legal_holiday_and_vacation_schedule_builder.md` |
| "High-conflict co-parenting provisions" | `custody/legal_high_conflict_parenting_coordination_provisions.md` |
| "Calculate child support" | `custody/legal_child_support_calculation_framework.md` |
| "Modify custody / parenting time" | `custody/legal_custody_modification_analysis_and_motion.md` |
| "Relocation / move-away analysis" | `custody/legal_relocation_move_away_analysis.md` |
| "Prep for / respond to a custody evaluation" | `custody/legal_custody_evaluation_prep_and_response.md` |
| "Respond to a GAL report" | `custody/legal_guardian_ad_litem_report_response.md` |
| "Grandparent / third-party custody or visitation" | `custody/legal_grandparent_third_party_custody_visitation_analysis.md` |
| "Supervised visitation / safety plan" | `custody/legal_supervised_visitation_and_safety_plan.md` |
| "Enforce parenting time / contempt" | `custody/legal_parenting_time_enforcement_and_contempt_motion.md` |
| "Custody trial prep / factor proof plan" | `custody/legal_custody_trial_prep_and_factor_proof_plan.md` |
| "Establish paternity / parentage" | `custody/legal_paternity_parentage_establishment_and_custody.md` |
| "Custody mediation / settlement prep" | `custody/legal_custody_settlement_and_mediation_prep.md` |
| "Draft a custody mediation brief / statement" | `custody/legal_custody_mediation_brief_drafter.md` |
| "Custody mediation stalled — impasse / package strategy" | `custody/legal_custody_mediation_impasse_and_package_strategy.md` |
| **Family law — self-represented / self-organizing litigant** *(layperson; organizes your own side — not legal advice)* | |
| "Organize my whole divorce/custody case for my lawyer" | `family-self-advocacy/legalprep_attorney_handoff_brief.md` |
| "Build a neutral dated timeline of events" | `family-self-advocacy/legalprep_case_chronology_builder.md` |
| "Organize / index my evidence and exhibits" | `family-self-advocacy/legalprep_evidence_inventory_organizer.md` |
| "Compile texts/emails into a clean record" | `family-self-advocacy/legalprep_communication_record_compiler.md` |
| "Document a recalled incident factually" | `family-self-advocacy/legalprep_incident_documentation_organizer.md` |
| "Map witnesses/documents to the facts they support" | `family-self-advocacy/legalprep_witness_and_source_map.md` |
| "Get ready for my financial disclosure / affidavit" | `family-self-advocacy/legalprep_financial_disclosure_organizer.md` |
| "Inventory marital & separate assets and debts" | `family-self-advocacy/legalprep_asset_and_debt_inventory.md` |
| "Build a budget for support/needs discussions" | `family-self-advocacy/legalprep_monthly_budget_and_expense_worksheet.md` |
| "Checklist of financial documents to collect" | `family-self-advocacy/legalprep_financial_document_gathering_checklist.md` |
| "Respond to allegations with facts, not argument" | `family-self-advocacy/legalprep_allegation_response_organizer.md` |
| "Write a neutral factual account for my attorney" | `family-self-advocacy/legalprep_my_account_factual_statement.md` |
| "Organize genuine concerns about the other party for counsel" | `family-self-advocacy/legalprep_concerns_about_other_party_organizer.md` |
| "Prepare for a family-court hearing" | `family-self-advocacy/legalprep_hearing_preparation_organizer.md` |
| "Practice answering questions truthfully and calmly" | `family-self-advocacy/legalprep_testimony_practice_factual_recall.md` |
| "Prepare for my deposition (as the litigant)" | `family-self-advocacy/legalprep_deposition_preparation_organizer.md` |
| "Explain the family-court process and roles to me" | `family-self-advocacy/legalprep_court_process_explainer.md` |
| "Prepare for mediation / settlement talks" | `family-self-advocacy/legalprep_mediation_preparation_organizer.md` |
| "Understand a mediation agreement before I sign" | `family-self-advocacy/legalprep_mediation_agreement_review_organizer.md` |
| "Capture what happened in a mediation session" | `family-self-advocacy/legalprep_post_mediation_follow_up_organizer.md` |
| "Questions to ask at my attorney consultation" | `family-self-advocacy/legalprep_attorney_consultation_question_builder.md` |
| "Prepare for a custody evaluation / GAL interview" | `family-self-advocacy/legalprep_custody_evaluation_preparation_organizer.md` |
| "Map my facts to best-interests factor categories" | `family-self-advocacy/legalprep_best_interests_factor_self_map.md` |
| **Personal legal self-advocacy — NON-family (layperson; organizes/prepares your own side — not legal advice)** | |
| "Which professional or authority do I even need?" | `personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md` |
| "Document one incident factually (first-hand vs hearsay)" | `personal-self-advocacy/cross-cutting/legalprep_incident_documentation_organizer.md` |
| "Preserve and inventory my evidence (incl. digital)" | `personal-self-advocacy/cross-cutting/legalprep_evidence_preservation_and_digital_organizer.md` |
| "Build a neutral dated timeline of the matter" | `personal-self-advocacy/cross-cutting/legalprep_personal_legal_chronology_builder.md` |
| "Assemble a package for my attorney / the authority" | `personal-self-advocacy/cross-cutting/legalprep_professional_handoff_brief.md` |
| "Questions for my attorney consultation" | `personal-self-advocacy/cross-cutting/legalprep_consultation_question_builder.md` |
| "Document a workplace concern (harassment/discrimination/retaliation)" | `personal-self-advocacy/workplace/legalprep_workplace_concern_documentation_organizer.md` |
| "Draft my own internal HR complaint" | `personal-self-advocacy/workplace/legalprep_hr_complaint_narrative_preparer.md` |
| "Organize facts for an EEOC / agency intake" | `personal-self-advocacy/workplace/legalprep_eeoc_agency_charge_preparation_organizer.md` |
| "Log workplace retaliation after I complained" | `personal-self-advocacy/workplace/legalprep_workplace_retaliation_log.md` |
| "Document unpaid wages / overtime / misclassification" | `personal-self-advocacy/workplace/legalprep_wage_hour_issue_documentation_organizer.md` |
| "Log harassment / stalking incidents (safety-forward)" | `personal-self-advocacy/harassment-stalking/legalprep_harassment_stalking_incident_log.md` |
| "Organize my account for a protective-order request" | `personal-self-advocacy/harassment-stalking/legalprep_protective_order_preparation_organizer.md` |
| "Prepare my own account for a police report" | `personal-self-advocacy/harassment-stalking/legalprep_police_report_account_preparer.md` |
| "Preserve threat evidence + digital-safety steps" | `personal-self-advocacy/harassment-stalking/legalprep_digital_safety_threat_evidence_organizer.md` |
| "Draft my own cyberharassment report to a platform" | `personal-self-advocacy/harassment-stalking/legalprep_cyberharassment_platform_report_preparer.md` |
| "Document a false statement made about me" | `personal-self-advocacy/defamation-reputation/legalprep_defamation_concern_documentation_organizer.md` |
| "Draft my own content-removal report to a platform" | `personal-self-advocacy/defamation-reputation/legalprep_online_content_removal_platform_report_preparer.md` |
| "Draft my own correction / retraction request" | `personal-self-advocacy/defamation-reputation/legalprep_correction_retraction_request_preparer.md` |
| "Log the concrete harm to my reputation" | `personal-self-advocacy/defamation-reputation/legalprep_reputation_harm_impact_log.md` |
| "Document my stolen / infringed work" | `personal-self-advocacy/ip-theft/legalprep_ip_infringement_documentation_organizer.md` |
| "Draft my own DMCA takedown notice (I sign it)" | `personal-self-advocacy/ip-theft/legalprep_dmca_takedown_notice_preparer.md` |
| "Organize proof of my ownership / priority" | `personal-self-advocacy/ip-theft/legalprep_ownership_priority_evidence_organizer.md` |
| "Draft my own marketplace infringement report" | `personal-self-advocacy/ip-theft/legalprep_marketplace_infringement_report_preparer.md` |
| "Document a consumer dispute / bad product / billing error" | `personal-self-advocacy/consumer-scams/legalprep_consumer_complaint_documentation_organizer.md` |
| "Report a scam / fraud (FTC / IC3 / bank)" | `personal-self-advocacy/consumer-scams/legalprep_scam_fraud_report_preparer.md` |
| "Draft my own refund / chargeback dispute" | `personal-self-advocacy/consumer-scams/legalprep_refund_chargeback_dispute_preparer.md` |
| "Document a tenant issue (repairs / deposit / notice)" | `personal-self-advocacy/housing-landlord-tenant/legalprep_tenant_issue_documentation_organizer.md` |
| "Draft my own response to my landlord" | `personal-self-advocacy/housing-landlord-tenant/legalprep_landlord_notice_response_preparer.md` |
| "Draft my own security-deposit dispute letter" | `personal-self-advocacy/housing-landlord-tenant/legalprep_security_deposit_dispute_preparer.md` |
| "Document identity theft + prepare my reports" | `personal-self-advocacy/identity-theft/legalprep_identity_theft_documentation_and_report_preparer.md` |
| "Draft my own fraud-dispute letters (bureau / bank)" | `personal-self-advocacy/identity-theft/legalprep_fraud_dispute_narrative_preparer.md` |
| "Draft my own debt-validation / dispute letter" | `personal-self-advocacy/debt-collection/legalprep_debt_validation_dispute_letter_preparer.md` |
| "Log collection contacts I find harassing" | `personal-self-advocacy/debt-collection/legalprep_collection_harassment_documentation_log.md` |
| "Organize my small-claims case (facts / evidence / amount)" | `personal-self-advocacy/small-claims/legalprep_small_claims_case_preparation_organizer.md` |
| "Prepare for my small-claims hearing (practice testimony)" | `personal-self-advocacy/small-claims/legalprep_small_claims_hearing_preparation_and_testimony_practice.md` |
