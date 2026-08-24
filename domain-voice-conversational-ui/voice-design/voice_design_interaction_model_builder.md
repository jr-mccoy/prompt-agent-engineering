---
title: "Voice Interaction Model Builder"
category: voice-conversational-ui/voice-design
description: "Create or review a voice application's interaction model from scratch including intents, sample utterances, slot types, confirmation prompts, and fallback handling for any platform"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - OC-03
difficulty: intermediate
tags:
  - interaction-model
  - intents
  - utterances
  - slot-types
  - voice-design
  - platform-agnostic
updated: "2026-03-19"
---

# Voice Interaction Model Builder

**Objective:** Create or review a platform-agnostic voice interaction model, producing a complete specification of intents, sample utterances, slot types, confirmation strategies, and fallback handling that can be implemented on any voice platform.

**When to Use:**
- Use when: Starting a new voice application and need to design the interaction model
- Use when: Translating existing functionality into a voice-first interface
- Use when: Reviewing an interaction model for utterance coverage gaps
- Use when: Porting a voice app between platforms (Alexa → Google → custom)
- Don't use when: You need platform-specific guidance (use Alexa/Google-specific prompts)

## Instructions

1. **Map User Goals to Intents**
   - List all tasks users should accomplish via voice
   - Group related actions into intents (avoid 1:1 action-to-intent mapping)
   - Determine intent granularity: too few = ambiguity, too many = confusion
   - Separate informational intents (queries) from transactional intents (actions)
   - Identify intents that require confirmation before execution

2. **Generate Sample Utterances**
   For each intent, generate 15-30 diverse utterances covering:
   - **Formal variations**: "I would like to book a flight"
   - **Casual variations**: "Book me a flight"
   - **Terse variations**: "Flight booking"
   - **Context-heavy**: "Same as last time but for next Tuesday"
   - **With and without slots**: "Book a flight" vs "Book a flight to Paris on Friday"
   - **Regional variations**: Account for dialect differences
   - **Error-prone phrasings**: Common mispronunciations or near-misses

3. **Define Slot Types**
   For each slot:
   - Name, type (built-in vs custom), and whether required
   - Enumerated values with synonyms for custom types
   - Validation rules (date ranges, value constraints)
   - Elicitation prompts when slot is missing
   - Reprompt strategy when validation fails

4. **Design Confirmation Patterns**
   - **No confirmation**: Low-risk, easily reversible actions
   - **Implicit confirmation**: Echo back values in natural response ("Your flight to Paris...")
   - **Explicit confirmation**: High-risk or irreversible actions ("Should I book this for $450?")
   - **Progressive confirmation**: Confirm critical slots individually, then full intent

5. **Build Fallback and Help Strategy**
   - **No-match (Level 1)**: Rephrase request with hint
   - **No-match (Level 2)**: Provide example utterances
   - **No-match (Level 3)**: Offer to connect to alternate channel
   - **No-input**: Gentle reprompt, then offer to end session
   - **Contextual help**: Different help based on current state

6. **CRITICAL: Validate coverage**
   - Run through 20+ user scenarios end-to-end
   - Check for intent conflicts (same utterance matching multiple intents)
   - Verify every dialog state has an exit path
   - Ensure slot elicitation is natural, not interrogative
   - **Confidence**: High (tested with real utterances), Medium (modeled), Low (theoretical)

## False-Positive Prevention (MUST follow)

- **DON'T** create separate intents for minor utterance variations (use one intent with slots)
- **DON'T** generate only "template" utterances ("book a {destination} flight") without natural variants
- **DON'T** require explicit confirmation for every action (it kills conversation flow)
- **DON'T** design interrogation-style slot filling ("What city? What date? What time?")
- **DO** include utterances that combine multiple slots in one sentence
- **DO** test with real users or at minimum with colleagues unfamiliar with the system
- **DO** design utterances people would actually say, not how you'd type a search query

## Expected Output

```markdown
## Voice Interaction Model: [Application Name]

### Intent Map
| Intent | Type | Slots | Confirmation | Multi-turn |
|--------|------|-------|-------------|------------|
| BookFlight | Transactional | 4 | Explicit | Yes |
| CheckStatus | Informational | 1 | None | No |

### Intent Detail: [IntentName]
**Purpose:** [What this intent does]
**Sample Utterances:**
1. "[Natural utterance with {slot} marked]"
2. "[Variation]"
... (15-30 total)

**Slots:**
| Slot | Type | Required | Elicitation | Validation |
|------|------|----------|-------------|------------|
| {destination} | City | Yes | "Where to?" | Must be served airport |

**Confirmation Strategy:** [Description]

### Fallback Strategy
| Level | Trigger | Response |
|-------|---------|----------|
| 1 | First no-match | [Hint-based reprompt] |
| 2 | Second no-match | [Example utterances] |
| 3 | Third no-match | [Alternate channel offer] |

### Coverage Validation
| Scenario | Path | Status |
|----------|------|--------|
| [User story] | [Intent chain] | Covered / Gap |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Platform-agnostic model design
- **ST-02 (Structured Sequential Instructions):** Goals → intents → utterances → slots → confirmation
- **RT-02 (Multi-Dimensional Analysis):** Coverage, naturalness, conflict analysis
- **CM-01 (Explicit Context Framing):** Voice-specific constraints
- **OC-03 (Structured Output):** Complete interaction model specification

## Customization Guide

- **For Alexa**: Add AMAZON.* built-in intents, dialog delegation config
- **For Google Actions**: Map to scenes, add suggestion chips
- **For Rasa**: Convert to stories/rules format, add training examples
- **For IVR Systems**: Add DTMF alternatives, hold music, transfer patterns
