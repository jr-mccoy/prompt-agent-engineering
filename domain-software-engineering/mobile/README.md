# Mobile Development Prompts

Comprehensive prompts for mobile app development across Android, iOS, React Native, Flutter, and cross-platform architectures.

**Total Prompts:** 255  •  _Last refreshed: 2026-04-17_

---

## Structure

Mobile prompts are organized into three top-level buckets: **android/**, **ios/**, and **cross-platform/**. Each platform uses a consistent lifecycle-based substructure (planning → implementation → analysis → improvement → testing → publishing → maintenance), plus a `targeted-reviews/` subdirectory for focused, deep-dive reviews of specific concerns (e.g. sync, state management, security rules).

```
mobile/
├── android/                 (134 prompts)
│   ├── planning/            (13)  — app concept, tech stack, architecture, scaffolding
│   ├── implementation/      (11)  — Compose screens, DI, data layer, navigation, background work
│   ├── analysis/            (19)  — architecture, performance, security, codebase-health audits
│   ├── improvement/         (14)  — refactoring, UI polish, modernization, a11y, UX
│   ├── testing/             (6)   — unit, UI, screenshot, integration testing
│   ├── publishing/          (16)  — release prep, Play Store, staged rollout, privacy compliance
│   ├── maintenance/         (10)  — SDK migration, dependency updates, crash analysis
│   └── targeted-reviews/    (45)  — focused reviews (sync, Compose recomposition, Room, Hilt, etc.)
├── ios/                     (103 prompts)
│   ├── planning/            (13)
│   ├── implementation/      (14)  — SwiftUI, CloudKit, widgets, app intents, push, background tasks
│   ├── analysis/            (13)  — architecture, performance, security audits
│   ├── improvement/         (12)
│   ├── testing/             (7)
│   ├── publishing/          (14)  — App Store, privacy policy, ToS generation
│   ├── maintenance/         (10)
│   └── targeted-reviews/    (20)
├── cross-platform/          (18 prompts)
│   ├── migration/           (13)  — Android↔iOS migration, Compose↔SwiftUI, Room↔Core Data, DI, concurrency
│   └── (5 root)             — React Native perf, Flutter widget analysis, cross-platform arch, mobile CI/CD, mobile security
└── README.md
```

---

## Quick Selection Guide

### "I need to plan / scaffold a new app"
→ `android/planning/` or `ios/planning/`

### "I need to implement a feature (screen, DI, navigation, background work)"
→ `android/implementation/` or `ios/implementation/`

### "I need to audit / review an existing codebase"
→ `android/analysis/` or `ios/analysis/` for broad reviews  
→ `android/targeted-reviews/` or `ios/targeted-reviews/` for focused deep dives

### "I need to improve / refactor existing code"
→ `android/improvement/` or `ios/improvement/`

### "I need to test mobile code"
→ `android/testing/` or `ios/testing/`

### "I need to ship / publish the app"
→ `android/publishing/` or `ios/publishing/`

### "I need to keep the app healthy after launch"
→ `android/maintenance/` or `ios/maintenance/`

### "I'm migrating from Android to iOS (or vice versa)"
→ `cross-platform/migration/`

### "I'm on React Native / Flutter / KMP"
→ `cross-platform/`

### "I need mobile-platform-agnostic CI/CD or security guidance"
→ `cross-platform/mobile_cicd_pipeline_optimization.md`, `cross-platform/mobile_app_security_review.md`

---

## Highlight: Targeted Reviews

The `targeted-reviews/` subdirectories hold the sharpest Tier 1 prompts in the repo — each one is scoped to a single concern and includes explicit verification requirements and false-positive prevention. Examples:

- `android/targeted-reviews/android_sync_architecture_review.md` — offline-first conflict resolution
- `android/targeted-reviews/android_compose_recomposition_review.md` — Compose stability & skipping
- `android/targeted-reviews/android_sqlcipher_key_management_review.md` — encrypted DB key handling
- `ios/targeted-reviews/...` — analogous iOS deep dives

Use these when you suspect a specific subsystem has issues, rather than a general-purpose audit.

---

## Related Categories

- **[Analysis/Architecture](../analysis/architecture/)** — Cross-platform architecture prompts
- **[Analysis/Security](../analysis/security/)** — Generic security prompts (non-mobile)
- **[Analysis/Performance](../analysis/performance/)** — Generic performance analysis
- **[Testing](../testing/)** — Non-mobile testing prompts
- **[DevOps](../devops/)** — Backend / server CI/CD

---

## Recent Changes

- **2026-04-17** — Consolidated parallel hierarchies: `android-targeted-reviews/` merged into `android/targeted-reviews/`; `ios-targeted-reviews/` into `ios/targeted-reviews/`; `cross-platform-migration/` into `cross-platform/migration/`. Loose root-level `android_*`, `ios_*`, and `mobile_*` files moved into topic subdirectories.
