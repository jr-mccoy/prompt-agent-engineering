---
title: "iOS Snapshot Testing"
category: mobile-development
description: "Implement visual regression testing with swift-snapshot-testing for SwiftUI views and UIKit view controllers across device sizes, Dynamic Type, and dark/light mode"
techniques:
  - ST-01
  - RT-02
  - DS-02
  - RT-04
difficulty: intermediate
tags:
  - ios
  - swift
  - testing
  - snapshot-testing
  - visual-regression
  - swiftui
  - accessibility
updated: "2026-03-19"
---

# iOS Snapshot Testing

**Objective:** Implement visual regression testing using swift-snapshot-testing (by Point-Free) to catch unintended UI changes in SwiftUI views, UIKit view controllers, and reusable components. Tests verify rendering across multiple device sizes, Dynamic Type accessibility sizes, dark/light mode, and locale-specific layouts to ensure pixel-perfect consistency.

**When to Use:** Use this prompt when building a design system or component library, when UI regressions have reached production, when supporting multiple device sizes or accessibility configurations, or when reviewing UI changes in pull requests. Snapshot tests complement (but do not replace) UI tests -- they verify appearance, not behavior.

**Prompt Type:** Modular (200-240 lines)

---

## Context Gathering

1. **UI Framework:**
   - "Is the app SwiftUI, UIKit, or hybrid?"
   - "Are there reusable components or a design system?"

2. **Device Matrix:**
   - "Which devices must be supported (iPhone SE, iPhone 15, iPhone 15 Pro Max, iPad)?"
   - "What's the minimum iOS version?"

3. **Accessibility Requirements:**
   - "Does the app need to support Dynamic Type?"
   - "Are there high-contrast or reduced motion requirements?"

4. **CI/CD:**
   - "Are snapshot reference images committed to git?"
   - "What simulator is used in CI (must match for pixel-exact comparisons)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before generating ANY snapshot test, you MUST:**

1. **Pin the simulator** - Snapshot tests are pixel-exact. Different simulators, OS versions, or hardware produce different results. Document which simulator generates reference images.
2. **Inject all dependencies** - Views must render with deterministic data. No network calls, no current date/time, no random values.
3. **Control the environment** - Color scheme, locale, Dynamic Type size, layout direction, and calendar must be explicitly set, not inherited from the test runner.
4. **Plan for reference image management** - Reference images must be committed to git and reviewed in PRs. Establish a clear process for updating them.
5. **Size the test surface correctly** - Test components in isolation, not embedded in full navigation stacks (unless testing navigation chrome specifically).

**Snapshot tests that break on every CI run due to environment differences are worse than no tests.** Determinism is non-negotiable.

### False-Positive Prevention

- ❌ Do NOT run snapshot tests on different simulator versions than reference images
- ❌ Do NOT include animated content (spinners, shimmer) in snapshots
- ❌ Do NOT snapshot views that depend on real-time data (clocks, live content)
- ❌ Do NOT test every state permutation -- focus on visually distinct states
- ❌ Do NOT compare snapshots across macOS versions (font rendering differs)
- ✅ DO use a fixed date/locale/calendar in all snapshot environments
- ✅ DO test light and dark mode as separate assertions
- ✅ DO include at least one Dynamic Type size (preferably `accessibilityExtraExtraExtraLarge`)
- ✅ DO verify both smallest (iPhone SE) and largest (Pro Max or iPad) devices
- ✅ DO document the exact simulator used for reference generation

---

### Module 1: Project Setup

```swift
// Package.swift or SPM dependency
// .package(url: "https://github.com/pointfreeco/swift-snapshot-testing", from: "1.15.0")

// Test target configuration:
// - Create a dedicated test target: AppSnapshotTests
// - Set the reference directory in test plan or scheme
// - Pin simulator: iPhone 15, iOS 17.x
```

**Directory Structure:**

```
AppSnapshotTests/
├── Screens/
│   ├── LoginViewSnapshotTests.swift
│   ├── HomeViewSnapshotTests.swift
│   └── ProfileViewSnapshotTests.swift
├── Components/
│   ├── ButtonSnapshotTests.swift
│   ├── CardSnapshotTests.swift
│   └── EmptyStateSnapshotTests.swift
├── Helpers/
│   ├── SnapshotTestCase.swift          # Base class with shared config
│   └── View+SnapshotHelpers.swift      # Environment injection
└── __Snapshots__/                       # Reference images (git-tracked)
    ├── LoginViewSnapshotTests/
    │   ├── test_loginView_lightMode.1.png
    │   ├── test_loginView_darkMode.1.png
    │   └── test_loginView_dynamicTypeXXXL.1.png
    └── ...
```

### Module 2: Snapshot Test Helpers

```swift
import SnapshotTesting
import SwiftUI
import XCTest

// MARK: - Base Test Case

class SnapshotTestCase: XCTestCase {

    /// Set to true to regenerate all reference images
    /// IMPORTANT: Never commit with this set to true
    var isRecording: Bool {
        // Override per-test or use environment variable
        ProcessInfo.processInfo.environment["SNAPSHOT_RECORD"] == "true"
    }

    override func setUp() {
        super.setUp()
        // Disable animations for deterministic rendering
        UIView.setAnimationsEnabled(false)
        // Set recording mode from environment
        // isRecording = true  // Uncomment to record new references
    }

    override func tearDown() {
        UIView.setAnimationsEnabled(true)
        super.tearDown()
    }
}

// MARK: - SwiftUI Snapshot Helpers

extension View {

    /// Wrap in a hosting controller with a fixed environment
    func snapshotContainer(
        colorScheme: ColorScheme = .light,
        dynamicTypeSize: DynamicTypeSize = .medium,
        locale: Locale = Locale(identifier: "en_US")
    ) -> UIHostingController<some View> {
        let view = self
            .environment(\.colorScheme, colorScheme)
            .environment(\.dynamicTypeSize, dynamicTypeSize)
            .environment(\.locale, locale)

        let controller = UIHostingController(rootView: view)
        controller.overrideUserInterfaceStyle = colorScheme == .dark ? .dark : .light
        return controller
    }
}

// MARK: - Device Configurations

enum SnapshotDevice {
    static let iPhoneSE = ViewImageConfig.iPhoneSe
    static let iPhone15 = ViewImageConfig.iPhone13  // Same logical size
    static let iPhone15ProMax = ViewImageConfig.iPhone13ProMax
    static let iPadPro11 = ViewImageConfig.iPadPro11
}

// MARK: - Multi-Configuration Test Runner

extension SnapshotTestCase {

    /// Test a SwiftUI view across multiple configurations
    func assertSnapshots<V: View>(
        of view: V,
        named name: String,
        devices: [String: ViewImageConfig] = ["iPhone15": SnapshotDevice.iPhone15],
        colorSchemes: [ColorScheme] = [.light, .dark],
        dynamicTypeSizes: [DynamicTypeSize] = [.medium],
        file: StaticString = #file,
        testName: String = #function,
        line: UInt = #line
    ) {
        for (deviceName, device) in devices {
            for scheme in colorSchemes {
                for typeSize in dynamicTypeSizes {
                    let schemeName = scheme == .dark ? "dark" : "light"
                    let sizeName = "\(typeSize)"
                    let testID = "\(deviceName)_\(schemeName)_\(sizeName)"

                    let controller = view.snapshotContainer(
                        colorScheme: scheme,
                        dynamicTypeSize: typeSize
                    )

                    assertSnapshot(
                        of: controller,
                        as: .image(on: device),
                        named: "\(name)_\(testID)",
                        record: isRecording,
                        file: file,
                        testName: testName,
                        line: line
                    )
                }
            }
        }
    }
}
```

### Module 3: SwiftUI View Snapshots

```swift
import SnapshotTesting
import SwiftUI
@testable import MyApp

final class LoginViewSnapshotTests: SnapshotTestCase {

    // MARK: - Default State

    func test_loginView_lightMode() {
        let view = LoginView(viewModel: .preview(state: .idle))

        assertSnapshot(
            of: view.snapshotContainer(colorScheme: .light),
            as: .image(on: SnapshotDevice.iPhone15),
            record: isRecording
        )
    }

    func test_loginView_darkMode() {
        let view = LoginView(viewModel: .preview(state: .idle))

        assertSnapshot(
            of: view.snapshotContainer(colorScheme: .dark),
            as: .image(on: SnapshotDevice.iPhone15),
            record: isRecording
        )
    }

    // MARK: - Error State

    func test_loginView_withError() {
        let view = LoginView(
            viewModel: .preview(state: .error("Invalid email or password"))
        )

        assertSnapshot(
            of: view.snapshotContainer(),
            as: .image(on: SnapshotDevice.iPhone15),
            record: isRecording
        )
    }

    // MARK: - Loading State

    func test_loginView_loading() {
        let view = LoginView(viewModel: .preview(state: .loading))

        assertSnapshot(
            of: view.snapshotContainer(),
            as: .image(on: SnapshotDevice.iPhone15),
            record: isRecording
        )
    }

    // MARK: - Dynamic Type

    func test_loginView_dynamicTypeAccessibilityXXXL() {
        let view = LoginView(viewModel: .preview(state: .idle))

        assertSnapshot(
            of: view.snapshotContainer(
                dynamicTypeSize: .accessibilityExtraExtraExtraLarge
            ),
            as: .image(on: SnapshotDevice.iPhone15),
            record: isRecording
        )
    }

    // MARK: - Device Sizes

    func test_loginView_iPhoneSE() {
        let view = LoginView(viewModel: .preview(state: .idle))

        assertSnapshot(
            of: view.snapshotContainer(),
            as: .image(on: SnapshotDevice.iPhoneSE),
            record: isRecording
        )
    }

    func test_loginView_iPhone15ProMax() {
        let view = LoginView(viewModel: .preview(state: .idle))

        assertSnapshot(
            of: view.snapshotContainer(),
            as: .image(on: SnapshotDevice.iPhone15ProMax),
            record: isRecording
        )
    }

    // MARK: - Multi-Configuration (bulk test)

    func test_loginView_allConfigurations() {
        let view = LoginView(viewModel: .preview(state: .idle))

        assertSnapshots(
            of: view,
            named: "login_idle",
            devices: [
                "iPhoneSE": SnapshotDevice.iPhoneSE,
                "iPhone15": SnapshotDevice.iPhone15,
            ],
            colorSchemes: [.light, .dark],
            dynamicTypeSizes: [.medium, .accessibilityExtraExtraExtraLarge]
        )
    }
}
```

### Module 4: UIKit View Controller Snapshots

```swift
import SnapshotTesting
@testable import MyApp

final class SettingsViewControllerSnapshotTests: SnapshotTestCase {

    func test_settingsVC_lightMode() {
        let vc = SettingsViewController()
        vc.configure(with: SettingsViewModel.preview())

        vc.overrideUserInterfaceStyle = .light

        assertSnapshot(
            of: vc,
            as: .image(on: SnapshotDevice.iPhone15),
            record: isRecording
        )
    }

    func test_settingsVC_darkMode() {
        let vc = SettingsViewController()
        vc.configure(with: SettingsViewModel.preview())

        vc.overrideUserInterfaceStyle = .dark

        assertSnapshot(
            of: vc,
            as: .image(on: SnapshotDevice.iPhone15),
            record: isRecording
        )
    }

    func test_settingsVC_withNotificationBadge() {
        let vc = SettingsViewController()
        let vm = SettingsViewModel.preview(unreadNotifications: 5)
        vc.configure(with: vm)

        assertSnapshot(
            of: vc,
            as: .image(on: SnapshotDevice.iPhone15),
            record: isRecording
        )
    }
}
```

### Module 5: Component Library Snapshots

```swift
import SnapshotTesting
import SwiftUI
@testable import MyApp

final class DesignSystemSnapshotTests: SnapshotTestCase {

    // MARK: - Buttons

    func test_primaryButton_allStates() {
        let states: [(String, Bool, Bool)] = [
            ("enabled", true, false),
            ("disabled", false, false),
            ("loading", true, true),
        ]

        for (name, isEnabled, isLoading) in states {
            let view = PrimaryButton(
                title: "Continue",
                isEnabled: isEnabled,
                isLoading: isLoading,
                action: {}
            )
            .frame(width: 320)
            .padding()

            assertSnapshot(
                of: view.snapshotContainer(),
                as: .image,
                named: "primaryButton_\(name)",
                record: isRecording
            )
        }
    }

    // MARK: - Cards

    func test_contentCard_withImage() {
        let view = ContentCard(
            title: "Sample Article",
            subtitle: "This is a preview description for the card component",
            imageURL: nil,  // Use placeholder
            isBookmarked: false
        )
        .frame(width: 350)
        .padding()

        assertSnapshots(
            of: view,
            named: "contentCard",
            colorSchemes: [.light, .dark]
        )
    }

    // MARK: - Empty States

    func test_emptyState_noResults() {
        let view = EmptyStateView(
            icon: "magnifyingglass",
            title: "No Results",
            message: "Try adjusting your search filters",
            actionTitle: "Clear Filters",
            action: {}
        )

        assertSnapshot(
            of: view.snapshotContainer(),
            as: .image(on: SnapshotDevice.iPhone15),
            record: isRecording
        )
    }
}
```

---

## Expected Output

1. **Test Infrastructure** - Base test case, helpers, device configurations
2. **SwiftUI Snapshots** - Views across color schemes, devices, and Dynamic Type
3. **UIKit Snapshots** - View controllers with interface style overrides
4. **Component Snapshots** - Design system elements in all visual states
5. **Reference Image Directory** - Organized `__Snapshots__/` structure
6. **CI Configuration** - Pinned simulator and recording mode control

---

## Example Interaction

**User:** "We have a SwiftUI app with a custom design system. We need snapshot tests for our onboarding flow (3 screens) across iPhone SE, iPhone 15, and Dynamic Type large."

**Agent Response:**

```swift
import SnapshotTesting
import SwiftUI
@testable import MyApp

final class OnboardingSnapshotTests: SnapshotTestCase {

    private let screens: [(name: String, view: AnyView)] = [
        ("welcome", AnyView(OnboardingWelcomeView())),
        ("features", AnyView(OnboardingFeaturesView(features: .preview))),
        ("permissions", AnyView(OnboardingPermissionsView())),
    ]

    func test_onboarding_allScreens_iPhone15_light() {
        for screen in screens {
            assertSnapshot(
                of: screen.view.snapshotContainer(colorScheme: .light),
                as: .image(on: SnapshotDevice.iPhone15),
                named: "\(screen.name)_iPhone15_light",
                record: isRecording
            )
        }
    }

    func test_onboarding_allScreens_iPhoneSE_light() {
        for screen in screens {
            assertSnapshot(
                of: screen.view.snapshotContainer(colorScheme: .light),
                as: .image(on: SnapshotDevice.iPhoneSE),
                named: "\(screen.name)_iPhoneSE_light",
                record: isRecording
            )
        }
    }

    func test_onboarding_allScreens_dynamicTypeLarge() {
        for screen in screens {
            assertSnapshot(
                of: screen.view.snapshotContainer(
                    dynamicTypeSize: .xxxLarge
                ),
                as: .image(on: SnapshotDevice.iPhone15),
                named: "\(screen.name)_dynamicType_xxxLarge",
                record: isRecording
            )
        }
    }

    func test_onboarding_allScreens_darkMode() {
        for screen in screens {
            assertSnapshot(
                of: screen.view.snapshotContainer(colorScheme: .dark),
                as: .image(on: SnapshotDevice.iPhone15),
                named: "\(screen.name)_iPhone15_dark",
                record: isRecording
            )
        }
    }
}
```

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on visual regression prevention across configurations
- **RT-02** (Step-by-Step Reasoning): Modular progression from setup to helpers to tests
- **DS-02** (Domain Expertise): swift-snapshot-testing API, SwiftUI environment injection, UIKit trait overrides
- **RT-04** (Comparative Analysis): Multi-device and multi-configuration comparison matrix

---

## Related Prompts

- [ios_test_strategy_design.md](ios_test_strategy_design.md) - Where snapshot tests fit in the overall pyramid
- [ios_ui_test_generation.md](ios_ui_test_generation.md) - Behavioral UI tests that complement visual snapshots
- [ios_unit_test_generation.md](ios_unit_test_generation.md) - Unit tests for ViewModel logic driving view states

---

## Customization Guide

| Aspect | How to Customize |
|--------|-----------------|
| **Snapshot Library** | Replace swift-snapshot-testing with iOSSnapshotTestCase (Uber) for UIKit-heavy projects |
| **Device Matrix** | Add iPad configurations for universal apps, or remove SE for iPhone-only apps |
| **Tolerance** | Use `precision: 0.99` for views with sub-pixel rendering differences across CI runners |
| **Localization** | Add locale parameter snapshots for RTL (Arabic, Hebrew) and long-text languages (German) |
| **Preview Data** | Create `ViewModel.preview(state:)` factory methods for each visually distinct state |
| **CI Integration** | Upload diff images as CI artifacts when tests fail for easy visual comparison in PRs |
