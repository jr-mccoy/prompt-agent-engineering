---
title: "Android Code Modernization"
category: mobile-development
description: "Systematically modernizes an Android codebase to current best practices, migrating deprecated APIs and adopting modern Kotlin and Jetpack conventions"
techniques:
  - ST-01
  - ST-02
  - RT-04
  - RT-05
  - DS-06
  - ST-03
  - NE-02
  - NE-07
difficulty: advanced
tags:
  - android
  - mobile-development
  - modernization
  - kotlin
  - jetpack
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_codebase_health_assessment.md
  - domain-software-engineering/mobile/android/analysis/android_architecture_review.md
  - domain-software-engineering/mobile/android/analysis/android_dependency_audit.md
  - domain-software-engineering/mobile/android/improvement/android_kotlin_refactoring.md
---

# Android Code Modernization

**Objective:** Systematically modernize an Android codebase to current best practices, migrating from deprecated patterns, updating APIs, and adopting modern Kotlin and Jetpack conventions.

**When to Use:** Use this prompt when you need to update an Android app to modern standards, migrate from deprecated APIs, convert legacy patterns to current best practices, or prepare a codebase for new development. Ideal after a codebase health assessment identifies modernization opportunities, during planned tech debt reduction sprints, or before major feature development.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before beginning modernization, understand the scope and constraints:

1. **Current State:**
   - "What's the oldest part of this codebase (age, original Android/Kotlin versions)?"
   - "Are there known areas that feel 'legacy' or difficult to work with?"

2. **Constraints:**
   - "What's the minimum SDK version you need to support?"
   - "Are there any dependencies or integrations that constrain what can be updated?"
   - "Is there a preference for incremental changes vs larger refactors?"

3. **Priorities:**
   - "What's most important: stability, performance, developer experience, or maintainability?"
   - "Are there specific modernization goals (e.g., Compose migration, coroutines adoption)?"

4. **Risk Tolerance:**
   - "Are there areas that are 'off limits' due to stability concerns?"
   - "What's the testing coverage like for areas we might modernize?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual deprecation status** - Don't flag based on age alone. Verify that the code actually uses deprecated APIs or patterns.
2. **Check for existing modernization** - Search for migration work in progress or planned updates.
3. **Understand the context** - Consider WHY legacy patterns exist. Compatibility requirements and stability may justify older approaches.
4. **Confirm actual benefit** - Does modernizing this provide real value? Some "legacy" code works fine and doesn't need updating.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `LegacyFragment.kt:23`).

**Finding LIMITED modernization needs is an acceptable outcome.** If the code is reasonably modern and working, say so with confidence. Don't manufacture modernization urgency.

### False-Positive Prevention

- ❌ Do NOT flag working stable code as "must modernize"
- ❌ Do NOT assume all older patterns are wrong
- ❌ Do NOT recommend modernization without considering migration risk
- ❌ Do NOT report stylistic preferences as modernization requirements
- ✅ DO differentiate between deprecated APIs and just older patterns
- ✅ DO consider test coverage before recommending changes
- ✅ DO understand the stability vs. modernity trade-off
- ✅ DO prioritize actual deprecations over cosmetic updates

---

### Phase 1: Modernization Opportunity Discovery

#### 1.1 Kotlin Language Modernization

**Scan for outdated Kotlin patterns:**

```kotlin
// OUTDATED: Java-style null checks
if (user != null) {
    val name = user.name
}

// MODERN: Safe call and elvis operator
val name = user?.name ?: "Unknown"

// OUTDATED: Explicit type declarations
val list: List<String> = ArrayList<String>()

// MODERN: Type inference
val list = mutableListOf<String>()

// OUTDATED: Manual string building
val message = "User: " + name + ", Age: " + age

// MODERN: String templates
val message = "User: $name, Age: $age"
```

**Kotlin Modernization Checklist:**

| Pattern | Current State | Modern Alternative |
|---------|--------------|-------------------|
| Null handling | `if (x != null)` | `?.let`, `?:`, `?.` |
| String building | Concatenation | String templates |
| Collections | Java collections | Kotlin collections |
| Loops | Traditional for loops | `forEach`, `map`, `filter` |
| Type declarations | Explicit everywhere | Type inference |
| Singleton | Object + companion | `object` declaration |
| Data classes | Regular class + equals/hashCode | `data class` |
| Sealed classes | Enum + when else | `sealed class/interface` |
| Scope functions | Verbose code | `let`, `run`, `apply`, `also`, `with` |

#### 1.2 Deprecated Android API Detection

**Search for deprecated APIs:**

```kotlin
// DEPRECATED: AsyncTask
class MyTask : AsyncTask<Void, Void, Result>() {
    override fun doInBackground(vararg params: Void?): Result { }
}
// MODERN: Coroutines
suspend fun doWork(): Result = withContext(Dispatchers.IO) { }

// DEPRECATED: Loader
class MyLoader : AsyncTaskLoader<Data>(context) { }
// MODERN: ViewModel + Flow

// DEPRECATED: LocalBroadcastManager
LocalBroadcastManager.getInstance(context).sendBroadcast(intent)
// MODERN: Flow, LiveData, or EventBus patterns

// DEPRECATED: startActivityForResult
startActivityForResult(intent, REQUEST_CODE)
// MODERN: Activity Result API
val launcher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { }
```

#### 1.3 Jetpack Migration Opportunities

**Identify Jetpack adoption gaps:**

```kotlin
// Legacy: SharedPreferences
val prefs = getSharedPreferences("prefs", MODE_PRIVATE)
prefs.edit().putString("key", value).apply()
// Modern: DataStore
val dataStore = context.dataStore
dataStore.edit { it[KEY] = value }

// Legacy: LiveData everywhere
private val _data = MutableLiveData<Data>()
val data: LiveData<Data> = _data
// Modern: StateFlow (especially with Compose)
private val _data = MutableStateFlow<Data>(initial)
val data: StateFlow<Data> = _data.asStateFlow()

// Legacy: Manual fragment transactions
supportFragmentManager.beginTransaction()
    .replace(R.id.container, fragment)
    .addToBackStack(null)
    .commit()
// Modern: Navigation Component
navController.navigate(R.id.destination)

// Legacy: Manual ViewModel creation
val viewModel = ViewModelProviders.of(this).get(MyViewModel::class.java)
// Modern: by viewModels() delegate
val viewModel: MyViewModel by viewModels()
```

#### 1.4 Build System Modernization

**Check build configuration status:**

```kotlin
// Legacy: Groovy build files
build.gradle
apply plugin: 'com.android.application'

// Modern: Kotlin DSL
build.gradle.kts
plugins {
    id("com.android.application")
}

// Legacy: Hardcoded versions
implementation "androidx.core:core-ktx:1.9.0"

// Modern: Version catalog (libs.versions.toml)
[versions]
core-ktx = "1.12.0"
[libraries]
androidx-core-ktx = { module = "androidx.core:core-ktx", version.ref = "core-ktx" }

// In build.gradle.kts:
implementation(libs.androidx.core.ktx)
```

---

### Phase 2: Categorize Opportunities

**CHECKPOINT 1:** Present discovered modernization opportunities.

```markdown
## Modernization Opportunities Discovered

### Summary

| Category | Items Found | Effort | Impact |
|----------|-------------|--------|--------|
| Kotlin Language | [X] items | [Low/Med/High] | [Impact] |
| Deprecated APIs | [X] items | [Low/Med/High] | [Impact] |
| Jetpack Migration | [X] items | [Low/Med/High] | [Impact] |
| Build System | [X] items | [Low/Med/High] | [Impact] |

### Quick Wins (Low Effort, High Value)
1. [Opportunity] - [Location] - [Benefit]
2. [Opportunity] - [Location] - [Benefit]
3. [Opportunity] - [Location] - [Benefit]

### Strategic Improvements (Medium Effort)
1. [Opportunity] - [Files affected] - [Benefit]
2. [Opportunity] - [Files affected] - [Benefit]

### Major Migrations (High Effort)
1. [Migration] - [Scope] - [Risk level]
2. [Migration] - [Scope] - [Risk level]

### Questions

1. Which categories would you like to prioritize?
2. Are there any items we should skip due to constraints?
3. Should I proceed with quick wins immediately, or wait for full plan approval?
```

---

### Phase 3: Detailed Modernization Plan

After user feedback, create detailed implementation plan.

#### 3.1 Kotlin Language Improvements

**Priority: Force Unwrap (!!) Removal**

```kotlin
// Pattern to find:
grep -r "!!" --include="*.kt"

// Common fixes:

// BEFORE: Force unwrap
val name = user!!.name

// AFTER Option 1: Safe call with default
val name = user?.name ?: "Unknown"

// AFTER Option 2: Early return
val user = user ?: return
val name = user.name

// AFTER Option 3: Require (for programmer errors)
val name = requireNotNull(user) { "User should not be null here" }.name
```

**Priority: Scope Function Adoption**

```kotlin
// BEFORE: Verbose null check
if (user != null) {
    updateName(user.name)
    updateAge(user.age)
    saveUser(user)
}

// AFTER: let for null checks
user?.let {
    updateName(it.name)
    updateAge(it.age)
    saveUser(it)
}

// BEFORE: Builder pattern verbose
val intent = Intent(this, TargetActivity::class.java)
intent.putExtra("key1", value1)
intent.putExtra("key2", value2)
startActivity(intent)

// AFTER: apply for configuration
Intent(this, TargetActivity::class.java).apply {
    putExtra("key1", value1)
    putExtra("key2", value2)
}.also { startActivity(it) }
```

#### 3.2 Coroutines Migration

**From Callbacks to Coroutines:**

```kotlin
// BEFORE: Callback-based API
fun fetchUser(callback: (User?, Error?) -> Unit) {
    api.getUser(object : Callback<User> {
        override fun onSuccess(user: User) {
            callback(user, null)
        }
        override fun onError(error: Error) {
            callback(null, error)
        }
    })
}

// AFTER: Suspend function
suspend fun fetchUser(): Result<User> = withContext(Dispatchers.IO) {
    try {
        Result.success(api.getUser())
    } catch (e: Exception) {
        Result.failure(e)
    }
}

// AFTER: Using suspendCancellableCoroutine for legacy APIs
suspend fun fetchUser(): User = suspendCancellableCoroutine { continuation ->
    val call = api.getUser(object : Callback<User> {
        override fun onSuccess(user: User) {
            continuation.resume(user)
        }
        override fun onError(error: Error) {
            continuation.resumeWithException(error)
        }
    })
    continuation.invokeOnCancellation { call.cancel() }
}
```

**From RxJava to Coroutines:**

```kotlin
// BEFORE: RxJava Observable
fun getUsers(): Observable<List<User>> {
    return api.getUsers()
        .subscribeOn(Schedulers.io())
        .observeOn(AndroidSchedulers.mainThread())
}

// AFTER: Kotlin Flow
fun getUsers(): Flow<List<User>> = flow {
    emit(api.getUsers())
}.flowOn(Dispatchers.IO)

// ViewModel usage
viewModelScope.launch {
    getUsers().collect { users ->
        _usersState.value = users
    }
}
```

#### 3.3 Jetpack Migrations

**LiveData to StateFlow Migration:**

```kotlin
// BEFORE: LiveData in ViewModel
class UserViewModel : ViewModel() {
    private val _user = MutableLiveData<User>()
    val user: LiveData<User> = _user

    private val _loading = MutableLiveData<Boolean>()
    val loading: LiveData<Boolean> = _loading

    fun loadUser() {
        _loading.value = true
        viewModelScope.launch {
            _user.value = repository.getUser()
            _loading.value = false
        }
    }
}

// AFTER: StateFlow with UI State
data class UserUiState(
    val user: User? = null,
    val isLoading: Boolean = false,
    val error: String? = null
)

class UserViewModel : ViewModel() {
    private val _uiState = MutableStateFlow(UserUiState())
    val uiState: StateFlow<UserUiState> = _uiState.asStateFlow()

    fun loadUser() {
        viewModelScope.launch {
            _uiState.update { it.copy(isLoading = true) }
            try {
                val user = repository.getUser()
                _uiState.update { it.copy(user = user, isLoading = false) }
            } catch (e: Exception) {
                _uiState.update { it.copy(error = e.message, isLoading = false) }
            }
        }
    }
}

// Fragment/Compose collection
// In Fragment:
viewLifecycleOwner.lifecycleScope.launch {
    viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { state -> updateUi(state) }
    }
}

// In Compose:
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```

**SharedPreferences to DataStore Migration:**

```kotlin
// BEFORE: SharedPreferences
class PreferencesManager(context: Context) {
    private val prefs = context.getSharedPreferences("app_prefs", MODE_PRIVATE)

    var username: String
        get() = prefs.getString("username", "") ?: ""
        set(value) = prefs.edit().putString("username", value).apply()
}

// AFTER: Preferences DataStore
class PreferencesManager(private val context: Context) {

    private val Context.dataStore by preferencesDataStore(name = "app_prefs")

    private object PreferencesKeys {
        val USERNAME = stringPreferencesKey("username")
    }

    val username: Flow<String> = context.dataStore.data
        .map { preferences -> preferences[PreferencesKeys.USERNAME] ?: "" }

    suspend fun setUsername(value: String) {
        context.dataStore.edit { preferences ->
            preferences[PreferencesKeys.USERNAME] = value
        }
    }
}
```

**Activity Result API Migration:**

```kotlin
// BEFORE: onActivityResult
class MyActivity : AppCompatActivity() {
    companion object {
        private const val REQUEST_PICK_IMAGE = 1
    }

    fun pickImage() {
        val intent = Intent(Intent.ACTION_PICK)
        intent.type = "image/*"
        startActivityForResult(intent, REQUEST_PICK_IMAGE)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == REQUEST_PICK_IMAGE && resultCode == RESULT_OK) {
            val uri = data?.data
            // Handle image
        }
    }
}

// AFTER: Activity Result API
class MyActivity : AppCompatActivity() {

    private val pickImageLauncher = registerForActivityResult(
        ActivityResultContracts.GetContent()
    ) { uri: Uri? ->
        uri?.let { handleImage(it) }
    }

    fun pickImage() {
        pickImageLauncher.launch("image/*")
    }
}
```

#### 3.4 Build System Modernization

**Groovy to Kotlin DSL Migration:**

```kotlin
// BEFORE: build.gradle (Groovy)
plugins {
    id 'com.android.application'
    id 'kotlin-android'
}

android {
    compileSdk 34

    defaultConfig {
        applicationId "com.example.app"
        minSdk 24
        targetSdk 34
        versionCode 1
        versionName "1.0"
    }
}

dependencies {
    implementation "androidx.core:core-ktx:1.12.0"
}

// AFTER: build.gradle.kts (Kotlin DSL)
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.app"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"
    }
}

dependencies {
    implementation(libs.androidx.core.ktx)
}
```

**Version Catalog Setup:**

```toml
# gradle/libs.versions.toml
[versions]
kotlin = "1.9.21"
agp = "8.2.0"
core-ktx = "1.12.0"
lifecycle = "2.6.2"
compose-bom = "2024.01.00"

[libraries]
androidx-core-ktx = { module = "androidx.core:core-ktx", version.ref = "core-ktx" }
androidx-lifecycle-runtime = { module = "androidx.lifecycle:lifecycle-runtime-ktx", version.ref = "lifecycle" }
androidx-lifecycle-viewmodel = { module = "androidx.lifecycle:lifecycle-viewmodel-ktx", version.ref = "lifecycle" }

# Compose BOM
compose-bom = { module = "androidx.compose:compose-bom", version.ref = "compose-bom" }
compose-ui = { module = "androidx.compose.ui:ui" }
compose-material3 = { module = "androidx.compose.material3:material3" }

[bundles]
lifecycle = ["androidx-lifecycle-runtime", "androidx-lifecycle-viewmodel"]

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
```

---

### Phase 4: Implementation

**CHECKPOINT 2:** Before making changes, confirm the plan.

```markdown
## Implementation Plan Confirmation

### Changes to Make

**Immediate (Will do now):**
1. [Specific change] - [X files affected]
2. [Specific change] - [X files affected]

**Deferred (After verification):**
1. [Change requiring more testing]

### Files to Modify

| File | Changes | Risk |
|------|---------|------|
| [file] | [description] | [Low/Med/High] |

### Verification Steps
1. Build project after changes
2. Run existing tests
3. Manual verification of [areas]

**Proceed with implementation? (yes/no)**
```

---

### Phase 5: Execute and Report

After approval, make changes systematically:

1. **Make changes incrementally** - One category at a time
2. **Preserve behavior** - Refactor, don't change functionality
3. **Document changes** - Track all modifications
4. **Verify after each change** - Ensure builds pass

**Final Report:**

```markdown
## Modernization Complete

### Changes Made

| Category | Files Modified | Changes |
|----------|---------------|---------|
| Kotlin Language | [X] | [Summary] |
| Deprecated APIs | [X] | [Summary] |
| Jetpack | [X] | [Summary] |
| Build System | [X] | [Summary] |

### Detailed Change Log

#### Kotlin Language Improvements
- [file:line] - [Change description]
- [file:line] - [Change description]

#### Deprecated API Replacements
- [file:line] - [Old API] → [New API]

### Verification
- [ ] Project builds successfully
- [ ] All tests pass
- [ ] No new warnings introduced

### Remaining Opportunities
[Items not addressed in this session and why]

### Recommended Next Steps
1. [Follow-up action]
2. [Additional modernization]
```

---

## Expected Output

1. **Discovery Report** - All modernization opportunities found
2. **Prioritized Plan** - Categorized by effort and impact
3. **Implementation Details** - Specific code changes with before/after
4. **Change Log** - Record of all modifications made
5. **Verification Report** - Build and test status after changes

---

## Techniques Used

- **ST-01** (Clear Objective): Focused modernization objective
- **ST-02** (Sequential Instructions): Phased discovery → plan → implement
- **RT-04** (Best Practice Review): Modern Android/Kotlin standards
- **RT-05** (Evidence-Based Reasoning): Specific code locations
- **DS-06** (Prioritization Guidance): Effort/impact categorization
- **ST-03** (Output Format Templates): Structured reports
- **NE-02** (Phased Workflow): Clear checkpoints
- **NE-07** (Discussion Before Action): Approval gates before changes

---

## Related Prompts

- [android_codebase_health_assessment.md](../analysis/android_codebase_health_assessment.md) - Initial assessment
- [android_architecture_review.md](../analysis/android_architecture_review.md) - Architecture analysis
- [android_dependency_audit.md](../analysis/android_dependency_audit.md) - Dependency updates
- [android_kotlin_refactoring.md](android_kotlin_refactoring.md) - Kotlin-specific refactoring

---

## Customization Guide

### For Java to Kotlin Migration

Add Java-specific detection:
- Java files to convert
- Android-specific Java patterns
- Interoperability considerations
- Null annotation handling

### For Compose Migration

Focus on UI modernization:
- View to Composable conversion
- State hoisting patterns
- Navigation migration
- Theme/styling updates

### For Incremental Updates

Minimize risk approach:
- One file at a time
- Preserve all behavior
- Add tests before refactoring
- Feature flags for new code paths

### For Major Version Jumps

Handle breaking changes:
- API level deprecations
- Library migration guides
- Backward compatibility shims
- Staged rollout approach
