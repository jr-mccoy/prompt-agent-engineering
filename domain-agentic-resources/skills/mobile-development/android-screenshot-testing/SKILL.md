---
name: android-screenshot-testing
description: "Screenshot-based UI testing for Android using ADB screen capture, Compose Preview Screenshot Testing, Paparazzi, and Roborazzi. Covers baseline capture, diff comparison, CI integration, and handling intentional UI changes. Use this skill when setting up visual regression testing, comparing UI across configurations, catching unintentional layout changes, or when a developer mentions 'screenshot testing', 'visual regression', 'Paparazzi', 'Roborazzi', or 'UI diff'."
metadata:
  tags:
    - android
    - testing
    - screenshots
    - visual-regression
    - compose
    - solo-developer
  updated: "2026-03-06"
---

# Android Screenshot Testing

Screenshot-based UI testing for Android apps. An automated "second pair of eyes" that catches unintentional visual regressions by comparing screenshots against golden baselines.

## Purpose

Solo developers ship UI changes without anyone looking at them. A one-pixel padding change can cascade into broken layouts on different screen sizes, and dark mode changes can make text invisible — all without a test failure. Screenshot testing captures the visual output of your UI components and compares them against approved baselines, catching regressions that unit tests and instrumented tests miss.

## When to Use This Skill

Use this skill when you need to:
- Set up visual regression testing for an Android project
- Catch unintentional UI changes during refactoring
- Test UI across configurations (dark mode, font scale, RTL, screen densities)
- Verify Compose components render correctly
- Add visual testing to CI pipelines
- Compare UI before and after a dependency upgrade

## When NOT to Use This Skill

Do NOT use this skill when:
- Testing business logic (use unit tests)
- Testing user interaction flows (use instrumented tests)
- Testing API responses (use integration tests)
- The UI is still rapidly changing (screenshots will break every commit)

## Prerequisites

- Android project with Compose or View-based UI
- For Paparazzi: JVM-based (no device/emulator needed)
- For Roborazzi: Robolectric compatible project
- For Compose Preview Screenshots: Jetpack Compose with `@Preview` annotations
- For ADB screenshots: Connected device or emulator

## Step 1: Choose Your Approach

| Approach | Device Needed? | Speed | Best For |
|----------|---------------|-------|----------|
| **Paparazzi** | No (JVM) | Very fast | Individual components, design system |
| **Roborazzi** | No (Robolectric) | Fast | Components with interaction state |
| **Compose Preview Screenshots** | No (Gradle task) | Fast | Compose `@Preview` functions |
| **ADB Screenshots** | Yes | Slow | Full-screen integration, real device rendering |

**Recommendation for solo devs:** Start with Paparazzi for component-level testing. It requires no device, runs fast, and catches the most common regressions.

## Step 2: Paparazzi Setup

### 2.1 Add Dependencies

```kotlin
// build.gradle.kts (app module)
plugins {
    id("app.cash.paparazzi") version "1.3.4"
}
```

### 2.2 Write Screenshot Tests

```kotlin
// src/test/java/com/example/myapp/screenshots/ButtonScreenshotTest.kt
import app.cash.paparazzi.Paparazzi
import org.junit.Rule
import org.junit.Test

class ButtonScreenshotTest {
    @get:Rule
    val paparazzi = Paparazzi()

    @Test
    fun primaryButton() {
        paparazzi.snapshot {
            PrimaryButton(text = "Click Me", onClick = {})
        }
    }

    @Test
    fun primaryButtonDisabled() {
        paparazzi.snapshot {
            PrimaryButton(text = "Disabled", onClick = {}, enabled = false)
        }
    }
}
```

### 2.3 Record and Verify

```bash
# Record golden baselines (run once, commit results)
./gradlew :app:recordPaparazziDebug

# Verify against baselines (run in CI)
./gradlew :app:verifyPaparazziDebug

# Baselines stored in: src/test/snapshots/
```

### 2.4 Multi-Configuration Testing

```kotlin
class ThemedScreenshotTest {
    @get:Rule
    val paparazzi = Paparazzi(
        deviceConfig = DeviceConfig.PIXEL_6.copy(
            nightMode = NightMode.NIGHT  // Dark mode
        )
    )

    @Test
    fun settingsScreenDarkMode() {
        paparazzi.snapshot {
            AppTheme(darkTheme = true) {
                SettingsScreen()
            }
        }
    }
}

// Test multiple configurations
class MultiConfigScreenshotTest {
    companion object {
        val configs = listOf(
            "light" to DeviceConfig.PIXEL_6,
            "dark" to DeviceConfig.PIXEL_6.copy(nightMode = NightMode.NIGHT),
            "large_font" to DeviceConfig.PIXEL_6.copy(fontScale = 1.5f),
            "rtl" to DeviceConfig.PIXEL_6.copy(layoutDirection = LayoutDirection.RTL),
        )
    }

    @get:Rule
    val paparazzi = Paparazzi()

    @Test
    fun headerComponent_allConfigs() {
        configs.forEach { (name, config) ->
            paparazzi.unsafeUpdateConfig(config)
            paparazzi.snapshot(name = "header_$name") {
                HeaderComponent(title = "Settings")
            }
        }
    }
}
```

## Step 3: Roborazzi Setup (Alternative)

### 3.1 Add Dependencies

```kotlin
// build.gradle.kts
plugins {
    id("io.github.takahirom.roborazzi") version "1.8.0"
}

dependencies {
    testImplementation("io.github.takahirom.roborazzi:roborazzi:1.8.0")
    testImplementation("io.github.takahirom.roborazzi:roborazzi-compose:1.8.0")
}
```

### 3.2 Write Tests

```kotlin
@RunWith(RobolectricTestRunner::class)
@GraphicsMode(GraphicsMode.Mode.NATIVE)
class ScreenshotTest {
    @get:Rule
    val composeTestRule = createComposeRule()

    @Test
    fun homeScreen() {
        composeTestRule.setContent {
            AppTheme { HomeScreen() }
        }
        composeTestRule.onRoot().captureRoboImage("screenshots/home.png")
    }
}
```

### 3.3 Record and Verify

```bash
# Record baselines
./gradlew recordRoborazziDebug

# Verify
./gradlew verifyRoborazziDebug

# Compare (generates diff images)
./gradlew compareRoborazziDebug
```

## Step 4: Compose Preview Screenshot Testing

### 4.1 Setup (Official Jetpack Library)

```kotlin
// build.gradle.kts
plugins {
    id("com.android.compose.screenshot") version "0.0.1-alpha07"
}

android {
    experimentalProperties["android.experimental.enableScreenshotTest"] = true
}
```

### 4.2 Annotate Previews

```kotlin
// Your existing @Preview functions are the test inputs
@Preview(showBackground = true)
@Composable
fun SettingsScreenPreview() {
    AppTheme {
        SettingsScreen(
            state = SettingsState.Default
        )
    }
}

@Preview(showBackground = true, uiMode = Configuration.UI_MODE_NIGHT_YES)
@Composable
fun SettingsScreenDarkPreview() {
    AppTheme(darkTheme = true) {
        SettingsScreen(
            state = SettingsState.Default
        )
    }
}
```

### 4.3 Record and Verify

```bash
# Record baselines from @Preview functions
./gradlew updateDebugScreenshotTest

# Verify against baselines
./gradlew validateDebugScreenshotTest
```

## Step 5: ADB-Based Screenshots (Integration Level)

### 5.1 Capture Full-Screen Screenshots

```bash
# Capture single screenshot
adb exec-out screencap -p > screenshots/home_screen.png

# Batch capture across a flow
adb shell am start -n com.example.myapp/.MainActivity
sleep 2
adb exec-out screencap -p > screenshots/01_home.png

adb shell input tap 500 800  # Tap settings
sleep 1
adb exec-out screencap -p > screenshots/02_settings.png

adb shell input keyevent KEYCODE_BACK
sleep 1
adb exec-out screencap -p > screenshots/03_back_to_home.png
```

### 5.2 Compare Screenshots

```bash
# Using ImageMagick to compare (install: brew install imagemagick)
compare screenshots/baseline/home.png screenshots/current/home.png screenshots/diff/home_diff.png

# Get numeric difference
compare -metric AE screenshots/baseline/home.png screenshots/current/home.png null: 2>/dev/null
# Output: number of pixels that differ (0 = identical)
```

## Step 6: CI Integration

### 6.1 GitHub Actions (Paparazzi)

```yaml
# .github/workflows/screenshot-tests.yml
name: Screenshot Tests
on: [pull_request]

jobs:
  verify-screenshots:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Verify Screenshots
        run: ./gradlew :app:verifyPaparazziDebug

      - name: Upload Diff Report
        if: failure()
        uses: actions/upload-artifact@v4
        with:
          name: screenshot-diffs
          path: app/build/reports/paparazzi/
```

## Step 7: Handling Intentional Changes

### 7.1 Updating Baselines

```bash
# When you intentionally change UI, update baselines:
./gradlew :app:recordPaparazziDebug

# Review the changes
git diff --stat  # See which baseline files changed

# Commit updated baselines
git add src/test/snapshots/
git commit -m "Update screenshot baselines for new settings UI"
```

### 7.2 Git LFS for Large Baselines

```bash
# If baselines make the repo large, use Git LFS
git lfs install
git lfs track "*.png"
git add .gitattributes
git commit -m "Track PNG files with Git LFS"
```

## Related Skills

- `android-testing-patterns` — Comprehensive test strategy including unit and instrumented tests
- `android-emulator-management` — Emulator setup for multi-configuration screenshot testing
- `android-adb-operations` — ADB commands for device-level screenshot capture
- `jetpack-compose-patterns` — Compose component patterns that produce testable UI
