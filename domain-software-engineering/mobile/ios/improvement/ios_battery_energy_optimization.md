---
title: "iOS Battery and Energy Optimization"
category: mobile-development
description: "Reduce iOS app energy consumption by optimizing location services, minimizing background processing, reducing network activity, deferring non-urgent work, and profiling with Energy Diagnostics"
techniques:
  - ST-01
  - RT-02
  - AG-02
  - AG-12
difficulty: advanced
tags:
  - ios
  - swift
  - battery
  - energy
  - performance
  - background-processing
updated: "2026-03-19"
---

# iOS Battery and Energy Optimization

**Objective:** Reduce an iOS app's energy consumption by optimizing location services usage, minimizing background processing, reducing unnecessary network activity, deferring non-urgent work, and using Energy Diagnostics in Instruments to measure and verify improvements.

**When to Use:** Use this prompt when users report excessive battery drain attributed to the app, when Xcode Organizer shows high energy impact metrics, when implementing location or background features, or proactively during performance optimization to ensure the app is a good citizen on the device.

**Prompt Type:** Modular (400-500 lines)

---

## Context Gathering

Before optimizing, understand the energy profile:

1. **Current Features:**
   - "Does the app use location services? What accuracy and frequency?"
   - "Are there background tasks? (Background fetch, processing, audio, VOIP)"
   - "How frequently does the app make network requests?"

2. **Symptoms:**
   - "Have users reported battery drain?"
   - "What does Xcode Organizer Energy report show?"
   - "Are there background crashes or terminations?"

3. **Requirements:**
   - "Which features genuinely need continuous location or background execution?"
   - "What is the acceptable latency for data freshness?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Profile with Instruments** - Do not guess at energy hotspots. Use the Energy Log template.
2. **Verify the overhead** - Not all background work is wasteful; verify frequency and duration.
3. **Check system coalescing** - iOS already batches some operations; confirm the overhead is app-caused.
4. **Measure before and after** - Provide quantified energy improvement, not just code changes.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations.

**Finding LOW energy usage is an acceptable outcome.** Some apps are naturally energy-efficient. Do not manufacture optimization opportunities.

### False-Positive Prevention

- ❌ Do NOT recommend removing location services that are core app features
- ❌ Do NOT flag all background tasks as wasteful (some are essential)
- ❌ Do NOT assume network requests are always excessive without frequency data
- ❌ Do NOT disable system features users depend on
- ✅ DO profile on a real device (Simulator has no energy metrics)
- ✅ DO test with the app in the background for extended periods
- ✅ DO check if iOS is already coalescing the work
- ✅ DO verify improvements with Energy Log instrument

---

### Module 1: Location Services Optimization

#### 1.1 Accuracy Level Selection

```swift
// WASTEFUL: GPS accuracy when approximate is sufficient
class LocationManager: NSObject, CLLocationManagerDelegate {
    let manager = CLLocationManager()

    func startTracking() {
        manager.desiredAccuracy = kCLLocationAccuracyBest // GPS radio active
        manager.distanceFilter = kCLDistanceFilterNone     // Every tiny movement
        manager.startUpdatingLocation()                    // Continuous
    }
}

// OPTIMIZED: Match accuracy to actual need
class LocationManager: NSObject, CLLocationManagerDelegate {
    let manager = CLLocationManager()

    func startTracking(for useCase: LocationUseCase) {
        switch useCase {
        case .cityLevelWeather:
            // Approximate location, no GPS needed
            manager.desiredAccuracy = kCLLocationAccuracyThreeKilometers
            manager.requestLocation() // One-shot, not continuous

        case .navigationTurnByTurn:
            // GPS needed, but only while in use
            manager.desiredAccuracy = kCLLocationAccuracyBestForNavigation
            manager.activityType = .automotiveNavigation
            manager.startUpdatingLocation()

        case .runTracking:
            manager.desiredAccuracy = kCLLocationAccuracyBest
            manager.activityType = .fitness
            manager.distanceFilter = 10 // Update every 10 meters, not every centimeter
            manager.startUpdatingLocation()

        case .geofencing:
            // No continuous location needed
            let region = CLCircularRegion(center: coordinate, radius: 200, identifier: "office")
            manager.startMonitoring(for: region) // Extremely low power
        }
    }
}
```

#### 1.2 Location Session Management

```swift
// WASTEFUL: Location updates never stopped
class ViewController: UIViewController {
    let locationManager = CLLocationManager()

    override func viewDidLoad() {
        super.viewDidLoad()
        locationManager.startUpdatingLocation()
    }
    // Never calls stopUpdatingLocation()!
}

// OPTIMIZED: Lifecycle-aware location management
class ViewController: UIViewController {
    let locationManager = CLLocationManager()

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        locationManager.startUpdatingLocation()
    }

    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        locationManager.stopUpdatingLocation()
    }
}

// SwiftUI:
struct MapView: View {
    @StateObject private var locationManager = LocationManager()

    var body: some View {
        Map(coordinateRegion: $region)
            .onAppear { locationManager.startUpdating() }
            .onDisappear { locationManager.stopUpdating() }
    }
}
```

---

### Module 2: Background Processing Optimization

#### 2.1 Background Task Efficiency

```swift
// WASTEFUL: Long background processing without time management
func application(_ application: UIApplication,
                 performFetchWithCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void) {
    // Runs expensive sync on every background fetch opportunity
    fullDatabaseSync() // May take 60+ seconds
    completionHandler(.newData)
}

// OPTIMIZED: Efficient background task with BGTaskScheduler
func scheduleBackgroundRefresh() {
    let request = BGAppRefreshTaskRequest(identifier: "com.app.refresh")
    request.earliestBeginDate = Date(timeIntervalSinceNow: 15 * 60) // 15 min minimum
    try? BGTaskScheduler.shared.submit(request)
}

func handleAppRefresh(task: BGAppRefreshTask) {
    // Schedule next refresh
    scheduleBackgroundRefresh()

    let syncTask = Task {
        do {
            // Only sync what has changed, not full database
            let lastSync = UserDefaults.standard.object(forKey: "lastSync") as? Date ?? .distantPast
            let changes = try await api.fetchChanges(since: lastSync)

            if changes.isEmpty {
                task.setTaskCompleted(success: true)
                return
            }

            try await database.apply(changes)
            UserDefaults.standard.set(Date(), forKey: "lastSync")
            task.setTaskCompleted(success: true)
        } catch {
            task.setTaskCompleted(success: false)
        }
    }

    task.expirationHandler = {
        syncTask.cancel()
    }
}
```

#### 2.2 Background URL Session

```swift
// WASTEFUL: Foreground downloads that fail when app backgrounds
func downloadFile(url: URL) async throws -> URL {
    let (localURL, _) = try await URLSession.shared.download(from: url)
    return localURL
    // Fails if user switches apps during download
}

// OPTIMIZED: Background URL session that continues when app is suspended
class DownloadManager: NSObject, URLSessionDownloadDelegate {
    lazy var backgroundSession: URLSession = {
        let config = URLSessionConfiguration.background(withIdentifier: "com.app.downloads")
        config.isDiscretionary = true            // iOS picks optimal time
        config.sessionSendsLaunchEvents = true   // Wake app on completion
        config.allowsExpensiveNetworkAccess = false // Wi-Fi only for large files
        config.allowsConstrainedNetworkAccess = false // Not on Low Data Mode
        return URLSession(configuration: config, delegate: self, delegateQueue: nil)
    }()

    func scheduleDownload(url: URL) {
        let task = backgroundSession.downloadTask(with: url)
        task.earliestBeginDate = Date(timeIntervalSinceNow: 60) // Defer if not urgent
        task.countOfBytesClientExpectsToSend = 200    // Small request
        task.countOfBytesClientExpectsToReceive = 5_000_000 // ~5MB response
        task.resume()
    }
}
```

---

### Module 3: Network Activity Reduction

#### 3.1 Request Coalescing and Caching

```swift
// WASTEFUL: Duplicate requests for the same data
class ProfileService {
    func getProfile() async throws -> Profile {
        // Called from 5 different screens, each making a new request
        let (data, _) = try await URLSession.shared.data(from: profileURL)
        return try JSONDecoder().decode(Profile.self, from: data)
    }
}

// OPTIMIZED: Request deduplication and caching
actor ProfileService {
    private var cachedProfile: (profile: Profile, timestamp: Date)?
    private var activeRequest: Task<Profile, Error>?

    func getProfile(maxAge: TimeInterval = 300) async throws -> Profile {
        // Return cached if fresh enough
        if let cached = cachedProfile, Date().timeIntervalSince(cached.timestamp) < maxAge {
            return cached.profile
        }

        // Deduplicate in-flight requests
        if let activeRequest = activeRequest {
            return try await activeRequest.value
        }

        let task = Task {
            let (data, _) = try await URLSession.shared.data(from: profileURL)
            let profile = try JSONDecoder().decode(Profile.self, from: data)
            cachedProfile = (profile, Date())
            activeRequest = nil
            return profile
        }

        activeRequest = task
        return try await task.value
    }
}
```

#### 3.2 Constrained Network Awareness

```swift
// WASTEFUL: Large downloads regardless of network condition
func syncMedia() async throws {
    for item in pendingMedia {
        try await downloadMedia(item) // Even on cellular/low data mode
    }
}

// OPTIMIZED: Network-aware downloads
func syncMedia() async throws {
    let monitor = NWPathMonitor()
    let path = await withCheckedContinuation { continuation in
        monitor.pathUpdateHandler = { path in
            continuation.resume(returning: path)
            monitor.cancel()
        }
        monitor.start(queue: .global())
    }

    if path.isExpensive || path.isConstrained {
        // On cellular or Low Data Mode: thumbnails only
        for item in pendingMedia {
            try await downloadThumbnail(item)
        }
    } else {
        // On Wi-Fi with no constraints: full media
        for item in pendingMedia {
            try await downloadMedia(item)
        }
    }
}
```

---

### Module 4: Deferring Non-Urgent Work

#### 4.1 Quality of Service Levels

```swift
// WASTEFUL: All work at high priority
Task {
    await syncAnalytics()     // Not urgent
    await prefetchImages()    // Not urgent
    await updateSearchIndex() // Not urgent
}

// OPTIMIZED: Appropriate QoS levels
// Urgent user-facing work:
Task(priority: .userInitiated) {
    await loadCurrentScreen()
}

// Deferrable background work:
Task.detached(priority: .utility) {
    await syncAnalytics()
}

Task.detached(priority: .background) {
    await prefetchImages()
    await updateSearchIndex()
}
```

#### 4.2 Work Batching

```swift
// WASTEFUL: Individual analytics events sent immediately
func trackEvent(_ event: AnalyticsEvent) {
    Task {
        try await api.sendEvent(event) // Network request per event
    }
}

// OPTIMIZED: Batch events and send periodically
actor AnalyticsService {
    private var eventBuffer: [AnalyticsEvent] = []
    private var flushTask: Task<Void, Never>?

    func track(_ event: AnalyticsEvent) {
        eventBuffer.append(event)

        if eventBuffer.count >= 20 {
            flush() // Flush when buffer is full
        } else if flushTask == nil {
            // Flush after 60 seconds of inactivity
            flushTask = Task {
                try? await Task.sleep(for: .seconds(60))
                flush()
            }
        }
    }

    private func flush() {
        guard !eventBuffer.isEmpty else { return }
        let batch = eventBuffer
        eventBuffer.removeAll()
        flushTask?.cancel()
        flushTask = nil

        Task.detached(priority: .background) {
            try? await api.sendEvents(batch) // Single request for batch
        }
    }
}
```

---

### Module 5: Energy Diagnostics Profiling

#### 5.1 Instruments Energy Log

```
1. Open Instruments (Cmd+I)
2. Select "Energy Log" template
3. Tracks:
   - Energy Impact (overall)
   - CPU Activity
   - Network Activity
   - Location Activity
   - GPU Activity
   - Background Activity
4. Run app through typical user flows
5. Identify energy spikes and correlate with code
```

#### 5.2 MetricKit Energy Metrics

```swift
import MetricKit

class EnergyMetricsSubscriber: NSObject, MXMetricManagerSubscriber {
    func didReceive(_ payloads: [MXMetricPayload]) {
        for payload in payloads {
            // CPU time
            if let cpuMetrics = payload.cpuMetrics {
                log("CPU time: \(cpuMetrics.cumulativeCPUTime)")
            }

            // Cellular condition time
            if let cellularMetrics = payload.cellularConditionMetrics {
                log("Cellular bars time: \(cellularMetrics.histogrammedCellularConditionTime)")
            }

            // Location activity
            if let locationMetrics = payload.locationActivityMetrics {
                log("Background location: \(locationMetrics.cumulativeBackgroundTime)")
            }

            // Network transfers
            if let networkMetrics = payload.networkTransferMetrics {
                log("Upload: \(networkMetrics.cumulativeCellularUpload)")
                log("Download: \(networkMetrics.cumulativeCellularDownload)")
            }
        }
    }
}
```

#### 5.3 Xcode Organizer Energy Reports

```
1. Open Xcode > Window > Organizer
2. Select your app > Energy
3. Review:
   - Average energy impact per session
   - Background energy usage
   - Location usage breakdown
   - Compare between app versions
4. Identify regressions after updates
```

---

## Expected Output

1. **Energy Profile** - Current energy consumption breakdown by subsystem
2. **Location Audit** - Location accuracy and frequency optimization plan
3. **Background Audit** - Background task review with efficiency improvements
4. **Network Audit** - Request frequency, caching, and batching recommendations
5. **Deferred Work Plan** - Non-urgent work identified and scheduled appropriately

---

## Example Interaction

**User reports battery drain from a fitness tracking app:**

```swift
// BEFORE: FitnessTracker.swift
class FitnessTracker {
    let locationManager = CLLocationManager()
    let timer = Timer.scheduledTimer(withTimeInterval: 1, repeats: true) { _ in
        uploadCurrentStats() // Network request every second
    }

    func startWorkout() {
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
        locationManager.distanceFilter = kCLDistanceFilterNone
        locationManager.allowsBackgroundLocationUpdates = true
        locationManager.pausesLocationUpdatesAutomatically = false
        locationManager.startUpdatingLocation()
    }
}
```

**Agent produces:**

```swift
// AFTER: FitnessTracker.swift
class FitnessTracker {
    let locationManager = CLLocationManager()
    private var statsBuffer: [WorkoutStat] = []

    func startWorkout() {
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
        locationManager.distanceFilter = 5 // Update every 5 meters, not every centimeter
        locationManager.allowsBackgroundLocationUpdates = true
        locationManager.pausesLocationUpdatesAutomatically = true // Let iOS save energy
        locationManager.activityType = .fitness // Enables motion-aware power management
        locationManager.startUpdatingLocation()

        // Buffer stats and upload in batches
        scheduleStatUpload()
    }

    private func scheduleStatUpload() {
        Task {
            while !Task.isCancelled {
                try? await Task.sleep(for: .seconds(30)) // Every 30s, not every 1s
                await uploadBufferedStats()
            }
        }
    }

    func stopWorkout() {
        locationManager.stopUpdatingLocation()
        Task { await uploadBufferedStats() } // Final flush
    }
}
```

**Energy savings:**
- `distanceFilter = 5` reduces GPS processing by ~80% during steady-pace activity
- `pausesLocationUpdatesAutomatically = true` lets iOS pause during stops
- `activityType = .fitness` enables motion coprocessor optimization
- Network requests reduced from 60/minute to 2/minute (30x reduction)
- Stats buffered locally and sent in batch

---

## Techniques Used

- **ST-01** (Clear Objective): Focused energy optimization
- **RT-02** (Multi-Format Output): Code examples with profiling instructions
- **AG-02** (Iterative Refinement): Measure, optimize, verify cycle
- **AG-12** (Diagnostic Process): Systematic energy hotspot identification

---

## Related Prompts

- [ios_startup_optimization.md](ios_startup_optimization.md) - Launch efficiency impacts energy budget
- [ios_memory_leak_detection.md](ios_memory_leak_detection.md) - Memory leaks waste energy
- [ios_app_size_optimization.md](ios_app_size_optimization.md) - Smaller binaries load faster

---

## Customization Guide

### For Always-On Location Apps

Special optimization:
- Use significant location change monitoring where possible
- Implement deferred location updates
- Use visit monitoring for place-based features
- Profile background location energy separately

### For Media Streaming Apps

Focus on:
- AVPlayer energy modes and buffer sizing
- Background audio session configuration
- Adaptive bitrate stream selection by battery level
- Download for offline to avoid repeated streaming

### For Messaging Apps

Optimize:
- Push notification delivery instead of polling
- WebSocket keep-alive interval tuning
- Media download deferral and progressive loading
- Typing indicator debouncing
