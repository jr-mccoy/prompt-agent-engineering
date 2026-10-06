# Coverage Roadmap: Subject-Matter Gaps Across the Prompt Corpus

**Status as of 2026-10-06:** **Waves 1–12 shipped (§6); quality backfill in progress (§6).**
- **Quality backfill (2026-10-06):** raising the weakest existing prompts: the `domain_writing_*` stubs, missing False-Positive Prevention sections, and missing frontmatter or technique metadata, in batches of about 30 files (§6).
- **Wave 12 (2026-10-05):** 11 prompts finishing biblical-studies Phase 3C: a pastoral Scripture-selection layer (`pastoral-scripture/`, 5, selection only, with crisis and abuse routing), Jewish–Christian dialogue (`jewish-christian-dialogue/`, 3) and digital study tools (`learner-self-study/`, 3), plus 7 routing cases (§6).
- **Wave 11 (2026-10-05):** 22 professional-facing prompts building all eight planned `domain-parenting/family-support-professional/` subfolders (intake, coaching, documentation, groups, referral, home visiting, foster/kinship/adoption, culturally responsive practice), each non-diagnostic with jurisdiction-aware reporting steps, plus 9 routing cases (§6).
- **Wave 10 (2026-10-04):** technique hygiene (13 undefined codes remapped in 110 files, a CI check on every prompt's `techniques:` list) and agentic-resource depth (7 skills, 4 agents, 4 commands, 4 personas; 3 one-skill categories folded into real ones).
- **Wave 9 (2026-10-03):** 39 prompts deepening thin subfolders in frontend, game development, creative writing and seven single-prompt folders, plus 15 routing cases (§6).
- **Wave 8 (2026-10-03):** 36 prompts on the second set of absent subjects (security operations, data engineering, FinOps, design systems, accessibility beyond components, ML for science, dementia care, DIY, cooking, special-education disputes, dating) and the first part of biblical-studies Phase 3C, plus 13 routing cases (§6).
- **Wave 7 (2026-10-03):** 46 prompts finishing the parenting caregiver folders, public administration, personal-development and negotiation Wave 2 items, institution-side student success, maintenance and reliability, and professional-services firm operations, plus 16 routing cases (§6).
- **Wave 6 (2026-10-02):** 48 prompts filling documented-but-unbuilt promises (parenting, policy, the operations / data-analytics / health-wellness Wave 2 lists) and six absent subjects, plus 15 routing regression cases and a CI repair (§6).
- **Wave 1:** 40 prompts. That is four new domains of 8 prompts each (ADR-0043)
  and `domain-personal-development/job-search/` (8). Six hollow READMEs now
  describe what actually exists.
- **Wave 2:** 64 prompts across ten areas (§6), plus 7 identity-preserving moves.
- **Wave 3:** 103 prompts built from the domains' own roadmaps (§6).
- **Wave 4:** 59 prompts adding depth to 11 thin domains, plus a structural cleanup: 8 duplicate presentation prompts retired and 5 decision-making prompts moved (§6).
- **Survival:** every specified candidate survived its duplicate sweep in Waves 1–3. In Wave 4, 4 of 63 candidates were dropped as duplicates of existing prompts or skills (§6). Wave 2's candidate list had already been cut by a pre-sweep, described in §6.
- **Wave 5:** 26 routing regression cases for the new scopes, audited for leakage. 8 target prompts gained plain-language tags (§6).
- **Remaining:** the Wave 3 tiers deferred below are scoped only as far as their boundaries. This document records a repository-wide audit of where the prompt
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
| [`domain-parenting/README.md`](../domain-parenting/README.md) (added 2026-10-02) | 10 planned `caregiver-facing/` folders and the whole `family-support-professional/` tree. Waves 6–7 built all 10 caregiver folders; the `family-support-professional/` tree remains unscheduled |
| [`domain-policy/README.md`](../domain-policy/README.md) (added 2026-10-02) | Five analyses promised "for Wave 4" that Wave 4 never included. Built in Wave 6 |

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
- The psy-ops roadmap made child-safety review a condition for the youth-manipulation prompt. The audit pass did a model-led child-safety review and made it more defensive (see below); a human review is still recommended.
- Both caveats are now visible to readers. The youth prompt, the 32 Wave 3 clinical prompts and `workup_dizziness_vertigo.md` open with a disclaimer and a **Review status: … AI only; not yet reviewed by a licensed clinician / child-safety professional** notice. The healthcare-clinical and psy-ops READMEs carry domain disclaimers. Remove a file's review-status line only after a qualified human has reviewed it.
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

### Wave 5: routing regression cases — shipped (26 cases)

`pae-engine/tests/data/search_routing_regression.v1.json` now has 146 cases.
The new ones are case-121 to case-146, with label source
`coverage_wave_judgment`:

| Class | Added | Covers |
|---|---|---|
| task | 20 | One per new subject home: sales, support, customer success, analytics (3), operations (2), wellness, job search, nonprofit, small business, trades, UX research, songwriting, security operations, after-death admin, criminal defense, travel refunds, PR/FAQ |
| route | 3 | Procurement, endurance training, explaining an experiment result |
| ambig | 1 | `sleep better` (wellness vs psychology) |
| norote | 1 | A pharmacy's opening hours |
| fuzzy | 1 | A misspelled MEDDPICC query |

**Leakage audit (ADR-0037).**
- No query contains all of a target's title tokens or id-tail tokens.
- Median query–target overlap on the task cases is 0.22, against the 0.50 gate.
- Highest Jaccard is 0.33 against a ROUTING_REFERENCE phrase and 0.14 against an earlier case.
- One draft query ("write the press release and customer questions…") had 0.75 overlap with its target's description. It was reworded before any search was run against it.

**First measurement, before any metadata change.**
- The new cases pulled three floors below their limits:
  - R@1 fell to 68.6% (floor 72%).
  - Task R@1 fell to 60.0% (floor 65%).
  - scope@1 fell to 79.1% (floor 80%).
- Only 8 of the 20 new task cases found their target at rank 1.
- The misses had one cause: the Wave 1–4 prompts are tagged in practitioner vocabulary, and people describe the situation instead:

  | Tagged as | People say |
  |---|---|
  | MEDDPICC, ABC/XYZ, reorder point | "the buyer never named who signs off", "how much stock" |
  | bereavement | "my dad passed away" |

**The fix, and its limits.**
- Plain-language tags were added to 13 target prompts, and each was then judged by one rule: keep an addition only if it moved its case to rank 1 (or, for a route case, to the right scope). Eight additions were kept. Five were reverted, because they did not reach rank 1 for cases 124, 131, 132, 138 and 140.
- Keeping all 13 would also have inverted the ranker guard (`test_bm25f_still_beats_the_rejected_baselines`): flat BM25 would have led the shipped BM25F on R@1, 77.9% to 76.7%. The reverted tags did not help BM25F at rank 1, but they did help the flat ranker.
- That result is a signal about the ranker, not about the prompts. It is recorded here instead of being tuned away.
- Queries were not reworded after measurement. No case was dropped. No threshold was refitted.

**Result.**

| | 120 cases (end of Wave 4) | 146 cases (Wave 5) |
|---|---|---|
| R@1 / R@5 | 77.3% / 87.9% | 76.7% / 84.9% |
| scope@1 / kind@1 | 84.7% / 97.6% | 83.6% / 97.7% |
| Shipped BM25F vs flat BM25, R@1 | 77.3% vs 75.8% | 76.7% vs 75.6% |

- New task cases at rank 1: 15 of 20.
- New cases with the right scope at rank 1: 20 of 25.
- None of the original 120 cases changes its top hit.

**Honest failures, kept in the set:**

| Case | Query is about | Search returns |
|---|---|---|
| 124 | A sudden drop in active users | A personal-development goals prompt |
| 131 | A food bank's first foundation grant | A food-and-beverage advertising prompt |
| 132 | A bakery price rise | A customer-side advocacy letter |
| 138 | A prosecutor's plea offer | A negotiation prompt |
| 140 | A launch announcement written before the build | The launch-strategy skill |

Case 145, the no-route pharmacy query, routes `weak` rather than `no_route`.

**Follow-up** (done in the audit pass below).
- Give the Wave 1–4 prompts plain-language situation tags as a deliberate pass across the corpus, not case by case.
- R@5 (84.9%) now sits one point above its 84% floor.

### Audit pass: fixes, the plain-language tag pass, and the deferred backlog (2026-09-24)

An independent audit of Waves 1–5, the follow-up tag pass, one missing prompt,
and the two backlogs Wave 3 deferred (built at the user's request).

**Audit findings fixed.**
- **Safety, HIGH:** the maternal mental-health hotline number was wrong in two
  psychology prompts (now 1-833-852-6262). The two nutrition prompts checked
  the disordered-eating guard but skipped the readiness-gate result, so a
  CLINICIAN-FIRST profile could still get a plan; they now stop on it. In the
  cytopenia workup, a line read as "avoid family-member *donors*" in aplastic
  anemia; it now says to avoid *transfusions* from family members.
- **Clinical structure:** the 32 Wave 3 `interp_*`/`specialty_*` prompts had no
  `related_prompts`, When to Use, Verification or False-Positive Prevention,
  and framed the model as the deciding attending. Each now has all four, a
  decision-support line, and a stop-and-escalate block. About 40 accuracy
  corrections were made (Fleischner risk arms, ESC PE risk classes, ASCO–SSO
  2024 germline testing, DLCO grading, cephalosporin side-chain rule made
  consistent across two prompts, lupus anticoagulant on a DOAC, dialysis vein
  preservation, and others). The older `workup_dizziness_vertigo.md` got
  accuracy fixes only.
- **Legal:** outdated premises in examples (2024–2025 Guidelines amendments,
  Sup. Ct. R. 37, a passed asylum one-year date), a missing mandatory-reporting
  screen in the voluntary-disclosure memo, a spoliation risk in the retention
  example, attorney-only scope guards on the appellate and criminal prompts,
  and four broken README links.
- **Health and psychology:** return after a febrile illness with chest symptoms
  now needs clinician clearance; heat-illness stop signs; sleep restriction
  only with clinician review; the red-flag screen now asks about controlled
  blood pressure; psychology W13 `related_prompts` trimmed to three.
- **Psy-ops youth prompt (child-safety review):** kept, made more defensive: a
  block written to the young person, a mandatory-reporting line for people who
  work with children, a ban on describing image content, official reporting
  channels named without numbers or URLs (a narrow README exception), and no
  identifying details about the child.
- **Duplicates:** no true duplicates. Five overlaps now state the distinction;
  the two older chatbot prompts point to the handoff prompt instead of
  repeating it.
- **Docs:** stale counts in five domain READMEs, `ROUTING_REFERENCE.md`,
  `REPO_MAP.md` and the contributor guide; 22 broken med-ed paths in the
  healthcare README; 13 old-style `decision-making/` references.

**Left as is, by domain convention.** Legal prompts keep 4–5
`related_prompts` (the roadmap requires "at least three") and written-advocacy
keeps 4 (all 41 files). Psy-ops, negotiation and written-advocacy have no
Example section anywhere; psy-ops' README fixes six headings.

**Plain-language tag pass.** 258 Wave 1–4 prompts got 634 situation tags,
written from each prompt's own content by reviewers who did not see the
regression queries. The 8 prompts already retagged in Wave 5 were skipped.
- **First measurement, all tags:** R@1 fell to 75.6% and tied flat BM25. Two
  new cases lost rank 1 because more tags diluted targets that Wave 5 had
  already tagged. One original case (004) changed its top hit to the wrong
  scope. Its two top hits were 0.012 apart, so total tag volume flipped them,
  not any one tag.
- **Kept set:** skip the 8 Wave 5 targets; one tag each (the most general)
  for legal, psy-ops, negotiation and written-advocacy; 2–4 elsewhere.
- **Result:**

| | Start of audit pass | After tag pass |
|---|---|---|
| R@1 / R@3 / R@5 | 76.7% / 82.6% / 84.9% | 77.9% / 83.7% / 86.0% |
| MRR | 0.803 | 0.815 |
| scope@1 / kind@1 | 83.6% / 97.7% | 84.5% / 97.7% |
| Flat BM25 R@1 (guard) | 75.6% | 75.6% |
| New task cases at rank 1 | 15 of 20 | 16 of 20 (131 fixed) |

- No original case changes its top hit. Case 060 keeps its top hit, but its
  routing status moves from `matched` to `ambiguous`; that case has no
  expected status.
- Cases 124, 132, 138 and 140 remain honest failures. Case 145 still routes
  `weak`. Nothing was reworded, relabelled, dropped or refitted.
- R@5 margin over the 84% floor went from 0.9 to 2.0 points.

**Added.**
- `domain-sales-customer/support/support_agent_interaction_qa_scorecard.md`:
  QA for human support agents. The duplicate sweep found none.
- Legal EXPANSION_ROADMAP Phase 3 (10 discovery and litigation prompts plus
  `domain-legal/field_guide.md`) and Phase 4 (10 specialized prompts).
- `domain-childrens-writing/EXPANSION_ROADMAP.md` items 1–12.

Every duplicate sweep came back clean. All 33 have complete frontmatter,
exactly three `related_prompts`, and the Tier 1 sections.

### Wave 6: kept promises and first absent subjects — shipped (48 prompts, 15 cases, 2026-10-02)

A second audit after Wave 5 found three kinds of weakness this roadmap had not
tracked: promises made in domain READMEs that no wave picked up (parenting,
policy), domain Wave 2 lists that were never built (operations, data-analytics,
health-wellness), and subjects with no prompts that §7 had not deferred. Wave 6
takes the documented promises first, then six absent subjects. Every candidate
went through a `pae search` duplicate sweep; none was dropped.

**Part 0, committed separately:** CI still ran the unit tests of the deleted
`continuity-kit/` and four links pointed at it. The step, the registry allowlist
entry and the live references were removed; ADRs and worked-run records keep
their historical mentions. The §9 audit command path was also corrected.

#### `domain-parenting/caregiver-facing/` (12), prefix `parenting_`, safety-gated

| Folder | Files | Nearest neighbour (distinct from) |
|---|---|---|
| `transitions-events/` | `new_sibling_arrival_prep`, `moving_house_child_transition`, `child_grief_after_death`, `new_school_transition_plan` | `parenting_sibling_spacing_dynamics`, `home_moving_checklist` (logistics), `parenting_hard_topics_age_appropriate_scripts`, `parenting_daycare_transition_plan` |
| `safety-risk/` | `body_safety_consent_lessons`, `home_alone_readiness_check`, `other_homes_safety_questions`, `home_childproofing_by_stage` | `parenting_puberty_prep_conversation_scripts`, `parenting_tween_emerging_independence_negotiation` |
| `health-body-sleep-feeding/` | `picky_eating_mealtime_plan`, `bedtime_resistance_plan_4_12`, `bedwetting_response_plan`, `medical_procedure_preparation` | `parenting_infant_feeding_troubleshooter`, `parenting_teen_eating_disorder_signal_response`, `parenting_sleep_regression_decoder` (0–3) |

Each carries the domain's Safety Block. Picky eating screens for ARFID, feeding
disorder and growth faltering before any home plan; body safety carries a
disclosure card with reporting routes; bedwetting routes to the pediatrician
first. Online grooming was left out: `psyops_youth_online_manipulation_guide`
covers it.

#### `domain-policy/` (5), flat, prefix `policy_`

| File | Nearest neighbour (distinct from) |
|---|---|
| `policy_regulatory_impact_analysis.md` | `legal_regulatory_change_impact_assessment` (a company's compliance view) |
| `policy_program_evaluation_design.md` | `program_program_evaluation_framework` (education), `science_causal_inference_design` |
| `policy_public_comment_letter.md` | `advocacy_regulator_complaint_drafter`, `legal_meet_and_confer_letter` |
| `policy_legislative_bill_analysis.md` | `legal_statutory_interpretation` |
| `policy_cross_jurisdiction_comparison.md` | `legal_jurisdiction_split_analysis` (case law) |

#### Domain Wave 2 lists (13 + 4)

| Domain | Files | Source |
|---|---|---|
| `operations` (5) | `ops_sales_and_operations_planning_cycle`, `ops_freight_mode_selection`, `ops_supplier_corrective_action_8d`, `ops_standard_work_and_kaizen_event`, `ops_facility_layout_flow_analysis` | [`EXPANSION_ROADMAP.md`](../domain-operations/EXPANSION_ROADMAP.md) Wave 2 |
| `data-analytics` (4) | `analytics_spreadsheet_model_audit` (≠ `finance_dcf_model_auditor`), `analytics_request_intake_triage`, `analytics_data_dictionary_writer` (≠ `science_data_dictionary_designer`), `analytics_business_forecast_for_planners` (narrowed to operational volumes; ≠ `finance_rolling_forecast_designer`) | [`EXPANSION_ROADMAP.md`](../domain-data-analytics/EXPANSION_ROADMAP.md) Wave 2 |
| `health-wellness` (4), safety-gated | `fitness_mobility_and_flexibility_routine`, `fitness_return_after_break_plan`, `fitness_active_ageing_plan` (clinician clearance recorded), `nutrition_hydration_and_heat_plan` (STRONG-GUARD; no dosing numbers) | [`EXPANSION_ROADMAP.md`](../domain-health-wellness/EXPANSION_ROADMAP.md) Wave 2 |

#### Absent subjects (18)

| Home | Files | Nearest neighbour (distinct from) |
|---|---|---|
| `domain-operations/quality-safety/` (4, new), `ops_` | `spc_control_chart_review`, `oee_loss_analysis`, `job_hazard_analysis`, `safety_incident_investigation` | `ops_root_cause_a3_report`, `ops_capacity_and_bottleneck_model`, `legal_workplace_investigation_plan_and_report` (misconduct). EHS prompts require a qualified safety professional's review and make no regulatory determination. |
| `domain-specialized-fields/insurance/` (4, new), `insurance_` | `commercial_submission_builder`, `underwriting_risk_assessment`, `claim_file_coverage_review`, `renewal_remarketing_plan` | `finance_business_insurance_coverage_review` (the insured), `advocacy_insurance_claim_denial_appeal` and `negotiation_insurance_claim_settlement` (the claimant). Coverage determinations rest with licensed adjusters and counsel. |
| `domain-AI-ML/` (4) | `genai_mcp_server_design_review`, `genai_mcp_server_threat_model`, `aiagent_computer_use_task_design`, `aiagent_browser_agent_trace_review` | `genai_mcp_tool_interface_design` (one tool), `aiagent_agentic_threat_model`, `browserauto_*` (a person's own automation), `agent_observability_prompt_for_traces` |
| `domain-professional-writing/journalism/` (3, new), `journalism_` | `story_desk_edit`, `source_verification_log`, `investigative_project_plan` | `writing_news_article_inverted_pyramid` (drafting), `legal_defamation_publicity_risk_screen` |
| `domain-professional-writing/translation/` (3, new), `translation_` | `project_brief_and_glossary`, `quality_review_mqm`, `transcreation_brief` | `localization_translation_management_workflow` (software i18n) |

The four AI-ML prompts cite 15 technique codes that no prompt had cited before
(GT, IPC and AG families), where the definitions genuinely apply.

**Dropped as duplicates:** none.

**Routing after Wave 6** (diagnostics harness; `case-147`–`case-161` added):

| | Before (146 cases) | After (161 cases) |
|---|---|---|
| R@1 / R@3 / R@5 | 77.9 / 83.7 / 86.0% | 75.8 / 82.8 / 85.9% |
| scope@1 / scope@3 (router) | 84.5 / 91.8% | 83.2 / 92.8% |

- **No original case lost ground.** Case 058 improved (rank 2 → 1). Case 141's
  top hit is now the freight-mode prompt, still in an acceptable scope. Case 012
  keeps its top hit but routes `ambiguous` instead of `matched`; it has no
  expected status.
- **Case 128 regressed during the build and was fixed.** The 8D prompt outranked
  the reorder-policy prompt on incidental words ("Before" in its title, "stock in
  transit" in its description). Both were reworded; no query or label changed.
- **New cases:** 11 of 15 route to an acceptable scope first, and 7 of the 13
  task cases rank their target first. Honest misses, kept as they are: 147 (new sibling), 148 (home alone),
  152 (8D, rank 3), 153 (OEE, rank 2, wrong scope), 155 (computer-use, rank 4,
  wrong scope); 154 ranks its target 2nd.
- **Leakage disclosure.** The case queries were written before any target was
  indexed, but the draft list sat beside the authoring brief where the
  authoring agents could read it. Two targets picked up tags echoing case 161
  and case 154 (`kid-only-eats-five-foods`, `dinner-battles-every-night`,
  `package-for-underwriters`). Those tags were replaced with independent wording
  before the cases were first measured. A tag-overlap scan of all 48 prompts
  against all 15 queries found no other echo beyond ordinary domain vocabulary.

**Left for later:** the misses above (147, 148, 152, 153, 155); `REPO_MAP.md`
counts for untouched domains were not re-audited.

### Wave 7: remaining documented promises — shipped (46 prompts, 16 cases, 2026-10-03)

Every candidate went through a `pae search` duplicate sweep. Where an existing
prompt already did the named job, the item was re-angled to the real gap and the
change recorded below; one was dropped.

#### `domain-parenting/caregiver-facing/` (23), prefix `parenting_`, safety-gated

All seven remaining planned caregiver folders now exist, each with a README.

| Folder | Files | Nearest neighbour (distinct from) |
|---|---|---|
| `coparenting-family-structure/` (4) | `kinship_care_first_months`, `foster_placement_first_weeks`, `solo_parent_load_and_support`, `lgbtq_parented_family_conversations` | `legal_third_party_custody_visitation_analysis`, `parenting_coparenting_with_unsafe_or_absent_parent` |
| `tech-digital/` (3) | `family_media_plan_all_ages`, `ai_chatbot_companion_family_rules`, `gaming_conflict_and_spending_reset` | `parenting_first_phone_decision_framework` and `parenting_video_game_agreement_designer` (ages 9–12), `psyops_youth_online_manipulation_guide` |
| `identity-culture/` (3) | `race_racism_conversations_by_age`, `multilingual_heritage_language_plan`, `interfaith_household_parenting_plan` (logistics only; §7 still defers comparative religion) | `parenting_hard_topics_age_appropriate_scripts` |
| `parent-capacity/` (3) | `parent_overload_load_redesign`, `fourth_trimester_support_plan`, `couple_strain_under_parenting_load` (private abuse screen first) | `clientself_caregiver_burnout_plan`, `parenting_postpartum_parent_capacity_check`, `psychology_gottman_intervention_planner` |
| `academics-skills/` (3) | `homework_battles_plan_5_8`, `struggling_reader_home_support`, `learning_concern_school_meeting` | `parenting_homework_autonomy_handoff_9_12`, `teaching_dyslexia_structured_literacy_plan` (teacher-facing), `advocacy_school_written_request` |
| `mental-health-behavior/` (4) | `school_refusal_young_child_5_8`, `young_child_lying_response_3_8`, `aggression_toward_family_safety_plan`, `child_suicide_talk_response_6_12` | the 9–12 and 13–18 versions (`parenting_school_refusal_decoder_tween`, `parenting_lying_pattern_function_analysis`, `parenting_teen_self_harm_signal_response`) |
| `neurodivergence/` (3) | `tics_tourette_home_school_plan`, `twice_exceptional_child_support`, `dcd_dyspraxia_home_support` | `parenting_sensory_at_home_toolkit`, `parenting_school_accommodation_conversation_prep` |

**Re-angled to avoid duplicates:** first-phone readiness became a whole-household
media plan; gaming time became a reset after a spending incident; postpartum became
a plan made before the birth; dyslexia-at-home merged into the struggling-reader
prompt and DCD/dyspraxia took its slot (nothing in the repo covered it); school
refusal, lying and suicide talk were narrowed to the younger ages that had no prompt.

#### `domain-policy/public-administration/` (6, new), prefix `policy_`

`local_budget_shortfall_options`, `grant_post_award_compliance` (≠
`nonprofit_foundation_grant_proposal`, pre-award), `agency_rulemaking_plan` (the
agency side; ≠ Wave 6 `policy_public_comment_letter`), `constituent_casework_system`,
`agency_performance_measures`, `public_meeting_staff_brief`.

#### Other domains (17)

| Home | Files | Nearest neighbour (distinct from) |
|---|---|---|
| `domain-personal-development/prompts/` (4) | `emotional-fitness/emotionalfitness_money_beliefs_and_avoidance`, `stakeholder/stakeholder_peer_conflict_navigation`, `stakeholder/stakeholder_reorg_navigation`, `identity/identity_meaning_sources_and_legacy_map` | `finance_net_worth_cashflow_diagnostic` (the numbers), `stakeholder_visibility_and_credit`, `lifetransition_navigating_new_role`, `identity_purpose_reignition` |
| `domain-negotiation/` (2) | `craft/negotiation_analytics_scorecard`, `channels/negotiation_ai_agent_mediated` | `negotiation_post_negotiation_debrief` (one deal), `negotiation_authority_mandate_limits`. The roadmap's human-broker half stays open. |
| `domain-education-teaching/` (5) | new `program/student-success/`: `program_first_year_advising_touchpoint_model`, `program_at_risk_student_outreach_plan`, `program_retention_persistence_data_review`; `instructor/reporting-communication/`: `teaching_parent_teacher_conference_prep`, `teaching_multilingual_family_outreach` | `program_early_warning_system_designer`, `teaching_parent_communication_composer` |
| `domain-operations/quality-safety/` (2) | `ops_preventive_maintenance_program`, `ops_repeat_failure_reliability_analysis` | `ops_oee_loss_analysis`, `risk_fmea_analysis` |
| `domain-specialized-fields/professional-services/` (4, new), prefix `proserv_` | `utilization_realization_review`, `fixed_fee_overrun_diagnosis`, `engagement_staffing_plan`, `independence_conflict_check` | `services_capacity_and_utilization_planner` (solo practice), `finance_engagement_profitability_postcalc` (after close), `legal_conflicts_check_memo` (law firms) |

**Dropped as duplicates (1):** the first-year early-alert system →
`program/evaluation-analytics/program_early_warning_system_designer.md`. A
first-year advising model took its slot.

**Routing after Wave 7** (`case-162`–`case-177` added):

| | Before (161 cases) | After (177 cases) |
|---|---|---|
| R@1 / R@3 / R@5 | 75.8 / 82.8 / 85.9% | 75.4 / 82.5 / 86.8% |
| scope@1 / scope@3 (router) | 83.2 / 92.8% | 84.4 / 92.9% |

- **Earlier cases.** Case 131 (food bank grant) regressed during the build: the
  foster prompt matched on "family", "first", "time" and "food". Its title and
  description were reworded ("Birth-Parent Visits", "meals") and the case is back
  to its pre-Wave-7 result. Case 153 (OEE) slipped from rank 2 to 3, still in the
  top 3, behind the new repeat-failure prompt, which legitimately matches "machine"
  and "break down"; left as is. Cases 148 and 155 improved.
- **New cases:** 14 of 16 route to an acceptable scope first, and 11 of the 15
  task cases rank their target first. Honest misses: 162 (kinship, rank 5), 164
  (first phone, rank 4, wrong scope), 174 (retention, rank 4), 175 (preventive
  maintenance, not in the top 5, wrong scope).
- **Leakage controls.** The case queries were drafted before authoring and kept
  out of the authoring agents' reach; they were written to disk only after every
  target file was final. Four targets carry tags overlapping a query's wording
  (`feel-guilty-spending-money`, `coworker-takes-credit-for-my-work`,
  `allowable-costs`, `set-limits-for-my-ai-assistant`); file timestamps show the
  tags predate the query file, so this is shared everyday phrasing.

**Left for later:** the misses above; the negotiation roadmap's human-broker
item; `domain-parenting/family-support-professional/` (8 planned subfolders, not
yet scheduled in any wave).

### Wave 8: second set of absent subjects — shipped (36 prompts, 13 cases, 2026-10-03)

| Home | Files | Nearest neighbour (distinct from) |
|---|---|---|
| `domain-software-engineering/analysis/security/` (4), `security_` | `detection_engineering_review`, `threat_hunting_plan`, `vulnerability_management_program`, `soc_alert_triage_runbook` (engineering-run on-call) | `risk_security_alert_triage_runbook` (non-engineers), `aiagent_secops_autonomous_defense`, `security_dependency_vulnerability_analysis` (one codebase) |
| `domain-software-engineering/data-engineering/` (5, new), `dataeng_` | `pipeline_design_review`, `dimensional_model_review`, `data_quality_test_strategy`, `incremental_load_backfill_plan`, `data_downtime_postmortem` | `skills/data-engineering/*` (tool how-to), `commands/architecture/data_pipeline`, `mldata_data_contract_design`, `analytics_sql_query_correctness_review` |
| `domain-software-engineering/cloud/` (2), `cloud_` | `bill_spike_investigation`, `commitment_rightsizing_plan` | `cloud_finops_cost_allocation` (the program), `cloud_cost_optimization` (broad sweep) |
| `domain-frontend-development/design-direction/` (3) | `frontend_design_system_audit`, `frontend_design_token_architecture`, `frontend_design_system_component_governance` | `frontend_styling_tailwind_design_system`, `frontend_styling_css_architecture` (one technology) |
| `domain-frontend-development/accessibility/` (2) | `frontend_accessibility_documents_slides`, `frontend_accessibility_program_governance` | `frontend_accessibility_wcag_audit`, the accessibility skills and agent |
| `domain-science/ml-for-science/` (3, new) | `science_ml_project_scoping`, `science_ml_validation_split_design` (narrowed: sample dependence, external-validation tiers, grouped uncertainty), `science_ml_interpretation_for_claims` | `science_ml_for_science_benchmark_design`, `mlframe_is_this_ml_problem`, `rai_interpretability_analysis` |
| `domain-productivity/home-life/` (7), `home_` | `dementia_caregiver_communication`, `dementia_home_safety_plan`, `parent_cannot_live_alone_talk`, `diy_repair_triage` (hard stops for gas, panel, structural, asbestos/lead), `small_repair_walkthrough`, `learn_to_cook_progression`, `pantry_first_weeknight_cooking` | `psychology_geriatric_depression_vs_dementia`, `personal_caring_for_aging_parent` (chooses the arrangement), `home_seasonal_maintenance_calendar`, `home_meal_plan_week` |
| `domain-written-advocacy/institutions-and-records/` (1) | `advocacy_special_education_disagreement` (IEP or eligibility disagreement, independent evaluation request) | `advocacy_school_written_request` (first requests), `parenting_learning_concern_school_meeting` |
| `domain-personal-development/prompts/relationships/` (2) | `relationships_dating_after_divorce`, `relationships_early_dating_safety_plan` | `lifetransition_post_breakup_rebuild`, `parenting_divorce_new_partner_introduction_timing`, `psyops_coercive_control_pattern_recognition` |
| `domain-biblical-studies/academic-writing/` (5, new) and `ministry-contexts/` (2) | exegesis paper scaffold, thesis workshop, literature review plan, annotated bibliography builder, peer-review self-check (all STRONG-GUARD: no invented sources, pages, readings or quotations); age-graded story retelling; special-needs inclusive teaching | `research_thesis_dissertation_structure`, `research_literature_review_plan`, `biblical_passage_exegesis_workflow`, `biblical_ministry_kids_bible_lesson_builder` |

**Decision recorded:** clinical-trial design stays in `domain-science/` (the
SPIRIT/CONSORT protocol outliner and the randomization, power and analysis-plan
prompts already live there); see that domain's EXPANSION_ROADMAP, Open Question 2.

**Dropped as duplicates:** none. Re-angled: the data-quality prompt became a test
strategy (contracts are covered in AI-ML), the commitment prompt was narrowed to
post-rightsizing purchases, the ML validation prompt was narrowed to what the
existing benchmark-design prompt lacks, and the special-education letter covers
disagreement after a decision rather than a first request.

**Routing after Wave 8** (`case-178`–`case-190` added, all task cases):

| | Before (177 cases) | After (190 cases) |
|---|---|---|
| R@1 / R@3 / R@5 | 75.4 / 82.5 / 86.8% | 73.2 / 82.7 / 85.8% |
| scope@1 / scope@3 / kind@1 (router) | 84.4 / 92.9 / 100% | 83.8 / 93.5 / 97.7% |

- **Earlier cases.**
  - Case 162 (kinship) fell out of the top 5 during the build. The new dating
    prompt matched on "kids" and "after". "Kids" was reworded to "children" in its
    title and description, and the case is back at rank 5.
  - Case 161 (picky eating, route) now routes to `productivity` first. The
    pantry-cooking prompt matches "dinner" and "food", which are its core
    vocabulary, so it was left as is. This is a real regression, and it is recorded.
  - Cases 004 (rank 5 → 6), 032 (status only) and 058 (rank 1 → 2, its pre-Wave-6
    rank; kind@1 returns to 97.7%) moved without any Wave 8 prompt overtaking them.
    Corpus growth shifted term weights.
- **New cases:** 11 of 13 reach an acceptable scope first, and 8 rank their target
  first. Misses: 178 (detections, rank 3), 179 (vulnerability backlog, top hit is a
  TON smart-contract scanner skill, wrong scope), 185 (dripping faucet, rank 2,
  wrong scope), 186 (learn to cook, rank 2), 189 (protein-stability ML, not in the
  top 5).
- **Leakage controls:** the same as Wave 7. Three targets carry tags overlapping a
  query's wording (`make-pdf-accessible`, `screen-reader-cant-read-our-report`,
  `write-bible-paper-for-class`, `special-education`). Their file timestamps predate
  the query file.

**Still open from the Wave 8 plan:** energy-sector and music-production work
(an undecided §7 proposal), and biblical-studies Phase 3C's pastoral-counseling and
Jewish–Christian dialogue items (both shipped in Wave 12).

### Wave 9: depth in thin subfolders — shipped (39 prompts, 15 cases, 2026-10-03)

Each new prompt had to do a different job from the one or two already in its
subfolder. Where a suggested topic was already covered, the agent picked the real
gap instead; nothing was dropped.

| Domain | Subfolder: added | Re-angled because already covered |
|---|---|---|
| `frontend-development` (13) | `animation/` motion system design, motion-safety audit; `qwik/` City loaders/actions, reactive state and tasks; `remix/` React Router v7 migration, sessions/auth/caching; `solidjs/` SolidStart data/SSR, control flow and components; `astro/` rendering modes and server islands; `forms/` multi-step wizard state; `performance/` field Core Web Vitals regression; `testing/` API mocking strategy; `typescript/` API contract typing | Remix revalidation and error boundaries (`frontend_remix_data_loading`), Solid reactivity pitfalls, Astro hydration (`frontend_astro_islands_architecture`), visual regression (`testing_visual_regression`), strict-mode migration (`frontend_typescript_type_safety_audit`) |
| `game-development` (9) | `ai/` stealth perception fairness, squad tactics and encounter director; `audio/` adaptive music, gameplay-readability mix; `narrative/` branching state management, environmental storytelling; `economy/` currency sink/faucet audit; `graphics/` art-to-technical budget; `level-design/` telemetry flow analysis | — |
| `creative-writing` (6) | `poetry/` meter, scansion and fixed forms; chapbook and collection ordering; `creative-nonfiction/` personal-essay reflection and the turn; ethics of writing about real people; `publishing-career/` self- vs traditional publishing; `songwriting/` co-writing sessions and splits | melody and prosody (`writing_song_structure_lyric_revision`) |
| Single-prompt folders (11) | `product-management/templates/` PRD one-pager, PRD change-request record; `hr-management/onboarding/` preboarding and first week, onboarding program audit; `finance/options/` covered call and cash-secured put; `prompt-engineering/prompt-optimization/` eval-driven iteration, failure-cluster prioritiser; `utilities/` template placeholder audit; `operations/project-delivery/` schedule recovery, closeout and lessons learned; `health-wellness/sleep-recovery/` shift-work and jet-lag timing (readiness gate; no sleep-aid advice) | the first-90-days plan (`hr_onboarding_thirty_sixty_ninety`), the decision log (`decisiondoc_log_entry`), the regression-diff reviewer (`improve_prompt_diff_explainer`) |

**Dropped as duplicates:** none.

**Routing after Wave 9** (`case-191`–`case-205` added). Five cases target
*pre-existing* prompts in the deepened subfolders, to check that the new siblings
did not take their queries. All five still rank their target first.

| | Before (190 cases) | After (205 cases) |
|---|---|---|
| R@1 / R@3 / R@5 | 73.2 / 82.7 / 85.8% | 75.7 / 84.3 / 87.1% |
| scope@1 / scope@3 / kind@1 (router) | 83.8 / 93.5 / 97.7% | 84.6 / 93.5 / 100% |

- **Earlier cases.** Cases 058 (rank 2 → 1) and 164 (rank 4 → 3) improved.
  Case 185 (dripping faucet) slipped from rank 2 to 3: the new economy prompt is a
  "sink/faucet" audit, which is that subject's standard term, so it was left as
  is. Case 093 ("onboarding", ambiguous) swapped between two HR onboarding prompts
  with no change in scope or status.
- **New cases:** 14 of 15 reach an acceptable scope first, and 12 of the 13 task
  cases rank their target first. Misses: 200 (self- vs traditional publishing,
  rank 4) and 203 (waking at 3am, route: the top hit is a learning prompt; it was
  wrong before Wave 9 too).
- **Leakage controls:** the same as Waves 7–8. Two targets carry tags
  overlapping a query's wording (the audio mix and branching-state prompts). Every
  Wave 9 file was saved before the query file was written.

### Wave 10: agentic-resource and technique hygiene — shipped (2026-10-04)

**Technique remap.** The 13 undefined codes (DC-01, PR-01/02/03, CR-01/02,
IT-01/02, AN-01, SC-01/03, FP-01, WF-01; 133 citations) were remapped file by
file to existing catalog codes, chosen from what each prompt actually does. No
new codes were defined. The main targets were:
- CR-01/02 → RT-01 (Chain-of-Thought), 18 healthcare files. The healthcare roadmap line that defined CR-01 as CoT was corrected.
- DC-01 (42) → about 20 different codes, for example AG-11, QA-05, NE-05, DT-01, CM-01.
- PR-01 → RP-01, QA-11, DS-29, QA-10.
- PR-02 → QA-01, RT-01, QA-15.
- PR-03 → ED-06, MP-04 and others.
- IT-01/02 → MP-03. SC-01 → RP-01. SC-03 and WF-01 → ST-02. AN-01 → RT-02. FP-01 → QA-12.

The 46 "ID (Name)" entries in the iOS and Android prompts are now bare IDs. Where
the name showed the author meant a different technique, the ID was switched: "ST-01
(Structured Task Decomposition)" → DT-01, "RT-02 (Checklist Verification)" → QA-10,
"DS-02 (Domain-Specific Terminology)" → CM-01, "RT-05 (Constraint Specification)"
→ CM-02, "QA-01 (Quality Assurance Gates)" → QA-08.

110 files were touched. The two `ai-governance-audit-kit/referenced-prompts/`
copies of edited prompts were re-synced with `check_vendored_copies.py --fix`.

**Validator.** `scripts/validate_technique_catalog.py` now checks every
`techniques:` entry in `PROMPT_INDEX.json`, and it runs in CI:
- An unknown or malformed ID is a hard error. The ID pattern is generic, so an uncatalogued prefix such as `DC-` is caught.
- A deprecated (merged) ID is a warning that names its merge target. OC-01 (141 citations) and QA-03 (1) remain as valid aliases.
- A parenthesised name that differs from the catalog's is a warning.
- `--uncited` lists the active IDs no prompt cites, by family: 100 now, informational only.
- Eight unit tests were added to `scripts/pae_registry/tests/test_metadata_and_techniques.py`.

**One-skill categories folded.** These moves preserve identity:
- `skills/ai-native-rollouts` → `skills/non-coding/business/`
- `skills/review-prompt` → `skills/llm-application-dev/`
- `skills/vibe-coding-rescue` → `skills/developer-tools/`

Each move is recorded in `meta/REORG_MAP.tsv`. Each UID is kept, and the retired
public ID is in `meta/registry/aliases.tsv`.

**New agentic resources (19).**

| Kind | Added | Re-angled or dropped |
|---|---|---|
| Skills (7) | `accessibility/` component-accessibility-contracts, accessibility-regression-gate; `game-development/` game-feel-juice-pass, playtest-telemetry-capture (with a tested log validator); `devops/` executable-runbook-authoring, infrastructure-drift-detection; `observability/` slo-burn-rate-alerting (its rules pass `promtool check rules` and `promtool test rules`) | Five re-angled away from an existing prompt, skill or command |
| Agents (4) | `deployment/` release-readiness-gatekeeper, progressive-delivery-controller (advisory; each change needs human confirmation); `orchestration/` task-decomposition-coordinator, result-reconciler | — |
| Commands (4) | `data-analysis/` dataset_profile, metric_sanity_check; `documentation/` docs_drift_check, changelog_reconcile | changelog-from-commits re-angled (the `changelog-automation` skill exists) |
| Personas (4) | `product/` product-operations lead, API/platform product manager; `specialized/` geospatial analyst, open-source maintainer | pricing strategist, accessibility reviewer and data-privacy reviewer dropped as duplicates |

**Routing:** no case changed scope. Case 058 ("persona that evaluates and compares
tools") went from rank 1 back to 2. It is a persona-versus-prompt near-tie that has
flipped back and forth as the corpus grows, so kind@1 reads 97.7%. Case 164 slipped
from rank 3 to 4. Scope@1 stays at 84.6% over 205 cases.

**Left for later:**
- Several Android prompts still list more than 5 techniques, and their body lists mislabel some valid codes (done: see the Wave 10 follow-up below).
- The `slo-implementation` skill's example alerts use 30-day burn-rate thresholds on a 28-day SLO (done: see CHANGELOG "Fixed").
- Most `personas/README.md` tree filenames are out of date.

### Wave 10 follow-up: technique hygiene leftovers — shipped (2026-10-05)

`scripts/validate_technique_catalog.py` now prints 0 warnings. No technique
codes were defined or deprecated.

**Deprecated codes.** OC-01 → ST-03 in 141 prompts and QA-03 → QA-01 in 1, in
frontmatter and in the same files' body technique lists, with catalog names.
Two files already listed the target, so the old code was deleted. In
`architecture_state_machine_design.md` the OC-01 entry described a verification
checklist, so it now cites QA-01. Notes that document the merge itself (the
catalog, comparison tables, technique analyses) were left as they were. The
validator section above records the pre-follow-up citation counts.

**Over-long lists.** 1,260 prompts listed more than 5 techniques. This pass
hand-read 65 of them and cut each to the 3–5 codes its body applies:
- every `mobile/android/improvement/` prompt over 5, `ios_privacy_compliance`,
  and the ABG, ECG and pharmacokinetics interpretation prompts;
- every other prompt with 8 or more codes (deep-analysis deepthink twins,
  family law, embedded, vibe-coding rescue, idea-to-product and others).

The 4 `domain-idea-to-product/` deepthink copies were re-synced with
`check_vendored_copies.py --fix`. Body technique lists now match frontmatter and
use catalog names. IDs were switched only where a body label showed a different
technique was meant, for example QA-01 "Constraint Specification" → CM-02, QA-05
"Abort Triggers" → QA-08, DS-03 "Multi-Criteria Ranking" → DS-06, and RT-01
"Comparative Analysis" folded into the RT-03 entry already listed. Family-law
prompts with a False-Positive Prevention section keep QA-12 in both `custody/`
and `divorce/`. CM-04 lost its only citation, a mislabel for "Forbidden
Patterns Explicit", so `--uncited` now reads 101.

**Mislabel.** Four `domain-biblical-studies/original-languages/` prompts cited
NE-14 (Multi-Audience Documentation Targeting) as "Fabrication Prevention".
They route every datum to a named edition or reference work, so they now cite
QA-05 (Citation Requirements). QA-12 (False Positives Identification) was
considered and rejected. Their ST-01 entries were also renamed to the catalog
name.

**Routing:** unchanged. Scope@1 84.6%, scope@3 93.5%, kind@1 97.7%, R@1 75.0%
and MRR 0.800 over 205 cases, the same before and after.

**Left for later:**
- 48 image-generation prompts (advertising, board decks, coloring books, the
  model guides) list 8–13 codes. They are exempt by design, because the 8 core
  SV techniques are the domain's required method (CLAUDE.md,
  `IMAGE_GENERATION_GUIDE.md`).
- 1,143 prompts list 6 or 7 codes (969 at 6, 174 at 7). They are spread
  across most domains and are worth a domain-by-domain pass.
- The audit's 5 soft "cited as" mislabels are shorthand cross-references
  inside `MASTER_TECHNIQUE_INDEX.md` itself, not prompt citations.
- Five vibe-coding-rescue and repo-audit prompts carry a "Dual-Failure
  Prevention (QA-20)" section without listing QA-20.

### Routing follow-up: the open misses from Waves 5–9 (2026-10-05)

A pass over the 22 open misses recorded in the "Routing after Wave N" notes
above, under the tuning rules: no query, label, threshold or floor changed, no
case added, no tag added because a query uses the word. Every candidate fix was
checked case by case against a full before snapshot of all 205 cases.

**Shipped: one engine change.** `pae_engine._lexical.Document` no longer
indexes a record's native `name` when it normalizes to the same terms as its
title. Only agentic resources carry a `name`, and for 703 of 711 of them it is
the title verbatim. Skills, agents, commands and personas therefore matched
their title words in one more field than a prompt with the same title, which
is a kind bias from metadata shape, not relevance. The 8 commands whose name
says something the title does not keep it. Three unit tests pin it
(`tests/test_lexical.py`); two of them fail without the change.

| | Before | After |
|---|---|---|
| R@1 / R@3 / R@5 / MRR | 75.0 / 83.6 / 87.1% / 0.800 | 75.0 / 83.6 / 87.1% / 0.800 |
| scope@1 / scope@3 / kind@1 (router) | 84.6 / 93.5 / 97.7% | 85.2 / 93.5 / 97.7% |
| ambiguous-class scope@1 | 68.8% | 75.0% |
| statuses (matched / ambiguous / weak / no_route) | 81 / 81 / 42 / 1 | 81 / 81 / 42 / 1 |
| Flat BM25 guard, R@1 and scope@1 | 75.0% and 82.8% | 75.0% and 83.4% (shipped still ≥ on both) |

- **Per case:** exactly one of 205 cases changes. Case 092 (`pricing`,
  ambiguous) now ranks the business-strategy pricing prompt above the marketing
  skill of the same name, so its routed scope moves from
  `agentic-resources/marketing` to `business-strategy`, an acceptable scope.
  Its status stays `ambiguous`. No case changed rank, top hit, scope or status
  otherwise.
- **§2 probes:** one moves, at rank 3 only. `restaurant menu pricing` shows the
  same business-strategy pricing prompt instead of the marketing skill.
- It fixes none of the 22 open misses.

**Tried and rejected** (each measured per case, then reverted):

| Change | Fixed | Regressed | Why rejected |
|---|---|---|---|
| Strip English clitics (`'s`, `'re`, `'ve`, `'t`…) before splitting | none | 162 drops out of the top 10 | The kinship target's only description match was a possessive `s` |
| Add pronouns (`they`, `them`, `their`, `myself`…) to the stopwords | none; 175 enters at rank 7, 162 moves 5 → 4 | 148 loses its parenting scope; 185 drops out of the top 10 | `myself` is evidence ("Can I Fix This Myself") |
| Index `path` only for terms not already in `pid`, or drop `path` | none; 178 3 → 2, 200 4 → 3, 189 enters at 9, 138 routes to `legal` | 030 and 188 lose rank 1 and their scope; 164 drops out of the top 10 | Mixed |
| Fold sibilant plurals (`-sses`, `-xes`, `-shes`, `-zzes`; optionally `-ches`) | none | none | Moves no case, so it does not meet the "improves the metrics" bar; `-ches` would also split `cache`/`caches` |
| Three plain-language tags on the case 164 target, written from its own "When to use" (peer pressure, the phone contract) and avoiding the query's words | none (still rank 4) | none | No effect; reverted, as Wave 5 did with tags that did not help |

**Per-case classification.** None is fixed. "Honest miss" means the right
resource exists and is described in its own words; the query describes the
situation in other words, and closing the distance would mean echoing the query.

| Case | Now | Class | Reason |
|---|---|---|---|
| 124 | not in top 10 | Honest miss | The target matches no query term. It says "metric", "sudden-drop"; the query names one metric ("weekly active users") and says "fell". The body uses "fell", but by the score arithmetic one tag would add about 2.3 against the 4.9 needed for the top 5, and the choice would be query-driven |
| 132 | not in top 10 | Honest miss | "Charge" is the winning charge-dispute prompt's real subject. The target says "price increase" and "lose customers", not "charge more" or "losing". Its "worried-about-regulars" tag already matches |
| 138 | not in top 10 | Honest miss | The query avoids "plea". The target's body says "prosecutor" once, so adding it to metadata would come from the query. Winners match "deal", "table", "walk", "client", their own vocabulary |
| 140 | not in top 10 | Honest miss | The query describes a PR/FAQ without naming it. The launch-strategy skill is a fair neighbour for "launch announcement". Tags were tried and reverted in Wave 5 |
| 145 | `weak` | Honest miss (structural) | `no_route` fires only when nothing matches at all; "pharmacy" legitimately matches the pharmacy-education folder. `weak` already means "no route selected", and the coverage threshold is not refitted |
| 147 | not in top 10 | Honest miss | The target is tagged `having-another-baby`, `toddler-jealous-of-baby`; the query says "expecting a second baby", "three year old". Only "baby" overlaps |
| 148 | not in top 10 | Honest miss | The child-suicide-talk prompt's 76-word description legitimately contains "stay", "after", "school", "want". The target's tags match four terms. Pronoun stopwords were tried and hurt this case |
| 152 | rank 3 | Honest miss | Two debugging prompts own "root cause … fix". The target says "supplier", never "vendor" |
| 153 | rank 3 | Honest miss | "Machine output" is the dual-output prompt's subject. The target says "OEE", "losses", "why-is-output-low" |
| 155 | rank 2 | Honest miss | The agent progress-report prompt legitimately matches "agent" and "report" in five fields. Gap 0.59 |
| 161 | `productivity` first | Honest miss (Wave 8 regression, kept) | "Dinner", "eat", "food" are the pantry prompt's core vocabulary. The target says "mealtime", "eater", "child". Wave 6 removed echo tags from this target, so re-adding them is ruled out |
| 162 | rank 5 | Honest miss | The target says "aunt", "parent-in-jail-or-rehab". The moving-house and two-homes prompts legitimately match "kids", "moving", "help" |
| 164 | rank 4 | Honest miss | Content-grounded tags tried; no effect. The "explain like I'm nine" and making-friends prompts match "like" and "friend" in their titles |
| 174 | rank 4 | Honest miss | The two adult-returner prompts carry "first-semester", their real subject (a returning student's first term). One of four acceptable targets ranks 4th |
| 175 | not in top 10 | Honest miss | Every query word is common. The fitness return-after-break prompt owns "after", "break", "week" in its title, slug and description; the targets match "maintenance" widely but "break" and "down" only in tags |
| 178 | rank 3 | Honest miss | The SOC alert-triage runbook is a close sibling and legitimately owns "SOC", "alert". Gap 2.3 |
| 179 | rank 8 | Honest miss | Six `<chain>-vulnerability-scanner` skills carry both rare query words in title, slug and path, which is their real subject. The target already has `scanner-backlog`. Path de-duplication would not fix it and regressed other cases |
| 185 | rank 3 | Honest miss | "Faucet" is the economy prompt's standard term (Wave 9) and "drips" is the nursing-drips card's. The targets say "dripping" and "fix-it-myself" |
| 186 | rank 2 | Honest miss | The pantry prompt is a defensible answer for "simple dinners … on weeknights". The target owns "learn" and "cook" |
| 189 | not in top 10 | Honest miss | No resource in the index says "neural" in its metadata; the query also matches the lab-protocol and ML-data prompts on "lab", "assay", "train", "data" |
| 200 | rank 4 | Honest miss | Three novel-craft prompts own "novel". The target is 0.34 behind the top hit |
| 203 | `education-teaching` first | **Missing content** | No healthy-adult prompt covers waking in the night and not getting back to sleep. The sleep audit covers routine and environment, the shift-work prompt covers timing, and the CBT-I calculator is clinical self-use. Resource that should exist: `domain-health-wellness/sleep-recovery/sleep_night_waking_back_to_sleep_plan.md` (readiness gate first, a get-up rule and clock-hiding, caffeine and alcohol timing, and a route to a clinician or CBT-I when waking persists for weeks) |

**Also fixed in passing:** `meta/registry/registry.jsonl` was stale at the
start of this pass: two agentic-resources index pages had been edited without
regenerating it, so `generate_registry.py --check` failed on a clean checkout.
It was regenerated; only those two content hashes changed.

**Left for later:** the night-waking prompt above. Most remaining misses are
vocabulary distance between situation language and practitioner language
(`fell` vs `drop`, `eats` vs `eater`, `vendor` vs `supplier`). The rules here
leave that to a synonym or stemming decision at the engine level, which
ADR-0021 rejected and which would need its own measurement.

### Wave 11: family-support professional cluster — shipped (22 prompts, 9 cases, 2026-10-05)

This wave builds the last documented parenting promise, the eight planned
`domain-parenting/family-support-professional/` subfolders that Wave 7 left
unscheduled. They are for parent educators, coaches, family support workers, home
visitors, caseworkers and family-time supervisors, not for caregivers. Every
candidate went through a `pae search` and `PROMPT_INDEX.json` duplicate sweep;
none was dropped.

#### `domain-parenting/family-support-professional/` (22), prefix `parenting_`, safety-gated

Each folder has a README, and the cluster has its own README stating the shared
safeguards.

| Folder | Files | Nearest neighbour (distinct from) |
|---|---|---|
| `intake-assessment/` (3) | `family_strengths_needs_intake`, `developmental_screen_results_talk`, `program_referral_triage_waitlist` | `psychology_pediatric_intake_with_caregiver` (clinical intake), `allied_health_sdoh_screening_response`, `parenting_developmental_red_flags_0_3` (caregiver) |
| `coaching-education/` (3) | `parent_coaching_session_plan`, `mandated_parent_engagement`, `curriculum_fidelity_adaptation` | `psychology_behavioral_parent_training_module` (clinician PCIT/BPT), `psychology_mi_decisional_balance_facilitator` |
| `plans-documentation/` (3) | `family_goal_plan_builder`, `family_contact_note_writer`, `case_closure_transition_summary` | `psychology_dap_progress_note`, `psychology_collateral_contact_note`, `psychology_termination_summary` (clinical records) |
| `group-facilitation/` (2) | `parent_group_session_design`, `parent_group_hard_moments` | `psychology_group_therapy_curriculum_builder`, `curric_small_group_facilitation_guide` (medical education), `biblical_groupleader_facilitation_dynamics` |
| `referral-resourcing/` (2) | `clinician_referral_by_nonclinician`, `referral_follow_through_barriers` | `psychology_referral_letter_generator` and `psychology_warm_handoff_narrative` (clinician to clinician), `allied_health_sdoh_screening_response` |
| `home-visit-fieldwork/` (3) | `home_visit_plan_and_interaction`, `home_visitor_worker_safety`, `home_visit_child_safety_concern` | `psychology_mandated_reporter_decision_walkthrough` (a licensed clinician's decision and therapy continuity), `ops_job_hazard_analysis` |
| `foster-kinship-adoption/` (3) | `resource_parent_stability_support`, `family_time_visit_supervision`, `life_story_work_with_child` | `parenting_foster_placement_first_weeks` and `parenting_kinship_care_first_months` (caregiver), `legal_supervised_visitation_and_safety_plan` (order language) |
| `culturally-responsive/` (3) | `interpreter_mediated_family_session`, `cultural_practice_vs_safety_check`, `immigrant_family_support_plan` | `teaching_multilingual_family_outreach` (teacher), `psychology_cultural_formulation_interview_drafter` (DSM CFI), `domain-legal/immigration/` |

Each prompt has a "Safeguarding, Consent, and Scope" block. It describes rather than
diagnoses, and the false-positive table has a "labelling instead of describing" row.
Its mandated-reporting steps are jurisdiction-aware: the threshold, the timeline and
whether a supervisor consult counts all vary, so the prompt says "verify locally".
In most US states the duty is personal, and a consult never delays a report or a
911 call. Each prompt names triggers for escalating to a licensed clinician, with
same-day and emergency routes. It covers consent, the limits of confidentiality
stated before anyone discloses, written releases, minimum-necessary sharing, and
de-identifying client details before they go into an AI tool. One example was
corrected in review: the child-safety prompt's example now confirms the bruised
infant's same-day medical check instead of leaving it to child-protection intake.

**Re-angled to avoid duplicates:** both `referral-resourcing/` prompts moved off
"screen, triage and match to resources", which the healthcare SDOH response
prompt already does. They now cover the parts it lacks: a non-clinician raising a
mental-health concern without diagnosing, and following a referral through to a
real connection when the family declines or stalls.

**Technique citations:** DS-30 (Ecosystem Mapping) had no citations before and is
now cited by the immigrant-family prompt, so `--uncited` reads 100.

**Routing after Wave 11** (`case-206`–`case-214` added):

| | Before (205 cases) | After (214 cases) |
|---|---|---|
| R@1 / R@3 / R@5 / MRR | 75.0 / 83.6 / 87.1% / 0.800 | 72.8 / 81.0 / 84.4% / 0.775 |
| scope@1 / scope@3 / kind@1 (router) | 85.2 / 93.5 / 97.7% | 84.8 / 93.3 / 97.7% |
| statuses (matched / ambiguous / weak / no_route) | 81 / 81 / 42 / 1 | 84 / 82 / 47 / 1 |
| Flat BM25 guard, R@1 and scope@1 | 75.0% and 83.4% | 71.4% and 82.6% (shipped still ≥ on both) |

- **Earlier cases: none regressed.** The 205 cases were compared one by one
  against a worktree of the base commit (`8f2398c`). No case changed its gold
  rank, top hit, search scope, router status or routed scope, so the 205-case
  aggregates are identical. The aggregate drop above comes entirely from the
  new cases. Three cases now show a new prompt below their unchanged top hit:
  - case 143 (A/B result for the boss): the developmental-screen prompt is
    2nd, on "explain" and "result". It trails by 1.95, and "results" is that
    prompt's real subject, so it was left as is.
  - case 163 (first foster placement): the carer-stability prompt is 2nd,
    5.1 behind. It is a legitimate sibling.
  - case 188 (dating after divorce): the developmental-screen prompt is 5th.

  No rewording was needed.
- **New cases:** 7 of 9 route to `parenting` first. Two of the 7 task cases rank
  their target first: 208 (clinician referral) and 209 (family-time
  supervision). Route case 210 (cultural practice) moved from
  `personal-development` to `parenting`. Honest misses, kept as they are:
  - 206 (worker safety, rank 14): the query's words are situation words
    ("boyfriend", "violent record", "protect myself") where the target says
    "field safety", "exits", "check-in".
  - 207 (child-safety concern, rank 19): "couch", "bruises", "toddler" also
    match the pediatrician-triage and postpartum prompts.
  - 211 (group hard moments, rank 15, routes to `creative-writing`): "told
    everyone", "partner" match the memoir-ethics and blended-family prompts.
  - 212 (mandated parent): not in the top 100, routes to `education-teaching`.
    "Program" and "court" pull higher-education course design and custody
    prompts.
  - 214 (life-story work): not in the top 100. Common parenting words ("her",
    "keep", "year old", "help") lift dozens of caregiver prompts above it.
- **Leakage controls (stronger than Waves 7–9):** the 9 queries were drafted
  before any prompt was written and never existed in a file the authoring agents
  could read. Before authoring, only a SHA-256 commitment of the query text was
  stored. The query file was written after every target was final, and its hash
  matches the commitment. Four targets carry plain-language tags that overlap a
  query's everyday wording:
  - `first-meeting-with-new-family` (case 213)
  - `family-does-things-differently` (case 210)
  - `one-parent-takes-over-the-group` (case 211)
  - `parent-upset-at-visit` (case 209)

  The authors could not have seen the queries, so this is shared phrasing.
  Separately, the family-time prompt's visit rules name "whispering" and
  "promises", which case 209 also uses. These are standard supervised-visit
  ground rules.
- **§2 probes:** the 26 original probes keep their top hits. One changes at rank 3
  only: `what to do after a parent dies paperwork` shows
  `home-household-paperwork-system` instead of the fourth-trimester prompt, a
  term-weight shift that involves no new prompt. Three new probes land in the new
  cluster: `home visiting program for new parents` →
  `parenting-home-visit-plan-and-interaction`, `parent education group
  facilitator` → `parenting-parent-group-session-design`, and `foster care
  caseworker` keeps the caregiver foster prompt first with the family-time and
  life-story prompts 2nd and 3rd.

**Left for later:** the five misses above. Like the Wave 5–9 misses, they come from
the distance between situation language and practitioner language. The cluster has
no prompt yet for a parent who is a minor, or for professional supervision and
reflective practice for family-support staff (`psychology_supervision_agenda_builder`
is clinical).

### Wave 12: biblical-studies Phase 3C completed — shipped (11 prompts, 7 cases, 2026-10-05)

Wave 8 shipped the first part of `domain-biblical-studies` Phase 3C (`academic-writing/` and two
children's-ministry prompts). This wave builds the three remaining items the user requested. The
fourth remainder item (youth apologetics, intergenerational worship) stays deferred in the domain
roadmap. Every candidate went through a `pae search` and `PROMPT_INDEX.json` keyword sweep; none was
dropped, and no keyword (chaplain, premarital, Second Temple, rabbinic, midrash, supersession, PKM)
had an existing biblical prompt.

| Home | Files | Nearest neighbour (distinct from) |
|---|---|---|
| `domain-biblical-studies/pastoral-scripture/` (5, new), `biblical_pastoral_` | `premarital_scripture_component`, `recovery_scripture_engagement`, `formation_practices_scripture`, `chaplaincy_scripture_selection`, `misused_texts_after_abuse` | `biblical_ministry_marriage_enrichment_study` (married couples' group study), `discipleship_track_married_couples`, `clientself_faith_integrated_coping_plan` (clinical self-use), `discipleship_spiritual_practices_designer` (a disciple's own practice set), `biblical_ministry_grief_and_loss_scripture_guide`, `discipleship_module_forgiveness_and_reconciliation` (curriculum module) |
| `domain-biblical-studies/jewish-christian-dialogue/` (3, new), `biblical_dialogue_` | `jewish_tradition_text_reading`, `second_temple_context`, `anti_judaism_teaching_check` | `biblical_apologetics_other_religions_dialogue` (any religion, topic level), `biblical_multiview_interpretation_map` (within-Christian views), `biblical_historical_cultural_context` (all background), `biblical_exegetical_fallacy_detector` (logic errors) |
| `domain-biblical-studies/learner-self-study/` (+3), `biblical_learner_` | `digital_tool_workflow_guide`, `pkm_bible_study_notes`, `audio_podcast_learning` | `biblical_learner_study_tool_skill_builder` (using a concordance or lexicon well), `bottleneck_pkm_second_brain_architecture` (general PKM), `study_note_organization_system_designer` (medical learners), `biblical_learner_bible_reading_habit_builder` |

**Guards.**
- **Pastoral prompts:** Scripture selection only. Each has a STRONG-GUARD banner, a "not counseling or
  therapy" banner, and crisis and abuse routing as Step 1. No hotline number or statute is given from
  memory; `[VERIFY]` slots stand in. Mandated reporting is "verify locally" and never delayed by a
  consult. Joint or couple work and reconciliation are never recommended where abuse is present.
  Clinical work routes to `domain-psychology/`, lay mentoring to `domain-discipleship/mentor-equipping/`.
- **Dialogue prompts:** Jewish interpretation is presented in its own terms and attributed to
  identifiable traditions. No midrash, Talmud, Targum or commentary is quoted or located from memory,
  and no supersessionist framing appears in the prompt's own voice. Christian theologies of Israel are
  described and attributed only. The Second Temple prompt gates later rabbinic sources as later.
- **Digital prompts:** STRONG-GUARD on product claims (features, prices, licences, stances are
  `[VERIFY]`), organised by tool category, with an AI-assistant fabrication protocol and provenance
  tags on notes.

One example was corrected in review: the Second Temple example had labelled an interpretive conclusion
about Mark 2 "ESTABLISHED"; it now separates the established context from the contested reading.

**Routing after Wave 12** (`case-215`–`case-221` added):

| | Before (214 cases) | After (221 cases) |
|---|---|---|
| R@1 / R@3 / R@5 / MRR | 72.8 / 81.0 / 84.4% / 0.775 | 73.2 / 81.7 / 85.0% / 0.781 |
| scope@1 / scope@3 / kind@1 (router) | 84.8 / 93.3 / 97.7% | 84.9 / 93.5 / 97.7% |
| statuses (matched / ambiguous / weak / no_route) | 84 / 82 / 47 / 1 | 86 / 83 / 51 / 1 |
| Flat BM25 guard, R@1 and scope@1 | 71.4% and 82.6% | 72.5% and 83.2% (shipped still ≥ on both) |

- **Earlier cases.** The 214 cases were compared one by one against a worktree of the base commit
  (`59fe977`).
  - Case 162 (kinship) fell from rank 5 to 6 during the build, taking R@5 below its 0.84 floor in
    `test_search_regression.py`. The misused-texts prompt had matched "after", "help" and "them" in
    its title and description. The title ("…How Traditions Read Them") and the description's opening
    were reworded, and case 162 is back at rank 5. Case 148 (14 → 15) recovered with the same fix.
  - Two cases still differ, and neither involves a new prompt:
    - Case 138 moved from rank 71 to 70.
    - Route case 213 keeps its routed scope, but its two top parenting prompts swapped places and its
      status went from ambiguous to weak. That is a term-weight shift from corpus growth, and the
      case has no expected status.
- **New cases:** 6 of 7 route to `biblical-studies` first, against 3 of 7 on the base commit (215 went to
  `discipleship`, 217 to `legal`, 218 to a technique). Five of the 6 task cases rank their target first: 215 (pre-marital), 216 (recovery), 217 (chaplaincy), 218 (Akedah,
  Jewish reading) and 219 (Pharisees and Essenes). Honest misses, kept as they are:
  - 220 (John 8 sermon, rank 2): `biblical_sermon_series_planner` stays first on "preaching", "next
    week" and "sermon".
  - 221 (notes in Logos or Obsidian, route): routes to `medical-education`. The medical note-system
    prompt names Obsidian outright; the new PKM prompt is 2nd and the workflow guide 5th.
- **Leakage controls (as in Wave 11):** the 7 queries were drafted before any prompt was written and
  never existed in a file the authoring agents could read. Only a SHA-256 commitment of the query text
  was stored before authoring. The query file was written after every target was final, and its hash
  matches the commitment. Three targets carry plain-language tags that overlap a query's everyday
  wording: `what-to-read-at-a-bedside` (case 217), `what-to-read-with-couple-before-wedding` (case
  215) and `pharisees` (case 219). The authors could not have seen the queries, so this is shared
  phrasing.
- **§2 probes:** all 30 earlier probes keep their top three. Three new probes land in the new
  prompts: `pastoral counseling scripture` → the three pastoral prompts (it previously surfaced the
  grief guide); `jewish interpretation of the bible` → `biblical-dialogue-jewish-tradition-text-reading`;
  `bible study app` → the PKM, audio and workflow prompts, with the workflow guide only 3rd.

**Left for later:** the two misses above, and the deferred Phase 3C remainder (youth apologetics,
intergenerational worship).

### Quality backfill: raising the weakest existing prompts (2026-10-06, in progress)

Quality work, not new coverage: no new subject and no new file. Three targets, in priority order:

1. The 24 stub prompts in `domain-professional-writing/domain-specific/` (`domain_writing_*`, ~30
   lines: a "Source" line and one fill-in prompt) are expanded to the house structure, or merged into
   a stronger neighbour that already does the same job for the same reader.
2. A **False-Positive Prevention** section is added wherever it is missing in `domain-image-generation`
   (all 161), `domain-presentations` (34 of 42), `domain-advertising` (17 of 22),
   `domain-medical-education` (125 of 213), `domain-healthcare-clinical` (259 of 372) and
   `domain-deep-analysis` (17 of 21). `domain-science` keeps its own "Floor (per README)" structure and is
   left alone.
3. Missing frontmatter or `techniques:` metadata is added in `domain-conversation-practice` (7 of 14),
   `domain-presentations` (14), `domain-professional-writing` (26), `domain-image-generation` (92) and
   `domain-deep-analysis` (11).

**Rules held in every batch.**
- Each FPP section names the traps *that* prompt's output is prone to, in its subject's vocabulary,
  and includes at least one concrete check (recompute, count, trace to an input). A script flags any
  FPP sentence shared between two files in a batch; none has been shipped.
- The domain's own FPP layout wins (numbered in `deep-analysis` and `advertising`, ❌/✅ elsewhere).
- Technique IDs come only from `### XX-NN:` headings in the catalogue;
  `validate_technique_catalog.py` passes with 0 errors.
- Every healthcare-clinical prompt touched carries the domain's medical disclaimer and a
  **Review status: … AI only (2026-10-06)** line.
- New frontmatter keeps the file's existing H1 as its title, so search does not shift.
- Search indexes only frontmatter fields, so an FPP section cannot move a routing result; new
  frontmatter can. Every batch is compared case by case (221 cases) and on the 27 §2 probes against
  base commit `4804bc1`.

| Batch | Files | What changed | Routing vs base |
|---|---|---|---|
| 1 | 24 stubs + 2 | 21 `domain_writing_*` stubs rewritten to Tier 1 (objective, distinct-from neighbour, delimited inputs, method with a verify step, output format, verification, FPP, one coherent example, techniques); 3 merged; frontmatter + FPP on `business_writing_executive_proposal_template.md` and `business_writing_investment_proposal_example.md` | All metrics unchanged (R@1 73.2%, MRR 0.781, scope@1 84.9%). No gold rank moves. Ten cases change only below the scored positions (3rd routed scope, or case 106's no-route top hit); case 213 goes weak → ambiguous (no expected status). One probe gains the realtor listing at rank 2 (`comparative market analysis for a listing`), with its top hit unchanged |
| 2 | 24 | `domain-deep-analysis` (17): FPP in the numbered domain layout for the five plain companions and `deepthink_evaluation` (the four older plain companions already carried a plain copy under "Common ways this goes wrong", now titled FPP with one verification item added); frontmatter + FPP on `BACKBONE.md`; `techniques` + a 3-item wrapper-level FPP on the 10 slash commands. `domain-conversation-practice` (7): frontmatter + persona-specific FPP on the persona template and the six AI-skeptic personas | Metrics unchanged. Two new descriptions pulled cases 208/214 into a 2nd/3rd routed scope on incidental words ("24-year-old", "seriously", "but … not"); reworded, and both are back to base. Case 138 rank 70 → 69 |
| 3 | 34 | `domain-presentations`: frontmatter + FPP on the 14 root `powerpoint_*` generators (title = H1; "board-deck", "qbr" tags only on their own files); deck-specific FPP on the 20 `board-decks/` image prompts (each names its own arithmetic: bridge closes, funnel never widens, RICE re-sorts, one A per RACI row) and targets the template's "realistic business placeholders" line that invites invented numbers | Metrics unchanged. Seven cases gain `presentations` (or lose another scope) at routed position 2–3 only, e.g. case 183 (slide decks + screen reader), where it is on-subject |
| 4 | 29 | `domain-advertising` (17): vertical-specific FPP on every image prompt, in the campaign prompts' numbered layout, covering both the product misrepresentation each vertical is prone to and invented text in rendered slots (prices, badges, logos, ratings), with regulatory questions routed to counsel, not answered. `domain-image-generation/gpt-image-2/` (12): FPP per prompt; two template defects fixed on the way — the executive slide asked for 16:9 at `1536x1024` (3:2, now `2560x1440`), and the multi-reference composite's IGNORE lists let a body reference and a scene reference leak face and lighting | No case or probe changes against batch 3 |
| 5 | 31 | `domain-image-generation`: `branding/` (7), `nano-banana/` (5), `coloring-book/` (9, plus frontmatter for `image_to_coloring_book_page.md`), `ecommerce-product/` (5), `publishing-covers/` (5). Fixed on the way: the KDP interior bleed size (8.75 → 8.625 in wide: the binding edge takes no bleed), the typography guide's typographic-quotes rule (both glyphs were straight quotes), and the palette's Application Guide citing Primary 600/800, which the scale never defines (now 700/900) | No case or probe changes against batch 4 |
| 6 | 29 | `domain-image-generation/healthcare/` (all 29): FPP centred on anti-fabrication — every rendered dose, range, unit, label and branch traced verbatim to the clinician-verified source, placeholders that must survive rendering, unit and tall-man checks, left/right frames — plus `techniques` (the 8 core SV techniques each file applies). The 16 PACU visuals follow the perianesthesia SAFETY_PREAMBLE. Fixed: `pacu_infographic_image_prompt.md` hard-coded SpO2, BP, HR, temperature and O2-flow values the SAFETY_PREAMBLE forbids (now `per facility protocol` / `per order`) and carried a stray "Wait - correction" size line; the anatomy diagram's worked example mixed viewer and patient left/right | Case 177's 3rd routed scope returns to its base value; nothing else changes against batch 5 |
| 7 | 35 (+1 vendored copy) | `domain-image-generation`: `social-media/` (6), `events-print/` (3), `merch-print-on-demand/` (3), `childrens-illustration/` (3), `comic-sequential/` (3), `scientific-technical/` (3), `visualizations/` (14, plus `techniques`: the 8 core SV techniques the folder README requires). Role-specific FPP: every rendered number or label traced to the intake, pixel-measured chart checks, tiling and cut-line tests, reading-order checks. The vendored copy of `social_thumbnail_cover_brief.md` in `portable-prompt-system/` was re-synced. Fixed: the event poster's example date ("Saturday, October 12, 2026" is a Monday; now October 10) | No case or probe changes against batch 6 |
| 9 | 24 | `domain-image-generation/worksheet-generators/` (second half: life-skills, math, music, science, social studies, specialized formats): FPP on the content a child works from (solve every item, count every object, count beats per bar, find every word-search word, recompute totals) plus `techniques` (SV-05 and the 8 core SV techniques every worksheet README requires). Fixed: the timelines generator asked for "evenly spaced event nodes", which teaches that unequal gaps are equal; it now asks for proportional spacing or a "not to scale" label | No case or probe changes against batch 7 |
| 8 | 30 | `domain-image-generation` root (9): FPP "when applying this guide" for the eight guides and workflows (dated capability claims marked `[VERIFY]`, checks run on the render rather than the prompt text, drift judged against the anchor), FPP for `infographic_meta_prompt.md`, and frontmatter for the three guides that had none (title = H1, description from their own opening line). `worksheet-generators/` first half (21: arts, assessment, early childhood, foreign language, language arts, calendar routines): content-accuracy FPP plus `techniques`. With batches 4–9, every `domain-image-generation` file now has an FPP section and `techniques` | No case or probe changes against batch 9 |
| 10 | 32 | `domain-medical-education` educator tracks (assessment items 8, case writing 11, curriculum design 8, remediation 6 — first half): FPP in the domain's ❌/✅ table layout, one level more specific than the field guide's domain-wide rows (solve items blind, recompute derived values, sum item counts and minutes, trace premises to released data, describe behaviour rather than diagnose the learner). Fixed on the way: the modified-essay example's stem anion gap (22) did not match its own Na/Cl/HCO3 (24), and the PBL example's knowledge check assumed diuretics for a patient who took only ibuprofen | No case or probe changes against batch 8 |
| 11 | 32 | `domain-medical-education`: rubrics and workplace-based assessment (7), simulation design (10), board drills (10), clinical-reasoning drills (5). FPP in the table layout: per-axis recompute of calibration samples, vitals that must move together, exits that never punish a correct action, items solved blind, LR math recomputed, select-all options justified independently. Fixed on the way: the high-fidelity simulation example advanced the patient into shock when the learner correctly voiced anaphylaxis concern (now: early epinephrine → improving state), and the 360 form's release thresholds disagreed between its map and its protocol | No case or probe changes against batch 10 |
| 12 | 30 | `domain-healthcare-clinical/prompts/care-plans/` (28) and two coordination prompts: disease-specific FPP (the classification each plan uses, the contraindication and monitoring misses for its drug classes, population-specific targets, scores to recompute) and the domain's medical disclaimer with an **AI-only Review status** on every file. Frontmatter for `medicine_behavioral_health_coordination_micro_guide.md`. Possible clinical errors spotted in the existing text were listed, not silently changed (see "Clinical issues found" below) | No case or probe changes against batch 11 |
| 13 | 29 | `domain-medical-education`: OSCE rehearsals (4), procedures (3), study systems (6) and `profession-specific/` (16: allied, dental, EMS, nursing, PA, pharmacy). FPP in the table layout, with each profession's exam, scope and accreditation facts marked `[VERIFY]` against the current official source | No case or probe changes against batch 12 |
| 14 | 32 | `domain-medical-education`: clinical reasoning (7), clinical rotation (6), foundational sciences (11), OSCE communication rehearsals (5) — the last of the domain's 125 prompts without FPP. All 213 medical-education prompts now carry FPP | No case or probe changes against batch 13 |
| 15 | 29 | `domain-healthcare-clinical`: acute care (19), allied health (3), `careplan_afib.md`, the five specialty `guides/` and the anticoagulation worked example in `examples/` (frontmatter added to all six; their FPP is framed "when using this guide/example"). Disclaimer with AI-only Review status on every file; `techniques` added to seven prompts that lacked them. `_archive/EXPANSION_ROADMAP_v1_safety_framing.md` is an archived planning document and was left out | No case or probe changes against batch 14 |
| 16 | 30 | `domain-healthcare-clinical`: communication (5), education (1), interpretation (9: the recomputation each needs — anion gap and delta-delta, Winter's, corrected calcium, QTc, R factor, absolute counts — and the reporting lab's ranges and units), nursing (10) and pathophysiology (5). Frontmatter for `medicine_clinical_visual_education_micro_guide.md` and `nursing_quick_reference_handbook_creator_prompt.md`. Disclaimer with AI-only Review status on every file | No case or probe changes against batch 15 |

**Merges in batch 1** (recorded in `meta/REORG_MAP.tsv`; references repointed by `apply_reorg_map.py`):

| Stub | Merged into | What was carried over |
|---|---|---|
| `domain_writing_attorney_discovery` (stub, deleted) | `domain-legal/discovery/legal_discovery_response_objections.md` | Case-background and facts-per-answer inputs; a Must Not against narrowing a verified interrogatory answer by omission |
| `domain_writing_physician_soap` (stub, deleted) | `domain-healthcare-clinical/prompts/workflow/medicine_clinical_documentation.md` | An outpatient office-visit SOAP variant; codes are the clinician's, never inferred; E/M level routed to the coding prompt. The file now carries the review-status disclaimer |
| `domain_writing_marketing_campaign` (stub, deleted) | `domain-business-strategy/go-to-market/workflow_marketing_campaign_brief_development.md` | A "presented to" constraint for agencies and consultants presenting to a client |

The other 21 stay where they are, because `client-services-studio/verticals/`, `domain-specialized-fields/`
and `domain-presentations/` name them as the customer-facing writing step. Each now states the neighbour
it is distinct from. One defect was fixed on the way: the investment-proposal worked example labelled
its scenarios "8% relative" while computing 20%, and its 3-year ROI left out the license renewals
(700% → ~287%).

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
python3 scripts/validate_technique_catalog.py && (cd techniques && python3 audit_technique_index.py)
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
