# Android Analysis Prompts

This folder contains **30 codebase-wide analysis prompts** for Android applications. They review, audit, and understand an *existing* codebase — structure, security, UI, performance, data, build, and quality — and produce prioritized, evidence-backed findings.

## Analysis vs. Targeted Reviews

| | **`analysis/` (this folder)** | **`../targeted-reviews/`** |
|---|---|---|
| Scope | Codebase-wide / whole-subsystem audits | One narrow, high-risk pattern |
| Question | "How healthy is X across the app?" | "Is this specific mechanism correct?" |
| Example | `android_concurrency_threading_analysis.md` | `android_coroutine_scope_review.md` |

Start broad here; drop into `../targeted-reviews/` for a deep, single-pattern pass when a finding warrants it.

## How These Prompts Work

Each prompt follows the same Tier-1 structure: **Objective → When to Use → Context Gathering → CRITICAL Verification Requirements + False-Positive Prevention → phased Instructions → Output Format → Techniques Used → Related Prompts.** Every finding requires a `file:line` location and a severity rating, and "finding the codebase healthy" is always an acceptable outcome — the prompts are tuned against manufacturing false concerns.

---

## Prompt Catalog

### Architecture & Code Quality

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_codebase_health_assessment.md](android_codebase_health_assessment.md) | Holistic health assessment and roadmap — **the entry point** | Comprehensive |
| [android_architecture_review.md](android_architecture_review.md) | Pattern implementation, layer boundaries, dependency flow | Comprehensive |
| [android_module_graph_analysis.md](android_module_graph_analysis.md) | Multi-module dependency graph, coupling, layering, god-modules | Comprehensive |
| [android_kotlin_best_practices.md](android_kotlin_best_practices.md) | Modern architecture, Jetpack, Kotlin language usage | Comprehensive |
| [ai_code_review_android.md](ai_code_review_android.md) | PR/pre-merge review checklist across 7 categories | Modular |
| [android_kotlin_compose_debugging_audit.md](android_kotlin_compose_debugging_audit.md) | Crash/defect patterns (null-safety, recomposition, coroutines) | Comprehensive |
| [android_technical_debt_assessment.md](android_technical_debt_assessment.md) | Catalog and prioritize debt with remediation roadmap | Comprehensive |
| [android_hilt_dagger_analysis.md](android_hilt_dagger_analysis.md) | DI configuration, scopes, modules, anti-patterns | Comprehensive |

### Security & Privacy

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_authentication_security_audit.md](android_authentication_security_audit.md) | Auth flows, 2FA, sessions, account-takeover risks | Comprehensive |
| [android_local_data_security_audit.md](android_local_data_security_audit.md) | At-rest storage, encryption, Keystore, backups | Comprehensive |
| [android_cloud_backend_security_audit.md](android_cloud_backend_security_audit.md) | Firestore/RTDB rules, Cloud Functions, sync, storage | Comprehensive |
| [android_manifest_permissions_audit.md](android_manifest_permissions_audit.md) | Permissions, exported components, manifest flags | Comprehensive |
| [android_privacy_data_flow_audit.md](android_privacy_data_flow_audit.md) | PII inventory, data flows, third-party SDK sharing, Data Safety | Comprehensive |

### UI, Compose & Accessibility

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_compose_ui_analysis.md](android_compose_ui_analysis.md) | Consistency, quality, appeal, competitiveness, a11y | Comprehensive |
| [android_compose_ui_consistency_audit.md](android_compose_ui_consistency_audit.md) | Typography/size/spacing + cross-theme layout invariance | Comprehensive |
| [android_compose_migration_analysis.md](android_compose_migration_analysis.md) | XML→Compose migration readiness and roadmap | Comprehensive |
| [android_theme_investigation.md](android_theme_investigation.md) | Theme architecture + root cause for persistent styling issues | Comprehensive |
| [android_accessibility_audit.md](android_accessibility_audit.md) | TalkBack, contrast, touch targets, dynamic type, RTL | Modular |
| [android_localization_i18n_readiness_audit.md](android_localization_i18n_readiness_audit.md) | Hardcoded strings, plurals, locale formatting, RTL | Modular |

> **Compose-UI: which prompt?**
> - **Broad quality & market appeal** (is the UI good and competitive?) → `android_compose_ui_analysis.md` (supports a low-token "Compressed mode").
> - **Layout precision** (typography/size/spacing consistency, cross-theme invariance) → `android_compose_ui_consistency_audit.md`.
> - **Screen-reader / low-vision / WCAG** → `android_accessibility_audit.md`.

### Performance & Resources

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_performance_audit.md](android_performance_audit.md) | Startup, UI, memory, network, database, background work | Comprehensive |
| [android_battery_drain_investigation.md](android_battery_drain_investigation.md) | 10-dimension battery consumption analysis | Comprehensive |
| [android_concurrency_threading_analysis.md](android_concurrency_threading_analysis.md) | Coroutine/Flow/dispatcher model, races, main-safety | Comprehensive |
| [android_resource_asset_analysis.md](android_resource_asset_analysis.md) | Resource hygiene, image formats, resource-driven size | Modular |

### Data & Networking

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_networking_layer_analysis.md](android_networking_layer_analysis.md) | Retrofit/OkHttp/Ktor config, retries, caching, errors, TLS | Comprehensive |
| [android_data_layer_persistence_analysis.md](android_data_layer_persistence_analysis.md) | Room/DataStore/prefs, migrations, source-of-truth, caching | Comprehensive |
| [android_navigation_deeplink_analysis.md](android_navigation_deeplink_analysis.md) | Nav graph, back-stack, type-safe args, deep-link coverage/security | Comprehensive |

### Dependencies & Build

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_dependency_audit.md](android_dependency_audit.md) | Version freshness, vulnerabilities, safe updates | Modular |
| [android_open_source_license_audit.md](android_open_source_license_audit.md) | License inventory, copyleft, compatibility, attribution | Modular |
| [android_build_gradle_health_analysis.md](android_build_gradle_health_analysis.md) | Version catalogs, convention plugins, build performance | Comprehensive |

### Testing

| Prompt | Description | Scope |
|--------|-------------|-------|
| [android_test_coverage_analysis.md](android_test_coverage_analysis.md) | Coverage gaps and test-suite quality (see also `../testing/`) | Modular |

---

## Recommended Analysis Workflow

```
1. Codebase Health Assessment  →  overall picture, routes to deeper prompts
        ↓
2. Architecture + Module Graph  →  if structural issues surface
        ↓
3. Domain deep-dives (run what's relevant):
     • Security & Privacy: auth → local data → cloud → manifest/permissions → privacy data-flow
     • Performance: performance audit → concurrency → battery → resources
     • UI: compose UI analysis → consistency → accessibility → localization
     • Data: networking → data-layer/persistence → navigation/deep-links
     • Build: dependency audit → build/Gradle health → license audit
        ↓
4. Technical Debt Assessment  →  consolidate and prioritize findings
        ↓
5. Drop into ../targeted-reviews/ for any high-risk pattern a finding flags
```

### Pre-Release Security & Privacy Pass

For apps with accounts and cloud data, run before publishing:

```
local data → authentication → cloud backend → manifest/permissions → privacy data-flow
        ↓
feed results into ../publishing/ (privacy compliance, Data Safety, release prep)
```

---

## Contributing

When adding a new analysis prompt:

1. Follow the Tier-1 structure (Objective, When to Use, Context Gathering, Verification + False-Positive Prevention, phased Instructions, Output Format, Techniques Used, Related Prompts).
2. Require `file:line` citations and severity ratings; include a "healthy is acceptable" guardrail.
3. Use canonical frontmatter (`techniques` with valid IDs from the master technique index, `difficulty`, `related_prompts`).
4. Add the prompt to this README in the right category and cross-reference related prompts.
5. Regenerate the index: `python3 ../../../../scripts/generate_prompt_index.py`.
