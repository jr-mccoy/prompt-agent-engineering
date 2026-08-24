---
name: mobile-ui-element-audit
description: "Perform hyper-detailed, pixel-level audits of individual mobile UI elements analyzing visual design, interaction states, micro-animations, accessibility, engagement potential, and platform compliance. Produces scored assessments with prioritized improvement plans and exact implementation specifications. Use this skill when auditing a button, navigation bar, card, input, modal, list, header, or any specific UI element, or when a developer mentions 'UI audit', 'element review', 'polish this component', 'make this button better', 'improve this card', or 'pixel perfect'."
metadata:
  tags:
    - mobile
    - ui
    - ux
    - audit
    - element-analysis
    - design-review
    - accessibility
    - engagement
    - polish
  updated: "2026-02-27"
---

# Mobile UI Element Audit

Perform surgical, element-level audits of any mobile UI component. Analyze visual design, interaction states, micro-animations, accessibility compliance, engagement potential, and platform fit. Produce scored assessments with prioritized, implementation-ready improvement plans.

## Purpose

Most UI reviews are too broad — they look at entire screens and miss the details that separate good apps from great ones. This skill zooms into individual elements and analyzes them across 10 dimensions at a level of detail that catches every gap, from missing interaction states to suboptimal animation timing to engagement opportunities.

## When to Use This Skill

Use this skill when you need to:
- Audit a specific UI element (button, card, nav bar, input, toggle, modal, etc.)
- Polish a component to best-in-class quality
- Identify missing interaction states (pressed, disabled, loading, error, empty)
- Evaluate animation and transition quality
- Check accessibility compliance at the element level
- Assess engagement potential of interactive elements
- Compare your element against industry best practices
- Prepare for design reviews or app store submission

## When NOT to Use This Skill

Do NOT use this skill when:
- Reviewing entire screens or flows (use a broader UI review approach)
- Focusing on business logic or data layer
- Working on app architecture without UI implications
- Need competitive teardown of other apps (use mobile-ui-competitive-teardown agent)

## Audit Process

### Step 1: Element Identification

Before auditing, clearly identify:
```
Element: [e.g., "Primary CTA button on checkout screen"]
Platform: [iOS / Android / Both]
Tech stack: [SwiftUI / UIKit / Compose / View / React Native / Flutter]
Current state: [Description or screenshot reference]
User context: [Where in the flow does this element appear?]
Business goal: [What should this element achieve?]
```

### Step 2: 10-Dimension Scoring

Score each dimension 1-10 with specific justification:

#### Dimension 1: Visual Polish (Weight: 15%)

**What to evaluate:**
- Color contrast against background (measure actual ratio)
- Corner radius consistency with app's design system
- Shadow/elevation appropriateness for the element's hierarchy level
- Padding/margin precision (should follow 4pt/8pt grid)
- Icon alignment and sizing relative to text
- Typography: correct weight, size, and color for the element type
- Border treatment consistency
- Dark mode appearance

**Scoring guide:**
| Score | Criteria |
|-------|---------|
| 1-3 | Inconsistent with design system, poor contrast, misaligned |
| 4-6 | Functional but lacks refinement, minor inconsistencies |
| 7-8 | Clean, consistent, matches design system well |
| 9-10 | Pixel-perfect, premium feel, intentional design choices |

#### Dimension 2: Interaction Feedback (Weight: 15%)

**What to evaluate:**
- Touch response time (< 100ms to visual change)
- Press state visual change (scale, color, opacity, ripple)
- Release animation (spring back, bounce, snap)
- Long-press behavior (if applicable)
- Haptic feedback pairing (appropriate type and timing)
- Sound feedback (if applicable)
- Visual confirmation of successful action

**Scoring guide:**
| Score | Criteria |
|-------|---------|
| 1-3 | No feedback, or delayed > 200ms, or jarring |
| 4-6 | Basic feedback (color change only), no animation or haptic |
| 7-8 | Smooth animation + haptic, feels responsive |
| 9-10 | Delightful, satisfying interaction with perfect timing |

#### Dimension 3: State Completeness (Weight: 12%)

**Required states for interactive elements:**
```
□ Default — Resting appearance
□ Pressed/Active — During touch
□ Focused — Keyboard/accessibility focus
□ Disabled — Cannot be interacted with
□ Loading — Performing async operation
□ Error — Something went wrong
□ Success — Action completed successfully
□ Empty — No content to display (for containers)
□ Hover — Mouse/trackpad (iPadOS, desktop mode)
```

**Scoring guide:**
| Score | Criteria |
|-------|---------|
| 1-3 | Only default state exists |
| 4-6 | Has default + pressed + disabled |
| 7-8 | All primary states designed (default, pressed, disabled, loading, error) |
| 9-10 | Every possible state designed with smooth transitions between them |

#### Dimension 4: Animation Quality (Weight: 10%)

**What to evaluate:**
- Duration appropriate for the action type (see timing reference)
- Easing curve matches the motion intent (ease-out for entrances, ease-in for exits)
- Spring physics used where organic motion is desired
- No jarring jumps or pops
- Animation serves a purpose (communicates state change, provides feedback)
- Performance: runs at 60fps, no jank or frame drops

**Timing reference:**
| Animation | Ideal Duration | Ideal Easing |
|-----------|---------------|-------------|
| Button press | 80-120ms | ease-out |
| State change | 200-300ms | ease-in-out |
| Expand/reveal | 250-350ms | ease-out |
| Dismiss/collapse | 200-250ms | ease-in |
| Enter screen | 300-400ms | ease-out |
| Exit screen | 250-300ms | ease-in |

#### Dimension 5: Accessibility (Weight: 12%)

**What to evaluate:**
- Touch target size (minimum 44x44pt iOS / 48x48dp Android)
- Color contrast ratio (minimum 4.5:1 for text, 3:1 for UI components)
- VoiceOver/TalkBack label (accurate, concise, includes state)
- Accessibility hint (describes what will happen when activated)
- Dynamic type support (text scales appropriately at all sizes)
- Color independence (information not conveyed by color alone)
- Focus order (logical tab/swipe order)
- Custom accessibility actions (if element has gestures)

**Scoring guide:**
| Score | Criteria |
|-------|---------|
| 1-3 | Fails contrast, tiny touch targets, no accessibility labels |
| 4-6 | Meets minimum WCAG AA, basic labels exist |
| 7-8 | WCAG AA compliant, good labels and hints, dynamic type works |
| 9-10 | WCAG AAA compliant, rich accessibility experience, custom actions |

#### Dimension 6: Engagement Potential (Weight: 10%)

**What to evaluate:**
- Does the element draw appropriate visual attention?
- Is it satisfying to interact with (tap, swipe, toggle)?
- Does it create desire for repeated interaction?
- Can it surface variable/personalized content?
- Does it provide social proof or social reward?
- Does it contribute to a larger engagement loop?
- Does interaction create user investment?

#### Dimension 7: Consistency (Weight: 8%)

**What to evaluate:**
- Matches the app's design system tokens (colors, spacing, typography, corners)
- Behaves consistently with similar elements elsewhere in the app
- Follows platform conventions (Material Design / Human Interface Guidelines)
- Uses the same animation timing and easing as other elements

#### Dimension 8: Performance (Weight: 6%)

**What to evaluate:**
- Renders without visible delay
- Animations run at 60fps
- No layout shift or size jumps during loading
- Efficient use of resources (no unnecessary recomposition/re-rendering)
- Works smoothly on lower-end devices

#### Dimension 9: Platform Fit (Weight: 6%)

**What to evaluate:**
- Follows platform conventions (iOS elements feel iOS-native, Android feels Material)
- Uses platform-appropriate gestures and patterns
- Respects system settings (dynamic type, dark mode, reduce motion)
- Uses platform-standard components where appropriate (don't reinvent system buttons)

#### Dimension 10: Emotional Impact (Weight: 6%)

**What to evaluate:**
- Does the element evoke the intended emotional response?
- Does it contribute to the app's overall personality/brand?
- Is the visual design emotionally appropriate for the context (e.g., calming for meditation, energetic for fitness)?
- Do micro-interactions create delight or just function?

### Step 3: Calculate Overall Score

```
Overall Score = Σ (Dimension Score × Weight)

Rating Scale:
  90-100: Exceptional — Best-in-class element
  80-89:  Excellent — Minor polish opportunities
  70-79:  Good — Several meaningful improvements available
  60-69:  Adequate — Functional but lacking polish
  50-59:  Needs Work — Multiple significant gaps
  Below 50: Major Redesign — Fundamental issues
```

### Step 4: Prioritized Improvement Plan

Rank improvements by impact score:

```
Impact Score = (Points Gained × Dimension Weight) / Implementation Effort

Implementation Effort Scale:
  1 = Trivial (< 1 hour, single file change)
  2 = Small (1-4 hours, 1-3 files)
  3 = Medium (4-16 hours, design + code changes)
  4 = Large (1-2 weeks, multiple systems)
  5 = Major (2+ weeks, requires design system changes)
```

### Step 5: Improvement Specifications

For each improvement, provide:

```
Improvement: [Title]
Dimension: [Which dimension it improves]
Current Score: [X/10] → Target Score: [Y/10]
Priority: [High/Medium/Low based on impact score]

Current State:
  [Exact description of current implementation]

Target State:
  [Exact description of desired implementation]

Specifications:
  - Colors: [Hex values]
  - Dimensions: [dp/pt values]
  - Animation: [Duration, easing, properties]
  - Haptic: [Type and timing]
  - Accessibility: [Labels, hints, traits]

Implementation Notes:
  - [Platform-specific guidance]
  - [Code pattern or approach]
  - [Potential gotchas]

Reference:
  - [App that does this well]
  - [Why their approach works]
```

## Element-Specific Checklists

### Buttons
```
□ Touch target ≥ 44x44pt / 48x48dp
□ Press state responds < 100ms
□ Disabled state is visually distinct but not invisible
□ Loading state replaces text with spinner (same button size)
□ Primary vs secondary vs tertiary hierarchy is clear
□ Text is legible at all dynamic type sizes
□ Icon + text alignment is vertically centered
□ Corner radius matches design system
□ Min-width ensures button doesn't look cramped with short labels
```

### Cards
```
□ Consistent padding (typically 16dp/16pt)
□ Shadow/elevation matches card hierarchy
□ Press state (if tappable) — slight scale + elevation change
□ Content truncation is handled gracefully (ellipsis, max lines)
□ Image loading shows placeholder/skeleton
□ Empty state if card content is dynamic
□ Swipe actions (if applicable) have discoverable hints
□ Card spacing in lists is consistent
```

### Navigation Bars
```
□ Active tab is visually prominent (color, weight, icon fill)
□ Inactive tabs are clearly secondary but still legible
□ Tab switching has smooth animation (crossfade or slide)
□ Badge indicators are positioned correctly and sized appropriately
□ Labels are concise (1 word ideal, 2 words max)
□ Touch targets extend to full tab width
□ Haptic feedback on tab switch (selection type)
□ Bar height and content follow platform conventions
```

### Text Inputs
```
□ Placeholder text is helpful and disappears on focus
□ Focus state has clear visual indicator (border color, label animation)
□ Error state shows inline message below field (red border + text)
□ Character count shown if max length exists
□ Keyboard type matches input (email, phone, URL, number)
□ Autocorrect/autocapitalize appropriate for field type
□ Clear button appears when text is entered
□ Secure text toggle for password fields
□ Multiline inputs grow smoothly with content
```

### Modals & Bottom Sheets
```
□ Scrim/overlay behind modal (60% black typical)
□ Entry animation: slide up + fade (300ms ease-out)
□ Exit animation: slide down + fade (250ms ease-in)
□ Swipe-to-dismiss with velocity threshold
□ Handle/grabber indicator at top of bottom sheets
□ Respects safe areas (notch, home indicator)
□ Focus trap — VoiceOver/TalkBack stays in modal
□ Dismiss on scrim tap (unless destructive content)
```

## Best Practices Summary

1. **Audit one element at a time** — depth over breadth
2. **Score before improving** — establish a baseline to measure against
3. **Fix high-weight dimensions first** — visual polish and interaction feedback are 30% of the score
4. **Provide exact values** — "make it bigger" is not an improvement specification
5. **Include before/after descriptions** — help the implementer visualize the transformation
6. **Reference best-in-class examples** — "like Instagram's like button animation" is more helpful than abstract descriptions
7. **Consider the element in context** — an element that scores 10/10 in isolation but clashes with the screen is not actually great
8. **Test with real users** — scores predict quality but user testing confirms it
9. **Re-audit after changes** — verify improvements actually improved the score
10. **Document audit results** — build an audit history to track quality improvement over time

## Related Skills

- `mobile-ui-micro-interactions` - Implement animation and haptic improvements identified by audits
- `mobile-ui-habit-loop-design` - Design engagement loops using audit findings on engagement potential
- `jetpack-compose-patterns` - Implement Compose UI improvements from audit recommendations
