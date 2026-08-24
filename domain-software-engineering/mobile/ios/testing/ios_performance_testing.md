---
title: "iOS Performance Testing"
category: mobile-development
description: "Detect performance regressions using XCTest measure blocks, os_signpost instrumentation, and custom metrics with Instruments guidance for profiling iOS apps"
techniques:
  - ST-01
  - RT-02
  - AG-12
  - DS-02
difficulty: advanced
tags:
  - ios
  - swift
  - testing
  - performance
  - xctest
  - instruments
  - os-signpost
updated: "2026-03-19"
---

# iOS Performance Testing

**Objective:** Detect performance regressions in iOS applications using XCTest measure blocks for automated benchmarking, os_signpost for precise interval instrumentation, and custom XCTMetric implementations for domain-specific measurements. Includes guidance on using Instruments for profiling and establishing performance baselines that can be tracked in CI.

**When to Use:** Use this prompt when app launch time has degraded, when scroll performance stutters, when a feature's response time has regressed, when Core Data or network operations are slower than expected, or when preparing performance baselines before a major release. Also useful when establishing performance budgets for new features.

**Prompt Type:** Modular (200-250 lines)

---

## Context Gathering

1. **Performance Concern:**
   - "What specific performance issue are you investigating (launch time, scroll jank, memory growth, API latency)?"
   - "Is there a measurable regression, or are you establishing baselines?"

2. **Application Profile:**
   - "What's the app's launch time target? Current measurement?"
   - "How large is the typical dataset (Core Data entities, list items, cached images)?"

3. **Measurement Infrastructure:**
   - "Are performance tests currently run in CI?"
   - "Is there an existing performance baseline or budget?"

4. **Instruments Experience:**
   - "Has the team used Instruments (Time Profiler, Allocations, Core Animation) before?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before generating ANY performance test, you MUST:**

1. **Define the metric precisely** - "Performance" is vague. Specify: wall clock time, CPU time, memory peak, memory growth, disk I/O, or frame rate.
2. **Establish a realistic baseline** - Run the test multiple times on the same hardware to determine natural variance before setting pass/fail thresholds.
3. **Control the environment** - Performance tests are sensitive to background processes, thermal state, and battery level. Tests must account for variance.
4. **Use appropriate sample sizes** - XCTest `measure` runs the block multiple times (default 5). Do not reduce iterations to hide flakiness.
5. **Test on representative data** - A performance test with 10 items won't catch O(n^2) regressions that appear at 10,000 items.

**Performance tests that fail intermittently due to environment noise are worse than no tests.** Set thresholds with sufficient margin for natural variance (typically 15-25%).

### False-Positive Prevention

- ❌ Do NOT set pass/fail thresholds tighter than natural variance (causes flaky failures)
- ❌ Do NOT measure Debug builds (compiler optimizations are disabled)
- ❌ Do NOT run performance tests on CI with shared runners (noisy neighbors)
- ❌ Do NOT measure one-time costs (first launch, migration) as steady-state performance
- ❌ Do NOT ignore warm-up runs that skew averages
- ✅ DO test with Release build configuration for realistic measurements
- ✅ DO use dedicated CI runners or test devices for consistent results
- ✅ DO separate cold-start from warm-start measurements
- ✅ DO document the hardware/simulator used for baselines
- ✅ DO set baselines in Xcode and track trends over time

---

### Module 1: XCTest Measure Blocks

```swift
import XCTest
@testable import MyApp

final class AppLaunchPerformanceTests: XCTestCase {

    // MARK: - App Launch Time

    func test_appLaunch_coldStart() throws {
        // Measures the full app launch sequence
        // Set a baseline in Xcode: Editor > Set Baseline
        measure(metrics: [XCTApplicationLaunchMetric()]) {
            XCUIApplication().launch()
        }
    }

    func test_appLaunch_warmStart() throws {
        // App is already in memory, measures resume time
        let app = XCUIApplication()
        app.launch()

        measure(metrics: [XCTApplicationLaunchMetric(waitUntilResponsive: true)]) {
            app.activate()
        }
    }
}

final class DataProcessingPerformanceTests: XCTestCase {

    // MARK: - Clock Time (Wall Clock)

    func test_jsonParsing_1000Items() {
        let jsonData = TestFixtures.largeUserListJSON(count: 1000)

        measure(metrics: [XCTClockMetric()]) {
            _ = try? JSONDecoder().decode([User].self, from: jsonData)
        }
    }

    // MARK: - CPU Time

    func test_imageProcessing_cpuTime() {
        let image = TestFixtures.sampleImage(size: CGSize(width: 4000, height: 3000))

        measure(metrics: [XCTCPUMetric()]) {
            _ = ImageProcessor.resize(image, to: CGSize(width: 400, height: 300))
        }
    }

    // MARK: - Memory

    func test_feedLoading_memoryUsage() {
        measure(metrics: [XCTMemoryMetric()]) {
            let viewModel = FeedViewModel(repository: LargeFeedRepository(itemCount: 500))
            _ = viewModel.loadInitialPage()
        }
    }

    // MARK: - Combined Metrics

    func test_searchOperation_allMetrics() {
        let dataset = TestFixtures.searchableDataset(size: 10_000)

        measure(
            metrics: [
                XCTClockMetric(),
                XCTCPUMetric(),
                XCTMemoryMetric(),
                XCTStorageMetric(),
            ]
        ) {
            _ = SearchEngine.search(query: "test query", in: dataset)
        }
    }

    // MARK: - Custom Options

    func test_coreDataFetch_withOptions() {
        let options = XCTMeasureOptions()
        options.iterationCount = 10  // More iterations for stable results

        measure(
            metrics: [XCTClockMetric()],
            options: options
        ) {
            let context = TestCoreDataStack().viewContext
            let request = NSFetchRequest<UserEntity>(entityName: "UserEntity")
            request.fetchLimit = 100
            _ = try? context.fetch(request)
        }
    }
}
```

### Module 2: os_signpost Instrumentation

```swift
import os.signpost
@testable import MyApp

// MARK: - Production Code: Signpost Instrumentation

extension OSLog {
    static let performance = OSLog(
        subsystem: Bundle.main.bundleIdentifier ?? "com.app",
        category: "Performance"
    )
    static let networking = OSLog(
        subsystem: Bundle.main.bundleIdentifier ?? "com.app",
        category: "Networking"
    )
    static let dataLayer = OSLog(
        subsystem: Bundle.main.bundleIdentifier ?? "com.app",
        category: "DataLayer"
    )
}

// Instrument a network request:
class APIClient {

    func fetchUser(id: String) async throws -> User {
        let signpostID = OSSignpostID(log: .networking)

        os_signpost(
            .begin,
            log: .networking,
            name: "FetchUser",
            signpostID: signpostID,
            "Fetching user %{public}@", id
        )

        defer {
            os_signpost(
                .end,
                log: .networking,
                name: "FetchUser",
                signpostID: signpostID,
                "Completed"
            )
        }

        let (data, response) = try await session.data(for: request)
        return try decoder.decode(User.self, from: data)
    }
}

// Instrument a Core Data operation:
class UserStore {

    func fetchAll() throws -> [User] {
        let signpostID = OSSignpostID(log: .dataLayer)

        os_signpost(.begin, log: .dataLayer, name: "FetchAllUsers", signpostID: signpostID)

        let request = NSFetchRequest<UserEntity>(entityName: "UserEntity")
        let entities = try context.fetch(request)

        os_signpost(
            .end,
            log: .dataLayer,
            name: "FetchAllUsers",
            signpostID: signpostID,
            "Fetched %d users", entities.count
        )

        return entities.map(\.toDomainModel)
    }
}

// Instrument a view appearance:
struct FeedView: View {
    let signpostID = OSSignpostID(log: .performance)

    var body: some View {
        List(items) { item in
            FeedItemRow(item: item)
        }
        .onAppear {
            os_signpost(.begin, log: .performance, name: "FeedView.Visible", signpostID: signpostID)
        }
        .onDisappear {
            os_signpost(.end, log: .performance, name: "FeedView.Visible", signpostID: signpostID)
        }
    }
}
```

### Module 3: Custom XCTMetric

```swift
import XCTest
@testable import MyApp

// MARK: - Custom Metric: Frame Drop Counter

/// Counts dropped frames during a measure block
final class FrameDropMetric: NSObject, XCTMetric {

    private var displayLink: CADisplayLink?
    private var previousTimestamp: CFTimeInterval = 0
    private var droppedFrames: Int = 0
    private let targetFrameDuration: CFTimeInterval = 1.0 / 60.0

    func reportMeasurements(
        from startTime: XCTPerformanceMeasurementTimestamp,
        to endTime: XCTPerformanceMeasurementTimestamp
    ) throws -> [XCTPerformanceMeasurement] {
        [
            XCTPerformanceMeasurement(
                identifier: "com.app.frameDrops",
                displayName: "Dropped Frames",
                doubleValue: Double(droppedFrames),
                unitSymbol: "frames"
            )
        ]
    }

    func willBeginMeasuring() {
        droppedFrames = 0
        previousTimestamp = 0
        displayLink = CADisplayLink(target: self, selector: #selector(tick))
        displayLink?.add(to: .main, forMode: .common)
    }

    func didStopMeasuring() {
        displayLink?.invalidate()
        displayLink = nil
    }

    @objc private func tick(_ link: CADisplayLink) {
        if previousTimestamp > 0 {
            let elapsed = link.timestamp - previousTimestamp
            if elapsed > targetFrameDuration * 1.5 {
                droppedFrames += Int(elapsed / targetFrameDuration) - 1
            }
        }
        previousTimestamp = link.timestamp
    }

    func copy(with zone: NSZone? = nil) -> Any {
        FrameDropMetric()
    }
}
```

### Module 4: Scroll Performance Tests

```swift
final class ScrollPerformanceTests: XCTestCase {

    private var app: XCUIApplication!

    override func setUpWithError() throws {
        continueAfterFailure = false
        app = XCUIApplication()
        app.launchArguments = ["--uitesting", "--preload-feed-500"]
        app.launch()
    }

    func test_feedScroll_performance() {
        let feedList = app.collectionViews["home_feed_list"]
        XCTAssertTrue(feedList.waitForExistence(timeout: 5))

        let options = XCTMeasureOptions()
        options.iterationCount = 3

        measure(
            metrics: [XCTOSSignpostMetric.scrollDecelerationMetric],
            options: options
        ) {
            feedList.swipeUp(velocity: .fast)
        }
    }

    func test_feedScroll_hitch_rate() throws {
        let feedList = app.collectionViews["home_feed_list"]
        XCTAssertTrue(feedList.waitForExistence(timeout: 5))

        // XCTOSSignpostMetric tracks animation hitches
        measure(metrics: [XCTOSSignpostMetric.scrollDraggingMetric]) {
            feedList.swipeUp(velocity: .slow)
            feedList.swipeDown(velocity: .slow)
        }
    }
}
```

### Module 5: Memory Leak Detection

```swift
final class MemoryLeakTests: XCTestCase {

    // MARK: - Retain Cycle Detection

    func test_viewModel_doesNotRetainSelf() {
        var viewModel: UserProfileViewModel? = UserProfileViewModel(
            repository: MockUserRepository()
        )
        weak var weakRef = viewModel

        // Simulate lifecycle
        Task {
            await viewModel?.loadUser(id: "1")
        }

        // Release strong reference
        viewModel = nil

        // Allow async work to complete
        let expectation = expectation(description: "dealloc")
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
            XCTAssertNil(weakRef, "ViewModel should be deallocated - possible retain cycle")
            expectation.fulfill()
        }
        wait(for: [expectation], timeout: 2)
    }

    // MARK: - Memory Growth Under Load

    func test_imageCache_doesNotGrowUnbounded() {
        let cache = ImageCache(maxSize: 50 * 1024 * 1024) // 50MB limit

        measure(metrics: [XCTMemoryMetric()]) {
            // Load 200 images - cache should evict
            for i in 0..<200 {
                let image = TestFixtures.sampleImage(
                    size: CGSize(width: 500, height: 500)
                )
                cache.store(image, forKey: "img_\(i)")
            }
        }

        // Verify cache respects its limit
        XCTAssertLessThan(
            cache.currentSize,
            55 * 1024 * 1024,
            "Cache should stay near its 50MB limit"
        )
    }
}
```

### Module 6: Instruments Profiling Guide

```
Instruments Profiling Workflow:
─────────────────────────────

1. TIME PROFILER (CPU hotspots)
   Product > Profile > Time Profiler
   - Look for: Functions taking >10ms on main thread
   - Sort by: Self Weight (descending)
   - Filter: Your app's binary (hide system frameworks)
   - Action: Move heavy work to background queue

2. ALLOCATIONS (Memory issues)
   Product > Profile > Allocations
   - Mark Generation before/after actions
   - Look for: Objects that persist across generations (leaks)
   - Filter: Allocation type = "Persistent"
   - Action: Break retain cycles, use weak references

3. CORE ANIMATION (Rendering)
   Product > Profile > Core Animation
   - Enable: Color Blended Layers, Color Offscreen-Rendered
   - Look for: Red/yellow blended areas (expensive compositing)
   - Target: <16.67ms per frame (60fps)
   - Action: Reduce transparency, pre-render complex layers

4. NETWORK (API performance)
   Product > Profile > Network
   - Look for: Requests >500ms, redundant requests
   - Check: Response sizes, compression, caching headers
   - Action: Add caching, reduce payload, use HTTP/2

5. SIGNPOST (Custom intervals)
   Product > Profile > Instruments > os_signpost
   - Visualize custom-instrumented intervals
   - Correlate with CPU/memory activity
   - Identify: Gaps, overlaps, unexpected durations
```

---

## Expected Output

1. **XCTest Measure Blocks** - Automated benchmarks for critical paths
2. **os_signpost Instrumentation** - Production code annotations for Instruments
3. **Custom Metrics** - Domain-specific measurement classes
4. **Scroll Performance Tests** - Frame rate and hitch detection
5. **Memory Tests** - Leak detection and growth bounds
6. **Instruments Guide** - Step-by-step profiling workflow

---

## Example Interaction

**User:** "Our app launch time degraded from 1.2s to 2.8s after adding a new analytics SDK. Help us measure and track it."

**Agent Response:**

```swift
import XCTest

final class LaunchPerformanceTests: XCTestCase {

    // MARK: - Launch Time Regression Detection

    func test_coldLaunch_staysUnder2Seconds() {
        // Set baseline: Editor > Set Baseline after first run
        // Baseline: 1.2s, Max acceptable: 2.0s
        measure(metrics: [XCTApplicationLaunchMetric()]) {
            XCUIApplication().launch()
        }
    }

    func test_launchPhases_instrumented() {
        // Add to AppDelegate to identify which phase regressed:
        //
        //   os_signpost(.begin, log: .performance, name: "AppLaunch.Phase1.SDKInit")
        //   AnalyticsSDK.initialize(config: config)
        //   os_signpost(.end, log: .performance, name: "AppLaunch.Phase1.SDKInit")
        //
        //   os_signpost(.begin, log: .performance, name: "AppLaunch.Phase2.DataLoad")
        //   loadInitialData()
        //   os_signpost(.end, log: .performance, name: "AppLaunch.Phase2.DataLoad")
        //
        //   os_signpost(.begin, log: .performance, name: "AppLaunch.Phase3.UISetup")
        //   setupRootViewController()
        //   os_signpost(.end, log: .performance, name: "AppLaunch.Phase3.UISetup")

        measure(metrics: [
            XCTApplicationLaunchMetric(waitUntilResponsive: true),
            XCTClockMetric(),
            XCTCPUMetric(),
        ]) {
            XCUIApplication().launch()
        }
    }
}

// Investigation steps:
// 1. Run test_coldLaunch to confirm regression (2.8s vs 1.2s baseline)
// 2. Add os_signpost to each launch phase
// 3. Profile with Instruments > Time Profiler
// 4. Likely fix: Defer analytics SDK init to after first frame
//    - Move AnalyticsSDK.initialize() to applicationDidBecomeActive
//    - Or use background queue: DispatchQueue.global().async { AnalyticsSDK.initialize() }
```

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on measurable performance regression detection
- **RT-02** (Step-by-Step Reasoning): Modular progression from basic measurement to advanced instrumentation
- **AG-12** (Iterative Refinement): Baseline establishment and threshold tuning over time
- **DS-02** (Domain Expertise): XCTest performance APIs, os_signpost, Instruments workflow

---

## Related Prompts

- [ios_test_strategy_design.md](ios_test_strategy_design.md) - Where performance tests fit in the overall strategy
- [ios_integration_testing.md](ios_integration_testing.md) - Integration tests for data layer performance
- [ios_unit_test_generation.md](ios_unit_test_generation.md) - Unit tests for algorithmic performance

---

## Customization Guide

| Aspect | How to Customize |
|--------|-----------------|
| **Metrics** | Add `XCTStorageMetric` for disk-heavy operations, or custom network latency metrics |
| **Thresholds** | Adjust baselines per hardware: physical devices are faster than simulators |
| **CI Integration** | Export performance results as JSON from `xcresult` bundles for trend dashboards |
| **Profiling Tools** | Use MetricKit for production performance monitoring alongside test-time Instruments |
| **Real Devices** | Run on physical devices for realistic thermal throttling and actual GPU performance |
| **Baseline Management** | Store baselines per device class (SE, standard, Pro Max) in Xcode test plans |
