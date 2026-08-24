---
name: android-admob-mediation
description: Integrates Google AdMob with mediation adapters, UMP consent management for GDPR/CCPA, ad format selection (banner, interstitial, rewarded, native, app open), Compose ad wrappers, and subscriber ad suppression. Activates when implementing ads, ad mediation, consent management, or coordinating ad display with subscription entitlements in Android apps.
metadata:
  tags:
    - admob
    - android
    - mediation
    - mobile
  updated: "2026-04-11"
---
# Android AdMob & Mediation

Complete integration guide for Google AdMob in Android apps with Jetpack Compose. Covers ad format selection, consent management (UMP SDK), mediation setup, and coordination with billing to suppress ads for subscribers.

## Purpose

AdMob integration requires more than just displaying ads. It requires consent management (GDPR/CCPA compliance), strategic ad placement that doesn't degrade UX, mediation for optimal fill rates, and coordination with the billing layer to suppress ads for paying subscribers. This skill covers the complete ad integration lifecycle.

## When to Use This Skill

Use this skill when you need to:
- Integrate AdMob into an Android app with Jetpack Compose
- Implement GDPR/CCPA consent management with the UMP SDK
- Choose and implement appropriate ad formats
- Set up mediation with multiple ad networks
- Suppress ads for premium subscribers
- Optimize ad revenue without degrading user experience

## When NOT to Use This Skill

Do NOT use this skill when:
- Implementing in-app purchases or subscriptions (use android-play-billing-subscriptions)
- Designing overall monetization strategy (use android-monetization-architect agent)
- Building for iOS (use iOS AdMob documentation)
- Using a non-AdMob ad network exclusively

## Step 1: Add Dependencies

```kotlin
// build.gradle.kts (app module)
dependencies {
    implementation("com.google.android.gms:play-services-ads:23.1.0")
    // UMP SDK for consent
    implementation("com.google.android.ump:user-messaging-platform:2.2.0")
}
```

```xml
<!-- AndroidManifest.xml -->
<manifest>
    <application>
        <meta-data
            android:name="com.google.android.gms.ads.APPLICATION_ID"
            android:value="ca-app-pub-XXXXXXXXXXXXXXXX~YYYYYYYYYY" />
    </application>
</manifest>
```

## Step 2: Consent Management (UMP SDK)

**Required before loading any ads.** See `references/consent_management_ump.md` for complete details.

```kotlin
@Singleton
class ConsentManager @Inject constructor(
    @ApplicationContext private val context: Context,
) {
    private var consentInformation: ConsentInformation? = null

    fun requestConsentIfNeeded(activity: Activity, onReady: (Boolean) -> Unit) {
        val params = ConsentRequestParameters.Builder()
            .setTagForUnderAgeOfConsent(false)
            .build()

        consentInformation = UserMessagingPlatform.getConsentInformation(context)
        consentInformation?.requestConsentInfoUpdate(
            activity, params,
            {
                // Consent info updated
                if (consentInformation?.isConsentFormAvailable == true) {
                    loadAndShowConsentForm(activity, onReady)
                } else {
                    onReady(canRequestAds())
                }
            },
            { error ->
                // Error — proceed without personalized ads
                onReady(canRequestAds())
            }
        )
    }

    private fun loadAndShowConsentForm(activity: Activity, onReady: (Boolean) -> Unit) {
        UserMessagingPlatform.loadAndShowConsentFormIfRequired(activity) { error ->
            onReady(canRequestAds())
        }
    }

    fun canRequestAds(): Boolean {
        return consentInformation?.canRequestAds() ?: false
    }
}
```

## Step 3: Initialize Mobile Ads SDK

```kotlin
@Singleton
class AdManager @Inject constructor(
    @ApplicationContext private val context: Context,
    private val consentManager: ConsentManager,
    private val entitlementManager: EntitlementManager,
) {
    private var isInitialized = false

    fun initialize(activity: Activity) {
        consentManager.requestConsentIfNeeded(activity) { canShowAds ->
            if (canShowAds && !isInitialized) {
                MobileAds.initialize(context) {
                    isInitialized = true
                }
            }
        }
    }

    // Check both consent and subscription before showing ads
    suspend fun shouldShowAds(): Boolean {
        val isPremium = entitlementManager.isPremium.first()
        return !isPremium && consentManager.canRequestAds() && isInitialized
    }
}
```

## Step 4: Implement Ad Formats

See `references/ad_format_decision_tree.md` for format selection guidance.

### Banner Ads (Compose)

```kotlin
@Composable
fun AdBanner(
    adManager: AdManager,
    modifier: Modifier = Modifier,
) {
    val shouldShow by adManager.shouldShowAdsFlow.collectAsState(initial = false)

    if (!shouldShow) return

    AndroidView(
        modifier = modifier
            .fillMaxWidth()
            .height(50.dp),
        factory = { context ->
            AdView(context).apply {
                setAdSize(AdSize.BANNER)
                adUnitId = if (BuildConfig.DEBUG) {
                    "ca-app-pub-3940256099942544/6300978111" // Test ID
                } else {
                    "ca-app-pub-XXXX/YYYY" // Production ID
                }
                loadAd(AdRequest.Builder().build())
            }
        }
    )
}
```

### Interstitial Ads

```kotlin
@Singleton
class InterstitialAdManager @Inject constructor(
    @ApplicationContext private val context: Context,
    private val adManager: AdManager,
) {
    private var interstitialAd: InterstitialAd? = null

    fun preload() {
        val adRequest = AdRequest.Builder().build()
        val adUnitId = if (BuildConfig.DEBUG) {
            "ca-app-pub-3940256099942544/1033173712" // Test ID
        } else {
            "ca-app-pub-XXXX/YYYY"
        }

        InterstitialAd.load(context, adUnitId, adRequest,
            object : InterstitialAdLoadCallback() {
                override fun onAdLoaded(ad: InterstitialAd) {
                    interstitialAd = ad
                }
                override fun onAdFailedToLoad(error: LoadAdError) {
                    interstitialAd = null
                }
            })
    }

    suspend fun showIfEligible(activity: Activity): Boolean {
        if (!adManager.shouldShowAds()) return false
        val ad = interstitialAd ?: return false

        ad.fullScreenContentCallback = object : FullScreenContentCallback() {
            override fun onAdDismissedFullScreenContent() {
                interstitialAd = null
                preload() // Preload next
            }
        }
        ad.show(activity)
        return true
    }
}
```

### Rewarded Ads

```kotlin
@Singleton
class RewardedAdManager @Inject constructor(
    @ApplicationContext private val context: Context,
) {
    private var rewardedAd: RewardedAd? = null

    fun preload() {
        val adRequest = AdRequest.Builder().build()
        val adUnitId = if (BuildConfig.DEBUG) {
            "ca-app-pub-3940256099942544/5224354917" // Test ID
        } else {
            "ca-app-pub-XXXX/YYYY"
        }

        RewardedAd.load(context, adUnitId, adRequest,
            object : RewardedAdLoadCallback() {
                override fun onAdLoaded(ad: RewardedAd) { rewardedAd = ad }
                override fun onAdFailedToLoad(error: LoadAdError) { rewardedAd = null }
            })
    }

    fun show(activity: Activity, onRewarded: (RewardItem) -> Unit): Boolean {
        val ad = rewardedAd ?: return false
        ad.show(activity) { reward -> onRewarded(reward) }
        return true
    }
}
```

## Step 5: Ad Suppression for Subscribers

```kotlin
// In AdManager — Flow that combines consent + entitlement
val shouldShowAdsFlow: Flow<Boolean> = combine(
    entitlementManager.isPremium,
    flowOf(consentManager.canRequestAds()),
) { isPremium, hasConsent ->
    !isPremium && hasConsent
}

// In Compose screens — conditionally show ad placements
@Composable
fun HomeScreen(adManager: AdManager) {
    val showAds by adManager.shouldShowAdsFlow.collectAsState(initial = false)

    Column {
        // Content...

        if (showAds) {
            AdBanner(adManager)
        }

        // More content...
    }
}
```

## Step 6: Ad Placement Strategy

**Rules for non-intrusive ad placement:**
1. **Never interrupt active user tasks** — No interstitial during typing, navigating, or completing an action
2. **Natural transition points** — Show interstitials between screen transitions, after completing a task
3. **Bottom of scrollable content** — Banners at bottom of lists, after content ends
4. **Reward for value** — Rewarded ads to unlock extra gamification features, skip timers
5. **Frequency cap** — Max 1 interstitial per 5 minutes, no more than 3 per session

```kotlin
// Frequency capping
@Singleton
class AdFrequencyCap @Inject constructor() {
    private var lastInterstitialTime = 0L
    private var sessionInterstitialCount = 0
    private val minInterval = 5 * 60 * 1000L // 5 minutes
    private val maxPerSession = 3

    fun canShowInterstitial(): Boolean {
        val now = System.currentTimeMillis()
        return sessionInterstitialCount < maxPerSession &&
            (now - lastInterstitialTime) > minInterval
    }

    fun recordInterstitialShown() {
        lastInterstitialTime = System.currentTimeMillis()
        sessionInterstitialCount++
    }
}
```

## Common Issues

### Ads Not Loading in Debug
Use test ad unit IDs during development. Production IDs only work on signed release builds distributed via Play Store.

### Consent Form Not Showing
The UMP SDK only shows the consent form in regions where it's required (EEA). Use `ConsentDebugSettings` to test:
```kotlin
val debugSettings = ConsentDebugSettings.Builder(context)
    .setDebugGeography(ConsentDebugSettings.DebugGeography.DEBUG_GEOGRAPHY_EEA)
    .addTestDeviceHashedId("TEST_DEVICE_HASH")
    .build()
```

### Ads Showing to Subscribers
Ensure `EntitlementManager.isPremium` emits `true` before AdManager initializes. Check the Flow combination timing.

## Resources

### references/ad_format_decision_tree.md
Decision framework for choosing the right ad format based on screen type, user flow, and revenue goals.

### references/consent_management_ump.md
Complete UMP SDK implementation guide with GDPR and CCPA handling.

## Related Skills

- `android-play-billing-subscriptions` — Billing integration for ad suppression logic
- `jetpack-compose-patterns` — Compose patterns for ad integration
