# iOS Development Prompts

> **Comprehensive prompt library for iOS development with AI coding agents**

This directory contains specialized prompts for iOS application development, organized by workflow phase. Use these prompts with AI coding agents (Claude Code, Cursor, etc.) to plan, analyze, build, test, improve, maintain, and publish iOS applications built with Swift, SwiftUI, and UIKit.

---

## Quick Navigation

| Phase | Description | Start Here |
|-------|-------------|------------|
| [Planning](#planning-prompts) | Validate concepts, select architecture, and scaffold projects | `ios_app_concept_validation.md` |
| [Analysis](#analysis-prompts) | Review and audit existing codebases | `ios_codebase_health_assessment.md` |
| [Implementation](#implementation-prompts) | Build new features and integrations | `ios_swiftui_screen_builder.md` |
| [Testing](#testing-prompts) | Test strategies and generation | `ios_test_strategy_design.md` |
| [Improvement](#improvement-prompts) | Enhance and modernize existing code | `ios_code_modernization.md` |
| [Maintenance](#maintenance-prompts) | Long-term upkeep and updates | `ios_crash_analysis.md` |
| [Publishing](#publishing-prompts) | Release and App Store optimization | `ios_release_preparation.md` |

---

## Planning Prompts

Prompts for validating concepts, designing architecture, selecting technology, and scaffolding iOS projects.

| Prompt | Description | Scope |
|--------|-------------|-------|
| [ios_app_concept_validation.md](planning/ios_app_concept_validation.md) | Validate app concept for market viability and Apple ecosystem fit | Comprehensive |
| [ios_architecture_selection.md](planning/ios_architecture_selection.md) | Guide architecture pattern selection (MVVM, TCA, VIPER, Clean, MV) | Comprehensive |
| [ios_tech_stack_selection.md](planning/ios_tech_stack_selection.md) | Select technology choices (SwiftUI vs UIKit, Core Data vs SwiftData, etc.) | Modular |
| [ios_feature_specification.md](planning/ios_feature_specification.md) | Transform requirements into iOS-specific technical specifications | Comprehensive |
| [ios_module_design.md](planning/ios_module_design.md) | Design multi-module project using Swift Package Manager | Comprehensive |
| [ios_modularization_strategy.md](planning/ios_modularization_strategy.md) | Plan phased modularization of monolithic codebase | Comprehensive |
| [ios_project_scaffold.md](planning/ios_project_scaffold.md) | Generate complete Xcode project structure | Comprehensive |
| [ios_offline_first_architecture.md](planning/ios_offline_first_architecture.md) | Design offline-first architecture with CloudKit sync | Comprehensive |
| [ios_data_retention_policy_design.md](planning/ios_data_retention_policy_design.md) | Design data retention and lifecycle management policy | Modular |
| [ios_learning_roadmap.md](planning/ios_learning_roadmap.md) | Generate personalized iOS development learning roadmap | Comprehensive |
| [ios_claude_md_generator.md](planning/ios_claude_md_generator.md) | Generate CLAUDE.md for iOS/Swift projects | Modular |
| [ios_kotlin_multiplatform_architecture.md](planning/ios_kotlin_multiplatform_architecture.md) | Design iOS-side KMP architecture | Comprehensive |
| [ios_ai_agent_workflow.md](planning/ios_ai_agent_workflow.md) | Configure AI coding agent workflow for iOS development | Modular |

### Recommended Planning Workflow

```
1. Start with App Concept Validation (is this worth building?)
         ↓
2. Select Architecture (MVVM, TCA, VIPER, Clean, MV)
         ↓
3. Choose Tech Stack (SwiftUI vs UIKit, Core Data vs SwiftData, etc.)
         ↓
4. Design Module Structure (Swift Package Manager modules)
         ↓
5. Generate Project Scaffold (create Xcode project)
         ↓
6. Create Feature Specifications (for each feature)
         ↓
7. Configure AI Agent Workflow (optimize development loop)
```

---

## Analysis Prompts

Prompts for reviewing, auditing, and understanding existing iOS codebases.

| Prompt | Description | Scope |
|--------|-------------|-------|
| [ios_codebase_health_assessment.md](analysis/ios_codebase_health_assessment.md) | Holistic assessment of codebase health, structure, and quality | Comprehensive |
| [ios_architecture_review.md](analysis/ios_architecture_review.md) | Deep analysis of architecture patterns and layer boundaries | Comprehensive |
| [ios_performance_audit.md](analysis/ios_performance_audit.md) | Identify performance bottlenecks and optimization opportunities | Comprehensive |
| [ios_technical_debt_assessment.md](analysis/ios_technical_debt_assessment.md) | Catalog and prioritize technical debt with remediation roadmap | Comprehensive |
| [ios_dependency_audit.md](analysis/ios_dependency_audit.md) | Audit third-party dependencies (SPM, CocoaPods, Carthage) | Modular |
| [ios_test_coverage_analysis.md](analysis/ios_test_coverage_analysis.md) | Analyze XCTest/XCUITest coverage and identify gaps | Modular |
| [ios_swiftui_migration_analysis.md](analysis/ios_swiftui_migration_analysis.md) | Assess UIKit-to-SwiftUI migration readiness | Comprehensive |
| [ios_local_data_security_audit.md](analysis/ios_local_data_security_audit.md) | **Security:** Audit local data security (Keychain, Data Protection) | Comprehensive |
| [ios_authentication_security_audit.md](analysis/ios_authentication_security_audit.md) | **Security:** Audit authentication security (Sign in with Apple, biometric) | Comprehensive |
| [ios_cloud_backend_security_audit.md](analysis/ios_cloud_backend_security_audit.md) | **Security:** Audit cloud backend security (CloudKit) | Comprehensive |
| [ios_open_source_license_audit.md](analysis/ios_open_source_license_audit.md) | Audit open source license compliance | Modular |
| [ios_ai_code_review.md](analysis/ios_ai_code_review.md) | AI-assisted code review for Swift/iOS | Modular |

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
         ↓
6. Analyze Test Coverage (identify testing gaps)
```

### Recommended Security Audit Workflow (Pre-Release)

```
1. Local Data Security Audit (Keychain, Data Protection, Core Data)
         ↓
2. Authentication Security Audit (Sign in with Apple, biometric, sessions)
         ↓
3. Cloud Backend Security Audit (CloudKit rules, sync, data integrity)
         ↓
4. Open Source License Audit (compliance verification)
         ↓
5. Privacy Compliance (GDPR, App Tracking Transparency, App Store policies)
         ↓
6. Release Preparation (security hardening, code signing)
```

> **For apps with user accounts and cloud data:** Run all three security audits before publishing. These prompts are designed to catch critical vulnerabilities in authentication, data storage, and cloud integrations that could lead to data breaches or account takeover.

---

## Implementation Prompts

Prompts for building features, integrating services, and writing production code.

| Prompt | Description | Scope |
|--------|-------------|-------|
| [ios_swiftui_screen_builder.md](implementation/ios_swiftui_screen_builder.md) | Build SwiftUI views with proper state management | Comprehensive |
| [ios_data_layer_implementation.md](implementation/ios_data_layer_implementation.md) | Build data layer with Core Data/SwiftData | Comprehensive |
| [ios_api_integration.md](implementation/ios_api_integration.md) | Implement networking with URLSession/async-await | Comprehensive |
| [ios_state_management.md](implementation/ios_state_management.md) | Implement state management (@Observable, Combine) | Comprehensive |
| [ios_navigation_implementation.md](implementation/ios_navigation_implementation.md) | Set up NavigationStack with deep links | Modular |
| [ios_dependency_injection.md](implementation/ios_dependency_injection.md) | Configure dependency injection | Modular |
| [ios_background_tasks.md](implementation/ios_background_tasks.md) | Implement BGTaskScheduler background processing | Modular |
| [ios_offline_first_sync.md](implementation/ios_offline_first_sync.md) | Build offline-first architecture with CloudKit sync | Comprehensive |
| [ios_cloudkit_integration.md](implementation/ios_cloudkit_integration.md) | Integrate CloudKit services | Modular |
| [ios_in_app_purchases.md](implementation/ios_in_app_purchases.md) | Implement StoreKit 2 for purchases and subscriptions | Modular |
| [ios_push_notifications.md](implementation/ios_push_notifications.md) | Implement APNs push notifications | Modular |
| [ios_widgets_app_intents.md](implementation/ios_widgets_app_intents.md) | Build WidgetKit/App Intents/Live Activities | Modular |
| [ios_app_clips.md](implementation/ios_app_clips.md) | Implement App Clips | Modular |
| [ios_swiftui_state_patterns.md](implementation/ios_swiftui_state_patterns.md) | Advanced SwiftUI state patterns | Comprehensive |

### Recommended Implementation Workflow

```
1. Configure Dependency Injection (foundation for all components)
         ↓
2. Implement Data Layer (Core Data/SwiftData, repositories)
         ↓
3. Add API Integration (URLSession, async/await networking)
         ↓
4. Set up State Management (@Observable, Combine)
         ↓
5. Build SwiftUI Screens (UI layer)
         ↓
6. Set up Navigation (NavigationStack, deep links)
         ↓
7. Add Background Tasks (BGTaskScheduler, sync)
         ↓
8. Integrate Platform Features (widgets, notifications, App Clips)
```

---

## Testing Prompts

Prompts for test strategy design, test generation, and quality assurance.

| Prompt | Description | Scope |
|--------|-------------|-------|
| [ios_test_strategy_design.md](testing/ios_test_strategy_design.md) | Design comprehensive test strategy tailored to project architecture and risk profile | Comprehensive |
| [ios_unit_test_generation.md](testing/ios_unit_test_generation.md) | Generate XCTest unit tests for ViewModels, Use Cases, and Repositories | Modular |
| [ios_ui_test_generation.md](testing/ios_ui_test_generation.md) | Implement XCUITest UI tests for critical user flows | Modular |
| [ios_integration_testing.md](testing/ios_integration_testing.md) | Integration tests for Core Data/network layers | Modular |
| [ios_snapshot_testing.md](testing/ios_snapshot_testing.md) | Visual regression testing with swift-snapshot-testing | Modular |
| [ios_performance_testing.md](testing/ios_performance_testing.md) | XCTest performance tests for critical paths | Modular |
| [ios_ai_test_generation.md](testing/ios_ai_test_generation.md) | AI-assisted test generation for Swift/iOS | Modular |

### Recommended Testing Workflow

```
1. Design Test Strategy (understand what needs testing)
         ↓
2. Generate Unit Tests (cover business logic first)
         ↓
3. Add Integration Tests (verify Core Data/network integration)
         ↓
4. Implement UI Tests (protect critical user flows)
         ↓
5. Set Up Snapshot Tests (catch visual regressions)
         ↓
6. Add Performance Tests (guard against regressions)
```

---

## Improvement Prompts

Prompts for enhancing, modernizing, and polishing existing iOS code.

| Prompt | Description | Scope |
|--------|-------------|-------|
| [ios_code_modernization.md](improvement/ios_code_modernization.md) | Modernize to Swift 6 and current best practices | Comprehensive |
| [ios_memory_leak_detection.md](improvement/ios_memory_leak_detection.md) | Identify and fix retain cycles and memory leaks | Comprehensive |
| [ios_startup_optimization.md](improvement/ios_startup_optimization.md) | Optimize app launch time | Modular |
| [ios_error_handling_improvement.md](improvement/ios_error_handling_improvement.md) | Improve error handling with typed throws | Modular |
| [ios_ui_polish_audit.md](improvement/ios_ui_polish_audit.md) | Audit UI polish and animation smoothness | Comprehensive |
| [ios_accessibility_improvement.md](improvement/ios_accessibility_improvement.md) | VoiceOver and Dynamic Type improvements | Comprehensive |
| [ios_user_experience_enhancement.md](improvement/ios_user_experience_enhancement.md) | HIG-compliant UX improvements | Comprehensive |
| [ios_swiftui_migration.md](improvement/ios_swiftui_migration.md) | Incremental UIKit-to-SwiftUI migration | Comprehensive |
| [ios_swift_concurrency_adoption.md](improvement/ios_swift_concurrency_adoption.md) | Adopt Swift Concurrency throughout codebase | Comprehensive |
| [ios_hig_compliance_review.md](improvement/ios_hig_compliance_review.md) | Human Interface Guidelines compliance review | Comprehensive |
| [ios_battery_energy_optimization.md](improvement/ios_battery_energy_optimization.md) | Reduce energy impact and battery drain | Modular |
| [ios_app_size_optimization.md](improvement/ios_app_size_optimization.md) | Reduce IPA size and optimize assets | Modular |

### Recommended Improvement Workflow

```
1. Run Code Modernization (update to Swift 6, current APIs)
         ↓
2. Adopt Swift Concurrency (async/await, actors, Sendable)
         ↓
3. Fix Memory Leaks (stability first)
         ↓
4. Optimize Startup Time (user-perceived performance)
         ↓
5. Improve Error Handling (typed throws, resilience)
         ↓
6. Migrate to SwiftUI (incremental UIKit replacement)
         ↓
7. Review HIG Compliance (platform consistency)
         ↓
8. Polish UI, Accessibility, and UX (final refinement)
         ↓
9. Optimize Battery and App Size (efficiency)
```

---

## Maintenance Prompts

Prompts for crash analysis, dependency updates, SDK upgrades, and long-term maintenance.

| Prompt | Description | Scope |
|--------|-------------|-------|
| [ios_crash_analysis.md](maintenance/ios_crash_analysis.md) | Analyze crash reports from Xcode Organizer | Comprehensive |
| [ios_dependency_update.md](maintenance/ios_dependency_update.md) | Safely update SPM/CocoaPods dependencies | Comprehensive |
| [ios_version_upgrade.md](maintenance/ios_version_upgrade.md) | Upgrade to new iOS deployment target | Comprehensive |
| [ios_swift_version_migration.md](maintenance/ios_swift_version_migration.md) | Migrate to new Swift version (5 to 6) | Comprehensive |
| [ios_user_feedback_analysis.md](maintenance/ios_user_feedback_analysis.md) | Analyze App Store reviews and feedback | Modular |
| [ios_tech_debt_triage.md](maintenance/ios_tech_debt_triage.md) | Triage and prioritize tech debt | Modular |
| [ios_performance_regression_detective.md](maintenance/ios_performance_regression_detective.md) | Investigate performance regressions | Comprehensive |
| [ios_xcode_build_optimization.md](maintenance/ios_xcode_build_optimization.md) | Optimize Xcode build times | Modular |
| [ios_certificate_provisioning_management.md](maintenance/ios_certificate_provisioning_management.md) | Manage code signing and provisioning profiles | Modular |
| [ios_deprecation_audit.md](maintenance/ios_deprecation_audit.md) | Audit deprecated Apple APIs and plan replacements | Modular |

### Recommended Maintenance Workflow

```
1. Analyze User Feedback (understand user pain points)
         ↓
2. Analyze Crashes (fix stability issues first)
         ↓
3. Triage Tech Debt (prioritize what to address)
         ↓
4. Investigate Performance Regressions (if metrics degraded)
         ↓
5. Update Dependencies (security and compatibility)
         ↓
6. Upgrade iOS Deployment Target (meet App Store requirements)
         ↓
7. Migrate Swift Version (adopt new language features)
         ↓
8. Audit Deprecated APIs (replace before removal)
         ↓
9. Optimize Xcode Build Times (developer productivity)
         ↓
10. Manage Certificates and Provisioning (avoid expiration)
```

---

## Publishing Prompts

Prompts for release preparation, App Store optimization, privacy compliance, and rollout strategies.

| Prompt | Description | Scope |
|--------|-------------|-------|
| [ios_release_preparation.md](publishing/ios_release_preparation.md) | Prepare app for production release | Comprehensive |
| [ios_privacy_compliance.md](publishing/ios_privacy_compliance.md) | App Store privacy requirements audit | Comprehensive |
| [ios_app_store_optimization.md](publishing/ios_app_store_optimization.md) | App Store Optimization (ASO) for discoverability | Comprehensive |
| [ios_app_thinning_optimization.md](publishing/ios_app_thinning_optimization.md) | App Thinning optimization (slicing, bitcode, ODR) | Modular |
| [ios_testflight_rollout.md](publishing/ios_testflight_rollout.md) | TestFlight beta testing and phased release strategy | Modular |
| [ios_privacy_labels_generator.md](publishing/ios_privacy_labels_generator.md) | Generate App Store privacy nutrition labels | Modular |
| [ios_app_review_guidelines_check.md](publishing/ios_app_review_guidelines_check.md) | Pre-submission App Review Guidelines audit | Comprehensive |
| [ios_app_store_review_response.md](publishing/ios_app_store_review_response.md) | Respond to App Store reviews professionally | Modular |
| [ios_screenshot_strategy.md](publishing/ios_screenshot_strategy.md) | App Store screenshot and preview strategy | Modular |
| [ios_pre_submission_checklist.md](publishing/ios_pre_submission_checklist.md) | Final pre-submission checklist | Comprehensive |
| [ios_privacy_policy_generator.md](publishing/ios_privacy_policy_generator.md) | Generate privacy policy for App Store submission | Modular |
| [ios_terms_of_service_generator.md](publishing/ios_terms_of_service_generator.md) | Generate terms of service | Modular |
| [ios_gdpr_compliance_audit.md](publishing/ios_gdpr_compliance_audit.md) | GDPR compliance audit | Comprehensive |
| [ios_release_management.md](publishing/ios_release_management.md) | App Store release lifecycle management | Comprehensive |

### Recommended Publishing Workflow

```
1. Run Release Preparation (build config, signing, hardening)
         ↓
2. Complete Privacy Compliance (App Tracking Transparency, data handling)
         ↓
3. Generate Privacy Labels (nutrition labels for App Store)
         ↓
4. Generate Privacy Policy and Terms of Service
         ↓
5. Run GDPR Compliance Audit (if serving EU users)
         ↓
6. Check App Review Guidelines (avoid rejection)
         ↓
7. Run Pre-Submission Checklist (final verification)
         ↓
8. Optimize App Thinning (reduce download size)
         ↓
9. Optimize App Store Listing (ASO)
         ↓
10. Plan Screenshot Strategy (maximize conversion)
         ↓
11. Plan TestFlight Rollout (beta → phased release)
         ↓
12. Manage Release Lifecycle (post-launch monitoring)
```

---

## How to Use These Prompts

### Basic Usage

1. Copy the prompt content into your AI coding agent
2. Provide your codebase context (repository path, specific files, or paste code)
3. Follow the interactive checkpoint process
4. Review findings before approving changes

### Tips for Best Results

- **Provide Context**: The more context you provide about your app (category, architecture, constraints), the better the analysis
- **Follow Checkpoints**: These prompts are designed with interactive checkpoints -- don't skip them
- **Iterate**: Use findings from one prompt to inform which prompt to run next
- **Combine Prompts**: Run multiple related prompts for comprehensive coverage

### Scope Guide

| Scope | Line Count | Best For |
|-------|-----------|----------|
| **Comprehensive** | 200-500 lines | Complex analysis, multi-dimensional review, architecture decisions |
| **Modular** | 80-150 lines | Focused tasks, single-concern implementations, specific fixes |

---

## Related Resources

- [ios/targeted-reviews/](../ios/targeted-reviews/) - Targeted review prompts for iOS-specific concerns
- [cross-platform/migration/](../cross-platform/migration/) - Cross-platform migration prompts (KMP, Flutter, React Native)
- [android/](../android/) - Android development prompts (parallel structure)
- [MASTER_TECHNIQUE_INDEX.md](../../../techniques/MASTER_TECHNIQUE_INDEX.md) - Prompt engineering techniques used
- [USE_CASE_LOOKUP.md](../../../techniques/USE_CASE_LOOKUP.md) - Use case patterns for prompt selection

---

*Last Updated: March 2026 | Total: 82 prompts (Planning: 13, Analysis: 12, Implementation: 14, Testing: 7, Improvement: 12, Maintenance: 10, Publishing: 14)*
