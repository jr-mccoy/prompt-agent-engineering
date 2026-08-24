---
title: "Android Module Design"
category: mobile-development
description: "Design a multi-module Android project structure — module types, boundaries, the dependency graph, and Gradle configuration — for a chosen architecture."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - AG-12
  - NE-07
difficulty: advanced
tags:
  - android
  - mobile-development
  - modularization
  - gradle
  - architecture
  - dependency-graph
updated: "2026-06-06"
---

# Android Module Design

**Objective:** Design an optimal multi-module architecture for an Android application by analyzing feature boundaries, dependency relationships, and build performance requirements to create a modular structure that improves build times, enforces separation of concerns, and enables team scalability.

**When to Use:** Use this prompt when planning to modularize a monolithic app, designing a new multi-module project from scratch, or evaluating whether your current module structure is optimal. Ideal when build times exceed 2-3 minutes, when multiple developers frequently have merge conflicts, or when you need to enforce architectural boundaries. Most valuable for apps with 10+ features or teams of 3+ developers.

**Sequence Map:** Use after architecture selection; use before project scaffold generation.

**Prompt Type:** Comprehensive (300-400 lines)

---

## Context Gathering

Before designing the module structure, gather essential context:

1. **Current State:**
   - "Is this a new project or modularizing an existing app?"
   - "If existing, how many source files and what are current build times?"
   - "What is the current package structure?"

2. **Feature Inventory:**
   - "What are the main features/screens in your app?"
   - "Which features are user-facing vs. shared infrastructure?"
   - "Are there features that could be independently developed/tested?"

3. **Team Structure:**
   - "How many developers work on the codebase?"
   - "Are there team boundaries that align with features?"
   - "Do you need to support feature teams working independently?"

4. **Technical Requirements:**
   - "Do you need dynamic feature delivery (Play Feature Delivery)?"
   - "Are there features that should be conditionally included?"
   - "What is your target build time improvement?"

5. **Dependencies:**
   - "Do you have shared UI components used across features?"
   - "Are there shared business logic or utilities?"
   - "Which third-party libraries are used across multiple features?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY module structure, you MUST:**

1. **Trace actual codebase size** - Don't recommend multi-module architecture for small apps.
2. **Check for existing structure** - Search for current package organization and build times.
3. **Understand the context** - Consider team size, feature count, and actual pain points.
4. **Confirm actual benefit** - Will modularization provide meaningful improvements?
5. **Provide specific recommendations** - Every module suggestion must include clear boundaries and dependencies.

**Recommending a SIMPLER structure is often better.** Not every app needs extensive modularization.

### False-Positive Prevention

- ❌ Do NOT recommend complex module structures for simple apps
- ❌ Do NOT assume every app needs feature modules
- ❌ Do NOT ignore migration complexity when recommending restructuring
- ❌ Do NOT create modules without clear boundaries
- ✅ DO consider build time improvements vs. complexity cost
- ✅ DO understand team capacity to maintain module structure
- ✅ DO start with essential modules before adding more
- ✅ DO provide clear dependency rules for each module

---

### Phase 1: Module Strategy Analysis

#### 1.1 Modularization Approaches

Present the main modularization strategies:

```markdown
## Modularization Strategies

### Strategy 1: By Feature (Recommended Default)

```
app/
├── :app                    # Application module (thin shell)
├── :feature:home           # Home feature
├── :feature:profile        # Profile feature
├── :feature:settings       # Settings feature
├── :core:ui                # Shared UI components
├── :core:data              # Shared data layer
├── :core:network           # Networking infrastructure
└── :core:common            # Common utilities
```

**Pros:**
- Clear ownership boundaries
- Parallel development by feature
- Easy to understand and navigate
- Scales well with team size

**Cons:**
- May require extracting shared code
- Cross-feature navigation complexity

---

### Strategy 2: By Layer

```
app/
├── :app
├── :presentation           # All UI code
├── :domain                 # All business logic
├── :data                   # All data access
└── :core                   # Infrastructure
```

**Pros:**
- Enforces Clean Architecture strictly
- Simple module graph

**Cons:**
- Doesn't scale with team size
- All features coupled within layers
- Limited build time benefits

---

### Strategy 3: Hybrid (Feature + Layer)

```
app/
├── :app
├── :feature:home
│   ├── :feature:home:ui
│   ├── :feature:home:domain
│   └── :feature:home:data
├── :feature:profile
│   └── [same structure]
├── :core:ui
├── :core:domain
└── :core:data
```

**Pros:**
- Maximum separation
- Strict layer boundaries per feature
- Best for large teams

**Cons:**
- Many modules to manage
- Complex dependency graph
- Overhead for small features

---

### Strategy 4: Dynamic Features (Play Feature Delivery)

```
app/
├── :app                          # Base APK
├── :feature:premium              # On-demand feature
│   └── (dynamicFeature = true)
├── :feature:ar-scanner           # Install-time feature
├── :core:[shared modules]
```

**Pros:**
- Smaller initial download size
- Features loaded on demand
- A/B testing capabilities

**Cons:**
- Additional complexity
- Testing challenges
- Not all features are candidates
```

#### 1.2 Feature Boundary Analysis

Analyze the codebase to identify natural feature boundaries:

```markdown
## Feature Boundary Analysis

### Identified Features

| Feature | Screens | Shared Dependencies | Team Owner | Isolation Score |
|---------|---------|---------------------|------------|-----------------|
| [Feature] | [List] | [What it shares] | [Team/Person] | [1-5] |

**Isolation Score Guide:**
- 5: Completely independent, no shared state
- 4: Minimal shared dependencies
- 3: Some shared data models or utilities
- 2: Significant shared business logic
- 1: Deeply intertwined with other features

### Shared Component Analysis

| Component | Used By | Module Candidate |
|-----------|---------|------------------|
| [Component] | [Features using it] | :core:[name] |

### Dependency Clusters

```
Feature A ──┬── SharedAuth ──┬── Feature B
            │                │
            └── SharedUser ──┘

Feature C ── Independent (good isolation)

Feature D ──── SharedPayment ──── Feature E
```
```

#### 1.3 Build Performance Analysis (for existing apps)

```markdown
## Build Performance Analysis

### Current Build Metrics
- Full build time: [X minutes]
- Incremental build time: [Y seconds]
- Largest modules by compilation time: [List]
- Most frequently changed modules: [List]

### Modularization Impact Estimate

| Module Split | Files | Est. Build Savings | Priority |
|--------------|-------|-------------------|----------|
| Extract :core:network | [X files] | [Y%] | High |
| Extract :feature:home | [X files] | [Y%] | High |
| [Other splits] | ... | ... | ... |

### Cache Efficiency Opportunities
- [Analysis of what can be cached better with modules]
```

---

### Phase 2: Module Design

**CHECKPOINT 1:** Present the analysis before proposing module structure.

```markdown
## Analysis Summary

### Key Findings
1. [Finding about feature boundaries]
2. [Finding about shared dependencies]
3. [Finding about team structure alignment]

### Recommended Strategy: [Strategy Name]

**Why This Strategy:**
- [Reason 1]
- [Reason 2]

### Estimated Impact
- Build time improvement: [X%]
- Module count: [Y modules]
- Migration effort: [Low/Medium/High]

**Do you agree with this approach? Any specific features you want to keep together or separate?**
```

After confirmation, proceed with detailed design:

#### 2.1 Module Graph Design

```markdown
## Proposed Module Structure

### Module Graph

```
                    ┌─────────┐
                    │  :app   │
                    └────┬────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
   ┌──────────┐   ┌──────────┐   ┌──────────┐
   │:feature: │   │:feature: │   │:feature: │
   │  home    │   │ profile  │   │ settings │
   └────┬─────┘   └────┬─────┘   └────┬─────┘
        │              │              │
        └──────────────┼──────────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
         ▼             ▼             ▼
   ┌──────────┐  ┌──────────┐  ┌──────────┐
   │ :core:ui │  │:core:data│  │:core:    │
   │          │  │          │  │ network  │
   └────┬─────┘  └────┬─────┘  └────┬─────┘
        │             │             │
        └─────────────┼─────────────┘
                      │
                      ▼
               ┌──────────┐
               │:core:    │
               │ common   │
               └──────────┘
```

### Module Inventory

| Module | Type | Purpose | Dependencies |
|--------|------|---------|--------------|
| :app | Application | Entry point, DI root, navigation host | All features, :core:* |
| :feature:home | Feature | Home screen and related flows | :core:ui, :core:data |
| :feature:profile | Feature | User profile management | :core:ui, :core:data, :core:auth |
| :core:ui | Library | Shared Composables, theme, design system | :core:common |
| :core:data | Library | Repositories, database, shared data models | :core:network, :core:common |
| :core:network | Library | API client, network utilities | :core:common |
| :core:common | Library | Utilities, extensions, base classes | None |

### Dependency Rules

```
✅ Allowed Dependencies:
- :app → :feature:* (all features)
- :app → :core:* (all core modules)
- :feature:* → :core:* (any core module)
- :core:data → :core:network
- :core:ui → :core:common
- :core:* → :core:common

❌ Forbidden Dependencies:
- :feature:* → :feature:* (features cannot depend on each other)
- :core:* → :feature:* (core cannot depend on features)
- :core:* → :app (core cannot depend on app)
- Circular dependencies of any kind
```
```

#### 2.2 Module Configuration

```markdown
## Module Configuration

### Gradle Setup

#### settings.gradle.kts
```kotlin
rootProject.name = "MyApp"

// Feature modules
include(":app")
include(":feature:home")
include(":feature:profile")
include(":feature:settings")

// Core modules
include(":core:ui")
include(":core:data")
include(":core:network")
include(":core:common")
```

#### Convention Plugins Structure
```
build-logic/
├── convention/
│   ├── build.gradle.kts
│   └── src/main/kotlin/
│       ├── AndroidApplicationConventionPlugin.kt
│       ├── AndroidLibraryConventionPlugin.kt
│       ├── AndroidFeatureConventionPlugin.kt
│       └── AndroidComposeConventionPlugin.kt
```

#### Feature Module Template (feature/home/build.gradle.kts)
```kotlin
plugins {
    id("myapp.android.feature")
    id("myapp.android.compose")
}

android {
    namespace = "com.example.myapp.feature.home"
}

dependencies {
    implementation(projects.core.ui)
    implementation(projects.core.data)

    testImplementation(projects.core.testing)
}
```

#### Core Module Template (core/data/build.gradle.kts)
```kotlin
plugins {
    id("myapp.android.library")
    id("myapp.android.hilt")
}

android {
    namespace = "com.example.myapp.core.data"
}

dependencies {
    implementation(projects.core.network)
    implementation(projects.core.common)

    implementation(libs.room.runtime)
    implementation(libs.room.ktx)
    ksp(libs.room.compiler)
}
```
```

#### 2.3 Navigation Between Modules

```markdown
## Inter-Module Navigation

### Navigation Strategy: [Recommended Approach]

#### Option A: Navigation Compose with Type-Safe Routes

```kotlin
// :core:navigation module
@Serializable
sealed interface Route {
    @Serializable
    data object Home : Route

    @Serializable
    data class Profile(val userId: String) : Route

    @Serializable
    data class Settings(val section: String? = null) : Route
}

// Each feature module provides its navigation graph
// :feature:home
fun NavGraphBuilder.homeGraph(
    onNavigateToProfile: (String) -> Unit
) {
    composable<Route.Home> {
        HomeScreen(onProfileClick = onNavigateToProfile)
    }
}

// :app module combines all graphs
@Composable
fun AppNavHost(navController: NavHostController) {
    NavHost(navController, startDestination = Route.Home) {
        homeGraph(
            onNavigateToProfile = { userId ->
                navController.navigate(Route.Profile(userId))
            }
        )
        profileGraph()
        settingsGraph()
    }
}
```

#### Option B: Navigator Interface Pattern

```kotlin
// :core:navigation
interface AppNavigator {
    fun navigateToHome()
    fun navigateToProfile(userId: String)
    fun navigateToSettings()
    fun navigateBack()
}

// :app provides implementation
class AppNavigatorImpl @Inject constructor(
    private val navController: NavController
) : AppNavigator {
    override fun navigateToProfile(userId: String) {
        navController.navigate("profile/$userId")
    }
}

// Features inject AppNavigator
@HiltViewModel
class HomeViewModel @Inject constructor(
    private val navigator: AppNavigator
) : ViewModel() {
    fun onProfileClick(userId: String) {
        navigator.navigateToProfile(userId)
    }
}
```

### Deep Link Support

```kotlin
// :core:navigation
object DeepLinks {
    const val PROFILE = "myapp://profile/{userId}"
    const val SETTINGS = "myapp://settings"
}

// Each feature declares its deep links
fun NavGraphBuilder.profileGraph() {
    composable(
        route = "profile/{userId}",
        deepLinks = listOf(
            navDeepLink { uriPattern = DeepLinks.PROFILE }
        )
    ) { backStackEntry ->
        ProfileScreen(userId = backStackEntry.arguments?.getString("userId"))
    }
}
```
```

#### 2.4 Shared Resource Management

```markdown
## Shared Resources

### Design System Module (:core:ui)

```
core/ui/
├── src/main/
│   ├── kotlin/
│   │   └── com/example/app/core/ui/
│   │       ├── theme/
│   │       │   ├── Theme.kt
│   │       │   ├── Color.kt
│   │       │   ├── Typography.kt
│   │       │   └── Spacing.kt
│   │       ├── components/
│   │       │   ├── AppButton.kt
│   │       │   ├── AppCard.kt
│   │       │   ├── AppTextField.kt
│   │       │   └── LoadingIndicator.kt
│   │       └── util/
│   │           └── ModifierExtensions.kt
│   └── res/
│       ├── values/
│       │   ├── strings_common.xml
│       │   └── dimens.xml
│       └── drawable/
│           └── [shared icons]
```

### String Resource Strategy

| Resource Type | Location | Access Pattern |
|---------------|----------|----------------|
| Feature-specific strings | :feature:* module | R.string.feature_* |
| Common UI strings | :core:ui | CoreR.string.* |
| Error messages | :core:common | CommonR.string.error_* |

### Drawable/Asset Strategy

| Asset Type | Location | Rationale |
|------------|----------|-----------|
| App icon, branding | :app | Only needed in app module |
| Common icons | :core:ui | Shared across features |
| Feature-specific images | :feature:* | Encapsulated with feature |
```

---

### Phase 3: Implementation Plan

**CHECKPOINT 2:** Present the complete module design for approval.

```markdown
## Module Design Summary

### Final Module Count: [X modules]

### Module Breakdown
- Application: 1
- Feature modules: [X]
- Core modules: [X]

### Key Design Decisions
1. [Decision with rationale]
2. [Decision with rationale]

### Dependency Enforcement
[How dependencies will be enforced - lint rules, architecture tests]

**Ready to discuss the migration/implementation plan?**
```

#### 3.1 Migration Strategy (for existing apps)

```markdown
## Migration Plan

### Phase 1: Foundation (Week 1)
- [ ] Set up build-logic with convention plugins
- [ ] Create :core:common module
- [ ] Extract truly shared utilities
- [ ] Verify builds work

### Phase 2: Core Modules (Week 2)
- [ ] Create :core:network (extract API client)
- [ ] Create :core:data (extract database, repositories interface)
- [ ] Create :core:ui (extract shared Composables, theme)
- [ ] Update :app to depend on core modules

### Phase 3: First Feature Module (Week 3)
- [ ] Extract [simplest feature] to :feature:[name]
- [ ] Set up inter-module navigation pattern
- [ ] Establish feature module template
- [ ] Document patterns for team

### Phase 4: Remaining Features (Week 4+)
- [ ] Extract remaining features one by one
- [ ] Each feature is one PR
- [ ] Update documentation as patterns evolve

### Migration Order (by isolation score)
1. [Most isolated feature] - Good first candidate
2. [Next most isolated]
3. ...
4. [Most connected feature] - Save for last

### Rollback Strategy
- Keep original code until feature module is verified
- Feature flags for gradual rollout if needed
- Each module extraction should be independently revertable
```

#### 3.2 Dependency Enforcement

```markdown
## Dependency Enforcement

### Gradle Module Dependency Restrictions

```kotlin
// build-logic/convention/src/main/kotlin/ModuleDependencyRestrictions.kt

// In feature module convention plugin
class AndroidFeatureConventionPlugin : Plugin<Project> {
    override fun apply(target: Project) {
        with(target) {
            // Verify no feature-to-feature dependencies
            configurations.all {
                resolutionStrategy {
                    eachDependency {
                        if (requested.group == rootProject.name &&
                            requested.name.startsWith("feature-") &&
                            project.name.startsWith("feature-") &&
                            requested.name != project.name
                        ) {
                            throw GradleException(
                                "Feature modules cannot depend on other features: " +
                                "${project.name} -> ${requested.name}"
                            )
                        }
                    }
                }
            }
        }
    }
}
```

### Architecture Tests

```kotlin
// Using ArchUnit or similar
@Test
fun `feature modules should not depend on other features`() {
    val rule = noClasses()
        .that().resideInAPackage("..feature.home..")
        .should().dependOnClassesThat()
        .resideInAnyPackage("..feature.profile..", "..feature.settings..")

    rule.check(importedClasses)
}
```
```

---

## Expected Output

The module design produces:

1. **Module Strategy Selection** - Chosen approach with rationale
2. **Module Graph** - Visual dependency diagram
3. **Module Inventory** - Complete list with purposes and dependencies
4. **Configuration Templates** - Gradle setup for each module type
5. **Navigation Design** - How modules communicate
6. **Migration Plan** - Phased approach with rollback strategy

---

## Example Interaction

**User:** We have a monolithic e-commerce app with about 200 Kotlin files. Build times are around 4 minutes. We have 4 developers and want to modularize. Main features are: product catalog, search, shopping cart, checkout, user account, and order history.

**Agent:**

## Analysis Summary

Based on your e-commerce app context:

### Feature Boundary Analysis

| Feature | Est. Files | Isolation Score | Notes |
|---------|------------|-----------------|-------|
| Product Catalog | ~40 | 4 | Shared product models |
| Search | ~25 | 5 | Self-contained |
| Shopping Cart | ~30 | 2 | Touches many features |
| Checkout | ~35 | 3 | Depends on cart, payment |
| User Account | ~35 | 4 | Auth is shared |
| Order History | ~25 | 4 | Depends on order models |

### Recommended Strategy: By Feature

**Module Structure:**
```
:app
:feature:catalog
:feature:search
:feature:cart
:feature:checkout
:feature:account
:feature:orders
:core:ui (design system)
:core:data (shared models, repos)
:core:network
:core:common
```

**Total: 12 modules**

### Estimated Impact
- Build time: 4 min → ~1.5-2 min (50% reduction)
- Incremental builds: Much faster when only one feature changes
- Team parallelization: 4 devs can work on 4 features without conflict

### Migration Order
1. :feature:search (highest isolation, good first test)
2. :feature:account (clear boundaries)
3. :feature:catalog (shared models → extract to :core:data first)
4. :feature:orders (similar to catalog)
5. :feature:cart (complex, save for later)
6. :feature:checkout (most dependencies, last)

**Does this approach align with your team structure and goals?**

---

## Techniques Used

- **ST-01** (Clear Objective): Focused objective on module structure design
- **ST-02** (Sequential Instructions): Analysis → Design → Implementation phases
- **RT-02** (Multi-Dimensional Analysis): Feature, team, and build considerations
- **RT-04** (Best Practice Review): Android modularization best practices
- **ST-03** (Output Format Templates): Module graph diagrams and tables
- **AG-12** (Quantitative Metrics): Build time estimates, file counts
- **NE-02** (Phased Workflow): Clear checkpoints through design process
- **NE-07** (Discussion Before Action): Approval gates before detailed design

---

## Related Prompts

- [android_architecture_selection.md](android_architecture_selection.md) - Select architecture before modularizing
- [android_codebase_health_assessment.md](../analysis/android_codebase_health_assessment.md) - Assess current state first
- [android_feature_specification.md](android_feature_specification.md) - Design features within modules
- [android_dependency_audit.md](../analysis/android_dependency_audit.md) - Audit dependencies before splitting

---

## Customization Guide

### For Different App Sizes

**Small App (< 50 files):**
- Likely doesn't need modularization yet
- Consider simple :app + :core:common split
- Focus on package structure first

**Medium App (50-200 files):**
- Feature modules + shared core
- 5-10 modules typically optimal
- Balance granularity with overhead

**Large App (200+ files):**
- Full feature + layer hybrid may be needed
- Consider sub-features within feature modules
- Dynamic feature delivery for install size

### For Different Team Structures

**Feature Teams:**
- Align modules to team ownership
- Consider separate repositories for modules
- API contracts between teams

**Platform Team:**
- Core modules owned by platform team
- Feature modules by product teams
- Strong API boundaries

### For Specific Goals

**Build Time Optimization:**
- Focus on extracting largest/slowest modules
- Maximize cacheability
- Consider remote build cache

**Code Ownership:**
- CODEOWNERS file per module
- Required reviewers from module owners
- Module-level documentation
