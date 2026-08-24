---
title: "iOS Architecture Review"
category: mobile-development
description: "Deep analysis of iOS app architecture evaluating MVVM/TCA/VIPER consistency, layer boundaries, dependency graph, and protocol-oriented design with modernization recommendations"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-04
  - AG-02
difficulty: advanced
tags:
  - ios
  - swift
  - mobile-development
  - architecture
  - mvvm
  - tca
  - viper
updated: "2026-03-19"
---

# iOS Architecture Review

**Objective:** Conduct a deep analysis of an iOS app's architecture, evaluating pattern implementation (MVVM, TCA, VIPER, or hybrid), layer boundaries, dependency graph, protocol-oriented design, state management, and navigation to provide modernization recommendations.

**When to Use:** Use this prompt when you need to understand how an iOS app is structured architecturally, identify architectural issues, evaluate adherence to best practices, or plan architectural improvements. Ideal after a codebase health assessment reveals architecture concerns, before major feature additions, or when onboarding to understand how the app is organized.

**Prompt Type:** Comprehensive (350-450 lines)

---

## Context Gathering

Before beginning the architecture review, gather context:

1. **Architecture Intent:**
   - "What architecture pattern was this app designed to follow (MVC, MVVM, TCA, VIPER, Clean Architecture, or unknown)?"
   - "Are there any architecture documentation or ADRs (Architecture Decision Records) I should be aware of?"

2. **Known Issues:**
   - "Are there specific architectural concerns you've encountered (e.g., hard to test, tangled dependencies, massive view controllers)?"

3. **Goals:**
   - "What's driving this review? (understanding the current state, planning refactoring, evaluating for new feature work)"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual code patterns** - Don't flag based on pattern matching alone. Verify that the suspected architectural issue actually causes problems.
2. **Check for existing patterns** - Search for consistent conventions, abstractions, or documentation that explain architectural decisions.
3. **Understand the context** - Consider WHY the architecture evolved this way. Team size, project history, and requirements are valid factors.
4. **Confirm actual impact** - Does this architectural choice actually hurt maintainability, testability, or scalability?
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `HomeViewModel.swift:34`).

**Finding the architecture ADEQUATE is an acceptable outcome.** If the codebase follows reasonable patterns for its context, say so with confidence. Don't manufacture architectural concerns.

### False-Positive Prevention

- ❌ Do NOT flag all deviations from "pure" architecture patterns as problems
- ❌ Do NOT flag pragmatic MVC as inherently bad if controllers are well-factored
- ❌ Do NOT assume inconsistency without searching for conventions
- ❌ Do NOT report architectural preferences as defects
- ✅ DO consider the project's size, team, and constraints
- ✅ DO understand that different architectures suit different contexts
- ✅ DO check for consistent application of chosen patterns
- ✅ DO weigh the cost of "fixing" architecture against actual benefits

---

### Phase 1: Architecture Discovery

#### 1.1 Pattern Identification

**Search for architectural indicators in the codebase:**

```swift
// MVC Indicators
- UIViewController subclasses with business logic
- Direct model manipulation in view controllers
- No intermediary between views and models

// MVVM Indicators
- ViewModel classes (ObservableObject conformance)
- @Published properties exposing UI state
- Views/ViewControllers observing ViewModel state
- Combine pipelines or async/await in ViewModels

// TCA (The Composable Architecture) Indicators
- Reducer protocol conformances
- State structs, Action enums
- Store<State, Action> usage
- Effect return types
- @Dependency property wrappers

// VIPER Indicators
- Router / Wireframe classes
- Interactor classes
- Presenter classes holding weak view references
- Entity models separate from view models

// Clean Architecture Indicators
- UseCase / Interactor protocols
- Separate modules for domain, data, presentation
- Dependency rule: outer layers depend on inner layers
- Domain entities without UIKit/SwiftUI imports

// Coordinator Pattern Indicators
- Coordinator protocol / base class
- NavigationController management in coordinators
- Child coordinator hierarchy
```

**Pattern Detection Checklist:**

| Pattern | Key Indicators | Consistency |
|---------|---------------|-------------|
| MVC | ViewController with model access | [Consistent/Partial/Inconsistent] |
| MVVM | ObservableObject, @Published, bindings | [Consistent/Partial/Inconsistent] |
| TCA | Reducer, Store, Effect, @Dependency | [Consistent/Partial/Inconsistent] |
| VIPER | Router, Interactor, Presenter, Entity | [Consistent/Partial/Inconsistent] |
| Clean | UseCase, Domain module, Dependency rule | [Consistent/Partial/Inconsistent] |
| Coordinator | Coordinator protocol, child management | [Consistent/Partial/Inconsistent] |

#### 1.2 Module Structure Analysis

**Examine project modules:**

```
// Single Target Structure
App/
└── Sources/
    ├── Features/
    ├── Core/
    ├── Data/
    └── Domain/

// Multi-Package Structure (SPM)
Package.swift defines:
├── App (executable)
├── FeatureHome (library)
├── FeatureProfile (library)
├── CoreNetworking (library)
├── CorePersistence (library)
└── SharedModels (library)

// Framework-Based Structure
├── App.xcodeproj
├── Frameworks/
│   ├── CoreKit.framework
│   ├── NetworkKit.framework
│   └── UIComponents.framework
```

**Evaluate:**
- Module organization strategy (by feature, by layer, hybrid)
- Module dependency graph (check import statements across modules)
- Access control boundaries (public/internal/private/package)
- Build performance impact of module structure

#### 1.3 Protocol-Oriented Design Assessment

**Evaluate protocol usage:**

```swift
// Good: Protocol-oriented abstractions
protocol NetworkServiceProtocol {
    func fetch<T: Decodable>(_ request: URLRequest) async throws -> T
}

// Good: Protocol composition
typealias DataManager = Fetchable & Storable & Cacheable

// Anti-pattern: Protocol for the sake of protocol (only one conformer, no testing need)
protocol HomeViewModelProtocol { /* mirrors the class exactly */ }
class HomeViewModel: HomeViewModelProtocol { }

// Good: Protocol with default implementation
extension Cacheable {
    func invalidateCache() { /* default behavior */ }
}
```

---

### Phase 2: Layer Analysis

#### 2.1 UI Layer Assessment

**Components to examine:**

```swift
// UIKit ViewControllers
- Lifecycle handling (viewDidLoad, viewWillAppear)
- Configuration change handling (traitCollectionDidChange)
- Business logic presence (should be minimal)

// SwiftUI Views
- State management (@State, @StateObject, @ObservedObject, @EnvironmentObject)
- View decomposition (body complexity)
- Side effect handling (.task, .onChange, .onAppear)
- Preview functions presence

// ViewModels
- State exposure pattern (@Published, CurrentValueSubject)
- Input handling (methods, Combine subjects, Action enums)
- Business logic location
- Cancellable/Task lifecycle management
```

**UI Layer Evaluation Criteria:**

| Criterion | Good Practice | Anti-Pattern |
|-----------|--------------|--------------|
| **Responsibility** | Display state, capture user input | Business logic, direct network calls |
| **State** | Observes ViewModel / Store state | Manages own complex business state |
| **Navigation** | Delegates to coordinator / NavigationStack | Contains hardcoded push/present logic |
| **Lifecycle** | Minimal lifecycle code | Heavy setup in viewDidLoad |

#### 2.2 Domain Layer Assessment

**Components to examine:**

```swift
// Use Cases / Interactors
- Single responsibility per use case
- No UIKit or SwiftUI imports
- Business rule encapsulation
- Proper naming (verb-based: FetchUserUseCase, ValidateEmailUseCase)

// Domain Models
- Pure Swift structs / value types
- No framework annotations (@objc, Codable only if needed)
- Business validation methods

// Repository Protocols (defined in domain)
- Defined in domain layer, implemented in data layer
- No implementation details leaked
- Proper abstraction level (no URLRequest in domain)
```

**Domain Layer Evaluation:**

| Criterion | Status | Notes |
|-----------|--------|-------|
| Layer exists | [Yes/No/Partial] | [Details] |
| Framework-free | [Yes/No] | [UIKit/SwiftUI imports found?] |
| Use cases present | [Yes/No/Partial] | [Count and quality] |
| Repository protocols | [Yes/No] | [Location] |

#### 2.3 Data Layer Assessment

**Components to examine:**

```swift
// Repository Implementations
- Protocol conformance
- Data source coordination
- Caching strategy (NSCache, in-memory, disk)
- Error handling and mapping

// Data Sources
- Local: Core Data / SwiftData, UserDefaults, Keychain, file system
- Remote: URLSession, Alamofire API clients
- Clear separation between sources

// Data Models
- DTOs (Codable structs for API responses)
- Managed objects (Core Data NSManagedObject / SwiftData @Model)
- Mappers to domain models
```

---

### Phase 3: Dependency Flow Analysis

#### 3.1 Dependency Direction Check

**Correct Dependency Flow:**
```
UI Layer -> Domain Layer <- Data Layer
   |              |            |
 Views       Use Cases    Repositories
ViewModels    Models     Data Sources
```

**Violations to Search For:**

```swift
// Domain layer importing UI frameworks
import UIKit  // VIOLATION in domain layer

// View directly accessing data layer
class HomeView: View {
    @State var items = CoreDataStack.shared.fetchAll()  // VIOLATION
}

// Data layer depending on UI models
class UserRepository {
    func getUser() -> UserCellViewModel  // VIOLATION - should return domain model
}
```

#### 3.2 Dependency Injection Analysis

**DI Approach Detection:**

```swift
// Constructor Injection (recommended)
class HomeViewModel {
    private let userRepository: UserRepositoryProtocol
    init(userRepository: UserRepositoryProtocol) { self.userRepository = userRepository }
}

// SwiftUI Environment
@Environment(\.networkService) var networkService
@EnvironmentObject var store: AppStore

// TCA Dependencies
@Dependency(\.apiClient) var apiClient

// Swinject / Factory / Needle
Container.shared.resolve(UserRepositoryProtocol.self)

// Service Locator (anti-pattern)
ServiceLocator.shared.resolve(UserRepository.self)

// Singleton access (anti-pattern for testability)
UserRepository.shared.fetchUser()
```

---

### Phase 4: State Management Review

#### 4.1 State Holder Patterns

**Identify state management approach:**

```swift
// SwiftUI @Observable (Swift 5.9+)
@Observable
class HomeViewModel {
    var items: [Item] = []
    var isLoading = false
}

// ObservableObject Pattern (pre-Observation)
class HomeViewModel: ObservableObject {
    @Published var items: [Item] = []
    @Published var isLoading = false
}

// TCA Store Pattern
@ObservedObject var store: StoreOf<Home>

// Combine-based Pattern
class HomeViewModel {
    let state: AnyPublisher<HomeState, Never>
    private let stateSubject = CurrentValueSubject<HomeState, Never>(.initial)
}
```

#### 4.2 UI State Modeling

```swift
// Good: Enum for exclusive states
enum LoadingState<T> {
    case idle
    case loading
    case loaded(T)
    case failed(Error)
}

// Good: Struct for composable state
struct HomeState: Equatable {
    var items: [Item] = []
    var isLoading = false
    var errorMessage: String?
}

// Anti-pattern: Scattered independent flags
class BadViewModel: ObservableObject {
    @Published var isLoading = false
    @Published var error: Error?
    @Published var items: [Item]?
    // Can have inconsistent states!
}
```

---

### Phase 5: Navigation Architecture

#### 5.1 Navigation Pattern Identification

```swift
// NavigationStack (iOS 16+)
NavigationStack(path: $router.path) {
    ContentView()
        .navigationDestination(for: Route.self) { route in ... }
}

// Coordinator Pattern (UIKit)
protocol Coordinator: AnyObject {
    var childCoordinators: [Coordinator] { get set }
    var navigationController: UINavigationController { get }
    func start()
}

// Router Pattern
class AppRouter: ObservableObject {
    @Published var path = NavigationPath()
    func navigate(to destination: Destination) { ... }
}

// Legacy: Storyboard Segues
override func prepare(for segue: UIStoryboardSegue, sender: Any?) { ... }
```

#### 5.2 Navigation Quality Assessment

| Aspect | Assessment | Notes |
|--------|------------|-------|
| Approach | [NavigationStack/Coordinator/Storyboard/Mixed] | |
| Type safety | [Typed routes/String-based/Segue identifiers] | |
| Deep linking | [Supported/Partial/None] | |
| Back navigation | [Proper/Issues] | |
| Modal presentation | [Consistent/Inconsistent] | |

---

### Phase 6: Findings Presentation

**CHECKPOINT:** Present architecture findings summary.

```markdown
## Architecture Review Summary

### Pattern Assessment

**Primary Pattern:** [MVC/MVVM/TCA/VIPER/Hybrid/Unclear]
**Consistency:** [High/Medium/Low]

### Layer Health

| Layer | Status | Key Issues |
|-------|--------|------------|
| UI | [Healthy/Issues] | [Summary] |
| Domain | [Present/Partial/Absent] | [Summary] |
| Data | [Healthy/Issues] | [Summary] |

### Critical Violations Found

1. **[Violation]** - [Location, Impact]
2. **[Violation]** - [Location, Impact]

### Questions Before Detailed Report

1. [Clarifying question about intent or constraints]
2. [Question about specific pattern found]

**Shall I proceed with the detailed architecture report and recommendations?**
```

---

### Phase 7: Detailed Architecture Report

```markdown
# Architecture Review Report: [App Name]

## Executive Summary

### Architecture Score: [A/B/C/D/F]

| Dimension | Score | Assessment |
|-----------|-------|------------|
| Pattern Clarity | [1-10] | [Clear/Hybrid/Unclear] |
| Layer Separation | [1-10] | [Strong/Weak/None] |
| Dependency Direction | [1-10] | [Correct/Violations] |
| State Management | [1-10] | [Modern/Legacy/Inconsistent] |
| Testability | [1-10] | [High/Medium/Low] |
| Protocol Design | [1-10] | [Principled/Excessive/Absent] |

### Architecture Profile
- **Pattern:** [Identified pattern with confidence level]
- **Modularization:** [Single target / SPM packages / Frameworks]
- **Navigation:** [Approach used]
- **DI:** [Approach and quality]

---

## Detailed Findings

### 1. Pattern Implementation

#### Identified: [Pattern Name]

**Evidence:**
```swift
// Example code showing pattern implementation
[Code snippet from actual codebase]
```

**Consistency Analysis:**

| Component Type | Follows Pattern | Deviations |
|----------------|-----------------|------------|
| ViewModels | [X/Y] | [List deviations] |
| Repositories | [X/Y] | [List deviations] |
| Use Cases | [X/Y or N/A] | [List deviations] |

---

## Modernization Recommendations

### Priority 1: Critical Fixes

| Fix | Current | Target | Effort | Impact |
|-----|---------|--------|--------|--------|
| [Fix] | [Current state] | [Target state] | [Hours/Days] | [High/Medium] |

### Priority 2: Architecture Improvements

| Improvement | Rationale | Approach |
|-------------|-----------|----------|
| Adopt @Observable | Better performance, less boilerplate | Incremental per-feature |
| Extract domain layer | Testability, separation of concerns | Define protocols first |
| Add NavigationStack router | Type-safe navigation, deep linking | Centralized Route enum |

### Priority 3: Modernization Opportunities

| Opportunity | Benefit | Complexity |
|-------------|---------|------------|
| Migrate to TCA | Predictable state, testable effects | High |
| Add SPM modularization | Build speed, encapsulation | Medium-High |
| Adopt Swift Concurrency | Structured concurrency, actor safety | Medium |

---

## Refactoring Roadmap

### Phase 1: Foundation (Low Risk)
- [Step 1]
- [Step 2]

### Phase 2: Core Architecture (Medium Risk)
- [Step 1]
- [Step 2]

### Phase 3: Full Modernization (Higher Risk)
- [Step 1]
- [Step 2]
```

---

## Expected Output

1. **Pattern Assessment** - Clear identification of architecture pattern(s) with confidence level
2. **Layer Analysis** - Detailed evaluation of each architectural layer
3. **Violation Report** - All dependency and pattern violations with locations
4. **State Management Review** - Assessment of current state handling
5. **Navigation Analysis** - Navigation architecture evaluation
6. **Modernization Roadmap** - Prioritized improvement recommendations

---

## Example Interaction

**User:** Review the architecture of this iOS e-commerce app. We think it's MVVM but it feels inconsistent.

**Agent:** I'll conduct a deep architecture review. Let me start by scanning for architectural patterns.

*[Agent performs architecture discovery]*

**Agent:**

## Architecture Review Summary

### Pattern Assessment

**Primary Pattern:** MVVM (with MVC remnants)
**Consistency:** Medium - 70% of features follow MVVM, 30% are still MVC

### Layer Health

| Layer | Status | Key Issues |
|-------|--------|------------|
| UI | Issues | 8 ViewControllers exceed 500 lines; mixing UIKit and SwiftUI without clear boundary |
| Domain | Partial | Use cases exist for checkout flow but not for catalog or user features |
| Data | Healthy | Repository pattern well-implemented with protocol abstractions |

### Critical Violations Found

1. **CartViewController.swift:142** - Direct Core Data fetch in view controller, bypassing repository
2. **ProductListViewModel.swift:78** - ViewModel imports UIKit for UIImage handling instead of using a domain image model

**Shall I proceed with the detailed architecture report and recommendations?**

---

## Techniques Used

- **ST-01** (Clear Objective): Focused architecture analysis objective
- **ST-02** (Sequential Instructions): Phased discovery and analysis process
- **RT-02** (Multi-Dimensional Analysis): Six-dimension architecture evaluation
- **RT-04** (Best Practice Review): iOS architecture best practices
- **AG-02** (Skeptical Default Stance): Honest assessment over validation

---

## Related Prompts

- [ios_codebase_health_assessment.md](ios_codebase_health_assessment.md) - Broader codebase evaluation
- [ios_technical_debt_assessment.md](ios_technical_debt_assessment.md) - Debt cataloging
- [ios_swiftui_migration_analysis.md](ios_swiftui_migration_analysis.md) - SwiftUI migration readiness
- [ios_ai_code_review.md](ios_ai_code_review.md) - AI-assisted Swift code review

---

## Customization Guide

### For SwiftUI-First Apps
- Emphasize @Observable vs ObservableObject patterns
- Check for proper @State / @Binding usage
- Analyze View decomposition and body complexity
- Review environment and preference key usage

### For TCA Apps
- Focus on Reducer composition and scope
- Check Effect management and cancellation
- Analyze @Dependency usage and test overrides
- Review navigation state management

### For Legacy UIKit Apps
- Focus on migration paths from MVC
- Identify quick wins for ViewModel extraction
- Consider Coordinator pattern for navigation
- Check for storyboard spaghetti

### For Multi-Module Apps
- Add module dependency graph analysis
- Check access control boundaries (public vs package)
- Evaluate build configuration consistency
- Assess inter-module communication patterns
