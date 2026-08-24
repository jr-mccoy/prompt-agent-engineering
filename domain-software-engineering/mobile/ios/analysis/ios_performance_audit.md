---
title: "iOS Performance Audit"
category: mobile-development
description: "Identifies iOS performance bottlenecks including main thread blocking, allocations, Core Animation hitches, network waterfalls, and energy impact with Instruments profiling references"
techniques:
  - ST-01
  - RT-02
  - RT-04
  - AG-02
  - AG-12
difficulty: advanced
tags:
  - ios
  - swift
  - mobile-development
  - performance
  - instruments
  - core-animation
  - energy
updated: "2026-03-19"
---

# iOS Performance Audit

**Objective:** Identify iOS performance bottlenecks including main thread blocking, excessive allocations, Core Animation hitches, network request waterfalls, energy impact, and app launch time issues, referencing Instruments profiling workflows and providing prioritized remediation.

**When to Use:** Use this prompt when users report the app feels "slow" or "janky," when App Store reviews mention performance, before major releases to ensure quality, when Xcode Organizer shows regressions in metrics (hang rate, launch time, disk writes), or when battery drain complaints surface. Best used after a codebase health assessment identifies performance concerns.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before beginning the audit, gather context:

1. **Symptoms:**
   - "What specific performance issues have been reported? (slow scrolling, slow launch, freezes, battery drain, high memory)"
   - "Which screens or workflows feel slowest?"

2. **Metrics:**
   - "Have you checked Xcode Organizer metrics (hang rate, launch time, memory, disk writes)?"
   - "Do you have any Instruments traces or MetricKit reports?"

3. **Environment:**
   - "What is the minimum deployment target and oldest device you support?"
   - "Are there background tasks, extensions, or background refresh running?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual execution paths** - Don't flag based on theoretical bottlenecks. Verify the code path is actually executed frequently enough to matter.
2. **Check for existing optimizations** - Search for caching, lazy loading, prefetching, or throttling already in place.
3. **Understand the context** - Consider HOW the code is used. A heavy operation run once at startup is different from one in a scroll path.
4. **Confirm measurable impact** - Would fixing this produce a user-noticeable improvement?
5. **Provide specific file:line locations** - Every finding MUST include exact code locations.

**Finding NO critical performance issues is an acceptable outcome.** If the app performs reasonably for its complexity, say so.

### False-Positive Prevention

- ❌ Do NOT flag every async operation as a potential bottleneck
- ❌ Do NOT assume allocation counts alone indicate leaks
- ❌ Do NOT flag background work that doesn't affect UI responsiveness
- ❌ Do NOT report micro-optimizations as critical (e.g., String interpolation vs concatenation)
- ✅ DO focus on user-perceivable performance (scrolling, launch, transitions)
- ✅ DO consider device tier when assessing impact
- ✅ DO check if Instruments would confirm the theoretical issue
- ✅ DO prioritize main thread work over background inefficiencies

---

### Phase 1: App Launch Performance

#### 1.1 Launch Time Analysis

**Pre-main time factors:**

```swift
// Check for:
- Dynamic library count (each dylib adds ~1-5ms)
- +load methods in Objective-C categories
- Static initializers (__attribute__((constructor)))
- Large storyboard as launch screen vs LaunchScreen.storyboard
```

**Post-main time factors:**

```swift
// AppDelegate / @main App struct
- application(_:didFinishLaunchingWithOptions:) duration
- SceneDelegate scene(_:willConnectTo:) setup
- Initial view controller / root view complexity
- Synchronous network calls at launch
- Core Data / SwiftData store setup
- Third-party SDK initialization (Firebase, analytics)

// Measure with:
// DYLD_PRINT_STATISTICS environment variable
// Instruments: App Launch template
// os_signpost for custom intervals
```

**Launch optimization checklist:**

```swift
// Good: Defer non-essential work
func application(_ application: UIApplication,
                 didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // Essential only
    setupCrashReporting()
    configureAppearance()

    // Defer everything else
    DispatchQueue.main.async {
        self.setupAnalytics()
        self.prefetchData()
    }
    return true
}

// Bad: Synchronous heavy work at launch
func application(...) -> Bool {
    let data = try! Data(contentsOf: largeFileURL) // Blocks main thread
    CoreDataStack.shared.loadPersistentStores() // Synchronous migration
    FirebaseApp.configure() // Can be slow
    return true
}
```

#### 1.2 First Frame Rendering

**Analyze initial view complexity:**
- Root view body computation cost (SwiftUI)
- Initial view controller's viewDidLoad weight (UIKit)
- Placeholder / skeleton screen usage
- Image loading strategy for initial content

---

### Phase 2: Main Thread Analysis

#### 2.1 Main Thread Blocking

**Search for synchronous work on main thread:**

```swift
// File I/O on main thread
let data = try Data(contentsOf: url) // BLOCKING if on main
let image = UIImage(contentsOfFile: path) // BLOCKING for large images

// Synchronous network calls
let (data, _) = try await URLSession.shared.data(from: url)
// ^ Fine if called from Task, bad if awaited on MainActor without yielding

// JSON parsing on main thread
let decoder = JSONDecoder()
let items = try decoder.decode([Item].self, from: largeData) // BLOCKING

// Core Data on main context
let results = try context.fetch(fetchRequest) // BLOCKING if main context

// Heavy computation
let sorted = largeArray.sorted { ... } // BLOCKING
let filtered = items.filter { expensivePredicate($0) } // BLOCKING
```

#### 2.2 Hang Detection Patterns

**Identify potential hangs (>250ms main thread blocks):**

```swift
// Instruments: Time Profiler template, "Record Waiting Threads"
// MetricKit: MXHangDiagnostic

// Common hang sources:
- Synchronous keychain access (SecItemCopyMatching)
- File coordination (NSFileCoordinator)
- Contended locks (@synchronized, NSLock, os_unfair_lock)
- Regex evaluation on large strings
- Layout passes with complex Auto Layout
- Large diffable data source updates
```

---

### Phase 3: Memory & Allocations

#### 3.1 Memory Usage Analysis

**Check for excessive memory consumption:**

```swift
// Large image handling
UIImage(named: "hero") // Cached permanently in image cache
UIImage(contentsOfFile: path) // Not cached, but decoded in full

// Use downsized thumbnails:
let options = [kCGImageSourceThumbnailMaxPixelSize: 200,
               kCGImageSourceCreateThumbnailFromImageAlways: true] as CFDictionary

// Core Data batch size
let request = NSFetchRequest<Item>(entityName: "Item")
request.fetchBatchSize = 20 // Good: only faults 20 at a time
// Missing fetchBatchSize = loads all into memory
```

#### 3.2 Retain Cycle Detection

**Search for common retain cycle patterns:**

```swift
// Missing capture list in closure
viewModel.onComplete = {
    self.dismiss(animated: true) // RETAIN CYCLE: closure captures self strongly
}

// Fix:
viewModel.onComplete = { [weak self] in
    self?.dismiss(animated: true)
}

// Timer retain cycles
timer = Timer.scheduledTimer(withTimeInterval: 1, repeats: true) { _ in
    self.updateUI() // RETAIN CYCLE if timer is stored as property
}

// Combine publisher without proper cancellation
cancellable = publisher.sink { [weak self] value in
    self?.process(value)
}
// Ensure cancellable is stored and cancelled on deinit

// NotificationCenter (pre-iOS 9 pattern, but check for custom implementations)
NotificationCenter.default.addObserver(self, selector: #selector(handle), name: .update, object: nil)
// Must removeObserver — or use closure-based API with stored token
```

#### 3.3 Autorelease Pool Usage

```swift
// Processing large collections
for item in veryLargeArray {
    autoreleasepool {
        let processed = processItem(item) // Prevents memory spike
        results.append(processed)
    }
}
```

---

### Phase 4: UI Rendering Performance

#### 4.1 Core Animation Hitches

**Identify hitch sources (commits > 16.67ms on 60Hz, 8.33ms on 120Hz):**

```swift
// Offscreen rendering triggers:
view.layer.cornerRadius = 10
view.layer.masksToBounds = true // Forces offscreen pass if combined with shadow
view.layer.shadowOffset = CGSize(width: 0, height: 2)
// Fix: use shadowPath or pre-render

// Excessive transparency / blending
view.backgroundColor = .clear // Forces blending with content behind
label.backgroundColor = .clear // On opaque backgrounds, set to match parent

// Large images in cells
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    cell.imageView?.image = UIImage(named: hugeImageName) // Decoded on main thread
    // Fix: Use thumbnail, decode on background, cache
}
```

#### 4.2 SwiftUI Performance

**Check for SwiftUI-specific issues:**

```swift
// Excessive body recomputation
struct ParentView: View {
    @StateObject var viewModel = ViewModel() // Good: created once

    var body: some View {
        // If viewModel publishes frequently, entire body re-evaluates
        List(viewModel.items) { item in
            ExpensiveRow(item: item) // Recomputed every publish
        }
    }
}

// Fix: Use EquatableView or extract subviews with own @ObservedObject
// Use Instruments: SwiftUI template to see body evaluation counts

// Missing .id() causing identity issues
ForEach(items) { item in // Ensure Item conforms to Identifiable properly
    ItemRow(item: item)
}

// Expensive computed properties in View body
var body: some View {
    let sortedItems = items.sorted() // Runs on every body call
    // Fix: move to ViewModel or use .onChange
}
```

#### 4.3 Collection View / Table View Performance

```swift
// Cell reuse configuration
func collectionView(_ collectionView: UICollectionView,
                    cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
    // Check for:
    // - Cell registration (modern API vs dequeueReusableCell crash)
    // - Image loading (async with placeholder vs synchronous)
    // - Auto Layout complexity per cell
    // - prepareForReuse() cleanup
}

// Prefetching implementation
func collectionView(_ collectionView: UICollectionView,
                    prefetchItemsAt indexPaths: [IndexPath]) {
    // Should prefetch images/data for upcoming cells
}
```

---

### Phase 5: Networking Performance

#### 5.1 Network Request Waterfalls

**Identify sequential request chains:**

```swift
// Anti-pattern: Waterfall requests
let user = try await api.fetchUser()
let profile = try await api.fetchProfile(userId: user.id) // Waits for user
let settings = try await api.fetchSettings(userId: user.id) // Waits for profile
// Total time: sum of all three

// Fix: Parallel where possible
async let user = api.fetchUser()
async let settings = api.fetchAppSettings()
let (userData, settingsData) = try await (user, settings)
let profile = try await api.fetchProfile(userId: userData.id)
// Total time: max(user, settings) + profile
```

#### 5.2 Caching Strategy

```swift
// URLCache configuration
let cache = URLCache(memoryCapacity: 50_000_000, diskCapacity: 100_000_000)
URLSession.shared.configuration.urlCache = cache

// HTTP caching headers respected?
// ETag / If-None-Match usage?
// Custom application-level caching (NSCache, disk)?
```

---

### Phase 6: Energy Impact

#### 6.1 Background Activity

```swift
// Background refresh
func application(_ application: UIApplication,
                 performFetchWithCompletionHandler completionHandler: ...) {
    // Check: Is work minimal and efficient?
}

// Background URLSession
let config = URLSessionConfiguration.background(withIdentifier: "com.app.upload")
// Check: Proper handling of background completion

// Location services
locationManager.desiredAccuracy = kCLLocationAccuracyBest // HIGH energy
// Use kCLLocationAccuracyHundredMeters when exact position not needed
locationManager.allowsBackgroundLocationUpdates = true // Check if truly needed
```

#### 6.2 Timer and Polling

```swift
// Aggressive polling
Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { ... }
// Consider: Push notifications, WebSocket, or longer intervals

// Display link when not needed
displayLink = CADisplayLink(target: self, selector: #selector(update))
displayLink.add(to: .current, forMode: .common)
// Check: Is it paused when not visible?
```

---

### Phase 7: Performance Report

```markdown
# Performance Audit Report: [App Name]

## Executive Summary

### Performance Score: [A/B/C/D/F]

| Category | Score | Impact |
|----------|-------|--------|
| Launch Time | [1-10] | [X.Xs cold launch] |
| Main Thread Health | [1-10] | [X hangs/hour] |
| Memory Efficiency | [1-10] | [X MB peak] |
| Scroll Performance | [1-10] | [X hitches/scroll] |
| Network Efficiency | [1-10] | [Assessment] |
| Energy Impact | [1-10] | [Assessment] |

### Critical Findings

| # | Finding | Location | Impact | Fix Effort |
|---|---------|----------|--------|------------|
| 1 | [Finding] | [file:line] | [User impact] | [Hours/Days] |
| 2 | [Finding] | [file:line] | [User impact] | [Hours/Days] |

### Instruments Templates to Run

| Issue | Template | What to Look For |
|-------|----------|-----------------|
| Slow launch | App Launch | Pre-main + post-main breakdown |
| Hangs | Time Profiler | Heaviest stack traces on main |
| Memory | Allocations / Leaks | Growth over time, leaked objects |
| Scrolling | Core Animation | Commit duration, offscreen renders |
| Energy | Energy Log | CPU wake-ups, location, networking |

### Optimization Roadmap

#### Quick Wins (< 1 day each)
1. [Optimization with expected improvement]
2. [Optimization with expected improvement]

#### Medium Effort (1-3 days)
1. [Optimization with expected improvement]

#### Significant Refactoring (1+ weeks)
1. [Optimization with expected improvement]
```

---

## Expected Output

1. **Launch Time Analysis** - Pre-main and post-main breakdown with bottlenecks
2. **Main Thread Report** - Blocking operations with severity and locations
3. **Memory Assessment** - Allocation patterns, retain cycles, peak usage
4. **Rendering Analysis** - Hitch sources, offscreen renders, recomposition costs
5. **Network Efficiency** - Waterfall detection, caching assessment
6. **Energy Report** - Background activity, polling, location services
7. **Prioritized Remediation** - Ordered by user-perceivable impact

---

## Example Interaction

**User:** Our app takes about 4 seconds to launch and scrolling in the feed is janky. We support iOS 16+ and our oldest test device is iPhone 11.

**Agent:** I'll conduct a performance audit focusing on launch time and scroll performance. Let me analyze the codebase.

*[Agent performs analysis]*

**Agent:**

### Critical Findings

1. **Launch: Synchronous Core Data migration** - `AppDelegate.swift:42` calls `loadPersistentStores()` synchronously. On first launch after an update with a migration, this blocks for 2-3 seconds. Move to background with a loading state.

2. **Launch: Firebase + Analytics init** - `AppDelegate.swift:28-35` initializes Firebase, Mixpanel, and Amplitude sequentially in `didFinishLaunching`. Defer to first `DispatchQueue.main.async` or even after first frame renders.

3. **Scroll: Full-resolution images in cells** - `FeedCell.swift:67` loads full 4K images via `UIImage(data:)` then lets the cell resize them. Use `CGImageSource` thumbnail API or Kingfisher's `.processor(.downsampling(size:))`.

4. **Scroll: Shadow without shadowPath** - `FeedCell.swift:23-26` sets `layer.shadowOffset` and `layer.cornerRadius` with `masksToBounds = true`, forcing offscreen render per cell. Set explicit `shadowPath` to a rounded rect.

**Estimated improvement:** Launch drops to ~1.5s, scroll hitches reduced by ~80%.

---

## Techniques Used

- **ST-01** (Clear Objective): Focused performance analysis objective
- **RT-02** (Multi-Dimensional Analysis): Six-category performance framework
- **RT-04** (Best Practice Review): Apple performance best practices and WWDC guidance
- **AG-02** (Skeptical Default Stance): Evidence-based findings only
- **AG-12** (Quantitative Metrics): Measurable performance targets

---

## Related Prompts

- [ios_codebase_health_assessment.md](ios_codebase_health_assessment.md) - Broader codebase evaluation
- [ios_technical_debt_assessment.md](ios_technical_debt_assessment.md) - Performance-related tech debt
- [ios_swiftui_migration_analysis.md](ios_swiftui_migration_analysis.md) - SwiftUI performance considerations
- [ios_ai_code_review.md](ios_ai_code_review.md) - Code-level performance patterns

---

## Customization Guide

### For Launch Time Focus
- Deep dive into pre-main (dylib loading, ObjC runtime)
- Profile didFinishLaunching with os_signpost
- Measure time-to-first-frame vs time-to-interactive

### For Scroll Performance Focus
- Concentrate on cell configuration cost
- Profile with Core Animation instrument
- Check prefetching and image pipeline

### For Memory Focus
- Run Leaks instrument analysis
- Check for abandoned memory (allocations growing without leaks)
- Profile with Memory Graph Debugger

### For Energy Focus
- Profile background activity with Energy Log
- Check location accuracy requirements
- Audit timer intervals and background modes
