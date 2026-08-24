---
title: "iOS Widgets, App Intents & Live Activities"
category: mobile-development
description: "Build WidgetKit widgets, App Intents for Siri and Shortcuts, and Live Activities with ActivityKit following modern iOS patterns."
techniques:
  - ST-01
  - ST-02
  - ST-03
difficulty: intermediate
tags:
  - ios
  - swift
  - widgetkit
  - app-intents
  - live-activities
  - mobile-development
updated: "2026-03-20"
---

# iOS Widgets, App Intents & Live Activities

**Objective:** Build production-ready WidgetKit widgets with timeline providers, configurable intents via App Intents, and real-time Live Activities using ActivityKit, including widget deep linking and shared data strategies between the app and extensions.

**When to Use:** Use this prompt when adding home screen widgets, Lock Screen widgets, Siri/Shortcuts integration via App Intents, or real-time status displays via Live Activities. Best used after the app's data layer and shared App Group are configured.

**Prompt Type:** Modular (150-400 lines)

---

## Context Gathering

Before building widgets or intents, gather essential context:

1. **Widget Requirements:**
   - "What data should the widget display (summary, status, quick actions)?"
   - "What widget families are needed (systemSmall, systemMedium, systemLarge, accessoryCircular, accessoryRectangular)?"
   - "Does the widget need user configuration (e.g., select an account, choose a category)?"

2. **Data Sharing:**
   - "Is an App Group already configured for shared data between the app and extensions?"
   - "What data store is used (UserDefaults, Core Data, SwiftData, file-based)?"
   - "How frequently does widget data change?"

3. **Live Activities:**
   - "Do you need real-time updates (order tracking, sports scores, timers)?"
   - "Will updates come via push tokens or local updates?"
   - "What should the Dynamic Island presentation look like?"

4. **App Intents:**
   - "What actions should Siri and Shortcuts expose?"
   - "Do intents need parameters (entities) the user selects?"
   - "Should actions be available from Spotlight or the Action button?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before implementing ANY code, you MUST:**

1. **Verify App Group** - Confirm a shared App Group is configured in both the main app and widget extension targets.
2. **Check widget extension target** - Ensure a WidgetKit Extension target exists or create one.
3. **Confirm data sharing strategy** - Understand how data flows from the app to the widget (shared UserDefaults, shared container, etc.).
4. **Follow project conventions** - Match existing model definitions, naming, and architecture patterns.
5. **Provide specific, working code** - All code samples MUST include target membership annotations and file paths.

### False-Positive Prevention

- Do NOT use URLSession or network calls directly in widget timeline providers; use cached/shared data
- Do NOT exceed the widget memory limit (~30MB); keep assets and data minimal
- Do NOT use interactive controls in widgets targeting below iOS 17; check deployment target
- Do NOT forget to call `WidgetCenter.shared.reloadTimelines(ofKind:)` when app data changes
- Do NOT start Live Activities when the app is in the background without push-to-start tokens
- DO use `@AppStorage` with the App Group suite name for shared preferences
- DO provide placeholder and snapshot timelines for fast widget gallery rendering
- DO support all requested widget families with appropriate layouts
- DO use `IntentTimelineProvider` for configurable widgets
- DO handle Activity expiration and stale state in Live Activities

---

### Phase 1: WidgetKit Timeline Provider

#### 1.1 Basic Widget with Timeline

```swift
// File: OrderWidget/OrderWidget.swift
// Target: OrderWidgetExtension

import WidgetKit
import SwiftUI

struct OrderEntry: TimelineEntry {
    let date: Date
    let order: SharedOrder?
    let configuration: OrderWidgetIntent?
}

struct OrderTimelineProvider: AppIntentTimelineProvider {
    typealias Entry = OrderEntry
    typealias Intent = OrderWidgetIntent

    private let dataStore = SharedDataStore()

    func placeholder(in context: Context) -> OrderEntry {
        OrderEntry(date: .now, order: .placeholder, configuration: nil)
    }

    func snapshot(for configuration: OrderWidgetIntent, in context: Context) async -> OrderEntry {
        let order = await dataStore.fetchLatestOrder()
        return OrderEntry(date: .now, order: order, configuration: configuration)
    }

    func timeline(for configuration: OrderWidgetIntent, in context: Context) async -> Timeline<OrderEntry> {
        let order = await dataStore.fetchLatestOrder()
        let entry = OrderEntry(date: .now, order: order, configuration: configuration)

        // Refresh every 15 minutes or when order status might change
        let nextUpdate = Calendar.current.date(byAdding: .minute, value: 15, to: .now)!
        return Timeline(entries: [entry], policy: .after(nextUpdate))
    }
}
```

#### 1.2 Widget View with Multiple Families

```swift
// File: OrderWidget/OrderWidgetView.swift
// Target: OrderWidgetExtension

import SwiftUI
import WidgetKit

struct OrderWidgetView: View {
    @Environment(\.widgetFamily) var family
    let entry: OrderEntry

    var body: some View {
        switch family {
        case .systemSmall:
            SmallOrderView(order: entry.order)
        case .systemMedium:
            MediumOrderView(order: entry.order)
        case .accessoryCircular:
            CircularOrderView(order: entry.order)
        case .accessoryRectangular:
            RectangularOrderView(order: entry.order)
        default:
            SmallOrderView(order: entry.order)
        }
    }
}

private struct SmallOrderView: View {
    let order: SharedOrder?

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            HStack {
                Image(systemName: "shippingbox.fill")
                    .foregroundStyle(.blue)
                Spacer()
                Text(order?.statusEmoji ?? "📦")
            }

            Spacer()

            if let order {
                Text(order.title)
                    .font(.headline)
                    .lineLimit(2)
                Text(order.statusDescription)
                    .font(.caption)
                    .foregroundStyle(.secondary)
            } else {
                Text("No Active Orders")
                    .font(.headline)
                    .foregroundStyle(.secondary)
            }
        }
        .containerBackground(.fill.tertiary, for: .widget)
        .widgetURL(URL(string: "myapp://orders/\(order?.id ?? "")"))
    }
}

private struct CircularOrderView: View {
    let order: SharedOrder?

    var body: some View {
        ZStack {
            AccessoryWidgetBackground()
            VStack(spacing: 2) {
                Image(systemName: order?.statusIcon ?? "shippingbox")
                    .font(.title3)
                Text(order?.shortStatus ?? "--")
                    .font(.caption2)
                    .widgetAccentable()
            }
        }
        .containerBackground(.fill.tertiary, for: .widget)
    }
}

// MARK: - Widget Configuration

struct OrderWidget: Widget {
    let kind = "OrderWidget"

    var body: some WidgetConfiguration {
        AppIntentConfiguration(
            kind: kind,
            intent: OrderWidgetIntent.self,
            provider: OrderTimelineProvider()
        ) { entry in
            OrderWidgetView(entry: entry)
        }
        .configurationDisplayName("Order Tracker")
        .description("Track your latest order status.")
        .supportedFamilies([
            .systemSmall,
            .systemMedium,
            .accessoryCircular,
            .accessoryRectangular
        ])
    }
}

#Preview("Small", as: .systemSmall) {
    OrderWidget()
} timeline: {
    OrderEntry(date: .now, order: .placeholder, configuration: nil)
    OrderEntry(date: .now, order: nil, configuration: nil)
}
```

---

### Phase 2: App Intents for Siri & Shortcuts

**CHECKPOINT 1:** Confirm widget rendering before building App Intents.

```markdown
## Widget Summary

| Component | Status |
|-----------|--------|
| Timeline provider | AppIntentTimelineProvider with 15-min refresh |
| Widget families | systemSmall, systemMedium, accessoryCircular, accessoryRectangular |
| Deep linking | widgetURL with order ID routing |
| Placeholder | Static preview for gallery |

**Proceed with App Intents?**
```

#### 2.1 App Intent Definition

```swift
// File: Shared/Intents/OrderWidgetIntent.swift
// Target: App + OrderWidgetExtension

import AppIntents

struct OrderWidgetIntent: WidgetConfigurationIntent {
    static var title: LocalizedStringResource = "Select Order"
    static var description: IntentDescription = "Choose which order to display."

    @Parameter(title: "Order")
    var selectedOrder: OrderEntity?
}

// MARK: - Entity for Siri/Shortcuts parameter resolution

struct OrderEntity: AppEntity {
    static var typeDisplayRepresentation = TypeDisplayRepresentation(name: "Order")
    static var defaultQuery = OrderEntityQuery()

    var id: String
    var title: String
    var status: String

    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(
            title: "\(title)",
            subtitle: "\(status)",
            image: .init(systemName: "shippingbox")
        )
    }
}

struct OrderEntityQuery: EntityQuery {
    private let dataStore = SharedDataStore()

    func entities(for identifiers: [String]) async throws -> [OrderEntity] {
        let orders = await dataStore.fetchOrders()
        return orders
            .filter { identifiers.contains($0.id) }
            .map { OrderEntity(id: $0.id, title: $0.title, status: $0.statusDescription) }
    }

    func suggestedEntities() async throws -> [OrderEntity] {
        let orders = await dataStore.fetchOrders()
        return orders.prefix(10).map {
            OrderEntity(id: $0.id, title: $0.title, status: $0.statusDescription)
        }
    }

    func defaultResult() async -> OrderEntity? {
        let order = await dataStore.fetchLatestOrder()
        return order.map { OrderEntity(id: $0.id, title: $0.title, status: $0.statusDescription) }
    }
}
```

#### 2.2 Standalone App Intent (Siri / Shortcuts / Action Button)

```swift
// File: Shared/Intents/ReorderIntent.swift
// Target: App

import AppIntents

struct ReorderIntent: AppIntent {
    static var title: LocalizedStringResource = "Reorder Last Order"
    static var description: IntentDescription = "Place the same order again."
    static var openAppWhenRun = false

    @Parameter(title: "Order")
    var order: OrderEntity

    func perform() async throws -> some IntentResult & ProvidesDialog {
        let service = OrderService()
        let newOrder = try await service.reorder(orderId: order.id)
        return .result(dialog: "Reordered \(newOrder.title). Estimated delivery: \(newOrder.estimatedDelivery).")
    }
}

// Register in AppShortcutsProvider for Spotlight and Siri suggestions
struct MyAppShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: ReorderIntent(),
            phrases: [
                "Reorder with \(.applicationName)",
                "Place my last order again in \(.applicationName)"
            ],
            shortTitle: "Reorder",
            systemImageName: "arrow.clockwise.circle"
        )
    }
}
```

---

### Phase 3: Live Activities with ActivityKit

#### 3.1 Activity Attributes

```swift
// File: Shared/Activities/OrderTrackingActivity.swift
// Target: App + OrderWidgetExtension

import ActivityKit

struct OrderTrackingAttributes: ActivityAttributes {
    // Fixed data that doesn't change during the activity
    let orderNumber: String
    let restaurantName: String

    // Dynamic data that updates in real-time
    struct ContentState: Codable, Hashable {
        enum DeliveryStatus: String, Codable {
            case preparing, enRoute, arriving, delivered
        }

        var status: DeliveryStatus
        var estimatedDelivery: Date
        var driverName: String?
        var currentStep: Int // 1-4
    }
}
```

#### 3.2 Live Activity UI

```swift
// File: OrderWidget/OrderLiveActivity.swift
// Target: OrderWidgetExtension

import SwiftUI
import WidgetKit
import ActivityKit

struct OrderLiveActivity: Widget {
    var body: some WidgetConfiguration {
        ActivityConfiguration(for: OrderTrackingAttributes.self) { context in
            // Lock Screen / Banner presentation
            OrderLockScreenView(
                attributes: context.attributes,
                state: context.state
            )
            .activityBackgroundTint(.blue.opacity(0.1))
        } dynamicIsland: { context in
            DynamicIsland {
                // Expanded regions
                DynamicIslandExpandedRegion(.leading) {
                    Image(systemName: "shippingbox.fill")
                        .foregroundStyle(.blue)
                        .font(.title2)
                }
                DynamicIslandExpandedRegion(.trailing) {
                    Text(context.state.estimatedDelivery, style: .timer)
                        .font(.headline)
                        .monospacedDigit()
                }
                DynamicIslandExpandedRegion(.bottom) {
                    OrderProgressBar(currentStep: context.state.currentStep)
                    if let driver = context.state.driverName {
                        Text("\(driver) is on the way")
                            .font(.caption)
                            .foregroundStyle(.secondary)
                    }
                }
            } compactLeading: {
                Image(systemName: "shippingbox.fill")
                    .foregroundStyle(.blue)
            } compactTrailing: {
                Text(context.state.estimatedDelivery, style: .timer)
                    .monospacedDigit()
                    .frame(width: 56)
            } minimal: {
                Image(systemName: "shippingbox.fill")
                    .foregroundStyle(.blue)
            }
        }
    }
}

private struct OrderProgressBar: View {
    let currentStep: Int
    private let steps = ["Ordered", "Preparing", "En Route", "Delivered"]

    var body: some View {
        HStack(spacing: 4) {
            ForEach(0..<steps.count, id: \.self) { index in
                VStack(spacing: 4) {
                    Circle()
                        .fill(index < currentStep ? Color.blue : Color.gray.opacity(0.3))
                        .frame(width: 8, height: 8)
                    Text(steps[index])
                        .font(.system(size: 9))
                        .foregroundStyle(index < currentStep ? .primary : .secondary)
                }
                if index < steps.count - 1 {
                    Rectangle()
                        .fill(index < currentStep - 1 ? Color.blue : Color.gray.opacity(0.3))
                        .frame(height: 2)
                }
            }
        }
    }
}
```

#### 3.3 Live Activity Management

```swift
// File: Services/Activities/LiveActivityManager.swift
// Target: App

import ActivityKit

@Observable
final class LiveActivityManager {
    private(set) var currentActivity: Activity<OrderTrackingAttributes>?

    func startTracking(orderNumber: String, restaurantName: String) throws {
        guard ActivityAuthorizationInfo().areActivitiesEnabled else { return }

        let attributes = OrderTrackingAttributes(
            orderNumber: orderNumber,
            restaurantName: restaurantName
        )
        let initialState = OrderTrackingAttributes.ContentState(
            status: .preparing,
            estimatedDelivery: Date().addingTimeInterval(30 * 60),
            driverName: nil,
            currentStep: 1
        )

        let content = ActivityContent(state: initialState, staleDate: nil)
        currentActivity = try Activity.request(
            attributes: attributes,
            content: content,
            pushType: .token // Enable push token updates from server
        )

        // Send push token to backend for server-driven updates
        Task {
            for await pushToken in currentActivity!.pushTokenUpdates {
                let tokenString = pushToken.map { String(format: "%02x", $0) }.joined()
                try? await APIClient.shared.registerActivityPushToken(
                    orderNumber: orderNumber,
                    token: tokenString
                )
            }
        }
    }

    func updateStatus(_ state: OrderTrackingAttributes.ContentState) async {
        let content = ActivityContent(state: state, staleDate: nil)
        await currentActivity?.update(content)
    }

    func endTracking(finalState: OrderTrackingAttributes.ContentState) async {
        let content = ActivityContent(state: finalState, staleDate: nil)
        await currentActivity?.end(content, dismissalPolicy: .after(.now + 3600))
    }
}
```

---

### Phase 4: Shared Data Layer

**CHECKPOINT 2:** Review widgets, intents, and activities before finalizing shared data.

```markdown
## Implementation Summary

| Component | Status |
|-----------|--------|
| Widget families | Small, Medium, Circular, Rectangular |
| Widget configuration | AppIntentConfiguration with entity selection |
| App Intents | Reorder action with Siri phrases |
| Live Activity | Lock Screen + Dynamic Island |
| Activity updates | Push token + local update support |

**Ready to finalize shared data and widget reload triggers?**
```

#### 4.1 Shared Data Store

```swift
// File: Shared/Data/SharedDataStore.swift
// Target: App + OrderWidgetExtension

import Foundation

actor SharedDataStore {
    private let defaults: UserDefaults
    private let decoder = JSONDecoder()
    private let encoder = JSONEncoder()

    init(suiteName: String = "group.com.yourapp.shared") {
        self.defaults = UserDefaults(suiteName: suiteName) ?? .standard
    }

    func fetchLatestOrder() -> SharedOrder? {
        guard let data = defaults.data(forKey: "latestOrder") else { return nil }
        return try? decoder.decode(SharedOrder.self, from: data)
    }

    func fetchOrders() -> [SharedOrder] {
        guard let data = defaults.data(forKey: "recentOrders") else { return [] }
        return (try? decoder.decode([SharedOrder].self, from: data)) ?? []
    }

    func saveLatestOrder(_ order: SharedOrder) throws {
        let data = try encoder.encode(order)
        defaults.set(data, forKey: "latestOrder")
    }
}
```

#### 4.2 Widget Reload Triggers

```swift
// File: Services/WidgetReloadService.swift
// Target: App

import WidgetKit

struct WidgetReloadService {
    static func reloadOrderWidget() {
        WidgetCenter.shared.reloadTimelines(ofKind: "OrderWidget")
    }

    static func reloadAllWidgets() {
        WidgetCenter.shared.reloadAllTimelines()
    }

    /// Call after any order data change in the main app
    static func onOrderUpdated(_ order: SharedOrder) async throws {
        let store = SharedDataStore()
        try await store.saveLatestOrder(order)
        reloadOrderWidget()
    }
}
```

---

## Expected Output

### File Structure

```
Shared/
├── Intents/
│   ├── OrderWidgetIntent.swift          # Widget configuration intent
│   └── ReorderIntent.swift              # Siri / Shortcuts action
├── Activities/
│   └── OrderTrackingActivity.swift      # ActivityAttributes definition
└── Data/
    └── SharedDataStore.swift            # App Group shared data

OrderWidget/  (Widget Extension Target)
├── OrderWidget.swift                    # Timeline provider
├── OrderWidgetView.swift                # Widget views per family
└── OrderLiveActivity.swift              # Live Activity UI

Services/
├── Activities/
│   └── LiveActivityManager.swift        # Activity lifecycle management
└── WidgetReloadService.swift            # Widget refresh triggers
```

### Implementation Checklist

- [ ] WidgetKit Extension target created
- [ ] App Group configured on both targets
- [ ] Timeline provider with proper refresh policy
- [ ] Widget views for all supported families
- [ ] Placeholder and snapshot implementations
- [ ] Widget deep linking via `widgetURL`
- [ ] App Intent for widget configuration
- [ ] App Entity with query for parameter selection
- [ ] Siri/Shortcuts integration with phrases
- [ ] Live Activity attributes with content state
- [ ] Dynamic Island compact and expanded views
- [ ] Push token forwarding for server-driven updates
- [ ] Shared data store via App Group UserDefaults
- [ ] Widget reload on app data changes

---

## Techniques Used

- **ST-01** (Clear Objective): Focused objective covering widgets, intents, and Live Activities
- **ST-02** (Sequential Instructions): Phased approach from widget through Live Activities to shared data
- **ST-03** (Output Format Templates): Code templates for each component

---

## Related Prompts

- [ios_push_notifications.md](../implementation/ios_push_notifications.md) - Push notifications for Live Activity token updates
- [ios_swiftui_screen_builder.md](../implementation/ios_swiftui_screen_builder.md) - SwiftUI patterns used in widget views
- [ios_data_layer_implementation.md](../implementation/ios_data_layer_implementation.md) - Data layer for shared data store
- [ios_app_clips.md](../implementation/ios_app_clips.md) - Another app extension pattern
