---
title: "iOS Version Upgrade"
category: mobile-development
description: "Upgrade to a new iOS deployment target with availability check audits, deprecated API replacement, new API adoption, Info.plist changes, entitlements updates, and minimum version impact analysis."
techniques:
  - ST-01
  - ST-02
  - NE-02
difficulty: intermediate
tags:
  - ios
  - swift
  - version-upgrade
  - deployment-target
updated: "2026-03-20"
---

# iOS Version Upgrade

**Objective:** Upgrade your app's minimum iOS deployment target by auditing availability checks, replacing deprecated APIs, adopting valuable new APIs, updating Info.plist and entitlements, and analyzing the impact on your user base.

**When to Use:** Use this prompt when raising your minimum deployment target (e.g., iOS 16 to iOS 17), typically timed with Apple's annual iOS release cycle. Best executed after the new iOS version reaches 80%+ adoption among your users, usually 3-6 months after release.

**Prompt Type:** Comprehensive (400+ lines)

---

## Context Gathering

Before upgrading, gather essential context:

1. **Current State:**
   - "What is your current minimum deployment target?"
   - "What is your target new minimum deployment target?"
   - "What percentage of your users are on each iOS version (check App Store Connect > Metrics)?"

2. **Codebase:**
   - "How many `if #available` / `@available` checks exist in the codebase?"
   - "Are there polyfills or backports for newer APIs?"
   - "What frameworks do you use that have version-specific features?"

3. **Dependencies:**
   - "Do all your dependencies support the new minimum target?"
   - "Are there dependencies that require the new minimum to unlock features?"

4. **Timeline:**
   - "When is your next major release?"
   - "Do you need to coordinate with backend API versioning?"
   - "Are there marketing or business requirements tied to this upgrade?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before changing ANY deployment target, you MUST:**

1. **Analyze user adoption data** - Never drop support for iOS versions with significant user share (>5%) without business approval.
2. **Audit all availability checks** - Every `if #available` and `@available` in the codebase must be evaluated for removal or retention.
3. **Check all dependencies** - Verify every SPM/CocoaPods/Carthage dependency supports the new minimum target.
4. **Test on the new minimum version** - Run the app on a simulator running the exact new minimum iOS version.
5. **Update all project targets** - Deployment target must be consistent across the main app, extensions, frameworks, and test targets.

**Raising the deployment target without removing availability checks creates dead code. Lowering it accidentally breaks compilation.**

### False-Positive Prevention

- ❌ Do NOT remove availability checks for APIs that require a version HIGHER than your new minimum
- ❌ Do NOT assume all users have updated - check actual adoption data
- ❌ Do NOT forget to update extension targets (widgets, watch, intents)
- ❌ Do NOT remove availability checks in shared frameworks that support other targets
- ❌ Do NOT ignore deprecation warnings - they become errors in future SDK versions
- ✅ DO update both the Xcode project deployment target AND Package.swift platform requirements
- ✅ DO communicate the minimum version change in release notes
- ✅ DO verify asset catalog compatibility (SF Symbols versions, color sets)
- ✅ DO test on the oldest supported iOS version after the upgrade
- ✅ DO update CI/CD pipeline simulator versions

---

### Phase 1: Impact Analysis

#### 1.1 User Adoption Assessment

Pull data from App Store Connect:

```markdown
## iOS Version Adoption (from App Store Connect)

| iOS Version | User Percentage | Cumulative | Impact if Dropped |
|-------------|----------------|------------|-------------------|
| iOS 18.x | 42% | 42% | - |
| iOS 17.x | 38% | 80% | - |
| iOS 16.x | 12% | 92% | 0% (keeping) |
| iOS 15.x | 5% | 97% | 5% users affected |
| iOS 14.x | 2% | 99% | 7% users affected |
| < iOS 14 | 1% | 100% | 8% users affected |

### Recommendation
- **Current minimum:** iOS 15
- **Proposed minimum:** iOS 17
- **Users affected:** 8% (iOS 15 and below)
- **Decision:** [Proceed / Defer / Modified target]
```

#### 1.2 Dependency Compatibility Check

```markdown
## Dependency Minimum iOS Requirements

| Dependency | Current Min | Latest Version Min | Compatible? |
|------------|-------------|-------------------|-------------|
| Alamofire 5.9 | iOS 13 | iOS 13 | Yes |
| Firebase 11.x | iOS 15 | iOS 15 | Yes |
| Kingfisher 8.0 | iOS 16 | iOS 16 | Yes |
| SDWebImage 5.x | iOS 13 | iOS 13 | Yes |
| Lottie 4.x | iOS 14 | iOS 14 | Yes |

All dependencies compatible with iOS 17 minimum: **YES / NO**
```

#### 1.3 Available API Improvements

When raising the deployment target, catalog APIs you can now use unconditionally:

```markdown
## APIs Unlocked by iOS 17 Minimum

### SwiftUI
| API | Replaces | Benefit |
|-----|----------|---------|
| `@Observable` macro | `ObservableObject` + `@Published` | Simpler state management, better performance |
| `.scrollPosition(id:)` | Manual scroll tracking | Native scroll position tracking |
| `#Preview` macro | `PreviewProvider` protocol | Cleaner preview syntax |
| `.containerRelativeFrame()` | GeometryReader hacks | Simpler responsive layouts |
| `ContentUnavailableView` | Custom empty states | Standard empty state pattern |
| `.sensoryFeedback()` | UIImpactFeedbackGenerator | Declarative haptics |

### UIKit
| API | Replaces | Benefit |
|-----|----------|---------|
| `UIContentUnavailableConfiguration` | Custom empty state views | Standard empty state |
| Animated SF Symbols | Custom animations | System-consistent animations |
| `UICollectionView` improvements | Manual diffing | Better performance |

### Foundation
| API | Replaces | Benefit |
|-----|----------|---------|
| Swift Regex | NSRegularExpression | Type-safe regex |
| Predicate macro | NSPredicate | Type-safe predicates for SwiftData |
```

---

### Phase 2: Availability Check Audit

**CHECKPOINT 1:** Confirm impact analysis is complete and upgrade is approved before modifying code.

```markdown
## Upgrade Decision

| Factor | Status |
|--------|--------|
| User adoption data reviewed | [Yes/No] |
| Affected user percentage | [X%] |
| Business approval obtained | [Yes/No] |
| Dependencies compatible | [Yes/No] |
| New minimum target | iOS [X] |

**Proceed with code changes?**
```

#### 2.1 Find All Availability Checks

```bash
# Find all #available checks
grep -rn "#available" --include="*.swift" Sources/ | wc -l
grep -rn "#available" --include="*.swift" Sources/

# Find all @available annotations
grep -rn "@available" --include="*.swift" Sources/

# Find availability checks for specific versions
grep -rn "#available(iOS 1[5-6]" --include="*.swift" Sources/
grep -rn "@available(iOS 1[5-6]" --include="*.swift" Sources/

# Find unavailable annotations
grep -rn "@available(\*, unavailable" --include="*.swift" Sources/
```

#### 2.2 Classify Availability Checks

For each availability check, determine the action:

| Check | New Min | Action |
|-------|---------|--------|
| `if #available(iOS 15, *)` | iOS 17 | **Remove** - always true |
| `if #available(iOS 16, *)` | iOS 17 | **Remove** - always true |
| `if #available(iOS 17, *)` | iOS 17 | **Remove** - always true |
| `if #available(iOS 18, *)` | iOS 17 | **Keep** - still conditional |
| `@available(iOS 16, *)` on type | iOS 17 | **Remove** annotation |
| `@available(iOS 18, *)` on type | iOS 17 | **Keep** annotation |

#### 2.3 Removing Availability Checks

```swift
// BEFORE: Conditional availability (minimum was iOS 15)
func showContent() {
    if #available(iOS 17, *) {
        // Modern path
        let config = UIContentUnavailableConfiguration.empty()
        contentUnavailableConfiguration = config
    } else {
        // Fallback path
        emptyStateView.isHidden = false
        emptyStateLabel.text = "No content"
    }
}

// AFTER: Unconditional usage (minimum is now iOS 17)
func showContent() {
    let config = UIContentUnavailableConfiguration.empty()
    contentUnavailableConfiguration = config
}
// DELETE: emptyStateView, emptyStateLabel, related constraints (dead code)
```

```swift
// BEFORE: @available annotation
@available(iOS 16, *)
struct ModernChartView: View {
    var body: some View {
        Chart { ... }
    }
}

// AFTER: Remove annotation (iOS 17 minimum includes iOS 16 APIs)
struct ModernChartView: View {
    var body: some View {
        Chart { ... }
    }
}
```

---

### Phase 3: Project Configuration

#### 3.1 Update Xcode Project Settings

Update these locations:

```markdown
## Deployment Target Updates

### Xcode Project
- [ ] Project > General > Minimum Deployments > iOS [NEW_VERSION]
- [ ] Each target > General > Minimum Deployments > iOS [NEW_VERSION]
  - [ ] Main app target
  - [ ] Widget extension
  - [ ] Notification service extension
  - [ ] Notification content extension
  - [ ] Share extension
  - [ ] Watch app (if applicable)
  - [ ] Unit test target
  - [ ] UI test target

### Package.swift (if applicable)
```swift
// File: Package.swift
let package = Package(
    name: "MyApp",
    platforms: [
        .iOS(.v17),  // Updated from .v15
        .watchOS(.v10),  // Update if applicable
    ],
    ...
)
```

### Podfile (if applicable)
```ruby
# File: Podfile
platform :ios, '17.0'  # Updated from '15.0'
```

### CI/CD Configuration
- [ ] Update simulator version in CI configuration
- [ ] Update Xcode version requirement (if needed)
- [ ] Update Fastlane configuration
```

#### 3.2 Info.plist Changes

Check for version-specific Info.plist keys:

```markdown
## Info.plist Audit

### Keys to Add (available in new minimum)
| Key | Purpose | Required? |
|-----|---------|-----------|
| `UIRequiresFullScreen` | iPad multitasking | Review |
| Privacy usage descriptions | New permission prompts | If using new APIs |

### Keys to Review
| Key | Consideration |
|-----|---------------|
| `LSMinimumSystemVersion` | Should match deployment target |
| `MinimumOSVersion` | Auto-set by Xcode, verify |
| Background mode entitlements | New capabilities available |
```

#### 3.3 Entitlements Review

```markdown
## Entitlements Audit

### New Entitlements Available
| Entitlement | iOS Version | Benefit | Adopt? |
|-------------|-------------|---------|--------|
| Journaling Suggestions | iOS 17.2+ | Journal integration | [Y/N] |
| Sensitive Content Analysis | iOS 17+ | CSAM detection for UGC | [Y/N] |
| Interactive Widgets | iOS 17+ | Widget app intents | [Y/N] |

### Existing Entitlements to Verify
- [ ] Push notification entitlement still valid
- [ ] App Groups still correctly configured
- [ ] Keychain sharing groups unchanged
- [ ] Associated domains unchanged
```

---

### Phase 4: Dead Code Removal & New API Adoption

**CHECKPOINT 2:** Confirm all project settings updated before code cleanup.

```markdown
## Configuration Status

| Setting | Updated | Verified |
|---------|---------|----------|
| Project deployment target | [Yes/No] | [Yes/No] |
| All extension targets | [Yes/No] | [Yes/No] |
| Package.swift / Podfile | [Yes/No] | [Yes/No] |
| CI/CD configuration | [Yes/No] | [Yes/No] |
| Info.plist | [Yes/No] | [Yes/No] |

**Proceed with dead code removal?**
```

#### 4.1 Remove Dead Fallback Code

After removing availability checks, delete the fallback implementations:

```bash
# Find potential dead code: fallback views, polyfills, backports
grep -rn "Fallback\|Backport\|Legacy\|Compat\|Polyfill" --include="*.swift" Sources/

# Find unused files that were only needed for older OS support
# Check for files only referenced inside removed #available blocks
```

#### 4.2 Adopt New APIs Strategically

Prioritize adoption by impact:

```markdown
## API Adoption Plan

### High Priority (Immediate)
| Old Pattern | New API | Files Affected | Effort |
|-------------|---------|----------------|--------|
| `ObservableObject` + `@Published` | `@Observable` | 24 ViewModels | 2 days |
| Custom empty states | `ContentUnavailableView` | 8 screens | 4 hours |
| `PreviewProvider` | `#Preview` macro | 45 files | 1 day |

### Medium Priority (Next Sprint)
| Old Pattern | New API | Files Affected | Effort |
|-------------|---------|----------------|--------|
| GeometryReader sizing | `.containerRelativeFrame()` | 6 views | 4 hours |
| Manual scroll tracking | `.scrollPosition(id:)` | 3 screens | 2 hours |

### Low Priority (Backlog)
| Old Pattern | New API | Files Affected | Effort |
|-------------|---------|----------------|--------|
| NSRegularExpression | Swift Regex | 4 utilities | 2 hours |
| UIImpactFeedbackGenerator | `.sensoryFeedback()` | 2 views | 1 hour |
```

---

## Expected Output

### Version Upgrade Report

```markdown
# iOS Deployment Target Upgrade Report

## Summary
- Previous minimum: iOS [OLD]
- New minimum: iOS [NEW]
- Users affected: [X%] ([N] users)
- Availability checks removed: [N]
- Dead code lines removed: [N]
- New APIs adopted: [N]

## Changes Made
### Configuration
- [List of project setting changes]

### Availability Checks
| File | Line | Check Removed | Fallback Code Deleted |
|------|------|---------------|----------------------|
| [file] | [line] | `#available(iOS X)` | [Y/N, lines] |

### New API Adoptions
| Old API | New API | Files Changed |
|---------|---------|---------------|
| [old] | [new] | [count] |

## Testing Results
- [ ] Builds successfully on new minimum target
- [ ] All unit tests pass
- [ ] All UI tests pass
- [ ] Tested on simulator running iOS [NEW_MIN]
- [ ] No new warnings introduced
- [ ] Binary size: [X MB] (delta: [+/- Y])
```

### Implementation Checklist

- [ ] User adoption data analyzed and upgrade approved
- [ ] All dependencies verified compatible
- [ ] Deployment target updated in Xcode project (all targets)
- [ ] Package.swift / Podfile updated
- [ ] All removable `#available` / `@available` checks identified
- [ ] Availability checks removed for versions at or below new minimum
- [ ] Dead fallback code deleted
- [ ] Info.plist reviewed and updated
- [ ] Entitlements reviewed
- [ ] CI/CD simulator versions updated
- [ ] Tested on new minimum iOS version simulator
- [ ] New API adoption plan created and prioritized
- [ ] Release notes updated to communicate minimum version change

---

## Techniques Used

- **ST-01** (Clear Objective): Focused objective on deployment target upgrade
- **ST-02** (Sequential Instructions): Phased approach from impact analysis to code cleanup
- **NE-02** (Phased Workflow): Clear phases with checkpoints and decision gates

---

## Related Prompts

- [ios_swift_version_migration.md](ios_swift_version_migration.md) - Migrate to new Swift version (often paired with iOS upgrade)
- [ios_dependency_update.md](ios_dependency_update.md) - Update dependencies alongside version upgrade
- [ios_deprecation_audit.md](ios_deprecation_audit.md) - Audit deprecated APIs for replacement
- [ios_tech_debt_triage.md](ios_tech_debt_triage.md) - Prioritize tech debt cleanup after upgrade
