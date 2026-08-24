# Android Improvement Prompts

Prompts in this directory **actively transform working Android code** — refactor, modernize, optimize, and polish. They assume the app already runs and you want it better.

**How this differs from sibling directories:**

| Directory | Purpose | Mutates code? |
|-----------|---------|---------------|
| `improvement/` (here) | Refactor / modernize / optimize / polish existing code | Yes |
| `analysis/` | Read-only audits and reviews (health, performance, UI consistency, best practices) | No |
| `targeted-reviews/` | Narrow single-lens reviews (recomposition, coroutine scope, Room queries, sync) | No |
| `maintenance/` | Upkeep — dependency/SDK updates, crash analysis, postmortems, ProGuard/R8 | Mixed |
| `testing/` | Test generation and test-suite strategy | Adds tests |
| `implementation/` | Build new features/layers from scratch | Adds code |
| `planning/` | Architecture/stack/module decisions before code | No |
| `publishing/` | Release, Play Store, compliance | No |

---

## Prompt index

### Code quality & refactoring
| Prompt | Use when | Difficulty |
|--------|----------|------------|
| [android_kotlin_refactoring_generalized.md](android_kotlin_refactoring_generalized.md) | **Start here.** Auto-detects stack, triages and scores all refactoring candidates, refactors the file(s) you pick. | Intermediate |
| [android_kotlin_refactoring.md](android_kotlin_refactoring.md) | You know the file and the stack is the classic Compose + Room + Firebase + Hilt set. | Advanced |
| [android_code_modernization.md](android_code_modernization.md) | Migrate deprecated APIs / adopt modern Kotlin + Jetpack conventions across the codebase. | Advanced |
| [android_error_handling_improvement.md](android_error_handling_improvement.md) | High crash rates, confusing error messages, inconsistent error handling. | Intermediate |
| [android_memory_leak_detection.md](android_memory_leak_detection.md) | OOM crashes, growing memory over time; find and fix leak patterns. | Intermediate |

### Performance & build
| Prompt | Use when | Difficulty |
|--------|----------|------------|
| [android_compose_performance_optimization.md](android_compose_performance_optimization.md) | Compose jank / excess recomposition — fix stability, strong-skipping, deferred reads, keys. | Advanced |
| [android_startup_optimization.md](android_startup_optimization.md) | Slow cold start; defer/lazy-init blocking work in Application/Activity. | Intermediate |
| [android_baseline_profiles_optimization.md](android_baseline_profiles_optimization.md) | Add Baseline/Startup Profiles + Macrobenchmark for faster launch and scrolling. | Intermediate |
| [android_build_speed_optimization.md](android_build_speed_optimization.md) | Gradle builds are slow — config cache, KSP, parallelization, build scans. | Intermediate |

### UI / UX
> Five UI prompts overlap by design — pick by **intent and inputs**:

| Prompt | Intent | Inputs needed | Output |
|--------|--------|---------------|--------|
| [android_ui_polish_audit.md](android_ui_polish_audit.md) | Lightweight consistency/polish audit | Code | Audit report |
| [android_compose_ui_polish.md](android_compose_ui_polish.md) | Production polish, **no redesign** | Screenshots **+** code | Polish spec (gated) |
| [android_compose_ui_improvement.md](android_compose_ui_improvement.md) | Redesign consultation (discovery → brainstorm → implement) | Screenshots + code | Full spec + implementation |
| [android_compose_ui_market_dominance_review.md](android_compose_ui_market_dominance_review.md) | Category-leading competitive overhaul | Full codebase + screenshots + competitors | Tiered roadmap |
| [android_user_experience_enhancement.md](android_user_experience_enhancement.md) | Flows, feedback, perceived perf, delight | Code + analytics/feedback | UX enhancement report |
| [android_accessibility_improvement.md](android_accessibility_improvement.md) | WCAG / TalkBack / touch targets / contrast | Code (ideally device testing) | Accessibility report + fixes |
| [android_edge_to_edge_predictive_back_adoption.md](android_edge_to_edge_predictive_back_adoption.md) | Adopt SDK 35 edge-to-edge, window insets, predictive back. | Code | Migration plan + fixes |
| [android_adaptive_large_screen_improvement.md](android_adaptive_large_screen_improvement.md) | Make a phone-only app adaptive for tablets/foldables. | Code | Adaptive-layout plan + fixes |

> For read-only UI analysis instead, see `../analysis/android_compose_ui_analysis.md` and `../analysis/android_compose_ui_consistency_audit.md`. To establish design direction before any polish, see `../planning/android_compose_ui_design_studio.md`.

### Cross-platform & build system
| Prompt | Use when | Difficulty |
|--------|----------|------------|
| [android_compose_multiplatform_migration.md](android_compose_multiplatform_migration.md) | Plan a move from Android-only Compose to Compose Multiplatform (iOS/Desktop/Web). | Advanced |
| [android_version_catalog_migration.md](android_version_catalog_migration.md) | Migrate Gradle deps to `libs.versions.toml` + convention plugins. | Intermediate |

---

## Conventions for prompts in this directory

Every prompt here should:
- Carry full frontmatter: `title`, `category: mobile-development`, `description`, `techniques`, `difficulty`, `tags` (including `android`), `updated`, `related_prompts`.
- Open with a **CRITICAL: Verification Requirements** + **False-Positive Prevention** block — finding the code is *already good* is an acceptable outcome.
- Require **evidence** (`File:line`) for every finding; never flag on pattern-match alone.
- Lock an output format and end with a verification checklist.
- Gate code changes behind explicit user approval where the prompt mutates production code.
