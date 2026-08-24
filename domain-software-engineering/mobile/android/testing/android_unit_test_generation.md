---
title: "Android Unit Test Generation"
category: mobile-development
description: "Generates comprehensive unit tests for Android components including ViewModels, repositories, use cases, and utility functions"
tags:
  - android
  - mobile-development
  - testing
updated: "2026-03-19"
---

# Android Unit Test Generation

**Objective:** Generate comprehensive, idiomatic unit tests for existing Android code, covering ViewModels, Use Cases, Repositories, and utility classes following modern Kotlin testing best practices.

**When to Use:** Use this prompt when you need to add test coverage to existing untested code, when preparing for a refactoring effort that requires safety nets, when onboarding to a codebase and using tests to understand behavior, or when expanding test coverage to meet quality gates.

**Prompt Type:** Modular (120-150 lines)

---

## Context Gathering

1. **Target Identification:**
   - "Which class(es) need unit tests? (Provide file path or paste code)"
   - "Is this a ViewModel, UseCase, Repository, or utility class?"

2. **Testing Environment:**
   - "What testing frameworks are available? (JUnit4, JUnit5, MockK, Mockito)"
   - "Is there a MainDispatcherRule or similar test utility already set up?"

3. **Scope:**
   - "Should I generate tests for all public methods or focus on specific areas?"
   - "Are there existing tests I should follow as a style guide?"

---

## Instructions

### CRITICAL: Implementation Requirements

**Before generating ANY test, you MUST:**

1. **Understand the code under test** - Read and understand the actual implementation before writing tests.
2. **Check for existing tests** - Search for existing test patterns, utilities, or conventions in the project.
3. **Follow project conventions** - Match existing test naming, structure, and assertion patterns.
4. **Provide specific, working tests** - All tests MUST include file paths (e.g., `UserViewModelTest.kt`) and be immediately runnable.
5. **Include meaningful assertions** - Tests should verify actual behavior, not just exercise code.

**Adapting to existing test patterns is required.** Match the project's testing style and frameworks.

### Quality Requirements

- ❌ Do NOT generate tests that just verify mocks return what they were told to return
- ❌ Do NOT generate placeholder tests with TODOs
- ❌ Do NOT mix testing frameworks if the project uses a specific one
- ❌ Do NOT generate tests that duplicate existing coverage
- ✅ DO follow existing test naming conventions
- ✅ DO use the project's established mocking approach
- ✅ DO test edge cases and error paths, not just happy paths
- ✅ DO specify exact file paths for all test files

---

### Phase 1: Code Analysis

#### 1.1 Class Structure Analysis

```markdown
## Class Under Test: [ClassName]

### Dependencies
| Dependency | Type | Test Approach |
|------------|------|---------------|
| [Dependency] | [Interface/Concrete] | [Mock/Fake] |

### Public Methods
| Method | Parameters | Return Type | Complexity |
|--------|------------|-------------|------------|
| [method] | [params] | [return] | [Low/Med/High] |

### State Properties (if ViewModel)
| Property | Type | Observable |
|----------|------|------------|
| [property] | [type] | [StateFlow/LiveData] |
```

#### 1.2 Test Scenario Identification

For each public method, identify:

```markdown
## Test Scenarios for [methodName]

### Happy Path
- [Normal successful execution scenario]

### Edge Cases
- [Empty input]
- [Boundary values]
- [Null handling]

### Error Scenarios
- [Network error]
- [Invalid input]
- [Timeout/exception]

### State Transitions (ViewModels)
- [Initial state → action → expected state]
```

---

### Phase 2: Test Generation

#### 2.1 Test Class Structure

```kotlin
class [ClassName]Test {

    // region Setup

    // Mocks
    private lateinit var mockDependency: DependencyType

    // System under test
    private lateinit var sut: ClassName

    @get:Rule
    val mainDispatcherRule = MainDispatcherRule()

    @BeforeEach
    fun setup() {
        mockDependency = mockk()
        sut = ClassName(mockDependency)
    }

    // endregion

    // region [Method/Feature Group Name]

    @Test
    fun `methodName should return expected result when condition`() {
        // Given
        // When
        // Then
    }

    // endregion
}
```

#### 2.2 ViewModel Test Patterns

```kotlin
class FeatureViewModelTest {

    @get:Rule
    val mainDispatcherRule = MainDispatcherRule()

    private val mockRepository: FeatureRepository = mockk()
    private lateinit var viewModel: FeatureViewModel

    @BeforeEach
    fun setup() {
        viewModel = FeatureViewModel(mockRepository)
    }

    // State observation tests
    @Test
    fun `initial state should be Loading`() = runTest {
        val state = viewModel.uiState.first()
        assertThat(state).isInstanceOf(UiState.Loading::class.java)
    }

    // Event handling tests
    @Test
    fun `onItemClick should navigate to detail screen`() = runTest {
        viewModel.sideEffects.test {
            viewModel.onEvent(FeatureEvent.OnItemClick("123"))

            val effect = awaitItem()
            assertThat(effect).isEqualTo(SideEffect.NavigateTo("detail/123"))
        }
    }

    // Data loading tests
    @Test
    fun `loadData success should update state with content`() = runTest {
        coEvery { mockRepository.getData() } returns Result.success(testData)

        viewModel.loadData()

        viewModel.uiState.test {
            val state = awaitItem()
            assertThat(state.data).isEqualTo(testData)
            assertThat(state.isLoading).isFalse()
        }
    }

    @Test
    fun `loadData failure should show error state`() = runTest {
        coEvery { mockRepository.getData() } returns Result.failure(IOException())

        viewModel.loadData()

        viewModel.uiState.test {
            val state = awaitItem()
            assertThat(state.error).isNotNull()
        }
    }
}
```

#### 2.3 UseCase Test Patterns

```kotlin
class GetFeatureDataUseCaseTest {

    private val mockRepository: FeatureRepository = mockk()
    private lateinit var useCase: GetFeatureDataUseCase

    @BeforeEach
    fun setup() {
        useCase = GetFeatureDataUseCase(mockRepository)
    }

    @Test
    fun `invoke should return mapped data from repository`() = runTest {
        val repositoryData = listOf(/* raw data */)
        val expectedData = listOf(/* mapped data */)
        coEvery { mockRepository.getAll() } returns repositoryData

        val result = useCase()

        assertThat(result).isEqualTo(expectedData)
    }

    @Test
    fun `invoke should filter inactive items`() = runTest {
        val mixedData = listOf(
            TestItem(active = true),
            TestItem(active = false),
            TestItem(active = true)
        )
        coEvery { mockRepository.getAll() } returns mixedData

        val result = useCase()

        assertThat(result).hasSize(2)
        assertThat(result.all { it.active }).isTrue()
    }

    @Test
    fun `invoke should propagate repository exception`() = runTest {
        coEvery { mockRepository.getAll() } throws IOException("Network error")

        assertThrows<IOException> {
            useCase()
        }
    }
}
```

#### 2.4 Repository Test Patterns

```kotlin
class FeatureRepositoryTest {

    private val mockLocalDataSource: LocalDataSource = mockk()
    private val mockRemoteDataSource: RemoteDataSource = mockk()
    private lateinit var repository: FeatureRepositoryImpl

    @BeforeEach
    fun setup() {
        repository = FeatureRepositoryImpl(mockLocalDataSource, mockRemoteDataSource)
    }

    @Test
    fun `getData should return cached data when available`() = runTest {
        val cachedData = listOf(testEntity())
        coEvery { mockLocalDataSource.getAll() } returns cachedData

        val result = repository.getData()

        assertThat(result).hasSize(1)
        coVerify(exactly = 0) { mockRemoteDataSource.fetch() }
    }

    @Test
    fun `getData should fetch remote when cache empty`() = runTest {
        coEvery { mockLocalDataSource.getAll() } returns emptyList()
        coEvery { mockRemoteDataSource.fetch() } returns listOf(testDto())
        coEvery { mockLocalDataSource.insertAll(any()) } just Runs

        val result = repository.getData()

        assertThat(result).isNotEmpty()
        coVerify { mockRemoteDataSource.fetch() }
        coVerify { mockLocalDataSource.insertAll(any()) }
    }

    @Test
    fun `refresh should update cache from remote`() = runTest {
        coEvery { mockRemoteDataSource.fetch() } returns listOf(testDto())
        coEvery { mockLocalDataSource.clear() } just Runs
        coEvery { mockLocalDataSource.insertAll(any()) } just Runs

        repository.refresh()

        coVerifyOrder {
            mockLocalDataSource.clear()
            mockRemoteDataSource.fetch()
            mockLocalDataSource.insertAll(any())
        }
    }
}
```

---

### Phase 3: Test Output

Present generated tests organized by test category:

```markdown
## Generated Tests for [ClassName]

### Test Summary
| Category | Test Count | Coverage |
|----------|------------|----------|
| Happy Path | [X] | Core functionality |
| Edge Cases | [X] | Boundary conditions |
| Error Handling | [X] | Exception scenarios |
| State Transitions | [X] | ViewModel states |

### Tests Generated
[Complete test class code]

### Missing Coverage (Intentional)
- [Private methods - covered through public API]
- [Platform-specific code - requires instrumented tests]
```

---

## Expected Output

1. **Complete test class** with all imports and setup
2. **Organized test methods** grouped by feature/method
3. **Clear test names** following `functionName_scenario_expectedResult` pattern
4. **Coverage summary** indicating what's tested and what's not

---

## Test Utilities Template

Provide these utilities if they don't exist:

```kotlin
// MainDispatcherRule.kt
class MainDispatcherRule(
    private val dispatcher: TestDispatcher = UnconfinedTestDispatcher()
) : TestWatcher() {

    override fun starting(description: Description) {
        Dispatchers.setMain(dispatcher)
    }

    override fun finished(description: Description) {
        Dispatchers.resetMain()
    }
}

// Test Fixtures
object TestFixtures {
    fun testItem(
        id: String = "test-id",
        name: String = "Test Item",
        active: Boolean = true
    ) = Item(id, name, active)
}
```

---

## Techniques Used

- **ST-01** (Clear Objective): Generate working unit tests
- **ST-02** (Sequential Instructions): Analyze → Plan → Generate
- **RT-04** (Best Practice Review): Modern Kotlin testing patterns
- **ST-03** (Output Format Templates): Consistent test structure

---

## Related Prompts

- [android_test_strategy_design.md](android_test_strategy_design.md) - Design overall strategy first
- [android_test_coverage_analysis.md](../analysis/android_test_coverage_analysis.md) - Identify coverage gaps
- [android_integration_testing.md](android_integration_testing.md) - For component integration tests
