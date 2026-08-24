---
title: "Android Feature Flag and Remote Config Lifecycle Cleanup"
category: mobile-development
description: "Inventories feature flags and Remote Config keys in an Android app, classifies each by lifecycle state, and produces a safe, prioritized retirement plan to pay down flag debt."
techniques:
  - ST-01
  - ST-02
  - DS-06
  - QA-01
  - RT-05
difficulty: intermediate
tags:
  - android
  - maintenance
  - feature-flags
  - remote-config
  - tech-debt
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_tech_debt_triage.md
  - domain-software-engineering/mobile/android/maintenance/android_third_party_sdk_upgrade_review.md
  - domain-software-engineering/mobile/android/improvement/android_code_modernization.md
  - domain-software-engineering/mobile/android/targeted-reviews/firebase_remote_config_strategy.md
---

# Android Feature Flag and Remote Config Lifecycle Cleanup

**Objective:** Inventory every feature flag and Remote Config key in the codebase, classify each by lifecycle state (active experiment, permanent ops toggle, stale/launched, dead), and produce a safe, prioritized retirement plan that removes dead branches without breaking live behavior.

**When to Use:** Use when flags have accumulated and the codebase is littered with conditional branches, after experiments conclude, during tech-debt paydown, or when stale flags create reasoning/testing overhead. Flags are debt that compounds: each adds a branch, doubles a test surface, and can silently diverge from server config.

**Prompt Type:** Modular (120-150 lines)

## Context Gathering

1. "What flag system(s) are in use — Firebase Remote Config, a custom flag service, build-time `BuildConfig` flags, or several?"
2. "Can you share the flag definitions/keys and where they're read (search hits for the flag accessor)?"
3. "Which flags gate experiments (A/B), which are operational kill switches, and which gated a now-launched feature?"
4. "What is the server-side default for each key, and what % of users currently see each variant?"
5. "What is the minimum supported app version still in the field (old clients may still read a key)?"

## Instructions

### CRITICAL: Verification Requirements

**Before recommending removal of any flag, you MUST:**

1. **Confirm it is truly dead** — the flag is fully rolled out (or fully off) AND no in-field app version depends on the removed branch.
2. **Identify both branches** — locate the kept path and the removed path in code; deleting a flag means deleting one branch, not just the read.
3. **Check server coupling** — removing a client read while the server still serves the key (or vice versa) can break old clients; sequence client and server changes.
4. **Distinguish permanent toggles from temporary flags** — kill switches and ops toggles are *not* debt; do not schedule them for removal.
5. **Verify no flag is the only mitigation for a known risk** — a flag protecting a risky path must keep a replacement guard if removed.

### False-Positive Prevention

- ❌ Do NOT remove a kill switch / operational toggle just because it looks unused — it's insurance
- ❌ Do NOT delete a client flag read while old app versions in the field still branch on it
- ❌ Do NOT assume "100% rollout" means safe to remove without confirming the off-branch is truly unreachable
- ❌ Do NOT bundle flag removal with unrelated refactors (keeps the diff reviewable and revertible)
- ✅ DO sequence: pin server value → remove client branch → remove server key (or the safe equivalent)
- ✅ DO keep a kept-branch test and delete the now-impossible-branch tests

### Phase 1: Flag Inventory & Classification

| Flag / Key | System | Read Locations (file:line) | Current State | Class | Min Client Dependency |
|------------|--------|----------------------------|---------------|-------|------------------------|
| [name] | [RC/custom/BuildConfig] | [paths] | [% on / default] | [Experiment / Permanent / Stale-launched / Dead] | [version or none] |

**Lifecycle classes:**
- **Experiment** — A/B in progress; keep until concluded.
- **Permanent** — kill switch / ops toggle; keep, document as permanent.
- **Stale-launched** — feature shipped to 100%; off-branch is dead → remove off-branch.
- **Dead** — no longer referenced or fully off with no plan → remove entirely.

### Phase 2: Retirement Plan (prioritized)

| Flag | Action | Removal Sequence | Risk | Owner | Verification |
|------|--------|------------------|------|-------|--------------|
| [name] | [Remove off-branch / Remove key / Keep+document] | [server-pin → client-remove → key-remove] | [H/M/L] | [name] | [test/build/monitor] |

Order by leverage: highest branch-complexity + lowest risk first.

### Phase 3: Safe Removal Checklist (per flag)

- [ ] Confirmed lifecycle class and rollout state with evidence
- [ ] Located kept-branch and dead-branch in code
- [ ] No in-field app version depends on the dead branch
- [ ] Server value pinned to the kept variant before client removal (if server-driven)
- [ ] Dead branch deleted; kept branch inlined
- [ ] Dead-branch tests removed; kept-path test retained/added
- [ ] Build green; flag accessor no longer referenced
- [ ] Server key scheduled for deletion after old clients age out (note date)

## Expected Output

1. Flag inventory table with lifecycle classification + evidence
2. Permanent-toggle list (explicitly excluded from removal)
3. Prioritized retirement plan with removal sequencing per flag
4. Per-flag safe-removal checklist
5. Residual-risk note for any flag kept "for now" with reasons

## Related Prompts

- [android_tech_debt_triage.md](android_tech_debt_triage.md) - Feed flag debt into the broader paydown plan
- [android_third_party_sdk_upgrade_review.md](android_third_party_sdk_upgrade_review.md) - Flags often gate SDK rollouts
- [android_code_modernization.md](../improvement/android_code_modernization.md) - Simplify code after branches are removed
- [../targeted-reviews/firebase_remote_config_strategy.md](../targeted-reviews/firebase_remote_config_strategy.md) - Remote Config rollout/governance patterns
