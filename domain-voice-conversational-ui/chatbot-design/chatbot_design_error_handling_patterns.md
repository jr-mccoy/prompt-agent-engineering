---
title: "Conversational Error Handling Patterns"
category: voice-conversational-ui/chatbot-design
description: "Design robust error handling and fallback strategies for conversational interfaces including no-match, no-input, disambiguation, confidence thresholds, progressive help, and human handoff"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-05
  - QA-02
difficulty: intermediate
tags:
  - error-handling
  - fallback
  - disambiguation
  - human-handoff
  - conversation-repair
  - graceful-degradation
updated: "2026-03-19"
---

# Conversational Error Handling Patterns

**Objective:** Design robust error handling and fallback strategies for conversational interfaces, covering no-match, no-input, disambiguation, confidence thresholds, progressive help, graceful degradation, and human handoff triggers.

**When to Use:**
- Use when: Building error handling for a new chatbot or voice assistant
- Use when: Users frequently hit dead ends or express frustration
- Use when: The bot's fallback rate is above 15%
- Use when: Reviewing error handling completeness before launch
- Don't use when: Designing the happy-path flows (use `chatbot_design_conversation_flow.md`)

## Instructions

1. **Categorize Error Types**
   Map all error scenarios the conversational interface can encounter:
   - **No-match**: User input not recognized by any intent
   - **No-input**: User didn't respond (voice timeout or empty message)
   - **Low-confidence match**: Intent matched but below confidence threshold
   - **Ambiguous match**: Multiple intents match with similar confidence
   - **Slot validation failure**: Recognized intent but invalid slot values
   - **System error**: Backend API failure, timeout, or exception
   - **Out-of-scope**: Recognized but unsupported request
   - **Inappropriate input**: Offensive content, PII in wrong context

2. **Design Progressive Error Recovery**
   For each error type, create a 3-level escalation:
   - **Level 1 (Gentle retry)**: Rephrase the question with a hint
   - **Level 2 (Guided help)**: Provide specific examples of what to say
   - **Level 3 (Escape)**: Offer alternatives (human, different channel, start over)

   Rules:
   - Never repeat the exact same error message
   - Each level should provide MORE help, not just retry
   - Maximum 3 attempts before escalating or offering escape
   - Preserve any information already gathered

3. **Set Confidence Thresholds**
   Define handling for confidence score ranges:
   - **High (>0.8)**: Execute the matched intent directly
   - **Medium (0.5-0.8)**: Execute with implicit confirmation ("I'll check your order status...")
   - **Low (0.3-0.5)**: Explicit disambiguation ("Did you mean X or Y?")
   - **Very low (<0.3)**: Treat as no-match, enter error recovery

4. **Design Disambiguation Patterns**
   - Present top 2-3 options when confidence is ambiguous
   - Use natural phrasing: "Did you want to check your balance or make a payment?"
   - Include a "neither" option to avoid forcing incorrect paths
   - Preserve the user's original input for context

5. **Plan Human Handoff Triggers**
   Define when and how to escalate to a human:
   - **Triggers**: 3+ errors, detected frustration, explicit request, high-stakes action
   - **Context transfer**: Summarize conversation for the human agent
   - **Warm vs cold**: Introduce the handoff or seamlessly transfer
   - **Availability handling**: What to do when no humans are available
   - **Return path**: Can the user come back to the bot after human interaction?

6. **Handle System Errors Gracefully**
   - API timeouts: "I'm having trouble looking that up. Can I try again?"
   - Partial failures: Show what you can, explain what's missing
   - Full outage: "I'm experiencing technical difficulties. Here's how to reach us..."
   - Never expose technical error messages to users
   - Log errors for debugging while showing user-friendly messages

7. **CRITICAL: Validate error handling coverage**
   - Trigger every error type and verify the bot responds appropriately
   - Test error chains (multiple errors in sequence)
   - Verify context preservation through error recovery
   - Ensure escape hatches are reachable from every state
   - **Confidence**: High (tested), Medium (designed), Low (placeholder)

## False-Positive Prevention (MUST follow)

- **DON'T** use the same error message for different error types
- **DON'T** blame the user ("I didn't understand you" → "I'm not sure I got that")
- **DON'T** loop forever — maximum 3 retries before offering escape
- **DON'T** lose collected information during error recovery
- **DON'T** assume the first intent match is correct below 0.7 confidence
- **DO** make error messages progressively more helpful
- **DO** always provide an escape route to a human
- **DO** log error patterns for continuous improvement

## Expected Output

```markdown
## Error Handling Design: [Bot Name]

### Error Type Map
| Error Type | Frequency | Current Handling | Proposed Handling |
|------------|-----------|-----------------|-------------------|
| No-match | 22% of turns | Generic "I don't understand" | 3-level progressive help |
| Low-confidence | 15% of turns | Force first match | Confidence-based routing |

### Confidence Thresholds
| Range | Action | Example Response |
|-------|--------|-----------------|
| >0.8 | Execute | (Direct response) |
| 0.5-0.8 | Implicit confirm | "I'll check your order status..." |
| 0.3-0.5 | Disambiguate | "Did you mean X or Y?" |
| <0.3 | No-match recovery | "I'm not sure I got that. You can..." |

### Progressive Error Recovery
#### No-Match
| Level | Message | Strategy |
|-------|---------|----------|
| 1 | "I'm not sure I got that. Could you rephrase?" | Gentle retry |
| 2 | "I can help with [X], [Y], or [Z]. Which of these?" | Guided options |
| 3 | "Let me connect you with someone who can help." | Human handoff |

### Human Handoff Protocol
| Trigger | Action | Context Passed |
|---------|--------|---------------|
| 3+ errors | Offer handoff | Full conversation transcript |
| User requests | Immediate transfer | Summary + user info |
| High-stakes | Confirm then transfer | Action details + auth status |

### System Error Responses
| Error | User-Facing Message | Internal Action |
|-------|-------------------|-----------------|
| API timeout | "Having trouble fetching that. Trying again..." | Retry 1x, then degrade |
| Full outage | "I'm experiencing issues. Call us at [number]." | Alert on-call |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Comprehensive error handling design
- **ST-02 (Structured Sequential Instructions):** Categorize → escalate → thresholds → disambiguate
- **RT-02 (Multi-Dimensional Analysis):** All error types analyzed systematically
- **ED-05 (Reference Class Priming):** Progressive recovery patterns as templates
- **QA-02 (Quality Indicators):** Coverage validation checklist

## Customization Guide

- **For Voice Assistants**: Add no-input (silence) handling, shorter error messages
- **For Web Chat**: Add typing indicators during recovery, rich message fallbacks
- **For WhatsApp/SMS**: Account for character limits, no rich formatting
- **For Enterprise Internal**: Less handoff focus, more self-service guidance
