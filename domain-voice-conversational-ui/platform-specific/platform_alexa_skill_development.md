---
title: "Alexa Skill End-to-End Development"
category: voice-conversational-ui/platform-specific
description: "End-to-end Alexa Skill development guidance covering manifest configuration, interaction model JSON, Lambda handler patterns with ASK SDK v2, session management, certification, and testing"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-01
  - QA-02
difficulty: advanced
tags:
  - alexa
  - ask-sdk
  - lambda
  - skill-development
  - certification
  - interaction-model
  - apl
updated: "2026-03-19"
---

# Alexa Skill End-to-End Development

**Objective:** Guide end-to-end Alexa Skill development, producing specifications and code patterns for manifest configuration, interaction model JSON, Lambda handler architecture (ASK SDK v2), session management, in-skill purchases, certification readiness, and testing strategies.

**When to Use:**
- Use when: Building a new Alexa Skill from design through certification
- Use when: Reviewing an existing Skill's implementation for best practices
- Use when: Preparing a Skill for Amazon certification submission
- Use when: Migrating a Skill from ASK SDK v1 to v2
- Don't use when: Designing the interaction model only (use `voice_design_alexa_skill_architecture.md`)

## Instructions

1. **Configure Skill Manifest**
   - Skill type: Custom, Smart Home, Flash Briefing, or Video
   - Locales and language support
   - Privacy and compliance settings
   - Account linking configuration (if needed)
   - Endpoint configuration (Lambda ARN or HTTPS)
   - Permissions (device address, lists, notifications, etc.)

2. **Build Interaction Model JSON**
   - Define invocation name (2-3 words, pronounceable, not a brand name without permission)
   - Configure intents with sample utterances
   - Define slot types with values and synonyms
   - Set up dialog model for multi-turn intents
   - Configure intent confirmation and slot validation
   - Test with Alexa Utterance Profiler

3. **Implement Lambda Handler (ASK SDK v2)**
   - Request handler architecture: one handler per intent
   - Use canHandle() for routing, handle() for logic
   - Implement interceptors for logging and state management
   - Error handler: catch-all for unexpected errors
   - Response builder patterns: speak(), reprompt(), withSimpleCard()
   - Keep handlers focused: business logic in separate service modules

4. **Design Session and Persistence**
   - Session attributes: In-memory state for current session
   - Persistent attributes: DynamoDB for cross-session state
   - Attribute management with AttributesManager
   - Session lifecycle: LaunchRequest → intents → SessionEndedRequest
   - Handle session timeout (8 seconds for response, user-initiated end)

5. **Implement APL for Visual Devices (if applicable)**
   - APL document structure: layouts, styles, resources
   - Responsive design: Hub landscape, Echo Show portrait, Fire TV
   - APL commands for animations and interactions
   - Touch event handling alongside voice
   - Fallback for non-APL devices

6. **Add In-Skill Purchases (if applicable)**
   - Product types: One-time, subscription, consumable
   - Upsell flow: contextual suggestion → purchase directive
   - Purchase result handling: accepted, declined, already purchased
   - Entitlement checking at Skill launch
   - Receipt management and refund handling

7. **Prepare for Certification**
   Certification checklist:
   - All required built-in intents handled (Help, Stop, Cancel, Fallback)
   - Skill responds within 8 seconds
   - No hardcoded responses for LaunchRequest (must vary)
   - Session ends cleanly (no open microphone without reprompt)
   - Privacy policy URL provided
   - Testing instructions for certification team
   - No content policy violations

8. **Design Testing Strategy**
   - Unit tests: Test each handler in isolation
   - Integration tests: Test handler chains with simulated requests
   - ASK CLI simulation: Test locally with `ask dialog`
   - Device testing: Test on actual Echo devices
   - Beta testing: Use Alexa beta testing program
   - Regression testing: Automated test suite for CI/CD

9. **CRITICAL: Validate before submission**
   - Run the Alexa Skill Validation API
   - Test all utterance paths end-to-end
   - Verify error handling with unexpected inputs
   - Check APL rendering on all supported devices
   - Test account linking flow (if applicable)
   - **Confidence**: High (tested on device), Medium (simulator only), Low (code review only)

## False-Positive Prevention (MUST follow)

- **DON'T** hardcode responses (certification requires variation)
- **DON'T** leave the microphone open without a reprompt
- **DON'T** use SSML that exceeds 8 seconds of audio
- **DON'T** store sensitive user data in session attributes (use DynamoDB with encryption)
- **DON'T** skip testing on actual devices (simulator misses real-world issues)
- **DO** handle SessionEndedRequest (even though you can't respond)
- **DO** implement proper error handling for every handler
- **DO** test with multiple Alexa-enabled device types

## Expected Output

```markdown
## Alexa Skill Development: [Skill Name]

### Manifest Configuration
| Setting | Value |
|---------|-------|
| Type | Custom |
| Locales | en-US, en-GB |
| Endpoint | Lambda: arn:aws:lambda:... |
| Permissions | [List] |

### Handler Architecture
| Handler | Intent | Responsibility |
|---------|--------|---------------|
| LaunchRequestHandler | LaunchRequest | Welcome, state check |
| [Intent]Handler | [Intent] | [Description] |
| ErrorHandler | * (catch-all) | Graceful error response |
| SessionEndedHandler | SessionEndedRequest | Cleanup |

### Code Pattern
```javascript
const IntentHandler = {
  canHandle(handlerInput) {
    return Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
      && Alexa.getIntentName(handlerInput.requestEnvelope) === 'MyIntent';
  },
  handle(handlerInput) {
    const speakOutput = 'Response text';
    return handlerInput.responseBuilder
      .speak(speakOutput)
      .reprompt('Reprompt text')
      .getResponse();
  }
};
```

### Testing Plan
| Test Type | Tool | Coverage |
|-----------|------|----------|
| Unit | Jest + ASK SDK test | All handlers |
| Integration | ASK CLI simulate | Key flows |
| Device | Echo, Echo Show | All APL layouts |
| Beta | Alexa Beta Testing | 10 testers |

### Certification Checklist
- [ ] Help, Stop, Cancel, Fallback handled
- [ ] Response times under 8 seconds
- [ ] Session management clean
- [ ] Privacy policy provided
- [ ] Testing instructions written
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** End-to-end Skill development
- **ST-02 (Structured Sequential Instructions):** Manifest → model → handler → session → APL → certification
- **RT-02 (Multi-Dimensional Analysis):** Code, testing, certification dimensions
- **CM-01 (Explicit Context Framing):** Alexa platform constraints
- **QA-02 (Quality Indicators):** Certification checklist

## Customization Guide

- **For Smart Home Skills**: Focus on device discovery, directive handling
- **For Flash Briefing Skills**: Simplified feed-based content delivery
- **For Kids Skills**: COPPA compliance, kid-directed content guidelines
- **For Multi-Modal Skills**: Heavy APL focus, touch + voice interaction
