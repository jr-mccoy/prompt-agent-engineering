# Android Planning Prompts

Planning-stage prompts that sit **upstream** of `../implementation/`, `../analysis/`, and `../testing/`. Use them to decide *what* you are building, *how* it should be structured, and *which* non-functional bars it must clear — **before** code is written. Each prompt gathers context, works in gated phases, and ends with a verification checklist.

There are **27 prompts** here, grouped into seven tracks. You rarely need all of them — pick by the decision you're facing. The pipeline below shows the common path.

---

## Recommended pipeline

```
                         ┌─ Product & Scope ──────────────────────────┐
  concept_validation ──▶ │ mvp_scope ▶ monetization ▶ analytics_plan   │
        │                │ device_support_and_form_factor             │
        ▼                └────────────────────────────────────────────┘
  Architecture & Technical Design                       Quality / Security / Compliance (by design)
  architecture_selection ─┬─ tech_stack_selection        performance_budget_and_nfr_plan
  navigation_and_screen_map│  module_design               mobile_threat_model
  domain_data_model_design │  modularization_strategy     privacy_by_design_and_permissions_plan
  backend_and_api_contract │  offline_first_architecture  data_retention_policy_design
                          └─ kotlin_multiplatform_arch    accessibility_and_localization_plan
        │
        ▼
  Design (UI/UX): compose_ui_design_studio
        │
        ▼
  Delivery planning: estimation_and_milestone_plan · learning_roadmap
        │
        ▼
  Scaffolding & AI-agent handoff:
  feature_specification ▶ project_scaffold ▶ ai_context_file_generator ▶ ai_agent_workflow
```

---

## 1. Product & Scope — *what & why*
Define the product, the cut line, and how success is measured before committing engineering effort.

| Prompt | What it produces | Level |
|--------|------------------|-------|
| [`android_app_concept_validation.md`](android_app_concept_validation.md) | Market/technical/competitive/monetization go-no-go verdict | intermediate |
| [`android_mvp_scope_and_release_roadmap.md`](android_mvp_scope_and_release_roadmap.md) | Defended MVP cut line, RICE+MoSCoW backlog, MVP→V1→V2 release train | intermediate |
| [`android_monetization_and_billing_strategy.md`](android_monetization_and_billing_strategy.md) | Monetization model, Play Billing catalog, paywall & entitlement plan | intermediate |
| [`android_analytics_measurement_plan.md`](android_analytics_measurement_plan.md) | North Star metric, funnel, event taxonomy & instrumentation spec | intermediate |
| [`android_device_support_and_form_factor_strategy.md`](android_device_support_and_form_factor_strategy.md) | minSdk/targetSdk decision + phone/tablet/foldable/Wear/TV/Auto/XR matrix | intermediate |

## 2. Architecture & Technical Design — *how it's structured*
Choose the patterns, boundaries, and contracts the codebase will be built on.

| Prompt | What it produces | Level |
|--------|------------------|-------|
| [`android_architecture_selection.md`](android_architecture_selection.md) | MVVM/MVI/Clean/hybrid recommendation + blueprint + migration path | intermediate |
| [`android_tech_stack_selection.md`](android_tech_stack_selection.md) | Justified library stack + version catalog | intermediate |
| [`android_navigation_and_screen_map.md`](android_navigation_and_screen_map.md) | Screen inventory, nav pattern, type-safe routes, deep-link strategy | intermediate |
| [`android_domain_data_model_design.md`](android_domain_data_model_design.md) | Domain/entity model, source-of-truth, storage routing, Room schema shape | advanced |
| [`android_backend_and_api_contract_plan.md`](android_backend_and_api_contract_plan.md) | Backend strategy decision + client API contract + sync model | advanced |
| [`android_module_design.md`](android_module_design.md) | Multi-module structure, boundaries, dependency graph, Gradle config | advanced |
| [`android_modularization_strategy.md`](android_modularization_strategy.md) | Phased extraction plan for an existing monolith + build-time estimate | advanced |
| [`android_offline_first_architecture.md`](android_offline_first_architecture.md) | Offline-first data + sync + conflict-resolution architecture | advanced |
| [`android_kotlin_multiplatform_architecture.md`](android_kotlin_multiplatform_architecture.md) | KMP shared-module architecture and platform boundaries | advanced |

## 3. Quality, Security & Compliance — *the bars, decided up front*
Cross-cutting non-functional requirements are cheaper to design in than to retrofit.

| Prompt | What it produces | Level |
|--------|------------------|-------|
| [`android_performance_budget_and_nfr_plan.md`](android_performance_budget_and_nfr_plan.md) | Quantified startup/frame/size/memory budgets + crash-free/ANR SLOs | advanced |
| [`android_mobile_threat_model.md`](android_mobile_threat_model.md) | Attack surface, STRIDE analysis, secrets/encryption decisions, mitigation backlog | advanced |
| [`android_privacy_by_design_and_permissions_plan.md`](android_privacy_by_design_and_permissions_plan.md) | Data-collection register, least-privilege permissions, Play Data Safety mapping | intermediate |
| [`android_data_retention_policy_design.md`](android_data_retention_policy_design.md) | Retention/deletion policy per data type | intermediate |
| [`android_accessibility_and_localization_plan.md`](android_accessibility_and_localization_plan.md) | WCAG/TalkBack a11y plan + localization/RTL/i18n strategy + QA matrix | intermediate |

## 4. Specialized capabilities

| Prompt | What it produces | Level |
|--------|------------------|-------|
| [`android_ondevice_ai_feature_plan.md`](android_ondevice_ai_feature_plan.md) | On-device-vs-cloud inference decision, runtime selection, responsible-AI guardrails | advanced |

## 5. Design (UI/UX)

| Prompt | What it produces | Level |
|--------|------------------|-------|
| [`android_compose_ui_design_studio.md`](android_compose_ui_design_studio.md) | Interactive, anti-cookie-cutter Compose design system (tokens + reference screen) | advanced |

Hands its locked design system off to [`../implementation/android_compose_screen_builder.md`](../implementation/android_compose_screen_builder.md).

## 6. Delivery & Execution Planning

| Prompt | What it produces | Level |
|--------|------------------|-------|
| [`android_estimation_and_milestone_plan.md`](android_estimation_and_milestone_plan.md) | Work breakdown, risk-adjusted estimates, milestone timeline | intermediate |
| [`android_learning_roadmap.md`](android_learning_roadmap.md) | Personalized, just-in-time Android skill roadmap | intermediate |

## 7. Scaffolding & AI-Agent Handoff — *instantiate & execute*
Once strategy is set, turn decisions into a buildable project and an agent-ready brief.

| Prompt | What it produces | Level |
|--------|------------------|-------|
| [`android_feature_specification.md`](android_feature_specification.md) | Implementation-ready spec for one feature (the planning→build handoff) | intermediate |
| [`android_project_scaffold.md`](android_project_scaffold.md) | Production-ready project scaffold (Gradle, catalog, packages, boilerplate) | intermediate |
| [`android_ai_context_file_generator.md`](android_ai_context_file_generator.md) | `CLAUDE.md`-style AI context/convention file for the project | intermediate |
| [`android_ai_agent_workflow.md`](android_ai_agent_workflow.md) | Playbook for delegating Android work to AI agents + verification gates | intermediate |

---

## Conventions
- **Frontmatter** on every prompt: `title`, `category`, `description`, `techniques` (IDs from [`../../../../techniques/MASTER_TECHNIQUE_INDEX.md`](../../../../techniques/MASTER_TECHNIQUE_INDEX.md)), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Currency:** examples target current Android (Kotlin 2.1+, Jetpack Compose, AGP 8.7+, Hilt, Coroutines/Flow, Room, DataStore, WorkManager, Navigation Compose, Media3). Versions are pulled from the project version catalog rather than hardcoded so guidance does not rot.
- **Structure:** Objective → When to Use → Sequence Map → Context Gathering → phased Instructions with CHECKPOINT gates → Expected Output → Verification → False-Positive Prevention.
- After adding or renaming a prompt here, regenerate the indexes: `python3 ../../../../scripts/generate_prompt_index.py`.
