---
title: "Android Third-Party SDK Upgrade Review"
category: mobile-development
description: "Reviews upgrades of bundled third-party SDKs (Firebase, ads, analytics, payments, push) for behavior, privacy, consent, and policy changes — distinct from routine application-library updates."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - android
  - maintenance
  - sdk
  - privacy
  - dependencies
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_dependency_update.md
  - domain-software-engineering/mobile/android/publishing/android_privacy_compliance.md
  - domain-software-engineering/mobile/android/publishing/play_store_data_safety_generator.md
  - domain-software-engineering/mobile/android/maintenance/android_feature_flag_lifecycle_cleanup.md
---

# Android Third-Party SDK Upgrade Review

**Objective:** Review an upgrade of a bundled third-party SDK (Firebase, Google Mobile Ads, analytics, attribution, payment, push, social login) for the changes that generic dependency bumps miss — runtime behavior shifts, new data collection, consent/permission requirements, manifest/init changes, and Play policy/Data Safety implications.

**When to Use:** Use when upgrading any SDK that collects data, shows ads, handles payments, manages identity, or runs background services — especially across major versions. Routine library bumps (a JSON parser, a coroutines patch) belong in `android_dependency_update.md`; this prompt is for SDKs whose upgrades can change **what data leaves the device** or **what the user must consent to**.

**Prompt Type:** Modular (130-160 lines)

## Context Gathering

1. "Which SDK, and what are the current and target versions? Link the changelog/migration guide."
2. "What does this SDK do in the app (ads, analytics, crash, auth, payments, push, attribution)?"
3. "What consent framework is in place (UMP/CMP, GDPR/CCPA gating), and which SDKs are gated by it?"
4. "What does the current Play Data Safety form declare for this SDK's data, and what's the app's privacy policy say?"
5. "Does the SDK add a `ContentProvider`/init-on-startup, new permissions, or background work?"

## Instructions

### CRITICAL: Verification Requirements

**Before approving the upgrade, you MUST:**

1. **Read the migration guide and changelog** — cite specific behavior changes, not "should be compatible." Major SDK versions frequently change defaults.
2. **Diff data collection** — determine whether the new version collects new data types or changes defaults (e.g., auto-collection on by default). This drives Data Safety + privacy-policy updates.
3. **Check consent/permission deltas** — new SDK versions may require UMP/consent integration, new runtime permissions, or `AD_ID` / tracking declarations.
4. **Inspect manifest & init changes** — new `ContentProvider` auto-init, `<meta-data>`, services, or default-enabled startup work that affects ANR/startup.
5. **Confirm policy alignment** — verify the upgrade doesn't introduce behavior that violates Play Families/ads/data policies for this app's category.

### False-Positive Prevention

- ❌ Do NOT treat an SDK major bump as a routine dependency update — it can silently change data flows
- ❌ Do NOT skip the Data Safety / privacy-policy reconciliation when collection changes
- ❌ Do NOT assume auto-collection defaults are unchanged across versions
- ❌ Do NOT ignore transitive SDKs the upgrade pulls in (an ads SDK may add attribution libs)
- ✅ DO gate any new data collection behind the existing consent framework before rollout
- ✅ DO verify startup/ANR impact if the SDK initializes on the main thread at launch
- ✅ DO stage the rollout and watch crash/ANR + consent metrics

### Phase 1: Change Surface Analysis

| Dimension | Current | Target | Change | Action |
|-----------|---------|--------|--------|--------|
| API/migration breaking changes | [n/a] | [items] | [summary] | [code edits] |
| Data collected (types) | [list] | [list] | [new/removed] | [Data Safety update?] |
| Auto-collection defaults | [on/off] | [on/off] | [delta] | [explicit opt config] |
| Consent / permissions | [UMP? perms] | [required] | [delta] | [consent gating] |
| Manifest / init / services | [current] | [new] | [provider/meta/service] | [startup review] |
| Min SDK / AGP / Kotlin reqs | [reqs] | [reqs] | [delta] | [toolchain check] |

### Phase 2: Privacy & Policy Reconciliation

| Check | Status | Evidence |
|-------|--------|----------|
| New/changed data types reflected in Play Data Safety | [Pass/Fail/N-A] | [form section] |
| Privacy policy covers new collection | [Pass/Fail/N-A] | [policy link] |
| Consent (GDPR/CCPA) gates new collection before it starts | [Pass/Fail/N-A] | [consent flow] |
| `AD_ID` permission / tracking declaration correct | [Pass/Fail/N-A] | [manifest] |
| Category policy (Families/health/finance) still satisfied | [Pass/Fail/N-A] | [policy] |

### Phase 3: Stability & Rollout

| Check | Status | Evidence |
|-------|--------|----------|
| Startup/ANR impact assessed (main-thread init?) | [Pass/Fail] | [trace/StrictMode] |
| Release build + R8 keep rules updated for the SDK | [Pass/Fail] | [build green] |
| Smoke test of SDK-driven flows (ad load, event, purchase, push) | [Pass/Fail] | [test run] |
| Staged rollout + metrics to watch defined | [Pass/Fail] | [rollout plan] |

## Expected Output

1. Change-surface table (API, data, consent, manifest, toolchain)
2. Privacy & policy reconciliation result (with Data Safety / policy actions)
3. Required code/manifest/keep-rule edits
4. Stability assessment (startup/ANR) + smoke-test list
5. Staged-rollout plan with consent + crash/ANR metrics to monitor
6. Go / no-go recommendation with residual risks

## Related Prompts

- [android_dependency_update.md](android_dependency_update.md) - For non-data, routine library updates
- [android_privacy_compliance.md](../publishing/android_privacy_compliance.md) - Full GDPR/CCPA/Play privacy audit
- [play_store_data_safety_generator.md](../publishing/play_store_data_safety_generator.md) - Regenerate Data Safety declarations
- [android_feature_flag_lifecycle_cleanup.md](android_feature_flag_lifecycle_cleanup.md) - Gate SDK rollout behind a flag
- [android_anr_vitals_analysis.md](android_anr_vitals_analysis.md) - If the SDK introduces startup ANRs
