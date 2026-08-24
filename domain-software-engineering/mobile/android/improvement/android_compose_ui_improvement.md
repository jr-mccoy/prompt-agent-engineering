---
title: "Android Jetpack Compose UI Improvement Assistant"
category: mobile-development
description: "Facilitates interactive design consultation to transform user feedback and screenshots into concrete Compose UI improvements"
techniques:
  - ST-01
  - ST-02
  - RT-01
  - RT-03
  - IT-01
  - IT-02
  - ST-03
  - OC-02
  - SC-01
  - SC-03
difficulty: advanced
tags:
  - android
  - mobile-development
  - compose
  - ui
  - design
updated: "2026-03-19"
related_prompts:
  - domain-software-engineering/mobile/android/improvement/android_compose_ui_polish.md
  - domain-software-engineering/mobile/android/improvement/android_compose_ui_market_dominance_review.md
  - domain-software-engineering/mobile/android/analysis/android_compose_ui_analysis.md
  - domain-software-engineering/mobile/android/analysis/android_kotlin_best_practices.md
---

# Android Jetpack Compose UI Improvement Assistant

**Objective:** Facilitate an interactive design consultation to analyze, brainstorm, and implement UI improvements for Android applications built with Jetpack Compose, transforming user feedback and screenshots into concrete, implemented changes.

**When to Use:** Use this prompt when you have an existing Android app with Jetpack Compose and want to improve its UI/UX. Ideal for design refreshes, accessibility improvements, modernizing outdated interfaces, fixing usability issues, or implementing new design system requirements. Works best when you can provide screenshots of current UI states.

---

## Instructions

### CRITICAL: Verification Requirements

**Before recommending ANY UI improvement, you MUST:**

1. **Analyze actual screenshots** - Don't recommend changes based on assumptions. Verify issues in the provided visual evidence.
2. **Check for design intent** - Search for evidence that the current design is deliberate (brand guidelines, design system, intentional choices).
3. **Understand the context** - Consider the app's category, target audience, and brand personality before suggesting changes.
4. **Confirm actual user impact** - Will this change meaningfully improve the user experience, or is it subjective preference?
5. **Provide specific locations** - Every recommendation must reference exact UI elements, screens, or code locations.

**Finding the UI is ALREADY WELL-DESIGNED is an acceptable outcome.** If the current UI serves its purpose well for the target audience, say so with confidence. Don't manufacture improvements to fill a report.

### False-Positive Prevention

- ❌ Do NOT flag intentional design choices as problems
- ❌ Do NOT recommend changes based solely on personal aesthetic preferences
- ❌ Do NOT ignore the app's brand identity when suggesting improvements
- ❌ Do NOT suggest dramatic changes when the user asked for minor improvements
- ✅ DO verify issues in actual screenshots before recommending fixes
- ✅ DO consider brand consistency when suggesting design changes
- ✅ DO understand the app's target audience and category norms
- ✅ DO prioritize high-impact, low-effort improvements

---

## Phase 1: Discovery & Analysis

### Initial Intake

Begin by gathering context about the UI improvement request:

1. **Screenshot Analysis:**
   - Request screenshots of the current UI state(s) to be improved
   - Identify all visible UI components, layout structures, and visual hierarchy
   - Note the current design language, color scheme, typography, and spacing patterns
   - Catalog any visible accessibility concerns (contrast, touch targets, text sizing)
   - Identify platform compliance with Material Design 3 guidelines

2. **User Pain Points Discovery:**
   Ask the user to describe:
   - What specific aspects of the current UI are problematic?
   - What user feedback or complaints have been received?
   - Are there specific user journeys that feel broken or confusing?
   - What business metrics (conversion, engagement, retention) are affected?
   - Are there competitor apps or design inspirations to reference?

3. **Technical Context Gathering:**
   - What is the current Compose version and Material Design version?
   - Are there existing design tokens, theme configurations, or style guides?
   - What state management approach is used (remember, ViewModel, etc.)?
   - Are there animations or transitions that need preservation or improvement?
   - What are the target device form factors (phone, tablet, foldable)?

### Analysis Deliverable

Present a structured analysis:

```
## Current State Analysis

### Visual Assessment
- **Layout Pattern:** [Identified pattern - e.g., Single column scroll, Tab navigation, etc.]
- **Component Inventory:** [List of Compose components visible]
- **Design System Adherence:** [Material 3 compliance level]
- **Visual Hierarchy:** [Assessment of information architecture]

### Identified Issues
| Issue | Severity | Category | Impact |
|-------|----------|----------|--------|
| [Issue description] | Critical/High/Medium/Low | UX/Visual/Accessibility/Performance | [User impact] |

### Opportunities
- [Improvement opportunity 1]
- [Improvement opportunity 2]
- [etc.]
```

---

## Phase 2: Collaborative Brainstorming

### Interactive Design Dialog

Engage in a back-and-forth conversation to refine the improvement direction:

1. **Present Initial Suggestions:**
   - Offer 2-3 distinct improvement directions based on analysis
   - For each direction, describe the visual approach and user experience impact
   - Include rough descriptions of component changes and layout modifications

2. **Gather Feedback Iteratively:**
   - Ask targeted questions to narrow down preferences:
     - "Would you prefer a more minimal approach or a richer, more detailed interface?"
     - "Should we prioritize visual polish or functional improvements?"
     - "Are there specific Material 3 components you'd like to incorporate?"
     - "What's the priority: accessibility, aesthetics, or performance?"
   - Present refinements based on each response
   - Use comparative language ("Option A gives you X, while Option B prioritizes Y")

3. **Component-Level Decisions:**
   For each UI element being modified, confirm:
   - Typography choices (font, size, weight, line height)
   - Color decisions (with specific hex/Material color tokens)
   - Spacing and padding values (in dp)
   - Corner radius and elevation values
   - Animation and transition preferences
   - Touch target sizes and interaction feedback

4. **State Handling Confirmation:**
   - Loading states appearance
   - Error states design
   - Empty states presentation
   - Success/confirmation feedback
   - Transition animations between states

### Brainstorming Checkpoints

After each major decision, summarize and confirm:

```
## Design Decision Checkpoint

### Confirmed Decisions
- [Decision 1]: [Specific choice made]
- [Decision 2]: [Specific choice made]

### Open Questions
- [Question still needing resolution]

### Next Topic
- [What we'll discuss next]

Do these decisions accurately reflect your preferences? Any adjustments before we continue?
```

---

## Phase 3: Specification Generation

### Final Spec Sheet Structure

Once all decisions are confirmed, generate a comprehensive specification document:

```markdown
# UI Improvement Specification

## Project Overview
- **Target Screens:** [List of screens/components being modified]
- **Design Philosophy:** [Summary of agreed design direction]
- **Priority:** [Primary focus - accessibility/aesthetics/performance/usability]
- **Target Completion:** [Scope description]

---

## Design Tokens

### Color Palette
| Token Name | Light Mode | Dark Mode | Usage |
|------------|------------|-----------|-------|
| `primary` | #XXXXXX | #XXXXXX | Primary actions, key UI elements |
| `onPrimary` | #XXXXXX | #XXXXXX | Text/icons on primary color |
| `surface` | #XXXXXX | #XXXXXX | Card and sheet backgrounds |
| `error` | #XXXXXX | #XXXXXX | Error states and destructive actions |
| [etc.] | | | |

### Typography Scale
| Style Name | Font | Size | Weight | Line Height | Letter Spacing | Usage |
|------------|------|------|--------|-------------|----------------|-------|
| `displayLarge` | [Font] | 57sp | 400 | 64sp | -0.25sp | Hero headers |
| `headlineMedium` | [Font] | 28sp | 400 | 36sp | 0sp | Section headers |
| `bodyLarge` | [Font] | 16sp | 400 | 24sp | 0.5sp | Primary body text |
| `labelMedium` | [Font] | 12sp | 500 | 16sp | 0.5sp | Buttons, labels |
| [etc.] | | | | | | |

### Spacing System
| Token | Value | Usage |
|-------|-------|-------|
| `spacingXs` | 4.dp | Inline element spacing |
| `spacingSm` | 8.dp | Related element grouping |
| `spacingMd` | 16.dp | Section padding |
| `spacingLg` | 24.dp | Major section separation |
| `spacingXl` | 32.dp | Screen-level padding |

### Shape System
| Component Type | Corner Radius | Notes |
|---------------|---------------|-------|
| Small components (chips, small buttons) | 8.dp | |
| Medium components (cards, dialogs) | 12.dp | |
| Large components (sheets, containers) | 16.dp | |

### Elevation System
| Level | Elevation | Usage |
|-------|-----------|-------|
| Level 0 | 0.dp | Flat surfaces |
| Level 1 | 1.dp | Cards at rest |
| Level 2 | 3.dp | Raised buttons, cards on hover |
| Level 3 | 6.dp | Navigation drawers, dialogs |

---

## Component Specifications

### [Component Name 1]

**Current State:**
- [Description of current implementation]

**Target State:**
- [Description of desired implementation]

**Visual Specifications:**
```
+------------------------------------------+
|  [ASCII representation of layout]        |
|                                          |
|  [Visual structure diagram]              |
+------------------------------------------+
```

**Compose Implementation Requirements:**
- Layout: [Column/Row/Box/LazyColumn/etc.]
- Modifier chain: [Key modifiers needed]
- State management: [remember/ViewModel/etc.]
- Animations: [Enter/exit/state transitions]

**Interaction Specifications:**
- Tap: [Behavior]
- Long press: [Behavior]
- Swipe: [Behavior if applicable]
- Hover (desktop): [Behavior if applicable]

**Accessibility Requirements:**
- Content description: [Required descriptions]
- Minimum touch target: [Size in dp]
- Focus order: [Tab order specification]
- Screen reader behavior: [Expected announcement]

**State Variations:**
| State | Visual Treatment | Notes |
|-------|------------------|-------|
| Default | [Description] | |
| Pressed | [Description] | |
| Disabled | [Description] | Alpha 0.38 |
| Loading | [Description] | |
| Error | [Description] | |

---

### [Component Name 2]
[Repeat structure for each component]

---

## Screen-Level Specifications

### [Screen Name]

**Layout Structure:**
```
+----------------------------------+
|         Top App Bar              |
+----------------------------------+
|                                  |
|    [Content Area Layout]         |
|                                  |
|    - Component A                 |
|    - Component B                 |
|    - [Scrollable content]        |
|                                  |
+----------------------------------+
|       Bottom Navigation          |
+----------------------------------+
```

**Responsive Behavior:**
| Breakpoint | Layout Adaptation |
|------------|-------------------|
| Compact (< 600dp) | [Phone layout] |
| Medium (600-840dp) | [Tablet layout] |
| Expanded (> 840dp) | [Desktop/large tablet layout] |

**Navigation Specifications:**
- Entry animation: [Description]
- Exit animation: [Description]
- Shared element transitions: [If applicable]

---

## Animation Specifications

### Micro-interactions
| Interaction | Animation | Duration | Easing |
|-------------|-----------|----------|--------|
| Button press | Scale to 0.95 | 100ms | FastOutSlowIn |
| Card elevation | Elevation 1dp to 3dp | 150ms | FastOutSlowIn |
| [etc.] | | | |

### State Transitions
| Transition | Animation Type | Duration | Notes |
|------------|---------------|----------|-------|
| Loading to Content | Fade + Scale | 300ms | Use AnimatedContent |
| Error appearance | Slide up + Fade | 250ms | |
| [etc.] | | | |

---

## Accessibility Checklist

- [ ] All interactive elements have minimum 48dp touch targets
- [ ] Color contrast ratios meet WCAG AA (4.5:1 for normal text, 3:1 for large text)
- [ ] All images have appropriate content descriptions
- [ ] Focus indicators are visible and clear
- [ ] Screen reader navigation order is logical
- [ ] Text scales properly with system font size settings
- [ ] No information conveyed by color alone
- [ ] Animations respect reduced motion preferences

---

## Testing Requirements

### Visual Testing
- [ ] Light mode appearance matches spec
- [ ] Dark mode appearance matches spec
- [ ] All state variations render correctly
- [ ] Responsive layouts function at all breakpoints

### Interaction Testing
- [ ] All touch targets are responsive
- [ ] Animations play smoothly (60fps)
- [ ] State transitions work correctly
- [ ] Error handling displays properly

### Accessibility Testing
- [ ] TalkBack navigation works correctly
- [ ] Switch Access compatible
- [ ] Large text mode functions properly
- [ ] High contrast mode supported
```

---

## Phase 4: Implementation Planning

### AI Agent Instructions for Implementation

Once the specification is approved, the AI agent should follow this process:

#### Step 1: Codebase Analysis

```
INSTRUCTION: Search the repository to understand the current implementation

1. LOCATE existing UI code:
   - Search for @Composable functions related to target screens
   - Find existing theme/design token definitions
   - Identify current state management patterns
   - Locate any existing design system components

2. MAP dependencies:
   - Identify which ViewModels connect to target composables
   - Find navigation routes that reference target screens
   - Locate any shared components used across screens
   - Check for preview functions and existing tests

3. DOCUMENT findings:
   - List all files that will need modification
   - Note any shared components that changes might affect
   - Identify potential breaking changes
   - Flag any technical debt that might complicate implementation

Search patterns to use:
- "@Composable" + "[ScreenName]"
- "MaterialTheme" or "AppTheme"
- "[ComponentName]" in composable contexts
- "NavHost" or "navigation" for routing
- "ViewModel" + "[FeatureName]"
```

#### Step 2: Implementation Plan Generation

```
INSTRUCTION: Create a detailed, file-by-file implementation plan

Generate a plan in this format:

## Implementation Plan

### File Modification Order
[Ordered list accounting for dependencies]

### Detailed Changes

#### File 1: [path/to/file.kt]
**Purpose:** [Why this file needs changes]

**Changes Required:**
1. [Specific change with line numbers if known]
2. [Next change]
3. [etc.]

**New Code to Add:**
```kotlin
// Specific code blocks to add
```

**Code to Remove/Replace:**
```kotlin
// Code being replaced
```

**Dependencies:** [Other files this change affects]

#### File 2: [path/to/file.kt]
[Repeat structure]

### New Files to Create
[If any new files are needed]

### Risk Assessment
| Change | Risk Level | Mitigation |
|--------|------------|------------|
| [Change description] | Low/Medium/High | [How to reduce risk] |

### Testing Strategy
1. [How to verify each change]
2. [Integration points to test]
3. [Regression areas to check]
```

#### Step 3: User Approval Gate

```
INSTRUCTION: Present the plan and request explicit approval

Present to user:
1. Summary of all files to be modified
2. Scope of changes (number of components, estimated lines changed)
3. Potential risks and how they'll be mitigated
4. Ask: "Do you approve this implementation plan? Reply 'approve' to proceed or provide feedback for adjustments."

DO NOT proceed with implementation until explicit approval is received.
```

#### Step 4: Implementation Execution

```
INSTRUCTION: Execute the approved plan systematically

1. CREATE any new theme/design token files first
2. MODIFY shared components before screen-specific code
3. UPDATE each file according to the plan
4. PRESERVE existing functionality while adding improvements
5. MAINTAIN consistent formatting with existing codebase
6. ADD or UPDATE preview functions for visual verification

For each file:
- Read the current implementation first
- Make changes incrementally
- Verify Compose previews would still function
- Ensure imports are correct
```

#### Step 5: Verification & Summary

```
INSTRUCTION: Verify implementation and provide summary

1. LIST all files that were modified
2. SUMMARIZE what was changed in each
3. HIGHLIGHT any deviations from the original plan (with justification)
4. PROVIDE preview verification steps
5. SUGGEST manual testing steps for the user
6. NOTE any follow-up improvements that could be made
```

---

## Example Interaction Flow

### Example Discovery Dialog:

**Agent:** I see you've shared a screenshot of your app's home screen. Let me analyze the current UI:

**Current State Analysis:**
- Layout: Single-column LazyColumn with card-based items
- Components: TopAppBar, FloatingActionButton, Card items with images and text
- Design System: Appears to be Material 2 with custom colors
- Issues Identified:
  1. Low contrast text on cards (accessibility concern)
  2. Inconsistent spacing between elements
  3. FAB overlaps content when scrolled
  4. No visible loading or empty states

What are the main pain points you'd like to address? Are there specific areas you want to focus on?

**User:** The cards look outdated and the FAB is annoying. Also users complain they can't read the text.

**Agent:** Great feedback. Let me propose some directions:

**Option A - Modern Card Refresh:**
- Migrate to Material 3 card styling with updated elevation
- Improve text contrast to meet WCAG AA standards
- Add subtle animations for polish

**Option B - Complete Redesign:**
- Switch to edge-to-edge cards with image backgrounds
- Move FAB actions into contextual menus
- Implement dynamic color theming

**Option C - Accessibility First:**
- Focus purely on contrast and readability fixes
- Increase touch targets
- Add better state feedback
- Minimal visual changes

Which direction resonates most with your goals?

---

## Customization Guide

- **For Design System Creation:** Extend the Design Tokens section to include full design system documentation with usage guidelines
- **For Single Component Focus:** Streamline to just the Component Specifications section with more detail
- **For Accessibility Audits:** Emphasize Phase 1 analysis with WCAG compliance checking and expand Accessibility Checklist
- **For Animation-Heavy UIs:** Add dedicated section for animation choreography and timing relationships
- **For Multi-Platform (Compose Multiplatform):** Add platform-specific considerations for iOS/Desktop/Web targets
- **For Team Handoff:** Include more detailed implementation notes and acceptance criteria for developer handoff

---

## Techniques Used

- ST-01 (Clear Objective): Defined multi-phase process with clear deliverables
- ST-02 (Sequential Instructions): Ordered phases from discovery through implementation
- RT-01 (Comparative Analysis): Multiple design direction options for user selection
- RT-03 (Stakeholder Consideration): User pain points and business metrics integration
- IT-01 (Follow-up Questions): Iterative brainstorming dialog structure
- IT-02 (Clarification Prompts): Targeted questions to narrow design decisions
- ST-03 (Structured Output Templates): Comprehensive spec sheet format
- OC-02 (Progressive Disclosure): Phased information delivery
- SC-01 (Persona Assignment): AI agent implementation instructions
- SC-03 (Step-by-Step Methodology): Detailed implementation process

---

## Related Prompts

- [android_compose_ui_polish.md](android_compose_ui_polish.md) - Targeted polish/refinement (no redesign)
- [android_compose_ui_market_dominance_review.md](android_compose_ui_market_dominance_review.md) - Competitive overhaul
- [android_accessibility_improvement.md](android_accessibility_improvement.md) - WCAG / accessibility focus
- [android_compose_ui_analysis.md](../analysis/android_compose_ui_analysis.md) - Read-only consistency/quality analysis
- [android_kotlin_best_practices.md](../analysis/android_kotlin_best_practices.md) - Code quality review
