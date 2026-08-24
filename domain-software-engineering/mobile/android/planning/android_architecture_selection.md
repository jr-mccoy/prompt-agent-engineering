---
title: "Android Architecture Selection"
category: mobile-development
description: "Recommend an Android architecture pattern (MVVM, MVI, Clean, or hybrid) matched to project, team, and constraints, with an implementation blueprint and migration path."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - RT-04
  - NE-07
difficulty: intermediate
tags:
  - android
  - mobile-development
  - architecture
  - mvvm
  - mvi
  - clean-architecture
updated: "2026-06-06"
---

# Android Architecture Selection

**Objective:** Guide the selection of an appropriate architecture pattern for an Android application by analyzing project requirements, team context, and technical constraints to recommend the optimal architectural approach with implementation guidance.

**When to Use:** Use this prompt when starting a new Android project, planning a major refactor of an existing app's architecture, or when evaluating whether your current architecture suits your evolving needs. Ideal for teams debating between MVVM, MVI, Clean Architecture, or hybrid approaches. Best used early in project planning before significant implementation begins.

**Sequence Map:** Use after concept validation; use before module design and tech stack selection.

**Prompt Type:** Comprehensive (350-450 lines)

---

## Context Gathering

Before recommending an architecture, gather comprehensive context:

1. **Project Overview:**
   - "What type of app are you building? (consumer, enterprise, SDK, utility, game)"
   - "What is the expected complexity? (simple CRUD, complex business logic, real-time features)"
   - "What is the expected scale? (number of screens, features, modules)"

2. **Team Context:**
   - "What is your team size and experience level with Android development?"
   - "Does your team have experience with any specific architecture patterns?"
   - "Are there iOS/web counterparts that share architecture patterns?"

3. **Technical Requirements:**
   - "What are your primary technical concerns? (testability, offline support, real-time updates, performance)"
   - "What is your testing strategy? (heavy unit testing, integration testing, minimal testing)"
   - "Do you need to support complex state management or multi-step workflows?"

4. **Constraints:**
   - "Are there existing architectural decisions or legacy code to consider?"
   - "Are there organizational standards or requirements to follow?"
   - "What is your timeline and can you invest in architectural foundation?"

5. **Existing Codebase (if applicable):**
   - "If this is a refactor, what patterns currently exist in the codebase?"
   - "What are the pain points with the current architecture?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY architecture, you MUST:**

1. **Trace actual project needs** - Don't recommend complex architectures for simple apps.
2. **Check for existing patterns** - Search for current architectural decisions if this is an existing codebase.
3. **Understand the context** - Consider team experience, project size, and timeline.
4. **Confirm actual benefit** - Will this architecture provide meaningful advantages for this specific project?
5. **Provide specific guidance** - Every recommendation must include implementation details.

**Recommending SIMPLER architecture is often better.** Don't over-architect small projects.

### False-Positive Prevention

- ❌ Do NOT recommend Clean Architecture for simple apps
- ❌ Do NOT assume every project needs full MVI
- ❌ Do NOT ignore team experience when recommending complex patterns
- ❌ Do NOT recommend architecture changes without migration plan
- ✅ DO consider the team's ability to maintain the chosen architecture
- ✅ DO match architecture complexity to project complexity
- ✅ DO provide concrete implementation examples
- ✅ DO consider gradual adoption paths for complex architectures

---

### Phase 1: Architecture Pattern Analysis

#### 1.1 Pattern Overview

Present an overview of the main Android architecture patterns:

```markdown
## Android Architecture Patterns Comparison

### MVVM (Model-View-ViewModel)
**Overview:** Separates UI (View) from business logic (ViewModel) with observable data patterns.

**Key Characteristics:**
- ViewModel exposes UI state via observable streams (StateFlow, LiveData)
- View observes state and renders accordingly
- Unidirectional data flow (View → ViewModel → Model → ViewModel → View)
- Native support via Jetpack ViewModel and Lifecycle components

**Best For:**
- Medium complexity apps
- Teams new to architectural patterns
- Apps with straightforward state management
- Rapid development needs

**Trade-offs:**
- ✅ Simple to understand and implement
- ✅ Excellent Jetpack integration
- ✅ Good testability
- ⚠️ Can become messy with complex state
- ⚠️ No standardized way to handle events/side effects
- ⚠️ ViewModels can grow large without discipline

---

### MVI (Model-View-Intent)
**Overview:** Unidirectional architecture where user intents produce new states through a reducer.

**Key Characteristics:**
- Single source of truth for UI state
- Immutable state objects
- Events (Intents) processed through reducer function
- Predictable state transitions
- Easy to debug and replay

**Best For:**
- Complex UI with many state combinations
- Apps requiring state history/time-travel debugging
- Teams familiar with Redux/Flux patterns
- Apps with complex user flows

**Trade-offs:**
- ✅ Predictable state management
- ✅ Excellent for complex UI
- ✅ Easy testing of state transitions
- ✅ Great debugging capabilities
- ⚠️ More boilerplate code
- ⚠️ Steeper learning curve
- ⚠️ Can be overkill for simple screens

---

### Clean Architecture
**Overview:** Domain-centric architecture with strict layer separation and dependency rules.

**Key Characteristics:**
- Layers: Presentation → Domain → Data
- Domain layer is pure Kotlin (no Android dependencies)
- Dependencies point inward (outer layers depend on inner)
- Use cases encapsulate business logic
- Repository pattern abstracts data sources

**Best For:**
- Large, complex applications
- Long-term projects requiring maintainability
- Teams with multiple developers
- Apps with complex business logic
- Projects requiring high testability

**Trade-offs:**
- ✅ Excellent separation of concerns
- ✅ Highly testable
- ✅ Scalable architecture
- ✅ Business logic independent of framework
- ⚠️ Significant boilerplate
- ⚠️ Overhead for simple features
- ⚠️ Requires discipline to maintain boundaries

---

### Hybrid Approaches
**Overview:** Combining patterns to leverage benefits of multiple approaches.

**Common Combinations:**
- **Clean + MVVM:** Clean Architecture layers with MVVM in presentation
- **Clean + MVI:** Clean Architecture with MVI state management
- **MVVM + Repository:** MVVM with repository pattern (no use cases)

**Best For:**
- Projects with varying complexity across features
- Gradual adoption of stricter architecture
- Teams wanting flexibility
```

#### 1.2 Requirements Mapping

Based on gathered context, map requirements to architecture characteristics:

```markdown
## Requirements Analysis

### Complexity Assessment
| Factor | Your Project | Architecture Implication |
|--------|--------------|-------------------------|
| Screen Count | [X screens] | [Simple/Medium/Complex] |
| State Complexity | [Low/Medium/High] | [MVVM sufficient / MVI beneficial] |
| Business Logic | [Thin/Moderate/Complex] | [Skip/Consider/Require domain layer] |
| Data Sources | [Single/Multiple] | [Simple repo / Full data layer] |
| Offline Requirements | [None/Basic/Full sync] | [Impacts data layer complexity] |

### Team Assessment
| Factor | Your Team | Architecture Implication |
|--------|-----------|-------------------------|
| Team Size | [X developers] | [More structure needed if larger] |
| Android Experience | [Junior/Mid/Senior] | [Simpler patterns for newer teams] |
| Architecture Experience | [Pattern familiarity] | [Consider learning curve] |
| Testing Culture | [Low/Medium/High] | [Affects layer separation needs] |

### Project Assessment
| Factor | Your Project | Architecture Implication |
|--------|--------------|-------------------------|
| Timeline | [Short/Medium/Long-term] | [Less/More architectural investment] |
| Expected Growth | [Stable/Growing/Rapid] | [Scalability consideration] |
| Maintenance Period | [Short/Long-term] | [Maintainability weight] |
| Team Stability | [Stable/Rotating] | [Documentation, standards importance] |
```

---

### Phase 2: Recommendation

**CHECKPOINT 1:** Present the analysis and initial recommendation.

```markdown
## Architecture Recommendation

Based on your requirements analysis, here's my recommendation:

### Primary Recommendation: [Pattern Name]

**Why This Pattern:**
1. [Reason matching your requirements]
2. [Reason matching your team context]
3. [Reason matching your constraints]

**How It Addresses Your Needs:**
- [Requirement 1] → [How pattern addresses it]
- [Requirement 2] → [How pattern addresses it]
- [Requirement 3] → [How pattern addresses it]

### Alternative Consideration: [Secondary Pattern]

**Consider This If:**
- [Condition where alternative might be better]
- [Condition where alternative might be better]

### Not Recommended: [Pattern to Avoid]

**Why Not:**
- [Reason it doesn't fit]
- [Risk if chosen anyway]

---

**Questions Before Implementation Details:**
1. Does this recommendation align with your team's preferences?
2. Are there any constraints I may have missed?
3. Would you like me to detail the alternative approach as well?
```

---

### Phase 3: Implementation Blueprint

After recommendation approval, provide implementation guidance:

#### 3.1 Package Structure

```markdown
## Recommended Package Structure

### MVVM Package Structure
```
com.example.app/
├── data/
│   ├── local/
│   │   ├── db/
│   │   │   ├── AppDatabase.kt
│   │   │   ├── dao/
│   │   │   └── entity/
│   │   └── preferences/
│   ├── remote/
│   │   ├── api/
│   │   └── dto/
│   ├── repository/
│   └── mapper/
├── di/
│   └── [Hilt modules]
├── ui/
│   ├── [feature]/
│   │   ├── [Feature]Screen.kt
│   │   ├── [Feature]ViewModel.kt
│   │   ├── [Feature]UiState.kt
│   │   └── components/
│   ├── navigation/
│   ├── theme/
│   └── common/
├── util/
└── App.kt
```

### Clean Architecture Package Structure
```
com.example.app/
├── domain/                    # Pure Kotlin layer
│   ├── model/
│   ├── repository/            # Interfaces only
│   └── usecase/
├── data/                      # Data layer implementation
│   ├── local/
│   ├── remote/
│   ├── repository/            # Implements domain interfaces
│   └── mapper/
├── presentation/              # UI layer
│   ├── [feature]/
│   │   ├── [Feature]Screen.kt
│   │   ├── [Feature]ViewModel.kt
│   │   └── [Feature]UiState.kt
│   ├── navigation/
│   └── common/
├── di/
└── App.kt
```

### MVI Package Structure
```
com.example.app/
├── data/
│   └── [Same as MVVM]
├── ui/
│   ├── [feature]/
│   │   ├── [Feature]Screen.kt
│   │   ├── [Feature]ViewModel.kt
│   │   ├── [Feature]State.kt      # Immutable state
│   │   ├── [Feature]Event.kt      # User intents
│   │   ├── [Feature]Effect.kt     # Side effects
│   │   └── [Feature]Reducer.kt    # State reducer (optional)
│   └── base/
│       ├── MviViewModel.kt        # Base MVI ViewModel
│       └── UiState.kt             # Base state interface
└── [Same structure for di, util, etc.]
```
```

#### 3.2 Core Components Template

```markdown
## Core Component Templates

### ViewModel Pattern (MVVM)

```kotlin
@HiltViewModel
class FeatureViewModel @Inject constructor(
    private val repository: FeatureRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow(FeatureUiState())
    val uiState: StateFlow<FeatureUiState> = _uiState.asStateFlow()

    init {
        loadData()
    }

    fun onAction(action: FeatureAction) {
        when (action) {
            is FeatureAction.Refresh -> loadData()
            is FeatureAction.ItemClick -> handleItemClick(action.item)
            // ... other actions
        }
    }

    private fun loadData() {
        viewModelScope.launch {
            _uiState.update { it.copy(isLoading = true) }
            repository.getData()
                .onSuccess { data ->
                    _uiState.update { it.copy(isLoading = false, data = data) }
                }
                .onFailure { error ->
                    _uiState.update { it.copy(isLoading = false, error = error.message) }
                }
        }
    }
}

data class FeatureUiState(
    val isLoading: Boolean = false,
    val data: List<Item> = emptyList(),
    val error: String? = null
)

sealed interface FeatureAction {
    data object Refresh : FeatureAction
    data class ItemClick(val item: Item) : FeatureAction
}
```

### MVI Pattern

```kotlin
@HiltViewModel
class FeatureViewModel @Inject constructor(
    private val repository: FeatureRepository
) : ViewModel() {

    private val _state = MutableStateFlow(FeatureState())
    val state: StateFlow<FeatureState> = _state.asStateFlow()

    private val _effect = Channel<FeatureEffect>()
    val effect: Flow<FeatureEffect> = _effect.receiveAsFlow()

    fun onEvent(event: FeatureEvent) {
        when (event) {
            is FeatureEvent.LoadData -> loadData()
            is FeatureEvent.ItemClicked -> handleItemClick(event.itemId)
            is FeatureEvent.RetryClicked -> loadData()
        }
    }

    private fun loadData() {
        viewModelScope.launch {
            reduce { copy(isLoading = true, error = null) }
            repository.getData()
                .onSuccess { data ->
                    reduce { copy(isLoading = false, items = data) }
                }
                .onFailure { error ->
                    reduce { copy(isLoading = false, error = error.toUiError()) }
                }
        }
    }

    private fun handleItemClick(itemId: String) {
        viewModelScope.launch {
            _effect.send(FeatureEffect.NavigateToDetail(itemId))
        }
    }

    private fun reduce(reducer: FeatureState.() -> FeatureState) {
        _state.update { it.reducer() }
    }
}

data class FeatureState(
    val isLoading: Boolean = false,
    val items: List<Item> = emptyList(),
    val error: UiError? = null
)

sealed interface FeatureEvent {
    data object LoadData : FeatureEvent
    data class ItemClicked(val itemId: String) : FeatureEvent
    data object RetryClicked : FeatureEvent
}

sealed interface FeatureEffect {
    data class NavigateToDetail(val itemId: String) : FeatureEffect
    data class ShowSnackbar(val message: String) : FeatureEffect
}
```

### Clean Architecture Use Case

```kotlin
class GetFeatureDataUseCase @Inject constructor(
    private val repository: FeatureRepository,
    private val mapper: FeatureMapper
) {
    suspend operator fun invoke(params: Params): Result<List<FeatureItem>> {
        return repository.getData(params.filter)
            .map { entities -> entities.map(mapper::toDomain) }
    }

    data class Params(val filter: String?)
}
```

### Repository Pattern

```kotlin
// Domain layer interface
interface FeatureRepository {
    suspend fun getData(filter: String?): Result<List<FeatureEntity>>
    suspend fun getById(id: String): Result<FeatureEntity?>
    suspend fun save(item: FeatureEntity): Result<Unit>
}

// Data layer implementation
class FeatureRepositoryImpl @Inject constructor(
    private val localDataSource: FeatureLocalDataSource,
    private val remoteDataSource: FeatureRemoteDataSource,
    private val mapper: FeatureDataMapper
) : FeatureRepository {

    override suspend fun getData(filter: String?): Result<List<FeatureEntity>> {
        return runCatching {
            // Try remote first, fallback to local
            val remoteData = remoteDataSource.fetchData(filter).getOrNull()
            if (remoteData != null) {
                localDataSource.saveAll(mapper.toLocal(remoteData))
                mapper.toDomain(remoteData)
            } else {
                mapper.toDomain(localDataSource.getAll())
            }
        }
    }
}
```
```

#### 3.3 Layer Boundaries & Rules

```markdown
## Architecture Rules

### Dependency Rules

```
┌─────────────────────────────────────────────────────┐
│                   Presentation                       │
│  (ViewModels, Screens, UI State)                    │
│                      │                               │
│                      ▼                               │
├─────────────────────────────────────────────────────┤
│                     Domain                           │
│  (Use Cases, Domain Models, Repository Interfaces)  │
│                      │                               │
│                      ▼                               │
├─────────────────────────────────────────────────────┤
│                      Data                            │
│  (Repositories, Data Sources, DTOs, Entities)       │
└─────────────────────────────────────────────────────┘

Dependencies flow DOWNWARD only.
Outer layers depend on inner layers, never the reverse.
```

### Layer Responsibilities

| Layer | Contains | Knows About | Doesn't Know |
|-------|----------|-------------|--------------|
| Presentation | ViewModels, Screens, UI State | Domain | Data, Android Framework internals |
| Domain | Use Cases, Domain Models, Repository Interfaces | Nothing | Presentation, Data, Android |
| Data | Repository Impl, Data Sources, DTOs | Domain interfaces | Presentation |

### Common Violations to Avoid

| Violation | Example | Fix |
|-----------|---------|-----|
| UI accessing data directly | Screen calling repository | Go through ViewModel |
| Domain knowing Android | UseCase using Context | Pass primitive data only |
| Data exposing DTOs to UI | ViewModel using ApiResponse | Map to domain model |
| Circular dependencies | Feature A → Feature B → Feature A | Extract shared interface |
```

---

### Phase 4: Migration Strategy (if applicable)

If this is a refactor of existing code:

```markdown
## Migration Strategy

### Incremental Migration Approach

**Phase 1: Foundation (Week 1-2)**
- Set up new package structure alongside existing
- Implement DI modules for new architecture
- Create base classes/interfaces

**Phase 2: Vertical Slice (Week 2-3)**
- Migrate ONE feature completely to new architecture
- Use this as the pattern template
- Document learnings and adjust patterns

**Phase 3: Feature-by-Feature Migration**
- Migrate features in priority order
- Maintain backward compatibility during transition
- Each PR should complete one feature migration

**Phase 4: Cleanup**
- Remove old code paths
- Consolidate duplicate utilities
- Update documentation

### Coexistence Patterns

During migration, old and new code must coexist:

```kotlin
// Shared navigation that works with both architectures
// Dependency injection that provides both old and new dependencies
// Gradual replacement of Activities → Fragments → Compose
```

### Risk Mitigation
- Keep old code functional until new code is tested
- Feature flags for gradual rollout
- Comprehensive test coverage before migration
```

---

## Expected Output

The architecture selection produces:

1. **Requirements Analysis** - Mapping of needs to architecture characteristics
2. **Pattern Comparison** - Relevant patterns compared against requirements
3. **Primary Recommendation** - Clear recommendation with rationale
4. **Implementation Blueprint** - Package structure, templates, rules
5. **Migration Strategy** - (If applicable) How to adopt incrementally

---

## Example Interaction

**User:** I'm starting a new fintech app for personal budgeting. We're a team of 3 Android developers, all mid-level. The app will have about 15 screens, need offline support, and sync data with our backend. We expect to maintain this for several years and add features regularly.

**Agent:**

## Architecture Analysis

Based on your context, here's my analysis:

### Requirements Mapping

| Factor | Your Project | Implication |
|--------|--------------|-------------|
| App Complexity | Medium-High (15 screens, offline sync) | Need structured approach |
| Team Size | 3 developers | Architecture should enable parallel work |
| Experience Level | Mid-level | Avoid overly complex patterns |
| Offline Support | Required | Strong data layer needed |
| Longevity | Multi-year | Maintainability is critical |
| Growth | Regular features | Scalability matters |

### Primary Recommendation: Clean Architecture + MVVM

**Why This Pattern:**
1. **Maintainability:** Your multi-year timeline makes Clean Architecture's separation valuable
2. **Team Parallelization:** 3 devs can work on different layers simultaneously
3. **Testability:** Fintech apps need high test coverage - Clean Architecture enables this
4. **Offline Support:** The structured data layer handles complex sync scenarios well
5. **Learning Curve:** MVVM in presentation layer is accessible for mid-level devs

**Consider MVI If:**
- Your budget screens have very complex state (multiple accounts, filters, date ranges combined)
- You find state bugs becoming common during development

**I'd avoid pure MVVM without domain layer because:**
- Your offline sync requirements will create complex business logic
- Without use cases, ViewModels will become bloated over time

**Would you like me to proceed with the detailed implementation blueprint for Clean Architecture + MVVM?**

---

## Techniques Used

- **ST-01** (Clear Objective): Focused objective on architecture selection
- **ST-02** (Sequential Instructions): Phased analysis → recommendation → blueprint
- **RT-02** (Multi-Dimensional Analysis): Technical, team, and project factors analyzed
- **RT-04** (Best Practice Review): Android architecture patterns and guidelines
- **RT-05** (Evidence-Based Reasoning): Recommendations tied to stated requirements
- **ST-03** (Output Format Templates): Structured comparison tables and code templates
- **NE-01** (Single-Question Pacing): Context gathering before analysis
- **NE-02** (Phased Workflow): Clear progression through decision process
- **NE-07** (Discussion Before Action): Checkpoint before detailed blueprint
- **AG-02** (Skeptical Default Stance): Honest trade-offs for each pattern

---

## Related Prompts

- [android_codebase_health_assessment.md](../analysis/android_codebase_health_assessment.md) - Assess existing architecture first
- [android_architecture_review.md](../analysis/android_architecture_review.md) - Deep review of current architecture
- [android_feature_specification.md](android_feature_specification.md) - Design features within chosen architecture
- [android_module_design.md](android_module_design.md) - Multi-module structure for chosen architecture
- [android_tech_stack_selection.md](android_tech_stack_selection.md) - Select libraries that complement architecture

---

## Customization Guide

### For Different Team Sizes

**Solo Developer:**
- Emphasize simplicity over scalability
- Recommend MVVM unless complexity truly demands more
- Consider skipping use cases for simple features

**Large Team (5+):**
- Emphasize interface contracts between layers
- Consider module boundaries early
- Add architecture decision records (ADRs)

### For Different App Types

**Consumer Social App:**
- Real-time updates may favor MVI
- Focus on UI layer patterns
- State complexity usually high

**Enterprise/B2B App:**
- Clean Architecture often required for compliance
- Heavier testing requirements
- More formal documentation needs

**SDK/Library:**
- Public API surface is architecture
- Internal architecture can be simpler
- Focus on interface stability

### For Specific Technical Needs

**Heavy Offline Requirements:**
- Always recommend robust data layer
- Consider Clean Architecture for complex sync
- Plan for conflict resolution

**Real-time Features (Chat, Feeds):**
- MVI often valuable for state management
- Consider reactive data layer
- Plan for WebSocket integration architecture

**High Performance Requirements:**
- Keep architecture lightweight
- Avoid excessive mapping between layers
- Consider memory allocation patterns
