---
name: android_gradle_upgrade
description: Upgrade Android Gradle Plugin (AGP) and dependencies with compatibility verification and migration...
version: "1.0.0"
category: mobile-development
tags: [ai, android, ci/cd, debug, go, gradle, java, kotlin]
agents_used: []
---

# Android Gradle Upgrade

Upgrade Android Gradle Plugin (AGP) and dependencies with compatibility verification and migration guidance. This command safely upgrades your Android project's Gradle configuration, handles breaking changes, and ensures compatibility across all dependencies.

## Context
The user needs to upgrade their Android project's Gradle Plugin, Kotlin version, and related dependencies. This requires careful analysis of compatibility, handling breaking changes, and proper migration steps to avoid build failures.

## Requirements
$ARGUMENTS

## Instructions

### 1. Current State Analysis

First, analyze the current project configuration:

**Check current versions:**
```bash
# Check AGP version
./gradlew -v

# Check Kotlin version
grep "kotlin" gradle/libs.versions.toml 2>/dev/null || grep "kotlin" build.gradle.kts || grep "kotlin" build.gradle

# Check Java version
java -version

# List outdated dependencies
./gradlew dependencyUpdates 2>/dev/null || echo "Install the versions plugin for dependency updates"
```

**Analyze build files:**
- `gradle/libs.versions.toml` (if using version catalog)
- `build.gradle.kts` (root project)
- `app/build.gradle.kts` (app module)
- `gradle/wrapper/gradle-wrapper.properties`

### 2. Compatibility Matrix

Reference the Android Gradle Plugin compatibility requirements:

| AGP Version | Min Gradle | Max Gradle | Min JDK | Min Android Studio |
|------------|------------|------------|---------|-------------------|
| 8.4 | 8.6 | 8.6 | 17 | Jellyfish |
| 8.3 | 8.4 | 8.6 | 17 | Iguana |
| 8.2 | 8.2 | 8.6 | 17 | Hedgehog |
| 8.1 | 8.0 | 8.6 | 17 | Giraffe |
| 8.0 | 8.0 | 8.5 | 17 | Flamingo |
| 7.4 | 7.5 | 8.1 | 11 | Electric Eel |

**Kotlin compatibility:**
| Kotlin | Compose Compiler | KSP |
|--------|-----------------|-----|
| 2.0.x | Built-in | 2.0.x-1.0.x |
| 1.9.x | 1.5.x | 1.9.x-1.0.x |
| 1.8.x | 1.4.x | 1.8.x-1.0.x |

### 3. Pre-Upgrade Checklist

Before upgrading, verify:

```markdown
- [ ] Git repository is clean (no uncommitted changes)
- [ ] All tests pass with current configuration
- [ ] Build succeeds without warnings
- [ ] CI/CD pipeline is green
- [ ] Backup created or rollback branch available
```

**Create backup branch:**
```bash
git checkout -b pre-gradle-upgrade-$(date +%Y%m%d)
git push origin pre-gradle-upgrade-$(date +%Y%m%d)
git checkout -b gradle-upgrade
```

### 4. Upgrade Gradle Wrapper

Update the Gradle wrapper first:

```bash
# Check current Gradle version
./gradlew --version

# Upgrade to specific version (match AGP requirements)
./gradlew wrapper --gradle-version=8.6

# Verify upgrade
./gradlew --version
```

Update `gradle/wrapper/gradle-wrapper.properties`:
```properties
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-8.6-bin.zip
networkTimeout=10000
validateDistributionUrl=true
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

### 5. Upgrade Android Gradle Plugin

Update AGP version in version catalog or build script:

**If using version catalog (`gradle/libs.versions.toml`):**
```toml
[versions]
agp = "8.3.0"  # Update this

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
android-library = { id = "com.android.library", version.ref = "agp" }
```

**If using traditional build script:**
```kotlin
// build.gradle.kts (root)
plugins {
    id("com.android.application") version "8.3.0" apply false
}
```

### 6. Upgrade Kotlin

Update Kotlin version alongside AGP:

**Version catalog:**
```toml
[versions]
kotlin = "2.0.0"  # or "1.9.22" for older projects
ksp = "2.0.0-1.0.21"  # Match Kotlin version

[plugins]
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
kotlin-compose = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
kotlin-serialization = { id = "org.jetbrains.kotlin.plugin.serialization", version.ref = "kotlin" }
ksp = { id = "com.google.devtools.ksp", version.ref = "ksp" }
```

### 7. Handle Breaking Changes

**AGP 8.0+ Changes:**

1. **Build features disabled by default:**
```kotlin
android {
    buildFeatures {
        buildConfig = true  // Explicitly enable if needed
    }
}
```

2. **Namespace required:**
```kotlin
android {
    namespace = "com.example.app"  // Required, not optional
}
```

3. **compileSdkVersion to compileSdk:**
```kotlin
android {
    compileSdk = 34  // Not compileSdkVersion
}
```

4. **minSdkVersion to minSdk:**
```kotlin
android {
    defaultConfig {
        minSdk = 26  // Not minSdkVersion
    }
}
```

**Kotlin 2.0 Changes:**

1. **Compose compiler plugin:**
```kotlin
// build.gradle.kts (app)
plugins {
    id("org.jetbrains.kotlin.plugin.compose")  // New plugin for Kotlin 2.0+
}

// Remove: composeOptions { kotlinCompilerExtensionVersion = "..." }
```

2. **K2 compiler (optional):**
```kotlin
// gradle.properties
kotlin.experimental.tryK2=true  // Opt-in for new compiler
```

### 8. Dependency Compatibility Updates

Update dependencies that require specific AGP/Kotlin versions:

**Hilt:**
```toml
[versions]
hilt = "2.50"  # Requires Kotlin 1.9+ or 2.0

[libraries]
hilt-android = { group = "com.google.dagger", name = "hilt-android", version.ref = "hilt" }
hilt-compiler = { group = "com.google.dagger", name = "hilt-compiler", version.ref = "hilt" }
```

**Room:**
```toml
[versions]
room = "2.6.1"  # Supports KSP 2.0

[libraries]
androidx-room-runtime = { group = "androidx.room", name = "room-runtime", version.ref = "room" }
androidx-room-compiler = { group = "androidx.room", name = "room-compiler", version.ref = "room" }
```

**Compose:**
```toml
[versions]
composeBom = "2024.02.00"  # Latest BOM
```

### 9. Migration Script

Run these commands in order:

```bash
#!/bin/bash

echo "=== Android Gradle Upgrade Script ==="

# Step 1: Clean project
echo "Cleaning project..."
./gradlew clean

# Step 2: Clear Gradle cache
echo "Clearing Gradle caches..."
rm -rf ~/.gradle/caches/transforms-*
rm -rf ~/.gradle/caches/build-cache-*
rm -rf .gradle/
rm -rf build/
rm -rf app/build/

# Step 3: Upgrade wrapper
echo "Upgrading Gradle wrapper..."
./gradlew wrapper --gradle-version=8.6

# Step 4: Sync and build
echo "Building project..."
./gradlew build --warning-mode all 2>&1 | tee upgrade-log.txt

# Step 5: Run tests
echo "Running tests..."
./gradlew test

# Step 6: Check for issues
echo "Checking for deprecations..."
grep -i "deprecated\|warning" upgrade-log.txt || echo "No deprecation warnings found"

echo "=== Upgrade complete ==="
```

### 10. Validation Steps

After upgrade, verify:

**Build validation:**
```bash
# Full clean build
./gradlew clean assembleDebug assembleRelease

# Run all tests
./gradlew testDebugUnitTest testReleaseUnitTest

# Lint check
./gradlew lintDebug

# Check for configuration cache issues
./gradlew --configuration-cache assembleDebug
```

**Compose-specific checks:**
```bash
# Verify Compose compilation
./gradlew :app:compileDebugKotlin

# Check for Compose compiler compatibility
./gradlew :app:compileDebugKotlin --info | grep -i "compose"
```

### 11. Common Issues and Solutions

**Issue: "Namespace not specified"**
```kotlin
// Solution: Add namespace to each module
android {
    namespace = "com.example.module"
}
```

**Issue: "kapt" deprecated**
```kotlin
// Solution: Migrate from kapt to KSP
// Before:
plugins {
    kotlin("kapt")
}
kapt(libs.room.compiler)

// After:
plugins {
    id("com.google.devtools.ksp")
}
ksp(libs.room.compiler)
```

**Issue: Compose compiler version mismatch**
```kotlin
// Solution for Kotlin 2.0+: Use compose plugin
plugins {
    id("org.jetbrains.kotlin.plugin.compose")
}
// Remove composeOptions block entirely
```

**Issue: JDK version incompatibility**
```kotlin
// Solution: Ensure JDK 17 for AGP 8.x
android {
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions {
        jvmTarget = "17"
    }
}
```

**Issue: "Cannot find symbol" after upgrade**
```bash
# Solution: Invalidate caches
./gradlew clean
rm -rf .gradle ~/.gradle/caches/modules-2/files-2.1/
./gradlew build
```

### 12. Rollback Procedure

If upgrade fails:

```bash
# Option 1: Git rollback
git checkout pre-gradle-upgrade-YYYYMMDD
git branch -D gradle-upgrade

# Option 2: Manual rollback
# Restore gradle-wrapper.properties
# Restore libs.versions.toml
# Restore build.gradle.kts files
./gradlew clean
rm -rf .gradle
./gradlew build
```

### 13. Post-Upgrade Optimization

After successful upgrade, consider these optimizations:

**Enable configuration cache:**
```properties
# gradle.properties
org.gradle.configuration-cache=true
org.gradle.configuration-cache.problems=warn
```

**Enable build cache:**
```properties
# gradle.properties
org.gradle.caching=true
```

**Parallel execution:**
```properties
# gradle.properties
org.gradle.parallel=true
org.gradle.workers.max=4
```

**Enable non-transitive R classes:**
```properties
# gradle.properties
android.nonTransitiveRClass=true
android.useAndroidX=true
```

## Output

After running this command, you will have:

1. **Updated Gradle wrapper** to compatible version
2. **Upgraded AGP** to target version
3. **Updated Kotlin** with proper Compose compiler integration
4. **Compatible dependencies** verified and updated
5. **Working build** with all tests passing
6. **Documented changes** for team reference

## Success Criteria

- [ ] `./gradlew assembleDebug` succeeds
- [ ] `./gradlew testDebugUnitTest` passes
- [ ] No deprecation warnings in build log
- [ ] App launches and functions correctly
- [ ] CI/CD pipeline passes

Target: $ARGUMENTS
