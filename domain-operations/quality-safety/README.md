# Operations — Quality and Safety

Six prompts for the people who keep a physical operation **stable, reliable,
efficient, and safe**: quality engineers and technicians, maintenance and reliability leads, EHS
coordinators, supervisors, and the small-plant manager who is all of them. The object
is the equipment, the process output, or the task a worker performs.

> **Safety gate.** `ops_job_hazard_analysis.md` and
> `ops_safety_incident_investigation.md` produce **drafts**. A qualified safety
> professional reviews and approves them before use, and neither makes a regulatory
> compliance, reportability, or legal determination. Both carry that statement as a
> structural block in their output. Lockout/tagout, confined space, hot work,
> process safety management, and chemical exposure assessment are flagged to
> specialist programmes, not written here.
>
> **Maintenance work stays within its limits.** The maintenance prompts schedule
> statutory inspections (pressure systems, lifting equipment, fire systems, safety
> interlocks) and flag isolation procedures for qualified review; they do not
> redesign them.
>
> **Modeled is not measured.** Capability indices, OEE recovery, MTBF targets, and residual risk
> ratings are computed from your inputs; label them, and confirm by measurement after
> the change.

## Prompts

| File | Purpose |
|---|---|
| `ops_spc_control_chart_review.md` | Chart choice from data type and subgroup size, limits from the process (not the spec), declared Western Electric/Nelson rules with their false-alarm cost, Cp/Cpk/Ppk only when stable and the gauge is adequate |
| `ops_oee_loss_analysis.md` | Definitions fixed first, A × P × Q with cross-check, six-big-losses waterfall in hours, the dominant loss stratified, and an audit of the data choices that inflate OEE |
| `ops_preventive_maintenance_program.md` | Asset criticality, run-to-failure / time-based / condition-based / failure-finding strategy per failure mode, PM tasks with acceptance limits, schedule load against real hours, compliance by criticality class, backlog in crew-weeks |
| `ops_repeat_failure_reliability_analysis.md` | Failures by mode with censored removals, MTBF / MTTR and the repair-time waterfall, downtime Pareto, trend test before Weibull (with validity caveats), RCM-lite task selection, modeled target with a verification date |
| `ops_job_hazard_analysis.md` | Observed task steps, energy-source hazard sweep, inherent and residual risk, controls chosen down the hierarchy with rejected levels recorded; draft for qualified review |
| `ops_safety_incident_investigation.md` | Sourced timeline, work-as-imagined vs. work-as-done, causal chain to system conditions, just-culture test before any individual conclusion, controls with effectiveness checks; draft for qualified review |

## How they compose

`ops_oee_loss_analysis` names the biggest loss on a constraint asset; if that loss is
quality, `ops_spc_control_chart_review` tells you whether it is common- or
special-cause variation, and either finding goes to
`../process-improvement/ops_root_cause_a3_report.md` for cause. If the loss is
breakdowns, `ops_repeat_failure_reliability_analysis` finds the failure mode and
pattern on the problem asset, and `ops_preventive_maintenance_program` sets the
strategy and schedule for the whole site, folding in what the reliability analysis
chose. On the safety side,
`ops_job_hazard_analysis` is written before the work; `ops_safety_incident_investigation`
after something goes wrong, and its findings update the JHA.

## Lives elsewhere

| If you need… | Go to |
|---|---|
| Investigating alleged misconduct (harassment, discrimination, retaliation) | `domain-legal/employment-labor/legal_workplace_investigation_plan_and_report.md` |
| Seasonal upkeep of your own home | `domain-productivity/home-life/home_seasonal_maintenance_calendar.md` |
| Software reliability, SLOs and error budgets | `domain-software-engineering/mobile/android/maintenance/android_reliability_slo_error_budget_review.md`; `domain-engineering-workflows/` |
| FMEA, bow-tie barrier analysis, or a risk register | `domain-risk/` — `risk_fmea_analysis.md`, `risk_bow_tie_analysis.md`, `risk_register_builder.md` |
| A supplier's defect and their 8D response | `../supply-chain-procurement/ops_supplier_corrective_action_8d.md` |
| Patient-safety adverse events in healthcare | `domain-healthcare-clinical/prompts/quality/medicine_adverse_event_analyzer.md` |
| Software incidents and outages | `domain-engineering-workflows/workflows/engineering_post_mortem_root_cause_ladder.md` |
| A business KPI that moved (not a process characteristic) | `domain-data-analytics/analysis-and-sql/analytics_metric_movement_investigation.md` |
| Research statistics and designed experiments | `domain-science/statistics/` |
