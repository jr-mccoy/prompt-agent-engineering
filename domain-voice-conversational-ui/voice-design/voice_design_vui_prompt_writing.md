---
title: "VUI Prompt Writing and Refinement"
category: voice-conversational-ui/voice-design
description: "Write and refine spoken prompts for voice interfaces applying principles of conversational copywriting including brevity, prosody awareness, disambiguation, and personality consistency"
techniques:
  - ST-01
  - ST-02
  - CM-01
  - QA-02
  - ED-05
difficulty: intermediate
tags:
  - vui-prompts
  - conversational-copywriting
  - ssml
  - prosody
  - voice-persona
  - system-utterances
updated: "2026-03-19"
---

# VUI Prompt Writing and Refinement

**Objective:** Write and refine the spoken prompts (system utterances) for a voice interface, applying conversational copywriting principles to create natural, clear, and personality-consistent voice output.

**When to Use:**
- Use when: Writing system prompts for a new voice application
- Use when: Refining existing prompts that feel robotic or confusing
- Use when: Establishing a voice persona's speaking style
- Use when: Localizing voice prompts for new markets
- Don't use when: Designing the interaction model itself (use `voice_design_interaction_model_builder.md`)

## Instructions

1. **Establish the Voice Persona**
   - Define personality traits (warm, professional, playful, authoritative)
   - Set formality level (casual, conversational, formal)
   - Determine humor usage (none, occasional, frequent)
   - Create a "voice persona card" with do's and don'ts
   - Write 3-5 example responses to calibrate the voice

2. **Write Initial Prompts**
   For each system utterance, draft with these principles:
   - **Brevity**: Keep to 1-2 sentences (under 4 seconds of speech)
   - **Front-load information**: Put the key point first
   - **Use contractions**: "I'll" not "I will", "can't" not "cannot"
   - **Active voice**: "I found 3 results" not "3 results were found"
   - **Conversational register**: Write how people talk, not how they write
   - **Avoid homophone confusion**: "four" not "4", "won" vs "one"

3. **Apply Prosody Awareness**
   - Read every prompt aloud — does it sound natural?
   - Check for awkward word clusters that are hard to pronounce
   - Use SSML for emphasis, pauses, and pacing where needed
   - Avoid long noun phrases ("your recently updated primary billing address")
   - Place pauses before important information

4. **Design Prompt Variations**
   - Write 3-5 variations for frequently heard prompts (prevents monotony)
   - Create escalating versions for repeated interactions (first time, second time, third time)
   - Design error prompts that are progressively more helpful
   - Vary opening phrases while keeping key information consistent

5. **Handle Edge Cases in Prompts**
   - Single vs plural: "1 result" vs "3 results"
   - Empty states: What to say when there's nothing to report
   - Long lists: How to present 10+ items verbally (summarize, paginate)
   - Ambiguous inputs: Disambiguation prompts that don't feel like interrogation
   - Timeouts: Gentle re-engagement ("Still there?")

6. **Add SSML Markup**
   - `<break>` for natural pauses between information chunks
   - `<emphasis>` for key values (prices, names, dates)
   - `<say-as>` for dates, phone numbers, addresses
   - `<prosody>` for rate/pitch adjustments on emotional content
   - `<audio>` for earcons and sound effects at interaction boundaries

7. **CRITICAL: Quality check all prompts**
   - Read every prompt aloud at conversation speed
   - Check that prompts sound natural on both smart speakers and phones
   - Verify personality consistency across all prompts
   - Ensure no prompt exceeds 8 seconds of audio
   - Test with text-to-speech to catch unnatural readings
   - **Confidence**: High (tested aloud), Medium (written only), Low (placeholder)

## False-Positive Prevention (MUST follow)

- **DON'T** write prompts that sound great on paper but are awkward spoken
- **DON'T** use jargon, abbreviations, or acronyms the user may not know
- **DON'T** start every prompt the same way ("Okay, ...", "Sure, ...")
- **DON'T** include visual formatting cues ("as shown below", "see the list")
- **DON'T** write prompts longer than 2 sentences for routine interactions
- **DO** test every prompt by reading it aloud at natural speed
- **DO** account for the listener having no visual reference
- **DO** use earcons (sounds) to replace visual feedback (success chime, error tone)

## Expected Output

```markdown
## VUI Prompt Library: [Application Name]

### Voice Persona
- **Name:** [Persona name]
- **Traits:** [3-5 adjectives]
- **Formality:** [Level]
- **Example calibration responses:**
  1. [Example]
  2. [Example]

### Prompt Category: [Category]

#### [Prompt ID]: [Purpose]
**Context:** [When this prompt plays]
**Primary:** "Here are your 3 upcoming flights. The next one leaves for Paris tomorrow at 8 AM."
**Variation 1:** "You've got 3 flights coming up. First up: Paris, tomorrow at 8 AM."
**Variation 2:** "I see 3 flights on your schedule. The soonest is tomorrow's 8 AM to Paris."
**SSML:**
```xml
<speak>
  Here are your <say-as interpret-as="cardinal">3</say-as> upcoming flights.
  <break time="300ms"/>
  The next one leaves for Paris <break time="200ms"/> tomorrow at
  <say-as interpret-as="time">8:00AM</say-as>.
</speak>
```
**Notes:** [Any special considerations]

### Error Prompts
| Level | Prompt | SSML |
|-------|--------|------|
| First no-match | "I didn't catch that. Try saying..." | [SSML] |
| Second no-match | "Still having trouble. You can say things like..." | [SSML] |
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** Prompt writing and refinement goal
- **ST-02 (Structured Sequential Instructions):** Persona → draft → prosody → variations → SSML
- **CM-01 (Explicit Context Framing):** Voice-specific writing constraints
- **QA-02 (Quality Indicators):** Read-aloud test, timing, consistency checks
- **ED-05 (Reference Class Priming):** Examples of good vs bad voice prompts

## Customization Guide

- **For Children's Apps**: Simpler vocabulary, shorter sentences, more enthusiastic tone
- **For Medical/Financial**: More formal, explicit confirmation, precise language
- **For Brand Voice Migration**: Start from existing brand guidelines, adapt for spoken medium
- **For Multi-language**: Design prompts for translation-friendliness, avoid idioms
