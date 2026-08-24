---
title: "iOS Modularization Strategy"
category: mobile-development
description: "Plan phased modularization of a monolithic iOS codebase into Swift Package Manager modules with risk mitigation, build time improvements, and team workflow preservation."
techniques:
  - ST-01
  - ST-02
  - NE-02
difficulty: advanced
tags:
  - ios
  - swift
  - modularization
  - refactoring
updated: "2026-03-20"
---

# iOS Modularization Strategy

**Objective:** Plan and execute a phased modularization of a monolithic iOS codebase into SPM modules, preserving stability, improving build times, enabling team autonomy, and establishing sustainable module boundaries without disrupting ongoing feature development.

**When to Use:** Use when an existing monolithic iOS app has grown beyond comfortable single-target development -- typically signaled by slow build times (>60s incremental), merge conflicts, difficulty onboarding developers, or the need for multiple teams to work independently. Do NOT use for greenfield projects (use ios_module_design.md instead).

**Prompt Type:** Comprehensive (400+ lines)

---

## Context Gathering

Before planning modularization, gather essential context:

1. **Current State:**
   - "What is the current clean build time? Incremental build time?"
   - "How many Swift files and lines of code?"
   - "What dependency manager is used (CocoaPods, SPM, Carthage, mixed)?"
   - "Are there existing frameworks or local packages?"

2. **Pain Points:**
   - "What specific problems is modularization meant to solve?"
   - "Where do merge conflicts most frequently occur?"
   - "Which parts of the codebase change most often?"

3. **Team:**
   - "How many developers? How many concurrent feature branches?"
   - "Is the team familiar with SPM and multi-module development?"
   - "Can you allocate dedicated time for modularization or must it happen alongside feature work?"

4. **Architecture:**
   - "What architecture pattern is used (MVC, MVVM, TCA, mixed)?"
   - "Is the codebase SwiftUI, UIKit, or hybrid?"
   - "Are there well-defined feature boundaries or is everything interleaved?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before executing ANY modularization step, you MUST:**

1. **Measure baseline metrics** - Record build times, file counts, and dependency graph before starting.
2. **Identify the dependency root** - Find the most-depended-upon code and extract it first.
3. **Ensure CI passes after each extraction** - Never batch multiple module extractions into one PR.
4. **Preserve git history** - Use `git mv` for file moves to maintain blame history.
5. **Run full test suite after each phase** - No regression is acceptable.

### False-Positive Prevention

- ❌ Do NOT attempt to modularize everything at once ("big bang" approach)
- ❌ Do NOT create modules with circular dependencies during extraction
- ❌ Do NOT break internal access control without understanding why it was internal
- ❌ Do NOT move files without updating all import statements and module maps
- ❌ Do NOT ignore CocoaPods/Carthage migration -- plan it explicitly
- ❌ Do NOT modularize code that changes weekly (extract stable code first)
- ✅ DO extract bottom-up (foundations first, features last)
- ✅ DO ship each module extraction independently to production
- ✅ DO measure build time improvement after each extraction
- ✅ DO keep a rollback plan for each phase

---

### Phase 1: Codebase Analysis

#### 1.1 Dependency Graph Discovery

```bash
# Generate import graph from Swift files
find . -name "*.swift" -exec grep -l "^import " {} \; | \
  xargs grep "^import " | sort | uniq -c | sort -rn

# Identify most-imported internal types
# (Types referenced across the most files are extraction candidates)
```

```markdown
## Dependency Hotspots
| Type/File | Referenced By (# files) | Current Location | Extraction Priority |
|-----------|------------------------|------------------|-------------------|
| APIClient | 45 | Sources/Networking/ | P0 - Extract first |
| User | 38 | Sources/Models/ | P0 |
| DesignTokens | 32 | Sources/UI/ | P0 |
| AppCoordinator | 28 | Sources/Navigation/ | P2 - Extract late |
| FeedService | 12 | Sources/Feed/ | P1 |
```

#### 1.2 Build Time Analysis

```markdown
## Baseline Metrics
| Metric | Value | Target |
|--------|-------|--------|
| Clean build | _s | Reduce 30%+ |
| Incremental build (1 file) | _s | < 10s |
| Swift file count | _ | N/A |
| Lines of code | _ | N/A |
| CocoaPods dependencies | _ | Migrate to SPM |
| Test suite duration | _s | Maintain or improve |
```

#### 1.3 Code Coupling Assessment

```markdown
## Coupling Zones
| Zone | Files | Coupling Level | Risk |
|------|-------|---------------|------|
| Networking + Models | _ | Tight | Medium - extract together |
| UI Components | _ | Loose | Low - clean extraction |
| Feature A ↔ Feature B | _ | Tight | High - requires interface extraction |
| AppDelegate/SceneDelegate | _ | Tight to everything | High - extract last |
```

---

### Phase 2: Extraction Plan

**CHECKPOINT 1:** Confirm baseline metrics and hotspots before planning extraction.

```markdown
## Analysis Summary
- Total files: _
- Dependency hotspots identified: _
- Clean build time baseline: _s
- Coupling zones: _ high-risk, _ low-risk

**Proceed with extraction plan?**
```

#### 2.1 Extraction Order (Bottom-Up)

```markdown
## Phase Order

### Phase 2a: Foundation Layer (Week 1-2)
Extract zero-dependency utilities first:
1. **FoundationExt** - Extensions on Foundation types, helpers
   - Risk: Low (no dependencies)
   - Files: ~15-20
   - Build impact: Minimal alone, enables all subsequent phases

2. **Core/Networking** - APIClient, endpoints, response models
   - Risk: Medium (many dependents)
   - Files: ~20-30
   - Build impact: Significant (unlocks parallel compilation)

3. **Core/Persistence** - SwiftData/CoreData stack, migration logic
   - Risk: Medium (data integrity critical)
   - Files: ~10-15
   - Build impact: Moderate

### Phase 2b: Domain Layer (Week 3-4)
4. **SharedUI** - Design system, reusable components, tokens
   - Risk: Low-Medium (many consumers but stable API)
   - Files: ~30-40
   - Build impact: Significant

5. **DomainModels** - Shared models, protocols, interfaces
   - Risk: Medium (must define public/internal boundaries)
   - Files: ~15-20

### Phase 2c: Feature Layer (Week 5-8)
6. **Feature modules** - One per feature, starting with least-coupled
   - Extract in order of least dependencies first
   - Each feature: 1-2 week cycle
```

#### 2.2 Per-Module Extraction Checklist

```markdown
## Module Extraction: [ModuleName]

### Pre-Extraction
- [ ] Identify all files to extract
- [ ] Map all internal dependencies
- [ ] Identify access control changes needed (internal → public)
- [ ] Create the SPM target in Package.swift
- [ ] Create test target

### Extraction
- [ ] `git mv` files to new module directory
- [ ] Update imports in moved files
- [ ] Change access control: internal → public for module API
- [ ] Update imports in remaining monolith files
- [ ] Fix all compilation errors
- [ ] Run full test suite

### Post-Extraction
- [ ] Measure incremental build time improvement
- [ ] Verify CI passes
- [ ] Merge to main
- [ ] Monitor for regressions for 2-3 days before next extraction
```

---

### Phase 3: Access Control Strategy

#### 3.1 Visibility Rules

```swift
// BEFORE: Everything is internal by default in a single target
class APIClient {
    func fetch<T: Decodable>(_ endpoint: Endpoint) async throws -> T { ... }
}

struct User {
    let id: String
    let name: String
}

// AFTER: Explicit public API for module boundary
public final class APIClient: Sendable {
    public func fetch<T: Decodable & Sendable>(
        _ endpoint: Endpoint
    ) async throws -> T { ... }

    // Keep implementation details internal
    internal func refreshToken() async throws { ... }
}

// Use package access level for cross-module-but-not-public APIs
package struct UserDTO {
    package let id: String
    package let name: String
}
```

#### 3.2 Common Access Control Pitfalls

| Pitfall | Solution |
|---------|---------|
| Making everything `public` | Only expose the module's intended API surface |
| Forgetting `public init` on public structs | Structs need explicit public initializers |
| Protocol conformance across modules | Conforming type OR protocol must be in same module, or use `@retroactive` |
| `@Observable` across modules | Class must be `public`, properties need `public` getters |
| Enum cases are always public if enum is public | Enums are safe to expose |

---

### Phase 4: CocoaPods/Carthage Migration

#### 4.1 Migration Strategy

```markdown
| Dependency | Current | Migration Target | Effort |
|-----------|---------|-----------------|--------|
| Alamofire | CocoaPod | SPM | Low (SPM supported) |
| Kingfisher | CocoaPod | SPM | Low (SPM supported) |
| Firebase | CocoaPod | SPM | Medium (complex podspec) |
| Custom internal pod | CocoaPod | Local SPM package | Medium |
| No SPM support lib | CocoaPod | Keep as Pod OR fork | High |
```

#### 4.2 Hybrid Period Management

```ruby
# Podfile during migration -- CocoaPods and SPM coexist
# Some deps via CocoaPods, others via SPM
# This is a valid intermediate state

target 'MyApp' do
  # Keep these until SPM equivalents are verified
  pod 'Firebase/Analytics', '~> 10.0'

  # These have been migrated to SPM -- REMOVE after verification
  # pod 'Alamofire' -- NOW IN Package.swift
end
```

---

### Phase 5: Validation and Measurement

**CHECKPOINT 2:** Review extraction progress and metrics.

```markdown
## Modularization Progress

| Module | Status | Build Impact | Issues |
|--------|--------|-------------|--------|
| FoundationExt | Extracted | -2s clean | None |
| Core/Networking | Extracted | -8s clean | 3 access control fixes |
| SharedUI | In Progress | TBD | |
| FeatureAuth | Planned | TBD | |

## Build Time Trend
| Date | Clean Build | Incremental | Modules Extracted |
|------|------------|-------------|------------------|
| Baseline | _s | _s | 0 |
| Week 2 | _s | _s | 2 |
| Week 4 | _s | _s | 4 |
```

#### 5.1 Success Criteria

```markdown
| Metric | Baseline | Target | Achieved |
|--------|----------|--------|----------|
| Clean build time | _s | -30% | |
| Incremental build time | _s | < 10s | |
| Merge conflicts/week | _ | -50% | |
| Module count | 1 | 6-10 | |
| Test suite passing | 100% | 100% | |
| Zero circular dependencies | N/A | Yes | |
```

---

## Expected Output

```
Modularization Plan
├── Codebase Analysis
│   ├── Dependency hotspots
│   ├── Build time baseline
│   └── Coupling assessment
├── Extraction Plan (ordered phases)
│   ├── Foundation layer (weeks 1-2)
│   ├── Domain layer (weeks 3-4)
│   └── Feature layer (weeks 5-8)
├── Per-Module Extraction Checklist
├── Access Control Migration Guide
├── CocoaPods/Carthage Migration Plan
└── Validation Metrics Dashboard
```

---

## Example Interaction

**User:** "Our app has 400 Swift files, 90-second clean builds, and we keep getting merge conflicts in the networking and model layers. Team of 5 developers, using MVVM with CocoaPods."

**Assistant:**

**Priority extraction order:**
1. **FoundationExt** (week 1) - ~20 utility files. Zero risk. Establishes the pattern.
2. **Core/Networking** (week 1-2) - APIClient + response models. This is your top merge conflict zone -- extracting it isolates the most contentious code. Expected: -15s clean build.
3. **SharedModels** (week 2) - User, shared DTOs. Second highest conflict zone.
4. **SharedUI** (week 3) - Design system components.
5. **Feature modules** (weeks 4-8) - One feature per week, starting with the most isolated.

**CocoaPods migration:** Start by adding SPM alongside CocoaPods. Migrate Alamofire and Kingfisher to SPM first (both support it). Keep Firebase as a Pod until all features are extracted (Firebase SPM integration is smoother in a single target).

**Build time projection:** With 5 modules extracted, expect clean build to drop from 90s to ~55-60s (parallel compilation). Incremental builds for isolated module changes: <8s.

---

## Techniques Used

- **ST-01** (Clear Objective): Phased modularization with measurable build time goals
- **ST-02** (Sequential Instructions): Ordered extraction phases from foundation to features
- **NE-02** (Phased Workflow): Each phase ships independently with validation checkpoints

---

## Related Prompts

- [ios_module_design.md](ios_module_design.md) - Design module architecture for greenfield projects
- [ios_architecture_selection.md](ios_architecture_selection.md) - Architecture patterns that support modularization
- [ios_project_scaffold.md](ios_project_scaffold.md) - Scaffold the target module structure

---

## Customization Guide

### For Very Large Codebases (1000+ files)
Add a "strangler fig" approach: create module boundaries but keep files in place initially. Use `@_exported import` to maintain backward compatibility, then move files gradually.

### For Teams with No Modularization Experience
Start with a single extraction (FoundationExt) as a learning exercise. Run a team retrospective after the first module before planning subsequent phases.

### For Apps with Heavy Objective-C Interop
Add bridging header migration strategy. Objective-C files cannot live in SPM targets -- plan mixed-language module boundaries carefully or keep Obj-C in the main target.
