---
title: "Android Compose Migration Analysis"
category: mobile-development
description: "Assesses Android app readiness for Jetpack Compose migration and provides phased migration roadmap"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-05
  - DS-06
difficulty: intermediate
tags:
  - analysis
  - android
  - mobile-development
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_compose_ui_analysis.md
  - domain-software-engineering/mobile/android/improvement/android_compose_multiplatform_migration.md
  - domain-software-engineering/mobile/android/targeted-reviews/android_compose_recomposition_review.md
---


# Android Compose Migration Analysis

**Objective:** Assess an Android app's readiness for Jetpack Compose migration, identify migration complexity, and provide a phased migration roadmap.

**When to Use:** Use this prompt when considering migrating from XML layouts to Jetpack Compose, planning UI modernization efforts, or evaluating the effort required for a Compose adoption project.

**Prompt Type:** Comprehensive (300-400 lines)

---

## Context Gathering

1. **Current UI State:**
   - "What percentage of screens use XML layouts vs Compose (if any)?"
   - "Are there custom Views that need migration?"

2. **Team Context:**
   - "Is the team familiar with Compose?"
   - "Is there a preference for incremental migration or full rewrite?"

3. **Constraints:**
   - "What's the minimum SDK level? (Compose requires API 21+)"
   - "Are there UI libraries that might not have Compose equivalents?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual migration complexity** - Don't flag based on pattern matching alone. Verify that the suspected migration challenge is actually difficult.
2. **Check for existing Compose adoption** - Search for existing Compose code, interop patterns, or migration progress that may already exist.
3. **Understand the context** - Consider WHY specific UI patterns exist. Some XML layouts may be better kept as-is.
4. **Confirm actual benefit** - Will migrating this specific screen provide real value? Not everything needs Compose.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `activity_main.xml`, `HomeFragment.kt:45`).

**Recommending PARTIAL migration is an acceptable outcome.** If some XML layouts work well and don't need migration, say so with confidence. Don't manufacture migration urgency.

### False-Positive Prevention

- ❌ Do NOT flag all XML layouts as "must migrate" (some are fine as-is)
- ❌ Do NOT assume migration is always beneficial without considering team skills and timeline
- ❌ Do NOT report working UI code as problematic just because it's not Compose
- ❌ Do NOT underestimate custom View complexity in migration estimates
- ✅ DO identify screens that would genuinely benefit from Compose
- ✅ DO consider team Compose experience when planning migration scope
- ✅ DO understand ComposeView interop for incremental migration
- ✅ DO weigh migration cost against actual UI/UX improvements

---

### Phase 1: Current UI Assessment

#### 1.1 UI Technology Inventory

```kotlin
// Count screens by type
Screens:
├── XML Layouts (Activities/Fragments)
│   ├── Simple layouts: [X]
│   ├── Complex layouts (custom views): [X]
│   └── RecyclerView-heavy: [X]
├── Compose Screens (if any): [X]
└── Hybrid (XML + Compose): [X]
```

#### 1.2 Complexity Assessment

**Layout Complexity:**

| Layout | Views Count | Nesting Depth | Custom Views | Complexity |
|--------|-------------|---------------|--------------|------------|
| [layout.xml] | [X] | [X levels] | [Yes/No] | [Low/Med/High] |

**Custom Views:**

| Custom View | Purpose | Compose Equivalent | Migration Effort |
|-------------|---------|-------------------|------------------|
| [CustomView] | [Purpose] | [Exists/Partial/None] | [Low/Med/High] |

#### 1.3 Dependency Compatibility

| Library | Current | Compose Support | Notes |
|---------|---------|-----------------|-------|
| Navigation | XML NavGraph | Native | Migration available |
| Material | Material 2 | Material 3 | Theme changes needed |
| [Library] | [Version] | [Yes/No/Partial] | [Notes] |

---

### Phase 2: Migration Readiness

#### 2.1 Architecture Readiness

```kotlin
// COMPOSE-READY: ViewModel with StateFlow
class MyViewModel : ViewModel() {
    private val _uiState = MutableStateFlow(UiState())
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()
}

// NEEDS WORK: ViewModel exposing LiveData to XML
class OldViewModel : ViewModel() {
    val data = MutableLiveData<Data>()
    // Works but StateFlow preferred for Compose
}

// NEEDS WORK: View references in ViewModel
class BadViewModel : ViewModel() {
    var textView: TextView? = null // Remove before Compose
}
```

**Readiness Checklist:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| Min SDK 21+ | [Met/Not Met] | |
| Kotlin 1.8+ | [Met/Not Met] | Compose requires modern Kotlin |
| ViewModels present | [Yes/Partial/No] | Compose works best with ViewModels |
| State hoisting ready | [Yes/Partial/No] | UI state in ViewModels |
| No View refs in business logic | [Yes/No] | Must fix before migration |

#### 2.2 Migration Strategy Options

**Option 1: Bottom-Up (Recommended for existing apps)**
```
Start with leaf components → screens → navigation
1. Create Compose components for buttons, cards, inputs
2. Embed in XML via ComposeView
3. Gradually convert entire screens
4. Finally migrate navigation
```

**Option 2: Top-Down**
```
Start with new screens → migrate existing
1. All new features in Compose
2. Gradually convert existing screens
3. Best when minimal XML changes needed
```

**Option 3: Screen-by-Screen**
```
Convert complete screens
1. Pick least complex screen
2. Full conversion to Compose
3. Move to next screen
```

---

### Phase 3: Migration Report

```markdown
## Compose Migration Analysis Report

### Executive Summary

| Metric | Value |
|--------|-------|
| Total Screens | [X] |
| Compose Ready | [X] |
| Simple Migration | [X] |
| Complex Migration | [X] |
| Custom Views | [X] |

### Migration Complexity Score: [Low/Medium/High]

### Readiness Assessment

| Category | Status | Blockers |
|----------|--------|----------|
| Architecture | [Ready/Needs Work] | [List] |
| Dependencies | [Ready/Needs Updates] | [List] |
| Team Skills | [Ready/Training Needed] | [Notes] |
| Min SDK | [Met/Not Met] | |

---

## Screen Migration Prioritization

### Phase 1: Foundation (Week 1-2)
*Setup and simple screens*

| Screen | Complexity | Dependencies | Order |
|--------|------------|--------------|-------|
| [Screen] | Low | None | 1 |

### Phase 2: Core Screens (Week 3-6)
*Main app functionality*

| Screen | Complexity | Dependencies | Order |
|--------|------------|--------------|-------|
| [Screen] | Medium | [Deps] | X |

### Phase 3: Complex Screens (Week 7+)
*Custom views and complex layouts*

| Screen | Complexity | Blockers | Order |
|--------|------------|----------|-------|
| [Screen] | High | [Issues] | X |

---

## Interoperability Guide

### Embedding Compose in XML
```kotlin
// In Activity/Fragment
val composeView = findViewById<ComposeView>(R.id.compose_view)
composeView.setContent {
    MyTheme {
        MyComposable()
    }
}
```

### Embedding XML in Compose
```kotlin
@Composable
fun LegacyViewWrapper() {
    AndroidView(
        factory = { context ->
            MyCustomView(context)
        },
        update = { view ->
            view.updateData(data)
        }
    )
}
```

---

## Risk Assessment

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Performance regression | Medium | High | Profile before/after |
| Feature parity gaps | Low | Medium | Test thoroughly |
| Team learning curve | High | Medium | Training, pair programming |

---

## Recommended Migration Order

1. **Setup:** Add Compose dependencies, create theme
2. **Components:** Buttons, cards, inputs, icons
3. **Simple Screens:** Settings, profile, static content
4. **List Screens:** LazyColumn migration from RecyclerView
5. **Complex Screens:** Custom views, animations
6. **Navigation:** Migrate to Compose Navigation
```

---

## Expected Output

1. **UI Inventory** - Current XML vs Compose breakdown
2. **Complexity Assessment** - Per-screen migration difficulty
3. **Readiness Checklist** - Blockers and prerequisites
4. **Migration Roadmap** - Phased conversion plan
5. **Risk Analysis** - Potential issues and mitigations

---

## Techniques Used

- **ST-01** (Clear Objective): Migration assessment focus
- **RT-02** (Multi-Dimensional Analysis): Multiple readiness factors
- **DS-06** (Prioritization Guidance): Migration order
- **ST-03** (Output Format Templates): Structured roadmap

---

## Related Prompts

- [android_architecture_review.md](android_architecture_review.md) - Architecture readiness
- [android_code_modernization.md](../improvement/android_code_modernization.md) - Modernization including Compose
- [android_ui_polish_audit.md](../improvement/android_ui_polish_audit.md) - UI quality assessment
