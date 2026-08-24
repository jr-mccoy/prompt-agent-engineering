---
title: "iOS Module Design"
category: mobile-development
description: "Design multi-module iOS project structure using Swift Package Manager with clear dependency graphs, interface boundaries, and build performance optimization."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ST-03
difficulty: advanced
tags:
  - ios
  - swift
  - spm
  - modules
  - architecture
updated: "2026-03-20"
---

# iOS Module Design

**Objective:** Design a multi-module iOS project using Swift Package Manager (SPM) with clearly defined module boundaries, dependency graphs, interface segregation, and build performance optimization, producing a complete module architecture ready for implementation.

**When to Use:** Use when starting a new project that warrants modularization (3+ developers, 20+ screens) or when planning the module structure for an existing monolithic app. Ideal after architecture selection and before project scaffolding.

**Prompt Type:** Comprehensive (400+ lines)

---

## Context Gathering

Before designing modules, gather essential context:

1. **Project Scope:**
   - "List all features/domains in the app (e.g., Auth, Profile, Feed, Payments)."
   - "Which features share data or workflows?"
   - "How many developers/teams will work on the project?"

2. **Technical Context:**
   - "What architecture pattern is used (MVVM, TCA, Clean)?"
   - "Are there existing SPM packages or CocoaPods/Carthage dependencies?"
   - "What is the minimum deployment target?"

3. **Build Requirements:**
   - "What is the current clean build time (if existing project)?"
   - "Is there a build time budget?"
   - "Do you need to distribute any modules as binary frameworks?"

4. **Organizational:**
   - "Do different teams own different features?"
   - "Are there shared design system components?"
   - "Is there a separate backend team with defined API contracts?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before designing ANY module structure, you MUST:**

1. **Map feature dependencies** - Identify which features depend on which shared capabilities.
2. **Enforce acyclic dependency graph** - No circular dependencies between modules.
3. **Define interface modules** - Separate protocols/interfaces from implementations.
4. **Verify build parallelism** - Independent modules must be compilable in parallel.
5. **Test each module independently** - Every module must have its own test target.

### False-Positive Prevention

- ❌ Do NOT create modules with circular dependencies
- ❌ Do NOT put all shared code in a single "Common" or "Utils" module (becomes a dump)
- ❌ Do NOT create too many fine-grained modules (build graph overhead exceeds benefit under 5 modules)
- ❌ Do NOT expose implementation details through module public APIs
- ❌ Do NOT make feature modules depend on other feature modules directly
- ✅ DO use interface modules (protocols) to break dependencies between features
- ✅ DO keep the dependency graph shallow (max 3-4 levels deep)
- ✅ DO design for parallel compilation
- ✅ DO provide demo apps per module for isolated development

---

### Phase 1: Domain Mapping

#### 1.1 Feature Domain Inventory

```markdown
| Feature Domain | Screens | External Dependencies | Shared Data |
|---------------|---------|----------------------|-------------|
| Auth | Login, Register, Forgot | AuthService API | User session |
| Profile | View, Edit, Settings | ProfileService API | User model |
| Feed | List, Detail, Comments | FeedService API | Feed items |
| Payments | Checkout, History | StoreKit, PaymentAPI | Purchase state |
```

#### 1.2 Shared Capability Mapping

```markdown
| Shared Capability | Used By | Type |
|-------------------|---------|------|
| Networking (APIClient) | All features | Infrastructure |
| User Session | Auth, Profile, Feed | Domain |
| Design System (UI components) | All features | UI |
| Analytics | All features | Infrastructure |
| Persistence (SwiftData) | Feed, Profile | Infrastructure |
| Image Loading | Feed, Profile | Infrastructure |
```

---

### Phase 2: Module Architecture

**CHECKPOINT 1:** Confirm feature domains and shared capabilities.

```markdown
## Domain Summary
- Feature domains: _
- Shared capabilities: _
- Cross-feature data sharing: _

**Proceed with module design?**
```

#### 2.1 Module Layering Strategy

```
┌─────────────────────────────────────────────┐
│                    App                       │  ← Composition Root
├──────────┬──────────┬──────────┬────────────┤
│FeatureAuth│FeatureFeed│FeatureProfile│FeaturePay│  ← Feature Modules
├──────────┴──────────┴──────────┴────────────┤
│              SharedUI (Design System)        │  ← UI Components
├──────────┬──────────┬───────────────────────┤
│DomainAuth │DomainFeed │  DomainProfile       │  ← Domain Interfaces
├──────────┴──────────┴───────────────────────┤
│              Core (Networking, Persistence)   │  ← Infrastructure
├─────────────────────────────────────────────┤
│              Foundation Extensions            │  ← Zero-dependency utilities
└─────────────────────────────────────────────┘
```

#### 2.2 Module Types

| Type | Naming Convention | Contains | Depends On |
|------|------------------|----------|-----------|
| **App** | `MyApp` | Composition root, DI, navigation | All modules |
| **Feature** | `Feature{Name}` | Screens, ViewModels, feature logic | Domain interfaces, SharedUI, Core |
| **Domain Interface** | `Domain{Name}` | Protocols, DTOs, use case interfaces | Foundation only |
| **Shared UI** | `SharedUI` | Reusable views, design tokens | Foundation only |
| **Core** | `Core` | Networking, persistence, analytics | Foundation only |
| **Foundation** | `FoundationExt` | Extensions, utilities, no imports | Nothing |

#### 2.3 Package.swift Structure

```swift
// Package.swift (workspace-level local package)
// swift-tools-version: 5.9

import PackageDescription

let package = Package(
    name: "AppModules",
    platforms: [.iOS(.v17)],
    products: [
        // Feature modules
        .library(name: "FeatureAuth", targets: ["FeatureAuth"]),
        .library(name: "FeatureFeed", targets: ["FeatureFeed"]),
        .library(name: "FeatureProfile", targets: ["FeatureProfile"]),

        // Shared modules
        .library(name: "SharedUI", targets: ["SharedUI"]),
        .library(name: "Core", targets: ["Core"]),
        .library(name: "DomainAuth", targets: ["DomainAuth"]),
        .library(name: "DomainFeed", targets: ["DomainFeed"]),
        .library(name: "FoundationExt", targets: ["FoundationExt"]),
    ],
    targets: [
        // Feature targets
        .target(
            name: "FeatureAuth",
            dependencies: ["DomainAuth", "SharedUI", "Core"]
        ),
        .target(
            name: "FeatureFeed",
            dependencies: ["DomainFeed", "DomainAuth", "SharedUI", "Core"]
        ),
        .target(
            name: "FeatureProfile",
            dependencies: ["DomainAuth", "SharedUI", "Core"]
        ),

        // Domain interface targets (protocol-only, lightweight)
        .target(name: "DomainAuth", dependencies: ["FoundationExt"]),
        .target(name: "DomainFeed", dependencies: ["FoundationExt"]),

        // Shared targets
        .target(name: "SharedUI", dependencies: ["FoundationExt"]),
        .target(name: "Core", dependencies: ["FoundationExt"]),
        .target(name: "FoundationExt", dependencies: []),

        // Test targets
        .testTarget(name: "FeatureAuthTests", dependencies: ["FeatureAuth"]),
        .testTarget(name: "FeatureFeedTests", dependencies: ["FeatureFeed"]),
        .testTarget(name: "CoreTests", dependencies: ["Core"]),
    ]
)
```

---

### Phase 3: Interface Design

**CHECKPOINT 2:** Validate dependency graph has no cycles.

```markdown
## Dependency Graph Validation
- Circular dependencies found: [Yes/No]
- Max dependency depth: _
- Modules compilable in parallel: _

**Proceed with interface design?**
```

#### 3.1 Domain Interface Pattern

```swift
// Sources/DomainAuth/UserSession.swift
// Protocol-only module -- no implementation

public protocol UserSessionProviding: Sendable {
    var currentUser: User? { get async }
    var isAuthenticated: Bool { get async }
    func signOut() async throws
}

public struct User: Sendable, Equatable, Codable {
    public let id: String
    public let email: String
    public let displayName: String

    public init(id: String, email: String, displayName: String) {
        self.id = id
        self.email = email
        self.displayName = displayName
    }
}
```

```swift
// Sources/FeatureAuth/AuthService.swift
// Implementation lives in feature module

import DomainAuth

final class AuthService: UserSessionProviding {
    var currentUser: User? { /* real implementation */ }
    var isAuthenticated: Bool { currentUser != nil }
    func signOut() async throws { /* real implementation */ }
}
```

```swift
// Sources/FeatureFeed/FeedViewModel.swift
// Depends on interface, not implementation

import DomainAuth

@Observable
final class FeedViewModel {
    private let userSession: any UserSessionProviding

    init(userSession: any UserSessionProviding) {
        self.userSession = userSession
    }
}
```

#### 3.2 Dependency Rule Enforcement

```markdown
## Module Dependency Rules

| Rule | Enforcement |
|------|------------|
| Feature → Feature: FORBIDDEN | SPM won't compile (not in dependencies) |
| Feature → Domain Interface: ALLOWED | Explicit dependency declaration |
| Feature → Core: ALLOWED | Infrastructure access |
| Feature → SharedUI: ALLOWED | Reusable components |
| Domain → Domain: FORBIDDEN | Keep interfaces isolated |
| Core → Feature: FORBIDDEN | Infrastructure never depends on features |
| SharedUI → Feature: FORBIDDEN | UI components never depend on features |
```

---

### Phase 4: Build Optimization

#### 4.1 Build Graph Analysis

```markdown
## Parallel Build Opportunities

Level 0 (no dependencies): FoundationExt
Level 1 (depends on L0): DomainAuth, DomainFeed, SharedUI, Core
Level 2 (depends on L1): FeatureAuth, FeatureFeed, FeatureProfile
Level 3 (depends on L2): App

**Effective parallelism:** 4 modules at Level 1, 3 modules at Level 2
**Critical path:** FoundationExt → Core → FeatureFeed → App
```

#### 4.2 Build Performance Rules

| Rule | Rationale |
|------|-----------|
| Keep FoundationExt tiny | It blocks everything |
| Domain interfaces have zero heavy dependencies | Fast compilation |
| Use `@_exported import` sparingly | Increases coupling |
| Prefer concrete types over generics in module APIs | Reduces specialization time |
| Enable BUILD_LIBRARY_FOR_DISTRIBUTION only for binary frameworks | Slower builds otherwise |

---

### Phase 5: Module Testing Strategy

#### 5.1 Test Organization

```
Tests/
├── FeatureAuthTests/          # Feature-level tests
│   ├── AuthViewModelTests.swift
│   └── Mocks/
│       └── MockUserSession.swift
├── FeatureFeedTests/
│   ├── FeedViewModelTests.swift
│   └── Mocks/
├── CoreTests/
│   ├── APIClientTests.swift
│   └── PersistenceTests.swift
└── IntegrationTests/          # Cross-module tests (in App target)
    └── AuthToFeedFlowTests.swift
```

#### 5.2 Mock Generation per Module

```swift
// Each domain interface module provides a mock for testing
// Sources/DomainAuth/Testing/MockUserSession.swift

#if DEBUG
public final class MockUserSession: UserSessionProviding {
    public var mockUser: User?
    public var currentUser: User? { mockUser }
    public var isAuthenticated: Bool { mockUser != nil }
    public func signOut() async throws { mockUser = nil }

    public init(user: User? = nil) { self.mockUser = user }
}
#endif
```

---

## Expected Output

```
Module Architecture Document
├── Domain Feature Inventory
├── Shared Capability Map
├── Module Layer Diagram
├── Package.swift (complete)
├── Interface Protocol Definitions
├── Dependency Rules Matrix
├── Build Graph Analysis
└── Module Testing Strategy
```

---

## Example Interaction

**User:** "We have Auth, Feed, Messaging, and Profile features. Three developers. MVVM architecture."

**Assistant:**

**Module Structure (7 modules):**
```
App → FeatureAuth, FeatureFeed, FeatureMessaging, FeatureProfile
FeatureAuth → DomainAuth, SharedUI, Core
FeatureFeed → DomainFeed, DomainAuth, SharedUI, Core
FeatureMessaging → DomainMessaging, DomainAuth, SharedUI, Core
FeatureProfile → DomainAuth, SharedUI, Core
```

**Key decision:** Messaging depends on DomainAuth (needs user info for chat) but NOT on FeatureAuth. The interface module breaks this dependency.

**Build parallelism:** 4 feature modules compile in parallel after Core + SharedUI complete. Estimated 40% build time reduction vs monolith.

---

## Techniques Used

- **ST-01** (Clear Objective): Design complete module architecture with dependency graph
- **ST-02** (Sequential Instructions): Five-phase approach from domain mapping to testing
- **RT-02** (Multi-Dimensional Analysis): Evaluates coupling, build performance, testability
- **ST-03** (Output Format Templates): Package.swift, protocol definitions, directory structures

---

## Related Prompts

- [ios_architecture_selection.md](ios_architecture_selection.md) - Architecture must be selected before module design
- [ios_modularization_strategy.md](ios_modularization_strategy.md) - For migrating existing monoliths to modules
- [ios_project_scaffold.md](ios_project_scaffold.md) - Scaffold the designed module structure

---

## Customization Guide

### For Micro-Feature Architecture
Split feature modules further: `FeatureFeedInterface`, `FeatureFeedUI`, `FeatureFeedData`. This adds build parallelism but increases module count. Only recommended for 8+ developer teams.

### For Binary Framework Distribution
Add XCFramework build targets for modules shared across apps. Use `BUILD_LIBRARY_FOR_DISTRIBUTION = YES` and document ABI stability requirements.

### For TCA-Based Projects
Each feature module contains its own Reducer, and composition happens at the App level via `Scope`. Domain interfaces become TCA `DependencyKey` conformances instead of standalone protocols.
