---
title: "Voice + Screen Multi-Modal Interaction Design"
category: voice-conversational-ui/multimodal
description: "Design multi-modal interactions combining voice and screen including voice-first with visual supplement, screen-first with voice shortcut, synchronized state, and adaptive layouts"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - ED-05
difficulty: advanced
tags:
  - multimodal
  - voice-screen
  - smart-display
  - adaptive-layout
  - synchronized-state
  - cross-surface
updated: "2026-03-19"
---

# Voice + Screen Multi-Modal Interaction Design

**Objective:** Design multi-modal interactions that combine voice and screen, producing interaction patterns for voice-first with visual supplement, screen-first with voice shortcut, synchronized state management, and adaptive layouts for smart displays, phones, and in-car systems.

**When to Use:**
- Use when: Building for devices with both voice and screen (Echo Show, phones, cars)
- Use when: Adding voice capabilities to an existing screen-based application
- Use when: Adding visual elements to a voice-first experience
- Use when: Designing cross-device experiences (start on speaker, continue on phone)
- Don't use when: Building for voice-only devices (use voice-design prompts)

## Instructions

1. **Define Multi-Modal Strategy**
   Choose the primary interaction paradigm:
   - **Voice-first, visual supplement**: Voice drives the interaction, screen provides context
   - **Screen-first, voice shortcut**: Screen is primary, voice accelerates common tasks
   - **Equal partners**: Both modalities are first-class interaction methods
   - **Adaptive**: Strategy shifts based on context and user behavior
   Document which strategy applies to which features.

2. **Design Voice-Screen Synchronization**
   - Screen must reflect current voice state (and vice versa)
   - When user taps a screen element, voice responds as if they said it
   - When user speaks, screen updates to show the result
   - Handle race conditions: what if user taps AND speaks simultaneously?
   - Define the "source of truth" when modalities conflict

3. **Create Interaction Patterns by Task Type**
   - **Browse/Search**: Voice query → visual results list → voice/tap selection
   - **Selection from list**: Voice reads highlights, screen shows full list, tap or say number
   - **Form filling**: Voice for quick fields, screen for complex input (address, credit card)
   - **Confirmation**: Voice summary + visual details, confirm by voice or tap
   - **Status/Dashboard**: Visual display with voice queries ("How's my order?")

4. **Design Adaptive Layouts**
   - **Smart display (Echo Show, Nest Hub)**: Large text, limited interaction, voice-primary
   - **Phone (portrait)**: Full touch interaction, voice as accelerator
   - **Tablet**: Rich visual layouts, voice for hands-free scenarios
   - **In-car**: Minimal visual (glanceable), voice-primary, safety constraints
   - **TV**: Remote + voice, 10-foot UI, limited text

5. **Handle Modality Transitions**
   - User starts with voice, switches to touch mid-interaction
   - User looking at screen, uses voice to skip navigation
   - Device loses voice capability (noisy environment) — fallback to touch
   - Device loses screen (driving, screen sleep) — fallback to voice
   - Cross-device: Start on smart speaker, continue on phone

6. **Define Content Adaptation Rules**
   Same content, different presentation per modality:
   - **Voice**: Summarize (top 3 results), offer "show more"
   - **Screen**: Show all results with visual hierarchy
   - **Both**: Voice announces key info, screen shows details
   - **Lists**: Voice reads first 3, screen shows all, "say a number to select"
   - **Errors**: Voice explains, screen shows suggestions

7. **CRITICAL: Validate multi-modal coherence**
   - Test every interaction with voice only, screen only, and both
   - Verify state synchronization across modalities
   - Ensure no feature is ONLY available via one modality (unless justified)
   - Test modality switching mid-task
   - Check that screen content is accessible (screen reader, contrast)
   - **Confidence**: High (tested on devices), Medium (prototyped), Low (designed only)

## False-Positive Prevention (MUST follow)

- **DON'T** require screen interaction for critical voice-started tasks
- **DON'T** read aloud everything displayed on screen (redundant and slow)
- **DON'T** show text that contradicts what the voice is saying
- **DON'T** assume the user is looking at the screen (they might not be)
- **DO** ensure every voice action has a visual confirmation on screen
- **DO** keep voice responses short when screen provides visual context
- **DO** test with the screen off to verify voice-only fallback works

## Expected Output

```markdown
## Multi-Modal Design: [Application Name]

### Strategy Overview
| Feature | Primary Modality | Secondary | Rationale |
|---------|-----------------|-----------|-----------|
| Search | Voice | Screen (results) | Natural to ask, browse visually |
| Checkout | Screen | Voice (confirm) | Complex input needs screen |
| Status | Voice | Screen (details) | Quick query, visual for depth |

### Interaction Patterns

#### Pattern: Search and Select
**Voice flow:**
1. User: "Show me Italian restaurants nearby"
2. System (voice): "I found 5 Italian restaurants. Bella's is closest at 0.3 miles."
3. System (screen): [Shows list of 5 with map, ratings, distance]
4. User: "Tell me more about the second one" OR [taps on second item]

#### Pattern: Form Completion
**Hybrid flow:**
1. Voice: "I'd like to make a reservation for 4 on Friday"
2. Screen: Shows form with party_size=4, date=Friday pre-filled
3. Voice: "Time? Say a time or tap one below"
4. Screen: Shows available time slot buttons
5. User: "7:30" OR [taps 7:30 PM]

### Device Adaptation Matrix
| Element | Smart Display | Phone | In-Car |
|---------|-------------|-------|--------|
| Results list | 3 visible, scroll | Full list | Voice-only, top 3 |
| Input method | Voice primary | Touch primary | Voice only |
| Confirmation | Voice + visual | Tap button | Voice "yes" |
| Images | Full size | Thumbnails | None |

### Synchronization Rules
| Event | Voice Response | Screen Update |
|-------|---------------|---------------|
| Voice search | Read top result | Show full list |
| Screen tap | Acknowledge selection | Highlight selected |
| Timeout | "Still looking?" | Show timeout notice |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Multi-modal interaction design
- **ST-02 (Structured Sequential Instructions):** Strategy → sync → patterns → layouts → transitions
- **RT-02 (Multi-Dimensional Analysis):** Device types, modalities, task types
- **CM-02 (Constraint Specification):** Device-specific constraints
- **ED-05 (Reference Class Priming):** Interaction pattern templates

## Customization Guide

- **For E-commerce**: Focus on browse/search and checkout patterns
- **For Smart Home**: Device control with status dashboard patterns
- **For Healthcare**: Patient-facing with privacy-sensitive screen content
- **For Automotive**: Strict glanceability rules, NHTSA compliance
