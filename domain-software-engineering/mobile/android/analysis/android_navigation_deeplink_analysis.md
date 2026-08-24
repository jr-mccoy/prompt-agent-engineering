---
title: "Android Navigation & Deep Link Analysis"
category: mobile-development
description: "Analyzes an Android app's navigation graph and deep-link handling for completeness, back-stack correctness, type-safe arguments, conditional/auth-gated routing, and deep-link coverage and validation, with prioritized fixes."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
  - QA-02
difficulty: intermediate
tags:
  - android
  - navigation
  - deep-links
  - jetpack-navigation
  - compose
  - analysis
  - mobile-development
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_manifest_permissions_audit.md
  - domain-software-engineering/mobile/android/analysis/android_architecture_review.md
  - domain-software-engineering/mobile/android/implementation/android_navigation_implementation.md
---

# Android Navigation & Deep Link Analysis

**Objective:** Analyze an Android app's navigation architecture — graph completeness and reachability, back-stack and up/back behavior, argument passing and type safety, conditional/auth-gated routing, and deep-link declaration, coverage, and parameter validation — and report navigation defects and deep-link risks with `file:line` evidence and concrete fixes.

**When to Use:** Use this when users report wrong back behavior, lost state on navigation, broken or unhandled deep links, or screens that are unreachable/duplicated in the stack; before adding deep-link campaigns; or when migrating to Navigation Compose / type-safe routes. Covers Jetpack Navigation (Compose and Fragment) and custom navigation.

---

## Context Gathering

1. **Nav stack:** "Navigation Compose, Navigation-Fragment, or custom? Single-activity or multi-activity?"
2. **Deep links:** "Which deep links / App Links exist (manifest intent filters, `navDeepLink`)? Any campaign or notification links?"
3. **Auth model:** "Are some destinations gated by auth/onboarding/feature flags?"
4. **Symptoms:** "Any reported back-button, state-loss, or broken-link issues?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the real graph** — from the nav graph definition / `NavHost` / manifest intent filters, not assumptions. Cite `file:line`.
2. **Confirm reachability and back behavior** — verify a destination is actually orphaned or that a `popUpTo`/`launchSingleTop` is actually wrong, before flagging.
3. **Check deep-link end-to-end** — declaration (manifest/`navDeepLink`) → routing → argument parsing → auth gating → target screen.
4. **Validate parameter handling** — deep-link params are untrusted input; confirm whether they're validated before use.

**A correct, well-guarded navigation graph is an acceptable outcome.** Don't manufacture issues.

### False-Positive Prevention

- ❌ Do NOT flag intentional `launchSingleTop`/`popUpTo` used to avoid duplicate destinations.
- ❌ Do NOT flag a destination reachable only via deep link as "orphaned."
- ❌ Do NOT demand App Links verification for internal/custom-scheme links not intended to be web-verified.
- ❌ Do NOT flag nullable args that are legitimately optional.
- ✅ DO flag destinations unreachable by any route.
- ✅ DO flag deep links that bypass auth/onboarding to protected screens.
- ✅ DO flag unvalidated deep-link parameters used in queries, intents, or WebViews.

---

### Phase 1: Navigation Inventory

| Item | What to Locate |
|------|----------------|
| Graph definition | Nav graph(s) / `NavHost` routes / fragment destinations |
| Destinations | Screens, dialogs, nested graphs; entry points |
| Arguments | Per-destination args, types, nullability, default values |
| Actions/transitions | How destinations connect; `popUpTo`, `launchSingleTop`, `restoreState` |
| Deep links | `<intent-filter>` (App Links/custom scheme), `navDeepLink`, notification PendingIntents |

---

### Phase 2: Graph Completeness & Back-Stack Correctness

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Orphan destination | MEDIUM | Screen with no incoming route (and not deep-link-only) |
| Wrong back behavior | HIGH | Back/up not returning to the expected destination; stuck loops |
| Duplicate destinations | MEDIUM | Same screen stacking repeatedly (missing `launchSingleTop`) |
| Lost state on nav | MEDIUM | Tab/list state not preserved (`saveState`/`restoreState` missing) |
| Start-destination logic | MEDIUM | Conditional start (auth/onboarding) handled fragilely |
| Nested graph wiring | LOW | Nested graphs with unclear entry/exit |

---

### Phase 3: Argument Passing & Type Safety

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Stringly-typed routes | MEDIUM | Manual route-string building instead of type-safe args/Safe Args |
| Large/object args | HIGH | Passing large objects/Parcelables through nav instead of IDs |
| Missing arg validation | MEDIUM | Required args assumed present without null/format checks |
| Encoding issues | LOW | Unencoded values breaking route parsing |

---

### Phase 4: Deep-Link Coverage & Security

| Check | Severity | What to Look For |
|-------|----------|-----------------|
| Auth-gate bypass | CRITICAL | Deep link landing on a protected screen without auth/onboarding checks |
| Unvalidated params | HIGH | Deep-link params used in DB/network/WebView/intent without validation |
| Missing handler | MEDIUM | Declared deep link with no destination/handler (dead link) |
| App Links verification | MEDIUM | `autoVerify` links without correct `assetlinks.json` (fall back to chooser) |
| Open redirect | HIGH | Deep link forwarding to an arbitrary URL/intent from a parameter |
| Coverage gaps | LOW | Important screens not deep-linkable where campaigns expect them |

---

## Output Format

```markdown
## Android Navigation & Deep Link Analysis Report

### Destination & Deep-Link Map
| Destination | Reachable via | Args (type, nullable) | Deep link | Auth-gated |
|-------------|---------------|------------------------|-----------|------------|

### Findings (severity-ordered)
**[SEVERITY] Area: title** — Location `file:line` · Issue · Fix

### Deep-Link Security Notes
- Auth bypass / unvalidated params / open-redirect findings.

### Prioritized Remediation (P1/P2/P3)
```

---

## Expected Output

1. **Destination & deep-link map.**
2. **Severity-rated findings** with locations and fixes.
3. **Deep-link security notes.**
4. **Prioritized remediation.**

---

## Techniques Used

- **ST-01** (Clear Objective): Navigation/deep-link scope.
- **ST-02** (Structured Sequential Instructions): Inventory → graph → args → deep links.
- **RT-02** (Multi-Dimensional Analysis): UX correctness + type safety + security.
- **RT-05** (Evidence-Based Reasoning): `file:line` citations across the path.
- **DS-06** (Prioritization Guidance): Severity ordering.
- **QA-02** (Edge Case Coverage): Auth bypass, encoding, App Links verification.

---

## Related Prompts

- [android_manifest_permissions_audit.md](android_manifest_permissions_audit.md) - Exported components & intent-filter exposure
- [android_architecture_review.md](android_architecture_review.md) - Navigation's place in app architecture
- [android_navigation_implementation.md](../implementation/android_navigation_implementation.md) - Implement type-safe navigation & deep links
