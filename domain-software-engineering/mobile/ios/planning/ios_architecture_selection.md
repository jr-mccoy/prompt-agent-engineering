---
title: "iOS Architecture Selection"
category: mobile-development
description: "Guide architecture pattern selection for iOS projects including MVVM, TCA, VIPER, Clean Architecture, and MV patterns with decision matrices and migration considerations."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-04
difficulty: intermediate
tags:
  - ios
  - swift
  - architecture
  - mvvm
  - tca
  - viper
updated: "2026-03-20"
---

# iOS Architecture Selection

**Objective:** Guide selection of the optimal iOS architecture pattern (MVVM, TCA, VIPER, Clean Architecture, or MV) based on project size, team expertise, testability requirements, and long-term maintainability goals, with concrete implementation examples for the recommended pattern.

**When to Use:** Use this prompt after app concept validation and before writing any production code. Ideal when starting a new project, planning a major refactor, or evaluating whether the current architecture serves the team's needs. Also valuable when onboarding a team that lacks consensus on architecture.

**Prompt Type:** Comprehensive (450+ lines)

---

## Context Gathering

Before recommending an architecture, gather essential context:

1. **Project Characteristics:**
   - "How many screens/features will the app have at launch? In 12 months?"
   - "Is the app primarily CRUD, real-time, media-heavy, or computation-heavy?"
   - "What is the expected codebase size (small <20 files, medium 20-100, large 100+)?"

2. **Team Profile:**
   - "How many iOS developers? Junior/mid/senior distribution?"
   - "What architectures has the team used before?"
   - "Is the team comfortable with reactive programming (Combine, async/await)?"
   - "How important is onboarding speed for new team members?"

3. **Technical Requirements:**
   - "What is the minimum iOS deployment target?"
   - "Is SwiftUI-first or UIKit-first? Or a hybrid?"
   - "What level of test coverage is required (unit, integration, UI)?"
   - "Are there specific performance requirements (startup time, memory)?"

4. **Organizational Constraints:**
   - "Is this a single team or will multiple teams contribute?"
   - "Are there existing shared libraries or frameworks to integrate?"
   - "What CI/CD infrastructure is in place?"
   - "Is there a modularization requirement?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY architecture, you MUST:**

1. **Assess all five major patterns** - Do not default to MVVM without evaluating alternatives against project needs.
2. **Score each pattern against project criteria** - Use the decision matrix with weighted scoring.
3. **Provide concrete Swift code examples** - Show how a real feature looks in the recommended architecture.
4. **Address migration path** - If an existing codebase exists, include incremental adoption strategy.
5. **Identify architecture-specific risks** - Every pattern has tradeoffs; make them explicit.

### False-Positive Prevention

- ❌ Do NOT recommend TCA for teams unfamiliar with functional programming without acknowledging the learning curve
- ❌ Do NOT recommend VIPER for small projects (ceremony exceeds value under ~30 screens)
- ❌ Do NOT recommend "vanilla MVC" -- always provide structured alternatives
- ❌ Do NOT ignore the team's existing expertise when scoring patterns
- ❌ Do NOT conflate architecture with design patterns (Repository, Coordinator are complementary, not alternatives)
- ✅ DO consider SwiftUI's built-in state management (@Observable) as reducing the need for heavy architecture
- ✅ DO account for Apple's platform direction (Observation framework, SwiftData) in recommendations
- ✅ DO recommend the simplest architecture that meets the requirements
- ✅ DO provide escape hatches for when the chosen architecture doesn't fit a specific feature

---

### Phase 1: Architecture Pattern Overview

#### 1.1 Pattern Comparison Matrix

| Dimension | MV (SwiftUI) | MVVM | TCA | VIPER | Clean |
|-----------|-------------|------|-----|-------|-------|
| **Complexity** | Low | Medium | High | High | High |
| **Learning curve** | Low | Low-Med | High | Medium | Medium |
| **Testability** | Medium | High | Very High | Very High | Very High |
| **Scalability** | Medium | High | High | Very High | Very High |
| **SwiftUI fit** | Excellent | Good | Good | Poor | Medium |
| **UIKit fit** | Poor | Good | Medium | Excellent | Good |
| **Boilerplate** | Minimal | Low | Medium | High | High |
| **Team size** | 1-3 | 2-8 | 3-10 | 5-15 | 5-15 |
| **Ideal project** | Small-Med | Any | State-heavy | Large UIKit | Domain-heavy |

#### 1.2 Pattern Definitions

**MV (Model-View with @Observable):**
```swift
// Minimal separation -- View owns state via @Observable models
@Observable
final class RecipeModel {
    var recipes: [Recipe] = []
    var isLoading = false

    func load() async {
        isLoading = true
        recipes = try await RecipeService.shared.fetchAll()
        isLoading = false
    }
}

struct RecipeListView: View {
    @State private var model = RecipeModel()
    var body: some View {
        List(model.recipes) { recipe in
            RecipeRow(recipe: recipe)
        }
        .task { await model.load() }
    }
}
```

**MVVM (Model-View-ViewModel):**
```swift
// ViewModel mediates between View and Model layers
@Observable
final class RecipeListViewModel {
    private(set) var state: ViewState<[Recipe]> = .idle
    private let repository: RecipeRepositoryProtocol

    init(repository: RecipeRepositoryProtocol = RecipeRepository()) {
        self.repository = repository
    }

    func load() async {
        state = .loading
        do {
            let recipes = try await repository.fetchRecipes()
            state = recipes.isEmpty ? .empty : .loaded(recipes)
        } catch {
            state = .error(error.localizedDescription)
        }
    }
}

struct RecipeListScreen: View {
    @State private var viewModel = RecipeListViewModel()
    var body: some View {
        StatefulView(state: viewModel.state) { recipes in
            List(recipes) { recipe in RecipeRow(recipe: recipe) }
        }
        .task { await viewModel.load() }
    }
}
```

**TCA (The Composable Architecture):**
```swift
// Unidirectional data flow with reducers and effects
@Reducer
struct RecipeList {
    @ObservableState
    struct State: Equatable {
        var recipes: [Recipe] = []
        var isLoading = false
    }

    enum Action {
        case onAppear
        case recipesResponse(Result<[Recipe], Error>)
    }

    @Dependency(\.recipeClient) var recipeClient

    var body: some ReducerOf<Self> {
        Reduce { state, action in
            switch action {
            case .onAppear:
                state.isLoading = true
                return .run { send in
                    await send(.recipesResponse(
                        Result { try await recipeClient.fetchAll() }
                    ))
                }
            case .recipesResponse(.success(let recipes)):
                state.isLoading = false
                state.recipes = recipes
                return .none
            case .recipesResponse(.failure):
                state.isLoading = false
                return .none
            }
        }
    }
}
```

**VIPER (View-Interactor-Presenter-Entity-Router):**
```swift
// Strict separation with explicit contracts
protocol RecipeListViewProtocol: AnyObject {
    func display(recipes: [RecipeViewModel])
    func displayError(message: String)
}

protocol RecipeListInteractorProtocol {
    func fetchRecipes()
}

protocol RecipeListPresenterProtocol {
    func viewDidLoad()
    func didSelect(recipe: RecipeViewModel)
}

protocol RecipeListRouterProtocol {
    func navigateToDetail(recipeId: String)
}
```

**Clean Architecture:**
```swift
// Domain-centric with use cases and dependency inversion
// Domain Layer (no framework imports)
protocol FetchRecipesUseCase {
    func execute() async throws -> [Recipe]
}

// Data Layer
final class FetchRecipesUseCaseImpl: FetchRecipesUseCase {
    private let repository: RecipeRepository
    func execute() async throws -> [Recipe] {
        try await repository.fetchAll()
    }
}

// Presentation Layer
@Observable
final class RecipeListViewModel {
    private let fetchRecipes: FetchRecipesUseCase
    // ...
}
```

---

### Phase 2: Decision Matrix Scoring

**CHECKPOINT 1:** Confirm project context before scoring.

```markdown
## Project Profile Summary

| Attribute | Value |
|-----------|-------|
| Project size | Small / Medium / Large |
| Team size | _ developers |
| Team experience | Junior / Mixed / Senior |
| UI framework | SwiftUI / UIKit / Hybrid |
| Test requirements | Low / Medium / High |
| Multi-team? | Yes / No |
| Deployment target | iOS _ |

**Proceed with architecture scoring?**
```

#### 2.1 Weighted Scoring

Score each architecture (1-5) for your project's specific needs:

```markdown
| Criterion | Weight | MV | MVVM | TCA | VIPER | Clean |
|-----------|--------|-----|------|-----|-------|-------|
| Team familiarity | 25% | | | | | |
| Testability needs | 20% | | | | | |
| Project complexity | 20% | | | | | |
| SwiftUI compatibility | 15% | | | | | |
| Onboarding speed | 10% | | | | | |
| Long-term scalability | 10% | | | | | |
| **Weighted Total** | | **_** | **_** | **_** | **_** | **_** |
```

#### 2.2 Automatic Disqualifiers

Apply these rules before scoring:

| Condition | Disqualify |
|-----------|-----------|
| Team < 3 people + no TCA experience | TCA |
| Project < 15 screens, single team | VIPER |
| UIKit-only codebase, no SwiftUI plans | MV |
| No unit testing requirement | TCA (overkill) |
| Regulatory compliance requiring audit trails | MV (insufficient separation) |
| Multi-team with shared modules | MV (coupling risk) |

---

### Phase 3: Implementation Blueprint

**CHECKPOINT 2:** Architecture selected. Provide implementation guide for the winner.

```markdown
## Architecture Decision Record

**Selected Architecture:** [Pattern]
**Score:** _/5 (weighted)
**Runner-up:** [Pattern] (_/5)

**Key reasons for selection:**
1. _
2. _
3. _

**Key risks to monitor:**
1. _
2. _

**Proceed with implementation blueprint?**
```

#### 3.1 Layer Structure

Provide the recommended project structure for the selected architecture:

```
// MVVM Example
App/
├── App/
│   ├── AppDelegate.swift
│   └── MyApp.swift
├── Features/
│   ├── Recipes/
│   │   ├── RecipeListScreen.swift
│   │   ├── RecipeListViewModel.swift
│   │   ├── RecipeDetailScreen.swift
│   │   ├── RecipeDetailViewModel.swift
│   │   └── Views/
│   │       ├── RecipeRow.swift
│   │       └── RecipeCard.swift
│   └── Settings/
│       ├── SettingsScreen.swift
│       └── SettingsViewModel.swift
├── Core/
│   ├── Models/
│   │   └── Recipe.swift
│   ├── Services/
│   │   ├── RecipeRepository.swift
│   │   └── RecipeRepositoryProtocol.swift
│   ├── Networking/
│   │   ├── APIClient.swift
│   │   └── Endpoints.swift
│   └── Persistence/
│       └── SwiftDataStore.swift
├── Shared/
│   ├── Components/
│   ├── Extensions/
│   └── Design/
└── Tests/
    ├── ViewModelTests/
    └── RepositoryTests/
```

#### 3.2 Dependency Flow Rules

```
View → ViewModel → Repository → DataSource
  ↓         ↓            ↓           ↓
 SwiftUI  @Observable  Protocol   URLSession/
                      Abstraction  SwiftData
```

**Rules:**
1. Views never import networking or persistence frameworks
2. ViewModels depend on protocol abstractions, not concrete types
3. Repositories are the single source of truth for data
4. DataSources are interchangeable (network, cache, mock)

#### 3.3 Testing Strategy by Layer

```markdown
| Layer | Test Type | Framework | What to Test |
|-------|-----------|-----------|-------------|
| ViewModel | Unit | XCTest | State transitions, error handling |
| Repository | Unit | XCTest | Data mapping, caching logic |
| View | Snapshot | swift-snapshot-testing | Visual regression |
| Integration | Integration | XCTest | ViewModel + real Repository |
| E2E | UI | XCUITest | Critical user flows |
```

---

### Phase 4: Migration Strategy

#### 4.1 If Migrating from MVC

```swift
// Step 1: Extract ViewModel from ViewController
// BEFORE (Massive View Controller)
class RecipeListVC: UIViewController {
    var recipes: [Recipe] = []
    func fetchRecipes() {
        URLSession.shared.dataTask(with: url) { data, _, _ in
            self.recipes = try JSONDecoder().decode([Recipe].self, from: data!)
            DispatchQueue.main.async { self.tableView.reloadData() }
        }.resume()
    }
}

// AFTER (Extracted ViewModel)
@Observable
final class RecipeListViewModel {
    private(set) var recipes: [Recipe] = []
    private let repository: RecipeRepositoryProtocol

    func load() async throws {
        recipes = try await repository.fetchRecipes()
    }
}

// ViewController becomes thin
class RecipeListVC: UIViewController {
    private let viewModel: RecipeListViewModel
    // Only handles UIKit lifecycle and binding
}
```

#### 4.2 Incremental Adoption Plan

```markdown
| Phase | Duration | Action | Risk |
|-------|----------|--------|------|
| 1 | 1-2 weeks | Establish patterns in one feature | Low |
| 2 | 2-4 weeks | Migrate 2-3 more features | Low |
| 3 | Ongoing | New features use new architecture | Low |
| 4 | As needed | Migrate remaining features opportunistically | Medium |

**Rule:** Never migrate more than one feature at a time. Ship each migration independently.
```

---

### Phase 5: Architecture Governance

#### 5.1 Lint Rules and Conventions

```swift
// SwiftLint rules to enforce architecture boundaries
// .swiftlint.yml additions

// Prevent Views from importing data layer
// Custom rule: Views should not import Foundation networking
custom_rules:
  view_layer_violation:
    name: "View Layer Violation"
    regex: "import (Alamofire|GRDB)"
    match_kinds:
      - identifier
    message: "Views should not import data layer frameworks"
    severity: error
```

#### 5.2 Code Review Checklist

```markdown
## Architecture Review Checklist
- [ ] New feature follows established architecture pattern
- [ ] ViewModel/Reducer has no UIKit/SwiftUI imports (except @Observable)
- [ ] Dependencies injected via protocol, not concrete type
- [ ] Unit tests cover ViewModel state transitions
- [ ] No business logic in View layer
- [ ] Navigation handled by designated coordinator/router
- [ ] Shared components placed in Shared/ not feature modules
```

---

## Expected Output

### Deliverables

```
Architecture Decision
├── Pattern Comparison (all 5 patterns)
├── Weighted Decision Matrix (scored)
├── Architecture Decision Record (ADR)
├── Project Structure Template
├── Dependency Flow Diagram
├── Testing Strategy by Layer
├── Migration Plan (if applicable)
└── Governance Rules
```

### Decision Checklist

- [ ] All five architecture patterns evaluated
- [ ] Decision matrix scored with project-specific weights
- [ ] Disqualifiers applied before scoring
- [ ] Concrete code examples for recommended pattern
- [ ] Project structure defined
- [ ] Testing strategy aligned to architecture
- [ ] Migration path provided (if existing codebase)
- [ ] Governance rules established

---

## Example Interaction

**User:** "We're a team of 4 (1 senior, 2 mid, 1 junior) building a SwiftUI-first recipe app. About 25 screens. We want good test coverage but the team has only used MVC before. iOS 17+."

**Assistant:**

### Recommendation: MVVM with @Observable

**Score: 4.2/5** (vs TCA 3.1, VIPER 2.5, Clean 3.4, MV 3.6)

**Rationale:**
1. **Team fit:** MVVM's learning curve from MVC is gentle -- ViewModels are conceptually similar to "extracted controller logic." TCA's functional patterns would slow the team significantly.
2. **SwiftUI alignment:** @Observable + @State provides natural MVVM bindings without Combine boilerplate. iOS 17+ means full Observation framework support.
3. **Testability:** ViewModels with protocol-based dependencies are straightforward to unit test -- matching your coverage goals without TCA's testing infrastructure overhead.
4. **Scale:** 25 screens is well within MVVM's sweet spot. Add coordinators for navigation if screen count grows past 40.

**Risk to monitor:** Ensure ViewModels don't grow into "Massive ViewModels" -- enforce the rule that each ViewModel handles one screen only.

---

## Techniques Used

- **ST-01** (Clear Objective): Focused architecture selection with measurable criteria
- **ST-02** (Sequential Instructions): Five-phase evaluation from overview to governance
- **RT-02** (Multi-Dimensional Analysis): Scoring across complexity, testability, team fit, scalability
- **RT-04** (Best Practice Review): Industry-standard patterns with Apple platform alignment

---

## Related Prompts

- [ios_app_concept_validation.md](ios_app_concept_validation.md) - Validate concept before selecting architecture
- [ios_module_design.md](ios_module_design.md) - Design module boundaries within chosen architecture
- [ios_tech_stack_selection.md](ios_tech_stack_selection.md) - Select complementary technology stack
- [ios_project_scaffold.md](ios_project_scaffold.md) - Generate project structure for chosen architecture

---

## Customization Guide

### For SwiftUI-Only Projects (iOS 17+)

Simplify the MV pattern consideration:
- @Observable eliminates most MVVM boilerplate
- Consider MV for simple screens, MVVM for complex screens (hybrid approach)
- ViewModels become optional rather than mandatory

### For Large Enterprise Teams (10+ developers)

Add these dimensions to the decision matrix:
- Module ownership boundaries (feature teams)
- Build time impact (module graph complexity)
- Binary framework distribution (XCFramework support)
- API contract enforcement between modules

### For Apps with Heavy Side Effects

Weight TCA higher when:
- Complex undo/redo requirements
- Time-travel debugging needs
- Deterministic state management is a regulatory requirement
- Multiple features interact with shared state
