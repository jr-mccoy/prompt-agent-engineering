---
title: "Android ProGuard/R8 Configuration Optimization"
category: mobile-development
description: "Audit and optimize ProGuard/R8 shrinking configuration for Android apps. Identifies missing keep rules causing runtime crashes, over-kept classes bloating APK size, and guides migration to R8 full mode with a comprehensive testing strategy."
techniques:
  - ST-01  # Clear Objective Statement
  - ST-02  # Structured Sequential Instructions
  - RT-02  # Multi-Dimensional Analysis
  - RT-05  # Evidence-Based Reasoning
  - QA-02  # Adversarial Thinking
difficulty: advanced
tags:
  - android
  - proguard
  - r8
  - optimization
  - solo-developer
  - apk-size
  - release-builds
updated: "2026-02-11"
related_prompts:
  - domain-software-engineering/mobile/android/publishing/android_app_bundle_optimization.md
  - domain-software-engineering/mobile/android/publishing/android_release_preparation.md
  - domain-software-engineering/mobile/android/analysis/android_performance_audit.md
  - domain-software-engineering/mobile/android/maintenance/android_dependency_update.md
---

# Android ProGuard/R8 Configuration Optimization

**Objective:** Systematically audit the current ProGuard/R8 configuration of an Android project, identify missing keep rules that cause runtime crashes (reflection, serialization, JNI), find over-kept classes that unnecessarily bloat APK size, analyze shrinking effectiveness using APK Analyzer, evaluate migration to R8 full mode, and establish a testing strategy that catches obfuscation issues before they reach users.

## When to Use

- Use when: Release builds crash with `ClassNotFoundException`, `NoSuchMethodException`, or `NoSuchFieldException` that do not occur in debug builds
- Use when: Your APK/AAB size is larger than expected and you suspect over-broad keep rules
- Use when: You are adding a new library that uses reflection, annotation processing, or serialization
- Use when: Migrating from ProGuard to R8 or enabling R8 full mode
- Use when: Preparing for a major release and want to verify shrinking configuration is correct
- Do not use when: You need general APK size reduction (use `android_app_bundle_optimization.md` instead)
- Do not use when: Performance issues are not related to build configuration (use `android_performance_audit.md`)

**Important context:** R8 is the default code shrinker since AGP 3.4, replacing ProGuard. R8 is backwards-compatible with ProGuard rules but offers additional optimizations. R8 "full mode" (`android.enableR8.fullMode=true`, default since AGP 8.0) performs more aggressive optimization but can break code that relies on runtime reflection if keep rules are incomplete. The most dangerous bugs from incorrect R8 configuration are those that only manifest in release builds, often in edge cases that automated tests miss.

---

## Context Gathering

Before starting the audit, gather:

1. **Current Configuration:**
   - "Where are your ProGuard/R8 rules defined? (proguard-rules.pro, consumer rules from libraries, multiple rule files?)"
   - "Is R8 enabled? Is R8 full mode enabled?"
   - "How many keep rules do you currently have? (rough count)"

2. **Build Configuration:**
   - "What is your AGP (Android Gradle Plugin) version?"
   - "Is minification enabled for all build types or just release?"
   - "Do you use `shrinkResources` in addition to `minifyEnabled`?"

3. **Library Landscape:**
   - "Which libraries use reflection? (Gson, Moshi, Retrofit, Room, Hilt, etc.)"
   - "Do you use any JNI/native code?"
   - "Do any libraries bundle their own consumer ProGuard rules?"

4. **Problem History:**
   - "Have you experienced release-only crashes? Which classes/methods were involved?"
   - "Have you added keep rules reactively (to fix crashes) without understanding why?"
   - "Do you test release builds before publishing?"

5. **Size Goals:**
   - "What is your current APK/AAB download size?"
   - "Do you have a size budget? (e.g., Google recommends < 150 MB for AAB)"
   - "Are there specific markets where download size is critical (emerging markets, low-bandwidth)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY rule change, you MUST:**

1. **Test both debug and release builds** -- A rule change that fixes a release crash but breaks debug behavior is not a solution. Verify both configurations.
2. **Check consumer ProGuard rules** -- Many libraries ship their own keep rules in `META-INF/proguard/` or via `consumerProguardFiles`. Verify you are not duplicating rules the library already provides.
3. **Trace the reflection path** -- Before adding a keep rule for a class, confirm HOW it is accessed via reflection. The keep rule must match the actual reflection pattern (class name, method name, constructor, fields).
4. **Measure before and after** -- Record APK size before changes and after. Rule changes without measurement are guesswork.
5. **Verify in production-like conditions** -- Test with release signing, real API endpoints, and actual user data when possible. Some obfuscation issues only surface with specific data patterns.

**Finding that the current configuration is already well-optimized is an acceptable outcome.** Not every project needs R8 rule changes.

### False-Positive Prevention

- Do NOT add blanket keep rules like `-keep class com.myapp.** { *; }` to fix individual issues -- this disables shrinking for the entire package
- Do NOT assume a crash is caused by R8 without verifying the stack trace points to an obfuscated or removed class/method
- Do NOT remove keep rules that libraries require without checking the library documentation and consumer rules
- Do NOT treat R8 warnings as errors unless they cause actual runtime failures -- some warnings are informational
- Do NOT recommend R8 full mode migration without a testing plan -- it WILL break apps that rely on implicit keeps
- DO verify each keep rule is necessary by temporarily removing it and running the test suite
- DO use `-printusage` to identify what R8 actually removes, rather than guessing
- DO use `-printseeds` to verify which classes are kept and why
- DO check the mapping file (`mapping.txt`) to understand obfuscation before diagnosing crashes
- DO distinguish between rules needed for the app code vs rules needed for third-party libraries

---

### Phase 1: Current Config Audit

Analyze the existing ProGuard/R8 configuration to understand what is being kept and why.

#### 1.1 Inventory All Rule Sources

```bash
# Find all ProGuard/R8 rule files in the project
find . -name "proguard-rules.pro" -o -name "proguard-*.pro" -o -name "*.pro" | sort

# Check Gradle configuration for rule file references
grep -r "proguardFiles\|consumerProguardFiles" --include="*.gradle*" .

# Extract consumer rules from AAR dependencies
# These are automatically applied but good to know about
unzip -l app/build/intermediates/full_jar/release/full.jar | grep proguard
```

#### 1.2 Classify Existing Rules

Categorize each rule by purpose:

```proguard
# CATEGORY 1: Library-required rules (DO NOT REMOVE without checking library docs)
# These prevent crashes in third-party code

# Retrofit (reflection-based API interface creation)
-keepattributes Signature
-keepattributes *Annotation*
-keep,allowshrinking,allowobfuscation class retrofit2.** { *; }
-keepclassmembers,allowshrinking,allowobfuscation interface * {
    @retrofit2.http.* <methods>;
}

# CATEGORY 2: Serialization rules (CRITICAL for data integrity)
# Missing these causes silent data corruption or crashes

# Gson - keeps field names for JSON serialization
-keepclassmembers class com.myapp.data.model.** {
    <fields>;
}

# Kotlin serialization
-keepattributes RuntimeVisibleAnnotations
-keep,includedescriptorclasses class com.myapp.**$$serializer { *; }

# CATEGORY 3: Reflection rules (needed for runtime class access)
# Missing these causes ClassNotFoundException or NoSuchMethodException

# Hilt / Dagger generated code
-keep class dagger.** { *; }
-keep class javax.inject.** { *; }
-keep class * extends dagger.hilt.android.internal.managers.ViewComponentManager$FragmentContextWrapper { *; }

# CATEGORY 4: Over-broad rules (CANDIDATES FOR TIGHTENING)
# These keep more than necessary

# BAD: Keeps everything in the package
-keep class com.myapp.** { *; }

# BETTER: Keep only what reflection needs
-keep class com.myapp.data.model.** { <fields>; }
-keepclassmembers class com.myapp.data.model.** {
    public <init>(...);
}
```

#### 1.3 Generate Diagnostic Reports

```groovy
// Add to app/build.gradle.kts for diagnostic output
android {
    buildTypes {
        release {
            // Show what R8 removes
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )

            // Generate diagnostic files (add temporarily for audit)
            // Remove after audit to avoid build slowdown
        }
    }
}

// In proguard-rules.pro (TEMPORARY - for audit only):

# Print classes/members that are kept (and why)
-printseeds seeds.txt

# Print classes/members that are removed
-printusage usage.txt

# Print the final merged configuration
-printconfiguration full-config.txt

# Print mapping of original to obfuscated names
# (This is usually already generated for crash reporting)
-printmapping mapping.txt
```

```bash
# After building release, analyze the diagnostic files
# Seeds: What is kept
wc -l app/build/outputs/mapping/release/seeds.txt

# Usage: What is removed
wc -l app/build/outputs/mapping/release/usage.txt

# Look for your app classes in seeds (should be minimal)
grep "com.myapp" app/build/outputs/mapping/release/seeds.txt | head -50
```

---

### Phase 2: Crash-Causing Rule Identification

Identify classes and members that are removed or obfuscated but accessed at runtime.

#### 2.1 Reflection Usage Analysis

```kotlin
// PATTERN 1: Gson/Moshi serialization models
// These classes MUST keep field names and no-arg constructors
data class UserProfile(
    val id: String,          // Gson reads this field name via reflection
    val displayName: String, // R8 will rename to 'a', 'b' etc. without keep
    val email: String
)

// Required keep rule:
// -keepclassmembers class com.myapp.data.model.UserProfile {
//     <fields>;
//     public <init>(...);
// }

// PATTERN 2: Retrofit interface methods
// R8 must keep method names and parameter annotations
interface ApiService {
    @GET("users/{id}")
    suspend fun getUser(@Path("id") userId: String): UserProfile
}

// Usually handled by Retrofit's consumer rules, but verify

// PATTERN 3: Room entity classes
// Room uses annotation processing at compile time, but may need keeps
// for runtime schema validation
@Entity(tableName = "users")
data class UserEntity(
    @PrimaryKey val id: String,
    @ColumnInfo(name = "display_name") val displayName: String
)

// PATTERN 4: Enum classes used in serialization
// R8 can remove enum values it thinks are unused
enum class OrderStatus {
    PENDING, PROCESSING, SHIPPED, DELIVERED, CANCELLED
}
// If deserialized from JSON: -keepclassmembers enum com.myapp.model.OrderStatus { *; }

// PATTERN 5: JNI native method declarations
// Native method names MUST NOT be obfuscated
class NativeLib {
    external fun processImage(bitmap: Bitmap): Bitmap
}
// Required: -keepclasseswithmembernames class * { native <methods>; }
```

#### 2.2 Systematic Crash Risk Assessment

```markdown
| Class/Member | Reflection Type | Currently Kept? | Risk if Removed | Required Rule |
|-------------|----------------|-----------------|-----------------|---------------|
| data models (*.model.*) | Gson serialization | Partially | CRASH: Malformed JSON | -keepclassmembers with fields |
| API interfaces | Retrofit proxy | Yes (consumer rules) | CRASH: API calls fail | Verify consumer rules sufficient |
| Room entities | Annotation processing | Compile-time only | LOW: Usually safe | Keep if runtime schema check used |
| Enum values | Deserialization | No | CRASH: Unknown enum value | -keepclassmembers enum |
| Parcelable classes | Bundle serialization | No | CRASH: ClassNotFoundException on restore | -keep class * implements Parcelable |
| WorkManager workers | Reflection instantiation | No | CRASH: Worker not found | -keep class * extends ListenableWorker |
| Firebase classes | SDK reflection | Consumer rules | Varies | Verify consumer rules |
```

#### 2.3 Testing for Missing Rules

```bash
# Build release APK
./gradlew assembleRelease

# Install and run with verbose class loading (reveals missing classes)
adb install -r app/build/outputs/apk/release/app-release.apk

# Monitor for R8-related crashes
adb logcat | grep -E "ClassNotFoundException|NoSuchMethodException|NoSuchFieldException|JsonSyntaxException"

# Run automated tests against release build
./gradlew connectedAndroidTest -Pandroid.testInstrumentationRunnerArguments.class=com.myapp.CriticalPathTests
```

---

### Phase 3: Size Optimization

Identify over-kept classes that inflate APK size unnecessarily.

#### 3.1 APK Analyzer Assessment

```bash
# Use Android Studio's APK Analyzer or command line
# Analyze the release APK
java -jar $ANDROID_HOME/cmdline-tools/latest/lib/apkanalyzer.jar \
  apk file-size app/build/outputs/apk/release/app-release.apk

# Compare DEX sizes between builds
java -jar $ANDROID_HOME/cmdline-tools/latest/lib/apkanalyzer.jar \
  dex packages app/build/outputs/apk/release/app-release.apk \
  --defined-only | head -20

# Find largest classes in DEX
java -jar $ANDROID_HOME/cmdline-tools/latest/lib/apkanalyzer.jar \
  dex packages app/build/outputs/apk/release/app-release.apk \
  --defined-only | sort -t$'\t' -k3 -n -r | head -20
```

#### 3.2 Identify Over-Broad Keep Rules

```proguard
# PROBLEM: Blanket keeps that prevent all shrinking
# These are the biggest size offenders

# BAD: Keeps entire package including unused classes
-keep class com.myapp.** { *; }
# FIX: Remove and add specific rules for reflection-accessed classes only

# BAD: Keeps all members of data classes
-keep class com.myapp.data.** { *; }
# FIX: Keep only fields (for serialization) and constructors
-keepclassmembers class com.myapp.data.model.** {
    <fields>;
    public <init>(...);
}

# BAD: Keeps all interfaces (prevents tree-shaking)
-keep interface com.myapp.** { *; }
# FIX: Only keep interfaces accessed via reflection (e.g., Retrofit)
-keep,allowobfuscation interface com.myapp.data.api.** { *; }

# TECHNIQUE: Use allowshrinking and allowobfuscation modifiers
# -keep,allowshrinking: Allow R8 to remove if truly unused
# -keep,allowobfuscation: Allow renaming but not removal
# -keepclassmembers: Keep members only if the class itself is kept
```

#### 3.3 Measure Shrinking Effectiveness

```markdown
## Shrinking Report

| Metric | Before Optimization | After Optimization | Change |
|--------|-------------------|-------------------|--------|
| Total APK size | [X] MB | [Y] MB | -[Z]% |
| DEX file count | [N] | [N] | [change] |
| Total DEX size | [X] MB | [Y] MB | -[Z]% |
| Method count | [N] | [N] | -[Z]% |
| Resource file count | [N] | [N] | -[Z]% |
| classes.dex size | [X] MB | [Y] MB | -[Z]% |

## Largest Kept Packages (from seeds.txt)
| Package | Kept Classes | Kept Methods | Reason |
|---------|-------------|-------------|--------|
| com.myapp.data.model | 23 | 156 | Serialization |
| com.google.firebase | 87 | 412 | Consumer rules |
| [package] | [N] | [N] | [reason] |
```

---

### Phase 4: R8 Full Mode Migration

Evaluate and optionally enable R8 full mode for maximum optimization.

#### 4.1 R8 Full Mode Differences

```markdown
## R8 Full Mode vs Compatibility Mode

| Behavior | Compatibility Mode | Full Mode |
|----------|-------------------|-----------|
| Default constructors | Kept for kept classes | Only kept if explicitly required |
| Enum values | All values kept | Unused values removed |
| -keepattributes | Broadly applied | Strictly applied |
| Library rule interpretation | Lenient | Strict |
| AGP default | < 8.0 | >= 8.0 |

## Common Breakages in Full Mode
1. Missing no-arg constructors for deserialization
2. Removed enum values that come from server
3. Stripped annotations needed at runtime
4. Removed default interface method implementations
```

#### 4.2 Enable Full Mode Safely

```properties
# gradle.properties

# Step 1: Enable full mode
android.enableR8.fullMode=true

# Step 2: Temporarily enable R8 compatibility workaround logging
# This shows what full mode would break
# android.r8.failOnMissingClasses=false  # Only during testing
```

```proguard
# Additional rules typically needed for full mode

# Keep no-arg constructors for serialized classes
-keepclassmembers class com.myapp.data.model.** {
    public <init>();
}

# Keep all enum values (server can return any value)
-keepclassmembers enum * {
    public static **[] values();
    public static ** valueOf(java.lang.String);
    <fields>;
}

# Keep runtime annotations
-keepattributes RuntimeVisibleAnnotations,RuntimeVisibleParameterAnnotations

# Keep Kotlin metadata (needed for kotlin-reflect)
-keep class kotlin.Metadata { *; }

# Keep default interface implementations
-keep interface com.myapp.domain.** { *; }
```

#### 4.3 Full Mode Migration Checklist

```markdown
- [ ] Enable `android.enableR8.fullMode=true` in gradle.properties
- [ ] Build release APK -- note all warnings and errors
- [ ] Run full test suite against release build
- [ ] Test every serialization path (JSON, Bundle, Parcelable, Room)
- [ ] Test every API endpoint (Retrofit interfaces)
- [ ] Test every WorkManager worker
- [ ] Test enum deserialization with all possible server values
- [ ] Test deep link handling
- [ ] Test process death and restoration
- [ ] Compare APK size (expect 5-15% additional reduction)
- [ ] Monitor crash-free rate for 48 hours after staged rollout
```

---

### Phase 5: Testing Strategy

Establish a testing approach that catches R8 issues before they reach production.

#### 5.1 Automated Release Build Testing

```groovy
// app/build.gradle.kts
android {
    buildTypes {
        // Create a debug build type that uses release shrinking
        create("debugMinified") {
            initWith(getByName("debug"))
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
            // Keep debuggable for easier stack traces
            isDebuggable = true
            signingConfig = signingConfigs.getByName("debug")
        }
    }
}
```

#### 5.2 Critical Path Test Suite

```kotlin
/**
 * Tests that MUST pass on minified builds.
 * Run with: ./gradlew connectedDebugMinifiedAndroidTest
 */
@RunWith(AndroidJUnit4::class)
class R8CriticalPathTests {

    @Test
    fun `serialization round-trip for all data models`() {
        // For each data model class, serialize to JSON and back
        val original = UserProfile(id = "123", displayName = "Test", email = "t@t.com")
        val json = gson.toJson(original)
        val restored = gson.fromJson(json, UserProfile::class.java)
        assertEquals(original, restored)
    }

    @Test
    fun `all API interfaces are callable`() {
        // Verify Retrofit can create implementations
        val api = retrofit.create(ApiService::class.java)
        assertNotNull(api)
        // Verify method is accessible (does not throw)
        val method = api.javaClass.getMethod("getUser", String::class.java)
        assertNotNull(method)
    }

    @Test
    fun `all enum values survive obfuscation`() {
        // Verify enum valueOf works for all values
        OrderStatus.values().forEach { status ->
            val restored = OrderStatus.valueOf(status.name)
            assertEquals(status, restored)
        }
    }

    @Test
    fun `parcelable classes survive bundle round-trip`() {
        val original = UserProfile(id = "123", displayName = "Test", email = "t@t.com")
        val bundle = Bundle().apply { putParcelable("user", original) }
        val restored = bundle.getParcelable<UserProfile>("user")
        assertEquals(original, restored)
    }

    @Test
    fun `WorkManager workers can be instantiated`() {
        // Verify WorkManager can find and create workers
        val workerClass = Class.forName("com.myapp.workers.SyncWorker")
        assertNotNull(workerClass)
    }
}
```

#### 5.3 CI Integration

```yaml
# .github/workflows/release-validation.yml
name: Release Build Validation

on:
  pull_request:
    branches: [main]

jobs:
  release-build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build minified debug
        run: ./gradlew assembleDebugMinified

      - name: Run R8 critical path tests
        run: ./gradlew connectedDebugMinifiedAndroidTest
          -Pandroid.testInstrumentationRunnerArguments.class=com.myapp.R8CriticalPathTests

      - name: Compare APK size
        run: |
          SIZE=$(stat -c%s app/build/outputs/apk/debugMinified/app-debugMinified.apk)
          echo "APK size: $SIZE bytes"
          # Fail if APK exceeds size budget
          if [ $SIZE -gt 20000000 ]; then
            echo "APK exceeds 20MB size budget!"
            exit 1
          fi

      - name: Archive mapping file
        uses: actions/upload-artifact@v4
        with:
          name: mapping
          path: app/build/outputs/mapping/debugMinified/mapping.txt
```

---

## Expected Output

The analysis should produce an R8 optimization report with the following structure:

### Output Format

```markdown
# R8/ProGuard Optimization Report
**Project:** [Project Name]
**Date:** [Date]
**Current APK Size:** [X] MB
**R8 Mode:** [Compatibility / Full]
**AGP Version:** [X.Y.Z]

## Configuration Audit
### Rule Sources
[List of all rule files and consumer rules]

### Rule Classification
| Rule | Category | Necessary? | Recommendation |
|------|----------|-----------|----------------|
[All rules categorized and assessed]

## Crash Risk Assessment
### Missing Rules Identified
[Classes/members at risk with evidence]

### Recommended Rule Additions
[Specific rules with explanation]

## Size Optimization
### Over-Broad Rules
[Rules to tighten with before/after impact]

### Shrinking Effectiveness
[Size metrics before and after]

## R8 Full Mode Assessment
### Migration Readiness: [Ready / Needs Work / Not Recommended]
[Assessment with specific blockers if any]

## Testing Strategy
### Critical Path Tests
[Test implementations or recommendations]

### CI Integration
[Pipeline configuration]

## Summary of Changes
| Change | Type | Size Impact | Risk |
|--------|------|-------------|------|
[All recommended changes with impact assessment]
```

---

## Customization Guide

- **For apps using Kotlin Serialization instead of Gson:** Replace Gson keep rules with `@Serializable` annotation keeps. Kotlin Serialization uses compile-time code generation and requires fewer keep rules than Gson.
- **For apps using Moshi with codegen:** Moshi's codegen adapter eliminates most reflection. Keep rules are only needed for `@JsonClass(generateAdapter = false)` classes.
- **For apps with WebView JavaScript interfaces:** Add `-keepclassmembers class * { @android.webkit.JavascriptInterface <methods>; }` to prevent removal of JS bridge methods.
- **For apps targeting APK (not AAB):** Focus on DEX optimization since you cannot rely on Play Store's per-device APK splitting. Consider multi-DEX threshold.
- **For apps with dynamic feature modules:** Each module needs its own ProGuard configuration. Use `consumerProguardFiles` to propagate rules from feature modules to the base module.
- **For multi-flavor builds:** Create per-flavor rule files (`proguard-rules-free.pro`, `proguard-rules-paid.pro`) to keep only classes used in each flavor.

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** The objective defines a five-part deliverable: audit, crash-risk identification, size optimization, R8 full mode evaluation, and testing strategy.
- **ST-02 (Structured Sequential Instructions):** Five phases build from understanding (audit) through risk identification, optimization, migration, and testing.
- **RT-02 (Multi-Dimensional Analysis):** Each rule is analyzed across necessity (is it needed?), scope (is it too broad?), and impact (what does it cost in APK size?).
- **RT-05 (Evidence-Based Reasoning):** Diagnostic output files (`seeds.txt`, `usage.txt`, `mapping.txt`) provide concrete evidence for every recommendation rather than guesswork.
- **QA-02 (Adversarial Thinking):** False-Positive Prevention guards against blanket keep rules, premature full mode migration, and removing library-required rules.

---

## Related Prompts

- [android_app_bundle_optimization.md](../publishing/android_app_bundle_optimization.md) - Broader APK/AAB size optimization beyond R8
- [android_release_preparation.md](../publishing/android_release_preparation.md) - Complete release checklist including R8 verification
- [android_performance_audit.md](../analysis/android_performance_audit.md) - Performance analysis that may surface R8-related issues
- [android_dependency_update.md](android_dependency_update.md) - Dependency updates may require R8 rule changes
