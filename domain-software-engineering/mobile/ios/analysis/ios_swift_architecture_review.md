---
title: "iOS/Swift Architecture Review"
category: mobile-development
description: "Analyzes iOS Swift codebases to identify design patterns, state management approaches, and modernization opportunities following Apple guidelines"
tags:
  - mobile-development
  - review
updated: "2026-03-19"
---

# iOS/Swift Architecture Review

**Objective:** Analyze iOS/Swift codebase architecture to identify design patterns, code organization, state management approaches, and opportunities for improvement following iOS best practices and Apple's Human Interface Guidelines.

**When to Use:** Use this prompt when reviewing iOS applications built with Swift, whether using UIKit, SwiftUI, or a hybrid approach. Ideal for architecture audits, onboarding to legacy codebases, or planning refactoring efforts.

**Instructions:**

1. **Analyze Project Structure:**
   * Examine the project organization (MVC, MVVM, VIPER, Clean Architecture, etc.)
   * Identify how features are organized (by layer, by feature, hybrid)
   * Review folder structure and file naming conventions
   * Assess module boundaries and dependencies

2. **Review Architectural Patterns:**
   * Identify the primary architectural pattern(s) in use
   * Evaluate consistency of pattern application across the codebase
   * Look for UIKit patterns: Delegation, Target-Action, Notifications, KVO
   * Check SwiftUI patterns: State management (@State, @Binding, @ObservedObject, @StateObject, @EnvironmentObject)
   * Assess use of Combine or async/await for reactive programming

3. **State Management Analysis:**
   * Review how application state is managed and shared
   * Identify data flow patterns (unidirectional, bidirectional)
   * Evaluate use of persistent storage (UserDefaults, CoreData, SwiftData, Realm, SQLite)
   * Check for proper separation between local and remote state
   * Assess caching strategies and data synchronization

4. **Navigation and Routing:**
   * Analyze navigation patterns (Coordinator pattern, Router, Storyboard segues, programmatic)
   * Review deep linking implementation
   * Check tab bar and navigation controller usage
   * Evaluate modal presentation management

5. **Dependency Management:**
   * Review dependency injection approach (constructor injection, property injection, service locators)
   * Evaluate third-party dependencies (CocoaPods, Swift Package Manager, Carthage)
   * Check for tight coupling and opportunities for abstraction
   * Assess protocol-oriented design usage

6. **View Layer Analysis:**
   * **UIKit Apps:** Review view controllers, custom views, Auto Layout usage, xib/storyboard vs. programmatic UI
   * **SwiftUI Apps:** Analyze view composition, view modifiers, custom views, PreferenceKey usage
   * Check for massive view controllers (over 300 lines)
   * Evaluate separation of concerns between views and business logic

7. **Networking Layer:**
   * Review networking architecture (URLSession, Alamofire, custom abstraction)
   * Check API client design and endpoint organization
   * Evaluate error handling and retry logic
   * Assess request/response serialization (Codable usage)
   * Review authentication and token management

8. **Concurrency and Threading:**
   * Analyze use of GCD, OperationQueue, async/await, and actors
   * Check for main thread violations and UI updates
   * Review background task handling
   * Identify potential race conditions or threading issues

9. **Memory Management:**
   * Check for retain cycles and memory leaks (especially in closures)
   * Review weak/unowned reference usage
   * Assess large object handling and lazy loading
   * Evaluate image caching and memory pressure handling

10. **Testing Architecture:**
    * Review unit test coverage and organization
    * Check for UI tests and snapshot tests
    * Assess testability of architecture (dependency injection, protocols)
    * Evaluate mock/stub usage

11. **Identify Anti-Patterns:**
    * Massive View Controllers (God Objects)
    * Excessive force unwrapping (!)
    * Overuse of singletons
    * Tight coupling between layers
    * Mixing UIKit and SwiftUI improperly
    * Synchronous operations on main thread
    * Inconsistent error handling

12. **Platform Integration:**
    * Review integration with iOS frameworks (CoreLocation, CoreMotion, HealthKit, etc.)
    * Check proper handling of app lifecycle events
    * Evaluate background modes and notifications
    * Assess widget and app extension architecture

**Expected Output:** A comprehensive architecture review report that includes:

1. **Architecture Summary:**
   - Primary architectural pattern identified
   - Overall organization assessment (Good/Moderate/Needs Improvement)
   - Technology stack overview

2. **Detailed Findings by Category:**
   - For each analysis area (structure, patterns, state management, etc.):
     - Current state description
     - Code examples demonstrating patterns
     - Strengths identified
     - Issues and anti-patterns found
     - Severity rating (Critical/High/Medium/Low)

3. **Specific Recommendations:**
   - Prioritized list of improvements
   - Refactoring suggestions with examples
   - Migration paths for identified issues
   - Best practices to adopt

4. **Code Examples:**
   - Before/after code snippets for recommended changes
   - Reference to line numbers and files where applicable

5. **Metrics:**
   - View controller complexity (lines of code, responsibilities)
   - Module coupling assessment
   - Test coverage gaps

**Example Output:**

```
# iOS Architecture Review Report

## Architecture Summary
- **Primary Pattern:** MVVM with Coordinator pattern
- **UI Framework:** SwiftUI with UIKit interop for legacy screens
- **State Management:** Combine + @Published properties
- **Overall Assessment:** Moderate - Good foundation with areas for improvement

## Detailed Findings

### 1. Project Structure (Status: Good)
**Strengths:**
- Clear feature-based organization: `Features/Authentication/`, `Features/Dashboard/`
- Proper separation of networking layer in `Services/NetworkLayer/`

**Issues:**
- Some shared models scattered across feature folders
- No clear distinction between domain and presentation models

**Code Example:**
File: `Features/Authentication/LoginViewController.swift`
```swift
// Current: View controller handling both UI and business logic
class LoginViewController: UIViewController {
    func loginButtonTapped() {
        // Direct network call - should be in ViewModel
        NetworkManager.shared.login(email: email, password: password)
    }
}
```

**Recommendation:**
- Create `Domain/Models/` folder for shared business models
- Move networking calls to ViewModels
- Introduce proper MVVM separation

[... more detailed sections ...]
```

**Techniques Used:**
- ST-01 (Clear Objective)
- ST-02 (Sequential Instructions)
- RT-02 (Multi-Dimensional Analysis)
- RT-06 (Pattern Recognition)
- ST-03 (Structured Output Templates)

**Related Prompts:**
- `mobile_app_security_review.md` - For security-specific analysis
- `cross_platform_architecture_design.md` - For apps using React Native/Flutter
- `architecture_layer_identification.md` - For general layer analysis
- `quality_code_style_consistency.md` - For Swift style guide compliance

**Customization Guide:**
- For pure UIKit apps: Focus more on sections 6 (UIKit specifics), remove SwiftUI analysis
- For pure SwiftUI apps: Skip UIKit patterns, emphasize declarative UI patterns
- For large enterprise apps: Add sections on modularization and feature flags
- For apps with Objective-C: Add analysis of Swift/Objective-C interop patterns
- Specify particular frameworks in use: "This app uses The Composable Architecture (TCA)" for specialized analysis
