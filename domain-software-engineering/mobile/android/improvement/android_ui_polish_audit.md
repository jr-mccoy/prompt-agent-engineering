---
title: "Android UI Polish Audit"
category: mobile-development
description: "Audits Android app UI for consistency and professional polish identifying areas needing refinement for high-quality experience"
techniques:
  - ST-01
  - RT-02
  - ST-03
  - OC-05
difficulty: intermediate
tags:
  - android
  - mobile-development
  - ui
  - compose
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_compose_ui_analysis.md
  - domain-software-engineering/mobile/android/improvement/android_accessibility_improvement.md
  - domain-software-engineering/mobile/android/improvement/android_user_experience_enhancement.md
---

# Android UI Polish Audit

**Objective:** Audit an Android app's UI for consistency, polish, and professional feel, identifying areas that need refinement to achieve a high-quality user experience.

**When to Use:** Use this prompt before app store submissions, during design QA, when the app "feels off" but issues aren't clear, or as part of regular quality audits.

**Prompt Type:** Comprehensive (300-400 lines)

---

## Context Gathering

1. **Design Context:**
   - "Is there a design system or style guide to follow?"
   - "What design personality are you aiming for (minimal, playful, professional)?"

2. **Known Issues:**
   - "Are there specific screens or flows that feel unpolished?"

3. **Platform:**
   - "Are you using Material Design 2 or 3? Compose or XML?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual UI inconsistencies** - Don't flag based on assumptions. Verify that the suspected polish issue actually appears in the running app.
2. **Check for design system compliance** - Search for existing design tokens, themes, or style guides that define intended values.
3. **Understand the context** - Consider WHY specific design choices were made. Intentional variations may serve UX purposes.
4. **Confirm actual user impact** - Does this actually look wrong to users, or is it subjective preference?
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `styles.xml:45`, `HomeScreen.kt:78`).

**Finding a POLISHED UI is an acceptable outcome.** If the UI is consistent and well-designed, say so with confidence. Don't manufacture polish concerns.

### False-Positive Prevention

- ❌ Do NOT flag intentional design variations as inconsistencies
- ❌ Do NOT flag based solely on personal aesthetic preferences
- ❌ Do NOT assume missing polish without checking the design system
- ❌ Do NOT report micro-issues that users won't notice
- ✅ DO verify issues on actual devices, not just code inspection
- ✅ DO understand Material Design guidelines and when they apply
- ✅ DO check for dark mode, dynamic colors, and accessibility variations
- ✅ DO consider platform conventions and user expectations

---

### Phase 1: Visual Consistency Analysis

#### 1.1 Spacing System

```kotlin
// Check for consistent spacing values
// Material Design recommends 4dp/8dp grid

Common issues:
- Inconsistent padding (16dp here, 12dp there)
- Margins varying between screens
- Spacing not following a system
```

#### 1.2 Typography

| Element | Font | Size | Weight | Consistent? |
|---------|------|------|--------|-------------|
| Headlines | [Font] | [sp] | [Weight] | [Yes/No] |
| Body | [Font] | [sp] | [Weight] | [Yes/No] |
| Labels | [Font] | [sp] | [Weight] | [Yes/No] |
| Buttons | [Font] | [sp] | [Weight] | [Yes/No] |

#### 1.3 Color Consistency

| Usage | Color | Hex | Used Consistently? |
|-------|-------|-----|-------------------|
| Primary | [Color] | [#XXXXXX] | [Yes/No] |
| Secondary | [Color] | [#XXXXXX] | [Yes/No] |
| Error | [Color] | [#XXXXXX] | [Yes/No] |
| Background | [Color] | [#XXXXXX] | [Yes/No] |

#### 1.4 Component Styling

| Component | Style Consistent? | Issues |
|-----------|------------------|--------|
| Buttons | [Yes/No] | [Varying corner radius, etc.] |
| Cards | [Yes/No] | [Elevation differences] |
| Input fields | [Yes/No] | [Style variations] |
| Icons | [Yes/No] | [Mixed icon sets] |

---

### Phase 2: Polish Assessment

#### 2.1 Loading States

| Screen | Has Loading State | Quality |
|--------|-------------------|---------|
| [Screen] | [Yes/No] | [Skeleton/Spinner/None] |

**Best Practice:**
```kotlin
// Good: Skeleton screens or shimmer
ShimmerPlaceholder(visible = isLoading)

// Acceptable: Progress indicator
CircularProgressIndicator()

// Poor: No indication or just blank screen
```

#### 2.2 Empty States

| Screen | Has Empty State | Quality |
|--------|-----------------|---------|
| [Screen] | [Yes/No] | [Designed/Generic/None] |

**Best Practice:**
```kotlin
@Composable
fun EmptyState(
    icon: ImageVector,
    title: String,
    subtitle: String,
    action: (() -> Unit)? = null
)
```

#### 2.3 Error States

| Screen | Has Error State | User-Friendly? |
|--------|-----------------|----------------|
| [Screen] | [Yes/No] | [Yes/Technical msg/Crash] |

#### 2.4 Transitions and Animations

| Transition | Present | Smooth? |
|------------|---------|---------|
| Screen navigation | [Yes/No] | [Smooth/Jarring/None] |
| List item changes | [Yes/No] | [Animated/Jump] |
| State changes | [Yes/No] | [Smooth/Instant] |

---

### Phase 3: Edge Cases

#### 3.1 Long Text Handling

```kotlin
// Check for text overflow handling
Text(
    text = longText,
    maxLines = 2,
    overflow = TextOverflow.Ellipsis // Proper handling?
)
```

| Location | Handles Long Text? | Method |
|----------|-------------------|--------|
| [Screen/Component] | [Yes/No] | [Ellipsis/Wrap/Clips] |

#### 3.2 Dark Mode

| Aspect | Light Mode | Dark Mode | Consistent? |
|--------|------------|-----------|-------------|
| Colors | [Good] | [Good/Issues] | [Yes/No] |
| Images | [OK] | [Visible?] | [Yes/No] |
| Elevation | [Clear] | [Visible?] | [Yes/No] |

#### 3.3 Large Font Support

| Screen | Works at 200%? | Issues |
|--------|----------------|--------|
| [Screen] | [Yes/No] | [Overlaps/Clips/OK] |

---

### Phase 4: Polish Report

```markdown
## UI Polish Audit Report

### Overall Polish Score: [A-F]

| Category | Score | Major Issues |
|----------|-------|--------------|
| Visual Consistency | [1-10] | [Summary] |
| Loading/Empty/Error States | [1-10] | [Summary] |
| Transitions | [1-10] | [Summary] |
| Edge Cases | [1-10] | [Summary] |
| Dark Mode | [1-10] | [Summary] |

---

## Detailed Findings

### High Priority Polish Issues

| Issue | Location | Impact | Fix Effort |
|-------|----------|--------|------------|
| [Issue] | [Screen] | [User impact] | [Low/Med/High] |

### Consistency Issues

| Category | Issue | Locations | Recommendation |
|----------|-------|-----------|----------------|
| Spacing | [Inconsistent] | [Screens] | [Use 8dp grid] |
| Typography | [Mixed sizes] | [Screens] | [Define type scale] |

### Missing States

| Screen | Missing | Priority |
|--------|---------|----------|
| [Screen] | Loading/Empty/Error | [High/Med/Low] |

---

## Polish Improvements

### Quick Wins
1. [Fast fix with high visual impact]
2. [Fast fix with high visual impact]

### Medium Effort
1. [Requires more work but valuable]

### Design System Needs
1. [Systematic improvement needed]

---

## Before/After Recommendations

### Example: [Screen Name]

**Current Issues:**
- [Issue 1]
- [Issue 2]

**Recommended Changes:**
- [Change 1]
- [Change 2]
```

---

## Expected Output

1. **Consistency Audit** - Visual inconsistencies identified
2. **State Coverage** - Missing loading/empty/error states
3. **Edge Case Handling** - Long text, dark mode, accessibility
4. **Polish Score** - Overall quality assessment
5. **Improvement Roadmap** - Prioritized fixes

---

## Techniques Used

- **ST-01** (Clear Objective): UI polish focus
- **RT-02** (Multi-Dimensional Analysis): Multiple UI aspects
- **ST-03** (Output Format Templates): Structured report
- **OC-05** (Severity Classification): Priority levels

---

## Related Prompts

- [android_compose_ui_analysis.md](../analysis/android_compose_ui_analysis.md) - Comprehensive UI review
- [android_accessibility_improvement.md](android_accessibility_improvement.md) - Accessibility focus
- [android_user_experience_enhancement.md](android_user_experience_enhancement.md) - UX improvements
