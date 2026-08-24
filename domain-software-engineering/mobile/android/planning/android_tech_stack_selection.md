---
title: "Android Tech Stack Selection"
category: mobile-development
description: "Select a cohesive Android technology stack (UI, networking, serialization, database, DI, images, async, navigation, testing) justified against project needs, with a version catalog."
techniques:
  - ST-01
  - ST-03
  - RT-02
  - RT-04
  - NE-01
  - AG-02
difficulty: intermediate
tags:
  - android
  - mobile-development
  - tech-stack
  - libraries
  - version-catalog
  - dependencies
updated: "2026-06-06"
---

# Android Tech Stack Selection

**Objective:** Guide the selection of an optimal technology stack for an Android application by evaluating libraries, frameworks, and tools against project requirements, team expertise, and long-term maintainability to produce a justified, cohesive set of dependencies.

**When to Use:** Use this prompt when starting a new Android project, evaluating alternatives to existing libraries, or modernizing an outdated tech stack. Ideal for making informed decisions about networking, database, DI, image loading, and other core infrastructure choices. Best used after architecture selection but before implementation begins.

**Sequence Map:** Use after architecture selection; use before project scaffold generation.

**Prompt Type:** Modular (150-200 lines)

---

## Context Gathering

Before recommending a tech stack, gather context:

1. **Project Requirements:**
   - "What type of app is this? (consumer, enterprise, SDK)"
   - "What are the key technical requirements? (offline support, real-time, heavy media)"

2. **Team Context:**
   - "What is your team's experience level?"
   - "Are there libraries your team already knows well?"
   - "Are there organizational standards to follow?"

3. **Constraints:**
   - "What is your minimum SDK level?"
   - "Are there app size constraints?"
   - "Any libraries explicitly required or forbidden?"

4. **Priorities:**
   - "What matters most: stability, cutting-edge features, community support, or performance?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY technology, you MUST:**

1. **Trace actual requirements** - Don't recommend technologies without understanding what the project actually needs.
2. **Check for existing decisions** - Search for existing libraries, team experience, or organizational standards.
3. **Understand the context** - Consider team size, experience, project timeline, and maintenance capacity.
4. **Confirm actual benefit** - Will this technology provide real value for this specific project?
5. **Provide specific recommendations** - Every suggestion must include version, rationale, and trade-offs.

**Recommending FEWER libraries is often better.** Don't recommend technologies just because they're popular.

### False-Positive Prevention

- ❌ Do NOT recommend technologies the team can't maintain
- ❌ Do NOT recommend every popular library without considering actual needs
- ❌ Do NOT ignore team experience when suggesting unfamiliar technologies
- ❌ Do NOT recommend multiple options for the same problem (decide)
- ✅ DO consider the learning curve and maintenance burden
- ✅ DO prioritize team familiarity for time-constrained projects
- ✅ DO consider library stability and long-term maintenance
- ✅ DO recommend specific versions with upgrade paths

---

### Phase 1: Category Analysis

Evaluate each technology category with current best options:

```markdown
## Tech Stack Categories

### 1. UI Framework
| Option | Maturity | Learning Curve | Best For |
|--------|----------|----------------|----------|
| **Jetpack Compose** | Stable (1.5+) | Medium | New projects, modern UI |
| **XML Views** | Mature | Low | Legacy, complex RecyclerViews |
| **Hybrid** | N/A | Higher | Migration, mixed requirements |

**Recommendation Factors:**
- New project → Compose
- Existing View codebase → Gradual migration or stay with Views
- Complex lists with animations → Consider Views for specific screens

---

### 2. Networking
| Option | Maturity | Size Impact | Best For |
|--------|----------|-------------|----------|
| **Retrofit + OkHttp** | Very Mature | ~2MB | REST APIs, proven reliability |
| **Ktor Client** | Mature | ~1.5MB | Multiplatform, Kotlin-first |
| **Apollo Kotlin** | Mature | Variable | GraphQL APIs |

**Recommendation Factors:**
- REST API → Retrofit (default choice)
- KMP planned → Ktor
- GraphQL backend → Apollo

---

### 3. Serialization
| Option | Performance | Kotlin Support | Best For |
|--------|-------------|----------------|----------|
| **Kotlinx Serialization** | Excellent | Native | Kotlin-first, type safety |
| **Moshi** | Very Good | Excellent | Retrofit integration |
| **Gson** | Good | Adequate | Legacy, simple needs |

**Recommendation Factors:**
- New project → Kotlinx Serialization
- Heavy Retrofit use → Moshi
- Legacy codebase → Keep Gson if stable

---

### 4. Local Database
| Option | Complexity | Type Safety | Best For |
|--------|------------|-------------|----------|
| **Room** | Low | Good | Most apps, Jetpack integration |
| **SQLDelight** | Medium | Excellent | Multiplatform, complex queries |
| **Realm** | Low | Good | Simple sync, object DB preference |

**Recommendation Factors:**
- Standard Android → Room (default)
- KMP planned → SQLDelight
- Simple data, quick start → DataStore for key-value

---

### 5. Dependency Injection
| Option | Compile Safety | Learning Curve | Best For |
|--------|----------------|----------------|----------|
| **Hilt** | Yes | Low | Most apps, Google recommended |
| **Koin** | No (runtime) | Very Low | Quick setup, small apps |
| **Dagger** | Yes | High | Maximum control, large apps |
| **Manual DI** | N/A | Low | Simple apps, SDKs |

**Recommendation Factors:**
- Most apps → Hilt (default)
- KMP, simple app → Koin
- SDK/library → Manual DI

---

### 6. Image Loading
| Option | Performance | Compose Support | Best For |
|--------|-------------|-----------------|----------|
| **Coil** | Excellent | Native | Compose apps, Kotlin-first |
| **Glide** | Excellent | Via extension | View-based, proven |
| **Picasso** | Good | Limited | Simple needs |

**Recommendation Factors:**
- Compose → Coil (default)
- Views → Glide
- Minimal images → May not need dedicated library

---

### 7. Async & Reactive
| Option | Learning Curve | Use Case |
|--------|----------------|----------|
| **Coroutines + Flow** | Medium | Default for all async work |
| **RxJava/RxKotlin** | High | Legacy, complex stream operations |
| **LiveData** | Low | Simple UI state (being replaced) |

**Recommendation Factors:**
- New project → Coroutines + Flow only
- Existing RxJava → Gradual migration

---

### 8. Navigation
| Option | Type Safety | Compose Support | Best For |
|--------|-------------|-----------------|----------|
| **Navigation Compose** | Yes (2.8+) | Native | Compose apps |
| **Navigation Component** | Partial | Via interop | View-based apps |
| **Custom/Voyager** | Varies | Yes | Multiplatform, specific needs |

---

### 9. Testing
| Category | Recommended | Alternative |
|----------|-------------|-------------|
| Unit Testing | JUnit 5 + Turbine | JUnit 4 |
| Mocking | MockK | Mockito-Kotlin |
| UI Testing | Compose Testing | Espresso |
| Assertions | Truth / Kotest | AssertJ |
```

---

### Phase 2: Stack Recommendation

**CHECKPOINT:** Present tailored recommendation based on gathered context.

```markdown
## Recommended Tech Stack for [Project Type]

### Core Stack
| Category | Choice | Rationale |
|----------|--------|-----------|
| UI | [Library] | [Why] |
| Networking | [Library] | [Why] |
| Serialization | [Library] | [Why] |
| Database | [Library] | [Why] |
| DI | [Library] | [Why] |
| Images | [Library] | [Why] |
| Async | [Library] | [Why] |
| Navigation | [Library] | [Why] |

### Version Catalog Entry
```toml
[versions]
kotlin = "1.9.21"
compose-bom = "2024.01.00"
# ... other versions

[libraries]
# ... library definitions

[plugins]
# ... plugin definitions
```

### Compatibility Notes
- [Any version compatibility concerns]
- [Known issues to be aware of]

### Alternatives Considered
| Category | Alternative | Why Not Chosen |
|----------|-------------|----------------|
| [Category] | [Option] | [Reason] |
```

---

## Expected Output

1. **Category-by-category analysis** relevant to project needs
2. **Recommended stack** with rationale for each choice
3. **Version catalog** ready to use
4. **Compatibility notes** and migration considerations

---

## Example Interaction

**User:** I'm starting a new consumer app for food delivery. Compose-based, needs offline support, REST API backend. Team of 2 mid-level Android devs. Target: API 26+.

**Agent:**

## Recommended Tech Stack

| Category | Choice | Rationale |
|----------|--------|-----------|
| UI | Jetpack Compose | New project, native modern UI |
| Networking | Retrofit + OkHttp | Proven, excellent for REST |
| Serialization | Kotlinx Serialization | Type-safe, Kotlin-native |
| Database | Room | Offline support, Jetpack integration |
| DI | Hilt | Google recommended, reasonable learning curve |
| Images | Coil | Compose-native, lightweight |
| Async | Coroutines + Flow | Modern standard, Room/Retrofit integration |
| Navigation | Navigation Compose | Type-safe routes, Compose-native |

### Additional Recommendations
- **WorkManager** for background sync (offline → online)
- **DataStore** for user preferences
- **Accompanist** for system UI controller, permissions

### Version Compatibility
All choices are compatible with API 26+ and current stable versions. Room + Coroutines + Retrofit provide excellent offline-first patterns for food delivery use cases.

---

## Techniques Used

- **ST-01** (Clear Objective): Focused on tech stack selection
- **RT-02** (Multi-Dimensional Analysis): Evaluating across multiple criteria
- **RT-04** (Best Practice Review): Current Android recommendations
- **ST-03** (Output Format Templates): Structured comparison tables
- **NE-01** (Single-Question Pacing): Context gathering first
- **AG-02** (Skeptical Default Stance): Honest trade-off assessment

---

## Related Prompts

- [android_architecture_selection.md](android_architecture_selection.md) - Select architecture first
- [android_dependency_audit.md](../analysis/android_dependency_audit.md) - Audit existing dependencies
- [android_project_scaffold.md](android_project_scaffold.md) - Generate project with selected stack

---

## Customization Guide

### For Kotlin Multiplatform
Prioritize: Ktor, SQLDelight, Koin, Kotlinx Serialization, Compose Multiplatform

### For Enterprise Apps
Prioritize: Proven stability over cutting-edge, Hilt, comprehensive testing stack

### For SDK Development
Minimize dependencies, prefer manual DI, avoid large transitive dependencies
