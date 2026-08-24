---
title: "iOS Project Scaffold"
category: mobile-development
description: "Generate complete Xcode project structure with folder organization, SPM configuration, build settings, CI/CD templates, and essential boilerplate for production iOS apps."
techniques:
  - ST-01
  - ST-02
  - ST-03
difficulty: intermediate
tags:
  - ios
  - swift
  - xcode
  - project-setup
updated: "2026-03-20"
---

# iOS Project Scaffold

**Objective:** Generate a complete, production-ready Xcode project structure with proper folder organization, SPM package configuration, build settings for multiple environments, essential boilerplate code, and CI/CD pipeline templates, ready for immediate feature development.

**When to Use:** Use when starting a new iOS project after architecture and tech stack decisions are made. Also useful when resetting a project structure that has drifted from best practices. Best applied before any feature code is written.

**Prompt Type:** Comprehensive (450+ lines)

---

## Context Gathering

Before generating the scaffold, gather essential context:

1. **Project Identity:**
   - "What is the app name and bundle identifier (e.g., com.company.appname)?"
   - "What is the organization name?"
   - "What minimum iOS version?"

2. **Architecture Decisions:**
   - "What architecture pattern (MVVM, TCA, Clean)?"
   - "Single target or multi-module (SPM)?"
   - "SwiftUI-first or UIKit-first?"

3. **Environment Configuration:**
   - "How many environments (Debug, Staging, Production)?"
   - "Different API base URLs per environment?"
   - "Different bundle IDs per environment (for parallel installs)?"

4. **Infrastructure:**
   - "What CI/CD platform (GitHub Actions, Bitrise, Xcode Cloud)?"
   - "What code signing approach (manual, automatic, Fastlane match)?"
   - "Any required third-party SDKs from day one?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before generating ANY scaffold, you MUST:**

1. **Confirm architecture choice** - Scaffold structure must match the selected architecture pattern.
2. **Validate bundle identifier format** - Must follow reverse domain notation.
3. **Include all environments** - Debug, Staging, and Release at minimum.
4. **Set up proper .gitignore** - Exclude Xcode user data, derived data, and credentials.
5. **Provide working build configurations** - The project must compile on first open.

### False-Positive Prevention

- ❌ Do NOT generate a scaffold that requires manual Xcode configuration to compile
- ❌ Do NOT hardcode API keys or secrets in source files
- ❌ Do NOT skip the test target setup
- ❌ Do NOT use a flat folder structure (group by feature, not by file type)
- ❌ Do NOT include placeholder files that serve no purpose
- ✅ DO generate a project that compiles and runs immediately
- ✅ DO include a working App entry point with basic navigation
- ✅ DO set up build configurations for all environments
- ✅ DO include .gitignore, .swiftlint.yml, and essential config files

---

### Phase 1: Project Structure

#### 1.1 Directory Layout

```
MyApp/
├── MyApp.xcodeproj/
├── MyApp/
│   ├── App/
│   │   ├── MyApp.swift                    # @main entry point
│   │   ├── AppDelegate.swift              # (if UIKit lifecycle needed)
│   │   └── ContentView.swift              # Root view
│   │
│   ├── Features/
│   │   ├── Home/
│   │   │   ├── HomeScreen.swift
│   │   │   ├── HomeViewModel.swift
│   │   │   └── Views/
│   │   │       └── HomeCard.swift
│   │   ├── Settings/
│   │   │   ├── SettingsScreen.swift
│   │   │   └── SettingsViewModel.swift
│   │   └── Onboarding/
│   │       └── OnboardingScreen.swift
│   │
│   ├── Core/
│   │   ├── Networking/
│   │   │   ├── APIClient.swift
│   │   │   ├── APIError.swift
│   │   │   ├── Endpoint.swift
│   │   │   └── Endpoints/
│   │   │       └── .gitkeep
│   │   ├── Persistence/
│   │   │   └── PersistenceController.swift
│   │   ├── Models/
│   │   │   └── .gitkeep
│   │   └── Extensions/
│   │       ├── Date+Formatting.swift
│   │       └── View+Modifiers.swift
│   │
│   ├── Shared/
│   │   ├── Components/
│   │   │   ├── LoadingView.swift
│   │   │   ├── ErrorStateView.swift
│   │   │   └── EmptyStateView.swift
│   │   ├── Design/
│   │   │   ├── AppTheme.swift
│   │   │   ├── AppColors.swift
│   │   │   └── AppFonts.swift
│   │   └── Navigation/
│   │       ├── AppRouter.swift
│   │       └── Route.swift
│   │
│   ├── Configuration/
│   │   ├── Debug.xcconfig
│   │   ├── Staging.xcconfig
│   │   ├── Release.xcconfig
│   │   └── Secrets.xcconfig.template
│   │
│   ├── Resources/
│   │   ├── Assets.xcassets/
│   │   │   ├── AppIcon.appiconset/
│   │   │   ├── AccentColor.colorset/
│   │   │   └── Colors/
│   │   ├── Localizable.xcstrings
│   │   └── Info.plist
│   │
│   └── Preview Content/
│       └── Preview Assets.xcassets/
│
├── MyAppTests/
│   ├── Features/
│   │   └── Home/
│   │       └── HomeViewModelTests.swift
│   ├── Core/
│   │   └── Networking/
│   │       └── APIClientTests.swift
│   ├── Helpers/
│   │   ├── XCTestCase+Async.swift
│   │   └── MockURLProtocol.swift
│   └── Fixtures/
│       └── .gitkeep
│
├── MyAppUITests/
│   ├── Screens/
│   │   └── HomeScreenUITests.swift
│   ├── Helpers/
│   │   └── XCUIApplication+Launch.swift
│   └── Screenshots/
│       └── .gitkeep
│
├── Packages/                               # Local SPM packages (if modular)
│   └── .gitkeep
│
├── Scripts/
│   ├── swiftlint.sh
│   ├── generate-secrets.sh
│   └── run-tests.sh
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── release.yml
│
├── .gitignore
├── .swiftlint.yml
├── .swiftformat
└── README.md
```

---

### Phase 2: Essential Boilerplate

**CHECKPOINT 1:** Confirm directory structure matches architecture choice.

```markdown
## Scaffold Summary
- Architecture: [MVVM/TCA/Clean]
- Module strategy: [Single target / Multi-module]
- Environments: [Debug, Staging, Release]
- UI Framework: [SwiftUI / UIKit / Hybrid]

**Proceed with boilerplate generation?**
```

#### 2.1 App Entry Point

```swift
// File: MyApp/App/MyApp.swift

import SwiftUI

@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

```swift
// File: MyApp/App/ContentView.swift

import SwiftUI

struct ContentView: View {
    @State private var selectedTab: AppTab = .home

    var body: some View {
        TabView(selection: $selectedTab) {
            NavigationStack {
                HomeScreen()
            }
            .tabItem {
                Label("Home", systemImage: "house")
            }
            .tag(AppTab.home)

            NavigationStack {
                SettingsScreen()
            }
            .tabItem {
                Label("Settings", systemImage: "gearshape")
            }
            .tag(AppTab.settings)
        }
    }
}

enum AppTab: Hashable {
    case home
    case settings
}

#Preview {
    ContentView()
}
```

#### 2.2 Networking Boilerplate

```swift
// File: MyApp/Core/Networking/APIClient.swift

import Foundation

actor APIClient {
    static let shared = APIClient()

    private let session: URLSession
    private let decoder: JSONDecoder

    init(session: URLSession = .shared) {
        self.session = session
        self.decoder = JSONDecoder()
        self.decoder.dateDecodingStrategy = .iso8601
        self.decoder.keyDecodingStrategy = .convertFromSnakeCase
    }

    func fetch<T: Decodable & Sendable>(_ endpoint: Endpoint) async throws -> T {
        let (data, response) = try await session.data(for: endpoint.urlRequest)

        guard let httpResponse = response as? HTTPURLResponse else {
            throw APIError.invalidResponse
        }

        guard 200...299 ~= httpResponse.statusCode else {
            throw APIError.httpError(statusCode: httpResponse.statusCode, data: data)
        }

        return try decoder.decode(T.self, from: data)
    }
}
```

```swift
// File: MyApp/Core/Networking/Endpoint.swift

import Foundation

struct Endpoint {
    let path: String
    let method: HTTPMethod
    let queryItems: [URLQueryItem]?
    let body: Data?
    let headers: [String: String]

    enum HTTPMethod: String {
        case get = "GET"
        case post = "POST"
        case put = "PUT"
        case delete = "DELETE"
        case patch = "PATCH"
    }

    var urlRequest: URLRequest {
        get throws {
            var components = URLComponents()
            components.scheme = "https"
            components.host = AppConfiguration.current.apiBaseURL
            components.path = path
            components.queryItems = queryItems

            guard let url = components.url else {
                throw APIError.invalidURL
            }

            var request = URLRequest(url: url)
            request.httpMethod = method.rawValue
            request.httpBody = body
            request.setValue("application/json", forHTTPHeaderField: "Content-Type")

            for (key, value) in headers {
                request.setValue(value, forHTTPHeaderField: key)
            }

            return request
        }
    }

    init(
        path: String,
        method: HTTPMethod = .get,
        queryItems: [URLQueryItem]? = nil,
        body: Data? = nil,
        headers: [String: String] = [:]
    ) {
        self.path = path
        self.method = method
        self.queryItems = queryItems
        self.body = body
        self.headers = headers
    }
}
```

```swift
// File: MyApp/Core/Networking/APIError.swift

import Foundation

enum APIError: LocalizedError {
    case invalidURL
    case invalidResponse
    case httpError(statusCode: Int, data: Data)
    case decodingError(Error)

    var errorDescription: String? {
        switch self {
        case .invalidURL: "Invalid URL"
        case .invalidResponse: "Invalid server response"
        case .httpError(let code, _): "Server error (HTTP \(code))"
        case .decodingError: "Failed to process server response"
        }
    }
}
```

#### 2.3 Environment Configuration

```swift
// File: MyApp/Configuration/AppConfiguration.swift

import Foundation

enum AppEnvironment: String {
    case debug
    case staging
    case release
}

struct AppConfiguration {
    let environment: AppEnvironment
    let apiBaseURL: String
    let analyticsEnabled: Bool

    static var current: AppConfiguration {
        #if DEBUG
        return .debug
        #elseif STAGING
        return .staging
        #else
        return .release
        #endif
    }

    static let debug = AppConfiguration(
        environment: .debug,
        apiBaseURL: "api-dev.example.com",
        analyticsEnabled: false
    )

    static let staging = AppConfiguration(
        environment: .staging,
        apiBaseURL: "api-staging.example.com",
        analyticsEnabled: true
    )

    static let release = AppConfiguration(
        environment: .release,
        apiBaseURL: "api.example.com",
        analyticsEnabled: true
    )
}
```

```
// File: MyApp/Configuration/Debug.xcconfig
SWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG
API_BASE_URL = api-dev.example.com
PRODUCT_BUNDLE_IDENTIFIER = com.company.myapp.debug
PRODUCT_NAME = MyApp (Dev)

// File: MyApp/Configuration/Staging.xcconfig
SWIFT_ACTIVE_COMPILATION_CONDITIONS = STAGING
API_BASE_URL = api-staging.example.com
PRODUCT_BUNDLE_IDENTIFIER = com.company.myapp.staging
PRODUCT_NAME = MyApp (Staging)

// File: MyApp/Configuration/Release.xcconfig
SWIFT_ACTIVE_COMPILATION_CONDITIONS =
API_BASE_URL = api.example.com
PRODUCT_BUNDLE_IDENTIFIER = com.company.myapp
PRODUCT_NAME = MyApp
```

---

### Phase 3: Developer Tooling

#### 3.1 SwiftLint Configuration

```yaml
# File: .swiftlint.yml
disabled_rules:
  - trailing_comma
  - opening_brace

opt_in_rules:
  - empty_count
  - closure_spacing
  - contains_over_filter_count
  - discouraged_optional_boolean
  - empty_string
  - fatal_error_message
  - first_where
  - force_unwrapping
  - implicitly_unwrapped_optional
  - overridden_super_call
  - private_action
  - private_outlet
  - unowned_variable_capture

excluded:
  - Packages
  - DerivedData
  - .build

line_length:
  warning: 120
  error: 200

type_body_length:
  warning: 300
  error: 500

file_length:
  warning: 400
  error: 600
```

#### 3.2 .gitignore

```gitignore
# File: .gitignore

# Xcode
*.xcuserdata/
*.xcworkspace/xcuserdata/
DerivedData/
build/
*.moved-aside
*.pbxuser
*.mode1v3
*.mode2v3
*.perspectivev3
!default.pbxuser
!default.mode1v3
!default.mode2v3
!default.perspectivev3
xcuserdata/

# SPM
.build/
Packages/
.swiftpm/

# CocoaPods (if applicable)
Pods/

# Secrets
*.xcconfig.local
Secrets.xcconfig

# IDE
.idea/
*.swp
.DS_Store

# Fastlane
fastlane/report.xml
fastlane/Preview.html
fastlane/screenshots/**/*.png
fastlane/test_output
```

#### 3.3 CI/CD Template (GitHub Actions)

```yaml
# File: .github/workflows/ci.yml
name: CI

on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  build-and-test:
    runs-on: macos-14
    steps:
      - uses: actions/checkout@v4

      - name: Select Xcode
        run: sudo xcode-select -s /Applications/Xcode_15.4.app

      - name: Build
        run: |
          xcodebuild build-for-testing \
            -scheme MyApp \
            -destination 'platform=iOS Simulator,name=iPhone 15' \
            -configuration Debug \
            | xcbeautify

      - name: Test
        run: |
          xcodebuild test-without-building \
            -scheme MyApp \
            -destination 'platform=iOS Simulator,name=iPhone 15' \
            -configuration Debug \
            | xcbeautify

  swiftlint:
    runs-on: macos-14
    steps:
      - uses: actions/checkout@v4
      - name: SwiftLint
        run: |
          brew install swiftlint
          swiftlint lint --strict
```

---

### Phase 4: Test Infrastructure

**CHECKPOINT 2:** Verify project compiles and tooling is configured.

```markdown
## Scaffold Status
- [ ] Project compiles with zero warnings
- [ ] All three configurations build successfully
- [ ] Test targets exist and run
- [ ] SwiftLint passes
- [ ] .gitignore excludes user data

**Proceed with test infrastructure?**
```

#### 4.1 Test Helpers

```swift
// File: MyAppTests/Helpers/MockURLProtocol.swift

import Foundation

final class MockURLProtocol: URLProtocol {
    static var requestHandler: ((URLRequest) throws -> (HTTPURLResponse, Data))?

    override class func canInit(with request: URLRequest) -> Bool { true }
    override class func canonicalRequest(for request: URLRequest) -> URLRequest { request }

    override func startLoading() {
        guard let handler = MockURLProtocol.requestHandler else {
            fatalError("MockURLProtocol.requestHandler not set")
        }

        do {
            let (response, data) = try handler(request)
            client?.urlProtocol(self, didReceive: response, cacheStoragePolicy: .notAllowed)
            client?.urlProtocol(self, didLoad: data)
            client?.urlProtocolDidFinishLoading(self)
        } catch {
            client?.urlProtocol(self, didFailWithError: error)
        }
    }

    override func stopLoading() {}

    static func mockSession() -> URLSession {
        let config = URLSessionConfiguration.ephemeral
        config.protocolClasses = [MockURLProtocol.self]
        return URLSession(configuration: config)
    }
}
```

```swift
// File: MyAppTests/Helpers/XCTestCase+Async.swift

import XCTest

extension XCTestCase {
    func assertThrowsAsync<T>(
        _ expression: @autoclosure () async throws -> T,
        _ message: String = "",
        file: StaticString = #filePath,
        line: UInt = #line
    ) async {
        do {
            _ = try await expression()
            XCTFail("Expected error to be thrown \(message)", file: file, line: line)
        } catch {
            // Expected
        }
    }
}
```

---

## Expected Output

### File Count by Category

```
App entry point:           3 files
Feature scaffolds:         6 files
Core/Networking:           3 files
Core/Persistence:          1 file
Shared components:         3 files
Design system:             3 files
Navigation:                2 files
Configuration:             4 files (+ xcconfig)
Test infrastructure:       4 files
CI/CD:                     2 files
Tooling config:            3 files (.gitignore, .swiftlint.yml, .swiftformat)
─────────────────────────────────
Total:                    ~34 files
```

### Project Checklist

- [ ] App compiles and runs on simulator
- [ ] Three build configurations (Debug, Staging, Release)
- [ ] Feature folder structure established
- [ ] Networking layer with mock support
- [ ] Shared UI components (loading, error, empty)
- [ ] Design system tokens defined
- [ ] Navigation structure in place
- [ ] Test targets with helpers
- [ ] CI/CD pipeline template
- [ ] SwiftLint configured
- [ ] .gitignore comprehensive

---

## Example Interaction

**User:** "New recipe app called 'Recipeze', com.recipeze.app, MVVM, SwiftUI, iOS 17+, single target for now, GitHub Actions CI."

**Assistant:** I'll generate the complete scaffold. Key decisions:

1. **Single target** with feature folders (not SPM modules yet -- can modularize later)
2. **@Observable ViewModels** since iOS 17+ (no ObservableObject/Combine needed)
3. **SwiftData** for persistence (iOS 17+ enables it)
4. **Three xcconfigs** with different bundle IDs for parallel installs

[Generates full directory structure and all boilerplate files]

The project will compile immediately after `git clone` and `open Recipeze.xcodeproj`. First feature development can start in `Features/Recipes/`.

---

## Techniques Used

- **ST-01** (Clear Objective): Generate compilable, production-ready project scaffold
- **ST-02** (Sequential Instructions): Four-phase generation from structure to testing
- **ST-03** (Output Format Templates): Complete file contents with exact paths

---

## Related Prompts

- [ios_architecture_selection.md](ios_architecture_selection.md) - Must be decided before scaffolding
- [ios_tech_stack_selection.md](ios_tech_stack_selection.md) - Technology choices inform scaffold contents
- [ios_module_design.md](ios_module_design.md) - For multi-module scaffold with SPM

---

## Customization Guide

### For UIKit-First Projects
Replace `@main App` with `@UIApplicationMain AppDelegate`, add `SceneDelegate`, and use `UINavigationController` / `UITabBarController` as root.

### For TCA Projects
Replace `@Observable` ViewModels with `@Reducer` structs, add `ComposableArchitecture` SPM dependency, and structure features as `FeatureName/FeatureName.swift` (reducer) + `FeatureNameView.swift`.

### For Multi-Module from Day One
Move `Core/`, `Shared/`, and each `Feature/` into separate SPM targets inside `Packages/AppModules/`. Reference ios_module_design.md for Package.swift configuration.
