---
name: mobile_ui_element_audit
description: Orchestrate a comprehensive UI element audit across trend research, element-level analysis, engagement optimization, and implementation planning to transform specific mobile UI elements from functional to exceptional
version: "1.0.0"
category: mobile-development
tags: [mobile, ui, ux, audit, element-analysis, micro-interaction, engagement, polish, ios, android]
agents_used: [mobile-ui-trend-researcher, mobile-ui-element-analyzer, mobile-ui-addiction-architect]
---

Orchestrate a comprehensive mobile UI element audit, coordinating 3 specialized agents across 4 phases to analyze, score, and produce implementation-ready improvement plans for specific UI elements:

[Extended thinking: This workflow performs surgical, element-level UI analysis rather than broad screen-level review. The key insight is that the difference between good and exceptional apps is in the details — the button press animation timing, the card shadow depth, the haptic feedback pairing, the loading state design. Users don't consciously notice these details, but they feel them. This workflow systematically evaluates every dimension of a UI element and produces exact specifications for improvement.

The workflow uses 3 specialized agents, each optimized for a distinct analytical lens:
- Trend Researcher (Opus): Context — what do best-in-class apps do with this element type?
- Element Analyzer (Opus): Depth — score every dimension of the current implementation
- Addiction Architect (Opus): Engagement — how can this element drive habit and delight?

Two user interaction gates ensure the developer controls scope and priorities:
1. After trend context: Developer confirms which trends and benchmarks are relevant
2. After scoring: Developer selects which improvements to implement

The workflow delivers exact specifications — hex colors, dp/pt dimensions, ms timing, easing curves — not vague design advice.]

## Configuration

### Supported Flags
- `--element=<element-type>`: Specify the element type (button, card, nav-bar, input, modal, list, toggle, header, fab, search-bar, pull-to-refresh, onboarding, empty-state)
- `--platform=ios|android|both`: Target platform (default: both)
- `--depth=quick|standard|deep`: Quick scores only, standard analysis, or deep with code samples (default: standard)
- `--focus=visual|interaction|engagement|accessibility|all`: Focus area (default: all)

### Parameters
- `$ARGUMENTS`: Description of the specific UI element(s) to audit, plus path to the project if code review is needed

## Phase 1: Trend Context & Benchmarking

### 1. Best-in-Class Research
- Use Task tool with subagent_type="mobile-ui-trend-researcher"
- Prompt: "Research current best practices and trends for the following mobile UI element: $ARGUMENTS.

  Provide:
  1) The top 5 apps that execute this element type exceptionally well (name + specific description of what makes their version great)
  2) Current design trends for this element type (2025-2026) — visual style, animation patterns, interaction patterns
  3) Platform-specific conventions (iOS Human Interface Guidelines vs Material Design 3) for this element
  4) Common mistakes and anti-patterns to avoid with this element type
  5) The single most impactful trend that could be applied to improve this element

  Be specific — include colors, timing, dimensions, and behavior descriptions, not vague inspiration."
- Expected output: Trend context report with specific benchmarks and best-in-class examples
- Context: This is the first phase — establishes the quality bar for the element

### USER INTERACTION GATE 1
Present the trend context to the developer and ask:

"Here are the best-in-class examples and current trends for your element type. Before I analyze your implementation:

1. **Which benchmark apps** are most relevant to your app's style and audience?
2. **Which trends** do you want me to prioritize in my recommendations?
3. **Any specific aspects** of the element you're most concerned about?

This helps me focus the analysis on what matters most to you."

**STOP and wait for developer response. Do not proceed to Phase 2 until the developer has provided direction.**

## Phase 2: Element Scoring & Analysis

### 2. Hyper-Detailed Element Analysis
- Use Task tool with subagent_type="mobile-ui-element-analyzer"
- Prompt: "Perform a comprehensive audit of the following UI element: $ARGUMENTS.

  Context from trend research: [TREND CONTEXT FROM PHASE 1]
  Developer's focus areas: [DEVELOPER INPUT FROM GATE 1]
  Benchmark apps: [SELECTED BENCHMARKS FROM GATE 1]

  Score the element across all 10 dimensions (1-10 each):
  1. Visual Polish (15%) — color, contrast, typography, spacing, shadows, consistency
  2. Interaction Feedback (15%) — touch response time, press states, release animation, haptic
  3. State Completeness (12%) — default, pressed, focused, disabled, loading, error, success, empty
  4. Animation Quality (10%) — timing, easing, purpose, performance
  5. Accessibility (12%) — touch targets, contrast ratios, VoiceOver/TalkBack, dynamic type
  6. Engagement Potential (10%) — visual magnetism, interaction satisfaction, variable reward potential
  7. Consistency (8%) — design system compliance, cross-app consistency
  8. Performance (6%) — render speed, animation framerate, resource efficiency
  9. Platform Fit (6%) — follows platform conventions, respects system settings
  10. Emotional Impact (6%) — evokes intended feeling, contributes to app personality

  For each dimension:
  - Current score with specific justification
  - What's working well (preserve these)
  - What's falling short (specific gaps)
  - Exact before/after specification for improvement

  Calculate overall weighted score.

  Identify the top 5 improvements ranked by impact-to-effort ratio. For each improvement, provide:
  - Exact specifications (hex colors, dp/pt dimensions, ms timing, easing curves)
  - Platform-specific implementation notes
  - Best-in-class app that does this well
  - Expected score improvement"
- Expected output: Complete 10-dimension scored audit with prioritized improvement plan
- Context from previous: Trend context from Phase 1, developer focus from Gate 1

### USER INTERACTION GATE 2
Present the scored audit to the developer and ask:

"Here's the complete audit with scores and prioritized improvements. Please review and let me know:

1. **Which improvements** do you want to implement? (You can approve all, or select specific ones by priority number)
2. **Any scores that surprise you?** I can explain the reasoning in more detail.
3. **Implementation preference:** Do you want code-level specifications, or design specifications only?

I'll design the engagement optimization and implementation plan based on your selections."

**STOP and wait for developer response. Do not proceed to Phase 3 until the developer has selected improvements.**

## Phase 3: Engagement Enhancement

### 3. Engagement Layer Design
- Use Task tool with subagent_type="mobile-ui-addiction-architect"
- Prompt: "Design engagement enhancements for the following UI element based on the audit findings: $ARGUMENTS.

  Audit results: [AUDIT SCORES FROM PHASE 2]
  Selected improvements: [DEVELOPER SELECTIONS FROM GATE 2]
  Benchmark apps: [SELECTED BENCHMARKS FROM GATE 1]

  For the selected improvements, add an engagement layer:
  1. How can this element contribute to the app's core engagement loop?
  2. What micro-reward can interacting with this element provide (haptic, animation, sound)?
  3. Can this element surface variable or personalized content?
  4. Can this element incorporate social proof or social reward?
  5. Does interaction with this element create user investment?
  6. What emotional response should this element trigger?

  For each engagement recommendation:
  - The specific psychological mechanism at work
  - A reference app that uses this pattern
  - Exact UI specification (animation timing, haptic type, visual treatment)
  - How it integrates with the improvements already selected

  Keep engagement enhancements subtle and value-driven — never manipulative."
- Expected output: Engagement enhancement specifications for each selected improvement
- Context from previous: Audit scores from Phase 2, developer selections from Gate 2

## Phase 4: Implementation Specification

### 4. Final Implementation Plan
- Use Task tool with subagent_type="mobile-ui-element-analyzer"
- Prompt: "Produce the final implementation specification for the UI element improvements: $ARGUMENTS.

  Combine the following into a single, implementation-ready specification:
  - Selected improvements from the audit: [PHASE 2 SELECTIONS]
  - Engagement enhancements: [PHASE 3 OUTPUT]

  For each improvement, provide:
  1. **Before state:** Exact description of current implementation
  2. **After state:** Exact description of target implementation
  3. **Visual specifications:**
     - Colors (hex values for light and dark mode)
     - Dimensions (dp for Android, pt for iOS)
     - Corner radius, shadow, elevation
     - Typography (font, weight, size, line height)
  4. **Interaction specifications:**
     - Touch feedback (scale, opacity, color change values)
     - Animation timing (duration in ms, easing curve name)
     - Haptic feedback (type and timing)
  5. **State specifications:**
     - Every state the element needs (default, pressed, disabled, loading, error, success)
     - Transition animation between states
  6. **Accessibility specifications:**
     - VoiceOver/TalkBack label and hint
     - Touch target dimensions
     - Dynamic type behavior
  7. **Platform-specific code patterns** (if requested by developer):
     - Compose/SwiftUI code snippets
     - Key modifier/view modifier chains

  Order the improvements by implementation sequence (dependencies first, quick wins before large changes).

  End with a re-scoring prediction: what the overall score should be after all improvements are implemented."
- Expected output: Complete implementation specification with exact values and predicted score improvement
- Context from previous: All previous phase outputs

## Success Criteria

### Analysis Criteria
- ✅ All 10 dimensions scored with specific justification
- ✅ Overall weighted score calculated
- ✅ Top 5 improvements identified and prioritized
- ✅ Best-in-class benchmarks referenced for each improvement

### Engagement Criteria
- ✅ Engagement enhancements are specific and implementable
- ✅ Psychological mechanisms are named and referenced
- ✅ Enhancements are ethical and value-driven
- ✅ Each enhancement references a real app example

### Implementation Criteria
- ✅ Every specification includes exact values (hex, dp/pt, ms)
- ✅ Both light and dark mode are addressed
- ✅ Accessibility requirements are met (WCAG AA minimum)
- ✅ Platform-specific guidance is provided for target platform(s)
- ✅ Implementation sequence is dependency-ordered

### Process Criteria
- ✅ Developer was consulted at both interaction gates
- ✅ No improvements implemented without developer selection
- ✅ Analysis covers the element in context (not just in isolation)

## Coordination Notes

- **Phase ordering is strict:** Trend Context → Element Scoring → Engagement Enhancement → Implementation Specification. Each phase builds on previous output.
- **User gates are essential:** Gate 1 sets the quality bar and focus. Gate 2 selects scope. Without developer input, the analysis may optimize for the wrong things.
- **Depth scales with flag:** `--depth=quick` produces scores + top 3 improvements only. `--depth=standard` adds full specifications. `--depth=deep` adds code snippets.
- **Context passing:** The trend context from Phase 1 calibrates the scoring in Phase 2. The engagement layer from Phase 3 enriches the implementation spec in Phase 4.
- **Single element focus:** This workflow is designed for 1-3 related elements, not full-screen audits. For broader UI reviews, run this multiple times for different element groups.

Target: $ARGUMENTS
