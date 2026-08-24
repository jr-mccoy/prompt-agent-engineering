---
title: "Slot Filling Strategy Design"
category: voice-conversational-ui/dialog-architecture
description: "Design slot filling and form completion strategies for task-oriented dialogs covering required vs optional slots, elicitation order, cross-slot validation, and correction handling"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - ED-05
  - QA-02
difficulty: intermediate
tags:
  - slot-filling
  - form-completion
  - task-oriented-dialog
  - elicitation
  - validation
  - dialog-policy
updated: "2026-03-19"
---

# Slot Filling Strategy Design

**Objective:** Design slot filling and form completion strategies for task-oriented dialogs, producing specifications for slot definitions, elicitation order, cross-slot validation, partial fills, implicit resolution from context, and correction handling.

**When to Use:**
- Use when: Building a bot that collects information to complete a task (booking, ordering, forms)
- Use when: Users complain the bot asks too many questions or in an unnatural order
- Use when: Optimizing an existing slot-filling dialog for fewer turns
- Use when: Designing slot filling that works across voice and text channels
- Don't use when: Building open-ended conversation (no structured data collection)

## Instructions

1. **Define the Slot Schema**
   For each task the bot performs:
   - List all information needed to complete the task
   - Classify each slot: **required** (must have) vs **optional** (improves result)
   - Define slot types: date, time, number, enum, free-text, entity reference
   - Set default values where sensible (e.g., quantity defaults to 1)
   - Define validation rules for each slot

2. **Optimize Elicitation Order**
   Design the order in which slots are requested:
   - **Dependency-first**: Slots that determine which other slots are needed
   - **User-expectation**: Ask in the order users naturally provide information
   - **Effort-gradient**: Easy slots first (builds momentum), complex slots later
   - **Context-dependent reordering**: If user provided some slots upfront, skip those
   - **Never interrogate**: Don't ask more than 2 slots per turn

3. **Design Natural Elicitation Prompts**
   - **Single-slot**: "Where would you like to go?"
   - **Multi-slot**: "When and where would you like to travel?" (collect 2 slots in one turn)
   - **Choice-based**: "Morning, afternoon, or evening?" (constrain the answer space)
   - **Conversational**: Embed slot requests naturally, not as form fields
   - **Progressive**: Ask the most important slot first, then fill in details

4. **Handle Implicit Slot Resolution**
   Slots can be filled without explicit questions:
   - **From context**: User is logged in → name and email are pre-filled
   - **From prior turns**: "Paris" mentioned earlier → destination pre-filled
   - **From defaults**: Standard selections for common scenarios
   - **From inference**: "Anniversary dinner" → party_size = 2 (inferred)
   - **Confirmation**: Always confirm implicitly resolved slots before acting

5. **Design Cross-Slot Validation**
   - Validate slot combinations (departure date must be before return date)
   - Check business rules (can't book same-day for international flights)
   - Handle cascading changes (changing the city may invalidate the venue)
   - Present validation errors clearly with actionable guidance

6. **Build Correction Handling**
   - **Direct correction**: "Actually, make that Tuesday" → update specific slot
   - **Reference correction**: "The second one, not the first" → resolve and update
   - **Wholesale restart**: "Start over" → clear all slots and begin again
   - **Partial restart**: "Change the dates but keep the destination" → selective clear
   - **Correction confirmation**: Echo the updated value back to the user

7. **Optimize for Fewer Turns**
   - Support one-shot filling: "Book a table for 4 at Nobu tomorrow at 7 PM"
   - Extract multiple slots from a single utterance
   - Use smart defaults to skip unnecessary questions
   - Offer "same as last time" for repeat users
   - Show a summary for confirmation instead of confirming each slot

8. **CRITICAL: Validate the strategy**
   - Test with users who provide information in unexpected order
   - Test one-shot utterances with all slots vs partial slots
   - Verify correction handling preserves other slots
   - Ensure cross-slot validation catches invalid combinations
   - Test with voice (where correction is harder)
   - **Confidence**: High (user-tested), Medium (designed), Low (theoretical)

## False-Positive Prevention (MUST follow)

- **DON'T** ask for information you could infer or look up
- **DON'T** re-ask for slots the user already provided
- **DON'T** force a fixed question order when the user provides info freely
- **DON'T** require explicit confirmation for every individual slot
- **DO** support flexible input order (user can provide any slot at any time)
- **DO** use summary confirmation instead of slot-by-slot confirmation
- **DO** remember slot values across corrections (don't clear everything)

## Expected Output

```markdown
## Slot Filling Design: [Task Name]

### Slot Schema
| Slot | Type | Required | Default | Validation | Source |
|------|------|----------|---------|------------|--------|
| destination | city | Yes | None | Must be served city | User input |
| date | date | Yes | None | Must be future date | User input |
| passengers | integer | Yes | 1 | 1-9 | Default or user |
| class | enum | No | Economy | Economy/Business/First | User input |

### Elicitation Strategy
| Priority | Slot | Prompt | Multi-slot? |
|----------|------|--------|-------------|
| 1 | destination | "Where would you like to fly?" | Can combine with date |
| 2 | date | "What date works for you?" | Can combine with passengers |
| 3 | passengers | Confirm default: "Just one passenger?" | - |
| 4 | class | Skip unless asked (default Economy) | - |

### One-Shot Pattern
**Full:** "Book a flight to Paris for 2 on Friday in business class"
→ Fills: destination=Paris, passengers=2, date=Friday, class=Business

**Partial:** "I need to fly to Paris"
→ Fills: destination=Paris
→ Asks: date, then confirms passengers default

### Cross-Slot Validation
| Rule | Slots | Error Message |
|------|-------|---------------|
| Future date | date | "That date has passed. When would you like to travel?" |
| Route exists | destination + origin | "We don't fly that route. Try [alternatives]." |

### Correction Patterns
| User Says | Action | Preserved |
|-----------|--------|-----------|
| "Make it Tuesday instead" | Update date | destination, passengers, class |
| "Change to 3 passengers" | Update passengers | destination, date, class |
| "Start over" | Clear all | Nothing |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Slot filling strategy design
- **ST-02 (Structured Sequential Instructions):** Schema → order → prompts → implicit → validation → correction
- **RT-02 (Multi-Dimensional Analysis):** Slots, order, validation, correction dimensions
- **ED-05 (Reference Class Priming):** One-shot and correction patterns as templates
- **QA-02 (Quality Indicators):** Turn count optimization metrics

## Customization Guide

- **For Voice**: Shorter prompts, more implicit confirmation, fewer choices per turn
- **For Web Chat**: Can show form alongside chat, richer correction UI
- **For Complex Forms (10+ slots)**: Group into sections, use summaries between sections
- **For Repeat Users**: "Same as last time?" shortcut, pre-filled from history
