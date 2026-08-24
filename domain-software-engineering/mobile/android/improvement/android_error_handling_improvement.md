---
title: "Android Error Handling Improvement"
category: mobile-development
description: "Analyzes and improves error handling patterns for consistent, user-friendly, and debuggable error management"
techniques:
  - ST-01
  - RT-04
  - ST-03
difficulty: intermediate
tags:
  - android
  - mobile-development
  - error-handling
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_codebase_health_assessment.md
  - domain-software-engineering/mobile/android/improvement/android_code_modernization.md
---

# Android Error Handling Improvement

**Objective:** Analyze and improve error handling patterns throughout an Android codebase, implementing consistent, user-friendly, and debuggable error handling strategies.

**When to Use:** Use this prompt when crash rates are high, error messages confuse users, debugging production issues is difficult, or error handling is inconsistent across the codebase.

**Prompt Type:** Modular (150-180 lines)

---

## Context Gathering

1. **Current Issues:**
   - "What types of errors are most common (network, database, validation)?"
   - "Are users seeing technical error messages?"

2. **Monitoring:**
   - "Is crash reporting (Crashlytics, Sentry) integrated?"
   - "Are non-fatal errors being tracked?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual error flows** - Don't flag based on pattern matching alone. Verify that the suspected error handling issue actually causes problems.
2. **Check for existing handling** - Search for try-catch blocks, Result types, or error boundaries that may already handle the concern.
3. **Understand the context** - Consider WHY specific error handling patterns were chosen. Some errors should crash; others need silent recovery.
4. **Confirm actual impact** - Does this actually cause poor user experience or debugging difficulty?
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `UserRepository.kt:89`).

**Finding ADEQUATE error handling is an acceptable outcome.** If errors are handled appropriately for the use case, say so with confidence. Don't manufacture error handling concerns.

### False-Positive Prevention

- ❌ Do NOT flag all empty catch blocks as wrong (some exceptions should be swallowed)
- ❌ Do NOT flag based solely on exception type without understanding context
- ❌ Do NOT assume missing handling without tracing the full error flow
- ❌ Do NOT report stylistic preferences as error handling defects
- ✅ DO verify that reported issues actually cause problems in production
- ✅ DO understand the difference between recoverable and fatal errors
- ✅ DO check for existing crash reporting integration
- ✅ DO consider user-facing vs. internal error handling differently

---

### Phase 1: Error Handling Analysis

#### 1.1 Current Pattern Detection

**Search for error handling patterns:**

```kotlin
// Anti-patterns to find:
try {
    // code
} catch (e: Exception) {
    // Empty catch - swallows errors silently
}

try {
    // code
} catch (e: Exception) {
    e.printStackTrace() // Only logs, no handling
}

try {
    // code
} catch (e: Exception) {
    throw RuntimeException(e) // Loses context, crashes app
}
```

#### 1.2 Error Pattern Inventory

| Pattern | Occurrences | Severity | Location |
|---------|-------------|----------|----------|
| Empty catch blocks | [X] | High | [files] |
| printStackTrace only | [X] | Medium | [files] |
| Generic Exception catch | [X] | Medium | [files] |
| Unhandled coroutine exceptions | [X] | High | [files] |

---

### Phase 2: Recommended Patterns

#### 2.1 Result Type Pattern

```kotlin
// Define a Result wrapper
sealed class Result<out T> {
    data class Success<T>(val data: T) : Result<T>()
    data class Error(val exception: Throwable, val message: String? = null) : Result<Nothing>()
}

// Use in repository
class UserRepository {
    suspend fun getUser(id: String): Result<User> {
        return try {
            val user = api.getUser(id)
            Result.Success(user)
        } catch (e: IOException) {
            Result.Error(e, "Network error. Please check your connection.")
        } catch (e: HttpException) {
            Result.Error(e, "Server error. Please try again later.")
        }
    }
}

// Handle in ViewModel
class UserViewModel : ViewModel() {
    fun loadUser(id: String) {
        viewModelScope.launch {
            when (val result = repository.getUser(id)) {
                is Result.Success -> _uiState.update { it.copy(user = result.data) }
                is Result.Error -> _uiState.update { it.copy(error = result.message) }
            }
        }
    }
}
```

#### 2.2 Coroutine Error Handling

```kotlin
// ViewModel with proper error handling
class MyViewModel : ViewModel() {

    private val exceptionHandler = CoroutineExceptionHandler { _, exception ->
        _uiState.update { it.copy(error = exception.toUserMessage()) }
        logError(exception) // Non-fatal logging
    }

    fun loadData() {
        viewModelScope.launch(exceptionHandler) {
            _uiState.update { it.copy(isLoading = true) }
            val data = repository.getData()
            _uiState.update { it.copy(data = data, isLoading = false) }
        }
    }
}

// Extension for user-friendly messages
fun Throwable.toUserMessage(): String = when (this) {
    is UnknownHostException -> "No internet connection"
    is SocketTimeoutException -> "Request timed out"
    is HttpException -> when (code()) {
        401 -> "Please log in again"
        403 -> "You don't have permission"
        404 -> "Resource not found"
        in 500..599 -> "Server error. Try again later."
        else -> "Something went wrong"
    }
    else -> "An unexpected error occurred"
}
```

#### 2.3 Global Error Handling

```kotlin
// Application-level crash handler
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        Thread.setDefaultUncaughtExceptionHandler { thread, throwable ->
            // Log to crash reporting
            Firebase.crashlytics.recordException(throwable)

            // Optionally show error screen instead of crash
            // startActivity(ErrorActivity.createIntent(this))
        }
    }
}

// Global coroutine exception handler
val globalExceptionHandler = CoroutineExceptionHandler { _, exception ->
    Firebase.crashlytics.recordException(exception)
}
```

#### 2.4 User-Friendly Error Display

```kotlin
// Error UI state
data class ErrorState(
    val message: String,
    val action: ErrorAction? = null,
    val isRetryable: Boolean = true
)

sealed class ErrorAction {
    object Retry : ErrorAction()
    object GoToSettings : ErrorAction()
    data class Navigate(val destination: String) : ErrorAction()
}

// In Compose
@Composable
fun ErrorDisplay(
    error: ErrorState,
    onRetry: () -> Unit,
    modifier: Modifier = Modifier
) {
    Column(
        modifier = modifier.padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text(error.message, style = MaterialTheme.typography.bodyLarge)
        if (error.isRetryable) {
            Button(onClick = onRetry) {
                Text("Try Again")
            }
        }
    }
}
```

---

### Phase 3: Error Handling Report

```markdown
## Error Handling Improvement Report

### Current State Assessment

| Metric | Value | Assessment |
|--------|-------|------------|
| Empty catch blocks | [X] | [Critical if > 0] |
| Proper Result handling | [%] | [Target: 100%] |
| User-friendly messages | [%] | [Target: 100%] |
| Crash reporting coverage | [%] | [Target: 100%] |

### Improvements Made

| Change | Location | Impact |
|--------|----------|--------|
| [Change] | [file:line] | [Impact] |

### Recommendations

1. **Immediate:** Remove all empty catch blocks
2. **Short-term:** Implement Result pattern in repositories
3. **Medium-term:** Add global error handling
4. **Ongoing:** Ensure all errors have user-friendly messages
```

---

## Expected Output

1. **Error Pattern Inventory** - Current error handling patterns
2. **Anti-pattern Identification** - Problems to fix
3. **Implementation Guide** - Recommended patterns with code
4. **Improvement Report** - Changes made and impact

---

## Techniques Used

- **ST-01** (Clear Objective): Error handling focus
- **RT-04** (Best Practice Review): Error handling patterns
- **ST-03** (Output Format Templates): Structured report

---

## Related Prompts

- [android_codebase_health_assessment.md](../analysis/android_codebase_health_assessment.md) - Overall health
- [android_code_modernization.md](android_code_modernization.md) - Modernization including error handling
