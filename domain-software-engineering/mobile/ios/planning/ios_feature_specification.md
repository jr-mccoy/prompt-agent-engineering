---
title: "iOS Feature Specification"
category: mobile-development
description: "Transform product requirements into iOS-specific technical specifications with acceptance criteria, API contracts, state diagrams, and implementation tasks."
techniques:
  - ST-01
  - ST-02
  - ST-03
difficulty: intermediate
tags:
  - ios
  - swift
  - requirements
  - specifications
updated: "2026-03-20"
---

# iOS Feature Specification

**Objective:** Transform product requirements or user stories into detailed iOS-specific technical specifications that include state management design, API contracts, UI specifications, accessibility requirements, and testable acceptance criteria, producing an implementation-ready document.

**When to Use:** Use when translating PRDs, design specs, or user stories into technical specifications for iOS implementation. Ideal after architecture selection and before sprint planning. Useful for bridging the gap between product managers and iOS engineers.

**Prompt Type:** Comprehensive (400+ lines)

---

## Context Gathering

Before generating specifications, gather essential context:

1. **Product Requirement:**
   - "What is the feature? Provide the PRD, user story, or verbal description."
   - "Who is the target user and what problem does this solve?"
   - "What are the acceptance criteria from the product side?"

2. **Design Assets:**
   - "Are there Figma/Sketch designs available?"
   - "Are there specific animations, transitions, or micro-interactions defined?"
   - "Does the design account for Dynamic Type and accessibility?"

3. **Technical Context:**
   - "What architecture pattern does the project use?"
   - "Are there existing screens or components to reuse?"
   - "What APIs are available or need to be built?"
   - "What is the data model for this feature?"

4. **Constraints:**
   - "What is the target iOS version?"
   - "Are there performance budgets (load time, memory)?"
   - "Are there offline requirements for this feature?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before writing ANY specification, you MUST:**

1. **Clarify ambiguous requirements** - List assumptions explicitly and request confirmation.
2. **Map to iOS capabilities** - Identify which Apple frameworks and APIs are needed.
3. **Define all states** - Every screen must specify loading, loaded, empty, error, and edge case states.
4. **Include accessibility from the start** - Not as an afterthought but as a core specification element.
5. **Provide testable acceptance criteria** - Each criterion must be verifiable via unit test, UI test, or manual test.

### False-Positive Prevention

- ❌ Do NOT write vague acceptance criteria ("app should be fast," "UI should look good")
- ❌ Do NOT omit error states or edge cases from the specification
- ❌ Do NOT specify UI without accessibility requirements
- ❌ Do NOT assume API contracts -- define them explicitly or flag as TBD
- ❌ Do NOT ignore offline behavior even if not explicitly requested
- ✅ DO quantify performance requirements (e.g., "list renders 60fps with 1000 items")
- ✅ DO specify exact state transitions with triggers
- ✅ DO include data model definitions with Swift types
- ✅ DO define error handling for every network call and user action

---

### Phase 1: Requirement Decomposition

#### 1.1 Feature Breakdown

```markdown
## Feature: [Feature Name]

### User Story
As a [user type], I want to [action] so that [benefit].

### Functional Requirements
| ID | Requirement | Priority | Complexity |
|----|------------|----------|-----------|
| FR-01 | | Must/Should/Could | S/M/L |
| FR-02 | | | |

### Non-Functional Requirements
| ID | Requirement | Metric |
|----|------------|--------|
| NFR-01 | Performance | Screen loads in < 500ms |
| NFR-02 | Accessibility | VoiceOver fully navigable |
| NFR-03 | Offline | Core data available offline |

### Assumptions
| # | Assumption | Confirmed? |
|---|-----------|-----------|
| 1 | | Yes/No/TBD |
```

#### 1.2 Screen Inventory

```markdown
| Screen | Type | Navigation | New/Existing |
|--------|------|-----------|-------------|
| | List/Detail/Form/Modal | Push/Sheet/FullScreen | New/Modify |
```

---

### Phase 2: Technical Specification

**CHECKPOINT 1:** Confirm requirements decomposition before technical design.

```markdown
## Requirements Summary
- Functional requirements: _ items
- Screens affected: _
- New API endpoints needed: _
- Assumptions requiring confirmation: _

**Proceed with technical specification?**
```

#### 2.1 State Design

```swift
// Define all possible states for the feature
enum FeatureState: Equatable {
    case idle
    case loading
    case loaded(FeatureData)
    case empty
    case error(FeatureError)
}

enum FeatureError: Equatable, LocalizedError {
    case networkUnavailable
    case unauthorized
    case serverError(String)
    case decodingFailed

    var errorDescription: String? {
        switch self {
        case .networkUnavailable: "No internet connection. Please check your network."
        case .unauthorized: "Your session has expired. Please sign in again."
        case .serverError(let msg): msg
        case .decodingFailed: "Something went wrong. Please try again."
        }
    }
}
```

#### 2.2 State Transition Diagram

```markdown
[idle] --onAppear--> [loading]
[loading] --success(data)--> [loaded]
[loading] --success(empty)--> [empty]
[loading] --failure--> [error]
[error] --retry--> [loading]
[loaded] --refresh--> [loading] (keep stale data visible)
[loaded] --delete(item)--> [loaded] or [empty]
```

#### 2.3 Data Models

```swift
// Define all models with exact Swift types
struct FeatureItem: Identifiable, Codable, Equatable {
    let id: UUID
    var title: String
    var description: String
    var status: Status
    var createdAt: Date
    var updatedAt: Date

    enum Status: String, Codable, CaseIterable {
        case draft, active, archived
    }
}
```

#### 2.4 API Contract

```markdown
### GET /api/v1/features
**Request:** Query params: `page`, `limit`, `status`
**Response 200:**
```json
{
  "items": [
    {
      "id": "uuid",
      "title": "string",
      "description": "string",
      "status": "draft|active|archived",
      "created_at": "ISO8601",
      "updated_at": "ISO8601"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100
  }
}
```
**Error responses:** 401 (unauthorized), 500 (server error)
```

---

### Phase 3: UI Specification

#### 3.1 Screen Specifications

For each screen, specify:

```markdown
### Screen: [Name]

**Layout:** NavigationStack > ScrollView > VStack
**Components:**
| Component | Type | Data Source | Interaction |
|-----------|------|-----------|------------|
| Header | Text | item.title | None |
| Status badge | Capsule | item.status | None |
| Action button | Button | N/A | Tap -> confirm dialog |

**States:**
| State | Visual | Behavior |
|-------|--------|----------|
| Loading | ProgressView centered | Disable interactions |
| Loaded | Content visible | All interactions enabled |
| Empty | ContentUnavailableView | Show CTA button |
| Error | Error message + retry | Retry button enabled |

**Accessibility:**
| Element | Label | Hint | Traits |
|---------|-------|------|--------|
| Item row | "{title}, {status}" | "Double tap to view details" | .isButton |
| Delete button | "Delete {title}" | "Double tap to delete" | .isButton |
```

#### 3.2 Navigation Specification

```markdown
| Source | Trigger | Destination | Transition | Data Passed |
|--------|---------|------------|-----------|-------------|
| List | Tap row | Detail | Push | item.id |
| Detail | Tap edit | Edit form | Sheet | item |
| List | Tap + | Create form | Sheet | None |
```

---

### Phase 4: Acceptance Criteria

**CHECKPOINT 2:** Review technical design before writing acceptance criteria.

```markdown
## Technical Design Summary
- States defined: _
- API endpoints: _
- Data models: _
- Screens specified: _

**Proceed with acceptance criteria?**
```

#### 4.1 Testable Acceptance Criteria

```markdown
### Functional Criteria
| ID | Criterion | Test Method |
|----|----------|------------|
| AC-01 | Given list screen loads, when API returns items, then items display in reverse chronological order | Unit test: ViewModel sorts by date descending |
| AC-02 | Given list screen loads, when API returns empty, then empty state shows with "Add" CTA | UI test: verify ContentUnavailableView |
| AC-03 | Given network error, when user taps retry, then loading state shows and API is called again | Unit test: ViewModel state transitions |
| AC-04 | Given item deleted, when only item removed, then screen transitions to empty state | Unit test: state changes to .empty |

### Accessibility Criteria
| ID | Criterion | Test Method |
|----|----------|------------|
| AX-01 | All interactive elements have accessibilityLabel | Accessibility audit |
| AX-02 | Screen is fully navigable with VoiceOver | Manual VoiceOver test |
| AX-03 | Dynamic Type up to AX5 does not break layout | Preview with .accessibilityExtraExtraExtraLarge |

### Performance Criteria
| ID | Criterion | Test Method |
|----|----------|------------|
| PF-01 | List renders at 60fps with 500 items | Instruments > Core Animation FPS |
| PF-02 | Screen appears within 500ms of navigation | Instruments > Time Profiler |
```

---

### Phase 5: Implementation Tasks

#### 5.1 Task Breakdown

```markdown
| Task | Estimate | Dependencies | Assignee |
|------|----------|-------------|----------|
| Define data models | 1h | None | |
| Implement API client endpoint | 2h | API contract finalized | |
| Build ViewModel with state machine | 3h | Models + API client | |
| Build list screen UI | 3h | ViewModel | |
| Build detail screen UI | 2h | ViewModel | |
| Add accessibility modifiers | 1h | UI complete | |
| Write ViewModel unit tests | 2h | ViewModel | |
| Write UI snapshot tests | 1h | UI complete | |
| Manual QA: VoiceOver + Dynamic Type | 1h | All above | |
| **Total** | **~16h** | | |
```

---

## Expected Output

```
Feature Specification Document
├── Requirement Decomposition
│   ├── User story and functional requirements
│   ├── Non-functional requirements with metrics
│   └── Assumptions log
├── Technical Specification
│   ├── State enum definitions (Swift)
│   ├── State transition diagram
│   ├── Data model definitions (Swift)
│   └── API contracts (request/response)
├── UI Specification
│   ├── Per-screen component inventory
│   ├── State-to-visual mapping
│   └── Navigation flow
├── Acceptance Criteria
│   ├── Functional (testable)
│   ├── Accessibility
│   └── Performance
└── Implementation Tasks (estimated)
```

---

## Example Interaction

**User:** "We need a favorites feature. Users should be able to favorite recipes and see them in a dedicated tab. Works offline."

**Assistant:**

**State Design:**
```swift
enum FavoritesState: Equatable {
    case idle
    case loaded([Recipe])
    case empty
}
// No loading/error states needed -- data is local-only (SwiftData)
```

**Key Specification Decisions:**
1. Favorites stored locally via SwiftData `@Attribute` on Recipe model (`isFavorite: Bool`)
2. No API needed -- purely local persistence with CloudKit sync via SwiftData
3. Favorites tab uses `@Query(filter: #Predicate { $0.isFavorite })` for automatic updates
4. Offline by design -- no network dependency

**Acceptance Criteria:**
- AC-01: Tapping heart icon toggles `isFavorite` and persists across app restart
- AC-02: Favorites tab shows only favorited recipes, sorted by favorited date
- AC-03: Removing last favorite transitions to empty state with "Browse Recipes" CTA

---

## Techniques Used

- **ST-01** (Clear Objective): Transforms requirements into implementation-ready specifications
- **ST-02** (Sequential Instructions): Five-phase decomposition from requirements to tasks
- **ST-03** (Output Format Templates): Structured tables and code templates for specifications

---

## Related Prompts

- [ios_architecture_selection.md](ios_architecture_selection.md) - Architecture must be selected before specifying features
- [ios_module_design.md](ios_module_design.md) - Determine which module a feature belongs to
- [ios_project_scaffold.md](ios_project_scaffold.md) - Scaffold project structure for specified features

---

## Customization Guide

### For Design-Heavy Features
Add a "Micro-Interactions" section specifying animations with SwiftUI `.animation()`, `.transition()`, and `withAnimation` parameters, including duration, curve, and trigger.

### For API-First Features
Expand the API Contract section to include full OpenAPI/Swagger spec integration, request/response mocking strategy, and API versioning plan.

### For Features with Complex Business Logic
Add a "Business Rules" section with decision tables mapping input conditions to expected outcomes, suitable for parameterized unit testing.
