---
title: "Android Version Catalog Migration"
category: mobile-development
description: "Migrate from traditional Gradle dependency management to Version Catalogs (libs.versions.toml), including Convention Plugins setup"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
difficulty: intermediate
tags:
  - android
  - gradle
  - version-catalog
  - convention-plugins
  - build-system
  - mobile-development
updated: "2026-02-12"
---

# Android Version Catalog Migration

**Objective:** Migrate an Android project from traditional Gradle dependency management (hardcoded version strings, `ext` blocks, `buildSrc`) to Gradle Version Catalogs (`libs.versions.toml`) with Convention Plugins — producing a centralized, type-safe, IDE-supported dependency management system that scales across multi-module projects.

**When to Use:** Use this prompt when your project has dependency versions scattered across multiple `build.gradle.kts` files, when you are modularizing and need consistent versions across modules, when `buildSrc` changes trigger full project recompilation, or when you want IDE autocompletion for dependency declarations. Version Catalogs are the official Gradle recommendation as of Gradle 8+ and are used by all Google sample projects.

**Important context:** Version Catalogs (`libs.versions.toml`) centralize dependency declarations in a TOML file. Combined with Convention Plugins (replacing `buildSrc`), they provide type-safe dependency access, IDE autocomplete, Dependabot/Renovate compatibility, and no rebuild penalty when changing versions (unlike `buildSrc`). This is the recommended approach for all new and existing Android projects.

---

## Context Gathering

1. **Current Setup:**
   - "How do you currently manage dependency versions (hardcoded, `ext` block, `buildSrc`, `buildscript`)?"
   - "How many modules does your project have?"
   - "Do you use any dependency management plugins (Gradle Versions Plugin, Renovate, Dependabot)?"
   - "Current Gradle version? (Version Catalogs are stable in Gradle 7.4+, recommended 8.0+)"

2. **Dependencies:**
   - "Approximately how many unique dependencies?"
   - "Do you use BOMs (e.g., Compose BOM, Firebase BOM, OkHttp BOM)?"
   - "Do you have custom Gradle plugins in `buildSrc`?"

---

## Instructions

### Step 1: Inventory Current Dependencies

Extract all dependencies from the project:

```bash
# Generate a full dependency list
./gradlew app:dependencies --configuration releaseRuntimeClasspath > deps.txt

# Find all dependency declarations across build files
grep -rn "implementation\|api\|kapt\|ksp\|testImplementation\|androidTestImplementation" \
  --include="*.gradle" --include="*.gradle.kts" .
```

Create a table of all dependencies:

| Group | Artifact | Current Version | Used In Modules |
|-------|----------|----------------|-----------------|
| androidx.core | core-ktx | 1.13.1 | app, feature-auth |
| io.ktor | ktor-client-core | 3.0.0 | core-network |
| ... | ... | ... | ... |

### Step 2: Create Version Catalog File

```toml
# gradle/libs.versions.toml

[versions]
# Build
agp = "8.7.0"
kotlin = "2.1.0"
ksp = "2.1.0-1.0.29"

# AndroidX
core-ktx = "1.15.0"
appcompat = "1.7.0"
activity-compose = "1.9.3"
lifecycle = "2.8.7"
navigation = "2.8.4"
room = "2.6.1"
datastore = "1.1.1"
work = "2.10.0"
hilt = "2.53.1"
hilt-navigation-compose = "1.2.0"

# Compose
compose-bom = "2024.12.01"

# Networking
ktor = "3.0.0"
kotlinx-serialization = "1.7.3"
kotlinx-coroutines = "1.9.0"

# Firebase
firebase-bom = "33.7.0"

# Testing
junit = "4.13.2"
androidx-test-ext = "1.2.1"
espresso = "3.6.1"
mockk = "1.13.13"
turbine = "1.2.0"

[libraries]
# AndroidX Core
androidx-core-ktx = { group = "androidx.core", name = "core-ktx", version.ref = "core-ktx" }
androidx-appcompat = { group = "androidx.appcompat", name = "appcompat", version.ref = "appcompat" }
androidx-activity-compose = { group = "androidx.activity", name = "activity-compose", version.ref = "activity-compose" }

# Lifecycle
androidx-lifecycle-runtime-ktx = { group = "androidx.lifecycle", name = "lifecycle-runtime-ktx", version.ref = "lifecycle" }
androidx-lifecycle-viewmodel-compose = { group = "androidx.lifecycle", name = "lifecycle-viewmodel-compose", version.ref = "lifecycle" }
androidx-lifecycle-runtime-compose = { group = "androidx.lifecycle", name = "lifecycle-runtime-compose", version.ref = "lifecycle" }

# Compose (via BOM)
compose-bom = { group = "androidx.compose", name = "compose-bom", version.ref = "compose-bom" }
compose-ui = { group = "androidx.compose.ui", name = "ui" }
compose-ui-graphics = { group = "androidx.compose.ui", name = "ui-graphics" }
compose-ui-tooling-preview = { group = "androidx.compose.ui", name = "ui-tooling-preview" }
compose-material3 = { group = "androidx.compose.material3", name = "material3" }
compose-ui-tooling = { group = "androidx.compose.ui", name = "ui-tooling" }
compose-ui-test-manifest = { group = "androidx.compose.ui", name = "ui-test-manifest" }
compose-ui-test-junit4 = { group = "androidx.compose.ui", name = "ui-test-junit4" }

# Navigation
androidx-navigation-compose = { group = "androidx.navigation", name = "navigation-compose", version.ref = "navigation" }

# Room
androidx-room-runtime = { group = "androidx.room", name = "room-runtime", version.ref = "room" }
androidx-room-ktx = { group = "androidx.room", name = "room-ktx", version.ref = "room" }
androidx-room-compiler = { group = "androidx.room", name = "room-compiler", version.ref = "room" }

# Hilt
hilt-android = { group = "com.google.dagger", name = "hilt-android", version.ref = "hilt" }
hilt-android-compiler = { group = "com.google.dagger", name = "hilt-android-compiler", version.ref = "hilt" }
hilt-navigation-compose = { group = "androidx.hilt", name = "hilt-navigation-compose", version.ref = "hilt-navigation-compose" }

# Networking
ktor-client-core = { group = "io.ktor", name = "ktor-client-core", version.ref = "ktor" }
ktor-client-android = { group = "io.ktor", name = "ktor-client-android", version.ref = "ktor" }
ktor-serialization-json = { group = "io.ktor", name = "ktor-serialization-kotlinx-json", version.ref = "ktor" }
kotlinx-serialization-json = { group = "org.jetbrains.kotlinx", name = "kotlinx-serialization-json", version.ref = "kotlinx-serialization" }
kotlinx-coroutines-core = { group = "org.jetbrains.kotlinx", name = "kotlinx-coroutines-core", version.ref = "kotlinx-coroutines" }
kotlinx-coroutines-android = { group = "org.jetbrains.kotlinx", name = "kotlinx-coroutines-android", version.ref = "kotlinx-coroutines" }

# Firebase (via BOM)
firebase-bom = { group = "com.google.firebase", name = "firebase-bom", version.ref = "firebase-bom" }
firebase-analytics = { group = "com.google.firebase", name = "firebase-analytics-ktx" }
firebase-auth = { group = "com.google.firebase", name = "firebase-auth-ktx" }
firebase-firestore = { group = "com.google.firebase", name = "firebase-firestore-ktx" }
firebase-crashlytics = { group = "com.google.firebase", name = "firebase-crashlytics-ktx" }

# Testing
junit = { group = "junit", name = "junit", version.ref = "junit" }
androidx-test-ext = { group = "androidx.test.ext", name = "junit", version.ref = "androidx-test-ext" }
espresso-core = { group = "androidx.test.espresso", name = "espresso-core", version.ref = "espresso" }
mockk = { group = "io.mockk", name = "mockk", version.ref = "mockk" }
turbine = { group = "app.cash.turbine", name = "turbine", version.ref = "turbine" }
kotlinx-coroutines-test = { group = "org.jetbrains.kotlinx", name = "kotlinx-coroutines-test", version.ref = "kotlinx-coroutines" }

[bundles]
compose = ["compose-ui", "compose-ui-graphics", "compose-ui-tooling-preview", "compose-material3"]
compose-debug = ["compose-ui-tooling", "compose-ui-test-manifest"]
lifecycle = ["androidx-lifecycle-runtime-ktx", "androidx-lifecycle-viewmodel-compose", "androidx-lifecycle-runtime-compose"]
testing = ["junit", "mockk", "turbine", "kotlinx-coroutines-test"]
android-testing = ["androidx-test-ext", "espresso-core", "compose-ui-test-junit4"]

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
android-library = { id = "com.android.library", version.ref = "agp" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
kotlin-compose = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
kotlin-serialization = { id = "org.jetbrains.kotlin.plugin.serialization", version.ref = "kotlin" }
ksp = { id = "com.google.devtools.ksp", version.ref = "ksp" }
hilt = { id = "com.google.dagger.hilt.android", version.ref = "hilt" }
room = { id = "androidx.room", version.ref = "room" }
```

### Step 3: Update Build Files

**Before (traditional):**
```kotlin
// app/build.gradle.kts
dependencies {
    implementation("androidx.core:core-ktx:1.15.0")
    implementation(platform("androidx.compose:compose-bom:2024.12.01"))
    implementation("androidx.compose.ui:ui")
    implementation("com.google.dagger:hilt-android:2.53.1")
    kapt("com.google.dagger:hilt-android-compiler:2.53.1")
}
```

**After (Version Catalog):**
```kotlin
// app/build.gradle.kts
dependencies {
    implementation(libs.androidx.core.ktx)
    implementation(platform(libs.compose.bom))
    implementation(libs.bundles.compose)
    implementation(libs.hilt.android)
    ksp(libs.hilt.android.compiler)
}
```

### Step 4: Convention Plugins (Optional but Recommended)

Replace `buildSrc` with Convention Plugins:

```kotlin
// build-logic/convention/build.gradle.kts
plugins {
    `kotlin-dsl`
}

dependencies {
    compileOnly(libs.android.gradle.plugin)
    compileOnly(libs.kotlin.gradle.plugin)
    compileOnly(libs.compose.gradle.plugin)
}

// build-logic/convention/src/main/kotlin/AndroidLibraryConventionPlugin.kt
class AndroidLibraryConventionPlugin : Plugin<Project> {
    override fun apply(target: Project) {
        with(target) {
            with(pluginManager) {
                apply("com.android.library")
                apply("org.jetbrains.kotlin.android")
            }
            extensions.configure<LibraryExtension> {
                compileSdk = 35
                defaultConfig { minSdk = 26 }
                compileOptions {
                    sourceCompatibility = JavaVersion.VERSION_17
                    targetCompatibility = JavaVersion.VERSION_17
                }
            }
        }
    }
}
```

Register in `build-logic/convention/build.gradle.kts`:
```kotlin
gradlePlugin {
    plugins {
        register("androidLibrary") {
            id = "yourapp.android.library"
            implementationClass = "AndroidLibraryConventionPlugin"
        }
    }
}
```

### Step 5: Migration Checklist

Execute the migration in this order:

1. [ ] Create `gradle/libs.versions.toml` with all versions, libraries, bundles, and plugins
2. [ ] Update `settings.gradle.kts` to enable version catalogs (default in Gradle 8+)
3. [ ] Update root `build.gradle.kts` to use `alias(libs.plugins.*)` for plugin declarations
4. [ ] Update each module's `build.gradle.kts` one at a time (start with `:app`)
5. [ ] Replace `kapt` with `ksp` where possible (Hilt, Room support KSP)
6. [ ] Create bundles for commonly grouped dependencies
7. [ ] (Optional) Set up Convention Plugins in `build-logic/`
8. [ ] Run `./gradlew assembleDebug` — verify the build succeeds
9. [ ] Run all tests — verify nothing broke
10. [ ] Configure Dependabot/Renovate to update the TOML file

---

## Expected Output

1. **`gradle/libs.versions.toml`** — complete version catalog file
2. **Updated `build.gradle.kts` files** — all modules using catalog references
3. **Convention Plugins** (if applicable) — shared build configuration
4. **Migration Checklist** — completed step-by-step with verification
5. **Dependency Audit Summary** — any deprecated or replaced dependencies found during migration

---

## CRITICAL: Verification Requirements

- [ ] The project builds successfully after migration (`./gradlew assembleDebug assembleRelease`)
- [ ] All tests pass (`./gradlew test connectedAndroidTest`)
- [ ] No hardcoded version strings remain in any `build.gradle.kts` file
- [ ] IDE autocomplete works for `libs.*` references
- [ ] BOM dependencies (Compose, Firebase) are correctly configured with `platform()`
- [ ] Plugin versions are declared in the `[plugins]` section, not hardcoded
- [ ] Convention Plugins (if created) do not trigger full recompilation on changes
