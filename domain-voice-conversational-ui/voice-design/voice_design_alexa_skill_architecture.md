---
title: "Alexa Skill Interaction Model Architecture"
category: voice-conversational-ui/voice-design
description: "Design or review an Alexa Skill's interaction model including intent schema, slot types, dialog delegation, multi-turn conversation flow, session management, and APL integration"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - DS-06
difficulty: advanced
tags:
  - alexa
  - voice-ui
  - interaction-model
  - intent-design
  - slot-types
  - dialog-delegation
  - apl
updated: "2026-03-19"
---

# Alexa Skill Interaction Model Architecture

**Objective:** Design or review an Alexa Skill's interaction model, producing a comprehensive intent schema with slot types, dialog delegation strategy, multi-turn conversation flows, session attribute management, and APL (Alexa Presentation Language) integration points.

**When to Use:**
- Use when: Designing a new Alexa Skill from scratch
- Use when: Reviewing an existing Skill's interaction model for completeness
- Use when: Migrating a chatbot or voice experience to the Alexa platform
- Use when: Troubleshooting user confusion or high fallback rates in an existing Skill
- Don't use when: Building a non-Alexa voice app (use `voice_design_interaction_model_builder.md` instead)

## Instructions

1. **Define the Skill's Core Purpose and Invocation**
   - Identify the primary user tasks the Skill must support
   - Define the invocation name and one-shot invocation patterns
   - Map the top 5-10 user goals as high-level intents
   - Identify which interactions are single-turn vs multi-turn

2. **Design the Intent Schema**
   For each custom intent:
   - **Intent name**: Follow Alexa naming conventions (PascalCase, verb-noun)
   - **Sample utterances**: Minimum 15-20 diverse utterances per intent
   - **Slot types**: Built-in (AMAZON.DATE, AMAZON.NUMBER) vs custom slot types
   - **Slot elicitation prompts**: For required slots with dialog delegation
   - **Slot validation**: Value ranges, synonyms, and confirmation prompts
   - **Intent confirmation**: When the full intent should be confirmed before execution

3. **Configure Dialog Delegation**
   - Identify which intents require multi-turn dialog
   - Define required vs optional slots per intent
   - Set slot elicitation order (most important first, context-dependent reordering)
   - Design confirmation prompts (implicit vs explicit)
   - Plan for slot value corrections mid-dialog

4. **Design Session Management**
   - Define session attributes to persist across turns
   - Plan session end conditions and goodbye flows
   - Design re-engagement patterns for returning users
   - Handle session timeout gracefully (8-second limit for responses)

5. **Plan APL Integration (if applicable)**
   - Identify which responses benefit from visual display
   - Design APL templates for Alexa-enabled screens
   - Ensure voice-first design (screen supplements, never replaces voice)
   - Handle headless devices (Echo Dot) vs screen devices (Echo Show)

6. **Map Built-in Intent Handling**
   - AMAZON.HelpIntent: Contextual help based on current state
   - AMAZON.StopIntent / AMAZON.CancelIntent: Clean session teardown
   - AMAZON.FallbackIntent: Progressive help strategy
   - AMAZON.YesIntent / AMAZON.NoIntent: Context-aware confirmation handling

7. **CRITICAL: Validate the interaction model**
   - Verify no utterance conflicts between intents
   - Check slot type coverage for expected user inputs
   - Ensure fallback paths exist for every dialog state
   - Test one-shot invocations cover the most common user paths
   - Verify response SSML stays under the 8-second audio limit
   - **Confidence levels** for each design decision:
     - **High Confidence**: Follows Alexa certification requirements
     - **Medium Confidence**: Best practice but context-dependent
     - **Low Confidence**: Tradeoff decision, document reasoning

## False-Positive Prevention (MUST follow)

- **DON'T** design utterances that overlap between intents without disambiguation
- **DON'T** require more than 3 slot fills in a single turn (cognitive overload)
- **DON'T** use explicit confirmation for every intent (only high-stakes actions)
- **DON'T** assume screen availability (always design voice-first)
- **DON'T** ignore AMAZON.FallbackIntent (it's required for certification)
- **DO** test with natural language variations, not just templated utterances
- **DO** consider regional language differences (US vs UK English)
- **DO** plan for users who say "yes" or "no" outside of confirmation flows
- **DO** keep SSML responses conversational and under 4 sentences

## Expected Output

```markdown
## Alexa Skill Interaction Model: [Skill Name]

### Skill Overview
- **Invocation Name:** "[name]"
- **Primary Use Cases:** [List]
- **Target Devices:** Echo, Echo Show, Echo Auto, Fire TV
- **Multi-Turn Intents:** [Count] of [Total] intents

### Intent Schema

#### [IntentName]
- **Purpose:** [Description]
- **Sample Utterances:**
  - "[utterance with {slot}]"
  - "[utterance variation]"
  - (15+ more)
- **Slots:**
  | Slot | Type | Required | Elicitation Prompt |
  |------|------|----------|-------------------|
  | {slotName} | AMAZON.DATE | Yes | "What date?" |
- **Confirmation:** [None / Implicit / Explicit]
- **Dialog Delegation:** [Enabled / Disabled]

### Session Attributes
| Attribute | Type | Purpose | Persisted |
|-----------|------|---------|-----------|
| lastIntent | string | Context for help | Session |

### APL Templates
| Screen | Template | Fallback (headless) |
|--------|----------|-------------------|
| Results | ListTemplate | Voice-only list |

### Built-in Intent Handling
| Intent | Behavior |
|--------|----------|
| HelpIntent | [Context-aware help strategy] |
| FallbackIntent | [Progressive help: hint → example → full help] |

### Certification Checklist
- [ ] All required built-in intents handled
- [ ] FallbackIntent implemented
- [ ] Session ends cleanly
- [ ] No prohibited content
- [ ] Privacy policy URL provided
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Specific design/review goal
- **ST-02 (Structured Sequential Instructions):** Step-by-step interaction model design
- **RT-02 (Multi-Dimensional Analysis):** Evaluates intents, slots, dialog, session, APL
- **CM-01 (Explicit Context Framing):** Alexa-specific constraints and certification requirements
- **DS-06 (Prioritization Guidance):** Ranks intents by user importance

## Customization Guide

- **For Kids Skills**: Add COPPA compliance checks, simpler language, no purchases
- **For Smart Home Skills**: Focus on device control intents, minimize multi-turn
- **For Flash Briefing Skills**: Simplify to content delivery, minimal interaction
- **For In-Skill Purchases**: Add purchase flow intents, upsell triggers, receipt management
