---
title: "Android State Management"
category: mobile-development
description: ""
tags:
  - android
  - mobile-development
updated: "2026-03-19"
---

# Android State Management

**Objective:** Implement robust, predictable UI state management using ViewModel, StateFlow, and modern Android patterns that ensure proper lifecycle handling, testability, and maintainable code.

**When to Use:** Use this prompt when implementing state management for screens or features in an Android app. Ideal for new feature development, migrating from LiveData to StateFlow, or adopting MVI patterns. Best used after architecture decisions and screen designs are finalized.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before implementing state management, gather essential context:

1. **Architecture Pattern:**
   - "What architecture pattern is the app using (MVVM, MVI, or hybrid)?"
   - "Is there an existing state management pattern to follow?"
   - "How are side effects (navigation, toasts) currently handled?"

2. **Screen Requirements:**
   - "What states does this screen need to represent (loading, content, error, empty)?"
   - "What user interactions need to be handled?"
   - "Are there background updates that affect this screen?"

3. **Data Sources:**
   - "Where does the screen data come from (repository, use cases, direct API)?"
   - "Should data be cached or refreshed each time?"
   - "Are there real-time updates (WebSocket, Firebase)?"

4. **Technical Preferences:**
   - "StateFlow vs SharedFlow for events?"
   - "Single UI state object vs multiple state flows?"
   - "Preference for sealed classes vs data classes for states?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before implementing ANY code, you MUST:**

1. **Understand existing state patterns** - Check for existing StateFlow, LiveData, or state management patterns in the codebase.
2. **Verify state requirements** - Confirm what state needs preservation across configuration changes and process death.
3. **Follow project conventions** - Match existing ViewModel patterns, state class organization, and side effect handling.
4. **Provide specific, working code** - All code samples MUST include file paths (e.g., `ui/home/HomeViewModel.kt`) and be copy-paste ready.
5. **Include proper lifecycle handling** - Use lifecycle-aware collection for all state flows.

**Adapting to existing state patterns is preferred over introducing new approaches.** Don't mix LiveData and StateFlow without clear migration strategy.

### Quality Requirements

- ❌ Do NOT mix state management approaches without clear reasoning
- ❌ Do NOT generate ViewModels without proper SavedStateHandle integration where needed
- ❌ Do NOT expose MutableStateFlow publicly
- ❌ Do NOT collect flows without lifecycle awareness
- ✅ DO follow existing state modeling patterns
- ✅ DO provide proper loading, error, and success states
- ✅ DO include proper side effect handling (one-time events)
- ✅ DO specify exact file paths for all code changes

---

### Phase 1: UI State Design

#### 1.1 State Modeling Principles

Design UI state following these principles:

**Single Source of Truth:**
```kotlin
// Good: All screen state in one place
data class ProfileUiState(
    val isLoading: Boolean = false,
    val user: User? = null,
    val posts: List<Post> = emptyList(),
    val error: ErrorState? = null
)

// Avoid: Scattered state that can become inconsistent
// var isLoading by mutableStateOf(false)
// var user by mutableStateOf<User?>(null)
// var error by mutableStateOf<String?>(null)
```

**Immutability:**
```kotlin
// Good: Immutable state with copy
val newState = currentState.copy(isLoading = false, user = loadedUser)

// Avoid: Mutable state
// currentState.isLoading = false
// currentState.user = loadedUser
```

**Exhaustive States:**
```kotlin
// Good: Clear, mutually exclusive states
sealed interface ProfileScreenState {
    data object Loading : ProfileScreenState
    data class Content(val user: User, val posts: List<Post>) : ProfileScreenState
    data class Error(val message: String, val canRetry: Boolean) : ProfileScreenState
}

// Good: Or use a single state class with clear combinations
data class ProfileUiState(
    val isLoading: Boolean = false,
    val user: User? = null,
    val error: ErrorState? = null
) {
    val showContent: Boolean get() = user != null && !isLoading
    val showEmptyState: Boolean get() = user != null && posts.isEmpty() && !isLoading
}
```

#### 1.2 Comprehensive State Class Design

Design a complete UI state class:

```kotlin
data class FeatureUiState(
    // Loading states
    val isLoading: Boolean = false,
    val isRefreshing: Boolean = false,
    val isLoadingMore: Boolean = false,

    // Data
    val items: List<ItemUiModel> = emptyList(),
    val selectedItem: ItemUiModel? = null,

    // Pagination
    val hasMoreItems: Boolean = true,
    val currentPage: Int = 1,

    // UI state
    val searchQuery: String = "",
    val filterOptions: FilterOptions = FilterOptions(),
    val sortOrder: SortOrder = SortOrder.NEWEST,

    // Error state
    val error: ErrorState? = null
) {
    // Derived properties
    val showContent: Boolean
        get() = items.isNotEmpty() && !isLoading

    val showEmptyState: Boolean
        get() = items.isEmpty() && !isLoading && error == null

    val showErrorState: Boolean
        get() = error != null && items.isEmpty()

    val filteredItems: List<ItemUiModel>
        get() = items
            .filter { filterOptions.matches(it) }
            .let { list ->
                when (sortOrder) {
                    SortOrder.NEWEST -> list.sortedByDescending { it.createdAt }
                    SortOrder.OLDEST -> list.sortedBy { it.createdAt }
                    SortOrder.NAME -> list.sortedBy { it.name }
                }
            }
}

data class ErrorState(
    val message: String,
    val type: ErrorType,
    val canRetry: Boolean = true
)

enum class ErrorType {
    NETWORK,
    SERVER,
    VALIDATION,
    UNKNOWN
}
```

#### 1.3 Event/Intent Design

Define user actions as sealed classes:

```kotlin
sealed interface FeatureEvent {
    // Data loading
    data object LoadInitial : FeatureEvent
    data object Refresh : FeatureEvent
    data object LoadMore : FeatureEvent
    data object Retry : FeatureEvent

    // User interactions
    data class OnItemClick(val itemId: String) : FeatureEvent
    data class OnItemLongClick(val itemId: String) : FeatureEvent
    data class OnSearchQueryChange(val query: String) : FeatureEvent
    data class OnFilterChange(val filter: FilterOptions) : FeatureEvent
    data class OnSortChange(val sortOrder: SortOrder) : FeatureEvent

    // Item actions
    data class OnDeleteItem(val itemId: String) : FeatureEvent
    data class OnToggleFavorite(val itemId: String) : FeatureEvent

    // Dialog/Sheet actions
    data object OnDismissError : FeatureEvent
    data object OnConfirmDelete : FeatureEvent
    data object OnCancelDelete : FeatureEvent
}
```

---

### Phase 2: ViewModel Implementation

**CHECKPOINT 1:** Present state design for review.

```markdown
## State Design Summary

### UI State Structure
```kotlin
data class [Feature]UiState(
    // [List state fields]
)
```

### Events/Intents
| Event | Description | State Changes |
|-------|-------------|---------------|
| LoadInitial | First load | isLoading → true/false, items |
| OnItemClick | User taps item | Navigation effect |

### Derived Properties
| Property | Logic |
|----------|-------|
| showContent | items.isNotEmpty() && !isLoading |

**Does this state design cover all screen requirements?**
```

#### 2.1 Basic ViewModel Structure

Implement ViewModel with StateFlow:

```kotlin
@HiltViewModel
class FeatureViewModel @Inject constructor(
    private val getItemsUseCase: GetItemsUseCase,
    private val deleteItemUseCase: DeleteItemUseCase,
    private val savedStateHandle: SavedStateHandle
) : ViewModel() {

    // UI State
    private val _uiState = MutableStateFlow(FeatureUiState())
    val uiState: StateFlow<FeatureUiState> = _uiState.asStateFlow()

    // One-time events (navigation, snackbars)
    private val _events = Channel<FeatureUiEvent>(Channel.BUFFERED)
    val events: Flow<FeatureUiEvent> = _events.receiveAsFlow()

    // Restore state from process death
    private val savedQuery = savedStateHandle.getStateFlow("search_query", "")

    init {
        // Restore saved state
        viewModelScope.launch {
            savedQuery.collect { query ->
                _uiState.update { it.copy(searchQuery = query) }
            }
        }

        // Initial load
        onEvent(FeatureEvent.LoadInitial)
    }

    fun onEvent(event: FeatureEvent) {
        when (event) {
            is FeatureEvent.LoadInitial -> loadInitial()
            is FeatureEvent.Refresh -> refresh()
            is FeatureEvent.LoadMore -> loadMore()
            is FeatureEvent.Retry -> retry()
            is FeatureEvent.OnItemClick -> onItemClick(event.itemId)
            is FeatureEvent.OnSearchQueryChange -> onSearchQueryChange(event.query)
            is FeatureEvent.OnDeleteItem -> onDeleteItem(event.itemId)
            is FeatureEvent.OnDismissError -> dismissError()
            // ... handle other events
        }
    }

    private fun loadInitial() {
        if (_uiState.value.isLoading) return

        viewModelScope.launch {
            _uiState.update { it.copy(isLoading = true, error = null) }

            getItemsUseCase(page = 1)
                .onSuccess { result ->
                    _uiState.update {
                        it.copy(
                            isLoading = false,
                            items = result.items.map(Item::toUiModel),
                            hasMoreItems = result.hasMore,
                            currentPage = 1
                        )
                    }
                }
                .onFailure { error ->
                    _uiState.update {
                        it.copy(
                            isLoading = false,
                            error = error.toErrorState()
                        )
                    }
                }
        }
    }

    private fun refresh() {
        viewModelScope.launch {
            _uiState.update { it.copy(isRefreshing = true) }

            getItemsUseCase(page = 1)
                .onSuccess { result ->
                    _uiState.update {
                        it.copy(
                            isRefreshing = false,
                            items = result.items.map(Item::toUiModel),
                            hasMoreItems = result.hasMore,
                            currentPage = 1,
                            error = null
                        )
                    }
                }
                .onFailure { error ->
                    _uiState.update { it.copy(isRefreshing = false) }
                    _events.send(FeatureUiEvent.ShowSnackbar(error.message ?: "Refresh failed"))
                }
        }
    }

    private fun loadMore() {
        val currentState = _uiState.value
        if (currentState.isLoadingMore || !currentState.hasMoreItems) return

        viewModelScope.launch {
            _uiState.update { it.copy(isLoadingMore = true) }

            val nextPage = currentState.currentPage + 1
            getItemsUseCase(page = nextPage)
                .onSuccess { result ->
                    _uiState.update {
                        it.copy(
                            isLoadingMore = false,
                            items = it.items + result.items.map(Item::toUiModel),
                            hasMoreItems = result.hasMore,
                            currentPage = nextPage
                        )
                    }
                }
                .onFailure { error ->
                    _uiState.update { it.copy(isLoadingMore = false) }
                    _events.send(FeatureUiEvent.ShowSnackbar("Failed to load more"))
                }
        }
    }

    private fun onSearchQueryChange(query: String) {
        savedStateHandle["search_query"] = query
        _uiState.update { it.copy(searchQuery = query) }
    }

    private fun onItemClick(itemId: String) {
        viewModelScope.launch {
            _events.send(FeatureUiEvent.NavigateToDetail(itemId))
        }
    }

    private fun dismissError() {
        _uiState.update { it.copy(error = null) }
    }
}
```

#### 2.2 UI Events (Side Effects)

Define one-time UI events:

```kotlin
sealed interface FeatureUiEvent {
    data class NavigateToDetail(val itemId: String) : FeatureUiEvent
    data class ShowSnackbar(val message: String) : FeatureUiEvent
    data class ShowDialog(val dialogType: DialogType) : FeatureUiEvent
    data object NavigateBack : FeatureUiEvent
    data class ShareItem(val item: ItemUiModel) : FeatureUiEvent
}
```

#### 2.3 State Update Helpers

Create extension functions for clean state updates:

```kotlin
// Extension for updating state with loading
private inline fun MutableStateFlow<FeatureUiState>.withLoading(
    block: FeatureUiState.() -> FeatureUiState
) {
    update { it.copy(isLoading = true, error = null) }
    update { it.block().copy(isLoading = false) }
}

// Extension for error handling
private fun Throwable.toErrorState(): ErrorState = ErrorState(
    message = message ?: "Unknown error occurred",
    type = when (this) {
        is NetworkException.NoInternetConnection -> ErrorType.NETWORK
        is NetworkException.ServerError -> ErrorType.SERVER
        else -> ErrorType.UNKNOWN
    },
    canRetry = this !is NetworkException.Forbidden
)

// Domain to UI model mapping
private fun Item.toUiModel(): ItemUiModel = ItemUiModel(
    id = id,
    name = name,
    description = description.take(100),
    imageUrl = imageUrl,
    createdAt = createdAt,
    formattedDate = createdAt.formatRelative()
)
```

---

### Phase 3: Compose Integration

#### 3.1 State Collection in Compose

Properly collect state in Compose:

```kotlin
@Composable
fun FeatureScreen(
    viewModel: FeatureViewModel = hiltViewModel(),
    onNavigateToDetail: (String) -> Unit,
    onNavigateBack: () -> Unit
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    // Handle one-time events
    LaunchedEffect(Unit) {
        viewModel.events.collect { event ->
            when (event) {
                is FeatureUiEvent.NavigateToDetail -> onNavigateToDetail(event.itemId)
                is FeatureUiEvent.NavigateBack -> onNavigateBack()
                is FeatureUiEvent.ShowSnackbar -> {
                    // Show snackbar via SnackbarHostState
                }
                is FeatureUiEvent.ShowDialog -> {
                    // Handle dialog
                }
                is FeatureUiEvent.ShareItem -> {
                    // Handle share intent
                }
            }
        }
    }

    FeatureScreenContent(
        uiState = uiState,
        onEvent = viewModel::onEvent
    )
}

@Composable
private fun FeatureScreenContent(
    uiState: FeatureUiState,
    onEvent: (FeatureEvent) -> Unit
) {
    Scaffold(
        topBar = {
            FeatureTopBar(
                searchQuery = uiState.searchQuery,
                onSearchQueryChange = { onEvent(FeatureEvent.OnSearchQueryChange(it)) }
            )
        }
    ) { padding ->
        Box(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
        ) {
            when {
                uiState.isLoading && uiState.items.isEmpty() -> {
                    LoadingState()
                }
                uiState.showErrorState -> {
                    ErrorState(
                        error = uiState.error!!,
                        onRetry = { onEvent(FeatureEvent.Retry) },
                        onDismiss = { onEvent(FeatureEvent.OnDismissError) }
                    )
                }
                uiState.showEmptyState -> {
                    EmptyState(
                        message = "No items found",
                        onRefresh = { onEvent(FeatureEvent.Refresh) }
                    )
                }
                else -> {
                    ItemsList(
                        items = uiState.filteredItems,
                        isRefreshing = uiState.isRefreshing,
                        isLoadingMore = uiState.isLoadingMore,
                        onRefresh = { onEvent(FeatureEvent.Refresh) },
                        onLoadMore = { onEvent(FeatureEvent.LoadMore) },
                        onItemClick = { onEvent(FeatureEvent.OnItemClick(it.id)) }
                    )
                }
            }
        }
    }
}
```

#### 3.2 Pull-to-Refresh Pattern

```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun ItemsList(
    items: List<ItemUiModel>,
    isRefreshing: Boolean,
    isLoadingMore: Boolean,
    onRefresh: () -> Unit,
    onLoadMore: () -> Unit,
    onItemClick: (ItemUiModel) -> Unit
) {
    val pullToRefreshState = rememberPullToRefreshState()

    PullToRefreshBox(
        isRefreshing = isRefreshing,
        onRefresh = onRefresh,
        state = pullToRefreshState
    ) {
        LazyColumn(
            modifier = Modifier.fillMaxSize(),
            contentPadding = PaddingValues(16.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            items(
                items = items,
                key = { it.id }
            ) { item ->
                ItemCard(
                    item = item,
                    onClick = { onItemClick(item) }
                )
            }

            // Load more trigger
            item {
                LaunchedEffect(Unit) {
                    onLoadMore()
                }

                if (isLoadingMore) {
                    Box(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp),
                        contentAlignment = Alignment.Center
                    ) {
                        CircularProgressIndicator()
                    }
                }
            }
        }
    }
}
```

---

### Phase 4: Advanced Patterns

**CHECKPOINT 2:** Review basic implementation before advanced patterns.

```markdown
## Implementation Summary

### Components Created
| Component | Responsibility |
|-----------|---------------|
| FeatureUiState | Holds all screen state |
| FeatureEvent | Represents user actions |
| FeatureUiEvent | One-time effects |
| FeatureViewModel | State management |
| FeatureScreen | Compose UI |

### State Flow
```
User Action → Event → ViewModel → State Update → UI Recomposition
                ↓
           Side Effect → UI Event → Navigation/Snackbar
```

**Ready for advanced patterns (form handling, debouncing)?**
```

#### 4.1 Form State Management

Handle complex form state:

```kotlin
data class FormUiState(
    val email: String = "",
    val password: String = "",
    val confirmPassword: String = "",

    val emailError: String? = null,
    val passwordError: String? = null,
    val confirmPasswordError: String? = null,

    val isSubmitting: Boolean = false,
    val submitError: String? = null
) {
    val isValid: Boolean
        get() = email.isNotBlank() &&
                password.isNotBlank() &&
                password == confirmPassword &&
                emailError == null &&
                passwordError == null &&
                confirmPasswordError == null

    val canSubmit: Boolean
        get() = isValid && !isSubmitting
}

// In ViewModel
private fun onEmailChange(email: String) {
    _uiState.update {
        it.copy(
            email = email,
            emailError = validateEmail(email)
        )
    }
}

private fun validateEmail(email: String): String? = when {
    email.isBlank() -> "Email is required"
    !email.contains("@") -> "Invalid email format"
    else -> null
}

private fun onSubmit() {
    val state = _uiState.value
    if (!state.canSubmit) return

    viewModelScope.launch {
        _uiState.update { it.copy(isSubmitting = true, submitError = null) }

        submitFormUseCase(state.email, state.password)
            .onSuccess {
                _events.send(FormUiEvent.SubmitSuccess)
            }
            .onFailure { error ->
                _uiState.update {
                    it.copy(
                        isSubmitting = false,
                        submitError = error.message
                    )
                }
            }
    }
}
```

#### 4.2 Debounced Search

Implement search with debouncing:

```kotlin
@HiltViewModel
class SearchViewModel @Inject constructor(
    private val searchUseCase: SearchUseCase
) : ViewModel() {

    private val _searchQuery = MutableStateFlow("")
    val searchQuery: StateFlow<String> = _searchQuery.asStateFlow()

    private val _searchResults = MutableStateFlow<List<SearchResult>>(emptyList())
    val searchResults: StateFlow<List<SearchResult>> = _searchResults.asStateFlow()

    private val _isSearching = MutableStateFlow(false)
    val isSearching: StateFlow<Boolean> = _isSearching.asStateFlow()

    init {
        viewModelScope.launch {
            _searchQuery
                .debounce(300) // Wait 300ms after last keystroke
                .distinctUntilChanged()
                .filter { it.length >= 2 } // Minimum query length
                .collectLatest { query ->
                    performSearch(query)
                }
        }
    }

    fun onSearchQueryChange(query: String) {
        _searchQuery.value = query

        // Clear results immediately if query too short
        if (query.length < 2) {
            _searchResults.value = emptyList()
        }
    }

    private suspend fun performSearch(query: String) {
        _isSearching.value = true

        searchUseCase(query)
            .onSuccess { results ->
                _searchResults.value = results
            }
            .onFailure {
                // Handle error
            }

        _isSearching.value = false
    }
}
```

#### 4.3 Real-time Updates

Handle real-time data streams:

```kotlin
@HiltViewModel
class MessagesViewModel @Inject constructor(
    private val messagesRepository: MessagesRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow(MessagesUiState())
    val uiState: StateFlow<MessagesUiState> = _uiState.asStateFlow()

    init {
        // Observe real-time messages
        viewModelScope.launch {
            messagesRepository.observeMessages()
                .catch { error ->
                    _uiState.update {
                        it.copy(error = error.toErrorState())
                    }
                }
                .collect { messages ->
                    _uiState.update {
                        it.copy(
                            messages = messages.map(Message::toUiModel),
                            error = null
                        )
                    }
                }
        }

        // Observe connection status
        viewModelScope.launch {
            messagesRepository.connectionStatus
                .collect { status ->
                    _uiState.update { it.copy(connectionStatus = status) }
                }
        }
    }
}
```

---

## Expected Output

### File Structure Created

```
feature/
├── presentation/
│   ├── FeatureScreen.kt
│   ├── FeatureViewModel.kt
│   ├── FeatureUiState.kt
│   ├── FeatureEvent.kt
│   ├── FeatureUiEvent.kt
│   └── components/
│       ├── ItemCard.kt
│       ├── LoadingState.kt
│       ├── ErrorState.kt
│       └── EmptyState.kt
└── model/
    └── ItemUiModel.kt
```

### Implementation Checklist

- [ ] UI state data class with all screen states
- [ ] Event sealed interface for user actions
- [ ] UI event sealed interface for side effects
- [ ] ViewModel with StateFlow and event handling
- [ ] Compose screen with state collection
- [ ] One-time event handling (LaunchedEffect)
- [ ] Loading, error, empty, content states
- [ ] Pull-to-refresh (if applicable)
- [ ] Pagination (if applicable)
- [ ] SavedStateHandle for process death

---

## Example Interaction

**User:** I need state management for a shopping cart screen. Users can add/remove items, apply promo codes, and checkout.

**Agent:** I'll help design state management for your cart screen. Let me confirm the requirements:

1. What information do you show per cart item (quantity, price, options)?
2. Can users modify quantity directly in the cart?
3. What happens on successful checkout - navigate to order confirmation?

**User:** Show name, image, price, quantity. Yes, users can adjust quantity with +/- buttons. After checkout, navigate to order confirmation with order ID.

**Agent:**

## Cart UI State Design

```kotlin
data class CartUiState(
    // Cart data
    val items: List<CartItemUiModel> = emptyList(),
    val promoCode: String = "",
    val appliedPromo: AppliedPromo? = null,

    // Calculations
    val subtotal: Money = Money.ZERO,
    val discount: Money = Money.ZERO,
    val tax: Money = Money.ZERO,
    val total: Money = Money.ZERO,

    // Loading states
    val isLoading: Boolean = false,
    val isApplyingPromo: Boolean = false,
    val isCheckingOut: Boolean = false,

    // Errors
    val promoError: String? = null,
    val checkoutError: String? = null
) {
    val isEmpty: Boolean get() = items.isEmpty()
    val itemCount: Int get() = items.sumOf { it.quantity }
    val canCheckout: Boolean get() = items.isNotEmpty() && !isCheckingOut
}

data class CartItemUiModel(
    val id: String,
    val productId: String,
    val name: String,
    val imageUrl: String,
    val price: Money,
    val quantity: Int,
    val maxQuantity: Int = 99
) {
    val lineTotal: Money get() = price * quantity
    val canIncrease: Boolean get() = quantity < maxQuantity
    val canDecrease: Boolean get() = quantity > 1
}
```

**Does this state structure work for your cart?**

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective for state management
- **ST-02** (Sequential Instructions): Phased approach from design to integration
- **RT-02** (Multi-Dimensional Analysis): Covers state, events, ViewModel, UI
- **RT-04** (Best Practice Review): Modern Android state management patterns
- **ST-03** (Output Format Templates): Code templates for each component
- **NE-02** (Phased Workflow): Clear phases with checkpoints
- **NE-07** (Discussion Before Action): Review points for state design

---

## Related Prompts

- [android_architecture_selection.md](../planning/android_architecture_selection.md) - Choose MVVM vs MVI
- [android_compose_screen_builder.md](android_compose_screen_builder.md) - Build Compose UI for state
- [android_navigation_implementation.md](android_navigation_implementation.md) - Handle navigation events
- [android_unit_test_generation.md](../testing/android_unit_test_generation.md) - Test ViewModels
- [android_compose_ui_testing.md](../testing/android_compose_ui_testing.md) - Test Compose with state

---

## Customization Guide

### For MVI Architecture

Adopt stricter MVI patterns:
- Rename Event to Intent
- Make state changes purely through reduce function
- Side effects through explicit Effect channel

### For Simple Screens

Simplify for basic screens:
- Skip event sealed class, use direct method calls
- Use simpler state class
- May not need UI events channel

### For Form-Heavy Screens

Enhance for complex forms:
- Separate form state from screen state
- Add field-level validation
- Track dirty/pristine state per field

### For Real-time Features

Adapt for WebSocket/Firebase:
- Add connection status to state
- Handle reconnection logic
- Merge local and remote state updates
