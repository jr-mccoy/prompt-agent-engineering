---
title: "Voice Error Recovery Patterns"
category: voice-conversational-ui/voice-ux
description: "Design error recovery patterns for voice interfaces including incremental prompting, reprompt escalation, contextual help, disambiguation, graceful fallback to screen, and progress-preserving restart"
techniques:
  - ST-01
  - ST-02
  - ED-05
  - CM-01
  - QA-02
difficulty: intermediate
tags:
  - error-recovery
  - voice-ux
  - reprompt
  - disambiguation
  - graceful-degradation
  - conversation-repair
updated: "2026-03-19"
---

# Voice Error Recovery Patterns

**Objective:** Design error recovery patterns specifically for voice interfaces, producing a pattern library covering incremental prompting, reprompt escalation, contextual help, disambiguation strategies, graceful fallback to screen, and progress-preserving restart mechanisms.

**When to Use:**
- Use when: Building error handling for a voice-first application
- Use when: Users frequently say "I don't know what to say" or abandon sessions
- Use when: The voice app's error/fallback rate is above 10%
- Use when: Adapting error handling from text chat to voice
- Don't use when: Designing text-only chatbot errors (use `chatbot_design_error_handling_patterns.md`)

## Instructions

1. **Map Voice-Specific Error Scenarios**
   Voice errors differ from text errors:
   - **ASR failure**: Speech not recognized at all (noise, mumble, accent)
   - **ASR misrecognition**: Speech recognized but incorrectly
   - **Silence/no-input**: User didn't speak within the timeout window
   - **Intent confusion**: Words recognized but intent unclear
   - **Out-of-turn**: User speaks while system is still talking (barge-in)
   - **Background speech**: TV, other people, ambient noise captured

2. **Design Incremental Prompting**
   Each reprompt should add information:
   - **Attempt 1**: Short reprompt with the original question slightly reworded
   - **Attempt 2**: Add a concrete example ("You can say something like...")
   - **Attempt 3**: Offer constrained choices ("Would you like A, B, or C?")
   - **Attempt 4**: Offer alternate channel or human help
   Never repeat the exact same prompt verbatim.

3. **Build Contextual Help System**
   - Help responses change based on current dialog state
   - At greeting: Overview of what the bot can do
   - During slot filling: Explain what information is needed and why
   - During confirmation: Explain what will happen if user says yes
   - After error: Explain what went wrong and how to proceed
   - Universal: "You can always say 'help' or 'start over'"

4. **Design Disambiguation for Voice**
   Voice-specific disambiguation challenges:
   - Homophones: "to/too/two", "there/their/they're" — use context to resolve
   - Similar-sounding words: "fifteen" vs "fifty" — echo back for confirmation
   - Accent variations: Build broader phonetic matching
   - Multi-intent: "Check my order and also change my address" — handle sequentially
   - Offer numbered choices: "Was that option 1, Seattle, or option 2, Portland?"

5. **Design Screen Fallback Patterns**
   For multi-modal devices (phone, smart display):
   - When voice fails 2+ times, offer "I've put some options on your screen"
   - Transfer complex selections (long lists, forms) to visual display
   - Keep voice as the confirmation channel: "Tap your choice and I'll confirm"
   - For voice-only devices: offer to send a link to phone or email

6. **Build Progress-Preserving Restart**
   When the user says "start over" or the conversation derails:
   - Save all successfully collected information
   - Offer: "I still have [collected info]. Would you like to keep that or start fresh?"
   - Reset only the problematic part of the conversation
   - Provide a summary of where things stand before restarting

7. **Design Earcon and Audio Feedback**
   Non-verbal audio cues for voice interactions:
   - Success sound: Confirms action was taken
   - Error sound: Signals something went wrong (distinct from success)
   - Listening indicator: Audio cue that the mic is active
   - Processing indicator: Brief sound while system thinks
   - Keep sounds short (<1 second) and distinctive

8. **CRITICAL: Validate recovery patterns**
   - Test every error scenario at least 3 times in sequence
   - Verify that progressive prompts don't loop
   - Ensure escalation actually reaches a human or alternate channel
   - Check that preserved progress is accurate
   - Test with real speech in noisy environments
   - **Confidence**: High (user-tested), Medium (internal testing), Low (designed only)

## False-Positive Prevention (MUST follow)

- **DON'T** repeat the same error message verbatim on retry
- **DON'T** use more than 4 retry attempts before escalating
- **DON'T** say "I didn't understand you" (blame language) — say "I didn't catch that"
- **DON'T** clear collected data on error recovery
- **DON'T** play long error messages on voice (keep under 3 seconds)
- **DO** make each retry more helpful than the last
- **DO** always offer a way out (human, different channel, stop)
- **DO** use audio cues to supplement voice prompts

## Expected Output

```markdown
## Voice Error Recovery Patterns: [Application Name]

### Error Scenario Map
| Scenario | Frequency | Current Handling | Improved Handling |
|----------|-----------|-----------------|-------------------|
| ASR failure | 8% of turns | "I didn't understand" (repeated) | 4-level progressive prompting |
| Silence | 12% of turns | 3s timeout, no warning | 5s + warning + gentle reprompt |
| Misrecognition | 5% of turns | Execute wrong intent | Echo + confirm before acting |

### Progressive Prompting Library

#### Context: [Slot Filling — Destination]
| Attempt | System Prompt | Strategy |
|---------|--------------|----------|
| 1 | "Sorry, where did you want to go?" | Rephrase |
| 2 | "Try saying a city name, like 'New York' or 'Chicago'" | Example |
| 3 | "Here are popular destinations: New York, Chicago, or LA. Which one?" | Constrain |
| 4 | "Let me transfer you to an agent who can help." | Escalate |

### Contextual Help Map
| Dialog State | Help Response |
|-------------|---------------|
| Greeting | "I can help with flights, hotels, and car rentals. Which one?" |
| Collecting destination | "Tell me the city you want to travel to." |
| Confirmation | "Say 'yes' to confirm or 'no' to make changes." |

### Screen Fallback Triggers
| Trigger | Visual Fallback |
|---------|----------------|
| 2+ ASR failures | Show options as tappable buttons |
| List >5 items | Display scrollable list on screen |
| Complex form | Transfer to screen-based form |

### Audio Cues
| Cue | Sound | Duration | When |
|-----|-------|----------|------|
| Listening | Soft chime | 0.3s | Mic activates |
| Success | Rising tone | 0.5s | Action confirmed |
| Error | Gentle buzz | 0.4s | Recognition failed |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Voice error recovery pattern design
- **ST-02 (Structured Sequential Instructions):** Scenarios → prompting → help → disambiguation → fallback
- **ED-05 (Reference Class Priming):** Pattern library with concrete examples
- **CM-01 (Explicit Context Framing):** Voice-specific constraints
- **QA-02 (Quality Indicators):** Frequency and impact tracking

## Customization Guide

- **For Smart Speakers (no screen)**: Skip screen fallback, enhance verbal disambiguation
- **For Smart Displays**: Rich screen fallback, visual + voice coordination
- **For Phone/IVR**: Add DTMF fallback, operator transfer option
- **For Automotive**: Simpler prompts, no screen interaction, driver safety priority
