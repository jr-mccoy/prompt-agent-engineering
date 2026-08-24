---
title: "Android Process Death State Recovery Review"
category: mobile/android/targeted-reviews
description: "Android Process Death State Recovery Review."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - android
  - death
  - mobile
  - process
  - recovery
  - reviews
updated: "2026-03-19"
related_prompts: []
---

# Android Process Death State Recovery Review

**Objective:** Conduct a targeted review of process death handling in Android applications, analyzing SavedStateHandle usage, navigation state restoration, ViewModel state preservation, and user experience during process death recovery scenarios.

**When to Use:** Use this prompt when debugging state loss issues, before releasing complex forms or multi-step flows, when users report lost data after app backgrounding, during architecture review of new features, or when implementing "Don't keep activities" developer option testing.

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace the actual state lifecycle** - Don't flag based on pattern matching alone. Verify that the suspected state loss actually occurs during process death.
2. **Check for existing state preservation** - Search for SavedStateHandle, onSaveInstanceState, or persistent storage that may already handle the concern.
3. **Understand the context** - Consider WHAT state truly needs preservation. Not all state needs to survive process death.
4. **Confirm actual user impact** - Test with "Don't keep activities" developer option enabled.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `CheckoutViewModel.kt:89`).

**Finding NO issues is an acceptable outcome.** If state management handles process death correctly, say so with confidence. Don't manufacture state loss concerns.

### False-Positive Prevention

- ❌ Do NOT flag missing SavedStateHandle for state that can be re-fetched cheaply
- ❌ Do NOT flag transient UI state (loading, error) as needing preservation
- ❌ Do NOT assume state loss without testing actual process death scenarios
- ❌ Do NOT report issues for state that is intentionally cleared on process death
- ✅ DO test with "Don't keep activities" enabled on real devices
- ✅ DO understand the difference between configuration change and process death
- ✅ DO check for proper parcelization of complex saved state
- ✅ DO consider state size limits (< 1MB bundle size)

---

### 1. ViewModel State Preservation

Analyze SavedStateHandle integration:

* **SavedStateHandle Usage:**
  - Review which ViewModels use SavedStateHandle
  - Check for critical state saved vs. re-fetchable state
  - Assess SavedStateHandle injection pattern
  - Verify getStateFlow/getLiveData usage

* **State Selection:**
  - Review what state is persisted (user input, selections, scroll position)
  - Check that transient state is NOT persisted (loading, errors)
  - Assess parcelization of complex objects
  - Verify state size (should be < 1MB total)

* **State Restoration:**
  - Check restoration logic in ViewModel initialization
  - Review handling of stale restored state
  - Assess migration of restored state format
  - Verify no crashes on null restored state

### 2. Navigation State

Evaluate navigation restoration:

* **Navigation Arguments:**
  - Review navigation argument handling
  - Check for argument availability after process death
  - Assess deep link restoration
  - Verify back stack preservation

* **Navigation Compose:**
  - Check NavHost state restoration
  - Review rememberNavController behavior
  - Assess nested navigation restoration
  - Verify dialog state preservation

* **Custom Navigation:**
  - Review any custom navigation state
  - Check for navigation state persistence
  - Assess pending navigation handling
  - Verify no navigation loops on restore

### 3. Form and Input State

Analyze user input preservation:

* **Text Input:**
  - Review TextField state persistence
  - Check for unsaved changes preservation
  - Assess form validation state
  - Verify cursor position restoration

* **Selection State:**
  - Check checkbox, radio, toggle preservation
  - Review dropdown/spinner selection
  - Assess date/time picker state
  - Verify multi-select preservation

* **Complex Input:**
  - Review image/file picker state
  - Check for draft content preservation
  - Assess rich text editor state
  - Verify pending upload state

### 4. List and Scroll State

Evaluate scroll position:

* **LazyColumn/LazyRow:**
  - Review LazyListState rememberSaveable usage
  - Check for scroll position restoration
  - Assess firstVisibleItemIndex saving
  - Verify offset preservation

* **Paging State:**
  - Review Paging 3 restoration
  - Check for page position preservation
  - Assess loaded data caching
  - Verify no duplicate loading

### 5. Dialog and Sheet State

Analyze transient UI state:

* **Dialog State:**
  - Check dialog visibility preservation
  - Review dialog content/selection state
  - Assess confirmation dialog recovery
  - Verify no duplicate dialogs

* **Bottom Sheet State:**
  - Review sheet expansion state
  - Check for sheet content preservation
  - Assess modal sheet recovery
  - Verify proper dismiss handling

### 6. In-Flight Operations

Evaluate pending operation handling:

* **Network Requests:**
  - Check behavior of interrupted API calls
  - Review retry on restoration
  - Assess idempotency for retried operations
  - Verify no duplicate submissions

* **Background Work:**
  - Review WorkManager job survival
  - Check for operation resume logic
  - Assess progress restoration
  - Verify completion handling

### 7. Authentication State

Analyze auth persistence:

* **Login State:**
  - Check auth token survival across process death
  - Review session restoration
  - Assess re-authentication requirements
  - Verify biometric state handling

* **Sensitive Screens:**
  - Review security screen state after restoration
  - Check for re-authentication prompts
  - Assess session timeout handling
  - Verify no sensitive data exposure

### 8. Testing Strategy

Evaluate process death testing:

* **Test Coverage:**
  - Check for process death simulation in tests
  - Review savedInstanceState bundle testing
  - Assess StateRestorationTester usage (Compose)
  - Verify manual testing with developer options

---

## Expected Output

Provide a comprehensive process death recovery review report including:

### 1. Executive Summary
- Overall process death handling rating
- Critical state loss scenarios
- User experience impact assessment
- Test coverage status

### 2. State Preservation Matrix

| Screen/Component | User Input | Scroll | Selection | Dialog | Issues |
|------------------|------------|--------|-----------|--------|--------|
| [Screen] | [Saved/Lost] | [Saved/Lost] | [Saved/Lost] | [Saved/Lost] | [Count] |

### 3. Detailed Findings

For each issue:
- **Location:** Screen/ViewModel
- **Issue:** Description of state loss
- **User Impact:** Experience degradation
- **Severity:** Critical/High/Medium/Low
- **Current Code:** Missing preservation
- **Recommended Fix:** SavedStateHandle implementation

### 4. Test Recommendations

List of scenarios to test with "Don't keep activities" enabled.

### 5. Prioritized Remediation

Ordered by user impact.

---

## Example Output

```markdown
# Process Death State Recovery Review

## Executive Summary
- **Overall Handling:** Poor - Multiple critical state losses
- **Screens with Issues:** 8 of 12 screens lack proper restoration
- **User Impact:** Data loss in forms, lost scroll position, navigation confusion
- **Test Coverage:** No process death tests found

## Critical Findings

### CRITICAL-1: Form Data Lost in Todo Editor
**Severity:** Critical
**Impact:** User loses typed todo after switching apps

**Location:** TodoEditorViewModel.kt

**Scenario:**
1. User types long description in todo editor
2. User switches to another app (e.g., to copy text)
3. System kills app for memory
4. User returns to app
5. All typed content is gone

**Current Implementation:**
```kotlin
@HiltViewModel
class TodoEditorViewModel @Inject constructor(
    private val repository: ITodoRepository
) : ViewModel() {

    // PROBLEM: State not saved!
    private val _title = MutableStateFlow("")
    val title: StateFlow<String> = _title.asStateFlow()

    private val _description = MutableStateFlow("")
    val description: StateFlow<String> = _description.asStateFlow()

    private val _dueDate = MutableStateFlow<LocalDate?>(null)
    val dueDate: StateFlow<LocalDate?> = _dueDate.asStateFlow()

    fun updateTitle(value: String) { _title.value = value }
    fun updateDescription(value: String) { _description.value = value }
    fun updateDueDate(date: LocalDate?) { _dueDate.value = date }
}
```

**Recommended Fix:**
```kotlin
@HiltViewModel
class TodoEditorViewModel @Inject constructor(
    private val repository: ITodoRepository,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    // Navigation argument (always available after process death)
    private val todoId: String? = savedStateHandle["todoId"]

    // User input preserved via SavedStateHandle
    val title = savedStateHandle.getStateFlow("title", "")
    val description = savedStateHandle.getStateFlow("description", "")

    // For non-primitive types, handle serialization
    val dueDate: StateFlow<LocalDate?> = savedStateHandle
        .getStateFlow<Long?>("dueDate", null)
        .map { it?.let { LocalDate.ofEpochDay(it) } }
        .stateIn(viewModelScope, SharingStarted.Eagerly, null)

    fun updateTitle(value: String) {
        savedStateHandle["title"] = value
    }

    fun updateDescription(value: String) {
        savedStateHandle["description"] = value
    }

    fun updateDueDate(date: LocalDate?) {
        savedStateHandle["dueDate"] = date?.toEpochDay()
    }

    // Transient state NOT saved (re-computed on restore)
    private val _isLoading = MutableStateFlow(false)
    val isLoading: StateFlow<Boolean> = _isLoading.asStateFlow()

    private val _error = MutableStateFlow<String?>(null)
    val error: StateFlow<String?> = _error.asStateFlow()

    init {
        // If editing existing todo, load only if not restored
        todoId?.let { id ->
            if (savedStateHandle.get<String>("title") == null) {
                loadExistingTodo(id)
            }
        }
    }
}
```

---

### HIGH-1: LazyColumn Scroll Position Lost
**Severity:** High
**Impact:** User loses place in long list, frustrating scroll experience

**Location:** TodoListScreen.kt

**Current Implementation:**
```kotlin
@Composable
fun TodoListScreen(viewModel: TodoViewModel = hiltViewModel()) {
    val todos by viewModel.todos.collectAsStateWithLifecycle()

    // PROBLEM: LazyListState not saved!
    LazyColumn {
        items(todos, key = { it.id }) { todo ->
            TodoItem(todo = todo)
        }
    }
}
```

**Recommended Fix:**
```kotlin
@Composable
fun TodoListScreen(viewModel: TodoViewModel = hiltViewModel()) {
    val todos by viewModel.todos.collectAsStateWithLifecycle()

    // CORRECT: Use rememberSaveable for scroll state
    val listState = rememberSaveable(saver = LazyListState.Saver) {
        LazyListState()
    }

    LazyColumn(state = listState) {
        items(todos, key = { it.id }) { todo ->
            TodoItem(todo = todo)
        }
    }
}

// For complex scenarios, save in ViewModel
@HiltViewModel
class TodoViewModel @Inject constructor(
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    // Save scroll position
    fun saveScrollPosition(firstVisibleIndex: Int, offset: Int) {
        savedStateHandle["scrollIndex"] = firstVisibleIndex
        savedStateHandle["scrollOffset"] = offset
    }

    val savedScrollPosition: Pair<Int, Int>?
        get() {
            val index = savedStateHandle.get<Int>("scrollIndex")
            val offset = savedStateHandle.get<Int>("scrollOffset")
            return if (index != null && offset != null) Pair(index, offset) else null
        }
}
```

---

### HIGH-2: Navigation Arguments Lost
**Severity:** High
**Impact:** User sees wrong screen content after restore

**Location:** ConversationScreen.kt

**Current Implementation:**
```kotlin
// Navigation defined with argument
NavHost(navController, startDestination = "home") {
    composable(
        route = "conversation/{conversationId}",
        arguments = listOf(navArgument("conversationId") { type = NavType.StringType })
    ) { backStackEntry ->
        val conversationId = backStackEntry.arguments?.getString("conversationId")
        ConversationScreen(conversationId = conversationId)  // Can be null after process death!
    }
}

@Composable
fun ConversationScreen(conversationId: String?) {
    // CRASH or wrong behavior if conversationId is null!
    val viewModel: ConversationViewModel = hiltViewModel()
}
```

**Recommended Fix:**
```kotlin
// Navigation arguments are automatically restored by Navigation Compose
// BUT ViewModel should get them from SavedStateHandle, not composable parameter

@HiltViewModel
class ConversationViewModel @Inject constructor(
    private val repository: IMessageRepository,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    // Get argument from SavedStateHandle - survives process death
    private val conversationId: String = savedStateHandle.get<String>("conversationId")
        ?: throw IllegalArgumentException("conversationId is required")

    val messages = repository.observeMessages(conversationId)
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())
}

@Composable
fun ConversationScreen(
    viewModel: ConversationViewModel = hiltViewModel()  // No parameter needed!
) {
    val messages by viewModel.messages.collectAsStateWithLifecycle()
    // conversationId is safely in ViewModel via SavedStateHandle
}
```

---

### MEDIUM-1: Dialog State Not Preserved
**Severity:** Medium
**Impact:** User's dialog disappears, may lose context

**Location:** ShoppingListScreen.kt

**Current Implementation:**
```kotlin
@Composable
fun ShoppingListScreen() {
    // PROBLEM: Not saved!
    var showAddDialog by remember { mutableStateOf(false) }
    var itemName by remember { mutableStateOf("") }

    if (showAddDialog) {
        AddItemDialog(
            itemName = itemName,
            onItemNameChange = { itemName = it },
            onConfirm = { /* add item */ },
            onDismiss = { showAddDialog = false }
        )
    }
}
```

**Recommended Fix:**
```kotlin
@Composable
fun ShoppingListScreen(
    viewModel: ShoppingViewModel = hiltViewModel()
) {
    // Dialog visibility in ViewModel (survives process death)
    val showAddDialog by viewModel.showAddDialog.collectAsStateWithLifecycle()
    val pendingItemName by viewModel.pendingItemName.collectAsStateWithLifecycle()

    if (showAddDialog) {
        AddItemDialog(
            itemName = pendingItemName,
            onItemNameChange = { viewModel.updatePendingItemName(it) },
            onConfirm = { viewModel.confirmAddItem() },
            onDismiss = { viewModel.dismissAddDialog() }
        )
    }
}

@HiltViewModel
class ShoppingViewModel @Inject constructor(
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    val showAddDialog = savedStateHandle.getStateFlow("showAddDialog", false)
    val pendingItemName = savedStateHandle.getStateFlow("pendingItemName", "")

    fun showAddDialog() { savedStateHandle["showAddDialog"] = true }
    fun dismissAddDialog() {
        savedStateHandle["showAddDialog"] = false
        savedStateHandle["pendingItemName"] = ""
    }
    fun updatePendingItemName(name: String) { savedStateHandle["pendingItemName"] = name }
}
```

---

### MEDIUM-2: Pending Upload Lost
**Severity:** Medium
**Impact:** User's photo upload fails silently

**Location:** ProfileEditViewModel.kt

**Current Implementation:**
```kotlin
@HiltViewModel
class ProfileEditViewModel : ViewModel() {
    // PROBLEM: Selected photo URI lost on process death
    private val _pendingPhotoUri = MutableStateFlow<Uri?>(null)
    val pendingPhotoUri: StateFlow<Uri?> = _pendingPhotoUri.asStateFlow()

    fun selectPhoto(uri: Uri) {
        _pendingPhotoUri.value = uri
    }

    fun saveProfile() {
        val photoUri = _pendingPhotoUri.value
        // Upload photo...
    }
}
```

**Recommended Fix:**
```kotlin
@HiltViewModel
class ProfileEditViewModel @Inject constructor(
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    // URI can be saved as String
    val pendingPhotoUri: StateFlow<Uri?> = savedStateHandle
        .getStateFlow<String?>("pendingPhotoUri", null)
        .map { it?.let { Uri.parse(it) } }
        .stateIn(viewModelScope, SharingStarted.Eagerly, null)

    fun selectPhoto(uri: Uri) {
        savedStateHandle["pendingPhotoUri"] = uri.toString()
    }

    fun clearPendingPhoto() {
        savedStateHandle["pendingPhotoUri"] = null
    }
}
```

---

## State Preservation Matrix

| Screen | User Input | Scroll | Selection | Dialog | Status |
|--------|------------|--------|-----------|--------|--------|
| TodoEditor | ❌ Lost | N/A | ❌ Lost | N/A | Critical |
| TodoList | N/A | ❌ Lost | ✓ Saved | N/A | High |
| ShoppingList | ❌ Lost | ❌ Lost | ✓ Saved | ❌ Lost | High |
| Conversation | N/A | ❌ Lost | N/A | N/A | Medium |
| ProfileEdit | ❌ Lost | N/A | ❌ Lost | N/A | Medium |
| Calendar | N/A | ✓ Saved | ✓ Saved | N/A | OK |
| Settings | N/A | N/A | ✓ Saved | N/A | OK |

## Test Recommendations

Enable "Don't keep activities" in Developer Options and test:

1. **Todo Editor Flow:**
   - Open new todo editor
   - Type title and description
   - Press home, wait 30 seconds
   - Return to app
   - Verify content is preserved

2. **Long List Scroll:**
   - Scroll to item #50 in todo list
   - Background app
   - Kill app via recent apps
   - Reopen app
   - Verify scroll position restored

3. **Dialog Mid-Action:**
   - Open add shopping item dialog
   - Type item name
   - Background app, kill process
   - Return - dialog should reappear with content

4. **Navigation Deep Link:**
   - Navigate to conversation
   - Background and kill
   - Return - should be in same conversation

## Remediation Priority

### Critical (Immediate)
1. Add SavedStateHandle to TodoEditorViewModel

### High Priority (This Sprint)
1. Fix scroll position preservation in all lists
2. Fix navigation argument handling

### Medium Priority (Next Sprint)
1. Preserve dialog states
2. Save pending file selections
3. Add process death tests

### Low Priority (Backlog)
1. Document state preservation patterns
2. Create SavedStateHandle utilities
3. Add state restoration analytics
```

---

## Techniques Used

- **ST-01** (Clear Objective Statement) - Process death focus
- **ST-02** (Structured Sequential Instructions) - Systematic analysis
- **RT-02** (Multi-Dimensional Analysis) - State, navigation, input
- **RT-05** (Evidence-Based Reasoning) - Code examples
- **ST-03** (Output Format Templates) - State matrix
- **DS-06** (Prioritization Guidance) - User impact priority

---

## Related Prompts

- `android_viewmodel_state_management_review.md` - For ViewModel patterns
- `android_compose_recomposition_review.md` - For Compose state
- `android_kotlin_best_practices.md` - General patterns
- `testing_unit_test_generation.md` - For process death tests
- `mobile_app_security_review.md` - For security state handling

---

## Customization Guide

- **For Form-Heavy Apps:** Focus on input preservation, draft saving
- **For Media Apps:** Add playback position, queue state preservation
- **For E-commerce:** Add cart state, checkout flow preservation
- **For Auth Flows:** Add 2FA state, OAuth flow preservation
- **For Multi-Step Flows:** Add wizard step preservation
