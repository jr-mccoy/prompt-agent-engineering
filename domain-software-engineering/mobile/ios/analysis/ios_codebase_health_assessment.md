---
title: "iOS Codebase Health Assessment"
category: mobile-development
description: "Conducts comprehensive health assessment of iOS codebases evaluating project structure, Swift version, framework usage, code organization, and architectural health to provide actionable roadmap"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-04
  - AG-02
  - DS-02
difficulty: intermediate
tags:
  - ios
  - swift
  - mobile-development
  - codebase-health
  - code-quality
updated: "2026-03-19"
---

# iOS Codebase Health Assessment

**Objective:** Conduct a comprehensive health assessment of an iOS codebase, evaluating project structure, Swift version, framework usage, code organization, architecture, dependencies, testing, and documentation to provide an actionable improvement roadmap.

**When to Use:** Use this prompt as the **entry point** for any existing iOS codebase you are unfamiliar with or want to systematically evaluate. Ideal for onboarding to a new project, pre-acquisition technical due diligence, quarterly health checks, or before planning major refactoring efforts. This assessment provides a holistic view that informs which specialized prompts to use next.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before beginning the assessment, gather essential context by asking these questions one at a time:

1. **Project Context:**
   - "What is the app's primary purpose and target audience?"
   - "How old is this codebase, and how many developers typically work on it?"

2. **Known Concerns:**
   - "Are there any specific areas you're already concerned about?"
   - "Have there been recent issues (crashes, performance problems, App Store rejections)?"

3. **Constraints:**
   - "Are there any constraints I should know about (minimum iOS deployment target, specific framework requirements, Objective-C interop needs)?"

4. **Goals:**
   - "What are your primary goals for this assessment? (general health check, preparation for feature work, identifying quick wins, comprehensive audit)"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Trace actual code patterns** - Don't flag based on surface-level observations. Verify that suspected issues actually impact codebase health.
2. **Check for existing solutions** - Search for architectural patterns, utilities, or conventions that may already address concerns.
3. **Understand the context** - Consider WHY the codebase evolved this way. Team size, timeline, and requirements are valid factors.
4. **Confirm actual impact** - Does this actually slow down development, cause bugs, or hurt maintainability?
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `HomeViewController.swift:45`).

**Finding NO major issues is an acceptable outcome.** If the codebase is reasonably healthy, say so with confidence. Don't manufacture problems to fill a report.

### False-Positive Prevention

- ❌ Do NOT flag all deviation from "ideal" architecture as problems
- ❌ Do NOT flag patterns that work well for the team's context
- ❌ Do NOT assume missing tests mean no quality assurance exists
- ❌ Do NOT report stylistic preferences as health issues
- ❌ Do NOT penalize Objective-C interop if the project reasonably requires it
- ✅ DO consider the project's age, team size, and constraints
- ✅ DO understand that pragmatic code can be healthy code
- ✅ DO check for team conventions before flagging inconsistencies
- ✅ DO weigh the cost of "fixing" against actual benefits

---

### Phase 1: Discovery & Initial Scan

Perform a systematic exploration of the codebase to understand its structure and components.

#### 1.1 Project Structure Analysis

**Scan the root directory and build configuration:**

```
Files to examine:
├── *.xcodeproj / *.xcworkspace
├── Package.swift (SPM)
├── Podfile / Podfile.lock (CocoaPods)
├── Cartfile / Cartfile.resolved (Carthage)
├── .swift-version
├── .swiftlint.yml / .swiftformat
├── project.pbxproj (build settings)
├── Info.plist / *.plist
└── [Module / Framework targets]
```

**Evaluate:**
- [ ] Xcode project version and workspace setup
- [ ] Swift version (language and compiler)
- [ ] Dependency manager(s) in use (SPM, CocoaPods, Carthage, or mixed)
- [ ] Target structure (single target vs multi-target, app extensions)
- [ ] Build configurations (Debug, Release, custom schemes)
- [ ] Code signing and provisioning setup
- [ ] Build settings consistency across targets

#### 1.2 Source Code Structure

**Explore the main source directories:**

```
ProjectName/
├── App/
│   ├── AppDelegate.swift / @main App struct
│   └── SceneDelegate.swift (if UIKit lifecycle)
├── Features/ or Screens/ or Modules/
│   ├── Home/
│   ├── Profile/
│   └── Settings/
├── Core/ or Common/
│   ├── Networking/
│   ├── Persistence/
│   └── Extensions/
├── Resources/
│   ├── Assets.xcassets
│   ├── Localizable.strings / String Catalogs
│   └── LaunchScreen.storyboard
└── Supporting Files/
```

**Evaluate:**
- [ ] Folder organization (by feature vs by layer)
- [ ] Naming conventions consistency
- [ ] Resource organization (asset catalogs, localization)
- [ ] Info.plist configuration (permissions, URL schemes, capabilities)
- [ ] Storyboard vs programmatic UI vs SwiftUI usage

#### 1.3 Architecture Pattern Identification

**Search for architectural indicators:**

```swift
// Look for these patterns:
- ViewController subclasses (MVC indicator)
- ViewModel classes / ObservableObject conformances (MVVM indicator)
- Reducer structs / Store classes (TCA / Redux indicator)
- Router / Coordinator classes (Coordinator pattern)
- Interactor / Presenter classes (VIPER indicator)
- Protocol-oriented abstractions (POP design)
```

**Identify:**
- Primary architecture pattern in use
- Consistency of pattern application
- Layer separation (UI, Domain, Data)
- Dependency injection approach (manual, Swinject, Factory, @Environment)

#### 1.4 Dependency Inventory

**Analyze dependency manifests:**

```
Categorize dependencies:
- Apple frameworks (UIKit, SwiftUI, Combine, SwiftData, Core Data)
- Networking (Alamofire, URLSession wrappers, Moya)
- Persistence (Realm, GRDB, Core Data, SwiftData)
- Image loading (Kingfisher, SDWebImage, Nuke)
- DI framework (Swinject, Factory, Needle)
- Reactive (Combine, RxSwift, AsyncAlgorithms)
- Testing libraries (Quick, Nimble, SnapshotTesting)
- Third-party services (Firebase, Analytics, crash reporting)
```

**Evaluate:**
- [ ] Dependency count and complexity
- [ ] Version freshness (major versions behind)
- [ ] Duplicate functionality (multiple libraries for same purpose)
- [ ] Deprecated library usage
- [ ] SPM vs CocoaPods migration status

#### 1.5 Test Infrastructure

**Examine test targets:**

```
ProjectNameTests/        (unit tests - XCTest)
ProjectNameUITests/      (UI tests - XCUITest)
ProjectNameSnapshotTests/ (snapshot tests, if present)
```

**Evaluate:**
- [ ] Test presence and organization
- [ ] Test naming conventions
- [ ] Testing frameworks in use (XCTest, Quick/Nimble, swift-testing)
- [ ] Mock/stub/fake infrastructure
- [ ] Test plan configuration (.xctestplan files)

#### 1.6 Documentation State

**Check for documentation:**

```
Files to look for:
├── README.md
├── CONTRIBUTING.md
├── docs/ or Documentation/
├── ARCHITECTURE.md or ADRs
└── DocC bundles (.docc)
```

**Evaluate:**
- [ ] README completeness (setup instructions, architecture overview)
- [ ] Architecture documentation
- [ ] API/code documentation (DocC, inline comments)
- [ ] Inline code comment quality

---

### Phase 2: Detailed Analysis

After the initial scan, perform deeper analysis in each area.

#### 2.1 Code Quality Deep Dive

**Swift Idiom Usage:**
- Search for anti-patterns: force unwraps (`!`), force casts (`as!`), force try (`try!`)
- Evaluate Optional handling patterns (guard let, if let, nil coalescing, Optional chaining)
- Check proper use of value types vs reference types
- Assess protocol-oriented design (protocol extensions, protocol composition)
- Review enum usage (associated values, CaseIterable, RawRepresentable)

**Concurrency and Async/Await:**
- Check Swift Concurrency adoption (async/await, Task, TaskGroup)
- Evaluate actor usage for thread safety
- Look for structured concurrency violations (detached tasks, unstructured Task {})
- Assess Sendable conformance and data-race safety
- Check for legacy concurrency patterns (DispatchQueue, OperationQueue)

**Resource Management:**
- Check for retain cycles (closure capture lists, delegate patterns)
- Evaluate Combine subscription lifecycle management (AnyCancellable storage)
- Look for potential memory leaks (strong reference cycles in closures)

#### 2.2 Architecture Quality Assessment

**Layer Boundaries:**
- Check if Views/ViewControllers depend only on ViewModels
- Verify Data layer is properly abstracted behind protocols
- Look for layer violations (Views directly accessing persistence)
- Assess model mapping between layers (DTO -> Domain -> View models)

**Component Organization:**
- Evaluate ViewModel responsibilities (too much logic?)
- Check Repository pattern implementation
- Assess use case granularity (if Clean Architecture)
- Review navigation architecture (NavigationStack, Coordinator, Storyboard segues)

**State Management:**
- Identify state holder patterns (@State, @StateObject, @ObservedObject, @EnvironmentObject)
- Evaluate UI state modeling
- Check for state consistency patterns
- Assess side effect handling

#### 2.3 Build System Health

**Xcode Project Configuration:**
- Check for build performance issues (large xibs, unbounded build phases)
- Evaluate build phase scripts (SwiftLint, code generation)
- Assess modularization opportunities (Swift packages, frameworks)
- Review code signing configuration

**CI/CD Readiness:**
- Check for CI configuration files (.github/workflows, fastlane, Xcode Cloud)
- Evaluate build reproducibility
- Assess provisioning profile and certificate management

#### 2.4 Security Quick Scan

**Common Issues to Check:**
- Hardcoded secrets or API keys in source
- Insecure UserDefaults usage for sensitive data
- Missing App Transport Security exceptions review
- Keychain usage patterns
- Jailbreak detection if required

---

### Phase 3: Findings Presentation

**CHECKPOINT 1:** Present the initial findings summary to the user.

Compile findings into the Health Report structure below and present to the user before proceeding.

```markdown
## Initial Scan Complete

I've completed the initial codebase scan. Here's what I found at a high level:

### Quick Stats
- **Codebase Size:** [X Swift files, Y lines of code]
- **Target Count:** [X targets (app, extensions, frameworks)]
- **Architecture Pattern:** [Identified pattern]
- **Swift Version:** [X.X]
- **Deployment Target:** iOS [XX] | **Built With:** Xcode [XX.X]

### First Impressions
[2-3 sentences on overall impression]

### Areas of Note
- **Strengths:** [2-3 bullet points]
- **Concerns:** [2-3 bullet points]

### Questions Before Deep Dive
1. [Any clarifying questions based on findings]
2. [Questions about unusual patterns found]

**Would you like me to proceed with the detailed analysis, or would you like me to focus on any specific area first?**
```

---

### Phase 4: Comprehensive Health Report

After user confirmation, compile the full assessment.

#### Health Report Structure

```markdown
# Codebase Health Report: [App Name]

## Executive Summary

### Health Score: [A/B/C/D/F]

| Category | Score | Status |
|----------|-------|--------|
| Project Structure | [1-10] | [emoji] |
| Architecture | [1-10] | [emoji] |
| Code Quality | [1-10] | [emoji] |
| Dependencies | [1-10] | [emoji] |
| Testing | [1-10] | [emoji] |
| Documentation | [1-10] | [emoji] |

**Score Guide:** 9-10: Excellent | 7-8: Good | 5-6: Adequate | 3-4: Needs Work | 1-2: Critical

### Key Strengths
1. [Strength with evidence: file:line or pattern reference]
2. [Strength with evidence]
3. [Strength with evidence]

### Critical Issues (Immediate Attention)
1. [Issue with severity, location, and impact]
2. [Issue with severity, location, and impact]
3. [Issue with severity, location, and impact]

### Technical Debt Estimate
- **Low-Hanging Fruit:** [X items, estimated Y hours]
- **Medium Effort:** [X items, estimated Y days]
- **Major Refactoring:** [X items, estimated Y weeks]

---

## Detailed Findings

### 1. Project Structure Analysis

#### Current State
[Description of current structure]

#### Findings

| Finding | Severity | Location | Recommendation |
|---------|----------|----------|----------------|
| [Finding] | [Critical/High/Medium/Low] | [file/path] | [Action] |

#### Structure Assessment
- **Target Organization:** [Single/Multi-target, assessment]
- **Build System:** [SPM/CocoaPods/Carthage/mixed status]
- **Folder Structure:** [By feature/layer, consistency]

---

### 2. Architecture Assessment

#### Identified Pattern: [MVC/MVVM/TCA/VIPER/Hybrid]

#### Layer Analysis

**UI Layer:**
- Components: [ViewControllers, SwiftUI Views, Composites]
- ViewModel usage: [Proper/Issues found]
- State management: [@State/@StateObject/ObservableObject/Other]

**Domain Layer:**
- Presence: [Yes/No/Partial]
- Use cases: [Pattern assessment]
- Business logic location: [Appropriate/Scattered]

**Data Layer:**
- Repository pattern: [Implemented/Partial/Missing]
- Data sources: [Local/Remote/Both]
- Caching strategy: [Present/Absent]

#### Architecture Issues

| Issue | Severity | Example | Impact |
|-------|----------|---------|--------|
| [Layer violation] | [Severity] | [file:line] | [Impact] |

---

### 3. Code Quality Assessment

#### Swift Usage

| Aspect | Status | Examples |
|--------|--------|----------|
| Optional Safety | [Good/Needs Work] | [Specific patterns found] |
| Concurrency | [Good/Needs Work] | [Usage patterns] |
| Idioms | [Good/Needs Work] | [Examples] |

#### Code Smells Identified

| Smell | Count | Severity | Examples |
|-------|-------|----------|----------|
| Force unwrapping (!) | [X] | High | [files] |
| Massive view controllers | [X] | Medium | [files] |
| Long methods | [X] | Medium | [files] |
| Dead code | [X] | Low | [files] |

---

### 4. Dependency Health

#### Version Analysis

| Category | Library | Current | Latest | Status |
|----------|---------|---------|--------|--------|
| Language | Swift | X.X | Y.Y | [Up to date/Behind] |
| Tooling | Xcode | X.X | Y.Y | [Status] |
| Framework | [Library] | X.X.X | Y.Y.Y | [Status] |

---

### 5. Testing Assessment

#### Test Coverage Overview

| Test Type | Present | Count | Quality |
|-----------|---------|-------|---------|
| Unit Tests | [Yes/No] | [X] | [Assessment] |
| Integration Tests | [Yes/No] | [X] | [Assessment] |
| UI Tests | [Yes/No] | [X] | [Assessment] |
| Snapshot Tests | [Yes/No] | [X] | [Assessment] |

---

### 6. Documentation Assessment

#### Documentation Inventory

| Document | Present | Quality | Last Updated |
|----------|---------|---------|--------------|
| README | [Yes/No] | [1-10] | [Date/Unknown] |
| Architecture docs | [Yes/No] | [1-10] | [Date/Unknown] |
| DocC bundles | [Yes/No] | [1-10] | [Date/Unknown] |
| Setup guide | [Yes/No] | [1-10] | [Date/Unknown] |

---

## Risk Assessment

### Security Risks

| Risk | Severity | Location | Mitigation |
|------|----------|----------|------------|
| [Risk] | [Critical/High/Medium/Low] | [Where] | [Action] |

### Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk] | [High/Medium/Low] | [Description] | [Action] |

---

## Recommended Next Steps

### Immediate (This Week)
1. **[Action]** - [Why, effort estimate]
2. **[Action]** - [Why, effort estimate]

### Short-term (This Month)
1. **[Action]** - [Why, effort estimate]
2. **[Action]** - [Why, effort estimate]

### Medium-term (This Quarter)
1. **[Action]** - [Why, effort estimate]
2. **[Action]** - [Why, effort estimate]

---

## Recommended Follow-up Prompts

Based on this assessment, consider using these prompts next:

| Finding | Recommended Prompt | Priority |
|---------|-------------------|----------|
| [Architecture issues] | `ios_architecture_review.md` | High |
| [Performance concerns] | `ios_performance_audit.md` | Medium |
| [Tech debt] | `ios_technical_debt_assessment.md` | Medium |
| [Test gaps] | `ios_test_coverage_analysis.md` | Medium |
| [Security concerns] | `ios_local_data_security_audit.md` | High |
```

---

### Phase 5: Discussion & Next Steps

**CHECKPOINT 2:** After presenting the full report, engage with the user.

```markdown
## Questions for Discussion

1. Does this assessment align with your perception of the codebase?
2. Are there any findings that surprise you or seem incorrect?
3. Which areas would you like to prioritize for improvement?
4. Are there constraints (time, resources) that should influence our approach?

## Ready to Take Action?

I can help you start addressing these findings. Would you like me to:

- [ ] Deep dive into any specific area
- [ ] Start working on the highest priority issue
- [ ] Generate a detailed remediation plan for a specific category
- [ ] Run a more focused audit (architecture, performance, dependencies, security)

**What would be most valuable for you right now?**
```

---

## Expected Output

The assessment produces:

1. **Executive Summary** - Quick overview with health score and key findings
2. **Detailed Findings** - Category-by-category analysis with evidence
3. **Risk Assessment** - Security, technical, and maintainability risks
4. **Action Plan** - Prioritized recommendations with effort estimates
5. **Follow-up Guide** - Which specialized prompts to use next

---

## Example Interaction

**User:** Please assess the health of this iOS app. It's a health & fitness app about 4 years old, currently maintained by 3 developers.

**Agent:** I'll conduct a comprehensive health assessment. Let me start by exploring the codebase structure.

*[Agent performs initial scan]*

**Agent:**

## Initial Scan Complete

### Quick Stats
- **Codebase Size:** 312 Swift files, ~48,000 lines of code
- **Target Count:** 3 targets (main app, WidgetKit extension, unit tests)
- **Architecture Pattern:** MVVM with Repository pattern
- **Swift Version:** 5.9 (current is 6.0)
- **Deployment Target:** iOS 16.0 | **Built With:** Xcode 15.2

### First Impressions
The codebase shows a clear MVVM pattern with consistent ViewModel conventions across features. The mix of UIKit and SwiftUI is well-managed through a hosting pattern. Dependencies are moderately outdated, with some Combine-based networking that could migrate to async/await.

### Areas of Note
- **Strengths:** Consistent ViewModel patterns, solid Keychain wrapper, well-organized asset catalogs with localization
- **Concerns:** No SwiftLint configuration, several force unwraps in the networking layer, HealthKit integration lacks error handling

### Questions Before Deep Dive
1. I see both UIKit and SwiftUI views - is there an active migration strategy, or is this a gradual transition?
2. The app uses both Core Data and UserDefaults for persistence - is the Core Data store the source of truth for workout data?

**Would you like me to proceed with the detailed analysis, or focus on any specific area first?**

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective with clear scope
- **ST-02** (Sequential Instructions): Phased discovery -> analysis -> report -> action
- **RT-02** (Multi-Dimensional Analysis): Six-category assessment framework
- **RT-04** (Best Practice Review): Evaluation against iOS/Swift best practices
- **AG-02** (Skeptical Default Stance): Honest assessment over validation
- **DS-02** (Domain Knowledge): iOS-specific framework and tooling expertise

---

## Related Prompts

- [ios_architecture_review.md](ios_architecture_review.md) - Deep dive into architecture patterns
- [ios_performance_audit.md](ios_performance_audit.md) - Performance bottleneck identification
- [ios_technical_debt_assessment.md](ios_technical_debt_assessment.md) - Detailed debt cataloging
- [ios_dependency_audit.md](ios_dependency_audit.md) - Focused dependency analysis
- [ios_test_coverage_analysis.md](ios_test_coverage_analysis.md) - Test coverage evaluation
- [ios_ai_code_review.md](ios_ai_code_review.md) - AI-assisted Swift code review

---

## Customization Guide

### For Different Assessment Depths

**Quick Health Check (15-minute scan):**
- Focus on Phase 1 only
- Skip detailed code quality analysis
- Provide high-level summary without deep file references

**Due Diligence Assessment:**
- Extend security analysis
- Add compliance checking (HIPAA, App Store guidelines)
- Include team/process assessment questions
- Emphasize risk quantification

**Pre-Migration Assessment:**
- Focus heavily on architecture and dependencies
- Assess SwiftUI readiness if migration planned
- Identify migration blockers and risks

### For Different App Types

**Consumer Apps:**
- Emphasize UI/UX code quality
- Focus on performance and battery impact
- Check for analytics and crash reporting integration

**Enterprise Apps:**
- Emphasize security assessment
- Check for MDM compatibility
- Assess authentication and data protection

**SDK/Framework Projects:**
- Focus on API surface analysis
- Check backward compatibility patterns
- Assess DocC documentation completeness

### Adjusting Severity Thresholds

For **new projects** (< 6 months):
- Be stricter on architecture patterns
- More forgiving on test coverage
- Emphasize foundation quality

For **mature projects** (> 3 years):
- Focus on technical debt accumulation
- Emphasize modernization opportunities (Swift Concurrency, SwiftUI, SwiftData)
- Check for deprecated API usage

For **legacy rescue** projects:
- Lower expectations for initial scores
- Focus on critical issues only
- Emphasize incremental improvement path
