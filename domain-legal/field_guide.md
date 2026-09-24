# Legal Field Guide

**Purpose:** One page for finding the right prompt in `domain-legal/` and using it the way the domain expects. It covers how to pick a subfolder by task and posture, the domain's conventions (the target for all new and updated prompts; older prompts follow most but not all of them), and a "start here" table for each practice area. For the full directory map and routing rules, see [README.md](README.md). For how the library was built, see [EXPANSION_ROADMAP.md](EXPANSION_ROADMAP.md).

---

## 1. First decision: who is running the prompt?

The domain has two tracks that follow opposite conventions. Pick the track before picking a folder.

| Who is running it | Track | Filename prefix | What the prompts do |
|---|---|---|---|
| Attorney, paralegal, in-house counsel, legal ops, compliance | **Practitioner** (every folder except the two below) | `legal_` | Draft, analyze, and strategize. No "consult an attorney" boilerplate; guardrails are specific, testable constraints. |
| Person handling their own divorce or custody matter | **Family self-advocacy**: [family-self-advocacy/](family-self-advocacy/README.md) | `legalprep_` | Organize facts, records, and preparation for handoff to counsel or the court process. No legal advice, strategy, citations, or outcome predictions. Mandatory Safety Block. |
| Person handling their own non-family matter (work, harassment, housing, debt, scams, IP theft, small claims) | **Personal self-advocacy**: [personal-self-advocacy/](personal-self-advocacy/README.md) | `legalprep_` | Same stance as family self-advocacy. Self-submit preparers draft the user's *own* factual account for channels built for non-lawyers. |

**Crossing tracks.** Prompts added or updated since 2026-09-24 open with an attorney-facing scope guard, and older practitioner prompts are being brought to the same convention; where a prompt lacks one, apply it yourself. If a layperson reaches one, the guard sends them to [the professional/authority router](personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md). Self-advocacy prompts end in a handoff brief ([personal](personal-self-advocacy/cross-cutting/legalprep_professional_handoff_brief.md), [family](family-self-advocacy/legalprep_attorney_handoff_brief.md)) that a practitioner can pick up.

---

## 2. Second decision: which folder, by task and posture

| You need to… | Posture / stage | Folder |
|---|---|---|
| Find, read, or synthesize law | Any | [research/](research/) |
| Take in a new matter, engage a client, send a demand or status update | Pre-suit / matter opening | [client-intake-communications/](client-intake-communications/) |
| Plead, move, value, try, or settle a civil case | Filed or about to be filed | [litigation/](litigation/) |
| Preserve, request, resist, or compel written discovery; subpoena nonparties | Discovery | [discovery/](discovery/) |
| Prepare, take, defend, or summarize a deposition | Discovery | [depositions/](depositions/) |
| Choose issues, write the statement of facts, argue on appeal | After judgment and post-trial motions | [appellate/](appellate/) |
| Draft, review, or redline a contract; plan a negotiation | Transactional | [contracts-transactional/](contracts-transactional/) |
| Diligence, board action, disclosure schedules, integration | Corporate / M&A | [corporate-ma/](corporate-ma/) |
| Employment documents, classification, investigations, agency charges | Employment | [employment-labor/](employment-labor/) |
| Clearance, infringement, licensing, takedowns | IP | [ip/](ip/) |
| Privacy assessments, breach response, retention | Privacy / data | [privacy-data/](privacy-data/) |
| Compliance programs, government subpoenas/CIDs, voluntary disclosure | Regulatory | [regulatory-compliance/](regulatory-compliance/) |
| Conflicts, sanctions risk, unauthorized practice | Professional responsibility | [ethics-professional-conduct/](ethics-professional-conduct/) |
| Triage intake, spend, playbooks, executive and board updates | In-house operations | [in-house-legalops/](in-house-legalops/) |
| Practice-area work | Specialist | [bankruptcy-restructuring/](bankruptcy-restructuring/), [tax/](tax/), [immigration/](immigration/), [criminal/](criminal/), [real-estate/](real-estate/), [trusts-estates/](trusts-estates/), [divorce/](divorce/), [custody/](custody/) |

**Tie-breakers.**
- **The object decides.** A settlement in a divorce is [divorce/](divorce/legal_marital_settlement_agreement_drafter.md), not [litigation/](litigation/legal_settlement_agreement_drafter.md). An employee separation with no pending claim is [employment-labor/](employment-labor/legal_employment_offer_and_separation_package.md).
- **"Protective order" has two meanings.** A discovery confidentiality order is in [discovery/](discovery/legal_protective_order_drafter.md). A domestic-violence or harassment restraining order is in [divorce/](divorce/legal_domestic_violence_protective_order_petition.md) (attorney) or [personal-self-advocacy/harassment-stalking/](personal-self-advocacy/harassment-stalking/legalprep_protective_order_preparation_organizer.md) (self-represented).
- **Issuing vs. receiving a subpoena.** Issuing one is [discovery/](discovery/legal_subpoena_drafter.md). Responding to one is [regulatory-compliance/](regulatory-compliance/legal_subpoena_or_cid_response_strategy.md). Fighting one in court is [discovery/](discovery/legal_motion_for_protective_order_drafter.md).
- **Valuation vs. advocacy.** An internal settlement number comes from [the value-range analysis](litigation/legal_settlement_value_range_analysis.md). What you send the mediator comes from [the mediation position paper](litigation/legal_mediation_position_paper.md), which uses that number.

---

## 3. Conventions every practitioner prompt shares

| Convention | What it means in practice |
|---|---|
| **Jurisdiction is a required input** | Prompts ask for the court, governing law, and (where relevant) venue and posture. If it is missing, the output marks every rule reference `[VERIFY]` rather than assuming federal or any one state's law. |
| **No fabricated authority** | Case names, statute and rule numbers, regulatory provisions, and quotations come only from what the user supplies. Everything else is a placeholder. |
| **Placeholders** | `[CITE: proposition]` means authority is needed. `[NEED PIN: source]` means a pinpoint is missing. `[NEED HOLDING: case]` means the holding has to be confirmed. `[VERIFY: item]` marks a rule, deadline, threshold, or form that varies by jurisdiction or changes over time. `[NEED: fact]` marks a missing fact. `[R. __]` (or `[REC: …]`) marks a record cite that has not been supplied yet; `[AR: …]` marks a missing administrative-record location. Older prompts may use only `[CITE]`/`[NEED PIN]` — the `[VERIFY]` convention is the target for all new work. |
| **Deadlines are never computed from memory** | Prompts take deadlines from the notice, order, or supplied rule text and mark them `[VERIFY]`. Some post-judgment deadlines cannot be extended. |
| **Locked output format** | Each prompt fixes the structure of its deliverable (memo, motion package, redline, table schema) so outputs can be compared and reviewed. |
| **Verification block** | Phase 2+ prompts check jurisdiction lock, citation discipline, and scope discipline, plus checks specific to the task. |
| **False-positive matrix** | A table of the model's most likely mistakes on this task, each paired with its correction. |
| **No performative disclaimers** | Specific guardrails do the job that "consult a licensed attorney" boilerplate would only pretend to do. The self-advocacy tracks are the deliberate exception. |
| **Fictional examples** | Worked examples use invented parties. |

**Citation style.** Prompts do not pick a citation manual. State the style you need (Bluebook, ALWD, or a state style manual or court rule) in your inputs, and the prompt formats only the authority you supply in that style. Captions and formatting follow the court's local rules, which you supply or which the prompt marks `[VERIFY]`.

---

## 4. A civil case, start to finish

| Stage | Prompt(s) |
|---|---|
| Intake and conflicts | [New-matter intake](client-intake-communications/legal_new_matter_intake_summary.md) → [conflicts check](ethics-professional-conduct/legal_conflicts_check_memo.md) → [engagement letter](client-intake-communications/legal_engagement_letter_drafter.md) |
| Preserve | [Litigation hold notice](discovery/legal_litigation_hold_notice_drafter.md) → [custodian interview](discovery/legal_ediscovery_custodian_interview.md) |
| Pre-suit | [Demand letter](client-intake-communications/legal_demand_letter_drafter.md), [case strategy](litigation/legal_case_strategy_assessment.md), [budget](litigation/legal_litigation_budget_phase_estimator.md) |
| Pleadings | [Complaint](litigation/legal_complaint_drafter.md), [12(b)(6) motion](litigation/legal_motion_to_dismiss_12b6.md), [answer](litigation/legal_answer_with_affirmative_defenses.md) |
| Confidentiality | [Stipulated protective order](discovery/legal_protective_order_drafter.md) |
| Written discovery | [RFPs](discovery/legal_document_request_drafter.md), [interrogatories](discovery/legal_interrogatory_drafter.md), [responses and objections](discovery/legal_discovery_response_objections.md), [privilege review](discovery/legal_privilege_review_protocol.md), [privilege log](discovery/legal_privilege_log_generator.md), [nonparty subpoena](discovery/legal_subpoena_drafter.md) |
| Discovery disputes | [Meet-and-confer letter](discovery/legal_meet_and_confer_letter.md) → [motion to compel](discovery/legal_motion_to_compel_drafter.md) or [motion for protective order](discovery/legal_motion_for_protective_order_drafter.md) |
| Depositions | [30(b)(6) notice](discovery/legal_30b6_notice_drafter.md) → [30(b)(6) outline](depositions/legal_deposition_outline_30b6.md), [witness outline](depositions/legal_deposition_outline_witness.md), [witness prep](depositions/legal_deposition_witness_prep_script.md), [expert prep](depositions/legal_expert_deposition_prep.md), [summary](depositions/legal_deposition_summary.md) |
| Dispositive motions | [Summary judgment](litigation/legal_motion_for_summary_judgment.md) |
| Resolution | [Settlement value range](litigation/legal_settlement_value_range_analysis.md) → [mediation position paper](litigation/legal_mediation_position_paper.md) → [settlement agreement](litigation/legal_settlement_agreement_drafter.md) |
| Trial | [Theme and narrative](litigation/legal_trial_theme_and_narrative_designer.md), [motions in limine](litigation/legal_motion_in_limine_set.md), [jury instructions](litigation/legal_jury_instruction_drafter.md) |
| After judgment | [Post-trial motion set](litigation/legal_post_trial_motion_set.md), [fee petition](litigation/legal_attorney_fee_petition.md) |
| Appeal | [Issue selection](appellate/legal_issue_selection_memo.md) → [statement of facts](appellate/legal_statement_of_facts_builder.md) → [oral argument](appellate/legal_oral_argument_prep.md) |
| Before filing anything risky | [Sanctions-risk premortem](ethics-professional-conduct/legal_sanctions_risk_premortem.md) |

---

## 5. Start here, by practice area

| Practice area | Start with | Then |
|---|---|---|
| Legal research | [Research plan](research/legal_research_plan.md) | [IRAC memo](research/legal_research_memo_irac.md), [jurisdiction split](research/legal_jurisdiction_split_analysis.md) |
| Issue spotting from a fact pattern | [Issue spotter](research/legal_issue_spotter_from_facts.md) | [Case strategy](litigation/legal_case_strategy_assessment.md) |
| Contracts | [Full-contract redline](contracts-transactional/legal_contract_review_full_redline.md) | [Risk heatmap](contracts-transactional/legal_contract_risk_heatmap.md), [negotiation position paper](contracts-transactional/legal_negotiation_position_paper.md) |
| Corporate / M&A | [Diligence request list](corporate-ma/legal_due_diligence_request_list.md) | [Diligence findings memo](corporate-ma/legal_due_diligence_findings_memo.md), [disclosure schedules](corporate-ma/legal_disclosure_schedule_drafter.md) |
| Employment | [Termination risk review](employment-labor/legal_pip_and_termination_risk_review.md) | [EEOC position statement](employment-labor/legal_eeoc_position_statement_drafter.md), [workplace investigation](employment-labor/legal_workplace_investigation_plan_and_report.md) |
| IP | [Trademark clearance](ip/legal_trademark_clearance_analysis.md) | [Fair use](ip/legal_copyright_fair_use_analysis.md), [patent claim chart](ip/legal_patent_claim_chart.md) |
| Privacy / data | [DPIA](privacy-data/legal_privacy_impact_assessment_dpia.md) | [Breach runbook](privacy-data/legal_data_breach_response_runbook.md), [retention schedule](privacy-data/legal_records_retention_schedule_design.md) |
| Regulatory | [Compliance gap analysis](regulatory-compliance/legal_compliance_program_gap_analysis.md) | [Internal investigation](regulatory-compliance/legal_internal_investigation_plan.md), [voluntary disclosure](regulatory-compliance/legal_voluntary_disclosure_decision_memo.md) |
| In-house operations | [Intake triage router](in-house-legalops/legal_legal_intake_triage_router.md) | [Executive matter summary](in-house-legalops/legal_matter_summary_for_executive.md), [spend anomalies](in-house-legalops/legal_legal_spend_anomaly_analyzer.md) |
| Bankruptcy | [Chapter selection](bankruptcy-restructuring/legal_chapter_selection_and_eligibility_analysis.md) | [Automatic stay motions](bankruptcy-restructuring/legal_automatic_stay_motion_set.md), [proof of claim](bankruptcy-restructuring/legal_proof_of_claim_drafter.md) |
| Tax | [Tax research memo](tax/legal_tax_research_memo.md) | [IRS IDR response](tax/legal_irs_idr_response.md) |
| Immigration | [Naturalization eligibility](immigration/legal_naturalization_eligibility_analysis.md) | [H-1B RFE response](immigration/legal_h1b_rfe_response.md), [PERM audit](immigration/legal_perm_audit_response.md) |
| Criminal defense | [Brady/Giglio request](criminal/legal_brady_giglio_review_request.md) | [Motion to suppress](criminal/legal_motion_to_suppress.md), [plea offer analysis](criminal/legal_plea_offer_analysis.md) |
| Real estate | [Title commitment review](real-estate/legal_title_commitment_review.md) | [Purchase agreement redline](real-estate/legal_purchase_agreement_redline.md), [zoning](real-estate/legal_zoning_use_analysis.md) |
| Trusts and estates | [Estate tax planning memo](trusts-estates/legal_estate_tax_planning_memo.md) | [Revocable trust](trusts-estates/legal_revocable_trust_drafter.md), [will](trusts-estates/legal_will_drafter.md) |
| Divorce (attorney) | [Divorce intake and assessment](divorce/legal_divorce_intake_and_case_assessment.md) | [Property characterization](divorce/legal_marital_property_characterization_analysis.md), [MSA](divorce/legal_marital_settlement_agreement_drafter.md) |
| Custody (attorney) | [Best-interests analysis](custody/legal_custody_best_interests_analysis.md) | [UCCJEA jurisdiction](custody/legal_uccjea_jurisdiction_analysis.md), [parenting plan](custody/legal_parenting_plan_drafter.md) |
| Appellate | [Issue selection](appellate/legal_issue_selection_memo.md) | [Petition for review](appellate/legal_petition_for_review_drafter.md) |
| Ethics | [Conflicts check](ethics-professional-conduct/legal_conflicts_check_memo.md) | [Sanctions premortem](ethics-professional-conduct/legal_sanctions_risk_premortem.md) |
| Self-represented, family | [Case chronology](family-self-advocacy/legalprep_case_chronology_builder.md) | [Evidence inventory](family-self-advocacy/legalprep_evidence_inventory_organizer.md), [attorney handoff brief](family-self-advocacy/legalprep_attorney_handoff_brief.md) |
| Self-represented, non-family | [Professional/authority router](personal-self-advocacy/cross-cutting/legalprep_professional_authority_router.md) | [Personal legal chronology](personal-self-advocacy/cross-cutting/legalprep_personal_legal_chronology_builder.md), [handoff brief](personal-self-advocacy/cross-cutting/legalprep_professional_handoff_brief.md) |

---

## 6. Using these prompts well

- **Give the prompt your jurisdiction's actual rule text** whenever you have it. Output quality depends most on this input, and it is what turns `[VERIFY]` markers into firm statements.
- **Chain prompts instead of stretching one.** The value range feeds the mediation paper. The meet-and-confer letter feeds the motion to compel. The 30(b)(6) notice feeds the outline. Each prompt's "Not this prompt if" section names its neighbours.
- **Resolve every placeholder before filing or sending.** A placeholder left in the output is a task still open, not a draft ready to go out.
- **Match the reader.** If a practitioner prompt's scope guard fires, switch tracks rather than softening the prompt.
