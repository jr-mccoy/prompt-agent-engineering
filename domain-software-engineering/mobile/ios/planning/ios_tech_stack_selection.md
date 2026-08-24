---
title: "iOS Tech Stack Selection"
category: mobile-development
description: "Select technology choices for iOS projects including SwiftUI vs UIKit, Core Data vs SwiftData, networking, dependency injection, and third-party dependencies."
techniques:
  - ST-01
  - RT-02
difficulty: intermediate
tags:
  - ios
  - swift
  - tech-stack
  - swiftui
  - uikit
updated: "2026-03-20"
---

# iOS Tech Stack Selection

**Objective:** Select the optimal technology stack for an iOS project across UI framework, data persistence, networking, dependency injection, and third-party dependencies, producing a justified technology decision document.

**When to Use:** Use after architecture selection and before project scaffolding. Ideal when starting a new project or evaluating a major stack migration. Also useful when auditing an existing stack for modernization opportunities.

**Prompt Type:** Modular (200-300 lines)

---

## Context Gathering

Before recommending technologies, gather essential context:

1. **Project Constraints:**
   - "What is the minimum iOS deployment target?"
   - "Is there an existing codebase or is this greenfield?"
   - "Are there mandated technologies from the organization?"

2. **Requirements:**
   - "Does the app need offline support?"
   - "What kind of data does the app persist (simple key-value, relational, documents)?"
   - "Are there real-time or background processing requirements?"

3. **Team:**
   - "What technologies is the team already proficient with?"
   - "How important is minimizing third-party dependencies?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY technology, you MUST:**

1. **Check iOS version compatibility** - Verify the API is available on the minimum deployment target.
2. **Evaluate first-party vs third-party** - Always prefer Apple frameworks when they meet requirements.
3. **Assess maintenance risk** - Check third-party library activity (last commit, open issues, bus factor).
4. **Provide migration paths** - If recommending newer tech, show how to coexist with legacy.

### False-Positive Prevention

- ❌ Do NOT recommend SwiftData for iOS 16 or earlier targets
- ❌ Do NOT recommend third-party libraries when Apple provides equivalent APIs
- ❌ Do NOT recommend Combine for new code when async/await is available on target
- ❌ Do NOT ignore the cost of adding external dependencies (binary size, build time, supply chain risk)
- ✅ DO prefer first-party frameworks for long-term maintainability
- ✅ DO consider Apple's deprecation trajectory when evaluating technologies
- ✅ DO account for the debugging advantage of first-party frameworks

---

### Phase 1: Decision Categories

#### 1.1 UI Framework

| Factor | SwiftUI | UIKit | Hybrid |
|--------|---------|-------|--------|
| **Best for** | iOS 16+, new projects | iOS 14+, complex custom UI | Migration, mixed needs |
| **Strengths** | Declarative, previews, less code | Mature, full control, UICollectionView | Gradual adoption |
| **Weaknesses** | Navigation quirks, limited custom layouts | Verbose, no previews | Two mental models |
| **Choose when** | Greenfield, standard UI patterns | Custom animations, legacy | Existing UIKit + new features |

**Decision rule:** If iOS 16+ and no heavy custom UICollectionView layouts, default to SwiftUI.

#### 1.2 Data Persistence

| Factor | SwiftData | Core Data | GRDB/SQLite | UserDefaults | Keychain |
|--------|-----------|-----------|-------------|-------------|----------|
| **iOS min** | 17 | 11 | Any | Any | Any |
| **Best for** | Swift models, simple relations | Complex relations, iCloud | SQL control, performance | Preferences | Credentials |
| **Complexity** | Low | High | Medium | Minimal | Low |
| **CloudKit sync** | Built-in | NSPersistentCloudKitContainer | Manual | Via iCloud KV | N/A |

```swift
// SwiftData (iOS 17+)
@Model
final class Recipe {
    var title: String
    var ingredients: [Ingredient]
    var createdAt: Date

    init(title: String, ingredients: [Ingredient] = []) {
        self.title = title
        self.ingredients = ingredients
        self.createdAt = .now
    }
}

// Core Data (iOS 11+)
// Requires .xcdatamodeld, NSManagedObject subclasses, NSPersistentContainer setup
```

#### 1.3 Networking

| Factor | URLSession | Alamofire | gRPC-Swift |
|--------|-----------|-----------|------------|
| **Best for** | REST APIs, standard needs | Complex auth, retry, interceptors | Protobuf APIs |
| **Async/await** | Native (iOS 15+) | Supported | Supported |
| **Recommendation** | Default choice | Only if URLSession insufficient | Only if backend uses gRPC |

```swift
// Modern URLSession (sufficient for most apps)
final class APIClient {
    private let session: URLSession
    private let decoder = JSONDecoder()

    func fetch<T: Decodable>(_ endpoint: Endpoint) async throws -> T {
        let (data, response) = try await session.data(for: endpoint.request)
        guard let http = response as? HTTPURLResponse, 200...299 ~= http.statusCode else {
            throw APIError.invalidResponse
        }
        return try decoder.decode(T.self, from: data)
    }
}
```

#### 1.4 Dependency Injection

| Approach | Complexity | Testability | Runtime Safety |
|----------|-----------|-------------|---------------|
| Init injection | Low | High | Compile-time |
| @Environment (SwiftUI) | Low | Medium | Runtime |
| swift-dependencies (TCA) | Medium | Very High | Compile-time |
| Factory/Swinject | Medium | High | Runtime |

**Recommendation:** Init injection for most projects. Use `@Environment` for SwiftUI-specific dependencies. Use `swift-dependencies` only with TCA.

---

### Phase 2: Technology Decision Matrix

**CHECKPOINT:** Confirm project constraints before finalizing.

```markdown
## Stack Selection Summary

| Category | Selected | Rationale |
|----------|----------|-----------|
| UI Framework | | |
| Persistence | | |
| Networking | | |
| DI Approach | | |
| Image Loading | | |
| Analytics | | |
| Crash Reporting | | |
| Logging | | |
| Testing | | |

## Third-Party Dependencies
| Library | Purpose | Last Updated | Risk Level |
|---------|---------|-------------|------------|
| | | | |

## Total Dependencies: _
**Target: < 10 third-party dependencies for maintainability**
```

---

## Expected Output

A technology decision document with justified selections per category, dependency inventory, and version compatibility matrix.

---

## Example Interaction

**User:** "New recipe app, iOS 17+, SwiftUI-first, needs offline support and cloud sync. Team of 3, want minimal dependencies."

**Assistant:**

| Category | Selected | Rationale |
|----------|----------|-----------|
| UI | SwiftUI | iOS 17+ target, greenfield, team preference |
| Persistence | SwiftData | iOS 17+, native Swift models, built-in CloudKit sync |
| Networking | URLSession + async/await | Standard REST, no complex interceptor needs |
| DI | Init injection | Simple, compile-safe, no framework needed |
| Image Loading | AsyncImage + custom cache | Avoid Kingfisher/SDWebImage dependency for basic needs |
| Testing | XCTest + swift-snapshot-testing | One external dep for visual regression |

**Total third-party deps: 1** (swift-snapshot-testing, dev only)

---

## Techniques Used

- **ST-01** (Clear Objective): Focused technology selection with decision criteria
- **RT-02** (Multi-Dimensional Analysis): Evaluates across compatibility, complexity, risk, and team fit

---

## Related Prompts

- [ios_architecture_selection.md](ios_architecture_selection.md) - Select architecture before choosing tech stack
- [ios_project_scaffold.md](ios_project_scaffold.md) - Scaffold project with selected stack
- [ios_offline_first_architecture.md](ios_offline_first_architecture.md) - Design offline-first with selected persistence

---

## Customization Guide

### For Enterprise Apps
Add categories for: MDM SDK, SSO framework (AppAuth), analytics platform (Firebase vs Amplitude), feature flagging (LaunchDarkly vs custom).

### For Minimalist Approach
Challenge every third-party dependency: "Can URLSession replace this? Can @Observable replace this? Can SwiftData replace this?" Target zero third-party runtime dependencies.
