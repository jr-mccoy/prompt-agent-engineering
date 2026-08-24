---
title: "iOS UI Polish Audit"
category: mobile-development
description: "Audit iOS app UI for animation quality, gesture conflicts, safe area handling, dark mode support, Dynamic Island adaptation, and platform idiom compliance"
techniques:
  - ST-01
  - RT-02
  - RT-04
  - AG-02
difficulty: intermediate
tags:
  - ios
  - swift
  - ui-polish
  - animations
  - dark-mode
  - safe-area
updated: "2026-03-19"
---

# iOS UI Polish Audit

**Objective:** Conduct a comprehensive UI polish audit of an iOS app, examining animation quality, gesture recognizer conflicts, safe area compliance, dark mode support, and adherence to platform idioms. Identify rough edges that degrade perceived quality and provide specific fixes.

**When to Use:** Use this prompt before a major release to ensure visual polish, when users report UI glitches or inconsistencies, when adding dark mode support, when targeting new device form factors (Dynamic Island, iPad), or during design QA review cycles.

**Prompt Type:** Comprehensive (450-550 lines)

---

## Context Gathering

Before beginning the audit, understand the scope:

1. **Current State:**
   - "What iOS versions and devices does the app support?"
   - "Is dark mode currently supported? Partially or fully?"
   - "Are there known UI issues or user complaints about visual quality?"

2. **Design System:**
   - "Is there a design system or style guide?"
   - "Are custom animations used, or mostly system defaults?"
   - "What UI framework is primary? (SwiftUI, UIKit, or mixed)"

3. **Priority Areas:**
   - "Which screens or flows are highest priority for polish?"
   - "Are there upcoming device targets (iPad, Vision Pro)?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Verify the issue is real** - Test on actual devices or confirm via code analysis, not assumptions.
2. **Check intentionality** - Some unconventional UI choices are deliberate design decisions.
3. **Consider context** - A game or creative app may intentionally break platform conventions.
4. **Assess user impact** - Prioritize issues users actually encounter over theoretical concerns.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations.

**Finding a POLISHED app is an acceptable outcome.** Not every app has UI issues. If the app looks and feels good, say so.

### False-Positive Prevention

- ❌ Do NOT flag intentional custom UI as "non-standard"
- ❌ Do NOT require system animations when custom ones are well-implemented
- ❌ Do NOT flag safe area insets on screens that intentionally extend to edges
- ❌ Do NOT assume missing dark mode is a bug (may be a conscious decision)
- ✅ DO check for actual user-facing visual glitches
- ✅ DO verify animations run at 60/120fps on target devices
- ✅ DO test safe area handling across device families
- ✅ DO verify color contrast in both light and dark modes

---

### Phase 1: Animation Quality Audit

#### 1.1 Animation Timing and Curves

```swift
// ROUGH: Linear animations feel mechanical
UIView.animate(withDuration: 0.3) {
    view.alpha = 0
}

// POLISHED: Spring animations feel natural
UIView.animate(
    withDuration: 0.35,
    delay: 0,
    usingSpringWithDamping: 0.8,
    initialSpringVelocity: 0.5,
    options: [],
    animations: { view.alpha = 0 }
)

// BEST: SwiftUI spring animation
withAnimation(.spring(duration: 0.35, bounce: 0.2)) {
    isVisible = false
}
```

#### 1.2 Interactive Dismissal Support

```swift
// ROUGH: No interactive dismiss on presented sheets
class DetailViewController: UIViewController {
    // Modal with no swipe-to-dismiss support
}

// POLISHED: Support interactive dismissal
class DetailViewController: UIViewController, UIAdaptivePresentationControllerDelegate {
    override func viewDidLoad() {
        super.viewDidLoad()
        presentationController?.delegate = self
    }

    func presentationControllerShouldDismiss(
        _ presentationController: UIPresentationController
    ) -> Bool {
        return !hasUnsavedChanges
    }

    func presentationControllerDidAttemptToDismiss(
        _ presentationController: UIPresentationController
    ) {
        showUnsavedChangesAlert()
    }
}
```

#### 1.3 Animation Cancellation

```swift
// ROUGH: Animations stack or conflict
func showBadge() {
    UIView.animate(withDuration: 0.3) {
        self.badgeView.transform = CGAffineTransform(scaleX: 1.2, y: 1.2)
    } completion: { _ in
        UIView.animate(withDuration: 0.2) {
            self.badgeView.transform = .identity
        }
    }
}
// Calling showBadge() rapidly creates stacking animations

// POLISHED: Cancel previous animations
func showBadge() {
    badgeView.layer.removeAllAnimations()
    UIView.animate(
        withDuration: 0.3,
        delay: 0,
        usingSpringWithDamping: 0.6,
        initialSpringVelocity: 0.8,
        options: [.beginFromCurrentState],
        animations: { self.badgeView.transform = CGAffineTransform(scaleX: 1.2, y: 1.2) }
    ) { _ in
        UIView.animate(withDuration: 0.2) {
            self.badgeView.transform = .identity
        }
    }
}
```

---

### Phase 2: Gesture Conflict Resolution

#### 2.1 Scroll View + Gesture Conflicts

```swift
// PROBLEM: Pan gesture conflicts with scroll view
class CardViewController: UIViewController {
    let scrollView = UIScrollView()
    let panGesture = UIPanGestureRecognizer()

    // Users cannot scroll because pan gesture intercepts touches
}

// FIX: Gesture recognizer delegation
class CardViewController: UIViewController, UIGestureRecognizerDelegate {
    func setupGestures() {
        panGesture.delegate = self
        panGesture.addTarget(self, action: #selector(handlePan))
        view.addGestureRecognizer(panGesture)
    }

    func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool {
        guard let pan = gestureRecognizer as? UIPanGestureRecognizer else { return true }
        let velocity = pan.velocity(in: view)
        // Only begin if horizontal movement dominates
        return abs(velocity.x) > abs(velocity.y)
    }

    func gestureRecognizer(
        _ gestureRecognizer: UIGestureRecognizer,
        shouldRecognizeSimultaneouslyWith other: UIGestureRecognizer
    ) -> Bool {
        return other is UITapGestureRecognizer
    }
}
```

---

### Phase 3: Safe Area and Layout

#### 3.1 Safe Area Compliance

```swift
// BROKEN: Content hidden under notch/Dynamic Island
class ListViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.frame = view.bounds // Ignores safe area
    }
}

// FIXED: Respect safe area
class ListViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            tableView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
            tableView.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            tableView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
            tableView.bottomAnchor.constraint(equalTo: view.bottomAnchor) // Scroll under bottom
        ])
        tableView.contentInsetAdjustmentBehavior = .automatic
    }
}

// SwiftUI equivalent:
struct ListView: View {
    var body: some View {
        List(items) { item in
            ItemRow(item: item)
        }
        // Safe area is handled automatically in SwiftUI
        // Only ignore when intentional:
        // .ignoresSafeArea(.container, edges: .bottom)
    }
}
```

#### 3.2 Keyboard Avoidance

```swift
// BROKEN: Text field hidden behind keyboard
struct ChatView: View {
    @State private var message = ""

    var body: some View {
        VStack {
            MessageList(messages: messages)
            TextField("Message", text: $message)
        }
        // No keyboard avoidance
    }
}

// POLISHED: Proper keyboard handling
struct ChatView: View {
    @State private var message = ""

    var body: some View {
        VStack {
            MessageList(messages: messages)
            TextField("Message", text: $message)
                .textFieldStyle(.roundedBorder)
                .padding()
        }
        .safeAreaInset(edge: .bottom) {
            // Content automatically adjusts for keyboard in iOS 15+
        }
    }
}
```

---

### Phase 4: Dark Mode Support

#### 4.1 Color System Audit

```swift
// BROKEN: Hardcoded colors that break in dark mode
label.textColor = .black       // Invisible on dark background
view.backgroundColor = .white  // Blinding in dark mode

// FIXED: Semantic colors
label.textColor = .label                    // Adapts automatically
view.backgroundColor = .systemBackground    // Adapts automatically

// Custom colors with dark mode variants:
// In Assets.xcassets, define color set with:
// - Any Appearance: #1A1A2E
// - Dark Appearance: #E0E0FF

// SwiftUI:
struct ThemedCard: View {
    var body: some View {
        VStack {
            Text("Title")
                .foregroundStyle(.primary)    // Adapts
            Text("Subtitle")
                .foregroundStyle(.secondary)  // Adapts
        }
        .background(.regularMaterial)         // Adapts beautifully
    }
}
```

#### 4.2 Image Dark Mode Adaptation

```swift
// ROUGH: Images look wrong in dark mode
Image("logo") // Single appearance only

// POLISHED: Provide dark mode variants in asset catalog
// Or use SF Symbols that adapt:
Image(systemName: "person.circle.fill")
    .symbolRenderingMode(.hierarchical)
    .foregroundStyle(.tint)

// Or tint template images:
Image("custom-icon")
    .renderingMode(.template)
    .foregroundStyle(.primary)
```

#### 4.3 Status Bar and Navigation Appearance

```swift
// ROUGH: Status bar text invisible against matching background
override var preferredStatusBarStyle: UIStatusBarStyle {
    return .default // May not contrast with custom backgrounds
}

// POLISHED: Dynamic status bar style
override var preferredStatusBarStyle: UIStatusBarStyle {
    if traitCollection.userInterfaceStyle == .dark {
        return .lightContent
    }
    return .darkContent
}

// Better: Use system navigation bar appearance
let appearance = UINavigationBarAppearance()
appearance.configureWithDefaultBackground()
navigationController?.navigationBar.standardAppearance = appearance
navigationController?.navigationBar.scrollEdgeAppearance = appearance
```

---

### Phase 5: Platform Idiom Compliance

#### 5.1 System Font Usage

```swift
// ROUGH: Hardcoded font sizes that ignore accessibility
let label = UILabel()
label.font = UIFont.systemFont(ofSize: 16)

// POLISHED: Text styles that scale with Dynamic Type
label.font = .preferredFont(forTextStyle: .body)
label.adjustsFontForContentSizeCategory = true

// SwiftUI:
Text("Hello")
    .font(.body)  // Automatically supports Dynamic Type
```

#### 5.2 Trait Collection Responsiveness

```swift
// Handle appearance changes smoothly
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
    super.traitCollectionDidChange(previousTraitCollection)

    if traitCollection.hasDifferentColorAppearance(comparedTo: previousTraitCollection) {
        updateCustomColors()
    }

    if traitCollection.horizontalSizeClass != previousTraitCollection?.horizontalSizeClass {
        updateLayout(for: traitCollection.horizontalSizeClass)
    }
}
```

---

## Expected Output

1. **Polish Inventory** - All UI issues found with severity and screenshots/descriptions
2. **Animation Report** - Animation quality assessment with timing recommendations
3. **Gesture Audit** - Gesture conflicts identified with resolution strategies
4. **Dark Mode Report** - Color and image adaptation gaps
5. **Safe Area Report** - Layout issues across device families

---

## Example Interaction

**User reports a settings screen that looks rough:**

```swift
// BEFORE: SettingsViewController.swift
class SettingsViewController: UITableViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Settings"
        tableView.backgroundColor = UIColor(red: 0.95, green: 0.95, blue: 0.95, alpha: 1.0)
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: .value1, reuseIdentifier: "cell")
        cell.textLabel?.font = UIFont.systemFont(ofSize: 16)
        cell.textLabel?.textColor = .black
        cell.backgroundColor = .white
        return cell
    }
}
```

**Agent produces:**

```swift
// AFTER: SettingsViewController.swift
class SettingsViewController: UITableViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Settings"
        tableView.backgroundColor = .systemGroupedBackground
        navigationController?.navigationBar.prefersLargeTitles = true
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: .value1, reuseIdentifier: "cell")
        cell.textLabel?.font = .preferredFont(forTextStyle: .body)
        cell.textLabel?.adjustsFontForContentSizeCategory = true
        cell.textLabel?.textColor = .label
        cell.backgroundColor = .secondarySystemGroupedBackground
        cell.accessoryType = .disclosureIndicator
        return cell
    }
}
```

**Issues fixed:**
- Hardcoded background color replaced with `systemGroupedBackground` (dark mode compatible)
- Hardcoded text color `.black` replaced with `.label` (adapts to appearance)
- Hardcoded cell background replaced with `secondarySystemGroupedBackground`
- Font changed to `.preferredFont` with Dynamic Type support
- Large title navigation added per HIG for settings screens
- Disclosure indicator added for navigable rows

---

## Techniques Used

- **ST-01** (Clear Objective): Focused UI polish audit
- **RT-02** (Multi-Format Output): Code, checklists, and visual descriptions
- **RT-04** (Best Practice Review): Apple HIG and platform conventions
- **AG-02** (Iterative Refinement): Phase-by-phase audit with prioritization

---

## Related Prompts

- [ios_accessibility_improvement.md](ios_accessibility_improvement.md) - Accessibility overlaps with polish
- [ios_hig_compliance_review.md](ios_hig_compliance_review.md) - Deeper HIG compliance audit
- [ios_user_experience_enhancement.md](ios_user_experience_enhancement.md) - UX interaction patterns

---

## Customization Guide

### For SwiftUI-Only Apps

Focus on:
- `.animation()` modifier usage and implicit vs explicit animations
- Navigation transition customization
- `matchedGeometryEffect` for hero transitions
- Sheet and fullScreenCover presentation polish

### For iPad Optimization

Additional checks:
- Pointer/hover effect support
- Keyboard shortcut implementation
- Split view and sidebar navigation
- Drag and drop support
- Pencil interaction polish

### For Localization Polish

Verify:
- RTL layout support for Arabic/Hebrew
- Text truncation with long translations
- Date/number formatting by locale
- Dynamic Type with non-Latin scripts
