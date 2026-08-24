---
title: "Conversational Context Management"
category: voice-conversational-ui/dialog-architecture
description: "Design context and memory systems for multi-turn conversations covering short-term context, long-term memory, context carryover rules, entity resolution, and anaphora handling"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - ED-05
difficulty: advanced
tags:
  - context-management
  - conversation-memory
  - multi-turn
  - entity-resolution
  - anaphora
  - session-management
updated: "2026-03-19"
---

# Conversational Context Management

**Objective:** Design a context and memory management system for multi-turn conversations, specifying short-term context handling, long-term memory architecture, context carryover rules, entity resolution strategies, and anaphora handling patterns.

**When to Use:**
- Use when: Building a multi-turn conversational system that needs to track context
- Use when: Users complain the bot "forgets" what they just said
- Use when: Designing context passing between bot components or microservices
- Use when: Planning memory architecture for an LLM-powered chatbot
- Don't use when: Building single-turn Q&A systems with no conversation state

## Instructions

1. **Define Context Layers**
   Design a layered context architecture:
   - **Turn context**: Current utterance, recognized intent, extracted entities
   - **Dialog context**: Active flow, filled slots, conversation state
   - **Session context**: User identity, authentication status, session preferences
   - **User context**: Long-term preferences, history, profile data
   - **Global context**: Time, location, device type, channel

2. **Design Context Carryover Rules**
   Define when context persists vs resets:
   - **Entity carryover**: "Show me flights to Paris" → "What about hotels?" (Paris carries over)
   - **Intent carryover**: If user says "and for next week?" after a search, carry the search intent
   - **Scope rules**: How far back entities remain valid (turn count or time-based)
   - **Reset triggers**: What clears context (topic change, explicit reset, session timeout)
   - **Priority rules**: When new context conflicts with carried context

3. **Handle Entity Resolution**
   - **Coreference resolution**: "it", "that one", "the first one" → resolve to specific entity
   - **Relative references**: "next Tuesday", "the cheaper one", "my usual"
   - **Implicit entities**: "Book it" → what is "it" referring to?
   - **Ambiguous references**: Multiple possible referents → ask for clarification
   - **Entity update**: "Actually, make that Wednesday instead" → update existing entity

4. **Design Anaphora Handling**
   Pronoun and reference resolution patterns:
   - **Pronoun mapping**: "he/she/it/they/that" → most recent matching entity
   - **Demonstrative references**: "this flight", "that hotel" → resolve from recent context
   - **Ellipsis handling**: "And for two people" (missing verb/subject from prior turn)
   - **Comparative references**: "a cheaper one", "somewhere closer"
   - **Fallback**: When resolution is ambiguous, ask a clarifying question

5. **Architect Long-Term Memory**
   - **What to store**: User preferences, past transactions, feedback, learned patterns
   - **Storage mechanism**: Database, key-value store, vector store for semantic retrieval
   - **Retrieval strategy**: When and how to surface past context
   - **Privacy controls**: What users can view, edit, and delete
   - **Decay policy**: When old context becomes irrelevant

6. **Design Cross-Channel Context**
   If the bot operates across channels (web, mobile, voice):
   - Session continuity: Can users switch channels mid-conversation?
   - Context format normalization: Different channels, same context model
   - Channel-specific adaptations: What context is relevant per channel
   - Handoff context: What to pass when escalating to a human agent

7. **CRITICAL: Validate context management**
   - Test 10+ multi-turn scenarios with entity carryover
   - Verify anaphora resolution with ambiguous references
   - Test context reset triggers don't lose important data
   - Ensure privacy controls actually delete what they should
   - Check performance with large context histories
   - **Confidence**: High (tested end-to-end), Medium (designed), Low (conceptual)

## False-Positive Prevention (MUST follow)

- **DON'T** carry all context indefinitely (context bloat → confusion)
- **DON'T** assume the most recent entity is always the correct referent
- **DON'T** store PII in long-term memory without explicit consent
- **DON'T** resolve ambiguous references silently — ask the user
- **DO** define explicit context scoping rules (not just "keep everything")
- **DO** test with conversations that change topic mid-session
- **DO** provide users control over stored preferences and history

## Expected Output

```markdown
## Context Management Design: [Application Name]

### Context Layers
| Layer | Contents | Scope | Storage | TTL |
|-------|----------|-------|---------|-----|
| Turn | Current intent, entities | Single turn | Memory | Immediate |
| Dialog | Active flow, slot values | Current task | Session store | Task completion |
| Session | Auth, preferences | Current session | Redis | 30 min inactivity |
| User | History, preferences | Permanent | Database | User-controlled |

### Carryover Rules
| Entity Type | Carryover Scope | Reset Trigger | Example |
|-------------|----------------|---------------|---------|
| Location | 3 turns | New location mentioned | "Paris" carries to hotel search |
| Date | Current task | Task completion | "Next Friday" for flight + hotel |
| Product | 5 turns | New product category | "iPhone 15" for specs + pricing |

### Anaphora Resolution
| Reference | Resolution Strategy | Fallback |
|-----------|-------------------|----------|
| "it" / "that" | Most recent singular entity | "Which item do you mean?" |
| "the first one" | Ordered list index | "Could you specify which one?" |
| "my usual" | User preference lookup | "I don't have a usual on file. What would you like?" |

### Long-Term Memory Schema
| Field | Type | Consent Required | Deletable |
|-------|------|-----------------|-----------|
| preferred_name | string | No (inferred) | Yes |
| past_orders | array | Yes | Yes |
| communication_pref | enum | Yes | Yes |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Context management system design
- **ST-02 (Structured Sequential Instructions):** Layers → carryover → resolution → anaphora → memory
- **RT-02 (Multi-Dimensional Analysis):** Multiple context layers and resolution strategies
- **CM-02 (Constraint Specification):** Privacy, performance, scope constraints
- **ED-05 (Reference Class Priming):** Resolution strategy patterns as templates

## Customization Guide

- **For Voice Assistants**: Shorter carryover scope (voice memory is limited), more aggressive clarification
- **For LLM-Based Bots**: Focus on context window management and summarization
- **For Multi-Tenant**: Ensure context isolation between users/organizations
- **For Regulated Industries**: Strict PII controls, audit logging of context access
