# Domain-Operations Expansion Roadmap

**Status as of 2026-10-03:** Wave 1 (8 prompts), Wave 2 (9 prompts), Wave 3 (2 prompts) and Wave 4 (2 prompts) shipped — **21 prompts**
across `process-improvement/` (6), `supply-chain-procurement/` (6), `quality-safety/` (6),
and `project-delivery/` (3).
Planned and scoped in [`../meta/COVERAGE_ROADMAP.md`](../meta/COVERAGE_ROADMAP.md),
which records the nearest-neighbour boundaries each prompt was written against.

---

## Wave 2 — shipped (2026-10-02, coverage Wave 6)

All five Wave 2 candidates shipped, plus a new `quality-safety/` subfolder added to
scope (it was not on the candidate list). Domain total: **17 prompts**.

| Item | Shipped as | Distinct from |
|---|---|---|
| **S&OP cadence** | `supply-chain-procurement/ops_sales_and_operations_planning_cycle.md` | `ops_inventory_reorder_policy.md` (SKU-level policy, not the monthly plan); `domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md` (P&L re-forecast process); `domain-productivity/operating-cadence/` (individual cadence) |
| **Logistics / freight mode choice** | `supply-chain-procurement/ops_freight_mode_selection.md` | `ops_supplier_selection_scorecard.md` (supplier, not carrier mode) |
| **Standard work + kaizen event plan** | `process-improvement/ops_standard_work_and_kaizen_event.md` | `ops_process_map_and_waste_scan.md` (diagnosis); `business_writing_sop.md` (writing the procedure) |
| **Supplier quality / corrective action (SCAR)** | `supply-chain-procurement/ops_supplier_corrective_action_8d.md` | `ops_root_cause_a3_report.md` (your own problem, not the supplier's) |
| **Facility layout** | `process-improvement/ops_facility_layout_flow_analysis.md` | `ops_capacity_and_bottleneck_model.md` (capacity, not space) |
| *Added scope:* **SPC review** | `quality-safety/ops_spc_control_chart_review.md` | `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md` (business KPIs); `domain-science/statistics/` (research inference) |
| *Added scope:* **OEE loss analysis** | `quality-safety/ops_oee_loss_analysis.md` | `ops_capacity_and_bottleneck_model.md` (the system constraint, not one asset's losses) |
| *Added scope:* **Job hazard analysis** | `quality-safety/ops_job_hazard_analysis.md` | `domain-risk/risk_bow_tie_analysis.md`, `risk_fmea_analysis.md` (top-event and failure-mode views) |
| *Added scope:* **Safety incident investigation** | `quality-safety/ops_safety_incident_investigation.md` | `domain-legal/employment-labor/legal_workplace_investigation_plan_and_report.md` (misconduct, not safety events) |

The two safety prompts are drafts for review by a qualified safety professional and
make no regulatory compliance determination; future safety prompts must carry the
same structural review block.

---

## Wave 3 — shipped (2026-10-03, coverage Wave 7)

Maintenance and reliability, placed in `quality-safety/` because its object is the
equipment and its users (maintenance and reliability leads) are already that
subfolder's readers; both prompts compose directly with `ops_oee_loss_analysis.md`,
whose breakdown loss they take apart. Domain total: **19 prompts**.

| Item | Shipped as | Distinct from |
|---|---|---|
| **Preventive maintenance program design** | `quality-safety/ops_preventive_maintenance_program.md` | `ops_oee_loss_analysis.md` (one asset's losses, not the site's maintenance strategy); `domain-risk/risk_fmea_analysis.md` (formal failure-mode scoring); `domain-productivity/home-life/home_seasonal_maintenance_calendar.md` (home upkeep) |
| **Equipment reliability / repeat-failure analysis** | `quality-safety/ops_repeat_failure_reliability_analysis.md` | `ops_oee_loss_analysis.md` (all six losses in hours, not failure modes and intervals); `process-improvement/ops_root_cause_a3_report.md` (structured cause report it hands off to) |

## Wave 4 — shipped (2026-10-03, coverage Wave 9)

Depth in `project-delivery/`, which held only the plan. Domain total: **21 prompts**.

| Item | Shipped as | Distinct from |
|---|---|---|
| **Schedule recovery for a slipping project** | `project-delivery/ops_schedule_recovery_plan.md` | `ops_non_software_project_plan.md` (builds the baseline it re-forecasts); `domain-specialized-fields/professional-services/proserv_fixed_fee_overrun_diagnosis.md` (budget overrun on a client engagement, not schedule recovery) |
| **Project closeout and lessons learned** | `project-delivery/ops_project_closeout_and_lessons_learned.md` | `domain-decision-making/documentation/decisiondoc_after_action_report.md` (decision quality vs outcome); `domain-risk/risk_after_action_review.md` (after a risk event); `domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md` (software incidents); `domain-game-development/production/production_project_postmortem.md` (games) |

## Wave 5 — candidates (not yet built)

None scoped yet. Run `pae search` and check `meta/COVERAGE_ROADMAP.md` before adding.

---

## Conventions for future authors

1. Prefix `ops_` in every subfolder; `category: operations/<subfolder>`.
2. Match Wave 1 structure: Objective → When to Use (with a "Not this prompt if…"
   line) → Inputs → Method → Output Format → Verification → False-Positive
   Prevention → one coherent Example Output with numbers that add up → Techniques
   Used → Related Prompts. Exactly three `related_prompts`.
3. Label modeled figures as modeled; tag inputs `measured` / `sampled (n=)` /
   `estimated`. Flag safety-critical and regulated work for qualified review.
4. Technique IDs must exist in `techniques/MASTER_TECHNIQUE_INDEX.md`.
5. After adding files, regenerate the index: `python3 scripts/generate_prompt_index.py`.
