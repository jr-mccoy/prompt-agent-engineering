---
title: "Ad Placement Strategy"
category: startup/monetization
description: "Design a non-intrusive ad strategy for an Android app — ad format comparison, placement timing rules, frequency capping, AdMob mediation setup with fallback networks, user experience preservation, and premium opt-out for solo developers"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - monetization
  - android
  - advertising
  - admob
  - ad-placement
  - mediation
  - solo-developer
updated: "2026-02-11"
---

# Ad Placement Strategy

**Objective:** Design a complete, non-intrusive ad strategy for an Android app — including ad format selection with realistic eCPM benchmarks, placement timing rules that never interrupt critical user flows, frequency capping logic, AdMob mediation setup with fallback networks (Unity Ads, Meta Audience Network, AppLovin), user experience preservation guidelines, and a premium upgrade path that removes ads — so that ad revenue supplements or sustains the app without degrading the experience that makes users stay.

**When to Use:** Use this after you have decided that ads are part of your monetization model (see `monetization_model_selector.md`). This prompt takes you from "I want ads in my app" to "here is exactly which formats go where, how often they show, what networks fill them, and how I protect the user experience." Use it before writing any ad integration code — poorly placed ads are the fastest way to earn 1-star reviews and drive users to competitors.

---

## Context Gathering

Before designing your ad strategy, gather essential context:

1. **App Usage Patterns:**
   - "How long is a typical user session (seconds, minutes, hours)?"
   - "How many sessions per day does a typical user have?"
   - "What are the natural pauses or transitions in the user flow?"
   - "Is your app used in focused, uninterrupted bursts or in casual, browsable sessions?"

2. **User Demographics:**
   - "What are your top 5 countries by user volume?"
   - "What is the age range of your users (affects COPPA/ad targeting)?"
   - "Are users consumers, professionals, or students?"
   - "How tolerant is your audience of ads? (Casual game users expect ads; productivity users hate them)"

3. **Current Metrics:**
   - "What is your current DAU (daily active users)?"
   - "What is your DAU/MAU ratio (stickiness)?"
   - "What is your retention rate at Day 1, Day 7, Day 30?"
   - "If you already have ads, what is your current eCPM and fill rate?"

4. **App Architecture:**
   - "Does your app have natural content breaks (between levels, articles, tasks)?"
   - "Are there optional actions users take that could be incentivized (hints, retries, bonus content)?"
   - "How many distinct screens does a typical session touch?"
   - "Are there loading screens or transition screens?"

5. **Revenue Goals and Constraints:**
   - "What is your monthly revenue target from ads?"
   - "Are ads the sole revenue source or part of a hybrid model?"
   - "Do you also offer a premium/subscription tier that removes ads?"
   - "What is your absolute minimum acceptable user experience standard?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before designing ANY ad placement strategy, you MUST:**

1. **Verify your DAU justifies ads** — Ad revenue is a volume game. At fewer than 1,000 DAU, ad revenue will be negligible (under $15/month with banners). If your DAU is below 1,000, consider whether the user experience cost of ads is worth the revenue. Focus on growing users first.
2. **Verify ads don't conflict with your value proposition** — If your app's selling point is "clean, distraction-free experience" (meditation, focus timer, reading), ads directly undermine your core promise. Either skip ads entirely or confine them to a single, dismissible banner.
3. **Verify you are not targeting children under 13** — COPPA and Google Play Families Policy impose strict restrictions on ad targeting for children. You must use certified ad SDKs, disable personalized ads, and avoid certain ad formats (interstitials with close timers, for example).
4. **Verify your ad placements pass the "friend test"** — Show your app with ads to a friend who uses your app. If they say "this is annoying," redesign. If they barely notice the ads, you have found good placements.
5. **Verify you have a premium escape hatch** — Always offer a way for users to pay to remove ads. Users who hate ads but love your app are your highest-value segment. Don't force them to leave.
6. **Acceptable null result** — It is valid to conclude that ads are not appropriate for your app. If your user base is small, your app is premium-focused, or ads would fundamentally compromise the experience, recommend deferring ads or skipping them entirely.

### False-Positive Prevention

- Do NOT place interstitials during active user input (typing, drawing, recording) — this causes data loss and rage
- Do NOT show ads immediately after app launch — users have not received value yet and will associate your app with annoyance
- Do NOT use ad formats that mimic UI elements (native ads that look like buttons or navigation) — this violates Google Play policy and erodes trust
- Do NOT show more than 1 interstitial per 3-minute window — excessive interstitials are the #1 reason users cite for uninstalling ad-supported apps
- Do NOT rely on a single ad network — fill rates drop to 60-80% and you lose 20-40% of potential revenue
- Do NOT disable ads for the first session and then surprise users with ads — this feels like bait-and-switch
- DO show ads at natural content boundaries (between levels, after saving, between articles)
- DO give users agency where possible (rewarded ads are user-initiated by definition)
- DO implement frequency capping to prevent ad fatigue
- DO track ad-related user exits and reduce frequency if correlation appears
- DO offer a clear "Remove Ads" purchase or subscription upgrade

---

### Phase 1: Ad Format Selection

#### 1.1 Ad Format Comparison

| Format | eCPM Range (US) | eCPM Range (Global Avg) | User Experience Impact | Best For | Implementation Effort |
|--------|-----------------|------------------------|----------------------|----------|----------------------|
| **Banner** | $0.30-$1.50 | $0.10-$0.50 | Low (persistent, ignorable) | Steady baseline revenue | Low (drop-in view) |
| **Interstitial** | $5.00-$15.00 | $2.00-$8.00 | High (full-screen interruption) | Revenue spikes at transitions | Medium (timing logic) |
| **Rewarded Video** | $10.00-$30.00 | $5.00-$15.00 | Positive (user-initiated) | Highest eCPM, best UX | Medium (reward logic) |
| **Native** | $3.00-$8.00 | $1.00-$4.00 | Low-Medium (blends into content) | Content-heavy apps, feeds | High (custom layout) |
| **App Open** | $8.00-$20.00 | $3.00-$10.00 | Medium (on cold start) | Passive revenue on launch | Low (lifecycle hook) |

**eCPM reality check:** These are US-centric numbers. If your audience is 70% India, Southeast Asia, or Latin America, divide by 3-8x. A "global average" app with mixed geo traffic typically sees:
- Banner: ~$0.20-$0.50 blended eCPM
- Interstitial: ~$3.00-$6.00 blended eCPM
- Rewarded: ~$8.00-$15.00 blended eCPM

#### 1.2 Format Selection Framework

Choose formats based on your app type:

```
App Type: Casual Game
  Recommended: Rewarded Video (primary) + Interstitial (secondary) + Banner (baseline)
  Rationale: Games have natural break points and users are trained to watch ads for rewards

App Type: Productivity / Utility
  Recommended: Banner (only) or Banner + Native (if content feed exists)
  Rationale: Productivity users are task-focused; interstitials destroy flow

App Type: Content / News / Reading
  Recommended: Native (in-feed) + Banner (article footer) + Interstitial (between articles)
  Rationale: Native blends into content stream; interstitials work at article transitions

App Type: Social / Communication
  Recommended: Native (in-feed) + Banner (non-chat screens)
  Rationale: Never interrupt conversations; ads in feeds are expected

App Type: Fitness / Health Tracking
  Recommended: Rewarded (bonus insights) + Banner (dashboard only)
  Rationale: Active workout screens must be ad-free; reward for extra content works
```

#### 1.3 Revenue Estimation by Format Mix

**For an app with 10,000 DAU, 2 sessions/day, US-heavy audience:**

| Format Mix | Daily Impressions | Estimated Daily Revenue | Monthly Revenue |
|-----------|-------------------|----------------------|----------------|
| Banner only | 20,000 | $10-$20 | $300-$600 |
| Banner + Interstitial (1/session) | 20,000 + 20,000 | $10 + $100-$200 | $3,300-$6,300 |
| Banner + Rewarded (0.5/session) | 20,000 + 10,000 | $10 + $100-$200 | $3,300-$6,300 |
| Banner + Interstitial + Rewarded | 20,000 + 20,000 + 5,000 | $10 + $150 + $75 | $7,000-$7,500 |
| Native in-feed (5 impressions/session) | 100,000 | $200-$500 | $6,000-$15,000 |

**Diminishing returns warning:** Adding a third or fourth ad format increases complexity and QA burden significantly. For solo developers, start with 2 formats maximum.

---

### Phase 2: Placement Design

#### 2.1 Placement Timing Rules

**The Ad Placement Golden Rules:**

```
RULE 1: NEVER during critical user flows
  - Never during text input, form submission, or data entry
  - Never during recording (audio, video, photo)
  - Never during payment or checkout flows
  - Never during onboarding or first-time setup

RULE 2: ALWAYS at natural boundaries
  - Between levels/stages (games)
  - After saving or completing a task (productivity)
  - Between articles or content pieces (content apps)
  - After viewing results or a summary screen
  - During screen transitions (app open ad)

RULE 3: USER-INITIATED for highest value
  - "Watch ad to unlock bonus content"
  - "Watch ad for extra hints/retries"
  - "Watch ad to remove cooldown timer"
  - Users who choose to watch have 3-5x higher completion rates

RULE 4: TRANSPARENT about the exchange
  - Always show what the user gets before asking them to watch
  - "Watch a short video to get 50 bonus coins"
  - Never auto-play rewarded ads or trick users into watching
```

#### 2.2 Placement Map by Screen Type

| Screen Type | Banner OK? | Interstitial OK? | Rewarded OK? | Native OK? | Notes |
|------------|------------|------------------|-------------|------------|-------|
| **Home / Dashboard** | Bottom banner | No | If relevant | In feed | Keep clean, banner is sufficient |
| **Content Detail** | Article footer | No (while reading) | For bonus content | In-article | Never interrupt reading |
| **Task Completion** | No | Yes (after save) | Yes (for bonus) | No | Best interstitial placement |
| **Level Complete** | No | Yes | Yes (for rewards) | No | Users expect this |
| **Loading Screen** | No | No | No | No | Feels like punishment |
| **Settings** | No | No | No | No | Respect user intent |
| **Search Results** | No | No | No | In results | Must look distinct from results |
| **Between Sessions** | No | App open ad | No | No | Max 1 per cold start |

#### 2.3 Banner Placement Guidelines

```
Banner positioning hierarchy (best to worst):

1. Bottom of screen (anchored) — Industry standard, least intrusive
   - Users' thumbs naturally rest below the banner
   - Does not push content down
   - Avoid overlapping navigation buttons (48dp minimum gap)

2. Between content sections — Natural break point in scrollable content
   - Every 4-6 content items in a list/feed
   - Never between the 1st and 2nd item (too aggressive)

3. Top of screen (below toolbar) — Acceptable but less standard
   - Can feel more intrusive
   - Use only if bottom is occupied by navigation

NEVER:
- Floating/overlaying content
- Inside scrollable content that causes accidental clicks
- Adjacent to interactive elements (buttons, toggles) — 48dp minimum gap
- On screens with fewer than 3 content items (banner dominates)
```

#### 2.4 Interstitial Timing State Machine

```kotlin
// Interstitial display logic
class InterstitialManager(
    private val minSecondsBetweenAds: Int = 180,       // 3 minutes minimum
    private val minActionsBetweenAds: Int = 3,          // 3 user actions minimum
    private val maxAdsPerSession: Int = 4,              // Cap per session
    private val cooldownAfterDismiss: Int = 300          // 5 min if user closes early
) {
    private var lastAdShownTime: Long = 0
    private var actionsSinceLastAd: Int = 0
    private var adsShownThisSession: Int = 0
    private var sessionStartTime: Long = System.currentTimeMillis()

    fun onUserAction() {
        actionsSinceLastAd++
    }

    fun canShowInterstitial(): Boolean {
        val now = System.currentTimeMillis()
        val secondsSinceLastAd = (now - lastAdShownTime) / 1000

        return secondsSinceLastAd >= minSecondsBetweenAds
            && actionsSinceLastAd >= minActionsBetweenAds
            && adsShownThisSession < maxAdsPerSession
    }

    fun onAdShown() {
        lastAdShownTime = System.currentTimeMillis()
        actionsSinceLastAd = 0
        adsShownThisSession++
    }

    fun onSessionStart() {
        adsShownThisSession = 0
        sessionStartTime = System.currentTimeMillis()
    }
}
```

---

### Phase 3: Mediation Setup

#### 3.1 Why Mediation Matters

A single ad network (even AdMob) cannot fill 100% of your ad requests at the highest eCPM. Mediation lets multiple networks compete for each impression, increasing both fill rate and revenue.

**Impact of mediation:**
- Fill rate: 70-85% (single network) vs. 95-99% (mediated)
- eCPM lift: 15-40% from network competition
- Revenue impact: 25-60% total revenue increase

#### 3.2 Recommended Mediation Stack

| Priority | Network | Strengths | eCPM Tier | Fill Rate | Notes |
|----------|---------|-----------|-----------|-----------|-------|
| 1 (Primary) | **Google AdMob** | Highest fill, best Android integration | Medium-High | 90-95% | Always include as baseline |
| 2 | **AppLovin / MAX** | Strong rewarded and interstitial eCPMs | High | 80-90% | Best mediation platform alternative |
| 3 | **Unity Ads** | Excellent for games, rewarded video | High (games) | 70-85% | Essential for game apps |
| 4 | **Meta Audience Network** | Strong native and banner eCPMs | Medium-High | 70-80% | Requires Facebook SDK |
| 5 | **ironSource** | Good rewarded, strong mediation | Medium-High | 75-85% | Consider if using Unity |
| 6 | **Pangle (TikTok)** | Growing, competitive eCPMs | Medium | 60-75% | Newer, improving |

**Solo developer recommendation:** Start with AdMob as primary + 1 backup network. Add more networks only when you have 5,000+ DAU and the complexity is justified by revenue.

#### 3.3 AdMob Mediation Configuration

```kotlin
// build.gradle.kts (app-level)
dependencies {
    // Google Mobile Ads SDK (includes AdMob mediation)
    implementation("com.google.android.gms:play-services-ads:23.6.0")

    // Mediation adapters — add the networks you use
    implementation("com.google.ads.mediation:unity:4.12.4.0")
    implementation("com.google.ads.mediation:facebook:6.18.0.0")
    implementation("com.google.ads.mediation:applovin:13.0.1.0")
}
```

```kotlin
// Application class — initialize Mobile Ads SDK
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        MobileAds.initialize(this) { initializationStatus ->
            val statusMap = initializationStatus.adapterStatusMap
            for ((adapter, status) in statusMap) {
                Log.d("AdInit", "Adapter: $adapter -> ${status.initializationState}")
            }
        }
    }
}
```

#### 3.4 Waterfall vs. Bidding

```
Waterfall (Traditional):
  Ad request → Network A (highest eCPM floor) → if no fill →
  Network B (second highest) → if no fill →
  Network C (lowest floor) → if no fill → no ad

  Pros: Predictable, easy to configure
  Cons: Slower, may miss higher bids from lower-priority networks

Bidding (Real-Time):
  Ad request → All networks bid simultaneously → highest bid wins

  Pros: Higher eCPM (competition), faster, less manual tuning
  Cons: Not all networks support bidding, requires SDK updates

Recommendation for solo developers:
  Use AdMob's mediation with bidding enabled for networks that support it.
  Fall back to waterfall for networks that don't.
  This "hybrid" approach is what AdMob configures by default.
```

#### 3.5 AdMob Integration: Banner Ad

```kotlin
// BannerAdManager.kt — Reusable banner ad component
class BannerAdManager(
    private val context: Context,
    private val adUnitId: String,
    private val adSize: AdSize = AdSize.BANNER
) {
    private var adView: AdView? = null

    fun loadBannerAd(container: FrameLayout) {
        adView = AdView(context).apply {
            setAdSize(adSize)
            this.adUnitId = this@BannerAdManager.adUnitId
            adListener = object : AdListener() {
                override fun onAdLoaded() {
                    Log.d("BannerAd", "Ad loaded successfully")
                    container.visibility = View.VISIBLE
                }
                override fun onAdFailedToLoad(error: LoadAdError) {
                    Log.e("BannerAd", "Failed to load: ${error.message}")
                    container.visibility = View.GONE
                }
                override fun onAdClicked() {
                    // Log analytics event
                }
            }
        }
        container.removeAllViews()
        container.addView(adView)

        val adRequest = AdRequest.Builder().build()
        adView?.loadAd(adRequest)
    }

    fun pause() { adView?.pause() }
    fun resume() { adView?.resume() }
    fun destroy() { adView?.destroy() }
}
```

#### 3.6 AdMob Integration: Rewarded Ad

```kotlin
// RewardedAdManager.kt — Load and show rewarded ads
class RewardedAdManager(
    private val activity: Activity,
    private val adUnitId: String
) {
    private var rewardedAd: RewardedAd? = null
    private var isLoading = false

    fun preload() {
        if (isLoading || rewardedAd != null) return
        isLoading = true

        val adRequest = AdRequest.Builder().build()
        RewardedAd.load(activity, adUnitId, adRequest,
            object : RewardedAdLoadCallback() {
                override fun onAdLoaded(ad: RewardedAd) {
                    rewardedAd = ad
                    isLoading = false
                    Log.d("RewardedAd", "Ad preloaded")
                }
                override fun onAdFailedToLoad(error: LoadAdError) {
                    rewardedAd = null
                    isLoading = false
                    Log.e("RewardedAd", "Failed to load: ${error.message}")
                }
            }
        )
    }

    fun isReady(): Boolean = rewardedAd != null

    fun show(onRewardEarned: (type: String, amount: Int) -> Unit) {
        val ad = rewardedAd ?: run {
            Log.w("RewardedAd", "Ad not ready, preloading...")
            preload()
            return
        }

        ad.fullScreenContentCallback = object : FullScreenContentCallback() {
            override fun onAdDismissedFullScreenContent() {
                rewardedAd = null
                preload() // Pre-load next ad
            }
            override fun onAdFailedToShowFullScreenContent(error: AdError) {
                rewardedAd = null
                preload()
            }
        }

        ad.show(activity) { rewardItem ->
            onRewardEarned(rewardItem.type, rewardItem.amount)
        }
    }
}

// Usage in Activity/Fragment
rewardedAdManager.show { type, amount ->
    // Grant reward to user
    viewModel.grantBonus(amount)
    analytics.logEvent("rewarded_ad_completed", bundleOf("reward_type" to type))
}
```

#### 3.7 AdMob Integration: Interstitial Ad

```kotlin
// InterstitialAdManager.kt — Interstitial with frequency capping
class InterstitialAdManager(
    private val activity: Activity,
    private val adUnitId: String,
    private val frequencyManager: InterstitialManager
) {
    private var interstitialAd: InterstitialAd? = null

    fun preload() {
        val adRequest = AdRequest.Builder().build()
        InterstitialAd.load(activity, adUnitId, adRequest,
            object : InterstitialAdLoadCallback() {
                override fun onAdLoaded(ad: InterstitialAd) {
                    interstitialAd = ad
                }
                override fun onAdFailedToLoad(error: LoadAdError) {
                    interstitialAd = null
                }
            }
        )
    }

    fun showIfEligible(): Boolean {
        if (!frequencyManager.canShowInterstitial()) return false
        val ad = interstitialAd ?: return false

        ad.fullScreenContentCallback = object : FullScreenContentCallback() {
            override fun onAdDismissedFullScreenContent() {
                interstitialAd = null
                frequencyManager.onAdShown()
                preload()
            }
            override fun onAdFailedToShowFullScreenContent(error: AdError) {
                interstitialAd = null
                preload()
            }
        }
        ad.show(activity)
        return true
    }
}
```

---

### Phase 4: UX Preservation Rules

#### 4.1 The Ad Experience Scorecard

Rate your ad implementation on each dimension before shipping:

| Dimension | Score (1-5) | Red Flag Threshold | What to Check |
|-----------|------------|-------------------|---------------|
| **Predictability** | [Score] | Below 3 | Can users predict when ads will appear? |
| **Interruptiveness** | [Score] | Below 3 | Do ads break the user's flow? |
| **Relevance** | [Score] | Below 2 | Are ads appropriate for your audience? |
| **Escapability** | [Score] | Below 4 | Can users dismiss ads quickly? |
| **Frequency** | [Score] | Below 3 | Are users seeing too many ads? |
| **Transparency** | [Score] | Below 4 | Do users know they can pay to remove ads? |

**If any dimension scores below the red flag threshold, redesign that aspect before shipping.**

#### 4.2 Ad-Free Experience for Premium Users

```kotlin
// PremiumAdController.kt — Disable ads for premium subscribers
class PremiumAdController(
    private val subscriptionRepository: SubscriptionRepository
) {
    fun shouldShowAds(): Boolean {
        return !subscriptionRepository.isPremiumActive()
    }

    fun shouldShowBanner(): Boolean = shouldShowAds()
    fun shouldShowInterstitial(): Boolean = shouldShowAds()
    fun shouldShowRewarded(): Boolean {
        // Rewarded ads can optionally remain available for premium users
        // who want bonus rewards. This is user-initiated, so it is acceptable.
        return true // or shouldShowAds() if you want them fully removed
    }
}

// Usage throughout the app
if (premiumAdController.shouldShowBanner()) {
    bannerAdManager.loadBannerAd(bannerContainer)
} else {
    bannerContainer.visibility = View.GONE
}
```

#### 4.3 Ad Fatigue Detection

Monitor these signals that your ads are driving users away:

| Signal | Measurement | Threshold | Action |
|--------|------------|-----------|--------|
| Session length decrease | Compare sessions with 0 ads vs. 3+ ads | >15% decrease with ads | Reduce frequency |
| Day-1 retention drop | Compare cohorts before/after ad implementation | >5% drop | Revise placements |
| 1-star reviews mentioning ads | Monitor Play Store reviews | >10% of reviews | Immediate audit |
| Interstitial close-before-view rate | Track close within 1 second | >50% | Wrong placement timing |
| Uninstalls after ad impression | Correlate uninstall events with recent ad views | Spike after interstitials | Reduce interstitial frequency |

#### 4.4 Content Category Filtering

```xml
<!-- res/xml/ad_content_rating.xml -->
<!-- Configure content filtering for your audience -->
<RequestConfiguration>
    <!-- Set max ad content rating -->
    <!-- G = General, PG = Parental Guidance, T = Teen, MA = Mature -->
    <MaxAdContentRating value="PG" />

    <!-- Tag for child-directed treatment (COPPA) -->
    <!-- Set to true ONLY if your app targets children under 13 -->
    <TagForChildDirectedTreatment value="false" />

    <!-- Tag for under age of consent (GDPR) -->
    <TagForUnderAgeOfConsent value="false" />
</RequestConfiguration>
```

```kotlin
// Apply content filtering in Application.onCreate()
val requestConfiguration = RequestConfiguration.Builder()
    .setMaxAdContentRating(RequestConfiguration.MAX_AD_CONTENT_RATING_PG)
    .setTagForChildDirectedTreatment(
        RequestConfiguration.TAG_FOR_CHILD_DIRECTED_TREATMENT_FALSE
    )
    .build()
MobileAds.setRequestConfiguration(requestConfiguration)
```

---

### Phase 5: Revenue Optimization

#### 5.1 Optimization Levers (Priority Order)

| Priority | Lever | Expected Impact | Effort | How |
|----------|-------|----------------|--------|-----|
| 1 | **Add mediation** | +25-60% revenue | Medium | Add 1-2 backup networks |
| 2 | **Add rewarded ads** | +30-100% revenue | Medium | Identify reward opportunities |
| 3 | **Optimize placement timing** | +10-30% revenue | Low | A/B test trigger points |
| 4 | **Increase session length** | +15-25% revenue | High | Improve app engagement |
| 5 | **Adaptive banner sizes** | +10-20% banner revenue | Low | Use AdSize.getCurrentOrientationAnchoredAdaptiveBannerAdSize() |
| 6 | **Geographic eCPM targeting** | +5-15% revenue | Medium | Show more ads in low-eCPM regions, fewer in high-eCPM |
| 7 | **Add native ads** | +20-40% revenue | High | Custom ad layouts in feeds |

#### 5.2 A/B Testing Ad Placements

```kotlin
// Simple ad placement A/B test
object AdPlacementTest {
    fun getInterstitialFrequency(userId: String): Int {
        // Test: 2 actions between ads vs. 4 actions between ads
        val variant = if (userId.hashCode().absoluteValue % 2 == 0) "frequent" else "moderate"
        return when (variant) {
            "frequent" -> 2   // Show after every 2 completed actions
            "moderate" -> 4   // Show after every 4 completed actions
            else -> 3
        }
    }
}
```

Track these metrics per variant:
- **Revenue per DAU (ARPDAU)** — Primary metric
- **Session length** — Must not decrease significantly
- **Day-7 retention** — Must not decrease by more than 2%
- **Sessions per user per day** — Must remain stable

#### 5.3 Revenue Benchmarks by App Category

| Category | Banner ARPDAU | Interstitial ARPDAU | Rewarded ARPDAU | Total ARPDAU |
|----------|--------------|--------------------|--------------------|-------------|
| Casual Games | $0.01-$0.03 | $0.02-$0.08 | $0.03-$0.10 | $0.06-$0.21 |
| Puzzle Games | $0.01-$0.02 | $0.03-$0.10 | $0.05-$0.15 | $0.09-$0.27 |
| Productivity | $0.01-$0.02 | $0.00-$0.02 | N/A | $0.01-$0.04 |
| News/Content | $0.02-$0.05 | $0.01-$0.03 | N/A | $0.03-$0.08 |
| Fitness | $0.01-$0.03 | $0.01-$0.04 | $0.02-$0.06 | $0.04-$0.13 |
| Social | $0.02-$0.04 | $0.00-$0.01 | N/A | $0.02-$0.05 |

**How to use these benchmarks:** Multiply your DAU by the ARPDAU range. Example: 10,000 DAU casual game with all three formats = $0.06-$0.21 x 10,000 = $600-$2,100/month.

#### 5.4 Monthly Revenue Tracking Template

```
## Ad Revenue Dashboard — [Month]

### Summary
| Metric | This Month | Last Month | Change |
|--------|-----------|------------|--------|
| Total ad revenue | $[X] | $[X] | [+/-X%] |
| ARPDAU | $[X] | $[X] | [+/-X%] |
| Average DAU | [N] | [N] | [+/-X%] |
| Fill rate | [X]% | [X]% | [+/-X%] |
| Blended eCPM | $[X] | $[X] | [+/-X%] |

### By Format
| Format | Impressions | Revenue | eCPM | Fill Rate |
|--------|------------|---------|------|-----------|
| Banner | [N] | $[X] | $[X] | [X]% |
| Interstitial | [N] | $[X] | $[X] | [X]% |
| Rewarded | [N] | $[X] | $[X] | [X]% |
| Native | [N] | $[X] | $[X] | [X]% |

### By Network
| Network | Revenue | eCPM | Fill Rate | Share |
|---------|---------|------|-----------|-------|
| AdMob | $[X] | $[X] | [X]% | [X]% |
| Unity Ads | $[X] | $[X] | [X]% | [X]% |
| Meta | $[X] | $[X] | [X]% | [X]% |
| AppLovin | $[X] | $[X] | [X]% | [X]% |

### Health Metrics
| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| Day-1 retention | [X]% | >40% | OK / WARNING |
| Session length | [X] min | >3 min | OK / WARNING |
| Ad-related 1-star reviews | [N] | <5/month | OK / WARNING |
```

---

## Expected Output

```markdown
# Ad Placement Strategy: [App Name]

## Format Selection
| Format | Include? | Placement | eCPM Estimate | Monthly Revenue Estimate |
|--------|---------|-----------|---------------|------------------------|
| Banner | [Yes/No] | [Where] | $[X] | $[X] |
| Interstitial | [Yes/No] | [When/Where] | $[X] | $[X] |
| Rewarded | [Yes/No] | [Reward for what] | $[X] | $[X] |
| Native | [Yes/No] | [In-feed location] | $[X] | $[X] |

## Placement Rules
- Interstitial triggers: [List of valid trigger points]
- Frequency cap: Max [N] interstitials per session, [N] seconds apart
- Banner position: [Top / Bottom / In-content]
- Rewarded triggers: [What user action leads to reward offer]

## Mediation Stack
| Priority | Network | Formats | Expected eCPM |
|----------|---------|---------|--------------|
| 1 | [Network] | [Formats] | $[X] |
| 2 | [Network] | [Formats] | $[X] |
| 3 | [Network] | [Formats] | $[X] |

## UX Safeguards
- Screens with NO ads: [List]
- Frequency limits: [Details]
- Premium opt-out: [Mechanism]
- Fatigue monitoring: [Metrics and thresholds]

## Revenue Projection
| Scenario | Monthly Revenue | ARPDAU |
|----------|----------------|--------|
| Pessimistic (low fill, low eCPM) | $[X] | $[X] |
| Expected | $[X] | $[X] |
| Optimistic (high fill, high eCPM) | $[X] | $[X] |

## Implementation Priority
1. [First: Banner ads on main screen]
2. [Second: Interstitial at transition points]
3. [Third: Rewarded ads for bonus content]
4. [Fourth: Mediation setup with backup network]
5. [Fifth: Premium ad-removal purchase]
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Focused on designing a complete ad strategy, not just integrating an SDK
- **ST-02** (Structured Sequential Instructions) — Five-phase process from format selection through revenue optimization
- **RT-02** (Multi-Dimensional Analysis) — Ad formats evaluated across eCPM, UX impact, implementation effort, and app type fit
- **CM-01** (Explicit Context Framing) — Context gathering about usage patterns, audience, architecture, and revenue goals
- **DS-06** (Prioritization Guidance) — Optimization levers ranked by impact-to-effort ratio, format selection framework by app type

---

## Related Prompts

- `monetization_model_selector.md` — Decide whether ads are the right monetization model for your app
- `monetization_subscription_design.md` — Design the premium tier that removes ads
- `monetization_paywall_optimization.md` — Design the paywall for ad-removal purchases
- `monetization_revenue_analytics.md` — Track ad revenue metrics alongside subscription metrics
- `monetization_pricing_strategy.md` — Price the ad-removal purchase or subscription

---

## Customization Guide

- **For games:** Prioritize rewarded video ads above all other formats. Game users are conditioned to watch ads for rewards, and rewarded ads have 3-5x the eCPM of banners. Place interstitials between levels (never mid-level). Consider "watch ad to continue" as a monetization mechanic, but always offer an alternative (coins, gems, wait timer).
- **For content/news apps:** Focus on native ads that blend into your content feed. In-article native ads have the highest engagement in content apps. Interstitials between articles work but should be limited to every 3rd article transition to avoid fatigue. Banner ads in article footers are acceptable but low-revenue.
- **For productivity apps:** Minimize ad presence. A single anchored banner on the main screen may be acceptable, but interstitials in productivity apps drive users to competitors. If you must use ads, offer a very affordable ad-removal option ($1.99-$2.99 one-time) to convert annoyed users into paying customers.
- **For apps in emerging markets:** Expect 3-8x lower eCPMs. Compensate by allowing slightly higher ad frequency since users in these markets are more accustomed to ad-supported apps. Consider offertag walls (complete offer to earn reward) as an additional format, as they perform well in price-sensitive markets.
- **For apps with child audiences:** Use only Google-certified ad SDKs, disable personalized advertising, avoid interstitials with countdown timers (children accidentally click), and never use rewarded ads that incentivize engagement with inappropriate content. Review Google Play Families Policy requirements carefully.
