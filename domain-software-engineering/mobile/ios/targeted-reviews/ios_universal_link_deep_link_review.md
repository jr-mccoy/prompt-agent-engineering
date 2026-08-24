---
title: "iOS Universal Link & Deep Link Review"
category: mobile-development
description: "Review Universal Links AASA file configuration, onOpenURL handling, routing architecture, and deferred deep linking for complete deep link coverage."
techniques:
  - ST-01
  - RT-02
  - RT-04
  - AG-02
difficulty: advanced
tags:
  - ios
  - swift
  - code-review
  - universal-links
  - deep-linking
  - navigation
updated: "2026-03-19"
---

# iOS Universal Link & Deep Link Review

**Objective:** Audit Universal Links and deep linking for correct AASA file configuration, complete onOpenURL handling in SwiftUI, routing architecture robustness, and deferred deep linking for install-then-open flows to ensure users reach the correct content reliably.

**When to Use:** Apply when implementing or reviewing Universal Links, custom URL schemes, or deferred deep linking. Essential before marketing campaigns that rely on deep links or when users report broken link handling.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. Does the app use Universal Links, custom URL schemes, or both?
2. Where is the AASA file hosted and is it accessible via CDN?
3. How are deep links routed to specific screens (coordinator, router, ad-hoc)?
4. Is deferred deep linking needed (link -> App Store -> install -> open -> content)?

## Instructions

### CRITICAL: Verification Requirements

- AASA file must be served at /.well-known/apple-app-site-association with correct content-type
- Every deep link pattern in AASA must have a corresponding handler in the app
- Deep link handling must work from cold start, warm start, and already-running states
- URL parameters must be validated and sanitized before use in navigation or data queries

### False-Positive Prevention

- ❌ Do NOT flag custom URL schemes as insecure if they only handle non-sensitive navigation
- ✅ DO flag custom URL schemes that accept auth tokens or sensitive parameters
- ❌ Do NOT flag missing deferred deep linking if the app doesn't use install campaigns
- ✅ DO flag missing deferred deep linking if marketing links go to App Store first
- ❌ Do NOT flag AASA wildcards as always bad — they're valid for pattern matching
- ✅ DO flag overly broad AASA patterns that match unintended URLs

1. **AASA File Configuration**

```json
// BAD: Overly broad pattern matches everything
{
    "applinks": {
        "apps": [],
        "details": [{
            "appID": "TEAM.com.app.bundle",
            "paths": ["*"]  // matches every URL on the domain — too broad
        }]
    }
}

// GOOD: Specific patterns with exclusions
{
    "applinks": {
        "details": [{
            "appIDs": ["TEAM.com.app.bundle"],
            "components": [
                { "/": "/product/*", "comment": "Product pages" },
                { "/": "/user/*/profile", "comment": "User profiles" },
                { "/": "/invite/*", "comment": "Invite links" },
                { "/": "/api/*", "exclude": true, "comment": "Exclude API calls" },
                { "/": "/admin/*", "exclude": true, "comment": "Exclude admin" }
            ]
        }]
    }
}
```

2. **onOpenURL Handling**

```swift
// BAD: Only handles URL in one place — misses cold start
struct ContentView: View {
    var body: some View {
        TabView { /* ... */ }
            .onOpenURL { url in
                handleDeepLink(url) // only works when this view is already loaded
            }
    }
}

// GOOD: Handle at app level for all launch states
@main
struct MyApp: App {
    @State private var router = AppRouter()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(router)
                .onOpenURL { url in
                    router.handleDeepLink(url)
                }
        }
    }
}

// Also handle in AppDelegate for cold start with UIKit lifecycle
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
          let url = userActivity.webpageURL else { return false }
    return router.handleDeepLink(url)
}
```

3. **URL Validation and Routing**

```swift
// BAD: Unvalidated URL parameters used directly
func handleDeepLink(_ url: URL) {
    let components = URLComponents(url: url, resolvingAgainstBaseURL: true)
    let productId = components?.queryItems?.first(where: { $0.name == "id" })?.value
    loadProduct(id: productId!) // force unwrap, no validation, possible injection
}

// GOOD: Validated routing with type-safe parsing
enum DeepLinkRoute {
    case product(id: String)
    case profile(username: String)
    case invite(code: String)

    init?(url: URL) {
        guard let components = URLComponents(url: url, resolvingAgainstBaseURL: true) else { return nil }
        let path = components.path.split(separator: "/").map(String.init)

        switch path {
        case ["product", let id] where id.allSatisfy(\.isAlphanumeric):
            self = .product(id: id)
        case ["user", let username, "profile"] where username.count <= 30:
            self = .profile(username: username)
        case ["invite", let code] where code.count == 8:
            self = .invite(code: code)
        default:
            return nil
        }
    }
}

func handleDeepLink(_ url: URL) -> Bool {
    guard let route = DeepLinkRoute(url: url) else {
        logger.warning("Unhandled deep link: \(url.absoluteString)")
        return false
    }
    router.navigate(to: route)
    return true
}
```

4. **Deferred Deep Linking**

```swift
// BAD: No deferred deep link — user installs from link, opens to home screen
// Marketing link: https://app.com/product/123 → App Store → Install → Opens to Home

// GOOD: Clipboard or pasteboard-based deferred deep link
func checkDeferredDeepLink() {
    guard isFirstLaunch else { return }

    // Option 1: Check pasteboard (with user consent in iOS 16+)
    if let url = UIPasteboard.general.url,
       url.host == "app.com",
       let route = DeepLinkRoute(url: url) {
        pendingRoute = route
    }

    // Option 2: Use App Clip invocation URL
    // Option 3: Use attribution service (Branch, AppsFlyer)
}

// Handle pending route after onboarding completes
func onOnboardingComplete() {
    if let route = pendingRoute {
        router.navigate(to: route)
        pendingRoute = nil
    }
}
```

## Expected Output

```
## Universal Link & Deep Link Review Report

### Summary
- **AASA patterns reviewed:** N
- **Handler coverage:** N of N patterns handled
- **URL validation issues:** N
- **Launch state coverage:** Cold/Warm/Running
- **Deferred deep link support:** Present/Absent

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **User impact:** ...
- **Recommendation:** ...
```

## Example Output

```
## Universal Link & Deep Link Review Report

### Summary
- **AASA patterns reviewed:** 6
- **Handler coverage:** 4 of 6 patterns handled
- **URL validation issues:** 2
- **Launch state coverage:** Warm and Running only (missing cold start)
- **Deferred deep link support:** Absent

### Findings

#### [Critical] Missing Cold Start Handler — AppDelegate.swift
- **Issue:** `application(_:continue:restorationHandler:)` not implemented. Universal Links from terminated state are dropped.
- **User impact:** Users tapping links when app is not running see home screen instead of content.
- **Recommendation:** Implement the UIApplicationDelegate method and route to AppRouter.

#### [Warning] Unvalidated Parameter — DeepLinkHandler.swift:L34
- **Issue:** Product ID extracted from URL query without validation, passed directly to API call.
- **Recommendation:** Add alphanumeric validation and length check before using in API request.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates AASA, handling, validation, deferred
- **RT-02 (Role-Based Task Framing):** Reviewer acts as iOS deep linking specialist
- **RT-04 (Constraint-Based Refinement):** Enforces all-launch-state coverage and validation
- **AG-02 (Automated Guardrails):** Prevents false flags on valid custom schemes and wildcards

## Related Prompts

- `ios_coordinator_navigation_review.md` — Navigation architecture for deep link routing
- `ios_push_notification_review.md` — Notification-triggered deep links
- `ios_app_intent_shortcuts_review.md` — Siri and Shortcuts deep link handling

## Customization Guide

- **E-commerce apps:** Add product URL pattern coverage and cart deep link handling
- **Social apps:** Add user profile, post, and conversation deep link patterns
- **Multi-platform:** Add macOS Universal Link handling differences
