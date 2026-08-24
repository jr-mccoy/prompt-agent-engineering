---
title: "Android minSdk Raise Planner"
category: mobile-development
description: "Plans raising an Android app's minSdkVersion — quantifying the user impact of dropping old-OS support, then identifying compat shims, workarounds, and dependency floors that can be removed to simplify the codebase."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - maintenance
  - minsdk
  - modernization
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_target_sdk_migration.md
  - domain-software-engineering/mobile/android/maintenance/android_sdk_migration.md
  - domain-software-engineering/mobile/android/improvement/android_code_modernization.md
  - domain-software-engineering/mobile/android/maintenance/android_build_toolchain_upgrade.md
---

# Android minSdk Raise Planner

**Objective:** Plan raising the app's `minSdkVersion` by first quantifying how many real users would be dropped, then cataloging the compatibility shims, version-gated branches (`Build.VERSION.SDK_INT` checks), AppCompat/desugaring workarounds, and dependency floors that become removable once the floor rises — producing a net simplification with an explicit user-impact trade-off.

**When to Use:** Use when old `SDK_INT` checks clutter the code, when a desired API/library requires a higher floor, when desugaring or compat libraries add weight, or during modernization. This is the **inverse** of `targetSdk` work: `targetSdk` is about adopting new-OS behavior (and is Play-mandated); `minSdk` is about *dropping* old-OS support (a product decision with user-reach cost).

**Prompt Type:** Modular (120-150 lines)

## Context Gathering

1. "What is the current `minSdkVersion`, and what candidate floor are you considering (e.g., 24 → 26 → 28)?"
2. "What is your active-user distribution by API level (Play Console → Statistics / device catalog)?"
3. "What's driving this — a library requirement, code simplification, desugaring removal, or security?"
4. "Are there contractual/enterprise/regional commitments to specific old OS versions?"
5. "Can you share representative `Build.VERSION.SDK_INT` / `@RequiresApi` / compat usages in the code?"

## Instructions

### CRITICAL: Verification Requirements

**Before recommending a new floor, you MUST:**

1. **Quantify the dropped audience with real data** — state the % (and absolute count if available) of *active* users below each candidate floor. Never raise minSdk on intuition.
2. **Tie the raise to concrete wins** — list the specific shims/branches/dependencies that become removable at each candidate floor; a raise with no simplification payoff needs strong external justification.
3. **Separate "removable now" from "still needed"** — a `SDK_INT >= X` check is only dead if the new floor ≥ X for *all* branches it guards.
4. **Check dependency floors** — confirm whether libraries actually require the higher minSdk or whether the floor is being raised unnecessarily.
5. **Respect commitments** — flag any enterprise/regional/contractual obligations that block the raise regardless of usage numbers.

### False-Positive Prevention

- ❌ Do NOT raise minSdk based on global market share — use *this app's* active-user distribution
- ❌ Do NOT delete a `SDK_INT` branch unless the new floor makes every guarded path unreachable
- ❌ Do NOT assume desugaring can be removed — verify which desugared APIs are used and their minSdk
- ❌ Do NOT bundle the minSdk raise with unrelated refactors in one commit
- ✅ DO present the user-reach cost as a first-class trade-off, not a footnote
- ✅ DO sequence: raise floor → remove now-dead branches → drop unneeded compat deps
- ✅ DO keep a kept-path test; remove tests for now-impossible old-OS branches

### Phase 1: User-Impact Quantification

| Candidate minSdk | Active Users Below Floor (%) | Absolute (if known) | Acceptable? | Notes |
|------------------|------------------------------|---------------------|-------------|-------|
| [26] | [%] | [count] | [Y/N] | [trend over last 6–12 mo] |
| [28] | [%] | [count] | [Y/N] | [accelerating decline?] |

Recommend the floor where simplification payoff is high and dropped active users is acceptable.

### Phase 2: Simplification Payoff Inventory

| Removable Item | Type | Guarded API Level | Removable at minSdk | Location(s) |
|----------------|------|-------------------|---------------------|-------------|
| [SDK_INT branch] | Version check | [< X] | [X] | [file:line] |
| [Compat helper] | AppCompat/shim | [< X] | [X] | [file] |
| [Desugared API] | Desugaring | [< X] | [X] | [usage] |
| [Dependency floor] | Library | [requires X] | [X] | [libs.versions.toml] |

### Phase 3: Execution & Verification Plan

| Step | Action | Verify | Rollback |
|------|--------|--------|----------|
| 1 | Raise `minSdk` in build config | Build green; resolves deps | revert |
| 2 | Remove now-dead `SDK_INT` branches | tests pass; lint clean | revert per branch |
| 3 | Drop unneeded compat/desugar deps | release build green; size delta | restore dep |
| 4 | Remove old-OS-only tests; keep current-path tests | suite green | restore |

**Verification checklist:**
- [ ] User-impact number sourced from Play Console active users (not market data)
- [ ] Every removed branch confirmed unreachable at new floor
- [ ] Desugaring removal validated against actual API usage
- [ ] APK/AAB size delta recorded
- [ ] No contractual/enterprise obligation violated

## Expected Output

1. User-impact table per candidate floor (with trend)
2. Recommended floor + the user-reach trade-off stated explicitly
3. Simplification payoff inventory (what gets deleted)
4. Sequenced execution plan with per-step verification + rollback
5. Blockers list (commitments, dependency realities)

## Related Prompts

- [android_target_sdk_migration.md](android_target_sdk_migration.md) - The complementary (Play-mandated) targetSdk planning
- [android_sdk_migration.md](android_sdk_migration.md) - Migrate deprecated APIs uncovered while removing branches
- [android_code_modernization.md](../improvement/android_code_modernization.md) - Modernize the simplified code paths
- [android_build_toolchain_upgrade.md](android_build_toolchain_upgrade.md) - A higher floor may unlock toolchain/library upgrades
