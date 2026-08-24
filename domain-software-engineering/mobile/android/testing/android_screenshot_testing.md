---
title: "Android Screenshot Testing"
category: mobile-development
description: "./gradlew recordPaparazziDebug"
tags:
  - android
  - mobile-development
  - testing
updated: "2026-03-19"
---

# Android Screenshot Testing

**Objective:** Implement screenshot testing (visual regression testing) for Android apps to catch unintended UI changes, validate design consistency, and ensure visual quality across different states and configurations.

**When to Use:** Use this prompt when establishing visual regression testing for a design system, when validating UI consistency across themes (light/dark mode), when protecting critical screens from visual regressions during refactoring, or when ensuring design spec compliance.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

1. **Testing Goals:**
   - "What UI components or screens need screenshot coverage?"
   - "Do you need to test multiple configurations (dark mode, locales, font sizes)?"

2. **Tool Preference:**
   - "Are you open to any screenshot testing library, or is there a preference?"
   - "Is there existing screenshot testing infrastructure?"

3. **CI/CD Considerations:**
   - "Where will screenshot tests run (local, CI)?"
   - "How should baseline images be stored (repo, cloud)?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before generating ANY test, you MUST:**

1. **Understand the UI components** - Read the actual composables/views to understand states and configurations.
2. **Check for existing screenshot tests** - Search for existing Paparazzi, Roborazzi, or other screenshot testing setup.
3. **Follow project conventions** - Match existing test naming, baseline storage, and configuration patterns.
4. **Provide specific, working tests** - All tests MUST include file paths and proper baseline handling.
5. **Include meaningful configurations** - Test different themes, locales, and states that matter.

**Adapting to existing screenshot patterns is required.** Match the project's screenshot testing approach.

### Quality Requirements

- ❌ Do NOT generate screenshot tests for every component (focus on critical UI)
- ❌ Do NOT ignore dark mode/light mode variations
- ❌ Do NOT use hardcoded preview data if production data patterns exist
- ❌ Do NOT skip baseline management instructions
- ✅ DO test multiple theme configurations
- ✅ DO provide clear baseline update instructions
- ✅ DO focus on screens/components with high visual regression risk
- ✅ DO specify exact file paths for all test files

---

### Phase 1: Setup

#### 1.1 Tool Selection

| Tool | Pros | Cons | Best For |
|------|------|------|----------|
| **Paparazzi** | Fast (JVM), no emulator | Compose only, limited interactions | Component libraries |
| **Roborazzi** | Robolectric-based, fast | Limited animations | Screen states |
| **Shot** | Established, good CI support | Requires emulator | Full screens |
| **Compose Preview Screenshot** | Official Google tool | Compose only | Preview-based testing |

#### 1.2 Paparazzi Setup (Recommended for Compose)

```kotlin
// build.gradle.kts (app module)
plugins {
    id("app.cash.paparazzi") version "1.3.2"
}

dependencies {
    testImplementation("app.cash.paparazzi:paparazzi:1.3.2")
}
```

#### 1.3 Roborazzi Setup (Alternative)

```kotlin
// build.gradle.kts
plugins {
    id("io.github.takahirom.roborazzi") version "1.7.0"
}

dependencies {
    testImplementation("io.github.takahirom.roborazzi:roborazzi:1.7.0")
    testImplementation("io.github.takahirom.roborazzi:roborazzi-compose:1.7.0")
}
```

---

### Phase 2: Component Screenshot Tests

#### 2.1 Paparazzi Component Tests

```kotlin
class ButtonScreenshotTest {

    @get:Rule
    val paparazzi = Paparazzi(
        deviceConfig = DeviceConfig.PIXEL_5,
        theme = "android:Theme.Material3.Light"
    )

    @Test
    fun primaryButton_default() {
        paparazzi.snapshot {
            AppTheme {
                PrimaryButton(
                    text = "Click Me",
                    onClick = {}
                )
            }
        }
    }

    @Test
    fun primaryButton_disabled() {
        paparazzi.snapshot {
            AppTheme {
                PrimaryButton(
                    text = "Click Me",
                    onClick = {},
                    enabled = false
                )
            }
        }
    }

    @Test
    fun primaryButton_loading() {
        paparazzi.snapshot {
            AppTheme {
                PrimaryButton(
                    text = "Click Me",
                    onClick = {},
                    isLoading = true
                )
            }
        }
    }
}
```

#### 2.2 Multi-Configuration Testing

```kotlin
class ThemeScreenshotTest {

    @get:Rule
    val paparazzi = Paparazzi()

    @Test
    fun card_lightTheme() {
        paparazzi.snapshot {
            AppTheme(darkTheme = false) {
                ItemCard(item = testItem)
            }
        }
    }

    @Test
    fun card_darkTheme() {
        paparazzi.snapshot {
            AppTheme(darkTheme = true) {
                ItemCard(item = testItem)
            }
        }
    }
}

// Parameterized testing for multiple configurations
@RunWith(Parameterized::class)
class ComponentConfigurationTest(
    private val config: TestConfig
) {
    @get:Rule
    val paparazzi = Paparazzi(
        deviceConfig = config.deviceConfig,
        theme = config.theme
    )

    @Test
    fun component_allConfigurations() {
        paparazzi.snapshot(name = config.name) {
            AppTheme(darkTheme = config.darkMode) {
                TestComponent()
            }
        }
    }

    data class TestConfig(
        val name: String,
        val deviceConfig: DeviceConfig,
        val theme: String,
        val darkMode: Boolean
    )

    companion object {
        @JvmStatic
        @Parameterized.Parameters(name = "{0}")
        fun configs() = listOf(
            TestConfig("phone_light", DeviceConfig.PIXEL_5, "Theme.Material3.Light", false),
            TestConfig("phone_dark", DeviceConfig.PIXEL_5, "Theme.Material3.Dark", true),
            TestConfig("tablet_light", DeviceConfig.NEXUS_10, "Theme.Material3.Light", false),
        )
    }
}
```

---

### Phase 3: Screen State Screenshots

#### 3.1 All Screen States

```kotlin
class FeatureScreenScreenshotTest {

    @get:Rule
    val paparazzi = Paparazzi(
        deviceConfig = DeviceConfig.PIXEL_5
    )

    @Test
    fun screen_loading() {
        paparazzi.snapshot {
            FeatureScreen(
                uiState = FeatureUiState(isLoading = true),
                onEvent = {}
            )
        }
    }

    @Test
    fun screen_empty() {
        paparazzi.snapshot {
            FeatureScreen(
                uiState = FeatureUiState(
                    isLoading = false,
                    items = emptyList()
                ),
                onEvent = {}
            )
        }
    }

    @Test
    fun screen_content() {
        paparazzi.snapshot {
            FeatureScreen(
                uiState = FeatureUiState(
                    isLoading = false,
                    items = testItems
                ),
                onEvent = {}
            )
        }
    }

    @Test
    fun screen_error() {
        paparazzi.snapshot {
            FeatureScreen(
                uiState = FeatureUiState(
                    isLoading = false,
                    error = "Something went wrong"
                ),
                onEvent = {}
            )
        }
    }

    private val testItems = listOf(
        Item("1", "First Item", "Description"),
        Item("2", "Second Item", "Description"),
        Item("3", "Third Item", "Description")
    )
}
```

#### 3.2 Edge Case Screenshots

```kotlin
class EdgeCaseScreenshotTest {

    @get:Rule
    val paparazzi = Paparazzi()

    @Test
    fun longText_wrapsCorrectly() {
        paparazzi.snapshot {
            ItemCard(
                item = Item(
                    id = "1",
                    title = "This is a very long title that should wrap to multiple lines correctly",
                    subtitle = "This subtitle is also quite long and tests text wrapping behavior"
                )
            )
        }
    }

    @Test
    fun specialCharacters_displayCorrectly() {
        paparazzi.snapshot {
            ItemCard(
                item = Item(
                    id = "1",
                    title = "Price: $99.99 (50% off!)",
                    subtitle = "Email: test@example.com"
                )
            )
        }
    }

    @Test
    fun emptyState_placeholder() {
        paparazzi.snapshot {
            ItemCard(
                item = Item(
                    id = "1",
                    title = "",
                    subtitle = ""
                )
            )
        }
    }
}
```

---

### Phase 4: CI Integration

#### 4.1 Gradle Tasks

```bash
# Record new baseline images
./gradlew recordPaparazziDebug

# Verify against baseline
./gradlew verifyPaparazziDebug

# Update specific test
./gradlew recordPaparazziDebug --tests "ComponentScreenshotTest.button_primary"
```

#### 4.2 GitHub Actions Workflow

```yaml
name: Screenshot Tests

on:
  pull_request:
    paths:
      - 'app/src/main/**/*.kt'
      - 'app/src/test/**/screenshot/**'

jobs:
  screenshot-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up JDK
        uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'

      - name: Run screenshot tests
        run: ./gradlew verifyPaparazziDebug

      - name: Upload failure diffs
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: screenshot-failures
          path: app/build/paparazzi/failures/
```

#### 4.3 Baseline Management

```markdown
## Baseline Image Guidelines

### Storage
- Store in `app/src/test/snapshots/` (committed to repo)
- Use Git LFS for large baseline sets
- Include in `.gitattributes`: `*.png filter=lfs diff=lfs merge=lfs`

### Naming Convention
- `[ClassName]_[testMethodName].png`
- Example: `ButtonScreenshotTest_primaryButton_default.png`

### Updating Baselines
1. Review visual diff in CI artifacts
2. If intentional: `./gradlew recordPaparazziDebug`
3. Commit updated baselines with descriptive message
4. Include "visual change" label on PR
```

---

## Expected Output

```markdown
## Screenshot Tests for [Component/Screen]

### Test Matrix
| Component | States | Configurations | Total Screenshots |
|-----------|--------|----------------|-------------------|
| [Name] | [X] | [Light/Dark/Tablet] | [X] |

### Coverage
- [ ] All user-visible states (loading, content, error, empty)
- [ ] Theme variations (light/dark)
- [ ] Device sizes (phone/tablet)
- [ ] Edge cases (long text, special characters)

### Generated Tests
[Complete test class]

### CI Configuration
[Workflow file for screenshot verification]
```

---

## Best Practices

### Deterministic Screenshots
```kotlin
// Use fixed data, not random
private val testItem = Item(
    id = "test-id",
    title = "Test Title",
    createdAt = 1700000000000L // Fixed timestamp
)

// Disable animations
@get:Rule
val paparazzi = Paparazzi(
    renderingMode = RenderingMode.SHRINK // Consistent sizing
)
```

### Organize by Feature
```
src/test/kotlin/
└── screenshot/
    ├── components/
    │   ├── ButtonScreenshotTest.kt
    │   └── CardScreenshotTest.kt
    ├── screens/
    │   ├── HomeScreenScreenshotTest.kt
    │   └── DetailScreenScreenshotTest.kt
    └── themes/
        └── ThemeScreenshotTest.kt
```

---

## Techniques Used

- **ST-01** (Clear Objective): Visual regression testing setup
- **RT-04** (Best Practice Review): Screenshot testing patterns
- **ST-03** (Output Format Templates): Organized test structure

---

## Related Prompts

- [android_test_strategy_design.md](android_test_strategy_design.md) - Include screenshots in strategy
- [android_compose_ui_testing.md](android_compose_ui_testing.md) - Functional UI tests
- [android_ui_polish_audit.md](../improvement/android_ui_polish_audit.md) - Visual consistency audit
