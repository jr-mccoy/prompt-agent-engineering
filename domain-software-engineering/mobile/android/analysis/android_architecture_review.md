---
title: "Android Architecture Review"
category: mobile-development
description: "Analyzes Android app architecture evaluating pattern implementation, layer boundaries, and dependency flow with modernization recommendations"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: advanced
tags:
  - android
  - mobile-development
  - review
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_codebase_health_assessment.md
  - domain-software-engineering/mobile/android/analysis/android_module_graph_analysis.md
  - domain-software-engineering/mobile/android/analysis/android_technical_debt_assessment.md
  - domain-software-engineering/mobile/android/planning/android_modularization_strategy.md
---


# Android Architecture Review

**Objective:** Conduct a deep analysis of an Android app's architecture, evaluating pattern implementation, layer boundaries, dependency flow, state management, and navigation to provide modernization recommendations.

**When to Use:** Use this prompt when you need to understand how an Android app is structured architecturally, identify architectural issues, evaluate adherence to best practices, or plan architectural improvements. Ideal after a codebase health assessment reveals architecture concerns, before major feature additions, or when onboarding to understand how the app is organized.

**Prompt Type:** Comprehensive (350-450 lines)

---

## Context Gathering

Before beginning the architecture review, gather context:

1. **Architecture Intent:**
   - "What architecture pattern was this app designed to follow (MVVM, MVI, MVP, Clean Architecture, or unknown)?"
   - "Are there any architecture documentation or ADRs (Architecture Decision Records) I should be aware of?"

2. **Known Issues:**
   - "Are there specific architectural concerns you've encountered (e.g., hard to test, tangled dependencies, unclear responsibilities)?"

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
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `HomeViewModel.kt:34`).

**Finding the architecture ADEQUATE is an acceptable outcome.** If the codebase follows reasonable patterns for its context, say so with confidence. Don't manufacture architectural concerns.

### False-Positive Prevention

- ❌ Do NOT flag all deviations from "pure" architecture patterns as problems
- ❌ Do NOT flag pragmatic shortcuts that work well for the project
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

```kotlin
// MVVM Indicators
- ViewModel classes extending androidx.lifecycle.ViewModel
- LiveData or StateFlow exposing UI state
- View/Fragment/Activity observing ViewModel state
- No business logic in UI components

// MVI Indicators
- Sealed classes for Intent/Action/Event
- Sealed classes for State
- Reducer functions processing intents to state
- Unidirectional data flow patterns

// MVP Indicators
- Presenter classes
- View interfaces (Contract interfaces)
- Presenter holding view reference

// Clean Architecture Indicators
- UseCase or Interactor classes
- Separate modules for domain, data, presentation
- Dependency rule: outer layers depend on inner layers
- Domain entities without Android dependencies

// Repository Pattern Indicators
- Repository interfaces and implementations
- Data source abstractions (LocalDataSource, RemoteDataSource)
- Model mapping between layers
```

**Pattern Detection Checklist:**

| Pattern | Key Indicators | Consistency |
|---------|---------------|-------------|
| MVVM | ViewModel, StateFlow/LiveData, UI observing state | [Consistent/Partial/Inconsistent] |
| MVI | Intent sealed class, Reducer, Side effects | [Consistent/Partial/Inconsistent] |
| MVP | Presenter, Contract interface, View reference | [Consistent/Partial/Inconsistent] |
| Clean | UseCase, Domain module, Dependency rule | [Consistent/Partial/Inconsistent] |
| Repository | Repository interface, DataSource abstraction | [Consistent/Partial/Inconsistent] |

#### 1.2 Module Structure Analysis

**Examine project modules:**

```
// Single Module Structure
app/
└── src/main/kotlin/com/example/app/
    ├── ui/
    ├── data/
    ├── domain/
    └── di/

// Multi-Module Structure (Feature-based)
:app
:core:common
:core:network
:core:database
:feature:home
:feature:profile
:feature:settings

// Multi-Module Structure (Layer-based)
:app
:presentation
:domain
:data
```

**Evaluate:**
- Module organization strategy (by feature, by layer, hybrid)
- Module dependency graph
- API boundaries between modules
- Build performance impact of module structure

#### 1.3 Package Structure Analysis

**Examine package organization:**

```kotlin
// Package by Layer
com.example.app/
├── activities/
├── fragments/
├── viewmodels/
├── repositories/
├── models/
└── utils/

// Package by Feature
com.example.app/
├── home/
│   ├── HomeFragment.kt
│   ├── HomeViewModel.kt
│   └── HomeRepository.kt
├── profile/
│   ├── ProfileFragment.kt
│   └── ProfileViewModel.kt
└── core/
    ├── network/
    └── database/

// Clean Architecture Packages
com.example.app/
├── presentation/
│   └── features/
├── domain/
│   ├── model/
│   ├── repository/
│   └── usecase/
└── data/
    ├── repository/
    ├── local/
    └── remote/
```

---

### Phase 2: Layer Analysis

#### 2.1 UI Layer Assessment

**Components to examine:**

```kotlin
// Activities/Fragments
- Lifecycle handling
- Configuration change handling
- Navigation responsibility
- Business logic presence (should be minimal)

// Composables (if using Compose)
- State hoisting patterns
- Recomposition optimization
- Side effect handling (LaunchedEffect, etc.)
- Preview functions presence

// ViewModels
- State exposure pattern (StateFlow, LiveData)
- Input handling (events, actions)
- Business logic location
- Lifecycle awareness
- SavedStateHandle usage
```

**UI Layer Evaluation Criteria:**

| Criterion | Good Practice | Anti-Pattern |
|-----------|--------------|--------------|
| **Responsibility** | Display state, capture user input | Business logic, data fetching directly |
| **State** | Observes ViewModel state | Manages own complex state |
| **Navigation** | Delegates to navigator/ViewModel | Contains navigation logic |
| **Lifecycle** | Minimal lifecycle code | Heavy lifecycle management |

#### 2.2 Domain Layer Assessment

**Components to examine:**

```kotlin
// Use Cases / Interactors
- Single responsibility per use case
- No Android dependencies
- Business rule encapsulation
- Proper naming (verb-based: GetUserUseCase, ValidateEmailUseCase)

// Domain Models
- Pure Kotlin data classes
- No framework annotations
- Business validation methods

// Repository Interfaces
- Defined in domain layer
- No implementation details leaked
- Proper abstraction level
```

**Domain Layer Evaluation:**

| Criterion | Status | Notes |
|-----------|--------|-------|
| Layer exists | [Yes/No/Partial] | [Details] |
| Android-free | [Yes/No] | [Android dependencies found] |
| Use cases present | [Yes/No/Partial] | [Count and quality] |
| Repository interfaces | [Yes/No] | [Location] |

#### 2.3 Data Layer Assessment

**Components to examine:**

```kotlin
// Repository Implementations
- Interface implementation
- Data source coordination
- Caching strategy
- Error handling

// Data Sources
- Local: Room DAOs, SharedPreferences/DataStore
- Remote: Retrofit services, API clients
- Clear separation between sources

// Data Models
- DTOs for network responses
- Entities for database
- Mappers to domain models
```

**Data Layer Evaluation:**

| Criterion | Status | Notes |
|-----------|--------|-------|
| Repository pattern | [Implemented/Partial/Missing] | [Quality assessment] |
| Local data source | [Present/Absent] | [Implementation] |
| Remote data source | [Present/Absent] | [Implementation] |
| Model mapping | [Yes/No] | [Approach used] |
| Single source of truth | [Yes/No] | [Strategy] |

---

### Phase 3: Dependency Analysis

#### 3.1 Dependency Direction Check

**Correct Dependency Flow:**
```
UI Layer → Domain Layer → Data Layer
    ↓              ↓            ↓
  Views      Use Cases    Repositories
ViewModels    Models     Data Sources
```

**Violations to Search For:**

```kotlin
// Domain layer importing Android classes
import android.content.Context  // VIOLATION in domain

// UI layer directly accessing data layer
class HomeFragment {
    @Inject lateinit var userDao: UserDao  // VIOLATION
}

// Data layer depending on UI models
class UserRepository {
    fun getUser(): UserUiModel  // VIOLATION - should return domain model
}
```

#### 3.2 Dependency Injection Analysis

**DI Framework Detection:**

```kotlin
// Hilt indicators
@HiltAndroidApp
@AndroidEntryPoint
@Inject constructor
@Module @InstallIn

// Dagger indicators
@Component
@Subcomponent
@Module @Provides

// Koin indicators
startKoin { }
modules(appModule)
by inject()

// Manual DI
class AppContainer { }
ServiceLocator pattern
```

**DI Quality Evaluation:**

| Aspect | Assessment | Issues |
|--------|------------|--------|
| Framework | [Hilt/Dagger/Koin/Manual/None] | [Version, configuration] |
| Scope usage | [Appropriate/Over-scoped/Under-scoped] | [Specific issues] |
| Module organization | [Clean/Messy] | [Details] |
| Interface binding | [Good/Partial/Missing] | [Concrete dependencies] |

---

### Phase 4: State Management Review

#### 4.1 State Holder Patterns

**Identify state management approach:**

```kotlin
// StateFlow Pattern (Recommended)
class MyViewModel : ViewModel() {
    private val _uiState = MutableStateFlow(UiState())
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()
}

// LiveData Pattern (Legacy but valid)
class MyViewModel : ViewModel() {
    private val _uiState = MutableLiveData<UiState>()
    val uiState: LiveData<UiState> = _uiState
}

// Compose State Pattern
@Composable
fun MyScreen(viewModel: MyViewModel) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
}
```

#### 4.2 UI State Modeling

**Evaluate state model design:**

```kotlin
// Good: Sealed class for exclusive states
sealed class UiState {
    object Loading : UiState()
    data class Success(val data: Data) : UiState()
    data class Error(val message: String) : UiState()
}

// Good: Data class for composable state
data class ProfileUiState(
    val isLoading: Boolean = false,
    val user: User? = null,
    val error: String? = null
)

// Anti-pattern: Multiple independent flags
class BadViewModel {
    val isLoading = MutableStateFlow(false)
    val error = MutableStateFlow<String?>(null)
    val data = MutableStateFlow<Data?>(null)
    // Can have inconsistent states!
}
```

#### 4.3 Side Effects Handling

**Check for proper side effect patterns:**

```kotlin
// Events/One-time actions
sealed class UiEvent {
    data class ShowSnackbar(val message: String) : UiEvent()
    data class Navigate(val route: String) : UiEvent()
}

// Channel for one-time events (recommended)
private val _events = Channel<UiEvent>()
val events = _events.receiveAsFlow()

// SharedFlow for events
private val _events = MutableSharedFlow<UiEvent>()
val events = _events.asSharedFlow()
```

---

### Phase 5: Navigation Architecture

#### 5.1 Navigation Pattern Identification

**Identify navigation approach:**

```kotlin
// Navigation Component (XML)
- NavHostFragment in layout
- nav_graph.xml files
- SafeArgs for type-safe arguments

// Navigation Component (Compose)
- NavHost composable
- rememberNavController()
- composable("route") destinations

// Custom Navigation
- Manual fragment transactions
- startActivity() calls
- Custom router/coordinator patterns
```

#### 5.2 Navigation Quality Assessment

| Aspect | Assessment | Notes |
|--------|------------|-------|
| Approach | [NavComponent/Compose/Custom/Mixed] | |
| Type safety | [SafeArgs/Routes/Loose] | |
| Deep linking | [Supported/Partial/None] | |
| Back stack | [Proper/Issues] | |
| Single Activity | [Yes/No/Hybrid] | |

---

### Phase 6: Findings Presentation

**CHECKPOINT:** Present architecture findings summary.

```markdown
## Architecture Review Summary

### Pattern Assessment

**Primary Pattern:** [MVVM/MVI/MVP/Clean/Hybrid/Unclear]
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

### Architecture Profile
- **Pattern:** [Identified pattern with confidence level]
- **Modularization:** [Single/Multi-module, strategy]
- **Navigation:** [Approach used]
- **DI:** [Framework and quality]

---

## Detailed Findings

### 1. Pattern Implementation

#### Identified: [Pattern Name]

**Evidence:**
```kotlin
// Example code showing pattern implementation
[Code snippet from actual codebase]
```

**Consistency Analysis:**

| Component Type | Follows Pattern | Deviations |
|----------------|-----------------|------------|
| ViewModels | [X/Y] | [List deviations] |
| Repositories | [X/Y] | [List deviations] |
| Use Cases | [X/Y or N/A] | [List deviations] |

**Pattern Issues:**

| Issue | Severity | Location | Recommendation |
|-------|----------|----------|----------------|
| [Issue] | [Critical/High/Medium/Low] | [file:line] | [Fix] |

---

### 2. Layer Boundary Analysis

#### UI Layer

**Strengths:**
- [Strength with example]

**Violations:**

| Violation | File | Line | Fix |
|-----------|------|------|-----|
| Business logic in Fragment | [file] | [line] | Move to ViewModel |
| Direct data access | [file] | [line] | Use repository |

#### Domain Layer

**Status:** [Present/Partial/Absent]

**Assessment:**
[Detailed assessment of domain layer]

#### Data Layer

**Repository Analysis:**

| Repository | Interface | Implementation | Quality |
|------------|-----------|----------------|---------|
| UserRepository | [Yes/No] | [Details] | [1-10] |

---

### 3. Dependency Flow

**Dependency Graph:**
```
[Module/Package dependency visualization]
```

**Violations Found:**

| From | To | Type | Severity |
|------|-------|------|----------|
| [Source] | [Target] | [Import/Inheritance] | [Severity] |

---

### 4. State Management

**Current Approach:** [StateFlow/LiveData/Mixed]

**State Model Quality:**

| ViewModel | State Type | Issues |
|-----------|------------|--------|
| [ViewModel] | [Sealed/Data/Flags] | [Issues] |

**Recommendations:**
- [State management improvement]

---

### 5. Navigation

**Current Setup:**
- Framework: [Navigation Component/Custom/Mixed]
- Pattern: [Single Activity/Multi Activity]
- Type Safety: [SafeArgs/Loose typing]

**Issues:**

| Issue | Location | Impact | Fix |
|-------|----------|--------|-----|
| [Issue] | [Where] | [Impact] | [Solution] |

---

## Modernization Recommendations

### Priority 1: Critical Fixes

| Fix | Current | Target | Effort | Impact |
|-----|---------|--------|--------|--------|
| [Fix] | [Current state] | [Target state] | [Hours/Days] | [High/Medium] |

### Priority 2: Architecture Improvements

| Improvement | Rationale | Approach |
|-------------|-----------|----------|
| [Improvement] | [Why] | [How] |

### Priority 3: Modernization Opportunities

| Opportunity | Benefit | Complexity |
|-------------|---------|------------|
| Migrate to MVI | Better testability, predictable state | Medium |
| Add domain layer | Clearer business logic, testability | Medium-High |
| Modularize | Build speed, code isolation | High |

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

---

## Questions for Discussion

1. Are there constraints that limit architectural changes?
2. Is the team familiar with [recommended pattern]?
3. What's the appetite for breaking changes vs incremental improvement?
```

---

## Severity Ratings

Use these severity levels for issues:

- **Critical**: Architecture violations causing bugs, crashes, or severe maintainability issues
- **High**: Significant deviations that impact testability or developer productivity
- **Medium**: Improvement opportunities that would enhance code quality
- **Low**: Minor suggestions and polish items

---

## Expected Output

1. **Pattern Assessment** - Clear identification of architecture pattern(s) with confidence level
2. **Layer Analysis** - Detailed evaluation of each architectural layer
3. **Violation Report** - All dependency and pattern violations with locations
4. **State Management Review** - Assessment of current state handling
5. **Navigation Analysis** - Navigation architecture evaluation
6. **Modernization Roadmap** - Prioritized improvement recommendations

---

## Techniques Used

- **ST-01** (Clear Objective): Focused architecture analysis objective
- **ST-02** (Sequential Instructions): Phased discovery and analysis process
- **RT-02** (Multi-Dimensional Analysis): Five-dimension architecture evaluation
- **RT-04** (Best Practice Review): Android architecture best practices
- **RT-05** (Evidence-Based Reasoning): Code examples and file references
- **ST-03** (Output Format Templates): Structured report with tables
- **OC-05** (Severity Classification): Critical/High/Medium/Low ratings
- **NE-02** (Phased Workflow): Clear checkpoints between analysis phases
- **NE-07** (Discussion Before Action): User approval before recommendations

---

## Related Prompts

- [android_codebase_health_assessment.md](android_codebase_health_assessment.md) - Broader codebase evaluation
- [android_code_modernization.md](../improvement/android_code_modernization.md) - Implement modernization
- [android_technical_debt_assessment.md](android_technical_debt_assessment.md) - Debt cataloging
- [android_kotlin_best_practices.md](android_kotlin_best_practices.md) - Kotlin patterns review

---

## Customization Guide

### For Compose-First Apps
- Emphasize Compose state patterns
- Check for proper `remember` and `derivedStateOf` usage
- Analyze composition local usage
- Review Compose navigation patterns

### For Legacy Apps
- Focus on migration paths
- Identify quick wins vs major refactors
- Consider incremental modernization
- Check for deprecated pattern usage

### For Multi-Module Apps
- Add module dependency analysis
- Check API surface exposure
- Evaluate build configuration
- Assess inter-module communication

### For Apps Planning Major Features
- Evaluate architecture extensibility
- Check for patterns that scale
- Identify bottlenecks for feature addition
- Recommend preparation steps
