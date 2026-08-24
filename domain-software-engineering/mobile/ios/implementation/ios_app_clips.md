---
title: "iOS App Clips Implementation"
category: mobile-development
description: "Implement App Clips with proper target setup, invocation URL configuration, size budget management, shared code strategy, App Clip Card design, and location verification."
techniques:
  - ST-01
  - ST-02
difficulty: intermediate
tags:
  - ios
  - swift
  - app-clips
  - mobile-development
updated: "2026-03-20"
---

# iOS App Clips Implementation

**Objective:** Implement a production-ready App Clip with proper Xcode target setup, invocation URL configuration, size budget management under 15MB, shared code architecture with the main app, App Clip Card metadata, and location-based verification for physical invocations.

**When to Use:** Use this prompt when building an App Clip to provide lightweight, focused functionality at the point of need -- such as ordering at a restaurant, renting a scooter, or checking in at a venue. Best used after the main app's core feature is implemented and you want to expose a streamlined entry point.

**Prompt Type:** Modular (150-300 lines)

---

## Context Gathering

Before implementing the App Clip, gather essential context:

1. **Use Case:**
   - "What single task should the App Clip accomplish?"
   - "What is the physical or digital invocation point (NFC tag, QR code, Safari Smart Banner, Maps)?"
   - "Does the user need to authenticate, or can the flow be anonymous?"

2. **Feature Scope:**
   - "Which screens from the main app are needed in the App Clip?"
   - "What data models, services, and UI components must be shared?"
   - "Can the App Clip use ephemeral notifications or Sign in with Apple?"

3. **Size Budget:**
   - "What is the current estimated size of shared code and assets?"
   - "Are there heavy dependencies (image processing, ML models) that must be excluded?"
   - "Which asset catalogs and resources are required?"

4. **Invocation:**
   - "What URL pattern will trigger the App Clip (e.g., `https://example.com/clip/location/{id}`)?"
   - "Is location verification needed (physical NFC/QR invocations)?"
   - "Are multiple invocation URLs needed for different experiences?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY code, you MUST:**

1. **Verify the 15MB limit** - The App Clip binary must be under 15MB (thinned, signed). Monitor size throughout development.
2. **Check shared code feasibility** - Ensure shared modules compile independently without pulling in unnecessary dependencies.
3. **Confirm invocation URL ownership** - Verify Apple App Site Association (AASA) file can be hosted at the invocation domain.
4. **Follow project conventions** - Match existing architecture, module boundaries, and naming.
5. **Provide specific, working code** - All code samples MUST include target membership annotations and file paths.

### False-Positive Prevention

- Do NOT include features beyond the single focused task; App Clips must be minimal
- Do NOT use frameworks that inflate binary size (e.g., full Firebase SDK -- use REST instead)
- Do NOT assume persistent storage; App Clip data may be deleted after inactivity
- Do NOT forget to handle the transition from App Clip to full app installation
- Do NOT skip the AASA file configuration; invocation URLs will not work without it
- DO share code via shared frameworks or target membership, not copy-paste
- DO use `SKOverlay` to prompt full app download after task completion
- DO test with the `_XCAppClipURL` environment variable in Xcode schemes
- DO implement ephemeral notification permission for time-sensitive follow-ups
- DO verify location for physical invocations to prevent URL spoofing

---

### Phase 1: Xcode Target & Project Setup

#### 1.1 App Clip Target Configuration

```swift
// Steps (not code -- Xcode configuration):
// 1. File > New > Target > App Clip
// 2. Name: "YourAppClip"
// 3. Bundle Identifier: "com.yourcompany.yourapp.Clip"
//    (MUST be main app bundle ID + ".Clip")
// 4. Add to the same App Group as the main app

// File: YourAppClip/YourAppClipApp.swift
// Target: YourAppClip

import SwiftUI

@main
struct YourAppClipApp: App {
    var body: some Scene {
        WindowGroup {
            AppClipRootView()
                .onContinueUserActivity(
                    NSUserActivityTypeBrowsingWeb,
                    perform: handleUserActivity
                )
        }
    }

    private func handleUserActivity(_ activity: NSUserActivity) {
        guard let url = activity.webpageURL else { return }

        // Parse invocation URL to determine which experience to show
        let components = URLComponents(url: url, resolvingAgainstBaseURL: false)
        let locationId = components?.queryItems?
            .first(where: { $0.name == "id" })?.value

        AppClipState.shared.locationId = locationId
        AppClipState.shared.invocationURL = url
    }
}
```

#### 1.2 App Clip State

```swift
// File: YourAppClip/AppClipState.swift
// Target: YourAppClip

import SwiftUI

@Observable
final class AppClipState {
    static let shared = AppClipState()

    var locationId: String?
    var invocationURL: URL?
    var isLoading = true
    var error: AppClipError?

    enum AppClipError: LocalizedError {
        case locationVerificationFailed
        case invalidInvocation
        case networkError(String)

        var errorDescription: String? {
            switch self {
            case .locationVerificationFailed:
                return "Please scan the code at the physical location."
            case .invalidInvocation:
                return "This link is not valid. Please try scanning again."
            case .networkError(let msg):
                return msg
            }
        }
    }

    private init() {}
}
```

---

### Phase 2: Shared Code Architecture

**CHECKPOINT 1:** Confirm target setup before organizing shared code.

```markdown
## Target Setup Summary

| Item | Status |
|------|--------|
| App Clip target created | Bundle ID = main + ".Clip" |
| App Group shared | Same group as main app |
| Invocation URL handler | NSUserActivityTypeBrowsingWeb |
| State management | AppClipState observable |

**Proceed with shared code organization?**
```

#### 2.1 Shared Framework Strategy

```
Project Structure:
├── YourApp/                    # Main app target
│   ├── AppDelegate.swift
│   └── Features/
├── YourAppClip/                # App Clip target
│   ├── YourAppClipApp.swift
│   ├── AppClipState.swift
│   └── AppClipRootView.swift
├── SharedKit/                  # Shared framework (both targets)
│   ├── Models/
│   │   └── Location.swift
│   ├── Services/
│   │   ├── APIClient.swift     # Lightweight HTTP client
│   │   └── LocationService.swift
│   ├── Views/
│   │   ├── OrderView.swift
│   │   └── PaymentView.swift
│   └── Utilities/
│       └── Extensions.swift
```

```swift
// File: SharedKit/Models/Location.swift
// Target: SharedKit (linked by both App and AppClip)

import Foundation

struct Location: Codable, Identifiable {
    let id: String
    let name: String
    let address: String
    let latitude: Double
    let longitude: Double
    let menuURL: URL?
}
```

#### 2.2 Size Budget Management

```swift
// Strategies to stay under 15MB:

// 1. Use system SF Symbols instead of custom icons
Image(systemName: "cart.fill")  // 0 KB vs custom icon

// 2. Use asset catalog slicing -- only include assets needed by App Clip
// Mark assets with target membership: YourAppClip only for clip-specific,
// SharedKit for shared assets

// 3. Exclude heavy dependencies via conditional compilation
#if !APPCLIP
import HeavyAnalyticsSDK  // Only in main app
#endif

// 4. Use REST APIs instead of heavy SDKs
// Instead of: import FirebaseFirestore (adds ~8MB)
// Use direct URLSession calls to your backend

// 5. Monitor size with every build:
// Product > Archive > Distribute App > Ad Hoc > Thin for specific device
// Check the App Thinning Size Report
```

---

### Phase 3: App Clip Experience

#### 3.1 Root View with Location Verification

```swift
// File: YourAppClip/AppClipRootView.swift
// Target: YourAppClip

import SwiftUI
import CoreLocation
import SharedKit

struct AppClipRootView: View {
    @State private var state = AppClipState.shared
    @State private var location: Location?
    @State private var showFullAppOverlay = false

    var body: some View {
        NavigationStack {
            Group {
                if state.isLoading {
                    ProgressView("Loading...")
                } else if let error = state.error {
                    errorView(error)
                } else if let location {
                    LocationExperienceView(
                        location: location,
                        onComplete: { showFullAppOverlay = true }
                    )
                } else {
                    ProgressView("Verifying location...")
                }
            }
            .task {
                await loadExperience()
            }
            .appStoreOverlay(isPresented: $showFullAppOverlay) {
                SKOverlay.AppClipConfiguration(position: .bottom)
            }
        }
    }

    private func loadExperience() async {
        guard let locationId = state.locationId else {
            state.error = .invalidInvocation
            state.isLoading = false
            return
        }

        do {
            // Fetch location data
            let fetchedLocation = try await APIClient.shared.fetchLocation(id: locationId)

            // Verify physical proximity for NFC/QR invocations
            let isNearby = await verifyLocation(
                latitude: fetchedLocation.latitude,
                longitude: fetchedLocation.longitude
            )

            if isNearby {
                self.location = fetchedLocation
            } else {
                state.error = .locationVerificationFailed
            }
        } catch {
            state.error = .networkError(error.localizedDescription)
        }

        state.isLoading = false
    }

    private func verifyLocation(latitude: Double, longitude: Double) async -> Bool {
        let manager = CLLocationManager()

        // App Clips can request when-in-use without full permission prompt
        guard let userLocation = manager.location else { return true }

        let targetLocation = CLLocation(latitude: latitude, longitude: longitude)
        let distance = userLocation.distance(from: targetLocation)

        // Allow 500 meter radius for location verification
        return distance < 500
    }

    private func errorView(_ error: AppClipState.AppClipError) -> some View {
        ContentUnavailableView {
            Label("Unable to Load", systemImage: "exclamationmark.triangle")
        } description: {
            Text(error.localizedDescription)
        } actions: {
            Button("Try Again") {
                state.isLoading = true
                state.error = nil
                Task { await loadExperience() }
            }
            .buttonStyle(.borderedProminent)
        }
    }
}
```

#### 3.2 Ephemeral Notifications

```swift
// File: YourAppClip/EphemeralNotifications.swift
// Target: YourAppClip

import UserNotifications

struct EphemeralNotificationManager {
    /// App Clips get ephemeral notification permission for up to 8 hours
    /// after the user interacts with the clip. No permission prompt needed.
    static func scheduleOrderUpdate(orderId: String, estimatedMinutes: Int) async throws {
        let content = UNMutableNotificationContent()
        content.title = "Order Update"
        content.body = "Your order #\(orderId) is ready for pickup!"
        content.sound = .default

        let trigger = UNTimeIntervalNotificationTrigger(
            timeInterval: TimeInterval(estimatedMinutes * 60),
            repeats: false
        )

        let request = UNNotificationRequest(
            identifier: "order-\(orderId)",
            content: content,
            trigger: trigger
        )

        try await UNUserNotificationCenter.current().add(request)
    }
}
```

---

### Phase 4: Apple App Site Association & App Clip Card

**CHECKPOINT 2:** Review the experience flow before configuring invocation.

```markdown
## Experience Flow

| Step | Component |
|------|-----------|
| 1. Scan/Tap | NFC tag, QR code, or Safari link |
| 2. Invocation | URL parsed, location ID extracted |
| 3. Verification | Physical location proximity check |
| 4. Experience | Location-specific content loaded |
| 5. Completion | SKOverlay prompts full app install |

**Ready for AASA and App Clip Card configuration?**
```

#### 4.1 Apple App Site Association

```json
// File hosted at: https://example.com/.well-known/apple-app-site-association

{
    "appclips": {
        "apps": [
            "TEAMID.com.yourcompany.yourapp.Clip"
        ]
    },
    "applinks": {
        "apps": [],
        "details": [
            {
                "appIDs": [
                    "TEAMID.com.yourcompany.yourapp",
                    "TEAMID.com.yourcompany.yourapp.Clip"
                ],
                "components": [
                    {
                        "/": "/clip/*",
                        "comment": "App Clip invocation URLs"
                    }
                ]
            }
        ]
    }
}
```

#### 4.2 App Clip Card Configuration

```markdown
## App Store Connect Configuration

1. Navigate to your app in App Store Connect
2. Select "App Clip Experiences" under the App Clip section
3. Configure:
   - **Header Image:** 1800x1200 px (3:2 aspect ratio)
   - **Title:** "Order at [Location Name]" (max 30 characters recommended)
   - **Subtitle:** "Scan to order and pay" (max 56 characters)
   - **Call to Action:** "Open" (default) or "Play", "View", "Shop"

### Advanced App Clip Experience (URL-specific cards):
- URL: https://example.com/clip/location/123
- Matches: Prefix match (handles /clip/location/123?table=5 etc.)
- Location: Associate with a Maps location for proactive suggestions
```

#### 4.3 Data Migration to Full App

```swift
// File: SharedKit/Utilities/AppClipDataMigration.swift
// Target: SharedKit

import Foundation

struct AppClipDataMigration {
    private static let appGroupDefaults = UserDefaults(suiteName: "group.com.yourcompany.yourapp")

    /// Save data in App Clip so full app can access it
    static func saveForMigration(key: String, data: Codable) throws {
        let encoded = try JSONEncoder().encode(AnyEncodable(data))
        appGroupDefaults?.set(encoded, forKey: "clip_migration_\(key)")
    }

    /// Read migrated data in full app after installation
    static func readMigrated<T: Decodable>(key: String, as type: T.Type) -> T? {
        guard let data = appGroupDefaults?.data(forKey: "clip_migration_\(key)") else {
            return nil
        }
        return try? JSONDecoder().decode(T.self, from: data)
    }

    /// Clean up migration data after full app has consumed it
    static func clearMigrationData() {
        let keys = appGroupDefaults?.dictionaryRepresentation().keys
            .filter { $0.hasPrefix("clip_migration_") }
        keys?.forEach { appGroupDefaults?.removeObject(forKey: $0) }
    }
}
```

---

## Expected Output

### File Structure

```
YourAppClip/
├── YourAppClipApp.swift               # App entry point with URL handling
├── AppClipState.swift                 # Invocation state management
├── AppClipRootView.swift              # Root view with location verification
└── EphemeralNotifications.swift       # Time-limited notification support

SharedKit/
├── Models/
│   └── Location.swift                 # Shared data model
├── Services/
│   ├── APIClient.swift                # Lightweight HTTP client
│   └── LocationService.swift          # Location utilities
├── Views/
│   ├── OrderView.swift                # Shared order flow UI
│   └── PaymentView.swift              # Shared payment UI
└── Utilities/
    └── AppClipDataMigration.swift     # Data migration to full app

Server:
└── .well-known/apple-app-site-association
```

### Implementation Checklist

- [ ] App Clip target created with correct bundle ID (main + ".Clip")
- [ ] App Group shared between main app and App Clip
- [ ] Invocation URL handling via `onContinueUserActivity`
- [ ] AASA file hosted and verified
- [ ] App Clip Card configured in App Store Connect
- [ ] Binary size under 15MB (thinned)
- [ ] Shared code via framework with proper target membership
- [ ] Heavy dependencies excluded from App Clip target
- [ ] Location verification for physical invocations
- [ ] Ephemeral notifications for follow-up
- [ ] `SKOverlay` for full app installation prompt
- [ ] Data migration via App Group for full app transition
- [ ] Xcode scheme with `_XCAppClipURL` for testing

---

## Techniques Used

- **ST-01** (Clear Objective): Focused objective for App Clip implementation
- **ST-02** (Sequential Instructions): Phased approach from target setup through invocation configuration

---

## Related Prompts

- [ios_widgets_app_intents.md](../implementation/ios_widgets_app_intents.md) - Another extension target pattern
- [ios_navigation_implementation.md](../implementation/ios_navigation_implementation.md) - Deep link routing from App Clip
- [ios_app_thinning_optimization.md](../publishing/ios_app_thinning_optimization.md) - Binary size optimization strategies
- [ios_push_notifications.md](../implementation/ios_push_notifications.md) - Notification patterns used in ephemeral mode
