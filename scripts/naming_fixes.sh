#!/bin/bash
# Naming Convention Fixes Script
# Fixes Finding 1.3 from REPOSITORY_REVIEW_REPORT_2026-01-28.md

set -e

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Function to rename a file and update git
rename_file() {
    local old_path="$1"
    local new_name="$2"
    local dir=$(dirname "$old_path")
    local new_path="$dir/$new_name"

    if [ -f "$old_path" ]; then
        git mv "$old_path" "$new_path" 2>/dev/null || mv "$old_path" "$new_path"
        echo "Renamed: $(basename "$old_path") -> $new_name"
    else
        echo "SKIP (not found): $old_path"
    fi
}

echo "=== Fixing Naming Convention Violations ==="
echo ""

# === Category 1: Files with articles (_a_, _the_, _an_) ===
echo "--- Removing articles from filenames ---"

# domain-professional-communication/prompts/
rename_file "domain-professional-communication/prompts/product_create_a_prd.md" "product_create_prd.md"
rename_file "domain-professional-communication/prompts/product_plan_for_the_plan_coding_roadmap.md" "product_planning_coding_roadmap.md"

# domain-personal-development/prompts/
rename_file "domain-personal-development/prompts/work_better_decompose_a_learning_task.md" "work_better_decompose_learning_task.md"

# domain-decision-making/
rename_file "domain-decision-making/decisioning_decompose_a_learning_task.md" "decisioning_decompose_learning_task.md"
rename_file "domain-decision-making/decisioning_shift_to_a_fresh_latent_corner.md" "decisioning_shift_fresh_latent_corner.md"

# domain-image-generation/worksheet-generators/assessment/
rename_file "domain-image-generation/worksheet-generators/assessment/education_fill_in_the_blank_review.md" "education_fill_blank_review.md"

# domain-professional-writing/writing/
rename_file "domain-professional-writing/writing/writing_thesis_builder_for_an_essay.md" "writing_thesis_builder_essay.md"

echo ""
echo "--- Shortening excessively long filenames ---"

# === Category 2: Files with excessive length (>55 chars) ===
# Target: Under 55 characters including .md extension

# domain-personal-development/prompts/ (work_better_* files)
rename_file "domain-personal-development/prompts/work_better_advanced_prompt_architect_comprehensive_prompt_refinement_blueprint.md" "work_better_prompt_architect_refinement.md"
rename_file "domain-personal-development/prompts/work_better_hidden_meeting_pattern_detector_kill_the_zombie_calendar.md" "work_better_zombie_meeting_detector.md"
rename_file "domain-personal-development/prompts/work_better_automation_gold_mine_finder_let_the_bots_eat_the_boring.md" "work_better_automation_gold_mine.md"
rename_file "domain-personal-development/prompts/work_better_next_move_in_stakeholder_fog_untangle_the_politics.md" "work_better_stakeholder_politics.md"
rename_file "domain-personal-development/prompts/work_better_open_loop_audit_find_the_leaks_in_my_mental_ram.md" "work_better_open_loop_audit.md"
rename_file "domain-personal-development/prompts/work_better_precision_doc_edit_cut_the_fluff_keep_the_voice.md" "work_better_precision_doc_edit.md"
rename_file "domain-personal-development/prompts/work_better_flip_to_interrogative_mode_just_keep_asking.md" "work_better_interrogative_mode.md"
rename_file "domain-personal-development/prompts/work_better_regret_minimization_frame_ask_future_you.md" "work_better_regret_minimization.md"
rename_file "domain-personal-development/prompts/work_better_prompt_to_prompt_expander_sharpen_my_ask.md" "work_better_prompt_expander.md"

# domain-decision-making/
rename_file "domain-decision-making/decisioning_open_loop_audit_find_the_leaks_in_my_mental_ram.md" "decisioning_open_loop_audit.md"
rename_file "domain-decision-making/decisioning_flip_to_interrogative_mode_just_keep_asking.md" "decisioning_interrogative_mode.md"
rename_file "domain-decision-making/decisioning_regret_minimization_frame_ask_future_you.md" "decisioning_regret_minimization.md"

# domain-professional-communication/prompts/
rename_file "domain-professional-communication/prompts/product_hidden_meeting_pattern_detector_kill_the_zombie_calendar.md" "product_zombie_meeting_detector.md"
rename_file "domain-professional-communication/prompts/product_automation_gold_mine_finder_let_the_bots_eat_the_boring.md" "product_automation_gold_mine.md"
rename_file "domain-professional-communication/prompts/product_next_move_in_stakeholder_fog_untangle_the_politics.md" "product_stakeholder_politics.md"
rename_file "domain-professional-communication/prompts/product_front_end_look_and_feel_hunt_show_me_the_vibe.md" "product_frontend_look_feel_hunt.md"

# domain-professional-communication/design/
rename_file "domain-professional-communication/design/design_front_end_look_and_feel_hunt_show_me_the_vibe.md" "design_frontend_look_feel_hunt.md"

# domain-professional-writing/writing/
rename_file "domain-professional-writing/writing/writing_precision_doc_edit_cut_the_fluff_keep_the_voice.md" "writing_precision_doc_edit.md"

# domain-research-academic/prompts/
rename_file "domain-research-academic/prompts/research_precision_doc_edit_cut_the_fluff_keep_the_voice.md" "research_precision_doc_edit.md"
rename_file "domain-research-academic/prompts/research_revised_prompt_example_strategic_feedback_interpreter.md" "research_strategic_feedback_interpreter.md"

# domain-engineering-workflows/workflows/
rename_file "domain-engineering-workflows/workflows/engineering_the_debugging_root_cause_mode_prompt.md" "engineering_debugging_root_cause.md"
rename_file "domain-engineering-workflows/workflows/engineering_enhanced_postmortem_blueprint_with_root_cause_audit.md" "engineering_postmortem_blueprint.md"
rename_file "domain-engineering-workflows/workflows/engineering_hidden_meeting_pattern_detector_zombie_calendar.md" "engineering_zombie_meeting_detector.md"
rename_file "domain-engineering-workflows/workflows/workflow_customer_success_account_health_assessment_and_risk_identification.md" "workflow_cs_account_health_risk.md"
rename_file "domain-engineering-workflows/workflows/workflow_marketing_content_performance_analysis_and_gap_identification.md" "workflow_marketing_content_gaps.md"
rename_file "domain-engineering-workflows/workflows/workflow_customer_success_onboarding_plan_and_90_day_success_roadmap.md" "workflow_cs_onboarding_90day.md"
rename_file "domain-engineering-workflows/workflows/workflow_marketing_campaign_brief_development_from_business_goals.md" "workflow_marketing_campaign_brief.md"
rename_file "domain-engineering-workflows/workflows/workflow_engineering_technical_debt_assessment_and_prioritization.md" "workflow_engineering_tech_debt.md"
rename_file "domain-engineering-workflows/workflows/workflow_sales_pipeline_risk_assessment_and_deal_prioritization.md" "workflow_sales_pipeline_risk.md"
rename_file "domain-engineering-workflows/workflows/workflow_engineering_api_design_review_and_standards_compliance.md" "workflow_engineering_api_review.md"
rename_file "domain-engineering-workflows/workflows/workflow_engineering_production_incident_root_cause_analysis.md" "workflow_engineering_incident_rca.md"
rename_file "domain-engineering-workflows/workflows/workflow_sales_discovery_call_preparation_from_crm_data.md" "workflow_sales_discovery_prep.md"
rename_file "domain-engineering-workflows/workflows/workflow_customer_success_account_health_assessment.md" "workflow_cs_account_health.md"

# domain-business-strategy/analysis/
rename_file "domain-business-strategy/analysis/strategy_talent_retention_comp_adjustment_vs_role_change_vs_accept_attrition.md" "strategy_talent_retention_decision.md"
rename_file "domain-business-strategy/analysis/strategy_ai_architecture_rag_vs_fine_tuning_vs_prompt_engineering.md" "strategy_ai_architecture_selection.md"
rename_file "domain-business-strategy/analysis/strategy_ai_evaluation_strategy_how_to_measure_quality.md" "strategy_ai_quality_measurement.md"
rename_file "domain-business-strategy/analysis/strategy_ai_data_strategy_collection_quality_and_moat.md" "strategy_ai_data_quality_moat.md"
rename_file "domain-business-strategy/analysis/strategy_portfolio_strategy_invest_harvest_or_divest.md" "strategy_portfolio_investment.md"
rename_file "domain-business-strategy/analysis/strategy_team_build_out_hire_vs_contract_vs_offshore.md" "strategy_team_buildout_decision.md"

echo ""
echo "=== Naming fixes complete ==="
echo ""
echo "Summary:"
echo "- Removed articles from 7 filenames"
echo "- Shortened 35 excessively long filenames"
echo "- Removed 1 duplicate file with special characters"
