# Android Development Prompts

> **Comprehensive prompt library for Android development with AI coding agents**

This directory contains specialized prompts for Android application development, organized by workflow phase. Use these prompts with AI coding agents (Claude Code, Cursor, etc.) to analyze, improve, build, test, and maintain Android applications.

---

## Quick Navigation

| Phase | Description | Start Here |
|-------|-------------|------------|
| [Analysis](#analysis-prompts) | Review and audit existing codebases | `android_codebase_health_assessment.md` |
| [Improvement](#improvement-prompts) | Enhance and modernize existing code | `android_code_modernization.md` |
| [Planning](#planning-prompts) | Design features and architecture | `android_feature_specification.md` |
| [Implementation](#implementation-prompts) | Build new features and integrations | Coming Soon |
| [Testing](#testing-prompts) | Test strategies and generation | `android_test_strategy_design.md` |
| [Implementation](#implementation-prompts) | Build new features and integrations | `android_data_layer_implementation.md` |
| [Testing](#testing-prompts) | Test strategies and generation | Coming Soon |
| [Publishing](#publishing-prompts) | Release and store optimization | `android_release_preparation.md` |
| [Maintenance](#maintenance-prompts) | Long-term upkeep and updates | `android_crash_analysis.md` |

---

## Analysis Prompts

Prompts for reviewing, auditing, and understanding existing Android codebases (30 prompts). See [analysis/README.md](analysis/README.md) for the full catalog, the analysis-vs-targeted-reviews distinction, and detailed workflows.

**Architecture & Code Quality**

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_codebase_health_assessment.md](analysis/android_codebase_health_assessment.md) | Holistic codebase health and roadmap — **start here** | Comprehensive |
| [android_architecture_review.md](analysis/android_architecture_review.md) | Architecture patterns, layer boundaries, dependency flow | Comprehensive |
| [android_module_graph_analysis.md](analysis/android_module_graph_analysis.md) | Multi-module coupling, layering, god-modules | Comprehensive |
| [android_kotlin_best_practices.md](analysis/android_kotlin_best_practices.md) | Modern architecture, Jetpack, Kotlin usage | Comprehensive |
| [ai_code_review_android.md](analysis/ai_code_review_android.md) | PR/pre-merge review checklist (7 categories) | Modular |
| [android_kotlin_compose_debugging_audit.md](analysis/android_kotlin_compose_debugging_audit.md) | Crash/defect patterns (null-safety, recomposition, coroutines) | Comprehensive |
| [android_technical_debt_assessment.md](analysis/android_technical_debt_assessment.md) | Catalog and prioritize technical debt | Comprehensive |
| [android_hilt_dagger_analysis.md](analysis/android_hilt_dagger_analysis.md) | Hilt/Dagger DI configuration and scopes | Comprehensive |

**Security & Privacy**

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_authentication_security_audit.md](analysis/android_authentication_security_audit.md) | **Security:** Auth flows, 2FA, sessions | Comprehensive |
| [android_local_data_security_audit.md](analysis/android_local_data_security_audit.md) | **Security:** At-rest storage, encryption, Keystore | Comprehensive |
| [android_cloud_backend_security_audit.md](analysis/android_cloud_backend_security_audit.md) | **Security:** Cloud rules, functions, sync, storage | Comprehensive |
| [android_manifest_permissions_audit.md](analysis/android_manifest_permissions_audit.md) | **Security:** Permissions, exported components, manifest flags | Comprehensive |
| [android_privacy_data_flow_audit.md](analysis/android_privacy_data_flow_audit.md) | **Privacy:** PII flows, third-party SDK sharing, Data Safety | Comprehensive |

**UI, Compose & Accessibility**

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_compose_ui_analysis.md](analysis/android_compose_ui_analysis.md) | UI consistency, quality, appeal, competitiveness | Comprehensive |
| [android_compose_ui_consistency_audit.md](analysis/android_compose_ui_consistency_audit.md) | Typography/size/spacing + cross-theme invariance | Comprehensive |
| [android_compose_migration_analysis.md](analysis/android_compose_migration_analysis.md) | XML→Compose migration readiness | Comprehensive |
| [android_theme_investigation.md](analysis/android_theme_investigation.md) | Theme architecture + persistent styling root cause | Comprehensive |
| [android_accessibility_audit.md](analysis/android_accessibility_audit.md) | TalkBack, contrast, touch targets, dynamic type, RTL | Modular |
| [android_localization_i18n_readiness_audit.md](analysis/android_localization_i18n_readiness_audit.md) | Hardcoded strings, plurals, locale formatting, RTL | Modular |

**Performance & Resources**

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_performance_audit.md](analysis/android_performance_audit.md) | Startup, UI, memory, network, DB, background work | Comprehensive |
| [android_battery_drain_investigation.md](analysis/android_battery_drain_investigation.md) | 10-dimension battery consumption analysis | Comprehensive |
| [android_concurrency_threading_analysis.md](analysis/android_concurrency_threading_analysis.md) | Coroutine/Flow/dispatcher model, races, main-safety | Comprehensive |
| [android_resource_asset_analysis.md](analysis/android_resource_asset_analysis.md) | Resource hygiene, image formats, resource-driven size | Modular |

**Data, Networking & Build**

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_networking_layer_analysis.md](analysis/android_networking_layer_analysis.md) | Retrofit/OkHttp/Ktor config, retries, caching, TLS | Comprehensive |
| [android_data_layer_persistence_analysis.md](analysis/android_data_layer_persistence_analysis.md) | Room/DataStore/prefs, migrations, source-of-truth | Comprehensive |
| [android_navigation_deeplink_analysis.md](analysis/android_navigation_deeplink_analysis.md) | Nav graph, back-stack, deep-link coverage/security | Comprehensive |
| [android_dependency_audit.md](analysis/android_dependency_audit.md) | Dependency versions, vulnerabilities, safe updates | Modular |
| [android_build_gradle_health_analysis.md](analysis/android_build_gradle_health_analysis.md) | Version catalogs, convention plugins, build performance | Comprehensive |
| [android_open_source_license_audit.md](analysis/android_open_source_license_audit.md) | License inventory, copyleft, attribution | Modular |
| [android_test_coverage_analysis.md](analysis/android_test_coverage_analysis.md) | Test coverage gaps and suite quality | Modular |

### Recommended Analysis Workflow

```
1. Start with Codebase Health Assessment (overall picture)
         ↓
2. Deep dive into Architecture Review (if structural issues found)
         ↓
3. Run Performance Audit (if performance concerns)
         ↓
4. Assess Technical Debt (prioritize improvements)
         ↓
5. Audit Dependencies (before major updates)
```

### Recommended Security Audit Workflow (Pre-Release)

```
1. Local Data Security Audit (databases, storage, keystore)
         ↓
2. Authentication Security Audit (auth flows, 2FA, sessions)
         ↓
3. Cloud Backend Security Audit (Firebase rules, functions, sync)
         ↓
4. Privacy Compliance (GDPR, CCPA, Play Store policies)
         ↓
5. Release Preparation (security hardening, ProGuard)
```

> **For apps with user accounts and cloud data:** Run all three security audits before publishing. These prompts are designed to catch critical vulnerabilities in authentication, data storage, and cloud integrations that could lead to data breaches or account takeover.

---

## Improvement Prompts

Prompts for enhancing, modernizing, and polishing existing Android code.

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_code_modernization.md](improvement/android_code_modernization.md) | Systematically modernize to current best practices | Comprehensive |
| [android_memory_leak_detection.md](improvement/android_memory_leak_detection.md) | Identify and fix memory leaks through static analysis | Comprehensive |
| [android_startup_optimization.md](improvement/android_startup_optimization.md) | Optimize app cold start time | Modular |
| [android_error_handling_improvement.md](improvement/android_error_handling_improvement.md) | Improve error handling patterns throughout codebase | Modular |
| [android_ui_polish_audit.md](improvement/android_ui_polish_audit.md) | Audit UI for consistency, polish, and professional feel | Comprehensive |
| [android_accessibility_improvement.md](improvement/android_accessibility_improvement.md) | Audit and improve app accessibility | Comprehensive |
| [android_user_experience_enhancement.md](improvement/android_user_experience_enhancement.md) | Identify and implement UX improvements | Comprehensive |

### Recommended Improvement Workflow

```
1. Run Code Modernization (update patterns and APIs)
         ↓
2. Fix Memory Leaks (stability first)
         ↓
3. Optimize Startup (user-perceived performance)
         ↓
4. Improve Error Handling (resilience)
         ↓
5. Polish UI and UX (final refinement)
```

---

## Planning Prompts

Prompts for designing features, selecting architecture, and planning projects.

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_feature_specification.md](planning/android_feature_specification.md) | Transform requirements into detailed technical specifications | Comprehensive |
| [android_architecture_selection.md](planning/android_architecture_selection.md) | Guide selection of optimal architecture pattern (MVVM, MVI, Clean) | Comprehensive |
| [android_module_design.md](planning/android_module_design.md) | Design multi-module architecture for scalability | Comprehensive |
| [android_tech_stack_selection.md](planning/android_tech_stack_selection.md) | Select and justify technology choices for new projects | Modular |
| [android_app_concept_validation.md](planning/android_app_concept_validation.md) | Validate app ideas for market viability and feasibility | Comprehensive |
| [android_project_scaffold.md](planning/android_project_scaffold.md) | Generate complete project structure with boilerplate | Comprehensive |

### Recommended Planning Workflow

```
1. Start with App Concept Validation (is this worth building?)
         ↓
2. Select Architecture (MVVM, MVI, Clean Architecture)
         ↓
3. Choose Tech Stack (libraries and frameworks)
         ↓
4. Design Module Structure (if multi-module needed)
         ↓
5. Generate Project Scaffold (create initial project)
         ↓
6. Create Feature Specifications (for each feature)
```

---

## Implementation Prompts

Prompts for building features, integrating services, and writing production code.

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_data_layer_implementation.md](implementation/android_data_layer_implementation.md) | Build data layer with Room, Repository pattern, and data sources | Comprehensive |
| [android_api_integration.md](implementation/android_api_integration.md) | Implement REST API integration with Retrofit and error handling | Comprehensive |
| [android_state_management.md](implementation/android_state_management.md) | Implement UI state management with ViewModel and StateFlow | Comprehensive |
| [android_navigation_implementation.md](implementation/android_navigation_implementation.md) | Set up type-safe Compose Navigation with deep links | Modular |
| [android_dependency_injection.md](implementation/android_dependency_injection.md) | Configure Hilt dependency injection with proper scoping | Modular |
| [android_compose_screen_builder.md](implementation/android_compose_screen_builder.md) | Build production-ready Compose screens with Material 3 | Comprehensive |
| [android_background_work.md](implementation/android_background_work.md) | Implement background processing with WorkManager | Modular |
| [android_offline_first_sync.md](implementation/android_offline_first_sync.md) | Build offline-first architecture with sync capabilities | Comprehensive |
| [android_firebase_integration.md](implementation/android_firebase_integration.md) | Integrate Firebase services (Auth, Firestore, FCM) | Modular |
| [android_in_app_billing.md](implementation/android_in_app_billing.md) | Implement Google Play Billing for purchases and subscriptions | Modular |

### Recommended Implementation Workflow

```
1. Set up Dependency Injection (foundation for all components)
         ↓
2. Implement Data Layer (Room, repositories)
         ↓
3. Add API Integration (network layer)
         ↓
4. Configure State Management (ViewModels)
         ↓
5. Build Compose Screens (UI layer)
         ↓
6. Set up Navigation (connect screens)
         ↓
7. Add Background Work (sync, uploads)
```

---

## Testing Prompts

Prompts for test strategy design, test generation, and quality assurance.

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_test_strategy_design.md](testing/android_test_strategy_design.md) | Design comprehensive test strategy tailored to project architecture and risk profile | Comprehensive |
| [android_unit_test_generation.md](testing/android_unit_test_generation.md) | Generate unit tests for ViewModels, Use Cases, Repositories, and utilities | Modular |
| [android_compose_ui_testing.md](testing/android_compose_ui_testing.md) | Implement Compose UI tests for screens, components, and navigation | Modular |
| [android_integration_testing.md](testing/android_integration_testing.md) | Implement integration tests for database, API, and repository layers | Modular |
| [android_screenshot_testing.md](testing/android_screenshot_testing.md) | Set up screenshot/visual regression testing with Paparazzi or Roborazzi | Modular |
| [android_test_flakiness_triage_quarantine.md](testing/android_test_flakiness_triage_quarantine.md) | Triage flaky tests, quarantine safely, and run structured deflake recovery | Modular |
| [android_ci_test_pipeline_optimization.md](testing/android_ci_test_pipeline_optimization.md) | Optimize CI test stages, sharding, caching, and risk-based gates | Modular |
| [android_device_api_test_matrix_design.md](testing/android_device_api_test_matrix_design.md) | Design risk-based device/API-level matrix for PR, nightly, and pre-release runs | Modular |
| [android_contract_testing_network_data_boundaries.md](testing/android_contract_testing_network_data_boundaries.md) | Define and enforce contracts across API, mapping, and persistence boundaries | Modular |
| [android_mutation_testing_effectiveness_review.md](testing/android_mutation_testing_effectiveness_review.md) | Measure test effectiveness using mutation testing and escaped-defect signals | Modular |

### Recommended Testing Workflow

```
1. Design Test Strategy (scope risks and quality goals)
         ↓
2. Design Device/API Matrix (decide PR vs nightly vs pre-release coverage)
         ↓
3. Optimize CI Pipeline (fast lane vs confidence lane + quality gates)
         ↓
4. Generate Unit Tests (cover business logic first)
         ↓
5. Add Integration + Contract Tests (verify boundaries and component integration)
         ↓
6. Implement UI Tests (protect critical user flows)
         ↓
7. Set Up Screenshot Tests (catch visual regressions)
         ↓
8. Run Flakiness Triage + Quarantine (stabilize signal without hiding risk)
         ↓
9. Review Test Effectiveness with Mutation Testing (improve defect detection power)
         ↓
10. Feed readiness status into Play Store pre-launch checklist before release
```

---

## Publishing Prompts

Prompts for release preparation, store optimization, privacy compliance, and rollout strategies.

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_release_governance_runbook.md](publishing/android_release_governance_runbook.md) | End-to-end publishing governance flow from compliance to incident response | Comprehensive |
| [android_release_preparation.md](publishing/android_release_preparation.md) | Prepare app for production release with signing, versioning, and security hardening | Comprehensive |
| [android_privacy_compliance.md](publishing/android_privacy_compliance.md) | Audit for GDPR, CCPA, and Play Store privacy compliance | Comprehensive |
| [android_play_store_optimization.md](publishing/android_play_store_optimization.md) | App Store Optimization (ASO) for better discoverability and conversion | Comprehensive |
| [android_app_bundle_optimization.md](publishing/android_app_bundle_optimization.md) | Reduce app download and install size | Modular |
| [android_staged_rollout.md](publishing/android_staged_rollout.md) | Beta testing and staged rollout strategy | Modular |

### Recommended Publishing Workflow

```
1. Run Privacy Compliance Audit (policy, data handling, disclosures)
         ↓
2. Generate Data Safety Artifacts (Play Console-ready declarations)
         ↓
3. Prepare Listing Assets (screenshots, descriptions, legal links)
         ↓
4. Execute Pre-Launch Checks (release build, policy, pre-launch report)
         ↓
5. Run Staged Rollout Plan (risk-gated promotion to 100%)
         ↓
6. Operate Review-Response and Incident Loop (monitor, respond, improve)
```

---

## Maintenance Prompts

Prompts for crash/ANR analysis, the incident lifecycle, dependency/SDK/toolchain upgrades, debt paydown, and long-term reliability. **See the [maintenance/ local index](maintenance/README.md) for clusters, prompt chains, and cadence.**

**Stability — crashes, ANRs, regressions**

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_crash_analysis.md](maintenance/android_crash_analysis.md) | Analyze crash reports, identify root causes, and implement fixes | Comprehensive |
| [android_anr_vitals_analysis.md](maintenance/android_anr_vitals_analysis.md) | Diagnose ANRs against Play Vitals thresholds (main-thread blocking, lock contention) | Comprehensive |
| [android_performance_regression_detective.md](maintenance/android_performance_regression_detective.md) | Detect, bisect, and verify performance regressions | Comprehensive |

**Incident lifecycle — triage, respond, learn**

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_incident_triage_and_severity_classification.md](maintenance/android_incident_triage_and_severity_classification.md) | Triage production incidents and assign consistent severity | Modular |
| [android_on_call_runbook_generator.md](maintenance/android_on_call_runbook_generator.md) | Generate per-failure-mode on-call runbooks (detect → mitigate → escalate) | Comprehensive |
| [android_postmortem_and_corrective_action_planning.md](maintenance/android_postmortem_and_corrective_action_planning.md) | Build blameless postmortems with prioritized corrective actions | Comprehensive |
| [android_regression_prevention_checklist_after_hotfixes.md](maintenance/android_regression_prevention_checklist_after_hotfixes.md) | Prevent secondary regressions after emergency fixes | Modular |
| [android_observability_logging_quality_review.md](maintenance/android_observability_logging_quality_review.md) | Audit logging, metrics, and trace quality for incident readiness | Comprehensive |
| [android_reliability_slo_error_budget_review.md](maintenance/android_reliability_slo_error_budget_review.md) | Define reliability SLOs + error-budget policy that gates releases | Modular |

**Dependencies, SDKs & toolchain**

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_dependency_audit.md](maintenance/android_dependency_audit.md) | Comprehensive CVE + abandonment-risk audit with multi-sprint paydown plan | Comprehensive |
| [android_dependency_update.md](maintenance/android_dependency_update.md) | Safely apply dependency updates with compatibility analysis and migration | Comprehensive |
| [android_third_party_sdk_upgrade_review.md](maintenance/android_third_party_sdk_upgrade_review.md) | Review data-collecting SDK upgrades (Firebase, ads, analytics) for behavior/privacy/consent | Modular |
| [android_build_toolchain_upgrade.md](maintenance/android_build_toolchain_upgrade.md) | Coordinated AGP/Gradle/Kotlin/JDK/KSP upgrade with compatibility matrix | Comprehensive |
| [android_target_sdk_migration.md](maintenance/android_target_sdk_migration.md) | **Plan** the annual targetSdk bump — behavior-change mapping + deadline tracking | Comprehensive |
| [android_version_upgrade.md](maintenance/android_version_upgrade.md) | **Execute** the targetSdk upgrade — apply, test, roll out | Comprehensive |
| [android_sdk_migration.md](maintenance/android_sdk_migration.md) | Migrate from deprecated APIs to modern replacements (AsyncTask→Coroutines, etc.) | Comprehensive |
| [android_min_sdk_raise_planner.md](maintenance/android_min_sdk_raise_planner.md) | Plan raising minSdk — user-reach trade-off + removable compat shims | Modular |

**Code health, debt & product signal**

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_tech_debt_triage.md](maintenance/android_tech_debt_triage.md) | Inventory, score, and schedule tech-debt paydown (interest model) | Comprehensive |
| [android_feature_flag_lifecycle_cleanup.md](maintenance/android_feature_flag_lifecycle_cleanup.md) | Inventory flags/Remote Config, classify, retire dead branches safely | Modular |
| [android_proguard_r8_optimization.md](maintenance/android_proguard_r8_optimization.md) | Audit/optimize R8 keep rules, shrinking, full-mode migration | Comprehensive |
| [android_user_feedback_analysis.md](maintenance/android_user_feedback_analysis.md) | Analyze user feedback and translate insights into development tasks | Modular |

### Recommended Maintenance Workflow

```
1. Analyze User Feedback (understand user pain points)
         ↓
2. Analyze Crashes (fix stability issues first)
         ↓
3. Update Dependencies (security and compatibility)
         ↓
4. Upgrade targetSdk (meet Play Store requirements)
         ↓
5. Migrate Deprecated APIs (modernize codebase)
         ↓
6. Monitor and Iterate (ongoing maintenance)
```

---

## Legacy Prompts (In Parent Directory)

The following prompts exist in the parent `mobile-development/` directory and may be migrated here in future updates:

| Legacy Prompt | Recommended Migration |
|--------------|----------------------|
| `android_battery_drain_investigation.md` | → `android/analysis/` |
| `android_compose_ui_analysis.md` | → `android/analysis/` |
| `android_compose_ui_improvement.md` | → `android/improvement/` |
| `android_compose_ui_polish.md` | → `android/improvement/` |
| `android_kotlin_best_practices.md` | → `android/analysis/` |
| `android_kotlin_refactoring.md` | → `android/improvement/` |

---


## Maintenance Cadence

Use this recurring routine to keep Android reliability healthy between major projects:

### Weekly Reliability Routine

- Review new crash/ANR clusters and run [android_incident_triage_and_severity_classification.md](maintenance/android_incident_triage_and_severity_classification.md) for emerging patterns.
- Spot-check hot paths with [android_performance_audit.md](analysis/android_performance_audit.md) sections relevant to startup, jank, and battery.
- Run focused diagnostics where risk is highest:
  - [android_workmanager_background_review.md](targeted-reviews/android_workmanager_background_review.md)
  - [android_process_death_recovery_review.md](targeted-reviews/android_process_death_recovery_review.md)
  - [android_silent_data_loss_detection.md](targeted-reviews/android_silent_data_loss_detection.md)

### Pre-Release Routine

- Re-run high-risk maintenance prompts:
  - [android_observability_logging_quality_review.md](maintenance/android_observability_logging_quality_review.md)
  - [android_crash_analysis.md](maintenance/android_crash_analysis.md)
  - [android_performance_regression_detective.md](maintenance/android_performance_regression_detective.md)
- Confirm rollout safety and rollback readiness with [android_staged_rollout.md](publishing/android_staged_rollout.md).

### Post-Incident Routine

- Perform immediate triage using [android_incident_triage_and_severity_classification.md](maintenance/android_incident_triage_and_severity_classification.md).
- Create a formal retrospective via [android_postmortem_and_corrective_action_planning.md](maintenance/android_postmortem_and_corrective_action_planning.md).
- Before normal release cadence resumes, complete [android_regression_prevention_checklist_after_hotfixes.md](maintenance/android_regression_prevention_checklist_after_hotfixes.md).

## How to Use These Prompts

### Basic Usage

1. Copy the prompt content into your AI coding agent
2. Provide your codebase context (repository path, specific files, or paste code)
3. Follow the interactive checkpoint process
4. Review findings before approving changes

### Tips for Best Results

- **Provide Context**: The more context you provide about your app (category, architecture, constraints), the better the analysis
- **Follow Checkpoints**: These prompts are designed with interactive checkpoints—don't skip them
- **Iterate**: Use findings from one prompt to inform which prompt to run next
- **Combine Prompts**: Run multiple related prompts for comprehensive coverage

### Scope Guide

| Scope | Line Count | Best For |
|-------|-----------|----------|
| **Comprehensive** | 200-500 lines | Complex analysis, multi-dimensional review, architecture decisions |
| **Modular** | 80-150 lines | Focused tasks, single-concern implementations, specific fixes |

---

## Related Resources

- [analysis/README.md](analysis/README.md) - Full Android analysis prompt catalog and workflows
- [MASTER_TECHNIQUE_INDEX.md](../../../techniques/MASTER_TECHNIQUE_INDEX.md) - Prompt engineering techniques used
- [CONTRIBUTING.md](../../../CONTRIBUTING.md) - How to contribute new prompts

---

*Last Updated: 2026-06-06 | Maintenance phase expanded to 21 prompts (see [maintenance/README.md](maintenance/README.md)); Analysis phase expanded to 30 codebase-wide prompts (see [analysis/README.md](analysis/README.md)).*
