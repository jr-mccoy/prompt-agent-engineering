---
title: "Google Actions Project Review"
category: voice-conversational-ui/voice-design
description: "Review a Google Actions project for best practices including scene-based architecture, type definitions, webhook fulfillment patterns, and cross-surface handling"
techniques:
  - ST-01
  - RT-02
  - RT-05
  - CM-01
  - DS-06
difficulty: advanced
tags:
  - google-actions
  - google-assistant
  - voice-ui
  - scene-architecture
  - webhook-fulfillment
  - cross-surface
updated: "2026-03-19"
---

# Google Actions Project Review

**Objective:** Review an existing Google Actions project for adherence to best practices, evaluating scene-based architecture, type definitions, webhook fulfillment patterns, cross-surface handling, and overall conversational quality.

**When to Use:**
- Use when: Auditing an existing Google Actions project before launch
- Use when: Debugging user drop-off or confusion in a Google Assistant action
- Use when: Evaluating whether an Action follows Google's design guidelines
- Don't use when: Starting a new project from scratch (use `voice_design_interaction_model_builder.md`)

## Instructions

1. **Review Scene Architecture**
   - Map the scene graph and identify all scene transitions
   - Verify each scene has clear entry conditions and exit paths
   - Check for orphaned scenes (unreachable states)
   - Evaluate slot filling within scenes vs across scenes
   - Ensure the Main invocation scene routes correctly

2. **Evaluate Type Definitions**
   - Review custom types for completeness and synonym coverage
   - Check that built-in types (actions.type.DateTime, etc.) are used where appropriate
   - Verify type entity values cover expected user inputs
   - Assess free-form vs enumerated type decisions

3. **Analyze Webhook Fulfillment**
   - Review handler organization and naming conventions
   - Check for proper use of `conv.session.params` vs `conv.user.params`
   - Evaluate error handling in webhook responses
   - Verify webhook timeout handling (5-second limit)
   - Check for proper scene transition from webhooks

4. **Assess Cross-Surface Handling**
   - Verify responses adapt to surface capabilities (smart speaker, smart display, phone)
   - Check that rich responses (cards, carousels) have voice-only fallbacks
   - Evaluate media responses for audio-only surfaces
   - Test screen-transfer flows where applicable

5. **Review Conversation Quality**
   - Evaluate system prompts for natural conversational tone
   - Check suggestion chips for discoverability
   - Review no-match and no-input handling per scene
   - Verify the action handles unexpected intents gracefully
   - Assess conversation repair strategies

6. **CRITICAL: Validate findings**
   - Test each finding against Google's Actions design guidelines
   - Verify that flagged issues actually impact user experience
   - Check if patterns have platform-specific justifications
   - **Confidence levels**: High (violates guidelines), Medium (suboptimal), Low (potential improvement)

## False-Positive Prevention (MUST follow)

- **DON'T** flag simple Actions for lacking scene complexity
- **DON'T** criticize webhook usage when client-side fulfillment suffices
- **DON'T** require rich responses on every turn (voice-first is valid)
- **DO** consider the Action's category (transactions, media, information) when evaluating
- **DO** verify that "missing" features aren't handled by platform defaults
- **DO** test recommendations against actual Google Assistant behavior

## Expected Output

```markdown
## Google Actions Review: [Action Name]

### Architecture Overview
- **Scenes:** [Count] scenes, [Count] transitions
- **Types:** [Count] custom, [Count] built-in
- **Webhooks:** [Count] handlers
- **Surface Support:** Speaker / Display / Phone / Auto

### Findings

#### Finding 1: [Issue Title]
- **Severity:** High | Medium | Low
- **Confidence:** High | Medium | Low
- **Location:** [Scene/handler name]
- **Evidence:** [Specific configuration or code]
- **Recommendation:** [Fix with example]

### Cross-Surface Matrix
| Response | Speaker | Display | Phone |
|----------|---------|---------|-------|
| [Response] | [How handled] | [How handled] | [How handled] |

### Prioritized Recommendations
[Ranked list with effort estimates]
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Specific review goal
- **RT-02 (Multi-Dimensional Analysis):** Scenes, types, webhooks, surfaces, quality
- **RT-05 (Evidence-Based Reasoning):** Requires evidence for each finding
- **CM-01 (Explicit Context Framing):** Google Actions-specific constraints
- **DS-06 (Prioritization Guidance):** Impact-ranked recommendations

## Customization Guide

- **For Transactional Actions**: Add payment flow review, order update handling
- **For Media Actions**: Focus on media playback controls, queue management
- **For Smart Home Actions**: Evaluate device traits, SYNC/QUERY/EXECUTE handlers
