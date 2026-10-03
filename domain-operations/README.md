# Domain: Operations

Nineteen prompts for people who run **how work physically or organizationally gets
done**: a process, a supplier base, an inventory, a quality defect, or a project
that is not software. The domain's subject is the operation itself. You bring the
process, the SKU list, the bids, or the move date; the prompts turn them into a map,
a model, a policy, or a plan whose numbers can be checked.

Users are operations managers, plant and warehouse leads, buyers and procurement
staff, facilities managers, continuous-improvement practitioners (lean, Six Sigma),
quality, maintenance and EHS staff, and small-business owners who do all of those jobs at once.

> ## Guard — read this first
>
> - **Modeled is not measured.** Capacity, lead-time, safety-stock, benefit, and
>   schedule figures that these prompts compute from your inputs are **models**.
>   Every prompt labels them *modeled* or *estimate* and tags each input `measured`,
>   `sampled (n=)`, or `estimated`. Do not report a modeled improvement as achieved
>   until it has been measured after the change.
> - **Safety-critical and regulated work goes to a qualified reviewer.** Fire and
>   life safety, structural and electrical work, occupancy permits, food safety,
>   medical devices, aerospace parts, hazardous materials, and public-sector
>   procurement rules are *flagged*, not decided, here. The responsible qualified
>   professional, quality function, or authority approves them.
> - **No invented data.** Where an input is missing, the output carries a
>   `[measure]` or `[verify]` marker and a data-collection step rather than a
>   plausible number.

---

## Directory map

| Subdirectory | What it covers | Prompts |
|---|---|---|
| `process-improvement/` | As-is mapping and waste, root-cause A3, DMAIC chartering, capacity and bottlenecks, standard work and kaizen, facility layout | 6 |
| `supply-chain-procurement/` | Supplier selection and TCO, inventory reorder policy, buyer-side RFPs, S&OP, freight mode, supplier corrective action (8D) | 6 |
| `quality-safety/` | SPC and capability, OEE losses, preventive maintenance program, repeat-failure reliability analysis, job hazard analysis, safety incident investigation — safety prompts are drafts for qualified review ([README](quality-safety/README.md)) | 6 |
| `project-delivery/` | Fixed-date non-software projects: WBS, critical path, RACI | 1 |

**File naming:** `ops_{specific_function}.md` in every subfolder.

### `process-improvement/`

| File | Purpose |
|---|---|
| `ops_process_map_and_waste_scan.md` | SIPOC boundaries, value-stream timeline (touch vs. queue time), eight-waste scan tied to steps, lead time vs. touch time and PCE |
| `ops_root_cause_a3_report.md` | One-page A3: quantified gap, current condition from data, fishbone to widen and 5-why to deepen, countermeasures, a disconfirming result, follow-up |
| `ops_dmaic_project_charter.md` | Problem statement without cause or solution, CTQs with operational definitions, baseline with variation, in/out scope, estimated benefit, measurement-system check before Analyze |
| `ops_capacity_and_bottleneck_model.md` | Effective capacity per step, utilization at average and peak, the one constraint, Little's Law cross-check, ρ/(1−ρ) queueing sanity, where the constraint moves next |
| `ops_standard_work_and_kaizen_event.md` | Takt, observed element times, theoretical operators with the fraction shown, operator balance, standard work set, a scoped 3–5 day event, 30-day sustain audit |
| `ops_facility_layout_flow_analysis.md` | Spaghetti diagram, from-to matrix, load × distance score, SLP adjacency chart, fixed constraints, 2–3 layout options with cost, downtime, payback, and qualified-review items |

### `supply-chain-procurement/`

| File | Purpose |
|---|---|
| `ops_supplier_selection_scorecard.md` | Weighted criteria on anchored scales fixed before scoring, landed TCO, supply risk, weight sensitivity, single/dual/split sourcing with its premium |
| `ops_inventory_reorder_policy.md` | ABC/XYZ segmentation, service level per cell (CSL vs. fill rate), safety stock with lead-time variability, reorder point, EOQ vs. MOQ, cost per point of service |
| `ops_rfp_procurement_package.md` | Buyer-side RFP: mandatory vs. evaluated requirements, one price form, rubric frozen before bids, single-channel Q&A published to all, independent scoring, award record |
| `ops_sales_and_operations_planning_cycle.md` | Monthly S&OP in product families: forecast bias and WMAPE, unconstrained demand review, supply review with gaps in units and weeks, pre-S&OP priced scenarios, executive decisions, decisions log |
| `ops_freight_mode_selection.md` | Parcel/LTL/FTL/intermodal/air/ocean screen, landed cost per unit incl. in-transit and safety-stock carrying, mean and P90 transit, Incoterms 2020 consequences, stress test |
| `ops_supplier_corrective_action_8d.md` | SCAR in is/is-not form, D0–D8 gate review, occurrence and escape root causes, containment with a clean point, verification of effectiveness on your own post-change data |

### `quality-safety/`

| File | Purpose |
|---|---|
| `ops_spc_control_chart_review.md` | Chart selection, control limits from the process not the spec, declared Western Electric/Nelson rules and false-alarm cost, Cp/Cpk/Ppk only when stable with gauge R&R stated |
| `ops_oee_loss_analysis.md` | Definitions first, availability × performance × quality with cross-check, six-big-losses waterfall in hours, dominant loss, data-honesty audit |
| `ops_preventive_maintenance_program.md` | Asset criticality A/B/C, run-to-failure vs time-based vs condition-based vs failure-finding per failure mode, PM tasks with acceptance limits, schedule load vs real hours, compliance by class, backlog in crew-weeks |
| `ops_repeat_failure_reliability_analysis.md` | Failures by mode with censored removals, MTBF/MTTR and repair-time waterfall, downtime Pareto, trend test before Weibull, RCM-lite task choice, modeled target with verification date |
| `ops_job_hazard_analysis.md` | Observed steps, energy-source hazard sweep, inherent and residual risk, hierarchy of controls; **draft for qualified safety review, no compliance determination** |
| `ops_safety_incident_investigation.md` | Sourced timeline, work-as-done vs. work-as-imagined, causal chain to system conditions, just-culture test, controls with effectiveness checks; **draft for qualified safety review**; misconduct goes to `domain-legal/` |

### `project-delivery/`

| File | Purpose |
|---|---|
| `ops_non_software_project_plan.md` | Office moves, events, installs, multi-site rollouts: deliverable WBS, critical path and float, RACI with one Accountable, go/no-go gates, critical-path risks |

---

## Quick routing

| You're saying | Use |
|---|---|
| "This process takes forever and nobody knows where the time goes" | `process-improvement/ops_process_map_and_waste_scan.md` |
| "We keep fixing this defect and it keeps coming back" | `process-improvement/ops_root_cause_a3_report.md` |
| "The sponsor wants a scoped Six Sigma project before assigning people" | `process-improvement/ops_dmaic_project_charter.md` |
| "Everyone is busy and we still can't keep up with demand" | `process-improvement/ops_capacity_and_bottleneck_model.md` |
| "The cheapest supplier isn't obviously the best one" | `supply-chain-procurement/ops_supplier_selection_scorecard.md` |
| "We have stockouts and excess stock at the same time" | `supply-chain-procurement/ops_inventory_reorder_policy.md` |
| "I need to run a fair tender and defend the award" | `supply-chain-procurement/ops_rfp_procurement_package.md` |
| "Sales, ops, and finance each have a different plan" | `supply-chain-procurement/ops_sales_and_operations_planning_cycle.md` |
| "Should we ship LTL or full truckloads?" | `supply-chain-procurement/ops_freight_mode_selection.md` |
| "The supplier's 8D says 'retrained' again" | `supply-chain-procurement/ops_supplier_corrective_action_8d.md` |
| "Everyone does this job differently; we need a kaizen week" | `process-improvement/ops_standard_work_and_kaizen_event.md` |
| "Forklifts cross the whole building all day" | `process-improvement/ops_facility_layout_flow_analysis.md` |
| "Is this process in control, and is our Cpk real?" | `quality-safety/ops_spc_control_chart_review.md` |
| "The machine runs but output is far below nameplate" | `quality-safety/ops_oee_loss_analysis.md` |
| "We're always firefighting breakdowns and the PM list is a copy of the manual" | `quality-safety/ops_preventive_maintenance_program.md` |
| "This pump has failed six times this year and it's getting worse" | `quality-safety/ops_repeat_failure_reliability_analysis.md` |
| "We need a hazard analysis before anyone does this task" | `quality-safety/ops_job_hazard_analysis.md` |
| "Someone nearly got hit by a forklift" | `quality-safety/ops_safety_incident_investigation.md` |
| "We move offices in 14 weeks — will we make it?" | `project-delivery/ops_non_software_project_plan.md` |

## How the prompts compose

`ops_process_map_and_waste_scan` is the usual entry point: its timeline becomes the
current-condition section of `ops_root_cause_a3_report` or the Measure phase of
`ops_dmaic_project_charter`, and a queue that turns out to be a capacity shortfall
goes to `ops_capacity_and_bottleneck_model`. On the supply side,
`ops_rfp_procurement_package` runs the competitive event, `ops_supplier_selection_scorecard`
turns the bids into a sourcing decision, and the chosen supplier's lead time and MOQ
feed `ops_inventory_reorder_policy`. `ops_non_software_project_plan` uses the RFP
prompt to contract its vendors and hands its critical-path risks to
`domain-risk/risk_register_builder.md`.

A diagnosed process goes to `ops_standard_work_and_kaizen_event` for a focused fix, or
to `ops_facility_layout_flow_analysis` when the waste is transport. Monthly,
`ops_sales_and_operations_planning_cycle` sets the family-level plan that the reorder
policy executes, and `ops_freight_mode_selection` sets the freight line and lead time
that the scorecard and reorder policy consume; a supplier defect runs through
`ops_supplier_corrective_action_8d`. In `quality-safety/`, `ops_oee_loss_analysis`
names the biggest loss on a constraint asset, `ops_spc_control_chart_review` separates
common from special causes, `ops_repeat_failure_reliability_analysis` takes a breakdown
loss down to its failure mode, `ops_preventive_maintenance_program` sets maintenance
strategy and schedule across the site, and the safety pair — `ops_job_hazard_analysis` before
the work, `ops_safety_incident_investigation` after an event — feed each other.

---

## Not here — negative boundaries

| If you need… | Go to |
|---|---|
| A maintained risk register, an FMEA, or a business continuity plan | `domain-risk/` — `risk_register_builder.md`, `risk_fmea_analysis.md`, `risk_business_continuity_plan.md` |
| Investigating alleged workplace misconduct (not a safety event) | `domain-legal/employment-labor/legal_workplace_investigation_plan_and_report.md` |
| The finance team's P&L rolling re-forecast process | `domain-finance/corporate-finance-fpa/finance_rolling_forecast_designer.md` |
| Software delivery: sprints, incidents, software post-mortems, debugging | `domain-engineering-workflows/` — e.g. `workflows/engineering_post_mortem_root_cause_ladder.md`, `workflows/engineering_debugging_root_cause.md` |
| **Writing** the SOP for a process (not designing it) | `domain-professional-writing/business-writing/business_writing_sop.md` |
| Evaluating **one** product or software vendor for a purchase decision | `domain-business-strategy/research/research_vendor_evaluation.md` |
| A banking-services RFP | `domain-finance/treasury-capital-markets/finance_bank_relationship_rfp_framework.md` |
| Responding to an RFP as the seller | `domain-professional-writing/business-writing/business_writing_proposal.md` |
| Negotiating price and terms with a vendor | `domain-negotiation/contexts/negotiation_vendor_procurement_buyside.md` |
| Forecasting intermittent demand | `domain-AI-ML/specialized-ml/time-series/ts_intermittent_demand_forecasting.md` |
| Billable-day capacity in a services firm | `domain-business-strategy/client-services/services_capacity_and_utilization_planner.md` |
| Software sprint planning from a PRD | `domain-product-management/prompts/product_delivery_sprint_planner.md` |
| Your own personal bottlenecks and workflow | `domain-productivity/bottlenecks/` |
| Data pipelines, dashboards, and marketing operations tooling | `domain-agentic-resources/skills/data-engineering/`, `domain-agentic-resources/skills/marketing/` |

**Subject decides first:** if the object is a codebase, it is software engineering;
a contract, legal; a model or dataset, AI-ML. This domain holds the operation —
the process, the supplier, the stock, the physical project.

See [`EXPANSION_ROADMAP.md`](EXPANSION_ROADMAP.md) for the next wave.
