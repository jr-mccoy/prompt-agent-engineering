---
title: "iOS SwiftUI-UIKit Interop Review"
category: mobile-development
description: "Review UIViewRepresentable and UIViewControllerRepresentable for coordinator lifecycle, update propagation, sizing conflicts, and memory management."
techniques:
  - ST-01
  - RT-02
  - RT-04
  - AG-02
difficulty: advanced
tags:
  - ios
  - swift
  - code-review
  - swiftui
  - uikit
  - interop
updated: "2026-03-19"
---

# iOS SwiftUI-UIKit Interop Review

**Objective:** Audit UIViewRepresentable and UIViewControllerRepresentable implementations for correct coordinator lifecycle, bidirectional update propagation without infinite loops, intrinsic sizing and Auto Layout conflicts, and memory management to prevent leaks at the SwiftUI-UIKit boundary.

**When to Use:** Apply when reviewing any bridged UIKit component in SwiftUI, investigating layout issues with wrapped UIKit views, or debugging retain cycles in coordinator-based wrappers.

**Prompt Type:** Modular (80-150 lines)

## Context Gathering

1. What UIKit components are being wrapped (UITextView, MKMapView, WKWebView, custom)?
2. Does the wrapper need bidirectional data flow (SwiftUI state <-> UIKit delegate)?
3. Are there Auto Layout constraints inside the wrapped UIKit view?
4. Is the wrapped view expensive to create (web views, map views)?

## Instructions

### CRITICAL: Verification Requirements

- Coordinator must be the delegate/data source — never the Representable struct itself (it is recreated)
- updateUIView must be idempotent and guard against setting values that trigger delegate callbacks
- Wrapped UIKit views with intrinsic content size must communicate size to SwiftUI correctly
- Coordinator must not hold strong references to the Representable struct

### False-Positive Prevention

- ❌ Do NOT flag recreating lightweight UIViews in makeUIView — some views are cheap to create
- ✅ DO flag recreating expensive views (WKWebView, MKMapView) — should be cached or use coordinator
- ❌ Do NOT flag updateUIView being called frequently — SwiftUI controls this, not the developer
- ✅ DO flag updateUIView performing expensive operations without change checks
- ❌ Do NOT flag coordinators storing UIKit view references when needed for delegate callbacks
- ✅ DO flag coordinators storing strong references back to the SwiftUI Representable struct

1. **Coordinator Lifecycle**

```swift
// BAD: Representable struct acts as delegate — recreated each SwiftUI update
struct MyTextView: UIViewRepresentable {
    @Binding var text: String

    func makeUIView(context: Context) -> UITextView {
        let view = UITextView()
        view.delegate = self as? UITextViewDelegate // will never work
        return view
    }
}

// GOOD: Coordinator as stable delegate
struct MyTextView: UIViewRepresentable {
    @Binding var text: String

    func makeCoordinator() -> Coordinator { Coordinator(text: $text) }

    func makeUIView(context: Context) -> UITextView {
        let view = UITextView()
        view.delegate = context.coordinator
        return view
    }

    func updateUIView(_ uiView: UITextView, context: Context) {
        if uiView.text != text { uiView.text = text }
    }

    class Coordinator: NSObject, UITextViewDelegate {
        var text: Binding<String>
        init(text: Binding<String>) { self.text = text }

        func textViewDidChange(_ textView: UITextView) {
            text.wrappedValue = textView.text
        }
    }
}
```

2. **Update Propagation Without Loops**

```swift
// BAD: Infinite loop — updateUIView sets text, triggers delegate, updates binding, triggers updateUIView
func updateUIView(_ uiView: UITextView, context: Context) {
    uiView.text = text // triggers textViewDidChange -> updates binding -> triggers updateUIView
}

// GOOD: Guard against no-change updates
func updateUIView(_ uiView: UITextView, context: Context) {
    if uiView.text != text {
        uiView.text = text // only set when genuinely different
    }
}

// ALSO GOOD: Disable delegate during programmatic updates
func updateUIView(_ uiView: UITextView, context: Context) {
    context.coordinator.isUpdating = true
    uiView.text = text
    context.coordinator.isUpdating = false
}

// In coordinator:
func textViewDidChange(_ textView: UITextView) {
    guard !isUpdating else { return }
    text.wrappedValue = textView.text
}
```

3. **Sizing and Layout**

```swift
// BAD: Wrapped UIKit view has no intrinsic size — SwiftUI gives it zero frame
struct WrappedLabel: UIViewRepresentable {
    let text: String
    func makeUIView(context: Context) -> UILabel {
        let label = UILabel()
        label.text = text
        return label
    }
    func updateUIView(_ uiView: UILabel, context: Context) { uiView.text = text }
    // Missing: SwiftUI doesn't know preferred size
}

// GOOD: Provide sizing via sizeThatFits or fixedSize
struct WrappedLabel: UIViewRepresentable {
    let text: String

    func makeUIView(context: Context) -> UILabel {
        let label = UILabel()
        label.numberOfLines = 0
        label.setContentHuggingPriority(.required, for: .vertical)
        label.setContentCompressionResistancePriority(.required, for: .vertical)
        return label
    }

    func updateUIView(_ uiView: UILabel, context: Context) { uiView.text = text }

    func sizeThatFits(_ proposal: ProposedViewSize, uiView: UILabel, context: Context) -> CGSize? {
        let width = proposal.width ?? UIView.layoutFittingExpandedSize.width
        return uiView.sizeThatFits(CGSize(width: width, height: .greatestFiniteMagnitude))
    }
}
```

4. **Memory Management**

```swift
// BAD: Coordinator retains closure that captures Representable
class Coordinator {
    var onComplete: (() -> Void)?
}
struct MyView: UIViewRepresentable {
    var handleComplete: () -> Void

    func makeCoordinator() -> Coordinator {
        let c = Coordinator()
        c.onComplete = handleComplete // captures self through closure chain
        return c
    }
}

// GOOD: Use weak references and Binding for back-communication
class Coordinator: NSObject {
    var isComplete: Binding<Bool>
    init(isComplete: Binding<Bool>) { self.isComplete = isComplete }

    func didComplete() {
        isComplete.wrappedValue = true
    }
}
```

## Expected Output

```
## SwiftUI-UIKit Interop Review Report

### Summary
- **Representable types reviewed:** N
- **Coordinator lifecycle issues:** N
- **Update loop risks:** N
- **Sizing/layout issues:** N
- **Memory management issues:** N

### Findings
#### [Severity] Issue — File:Line
- **Issue:** ...
- **Recommendation:** ...
```

## Example Output

```
## SwiftUI-UIKit Interop Review Report

### Summary
- **Representable types reviewed:** 4
- **Coordinator lifecycle issues:** 1
- **Update loop risks:** 2
- **Sizing/layout issues:** 1
- **Memory management issues:** 1

### Findings

#### [Critical] Update Loop — RichTextEditor.swift:L48
- **Issue:** `updateUIView` unconditionally sets `textView.attributedText`, triggering `textViewDidChange` delegate callback, which updates the Binding, which triggers another `updateUIView`.
- **Recommendation:** Add `guard uiView.attributedText != attributedText else { return }` in `updateUIView`.

#### [Warning] Zero Height — ExpandingTextView.swift:L12
- **Issue:** Wrapped UITextView renders at zero height because no `sizeThatFits` override and no `fixedSize()` or `.frame(height:)` applied.
- **Recommendation:** Implement `sizeThatFits(_:uiView:context:)` returning text fitting size.
```

## Techniques Used

- **ST-01 (Structured Task Decomposition):** Separates coordinator, updates, sizing, memory
- **RT-02 (Role-Based Task Framing):** Reviewer acts as SwiftUI-UIKit bridge specialist
- **RT-04 (Constraint-Based Refinement):** Enforces idempotent updates and correct delegation
- **AG-02 (Automated Guardrails):** Prevents false flags on lightweight views and expected update frequency

## Related Prompts

- `ios_swiftui_view_update_review.md` — SwiftUI view performance
- `ios_core_animation_hitch_review.md` — Rendering performance at the layer boundary
- `ios_observable_state_management_review.md` — State flow through interop boundaries

## Customization Guide

- **WKWebView wrappers:** Add navigation delegate completeness and JavaScript bridge memory checks
- **MKMapView wrappers:** Add annotation reuse and region update debouncing checks
- **Camera/AVFoundation:** Add session lifecycle and preview layer sizing checks
