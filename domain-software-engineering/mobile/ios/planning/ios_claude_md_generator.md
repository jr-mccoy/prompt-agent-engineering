---
title: "iOS CLAUDE.md Generator"
category: mobile-development
description: "Generate a CLAUDE.md project intelligence file for iOS/Swift projects to optimize AI coding agent performance with project-specific conventions, patterns, and constraints."
techniques:
  - ST-01
  - ST-03
difficulty: intermediate
tags:
  - ios
  - swift
  - claude-code
  - ai-agent
updated: "2026-03-20"
---

# iOS CLAUDE.md Generator

**Objective:** Generate a comprehensive CLAUDE.md file for an iOS/Swift project that provides AI coding agents (Claude Code, Cursor, GitHub Copilot) with project-specific conventions, architecture patterns, naming standards, testing expectations, and common pitfalls, enabling the agent to produce code that matches the project's style from the first interaction.

**When to Use:** Use when setting up an iOS project for AI-assisted development, onboarding a new AI tool to an existing codebase, or when AI agents consistently produce code that doesn't match project conventions. Run once and update as conventions evolve.

**Prompt Type:** Modular (200-300 lines)

---

## Context Gathering

Before generating the CLAUDE.md, gather essential context:

1. **Project Basics:**
   - "What is the app name and bundle ID?"
   - "What minimum iOS version?"
   - "SwiftUI-first, UIKit-first, or hybrid?"

2. **Architecture:**
   - "What architecture pattern (MVVM, TCA, Clean, MV)?"
   - "Single target or multi-module (SPM)?"
   - "How is dependency injection handled?"

3. **Conventions:**
   - "What naming conventions are used for files, types, and variables?"
   - "How is navigation structured?"
   - "What state management approach (@Observable, Combine, TCA Store)?"

4. **Tooling:**
   - "What linter/formatter (SwiftLint, SwiftFormat)?"
   - "What testing frameworks (XCTest, swift-testing, Quick/Nimble)?"
   - "What CI/CD platform?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before generating ANY CLAUDE.md, you MUST:**

1. **Scan the actual codebase** - Derive conventions from existing code, not assumptions.
2. **Identify patterns, not just rules** - Show code examples of how things are done.
3. **Include common mistakes** - List things the AI agent should NOT do in this project.
4. **Keep it actionable** - Every section should change agent behavior.

### False-Positive Prevention

- ❌ Do NOT generate generic Swift advice -- focus on THIS project's specifics
- ❌ Do NOT include information the agent can infer from code (obvious things)
- ❌ Do NOT make the file too long (>300 lines loses effectiveness)
- ❌ Do NOT include temporary information (sprint goals, current bugs)
- ✅ DO include project-specific patterns with code examples
- ✅ DO list explicit anti-patterns seen in this codebase
- ✅ DO specify exact file paths for important conventions
- ✅ DO update when major patterns change

---

### Phase 1: Project Intelligence Template

#### 1.1 CLAUDE.md Structure

```markdown
# CLAUDE.md - [App Name]

## Project Overview
- **App:** [Name] - [one-line description]
- **Platform:** iOS [min version]+
- **Language:** Swift [version]
- **UI Framework:** SwiftUI / UIKit / Hybrid
- **Architecture:** [MVVM / TCA / Clean / MV]
- **Package Manager:** SPM / CocoaPods / Mixed

## Build & Run
```bash
# Build
xcodebuild -scheme [Scheme] -destination 'platform=iOS Simulator,name=iPhone 16'

# Test
xcodebuild test -scheme [Scheme] -destination 'platform=iOS Simulator,name=iPhone 16'

# Lint
swiftlint lint --strict
```

## Project Structure
```
[Actual project directory tree with annotations]
```

## Architecture Rules

### State Management
- Use `@Observable` for ViewModels (NOT ObservableObject)
- `@State` owns state at the source view
- `@Binding` passes state to child views
- `@Environment` for dependency injection

### File Organization
- One type per file (exceptions: small helper types)
- Feature folders: `Features/[Name]/[Name]Screen.swift`
- ViewModels: `Features/[Name]/[Name]ViewModel.swift`
- Shared components: `Shared/Components/`

### Naming Conventions
- Screens: `[Feature]Screen` (not View, not ViewController)
- ViewModels: `[Feature]ViewModel`
- Protocols: `[Name]Protocol` or `[Name]Providing`
- Extensions: `[Type]+[Capability].swift`

## Code Patterns

### ViewModel Pattern
```swift
@Observable
final class [Feature]ViewModel {
    enum State: Equatable {
        case idle, loading, loaded([Model]), error(String)
    }
    private(set) var state: State = .idle
    private let repository: [Feature]RepositoryProtocol

    init(repository: [Feature]RepositoryProtocol = [Feature]Repository()) {
        self.repository = repository
    }
}
```

### Screen Pattern
```swift
struct [Feature]Screen: View {
    @State private var viewModel = [Feature]ViewModel()
    var body: some View {
        // State-based content switching
    }
}
```

### Error Handling
- Network errors: Map to user-friendly messages via `APIError`
- Never force unwrap in production code
- Use `Result` type only when async/await is not suitable

## Testing Conventions
- Test file mirrors source: `Features/Home/HomeViewModelTests.swift`
- Use `MockURLProtocol` for network tests
- Test ViewModels by verifying state transitions
- Snapshot tests for complex UI components

## Common Mistakes to Avoid
- ❌ Do NOT use `ObservableObject` / `@Published` (project uses `@Observable`)
- ❌ Do NOT create views without accessibility labels
- ❌ Do NOT hardcode colors (use `AppTheme.Colors.*`)
- ❌ Do NOT hardcode strings (use `Localizable.xcstrings`)
- ❌ Do NOT add Combine imports for new code
- ❌ Do NOT skip `#Preview` macros
- ❌ Do NOT put business logic in Views

## Dependencies
| Package | Purpose | Import |
|---------|---------|--------|
| [List actual SPM dependencies] | | |

## CI/CD
- PRs require: build success + all tests pass + SwiftLint clean
- Branch naming: `feature/`, `bugfix/`, `release/`
- Commit format: conventional commits
```

---

### Phase 2: Codebase Scanning

#### 2.1 Auto-Detection Commands

Run these to populate the template from the actual codebase:

```bash
# Detect minimum iOS version
grep -r "platform" Package.swift 2>/dev/null || grep "IPHONEOS_DEPLOYMENT_TARGET" *.xcodeproj/project.pbxproj

# Detect architecture pattern
find . -name "*.swift" | head -50 | xargs grep -l "ViewModel\|Reducer\|Interactor\|UseCase"

# Detect state management
grep -r "@Observable\|ObservableObject\|@Published\|Store<" --include="*.swift" | head -10

# Detect testing framework
grep -r "import XCTest\|import Testing\|import Quick" --include="*.swift" | head -5

# Detect dependencies
cat Package.swift 2>/dev/null | grep ".package("
cat Podfile 2>/dev/null

# Detect naming patterns
find . -name "*Screen.swift" -o -name "*View.swift" -o -name "*ViewController.swift" | head -20
```

#### 2.2 Convention Inference

```markdown
## Scan Results → Convention Mapping

| What I Found | Convention to Document |
|-------------|----------------------|
| `@Observable` in ViewModels | State management: Observation framework |
| Files named `*Screen.swift` | Naming: Screens, not Views |
| `#Preview` macros present | Always include previews |
| `.accessibilityLabel` usage | Accessibility is required |
| No Combine imports | Avoid Combine in new code |
| `AppTheme.Colors.*` usage | Use design tokens |
```

---

### Phase 3: Validation

**CHECKPOINT:** Review generated CLAUDE.md against the codebase.

```markdown
## CLAUDE.md Quality Check
- [ ] Build commands actually work when pasted into terminal
- [ ] Architecture pattern matches actual code (not aspirational)
- [ ] Naming conventions match 90%+ of existing files
- [ ] Common mistakes list reflects real anti-patterns in this codebase
- [ ] Dependencies list is accurate and complete
- [ ] No generic advice -- everything is project-specific
```

---

## Expected Output

A single `CLAUDE.md` file (100-200 lines) placed at the project root that enables AI coding agents to produce project-consistent code immediately.

---

## Example Interaction

**User:** "Generate CLAUDE.md for our recipe app. MVVM, SwiftUI, iOS 17+, SwiftData, uses TipKit. Three SPM modules: FeatureRecipes, SharedUI, Core."

**Assistant:**

```markdown
# CLAUDE.md - Recipeze

## Project Overview
- **App:** Recipeze - AI-powered recipe discovery and meal planning
- **Platform:** iOS 17+
- **Language:** Swift 5.9
- **UI Framework:** SwiftUI (no UIKit)
- **Architecture:** MVVM with @Observable
- **Modules:** FeatureRecipes, SharedUI, Core (SPM local packages)

## Build & Run
xcodebuild -scheme Recipeze -destination 'platform=iOS Simulator,name=iPhone 16'

## Architecture Rules
- ViewModels use @Observable (NEVER ObservableObject)
- SwiftData for persistence (NEVER Core Data)
- TipKit for user education (NEVER custom tooltip views)
- All new screens must have #Preview with multiple states

## Common Mistakes
- ❌ NEVER import UIKit (SwiftUI-only project)
- ❌ NEVER use UserDefaults for structured data (use SwiftData)
- ❌ NEVER create UI without accessibilityLabel
- ❌ NEVER hardcode strings (use String Catalogs)
```

---

## Techniques Used

- **ST-01** (Clear Objective): Generate project-specific AI agent configuration
- **ST-03** (Output Format Templates): Structured CLAUDE.md template with code examples

---

## Related Prompts

- [ios_project_scaffold.md](ios_project_scaffold.md) - Generate CLAUDE.md alongside project scaffold
- [ios_architecture_selection.md](ios_architecture_selection.md) - Architecture informs CLAUDE.md content
- [ios_ai_agent_workflow.md](ios_ai_agent_workflow.md) - Configure full AI agent workflow

---

## Customization Guide

### For Multi-Team Projects
Add team ownership sections: which team owns which module, who to contact for architecture questions, and module-specific conventions that differ from project defaults.

### For Open Source Projects
Add contributor-focused sections: how to set up the dev environment, how to run tests, coding standards for external contributors, and PR review expectations.
