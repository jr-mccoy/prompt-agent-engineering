---
title: "Custom Voice Assistant Architecture"
category: voice-conversational-ui/voice-design
description: "Architect a custom voice assistant end-to-end covering wake-word detection, ASR pipeline, NLU engine selection, dialog management, TTS voice selection, and deployment strategy"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - CM-02
  - DS-06
difficulty: expert
tags:
  - voice-assistant
  - asr
  - tts
  - wake-word
  - custom-voice
  - architecture
  - speech-recognition
updated: "2026-03-19"
---

# Custom Voice Assistant Architecture

**Objective:** Design the complete architecture for a custom voice assistant, producing a technical design document covering wake-word detection, ASR (Automatic Speech Recognition) pipeline, NLU engine, dialog management, TTS (Text-to-Speech) synthesis, and deployment topology.

**When to Use:**
- Use when: Building a branded voice assistant (not using Alexa/Google)
- Use when: Designing a voice interface for embedded devices, kiosks, or automotive
- Use when: Evaluating build-vs-buy decisions for voice technology components
- Use when: Planning a voice assistant with specific privacy or latency requirements
- Don't use when: Building on top of Alexa or Google (use platform-specific prompts)

## Instructions

1. **Define Requirements and Constraints**
   - Target hardware: Cloud-connected, edge-only, or hybrid
   - Latency requirements: End-to-end response time budget
   - Privacy requirements: On-device processing, data residency
   - Language support: Languages, dialects, code-switching
   - Domain scope: General-purpose vs domain-specific

2. **Design Wake-Word Detection**
   - Select approach: Custom keyword model vs open-source (Porcupine, Snowboy, OpenWakeWord)
   - Define false acceptance rate (FAR) and false rejection rate (FRR) targets
   - Plan for noisy environments (SNR requirements)
   - Design wake-word confirmation UX (audio chime, visual indicator)
   - Address always-on microphone privacy concerns

3. **Architect ASR Pipeline**
   - Select ASR engine: Cloud (Google STT, AWS Transcribe, Azure Speech, Deepgram, AssemblyAI) vs on-device (Whisper, Vosk, Coqui)
   - Design streaming vs batch recognition strategy
   - Plan for endpoint detection (when user stops speaking)
   - Configure domain-specific language models or custom vocabularies
   - Handle multi-speaker scenarios if needed
   - Design audio preprocessing: noise cancellation, echo cancellation, beamforming

4. **Select NLU Approach**
   - Intent classification + entity extraction: Rasa, LUIS, Dialogflow, custom models
   - LLM-based understanding: GPT/Claude with function calling
   - Hybrid: Traditional NLU for known intents, LLM for open-ended
   - Define confidence thresholds and fallback routing

5. **Design Dialog Management**
   - Select approach: Rule-based, frame-based, or neural dialog management
   - Design state tracking for multi-turn conversations
   - Plan context persistence (session, user, device levels)
   - Define conversation policies (when to ask, confirm, act)
   - Design proactive suggestions and follow-up turns

6. **Configure TTS Synthesis**
   - Select TTS engine: Cloud (Google TTS, Amazon Polly, Azure Neural Voices, ElevenLabs) vs on-device
   - Voice selection: Pre-built voice vs custom voice cloning
   - SSML support for prosody control, emphasis, pauses
   - Design audio caching strategy for common responses
   - Plan for streaming TTS to reduce perceived latency

7. **Plan Deployment and Integration**
   - Client-server architecture: What runs on-device vs in cloud
   - API design between components
   - Monitoring and logging for each pipeline stage
   - A/B testing framework for voice experience iterations
   - Scalability planning for concurrent users

8. **CRITICAL: Validate architecture decisions**
   - Verify latency budget is achievable end-to-end
   - Confirm privacy requirements are met by each component
   - Check that fallback paths exist when any component fails
   - **Confidence levels**: High (proven in production), Medium (emerging tech), Low (experimental)

## False-Positive Prevention (MUST follow)

- **DON'T** recommend cloud-only when latency/privacy requires edge processing
- **DON'T** over-engineer for scale before validating the voice experience works
- **DON'T** assume LLM-based NLU is always better than traditional intent classification
- **DON'T** ignore the "perceived latency" dimension (streaming TTS, progressive responses)
- **DO** include cost estimates for cloud API usage at target scale
- **DO** consider the hardware constraints of the deployment target
- **DO** plan for graceful degradation when network is unavailable

## Expected Output

```markdown
## Custom Voice Assistant Architecture: [Project Name]

### Requirements Summary
| Requirement | Target |
|-------------|--------|
| End-to-end latency | < [X]ms |
| Privacy | [On-device / Cloud / Hybrid] |
| Languages | [List] |
| Deployment | [Cloud / Edge / Hybrid] |

### Component Architecture
[Diagram or description of component flow]
Wake Word → ASR → NLU → Dialog Manager → Response Generator → TTS → Audio Output

### Component Decisions
| Component | Selection | Rationale | Confidence |
|-----------|-----------|-----------|------------|
| Wake Word | [Choice] | [Why] | High/Med/Low |
| ASR | [Choice] | [Why] | High/Med/Low |
| NLU | [Choice] | [Why] | High/Med/Low |
| Dialog | [Choice] | [Why] | High/Med/Low |
| TTS | [Choice] | [Why] | High/Med/Low |

### Latency Budget
| Stage | Target | Notes |
|-------|--------|-------|
| Wake word detection | [X]ms | On-device |
| Audio capture | [X]ms | Endpoint detection |
| ASR | [X]ms | Streaming |
| NLU | [X]ms | [Cloud/Edge] |
| Dialog + Response | [X]ms | Business logic |
| TTS | [X]ms | Streaming |
| **Total** | **[X]ms** | |

### Deployment Architecture
[Infrastructure diagram or description]

### Cost Projection
[Monthly cost at target usage levels]
```

## Techniques Used

- **ST-01 (Clear Objective Statement):** End-to-end architecture design
- **ST-02 (Structured Sequential Instructions):** Component-by-component design flow
- **RT-02 (Multi-Dimensional Analysis):** Evaluates latency, privacy, cost, quality
- **CM-02 (Constraint Specification):** Hardware, latency, privacy constraints
- **DS-06 (Prioritization Guidance):** Component selection with tradeoff analysis

## Customization Guide

- **For Automotive**: Emphasize noise cancellation, hands-free operation, driver distraction limits
- **For Smart Home**: Focus on far-field recognition, multi-room audio, device control
- **For Healthcare**: Add HIPAA compliance, medical terminology, patient safety considerations
- **For Retail Kiosks**: Consider noisy environments, multi-language, accessibility requirements
