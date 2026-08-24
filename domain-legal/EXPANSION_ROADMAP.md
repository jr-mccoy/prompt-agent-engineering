# Domain-Legal Expansion Roadmap

**Status as of 2026-05-11:** Phase 1 (25 prompts) and Phase 2A (42 prompts: 4 deferred from Phase 1 + 38 new across 6 subdirectories) shipped. Cumulative: 67 prompts. This document tracks the remaining ~67 prompts planned for the legal practitioner library.

Filing convention: `legal_{specific_function}.md` inside the relevant practice-area subdirectory. All prompts follow the structural conventions established in Phase 1: required jurisdiction input, explicit no-fabrication clauses for citations, locked output formats, verification block, false-positive matrix, no generic refusal/safety boilerplate.

---

## Phase 1 + Phase 2A Status

### Shipped (67 prompts + README)

```
domain-legal/
├── README.md
├── research/                       6/6   ✓
├── litigation/                    10/10  ✓ (3 carried from Phase 1 deferral, completed in Phase 2A)
├── discovery/                      8/8   ✓ (1 carried from Phase 1 deferral, completed in Phase 2A)
├── depositions/                    5/5   ✓
├── contracts-transactional/       12/12  ✓ (Phase 2A)
├── corporate-ma/                   6/6   ✓ (Phase 2A)
├── employment-labor/               6/6   ✓ (Phase 2A)
├── ip/                             5/5   ✓ (Phase 2A)
├── client-intake-communications/   4/4   ✓ (Phase 2A)
└── in-house-legalops/              5/5   ✓ (Phase 2A)
```

### Deferred from Phase 1 — DELIVERED IN PHASE 2A

| File | Subdirectory | Status |
|---|---|---|
| `legal_motion_in_limine_set.md` | litigation | ✓ Shipped |
| `legal_litigation_budget_phase_estimator.md` | litigation | ✓ Shipped |
| `legal_trial_theme_and_narrative_designer.md` | litigation | ✓ Shipped |
| `legal_privilege_review_protocol.md` | discovery | ✓ Shipped |

---

## Phase 2 — Remaining Subdirectories and Prompts

### Phase 2A — Transactional and In-House Foundations — ✓ COMPLETE (42 prompts shipped 2026-05-11)

These were the daily workflows of corporate counsel, contract managers, and legal operations.

**Status: all 42 prompts (38 new + 4 carried) shipped.** The lists below are preserved as a record of what was built.

#### `contracts-transactional/` (12)
| File | Description |
|---|---|
| `legal_contract_review_full_redline.md` | Full review with risk-tiered comments and redlines; outputs both clean and redlined versions plus issues memo |
| `legal_contract_clause_redline_targeted.md` | Focused redline pass on indemnity, limitation of liability, IP ownership, warranties, termination |
| `legal_contract_risk_heatmap.md` | Issue list with severity score, negotiation posture (must-have / should-have / fallback), and escalation triggers |
| `legal_msa_drafter.md` | Master Services Agreement with standard schedules; calibrated to buyer or supplier posture |
| `legal_sow_drafter.md` | Statement of Work tied to MSA; deliverables, acceptance criteria, change-order procedures |
| `legal_nda_mutual_drafter.md` | Mutual NDA with definition of confidential info, exclusions, term, residuals, return-or-destroy |
| `legal_dpa_gdpr_drafter.md` | Data processing addendum with SCCs, sub-processor flow-down, audit and breach terms |
| `legal_saas_subscription_agreement_drafter.md` | SaaS subscription with usage metrics, SLAs, data portability, termination assistance |
| `legal_licensing_agreement_drafter.md` | IP / software license with scope, field-of-use, exclusivity, royalties, audit rights |
| `legal_term_sheet_to_definitive_translator.md` | Convert a term sheet into a structured first draft of definitive documents with open-issue list |
| `legal_clause_library_extractor.md` | Extract reusable clauses from a corpus of executed contracts with metadata for retrieval |
| `legal_negotiation_position_paper.md` | Internal posture memo with primary, fallback, and walkaway positions per issue |

#### `corporate-ma/` (6)
| File | Description |
|---|---|
| `legal_due_diligence_request_list.md` | Buy-side DD checklist tailored to deal type (asset, stock, merger), industry, and red-flag focus |
| `legal_due_diligence_findings_memo.md` | Issues organized by severity, deal-impact translation, indemnity/escrow recommendations |
| `legal_disclosure_schedule_drafter.md` | Disclosure schedule structured to representations and warranties with cross-reference table |
| `legal_board_resolution_drafter.md` | Board resolutions for transactional approvals with recitals, resolutions, certification |
| `legal_409a_or_qsbs_issue_spotter.md` | Identify §409A deferred-comp issues and QSBS qualification questions in a deal context |
| `legal_post_closing_integration_legal_checklist.md` | 30/60/90-day legal integration tasks: assignments, consents, employment, IP, regulatory |

#### `employment-labor/` (6)
| File | Description |
|---|---|
| `legal_employment_offer_and_separation_package.md` | Coordinated offer / amendment / separation set with at-will, IP, restrictive-covenant, release |
| `legal_workplace_investigation_plan_and_report.md` | Title VII / harassment investigation plan, witness order, finding-of-fact memo |
| `legal_pip_and_termination_risk_review.md` | Pre-termination risk review: protected-class exposure, retaliation timing, documentation gaps |
| `legal_wage_hour_classification_analysis.md` | Exempt/non-exempt and contractor/employee analysis under federal and state tests |
| `legal_non_compete_enforceability_analysis.md` | Multi-state enforceability of restrictive covenants under current law |
| `legal_eeoc_position_statement_drafter.md` | Position statement responding to a charge, with factual chronology and legal framing |

#### `ip/` (5)
| File | Description |
|---|---|
| `legal_patent_claim_chart.md` | Element-by-element claim chart mapping claims to accused product or prior art |
| `legal_trademark_clearance_analysis.md` | Knockout + full clearance analysis with likelihood-of-confusion factors |
| `legal_copyright_fair_use_analysis.md` | Four-factor fair use analysis grounded in supplied authority |
| `legal_dmca_takedown_and_counter_notice.md` | Takedown notice and counter-notice with required statutory elements |
| `legal_open_source_license_compatibility_review.md` | Compatibility analysis for a dependency tree against project license |

#### `client-intake-communications/` (4)
| File | Description |
|---|---|
| `legal_new_matter_intake_summary.md` | Intake summary: facts, conflicts check inputs, scope, fee structure, immediate actions |
| `legal_engagement_letter_drafter.md` | Engagement letter with scope, fees, conflicts, termination, file-retention provisions |
| `legal_demand_letter_drafter.md` | Pre-litigation demand: factual recitation, legal claim, requested cure, deadline, leverage |
| `legal_client_status_update_memo.md` | Client-facing matter update: progress, next steps, decisions needed, budget posture |

#### `in-house-legalops/` (5)
| File | Description |
|---|---|
| `legal_matter_summary_for_executive.md` | Executive matter summary: risk, cost, timeline, decision needed — one-page format |
| `legal_legal_spend_anomaly_analyzer.md` | Outside-counsel invoice review for billing anomalies, scope drift, staffing efficiency |
| `legal_playbook_builder_for_contract_type.md` | Playbook with primary / fallback / walkaway positions per clause for a contract type |
| `legal_legal_intake_triage_router.md` | Triage incoming legal requests by type, urgency, and routing destination |
| `legal_board_legal_update_brief.md` | Quarterly board legal update: litigation, regulatory, transactions, governance |

### Phase 2B — Regulatory, Privacy, Compliance (~12 prompts)

#### `regulatory-compliance/` (5)
| File | Description |
|---|---|
| `legal_regulatory_change_impact_assessment.md` | Map a new rule against current operations, identify gaps, assign remediation owners and dates |
| `legal_compliance_program_gap_analysis.md` | Gap analysis against a compliance framework (FCPA, AML, sanctions, antitrust) with remediation plan |
| `legal_subpoena_or_cid_response_strategy.md` | Response strategy for a subpoena or civil investigative demand: scope objections, production plan, privilege |
| `legal_internal_investigation_plan.md` | Internal investigation plan: privilege framing, witness order, document collection, reporting |
| `legal_voluntary_disclosure_decision_memo.md` | Decision memo on voluntary self-disclosure: factors, leniency exposure, timing, structure |

#### `privacy-data/` (4)
| File | Description |
|---|---|
| `legal_privacy_impact_assessment_dpia.md` | DPIA structured around lawful basis, data flows, risk assessment, mitigations |
| `legal_data_breach_response_runbook.md` | 50-state and international notification triage; regulator notice; consumer notice; mitigation |
| `legal_vendor_privacy_assessment.md` | Vendor DPA / SCC / TIA review; transfer-mechanism analysis; sub-processor flow-down |
| `legal_records_retention_schedule_design.md` | Retention schedule by record class, jurisdiction, and litigation-hold interaction |

#### `ethics-professional-conduct/` (3)
| File | Description |
|---|---|
| `legal_conflicts_check_memo.md` | Conflicts analysis under MRPC 1.7 / 1.9 / 1.10 with imputation and waiver options |
| `legal_sanctions_risk_premortem.md` | Pre-mortem on sanctions exposure under Rule 11, §1927, inherent power, fee-shifting statutes |
| `legal_unauthorized_practice_jurisdictional_assessment.md` | UPL analysis for cross-border or remote practice, including pro hac vice, in-house registration, multi-jurisdictional practice rules |

### Phase 2C — Specialty Practice Areas (~30 prompts)

#### `bankruptcy-restructuring/` (5)
| File | Description |
|---|---|
| `legal_chapter_selection_and_eligibility_analysis.md` | Chapter 7 / 11 / 13 / Subchapter V eligibility and strategic selection |
| `legal_proof_of_claim_drafter.md` | POC with priority classification, supporting documentation, secured/unsecured analysis |
| `legal_chapter_11_plan_analysis.md` | Plan feasibility, classification, best-interests, cramdown, absolute-priority issues |
| `legal_automatic_stay_motion_set.md` | Motion for relief from stay (and opposition) with cause/lack-of-equity analysis |
| `legal_363_sale_strategy_memo.md` | §363 sale process: stalking horse, bid procedures, free-and-clear analysis, sale order terms |

#### `tax/` (5)
| File | Description |
|---|---|
| `legal_tax_research_memo.md` | Tax-specific research memo: code, regs, rulings, case law, pinpointed citations |
| `legal_section_1031_exchange_analysis.md` | Like-kind exchange qualification, identification rules, replacement timing, related-party traps |
| `legal_rd_credit_position_memo.md` | §41 R&D credit qualification, qualified research expense analysis, documentation requirements |
| `legal_transfer_pricing_position_paper.md` | Transfer pricing methodology selection, comparables, documentation under §482 / OECD |
| `legal_irs_idr_response.md` | Response to IRS Information Document Request: scope objections, privilege, production plan |

#### `immigration/` (5)
| File | Description |
|---|---|
| `legal_h1b_rfe_response.md` | Response to H-1B Request for Evidence on specialty occupation, employer-employee relationship, prevailing wage |
| `legal_perm_audit_response.md` | PERM labor certification audit response: recruitment documentation, prevailing wage, ability to pay |
| `legal_i589_asylum_declaration_framework.md` | Asylum declaration structure: nexus, persecution, government action/inability, internal relocation, country conditions |
| `legal_eb1_extraordinary_ability_petition.md` | EB-1A petition with criteria mapping, evidence quality assessment, final-merits analysis |
| `legal_naturalization_eligibility_analysis.md` | Naturalization eligibility: residence, physical presence, good moral character, English/civics |

#### `family/` — ✅ DELIVERED as `divorce/` (19) + `custody/` (18)

The planned five-prompt `family/` set was expanded into two dedicated, comprehensive subsections instead of a single directory. All five originally planned files shipped (in their respective subsections), plus prenup/postnup drafting + enforceability, DV protective order, paternity/parentage, and a full practitioner workflow per subsection.

**`divorce/` (19):** intake/case assessment; petition; response/counterpetition; temporary (pendente lite) orders; financial affidavit/disclosure; property characterization; property division/equalization; business valuation/division; retirement division/QDRO; hidden-asset/dissipation investigation; divorce tax consequences; spousal support/alimony; **marital settlement agreement**; prenuptial/postnuptial drafter; prenup/postnup enforceability; divorce discovery plan; trial prep/findings; post-judgment modification/enforcement; **DV protective order petition**.

**`custody/` (18):** best-interests analysis; UCCJEA jurisdiction; custody petition/motion; temporary/emergency custody; **parenting plan**; holiday/vacation schedule; high-conflict coordination provisions; **child support calculation**; modification; **relocation/move-away analysis**; custody-evaluation prep/response; GAL report response; grandparent/third-party custody/visitation; supervised visitation/safety plan; parenting-time enforcement/contempt; custody trial prep/factor proof; paternity/parentage establishment; custody settlement/mediation prep.

Original planned files (now shipped):
| Planned file | Shipped as |
|---|---|
| `legal_parenting_plan_drafter.md` | `custody/legal_parenting_plan_drafter.md` |
| `legal_child_support_calculation_framework.md` | `custody/legal_child_support_calculation_framework.md` |
| `legal_marital_settlement_agreement_drafter.md` | `divorce/legal_marital_settlement_agreement_drafter.md` |
| `legal_protective_order_petition.md` | `divorce/legal_domestic_violence_protective_order_petition.md` |
| `legal_relocation_motion_analysis.md` | `custody/legal_relocation_move_away_analysis.md` |

#### `criminal/` (5)
| File | Description |
|---|---|
| `legal_motion_to_suppress.md` | Suppression motion: Fourth/Fifth/Sixth Amendment grounds with factual basis and authority |
| `legal_plea_offer_analysis.md` | Plea analysis: guideline exposure, collateral consequences, immigration impact, trial probability |
| `legal_sentencing_memorandum.md` | Sentencing memo: §3553(a) factors, guideline analysis, mitigation, character evidence |
| `legal_bwc_review_protocol.md` | Body-worn camera review for inconsistencies, exculpatory content, suppression hooks |
| `legal_brady_giglio_review_request.md` | Brady/Giglio request and tracking framework for a defense file |

#### `appellate/` (5)
| File | Description |
|---|---|
| `legal_issue_selection_memo.md` | Appellate issue selection: preservation, standard of review, strength, narrative fit |
| `legal_statement_of_facts_builder.md` | Record-grounded statement of facts with citations to RA/JA, neutral framing of disputed facts |
| `legal_oral_argument_prep.md` | Oral argument prep: question anticipation, concession map, hot-bench drills, time strategy |
| `legal_petition_for_review_drafter.md` | Cert petition or state-supreme review petition tied to grant criteria |
| `legal_amicus_brief_strategy_memo.md` | Amicus strategy: angle selection, party coordination, anti-redundancy, signal value |

#### `real-estate/` (5)
| File | Description |
|---|---|
| `legal_purchase_agreement_redline.md` | PSA redline calibrated to buyer or seller posture with risk-tiered comments |
| `legal_title_commitment_review.md` | Title-commitment review: schedule B-I and B-II analysis, endorsement strategy, cure plan |
| `legal_commercial_lease_abstract.md` | Lease abstract with key terms, options, defaults, tenant/landlord obligations, side-letter integration |
| `legal_zoning_use_analysis.md` | Permitted/conditional/prohibited use analysis with variance and special-permit posture |
| `legal_easement_drafter.md` | Easement drafting: scope, term, maintenance, indemnity, recordable form |

#### `trusts-estates/` (5)
| File | Description |
|---|---|
| `legal_will_drafter.md` | Will with specific bequests, residuary, trust pour-over, fiduciary appointments, tax provisions |
| `legal_revocable_trust_drafter.md` | Revocable trust: funding mechanics, successor trustee, distribution standards, tax provisions |
| `legal_estate_tax_planning_memo.md` | Estate tax exposure analysis with lifetime gifting, GST, portability, valuation strategies |
| `legal_probate_inventory_and_accounting.md` | Inventory and accounting frameworks meeting state-court requirements |
| `legal_trust_modification_or_decanting_analysis.md` | Modification, reformation, decanting, or non-judicial settlement analysis under controlling state law |

---

## Personal Legal Self-Advocacy (Layperson, Non-Family) — ✅ DELIVERED (2026-07-23, 36 prompts)

The second **litigant-facing** area of `domain-legal/` (after `family-self-advocacy/`), and the second to *invert* the domain's attorney-only, disclaimer-free convention. Written for a **layperson handling their own side** of a **non-family** personal legal matter. Filed under `personal-self-advocacy/` with matter-specific subdirectories; naming convention `legalprep_{function}.md`; frontmatter `category: legalprep`, `intended_use: model-testing`.

**Conventions (distinct from the practitioner library):** required jurisdiction input; mandatory **Safety Block** (verified resources only — no invented hotline numbers; `[VERIFY:]` where a number is uncertain); load-bearing **not-legal-advice** boundary; **no legal conclusions** ("this *is* harassment/defamation/retaliation/infringement"), no citations, no outcome prediction, no court pleadings; organize/document/prepare only — routing legal questions to an attorney or the relevant authority. Where a channel is built for non-lawyers, a **self-submit variant** helps draft the user's *own* factual account/letter (labeled "NOT A LEGAL FILING"), with any statutory certification (e.g. DMCA good-faith/perjury statement) presented as the user's own attestation to read, verify, and sign.

| Subdirectory | Count | Contents |
|---|---|---|
| `cross-cutting/` | 6 | professional/authority router · incident documentation organizer · evidence-preservation & digital organizer · personal-legal chronology builder · professional handoff brief (anchor) · consultation-question builder |
| `workplace/` | 5 | workplace-concern documentation organizer · HR-complaint narrative preparer *(self-submit)* · EEOC/agency charge preparation organizer · retaliation log · wage-hour issue documentation organizer |
| `harassment-stalking/` | 5 | harassment/stalking incident log · protective-order preparation organizer *(self-submit)* · police-report account preparer *(self-submit)* · digital-safety & threat-evidence organizer · cyberharassment platform-report preparer *(self-submit)* |
| `defamation-reputation/` | 4 | defamation-concern documentation organizer · online content-removal/platform-report preparer *(self-submit)* · correction/retraction request preparer *(self-submit)* · reputation-harm impact log |
| `ip-theft/` | 4 | IP-infringement documentation organizer · DMCA takedown-notice preparer *(self-submit)* · ownership/priority evidence organizer · marketplace infringement-report preparer *(self-submit)* |
| `consumer-scams/` | 3 | consumer-complaint documentation organizer · scam/fraud report preparer *(self-submit)* · refund/chargeback dispute preparer *(self-submit)* |
| `housing-landlord-tenant/` | 3 | tenant-issue documentation organizer · landlord notice-response preparer *(self-submit)* · security-deposit dispute preparer *(self-submit)* |
| `identity-theft/` | 2 | identity-theft documentation & report preparer *(self-submit)* · fraud-dispute narrative preparer *(self-submit)* |
| `debt-collection/` | 2 | debt-validation/dispute letter preparer *(self-submit)* · collection-harassment documentation log |
| `small-claims/` | 2 | small-claims case preparation organizer · small-claims hearing preparation & testimony practice |

Attorney-side counterparts remain in the practitioner library (`employment-labor/`, `ip/`, `litigation/`, `client-intake-communications/`) and are cross-linked from each prompt.

---

## Phase 3 — Field Guide and Cross-Cutting Resources (~10 prompts)

### `field_guide.md` (one document, not a prompt)
- Citation conventions (Bluebook, ALWD, state-specific)
- Pleading-standard quick reference
- Document and motion captioning by jurisdiction
- Privilege quick map
- Evidentiary-objection cheat sheet
- Common procedural deadlines (federal default, state outliers)

### Cross-cutting (~10)
| File | Subdirectory | Description |
|---|---|---|
| `legal_litigation_hold_notice_drafter.md` | discovery | Litigation hold notice and acknowledgment with custodian-specific instructions |
| `legal_30b6_notice_drafter.md` | discovery | Companion to existing 30(b)(6) outline — drafts the notice topics |
| `legal_subpoena_drafter.md` | discovery | Rule 45 subpoena with scope, place of compliance, objection deadlines |
| `legal_protective_order_drafter.md` | discovery | Negotiated protective order with confidentiality tiers, AEO, source code, clawback |
| `legal_settlement_agreement_drafter.md` | litigation | Comprehensive settlement agreement: release scope, confidentiality, non-disparagement, allocation, taxes |
| `legal_mediation_position_paper.md` | litigation | Mediation submission: case posture, leverage, settlement bands, decision-tree |
| `legal_motion_for_protective_order_drafter.md` | discovery | Motion for protective order on overbroad discovery, deposition scope, or subpoena |
| `legal_motion_to_compel_drafter.md` | discovery | Motion to compel with deficiency log, meet-and-confer record, fee-shifting request |
| `legal_attorney_fee_petition.md` | litigation | Lodestar fee petition with hours, rates, multipliers, fee-shifting basis |
| `legal_post_trial_motion_set.md` | litigation | Renewed JMOL, new trial, remittitur, alteration-of-judgment motions |

---

## Phase 4 — Stretch / Specialized (Authored Last)

These are valuable but lower-priority because the audience is narrower or because Phase 1–3 covers most evaluation needs.

| File | Topic |
|---|---|
| `legal_admin_law_apa_review.md` | Administrative law: APA challenge analysis, arbitrary-and-capricious framing |
| `legal_securities_disclosure_review.md` | 10-K/10-Q risk-factor and MD&A review |
| `legal_antitrust_merger_clearance_memo.md` | HSR analysis, merger-clearance theory of harm, remedies posture |
| `legal_ada_accommodation_dialogue_script.md` | Interactive process for accommodation requests |
| `legal_class_certification_analysis.md` | Rule 23 numerosity / commonality / typicality / adequacy / predominance / superiority |
| `legal_arbitration_demand_drafter.md` | AAA / JAMS arbitration demand with claim recitation and relief |
| `legal_environmental_permit_analysis.md` | NEPA / CWA / CAA permit posture and challenge analysis |
| `legal_government_contract_dispute_memo.md` | CDA claim, REA, termination-for-convenience analysis |
| `legal_healthcare_stark_kickback_review.md` | Stark / AKS analysis on a referral arrangement |
| `legal_election_law_compliance_review.md` | Campaign finance, lobbying registration, gift rule analysis |

---

## Tracking Targets

| Phase | Subdirectories | Prompts | Cumulative |
|---|---|---|---|
| Phase 1 (shipped) | research, litigation, discovery, depositions | 25 | 25 |
| Phase 2A | contracts-transactional, corporate-ma, employment-labor, ip, client-intake-communications, in-house-legalops, + 4 deferred from Phase 1 | 42 | 67 |
| Phase 2B | regulatory-compliance, privacy-data, ethics-professional-conduct | 12 | 79 |
| Phase 2C | bankruptcy-restructuring, tax, immigration, family, criminal, appellate, real-estate, trusts-estates | 35 | 114 |
| Personal Self-Advocacy (shipped, litigant-facing track) | cross-cutting, workplace, harassment-stalking, defamation-reputation, ip-theft, consumer-scams, housing-landlord-tenant, identity-theft, debt-collection, small-claims | 36 | — |
| Phase 3 | field_guide.md + cross-cutting | 10 | 124 |
| Phase 4 (stretch) | specialized topics | 10 | 134 |

---

## Authoring Conventions (Reaffirmed)

Every Phase 2+ prompt must include:

- **Frontmatter** with title, category, description, technique IDs, difficulty tag, tags, updated date, and at least three `related_prompts` cross-references.
- **Required jurisdiction input** (and governing-law / venue / posture where applicable).
- **No-fabrication clause** specifically targeting case names, statutory cites, regulatory provisions, and quoted text. Use `[CITE: ...]`, `[NEED PIN: ...]`, `[NEED HOLDING: ...]` placeholders.
- **Locked output format** sized to the deliverable (memo, motion caption, redline, table schema).
- **Verification block** with self-check items including jurisdiction lock, citation discipline, scope discipline, and any task-specific risks.
- **False-positive matrix** capturing the most common model failure modes for that task.
- **No generic refusal or "consult a licensed attorney" boilerplate.** Substantive guardrails replace performative ones.

## Cross-Repository Updates

After Phase 2A landed (2026-05-11):
- ✓ Updated `CLAUDE.md` with `domain-legal/` routing block and a "User says X → use Y" table.
- ☐ Update `PROMPT_INDEX.json` and `PROMPT_INDEX.md` to include all `domain-legal/` entries (pending).
- ☐ Add a domain entry to top-level `README.md`'s domain index (pending).
- ☐ Add a `domain-legal/field_guide.md` once Phase 2B surfaces additional recurring conventions (deferred).

After the Personal Self-Advocacy set landed (2026-07-23):
- ✓ Added `personal-self-advocacy/README.md` (umbrella convention, Safety Block spec, matter file map, routing).
- ✓ Updated `domain-legal/README.md` (two-exceptions note, directory map, routing rows).
- ✓ Updated root `CLAUDE.md` Legal section with a routing block + quick-reference rows.
- ✓ Registered the 36 new prompts in `PROMPT_INDEX.json` / `PROMPT_INDEX.md`.

## Authoring Order Recommendation

1. **Phase 2A first.** Highest daily-workflow density; broadest practitioner relevance.
2. **Phase 2B next.** Regulatory and compliance patterns recur across industries and pair well with Phase 2A transactional and in-house work.
3. **Phase 2C last among the planned set.** Practice-area specialty work; useful for evaluating whether models can handle jurisdiction-specific and procedurally-distinct workflows.
4. **Phase 3** in parallel with 2A–2C as cross-cutting needs surface.
5. **Phase 4** only after the core 124 are evaluated and gaps are identified empirically.
