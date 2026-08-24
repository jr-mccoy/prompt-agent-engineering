# Android Maintenance Prompts

> **Long-term upkeep, reliability, and the incident lifecycle for production Android apps.**

These prompts cover the work that keeps a shipped Android app healthy: diagnosing crashes and ANRs, running the incident lifecycle (triage → respond → postmortem), keeping dependencies/SDKs/toolchain current, paying down debt, and turning telemetry into release control.

Pair them with the [`../analysis/`](../analysis/) prompts (read-only audits), [`../targeted-reviews/`](../targeted-reviews/) (single-failure-mode deep dives), and [`../publishing/`](../publishing/) (release + rollout).

---

## Prompts by Cluster

### Stability — Crashes, ANRs, Regressions

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_crash_analysis.md](android_crash_analysis.md) | Analyze crash reports/stack traces, find root causes, implement fixes | Comprehensive |
| [android_anr_vitals_analysis.md](android_anr_vitals_analysis.md) | Diagnose ANRs against Play Vitals thresholds — main-thread blocking, lock contention, slow binder | Comprehensive |
| [android_performance_regression_detective.md](android_performance_regression_detective.md) | Detect, bisect, and verify performance regressions via Vitals + Macrobenchmark | Comprehensive |

### Incident Lifecycle — Triage, Respond, Learn

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_incident_triage_and_severity_classification.md](android_incident_triage_and_severity_classification.md) | Triage live incidents, assign SEV, drive first response | Modular |
| [android_on_call_runbook_generator.md](android_on_call_runbook_generator.md) | Generate per-failure-mode on-call runbooks (detection → mitigate → escalate) | Comprehensive |
| [android_postmortem_and_corrective_action_planning.md](android_postmortem_and_corrective_action_planning.md) | Blameless postmortem + prioritized corrective actions | Comprehensive |
| [android_regression_prevention_checklist_after_hotfixes.md](android_regression_prevention_checklist_after_hotfixes.md) | Prevent secondary regressions after emergency fixes | Modular |
| [android_observability_logging_quality_review.md](android_observability_logging_quality_review.md) | Audit logging/metrics/traces for incident readiness | Comprehensive |
| [android_reliability_slo_error_budget_review.md](android_reliability_slo_error_budget_review.md) | Define reliability SLOs + error-budget policy that gates releases | Modular |

### Dependencies, SDKs & Toolchain

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_dependency_audit.md](android_dependency_audit.md) | Comprehensive CVE + abandonment-risk audit with multi-sprint paydown plan | Comprehensive |
| [android_dependency_update.md](android_dependency_update.md) | Safely **apply** a set of dependency updates with breaking-change analysis | Comprehensive |
| [android_third_party_sdk_upgrade_review.md](android_third_party_sdk_upgrade_review.md) | Review data-collecting SDK upgrades (Firebase, ads, analytics) for behavior/privacy/consent | Modular |
| [android_build_toolchain_upgrade.md](android_build_toolchain_upgrade.md) | Coordinated AGP/Gradle/Kotlin/JDK/KSP upgrade with compatibility matrix | Comprehensive |
| [android_target_sdk_migration.md](android_target_sdk_migration.md) | **Plan** the annual targetSdk bump — behavior-change mapping + deadline tracking | Comprehensive |
| [android_version_upgrade.md](android_version_upgrade.md) | **Execute** the targetSdk upgrade — apply, test, roll out | Comprehensive |
| [android_sdk_migration.md](android_sdk_migration.md) | Migrate deprecated APIs to modern replacements (AsyncTask→Coroutines, etc.) | Comprehensive |
| [android_min_sdk_raise_planner.md](android_min_sdk_raise_planner.md) | Plan raising minSdk — user-reach trade-off + removable compat shims | Modular |

### Code Health & Debt

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_tech_debt_triage.md](android_tech_debt_triage.md) | Inventory, score, and schedule tech-debt paydown (interest model) | Comprehensive |
| [android_feature_flag_lifecycle_cleanup.md](android_feature_flag_lifecycle_cleanup.md) | Inventory flags/Remote Config, classify, and retire dead branches safely | Modular |
| [android_proguard_r8_optimization.md](android_proguard_r8_optimization.md) | Audit/optimize R8 keep rules, shrinking, full-mode migration | Comprehensive |

### Product Signal

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_user_feedback_analysis.md](android_user_feedback_analysis.md) | Turn Play reviews/support feedback into prioritized dev tasks | Modular |

---

## Prompt Chains (run in sequence)

**SDK / version upgrades**
```
android_target_sdk_migration  (plan behavior changes + deadline)
        ↓
android_version_upgrade       (execute: apply, test, stage rollout)
        ↓
android_build_toolchain_upgrade  (if AGP/Gradle/Kotlin floor must move)
        ↓
android_sdk_migration / android_min_sdk_raise_planner  (modernize / drop old-OS shims)
```

**Dependencies**
```
android_dependency_audit (../analysis = quick · maintenance = deep+paydown)
        ↓
android_dependency_update            (apply selected updates)
        ↓
android_third_party_sdk_upgrade_review  (for data/ads/analytics SDKs)
```

**Incident lifecycle**
```
android_incident_triage_and_severity_classification
        ↓                              ↘
android_on_call_runbook_generator   android_crash_analysis / android_anr_vitals_analysis
        ↓
android_regression_prevention_checklist_after_hotfixes
        ↓
android_postmortem_and_corrective_action_planning
        ↓
android_observability_logging_quality_review → android_reliability_slo_error_budget_review
```

---

## Maintenance Cadence

- **Weekly:** review new crash/ANR clusters (`android_anr_vitals_analysis`, `android_crash_analysis`); check error-budget burn (`android_reliability_slo_error_budget_review`).
- **Per release:** evaluate SLO release gates; re-run `android_regression_prevention_checklist_after_hotfixes` for any hotfix.
- **Quarterly:** `android_dependency_audit`, `android_tech_debt_triage`, `android_feature_flag_lifecycle_cleanup`; plan annual `android_target_sdk_migration`.
- **Post-incident:** `android_incident_triage…` → `android_postmortem…` → update runbooks (`android_on_call_runbook_generator`) and close detection gaps (`android_observability_logging_quality_review`).

---

## Scope Guide

| Scope | Line Count | Best For |
|-------|-----------|----------|
| **Comprehensive** | 200-500 lines | Multi-phase diagnosis, migrations, architecture-level decisions |
| **Modular** | 80-160 lines | Focused single-concern tasks, checklists, reviews |

## Authoring Convention

Every prompt here uses full frontmatter (`title`, `category`, `description`, `techniques`, `difficulty`, `tags`, `updated`, `related_prompts`), then the body sections: **Objective → When to Use → Context Gathering → Instructions (CRITICAL Verification Requirements + False-Positive Prevention) → phased tables → Expected Output → Related Prompts.** New maintenance prompts should match this shape.

---

*Maintenance prompts: 21 · Last updated: 2026-06-06*
