---
title: "iOS AI Agent Workflow"
category: mobile-development
description: "Configure AI coding agent workflows for iOS development including task decomposition, context management, code generation patterns, and quality verification loops."
techniques:
  - ST-01
  - ST-02
difficulty: intermediate
tags:
  - ios
  - swift
  - ai-agent
  - workflow
updated: "2026-03-20"
---

# iOS AI Agent Workflow

**Objective:** Configure an optimal AI coding agent workflow for iOS/Swift development that maximizes code quality, minimizes iteration cycles, and produces production-ready code by providing the agent with proper context, task decomposition strategies, and verification checkpoints specific to iOS development.

**When to Use:** Use when setting up AI coding agents (Claude Code, Cursor, GitHub Copilot) for iOS development work. Ideal for establishing team standards on how to interact with AI agents for iOS tasks, reducing prompt iteration, and ensuring generated code meets project standards.

**Prompt Type:** Modular (250-300 lines)

---

## Context Gathering

Before configuring the workflow, gather essential context:

1. **Agent Setup:**
   - "Which AI coding agent(s) are being used (Claude Code, Cursor, GitHub Copilot)?"
   - "Is there an existing CLAUDE.md or project rules file?"
   - "What is the team's AI agent experience level?"

2. **Project Context:**
   - "What architecture pattern does the project use?"
   - "What are the most common development tasks (new features, bug fixes, tests, refactoring)?"
   - "What code review standards are in place?"

3. **Quality Gates:**
   - "What must pass before code is merged (tests, lint, build, review)?"
   - "Are there specific iOS requirements (accessibility, Dynamic Type, performance)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before configuring ANY workflow, you MUST:**

1. **Ensure CLAUDE.md exists** - The agent needs project-specific context to produce matching code.
2. **Define task decomposition rules** - AI agents work best with focused, single-responsibility tasks.
3. **Establish verification loops** - Never trust AI output without automated validation.
4. **Set context boundaries** - Tell the agent what files to read and what to ignore.

### False-Positive Prevention

- ❌ Do NOT ask the agent to build an entire feature in one prompt (too broad, quality drops)
- ❌ Do NOT skip the verification step (build, test, lint) after each generation
- ❌ Do NOT provide ambiguous requirements ("make it better")
- ❌ Do NOT assume the agent knows your project conventions without CLAUDE.md
- ✅ DO decompose work into single-screen or single-component tasks
- ✅ DO verify generated code compiles before proceeding to the next task
- ✅ DO provide existing code as context when asking for additions
- ✅ DO use the agent for test generation after implementation (high-value, low-risk)

---

### Phase 1: Task Decomposition Patterns

#### 1.1 iOS Task Taxonomy

| Task Type | AI Agent Effectiveness | Best Approach |
|-----------|----------------------|---------------|
| **New screen (SwiftUI)** | High | Provide design spec + existing screen as pattern |
| **ViewModel logic** | Very High | Specify states, inputs, and expected transitions |
| **Unit test generation** | Very High | Provide implementation, ask for tests |
| **Bug fix** | Medium | Provide error, stack trace, and relevant code |
| **Refactoring** | High | Specify before/after pattern clearly |
| **API integration** | High | Provide endpoint spec + existing APIClient |
| **Accessibility pass** | High | Ask to audit and add modifiers to existing views |
| **Performance optimization** | Low-Medium | Requires Instruments data the agent cannot access |
| **Architecture design** | Medium | Good for options analysis, not final decisions |
| **Complex animations** | Low | SwiftUI animation requires visual iteration |

#### 1.2 Task Decomposition Template

```markdown
## Task: [Feature Name]

### Context Files (agent should read these first)
- `Features/ExistingFeature/ExistingScreen.swift` (pattern to follow)
- `Core/Networking/APIClient.swift` (networking layer)
- `Shared/Components/` (reusable components)
- `CLAUDE.md` (project conventions)

### Subtasks (execute in order)
1. **Define data model** → `Core/Models/NewModel.swift`
   - Input: API response JSON sample
   - Output: Codable Swift struct
   - Verify: Compiles, matches JSON keys

2. **Create API endpoint** → `Core/Networking/Endpoints/NewEndpoint.swift`
   - Input: API documentation / endpoint URL
   - Output: Endpoint definition using existing pattern
   - Verify: Compiles, request URL is correct

3. **Build ViewModel** → `Features/New/NewViewModel.swift`
   - Input: Required states (loading, loaded, error, empty)
   - Output: @Observable ViewModel with all state transitions
   - Verify: Compiles, states are Equatable

4. **Build screen** → `Features/New/NewScreen.swift`
   - Input: Design spec or description + existing screen pattern
   - Output: SwiftUI view with all states, accessibility, #Preview
   - Verify: Compiles, previews render, VoiceOver navigable

5. **Write tests** → `Tests/Features/New/NewViewModelTests.swift`
   - Input: ViewModel implementation
   - Output: Tests covering all state transitions + error paths
   - Verify: All tests pass

6. **Accessibility audit** → Update screen with any missing modifiers
   - Input: Completed screen
   - Output: accessibilityLabel, accessibilityHint, Dynamic Type support
   - Verify: VoiceOver walkthrough
```

---

### Phase 2: Prompt Patterns for iOS Tasks

#### 2.1 Screen Generation Prompt

```markdown
Build a SwiftUI screen following the pattern in `Features/Home/HomeScreen.swift`.

**Screen:** [Name]Screen
**File path:** Features/[Name]/[Name]Screen.swift
**ViewModel:** Features/[Name]/[Name]ViewModel.swift

**Requirements:**
- States: loading (ProgressView), loaded (content), empty (ContentUnavailableView), error (retry button)
- Data: [describe what the screen displays]
- Actions: [list user interactions]
- Navigation: [push/sheet/fullscreen to where]

**Must include:**
- @Observable ViewModel with protocol-based dependency injection
- .accessibilityLabel on all interactive elements
- .refreshable for pull-to-refresh
- #Preview macros for all states
- Dynamic Type support for AX text sizes

**Must NOT include:**
- ObservableObject or @Published
- Force unwraps
- Hardcoded colors or strings
- Business logic in the View
```

#### 2.2 Test Generation Prompt

```markdown
Generate unit tests for the ViewModel at `Features/Recipes/RecipeListViewModel.swift`.

**Test file:** Tests/Features/Recipes/RecipeListViewModelTests.swift
**Follow pattern in:** Tests/Features/Home/HomeViewModelTests.swift

**Test these scenarios:**
1. Initial state is .idle
2. load() transitions to .loading then .loaded with data
3. load() transitions to .loading then .error on failure
4. load() transitions to .loading then .empty when no data
5. refresh() keeps existing data visible during reload
6. delete() removes item and updates state
7. delete() last item transitions to .empty

**Must include:**
- Mock repository using protocol conformance
- async/await test patterns
- XCTAssertEqual for state verification
- No sleep() calls -- use expectations or direct async
```

#### 2.3 Bug Fix Prompt

```markdown
Fix the following issue in `Features/Feed/FeedScreen.swift`:

**Bug:** [describe observable behavior]
**Expected:** [describe correct behavior]
**Error/crash:** [paste error message or stack trace]

**Relevant files:**
- `Features/Feed/FeedScreen.swift` (the buggy view)
- `Features/Feed/FeedViewModel.swift` (state management)
- `Core/Networking/APIClient.swift` (if networking related)

**Constraints:**
- Do not change the public API of FeedViewModel
- Do not introduce new dependencies
- Include a unit test that would have caught this bug
```

---

### Phase 3: Verification Loops

**CHECKPOINT:** Review task decomposition before execution.

```markdown
## Workflow Configuration
- CLAUDE.md present: [Yes/No]
- Tasks decomposed: _ subtasks
- Verification gates defined: [build/test/lint/accessibility]

**Ready to execute workflow?**
```

#### 3.1 After Each AI Generation

```bash
# 1. Build check (must pass)
xcodebuild build -scheme MyApp -destination 'platform=iOS Simulator,name=iPhone 16' 2>&1 | tail -5

# 2. Test check (must pass)
xcodebuild test -scheme MyApp -destination 'platform=iOS Simulator,name=iPhone 16' 2>&1 | tail -10

# 3. Lint check (must pass)
swiftlint lint --path Features/NewFeature/ --strict

# 4. Quick accessibility check
# Open Xcode Preview → Accessibility Inspector → Audit
```

#### 3.2 Quality Verification Checklist

```markdown
## Post-Generation Review
- [ ] Code compiles without warnings
- [ ] All existing tests still pass
- [ ] New tests cover happy path + error paths
- [ ] SwiftLint passes with no violations
- [ ] #Preview macros render correctly
- [ ] Accessibility labels present on all interactive elements
- [ ] No force unwraps, no hardcoded strings/colors
- [ ] File placed in correct directory per project structure
- [ ] Follows CLAUDE.md conventions
```

---

### Phase 4: Workflow Optimization

#### 4.1 Context Window Management

```markdown
## iOS-Specific Context Strategy

### Always include (every prompt):
- CLAUDE.md (project conventions)
- The specific file being modified

### Include for new features:
- An existing feature as a pattern reference
- Relevant data models
- Design spec or description

### Include for bug fixes:
- Error message / stack trace
- The file with the bug
- Related files (ViewModel, Model, API)

### Never include:
- Entire project directory listings
- Generated files (*.xcodeproj internals)
- Test fixtures (unless testing is the task)
- Third-party library source code
```

#### 4.2 Iteration Reduction Strategies

| Strategy | Reduces Iterations By |
|----------|----------------------|
| Provide existing code as pattern | 50-70% (agent matches style) |
| Include CLAUDE.md | 30-50% (avoids convention violations) |
| Specify exact file paths | 20-30% (no guessing) |
| List explicit "must not" constraints | 20-40% (prevents common mistakes) |
| Decompose into single-file tasks | 40-60% (focused, verifiable output) |

---

## Expected Output

A configured AI agent workflow document with task decomposition templates, prompt patterns for common iOS tasks, verification gates, and context management strategies.

---

## Example Interaction

**User:** "I need to add a favorites feature to our recipe app using Claude Code. How should I structure the work?"

**Assistant:**

**Task decomposition (5 prompts, not 1):**

1. **Prompt 1: Data model** - "Add `isFavorite: Bool` to the Recipe SwiftData model at `Core/Models/Recipe.swift`. Include a migration if needed."
   - Verify: builds, migration works

2. **Prompt 2: Repository method** - "Add `toggleFavorite(recipeId:)` and `fetchFavorites()` to RecipeRepository, following the pattern in `Core/Repositories/RecipeRepository.swift`."
   - Verify: builds, unit test passes

3. **Prompt 3: ViewModel** - "Create `FavoritesViewModel.swift` at `Features/Favorites/` following the HomeViewModel pattern. States: loaded (favorites list), empty (no favorites)."
   - Verify: builds, states work

4. **Prompt 4: Screen** - "Create `FavoritesScreen.swift` using the HomeScreen pattern. Include favorite toggle button, empty state with 'Browse Recipes' CTA."
   - Verify: builds, previews render, accessibility

5. **Prompt 5: Tests** - "Write tests for FavoritesViewModel covering: load favorites, toggle favorite on/off, empty state when no favorites. Follow HomeViewModelTests pattern."
   - Verify: all tests pass

**Total: ~30 minutes of agent interaction + 15 minutes of verification = 45 minutes for a complete tested feature.**

---

## Techniques Used

- **ST-01** (Clear Objective): Configure AI agent workflow for iOS development efficiency
- **ST-02** (Sequential Instructions): Phased approach from decomposition to verification

---

## Related Prompts

- [ios_claude_md_generator.md](ios_claude_md_generator.md) - Generate CLAUDE.md for the project
- [ios_project_scaffold.md](ios_project_scaffold.md) - Scaffold project with AI-friendly structure
- [ios_feature_specification.md](ios_feature_specification.md) - Specify features before passing to AI agent

---

## Customization Guide

### For Solo Developers
Simplify verification loops -- trust the build + test gate. Skip the code review step. Focus on test generation as the highest-value AI task (write code yourself, let AI write tests).

### For Large Teams
Add AI-generated code review standards: all AI-generated code must be reviewed by a human before merge. Tag AI-generated PRs. Track AI-generated code quality metrics over time.

### For TCA Projects
Modify prompt patterns to use Reducer structure. Task decomposition becomes: (1) State/Action definition, (2) Reducer logic, (3) View, (4) Tests using TestStore. TCA's deterministic testing makes AI-generated tests particularly reliable.
