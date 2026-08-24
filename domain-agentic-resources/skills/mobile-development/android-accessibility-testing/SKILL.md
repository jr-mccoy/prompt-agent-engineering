---
name: android-accessibility-testing
description: "Android-specific accessibility testing using ADB, Accessibility Scanner, TalkBack, and programmatic checks. Covers content descriptions, touch targets, color contrast, focus order, Compose semantics, and Play Store accessibility requirements. Use this skill when auditing app accessibility, fixing TalkBack issues, checking touch target sizes, verifying color contrast, or when a developer mentions 'accessibility', 'TalkBack', 'content description', 'touch target', 'a11y', or 'screen reader'."
metadata:
  tags:
    - android
    - accessibility
    - testing
    - talkback
    - compose
    - solo-developer
  updated: "2026-03-06"
---

# Android Accessibility Testing

Android-specific accessibility testing workflow covering TalkBack, Accessibility Scanner, programmatic checks, and Compose semantics. Catches the top 80% of accessibility issues in a 20-minute audit.

## Purpose

Accessibility makes your app usable by everyone, including the 15% of people worldwide who live with some form of disability. Solo developers often skip accessibility because they have no QA team or accessibility specialist. This skill provides a practical, checklist-based approach that catches the most impactful issues quickly — content descriptions, touch targets, color contrast, and focus order. These are also the issues that affect your Play Store rating and can lead to legal compliance requirements.

## When to Use This Skill

Use this skill when you need to:
- Audit an app for accessibility compliance before release
- Fix TalkBack navigation issues
- Verify touch target sizes meet the 48dp minimum
- Check color contrast ratios for text and interactive elements
- Add proper Compose semantics for screen readers
- Prepare for Play Store accessibility requirements
- Write automated accessibility tests

## When NOT to Use This Skill

Do NOT use this skill when:
- Testing web content accessibility (use `frontend_accessibility_wcag_audit` instead)
- Testing ARIA patterns for web (use `frontend_accessibility_aria_patterns`)
- The app is still in early prototyping (test accessibility once UI stabilizes)

## Prerequisites

- Android device or emulator with TalkBack available
- ADB connected to device
- App installed and navigable
- For automated tests: Espresso or Compose testing dependencies

## Step 1: Quick Accessibility Audit (20 minutes)

### 1.1 Enable TalkBack

```bash
# Enable TalkBack via ADB
adb shell settings put secure enabled_accessibility_services com.google.android.marvin.talkback/com.google.android.marvin.talkback.TalkBackService

# Enable accessibility
adb shell settings put secure accessibility_enabled 1

# Disable TalkBack when done
adb shell settings put secure enabled_accessibility_services ""
adb shell settings put secure accessibility_enabled 0
```

### 1.2 TalkBack Navigation Test

With TalkBack enabled, navigate through your main screens:

| Check | How to Test | Pass Criteria |
|-------|------------|---------------|
| Every element read | Swipe right through each screen | All interactive elements announced |
| Descriptions useful | Listen to announcements | Announcements describe function, not appearance |
| No "unlabeled button" | Swipe through buttons/icons | Every button has a content description |
| Reading order logical | Swipe through screen | Elements read in visual order (top-to-bottom, left-to-right) |
| Actions clear | Double-tap elements | "Double tap to activate" announced for buttons |
| State communicated | Toggle switches, select items | "Checked/unchecked", "selected" announced |

### 1.3 Content Description Audit

```bash
# Dump view hierarchy (look for missing contentDescription)
adb shell uiautomator dump /sdcard/ui_dump.xml
adb pull /sdcard/ui_dump.xml

# Search for elements without content descriptions
grep -c 'content-desc=""' ui_dump.xml
# Result should be 0 for interactive elements (images/icons need descriptions)
```

**Common Missing Descriptions:**

```kotlin
// BAD: Icon button with no description
IconButton(onClick = { /* ... */ }) {
    Icon(Icons.Default.Settings, contentDescription = null)  // TalkBack says "Unlabeled"
}

// GOOD: Descriptive content description
IconButton(onClick = { /* ... */ }) {
    Icon(Icons.Default.Settings, contentDescription = "Settings")
}

// GOOD: Decorative image (no description needed)
Image(
    painter = painterResource(R.drawable.decorative_wave),
    contentDescription = null  // Explicitly null for decorative elements
)
```

## Step 2: Touch Target Verification

### 2.1 Minimum Size: 48dp x 48dp

```bash
# Check screen density
adb shell wm density
# Example output: Physical density: 420

# 48dp at 420dpi = 48 * (420/160) = 126 pixels minimum
```

### 2.2 Compose Touch Targets

```kotlin
// BAD: Small icon with no minimum touch target
Icon(Icons.Default.Close, contentDescription = "Close", modifier = Modifier.size(24.dp))

// GOOD: Wrap in IconButton (automatically provides 48dp touch target)
IconButton(onClick = { /* ... */ }) {
    Icon(Icons.Default.Close, contentDescription = "Close", modifier = Modifier.size(24.dp))
}

// GOOD: Add minimum touch target manually
Icon(
    Icons.Default.Close,
    contentDescription = "Close",
    modifier = Modifier
        .size(24.dp)
        .sizeIn(minWidth = 48.dp, minHeight = 48.dp)
        .clickable { /* ... */ }
)
```

### 2.3 View-Based Touch Targets

```xml
<!-- BAD: Small button -->
<ImageButton
    android:layout_width="24dp"
    android:layout_height="24dp" />

<!-- GOOD: Adequate touch target -->
<ImageButton
    android:layout_width="48dp"
    android:layout_height="48dp"
    android:padding="12dp" />
```

## Step 3: Color Contrast

### 3.1 WCAG Contrast Ratios

| Text Type | Minimum Ratio (AA) | Enhanced Ratio (AAA) |
|-----------|-------------------|---------------------|
| Normal text (<18sp) | 4.5:1 | 7:1 |
| Large text (≥18sp or ≥14sp bold) | 3:1 | 4.5:1 |
| Non-text (icons, borders) | 3:1 | — |

### 3.2 Common Problem Areas

- Light gray text on white background
- Disabled state text too low contrast
- Dark mode text colors not adjusted
- Placeholder text in input fields
- Status bar text on custom colored backgrounds

### 3.3 Checking Contrast Programmatically

```kotlin
// In tests, use Accessibility Scanner assertions
@Test
fun settingsScreen_meetsContrastRequirements() {
    composeTestRule.setContent {
        AppTheme {
            SettingsScreen()
        }
    }

    // Use Accessibility Test Framework
    composeTestRule.onRoot().assertHasNoAccessibilityIssues()
}
```

## Step 4: Compose Accessibility Semantics

### 4.1 Key Semantics Properties

```kotlin
// Headings (for navigation structure)
Text(
    "Account Settings",
    modifier = Modifier.semantics { heading() },
    style = MaterialTheme.typography.headlineMedium
)

// Custom actions
Box(
    modifier = Modifier.semantics {
        contentDescription = "Item: Wireless Headphones, $49.99"
        customActions = listOf(
            CustomAccessibilityAction("Add to cart") { addToCart(); true },
            CustomAccessibilityAction("Save for later") { saveForLater(); true }
        )
    }
)

// State descriptions
Switch(
    checked = isEnabled,
    onCheckedChange = { /* ... */ },
    modifier = Modifier.semantics {
        stateDescription = if (isEnabled) "Enabled" else "Disabled"
    }
)

// Merging children (treat group as one element)
Row(modifier = Modifier.semantics(mergeDescendants = true) {}) {
    Icon(Icons.Default.Email, contentDescription = null)
    Text("user@example.com")
}
// TalkBack reads: "user@example.com" (not "Email icon" then "user@example.com")
```

### 4.2 Focus Order

```kotlin
// Custom traversal order (when visual order differs from logical order)
val (first, second) = remember { FocusRequester.createRefs() }

Text("Title", modifier = Modifier
    .focusRequester(first)
    .focusProperties { next = second }
)

Button(onClick = {}, modifier = Modifier
    .focusRequester(second)
    .focusProperties { previous = first }
) {
    Text("Action")
}
```

## Step 5: Automated Accessibility Testing

### 5.1 Espresso Accessibility Checks

```kotlin
// Enable accessibility checks for all Espresso tests
@Before
fun setUp() {
    AccessibilityChecks.enable()
        .setRunChecksFromRootView(true)
}

@Test
fun homeScreen_passesAccessibilityChecks() {
    // Any Espresso interaction will also run accessibility checks
    onView(withId(R.id.settings_button)).perform(click())
    // Accessibility violations will fail the test
}
```

### 5.2 Compose Accessibility Assertions

```kotlin
@Test
fun settingsScreen_allElementsLabeled() {
    composeTestRule.setContent {
        AppTheme { SettingsScreen() }
    }

    // Check that all clickable elements have content descriptions
    composeTestRule
        .onAllNodes(hasClickAction())
        .assertAll(hasContentDescription())
}

@Test
fun settingsScreen_touchTargetsMet() {
    composeTestRule.setContent {
        AppTheme { SettingsScreen() }
    }

    // Check minimum touch target sizes
    composeTestRule
        .onAllNodes(hasClickAction())
        .assertAll(hasMinimumTouchTargetSize(48.dp, 48.dp))
}
```

## Step 6: Accessibility Scanner (Google's Tool)

```bash
# Install Accessibility Scanner
adb shell pm list packages | grep accessibility.scanner
# If not installed, install from Play Store or:
# https://play.google.com/store/apps/details?id=com.google.android.apps.accessibility.auditor

# Launch scanner
adb shell am start -n com.google.android.apps.accessibility.auditor/.ScannerActivity
```

Use the floating button overlay to scan each screen. The scanner checks:
- Touch target sizes
- Color contrast ratios
- Content labeling
- Implementation details

## Accessibility Checklist Summary

| # | Check | Priority | Time |
|---|-------|----------|------|
| 1 | All buttons/icons have content descriptions | Critical | 5 min |
| 2 | Touch targets ≥ 48dp | Critical | 5 min |
| 3 | TalkBack navigation works end-to-end | High | 10 min |
| 4 | Color contrast ≥ 4.5:1 for text | High | 5 min |
| 5 | Heading structure for navigation | Medium | 3 min |
| 6 | State changes announced | Medium | 5 min |
| 7 | Custom actions for complex widgets | Medium | 5 min |
| 8 | Dark mode accessibility | Medium | 5 min |
| 9 | Font scaling support (up to 200%) | Low | 3 min |
| 10 | Automated test coverage | Low | 15 min setup |

**80/20 rule:** Items 1-4 catch 80% of accessibility issues. Start there.

## Related Skills

- `android-testing-patterns` — General testing patterns including accessibility tests
- `jetpack-compose-patterns` — Compose UI patterns with built-in accessibility
- `android-adb-operations` — ADB commands for enabling/disabling accessibility services
- `android-screenshot-testing` — Visual testing across accessibility configurations
