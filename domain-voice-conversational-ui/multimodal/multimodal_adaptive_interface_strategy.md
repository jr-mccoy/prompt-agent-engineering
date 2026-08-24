---
title: "Adaptive Interface Strategy"
category: voice-conversational-ui/multimodal
description: "Create an adaptive interface strategy that adjusts modality based on context including device capability detection, modality selection logic, graceful degradation, and content adaptation"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - DS-06
difficulty: advanced
tags:
  - adaptive-interface
  - context-aware
  - modality-switching
  - graceful-degradation
  - situational-awareness
  - device-detection
updated: "2026-03-19"
---

# Adaptive Interface Strategy

**Objective:** Create an adaptive interface strategy that adjusts interaction modality based on user context (driving, hands-busy, eyes-busy, noisy environment), producing specifications for device capability detection, modality selection logic, graceful degradation, and content adaptation per surface.

**When to Use:**
- Use when: Building an application that must work across multiple devices and contexts
- Use when: Users interact with your system in varied physical situations
- Use when: Designing a "works everywhere" conversational experience
- Use when: Users switch between devices (phone → car → smart speaker) during a task
- Don't use when: Building for a single fixed device type

## Instructions

1. **Map User Contexts and Constraints**
   Identify the situations your users are in:
   - **Hands-free, eyes-free** (driving, cooking): Voice-only
   - **Hands-free, eyes-available** (watching smart display): Voice + glanceable visuals
   - **Hands-available, eyes-busy** (walking): Touch + audio feedback
   - **Hands-available, eyes-available** (sitting with phone): Full multi-modal
   - **Noisy environment** (subway, bar): Text + visual, voice unreliable
   - **Quiet/social environment** (library, meeting): Text-only, no audio

2. **Design Device Capability Detection**
   Determine what each device can do:
   - Microphone: present, quality, far-field vs near-field
   - Speaker: present, quality, volume level
   - Screen: present, size, touch capability
   - Camera: for gesture recognition if applicable
   - Connectivity: online, offline, low bandwidth
   - Detect dynamically: headphones connected, car Bluetooth, screen orientation

3. **Build Modality Selection Logic**
   Create decision rules:
   ```
   IF device.hasScreen AND user.context == "stationary":
       primary = SCREEN, secondary = VOICE
   ELIF device.hasMic AND user.context == "driving":
       primary = VOICE, secondary = AUDIO_ONLY
   ELIF environment.noisy:
       primary = SCREEN, secondary = HAPTIC
   ELSE:
       primary = BEST_AVAILABLE, secondary = FALLBACK
   ```
   Allow user override: "Switch to text mode" / "Use voice instead"

4. **Design Graceful Degradation**
   When the preferred modality becomes unavailable:
   - Voice fails (noise) → Offer touch input, display suggestions
   - Screen unavailable (driving) → Switch to voice summaries
   - Network drops → Cache responses, queue actions, inform user
   - Degradation should be transparent: "It's noisy, so I'll show your options on screen"

5. **Plan Content Adaptation**
   Same information, adapted per modality:
   - **Voice**: Concise summary, key facts first, offer to elaborate
   - **Screen (small)**: Essential information, progressive disclosure
   - **Screen (large)**: Rich content, visual hierarchy, supporting details
   - **Audio-only**: Most critical info only, timing under 10 seconds
   - **Text notification**: One-line summary with action link

6. **Design Context Transitions**
   Handle users moving between contexts:
   - Phone → Car: Automatically switch to voice-primary, simplify visuals
   - Car → Walking: Detect Bluetooth disconnect, adjust modality
   - Home → Out: Smart speaker → phone, transfer session context
   - Active → Idle: Reduce interruptions, batch notifications

7. **CRITICAL: Validate adaptation logic**
   - Test in each identified user context
   - Verify that degradation is seamless, not jarring
   - Ensure user can always override automatic modality selection
   - Check that no critical functionality is lost in any context
   - Test context transitions mid-task
   - **Confidence**: High (tested in real contexts), Medium (simulated), Low (theoretical)

## False-Positive Prevention (MUST follow)

- **DON'T** switch modalities without informing the user
- **DON'T** assume context detection is always accurate (allow manual override)
- **DON'T** remove functionality in degraded mode — adapt presentation, not capability
- **DON'T** require setup or configuration for basic adaptation
- **DO** make adaptation feel natural, not disruptive
- **DO** remember user preferences for modality per context
- **DO** test the worst-case scenario (everything degrades at once)

## Expected Output

```markdown
## Adaptive Interface Strategy: [Application Name]

### Context Map
| Context | Primary Modality | Capabilities | Constraints |
|---------|-----------------|-------------|-------------|
| Driving | Voice | Mic, speaker, glanceable screen | No touch, minimal visual |
| At desk | Screen + voice | Full | None |
| Walking | Touch + audio | Phone screen, earbuds | Small screen, movement |
| Meeting | Text only | Phone screen | No audio |

### Adaptation Rules
| Trigger | From | To | User Notification |
|---------|------|----|-------------------|
| Bluetooth car connect | Screen-primary | Voice-primary | "Switching to voice mode for driving" |
| Noise level > threshold | Voice-primary | Screen-primary | "It's noisy — I've put options on screen" |
| User says "text mode" | Any | Text-only | "Got it, switching to text" |

### Content Adaptation Examples
| Content | Voice | Small Screen | Large Screen |
|---------|-------|-------------|-------------|
| Search results | "Top result is X" | Card list (3 visible) | Full grid with images |
| Confirmation | "Book for Friday at 7?" | Button: Confirm/Cancel | Details + Confirm button |

### Degradation Matrix
| Failure | Fallback | User Impact |
|---------|----------|-------------|
| Voice → fail | Touch + visual | Can still complete task |
| Screen → off | Voice only | Summary info, no visuals |
| Network → down | Cached data | Limited features, inform user |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Adaptive interface strategy
- **ST-02 (Structured Sequential Instructions):** Contexts → detection → logic → degradation → adaptation
- **RT-02 (Multi-Dimensional Analysis):** Multiple contexts, devices, and modalities
- **CM-02 (Constraint Specification):** Per-context physical constraints
- **DS-06 (Prioritization Guidance):** Priority modality per context

## Customization Guide

- **For Automotive Only**: Focus on driving safety, NHTSA guidelines, glanceable design
- **For Healthcare**: Add clinical context (sterile environment, patient-facing vs provider)
- **For Industrial/Field Work**: Add rugged conditions, glove-compatible, loud environments
- **For Accessibility**: Context detection should account for permanent vs situational disabilities
