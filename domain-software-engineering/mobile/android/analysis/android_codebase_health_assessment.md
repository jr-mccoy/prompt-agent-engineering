---
title: "Android Codebase Health Assessment"
category: mobile-development
description: "Conducts comprehensive health assessment of Android codebases evaluating structure, architecture, dependencies, and testing to provide actionable roadmap"
techniques:
  - ST-01
  - ST-02
  - ST-03
  - RT-02
  - DS-06
difficulty: intermediate
tags:
  - android
  - mobile-development
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/analysis/android_architecture_review.md
  - domain-software-engineering/mobile/android/analysis/android_technical_debt_assessment.md
  - domain-software-engineering/mobile/android/analysis/android_test_coverage_analysis.md
---


# Android Codebase Health Assessment

**Objective:** Conduct a comprehensive health assessment of an Android codebase, evaluating project structure, architecture, code quality, dependencies, testing, and documentation to provide an actionable improvement roadmap.

**When to Use:** Use this prompt as the **entry point** for any existing Android codebase you're unfamiliar with or want to systematically evaluate. Ideal for onboarding to a new project, pre-acquisition technical due diligence, quarterly health checks, or before planning major refactoring efforts. This assessment provides a holistic view that informs which specialized prompts to use next.

**Prompt Type:** Comprehensive (400-500 lines)

---

## Context Gathering

Before beginning the assessment, gather essential context by asking these questions one at a time:

1. **Project Context:**
   - "What is the app's primary purpose and target audience?"
   - "How old is this codebase, and how many developers typically work on it?"

2. **Known Concerns:**
   - "Are there any specific areas you're already concerned about?"
   - "Have there been recent issues (crashes, performance problems, difficult deployments)?"

3. **Constraints:**
   - "Are there any constraints I should know about (minimum API level, specific library requirements, legacy system integrations)?"

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
5. **Provide specific file:line locations** - Every finding MUST include exact code locations (e.g., `MainActivity.kt:45`).

**Finding NO major issues is an acceptable outcome.** If the codebase is reasonably healthy, say so with confidence. Don't manufacture problems to fill a report.

### False-Positive Prevention

- ❌ Do NOT flag all deviation from "ideal" architecture as problems
- ❌ Do NOT flag patterns that work well for the team's context
- ❌ Do NOT assume missing tests mean no quality assurance exists
- ❌ Do NOT report stylistic preferences as health issues
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
├── settings.gradle.kts / settings.gradle
├── build.gradle.kts / build.gradle (root)
├── gradle.properties
├── gradle/
│   ├── libs.versions.toml (version catalog)
│   └── wrapper/gradle-wrapper.properties
├── app/
│   └── build.gradle.kts / build.gradle
└── [feature modules]/
```

**Evaluate:**
- [ ] Gradle version and AGP (Android Gradle Plugin) version
- [ ] Kotlin version
- [ ] Build configuration approach (Groovy vs Kotlin DSL)
- [ ] Version catalog usage vs hardcoded versions
- [ ] Convention plugins presence
- [ ] Module structure (single module vs multi-module)
- [ ] Build flavors and variants configuration

#### 1.2 Source Code Structure

**Explore the main source directories:**

```
app/src/main/
├── java/ or kotlin/
│   └── [package structure]
├── res/
│   ├── layout/
│   ├── values/
│   ├── drawable/
│   └── [other resources]
└── AndroidManifest.xml
```

**Evaluate:**
- [ ] Package organization (by feature vs by layer)
- [ ] Naming conventions consistency
- [ ] Resource organization and naming
- [ ] Manifest configuration (permissions, components, features)

#### 1.3 Architecture Pattern Identification

**Search for architectural indicators:**

```kotlin
// Look for these patterns:
- ViewModel classes (MVVM indicator)
- Presenter classes (MVP indicator)
- UseCase/Interactor classes (Clean Architecture indicator)
- Repository classes (Repository pattern)
- State classes with sealed classes (MVI indicator)
```

**Identify:**
- Primary architecture pattern in use
- Consistency of pattern application
- Layer separation (UI, Domain, Data)
- Dependency injection approach (Hilt, Dagger, Koin, manual)

#### 1.4 Dependency Inventory

**Analyze build files for dependencies:**

```
Categorize dependencies:
- Android Jetpack libraries
- Networking (Retrofit, OkHttp, Ktor)
- Database (Room, SQLDelight, Realm)
- Image loading (Coil, Glide, Picasso)
- DI framework
- Testing libraries
- Third-party services (Firebase, analytics, crash reporting)
```

**Evaluate:**
- [ ] Dependency count and complexity
- [ ] Version freshness (major versions behind)
- [ ] Duplicate functionality (multiple libraries for same purpose)
- [ ] Deprecated library usage

#### 1.5 Test Infrastructure

**Examine test directories:**

```
app/src/
├── test/          (unit tests)
├── androidTest/   (instrumented tests)
└── sharedTest/    (shared test utilities, if present)
```

**Evaluate:**
- [ ] Test presence and organization
- [ ] Test naming conventions
- [ ] Testing frameworks in use
- [ ] Mock/fake infrastructure
- [ ] Test coverage configuration

#### 1.6 Documentation State

**Check for documentation:**

```
Files to look for:
├── README.md
├── CONTRIBUTING.md
├── docs/
├── architecture.md or ADRs
└── Code comments and KDoc
```

**Evaluate:**
- [ ] README completeness (setup instructions, architecture overview)
- [ ] Architecture documentation
- [ ] API/code documentation
- [ ] Inline code comments quality

---

### Phase 2: Detailed Analysis

After the initial scan, perform deeper analysis in each area.

#### 2.1 Code Quality Deep Dive

**Kotlin Idiom Usage:**
- Search for anti-patterns: `!!` (force unwrap), `var` overuse, platform types
- Evaluate null safety patterns
- Check for proper use of scope functions (let, run, apply, also, with)
- Assess data class, sealed class, and enum usage
- Review extension function organization

**Coroutines and Concurrency:**
- Check coroutine scope usage (viewModelScope, lifecycleScope, GlobalScope)
- Evaluate dispatcher usage (Main, IO, Default)
- Look for structured concurrency violations
- Assess Flow usage patterns
- Check for callback-to-coroutine migration opportunities

**Resource Management:**
- Check for resource leaks (unclosed streams, cursors)
- Evaluate lifecycle-aware component usage
- Look for potential memory leaks (static context references, handler leaks)

#### 2.2 Architecture Quality Assessment

**Layer Boundaries:**
- Check if UI layer depends only on Domain/ViewModel
- Verify Data layer is properly abstracted
- Look for layer violations (UI directly accessing database)
- Assess model mapping between layers (DTO → Domain → UI models)

**Component Organization:**
- Evaluate ViewModel responsibilities (too much logic?)
- Check Repository pattern implementation
- Assess use case granularity (if Clean Architecture)
- Review navigation architecture

**State Management:**
- Identify state holder patterns (StateFlow, LiveData, Compose State)
- Evaluate UI state modeling
- Check for state consistency patterns
- Assess side effect handling

#### 2.3 Build System Health

**Gradle Configuration:**
- Check for build performance issues (unbounded dependencies, slow scripts)
- Evaluate build caching configuration
- Assess modularization opportunities
- Review ProGuard/R8 configuration

**CI/CD Readiness:**
- Check for CI configuration files (.github/workflows, .gitlab-ci.yml, etc.)
- Evaluate build reproducibility
- Assess signing configuration security

#### 2.4 Security Quick Scan

**Common Issues to Check:**
- Hardcoded secrets or API keys
- Insecure SharedPreferences usage
- Missing network security config
- Exported components without proper protection
- WebView security if applicable

---

### Phase 3: Findings Presentation

**CHECKPOINT 1:** Present the initial findings summary to the user.

Compile findings into the Health Report structure below and present to the user before proceeding.

```markdown
## Initial Scan Complete

I've completed the initial codebase scan. Here's what I found at a high level:

### Quick Stats
- **Codebase Size:** [X files, Y lines of Kotlin/Java]
- **Module Count:** [X modules]
- **Architecture Pattern:** [Identified pattern]
- **Kotlin Version:** [X.X.X]
- **Min SDK:** [XX] | **Target SDK:** [XX]

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
- **Module Organization:** [Single/Multi-module, assessment]
- **Build System:** [Groovy/Kotlin DSL, version catalog status]
- **Package Structure:** [By feature/layer, consistency]

---

### 2. Architecture Assessment

#### Identified Pattern: [MVVM/MVI/MVP/Clean/Hybrid]

#### Layer Analysis

**UI Layer:**
- Components: [Activities, Fragments, Composables]
- ViewModel usage: [Proper/Issues found]
- State management: [StateFlow/LiveData/Other]

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

#### Kotlin Usage

| Aspect | Status | Examples |
|--------|--------|----------|
| Null Safety | [Good/Needs Work] | [Specific patterns found] |
| Coroutines | [Good/Needs Work] | [Usage patterns] |
| Idioms | [Good/Needs Work] | [Examples] |

#### Code Smells Identified

| Smell | Count | Severity | Examples |
|-------|-------|----------|----------|
| Force unwrapping (!!) | [X] | High | [files] |
| God classes | [X] | Medium | [files] |
| Long methods | [X] | Medium | [files] |
| Dead code | [X] | Low | [files] |

#### Positive Patterns
- [Good pattern observed with example]
- [Good pattern observed with example]

---

### 4. Dependency Health

#### Version Analysis

| Category | Library | Current | Latest | Status |
|----------|---------|---------|--------|--------|
| Core | Kotlin | X.X.X | Y.Y.Y | [Up to date/Behind] |
| Android | AGP | X.X.X | Y.Y.Y | [Status] |
| Jetpack | [Library] | X.X.X | Y.Y.Y | [Status] |

#### Dependency Issues

| Issue | Library | Risk | Recommendation |
|-------|---------|------|----------------|
| [Outdated] | [Library] | [Security/Compatibility] | [Update/Replace] |
| [Deprecated] | [Library] | [Future breakage] | [Migration path] |

#### Dependency Optimization
- **Unused dependencies:** [List if found]
- **Duplicate functionality:** [List if found]
- **Bundle size concerns:** [Large dependencies]

---

### 5. Testing Assessment

#### Test Coverage Overview

| Test Type | Present | Count | Quality |
|-----------|---------|-------|---------|
| Unit Tests | [Yes/No] | [X] | [Assessment] |
| Integration Tests | [Yes/No] | [X] | [Assessment] |
| UI Tests | [Yes/No] | [X] | [Assessment] |

#### Testing Infrastructure
- **Frameworks:** [JUnit, MockK, Espresso, etc.]
- **Mocking approach:** [Mocks/Fakes/Mixed]
- **Test organization:** [Assessment]

#### Coverage Gaps
- [Critical untested area 1]
- [Critical untested area 2]
- [Critical untested area 3]

---

### 6. Documentation Assessment

#### Documentation Inventory

| Document | Present | Quality | Last Updated |
|----------|---------|---------|--------------|
| README | [Yes/No] | [1-10] | [Date/Unknown] |
| Architecture docs | [Yes/No] | [1-10] | [Date/Unknown] |
| API docs | [Yes/No] | [1-10] | [Date/Unknown] |
| Setup guide | [Yes/No] | [1-10] | [Date/Unknown] |

#### Code Documentation
- **KDoc coverage:** [Percentage estimate]
- **Comment quality:** [Assessment]
- **Self-documenting code:** [Assessment]

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

### Maintainability Risks
- [Risk with explanation]
- [Risk with explanation]

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
| [Architecture issues] | `android_architecture_review.md` | High |
| [Performance concerns] | `android_performance_audit.md` | Medium |
| [Outdated code] | `android_code_modernization.md` | Medium |
| [Memory issues] | `android_memory_leak_detection.md` | High |
| [Test gaps] | `android_test_coverage_analysis.md` | Medium |
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
- [ ] Run a more focused audit (architecture, performance, dependencies)

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

**User:** Please assess the health of this Android app. It's a fintech app about 3 years old, currently maintained by 2 developers.

**Agent:** I'll conduct a comprehensive health assessment. Let me start by exploring the codebase structure.

*[Agent performs initial scan]*

**Agent:**

## Initial Scan Complete

### Quick Stats
- **Codebase Size:** 245 Kotlin files, ~38,000 lines of code
- **Module Count:** Single module (app)
- **Architecture Pattern:** MVVM with Repository pattern
- **Kotlin Version:** 1.8.10 (current is 1.9.21)
- **Min SDK:** 24 | **Target SDK:** 33 (current is 34)

### First Impressions
The codebase shows a clear MVVM architecture with consistent patterns across features. The single-module structure is becoming a bottleneck given the app's size. Dependencies are moderately outdated, with some Jetpack libraries 2-3 major versions behind.

### Areas of Note
- **Strengths:** Consistent ViewModel patterns, good null safety practices, Room database well-structured
- **Concerns:** No version catalog (hardcoded versions), limited test coverage, several force unwraps in network layer

### Questions Before Deep Dive
1. I see Firebase Crashlytics is integrated - have there been recurring crash patterns you're aware of?
2. The app uses both LiveData and StateFlow - is this intentional during a migration, or unintended inconsistency?

**Would you like me to proceed with the detailed analysis, or focus on any specific area first?**

---

## Techniques Used

- **ST-01** (Clear Objective): Single-sentence objective with clear scope
- **ST-02** (Sequential Instructions): Phased discovery → analysis → report → action
- **RT-02** (Multi-Dimensional Analysis): Six-category assessment framework
- **RT-04** (Best Practice Review): Evaluation against Android best practices
- **RT-05** (Evidence-Based Reasoning): All findings include file:line references
- **ST-03** (Output Format Templates): Structured report with tables
- **OC-05** (Severity Classification): Critical/High/Medium/Low ratings
- **AG-02** (Skeptical Default Stance): Honest assessment over validation
- **AG-12** (Quantitative Metrics): Numerical scoring for categories
- **NE-01** (Single-Question Pacing): Context gathering one question at a time
- **NE-02** (Phased Workflow): Clear checkpoints between phases
- **NE-07** (Discussion Before Action): User approval gates before proceeding

---

## Related Prompts

- [android_architecture_review.md](android_architecture_review.md) - Deep dive into architecture patterns
- [android_performance_audit.md](android_performance_audit.md) - Performance bottleneck identification
- [android_technical_debt_assessment.md](android_technical_debt_assessment.md) - Detailed debt cataloging
- [android_dependency_audit.md](android_dependency_audit.md) - Focused dependency analysis
- [android_code_modernization.md](../improvement/android_code_modernization.md) - Systematic modernization
- [android_kotlin_best_practices.md](android_kotlin_best_practices.md) - Kotlin-specific review

---

## Customization Guide

### For Different Assessment Depths

**Quick Health Check (15-minute scan):**
- Focus on Phase 1 only
- Skip detailed code quality analysis
- Provide high-level summary without deep file references

**Due Diligence Assessment:**
- Extend security analysis
- Add compliance checking (GDPR, CCPA indicators)
- Include team/process assessment questions
- Emphasize risk quantification

**Pre-Migration Assessment:**
- Focus heavily on architecture and dependencies
- Assess Compose readiness if migration planned
- Identify migration blockers and risks

### For Different App Types

**Consumer Apps:**
- Emphasize UI/UX code quality
- Focus on performance and battery impact
- Check for analytics and crash reporting integration

**Enterprise Apps:**
- Emphasize security assessment
- Check for MDM/EMM compatibility
- Assess authentication and data protection

**SDK/Library Projects:**
- Focus on API surface analysis
- Check backward compatibility patterns
- Assess documentation completeness

### Adjusting Severity Thresholds

For **new projects** (< 6 months):
- Be stricter on architecture patterns
- More forgiving on test coverage
- Emphasize foundation quality

For **mature projects** (> 3 years):
- Focus on technical debt accumulation
- Emphasize modernization opportunities
- Check for deprecated API usage

For **legacy rescue** projects:
- Lower expectations for initial scores
- Focus on critical issues only
- Emphasize incremental improvement path
