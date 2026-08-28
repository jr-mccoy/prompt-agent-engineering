# Engineering Workflows

Prompts for how an engineering team ships: debugging, incident response,
delivery planning, design drafts, and review practice.

**Total prompts:** 18

---

## Prompts

| Prompt | When to use |
|---|---|
| [`engineering_prompt_for_debugging_code.md`](engineering_prompt_for_debugging_code.md) | Systematic debugging of a stuck bug |
| [`engineering_debugging_root_cause.md`](engineering_debugging_root_cause.md) | Deeper root-cause pass when the systematic approach stalls |
| [`debug_prompt.md`](debug_prompt.md) | Quick debugging template |
| [`android_jetpack_compose_debug.md`](android_jetpack_compose_debug.md) | Android / Jetpack Compose specific debugging |
| [`engineering_post_mortem_root_cause_ladder.md`](engineering_post_mortem_root_cause_ladder.md) | Blameless post-mortem via a why-ladder |
| [`engineering_postmortem_blueprint.md`](engineering_postmortem_blueprint.md) | Full post-mortem document with a root-cause audit |
| [`workflow_engineering_incident_root_cause_analysis.md`](workflow_engineering_incident_root_cause_analysis.md) | Live production incident: timeline → cause → impact → owned actions → comms drafts |
| [`engineering_delivery_sprint_planner.md`](engineering_delivery_sprint_planner.md) | Sprint planning and estimation from the engineering seat |
| [`engineering_solo_dev_roadmap_planner.md`](engineering_solo_dev_roadmap_planner.md) | Quarterly roadmap for a solo or very small team, with a tech-debt allowance |
| [`pre_code_planning_canvas.md`](pre_code_planning_canvas.md) | Think before implementing |
| [`engineering_data_schema_draft.md`](engineering_data_schema_draft.md) | Draft a data schema |
| [`workflow_engineering_api_design_review.md`](workflow_engineering_api_design_review.md) | Review an API spec for standards, scalability, and breaking changes |
| [`workflow_engineering_technical_debt_assessment.md`](workflow_engineering_technical_debt_assessment.md) | Inventory and rank technical debt against real capacity |
| [`engineering_merged_pr_review_audit.md`](engineering_merged_pr_review_audit.md) | Audit what merged review actually caught |
| [`workflow_definition_of_done_builder.md`](workflow_definition_of_done_builder.md) | Build a definition of done for a team or a work type |
| [`engineering_project_status_summary.md`](engineering_project_status_summary.md) | Summarize project status for reporting |
| [`coding_problems_catalog.md`](coding_problems_catalog.md) | Catalog of coding challenges |
| [`todo_app_ui_polish_implementation_plan.md`](todo_app_ui_polish_implementation_plan.md) | Worked example of a UI polish plan |

---

## By purpose

**Debugging** — `engineering_prompt_for_debugging_code`, `engineering_debugging_root_cause`, `debug_prompt`, `android_jetpack_compose_debug`

**Incidents and post-mortems** — `workflow_engineering_incident_root_cause_analysis` (during and just after), `engineering_post_mortem_root_cause_ladder` and `engineering_postmortem_blueprint` (the write-up)

**Planning and delivery** — `engineering_delivery_sprint_planner`, `engineering_solo_dev_roadmap_planner`, `pre_code_planning_canvas`, `workflow_engineering_technical_debt_assessment`

**Design and review** — `engineering_data_schema_draft`, `workflow_engineering_api_design_review`, `engineering_merged_pr_review_audit`, `workflow_definition_of_done_builder`

**Reporting** — `engineering_project_status_summary`

---

## Route elsewhere for

- **Deciding what to build, PRDs, market sizing** → [`domain-product-management/`](../../domain-product-management/)
- **Sales, marketing, customer-success workflows** → [`domain-business-strategy/go-to-market/`](../../domain-business-strategy/go-to-market/) — these used to live here despite not being engineering
- **Code-level analysis, refactoring, repo audits** → [`domain-software-engineering/`](../../domain-software-engineering/)
- **Personal goal systems, stakeholder navigation, learning to code** → [`domain-personal-development/`](../../domain-personal-development/) and [`domain-learning-coding/`](../../domain-learning-coding/) — all three used to live here
- **Definition-of-done as a delegation gate for an AI agent** → [`../done-definition/`](../done-definition/)
