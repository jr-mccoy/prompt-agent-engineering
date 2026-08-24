---
title: "iOS Technical Debt Assessment"
category: mobile-development
description: "Catalog and prioritize technical debt across an iOS codebase with severity scoring, impact analysis, and a phased remediation roadmap with effort estimates"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-04
  - AG-02
difficulty: advanced
tags:
  - ios
  - swift
  - technical-debt
  - code-quality
updated: "2026-03-20"
---

# iOS Technical Debt Assessment

**Objective:** Systematically catalog and prioritize all forms of technical debt in an iOS codebase — deprecated APIs, compiler warnings, TODO/FIXME markers, architecture shortcuts, dependency rot, and testing gaps — then produce a severity-scored inventory with a phased remediation roadmap including effort estimates.

**When to Use:** Use this prompt when preparing a refactoring initiative, building a case for dedicated tech-debt sprints, onboarding to a legacy codebase, or before a major iOS version upgrade. Ideal after a codebase health assessment surfaces debt concerns or when build warnings have been accumulating unchecked.

**Prompt Type:** Comprehensive (350-500 lines)

---

## Context Gathering

Before beginning the assessment, gather context:

1. **Project History:**
   - "How old is the codebase and how many contributors have worked on it?"
   - "Have there been major rewrites or architecture changes?"

2. **Known Pain Points:**
   - "Are there areas the team already considers problematic or fragile?"
   - "Has anyone cataloged existing debt before?"

3. **Constraints:**
   - "What iOS deployment target are you supporting?"
   - "Are there upcoming deadlines that limit refactoring bandwidth?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Confirm the debt is real** - Verify that flagged items are genuinely outdated, deprecated, or problematic — not intentional design decisions.
2. **Check for migration plans** - Search for existing TODO comments, tickets, or documentation indicating the team is already aware of and tracking the debt.
3. **Assess actual impact** - Quantify how the debt affects build times, crash rates, developer velocity, or user experience.
4. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `LegacyNetworkManager.swift:87`).
5. **Distinguish debt from preference** - Using an older but stable pattern is not debt if it works correctly and is maintained.

**Finding LOW technical debt is an acceptable outcome.** If the codebase is well-maintained for its age and context, say so. Don't manufacture debt items to fill a report.

### False-Positive Prevention

- ❌ Do NOT flag working legacy code as debt purely because newer APIs exist
- ❌ Do NOT count every TODO comment as actionable debt without reading context
- ❌ Do NOT treat all compiler warnings as equal severity
- ❌ Do NOT flag deprecated APIs that have no replacement in the current deployment target
- ✅ DO check if deprecated APIs have available replacements for the project's minimum target
- ✅ DO verify that flagged patterns actually cause problems (crashes, slowdowns, confusion)
- ✅ DO consider the cost of remediation vs. the cost of keeping the debt
- ✅ DO group related debt items rather than listing each instance separately

---

### Phase 1: Debt Inventory

#### 1.1 Deprecated API Usage

**Scan for deprecated Apple APIs:**

```swift
// Common deprecated patterns to search for

// UIKit deprecations
UIWebView                    // Deprecated iOS 12, removed from App Store submissions
UIAlertView / UIActionSheet  // Deprecated iOS 9, use UIAlertController
beginAnimations/commitAnimations  // Deprecated, use UIView.animate
UIApplication.statusBarStyle // Deprecated iOS 9, use preferredStatusBarStyle

// Foundation deprecations
NSURLConnection              // Deprecated iOS 9, use URLSession
NSKeyedArchiver.archivedData(withRootObject:)  // Deprecated iOS 12
UIDevice.current.name        // Returns generic name in iOS 16+ without entitlement

// Swift concurrency
DispatchQueue.main.async     // Not deprecated but migration target for @MainActor
completionHandler patterns   // Migration target for async/await

// SwiftUI deprecations (if applicable)
NavigationView               // Deprecated iOS 16, use NavigationStack/NavigationSplitView
onChange(of:perform:)         // Deprecated iOS 17, use onChange(of:initial:_:)
```

**Deprecated API Inventory:**

| API | Replacement | Min Target | Files Affected | Severity |
|-----|-------------|------------|----------------|----------|
| [Deprecated API] | [Replacement] | [iOS version needed] | [Count] | [Critical/High/Medium/Low] |

#### 1.2 TODO/FIXME/HACK Markers

**Search for debt markers in source code:**

```bash
# Marker categories to scan
TODO:       # Planned work not yet done
FIXME:      # Known broken code
HACK:       # Intentional workaround
WORKAROUND: # Temporary fix
TEMP:       # Temporary code
XXX:        # Attention needed
@available(*, deprecated)  # Self-deprecated code
```

**Marker Classification:**

| Marker | File:Line | Age (git blame) | Context | Priority |
|--------|-----------|-----------------|---------|----------|
| [Marker text] | [Location] | [Date/Author] | [What it means] | [P1-P4] |

#### 1.3 Compiler Warnings

**Catalog active compiler warnings:**

```
// Warning categories
- Deprecation warnings (API usage)
- Type conversion warnings (implicit casts, loss of precision)
- Unused variable/import warnings
- Protocol conformance warnings
- Concurrency warnings (Sendable, @MainActor)
- Strict concurrency checking warnings (Swift 6 readiness)
```

**Warning Summary:**

| Warning Category | Count | Auto-Fixable | Effort to Fix |
|-----------------|-------|--------------|---------------|
| Deprecation | [N] | [Yes/No/Partial] | [Hours] |
| Concurrency | [N] | [Yes/No/Partial] | [Hours] |
| Type safety | [N] | [Yes/No/Partial] | [Hours] |
| Unused code | [N] | [Yes/No/Partial] | [Hours] |

---

### Phase 2: Debt Categorization

#### 2.1 Code Debt

**Code-level quality issues:**

```swift
// Massive types (> 500 lines)
// Search for large files that violate single responsibility
// Check: ViewControllers, ViewModels, Managers, Helpers

// God objects
// Classes with too many responsibilities
class AppManager {
    func handleNetworking() { }
    func managePersistence() { }
    func configureAnalytics() { }
    func handlePushNotifications() { }
    // Doing too much
}

// Force unwrapping in production code
let user = response.data!          // Crash risk
let cell = tableView.dequeueReusableCell(...)! // Common pattern but risky

// Stringly-typed patterns
let cell = tableView.dequeueReusableCell(withIdentifier: "ProductCell")
NotificationCenter.default.post(name: NSNotification.Name("UserDidLogin"))
UserDefaults.standard.string(forKey: "apiToken")
```

**Code Debt Inventory:**

| Issue | Instances | Risk | Effort | Priority |
|-------|-----------|------|--------|----------|
| Force unwraps in prod code | [N] | Crash risk | [Hours] | [P1-P4] |
| Files > 500 lines | [N] | Maintainability | [Days] | [P1-P4] |
| God objects | [N] | Testability | [Days] | [P1-P4] |
| Stringly-typed patterns | [N] | Refactoring risk | [Hours] | [P1-P4] |

#### 2.2 Architecture Debt

**Structural and design issues:**

```swift
// Singleton overuse
class NetworkManager {
    static let shared = NetworkManager()
    // Untestable, hidden dependencies
}

// Missing abstraction layers
class ProductViewController: UIViewController {
    func viewDidLoad() {
        URLSession.shared.dataTask(with: url) { data, _, _ in
            let products = try? JSONDecoder().decode([Product].self, from: data!)
            DispatchQueue.main.async { self.tableView.reloadData() }
        }.resume()
    }
    // View directly calling network — no repository, no ViewModel
}

// Circular dependencies
// ModuleA imports ModuleB, ModuleB imports ModuleA

// Mixed UI frameworks without clear boundary
// Some screens in UIKit, some in SwiftUI, no hosting strategy
```

#### 2.3 Dependency Debt

**Third-party dependency issues:**

| Dependency | Current Version | Latest | Behind By | Maintenance Status |
|-----------|----------------|--------|-----------|-------------------|
| [Library] | [Version] | [Version] | [Releases] | [Active/Stale/Abandoned] |

**Red Flags:**
- Dependencies not updated in > 12 months
- Dependencies with known CVEs
- Dependencies that don't support current Xcode/Swift version
- Abandoned dependencies with no active maintainer

#### 2.4 Testing Debt

**Testing infrastructure gaps:**

| Area | Coverage | Critical Gaps |
|------|----------|---------------|
| Unit tests | [%] | [Untested areas] |
| UI tests | [Count] | [Missing flows] |
| Snapshot tests | [Yes/No] | [Coverage] |
| Integration tests | [Yes/No] | [Coverage] |
| CI/CD test execution | [Yes/No] | [Issues] |

---

### Phase 3: Impact Scoring

#### 3.1 Severity Matrix

**Score each debt item on four dimensions (1-5 each):**

| Dimension | 1 (Low) | 3 (Medium) | 5 (High) |
|-----------|---------|------------|----------|
| **User Impact** | No user effect | Occasional UX issues | Crashes or data loss |
| **Developer Velocity** | Minor inconvenience | Slows feature work | Blocks development |
| **Risk** | Safe to ignore | Could escalate | Ticking time bomb |
| **Spread** | Isolated | Moderate spread | Pervasive across codebase |

**Composite Score:** (User Impact + Developer Velocity + Risk + Spread) / 4

#### 3.2 Priority Classification

| Priority | Score Range | Action |
|----------|------------|--------|
| P1 - Critical | 4.0 - 5.0 | Address in next sprint |
| P2 - High | 3.0 - 3.9 | Schedule within quarter |
| P3 - Medium | 2.0 - 2.9 | Plan for next quarter |
| P4 - Low | 1.0 - 1.9 | Address opportunistically |

---

### Phase 4: Remediation Roadmap

**CHECKPOINT:** Present debt summary and get confirmation before building roadmap.

```markdown
## Technical Debt Summary

### Debt Distribution

| Category | P1 | P2 | P3 | P4 | Total |
|----------|----|----|----|----|-------|
| Code | [N] | [N] | [N] | [N] | [N] |
| Architecture | [N] | [N] | [N] | [N] | [N] |
| Dependencies | [N] | [N] | [N] | [N] | [N] |
| Testing | [N] | [N] | [N] | [N] | [N] |

### Top 5 Critical Items

1. **[Item]** - Score: [X.X] - [Brief description]
2. **[Item]** - Score: [X.X] - [Brief description]
3. **[Item]** - Score: [X.X] - [Brief description]
4. **[Item]** - Score: [X.X] - [Brief description]
5. **[Item]** - Score: [X.X] - [Brief description]

**Shall I proceed with the detailed remediation roadmap?**
```

#### 4.1 Phased Remediation Plan

```markdown
### Phase 1: Quick Wins (1-2 sprints)

Target: P1 items with low effort, high impact

| Item | Effort | Impact | Approach |
|------|--------|--------|----------|
| Fix compiler warnings | 2-4 hours | Reduces noise, improves CI | Batch fix by category |
| Remove force unwraps | 1-2 days | Reduces crash risk | Replace with guard/optional binding |
| Update deprecated APIs | 1-3 days | Future-proofs | Search-and-replace where possible |

### Phase 2: Structural Improvements (1-2 quarters)

Target: P2 architecture and code debt

| Item | Effort | Impact | Approach |
|------|--------|--------|----------|
| Extract ViewModels from large VCs | 2-4 weeks | Testability | One screen at a time |
| Replace singletons with DI | 1-2 weeks | Testability | Introduce protocol + constructor injection |
| Add missing test coverage | 2-4 weeks | Confidence | Focus on critical business logic first |

### Phase 3: Strategic Modernization (2-4 quarters)

Target: P3-P4 modernization opportunities

| Item | Effort | Impact | Approach |
|------|--------|--------|----------|
| Migrate to async/await | 4-8 weeks | Code clarity | Start with new code, migrate gradually |
| Modularize into SPM packages | 4-6 weeks | Build speed | Extract shared code first |
| SwiftUI migration for new screens | Ongoing | Modern UX | New features in SwiftUI |
```

#### 4.2 Effort Estimation Summary

```markdown
### Total Estimated Effort

| Phase | Duration | Developer-Weeks | Risk |
|-------|----------|----------------|------|
| Phase 1: Quick Wins | 1-2 sprints | 1-2 | Low |
| Phase 2: Structural | 1-2 quarters | 4-8 | Medium |
| Phase 3: Strategic | 2-4 quarters | 8-16 | Medium-High |

### Recommended Approach
- Allocate 15-20% of sprint capacity to tech debt
- Track debt reduction metrics sprint-over-sprint
- Combine debt work with feature work when touching same files
```

---

## Expected Output

1. **Debt Inventory** - Complete catalog of all identified debt items with file:line locations
2. **Categorized Assessment** - Debt organized by type: code, architecture, dependency, testing
3. **Impact Scores** - Each item scored on user impact, velocity, risk, and spread
4. **Priority Matrix** - Items classified P1 through P4
5. **Remediation Roadmap** - Phased plan with effort estimates and approach descriptions

---

## Example Interaction

**User:** Assess the technical debt in our iOS shopping app. We've been adding features fast for two years and it feels like things are getting harder to maintain.

**Agent:** I'll conduct a comprehensive technical debt assessment. Let me start by scanning for common debt indicators.

*[Agent performs debt inventory scan]*

**Agent:**

## Technical Debt Summary

### Debt Distribution

| Category | P1 | P2 | P3 | P4 | Total |
|----------|----|----|----|----|-------|
| Code | 3 | 8 | 12 | 5 | 28 |
| Architecture | 1 | 4 | 3 | 0 | 8 |
| Dependencies | 2 | 3 | 1 | 0 | 6 |
| Testing | 1 | 2 | 1 | 0 | 4 |

### Top 5 Critical Items

1. **47 force unwraps in production code** - Score: 4.5 - Three crash reports this month trace to forced unwraps in `CartManager.swift:112` and `PaymentProcessor.swift:67`
2. **Alamofire 4.x (3 major versions behind)** - Score: 4.2 - Known security vulnerability CVE-2023-XXXX, blocks Swift 6 adoption
3. **Zero test coverage on checkout flow** - Score: 4.0 - Most revenue-critical path has no automated testing
4. **`AppDelegate.swift` at 1,847 lines** - Score: 3.8 - All initialization, routing, push handling, and deep linking in one file
5. **43 concurrency warnings** - Score: 3.5 - Blocks Swift 6 strict concurrency; data races possible in `CartManager`

**Shall I proceed with the detailed remediation roadmap?**

---

## Techniques Used

- **ST-01** (Clear Objective): Focused debt assessment objective with defined deliverables
- **ST-02** (Sequential Instructions): Phased inventory, categorization, scoring, and roadmap process
- **RT-02** (Multi-Dimensional Analysis): Four-category debt taxonomy with four-dimension scoring
- **RT-04** (Best Practice Review): iOS and Swift best practices as debt baseline
- **AG-02** (Skeptical Default Stance): Verify debt is real before reporting; low debt is acceptable

---

## Related Prompts

- [ios_codebase_health_assessment.md](ios_codebase_health_assessment.md) - Broader codebase evaluation
- [ios_architecture_review.md](ios_architecture_review.md) - Architecture-specific deep dive
- [ios_dependency_audit.md](ios_dependency_audit.md) - Detailed dependency analysis
- [ios_test_coverage_analysis.md](ios_test_coverage_analysis.md) - Test gap analysis

---

## Customization Guide

### For Swift 6 Migration Focus
- Weight concurrency warnings and Sendable conformance heavily
- Track `@preconcurrency` usage as temporary debt
- Prioritize actor isolation issues
- Check for unsafe global mutable state

### For App Store Compliance
- Prioritize deprecated APIs that Apple has flagged for removal
- Check for private API usage that could trigger rejection
- Verify minimum deployment target alignment with Apple's requirements
- Check for UIWebView references (blocked from submission)

### For Performance-Critical Apps
- Weight performance-related debt higher (synchronous I/O, main thread blocking)
- Catalog missing Instruments profiling coverage
- Check for memory leak patterns (retain cycles, closure captures)
- Assess image/asset optimization debt

### For Team Scaling
- Emphasize documentation debt (missing READMEs, outdated comments)
- Weight code clarity and naming consistency higher
- Prioritize modularization for parallel development
- Focus on onboarding friction as a debt metric
