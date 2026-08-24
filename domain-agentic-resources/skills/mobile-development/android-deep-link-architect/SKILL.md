---
name: android-deep-link-architect
description: "Design and validate deep link architecture covering App Links verification, intent filters, Navigation component integration, deferred deep links, and link testing automation. Use this skill when implementing deep linking, setting up App Links, configuring intent filters, handling deferred deep links, or when a developer mentions 'deep link', 'App Links', 'intent filter', 'assetlinks.json', or 'deferred deep link'."
metadata:
  tags:
    - android
    - deep-links
    - app-links
    - navigation
    - solo-developer
  updated: "2026-02-12"
---

# Android Deep Link Architect

Design and validate a complete deep link architecture for Android applications. Covers URI scheme deep links, verified Android App Links, Navigation component integration, deferred deep links for new installs, and automated testing — producing a deep linking system that works reliably across all entry points (browser, email, social media, QR codes, push notifications).

## Purpose

Deep links are how users reach specific content in your app from external sources. A well-designed deep link system drives user acquisition (marketing campaigns), improves user experience (direct content access), and enables cross-app communication. For solo developers, deep links are especially important for marketing (share links that open your app) and re-engagement (push notifications that navigate to specific screens).

## When to Use This Skill

Use this skill when you need to:
- Implement deep linking for the first time in an Android app
- Set up Android App Links (verified, HTTPS-based deep links)
- Integrate deep links with Jetpack Navigation Component or Compose Navigation
- Handle deferred deep links (user clicks link → installs app → sees content)
- Test deep link resolution across different entry points
- Debug deep links that are not resolving correctly

## When NOT to Use This Skill

Do NOT use this skill when:
- You need to implement push notifications (use push notification skill, then link deep links into it)
- You are building a web-only feature (no app involvement)
- You need dynamic links for analytics (Firebase Dynamic Links was deprecated — use App Links + custom UTM params)

## Prerequisites

- Android app with Jetpack Navigation or Compose Navigation
- (For App Links) A domain you control where you can host `.well-known/assetlinks.json`
- (For deferred deep links) Firebase or a third-party attribution SDK

## Step 1: Deep Link Strategy

### 1.1 Define Your Link Schema

```
Your App's Link Structure:
├── yourapp://                           # Custom scheme (fallback)
│   ├── yourapp://item/{id}              # View item
│   ├── yourapp://profile/{userId}       # View profile
│   ├── yourapp://settings               # Open settings
│   └── yourapp://search?q={query}       # Search
│
├── https://yourapp.com/                 # App Links (verified)
│   ├── https://yourapp.com/item/{id}
│   ├── https://yourapp.com/profile/{userId}
│   ├── https://yourapp.com/share/{code} # Shareable content
│   └── https://yourapp.com/invite/{ref} # Referral links
│
└── Special Links:
    ├── Push notification payload → yourapp://item/{id}
    ├── Email campaign → https://yourapp.com/item/{id}?utm_source=email
    └── QR code → https://yourapp.com/share/{code}
```

### 1.2 Link Type Decision Matrix

| Type | Format | Verification | Disambiguation | Use Case |
|------|--------|-------------|----------------|----------|
| **Custom Scheme** | `yourapp://path` | None | Shows app chooser | In-app navigation, legacy |
| **App Links** | `https://domain/path` | `.well-known/assetlinks.json` | Opens directly in app | Marketing, sharing, SEO |
| **Intent URL** | `intent://path#Intent;...` | None | Requires explicit intent | Advanced browser integration |

**Recommendation:** Use App Links (HTTPS) as primary, custom scheme as fallback.

## Step 2: Android Manifest Configuration

### 2.1 Intent Filters

```xml
<activity
    android:name=".MainActivity"
    android:exported="true"
    android:launchMode="singleTask">

    <!-- App Links (verified HTTPS) -->
    <intent-filter android:autoVerify="true">
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data
            android:scheme="https"
            android:host="yourapp.com"
            android:pathPrefix="/item" />
        <data
            android:scheme="https"
            android:host="yourapp.com"
            android:pathPrefix="/profile" />
        <data
            android:scheme="https"
            android:host="yourapp.com"
            android:pathPrefix="/share" />
        <data
            android:scheme="https"
            android:host="yourapp.com"
            android:pathPrefix="/invite" />
    </intent-filter>

    <!-- Custom scheme (fallback) -->
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data
            android:scheme="yourapp"
            android:host="item" />
        <data
            android:scheme="yourapp"
            android:host="profile" />
    </intent-filter>
</activity>
```

### 2.2 App Links Verification (assetlinks.json)

Host this file at `https://yourapp.com/.well-known/assetlinks.json`:

```json
[{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.yourpackage.app",
    "sha256_cert_fingerprints": [
      "AA:BB:CC:DD:EE:FF:00:11:22:33:44:55:66:77:88:99:AA:BB:CC:DD:EE:FF:00:11:22:33:44:55:66:77:88:99"
    ]
  }
}]
```

Get your signing certificate fingerprint:
```bash
# Debug keystore
keytool -list -v -keystore ~/.android/debug.keystore -alias androiddebugkey -storepass android | grep SHA256

# Release keystore
keytool -list -v -keystore release-keystore.jks -alias your-alias | grep SHA256

# Play App Signing (if using Google-managed signing)
# Get from Play Console → Setup → App signing → SHA-256 certificate fingerprint
```

## Step 3: Navigation Integration

### 3.1 Compose Navigation with Deep Links

```kotlin
// Navigation graph
NavHost(navController = navController, startDestination = "home") {
    composable("home") { HomeScreen() }

    composable(
        route = "item/{itemId}",
        arguments = listOf(navArgument("itemId") { type = NavType.StringType }),
        deepLinks = listOf(
            navDeepLink {
                uriPattern = "https://yourapp.com/item/{itemId}"
            },
            navDeepLink {
                uriPattern = "yourapp://item/{itemId}"
            }
        )
    ) { backStackEntry ->
        val itemId = backStackEntry.arguments?.getString("itemId")
        ItemDetailScreen(itemId = itemId)
    }

    composable(
        route = "profile/{userId}",
        arguments = listOf(navArgument("userId") { type = NavType.StringType }),
        deepLinks = listOf(
            navDeepLink {
                uriPattern = "https://yourapp.com/profile/{userId}"
            }
        )
    ) { backStackEntry ->
        val userId = backStackEntry.arguments?.getString("userId")
        ProfileScreen(userId = userId)
    }

    composable(
        route = "search?q={query}",
        arguments = listOf(navArgument("query") {
            type = NavType.StringType
            defaultValue = ""
        }),
        deepLinks = listOf(
            navDeepLink {
                uriPattern = "https://yourapp.com/search?q={query}"
            }
        )
    ) { backStackEntry ->
        val query = backStackEntry.arguments?.getString("query") ?: ""
        SearchScreen(initialQuery = query)
    }
}
```

### 3.2 Handle Deep Link in Activity

```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            val navController = rememberNavController()

            // Handle deep link from intent
            LaunchedEffect(Unit) {
                handleDeepLink(intent, navController)
            }

            AppNavHost(navController = navController)
        }
    }

    override fun onNewIntent(intent: Intent) {
        super.onNewIntent(intent)
        // Handle deep link when app is already running (singleTask)
        setIntent(intent)
    }

    private fun handleDeepLink(intent: Intent, navController: NavController) {
        // Navigation component handles deep link matching automatically
        // But you may need custom handling for analytics or authentication
        val uri = intent.data ?: return

        // Track deep link source
        val utmSource = uri.getQueryParameter("utm_source")
        analytics.logDeepLinkOpened(uri.toString(), utmSource)

        // Check if authentication is required
        if (uri.pathSegments.firstOrNull() in listOf("profile", "settings")) {
            if (!authManager.isLoggedIn) {
                // Redirect to login, then deep link destination
                navController.navigate("login?redirect=${uri}")
                return
            }
        }

        // Let NavController handle the deep link
        navController.handleDeepLink(intent)
    }
}
```

## Step 4: Deferred Deep Links

Handle the case where a user clicks a link but doesn't have the app installed yet:

### 4.1 Strategy

```
User clicks link → App not installed → Play Store → Install → App opens → Navigate to content
```

### 4.2 Implementation with Firebase

```kotlin
// In Application.onCreate() or MainActivity
Firebase.dynamicLinks
    .getDynamicLink(intent)
    .addOnSuccessListener { pendingDynamicLinkData ->
        val deepLink = pendingDynamicLinkData?.link ?: return@addOnSuccessListener
        // Navigate to the deep link destination
        navController.navigate(deepLink)
    }
```

**Note:** Firebase Dynamic Links was deprecated in August 2025. Alternatives:
- **Branch.io** — full-featured deep linking platform
- **AppsFlyer** — attribution + deep linking
- **Custom solution** — store link in clipboard or use Play Store referrer API

### 4.3 Custom Deferred Deep Link (No Third-Party SDK)

```kotlin
// Use Play Store Install Referrer API
val client = InstallReferrerClient.newBuilder(context).build()
client.startConnection(object : InstallReferrerStateListener {
    override fun onInstallReferrerSetupFinished(responseCode: Int) {
        if (responseCode == InstallReferrerClient.InstallReferrerResponse.OK) {
            val referrerDetails = client.installReferrer
            val referrerUrl = referrerDetails.installReferrer
            // Parse referrer URL for deep link destination
            // e.g., utm_content=item_12345 → navigate to item 12345
        }
    }
    override fun onInstallReferrerServiceDisconnected() {}
})
```

## Step 5: Testing Deep Links

### 5.1 Command-Line Testing

```bash
# Test App Link (HTTPS)
adb shell am start -a android.intent.action.VIEW -d "https://yourapp.com/item/12345"

# Test custom scheme
adb shell am start -a android.intent.action.VIEW -d "yourapp://item/12345"

# Verify App Links verification status
adb shell pm get-app-links com.yourpackage.app
```

### 5.2 Automated Test

```kotlin
@Test
fun deepLink_item_navigatesToItemDetail() {
    val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://yourapp.com/item/12345"))
    val scenario = launchActivity<MainActivity>(intent)

    // Verify the correct screen is shown
    composeTestRule.onNodeWithText("Item Details").assertIsDisplayed()
    composeTestRule.onNodeWithText("12345").assertIsDisplayed()
}

@Test
fun deepLink_invalidPath_showsHome() {
    val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://yourapp.com/nonexistent"))
    val scenario = launchActivity<MainActivity>(intent)

    // Should fall through to home screen
    composeTestRule.onNodeWithText("Home").assertIsDisplayed()
}
```

### 5.3 Verification Checklist

- [ ] App Links verification passes: `adb shell pm get-app-links` shows `verified`
- [ ] HTTPS links open directly in app (no disambiguation dialog)
- [ ] Custom scheme links open in app from browser
- [ ] Deep links work when app is not running (cold start)
- [ ] Deep links work when app is already running (warm/hot start with `onNewIntent`)
- [ ] Invalid deep links gracefully fall back to home screen
- [ ] Deep links work after app update (no broken links)
- [ ] Authentication-required deep links redirect to login then to destination

## Related Skills

- `android-release-pipeline` - Ensure assetlinks.json is updated before each release
- `android-testing-patterns` - Testing deep link resolution across scenarios
