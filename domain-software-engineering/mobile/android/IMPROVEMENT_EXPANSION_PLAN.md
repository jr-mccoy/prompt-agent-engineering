# Android Prompt Library — Review & Improvement/Expansion Plan

**Scope:** `domain-software-engineering/mobile/android/` (181 prompts across 8 lifecycle subdirectories)
**Reviewed:** 2026-07-03
**Status:** PLAN — no phase executed yet

---

## Part 1 — Review Findings

### 1.1 Current state

| Subdirectory | Prompts | Local README | Notes |
|---|---|---|---|
| `analysis/` | 30 | ✅ | Strongest cluster; consistent frontmatter, good workflows |
| `targeted-reviews/` | 45 | ✅ | Sharpest Tier-1 review prompts, but contains 15 misfiled Firebase prompts |
| `planning/` | 27 | ✅ | Broad; several files missing false-positive prevention |
| `maintenance/` | 21 | ✅ | Recently expanded, high quality |
| `improvement/` | 19 | ✅ | Good; a few overlap pairs |
| `publishing/` | 17 | ❌ | Mixed naming conventions, several placeholder descriptions |
| `implementation/` | 11 | ❌ | **Weakest cluster** — see 1.3 |
| `testing/` | 11 | ❌ | 6 newer prompts are Tier 1; 5 legacy ones lag |

This is the largest platform library in the repo (iOS: 103 prompts). Coverage of the analysis/review/maintenance side of the lifecycle is excellent; the build/implement side and modern form factors are the thin spots.

### 1.2 Documentation drift (highest-visibility problem)

- **`android/README.md` is badly stale.** The Quick Navigation table contains *duplicate, contradictory rows* (Implementation listed twice — once "Coming Soon", once with a real entry; same for Testing). The per-phase tables list only a fraction of actual content: Improvement shows 7 of 19, Planning 6 of 27, Publishing 6 of 17. The "Legacy Prompts (In Parent Directory)" section refers to six files that were migrated into `android/` long ago — the section is pure noise now.
- **`mobile/README.md` counts are stale**: claims android = 134 prompts (actual: 181), per-subdir counts wrong (analysis "19" vs 30, maintenance "10" vs 21, testing "6" vs 11, etc.), total "255" undercounts.
- **Root `CLAUDE.md`** routes to `mobile/` with "~255 prompts" — needs a refresh after counts are fixed.

### 1.3 Quality-tier gaps (against PROMPT_QUALITY_STANDARDS.md)

Scan results across all 181 prompts:

| Defect | Count | Concentration |
|---|---|---|
| Missing `techniques:` frontmatter | 20 | All 10–11 `implementation/` files, 5 `publishing/`, 5 legacy `testing/` |
| Empty `description: ""` | 1 | `implementation/android_in_app_billing.md` |
| Placeholder description (title restated) | 5 | `publishing/android_privacy_compliance.md`, `android_staged_rollout.md`, `android_play_store_optimization.md`, `targeted-reviews/android_room_migration_safety_audit.md`, `android_compose_recomposition_review.md` |
| No Verification/self-check section | 18 | 9 of 11 `implementation/`, 4 legacy `testing/`, 2 `planning/`, 2 `publishing/`, 1 `targeted-reviews/` |
| No False-Positive Prevention (the #1 Tier-1 differentiator) | 36 | All 11 `implementation/`, 9 of 11 `testing/`, 8 `planning/`, 4 `publishing/`, 3 `improvement/`, 1 `analysis/` |
| Missing `related_prompts:` field | 66 | Spread across all subdirs |
| `related_prompts: []` (present but empty) | 30 | Mostly `targeted-reviews/` |

**Conclusion:** `implementation/` is a wholesale pre-Tier-1 generation — every file lacks techniques, verification, and FPP. The 5 legacy `testing/` files (`android_unit_test_generation`, `android_compose_ui_testing`, `android_integration_testing`, `android_screenshot_testing`, `android_test_strategy_design`) share the same vintage.

### 1.4 Organizational issues

1. **Same-filename duplicate:** `analysis/android_dependency_audit.md` (238 lines, version-freshness focus) vs `maintenance/android_dependency_audit.md` (478 lines, CVE + abandonment-risk + paydown plan). Identical filename in two subdirs is a routing hazard; the maintenance version supersedes the analysis one.
2. **Near-duplicate pair:** `targeted-reviews/android_compose_recomposition_review.md` vs `android_compose_recomposition_problems_review.md` — both have placeholder descriptions; distinction (if any) is undocumented.
3. **Undifferentiated pairs needing explicit scope notes, not merging:**
   - `implementation/android_state_management.md` (empty description) vs `android_compose_state_management.md`
   - `improvement/android_kotlin_refactoring.md` vs `android_kotlin_refactoring_generalized.md`
4. **15 misfiled Firebase prompts in `targeted-reviews/`.** Files like `firebase_auth_implementation.md`, `firebase_emulator_suite_setup.md`, `firebase_analytics_strategy.md`, `firebase_cloud_functions_design.md`, `firebase_incident_response.md`, `firebase_cost_monitor_setup.md` are implementation/setup/strategy/ops prompts, not reviews. Only a handful (`firebase_security_rules_*` as audit, `firestore_query_optimization`, `firebase_health_check`) fit the "targeted review" contract that the mobile README advertises ("scoped to a single concern with verification requirements and false-positive prevention").
5. **Naming convention split:** 11 `publishing/` files and all 15 Firebase files lack the `android_` prefix. Not fatal (they are Android-scoped by directory), but inconsistent with the repo's `{category}_{specific_function}.md` convention and with every other file in the tree.

### 1.5 Cross-linking gaps

- **One-way link with the Android vibe-rescue set.** `vibe-coding-rescue/android/` links into this directory 4 times; nothing here links back. Users landing here with a broken AI-generated app never discover the rescue pipeline.
- **No routing to runnable counterparts.** `domain-agentic-resources/` contains ~30 Android skills (`android-room-database`, `android-agp-9-upgrade`, `android-navigation-3`, `android-play-billing-subscriptions`, `android-xr-jetpack-compose-glimmer`, …), 10+ Android agents, and 13 mobile-development commands. The README never mentions them, so users copy-paste prompts for tasks that have a packaged skill.
- 96 prompts have missing or empty `related_prompts`, weakening index-driven discovery.

### 1.6 Coverage gaps (expansion candidates)

Well covered: architecture, Compose UI quality, security/privacy audits, sync/offline, Room, Hilt, performance, release/Play Store, incident lifecycle, dependency/toolchain upgrades.

**Thin or absent:**

| Area | Gap |
|---|---|
| Notifications | Only a channel *review* exists — no notifications/FCM push implementation prompt (rich notifications skill exists with no prompt counterpart) |
| Media & camera | No CameraX capture, no Media3/ExoPlayer playback prompts |
| Lists at scale | No Paging 3 implementation prompt |
| App widgets | No Glance/app-widget prompt |
| Auth & crypto build-side | Audits exist (Keystore, auth, SQLCipher) but no biometric-auth + Keystore/EncryptedFile *implementation* prompt |
| Permission UX | Manifest *audit* exists; no runtime-permission UX flow implementation |
| Play platform APIs | No in-app updates / in-app review API, no Play Integrity API prompt |
| WebView | Security audits mention it; no WebView hardening implementation |
| On-device AI | Planning-level only (`android_ondevice_ai_feature_plan.md`); no implementation prompt (Gemini Nano / ML Kit / LiteRT) |
| Form factors | No Wear OS, Android TV, Auto/Automotive, or XR prompts (only strategy-level `device_support_and_form_factor_strategy`); adaptive/foldable exists only as one improvement prompt |
| Modern-stack migrations | No Navigation 3, K2/Kotlin 2.x, or KSP2 migration prompts (AGP-9 and Navigation-3 *skills* exist without prompt counterparts) |
| Perf testing | Baseline-profiles improvement exists, but no Macrobenchmark/Microbenchmark test-authoring prompt |
| 2025+ platform requirements | No 16 KB page-size migration prompt, no privacy-sandbox/ad-ID prompt |
| Connectivity/hardware | No BLE/Bluetooth, no location/maps implementation (only a geofence review) |

---

## Part 2 — Phased Plan

Phases are ordered so that each is independently shippable; 1–3 are hygiene (no new content), 4–6 are expansion.

### Phase 1 — Documentation & counts hygiene *(low risk, highest visible payoff)*

1. Rewrite `android/README.md`:
   - Fix the Quick Navigation table (remove duplicate/"Coming Soon" rows).
   - Replace exhaustive-but-stale per-phase tables with **curated highlights + a link to each subdir README** (the pattern `analysis/` and `maintenance/` already use). Full catalogs live in subdir READMEs, which stay closer to the files they index.
   - Delete the stale "Legacy Prompts" section.
   - Add a **Related Resources** section: `vibe-coding-rescue/android/` (rescue pipeline), `domain-agentic-resources/skills/mobile-development/` (runnable skills), `agents/frontend-mobile/`, `commands/mobile-development/`, and `cross-platform/migration/`.
   - Refresh the footer date/counts.
2. Create the three missing subdir READMEs: `implementation/README.md`, `publishing/README.md`, `testing/README.md` (catalog table + when-to-use + workflow, mirroring `maintenance/README.md`).
3. Update `mobile/README.md` counts and structure block; correct android per-subdir numbers.
4. Update the mobile counts line in root `CLAUDE.md`.

**Acceptance:** every count in the three READMEs matches `find`-verified reality; no dead or stale rows.

### Phase 2 — Tier-1 remediation of existing prompts

Priority order by defect concentration:

1. **`implementation/` (11 files):** add `techniques:` (typical set: ST-01/ST-02/CM-02/RT-02/QA-01), real descriptions (fix the empty `android_in_app_billing.md`), a **Verification** section (build/test/manual-check gates appropriate to implementation prompts), and **False-Positive Prevention** (e.g., "do not report missing acknowledgment handling if the app uses server-side acknowledgment").
2. **Legacy `testing/` (5 files):** same treatment; align with the 6 newer Tier-1 testing prompts.
3. **Remaining FPP gaps (20 files)** in planning/publishing/improvement/analysis.
4. **Fix the 5 placeholder descriptions.**
5. **`related_prompts` pass:** populate the 30 empty arrays and 66 missing fields with 2–4 genuine neighbors each (analysis ↔ improvement ↔ targeted-review chains; implementation → testing → publishing chains). Two-way links.
6. Regenerate `PROMPT_INDEX.json` / `PROMPT_INDEX.md` afterward (script if present, else targeted edits).

**Acceptance:** zero files missing techniques/description; zero implementation or testing files without Verification + FPP; spot-check 10 random `related_prompts` targets resolve to real paths.

### Phase 3 — Structural cleanup

1. **Dependency-audit duplicate:** fold anything unique from `analysis/android_dependency_audit.md` into the superior `maintenance/` version, then replace the analysis file's body with the merged content moved to maintenance **or** delete it and update all inbound references (analysis README + related_prompts). Recommended: keep only `maintenance/android_dependency_audit.md`.
2. **Recomposition pair:** diff the two; merge into one authoritative `android_compose_recomposition_review.md` (or give each a real, disjoint scope — e.g., proactive stability audit vs. symptom-driven jank diagnosis) and write honest descriptions either way.
3. **State-management & refactoring pairs:** keep both files but add explicit "vs." scope notes in *When to Use* + cross-links so a router can choose.
4. **Firebase relocation:** create `android/firebase/` (or move files to their true lifecycle homes) for the 15 `firebase_*`/`firestore_*` prompts; keep genuine audits (`firebase_security_rules_audit` already exists as `android_firebase_security_rules_audit.md`, `firestore_query_optimization`, `firebase_health_check`) in `targeted-reviews/` if preferred, move implementation/strategy/ops files out. Update `targeted-reviews/README.md`, main README, PROMPT_INDEX, and any inbound `related_prompts`.
5. **Naming:** document (don't mass-rename) the `play_store_*`/`privacy_*`/`firebase_*` prefix exception in the publishing/firebase READMEs — renames would break dozens of inbound references for cosmetic gain.

**Acceptance:** no duplicate filenames anywhere under `android/`; `targeted-reviews/` contains only single-concern review prompts; all moved files reachable from READMEs and index.

### Phase 4 — Expansion wave A: build-side & platform-API gaps (~13 prompts)

Highest-demand, evergreen topics; all `implementation/` unless noted:

| # | Prompt | Home |
|---|---|---|
| 1 | `android_notifications_fcm_implementation.md` — channels, FCM, rich notifications, permission flow | implementation |
| 2 | `android_camerax_capture_implementation.md` | implementation |
| 3 | `android_media3_playback_implementation.md` — ExoPlayer, MediaSession, background audio | implementation |
| 4 | `android_paging3_implementation.md` — network+DB paging, RemoteMediator | implementation |
| 5 | `android_glance_app_widget_implementation.md` | implementation |
| 6 | `android_biometric_keystore_implementation.md` — BiometricPrompt, Keystore-backed crypto | implementation |
| 7 | `android_runtime_permission_ux_implementation.md` — rationale flows, pre-prompts, denial recovery | implementation |
| 8 | `android_in_app_updates_review_api.md` — in-app updates + in-app review APIs | implementation |
| 9 | `android_webview_hardening_implementation.md` | implementation |
| 10 | `android_ondevice_ai_implementation.md` — ML Kit / Gemini Nano / LiteRT (companion to the existing planning prompt) | implementation |
| 11 | `android_play_integrity_implementation.md` | implementation |
| 12 | `android_macrobenchmark_testing.md` — Macro/Microbenchmark authoring + CI wiring | testing |
| 13 | `android_16kb_page_size_migration.md` — native-lib audit + migration (2025 Play requirement) | maintenance |

All authored to Tier 1 from day one (techniques, Must/Must-Not constraints, Verification, FPP, `related_prompts` both directions). Each cross-links its audit/review sibling where one exists (e.g., #6 ↔ `android_local_data_security_audit.md`).

### Phase 5 — Expansion wave B: form factors & modern-stack migrations (~9 prompts)

| # | Prompt | Home |
|---|---|---|
| 1 | `android_wear_os_app_plan.md` — tiles, complications, health services, standalone vs companion | planning |
| 2 | `android_wear_os_implementation.md` | implementation |
| 3 | `android_tv_leanback_compose_implementation.md` | implementation |
| 4 | `android_automotive_auto_readiness_plan.md` | planning |
| 5 | `android_foldable_adaptive_deep_review.md` — window size classes, hinge, continuity (deepens the existing improvement prompt) | targeted-reviews |
| 6 | `android_navigation3_migration.md` (pairs with the `android-navigation-3` skill) | improvement |
| 7 | `android_kotlin2_k2_migration.md` — K2 compiler, KSP2, compiler-plugin fallout | maintenance |
| 8 | `android_kmp_shared_module_extraction.md` — executes the existing KMP architecture plan | improvement |
| 9 | `android_xr_readiness_assessment.md` (pairs with the `android-xr-jetpack-compose-glimmer` skill) | planning |

### Phase 6 — Cross-linking, routing & index finalization

1. Add "Rescue an AI-built Android app" callout in `android/README.md` → `vibe-coding-rescue/android/` (making the link two-way).
2. Add a **prompt ↔ skill map** table to the README for the ~10 prompt/skill twins (billing ↔ `android-play-billing-subscriptions`, Room reviews ↔ `android-room-database`, screenshot testing ↔ `android-screenshot-testing`, toolchain upgrade ↔ `android-agp-9-upgrade`, edge-to-edge ↔ `android-edge-to-edge`, …).
3. Update root `CLAUDE.md`: refresh the mobile count, and add 3–5 routing examples for the new high-traffic prompts (notifications, CameraX, Wear OS, 16 KB migration, Navigation 3).
4. Regenerate `PROMPT_INDEX.json`/`.md`; verify new-prompt entries carry keywords and techniques.

---

## Part 3 — Sequencing & effort summary

| Phase | Type | Files touched | New prompts | Risk |
|---|---|---|---|---|
| 1 | Docs hygiene | ~6 | 3 READMEs | None |
| 2 | Quality remediation | ~100 (mostly frontmatter-only) | 0 | Low |
| 3 | Structural cleanup | ~20 + moves | 0 | Medium (inbound refs) |
| 4 | Expansion A | 13 new + sibling cross-links | 13 | Low |
| 5 | Expansion B | 9 new + sibling cross-links | 9 | Low |
| 6 | Linking & index | ~5 + index | 0 | Low |

End state: **~203 prompts**, all Tier 1, zero documentation drift, two-way links to the rescue pipeline and agentic resources, and coverage extended across the build-side, platform-API, and form-factor gaps.

Recommended execution order: 1 → 2 → 3 (hygiene debt first, so new content lands in a clean structure), then 4 → 6 (index once after wave A), then 5 → 6 again. Phases 4 and 5 can each be split across sessions per-prompt without blocking anything.
