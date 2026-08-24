---
title: "iOS Dependency Update"
category: mobile-development
description: "Safely update Swift Package Manager and CocoaPods dependencies with dependency graph analysis, semantic versioning assessment, breaking change identification, and regression testing plans."
techniques:
  - ST-01
  - ST-02
  - NE-02
difficulty: intermediate
tags:
  - ios
  - swift
  - dependencies
  - spm
  - cocoapods
  - maintenance
updated: "2026-03-20"
---

# iOS Dependency Update

**Objective:** Safely update SPM and CocoaPods dependencies by analyzing the dependency graph, assessing semantic versioning changes, identifying breaking changes, executing a phased update strategy (minor first, then major), and creating a regression testing plan.

**When to Use:** Use this prompt during scheduled maintenance windows, before major releases, when security advisories require updates, or when adopting new features from dependencies. Run quarterly at minimum to avoid large version jumps.

**Prompt Type:** Comprehensive (400+ lines)

---

## Context Gathering

Before updating dependencies, gather essential context:

1. **Dependency Manager:**
   - "Are you using SPM, CocoaPods, Carthage, or a mix?"
   - "Where is your dependency manifest (Package.swift, Podfile, Package.resolved)?"
   - "Do you pin exact versions or use version ranges?"

2. **Current State:**
   - "When was the last dependency update?"
   - "Are there known vulnerabilities in current dependency versions?"
   - "How many direct vs transitive dependencies do you have?"

3. **Risk Tolerance:**
   - "Is this a pre-release or post-release update cycle?"
   - "Are there dependencies that are known to introduce breaking changes?"
   - "What is your test coverage for code that uses external dependencies?"

4. **CI/CD:**
   - "Does your CI pipeline cache resolved dependencies?"
   - "Are there automated tests that exercise dependency integrations?"
   - "Can you run the full test suite before merging updates?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before updating ANY dependency, you MUST:**

1. **Audit the current dependency graph** - Know what you have before changing it. Run `swift package show-dependencies` or `pod outdated`.
2. **Read changelogs for every update** - Especially for major version bumps. Check release notes, migration guides, and breaking changes.
3. **Update in isolation** - Update one dependency (or one group of related dependencies) at a time. Never bulk-update everything simultaneously.
4. **Run full test suite after each update** - Compile, test, and ideally run the app before proceeding to the next update.
5. **Commit each update separately** - Enables clean git bisect if regressions appear later.

**A dependency update without testing is a deployment risk. Treat every update as a potential regression.**

### False-Positive Prevention

- ❌ Do NOT update all dependencies at once in a single commit
- ❌ Do NOT ignore deprecation warnings introduced by updates
- ❌ Do NOT skip reading changelogs for major version bumps
- ❌ Do NOT assume minor/patch updates are always safe
- ❌ Do NOT merge dependency updates without CI passing
- ❌ Do NOT update dependencies that your pinned Swift version does not support
- ✅ DO check minimum deployment target compatibility for each update
- ✅ DO verify binary size impact for significant updates
- ✅ DO create a rollback plan (keep the pre-update Package.resolved / Podfile.lock)
- ✅ DO update your lock file and commit it alongside the manifest change
- ✅ DO check for transitive dependency conflicts

---

### Phase 1: Dependency Audit

#### 1.1 Inventory Current Dependencies

**For SPM:**
```bash
# Show full dependency tree
swift package show-dependencies --format json > dependency_tree.json

# List resolved versions
cat Package.resolved | python3 -m json.tool

# Check for outdated packages (requires swift-package-manager-outdated or manual check)
swift package update --dry-run 2>&1
```

**For CocoaPods:**
```bash
# List outdated pods
pod outdated

# Show dependency tree
pod dependencies

# Check for vulnerabilities
bundle exec pod audit
```

#### 1.2 Dependency Graph Analysis

Create a dependency inventory table:

```markdown
## Dependency Inventory

| Package | Current | Latest | Type | Bump | Risk | Notes |
|---------|---------|--------|------|------|------|-------|
| Alamofire | 5.8.1 | 5.9.0 | Direct | Minor | Low | Networking layer |
| SwiftLint | 0.54.0 | 0.55.0 | Dev | Minor | Low | Build tool only |
| Firebase | 10.20.0 | 11.2.0 | Direct | Major | High | Analytics, Crashlytics |
| Kingfisher | 7.10.0 | 8.0.0 | Direct | Major | High | Image caching throughout app |
| SnapKit | 5.6.0 | 5.7.1 | Direct | Patch | Low | Layout constraints |
| KeychainAccess | 4.2.2 | 4.2.2 | Direct | None | - | Up to date |

### Transitive Dependencies
| Package | Pulled By | Current | Latest |
|---------|-----------|---------|--------|
| SwiftProtobuf | Firebase | 1.25.0 | 1.27.0 |
| GoogleUtilities | Firebase | 7.12.0 | 8.0.0 |
```

#### 1.3 Risk Assessment

Classify each dependency update:

| Risk Level | Criteria | Strategy |
|------------|----------|----------|
| **Low** | Patch update, dev-only dependency, no API changes | Batch together, single PR |
| **Medium** | Minor update, new APIs but no removals, widely used dep | Individual PR, targeted testing |
| **High** | Major update, API breaking changes, core dependency | Dedicated branch, full regression, migration guide review |
| **Critical** | Security vulnerability fix | Hotfix process, expedited review |

---

### Phase 2: Update Strategy

**CHECKPOINT 1:** Confirm dependency audit is complete before starting updates.

```markdown
## Update Plan

### Batch 1: Low-Risk (Patch + Dev Dependencies)
| Package | From | To | Risk |
|---------|------|----|------|
| SnapKit | 5.6.0 | 5.7.1 | Low |
| SwiftLint | 0.54.0 | 0.55.0 | Low |

### Batch 2: Medium-Risk (Minor Updates)
| Package | From | To | Risk |
|---------|------|----|------|
| Alamofire | 5.8.1 | 5.9.0 | Medium |

### Batch 3: High-Risk (Major Updates) - Individual PRs
| Package | From | To | Risk | Migration Guide |
|---------|------|----|------|-----------------|
| Firebase | 10.20.0 | 11.2.0 | High | [link] |
| Kingfisher | 7.10.0 | 8.0.0 | High | [link] |

**Proceed with Batch 1?**
```

#### 2.1 SPM Update Process

```bash
# Step 1: Create a branch for this update batch
git checkout -b chore/dependency-updates-2026-03

# Step 2: Back up the current lock file
cp Package.resolved Package.resolved.backup

# Step 3: Update a specific package
# Edit Package.swift to update the version requirement
# Then resolve
swift package resolve

# Step 4: Build and test
swift build
swift test

# Step 5: Commit this individual update
git add Package.swift Package.resolved
git commit -m "chore: update SnapKit from 5.6.0 to 5.7.1"
```

**Package.swift version specification patterns:**

```swift
dependencies: [
    // Exact version (most restrictive, safest)
    .package(url: "https://github.com/...", exact: "5.7.1"),

    // Up to next minor (allows patches, recommended for stability)
    .package(url: "https://github.com/...", from: "5.7.0"),

    // Version range (allows controlled flexibility)
    .package(url: "https://github.com/...", "5.7.0"..<"6.0.0"),

    // Branch-based (for pre-release testing only)
    .package(url: "https://github.com/...", branch: "main"),
]
```

#### 2.2 CocoaPods Update Process

```bash
# Step 1: Back up current lock file
cp Podfile.lock Podfile.lock.backup

# Step 2: Update a specific pod
pod update Alamofire --no-repo-update

# Step 3: Review what changed
diff Podfile.lock.backup Podfile.lock

# Step 4: Build and test
xcodebuild -workspace MyApp.xcworkspace -scheme MyApp -sdk iphonesimulator build test

# Step 5: Commit
git add Podfile Podfile.lock
git commit -m "chore: update Alamofire from 5.8.1 to 5.9.0"
```

#### 2.3 Major Version Update Checklist

For each major version update, follow this checklist:

```markdown
### Major Update: [Package Name] [Old] -> [New]

#### Pre-Update
- [ ] Read full changelog / release notes
- [ ] Read migration guide (if available)
- [ ] Identify all files that import this dependency
- [ ] List all APIs used from this dependency
- [ ] Check minimum iOS deployment target compatibility
- [ ] Check Swift version compatibility

#### During Update
- [ ] Update version in manifest
- [ ] Fix all compilation errors
- [ ] Address all deprecation warnings
- [ ] Update any wrapper/abstraction layers
- [ ] Verify no behavior changes in existing functionality

#### Post-Update
- [ ] All unit tests pass
- [ ] All UI tests pass
- [ ] Manual smoke test of affected features
- [ ] Binary size delta acceptable (< 5% growth)
- [ ] Launch time not regressed
- [ ] Memory usage not regressed
```

---

### Phase 3: Breaking Change Identification

#### 3.1 Finding Affected Code

```bash
# Find all files that import the dependency
grep -rn "import Alamofire" --include="*.swift" Sources/

# Find usage of specific deprecated/removed APIs
grep -rn "AF\.request" --include="*.swift" Sources/
grep -rn "responseJSON" --include="*.swift" Sources/  # Removed in Alamofire 5.x

# Count total usage
grep -c "import Kingfisher" --include="*.swift" -r Sources/
```

#### 3.2 Common Breaking Change Patterns

| Pattern | Detection | Resolution |
|---------|-----------|------------|
| Renamed API | Compiler error: "has been renamed to" | Follow compiler fix-it |
| Removed API | Compiler error: "is unavailable" | Check migration guide for replacement |
| Changed return type | Compiler error: type mismatch | Update calling code |
| New required parameter | Compiler error: missing argument | Add parameter with sensible default |
| Protocol change | Compiler error: does not conform | Add new required methods |
| Concurrency annotations | Warning: "sending value... risks data race" | Add `@Sendable`, `sending`, or actor isolation |

#### 3.3 Abstraction Layer Strategy

For high-risk dependencies, maintain an abstraction layer:

```swift
// File: Services/Networking/NetworkClient.swift
// Abstracts Alamofire so updates only affect this file

protocol NetworkClientProtocol {
    func request<T: Decodable>(_ endpoint: Endpoint) async throws -> T
}

final class NetworkClient: NetworkClientProtocol {
    func request<T: Decodable>(_ endpoint: Endpoint) async throws -> T {
        // Only Alamofire usage is here
        let response = await AF.request(
            endpoint.url,
            method: endpoint.method,
            parameters: endpoint.parameters,
            headers: endpoint.headers
        )
        .validate()
        .serializingDecodable(T.self)
        .response

        guard let value = response.value else {
            throw response.error ?? NetworkError.unknown
        }
        return value
    }
}
```

---

### Phase 4: Regression Testing Plan

**CHECKPOINT 2:** Confirm all updates applied and compilable before regression testing.

```markdown
## Update Status

| Package | Status | Compiles | Tests Pass |
|---------|--------|----------|------------|
| SnapKit | Updated | Yes | Yes |
| SwiftLint | Updated | Yes | N/A (dev tool) |
| Alamofire | Updated | Yes | Yes |
| Firebase | Updated | Yes | 3 failures |
| Kingfisher | Pending | - | - |

**Issues to resolve before proceeding:**
- Firebase: Analytics event format changed, update 3 test assertions
```

#### 4.1 Targeted Regression Tests

For each updated dependency, test the features that use it:

```markdown
## Regression Test Matrix

| Dependency | Features to Test | Test Type |
|------------|-----------------|-----------|
| Alamofire | Login, Feed loading, Image upload, Offline mode | Unit + Manual |
| Firebase | Analytics events, Crash reporting, Remote Config | Unit + Verify in console |
| Kingfisher | Image loading in feed, Profile avatars, Cache clearing | Manual + Memory profiling |
| SnapKit | All screens with programmatic layout | Visual regression |
```

#### 4.2 Automated Verification Script

```bash
#!/bin/bash
# File: Scripts/verify_dependency_update.sh

set -euo pipefail

echo "=== Dependency Update Verification ==="

echo "1. Clean build..."
xcodebuild clean -workspace MyApp.xcworkspace -scheme MyApp -quiet

echo "2. Build for simulator..."
xcodebuild build \
    -workspace MyApp.xcworkspace \
    -scheme MyApp \
    -sdk iphonesimulator \
    -destination 'platform=iOS Simulator,name=iPhone 16' \
    -quiet

echo "3. Run unit tests..."
xcodebuild test \
    -workspace MyApp.xcworkspace \
    -scheme MyApp \
    -sdk iphonesimulator \
    -destination 'platform=iOS Simulator,name=iPhone 16' \
    -resultBundlePath TestResults.xcresult \
    -quiet

echo "4. Check binary size..."
APP_PATH=$(find ~/Library/Developer/Xcode/DerivedData -name "MyApp.app" -path "*/Build/Products/Debug-iphonesimulator/*" | head -1)
SIZE=$(du -sm "$APP_PATH" | cut -f1)
echo "App size: ${SIZE}MB"

echo "5. Check for new warnings..."
xcodebuild build \
    -workspace MyApp.xcworkspace \
    -scheme MyApp \
    -sdk iphonesimulator \
    -destination 'platform=iOS Simulator,name=iPhone 16' \
    2>&1 | grep "warning:" | sort -u > new_warnings.txt
WARN_COUNT=$(wc -l < new_warnings.txt)
echo "Warnings: ${WARN_COUNT}"

echo "=== Verification Complete ==="
```

---

## Expected Output

### Dependency Update Report

```markdown
# Dependency Update Report - [Date]

## Summary
- Dependencies audited: [N]
- Updates available: [N]
- Updates applied: [N]
- Breaking changes resolved: [N]
- New warnings introduced: [N]

## Updates Applied
| Package | From | To | Bump | Breaking Changes | Binary Size Delta |
|---------|------|----|------|------------------|-------------------|
| [name] | [old] | [new] | [patch/minor/major] | [None/Yes: details] | [+/- KB] |

## Deferred Updates (with justification)
| Package | Available | Reason for Deferral | Target Date |
|---------|-----------|---------------------|-------------|
| [name] | [version] | [reason] | [date] |

## Regression Test Results
- Unit tests: [PASS/FAIL - details]
- UI tests: [PASS/FAIL - details]
- Manual smoke test: [PASS/FAIL - details]
- Binary size: [X MB] (delta: [+/- Y KB])
- Launch time: [X.Xs] (delta: [+/- Y ms])

## Follow-Up Actions
- [ ] Monitor crash-free rate post-release
- [ ] Schedule next dependency audit: [date]
- [ ] File ticket for deferred major updates
```

### Implementation Checklist

- [ ] Dependency graph audited and documented
- [ ] Semantic versioning changes assessed for each dependency
- [ ] Breaking changes identified and cataloged
- [ ] Low-risk updates applied and tested (batch)
- [ ] Medium-risk updates applied and tested (individual)
- [ ] High-risk updates applied with migration guide (individual PRs)
- [ ] Lock file committed alongside each update
- [ ] Full test suite passes after all updates
- [ ] Binary size and performance impact measured
- [ ] Rollback plan documented (backup lock file)

---

## Techniques Used

- **ST-01** (Clear Objective): Focused objective on safe dependency updates
- **ST-02** (Sequential Instructions): Phased approach from audit to regression testing
- **NE-02** (Phased Workflow): Clear phases with checkpoints and batched execution

---

## Related Prompts

- [ios_version_upgrade.md](ios_version_upgrade.md) - Upgrade iOS deployment target (often paired with dependency updates)
- [ios_swift_version_migration.md](ios_swift_version_migration.md) - Migrate to new Swift version (may require dependency updates)
- [ios_deprecation_audit.md](ios_deprecation_audit.md) - Audit deprecated APIs including from dependencies
- [ios_xcode_build_optimization.md](ios_xcode_build_optimization.md) - Optimize builds after dependency changes
