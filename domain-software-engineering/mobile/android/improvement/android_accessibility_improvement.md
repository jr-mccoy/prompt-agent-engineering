---
title: "Android Accessibility Improvement"
category: mobile-development
description: "Audits and improves Android accessibility ensuring usability for people with disabilities and compliance with standards"
techniques:
  - ST-01
  - RT-04
  - ST-03
  - OC-05
difficulty: intermediate
tags:
  - android
  - mobile-development
  - accessibility
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/improvement/android_ui_polish_audit.md
  - domain-software-engineering/mobile/android/improvement/android_user_experience_enhancement.md
---

# Android Accessibility Improvement

**Objective:** Audit and improve Android app accessibility, ensuring the app is usable by people with disabilities and compliant with accessibility standards.

**When to Use:** Use this prompt before app store submissions, when accessibility complaints are received, for compliance with accessibility laws (ADA, Section 508), or as part of inclusive design initiatives.

**Prompt Type:** Comprehensive (300-400 lines)

---

## Context Gathering

1. **Current State:**
   - "Has the app been tested with TalkBack or other accessibility services?"
   - "Are there known accessibility issues or complaints?"

2. **Requirements:**
   - "Do you need to meet specific compliance standards (WCAG 2.1, Section 508)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual accessibility barriers** - Don't flag based on pattern matching alone. Verify with TalkBack or Accessibility Scanner that issues exist.
2. **Check for existing accessibility support** - Search for contentDescription, semantics, or accessibility handling that may already address concerns.
3. **Understand the context** - Consider WHY certain patterns exist. Some decorative elements intentionally don't need descriptions.
4. **Confirm actual impact** - Test with real accessibility services to verify the issue affects users.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `IconButton.kt:34`).

**Finding GOOD accessibility is an acceptable outcome.** If the app is reasonably accessible, say so with confidence. Don't manufacture accessibility concerns.

### False-Positive Prevention

- ❌ Do NOT flag decorative images as missing contentDescription (they should use null)
- ❌ Do NOT flag based solely on missing attributes without testing actual behavior
- ❌ Do NOT assume issues without testing with TalkBack
- ❌ Do NOT report WCAG recommendations as hard requirements without checking compliance needs
- ✅ DO test with TalkBack and Accessibility Scanner
- ✅ DO understand the difference between decorative and informative elements
- ✅ DO check for semantic grouping and custom actions
- ✅ DO consider color contrast and touch target sizes

---

### Phase 1: Accessibility Audit

#### 1.1 Content Descriptions

**Image and Icon Accessibility:**

```kotlin
// Check all images and icons
Image(
    painter = painterResource(R.drawable.icon),
    contentDescription = "..." // Present? Meaningful?
)

// Decorative images should be null
Image(
    painter = painterResource(R.drawable.decorative),
    contentDescription = null // Correctly null for decorative
)
```

| Component Type | Total | Has Description | Quality |
|----------------|-------|-----------------|---------|
| ImageViews/Images | [X] | [X] | [Good/Poor/Missing] |
| ImageButtons | [X] | [X] | [Good/Poor/Missing] |
| Icons | [X] | [X] | [Good/Poor/Missing] |

#### 1.2 Touch Targets

```kotlin
// Minimum 48dp x 48dp recommended
// Check all interactive elements

// Good
Modifier.size(48.dp).clickable { }

// Bad - too small
Modifier.size(24.dp).clickable { }

// Fix with minimum touch target
Modifier.defaultMinSize(minWidth = 48.dp, minHeight = 48.dp)
```

| Component | Size | Meets 48dp? | Fix Needed |
|-----------|------|-------------|------------|
| [Component] | [Xdp x Xdp] | [Yes/No] | [Yes/No] |

#### 1.3 Color Contrast

**WCAG AA Requirements:**
- Normal text: 4.5:1 contrast ratio
- Large text (18sp+ or 14sp+ bold): 3:1 contrast ratio

| Text Element | Foreground | Background | Ratio | Passes? |
|--------------|------------|------------|-------|---------|
| Body text | [#XXXXXX] | [#XXXXXX] | [X:1] | [Yes/No] |
| Button text | [#XXXXXX] | [#XXXXXX] | [X:1] | [Yes/No] |
| Error text | [#XXXXXX] | [#XXXXXX] | [X:1] | [Yes/No] |

#### 1.4 Screen Reader Navigation

```kotlin
// Check for proper heading structure
Text(
    text = "Section Title",
    modifier = Modifier.semantics { heading() }
)

// Check for reading order
Column(
    modifier = Modifier.semantics { traversalIndex = 1f }
)

// Check for grouping related content
Row(
    modifier = Modifier.semantics(mergeDescendants = true) {
        contentDescription = "Item: Product name, $19.99"
    }
)
```

#### 1.5 Form Accessibility

```kotlin
// Labels for input fields
TextField(
    value = email,
    onValueChange = { email = it },
    label = { Text("Email address") }, // Present?
    supportingText = { Text("Enter your email") } // Helper text?
)

// Error announcements
TextField(
    isError = hasError,
    supportingText = {
        if (hasError) Text("Invalid email format")
    }
)
```

---

### Phase 2: Accessibility Testing Checklist

#### 2.1 TalkBack Testing

| Test | Result | Issues |
|------|--------|--------|
| All interactive elements focusable | [Pass/Fail] | [Details] |
| Meaningful focus order | [Pass/Fail] | [Details] |
| All images have descriptions | [Pass/Fail] | [Details] |
| Forms are labeled | [Pass/Fail] | [Details] |
| State changes announced | [Pass/Fail] | [Details] |

#### 2.2 Switch Access Testing

| Test | Result | Issues |
|------|--------|--------|
| All targets reachable | [Pass/Fail] | [Details] |
| Focus visible | [Pass/Fail] | [Details] |
| No focus traps | [Pass/Fail] | [Details] |

#### 2.3 Magnification Testing

| Test | Result | Issues |
|------|--------|--------|
| Content visible when zoomed | [Pass/Fail] | [Details] |
| No overlapping elements | [Pass/Fail] | [Details] |
| Text scales properly | [Pass/Fail] | [Details] |

---

### Phase 3: Accessibility Fixes

```kotlin
// Fix: Add content descriptions
Image(
    painter = painterResource(R.drawable.user_avatar),
    contentDescription = "User profile picture" // Was null
)

// Fix: Increase touch target
IconButton(
    onClick = { },
    modifier = Modifier.size(48.dp) // Was 24.dp
) {
    Icon(
        imageVector = Icons.Default.Close,
        contentDescription = "Close dialog"
    )
}

// Fix: Improve color contrast
// Before: Text color #AAAAAA on white (#FFFFFF) = 2.3:1
// After: Text color #666666 on white (#FFFFFF) = 5.7:1

// Fix: Add semantic information
@Composable
fun ProductCard(product: Product) {
    Card(
        modifier = Modifier.semantics(mergeDescendants = true) {
            contentDescription = "${product.name}, ${product.price}"
        }
    ) {
        // Card content
    }
}

// Fix: Live region for dynamic content
Text(
    text = statusMessage,
    modifier = Modifier.semantics {
        liveRegion = LiveRegionMode.Polite
    }
)
```

---

### Phase 4: Accessibility Report

```markdown
## Accessibility Audit Report

### Overall Accessibility Score: [A-F]

| Category | Score | Issues |
|----------|-------|--------|
| Content Descriptions | [1-10] | [Count] |
| Touch Targets | [1-10] | [Count] |
| Color Contrast | [1-10] | [Count] |
| Screen Reader | [1-10] | [Count] |
| Keyboard/Switch | [1-10] | [Count] |

### WCAG 2.1 AA Compliance

| Criterion | Status | Notes |
|-----------|--------|-------|
| 1.1.1 Non-text Content | [Pass/Fail] | |
| 1.4.3 Contrast (Minimum) | [Pass/Fail] | |
| 2.1.1 Keyboard | [Pass/Fail] | |
| 2.4.3 Focus Order | [Pass/Fail] | |
| 4.1.2 Name, Role, Value | [Pass/Fail] | |

---

## Issues by Priority

### Critical (Blocks Access)
| Issue | Location | Users Affected | Fix |
|-------|----------|----------------|-----|
| [Issue] | [Screen] | [Who] | [Solution] |

### High (Significantly Impacts)
| Issue | Location | Users Affected | Fix |
|-------|----------|----------------|-----|
| [Issue] | [Screen] | [Who] | [Solution] |

### Medium (Degrades Experience)
| Issue | Location | Fix |
|-------|----------|-----|
| [Issue] | [Screen] | [Solution] |

---

## Implementation Plan

### Immediate Fixes (This Sprint)
1. [Add missing content descriptions] - [X instances]
2. [Fix touch target sizes] - [X instances]

### Short-term (Next Sprint)
1. [Improve color contrast]
2. [Add heading structure]

### Long-term
1. [Comprehensive TalkBack testing]
2. [Accessibility testing in CI]
```

---

## Expected Output

1. **Accessibility Audit** - Current state assessment
2. **WCAG Compliance Check** - Standards compliance status
3. **Issue Prioritization** - By impact and user group
4. **Fix Recommendations** - Specific code changes
5. **Implementation Plan** - Phased improvement roadmap

---

## Techniques Used

- **ST-01** (Clear Objective): Accessibility focus
- **RT-04** (Best Practice Review): Accessibility standards
- **ST-03** (Output Format Templates): Structured audit
- **OC-05** (Severity Classification): Impact-based priority

---

## Related Prompts

- [android_ui_polish_audit.md](android_ui_polish_audit.md) - UI quality
- [android_user_experience_enhancement.md](android_user_experience_enhancement.md) - UX improvements
