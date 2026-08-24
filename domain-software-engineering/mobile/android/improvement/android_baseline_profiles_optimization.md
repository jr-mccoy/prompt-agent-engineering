---
title: "Android Baseline Profiles Optimization"
category: mobile-development
description: "Generate and optimize Baseline Profiles and Startup Profiles for faster app launch and smoother scrolling, including Macrobenchmark setup"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: intermediate
tags:
  - android
  - baseline-profiles
  - performance
  - startup-time
  - macrobenchmark
  - mobile-development
updated: "2026-02-12"
---

# Android Baseline Profiles Optimization

**Objective:** Generate and optimize Baseline Profiles and Startup Profiles for an Android application — setting up the Macrobenchmark test infrastructure, defining critical user journeys for profile generation, configuring profile installation, measuring before/after startup time and rendering performance, and establishing a CI pipeline for automated profile regeneration on each release.

**When to Use:** Use this prompt when your app's cold start time exceeds 1 second, when users report jank during scrolling or screen transitions, when you want to improve Time-To-Interactive for first-run users, or when Google Play Console's Android Vitals flags startup or rendering performance issues. Baseline Profiles typically deliver 15-40% faster cold start and 30-60% faster initial rendering of complex screens.

**Important context:** Baseline Profiles tell the Android Runtime (ART) which code paths to pre-compile (AOT) at install time rather than JIT-compiling at runtime. Without profiles, the first few runs of your app are slower because ART is interpreting and JIT-compiling code on the fly. Startup Profiles (a subset) specifically optimize the startup path. Since Android 12+, Cloud Profiles from the Play Store can partially replace manually-generated profiles, but custom profiles are more precise and available immediately on install (Cloud Profiles take days to aggregate).

---

## Context Gathering

1. **Current Performance:**
   - "What is your current cold start time (Time-To-Initial-Display and Time-To-Full-Display)?"
   - "Are there jank issues on specific screens (LazyColumn, animations, complex Composables)?"
   - "What does Android Vitals report for startup and rendering metrics?"

2. **App Architecture:**
   - "Is the app using Jetpack Compose, XML Views, or both?"
   - "How many Activities/Fragments are involved in the startup path?"
   - "Do you use a splash screen (SplashScreen API or custom)?"
   - "What initialization happens at startup (DI, analytics, Firebase, network)?"

3. **Build Setup:**
   - "Current Gradle version and Android Gradle Plugin version?"
   - "Do you have an existing `benchmark` or `macrobenchmark` module?"
   - "What is your min SDK version? (Baseline Profiles benefit API 28+, full support API 33+)"
   - "Are you using R8 (shrinking/obfuscation)?"

---

## Instructions

### Step 1: Set Up Macrobenchmark Module

Create the benchmarking infrastructure:

```kotlin
// settings.gradle.kts
include(":macrobenchmark")

// macrobenchmark/build.gradle.kts
plugins {
    id("com.android.test")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.yourpackage.macrobenchmark"
    compileSdk = 35

    defaultConfig {
        minSdk = 28  // Macrobenchmark requires API 28+
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    targetProjectPath = ":app"
    experimentalProperties["android.experimental.self-instrumenting"] = true
}

dependencies {
    implementation(libs.androidx.benchmark.macro.junit4)
    implementation(libs.androidx.test.ext.junit)
    implementation(libs.androidx.test.espresso.core)
    implementation(libs.androidx.test.uiautomator)
}
```

### Step 2: Create Baseline Profile Generator

```kotlin
// macrobenchmark/src/main/java/com/yourpackage/BaselineProfileGenerator.kt
@RunWith(AndroidJUnit4::class)
class BaselineProfileGenerator {

    @get:Rule
    val rule = BaselineProfileRule()

    @Test
    fun generateBaselineProfile() {
        rule.collect(
            packageName = "com.yourpackage.app",
            includeInStartupProfile = true,  // Also generates Startup Profile
            profileBlock = {
                // === STARTUP JOURNEY ===
                startActivityAndWait()
                device.waitForIdle()

                // === CRITICAL USER JOURNEY 1: Main screen interaction ===
                // Scroll the main list to profile LazyColumn rendering
                device.findObject(By.res("main_list")).apply {
                    repeat(3) {
                        fling(Direction.DOWN)
                        device.waitForIdle()
                    }
                }

                // === CRITICAL USER JOURNEY 2: Navigation ===
                // Navigate to commonly visited screens
                device.findObject(By.res("nav_search")).click()
                device.waitForIdle()

                device.findObject(By.res("nav_profile")).click()
                device.waitForIdle()

                // === CRITICAL USER JOURNEY 3: Key feature ===
                // Exercise the most-used feature path
                device.findObject(By.text("Create")).click()
                device.waitForIdle()
                device.pressBack()
            }
        )
    }
}
```

### Step 3: Configure Profile Installation in App Module

```kotlin
// app/build.gradle.kts
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("androidx.baselineprofile")
}

android {
    // ... existing config
}

baselineProfile {
    automaticGenerationDuringBuild = true  // Generate during release builds
    dexLayoutOptimization = true            // API 34+ DEX layout optimization
}

dependencies {
    baselineProfile(project(":macrobenchmark"))
    implementation(libs.androidx.profileinstaller)  // Required for profile delivery
}
```

### Step 4: Generate and Validate Profiles

```bash
# Generate baseline profiles
./gradlew :app:generateBaselineProfile

# Profiles are written to:
# app/src/main/generated/baselineProfiles/baseline-prof.txt
# app/src/main/generated/baselineProfiles/startup-prof.txt

# Verify profiles are non-empty and contain expected classes
cat app/src/main/generated/baselineProfiles/baseline-prof.txt | head -20
# Should show class/method rules like:
# HSPLcom/yourpackage/MainActivity;->onCreate(Landroid/os/Bundle;)V
# PLcom/yourpackage/ui/MainScreen;->MainScreen(...)V
```

### Step 5: Benchmark Before and After

Create benchmark tests to measure improvement:

```kotlin
@RunWith(AndroidJUnit4::class)
class StartupBenchmark {

    @get:Rule
    val rule = MacrobenchmarkRule()

    @Test
    fun startupNoCompilation() = startup(CompilationMode.None())

    @Test
    fun startupBaselineProfile() = startup(CompilationMode.Partial(
        baselineProfileMode = BaselineProfileMode.Require
    ))

    @Test
    fun startupFullCompilation() = startup(CompilationMode.Full())

    private fun startup(compilationMode: CompilationMode) {
        rule.measureRepeated(
            packageName = "com.yourpackage.app",
            metrics = listOf(
                StartupTimingMetric(),
                TraceSectionMetric("firstComposition"),  // Custom trace
            ),
            compilationMode = compilationMode,
            iterations = 10,
            startupMode = StartupMode.COLD,
        ) {
            pressHome()
            startActivityAndWait()
        }
    }
}
```

Run benchmarks: `./gradlew :macrobenchmark:connectedBenchmarkAndroidTest`

### Step 6: Optimize Profile Coverage

Identify high-impact code paths to add to the profile:

1. **Analyze startup trace:** Use Android Studio Profiler or Perfetto to identify heavy startup work
2. **Profile completeness:** Compare profiled classes against actual startup class loading — are key classes missing?
3. **Compose-specific:** Ensure commonly recomposed Composables are profiled (scroll through lists, trigger state changes)
4. **Navigation paths:** Profile the 3-5 most common navigation flows (not every screen)
5. **Third-party libraries:** Firebase, analytics, ad SDKs — these benefit from profiling too

### Step 7: CI Integration

```yaml
# .github/workflows/baseline-profiles.yml
name: Generate Baseline Profiles
on:
  push:
    branches: [release/*]

jobs:
  baseline-profiles:
    runs-on: macos-latest  # macOS for hardware acceleration
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'zulu'
      - name: Enable Hardware Acceleration
        run: |
          echo "y" | $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --install "system-images;android-34;google_apis;x86_64"
          $ANDROID_HOME/cmdline-tools/latest/bin/avdmanager create avd -n test -k "system-images;android-34;google_apis;x86_64" --device "Pixel 6"
      - name: Generate Baseline Profiles
        run: ./gradlew :app:generateBaselineProfile
      - name: Commit Profiles
        run: |
          git add app/src/main/generated/baselineProfiles/
          git commit -m "chore: regenerate baseline profiles" || echo "No changes"
          git push
```

---

## Expected Output

1. **Macrobenchmark Module** — complete module configuration and generator code
2. **Baseline Profile Rules** — generated profile file with method/class rules
3. **Startup Profile** — subset focused on the startup path
4. **Benchmark Results** — before/after comparison table showing startup and rendering improvements
5. **CI Configuration** — automated profile regeneration workflow
6. **Optimization Report** — identified high-impact code paths and recommendations

---

## CRITICAL: Verification Requirements

- [ ] Baseline profiles are generated and non-empty (check `baseline-prof.txt` has content)
- [ ] `ProfileInstaller` is in the dependency list (required for profile delivery on pre-API 33)
- [ ] Benchmark shows measurable improvement between `None()` and `Partial()` compilation modes
- [ ] Profiles regenerate successfully in CI (not just local)
- [ ] ProGuard/R8 rules do not strip profiled methods
- [ ] Profile generation tests use `testInstrumentationRunnerArguments` for device selection
- [ ] The release build includes profiles in the AAB (verify with `bundletool`)
