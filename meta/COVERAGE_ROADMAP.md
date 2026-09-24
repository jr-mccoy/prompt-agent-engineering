# Coverage Roadmap: Subject-Matter Gaps Across the Prompt Corpus

**Status as of 2026-09-24:** **Waves 1–4 shipped.**
- **Wave 1:** 40 prompts. That is four new domains of 8 prompts each (ADR-0043)
  and `domain-personal-development/job-search/` (8). Six hollow READMEs now
  describe what actually exists.
- **Wave 2:** 64 prompts across ten areas (§6), plus 7 identity-preserving moves.
- **Wave 3:** 103 prompts built from the domains' own roadmaps (§6).
- **Wave 4:** 59 prompts adding depth to 11 thin domains, plus a structural cleanup: 8 duplicate presentation prompts retired and 5 decision-making prompts moved (§6).
- **Survival:** every specified candidate survived its duplicate sweep in Waves 1–3. In Wave 4, 4 of 63 candidates were dropped as duplicates of existing prompts or skills (§6). Wave 2's candidate list had already been cut by a pre-sweep, described in §6.
- **Remaining:** Wave 5, plus the Wave 3 tiers deferred below, are scoped only as far as their boundaries. This document records a repository-wide audit of where the prompt
corpus is thin on subject matter and sequences the fix into five waves.

**Why a cross-repo roadmap.** Each domain's `EXPANSION_ROADMAP.md` plans growth
*inside* its own boundary. None of them can see the subjects that have no domain
at all, or two domains that each assume the other one covers something. This file
covers only that cross-domain view. Where a domain already has a roadmap, this
file cites it rather than copying it.

**What counts as a gap.** A gap is a subject with real demand where
`pae search` either returns nothing or returns resources about something else. A
low file count on its own isn't a gap: `domain-deep-analysis` is small and
complete.

---

## 1. Method (re-runnable)

1. **Distribution.** Count prompt files per `domain-*` directory and compare
   them against the domain's README.
2. **Topic scan.** Take 42 candidate real-world subjects and match each one
   against filenames and titles in every `domain-*` directory outside
   `domain-agentic-resources/`. False positives are removed by hand
   ("script" matching "scripture", `emotionalfitness_*` matching "fitness").
   Counts over body text alone run 5–20× high and weren't used.
3. **Skill sweep.** Check `domain-agentic-resources/skills/` separately. The
   last content phase kept 9 of 24 candidates (38%) because
   `skills/marketing/` already owned the territory.
4. **Router probes.** Run `pae search "<task>"` on a realistic task in each
   candidate subject and read the top three hits (§2).
5. **Backlog sweep.** Read every `EXPANSION_ROADMAP.md` and check whether each
   named file exists on disk.

## 2. Router probes

**Before:** top hits on 2026-09-24, before any Wave 1 content.
**After Wave 1:** the table that follows this one.

| Query | Top hits today | Reading |
|---|---|---|
| `song lyrics songwriting` | *(no hits)* | Absent |
| `strength training program` | `education-teaching/program/faculty-development/*`, `program/accreditation-review/*` | Absent: matched the word "program" |
| `job interview preparation` | `idea-to-product/stage-2-problem-validation/*`, `legal/family-self-advocacy/legalprep-custody-evaluation*` | Absent |
| `lean six sigma manufacturing` | `software-engineering/analysis/business/lean-canvas-*` | Absent |
| `restaurant menu pricing` | `education-teaching/instructor/student-support/*`, `psychology/client-self-use/*` | Absent |
| `ESG sustainability report` | `ai-ml/responsible-ai-governance/rai-sustainability-carbon*`, a discipleship mentor-sustainability prompt | Absent |
| `rental property analysis` | `legal/divorce/legal-marital-property-*`, `testing-qa/property-based-testing` | Absent |
| `podcast episode outline` | `image-generation/publishing-covers/cover-podcast-art`, two psychology prompts | Absent |
| `philosophy ethics essay` | memoir, grading-feedback and college-student guides | Absent |
| `grant proposal nonprofit` | `science/grants-funding/*` (NSF, ERC) | Research grants only |
| `SQL query churn cohort analysis` | `software-engineering/analysis/database/*`, SQL optimization skill | Engineer framing; no analyst craft |
| `cold outreach sales email sequence` | `skills/marketing/cold-email`, a slop checker, `sales-automator` | Covered by skills; don't duplicate |
| `usability test plan UX research` | `agents/design/design-ux-researcher`, voice-UX best practice | Agent only; no method prompts |
| `accounting bookkeeping month end close` | `finance/accounting-controllership/finance_month_end_close*` | Well covered |

**After Wave 1**, same day:

| Query | Top hit now | Reading |
|---|---|---|
| `strength training program` | `health-wellness/fitness/fitness-beginner-training-plan` | Fixed |
| `job interview preparation` | `personal-development/job-search/jobsearch-behavioral-interview-story-bank` | Fixed |
| `write a resume for a job posting` | `jobsearch-job-posting-fit-decoder`, `-cover-letter-builder`, `-resume-evidence-rewriter` (top 3) | Fixed |
| `lean six sigma manufacturing` | `operations/process-improvement/ops-dmaic-project-charter` | Fixed |
| `MEDDPICC deal qualification` | `sales-customer/sales/sales-deal-qualification-scorecard` | Fixed |
| `support ticket triage` | `sales-customer/support/support-ticket-triage-and-routing` | Fixed |
| `why did this metric drop` | `data-analytics/analysis-and-sql/analytics-metric-movement-investigation` | Fixed |
| `SQL query churn cohort analysis` | `data-analytics/analysis-and-sql/analytics-cohort-retention-analysis` | Fixed |
| `meal plan nutrition` | `health-wellness/nutrition/nutrition-meal-structure-planner`; `home_meal_plan_week` 3rd | Fixed; logistics prompt kept |
| `cold outreach sales email sequence` | `skills/marketing/cold-email` (unchanged) | Correct: the skill still owns copy |
| `song lyrics`, `grant proposal nonprofit` | unchanged | Wave 2 subjects |
| `restaurant menu pricing` | unchanged | Hospitality is deferred (§7) |

**Regression set.** The 120-case set scores the same as before Wave 1
(scope@1 83.5%, kind@1 97.6%), and no case changes its top hit. The one case
that did shift during Wave 1 is case-072, "board deck for the quarterly business
review", which expects `domain-presentations/`. The customer QBR prompt briefly
outranked the internal QBR deck. That was a metadata problem, not a better
answer, so the prompt was renamed `cs_customer_qbr_prep.md` and the word "deck"
was taken out of its description. The case label was not changed.

**After Wave 2**, same day:

| Query | Top hit now | Reading |
|---|---|---|
| `song lyrics songwriting` | `creative-writing/songwriting/writing-song-lyric-craft-workshop` | Fixed (had no hits at all) |
| `grant proposal nonprofit` | `business-strategy/nonprofit/nonprofit-foundation-grant-proposal`; research grants 3rd | Fixed |
| `donor appeal letter` | `business-strategy/nonprofit/nonprofit-donor-appeal-letter` | Fixed |
| `raise prices at my shop` | `business-strategy/small-business/smallbiz-price-increase-plan` | Fixed |
| `rental property analysis` | `specialized-fields/real-estate/realestate-rental-property-underwriting` | Fixed |
| `comparative market analysis for a listing` | `specialized-fields/real-estate/realestate-comparative-market-analysis` | Fixed |
| `ransomware incident response playbook` | `risk/risk-security-incident-response-playbook` | Fixed |
| `what to do after a parent dies paperwork` | `home-life/home-household-paperwork-system`, then `home-after-death-admin-checklist` | Fixed |
| `usability test plan UX research` | `frontend-development/ux-research/frontend-ux-usability-test-plan` | Fixed |
| `podcast episode outline` | `professional-writing/content-production/content-podcast-episode-outline` | Fixed |
| `news article inverted pyramid` | `professional-writing/writing/writing-news-article-inverted-pyramid` | Fixed |
| `philosophy ethics essay` | `learning/learning-ethics-dilemma-multi-framework` | Fixed |
| `practice Spanish conversation at B1 level` | `conversation-practice/conversation-lang-sim-master-template` | Fixed |
| `restaurant menu pricing` | unchanged | Deferred (hospitality, §7) |

**Regression set after Wave 2.** The scores are unchanged (scope@1 83.5%,
kind@1 97.6%). No case changes its top hit, compared case by case against the
end of Wave 1.

## 3. Gap map

### A. Subjects with no domain home

Ranked by real-world demand × current absence.

| # | Subject | Current state | Severity |
|---|---|---|---|
| 1 | **Job search (candidate side):** résumé, cover letter, LinkedIn, interview story bank, search cadence | 0 prompts. `personal-development/prompts/career/` is 17 AI-role career guides. Offers and salary are covered in `negotiation/`. | 5 |
| 2 | **Sales:** qualification, close plans, forecast review, account strategy | ~5 prompts in `business-strategy/go-to-market/` and `negotiation/contexts/`. Outbound copy and collateral are owned by `skills/marketing/`. | 5 |
| 3 | **Customer support / success:** triage, escalations, QBRs, renewals | ~5 prompts | 4 |
| 4 | **Business analytics:** metric definitions, SQL correctness, metric-movement investigation, experiment readouts | Split across ML eval, finance and board decks. Research statistics are covered in `science/statistics/`. | 4 |
| 5 | **Operations:** process improvement, lean/six sigma, suppliers, inventory, procurement, non-software projects | ~0. `risk_fmea_analysis` and one vendor evaluation exist. | 4 |
| 6 | **Consumer health and wellness:** training, nutrition, sleep for healthy adults | 0. `home_meal_plan_week` is meal logistics only. CBT-I and exercise-for-depression are in psychology. | 4 |
| 7 | **Small-business owner operations** (local shops, trades, freelancers) | Startup and solo-dev framing only | 3 |
| 8 | **Nonprofit and fundraising:** grants, donor appeals, board governance, impact reports | Research grants only | 3 |
| 9 | **Real estate and trades professionals** | Promised by `specialized-fields` and never built. One-off `domain_writing_*` files exist. | 3 |
| 10 | **UX research methods** | A single agent and one research-synthesis prompt | 3 |
| 11 | **Estate planning, household admin, family caregiving** | One aging-parent prompt and one beneficiary review | 3 |
| 12 | **Security operations (non-code):** IR playbooks, tabletop exercises, phishing awareness | ~2 prompts. AppSec is well covered (~40). | 3 |
| 13 | **Media production:** music and songwriting (0), podcast and video, journalism | 5 `content-production/` prompts | 3 |
| 14 | **Humanities self-study:** history, philosophy | Two tutoring drills | 2 |
| 15 | ESG, event planning, travel, hospitality, veterinary/pets, agriculture, interfaith | ≤2 each | 1–2 |

**Well covered (no action):** DevOps/SRE/cloud, AppSec and privacy
compliance (GDPR, SOC 2), mental-health self-help (~71), K-12 and higher
education, math tutoring, corporate accounting.

### B. Hollow or mis-described domains

| Domain | Files | Problem |
|---|---|---|
| `domain-specialized-fields` | 2 | The README names 26 `professional_*.md` files that don't exist anywhere. |
| `domain-conversation-practice` | 8 | The README promises language practice in 7 languages (`spanish/`, `french/`). The content is persuasion-persona simulators. |
| `domain-learning-coding` | 17 | The README lists `tutorials/`, `exercises/` and `explanations/` with "TBD" counts. Those folders don't exist. |
| `domain-game-development` | 24 | The README says "24 of 47" and cites a `MISSING_TOPICS_ANALYSIS.md` that doesn't exist. |
| `domain-decision-making` | 42 | The README describes `tradeoffs/`, `blind-spots/` and `frameworks/` folders that don't exist. |
| `domain-policy` | 4 | The README lists 1 of the 4 files. |
| `domain-advertising` | 17 | Static ad images only. The README is accurate but has no "not here" boundary for copy, video or media planning. |
| `domain-presentations` | 45 | About 9 near-duplicate root pairs, e.g. `powerpoint_board_deck` / `powerpoint_board_deck_generator`. |

### C. Thin but coherent domains

| Domain | Missing subtopics |
|---|---|
| `hr-management` | Career ladder, promotion packet, engagement survey, RIF plan, handbook policy, succession, pay equity |
| `product-management` | PR/FAQ, release notes, product experiment design, stakeholder update. PM content is spread across four domains. |
| `risk` | Vendor/third-party risk, KRIs, bow-tie, quantitative (Monte Carlo), risk-acceptance memo, board risk report, non-technical incident playbook |
| `ideation` | How-Might-We, Six Thinking Hats, TRIZ, morphological matrix, affinity mapping, workshop facilitation |
| `creative-writing` | Romance, horror, thriller, TV pilot / series bible, lyrics, comedy, line edit, continuity audit |
| `voice-conversational-ui` | SSML/TTS tuning, IVR, human handoff, realtime barge-in, transcript QA |
| `written-advocacy` | Airline compensation, tax penalty abatement, student-loan servicer, HOA and contractor disputes, prior authorization |
| `research-academic` | Thesis structuring, power analysis, mixed methods, data management plan |

### D. Already-planned, unbuilt backlog

These are built from their own roadmaps, not re-planned here.

| Source roadmap | Unbuilt |
|---|---|
| [`domain-legal/EXPANSION_ROADMAP.md`](../domain-legal/EXPANSION_ROADMAP.md) | Phase 2B (12), 2C (30), 3 (10), 4 (10) |
| [`domain-healthcare-clinical/EXPANSION_ROADMAP.md`](../domain-healthcare-clinical/EXPANSION_ROADMAP.md) | Lane 2 `interp_*`: 14 of 22. Lane 7 `specialty_*`: 18 of 18. |
| [`domain-psychology/REMAINING_PROMPTS_ROADMAP.md`](../domain-psychology/REMAINING_PROMPTS_ROADMAP.md) | Wave 13: 10 `clientself_*` specialty prompts |
| [`domain-childrens-writing/EXPANSION_ROADMAP.md`](../domain-childrens-writing/EXPANSION_ROADMAP.md) | 12 brainstorm items, 0 built |
| [`domain-psy-ops/EXPANSION_ROADMAP.md`](../domain-psy-ops/EXPANSION_ROADMAP.md) | 9 Wave 2 candidates |
| [`domain-negotiation/EXPANSION_ROADMAP.md`](../domain-negotiation/EXPANSION_ROADMAP.md) | Wave 2 contexts: landlord, insurance, medical bill, severance, licensing |

## 4. Taxonomy decision ([ADR-0043](adr/0043-subject-homes-for-sales-health-analytics-ops.md))

Subject decides first (`CLAUDE.md`). For six of the absent subjects the
existing domains have no home that fits by subject, only near misses by theme.
The proposal adds **four** domains and folds everything else into existing
domains.

| New domain | Object of the prompt | Distinct from |
|---|---|---|
| `domain-sales-customer/` | A deal, pipeline, customer account, or support queue | `skills/marketing/` (outbound copy, collateral); `negotiation/` (the negotiation itself); `business-strategy/go-to-market/` (marketing strategy, which stays there) |
| `domain-data-analytics/` | A business metric, query, dashboard, or experiment readout | `science/statistics/` (research inference); `AI-ML/` (models); `presentations/board-decks/` (rendering) |
| `domain-operations/` | A process, supplier, inventory, or non-software project | `risk/` (registers, FMEA, BCP); `engineering-workflows/` (software delivery) |
| `domain-health-wellness/` | A healthy adult's own training, eating, or sleep | `healthcare-clinical/` (the clinician holds the prompt); `psychology/client-self-use/` (mental health, CBT-I) |

**Folded into existing domains:**
- Job search → `domain-personal-development/job-search/` (Self scope).
- Nonprofit and small-business ops → `domain-business-strategy/` subfolders.
- Real estate and trades → a rebuilt `domain-specialized-fields/`.

**What the taxonomy change touches.** A new domain is wired into code at only two
points:
- `DOMAIN_DIRS` in `scripts/generate_prompt_index.py`. `scripts/pae_registry/membership.py`
  parses it and `generate_repo_facts.py` checks it against disk.
- `SAFETY_SENSITIVE_ROOTS` in `scripts/pae_registry/governance.py`, for
  `domain-health-wellness` only, so it is served `safety_gated` like clinical and
  psychology.

`structure.yml`, the naming validator and the engine all pick up `domain-*`
automatically.

Hand-maintained documents that change:
- `CLAUDE.md`: domain count and list, four subject-table rows, and a rewrite of
  the worked example that calls sales and customer success "org".
- `meta/ROUTING_REFERENCE.md`.
- `REPO_MAP.md`.
- The `README.md` domain library.
- `meta/registry/README.md` (its hand-written "44").

**No moves in Wave 1.** These five files stay put and are cross-linked from the
new domain:
- `go-to-market/workflow_sales_discovery_call_preparation`
- `workflow_sales_pipeline_risk_assessment`
- `workflow_win_loss_analysis`
- `workflow_cs_account_health`
- `workflow_customer_success_onboarding_plan`

They were relocated in Wave 2 through `meta/REORG_MAP.tsv`, each with an alias
row for its old public id. (An earlier version of this section said a move adds
tombstones. It does not; only `DELETED` rows do. A move changes only the
relationship-count test.)

## 5. Wave 1: shipped (40 prompts, all **NEW**, plus README repairs)

Every prompt follows the Tier 1 template in `PROMPT_QUALITY_STANDARDS.md`:
- **Frontmatter:** 3–5 real technique IDs and exactly 3 resolving
  `related_prompts`.
- **When to Use** names the bracketed neighbour below as what the prompt is
  **distinct from**.
- **False-Positive Prevention** is required.
- **Filenames:** 55 characters or fewer, one prefix per subfolder.

Any candidate killed by its duplicate sweep is dropped and counted in the
CHANGELOG survival rate. No substitute is invented to hit the number.

### `domain-personal-development/job-search/` (8), prefix `jobsearch_`

| File | Nearest neighbour (distinct from) |
|---|---|
| `jobsearch_target_role_and_market_map.md` | `career_internal_vs_external_move` |
| `jobsearch_resume_evidence_rewriter.md` | `career_residual_skills_inventory` |
| `jobsearch_job_posting_fit_decoder.md` | `hr_job_description_writer` (employer side) |
| `jobsearch_cover_letter_builder.md` | none |
| `jobsearch_linkedin_profile_audit.md` | `career_positioning_statement` |
| `jobsearch_networking_outreach_plan.md` | `hr_sourcing_outreach` (recruiter side); `skills/marketing/cold-email` |
| `jobsearch_behavioral_interview_story_bank.md` | `mllearn_ml_interview_prep` (ML only) |
| `jobsearch_pipeline_tracker_and_cadence.md` | `lifetransition_job_loss_recovery_plan`; hands off to `personal_career_offer_evaluation` and `negotiation_salary_raise_promotion` |

### `domain-sales-customer/` (8)

| File | Nearest neighbour (distinct from) |
|---|---|
| `sales/sales_deal_qualification_scorecard.md` | `workflow_sales_discovery_call_preparation` |
| `sales/sales_outbound_prospecting_sequence.md` | `skills/marketing/cold-email`, `sales-enablement`. Stays at account-strategy level, not copywriting. |
| `sales/sales_mutual_close_plan.md` | `negotiation_closing_and_final_concession` |
| `sales/sales_forecast_commit_review.md` | `workflow_sales_pipeline_risk_assessment` |
| `customer-success/cs_customer_qbr_prep.md` | `workflow_cs_account_health` |
| `customer-success/cs_renewal_risk_and_save_plan.md` | `skills/marketing/churn-prevention` (cancel flows) |
| `support/support_ticket_triage_and_routing.md` | `solo_dev_support_system` |
| `support/support_escalation_response_drafter.md` | `decisioning_escalation_decision_tree` |

### `domain-health-wellness/` (8), safety-gated

| File | Nearest neighbour (distinct from) |
|---|---|
| `foundations/wellness_readiness_and_red_flag_screen.md` | Entry gate. Routes red-flag symptoms to a clinician before anything else runs. |
| `foundations/wellness_sustainable_routine_designer.md` | `habits_habit_design_blueprint` |
| `fitness/fitness_beginner_training_plan.md` | none |
| `fitness/fitness_program_progression_review.md` | none |
| `fitness/fitness_endurance_event_build_plan.md` | none |
| `nutrition/nutrition_eating_pattern_audit.md` | Carries a STRONG-GUARD block for disordered eating |
| `nutrition/nutrition_meal_structure_planner.md` | `home_meal_plan_week` (logistics only) |
| `sleep-recovery/sleep_routine_and_environment_audit.md` | `clientself_sleep_cbt_i_sleep_restriction_calculator` (clinical insomnia) |

### `domain-data-analytics/` (8), prefix `analytics_`

| File | Nearest neighbour (distinct from) |
|---|---|
| `framing-and-metrics/analytics_question_to_analysis_plan.md` | `science_pre_specified_analysis_plan` (research) |
| `framing-and-metrics/analytics_metric_definition_spec.md` | `product_north_star_metric_definition` |
| `framing-and-metrics/analytics_kpi_tree_decomposition.md` | `skills/data-engineering/kpi-dashboard-design` |
| `analysis-and-sql/analytics_sql_query_correctness_review.md` | `sql-optimization-patterns` (performance, not grain, fan-out or nulls) |
| `analysis-and-sql/analytics_metric_movement_investigation.md` | `engineering_debugging_root_cause` |
| `analysis-and-sql/analytics_cohort_retention_analysis.md` | `boarddeck_cohort_retention_heatmap` (rendering) |
| `experiments-and-reporting/analytics_ab_test_readout.md` | `mleval_ab_test_design_for_models`; `skills/marketing/ab-test-setup` |
| `experiments-and-reporting/analytics_dashboard_critique.md` | `mlmonitor_monitoring_dashboard_design`; `solo_dev_metrics_dashboard` |

### `domain-operations/` (8), prefix `ops_`

| File | Nearest neighbour (distinct from) |
|---|---|
| `process-improvement/ops_process_map_and_waste_scan.md` | `business_writing_sop` (writing, not process design) |
| `process-improvement/ops_root_cause_a3_report.md` | `engineering_post_mortem_root_cause_ladder` |
| `process-improvement/ops_dmaic_project_charter.md` | `risk_fmea_analysis` |
| `process-improvement/ops_capacity_and_bottleneck_model.md` | `services_capacity_and_utilization_planner` |
| `supply-chain-procurement/ops_supplier_selection_scorecard.md` | `research_vendor_evaluation` (one product decision) |
| `supply-chain-procurement/ops_inventory_reorder_policy.md` | `ts_intermittent_demand_forecasting` |
| `supply-chain-procurement/ops_rfp_procurement_package.md` | `finance_bank_relationship_rfp_framework`; `business_writing_proposal` (seller side) |
| `project-delivery/ops_non_software_project_plan.md` | `product_delivery_sprint_planner` |

Each new domain gets a `README.md` covering:
- scope and a directory map
- a routing table
- **negative boundaries** ("X lives here, not there")
- guards, where relevant

It also gets a short local `EXPANSION_ROADMAP.md` that points back here.

### Hollow-README repairs (documentation only)

Each README now describes what exists. Promises it dropped moved into the later
waves below. No content was invented to match a stale promise. Where a README
still carried good material, the edit was surgical: `specialized-fields` keeps
its templates and loses only the table of `professional_*.md` files that never
existed.

| Domain | Change |
|---|---|
| `specialized-fields` | List the 2 real files. State the planned scope (real estate, trades, professional services; Wave 2). Point finance, sales and trades writing to their real homes. |
| `conversation-practice` | Describe it as persuasion-persona simulators. Language practice moves to Wave 2. |
| `learning-coding` | Replace the phantom tree with the 17 real flat files. |
| `decision-making` | Replace the phantom folders with the real `decisioning_*`, `scenario_*` and `tradeoff_*` families and `documentation/`. |
| `game-development` | Replace the dead `MISSING_TOPICS_ANALYSIS.md` reference with a link to Wave 4 here. |
| `policy` | List all 4 files. |
| `advertising` | **No change needed.** The README already has a "Route elsewhere for" table (added in an earlier phase). The audit that flagged it missed that section. |

## 6. Wave 2 (shipped) and later waves

### Wave 2: remaining absent subjects — shipped (64 prompts + 7 moves)

**Candidates dropped before writing.** Before anything was written, a duplicate
pre-sweep cut these candidates. Each already has an owner:
- non-lawyer engagement letter and standalone scope of work: `legal_engagement_letter_drafter`, `legal_sow_drafter`, client-services-studio stage 3;
- service-business pricing, shop supplier/inventory and a standalone 13-week
  forecast: `services_pricing_model_selector`, `ops_*`, `finance_cash_flow_forecasting_model`;
- nonprofit logic model: `program_logic_model_designer`;
- YouTube retention: `content_long_form_script`;
- news fact-check: three existing fact-checkers;
- generic language role-play, error-correction debrief and pronunciation drill: `domain-education-teaching/learner/language/`;
- voice-of-customer synthesis: `skills/marketing/customer-research`;
- standalone upsell map: the expansion section in `cs_account_health`.

The user chose to build the borderline humanities and language-sim candidates.
Each one states exactly what it is distinct from.

| Area | Shipped in | Prompts |
|---|---|---|
| Nonprofit and fundraising | `business-strategy/nonprofit/` (`nonprofit_*`) | 8 |
| Small-business owner ops | `business-strategy/small-business/` (`smallbiz_*`) | 6 |
| Real estate and trades | `specialized-fields/real-estate/`, `trades/` | 7 |
| Security operations (non-code) | `risk/` (`risk_security_*`, `risk_tabletop_*`, `risk_phishing_*`, `risk_vendor_security_*`, `risk_payment_fraud_*`) | 6 |
| Estate, household admin, caregiving | `personal-development/major-decisions/` (2), `productivity/home-life/` (5) | 7 |
| UX research methods | `frontend-development/ux-research/` (`frontend_ux_*`) | 7 |
| Songwriting and media production | `creative-writing/songwriting/` (2), `script-stage/` (1), `professional-writing/content-production/` (3), `professional-writing/writing/` (2) | 8 |
| Humanities self-study | `learning/` | 5 |
| Language conversation sims | `conversation-practice/` (`conversation_lang_sim_*`) | 6 |
| Sales and customer overflow | `sales-customer/` (strategic account plan, KB article, feedback routing loop, incident status update) | 4 |

**Moves in Wave 2** (committed separately): five go-to-market sales and CS
prompts went to `domain-sales-customer/`, and two `specialized-fields` legal
prompts went to `domain-legal/`. The uids were kept and the old ids resolve as
aliases. The original Wave 2 scoping table follows for the record.


| Area | Target folder | Est. | Boundary / nearest neighbour |
|---|---|---|---|
| Nonprofit and fundraising | `business-strategy/nonprofit/` | 8 | `science/grants-funding/` (research grants) |
| Small-business owner ops | `business-strategy/small-business/` | 8 | `startup/`, `client-services/` |
| Real estate, trades, professional services | `specialized-fields/` rebuild | 10 | `professional-writing/domain-specific/`. The 2 legal files move to `domain-legal`. |
| Security operations (non-code) | `risk/` | 5 | `software-engineering/analysis/security/` (code) |
| Estate and caregiving admin | `personal-development/major-decisions/`, `productivity/home-life/` | 6 | `personal_caring_for_aging_parent` |
| UX research methods | `frontend-development/` | 6 | `agents/design/design-ux-researcher` |
| Media production and music | `creative-writing/`, `professional-writing/content-production/` | 8 | `content_long_form_script` |
| Humanities self-study | `learning/` | 5 | `education-teaching/learner/study-by-discipline/` |
| Language conversation sims | `conversation-practice/` | 6 | `education-teaching/learner/language/` |
| Wave 1 overflow: account plan, KB article, voice-of-customer synthesis | `sales-customer/` | 4 | `skills/marketing/customer-research` |
| Relocate the 5 go-to-market sales and CS files, plus the 2 `specialized-fields` legal files | via `meta/REORG_MAP.tsv` + `aliases.tsv` | 7 moves | **Done.** uids kept; old ids resolve as aliases |

### Wave 3: existing backlog — shipped (103 prompts; committed plans only)

Each block was built from its own domain roadmap, and each roadmap now marks it shipped.

| Source roadmap | Built | Prompts |
|---|---|---|
| `domain-legal/EXPANSION_ROADMAP.md` Phase 2B | `regulatory-compliance/`, `privacy-data/`, `ethics-professional-conduct/` | 12 |
| `domain-legal/EXPANSION_ROADMAP.md` Phase 2C | `bankruptcy-restructuring/`, `tax/`, `immigration/`, `criminal/`, `appellate/`, `real-estate/`, `trusts-estates/` | 35 |
| `domain-healthcare-clinical/EXPANSION_ROADMAP.md` Lane 2 | `prompts/interpretation/interp_*` (the last 14) | 14 |
| `domain-healthcare-clinical/EXPANSION_ROADMAP.md` Lane 7 | `prompts/specialty/specialty_*` | 18 |
| `domain-psychology/REMAINING_PROMPTS_ROADMAP.md` W13 | `client-self-use/specialty/clientself_*` | 10 |
| `domain-psy-ops/EXPANSION_ROADMAP.md` Wave 2 | across the six existing subfolders | 9 |
| `domain-negotiation/EXPANSION_ROADMAP.md` Wave 2 | `contexts/` (landlord, insurance, medical bill, severance, licensing) | 5 |

**Deferred by the user's scope choice ("committed plans only"):**
- legal Phase 3 (cross-cutting and field guide) and Phase 4 (stretch);
- `domain-childrens-writing/EXPANSION_ROADMAP.md`, whose own roadmap calls its 12 items brainstorm only.

**Found and fixed while building:**
- `prompts/reasoning/workup_dizziness_vertigo.md` treated new unilateral hearing loss as a peripheral sign. That contradicted HINTS+ and the file's own worked example. It is now a central sign until stroke is excluded, and a duplicated troponin line is gone.
- The negotiation README was missing `negotiation_hiring_offer_employer_side.md`. It is now listed.

**Review before wider use:**
- The psy-ops roadmap made child-safety review a condition for the youth-manipulation prompt. Human review is still recommended.
- The dosing and thresholds in the healthcare worked examples are recommended for a clinician read-through.

### Wave 4: thin-domain depth — shipped (59 prompts + cleanup)

| Domain | Added | Prompts |
|---|---|---|
| `hr-management` | career ladder, promotion case, engagement survey, reduction in force, succession, pay equity audit | 6 |
| `product-management` | PR/FAQ, release notes, experiment design, stakeholder update | 4 |
| `risk` | third-party risk, KRIs, bow-tie, Monte Carlo, risk acceptance memo, board risk report | 6 |
| `research-academic` | thesis structure, mixed-methods design | 2 |
| `ideation` | How-Might-We, Six Hats, TRIZ, morphological matrix, affinity clustering, workshop facilitation | 6 |
| `presentations/narrative-delivery/` | investor pitch narrative, keynote arc, hostile Q&A prep, speaker rehearsal coach | 4 |
| `creative-writing` | romance, horror, thriller workshops; TV pilot and series bible; comedy craft; continuity audit | 6 |
| `voice-conversational-ui` | SSML/TTS tuning, IVR call flow, realtime turn-taking, human handoff, transcript QA rubric | 5 |
| `written-advocacy` | travel refund, tax penalty relief, student-loan dispute, HOA request, medical records, prior authorization | 6 |
| `advertising/campaign/` | copy variant matrix, UGC video script, placement spec checklist, media plan, claims compliance | 5 |
| `game-development` | quest and dialogue design, NPC AI, level blockout, playtest synthesis, combat balancing, HUD/feel, live-ops ethics, publisher pitch, postmortem | 9 |

**Dropped as duplicates (4):**
- research power analysis → `domain-science/methods-foundations/science_power_and_sample_size_calculator.md`
- data management plan → `domain-science/computational/science_data_management_plan_drafter.md`
- HR handbook policy → `skills/non-coding/business/employment-contract-templates`
- creative-writing line edit → `writing_revision_and_self_editing.md`

The contractor-dispute letter was also dropped, because `advocacy_service_nonperformance_demand.md` already covers it. Advertising was expanded beyond images at the user's explicit request; its README now separates campaign prompts from what the marketing skills still own.

**Routing after Wave 4:** scope@1 rose from 83.5% to 84.7%. Two cases changed their top hit, both acceptably: case-004 now reaches its expected `discipleship` scope, and case-084 ("risk analysis") now ranks the bow-tie prompt ahead of FMEA, still inside `risk`. Every Wave 4 probe lands on its new prompt.

**Cleanup, committed separately:** the `presentations` dedupe (8 retired copies) and the `decision-making` rehome (5 moves).

**Left for later:**
- The bot-to-human handoff prompt expands steps that already exist in two older chatbot prompts. Those could be trimmed to a pointer.
- No prompt scores human support agents' calls. The transcript QA rubric covers bot conversations only.


Wave 4 covers §3C, plus these items:
- `advertising` beyond images: copy, video/UGC scripts, platform specs, media
  plan, compliance.
- `presentations`: dedupe (**done**: eight duplicate copies retired as `merged-into` tombstones), then add the investor pitch deck, a conference
  talk, and Q&A prep.
- `decision-making` rehome (**done**): three crisis prompts → `domain-risk/`, competitive intelligence → `business-strategy/research/`, pricing experiments → `product-management/prompts/`.
- `game-development` Phase 2: narrative, NPC AI, playtest, balance, live-ops.

### Wave 5: routing regression cases

Add cases for the new scopes to
`pae-engine/tests/data/search_routing_regression.v1.json`. They must pass the
leakage audit (ADR-0037).

## 7. Explicitly not gaps / deferred

| Subject | Why not now |
|---|---|
| Agriculture, veterinary | Low demand relative to effort. Each needs a subject-matter owner. |
| Interfaith / comparative religion | The two faith domains are Christian by design. A comparative domain needs its own owner and review. |
| ESG / sustainability reporting | Reporting frameworks are moving fast. Revisit once one framework settles. |
| Travel, events, hospitality | `productivity/home-life/` covers the personal version adequately |
| DevOps, AppSec, mental-health self-help, K-12 | Already well covered (§3A) |

## 8. Guards

- **`domain-health-wellness`:**
  - The README carries a load-bearing safety guard.
  - The red-flag screen runs first.
  - Nutrition prompts carry a STRONG-GUARD for disordered eating.
  - Nothing prescribes for a diagnosed condition; those route to the clinician.
- **Sales, analytics, operations:** they have no safety gating. Each README states
  its negative boundary against `skills/marketing/` and `skills/data-engineering/`.
- **Router regression risks:**
  - case-046 ("MQL to SQL handoff" expects a skill) is at risk from the SQL
    prompts.
  - case-076 ("salary negotiation" expects `negotiation`) is at risk from job
    search, so job-search titles and tags leave out "salary".

## 9. Post-change checklist (per wave)

```
python3 scripts/generate_prompt_index.py
python3 scripts/generate_registry.py --write        # review new identity.tsv rows by hand
python3 scripts/generate_repo_facts.py --write
# bump counts in scripts/pae_registry/tests/test_generation.py
python3 domain-agentic-resources/inventory_counts.py --check
python3 scripts/validate_naming_conventions.py --ci
python3 scripts/validate_technique_catalog.py && python3 audit_technique_index.py
python3 scripts/check_relative_links.py
python3 scripts/check_frontmatter_references.py --check
python3 scripts/check_vendored_copies.py
python3 scripts/apply_reorg_map.py --check
(cd scripts && python3 -m unittest discover -s pae_registry/tests -t . -v)
python3 -m unittest discover -s tests -v
(cd pae-engine && python3 -m unittest discover -s tests -t tests -v)
```

Then re-run the §2 probes and record the after column. If a regression case
drops, fix the metadata. Relabel a case only when the new resource is genuinely
the better answer, and say so in the CHANGELOG.
