---
title: "Android Feature Specification"
category: mobile-development
description: "Produce a complete, implementation-ready specification for a single Android feature — requirements, architecture fit, data, UI states, and acceptance criteria."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-04
  - NE-02
difficulty: intermediate
tags:
  - android
  - mobile-development
  - feature-spec
  - requirements
  - acceptance-criteria
updated: "2026-06-06"
---

# Android Feature Specification

**Objective:** Transform high-level feature requirements into detailed, implementation-ready technical specifications that account for existing codebase patterns, architecture constraints, and Android platform best practices.

**When to Use:** Use this prompt when you have a feature idea or user story that needs to be translated into concrete technical specifications before implementation begins. Ideal for new features in existing apps, significant enhancements, or when onboarding new team members to understand feature scope. The output serves as a contract between planning and implementation.

**Sequence Map:** Use after architecture/module decisions; use before implementation and scaffolding execution for the feature.

**Prompt Type:** Comprehensive (300-400 lines)

---

## Context Gathering

Before beginning the specification process, gather essential context:

1. **Feature Overview:**
   - "What is the feature you want to build? Please describe it from a user's perspective."
   - "What problem does this feature solve for users?"

2. **Existing Codebase:**
   - "Is this for an existing app or a new project?"
   - "If existing, what is the current architecture pattern (MVVM, MVI, Clean Architecture)?"

3. **Constraints:**
   - "Are there any technical constraints (minimum API level, offline requirements, specific libraries to use/avoid)?"
   - "Are there time or resource constraints that should influence scope?"

4. **Dependencies:**
   - "Does this feature depend on or integrate with existing features?"
   - "Are there backend APIs already available, or do those need to be designed too?"

5. **Success Criteria:**
   - "How will you measure if this feature is successful?"
   - "Are there specific acceptance criteria already defined?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before specifying ANY feature, you MUST:**

1. **Trace actual requirements** - Don't over-specify beyond what's actually needed.
2. **Check for existing patterns** - Search for how similar features are implemented in the codebase.
3. **Understand the context** - Consider the existing architecture, team conventions, and time constraints.
4. **Confirm actual scope** - Is the specification appropriate for the feature complexity?
5. **Provide specific locations** - Every component must include exact file paths and interfaces.

**A SIMPLER specification is often better.** Don't over-engineer specifications for straightforward features.

### False-Positive Prevention

- ❌ Do NOT over-specify simple features with unnecessary complexity
- ❌ Do NOT ignore existing codebase patterns
- ❌ Do NOT recommend architecture changes for single features
- ❌ Do NOT leave ambiguity in critical specifications
- ✅ DO match specification detail to feature complexity
- ✅ DO follow existing project conventions
- ✅ DO include clear acceptance criteria
- ✅ DO consider edge cases and error scenarios

---

### Phase 1: Requirements Analysis

#### 1.1 Feature Decomposition

Break down the high-level feature into discrete user stories and use cases:

```markdown
## User Stories

### Primary Stories (Must Have)
- As a [user type], I want to [action] so that [benefit]
- ...

### Secondary Stories (Should Have)
- ...

### Nice to Have (Could Have)
- ...

## Use Cases

### UC-01: [Use Case Name]
- **Actor:** [Who initiates]
- **Preconditions:** [What must be true before]
- **Main Flow:**
  1. [Step 1]
  2. [Step 2]
  ...
- **Alternate Flows:**
  - [Variation description]
- **Postconditions:** [What is true after]
- **Error Conditions:**
  - [What can go wrong and how to handle]
```

#### 1.2 Existing Codebase Analysis

If adding to an existing codebase, analyze:

**Architecture Patterns:**
- Current architecture pattern in use
- Existing UI patterns (Compose, Views, or hybrid)
- State management approach (StateFlow, LiveData, MVI)
- Navigation structure
- Dependency injection setup

**Related Components:**
- Existing screens/features this touches
- Shared components that can be reused
- Data models that need extension
- APIs already integrated

**Code Conventions:**
- Naming patterns for classes, packages, files
- Module structure
- Test organization

#### 1.3 Platform Requirements

Identify Android-specific requirements:

```markdown
## Platform Considerations

### API Level Compatibility
- Minimum SDK: [X]
- Target SDK: [Y]
- Features requiring compat libraries: [list]

### Permissions Required
- [Permission] - [Why needed]

### Hardware/Sensor Requirements
- [Requirement if any]

### Screen Support
- Phone portrait: [Required/Optional]
- Phone landscape: [Required/Optional]
- Tablet: [Required/Optional]
- Foldables: [Required/Optional]

### Accessibility Requirements
- Content descriptions
- Screen reader navigation
- Touch target sizes
- Color contrast requirements
```

---

### Phase 2: Technical Specification

#### 2.1 Component Design

**CHECKPOINT 1:** Present the requirements analysis to the user before proceeding with technical design.

```markdown
## Requirements Summary

I've analyzed the feature requirements. Here's what I understand:

### Core Functionality
[Summary of what the feature does]

### User Journeys
[Key user flows identified]

### Scope Boundaries
- **In Scope:** [What's included]
- **Out of Scope:** [What's explicitly excluded]
- **Assumptions:** [What we're assuming]

### Questions Before Technical Design
1. [Clarification question]
2. [Scope question]

**Does this accurately capture the feature requirements?**
```

After confirmation, proceed with technical specification:

#### 2.2 Architecture Design

```markdown
## Architecture Specification

### Layer Breakdown

#### UI Layer
| Component | Type | Responsibility |
|-----------|------|----------------|
| [ScreenName]Screen | Composable | [What it displays/handles] |
| [ScreenName]ViewModel | ViewModel | [State management responsibilities] |
| [Name]UiState | Data Class | [UI state representation] |

#### Domain Layer (if using Clean Architecture)
| Component | Type | Responsibility |
|-----------|------|----------------|
| [Name]UseCase | Use Case | [Business logic encapsulated] |
| [Name]Repository | Interface | [Data operations contract] |

#### Data Layer
| Component | Type | Responsibility |
|-----------|------|----------------|
| [Name]RepositoryImpl | Repository | [Data coordination] |
| [Name]LocalDataSource | Data Source | [Local storage operations] |
| [Name]RemoteDataSource | Data Source | [API operations] |
| [Name]Entity | Entity | [Database model] |
| [Name]Dto | DTO | [API response model] |
| [Name]Mapper | Mapper | [Model transformations] |

### Data Flow Diagram

```
User Action
    ↓
[Screen] → [ViewModel] → [UseCase] → [Repository]
                                          ↓
                              [LocalDataSource] ←→ [RemoteDataSource]
                                          ↓
                                      [Database/API]
```

### State Management

```kotlin
// UI State Definition
data class FeatureUiState(
    val isLoading: Boolean = false,
    val data: List<Item> = emptyList(),
    val error: ErrorState? = null,
    val userInput: UserInput = UserInput()
)

sealed interface FeatureEvent {
    data class OnItemClick(val itemId: String) : FeatureEvent
    data class OnInputChange(val value: String) : FeatureEvent
    data object OnRefresh : FeatureEvent
    data object OnRetry : FeatureEvent
}

sealed interface FeatureSideEffect {
    data class NavigateTo(val route: String) : FeatureSideEffect
    data class ShowSnackbar(val message: String) : FeatureSideEffect
}
```
```

#### 2.3 Data Model Design

```markdown
## Data Models

### Domain Models
```kotlin
data class [DomainModel](
    val id: String,
    val field1: Type,
    val field2: Type,
    // ... all fields with types
)
```

### Database Entities (if local storage needed)
```kotlin
@Entity(tableName = "table_name")
data class [EntityName](
    @PrimaryKey val id: String,
    @ColumnInfo(name = "field_name") val field: Type,
    // ... all fields
)
```

### API DTOs (if network calls needed)
```kotlin
@Serializable
data class DtoName val field: Type,
    // ... all fields
)
```

### Model Relationships
[Diagram or description of how models relate]
```

#### 2.4 API Specification (if applicable)

```markdown
## API Specification

### Endpoints Required

| Method | Endpoint | Purpose | Request | Response |
|--------|----------|---------|---------|----------|
| GET | /api/v1/resource | Fetch items | Query params | List<ItemDto> |
| POST | /api/v1/resource | Create item | CreateRequest | ItemDto |
| PUT | /api/v1/resource/{id} | Update item | UpdateRequest | ItemDto |
| DELETE | /api/v1/resource/{id} | Delete item | - | 204 No Content |

### Request/Response Models

```kotlin
// Request
@Serializable
data class CreateResourceRequest(
    val field1: String,
    val field2: Int
)

// Response
@Serializable
data class ResourceResponse(
    val id: String,
    val field1: String,
    val createdAt: String
)
```

### Error Handling
| HTTP Status | Meaning | UI Behavior |
|-------------|---------|-------------|
| 400 | Bad Request | Show validation error |
| 401 | Unauthorized | Redirect to login |
| 404 | Not Found | Show not found state |
| 500 | Server Error | Show retry option |
```

#### 2.5 UI/UX Specification

```markdown
## UI Specification

### Screen Inventory

| Screen | Route | Entry Points | Exit Points |
|--------|-------|--------------|-------------|
| [ScreenName] | feature/main | Home, Deep link | Back, Item detail |

### Screen States

For each screen, define:

#### [ScreenName] States
| State | Condition | UI Display |
|-------|-----------|------------|
| Loading | Initial load | Shimmer/skeleton |
| Empty | No data | Empty state illustration + CTA |
| Content | Data available | Main content |
| Error | Load failed | Error message + retry |
| Partial Error | Some data, refresh failed | Content + error snackbar |

### Component Breakdown

```
[ScreenName]Screen
├── TopAppBar
│   ├── Navigation icon
│   ├── Title
│   └── Action buttons
├── Content
│   ├── FilterSection (if applicable)
│   ├── ListContent
│   │   └── ItemCard (repeated)
│   └── EmptyState (conditional)
├── FloatingActionButton (if applicable)
└── BottomBar (if applicable)
```

### Navigation Flows

```
[Entry Point] → FeatureScreen → DetailScreen → EditScreen
                     ↓                ↓
              SettingsScreen    ShareSheet
```

### Animations & Transitions
- Screen transitions: [Shared element / Fade / Slide]
- List animations: [Item animations]
- State transitions: [How states animate between each other]
```

---

### Phase 3: Implementation Plan

**CHECKPOINT 2:** Present the technical specification for review.

```markdown
## Technical Specification Summary

### Components to Create
- **New Files:** [count]
- **Modified Files:** [count]
- **New Dependencies:** [list any]

### Architecture Diagram
[Visual representation of components and relationships]

### Key Technical Decisions
1. [Decision] - [Rationale]
2. [Decision] - [Rationale]

### Questions/Concerns
1. [Any architectural concerns]
2. [Any scope concerns]

**Does this technical approach look correct? Any concerns before I create the implementation plan?**
```

#### 3.1 Implementation Breakdown

```markdown
## Implementation Tasks

### Phase 1: Foundation (Data Layer)
| Task | Files | Effort | Dependencies |
|------|-------|--------|--------------|
| Create data models | [files] | [S/M/L] | None |
| Implement database entities and DAO | [files] | [S/M/L] | Models |
| Create API service interface | [files] | [S/M/L] | DTOs |
| Implement repository | [files] | [S/M/L] | DAO, API |

### Phase 2: Business Logic (Domain Layer)
| Task | Files | Effort | Dependencies |
|------|-------|--------|--------------|
| Create use cases | [files] | [S/M/L] | Repository |
| Implement mappers | [files] | [S/M/L] | Models |

### Phase 3: UI Implementation
| Task | Files | Effort | Dependencies |
|------|-------|--------|--------------|
| Create ViewModel | [files] | [S/M/L] | Use cases |
| Implement main screen | [files] | [S/M/L] | ViewModel |
| Implement sub-screens | [files] | [S/M/L] | ViewModel |
| Add navigation | [files] | [S/M/L] | Screens |

### Phase 4: Polish & Integration
| Task | Files | Effort | Dependencies |
|------|-------|--------|--------------|
| Error handling | [files] | [S/M/L] | All |
| Loading states | [files] | [S/M/L] | Screens |
| Accessibility | [files] | [S/M/L] | Screens |
| Analytics integration | [files] | [S/M/L] | Events defined |

### Phase 5: Testing
| Task | Files | Effort | Dependencies |
|------|-------|--------|--------------|
| Unit tests for use cases | [files] | [S/M/L] | Use cases |
| ViewModel tests | [files] | [S/M/L] | ViewModel |
| UI tests | [files] | [S/M/L] | Screens |
| Integration tests | [files] | [S/M/L] | All |
```

#### 3.2 Dependency Requirements

```markdown
## Dependencies

### New Dependencies Required
| Library | Version | Purpose |
|---------|---------|---------|
| [library] | [version] | [why needed] |

### Existing Dependencies to Leverage
| Library | Current Version | How Used |
|---------|-----------------|----------|
| [library] | [version] | [usage] |

### Version Compatibility Notes
- [Any compatibility concerns]
```

#### 3.3 Risk Assessment

```markdown
## Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Technical risk] | [H/M/L] | [H/M/L] | [How to mitigate] |
| [Scope risk] | [H/M/L] | [H/M/L] | [How to mitigate] |
| [Integration risk] | [H/M/L] | [H/M/L] | [How to mitigate] |

## Open Questions
1. [Question needing answer before/during implementation]
2. [Question needing answer before/during implementation]
```

---

### Phase 4: Final Specification Document

**CHECKPOINT 3:** Present complete specification for approval.

Compile all sections into a comprehensive specification document that can be used as the implementation guide.

---

## Expected Output

### Specification Document Structure

```markdown
# Feature Specification: [Feature Name]

## 1. Overview
- Feature summary
- User stories
- Success criteria

## 2. Requirements
- Functional requirements
- Non-functional requirements
- Platform requirements

## 3. Technical Design
- Architecture components
- Data models
- API specification
- State management

## 4. UI/UX Design
- Screen inventory
- Component breakdown
- Navigation flows
- States and transitions

## 5. Implementation Plan
- Task breakdown
- Dependencies
- Risks

## 6. Testing Strategy
- Unit test coverage
- Integration test scenarios
- UI test cases

## 7. Appendix
- Glossary
- References
- Open questions
```

---

## Example Interaction

**User:** I want to add a favorites feature to my recipe app. Users should be able to save recipes they like and view them in a dedicated favorites screen.

**Agent:** I'll help you create a detailed specification for a favorites feature. Let me gather some context first.

1. What is the current architecture of your recipe app? (MVVM, MVI, Clean Architecture?)
2. How are recipes currently stored - local database, remote API, or both?

**User:** We use MVVM with Room for local storage. Recipes come from a REST API but are cached locally.

**Agent:** Great, that helps. A few more questions:

3. Should favorites sync across devices (requires backend support) or be device-local only?
4. Are there any existing patterns for "save" functionality I should follow?

**User:** Device-local only for now. We have a similar "bookmarks" feature for articles that you can reference.

**Agent:**

## Requirements Summary

I've analyzed the favorites feature requirements. Here's what I understand:

### Core Functionality
Users can mark recipes as favorites, which persists locally. A dedicated favorites screen displays all favorited recipes with the ability to unfavorite them.

### User Journeys
1. **Add to Favorites:** User viewing recipe → taps heart icon → recipe saved to favorites
2. **View Favorites:** User navigates to Favorites tab → sees grid of favorited recipes → taps to view details
3. **Remove from Favorites:** User taps filled heart on favorited recipe → recipe removed from favorites

### Scope Boundaries
- **In Scope:** Local favorites storage, favorites list screen, favorite/unfavorite action on recipe cards and detail screen
- **Out of Scope:** Cloud sync, folders/categories for favorites, sharing favorites
- **Assumptions:** Following existing bookmarks pattern, using Room for storage

### Questions Before Technical Design
1. Should we show a confirmation when removing from favorites, or immediately remove?
2. How should favorites be sorted - by date added, alphabetically, or user-customizable?

**Does this accurately capture the feature requirements?**

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective defining feature specification
- **ST-02** (Sequential Instructions): Phased approach from requirements to implementation
- **RT-02** (Multi-Dimensional Analysis): Coverage of architecture, data, UI, and testing
- **RT-04** (Best Practice Review): Android architecture patterns and conventions
- **ST-03** (Output Format Templates): Structured specification document format
- **NE-01** (Single-Question Pacing): Context gathering before analysis
- **NE-02** (Phased Workflow): Clear phases with checkpoint approvals
- **NE-07** (Discussion Before Action): Checkpoints for user feedback

---

## Related Prompts

- [android_architecture_selection.md](android_architecture_selection.md) - Select architecture pattern before feature design
- [android_module_design.md](android_module_design.md) - Design module structure for large features
- [android_data_layer_implementation.md](../implementation/android_data_layer_implementation.md) - Implement the data layer from spec
- [android_compose_screen_builder.md](../implementation/android_compose_screen_builder.md) - Build screens from UI spec
- [android_test_strategy_design.md](../testing/android_test_strategy_design.md) - Design test strategy for the feature

---

## Customization Guide

### For Different Feature Sizes

**Small Feature (1-2 screens):**
- Simplify architecture section to just ViewModel + Repository
- Combine implementation phases
- Focus on component-level rather than layer-level design

**Large Feature (5+ screens, new module):**
- Expand architecture to include module boundaries
- Add cross-module communication design
- Include migration/rollout strategy if replacing existing functionality

**Platform Feature (permissions, hardware):**
- Expand platform requirements section
- Add permission request flow specification
- Include fallback behavior for denied permissions

### For Different Team Contexts

**Solo Developer:**
- Focus on implementation sequence
- Reduce ceremony around documentation
- Emphasize quick iteration paths

**Team Environment:**
- Include more detailed interface contracts
- Add code review checkpoints
- Include PR/branch strategy

### Adjusting for Technical Debt

**Greenfield Context:**
- Full architecture design freedom
- Establish patterns for future features

**Legacy Context:**
- Analyze existing patterns more thoroughly
- Include migration/compatibility considerations
- Plan for incremental improvement
