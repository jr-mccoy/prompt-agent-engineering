---
title: "Android SDK Migration"
category: mobile-development
description: "Guides migration from deprecated Android SDK components and legacy APIs to modern replacements with minimal disruption"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-02
  - QA-01
difficulty: advanced
tags:
  - android
  - mobile-development
  - sdk-migration
  - deprecated-apis
  - maintenance
updated: "2026-06-06"
related_prompts:
  - domain-software-engineering/mobile/android/maintenance/android_target_sdk_migration.md
  - domain-software-engineering/mobile/android/maintenance/android_min_sdk_raise_planner.md
  - domain-software-engineering/mobile/android/improvement/android_code_modernization.md
  - domain-software-engineering/mobile/android/maintenance/android_dependency_update.md
---

# Android SDK Migration

**Objective:** Guide comprehensive migration from deprecated Android SDK components, legacy APIs, and outdated architectural patterns to their modern replacements, ensuring a smooth transition with minimal disruption.

**When to Use:** Use this prompt when you need to migrate away from deprecated Android APIs or architectural patterns—such as AsyncTask to Coroutines, LiveData to StateFlow, Loaders to ViewModels, or Support Library to AndroidX. Ideal when encountering deprecation warnings in builds, when legacy code blocks adoption of new features, or during planned modernization efforts. Prerequisites include identifying the specific deprecated components and understanding your app's architecture.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before beginning the SDK migration, gather essential context:

1. **Migration Scope:**
   - "What deprecated APIs or components are you migrating from?"
   - "Are you doing a full migration or incremental/partial migration?"
   - "What is the timeline and urgency for this migration?"

2. **Current State:**
   - "What Android versions does your app support (minSdk)?"
   - "Are you using any compatibility libraries for the deprecated APIs?"
   - "How widespread is the usage of the deprecated component?"

3. **Target State:**
   - "What modern replacement are you migrating to?"
   - "Are there specific patterns or implementations you want to follow?"
   - "Do you need to maintain backward compatibility?"

4. **Constraints:**
   - "Are there any third-party libraries dependent on the deprecated APIs?"
   - "Do you have test coverage for the components being migrated?"
   - "Are there any performance or stability requirements?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY migration, you MUST:**

1. **Trace actual deprecation usage** - Don't recommend migrations without confirming the deprecated API is actually used.
2. **Check for existing migrations** - Search for partial migrations or compatibility layers already in place.
3. **Understand the context** - Consider WHY specific patterns exist. Some "deprecated" code may work fine for years.
4. **Confirm actual benefit** - Will migration provide real value, or just cause churn?
5. **Provide specific file:line locations** - Every migration recommendation must include exact code locations.

**Recommending NO migration is sometimes correct.** Stable deprecated code may not need immediate attention.

### False-Positive Prevention

- ❌ Do NOT recommend migrating all deprecated APIs at once
- ❌ Do NOT assume deprecated means broken
- ❌ Do NOT ignore test coverage when recommending risky migrations
- ❌ Do NOT recommend migrations without clear benefit
- ✅ DO prioritize deprecations that actually affect functionality
- ✅ DO consider incremental migration over big-bang approaches
- ✅ DO check if deprecation warnings are actually relevant
- ✅ DO understand compatibility library alternatives

---

### Phase 1: Migration Assessment

Analyze the scope and complexity of the migration.

#### 1.1 Deprecated API Inventory

**Identify all deprecated usages:**

```kotlin
// Common deprecated APIs to search for:

// Threading & Async
// - AsyncTask → Coroutines
// - IntentService → WorkManager/Coroutines
// - Loader → ViewModel + Repository
// - Handler(Looper) → Coroutines

// Architecture
// - LiveData → StateFlow (where appropriate)
// - Fragment.setRetainInstance → ViewModel
// - onActivityResult → Activity Result API

// UI
// - Support Library → AndroidX
// - ListView → RecyclerView
// - Kotlin synthetics → ViewBinding
// - ProgressDialog → Custom dialog/inline

// Storage
// - SharedPreferences → DataStore
// - SQLiteOpenHelper → Room
// - File storage → Scoped storage

// Networking
// - HttpURLConnection → OkHttp/Retrofit
// - AsyncHttpClient → Retrofit + Coroutines

// Permissions
// - requestPermissions → Activity Result API
```

**Create deprecation inventory:**

| Component | Usage Count | Files Affected | Complexity | Priority |
|-----------|-------------|----------------|------------|----------|
| AsyncTask | 12 | 8 | Medium | High |
| LiveData | 45 | 20 | Low | Medium |
| onActivityResult | 6 | 4 | Low | Medium |
| Kotlin synthetics | 150 | 35 | Low | High |

#### 1.2 Dependency Analysis

**Analyze dependencies that may block migration:**

```kotlin
// Check for:

// 1. Libraries using deprecated APIs internally
dependencies {
    // Some older libraries may require deprecated APIs
    implementation("legacy:library:1.0") // Uses AsyncTask internally
}

// 2. Base classes exposing deprecated APIs
abstract class BaseViewModel : ViewModel() {
    // Exposes LiveData - affects all ViewModels
    protected val _loading = MutableLiveData<Boolean>()
    val loading: LiveData<Boolean> = _loading
}

// 3. Interfaces tied to deprecated patterns
interface DataCallback<T> {
    fun onSuccess(data: T)  // Callback pattern → Coroutines
    fun onError(error: Throwable)
}
```

#### 1.3 Risk Assessment

**Evaluate migration risks:**

```markdown
## Risk Matrix

### High Risk
- Components with no test coverage
- Shared/base classes used throughout app
- APIs with behavioral differences in replacement
- Third-party library dependencies

### Medium Risk
- Components with partial test coverage
- Feature-specific implementations
- APIs with equivalent replacements
- Direct 1:1 migration paths

### Low Risk
- Well-tested components
- Isolated usages
- Simple syntactic changes
- Well-documented migration paths
```

---

### Phase 2: Migration Strategy Design

Design the migration approach based on assessment.

#### 2.1 Migration Patterns

**Select appropriate migration strategy:**

```kotlin
// Strategy 1: Big Bang Migration
// - Migrate all usages at once
// - Best for: Small codebases, isolated components
// - Risk: High, but complete

// Strategy 2: Strangler Fig Pattern
// - Gradually replace old with new
// - Maintain both systems temporarily
// - Best for: Large codebases, critical paths
// - Risk: Low, but longer timeline

// Strategy 3: Branch by Abstraction
// - Create abstraction layer
// - Implement both old and new behind abstraction
// - Switch implementations gradually
// - Best for: Deeply embedded APIs

// Example: Branch by Abstraction for AsyncTask → Coroutines
interface AsyncOperation<T> {
    suspend fun execute(): T
}

// Old implementation
class AsyncTaskOperation<T>(
    private val task: AsyncTask<Unit, Unit, T>
) : AsyncOperation<T> {
    override suspend fun execute(): T = withContext(Dispatchers.IO) {
        // Bridge to AsyncTask
    }
}

// New implementation
class CoroutineOperation<T>(
    private val block: suspend () -> T
) : AsyncOperation<T> {
    override suspend fun execute(): T = block()
}
```

#### 2.2 Migration Order Planning

**Determine optimal migration order:**

```markdown
## Recommended Migration Order

### Layer 1: Foundation (Do First)
- Base classes and interfaces
- Utility classes
- DI modules providing deprecated types

### Layer 2: Data Layer
- Repositories
- Data sources
- Network clients

### Layer 3: Domain Layer
- Use cases
- Business logic

### Layer 4: Presentation Layer
- ViewModels
- UI components

### Layer 5: Entry Points (Do Last)
- Activities/Fragments
- Services
- Broadcast receivers
```

---

### Phase 3: Findings Presentation

**CHECKPOINT 1:** Present the migration assessment and strategy.

```markdown
## SDK Migration Analysis Report

### Migration Summary
| Metric | Value |
|--------|-------|
| Deprecated API | AsyncTask |
| Modern Replacement | Kotlin Coroutines |
| Total Usages | 24 |
| Files Affected | 15 |
| Test Coverage | 45% |
| Estimated Effort | Medium |

### Usage Breakdown

#### By Component Type
| Type | Count | Complexity |
|------|-------|------------|
| Repository | 8 | Medium |
| ViewModel | 6 | Low |
| Service | 4 | High |
| Utility | 6 | Low |

#### High-Risk Migrations
1. **BackgroundSyncService** - Complex AsyncTask with progress updates
2. **ImageProcessingTask** - Memory-intensive operations
3. **DatabaseMigrationTask** - Long-running with checkpoints

### Recommended Strategy
**Strangler Fig Pattern** with the following phases:

1. **Phase 1:** Add Coroutine infrastructure (scope, dispatchers)
2. **Phase 2:** Migrate utility classes (low risk)
3. **Phase 3:** Migrate repositories (medium risk)
4. **Phase 4:** Migrate ViewModels (low risk)
5. **Phase 5:** Migrate services (high risk)
6. **Phase 6:** Remove AsyncTask dependencies

### Effort Estimate
- Phase 1-2: Low effort
- Phase 3-4: Medium effort
- Phase 5-6: High effort

**Would you like me to proceed with Phase 1?**
```

---

### Phase 4: Implementation

Execute migration systematically.

#### 4.1 AsyncTask to Coroutines Migration

**Step 1: Add Coroutine infrastructure**

```kotlin
// build.gradle.kts
dependencies {
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3")
}

// Create coroutine scope provider
interface CoroutineScopeProvider {
    val mainScope: CoroutineScope
    val ioScope: CoroutineScope
}

class DefaultCoroutineScopeProvider : CoroutineScopeProvider {
    override val mainScope = CoroutineScope(
        SupervisorJob() + Dispatchers.Main.immediate
    )
    override val ioScope = CoroutineScope(
        SupervisorJob() + Dispatchers.IO
    )
}
```

**Step 2: Migrate simple AsyncTask**

```kotlin
// Before: AsyncTask
class FetchDataTask(
    private val callback: (List<Item>) -> Unit
) : AsyncTask<Void, Void, List<Item>>() {

    override fun doInBackground(vararg params: Void?): List<Item> {
        return repository.fetchItems()
    }

    override fun onPostExecute(result: List<Item>) {
        callback(result)
    }
}

// Usage
FetchDataTask { items ->
    updateUI(items)
}.execute()

// After: Coroutines
class ItemRepository(
    private val dispatcher: CoroutineDispatcher = Dispatchers.IO
) {
    suspend fun fetchItems(): List<Item> = withContext(dispatcher) {
        // Same logic as doInBackground
        dataSource.getItems()
    }
}

// Usage in ViewModel
class ItemViewModel(
    private val repository: ItemRepository
) : ViewModel() {

    private val _items = MutableStateFlow<List<Item>>(emptyList())
    val items: StateFlow<List<Item>> = _items.asStateFlow()

    fun loadItems() {
        viewModelScope.launch {
            _items.value = repository.fetchItems()
        }
    }
}
```

**Step 3: Migrate AsyncTask with progress**

```kotlin
// Before: AsyncTask with progress
class DownloadTask(
    private val progressCallback: (Int) -> Unit,
    private val completeCallback: (File) -> Unit
) : AsyncTask<String, Int, File>() {

    override fun doInBackground(vararg urls: String): File {
        val url = urls[0]
        var progress = 0
        // Download with progress
        while (downloading) {
            progress += 10
            publishProgress(progress)
        }
        return downloadedFile
    }

    override fun onProgressUpdate(vararg values: Int?) {
        progressCallback(values[0] ?: 0)
    }

    override fun onPostExecute(result: File) {
        completeCallback(result)
    }
}

// After: Coroutines with Flow
class DownloadRepository {

    fun downloadFile(url: String): Flow<DownloadState> = flow {
        emit(DownloadState.Starting)

        var progress = 0
        while (downloading) {
            progress += 10
            emit(DownloadState.Progress(progress))
        }

        emit(DownloadState.Complete(downloadedFile))
    }.flowOn(Dispatchers.IO)
}

sealed class DownloadState {
    object Starting : DownloadState()
    data class Progress(val percent: Int) : DownloadState()
    data class Complete(val file: File) : DownloadState()
    data class Error(val exception: Throwable) : DownloadState()
}

// Usage in ViewModel
class DownloadViewModel(
    private val repository: DownloadRepository
) : ViewModel() {

    private val _downloadState = MutableStateFlow<DownloadState>(DownloadState.Starting)
    val downloadState: StateFlow<DownloadState> = _downloadState.asStateFlow()

    fun download(url: String) {
        viewModelScope.launch {
            repository.downloadFile(url).collect { state ->
                _downloadState.value = state
            }
        }
    }
}
```

#### 4.2 LiveData to StateFlow Migration

**Step 1: Migrate ViewModel state**

```kotlin
// Before: LiveData
class UserViewModel : ViewModel() {
    private val _user = MutableLiveData<User>()
    val user: LiveData<User> = _user

    private val _loading = MutableLiveData<Boolean>()
    val loading: LiveData<Boolean> = _loading

    fun loadUser(id: String) {
        _loading.value = true
        viewModelScope.launch {
            _user.value = repository.getUser(id)
            _loading.value = false
        }
    }
}

// After: StateFlow with UI State
data class UserUiState(
    val user: User? = null,
    val isLoading: Boolean = false,
    val error: String? = null
)

class UserViewModel(
    private val repository: UserRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow(UserUiState())
    val uiState: StateFlow<UserUiState> = _uiState.asStateFlow()

    fun loadUser(id: String) {
        viewModelScope.launch {
            _uiState.update { it.copy(isLoading = true) }
            try {
                val user = repository.getUser(id)
                _uiState.update { it.copy(user = user, isLoading = false) }
            } catch (e: Exception) {
                _uiState.update { it.copy(error = e.message, isLoading = false) }
            }
        }
    }
}
```

**Step 2: Update observers**

```kotlin
// Before: LiveData observer in Fragment
viewModel.user.observe(viewLifecycleOwner) { user ->
    updateUserUI(user)
}
viewModel.loading.observe(viewLifecycleOwner) { isLoading ->
    showLoading(isLoading)
}

// After: StateFlow collector in Fragment
viewLifecycleOwner.lifecycleScope.launch {
    viewLifecycleOwner.repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.uiState.collect { state ->
            updateUserUI(state.user)
            showLoading(state.isLoading)
            state.error?.let { showError(it) }
        }
    }
}

// After: In Compose
@Composable
fun UserScreen(viewModel: UserViewModel) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    when {
        uiState.isLoading -> LoadingIndicator()
        uiState.error != null -> ErrorMessage(uiState.error!!)
        uiState.user != null -> UserContent(uiState.user!!)
    }
}
```

#### 4.3 onActivityResult to Activity Result API Migration

**Step 1: Migrate permission requests**

```kotlin
// Before: onActivityResult
class OldActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        requestPermissions(
            arrayOf(Manifest.permission.CAMERA),
            CAMERA_PERMISSION_REQUEST
        )
    }

    override fun onRequestPermissionsResult(
        requestCode: Int,
        permissions: Array<out String>,
        grantResults: IntArray
    ) {
        if (requestCode == CAMERA_PERMISSION_REQUEST) {
            if (grantResults.isNotEmpty() &&
                grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                openCamera()
            }
        }
    }

    companion object {
        private const val CAMERA_PERMISSION_REQUEST = 100
    }
}

// After: Activity Result API
class NewActivity : AppCompatActivity() {

    private val cameraPermissionLauncher = registerForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted ->
        if (isGranted) {
            openCamera()
        } else {
            showPermissionDeniedMessage()
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        cameraPermissionLauncher.launch(Manifest.permission.CAMERA)
    }
}
```

**Step 2: Migrate activity results**

```kotlin
// Before: startActivityForResult
class OldActivity : AppCompatActivity() {

    fun selectImage() {
        val intent = Intent(Intent.ACTION_PICK).apply {
            type = "image/*"
        }
        startActivityForResult(intent, IMAGE_PICK_REQUEST)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == IMAGE_PICK_REQUEST && resultCode == RESULT_OK) {
            data?.data?.let { uri ->
                processImage(uri)
            }
        }
    }

    companion object {
        private const val IMAGE_PICK_REQUEST = 200
    }
}

// After: Activity Result API
class NewActivity : AppCompatActivity() {

    private val imagePickerLauncher = registerForActivityResult(
        ActivityResultContracts.GetContent()
    ) { uri: Uri? ->
        uri?.let { processImage(it) }
    }

    // Or use Photo Picker for images/videos
    private val photoPickerLauncher = registerForActivityResult(
        ActivityResultContracts.PickVisualMedia()
    ) { uri: Uri? ->
        uri?.let { processImage(it) }
    }

    fun selectImage() {
        // Simple content picker
        imagePickerLauncher.launch("image/*")

        // Or modern photo picker
        photoPickerLauncher.launch(
            PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly)
        )
    }
}
```

#### 4.4 Kotlin Synthetics to ViewBinding Migration

**Step 1: Enable ViewBinding**

```kotlin
// build.gradle.kts
android {
    buildFeatures {
        viewBinding = true
    }
}
```

**Step 2: Migrate layouts**

```kotlin
// Before: Kotlin synthetics
import kotlinx.android.synthetic.main.activity_main.*

class OldActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Direct view access via synthetics
        textTitle.text = "Hello"
        buttonSubmit.setOnClickListener { submit() }
        recyclerItems.adapter = adapter
    }
}

// After: ViewBinding
class NewActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // Type-safe view access
        binding.textTitle.text = "Hello"
        binding.buttonSubmit.setOnClickListener { submit() }
        binding.recyclerItems.adapter = adapter
    }
}

// In Fragment
class NewFragment : Fragment(R.layout.fragment_new) {

    private var _binding: FragmentNewBinding? = null
    private val binding get() = _binding!!

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        _binding = FragmentNewBinding.bind(view)

        binding.textTitle.text = "Hello"
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null  // Prevent memory leaks
    }
}
```

#### 4.5 SharedPreferences to DataStore Migration

**Step 1: Add DataStore dependency**

```kotlin
// build.gradle.kts
dependencies {
    implementation("androidx.datastore:datastore-preferences:1.0.0")
}
```

**Step 2: Migrate preferences**

```kotlin
// Before: SharedPreferences
class OldPreferencesManager(context: Context) {

    private val prefs = context.getSharedPreferences("settings", Context.MODE_PRIVATE)

    var isDarkMode: Boolean
        get() = prefs.getBoolean("dark_mode", false)
        set(value) = prefs.edit().putBoolean("dark_mode", value).apply()

    var username: String?
        get() = prefs.getString("username", null)
        set(value) = prefs.edit().putString("username", value).apply()

    fun clear() {
        prefs.edit().clear().apply()
    }
}

// After: DataStore
class NewPreferencesManager(private val context: Context) {

    private val Context.dataStore by preferencesDataStore(name = "settings")

    private object PreferencesKeys {
        val DARK_MODE = booleanPreferencesKey("dark_mode")
        val USERNAME = stringPreferencesKey("username")
    }

    val isDarkMode: Flow<Boolean> = context.dataStore.data
        .map { preferences ->
            preferences[PreferencesKeys.DARK_MODE] ?: false
        }

    val username: Flow<String?> = context.dataStore.data
        .map { preferences ->
            preferences[PreferencesKeys.USERNAME]
        }

    suspend fun setDarkMode(enabled: Boolean) {
        context.dataStore.edit { preferences ->
            preferences[PreferencesKeys.DARK_MODE] = enabled
        }
    }

    suspend fun setUsername(name: String) {
        context.dataStore.edit { preferences ->
            preferences[PreferencesKeys.USERNAME] = name
        }
    }

    suspend fun clear() {
        context.dataStore.edit { it.clear() }
    }
}
```

---

### Phase 5: Testing & Verification

Verify migration correctness and stability.

#### 5.1 Migration Testing Strategy

**Test each migrated component:**

```kotlin
// Unit test for migrated repository
@Test
fun `fetchItems returns items from data source`() = runTest {
    // Given
    val expected = listOf(Item("1"), Item("2"))
    coEvery { dataSource.getItems() } returns expected

    // When
    val result = repository.fetchItems()

    // Then
    assertEquals(expected, result)
}

// Test for StateFlow behavior
@Test
fun `loadUser updates ui state correctly`() = runTest {
    // Given
    val user = User("123", "John")
    coEvery { repository.getUser("123") } returns user

    // When
    viewModel.loadUser("123")

    // Then
    val state = viewModel.uiState.value
    assertFalse(state.isLoading)
    assertEquals(user, state.user)
    assertNull(state.error)
}
```

#### 5.2 Regression Testing

**Verify no behavioral changes:**

```markdown
## Migration Regression Checklist

### Functional Verification
- [ ] All async operations complete successfully
- [ ] Progress updates display correctly
- [ ] Error handling works as expected
- [ ] Cancellation behavior preserved

### Performance Verification
- [ ] No memory leaks introduced
- [ ] No ANRs from main thread blocking
- [ ] Background operations don't block UI

### Edge Cases
- [ ] Configuration changes handled correctly
- [ ] Process death and restoration works
- [ ] Network errors handled properly
- [ ] Empty/null states handled
```

---

## Expected Output

### Migration Completion Report

```markdown
# SDK Migration Report

## Summary
| Metric | Value |
|--------|-------|
| Deprecated API | AsyncTask |
| Replacement | Kotlin Coroutines |
| Files Migrated | 15 |
| Usages Removed | 24 |
| Test Coverage | 85% (up from 45%) |

## Changes Made

### Phase 1: Infrastructure
- Added kotlinx-coroutines-android dependency
- Created CoroutineScopeProvider interface
- Updated DI modules with dispatchers

### Phase 2: Repository Layer
| File | Changes |
|------|---------|
| UserRepository.kt | Migrated 3 AsyncTasks to suspend functions |
| ItemRepository.kt | Migrated 2 AsyncTasks to Flow |
| SyncRepository.kt | Migrated 3 AsyncTasks with progress |

### Phase 3: ViewModel Layer
| File | Changes |
|------|---------|
| UserViewModel.kt | Updated to use StateFlow |
| ItemViewModel.kt | Migrated async loading |
| SyncViewModel.kt | Added progress collection |

### Phase 4: Service Layer
| File | Changes |
|------|---------|
| SyncService.kt | Converted to CoroutineWorker |
| DownloadService.kt | Migrated to coroutines |

## Removed Dependencies
- Removed AsyncTask imports from 15 files
- Removed deprecated callbacks from 8 interfaces

## Test Results
| Test Type | Passed | Failed | Coverage |
|-----------|--------|--------|----------|
| Unit Tests | 45 | 0 | 85% |
| Integration | 12 | 0 | 70% |
| UI Tests | 8 | 0 | 60% |

## Known Issues
- None

## Recommendations
- Consider migrating remaining LiveData to StateFlow
- Add coroutine exception handlers for better error tracking
```

---

## Example Interaction

**User:** Our app has a lot of AsyncTask usage and we want to migrate to Coroutines. Where do we start?

**Agent:** I'll help you migrate from AsyncTask to Kotlin Coroutines. Let me analyze your codebase to understand the scope.

*[Agent searches for AsyncTask usage patterns]*

## AsyncTask Migration Analysis

### Inventory
I found **24 AsyncTask usages** across **15 files**:

| Category | Count | Files |
|----------|-------|-------|
| Data fetching | 12 | Repository classes |
| File operations | 6 | FileUtils, DownloadManager |
| Database operations | 4 | Legacy DB helpers |
| Image processing | 2 | ImageProcessor |

### Complexity Assessment

**Simple Migrations (14 usages):**
- Basic `doInBackground` → `suspend fun`
- No progress updates
- Single result callback

**Medium Complexity (8 usages):**
- Progress updates → `Flow`
- Multiple callbacks → sealed class states
- Error handling → try/catch with Result

**Complex Migrations (2 usages):**
- `BackgroundSyncTask` - Long-running with checkpoints
- `BatchProcessingTask` - Parallel processing with progress

### Recommended Migration Path

**Phase 1: Setup (Low effort)**
- Add coroutines dependency
- Create coroutine scope utilities
- Update DI modules

**Phase 2: Simple migrations (Medium effort)**
- Migrate 14 simple AsyncTasks
- Focus on repositories first

**Phase 3: Complex migrations (High effort)**
- Migrate tasks with progress
- Update services to use WorkManager

### Dependencies to Update
- Your `BaseRepository` uses callbacks - needs interface update
- `NetworkClient` has async methods - wrap with coroutines

Would you like me to start with Phase 1, setting up the coroutine infrastructure?

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for SDK migration
- **ST-02** (Sequential Instructions): Phased migration approach
- **RT-02** (Multi-Dimensional Analysis): Code patterns, dependencies, risk assessment
- **RT-04** (Best Practice Review): Modern Android patterns (Coroutines, Flow, StateFlow)
- **RT-05** (Evidence-Based Reasoning): Specific code examples and migration paths
- **ST-03** (Output Format Templates): Structured migration reports and checklists
- **OC-05** (Severity Classification): Complexity ratings for migrations
- **AG-02** (Skeptical Default Stance): Risk assessment and testing verification
- **AG-12** (Quantitative Metrics): Usage counts, coverage metrics
- **NE-02** (Phased Workflow): Discovery → Assessment → Strategy → Implementation
- **NE-07** (Discussion Before Action): Approval checkpoints between phases

---

## Related Prompts

- [android_version_upgrade.md](android_version_upgrade.md) - targetSdk upgrades with behavior changes
- [android_dependency_update.md](android_dependency_update.md) - Update library dependencies
- [android_code_modernization.md](../improvement/android_code_modernization.md) - Broader modernization effort
- [android_technical_debt_assessment.md](../analysis/android_technical_debt_assessment.md) - Identify deprecated API debt
- [android_test_strategy_design.md](../testing/android_test_strategy_design.md) - Test coverage for migrations

---

## Customization Guide

### By Migration Type

**Threading Migrations (AsyncTask, IntentService, Handlers):**
- Focus on coroutine scope management
- Emphasize cancellation handling
- Consider WorkManager for persistent work

**Architecture Migrations (LiveData, Loaders, setRetainInstance):**
- Plan UI state modeling
- Consider MVI for complex screens
- Update observers/collectors

**Storage Migrations (SharedPreferences, SQLite, File storage):**
- Plan data migration strategy
- Handle backward compatibility
- Test data integrity

**UI Migrations (Synthetics, ListView, Support Library):**
- Consider batch file changes
- Update test assertions
- Verify resource references

### By Codebase Size

**Small Codebase (< 50 usages):**
- Big bang migration feasible
- Single PR approach
- Comprehensive testing

**Medium Codebase (50-200 usages):**
- Feature-by-feature migration
- Multiple PRs by layer
- Incremental testing

**Large Codebase (200+ usages):**
- Strangler fig pattern recommended
- Branch by abstraction for core APIs
- Dedicated migration sprints

### By Risk Tolerance

**Low Risk Tolerance (Production Critical):**
- Extensive testing at each phase
- Feature flags for new implementations
- Parallel running during transition
- Staged rollout

**Medium Risk Tolerance:**
- Standard test coverage
- Phase-by-phase verification
- Regular release cycle

**High Risk Tolerance (Internal/Development):**
- Rapid migration
- Smoke testing focus
- Quick iteration

### By Team Structure

**Single Developer:**
- Sequential migration
- One component at a time
- Self-review

**Small Team:**
- Divide by layer/feature
- Code review each migration
- Shared migration patterns

**Large Team:**
- Migration guide documentation
- Pattern examples
- Training sessions
- Code review standards
