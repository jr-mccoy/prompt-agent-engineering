---
title: "Firebase Remote Config Strategy"
category: mobile-development
description: "Design a Remote Config strategy — feature flags, A/B testing setup, gradual rollouts, maintenance mode toggles, emergency kill switches, parameter naming conventions, condition hierarchies, and default values strategy"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - android
  - firebase
  - remote-config
  - feature-flags
  - a-b-testing
  - solo-developer
updated: "2026-02-11"
---

# Firebase Remote Config Strategy

**Objective:** Design a comprehensive Firebase Remote Config strategy for an Android app — covering feature flag architecture, A/B testing integration, gradual rollout procedures (1% to 10% to 50% to 100%), maintenance mode toggles, emergency kill switches, parameter naming conventions, condition hierarchies (platform, version, user segment), and default values strategy — producing a Remote Config plan that enables safe feature delivery and rapid incident response without app store updates.

**When to Use:** Use this prompt when launching new features and you need a safe rollout mechanism, when you want A/B testing capability without third-party tools, when you need emergency controls to disable features without deploying, or when your app has grown beyond "deploy and pray" and needs operational maturity. Critical because Remote Config is the cheapest form of insurance — a well-designed kill switch can save you from a 1-star review avalanche when a feature breaks in production.

**Important context:** The biggest mistake solo developers make with Remote Config is treating it as a simple key-value store. Remote Config's real power is in its condition system — you can target parameters by platform, app version, user segment, country, and random percentile. This means you can roll out features to 1% of users, run A/B tests, and instantly disable broken features — all without touching your codebase. But this power requires discipline: without naming conventions and a parameter lifecycle plan, Remote Config becomes an unmaintainable mess of stale flags within months.

---

## Context Gathering

Before designing the Remote Config strategy, gather essential context:

1. **App and Release Context:**
   - "What is your current release cadence (weekly, biweekly, monthly)?"
   - "How many active app versions are typically in the wild?"
   - "Do you have a staged rollout process on Google Play, or do you release to 100% immediately?"
   - "Have you ever needed to emergency-disable a feature post-release?"

2. **Current State:**
   - "Is Firebase Remote Config already integrated in your app?"
   - "Are you using any feature flag system currently (hardcoded booleans, BuildConfig flags)?"
   - "How do you currently handle features that are not ready for all users?"
   - "Do you have any A/B tests running or planned?"

3. **Feature and Risk Context:**
   - "What features are you planning to launch in the next 1-3 months?"
   - "Which features interact with external services that could fail?"
   - "Do you have features that are high-risk (payments, data migration, new UI)?"
   - "Have you experienced production incidents that required emergency action?"

4. **User Segmentation:**
   - "Do you have distinct user segments (free vs. paid, new vs. returning)?"
   - "Are there features that should only be available in certain countries or languages?"
   - "Do you need beta tester groups for early access?"
   - "How do you identify internal/test users?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY Remote Config parameter, you MUST:**

1. **Verify a config parameter is needed** — Not every feature needs a remote flag. If the feature is low-risk, fully tested, and not experimental, a simple code deploy is fine. Over-flagging creates maintenance debt.
2. **Define the parameter lifecycle** — Every flag should have a planned removal date. Feature flags that live forever become technical debt and confuse future developers (including future you).
3. **Set correct defaults** — The in-app default value must be the SAFE value. If Remote Config fetch fails (no network, service outage), your app should behave conservatively. A feature flag default of `true` means the feature is ON even if Remote Config is unreachable.
4. **Test the off state** — Every feature behind a flag must work correctly when the flag is OFF. This sounds obvious but is the #1 source of flag-related bugs — developers only test the happy path with the flag enabled.
5. **Document conditions clearly** — Every condition in Remote Config should be named descriptively and documented. "Condition 1" tells no one anything three months later.

### False-Positive Prevention

- Do NOT recommend putting every feature behind a flag — only flag features that need gradual rollout, A/B testing, or emergency controls
- Do NOT set default values to the "new" behavior — defaults should always be the safe/existing behavior
- Do NOT create A/B tests without defining success metrics and a decision timeline
- Do NOT skip in-app defaults — relying entirely on server values means broken behavior when fetch fails
- Do NOT create conditions based on ephemeral criteria that will be stale in weeks
- DO define a naming convention before creating any parameters
- DO plan for parameter cleanup after features are fully rolled out
- DO test with Remote Config fetch disabled to verify safe defaults
- DO include a kill switch for any feature that calls external services
- DO document what each condition targets and why

---

### Phase 1: Parameter Design and Naming Convention

#### 1.1 Parameter Naming Convention

Adopt a strict naming convention before creating any parameters. Remote Config parameter keys must be alphanumeric with underscores, max 256 characters.

**Recommended convention:**

```
[category]_[feature]_[property]
```

| Category Prefix | Purpose | Examples |
|----------------|---------|----------|
| `feature_` | Feature flags (on/off) | `feature_dark_mode_enabled` |
| `rollout_` | Gradual rollout percentages | `rollout_new_editor_percent` |
| `config_` | Configuration values | `config_sync_interval_seconds` |
| `experiment_` | A/B test parameters | `experiment_onboarding_variant` |
| `kill_` | Emergency kill switches | `kill_payment_processing` |
| `maint_` | Maintenance mode flags | `maint_api_v2_down` |
| `ui_` | UI customization | `ui_home_banner_text` |

**Naming rules:**
- Use `snake_case` exclusively
- Be descriptive: `feature_photo_filters_enabled` not `pf_on`
- Include the value type hint when ambiguous: `config_cache_ttl_seconds` not `config_cache_ttl`
- Never abbreviate feature names
- Group related parameters with the same prefix: `feature_editor_*`, `feature_search_*`

#### 1.2 Parameter Lifecycle States

Every parameter should have a documented lifecycle:

```markdown
| State | Description | Action Required |
|-------|-------------|----------------|
| **DRAFT** | Defined but not yet in Remote Config console | Create parameter, set default to OFF |
| **TESTING** | Active in dev/staging, not yet in production conditions | Test both ON and OFF states |
| **ROLLING_OUT** | Gradually increasing to production users | Monitor metrics at each stage |
| **FULLY_LAUNCHED** | Reached 100%, flag still active | Schedule flag removal |
| **CLEANUP** | Feature is permanent, flag should be removed | Remove flag, hardcode behavior |
| **ARCHIVED** | Removed from code and console | Delete from Remote Config |
```

**Target timeline for flag cleanup:**
- Feature flags: Remove within 2 release cycles after 100% rollout
- Kill switches: Keep permanently (these are operational controls, not feature flags)
- A/B test parameters: Remove within 1 release cycle after decision made
- Config values: Keep as long as the feature exists (these are operational tuning knobs)

#### 1.3 Default Values Strategy

The in-app default is the most critical value — it determines app behavior when Remote Config is unreachable.

```kotlin
// Remote Config defaults — these are your safety net
val defaults = mapOf(
    // Feature flags — default to OFF (safe state)
    "feature_new_editor_enabled" to false,
    "feature_ai_suggestions_enabled" to false,
    "feature_social_sharing_enabled" to false,

    // Kill switches — default to ALIVE (feature works normally)
    // A kill switch being TRUE means "kill this feature"
    "kill_payment_processing" to false,
    "kill_external_api_calls" to false,
    "kill_push_notifications" to false,

    // Maintenance flags — default to NOT in maintenance
    "maint_app_wide" to false,
    "maint_sync_service" to false,

    // Config values — default to conservative/existing values
    "config_sync_interval_seconds" to 300L,
    "config_max_upload_size_mb" to 10L,
    "config_cache_ttl_seconds" to 3600L,

    // Rollout percentages — default to 0 (no one gets it)
    "rollout_new_onboarding_percent" to 0L,

    // A/B test variants — default to control group
    "experiment_onboarding_variant" to "control",
    "experiment_pricing_page_variant" to "control",
)
```

**The golden rule:** If Firebase is completely down and your app can only use defaults, the user experience should be identical to today's stable version. No new features, no experiments, just the known-good behavior.

---

### Phase 2: Condition Setup and Hierarchy

#### 2.1 Condition Architecture

Remote Config conditions are evaluated top-to-bottom, first match wins. Design your condition hierarchy carefully.

**Recommended condition hierarchy (top to bottom):**

```
Priority 1: Emergency overrides (kill switches)
  └─ "All Users" — no conditions, applies universally

Priority 2: Internal/beta testers
  └─ Condition: User in "beta_testers" segment (Analytics audience)

Priority 3: Version-specific targeting
  └─ Condition: App version >= X.Y.Z

Priority 4: Platform targeting
  └─ Condition: Android (vs iOS if cross-platform)

Priority 5: Percentage rollout
  └─ Condition: User in random percentile (1%, 10%, 50%, 100%)

Priority 6: User segment targeting
  └─ Condition: User property matches (free/premium, country, etc.)

Priority 7: Default value
  └─ Applies to everyone not matching above conditions
```

#### 2.2 Condition Definitions

Create these standard conditions in your Remote Config console:

```markdown
| Condition Name | Criteria | Purpose |
|---------------|----------|---------|
| `Internal Testers` | User in audience "internal_testers" | Test features before any rollout |
| `Beta Users` | User in audience "beta_testers" | Early access for opted-in users |
| `Rollout 1 Percent` | User in random percentile <= 1% | Initial canary rollout |
| `Rollout 10 Percent` | User in random percentile <= 10% | Early adopter rollout |
| `Rollout 50 Percent` | User in random percentile <= 50% | Broad rollout |
| `Android Only` | Platform is Android | Platform-specific features |
| `Premium Users` | User property "user_tier" = "premium" | Premium-only features |
| `App Version 3+` | App version >= 3.0.0 | Version-gated features |
| `US Users` | Country/Region is United States | Geo-targeted features |
```

#### 2.3 Kotlin Implementation for Conditions

```kotlin
// Set up user properties for condition targeting
class RemoteConfigManager(
    private val analytics: FirebaseAnalytics,
    private val remoteConfig: FirebaseRemoteConfig
) {
    fun setUserSegment(tier: String) {
        // This user property can be used in Remote Config conditions
        analytics.setUserProperty("user_tier", tier)
    }

    fun markAsBetaTester() {
        analytics.setUserProperty("beta_tester", "true")
    }

    fun markAsInternalTester() {
        analytics.setUserProperty("internal_tester", "true")
    }
}
```

---

### Phase 3: Feature Flag Implementation

#### 3.1 Remote Config Initialization

```kotlin
class FirebaseRemoteConfigSetup {

    fun initialize(context: Context) {
        val remoteConfig = Firebase.remoteConfig

        // Set fetch interval based on build type
        val configSettings = remoteConfigSettings {
            // In debug: fetch every time (0 seconds)
            // In production: fetch every 12 hours (43200 seconds)
            minimumFetchIntervalInSeconds = if (BuildConfig.DEBUG) 0 else 43200
        }
        remoteConfig.setConfigSettingsAsync(configSettings)

        // Set in-app defaults (the safety net)
        remoteConfig.setDefaultsAsync(R.xml.remote_config_defaults)

        // Fetch and activate on app start
        remoteConfig.fetchAndActivate()
            .addOnCompleteListener { task ->
                if (task.isSuccessful) {
                    val updated = task.result
                    Log.d("RemoteConfig", "Config fetched and activated: $updated")
                } else {
                    Log.w("RemoteConfig", "Config fetch failed, using defaults")
                }
            }
    }
}
```

#### 3.2 Feature Flag Access Pattern

```kotlin
/**
 * Centralized feature flag access.
 * NEVER access RemoteConfig directly from UI code.
 * Always go through this object for:
 *   1. Single source of truth
 *   2. Easy to find all flag usages
 *   3. Easy to remove flags during cleanup
 */
object FeatureFlags {
    private val config get() = Firebase.remoteConfig

    // ---- Feature Flags ----
    val isNewEditorEnabled: Boolean
        get() = config.getBoolean("feature_new_editor_enabled")

    val isAiSuggestionsEnabled: Boolean
        get() = config.getBoolean("feature_ai_suggestions_enabled")

    val isSocialSharingEnabled: Boolean
        get() = config.getBoolean("feature_social_sharing_enabled")

    // ---- Kill Switches ----
    // TRUE = feature is KILLED (disabled)
    val isPaymentProcessingKilled: Boolean
        get() = config.getBoolean("kill_payment_processing")

    val isExternalApiKilled: Boolean
        get() = config.getBoolean("kill_external_api_calls")

    // ---- Maintenance Mode ----
    val isAppInMaintenance: Boolean
        get() = config.getBoolean("maint_app_wide")

    val isSyncServiceInMaintenance: Boolean
        get() = config.getBoolean("maint_sync_service")

    // ---- Config Values ----
    val syncIntervalSeconds: Long
        get() = config.getLong("config_sync_interval_seconds")

    val maxUploadSizeMb: Long
        get() = config.getLong("config_max_upload_size_mb")

    // ---- A/B Test Variants ----
    val onboardingVariant: String
        get() = config.getString("experiment_onboarding_variant")
}
```

#### 3.3 Using Feature Flags in Code

```kotlin
// In a Composable
@Composable
fun EditorScreen() {
    if (FeatureFlags.isNewEditorEnabled) {
        NewEditorContent()
    } else {
        LegacyEditorContent()
    }
}

// In a ViewModel
class PaymentViewModel : ViewModel() {
    fun processPayment(amount: Double) {
        // Kill switch check BEFORE any payment logic
        if (FeatureFlags.isPaymentProcessingKilled) {
            _uiState.value = PaymentUiState.ServiceUnavailable(
                message = "Payments are temporarily unavailable. Please try again later."
            )
            return
        }

        // Proceed with payment...
    }
}

// Maintenance mode check at app level
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            if (FeatureFlags.isAppInMaintenance) {
                MaintenanceModeScreen()
            } else {
                AppNavigation()
            }
        }
    }
}
```

---

### Phase 4: A/B Testing Setup

#### 4.1 A/B Test Design Framework

Before creating any A/B test, fill in this specification:

```markdown
## A/B Test: [Name]

**Hypothesis:** [Changing X will cause Y because Z]
**Primary metric:** [One metric that determines success/failure]
**Secondary metrics:** [2-3 supporting metrics]
**Variants:**
  - Control: [Current behavior — what users see today]
  - Variant A: [Changed behavior]
  - (Optional) Variant B: [Alternative changed behavior]
**Sample size needed:** [Calculate based on desired statistical significance]
**Duration:** [Minimum days to run — typically 14-28 days]
**Decision criteria:** [What constitutes a "winner"?]
**Rollback plan:** [How to revert if variant causes problems]
```

#### 4.2 Firebase A/B Testing Integration

```kotlin
// A/B test variant in Remote Config
// The parameter "experiment_onboarding_variant" will have values:
//   "control" — existing onboarding
//   "variant_a" — shorter onboarding (3 screens instead of 5)
//   "variant_b" — video onboarding

@Composable
fun OnboardingFlow() {
    when (FeatureFlags.onboardingVariant) {
        "variant_a" -> ShortOnboarding()
        "variant_b" -> VideoOnboarding()
        else -> StandardOnboarding() // "control" and any unknown value
    }
}

// Log experiment exposure for accurate analysis
fun logExperimentExposure(experimentName: String, variant: String) {
    Firebase.analytics.logEvent("experiment_exposure") {
        param("experiment_name", experimentName)
        param("variant", variant)
    }
}
```

#### 4.3 A/B Testing Checklist

```markdown
Before launching an A/B test:
- [ ] Hypothesis is documented with expected impact
- [ ] Primary success metric is defined and measurable
- [ ] Both control and variant(s) are fully implemented and tested
- [ ] Default value maps to control group (safety net)
- [ ] Experiment exposure event is logged when user sees variant
- [ ] Sample size calculated (use an online power calculator)
- [ ] Duration planned (minimum 14 days, ideally 28)
- [ ] Rollback procedure documented (set condition to 0%)
- [ ] No other experiments running on the same user flow

After the test concludes:
- [ ] Results analyzed with statistical significance
- [ ] Decision made (ship variant, keep control, iterate)
- [ ] Winning variant rolled out to 100%
- [ ] Experiment parameter scheduled for cleanup
- [ ] Learnings documented for future experiments
```

---

### Phase 5: Kill Switches and Emergency Controls

#### 5.1 Kill Switch Architecture

Kill switches are NOT feature flags — they are operational controls that should NEVER be removed.

```kotlin
/**
 * Kill switch naming convention:
 *   kill_[feature_area]
 *
 * Kill switch semantics:
 *   false = feature is ALIVE (normal operation)
 *   true  = feature is KILLED (disabled, show fallback)
 *
 * Kill switches should exist for:
 *   1. Any feature that calls external APIs
 *   2. Any feature that processes payments
 *   3. Any feature that depends on a specific backend version
 *   4. Any feature that has caused production incidents before
 */

object KillSwitches {
    private val config get() = Firebase.remoteConfig

    // External service dependencies
    val isPaymentKilled: Boolean
        get() = config.getBoolean("kill_payment_processing")

    val isExternalApiKilled: Boolean
        get() = config.getBoolean("kill_external_api_calls")

    val isPushNotificationsKilled: Boolean
        get() = config.getBoolean("kill_push_notifications")

    // Feature-specific kill switches
    val isImageUploadKilled: Boolean
        get() = config.getBoolean("kill_image_upload")

    val isSyncKilled: Boolean
        get() = config.getBoolean("kill_sync_service")

    // Master kill switch — disables all non-essential features
    val isEmergencyModeActive: Boolean
        get() = config.getBoolean("kill_emergency_mode")
}
```

#### 5.2 Kill Switch Usage Pattern

```kotlin
// Wrap external service calls with kill switch checks
class ImageUploadService(
    private val storage: FirebaseStorage
) {
    suspend fun uploadImage(uri: Uri): Result<String> {
        if (KillSwitches.isImageUploadKilled) {
            return Result.failure(
                ServiceUnavailableException("Image upload is temporarily disabled")
            )
        }

        return try {
            val ref = storage.reference.child("images/${UUID.randomUUID()}")
            ref.putFile(uri).await()
            val url = ref.downloadUrl.await().toString()
            Result.success(url)
        } catch (e: Exception) {
            Result.failure(e)
        }
    }
}

// Emergency mode: minimal app functionality
@Composable
fun AppRoot() {
    when {
        KillSwitches.isEmergencyModeActive -> EmergencyModeScreen()
        FeatureFlags.isAppInMaintenance -> MaintenanceModeScreen()
        else -> NormalAppContent()
    }
}
```

#### 5.3 Emergency Response Procedure

When a production incident occurs:

```markdown
## Emergency Response Runbook

### Step 1: Assess (< 2 minutes)
- What is broken? (crashes, data corruption, wrong behavior)
- How many users are affected? (check Crashlytics, Analytics)
- Is the issue caused by a feature that has a kill switch?

### Step 2: Mitigate (< 5 minutes)
- If kill switch exists: Toggle it in Firebase Console
  1. Open Firebase Console → Remote Config
  2. Find the relevant kill_* parameter
  3. Set default value to `true` (kills the feature)
  4. Click "Publish changes"
  5. Users receive the update on next fetch (within 12 hours)
     For immediate effect: temporarily set fetch interval to 0

- If no kill switch exists: Consider staged Play Store rollout halt
  1. Open Google Play Console
  2. Halt the staged rollout
  3. Push a hotfix build

### Step 3: Communicate (< 10 minutes)
- Update app status page (if you have one)
- Respond to recent 1-star reviews mentioning the issue

### Step 4: Fix (hours/days)
- Root cause analysis
- Code fix with regression test
- Deploy fix, verify, then re-enable killed feature

### Step 5: Postmortem
- Document what happened and why
- Add kill switch if one was missing
- Update monitoring/alerts
```

---

### Phase 6: Maintenance Mode and Operational Controls

#### 6.1 Maintenance Mode Implementation

```kotlin
// Maintenance mode data class — allows custom messages from Remote Config
data class MaintenanceInfo(
    val isActive: Boolean,
    val message: String,
    val estimatedEndTime: String // ISO 8601 format
)

object MaintenanceConfig {
    private val config get() = Firebase.remoteConfig

    fun getMaintenanceInfo(): MaintenanceInfo {
        return MaintenanceInfo(
            isActive = config.getBoolean("maint_app_wide"),
            message = config.getString("maint_message").ifEmpty {
                "We're performing scheduled maintenance. Please check back shortly."
            },
            estimatedEndTime = config.getString("maint_estimated_end")
        )
    }

    fun isServiceInMaintenance(service: String): Boolean {
        return config.getBoolean("maint_${service}")
    }
}

// Maintenance screen
@Composable
fun MaintenanceModeScreen() {
    val info = MaintenanceConfig.getMaintenanceInfo()

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(32.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Icon(
            imageVector = Icons.Default.Build,
            contentDescription = null,
            modifier = Modifier.size(64.dp)
        )
        Spacer(modifier = Modifier.height(24.dp))
        Text(
            text = "Under Maintenance",
            style = MaterialTheme.typography.headlineMedium
        )
        Spacer(modifier = Modifier.height(16.dp))
        Text(
            text = info.message,
            style = MaterialTheme.typography.bodyLarge,
            textAlign = TextAlign.Center
        )
        if (info.estimatedEndTime.isNotEmpty()) {
            Spacer(modifier = Modifier.height(8.dp))
            Text(
                text = "Expected back: ${info.estimatedEndTime}",
                style = MaterialTheme.typography.bodyMedium,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
        }
    }
}
```

#### 6.2 Gradual Rollout Procedure

Follow this rollout procedure for every new feature:

```markdown
## Gradual Rollout Checklist: [Feature Name]

### Stage 0: Internal Testing (Day 1-3)
- [ ] Parameter created: `feature_[name]_enabled` = false (default)
- [ ] Condition "Internal Testers" set to true
- [ ] Internal team tests feature for 2-3 days
- [ ] No crashes or regressions reported
- [ ] Kill switch created: `kill_[name]` = false (default)

### Stage 1: Canary — 1% (Day 4-7)
- [ ] Condition "Rollout 1 Percent" set to true
- [ ] Monitor for 3+ days:
  - [ ] Crash-free rate unchanged (check Crashlytics)
  - [ ] No spike in error events (check Analytics)
  - [ ] No negative user feedback
  - [ ] Feature metrics look reasonable

### Stage 2: Early Adopters — 10% (Day 8-14)
- [ ] Condition "Rollout 10 Percent" set to true
- [ ] Monitor for 5+ days:
  - [ ] Crash-free rate remains above 99.5%
  - [ ] Feature engagement metrics within expected range
  - [ ] No support tickets related to new feature
  - [ ] Performance metrics (ANR rate, startup time) unchanged

### Stage 3: Broad — 50% (Day 15-21)
- [ ] Condition "Rollout 50 Percent" set to true
- [ ] Monitor for 7+ days:
  - [ ] All Stage 2 criteria still passing
  - [ ] A/B comparison: 50% with feature vs 50% without
  - [ ] Revenue/conversion impact assessed (if applicable)

### Stage 4: General Availability — 100% (Day 22+)
- [ ] Default value changed to true (all users)
- [ ] All rollout conditions removed (cleanup)
- [ ] Monitor for 1 release cycle
- [ ] Schedule flag removal from code

### Rollback at Any Stage
If any metric degrades:
1. Set feature parameter back to false for affected condition
2. Investigate root cause
3. Fix and restart from Stage 1
```

---

## Expected Output

### Remote Config Strategy Document

```markdown
# Remote Config Strategy: [App Name]

## Naming Convention
[Prefix rules and examples — copy from Phase 1.1]

## Parameter Inventory

### Feature Flags
| Parameter | Default | Current State | Lifecycle Stage | Cleanup Date |
|-----------|---------|--------------|-----------------|-------------|
| feature_[name]_enabled | false | Rolling out (10%) | ROLLING_OUT | [date] |
| feature_[name]_enabled | true | Fully launched | CLEANUP | [date] |

### Kill Switches (Permanent)
| Parameter | Default | Current State | Last Activated |
|-----------|---------|--------------|----------------|
| kill_payment_processing | false | Normal | Never |
| kill_external_api_calls | false | Normal | 2026-01-15 |

### Maintenance Flags
| Parameter | Default | Current State |
|-----------|---------|--------------|
| maint_app_wide | false | Normal |
| maint_sync_service | false | Normal |

### Config Values
| Parameter | Default | Current Value | Range |
|-----------|---------|--------------|-------|
| config_sync_interval_seconds | 300 | 300 | 60-3600 |
| config_max_upload_size_mb | 10 | 10 | 1-50 |

### A/B Tests
| Parameter | Variants | Status | Start Date | Decision Date |
|-----------|----------|--------|------------|--------------|
| experiment_onboarding_variant | control, variant_a | Running | [date] | [date] |

## Condition Hierarchy
[Priority-ordered conditions from Phase 2.1]

## Gradual Rollout Procedure
[Checklist from Phase 6.2]

## Emergency Response Runbook
[Procedure from Phase 5.3]

## Parameter Lifecycle Policy
[States and timelines from Phase 1.2]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Remote Config strategy focus with explicit scope
- **ST-02** (Structured Sequential Instructions) - Phased implementation from parameter design through operational controls
- **RT-02** (Multi-Dimensional Analysis) - Feature flags, kill switches, maintenance, A/B testing, and config values as distinct parameter types
- **CM-01** (Explicit Context Framing) - Remote Config capabilities, condition system, and fetch behavior
- **DS-06** (Prioritization Guidance) - Condition hierarchy, rollout stages, and parameter lifecycle

---

## Related Prompts

- `firebase_analytics_strategy.md` - Analytics events that power Remote Config conditions and A/B test metrics
- `firebase_crashlytics_workflow.md` - Crash monitoring during gradual rollouts
- `firebase_cloud_functions_design.md` - Server-side logic that may need kill switches
- `firebase_app_check_setup.md` - App attestation that pairs with feature gating
- `firebase_cost_optimization.md` - Cost controls related to config fetch frequency

---

## Customization Guide

- **For apps with multiple platforms (Android + iOS):** Add platform-specific conditions to every parameter. Use the `Android Only` and `iOS Only` conditions to roll out platform-specific fixes independently.
- **For apps with premium tiers:** Layer user segment conditions (free/premium) into the rollout process. Consider giving premium users early access to features as a perceived benefit.
- **For apps with frequent releases (weekly):** Shorten the rollout timeline (1 day per stage instead of 3-7 days). Use Remote Config primarily for kill switches and A/B tests rather than rollout gating, since your release cycle is already fast.
- **For apps with seasonal traffic (e-commerce, events):** Create a "freeze" condition that locks all feature flags during peak traffic periods. No rollouts during Black Friday.
- **For apps just starting out (< 1000 DAU):** Skip the percentage-based rollout (your user base is too small for statistical significance). Use Remote Config for kill switches and config values only. Add A/B testing when you reach 5000+ DAU.
