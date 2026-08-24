# UMP SDK Consent Management

## Overview

The User Messaging Platform (UMP) SDK handles GDPR (EU), CCPA (California), and other privacy regulation consent for ad personalization. It must be called BEFORE loading any ads.

## Flow

```
App Launch
    │
    ▼
Request consent info update
    │
    ├── Consent form available?
    │   ├── YES → Show form → User responds → Load ads accordingly
    │   └── NO → Region doesn't require consent → Load ads normally
    │
    └── Already consented?
        ├── YES → Load ads with stored consent
        └── NO → Show form on next eligible moment
```

## Implementation

### 1. Configure in AdMob Console

1. Go to **AdMob → Privacy & messaging → GDPR** (or CCPA)
2. Create a GDPR message with your privacy policy URL
3. Publish the message
4. Note: UMP SDK pulls the form from AdMob's servers

### 2. Request Consent Info Update

```kotlin
fun requestConsent(activity: Activity, onComplete: (Boolean) -> Unit) {
    val params = ConsentRequestParameters.Builder()
        .setTagForUnderAgeOfConsent(false)
        .build()

    val consentInfo = UserMessagingPlatform.getConsentInformation(activity)

    consentInfo.requestConsentInfoUpdate(activity, params,
        {
            // Success — check if form is needed
            UserMessagingPlatform.loadAndShowConsentFormIfRequired(activity) { error ->
                // Form shown (or not needed) — check if ads can load
                onComplete(consentInfo.canRequestAds())
            }
        },
        { error ->
            // Network error — use cached consent status
            onComplete(consentInfo.canRequestAds())
        }
    )
}
```

### 3. Debug Testing

```kotlin
// Force EEA geography for testing GDPR form
val debugSettings = ConsentDebugSettings.Builder(activity)
    .setDebugGeography(ConsentDebugSettings.DebugGeography.DEBUG_GEOGRAPHY_EEA)
    .addTestDeviceHashedId("YOUR_TEST_DEVICE_HASH") // From logcat
    .build()

val params = ConsentRequestParameters.Builder()
    .setConsentDebugSettings(debugSettings)
    .build()
```

**Get test device hash:** Check logcat for a line like:
```
Use new ConsentDebugSettings.Builder().addTestDeviceHashedId("ABCDEF0123456789") to set this as a debug device.
```

### 4. Reset Consent (for Testing)

```kotlin
// Reset stored consent for re-testing
UserMessagingPlatform.getConsentInformation(context).reset()
```

### 5. Respect Consent in Ad Loading

```kotlin
// Only load ads if consent allows it
if (consentInfo.canRequestAds()) {
    MobileAds.initialize(context)
    loadBannerAd()
    preloadInterstitial()
}
```

## CCPA (California)

For CCPA, the UMP SDK handles the "Do Not Sell My Personal Information" link. Configure it in AdMob console under Privacy & messaging → US state regulations.

## Privacy Policy Requirements

Your privacy policy must disclose:
- What data is collected by ads (device ID, IP address, usage patterns)
- Which ad networks receive data
- How users can opt out
- Data retention practices

Include this in both:
1. Play Store listing (Privacy policy URL)
2. In-app settings (link to privacy policy)
