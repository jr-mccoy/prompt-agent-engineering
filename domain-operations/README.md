# Domain: Operations

Eight prompts for people who run **how work physically or organizationally gets
done**: a process, a supplier base, an inventory, a quality defect, or a project
that is not software. The domain's subject is the operation itself. You bring the
process, the SKU list, the bids, or the move date; the prompts turn them into a map,
a model, a policy, or a plan whose numbers can be checked.

Users are operations managers, plant and warehouse leads, buyers and procurement
staff, facilities managers, continuous-improvement practitioners (lean, Six Sigma),
and small-business owners who do all of those jobs at once.

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
| `process-improvement/` | As-is mapping and waste, root-cause A3, DMAIC chartering, capacity and bottlenecks | 4 |
| `supply-chain-procurement/` | Supplier selection and TCO, inventory reorder policy, buyer-side RFPs | 3 |
| `project-delivery/` | Fixed-date non-software projects: WBS, critical path, RACI | 1 |

**File naming:** `ops_{specific_function}.md` in every subfolder.

### `process-improvement/`

| File | Purpose |
|---|---|
| `ops_process_map_and_waste_scan.md` | SIPOC boundaries, value-stream timeline (touch vs. queue time), eight-waste scan tied to steps, lead time vs. touch time and PCE |
| `ops_root_cause_a3_report.md` | One-page A3: quantified gap, current condition from data, fishbone to widen and 5-why to deepen, countermeasures, a disconfirming result, follow-up |
| `ops_dmaic_project_charter.md` | Problem statement without cause or solution, CTQs with operational definitions, baseline with variation, in/out scope, estimated benefit, measurement-system check before Analyze |
| `ops_capacity_and_bottleneck_model.md` | Effective capacity per step, utilization at average and peak, the one constraint, Little's Law cross-check, ρ/(1−ρ) queueing sanity, where the constraint moves next |

### `supply-chain-procurement/`

| File | Purpose |
|---|---|
| `ops_supplier_selection_scorecard.md` | Weighted criteria on anchored scales fixed before scoring, landed TCO, supply risk, weight sensitivity, single/dual/split sourcing with its premium |
| `ops_inventory_reorder_policy.md` | ABC/XYZ segmentation, service level per cell (CSL vs. fill rate), safety stock with lead-time variability, reorder point, EOQ vs. MOQ, cost per point of service |
| `ops_rfp_procurement_package.md` | Buyer-side RFP: mandatory vs. evaluated requirements, one price form, rubric frozen before bids, single-channel Q&A published to all, independent scoring, award record |

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

---

## Not here — negative boundaries

| If you need… | Go to |
|---|---|
| A maintained risk register, an FMEA, or a business continuity plan | `domain-risk/` — `risk_register_builder.md`, `risk_fmea_analysis.md`, `risk_business_continuity_plan.md` |
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
