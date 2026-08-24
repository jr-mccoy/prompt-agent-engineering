---
title: "iOS Deprecation Audit"
category: mobile-development
description: "Audit deprecated Apple APIs and plan replacements with compiler warning scanning, deprecated API inventory, replacement mapping, migration priority, and conditional availability patterns."
techniques:
  - ST-01
  - RT-02
difficulty: intermediate
tags:
  - ios
  - swift
  - deprecation
  - api-migration
updated: "2026-03-20"
---

# iOS Deprecation Audit

**Objective:** Audit all deprecated Apple API usage in an iOS codebase, create an inventory of deprecated calls, map each to its modern replacement, prioritize migration effort, and implement replacements using conditional availability patterns where necessary.

**When to Use:** Use this prompt after WWDC when new deprecations are announced, before raising your deployment target, when updating to a new Xcode version that introduces new warnings, or as part of a quarterly maintenance cycle. Also valuable before major releases to avoid App Store review issues.

**Prompt Type:** Modular (300+ lines)

---

## Context Gathering

Before auditing, gather essential context:

1. **Build Environment:**
   - "What Xcode version and SDK are you building against?"
   - "What is your minimum deployment target?"
   - "Are there existing deprecation warnings being suppressed?"

2. **Codebase:**
   - "How many Swift and Objective-C files are in the project?"
   - "Are there wrapper layers around Apple APIs that centralize usage?"
   - "Do you use any third-party libraries that may also have deprecated API usage?"

3. **Timeline:**
   - "When is the next App Store submission?"
   - "Are there upcoming Xcode version requirements from Apple?"
   - "Is a deployment target raise planned that would turn deprecation warnings into errors?"

4. **Risk Tolerance:**
   - "Are there deprecated APIs that currently work but may be removed in the next iOS version?"
   - "Are there areas where behavioral changes accompany the deprecation?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before migrating ANY deprecated API, you MUST:**

1. **Understand why it was deprecated** - Read the deprecation notice. Some APIs are deprecated for security reasons (urgent) vs. API cleanup (less urgent).
2. **Verify the replacement exists on your minimum target** - The replacement API may require a higher iOS version than your current minimum.
3. **Check for behavioral differences** - Replacement APIs may not be 1:1 equivalent. Understand what changed.
4. **Test the migration** - Deprecated APIs still work. Replacements may have subtle differences that require testing.
5. **Use conditional availability when needed** - If the replacement requires a higher OS than your minimum, use `#available` to support both.

**Deprecated does not mean broken. Prioritize by risk of removal and behavioral impact, not just warning count.**

### False-Positive Prevention

- ❌ Do NOT migrate deprecated APIs without verifying the replacement works on your minimum deployment target
- ❌ Do NOT assume the replacement API has identical behavior
- ❌ Do NOT suppress deprecation warnings with `@available(*, deprecated)` to hide the problem
- ❌ Do NOT migrate APIs in third-party code you do not own (file issues upstream instead)
- ❌ Do NOT batch all deprecation fixes into one PR (makes regression isolation difficult)
- ✅ DO check Apple's migration guides for deprecated frameworks (e.g., UIWebView to WKWebView)
- ✅ DO use `#available` checks when replacement requires higher OS than minimum target
- ✅ DO test on the oldest supported iOS version after migration
- ✅ DO group related deprecations into logical PRs
- ✅ DO check release notes for the iOS version that deprecated each API

---

### Phase 1: Deprecation Discovery

#### 1.1 Compiler Warning Scan

```bash
# Full build capturing all deprecation warnings
xcodebuild build \
    -workspace MyApp.xcworkspace \
    -scheme MyApp \
    -sdk iphonesimulator \
    -destination 'platform=iOS Simulator,name=iPhone 16' \
    2>&1 | grep "'.*' was deprecated" | sort -u

# Count deprecation warnings
xcodebuild build \
    -workspace MyApp.xcworkspace \
    -scheme MyApp \
    -sdk iphonesimulator \
    2>&1 | grep -c "was deprecated"

# Group by deprecated API
xcodebuild build \
    -workspace MyApp.xcworkspace \
    -scheme MyApp \
    -sdk iphonesimulator \
    2>&1 | grep "was deprecated" \
    | sed "s/.*'\(.*\)' was deprecated.*/\1/" \
    | sort | uniq -c | sort -rn

# Group by file
xcodebuild build \
    -workspace MyApp.xcworkspace \
    -scheme MyApp \
    -sdk iphonesimulator \
    2>&1 | grep "was deprecated" \
    | sed 's/:.*$//' | sort | uniq -c | sort -rn
```

#### 1.2 Manual Discovery

Beyond compiler warnings, check for:

```bash
# APIs deprecated without compiler warnings (runtime deprecations)
grep -rn "UIWebView" --include="*.swift" --include="*.m" Sources/
grep -rn "UIAlertView\|UIActionSheet" --include="*.swift" --include="*.m" Sources/
grep -rn "addressBookRef\|ABAddressBook" --include="*.swift" --include="*.m" Sources/

# String-based API usage that won't show compiler warnings
grep -rn "UIApplication.shared.openURL" --include="*.swift" Sources/
grep -rn "NSSortDescriptor(key:" --include="*.swift" Sources/
grep -rn "setValue.*forKey" --include="*.swift" Sources/

# Objective-C protocols that have been superseded
grep -rn "UITableViewDataSource\|UICollectionViewDataSource" --include="*.swift" Sources/ \
    | grep -v "Diffable"

# Check for deprecated Info.plist keys
grep -r "UILaunchStoryboardName\|UIMainStoryboardFile" *.plist 2>/dev/null
```

#### 1.3 Deprecated API Inventory

```markdown
## Deprecated API Inventory

### By Severity

#### Critical (Will be removed or already causes issues)
| API | Deprecated In | Removed In | Files | Urgency |
|-----|--------------|------------|-------|---------|
| UIWebView | iOS 12 | App Store rejects | 3 | IMMEDIATE |
| UIApplication.shared.openURL(_:) | iOS 10 | Not yet | 5 | HIGH |

#### High (Deprecated 2+ versions ago)
| API | Deprecated In | Replacement | Files | Notes |
|-----|--------------|-------------|-------|-------|
| ObservableObject | iOS 17* | @Observable | 24 | *Soft deprecation |
| UIActivityIndicatorView.Style.gray | iOS 13 | .medium | 8 | Trivial fix |
| UITableViewCell.textLabel | iOS 14 | Content configuration | 12 | Moderate effort |

#### Medium (Deprecated in latest SDK)
| API | Deprecated In | Replacement | Files | Notes |
|-----|--------------|-------------|-------|-------|
| [API name] | iOS 18 | [replacement] | [N] | [notes] |

#### Low (Deprecated but stable, no removal announced)
| API | Deprecated In | Replacement | Files | Notes |
|-----|--------------|-------------|-------|-------|
| [API name] | [version] | [replacement] | [N] | [notes] |

### Summary
| Severity | Count | Files Affected |
|----------|-------|----------------|
| Critical | [N] | [N] |
| High | [N] | [N] |
| Medium | [N] | [N] |
| Low | [N] | [N] |
| **Total** | **[N]** | **[N]** |
```

---

### Phase 2: Replacement Mapping

**CHECKPOINT 1:** Confirm inventory is complete before mapping replacements.

```markdown
## Audit Summary

| Metric | Value |
|--------|-------|
| Total deprecation warnings | [N] |
| Unique deprecated APIs | [N] |
| Files affected | [N] |
| Critical items | [N] |

**Proceed with replacement mapping?**
```

#### 2.1 Common Deprecation Replacements (iOS 15-18)

| Deprecated | Replacement | Min iOS | Migration Effort |
|------------|------------|---------|------------------|
| `ObservableObject` + `@Published` | `@Observable` macro | iOS 17 | Medium (per VM) |
| `PreviewProvider` protocol | `#Preview` macro | iOS 17 | Low (per file) |
| `UITableViewCell.textLabel` | `UIListContentConfiguration` | iOS 14 | Medium |
| `UITableViewCell.imageView` | `UIListContentConfiguration` | iOS 14 | Medium |
| `UIApplication.shared.openURL(_:)` | `UIApplication.shared.open(_:options:)` | iOS 10 | Low |
| `UIActivityIndicatorView.Style.gray` | `.medium` | iOS 13 | Trivial |
| `UIActivityIndicatorView.Style.whiteLarge` | `.large` | iOS 13 | Trivial |
| `UIApplication.statusBarOrientation` | `UIWindowScene.interfaceOrientation` | iOS 13 | Low |
| `UIScreen.main` | `UIApplication.shared.connectedScenes` | iOS 16 | Low-Medium |
| `NSPredicate(format:)` for SwiftData | `#Predicate` macro | iOS 17 | Medium |
| `UIMenuController` | `UIEditMenuInteraction` | iOS 16 | Medium |
| `UINavigationBar.appearance()` | `UINavigationBar.scrollEdgeAppearance` | iOS 13 | Medium |
| `WKWebView.evaluateJavaScript(_:)` | `WKWebView.callAsyncJavaScript(_:)` | iOS 15 | Low |

#### 2.2 Replacement with Conditional Availability

When the replacement requires a higher iOS version than your minimum:

```swift
// Pattern: Replacement available on newer OS, fallback for older

// BEFORE: Using deprecated API on all versions
let style: UIActivityIndicatorView.Style = .whiteLarge

// AFTER (if min target already >= iOS 13): Direct replacement
let style: UIActivityIndicatorView.Style = .large

// AFTER (if min target < iOS 13): Conditional
let style: UIActivityIndicatorView.Style
if #available(iOS 13, *) {
    style = .large
} else {
    style = .whiteLarge
}
```

**More complex example - UITableViewCell configuration:**

```swift
// BEFORE: Deprecated textLabel/imageView
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
    cell.textLabel?.text = items[indexPath.row].title
    cell.detailTextLabel?.text = items[indexPath.row].subtitle
    cell.imageView?.image = items[indexPath.row].icon
    return cell
}

// AFTER: Content configuration (iOS 14+)
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
    var content = cell.defaultContentConfiguration()
    content.text = items[indexPath.row].title
    content.secondaryText = items[indexPath.row].subtitle
    content.image = items[indexPath.row].icon
    cell.contentConfiguration = content
    return cell
}
```

**Framework-level deprecation - UIScreen.main:**

```swift
// BEFORE: Deprecated UIScreen.main
let bounds = UIScreen.main.bounds
let scale = UIScreen.main.scale

// AFTER: Scene-based (iOS 16+)
extension UIWindow {
    static var currentScreen: UIScreen? {
        UIApplication.shared.connectedScenes
            .compactMap { $0 as? UIWindowScene }
            .first?
            .screen
    }
}

let bounds = UIWindow.currentScreen?.bounds ?? .zero
let scale = UIWindow.currentScreen?.scale ?? 1.0
```

#### 2.3 Wrapper Pattern for Centralized Migration

```swift
// File: Utilities/DeprecationBridge.swift
// Centralizes deprecated API usage for easier future migration

enum AppURL {
    /// Opens a URL using the modern API, with fallback for older iOS
    static func open(_ url: URL, completion: ((Bool) -> Void)? = nil) {
        UIApplication.shared.open(url, options: [:]) { success in
            completion?(success)
        }
    }
}

enum AppScreen {
    /// Returns the primary screen bounds, bridging the UIScreen.main deprecation
    static var bounds: CGRect {
        if #available(iOS 16, *) {
            return UIApplication.shared.connectedScenes
                .compactMap { $0 as? UIWindowScene }
                .first?
                .screen
                .bounds ?? UIScreen.main.bounds
        } else {
            return UIScreen.main.bounds
        }
    }
}
```

---

### Phase 3: Migration Priority & Planning

#### 3.1 Priority Matrix

| Priority | Criteria | Action | Timeline |
|----------|----------|--------|----------|
| **P0** | App Store rejects (UIWebView) | Immediate fix | This sprint |
| **P1** | Security-related deprecation | Plan migration | Next sprint |
| **P2** | API will be removed in next major iOS | Schedule migration | This quarter |
| **P3** | Soft deprecation, modern alternative available | Opportunistic migration | When touching file |
| **P4** | Cosmetic deprecation, no removal timeline | Track but defer | Backlog |

#### 3.2 Migration Plan

```markdown
## Deprecation Migration Plan

### Sprint 1: Critical
| Deprecated API | Replacement | Files | Effort | Developer |
|---------------|-------------|-------|--------|-----------|
| UIWebView | WKWebView | 3 | 2 days | Senior |

### Sprint 2: High Priority
| Deprecated API | Replacement | Files | Effort | Developer |
|---------------|-------------|-------|--------|-----------|
| openURL | open(_:options:) | 5 | 2 hours | Any |
| ActivityIndicator.gray | .medium | 8 | 30 min | Any |
| textLabel/imageView | Content configuration | 12 | 1 day | Mid |

### Opportunistic (When Touching Files)
| Deprecated API | Replacement | Files | Effort |
|---------------|-------------|-------|--------|
| ObservableObject | @Observable | 24 | 30 min/file |
| PreviewProvider | #Preview | 45 | 5 min/file |

### Deferred (Track in Backlog)
| Deprecated API | Reason for Deferral | Review Date |
|---------------|---------------------|-------------|
| [API] | [Minimum target too low for replacement] | [date] |
```

#### 3.3 Opportunistic Migration Rules

For P3/P4 deprecations, establish team rules:

```markdown
## Boy Scout Rule for Deprecations

When a developer touches a file that contains deprecated APIs:

1. **Check if the replacement is available** on your minimum deployment target
2. **If yes and the fix is < 15 minutes:** Fix it in the same PR
3. **If yes but the fix is complex:** Create a follow-up ticket
4. **If no (requires higher OS):** Add a `// TODO: [iOS XX]` comment with the replacement API name

### Example Comment Format
```swift
// TODO: [iOS 17] Replace ObservableObject with @Observable macro
// See: https://developer.apple.com/documentation/Observation
class HomeViewModel: ObservableObject {
    @Published var items: [Item] = []
}
```
```

---

### Phase 4: Verification

**CHECKPOINT 2:** Confirm migration plan approved before implementing changes.

```markdown
## Migration Plan Status

| Priority | Items | Scheduled Sprint | Approved |
|----------|-------|-----------------|----------|
| P0 | [N] | Sprint [N] | [Yes/No] |
| P1 | [N] | Sprint [N] | [Yes/No] |
| P2 | [N] | Sprint [N] | [Yes/No] |
| Opportunistic | [N] | Ongoing | N/A |

**Proceed with implementation?**
```

#### 4.1 Post-Migration Verification

```bash
# Verify deprecation warning count decreased
BEFORE_COUNT=[previous count]

AFTER_COUNT=$(xcodebuild build \
    -workspace MyApp.xcworkspace \
    -scheme MyApp \
    -sdk iphonesimulator \
    2>&1 | grep -c "was deprecated")

echo "Before: $BEFORE_COUNT, After: $AFTER_COUNT, Resolved: $((BEFORE_COUNT - AFTER_COUNT))"

# Verify no new warnings introduced
xcodebuild build \
    -workspace MyApp.xcworkspace \
    -scheme MyApp \
    -sdk iphonesimulator \
    2>&1 | grep "warning:" | grep -v "was deprecated" | sort -u

# Run tests to verify no behavioral regressions
xcodebuild test \
    -workspace MyApp.xcworkspace \
    -scheme MyApp \
    -sdk iphonesimulator \
    -destination 'platform=iOS Simulator,name=iPhone 16'

# Also test on oldest supported simulator
xcodebuild test \
    -workspace MyApp.xcworkspace \
    -scheme MyApp \
    -sdk iphonesimulator \
    -destination 'platform=iOS Simulator,OS=17.0,name=iPhone 15'
```

#### 4.2 Ongoing Monitoring

```markdown
## Deprecation Monitoring Cadence

| Event | Action |
|-------|--------|
| After WWDC (June) | Full audit against new SDK deprecations |
| After Xcode GM (September) | Re-audit, plan pre-release migrations |
| Before each release | Check for new deprecation warnings |
| Quarterly | Review deferred items, re-assess priority |
| Deployment target raise | Remove conditional availability for old APIs |
```

---

## Expected Output

### Deprecation Audit Report

```markdown
# Deprecation Audit Report - [App Name] - [Date]

## Summary
- SDK version: Xcode [X], iOS [X] SDK
- Minimum deployment target: iOS [X]
- Total deprecation warnings: [N]
- Unique deprecated APIs: [N]
- Critical (App Store risk): [N]
- Files affected: [N]

## Inventory
[Full table of deprecated APIs with severity, replacement, and effort]

## Migration Plan
[Prioritized plan with sprint assignments]

## Metrics
| Metric | Before | Target |
|--------|--------|--------|
| Deprecation warnings | [N] | [N] |
| Critical deprecations | [N] | 0 |
| Files with deprecations | [N] | [N] |
```

### Implementation Checklist

- [ ] Full build compiled to capture all deprecation warnings
- [ ] Manual scan completed for non-warning deprecations
- [ ] Deprecated API inventory created with severity ratings
- [ ] Replacement mapped for each deprecated API
- [ ] Minimum iOS version verified for each replacement
- [ ] Conditional availability patterns applied where needed
- [ ] Migration prioritized (P0-P4)
- [ ] Sprint plan created for P0-P2 items
- [ ] Opportunistic migration rules established for the team
- [ ] Post-migration verification completed (warning count, tests, oldest OS)
- [ ] Monitoring cadence established

---

## Techniques Used

- **ST-01** (Clear Objective): Focused objective on auditing and planning deprecation migrations
- **RT-02** (Multi-Dimensional Analysis): Covers discovery, replacement mapping, prioritization, and verification

---

## Related Prompts

- [ios_version_upgrade.md](ios_version_upgrade.md) - Deployment target raises that enable removing availability checks
- [ios_swift_version_migration.md](ios_swift_version_migration.md) - Swift version changes that deprecate language features
- [ios_dependency_update.md](ios_dependency_update.md) - Dependencies that may also have deprecated API usage
- [ios_tech_debt_triage.md](ios_tech_debt_triage.md) - Deprecations as a category of tech debt
