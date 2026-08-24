---
name: android-play-billing-upgrade
description: Use this skill when upgrading or migrating an Android project from any
  legacy Google Play Billing Library (PBL) version to the latest stable version of
  PBL.
license: Complete terms in LICENSE.txt
metadata:
  author: Google LLC
  last-updated: '2026-07-02'
  upstream: https://github.com/android/skills
  upstream-path: play/play-billing-library-version-upgrade
  upstream-commit: 23d9eae21a4bfe0209e5b678f0ebe931e3c7dff4
  upstream-synced: '2026-08-02'
  keywords:
  - android
  - play billing
  - play billing library
  - pbl
  - upgrade
  - migration
  - deprecation
  - google play
---

## Phase 0: Intent Message

**Reporting Action**: Before proceeding, immediately tell the user: "I will
upgrade Play Billing Library to the latest version."

## Phase 1: Discovery \& Situational Awareness

1. **Primary Check (Build Version)** : Locate the project's billing dependency (e.g., `com.android.billingclient:billing`) in `build.gradle`, `build.gradle.kts`, or `libs.versions.toml`.
2. **Initial Compilation Test**: Attempt to sync and build the project immediately.
3. **Fallback Discovery (Effective Version)** :
   - **Trigger**: Only if the build fails immediately, scan the source code for deprecated artifacts.
   - **Logic** : The presence of deprecated APIs indicates the **"Effective
     Version"** ---defined as the version where those specific APIs were **last
     available**, not when they were introduced.
   - **Example** : If `SkuDetails` is present, treat the baseline as **PBL v7** or earlier (regardless of the version string in `build.gradle`).
4. **Identify Target \& Path** : Access the version tool or release notes to find the latest stable version and calculate a \[Direct/Stepped\] migration path based on the **Effective Version** baseline.

- **Calculate Migration Path** :
  - If the **Effective Version** is within 2 major versions of the target: Plan a **Direct Migration**.
  - If it is more than 2 major versions behind: Plan a **Stepped
    Migration**. Migrate by two major versions at a time (e.g., v4 -\> v6 -\> v8) until you are within two versions of the target.
- **Reporting Action**: Before proceeding, tell the user: "I've detected you are effectively on PBL \[Current\] and the latest is \[Target\]. I am planning a \[direct/stepped\] migration path."

## Phase 2: Contextual Document Mapping \& Planning

For every major version jump identified in your path, you **MUST** synthesize
instructions from:

- **[Migration Guide](https://developer.android.com/google/play/billing/migrate-gpblv%5BX%5D)** (where `[X]` is the target major version).
- **Release Highlights** : The "Deprecations" and "Breaking Changes" sections of the relevant [Release Notes](references/android/google/play/billing/release-notes.md).
- **Developer Documentation**: Consult your knowledge of the Google Play Billing documentation regarding the relevant features used in this app (e.g., Subscriptions, One-Time Products).
- **Develop the Plan**: Identify every specific code change required (API removals, class replacements, logic shifts) and print this out as a checklist.

## Phase 3: Instructions for Execution

*Reporting Action: For each of the following steps, give a brief explanation of
what you will be doing prior to execution, and a brief summary of what you
accomplished afterwards.*

### Step 1: SDK \& Environment Alignment

- **Action** : Update `build.gradle` to meet SDK requirements (e.g., "PBL 9 requires `compileSdk` 35").
- **Gradle Version**: Verify if the new library requires a newer Android Gradle Plugin (AGP) or Kotlin version.

### Step 2: Intent-based Refactoring

Analyze the intent of the existing code rather than performing purely textual
string replacement.

- **Action** : You **MUST** follow all deprecation instructions and refactor patterns from **both** the [references/migration-logic.md](references/migration-logic.md) section, the official migration guides, and the general documentation pages identified in Phase 2.
- **Verification** : Verify you are doing **all steps from all documentation** and then making sure you follow the specific directions from the checklist in the references.

### Step 3: Sequential Verification (Only applicable for Stepped Migrations)

1. **Upgrade** to the first major intermediate version in your path.
2. **Run `./gradlew assembleDebug`** to verify no intermediate breaking changes were missed.
3. **Repeat** until you reach the final target version.

### Step 4: Final Validation Checklist

1. **Smart Checklist Verification**:
2. Open [references/version-checklist.md](references/version-checklist.md) and locate the **Smart Version-Specific Checklist**.
3. **Action**: For every version between your \[Detected Effective Version\] and \[Detected New Version\], verify that every item has been addressed in the code using "Find in Files" or structural analysis.
4. **Tests** : Run all unit and implementation tests (`./gradlew test`).
5. **Clean Build** : Verify the project completes a full clean build: `./gradlew clean assembleDebug`. Then, run `./gradlew sync` and `./gradlew build` so that the user can immediately test the new version manually.

## Final Report

Explain the "Why" to the developer:

- "I updated your SDK to \[Version\] because PBL \[Version\] requires it for \[Reason from docs\]."
- "I removed your custom `retryConnection()` logic because it is now handled natively by the library using `enableAutoServiceReconnection()`."
- "Successfully upgraded from PBL \[Old\] to PBL \[New\] and verified with unit tests. Based on an analysis of features in the latest library and this application's current feature set, I suggest exploring \[New Feature\] (e.g., Prepaid Plans or Installments) from the latest release because it is now available but not yet implemented."

---

<!-- BEGIN LOCAL WRAPPER -->
<!-- Not from upstream. Source: local-wrapper.md. Re-applied on every sync;
     edit that file, never this block. -->

## Anti-fabrication override (read before Phase 2)

Phase 2 above instructs you to *"consult your knowledge of the Google Play Billing
documentation."* **Treat that as a pointer to go read the docs, not a licence to
recall them.** Billing API surface, version minimums, and deprecation timelines
change frequently, and a confidently wrong version number sends a developer into a
migration they did not need.

While running this skill:

- Do **not** state a PBL version number, `compileSdk`/`targetSdk` minimum, API
  signature, or deprecation deadline unless you read it in this session from the
  bundled `references/` or an official page.
- Anything unverified is written `[VERIFY: <what to confirm, and where>]`. Never
  substitute a plausible value.
- The bundled `references/android/google/play/billing/release-notes.md` is a snapshot
  pinned to this skill's `last-updated` date. If the migration target is newer than
  that snapshot, say so and verify against the live release notes.
- Do not assert what a specific PBL version "removed" or "introduced" from memory.
  Cite the release-notes entry.

This overrides any conflicting instruction above.

## When NOT to Use This Skill

Do NOT use this skill when:

- **You are integrating Play Billing for the first time.** This is an upgrade path
  that reasons from an existing effective version. Fresh integrations should start
  from the current official getting-started guide.
- **You are designing or changing subscription products** — base plans, offers,
  prepaid plans, grace periods. Use
  [`android-play-billing-subscriptions`](../android-play-billing-subscriptions/).
- **The app does not ship through Google Play** (sideloaded, enterprise, alternative
  store). Play Billing may not apply at all.
- **Only server-side purchase verification is broken.** That is backend work; this
  skill migrates client library usage.
- **The build is already failing for unrelated reasons.** Phase 1 uses build success
  as its discovery signal, so a pre-existing red build corrupts the version detection.

## Related Skills

- [`android-play-billing-subscriptions`](../android-play-billing-subscriptions/) —
  subscription product design, the usual follow-on once the library is current.
- [`android-agp-9-upgrade`](../android-agp-9-upgrade/) — a PBL bump often forces AGP,
  Kotlin, or `compileSdk` minimums. If both are due, sequence AGP first.
- [`android-play-policy-insights`](../android-play-policy-insights/) — billing
  changes carry policy surface (subscription terms disclosure, purchase flows).
- [`mobile-store-policy-readiness`](../mobile-store-policy-readiness/) — verify
  monetization disclosure before submitting the release.
- [`android-release-pipeline`](../android-release-pipeline/) — billing changes need
  testing against real Play test tracks, not just a local build.
