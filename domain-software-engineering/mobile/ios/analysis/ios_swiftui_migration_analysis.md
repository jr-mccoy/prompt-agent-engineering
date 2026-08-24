---
title: "iOS SwiftUI Migration Analysis"
category: mobile-development
description: "Assess UIKit-to-SwiftUI migration readiness with component inventory, complexity scoring, UIViewRepresentable mapping, state management transition plan, and phased migration roadmap"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - NE-02
difficulty: advanced
tags:
  - ios
  - swift
  - swiftui
  - uikit
  - migration
updated: "2026-03-20"
---

# iOS SwiftUI Migration Analysis

**Objective:** Assess an iOS app's readiness to migrate from UIKit to SwiftUI by inventorying all UI components, scoring migration complexity per screen, identifying UIViewRepresentable bridge requirements, planning state management transitions, and producing a phased migration roadmap with risk analysis.

**When to Use:** Use this prompt when planning a gradual UIKit-to-SwiftUI migration, evaluating whether SwiftUI is viable for your project's minimum deployment target, after an iOS version bump that makes SwiftUI adoption practical, or when building a business case for the migration investment.

**Prompt Type:** Comprehensive (350-500 lines)

---

## Context Gathering

Before beginning the analysis, gather context:

1. **Project State:**
   - "What is your current minimum deployment target?"
   - "What percentage of the app is UIKit vs. SwiftUI (if any SwiftUI exists)?"
   - "Are you using storyboards, XIBs, or programmatic UI?"

2. **Architecture:**
   - "What architecture pattern is in use (MVC, MVVM, VIPER, TCA)?"
   - "How is state managed currently (delegates, closures, Combine, KVO)?"
   - "Is there a navigation coordinator or router?"

3. **Goals:**
   - "Is this a full migration or a 'new screens in SwiftUI' strategy?"
   - "What timeline are you working with?"
   - "Are there specific screens or features to prioritize?"

---

## Instructions

### CRITICAL: Verification Requirements

**Before reporting ANY finding, you MUST:**

1. **Check deployment target compatibility** - Many SwiftUI APIs require iOS 15, 16, or 17+. Verify each recommendation against the actual minimum target.
2. **Assess actual complexity** - Don't score based on screen count alone. A simple screen with custom drawing is harder to migrate than a complex but standard form.
3. **Identify real blockers** - Some UIKit capabilities have no SwiftUI equivalent. These must be documented, not glossed over.
4. **Test UIViewRepresentable feasibility** - Verify that identified bridge components will actually work correctly in a SwiftUI lifecycle.

**Recommending against migration is a valid outcome.** If the app relies heavily on UIKit features without SwiftUI equivalents, or if the migration cost exceeds the benefit for the project's lifespan, say so clearly.

### False-Positive Prevention

- ❌ Do NOT assume every UIKit component has a SwiftUI equivalent
- ❌ Do NOT underestimate the effort of migrating custom UIKit views with complex gesture handling
- ❌ Do NOT ignore the learning curve for the team as a cost factor
- ❌ Do NOT recommend SwiftUI for screens that will need heavy UIViewRepresentable wrapping
- ✅ DO check that SwiftUI APIs needed are available at the minimum deployment target
- ✅ DO account for UIKit-only features (e.g., complex collection view layouts, custom transitions)
- ✅ DO evaluate whether the team has SwiftUI experience
- ✅ DO consider the hybrid UIKit+SwiftUI coexistence patterns

---

### Phase 1: Component Inventory

#### 1.1 Screen Catalog

**Enumerate every screen in the app:**

```
// Screen inventory approach:
// 1. Scan for UIViewController subclasses
// 2. Scan for SwiftUI View structs (if any)
// 3. Check storyboards and XIBs for view controller scenes
// 4. Map navigation graph (how screens connect)

// Example inventory entry:
Screen: Product Detail
├── Type: UIViewController (ProductDetailViewController.swift)
├── UI Method: Programmatic + XIB (ProductDetailView.xib)
├── Lines of Code: 340
├── Custom Views: 3 (RatingStarsView, ImageCarouselView, AddToCartButton)
├── UIKit-Specific: UICollectionViewCompositionalLayout, custom UIViewPropertyAnimator
└── Navigation: Push from ProductListVC, modal to ReviewsVC
```

| Screen | File | LOC | UI Method | Custom Views | UIKit-Specific APIs |
|--------|------|-----|-----------|-------------|-------------------|
| [Name] | [File] | [N] | [Storyboard/XIB/Programmatic] | [Count] | [List] |

#### 1.2 Custom View Inventory

**Catalog all custom UIView subclasses:**

```swift
// Categories of custom views:

// Simple (easy SwiftUI migration)
class GradientView: UIView { }          // → LinearGradient / custom Shape
class RoundedCardView: UIView { }       // → RoundedRectangle modifier
class BadgeLabel: UILabel { }           // → Text with overlay

// Medium (requires careful translation)
class AnimatedProgressBar: UIView { }   // → ProgressView + withAnimation
class ExpandableTextView: UIView { }    // → Text with .lineLimit toggle
class StarRatingView: UIView { }       // → Custom SwiftUI View with ForEach

// Complex (may need UIViewRepresentable)
class SignatureCanvasView: UIView { }   // → Canvas or UIViewRepresentable
class CustomMapAnnotationView: MKAnnotationView { }  // → Map annotation content
class RichTextEditor: UITextView { }    // → UIViewRepresentable (no SwiftUI equivalent)
```

| Custom View | Category | SwiftUI Equivalent | UIViewRepresentable Needed | Effort |
|------------|----------|-------------------|--------------------------|--------|
| [View] | [Simple/Medium/Complex] | [Equivalent or N/A] | [Yes/No] | [Hours/Days] |

#### 1.3 UIKit-Only Feature Inventory

**Identify UIKit features without direct SwiftUI equivalents:**

```swift
// Features requiring UIViewRepresentable or UIViewControllerRepresentable:

// Text and Input
UITextView with attributed text editing    // Limited in SwiftUI TextField/TextEditor
UISearchController with custom scopes      // .searchable is simpler but less flexible
UITextInput / custom keyboard              // No SwiftUI equivalent

// Collection Views
UICollectionViewCompositionalLayout        // LazyVGrid/LazyHGrid less flexible
UICollectionViewDiffableDataSource         // SwiftUI has ForEach but different model
Custom supplementary views                  // Section headers simpler in SwiftUI, custom harder

// Navigation
Custom view controller transitions         // No matchedGeometryEffect equivalent for all cases
UIPageViewController                       // TabView with .page style (limited)
UISplitViewController (complex)            // NavigationSplitView (iOS 16+)

// Media
AVPlayerViewController                     // VideoPlayer (limited customization)
Camera / UIImagePickerController           // PhotosPicker (iOS 16+) or UIViewControllerRepresentable
WKWebView                                  // No SwiftUI equivalent, must wrap

// Maps
MKMapView with heavy customization         // Map (iOS 17+) or UIViewRepresentable
Custom map overlays                         // MapContent (iOS 17+)

// Other
UIActivityViewController                   // ShareLink (iOS 16+) for simple cases
Document picker                            // .fileImporter modifier (limited)
```

---

### Phase 2: Migration Complexity Scoring

#### 2.1 Per-Screen Complexity Score

**Score each screen on five dimensions (1-5 each):**

| Dimension | 1 (Easy) | 3 (Moderate) | 5 (Hard) |
|-----------|---------|-------------|---------|
| **Layout** | Standard stack/list | Mixed layout with some custom | Complex custom layout, collection views |
| **State** | Simple local state | Shared state, some Combine | Complex state machine, KVO, delegates |
| **Navigation** | Simple push/pop | Modal + conditional flows | Custom transitions, deep linking |
| **UIKit Deps** | No UIKit-specific APIs | 1-2 UIKit-only features | Heavily UIKit-dependent |
| **Custom Views** | No custom views | 1-2 simple custom views | Multiple complex custom views |

**Composite Score:** Sum / 5

| Score Range | Migration Difficulty | Recommendation |
|-------------|---------------------|----------------|
| 1.0 - 1.8 | Easy | Migrate early, good learning opportunity |
| 1.9 - 2.8 | Moderate | Migrate in standard phase |
| 2.9 - 3.8 | Hard | Migrate with careful planning |
| 3.9 - 5.0 | Very Hard | Consider keeping in UIKit or bridging |

#### 2.2 Screen Migration Priority Matrix

```
                    Low Complexity ←→ High Complexity
                    │                              │
  High Value ──────►│  ★ MIGRATE FIRST             │  ⚠ PLAN CAREFULLY
  (frequent use,    │  Quick wins, high ROI         │  High impact but costly
   brand impact)    │                              │
                    │──────────────────────────────│
  Low Value ───────►│  ○ MIGRATE LATER             │  ✗ KEEP IN UIKIT
  (settings,        │  Easy but low priority        │  High cost, low return
   rare screens)    │                              │
```

| Screen | Complexity | Business Value | Quadrant | Migration Order |
|--------|-----------|---------------|----------|----------------|
| [Name] | [Score] | [High/Med/Low] | [Star/Warning/Circle/X] | [Phase #] |

---

### Phase 3: UIViewRepresentable Bridge Assessment

#### 3.1 Required Bridges

**For each component needing UIViewRepresentable:**

```swift
// Bridge complexity levels:

// Simple Bridge (< 1 day)
struct WebView: UIViewRepresentable {
    let url: URL
    func makeUIView(context: Context) -> WKWebView { WKWebView() }
    func updateUIView(_ webView: WKWebView, context: Context) {
        webView.load(URLRequest(url: url))
    }
}

// Medium Bridge (1-3 days) — needs Coordinator for delegates
struct CameraView: UIViewControllerRepresentable {
    @Binding var image: UIImage?
    func makeCoordinator() -> Coordinator { Coordinator(self) }
    // Coordinator handles UIImagePickerControllerDelegate
}

// Complex Bridge (3+ days) — lifecycle management, two-way binding
struct RichTextEditor: UIViewRepresentable {
    @Binding var attributedText: NSAttributedString
    @Binding var selectedRange: NSRange
    // Coordinator for UITextViewDelegate
    // updateUIView must handle external state changes
    // makeUIView must configure toolbar, input accessories
    // Keyboard management, scroll position sync
}
```

| Component | Bridge Type | Complexity | Two-Way Binding | Delegate Methods | Est. Effort |
|-----------|------------|-----------|----------------|-----------------|-------------|
| [Component] | [UIView/UIViewController] | [Simple/Medium/Complex] | [Yes/No] | [Count] | [Days] |

#### 3.2 Bridge Maintenance Cost

**Assess ongoing cost of maintaining bridges:**

- Bridges must be updated when UIKit component APIs change
- Bridges add complexity to the SwiftUI view hierarchy
- Bridges may have lifecycle mismatches (UIKit vs SwiftUI update cycle)
- Each bridge is a potential source of bugs at the framework boundary

**Decision:** If a screen requires 3+ bridges, consider keeping it in UIKit and hosting it via `UIViewControllerRepresentable` from the SwiftUI navigation layer instead.

---

### Phase 4: State Management Transition

#### 4.1 Current State Patterns

**Map existing state management to SwiftUI equivalents:**

```swift
// UIKit Pattern → SwiftUI Equivalent

// Delegate Pattern
protocol ProductDetailDelegate: AnyObject {
    func didAddToCart(_ product: Product)
}
// → Closure, @Binding, or Environment action

// KVO / didSet
var isLoading: Bool = false {
    didSet { loadingIndicator.isHidden = !isLoading }
}
// → @Published / @Observable property

// NotificationCenter
NotificationCenter.default.addObserver(self, selector: #selector(userDidLogin), ...)
// → @EnvironmentObject / @Environment or Combine publisher

// Combine
cancellable = viewModel.$items
    .receive(on: DispatchQueue.main)
    .sink { [weak self] items in self?.updateUI(items) }
// → Direct @Published binding in SwiftUI, or .onChange modifier

// Core Data
let fetchedResultsController: NSFetchedResultsController<Item>
// → @FetchRequest / @Query (SwiftData) / manual ObservableObject wrapper
```

| Current Pattern | Occurrences | SwiftUI Replacement | Migration Effort |
|----------------|-------------|-------------------|-----------------|
| Delegate | [N] | Closure / @Binding | [Per instance] |
| KVO / didSet | [N] | @Published / @Observable | [Per instance] |
| NotificationCenter | [N] | @Environment / Combine | [Per instance] |
| Combine sink in VC | [N] | Direct binding | [Per instance] |
| NSFetchedResultsController | [N] | @FetchRequest / @Query | [Per instance] |

#### 4.2 State Architecture Recommendation

**Based on current architecture, recommend SwiftUI state approach:**

```
Current Architecture → Recommended SwiftUI State

MVC (no ViewModels)
→ Extract ObservableObject ViewModels first
→ Then migrate views to SwiftUI observing those VMs
→ Benefit: ViewModels work with both UIKit and SwiftUI during transition

MVVM (ObservableObject already)
→ Views can migrate directly to SwiftUI
→ ViewModels already expose @Published properties
→ Consider @Observable macro migration (iOS 17+)

MVVM + Combine
→ Simplify: remove manual Combine subscriptions in views
→ SwiftUI handles observation automatically
→ Keep Combine for data layer transformations

TCA
→ TCA has first-class SwiftUI support
→ Migrate views, keep Reducers and Stores
→ Easiest architecture to migrate

VIPER
→ Most migration work — need to collapse Presenter/Interactor into ViewModel
→ Consider routing layer rewrite with NavigationStack
→ May benefit from architecture simplification during migration
```

---

### Phase 5: Phased Migration Plan

**CHECKPOINT:** Present migration readiness summary.

```markdown
## Migration Readiness Assessment

### Overall Readiness Score: [1-10]

| Factor | Score | Notes |
|--------|-------|-------|
| Deployment target compatibility | [1-10] | [Min iOS vs SwiftUI API needs] |
| Architecture readiness | [1-10] | [MVVM=high, MVC=low, TCA=high] |
| Component complexity | [1-10] | [Low custom views=high, heavy UIKit=low] |
| Team SwiftUI experience | [1-10] | [Estimate from code patterns] |
| UIViewRepresentable burden | [1-10] | [Few bridges=high, many=low] |

### Migration Strategy Recommendation

[Full migration / New screens only / Hybrid with timeline / Not recommended]

**Shall I proceed with the detailed phased migration plan?**
```

#### 5.1 Migration Phases

```markdown
### Phase 0: Foundation (2-4 weeks)

**Goal:** Establish infrastructure for hybrid UIKit + SwiftUI coexistence.

- [ ] Set up UIHostingController base class for embedding SwiftUI in UIKit
- [ ] Create SwiftUI preview infrastructure
- [ ] Establish @EnvironmentObject / @Environment patterns for app-wide state
- [ ] Define navigation bridging strategy (UIKit coordinator → SwiftUI NavigationStack)
- [ ] Create shared design system components in SwiftUI
- [ ] Set up SwiftUI-compatible theming / color assets

### Phase 1: Low-Risk Screens (4-8 weeks)

**Goal:** Migrate simple, low-traffic screens to build confidence.

| Screen | Current LOC | Est. SwiftUI LOC | Effort | Risk |
|--------|------------|-----------------|--------|------|
| [Settings] | [N] | [N] | [Days] | Low |
| [About] | [N] | [N] | [Days] | Low |
| [Profile Edit] | [N] | [N] | [Days] | Low |

### Phase 2: Core Screens (8-16 weeks)

**Goal:** Migrate primary user-facing screens.

| Screen | Current LOC | Est. SwiftUI LOC | Bridges Needed | Effort | Risk |
|--------|------------|-----------------|----------------|--------|------|
| [Home Feed] | [N] | [N] | [N] | [Weeks] | Medium |
| [Search] | [N] | [N] | [N] | [Weeks] | Medium |
| [Product Detail] | [N] | [N] | [N] | [Weeks] | Medium |

### Phase 3: Complex Screens (12-24 weeks)

**Goal:** Migrate remaining complex screens or establish permanent bridges.

| Screen | Current LOC | Decision | Rationale |
|--------|------------|----------|-----------|
| [Custom Editor] | [N] | [Migrate/Keep UIKit/Bridge] | [Why] |
| [Media Player] | [N] | [Migrate/Keep UIKit/Bridge] | [Why] |

### Phase 4: UIKit Removal (Ongoing)

**Goal:** Remove UIKit remnants once all screens are migrated.

- [ ] Remove storyboards and XIBs
- [ ] Remove UIKit-only extensions and utilities
- [ ] Remove UIViewRepresentable bridges where native SwiftUI alternatives become available
- [ ] Update deployment target to leverage newer SwiftUI APIs
```

---

## Expected Output

1. **Component Inventory** - Complete catalog of screens, custom views, and UIKit dependencies
2. **Complexity Scores** - Per-screen migration difficulty with priority matrix
3. **Bridge Requirements** - All UIViewRepresentable needs with effort estimates
4. **State Transition Plan** - Current → SwiftUI state management mapping
5. **Phased Migration Roadmap** - Sequenced plan with timelines and risk levels

---

## Example Interaction

**User:** We want to start migrating our iOS banking app from UIKit to SwiftUI. We're on iOS 16+ and use MVVM. Is it feasible?

**Agent:** I'll assess your migration readiness. Let me inventory the UI components and score complexity.

*[Agent catalogs screens, custom views, and UIKit dependencies]*

**Agent:**

## Migration Readiness Assessment

### Overall Readiness Score: 7/10

| Factor | Score | Notes |
|--------|-------|-------|
| Deployment target | 8/10 | iOS 16+ unlocks NavigationStack, ShareLink, Charts |
| Architecture readiness | 9/10 | MVVM with ObservableObject — ideal for SwiftUI |
| Component complexity | 6/10 | 4 screens use UICollectionViewCompositionalLayout heavily |
| Team SwiftUI experience | 5/10 | No existing SwiftUI code found — learning curve |
| UIViewRepresentable burden | 7/10 | 6 bridges needed, 2 complex (document scanner, signature) |

### Recommendation: Phased hybrid migration

Your MVVM architecture is well-suited for SwiftUI. The main challenges are:
1. **Transaction list** uses UICollectionViewCompositionalLayout with complex cells — `LazyVStack` with sticky headers achievable but different
2. **Document scanner** and **signature capture** will need permanent UIViewRepresentable bridges
3. **Custom chart views** can migrate to Swift Charts (iOS 16+)

I recommend: Phase 0 foundation work, then migrate Settings and Profile first, followed by Account Dashboard and Transaction Detail.

**Shall I proceed with the detailed per-screen migration plan?**

---

## Techniques Used

- **ST-01** (Clear Objective): Focused migration readiness assessment
- **ST-02** (Sequential Instructions): Phased inventory, scoring, and planning process
- **RT-02** (Multi-Dimensional Analysis): Five-dimension complexity scoring per screen
- **NE-02** (Guided Exploration): Progressive assessment from inventory through actionable plan

---

## Related Prompts

- [ios_architecture_review.md](ios_architecture_review.md) - Architecture evaluation (do this first)
- [ios_technical_debt_assessment.md](ios_technical_debt_assessment.md) - Debt that should be addressed before migration
- [ios_codebase_health_assessment.md](ios_codebase_health_assessment.md) - Overall health check
- [ios_performance_audit.md](ios_performance_audit.md) - Performance baseline before migration

---

## Customization Guide

### For iOS 17+ Minimum Target
- Recommend @Observable macro over ObservableObject
- Use SwiftData instead of Core Data @FetchRequest
- Leverage MapKit for SwiftUI (MapContentBuilder)
- Use new onChange(of:initial:) API
- Use #Preview macro instead of PreviewProvider

### For Large Team Migration
- Add team training phase to roadmap
- Recommend feature-flag-based SwiftUI rollout
- Plan for parallel UIKit and SwiftUI implementations during transition
- Establish SwiftUI code review guidelines and patterns document

### For Apps with Heavy Custom Drawing
- Evaluate Canvas vs UIViewRepresentable for each drawing component
- Check if Metal/Core Graphics usage can stay in UIViewRepresentable permanently
- Consider whether custom shapes can use SwiftUI Shape protocol
- Benchmark drawing performance in SwiftUI vs UIKit

### For Accessibility-Heavy Apps
- SwiftUI has stronger default accessibility support
- Audit current UIAccessibility customizations for SwiftUI equivalents
- Test VoiceOver with hybrid UIKit+SwiftUI navigation
- Verify Dynamic Type support translates correctly
