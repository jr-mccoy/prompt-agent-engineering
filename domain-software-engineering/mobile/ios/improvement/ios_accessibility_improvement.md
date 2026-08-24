---
title: "iOS Accessibility Improvement"
category: mobile-development
description: "Improve iOS app accessibility with VoiceOver support, Dynamic Type scaling, color contrast compliance, reduced motion support, and full assistive technology compatibility"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - RT-04
  - AG-02
difficulty: intermediate
tags:
  - ios
  - swift
  - accessibility
  - voiceover
  - dynamic-type
  - wcag
updated: "2026-03-19"
---

# iOS Accessibility Improvement

**Objective:** Improve an iOS app's accessibility by ensuring full VoiceOver support, proper Dynamic Type scaling, WCAG-compliant color contrast, reduced motion alternatives, and compatibility with all assistive technologies. Make the app usable by everyone.

**When to Use:** Use this prompt when preparing for accessibility audit or compliance review, when users report VoiceOver or accessibility issues, when adding Dynamic Type support, when targeting enterprise or government customers requiring WCAG compliance, or proactively to expand the app's reach.

**Prompt Type:** Comprehensive (500-600 lines)

---

## Context Gathering

Before beginning the accessibility audit, understand the scope:

1. **Current State:**
   - "Has the app been tested with VoiceOver?"
   - "Is Dynamic Type supported? Partially or fully?"
   - "Are there known accessibility issues or user complaints?"

2. **Compliance Requirements:**
   - "Is there a specific WCAG level required? (A, AA, AAA)"
   - "Are there legal or contractual accessibility requirements?"
   - "Does the app target education, healthcare, or government sectors?"

3. **Architecture:**
   - "Is the app primarily SwiftUI, UIKit, or mixed?"
   - "Are there custom controls or complex gesture interactions?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Test with VoiceOver** - Verify findings by tracing the accessibility tree, not guessing.
2. **Check existing accessibility attributes** - Code may already set labels/traits programmatically.
3. **Verify Dynamic Type behavior** - Check that layouts actually break, not just theoretically could.
4. **Measure contrast ratios** - Use actual color values, not visual approximation.
5. **Provide specific file:line locations** - Every finding MUST include exact code locations.

**Finding GOOD accessibility is an acceptable outcome.** SwiftUI provides many accessibility features automatically. Do not manufacture findings.

### False-Positive Prevention

- ❌ Do NOT flag decorative images as needing labels (they should be hidden)
- ❌ Do NOT require VoiceOver labels on elements that have visible text (automatic in SwiftUI)
- ❌ Do NOT flag Dynamic Type issues below the minimum deployment target
- ❌ Do NOT assume all custom views lack accessibility (they may use accessibility modifiers)
- ✅ DO verify VoiceOver navigation order is logical
- ✅ DO check that actionable elements have proper traits
- ✅ DO test with at least the two largest Dynamic Type sizes
- ✅ DO verify contrast ratios with actual color values

---

### Phase 1: VoiceOver Support

#### 1.1 Missing Accessibility Labels

```swift
// INACCESSIBLE: Icon-only button with no label
// UIKit:
let settingsButton = UIButton()
settingsButton.setImage(UIImage(systemName: "gear"), for: .normal)
// VoiceOver says: "Button" - user has no idea what it does

// ACCESSIBLE:
settingsButton.accessibilityLabel = "Settings"

// SwiftUI INACCESSIBLE:
Button(action: openSettings) {
    Image(systemName: "gear")
}
// VoiceOver says: "gear, Button"

// SwiftUI ACCESSIBLE:
Button(action: openSettings) {
    Image(systemName: "gear")
}
.accessibilityLabel("Settings")
```

#### 1.2 Grouping and Navigation Order

```swift
// POOR: VoiceOver reads each element separately
// User hears: "John" ... "Doe" ... "Engineer" ... "San Francisco"
struct ContactCard: View {
    var body: some View {
        HStack {
            VStack(alignment: .leading) {
                Text("John")
                Text("Doe")
            }
            VStack(alignment: .trailing) {
                Text("Engineer")
                Text("San Francisco")
            }
        }
    }
}

// GOOD: Elements grouped logically
struct ContactCard: View {
    var body: some View {
        HStack {
            VStack(alignment: .leading) {
                Text("John")
                Text("Doe")
            }
            VStack(alignment: .trailing) {
                Text("Engineer")
                Text("San Francisco")
            }
        }
        .accessibilityElement(children: .combine)
        // VoiceOver reads: "John Doe, Engineer, San Francisco"
    }
}

// BETTER: Custom label for natural reading
struct ContactCard: View {
    let contact: Contact

    var body: some View {
        HStack { /* ... layout ... */ }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel("\(contact.fullName), \(contact.title) in \(contact.city)")
    }
}
```

#### 1.3 Custom Actions

```swift
// POOR: Swipe-only actions inaccessible to VoiceOver
struct MessageRow: View {
    var body: some View {
        Text(message.text)
            .swipeActions {
                Button("Delete", role: .destructive) { delete() }
                Button("Archive") { archive() }
            }
    }
}

// GOOD: SwiftUI swipe actions are automatically VoiceOver accessible
// But for custom gestures, add custom actions:
struct MessageRow: View {
    var body: some View {
        Text(message.text)
            .swipeActions {
                Button("Delete", role: .destructive) { delete() }
                Button("Archive") { archive() }
            }
            .accessibilityAction(named: "Delete") { delete() }
            .accessibilityAction(named: "Archive") { archive() }
    }
}

// UIKit equivalent:
cell.accessibilityCustomActions = [
    UIAccessibilityCustomAction(name: "Delete") { _ in
        self.delete()
        return true
    },
    UIAccessibilityCustomAction(name: "Archive") { _ in
        self.archive()
        return true
    }
]
```

#### 1.4 Accessibility Traits

```swift
// MISSING: Custom views without proper traits
struct ToggleCard: View {
    @Binding var isEnabled: Bool

    var body: some View {
        HStack {
            Text("Notifications")
            Spacer()
            Circle()
                .fill(isEnabled ? .green : .gray)
                .onTapGesture { isEnabled.toggle() }
        }
    }
    // VoiceOver: "Notifications" - no indication it is toggleable
}

// FIXED: Proper traits and value
struct ToggleCard: View {
    @Binding var isEnabled: Bool

    var body: some View {
        HStack {
            Text("Notifications")
            Spacer()
            Circle()
                .fill(isEnabled ? .green : .gray)
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel("Notifications")
        .accessibilityValue(isEnabled ? "On" : "Off")
        .accessibilityAddTraits(.isButton)
        .accessibilityAction { isEnabled.toggle() }
        // VoiceOver: "Notifications, On, Button. Double tap to toggle."
    }
}
```

---

### Phase 2: Dynamic Type Support

#### 2.1 Text Style Adoption

```swift
// BROKEN: Fixed font sizes
// UIKit:
label.font = UIFont.systemFont(ofSize: 16)

// FIXED: Dynamic Type text styles
label.font = .preferredFont(forTextStyle: .body)
label.adjustsFontForContentSizeCategory = true

// SwiftUI (automatic):
Text("Hello")
    .font(.body) // Automatically scales

// Custom fonts with Dynamic Type:
// UIKit:
let descriptor = UIFontDescriptor.preferredFontDescriptor(withTextStyle: .body)
label.font = UIFont(descriptor: descriptor.withDesign(.rounded)!, size: 0)

// SwiftUI:
Text("Hello")
    .font(.custom("MyFont-Regular", size: 17, relativeTo: .body))
```

#### 2.2 Layout Adaptation for Large Text

```swift
// BROKEN: Horizontal layout clips at large sizes
struct PriceRow: View {
    var body: some View {
        HStack {
            Text("Premium Plan")
            Spacer()
            Text("$9.99/month")
        }
    }
    // At Accessibility XXL: text overlaps or clips
}

// FIXED: Adapt layout for large text
struct PriceRow: View {
    @Environment(\.dynamicTypeSize) var dynamicTypeSize

    var body: some View {
        let layout = dynamicTypeSize.isAccessibilitySize
            ? AnyLayout(VStackLayout(alignment: .leading))
            : AnyLayout(HStackLayout())

        layout {
            Text("Premium Plan")
            if !dynamicTypeSize.isAccessibilitySize {
                Spacer()
            }
            Text("$9.99/month")
                .foregroundStyle(.secondary)
        }
    }
}
```

#### 2.3 Scrollable Content for Large Text

```swift
// BROKEN: Fixed-height container clips large text
struct HeaderView: View {
    var body: some View {
        VStack {
            Text("Welcome Back")
                .font(.largeTitle)
            Text("Here is your daily summary")
                .font(.title3)
        }
        .frame(height: 120) // Clips at large type sizes
    }
}

// FIXED: Allow content to scroll or grow
struct HeaderView: View {
    var body: some View {
        VStack {
            Text("Welcome Back")
                .font(.largeTitle)
            Text("Here is your daily summary")
                .font(.title3)
        }
        .frame(minHeight: 120) // Grows with content
    }
}
```

---

### Phase 3: Color Contrast and Visual Accessibility

#### 3.1 WCAG Contrast Requirements

```swift
// FAILING: Low contrast text
Text("Subtle hint")
    .foregroundColor(Color(red: 0.7, green: 0.7, blue: 0.7)) // #B3B3B3 on white
    // Contrast ratio: 2.6:1 (FAILS WCAG AA minimum of 4.5:1)

// PASSING: Adequate contrast
Text("Subtle hint")
    .foregroundColor(Color(red: 0.46, green: 0.46, blue: 0.46)) // #757575 on white
    // Contrast ratio: 4.6:1 (PASSES WCAG AA)

// BEST: Use semantic colors that Apple has validated
Text("Subtle hint")
    .foregroundStyle(.secondary) // Apple ensures adequate contrast in both modes
```

#### 3.2 Color-Only Information

```swift
// INACCESSIBLE: Status conveyed only by color
struct StatusBadge: View {
    let status: Status

    var body: some View {
        Circle()
            .fill(status == .active ? .green : .red)
            .frame(width: 12, height: 12)
    }
    // Color-blind users cannot distinguish status
}

// ACCESSIBLE: Shape + color + label
struct StatusBadge: View {
    let status: Status

    var body: some View {
        HStack(spacing: 4) {
            Image(systemName: status == .active ? "checkmark.circle.fill" : "xmark.circle.fill")
                .foregroundStyle(status == .active ? .green : .red)
            Text(status == .active ? "Active" : "Inactive")
                .font(.caption)
        }
        .accessibilityElement(children: .combine)
    }
}
```

---

### Phase 4: Reduced Motion Support

#### 4.1 Respecting Motion Preferences

```swift
// ROUGH: Complex animations regardless of preference
struct HeroTransition: View {
    @State private var isExpanded = false

    var body: some View {
        CardView()
            .scaleEffect(isExpanded ? 1.5 : 1.0)
            .rotation3DEffect(.degrees(isExpanded ? 360 : 0), axis: (x: 0, y: 1, z: 0))
            .animation(.spring(duration: 0.8), value: isExpanded)
    }
}

// POLISHED: Respect reduced motion preference
struct HeroTransition: View {
    @State private var isExpanded = false
    @Environment(\.accessibilityReduceMotion) var reduceMotion

    var body: some View {
        CardView()
            .scaleEffect(isExpanded ? 1.5 : 1.0)
            .rotation3DEffect(
                .degrees(reduceMotion ? 0 : (isExpanded ? 360 : 0)),
                axis: (x: 0, y: 1, z: 0)
            )
            .animation(reduceMotion ? .none : .spring(duration: 0.8), value: isExpanded)
    }
}

// UIKit:
if UIAccessibility.isReduceMotionEnabled {
    // Simple fade or no animation
    UIView.animate(withDuration: 0.1) { view.alpha = 1 }
} else {
    // Full spring animation
    UIView.animate(withDuration: 0.6, delay: 0, usingSpringWithDamping: 0.7,
                   initialSpringVelocity: 0.5, options: [], animations: { /* ... */ })
}
```

---

### Phase 5: Assistive Technology Compatibility

#### 5.1 Switch Control Support

```swift
// Ensure all interactive elements are reachable via Switch Control
// Check: No gesture-only interactions without button alternatives
// Check: Focus order is logical for sequential scanning
// Check: Custom controls respond to .accessibilityActivate()

struct CustomSlider: View {
    @Binding var value: Double

    var body: some View {
        GeometryReader { geometry in
            // Custom drawing...
        }
        .accessibilityValue("\(Int(value))%")
        .accessibilityAdjustableAction { direction in
            switch direction {
            case .increment: value = min(100, value + 10)
            case .decrement: value = max(0, value - 10)
            @unknown default: break
            }
        }
    }
}
```

#### 5.2 Voice Control Compatibility

```swift
// Ensure buttons have visible labels that match accessibility labels
// Voice Control users say what they see

// PROBLEM: Accessibility label does not match visible text
Button("Buy") { purchase() }
    .accessibilityLabel("Purchase item")
// User says "Tap Buy" - Voice Control cannot find it
// User says "Tap Purchase item" - Works but confusing

// FIXED: Keep accessibility label matching visible text
Button("Buy") { purchase() }
    .accessibilityLabel("Buy")
    .accessibilityHint("Purchases the selected item")
```

---

## Expected Output

1. **VoiceOver Audit** - Missing labels, poor navigation order, missing traits
2. **Dynamic Type Report** - Fixed fonts, clipping layouts, non-scaling elements
3. **Contrast Report** - Color pairs failing WCAG AA with exact ratios
4. **Motion Audit** - Animations not respecting reduced motion preference
5. **Assistive Tech Report** - Switch Control and Voice Control compatibility gaps

---

## Example Interaction

**User provides a product card component:**

```swift
// BEFORE: ProductCard.swift
struct ProductCard: View {
    let product: Product

    var body: some View {
        VStack {
            AsyncImage(url: product.imageURL)
                .frame(height: 200)
            Text(product.name)
                .font(.system(size: 18, weight: .bold))
            HStack {
                Circle()
                    .fill(product.inStock ? .green : .red)
                    .frame(width: 8, height: 8)
                Text(product.price)
                    .font(.system(size: 14))
                    .foregroundColor(.gray)
            }
        }
        .onTapGesture { navigateToDetail() }
    }
}
```

**Agent produces:**

```swift
// AFTER: ProductCard.swift
struct ProductCard: View {
    let product: Product
    @Environment(\.dynamicTypeSize) var dynamicTypeSize

    var body: some View {
        VStack(alignment: .leading) {
            AsyncImage(url: product.imageURL) { image in
                image.resizable().aspectRatio(contentMode: .fill)
            } placeholder: {
                Rectangle().fill(.quaternary)
            }
            .frame(height: dynamicTypeSize.isAccessibilitySize ? 120 : 200)
            .clipped()
            .accessibilityHidden(true) // Decorative; product name suffices

            Text(product.name)
                .font(.headline) // Dynamic Type compatible

            HStack(spacing: 6) {
                Image(systemName: product.inStock ? "checkmark.circle.fill" : "xmark.circle.fill")
                    .foregroundStyle(product.inStock ? .green : .red)
                    .imageScale(.small)
                Text(product.inStock ? "In Stock" : "Out of Stock")
                    .font(.caption)
                Spacer()
                Text(product.price)
                    .font(.subheadline)
                    .foregroundStyle(.secondary) // Guaranteed contrast
            }
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel("\(product.name), \(product.price), \(product.inStock ? "In Stock" : "Out of Stock")")
        .accessibilityAddTraits(.isButton)
        .accessibilityHint("Opens product details")
        .onTapGesture { navigateToDetail() }
    }
}
```

**Issues fixed:**
- Fixed font sizes replaced with Dynamic Type text styles
- Color-only stock indicator now has icon and text
- Gray price text replaced with `.secondary` for guaranteed contrast
- Product card grouped as single accessible element with descriptive label
- Button trait and hint added for VoiceOver
- Decorative image hidden from VoiceOver
- Layout adapts image height for accessibility sizes

---

## Techniques Used

- **ST-01** (Clear Objective): Focused accessibility improvement
- **ST-02** (Sequential Instructions): Phased audit by accessibility domain
- **RT-02** (Multi-Format Output): Code, checklists, and contrast measurements
- **RT-04** (Best Practice Review): WCAG and Apple accessibility guidelines
- **AG-02** (Iterative Refinement): Progressive audit and fix cycles

---

## Related Prompts

- [ios_ui_polish_audit.md](ios_ui_polish_audit.md) - Visual polish overlaps with accessibility
- [ios_hig_compliance_review.md](ios_hig_compliance_review.md) - HIG accessibility requirements
- [ios_user_experience_enhancement.md](ios_user_experience_enhancement.md) - UX for all users

---

## Customization Guide

### For WCAG AAA Compliance

Stricter requirements:
- Contrast ratio 7:1 for normal text (vs 4.5:1 for AA)
- Sign language alternatives for audio content
- No timing-dependent interactions
- Multiple navigation methods

### For Education Apps

Focus on:
- Switch Control for students with motor disabilities
- Guided Access compatibility
- Speak Screen and Speak Selection support
- Simple, consistent navigation patterns

### For Media-Rich Apps

Additional checks:
- Closed captions for video content
- Audio descriptions for visual content
- Alternative text for complex images/charts
- Media playback controls accessible to VoiceOver
