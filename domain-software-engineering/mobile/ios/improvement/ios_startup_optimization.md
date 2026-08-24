---
title: "iOS Startup Optimization"
category: mobile-development
description: "Optimize iOS app launch time by reducing pre-main time (dylib loading, static initializers), optimizing didFinishLaunching, deferring initialization, and measuring with Instruments"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - AG-12
  - NE-02
difficulty: advanced
tags:
  - ios
  - swift
  - performance
  - launch-time
  - instruments
  - pre-main
updated: "2026-03-19"
---

# iOS Startup Optimization

**Objective:** Systematically reduce iOS app launch time by analyzing and optimizing both pre-main phases (dylib loading, rebase/bind, ObjC setup, static initializers) and post-main phases (application delegate initialization, first frame rendering), using Instruments for measurement and verification.

**When to Use:** Use this prompt when the app exceeds Apple's recommended launch time thresholds (400ms warm, 800ms cold), when App Store Connect reports launch time regressions in Xcode Organizer, when users complain about slow startup, or proactively as part of performance optimization sprints.

**Prompt Type:** Comprehensive (500-600 lines)

---

## Context Gathering

Before beginning optimization, understand the baseline:

1. **Current Performance:**
   - "What is the current cold launch time (kill app, wait 30s, launch)?"
   - "What does Xcode Organizer show for launch time metrics?"
   - "Is there a noticeable difference between cold and warm launch?"

2. **Architecture:**
   - "How many dynamic frameworks does the app link?"
   - "Are there static initializers or `+load` methods?"
   - "What work happens in `application(_:didFinishLaunchingWithOptions:)`?"

3. **Constraints:**
   - "Are there required startup tasks (auth checks, migration, remote config)?"
   - "What is the minimum acceptable launch experience?"
   - "Are there third-party SDKs that initialize at launch?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Measure before optimizing** - Do not guess at bottlenecks. Use Instruments App Launch template.
2. **Distinguish cold from warm launch** - Different optimizations apply.
3. **Verify the optimization matters** - A 2ms savings in a 2-second launch is noise.
4. **Check for required initialization** - Some startup work cannot be deferred without breaking functionality.
5. **Provide specific measurements** - Before/after timing for each optimization.

**Finding a FAST launch time is an acceptable outcome.** Not every app has launch time problems. Do not manufacture optimization urgency.

### False-Positive Prevention

- ❌ Do NOT recommend removing framework links without verifying they are unused
- ❌ Do NOT defer initialization that is required before first frame
- ❌ Do NOT assume all `+load` methods are problematic (some are required)
- ❌ Do NOT conflate app launch with perceived launch (splash screen duration)
- ✅ DO measure pre-main and post-main separately
- ✅ DO account for third-party SDK initialization requirements
- ✅ DO verify optimizations on a real device (not Simulator)
- ✅ DO test on the oldest supported device for worst-case numbers

---

### Phase 1: Pre-Main Optimization

#### 1.1 Dylib Loading Analysis

**Measure dylib loading time:**

```swift
// Add to scheme environment variables to log pre-main phases:
// DYLD_PRINT_STATISTICS = 1
// DYLD_PRINT_STATISTICS_DETAILS = 1

// Example output:
// Total pre-main time: 1.2 seconds (100.0%)
//   dylib loading time: 350ms (29.1%)
//   rebase/binding time: 120ms (10.0%)
//   ObjC setup time:     80ms  (6.7%)
//   initializer time:    650ms (54.2%)
```

**Reduce dynamic frameworks:**

```swift
// BEFORE: Many dynamic frameworks in Podfile
# Podfile
use_frameworks! # All pods as dynamic frameworks

// AFTER: Static linking where possible
# Podfile
use_frameworks! :linkage => :static

// Or in SPM, prefer static libraries:
// Package.swift
.library(
    name: "MyLibrary",
    type: .static,  // Not .dynamic
    targets: ["MyLibrary"]
)
```

#### 1.2 Static Initializer Reduction

```swift
// PROBLEMATIC: ObjC +load methods run before main()
@objc class LegacyTracker: NSObject {
    @objc static func load() {
        // This runs before main() - delays launch
        setupExpensiveTracking()
    }
}

// BETTER: Use +initialize (lazy, on first use) or move to app launch
@objc class LegacyTracker: NSObject {
    @objc static func initialize() {
        // Runs on first message to this class - not at startup
        setupExpensiveTracking()
    }
}

// BEST: Explicit initialization at appropriate time
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Initialize after first frame
        DispatchQueue.main.async {
            LegacyTracker.setup()
        }
        return true
    }
}
```

#### 1.3 Swift Global Variables

```swift
// SLOW: Complex global initialization
let dateFormatter: DateFormatter = {
    let formatter = DateFormatter()
    formatter.dateFormat = "yyyy-MM-dd"
    formatter.locale = Locale(identifier: "en_US_POSIX")
    formatter.timeZone = TimeZone(abbreviation: "UTC")
    return formatter
}()

// FASTER: Lazy initialization (default for Swift globals, but verify)
// Swift globals are already lazy, but accessing them at startup defeats the purpose.
// Ensure they are not accessed during launch.

// BEST: Instance-level or on-demand
struct DateFormatting {
    static func makeISO8601Formatter() -> DateFormatter {
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-MM-dd"
        formatter.locale = Locale(identifier: "en_US_POSIX")
        return formatter
    }
}
```

---

### Phase 2: Post-Main Optimization

#### 2.1 Application Delegate Audit

```swift
// BEFORE: Heavy didFinishLaunching
func application(_ application: UIApplication,
                 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

    // All of these block first frame:
    setupDatabase()           // 150ms
    setupAnalytics()          // 80ms
    setupCrashReporting()     // 40ms
    setupRemoteConfig()       // 200ms (network!)
    setupPushNotifications()  // 30ms
    setupAppearance()         // 20ms
    checkMigrations()         // 100ms
    preloadCache()            // 300ms
    setupFeatureFlags()       // 50ms

    return true
}

// AFTER: Tiered initialization
func application(_ application: UIApplication,
                 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

    // TIER 1: Required before first frame (< 100ms total)
    setupCrashReporting()     // Must catch crashes from the start
    setupAppearance()         // Required for correct first frame

    // TIER 2: Required soon, but after first frame
    DispatchQueue.main.async { [weak self] in
        self?.setupDatabase()
        self?.checkMigrations()
        self?.setupAnalytics()
    }

    // TIER 3: Can wait until needed
    // setupRemoteConfig() -> call when first screen that uses it appears
    // preloadCache() -> load on demand
    // setupFeatureFlags() -> fetch async, use cached values initially

    return true
}
```

#### 2.2 Scene Delegate Optimization (UIKit)

```swift
// BEFORE: Heavy scene setup
func scene(_ scene: UIScene, willConnectTo session: UISceneSession,
           options connectionOptions: UIScene.ConnectionOptions) {
    guard let windowScene = scene as? UIWindowScene else { return }

    let window = UIWindow(windowScene: windowScene)

    // Blocking: Full navigation stack built synchronously
    let tabBar = buildFullTabBarController()   // Creates ALL tabs
    let nav = buildNavigationStack()           // Pushes initial VCs
    loadInitialData()                          // Synchronous network

    window.rootViewController = tabBar
    window.makeKeyAndVisible()
    self.window = window
}

// AFTER: Minimal first frame
func scene(_ scene: UIScene, willConnectTo session: UISceneSession,
           options connectionOptions: UIScene.ConnectionOptions) {
    guard let windowScene = scene as? UIWindowScene else { return }

    let window = UIWindow(windowScene: windowScene)

    // Show a lightweight root immediately
    let rootVC = LaunchViewController() // Minimal skeleton UI
    window.rootViewController = rootVC
    window.makeKeyAndVisible()
    self.window = window

    // Build full UI after first frame
    Task { @MainActor in
        let tabBar = await buildTabBarController()
        window.rootViewController = tabBar
    }
}
```

#### 2.3 SwiftUI App Launch Optimization

```swift
// BEFORE: Heavy App init
@main
struct MyApp: App {
    @StateObject private var store = AppStore() // Complex init
    @StateObject private var authManager = AuthManager() // Network calls

    init() {
        setupAppearance()
        setupAnalytics()
        migrateDatabase()
    }

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(store)
                .environmentObject(authManager)
        }
    }
}

// AFTER: Deferred initialization
@main
struct MyApp: App {
    @State private var store = AppStore.shared
    @State private var isReady = false

    var body: some Scene {
        WindowGroup {
            if isReady {
                ContentView()
                    .environment(store)
            } else {
                LaunchScreen()
                    .task {
                        await store.initialize()
                        isReady = true
                    }
            }
        }
    }
}
```

---

### Phase 3: Instruments Measurement

#### 3.1 App Launch Template

```
1. Product > Profile (Cmd+I)
2. Select "App Launch" template
3. Record a cold launch (ensure app was killed)
4. Analyze the timeline:
   - Process creation to first frame
   - Thread activity during launch
   - Identify longest blocking operations
5. Use the "Thread State" track to find blocked main thread time
```

#### 3.2 Custom Signposts for Measurement

```swift
import os.signpost

private let launchLog = OSLog(subsystem: "com.app.launch", category: "startup")

class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

        os_signpost(.begin, log: launchLog, name: "AppLaunch")

        os_signpost(.begin, log: launchLog, name: "CrashReporting")
        setupCrashReporting()
        os_signpost(.end, log: launchLog, name: "CrashReporting")

        os_signpost(.begin, log: launchLog, name: "Database")
        setupDatabase()
        os_signpost(.end, log: launchLog, name: "Database")

        os_signpost(.end, log: launchLog, name: "AppLaunch")
        return true
    }
}
```

#### 3.3 MetricKit Launch Diagnostics

```swift
import MetricKit

class MetricsManager: NSObject, MXMetricManagerSubscriber {
    func didReceive(_ payloads: [MXMetricPayload]) {
        for payload in payloads {
            if let launchMetrics = payload.applicationLaunchMetrics {
                let coldLaunch = launchMetrics.histogrammedTimeToFirstDraw
                    .bucketEnumerator
                // Log or send to analytics
                print("Cold launch histogram: \(coldLaunch)")
            }
        }
    }
}
```

---

## Expected Output

1. **Baseline Measurement** - Current cold and warm launch times with phase breakdown
2. **Pre-Main Analysis** - Dylib count, static initializers, rebase/bind overhead
3. **Post-Main Audit** - Categorized initialization work with timing per item
4. **Optimization Plan** - Tiered initialization strategy with expected savings
5. **Verification Report** - Before/after measurements confirming improvements

---

## Example Interaction

**User reports 3-second cold launch time. Agent analyzes AppDelegate:**

```swift
// BEFORE: AppDelegate.swift - 2.1 seconds in didFinishLaunching
func application(_ application: UIApplication,
                 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()                    // 200ms
    Realm.Configuration.defaultConfiguration = config  // 350ms (migration)
    IAPManager.shared.initialize()             // 150ms
    ThemeManager.shared.apply()                // 30ms
    AnalyticsService.shared.start()            // 80ms
    RemoteConfigService.shared.fetch()         // 800ms (network!)
    ImageCache.shared.warmup()                 // 400ms
    DeepLinkRouter.shared.configure()          // 20ms
    return true
}
```

**Agent produces optimized version:**

```swift
// AFTER: AppDelegate.swift - 230ms in didFinishLaunching
func application(_ application: UIApplication,
                 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

    // TIER 1: Critical path only (230ms)
    FirebaseApp.configure()                    // 200ms - crash reporting depends on this
    ThemeManager.shared.apply()                // 30ms - needed for correct first frame

    // TIER 2: After first frame
    Task.detached(priority: .userInitiated) {
        await RealmManager.shared.initialize() // Migration off main thread
    }

    DispatchQueue.main.async {
        AnalyticsService.shared.start()
        IAPManager.shared.initialize()
        DeepLinkRouter.shared.configure()
    }

    // TIER 3: On demand
    // RemoteConfigService - fetch when settings screen opens, use cached
    // ImageCache.warmup() - removed, use on-demand caching

    return true
}
```

**Impact:** 2.1s reduced to 230ms post-main (91% reduction).

---

## Techniques Used

- **ST-01** (Clear Objective): Focused launch time optimization
- **ST-02** (Sequential Instructions): Pre-main then post-main analysis
- **RT-02** (Multi-Format Output): Timeline, code, and measurement reports
- **AG-12** (Diagnostic Process): Systematic bottleneck identification
- **NE-02** (Phased Workflow): Measure, analyze, optimize, verify

---

## Related Prompts

- [ios_battery_energy_optimization.md](ios_battery_energy_optimization.md) - Launch efficiency impacts energy
- [ios_app_size_optimization.md](ios_app_size_optimization.md) - Binary size affects dylib loading
- [ios_code_modernization.md](ios_code_modernization.md) - Modern APIs often have faster initialization

---

## Customization Guide

### For Widget/Extension Launch

Focus on:
- Extensions have stricter memory and time budgets
- Minimize framework linking for extensions
- Share data via App Groups, not runtime initialization
- Use lightweight data access (UserDefaults, small files)

### For SwiftUI-First Apps

Focus on:
- `@main` App struct initialization cost
- `@State` and `@StateObject` initialization timing
- `task {}` modifier for deferred async work
- Preview-safe initialization patterns

### For Apps with Required Auth

Handle authentication without blocking:
- Show skeleton/cached UI immediately
- Check auth state asynchronously
- Transition to login flow if needed after first frame
- Cache auth tokens for instant validation

### For Large Enterprise Apps

Additional considerations:
- Module-level lazy initialization
- Dynamic framework vs static library analysis
- Build configuration impact (debug vs release timing)
- A/B testing framework initialization deferral
