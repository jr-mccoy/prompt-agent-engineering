---
title: "To-Do App UI Polish Implementation Plan"
category: engineering-workflows/workflows
description: "Produce a prioritized, task-by-task implementation plan to polish a Jetpack Compose UI to production quality — each task with the problem, the file to find, before/after Kotlin, and a visual verification step."
techniques:
  - ST-01
  - ST-02
  - DS-06
  - DS-03
  - QA-01
difficulty: intermediate
tags:
  - jetpack-compose
  - android
  - ui-polish
  - implementation-plan
  - design-system
updated: "2026-06-07"
related_prompts:
  - domain-engineering-workflows/tasks/task_sorting_kotlin_implementation_verifier.md
  - domain-engineering-workflows/improvement/improvement_refactoring.md
  - domain-engineering-workflows/workflows/debug_prompt.md
---

# To-Do App UI Polish Implementation Plan

**Objective:** Produce a prioritized, task-by-task plan to polish a Jetpack Compose To-Do UI to production quality — each task naming the problem, the likely file, before/after Kotlin, and a visual verification step — driven by screenshot analysis and applied to the real Compose codebase.

**When to use:**
- Elevating a working but rough Compose UI to production polish.
- Translating screenshot/design feedback into concrete Compose edits.
- Producing a reviewable, sequenced set of UI tasks for an engineer or agent.

**When NOT to use:**
- Non-Compose / non-Android UIs (the Kotlin/Compose specifics won't apply).
- Functional bug fixing — use `debug_prompt.md`.
- General code refactoring — use `improvement_refactoring.md`.

**Audience:** Android engineers (or a coding agent) polishing a Jetpack Compose UI.

---

## Inputs / Context

The user supplies:
1. **Screenshots/recordings** of the current UI showing the issues.
2. **The Compose codebase** — file names/paths for the relevant screens, bottom sheets, and theme.
3. **Design intent** — palette, dark/light theme, brand accents (or accept the recommended palette below).
4. **Constraints** — min SDK, design-system rules, components that must not change.

Because exact file names vary, each task gives the likely file and a "find code similar to" anchor; verify against the real source before editing.

---

## Constraints

### Must
- Prioritize tasks (high-impact visibility/contrast first); each task is independently applyable.
- For each task: the problem, the likely file, a "find similar to" anchor, before/after Kotlin, and a visual verification.
- Respect the theme (dark/light) and a consistent accent palette; standardize spacing on an 8dp grid.
- Keep touch targets ≥48dp and contrast accessible.

### Must Not
- Assume exact file names — provide anchors and tell the implementer to verify.
- Hardcode colors where a theme token exists (prefer `MaterialTheme.colorScheme` / a central theme).
- Change behavior/functionality under the guise of polish.
- Invent screenshot details not actually shown.

---

## Document Purpose
This plan provides detailed, sequenced instructions for polishing a Jetpack Compose To-Do application UI. It is based on screenshot analysis and should be applied to the actual codebase containing the Compose UI files.

---

## Executive Summary

**Goal:** Elevate the existing To-Do app UI to production-ready quality through targeted refinements.

**Key Focus Areas:**
1. Typography contrast and hierarchy improvements
2. Color harmonization (unified accent palette with distinct orange Cancel)
3. Component consistency and selection state clarity
4. Spacing standardization on 8dp grid
5. User-friendly data display (location formatting)
6. Sort popup dark theme compliance (fix white background)

**Estimated Effort:** 2-4 hours of implementation time

---

## Color Palette Reference

### Recommended Theme Colors

```kotlin
// Primary palette (blue family - matches existing dropdown gradients)
val PrimaryBlue = Color(0xFF5E8BFF)
val PrimaryBlueLight = Color(0xFF8AABFF)
val PrimaryContainer = Color(0xFF1E3A5F)

// Cancel/Destructive accent (orange family - BRIGHT and DISTINCT)
val CancelOrange = Color(0xFFFF9853)        // Bright, warm orange
val CancelOrangeAlt = Color(0xFFFFAB6B)     // Slightly lighter variant
val CancelOrangeVibrant = Color(0xFFFF8A3D) // More saturated option

// Surface colors (existing dark theme)
val SurfaceDark = Color(0xFF0D1B2A)         // Main background
val SurfaceContainer = Color(0xFF1B2838)    // Cards, bottom sheet
val SurfaceElevated = Color(0xFF243447)     // Elevated components

// Text colors
val OnSurfaceHigh = Color(0xFFE8EDF3)       // 87% - Primary text
val OnSurfaceMedium = Color(0xFFB0B8C1)     // 60% - Secondary text
val OnSurfaceLow = Color(0xFF6B7280)        // 38% - Disabled/hint

// Accent for selections
val SelectionPurple = Color(0xFF7C4DFF)     // Keep for priority star
```

---

## Implementation Tasks (In Priority Order)

### Task 1: Fix "New task" Title Visibility

**Problem:** Title appears at ~40% opacity, making the modal feel unnamed.

**File to modify:** Look for `NewTaskBottomSheet.kt`, `AddTaskSheet.kt`, or similar.

**Find code similar to:**
```kotlin
Text(
    text = "New task",
    color = Color.White.copy(alpha = 0.4f),
    // or
    color = SomeColor.copy(alpha = 0.38f),
    // or using a dim style
)
```

**Replace with:**
```kotlin
Text(
    text = "New task",
    style = MaterialTheme.typography.titleLarge,
    fontWeight = FontWeight.SemiBold,
    color = MaterialTheme.colorScheme.onSurface, // Full 87% opacity
    modifier = Modifier.padding(vertical = 16.dp)
)
```

**Verification:** Title should be clearly readable, same brightness as input field label.

---

### Task 2: Brighten Cancel Button (Orange Family)

**Problem:** Current coral/salmon color is too muted and doesn't pop.

**Design Decision:** Keep orange family but make it BRIGHT and DISTINCT.

**File to modify:** Same bottom sheet file, look for Cancel button.

**Find code similar to:**
```kotlin
TextButton(onClick = onDismiss) {
    Text(
        text = "Cancel",
        color = Color(0xFFE57373), // Muted coral
        // or
        color = Color(0xFFCF6679), // Pink-ish
    )
}
```

**Replace with:**
```kotlin
TextButton(onClick = onDismiss) {
    Text(
        text = "Cancel",
        color = Color(0xFFFF9853), // Bright warm orange
        fontWeight = FontWeight.Medium,
        style = MaterialTheme.typography.labelLarge
    )
}
```

**Alternative orange options to try:**
```kotlin
// Option A: Warm bright orange (RECOMMENDED)
color = Color(0xFFFF9853)

// Option B: Slightly more saturated/punchy
color = Color(0xFFFF8A3D)

// Option C: Lighter, friendlier
color = Color(0xFFFFAB6B)

// Option D: If you want it even more vibrant
color = Color(0xFFFF7B2E)
```

**Verification:** Cancel should be immediately visible, clearly distinct from other elements, and feel intentional (not accidental or error-like).

---

### Task 3: Activate Save Button Appearance

**Problem:** Save button looks disabled/muted even when the form is valid.

**File to modify:** Same bottom sheet file.

**Find code similar to:**
```kotlin
TextButton(onClick = onSave) {
    Text("Save", color = Color.Gray)
}
// or
Button(
    onClick = onSave,
    colors = ButtonDefaults.buttonColors(
        containerColor = Color.Transparent
    )
)
```

**Replace with:**
```kotlin
FilledTonalButton(
    onClick = onSave,
    enabled = taskTitle.isNotBlank(), // Enable when there's content
    modifier = Modifier.defaultMinSize(minWidth = 72.dp),
    colors = ButtonDefaults.filledTonalButtonColors(
        containerColor = MaterialTheme.colorScheme.primaryContainer,
        contentColor = MaterialTheme.colorScheme.onPrimaryContainer,
        disabledContainerColor = MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.5f),
        disabledContentColor = MaterialTheme.colorScheme.onSurface.copy(alpha = 0.38f)
    ),
    shape = RoundedCornerShape(8.dp)
) {
    Text(
        text = "Save",
        fontWeight = FontWeight.Medium
    )
}
```

**Or if you prefer to keep it as text button but visible:**
```kotlin
TextButton(
    onClick = onSave,
    enabled = taskTitle.isNotBlank()
) {
    Text(
        text = "Save",
        color = if (taskTitle.isNotBlank()) {
            MaterialTheme.colorScheme.primary
        } else {
            MaterialTheme.colorScheme.onSurface.copy(alpha = 0.38f)
        },
        fontWeight = FontWeight.SemiBold
    )
}
```

**Verification:** Save should look clickable and ready when task field has content.

---

### Task 4: Harmonize Task Input Field Border

**Problem:** Purple/magenta border clashes with blue accents used elsewhere.

**File to modify:** Same bottom sheet file, look for OutlinedTextField.

**Find code similar to:**
```kotlin
OutlinedTextField(
    value = taskTitle,
    onValueChange = { taskTitle = it },
    // Colors may be default or custom purple
)
```

**Replace with:**
```kotlin
OutlinedTextField(
    value = taskTitle,
    onValueChange = { taskTitle = it },
    modifier = Modifier.fillMaxWidth(),
    label = {
        Text(
            "Task",
            color = MaterialTheme.colorScheme.primary
        )
    },
    placeholder = {
        Text(
            "What needs to be done?",
            color = MaterialTheme.colorScheme.onSurface.copy(alpha = 0.5f)
        )
    },
    colors = OutlinedTextFieldDefaults.colors(
        focusedBorderColor = Color(0xFF5E8BFF),      // Blue to match dropdowns
        unfocusedBorderColor = MaterialTheme.colorScheme.outline.copy(alpha = 0.5f),
        focusedLabelColor = Color(0xFF5E8BFF),
        cursorColor = Color(0xFF5E8BFF),
        focusedTextColor = MaterialTheme.colorScheme.onSurface,
        unfocusedTextColor = MaterialTheme.colorScheme.onSurface
    ),
    shape = RoundedCornerShape(12.dp),
    singleLine = true
)
```

**Verification:** Input field border should feel like it belongs with the filter dropdowns above.

---

### Task 5: Improve Visibility Toggle Selection State

**Problem:** "Family" vs "Personal" selection is too subtle to distinguish.

**File to modify:** Look for visibility toggle component, might be inline or separate.

**Find code similar to:**
```kotlin
Row {
    Button(onClick = { visibility = "Family" }) {
        Text("Family")
    }
    Button(onClick = { visibility = "Personal" }) {
        Text("Personal")
    }
}
```

**Replace with complete component:**
```kotlin
@Composable
fun VisibilityToggleGroup(
    selectedVisibility: String,
    onVisibilitySelected: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    Column(modifier = modifier) {
        Text(
            text = "Visibility",
            style = MaterialTheme.typography.labelMedium,
            color = MaterialTheme.colorScheme.onSurface.copy(alpha = 0.6f),
            modifier = Modifier.padding(bottom = 8.dp)
        )

        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            listOf("Family", "Personal").forEach { option ->
                val isSelected = option == selectedVisibility

                Surface(
                    modifier = Modifier
                        .weight(1f)
                        .height(48.dp)
                        .clip(RoundedCornerShape(10.dp))
                        .clickable { onVisibilitySelected(option) },
                    color = if (isSelected) {
                        Color(0xFF5E8BFF).copy(alpha = 0.15f) // Light blue tint
                    } else {
                        MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.3f)
                    },
                    border = BorderStroke(
                        width = if (isSelected) 2.dp else 1.dp,
                        color = if (isSelected) {
                            Color(0xFF5E8BFF) // Solid blue border when selected
                        } else {
                            MaterialTheme.colorScheme.outline.copy(alpha = 0.3f)
                        }
                    ),
                    shape = RoundedCornerShape(10.dp)
                ) {
                    Box(
                        contentAlignment = Alignment.Center,
                        modifier = Modifier.fillMaxSize()
                    ) {
                        Text(
                            text = option,
                            style = MaterialTheme.typography.bodyMedium,
                            fontWeight = if (isSelected) FontWeight.SemiBold else FontWeight.Normal,
                            color = if (isSelected) {
                                Color(0xFF8AABFF) // Brighter blue text
                            } else {
                                MaterialTheme.colorScheme.onSurface.copy(alpha = 0.7f)
                            }
                        )
                    }
                }
            }
        }
    }
}
```

**Verification:** Selected option should be immediately obvious at a glance.

---

### Task 6: Enhance Bottom Sheet Drag Handle

**Problem:** Drag handle is nearly invisible.

**File to modify:** Top of bottom sheet content.

**Add or replace:**
```kotlin
// Add this at the very top of your bottom sheet Column
Box(
    modifier = Modifier
        .fillMaxWidth()
        .padding(top = 12.dp, bottom = 4.dp),
    contentAlignment = Alignment.Center
) {
    Surface(
        modifier = Modifier
            .width(36.dp)
            .height(4.dp),
        shape = RoundedCornerShape(2.dp),
        color = MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.4f)
    ) {}
}
```

**Verification:** Handle should be visible but not distracting.

---

### Task 7: Humanize Location Display

**Problem:** Raw coordinates "(31.2381, -85.4565)" mean nothing to users.

**File to modify:** Task item card component.

**Find code similar to:**
```kotlin
Text(
    text = "Near 4370 (${location.latitude}, ${location.longitude})"
)
```

**Replace with:**
```kotlin
// Option A: If you have reverse geocoding
Text(
    text = buildString {
        append("Near ")
        append(location.addressLine ?: location.locality ?: location.streetNumber ?: "")
        // Don't show coordinates at all, or show only if no address
    },
    style = MaterialTheme.typography.bodySmall,
    color = MaterialTheme.colorScheme.primary
)

// Option B: If you must show coordinates, format them nicely
Text(
    text = "📍 ${formatLocation(location)}",
    style = MaterialTheme.typography.bodySmall,
    color = MaterialTheme.colorScheme.primary
)

// Helper function
fun formatLocation(location: TaskLocation): String {
    return location.displayName
        ?: location.address
        ?: "%.2f°, %.2f°".format(location.latitude, location.longitude)
}
```

**Ideal solution:** Implement reverse geocoding on location save:
```kotlin
suspend fun getAddressFromCoordinates(lat: Double, lng: Double): String? {
    return try {
        val geocoder = Geocoder(context, Locale.getDefault())
        val addresses = geocoder.getFromLocation(lat, lng, 1)
        addresses?.firstOrNull()?.let { address ->
            listOfNotNull(
                address.thoroughfare,      // Street name
                address.subThoroughfare,   // Street number
                address.locality           // City
            ).joinToString(" ")
        }
    } catch (e: Exception) {
        null
    }
}
```

**Verification:** Location should read like "Near Main St" or "Near Downtown" not coordinates.

---

### Task 8: Standardize Spacing Throughout

**Problem:** Inconsistent spacing creates visual rhythm issues.

**Apply these spacing standards:**

```kotlin
// Bottom sheet content padding
Column(
    modifier = Modifier
        .fillMaxWidth()
        .padding(horizontal = 20.dp) // Consistent horizontal padding
        .padding(bottom = 24.dp),    // Bottom padding for gesture area
    verticalArrangement = Arrangement.spacedBy(16.dp) // Consistent vertical rhythm
) {
    // Header row (Cancel, Title, Save)
    // ...

    // Task input field
    // ...

    Spacer(modifier = Modifier.height(4.dp)) // Small break before options

    // Action buttons row 1 (Priority, Due date)
    Row(
        modifier = Modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        // buttons with Modifier.weight(1f)
    }

    // Action buttons row 2 (Repeat, Location)
    Row(
        modifier = Modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        // buttons with Modifier.weight(1f)
    }

    Spacer(modifier = Modifier.height(4.dp)) // Small break before visibility

    // Visibility toggle
    // ...
}
```

**Verification:** UI should feel balanced and intentional, not cramped or scattered.

---

### Task 9: Polish Action Buttons (Priority, Due date, Repeat, Location)

**Problem:** Buttons have inconsistent styling.

**Create a reusable component:**
```kotlin
@Composable
fun ActionOptionButton(
    text: String,
    icon: ImageVector,
    isSelected: Boolean = false,
    onClick: () -> Unit,
    modifier: Modifier = Modifier
) {
    OutlinedButton(
        onClick = onClick,
        modifier = modifier.height(48.dp),
        shape = RoundedCornerShape(10.dp),
        border = BorderStroke(
            width = 1.dp,
            color = if (isSelected) {
                Color(0xFF5E8BFF)
            } else {
                MaterialTheme.colorScheme.outline.copy(alpha = 0.4f)
            }
        ),
        colors = ButtonDefaults.outlinedButtonColors(
            containerColor = if (isSelected) {
                Color(0xFF5E8BFF).copy(alpha = 0.1f)
            } else {
                Color.Transparent
            },
            contentColor = if (isSelected) {
                Color(0xFF8AABFF)
            } else {
                MaterialTheme.colorScheme.onSurface.copy(alpha = 0.8f)
            }
        ),
        contentPadding = PaddingValues(horizontal = 12.dp)
    ) {
        Icon(
            imageVector = icon,
            contentDescription = null,
            modifier = Modifier.size(20.dp)
        )
        Spacer(modifier = Modifier.width(8.dp))
        Text(
            text = text,
            style = MaterialTheme.typography.bodyMedium,
            maxLines = 1,
            overflow = TextOverflow.Ellipsis
        )
    }
}

// Usage
Row(
    modifier = Modifier.fillMaxWidth(),
    horizontalArrangement = Arrangement.spacedBy(12.dp)
) {
    ActionOptionButton(
        text = "Priority",
        icon = if (isPriority) Icons.Filled.Star else Icons.Outlined.StarBorder,
        isSelected = isPriority,
        onClick = { isPriority = !isPriority },
        modifier = Modifier.weight(1f)
    )
    ActionOptionButton(
        text = dueDate?.format() ?: "Due date",
        icon = Icons.Outlined.Schedule,
        isSelected = dueDate != null,
        onClick = { showDatePicker = true },
        modifier = Modifier.weight(1f)
    )
}
```

---

### Task 10: Fix Sort Popup Background Color

**Problem:** The sort popup (DropdownMenu) on the Notes screen uses a default white/light background, which clashes with the app's dark theme. The popup showing "Newest first", "Recently edited", and "Alphabetical" options should use a dark surface color consistent with the rest of the UI.

**File to modify:** Look for `NotesScreen.kt`, `TaskListScreen.kt`, or wherever the sort DropdownMenu is defined.

**Find code similar to:**
```kotlin
DropdownMenu(
    expanded = showSortMenu,
    onDismissRequest = { showSortMenu = false }
) {
    DropdownMenuItem(
        text = { Text("Newest first") },
        onClick = { /* ... */ }
    )
    DropdownMenuItem(
        text = { Text("Recently edited") },
        onClick = { /* ... */ }
    )
    DropdownMenuItem(
        text = { Text("Alphabetical") },
        onClick = { /* ... */ }
    )
}
```

**Replace with:**
```kotlin
MaterialTheme(
    colorScheme = MaterialTheme.colorScheme.copy(
        surface = Color(0xFF1B2838),        // Dark surface for popup background
        onSurface = Color(0xFFE8EDF3)       // Light text for readability
    )
) {
    DropdownMenu(
        expanded = showSortMenu,
        onDismissRequest = { showSortMenu = false },
        modifier = Modifier.background(Color(0xFF1B2838)) // Explicit dark background
    ) {
        DropdownMenuItem(
            text = {
                Text(
                    "Newest first",
                    color = Color(0xFFE8EDF3) // High-emphasis text
                )
            },
            onClick = {
                sortOrder = SortOrder.NEWEST
                showSortMenu = false
            }
        )
        DropdownMenuItem(
            text = {
                Text(
                    "Recently edited",
                    color = Color(0xFFE8EDF3)
                )
            },
            onClick = {
                sortOrder = SortOrder.RECENTLY_EDITED
                showSortMenu = false
            }
        )
        DropdownMenuItem(
            text = {
                Text(
                    "Alphabetical",
                    color = Color(0xFFE8EDF3)
                )
            },
            onClick = {
                sortOrder = SortOrder.ALPHABETICAL
                showSortMenu = false
            }
        )
    }
}
```

**Alternative approach — Override via `DropdownMenuDefaults` or custom `MenuDefaults`:**
```kotlin
DropdownMenu(
    expanded = showSortMenu,
    onDismissRequest = { showSortMenu = false },
    modifier = Modifier
        .background(
            color = Color(0xFF1B2838),           // SurfaceContainer from theme
            shape = RoundedCornerShape(12.dp)
        )
) {
    val sortOptions = listOf(
        "Newest first" to SortOrder.NEWEST,
        "Recently edited" to SortOrder.RECENTLY_EDITED,
        "Alphabetical" to SortOrder.ALPHABETICAL
    )
    sortOptions.forEach { (label, order) ->
        val isSelected = sortOrder == order
        DropdownMenuItem(
            text = {
                Text(
                    text = label,
                    color = if (isSelected) {
                        Color(0xFF8AABFF) // Primary blue light for selected item
                    } else {
                        Color(0xFFE8EDF3) // Standard high-emphasis text
                    },
                    fontWeight = if (isSelected) FontWeight.SemiBold else FontWeight.Normal
                )
            },
            onClick = {
                sortOrder = order
                showSortMenu = false
            },
            leadingIcon = if (isSelected) {
                {
                    Icon(
                        imageVector = Icons.Default.Check,
                        contentDescription = null,
                        tint = Color(0xFF8AABFF),
                        modifier = Modifier.size(18.dp)
                    )
                }
            } else null
        )
    }
}
```

**Best approach — Set the popup background in the app theme globally:**

If using a custom theme, set the popup/menu surface color in your `Theme.kt`:
```kotlin
private val DarkColorScheme = darkColorScheme(
    surface = Color(0xFF0D1B2A),               // Main background
    surfaceContainer = Color(0xFF1B2838),       // Cards, bottom sheets, popups
    surfaceContainerHigh = Color(0xFF243447),   // Elevated components
    onSurface = Color(0xFFE8EDF3),             // Primary text
    onSurfaceVariant = Color(0xFFB0B8C1),      // Secondary text
    primary = Color(0xFF5E8BFF),               // Primary accent
    // ...
)
```

This ensures all `DropdownMenu`, `ExposedDropdownMenu`, and popup surfaces inherit the dark theme automatically, eliminating the white background without per-component overrides.

**Root Cause:** Jetpack Compose `DropdownMenu` uses `MaterialTheme.colorScheme.surface` for its background. If the app theme doesn't override this value for dark mode, or if the popup is rendered outside the themed scope, it falls back to the default light surface color (white).

**Verification:**
- Sort popup background matches app dark theme (`#1B2838` or `#243447`)
- Text on popup is readable with high contrast (`#E8EDF3`)
- Selected sort option is visually distinguishable
- Popup shadow/elevation blends with dark background
- No flash of white when popup opens

---

## Complete Bottom Sheet Structure Example

Here's how the polished bottom sheet should be structured:

```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun NewTaskBottomSheet(
    onDismiss: () -> Unit,
    onSave: (Task) -> Unit,
    sheetState: SheetState
) {
    var taskTitle by remember { mutableStateOf("") }
    var isPriority by remember { mutableStateOf(false) }
    var dueDate by remember { mutableStateOf<LocalDate?>(null) }
    var repeatInterval by remember { mutableStateOf<RepeatInterval?>(null) }
    var location by remember { mutableStateOf<TaskLocation?>(null) }
    var visibility by remember { mutableStateOf("Family") }

    ModalBottomSheet(
        onDismissRequest = onDismiss,
        sheetState = sheetState,
        containerColor = Color(0xFF1B2838), // Surface container color
        dragHandle = {
            // Enhanced drag handle
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(top = 12.dp, bottom = 4.dp),
                contentAlignment = Alignment.Center
            ) {
                Surface(
                    modifier = Modifier.width(36.dp).height(4.dp),
                    shape = RoundedCornerShape(2.dp),
                    color = Color.White.copy(alpha = 0.3f)
                ) {}
            }
        }
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = 20.dp)
                .padding(bottom = 32.dp)
                .navigationBarsPadding(),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            // Header Row
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
                verticalAlignment = Alignment.CenterVertically
            ) {
                // CANCEL - Bright Orange
                TextButton(onClick = onDismiss) {
                    Text(
                        text = "Cancel",
                        color = Color(0xFFFF9853), // BRIGHT ORANGE
                        fontWeight = FontWeight.Medium,
                        style = MaterialTheme.typography.labelLarge
                    )
                }

                // TITLE - Full visibility
                Text(
                    text = "New task",
                    style = MaterialTheme.typography.titleLarge,
                    fontWeight = FontWeight.SemiBold,
                    color = Color(0xFFE8EDF3) // 87% white
                )

                // SAVE - Visible and actionable
                FilledTonalButton(
                    onClick = {
                        onSave(Task(
                            title = taskTitle,
                            isPriority = isPriority,
                            dueDate = dueDate,
                            repeatInterval = repeatInterval,
                            location = location,
                            visibility = visibility
                        ))
                    },
                    enabled = taskTitle.isNotBlank(),
                    colors = ButtonDefaults.filledTonalButtonColors(
                        containerColor = Color(0xFF1E3A5F),
                        contentColor = Color(0xFF8AABFF)
                    ),
                    shape = RoundedCornerShape(8.dp)
                ) {
                    Text("Save", fontWeight = FontWeight.Medium)
                }
            }

            // Task Input - Blue border to match theme
            OutlinedTextField(
                value = taskTitle,
                onValueChange = { taskTitle = it },
                modifier = Modifier.fillMaxWidth(),
                label = { Text("Task") },
                placeholder = { Text("What needs to be done?") },
                colors = OutlinedTextFieldDefaults.colors(
                    focusedBorderColor = Color(0xFF5E8BFF),
                    unfocusedBorderColor = Color.White.copy(alpha = 0.2f),
                    focusedLabelColor = Color(0xFF5E8BFF),
                    cursorColor = Color(0xFF5E8BFF)
                ),
                shape = RoundedCornerShape(12.dp),
                singleLine = true
            )

            // Action Buttons Row 1
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                ActionOptionButton(
                    text = "Priority",
                    icon = if (isPriority) Icons.Filled.Star else Icons.Outlined.StarBorder,
                    isSelected = isPriority,
                    onClick = { isPriority = !isPriority },
                    modifier = Modifier.weight(1f)
                )
                ActionOptionButton(
                    text = dueDate?.format(DateTimeFormatter.ofPattern("MMM d")) ?: "Due date",
                    icon = Icons.Outlined.Schedule,
                    isSelected = dueDate != null,
                    onClick = { /* show date picker */ },
                    modifier = Modifier.weight(1f)
                )
            }

            // Action Buttons Row 2
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                ActionOptionButton(
                    text = repeatInterval?.displayName ?: "Repeat",
                    icon = Icons.Outlined.Repeat,
                    isSelected = repeatInterval != null,
                    onClick = { /* show repeat picker */ },
                    modifier = Modifier.weight(1f)
                )
                ActionOptionButton(
                    text = location?.shortDisplayName ?: "Location",
                    icon = Icons.Outlined.LocationOn,
                    isSelected = location != null,
                    onClick = { /* show location picker */ },
                    modifier = Modifier.weight(1f)
                )
            }

            Spacer(modifier = Modifier.height(4.dp))

            // Visibility Toggle
            VisibilityToggleGroup(
                selectedVisibility = visibility,
                onVisibilitySelected = { visibility = it }
            )
        }
    }
}
```

---

## Testing Checklist

After implementing changes, verify:

### Visual Verification
- [ ] "New task" title is clearly readable (not dim)
- [ ] "Cancel" is bright orange and stands out
- [ ] "Save" looks enabled when task title has text
- [ ] "Save" looks disabled when task title is empty
- [ ] Input field border is blue (matches filter dropdowns)
- [ ] Visibility toggle shows clear selected state
- [ ] Drag handle is visible at top of sheet
- [ ] Spacing feels balanced throughout
- [ ] Sort popup uses dark background (#1B2838), not white
- [ ] Sort popup text is readable on dark background
- [ ] Selected sort option is visually distinct
- [ ] All touch targets are at least 48dp

### Functional Verification
- [ ] Cancel dismisses the sheet
- [ ] Save creates task with all selected options
- [ ] Priority toggle works
- [ ] Date picker opens and sets date
- [ ] Repeat picker opens and sets interval
- [ ] Location picker opens and sets location
- [ ] Visibility toggle switches between options

### Dark Mode Verification
- [ ] All text has sufficient contrast
- [ ] No color banding or artifacts
- [ ] Selected states are visible
- [ ] Icons are visible against backgrounds

---

## Quick Reference: Color Values

```
Primary Blue:        #5E8BFF
Primary Blue Light:  #8AABFF
Primary Container:   #1E3A5F

CANCEL ORANGE:       #FF9853  ← Use this!
(Alt brighter):      #FF8A3D
(Alt lighter):       #FFAB6B

Surface Dark:        #0D1B2A
Surface Container:   #1B2838
Surface Elevated:    #243447

Text High:           #E8EDF3 (87%)
Text Medium:         #B0B8C1 (60%)
Text Low:            #6B7280 (38%)

Priority Star:       #7C4DFF (keep existing purple)
```

---

## Summary of Changes

| Element | Before | After |
|---------|--------|-------|
| "New task" title | ~40% opacity, invisible | 87% opacity, SemiBold |
| Cancel button | Muted coral #E57373 | Bright orange #FF9853 |
| Save button | Gray/muted always | Blue tonal, enabled state |
| Input border | Purple/magenta | Blue #5E8BFF |
| Visibility toggle | Subtle selection | Clear border + fill |
| Drag handle | Nearly invisible | 36x4dp, 40% opacity |
| Location text | Raw coordinates | Human-readable address |
| Spacing | Inconsistent | 20dp horizontal, 16dp vertical |
| Sort popup background | Default white/light surface | Dark surface #1B2838 matching theme |

---

*Document created for UI polish implementation. Apply these changes to your Jetpack Compose codebase.*

---

## False-Positive Prevention

❌ **DON'T:**
- Don't assume the exact file names — use the "find code similar to" anchors and verify against the real source first.
- Don't hardcode color hex values where a theme token exists; prefer `MaterialTheme.colorScheme` or a central theme.
- Don't alter behavior (save logic, navigation) while polishing visuals.
- Don't claim a screenshot shows something it doesn't — work only from what's visible.

✅ **DO:**
- Anchor each change to a "find similar to" snippet and confirm before editing.
- Keep changes theme-aware and on the 8dp spacing grid.
- Verify each task visually (contrast, selected state, dark mode) after applying.
- Keep touch targets ≥48dp and text contrast accessible.

---

## Verification

- [ ] Tasks prioritized; each is independently applyable.
- [ ] Every task has problem, likely file, anchor, before/after Kotlin, and a visual check.
- [ ] Colors use theme tokens where available; spacing on the 8dp grid.
- [ ] Dark/light theme handled (e.g. sort popup not white in dark mode).
- [ ] Touch targets ≥48dp; contrast accessible.
- [ ] No behavioral changes introduced; no invented screenshot details.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the production-polish goal for the Compose UI.
- **ST-02 (Structured Sequential Instructions):** Sequenced, numbered tasks from highest-impact down.
- **DS-06 (Prioritization and Severity Guidance):** Orders tasks by visual impact and effort.
- **DS-03 (Progressive Disclosure):** Per-task problem → file → before/after → verification structure.
- **QA-01 (Self-Verification):** Visual verification per task plus a final testing checklist.

---

## Related Prompts

- `domain-engineering-workflows/tasks/task_sorting_kotlin_implementation_verifier.md` — Verify the Kotlin quality of the changes.
- `domain-engineering-workflows/improvement/improvement_refactoring.md` — Refactor underlying components surfaced during polish.
- `domain-engineering-workflows/workflows/debug_prompt.md` — Fix functional bugs uncovered while polishing.
