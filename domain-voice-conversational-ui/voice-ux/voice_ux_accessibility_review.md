---
title: "Conversational Interface Accessibility Review"
category: voice-conversational-ui/voice-ux
description: "Review a conversational interface for accessibility covering speech rate accommodation, cognitive load management, alternative input modalities, timeout handling, and multilingual support"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - QA-02
difficulty: intermediate
tags:
  - accessibility
  - voice-accessibility
  - cognitive-load
  - speech-impairment
  - inclusive-design
  - multilingual
updated: "2026-03-19"
---

# Conversational Interface Accessibility Review

**Objective:** Review a conversational interface for accessibility compliance, evaluating speech rate accommodation, cognitive load management, alternative input modalities, timeout handling, support for users with speech impairments, and multilingual accessibility.

**When to Use:**
- Use when: Launching a voice or chat interface and need accessibility review
- Use when: Receiving accessibility complaints from users
- Use when: Required to meet WCAG or organizational accessibility standards
- Use when: Expanding to markets with diverse language and ability needs
- Don't use when: Reviewing visual/web accessibility (use frontend accessibility prompts)

## Instructions

1. **Evaluate Speech and Hearing Accessibility**
   - Are speech rate and volume adjustable?
   - Is there an alternative to voice input (text, touch, switch access)?
   - Are audio responses supplemented with visual/text alternatives?
   - Is background noise handled gracefully (noise cancellation)?
   - Can users with speech impairments use the system effectively?
   - Are captions or transcripts available for audio output?

2. **Assess Cognitive Load Management**
   - Are instructions simple and unambiguous?
   - How many choices are presented at once? (optimal: 3-5 for voice, 5-7 for text)
   - Are complex tasks broken into manageable steps?
   - Is jargon avoided or explained?
   - Are users oriented about where they are in a multi-step process?
   - Can users ask for information to be repeated?

3. **Review Timeout and Pacing**
   - How long before timeout on voice input? (minimum: 5 seconds, accessible: 10+)
   - Can timeout duration be extended or disabled?
   - Is there a warning before timeout?
   - Can users pause mid-flow and resume later?
   - Are responses paced appropriately (not too fast, not too slow)?

4. **Check Alternative Input Modalities**
   - Voice: Is it the ONLY input method, or one of several?
   - Text: Can users type instead of speak?
   - Touch/Tap: Are button alternatives provided for common responses?
   - Switch access: Can users navigate with assistive switches?
   - DTMF: For phone-based systems, are keypad alternatives available?

5. **Evaluate Multilingual Accessibility**
   - Does the system detect or ask for language preference?
   - Are language switches handled gracefully mid-conversation?
   - Is the NLU model accurate for non-native speakers?
   - Are cultural communication patterns respected (directness, formality)?
   - Is the TTS voice appropriate for each language?

6. **Test with Assistive Technology**
   - Screen reader compatibility (for chat interfaces)
   - Voice control software compatibility
   - Switch access device compatibility
   - Magnification and zoom support
   - High contrast mode support

7. **CRITICAL: Validate against standards**
   - Map findings to WCAG 2.1/2.2 guidelines where applicable
   - Check against platform-specific accessibility requirements (Alexa, Google)
   - Verify that accessibility features don't degrade the experience for other users
   - Ensure no accessibility feature is "hidden" or hard to discover
   - **Confidence**: High (tested with assistive tech), Medium (evaluated), Low (theoretical)

## False-Positive Prevention (MUST follow)

- **DON'T** require perfect speech recognition as the ONLY input method
- **DON'T** set timeouts under 5 seconds for voice input
- **DON'T** present more than 5 options verbally without pagination
- **DON'T** assume all users can hear, speak, or read at the same speed
- **DO** provide at least one alternative input modality
- **DO** test with users who have actual accessibility needs
- **DO** consider situational disabilities (driving, loud environment, hands busy)

## Expected Output

```markdown
## Accessibility Review: [Application Name]

### Compliance Summary
| Area | Status | Issues | Priority |
|------|--------|--------|----------|
| Speech/Hearing | Partial | No text alternative for voice input | High |
| Cognitive Load | Good | Occasional complex prompts | Medium |
| Timeout/Pacing | Poor | 3-second timeout, no extension | Critical |
| Alternative Input | Partial | Text available, no touch/switch | Medium |
| Multilingual | N/A | English only currently | - |
| Assistive Tech | Not tested | Needs evaluation | High |

### Critical Issues
| Issue | Impact | Users Affected | Fix |
|-------|--------|---------------|-----|
| 3-second timeout | Users can't complete input | Slow speakers, elderly | Extend to 10s + warning |

### WCAG Mapping
| Finding | WCAG Criterion | Level |
|---------|---------------|-------|
| No text input alternative | 2.1.1 Keyboard | A |
| Short timeout | 2.2.1 Timing Adjustable | A |

### Recommendations
[Prioritized list with effort estimates]
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Accessibility review
- **ST-02 (Structured Sequential Instructions):** Category-by-category evaluation
- **RT-02 (Multi-Dimensional Analysis):** Speech, cognitive, timeout, input, multilingual
- **CM-02 (Constraint Specification):** WCAG standards and platform requirements
- **QA-02 (Quality Indicators):** Compliance status tracking

## Customization Guide

- **For Voice-Only Devices**: Emphasize speech alternatives, timeout handling, pacing
- **For Chat Interfaces**: Focus on screen reader compatibility, keyboard navigation
- **For Phone/IVR**: Add DTMF alternatives, hearing-impaired relay service support
- **For Children's Applications**: Simplified language, longer timeouts, reduced choices
