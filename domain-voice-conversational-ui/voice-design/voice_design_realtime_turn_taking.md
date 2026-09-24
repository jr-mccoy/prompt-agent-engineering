---
title: "Realtime Voice Agent Turn-Taking & Barge-In — Latency Budget, Endpointing, and Interruption Handling"
category: voice-conversational-ui/voice-design
description: "Tune when a realtime voice agent (cascaded ASR-LLM-TTS or speech-to-speech) starts and stops talking: a measured latency budget from end of user speech to first agent audio, endpointing that adapts to what is being collected, barge-in that stops playback fast and truncates history to what was actually heard, backchannel versus interruption rules, and a test battery for cut-offs, false barge-ins, and talk-over; distinct from the custom voice assistant architecture (component selection) and from IVR call-flow design (menus and routing)."
techniques:
  - CM-02
  - DS-02
  - RT-10
  - QA-10
  - ST-03
difficulty: advanced
tags:
  - realtime-voice
  - turn-taking
  - barge-in
  - endpointing
  - latency
  - voice-agent
  - cuts-people-off
  - awkward-silences
  - talks-over-callers
updated: "2026-09-24"
related_prompts:
  - domain-voice-conversational-ui/voice-design/voice_design_custom_voice_assistant.md
  - domain-voice-conversational-ui/voice-design/voice_design_ivr_call_flow.md
  - domain-voice-conversational-ui/chatbot-design/chatbot_design_llm_powered_architecture.md
---

# Realtime Voice Agent Turn-Taking & Barge-In

**Objective:** Make a realtime voice agent feel like a conversation partner:
it answers quickly, does not cut people off mid-thought, stops when
interrupted, ignores its own echo and background noise, and remembers only
what the caller actually heard.

**When to Use:**
- Callers say the agent "talks over me," "cuts me off," or "takes forever."
- The agent interrupts itself because it hears its own voice or room noise.
- After an interruption, the agent refers to things the caller never heard.
- You are moving from a turn-based IVR to a streaming LLM voice agent.

**Not this prompt if:**
- You are selecting ASR, NLU, TTS, or wake-word components →
  `domain-voice-conversational-ui/voice-design/voice_design_custom_voice_assistant.md`.
- You are designing menus, authentication, and routing on a phone line →
  `voice_design_ivr_call_flow.md`.
- You are designing the LLM layer (RAG, guardrails, tools, cost) →
  `domain-voice-conversational-ui/chatbot-design/chatbot_design_llm_powered_architecture.md`.

## Inputs

1. **Pipeline**: cascaded (VAD → ASR → LLM → TTS) or speech-to-speech; vendors
   and whether each stage streams.
2. **Transport**: phone (PSTN/SIP), WebRTC, app; echo cancellation available?
3. **Current measurements**: latency per stage, if any; call recordings.
4. **Conversation types**: short Q&A, form filling (digits, addresses), long
   explanations, tool calls with slow back ends.
5. **Complaints** and example calls.

## Method

1. **State the constraints (CM-02).** The response-latency target (usually
   stated as a percentile, e.g. p50 and p95), platform limits (codec, jitter
   buffer, echo cancellation), and behaviours that must never happen
   (reading back sensitive data after an interruption, continuing to speak
   over a caller who says "stop").
2. **Build the latency budget (DS-02).** Measure, don't estimate, from the
   caller's last word to the first audible agent audio, split into:
   endpoint wait (silence before the turn is declared over), ASR finalization,
   LLM time to first token, TTS time to first audio, and network/playout.
   Record p50 and p95 for each; a budget that sums averages hides the tail.
   Human turn gaps are typically a few hundred milliseconds; long gaps read
   as confusion or a dropped line.
3. **Tune endpointing by context.** A single silence threshold forces a
   trade-off: short cuts people off, long feels sluggish. Use context:
   - Longer thresholds when collecting digit strings, addresses, or when
     the caller is mid-list or says "um"/"let me see."
   - Shorter after yes/no questions.
   - Semantic or model-based end-of-turn detection where available, with
     silence as the fallback.
4. **Design barge-in.**
   - **Stop time:** playback stops within a target measured from caller
     speech onset `[measure]`.
   - **Truncate history:** record only the portion of the agent's reply
     actually played; the model must not assume the caller heard the rest.
   - **Non-interruptible segments:** legally required disclosures only;
     keep them short.
   - **Echo and noise:** echo cancellation on; a minimum speech duration or
     confidence before treating sound as barge-in.
5. **Separate backchannels from interruptions.** "Mm-hm," "yeah," and "okay"
   during agent speech usually mean *continue*; "wait," "no," "stop," or a
   new question mean *yield*. Define both lists and a default for unclassified speech.
6. **Cover slow operations.** When a tool call will exceed the budget, speak
   a short acknowledgment ("Let me check that table for you") and, for long
   waits, a progress line; never fill with repeated identical phrases.
7. **Diagnose with a decision tree (RT-10).** Symptom → likely stage → test:
   *cuts off* → endpoint too short or no context rule; *slow* → largest p95
   stage; *self-interrupts* → echo; *refers to unheard content* → history
   not truncated; *talks over* → barge-in disabled or too insensitive.
8. **Test (QA-10).** A battery of recorded scenarios: pauses mid-sentence,
   digit strings with gaps, backchannels during long answers, hard
   interruptions, TV noise, speakerphone echo, slow tool calls. Rate each
   finding **High** (measured on real calls), **Medium** (measured in test),
   **Low** (inferred).

## Output Format (ST-03)

```
## Constraints
Latency target (p50/p95) · Transport · Echo cancellation · Must-never behaviours
## Latency budget
| Stage | p50 | p95 | Target | Fix if over |
## Endpointing rules
| Context | Rule | Threshold / method |
## Barge-in design
Stop-time target · History truncation · Non-interruptible segments · Echo/noise gating
## Backchannel vs interruption lexicon
## Slow-operation handling
## Symptom decision tree
## Test battery
| Scenario | Expected | Result | Confidence |
## Measures
Response latency p50/p95 · false cut-off rate · false barge-in rate · talk-over rate · "repeat that" rate
```

## Verification

- [ ] Latency is measured end to end in audio, at p50 and p95, per stage.
- [ ] Endpointing has at least one context-specific rule for slow-input tasks.
- [ ] Barge-in stops playback and truncates history to what was played.
- [ ] Backchannels do not stop the agent; "stop" always does.
- [ ] Echo and noise cases are in the test battery.
- [ ] Every measured number is labelled with its source; unmeasured values are `[measure]`.

## False-Positive Prevention

1. **Do not quote vendor latency as your latency.** Vendor figures exclude your
   network, telephony, and endpoint wait; measure in your own calls.
2. **Do not tune on averages.** A fast p50 with a slow p95 still produces
   calls that feel broken.
3. **Do not treat every sound as barge-in.** Coughs, backchannels, and echo
   are the usual causes of "the agent keeps stopping."
4. **Do not shorten endpointing globally to cut latency.** Fix the slowest
   stage first; shortening endpointing trades speed for cut-offs.
5. **Do not make everything non-interruptible.** Only required disclosures
   justify it; long uninterruptible speech drives hang-ups.
6. **Do not assume a speech-to-speech model removes these problems.** It
   changes the stages, not the need to measure turn-taking.
7. **Do not diagnose from transcripts alone.** Timing problems are invisible in
   text; listen to recordings with timestamps.

## Example

**Input (summary):** Restaurant booking phone agent, cascaded pipeline over SIP,
streaming ASR and TTS. Complaints: "it cut me off when I gave my phone number";
"it kept talking when I said no"; ~2-second silences before replies.

```
## Constraints
Target: p50 ≤ 1.0 s, p95 ≤ 1.8 s to first audio [agreed with product].
Transport: SIP, carrier echo cancellation on. Must never: continue after "stop";
read back a card number (none collected).

## Latency budget (measured on 200 calls)
| Stage | p50 | p95 | Target | Fix if over |
|---|---|---|---|---|
| Endpoint wait | 700 ms | 700 ms | context rule | see rules |
| ASR final | 150 ms | 300 ms | ok | — |
| LLM first token | 600 ms | 1,400 ms | 500 / 900 | smaller model for routing turns; shorter system prompt |
| TTS first audio | 200 ms | 350 ms | ok | — |
| Network/playout | 120 ms | 250 ms | ok | — |
| Sum of stages | 1.77 s | 3.0 s (upper bound; measured end-to-end p95 2.6 s) | 1.0 / 1.8 s | LLM is the p95 driver |

## Endpointing rules
| Context | Rule | Threshold |
|---|---|---|
| Collecting phone number | Wait for 11 digits or 1.5 s silence | 1.5 s |
| Yes/no question | Short | 500 ms |
| Default | Semantic end-of-turn, silence fallback | 700 ms |

## Barge-in design
Stop-time target ≤ 200 ms [measure]. History keeps only played text (the
"no" complaint: agent had kept the full unplayed confirmation in history).
Non-interruptible: none. Gate: ≥ 250 ms of speech above noise floor.

## Backchannel vs interruption lexicon
Continue: mm-hm, yeah, okay, right. Yield: no, wait, stop, hang on, any question.
Unclassified: yield if > 600 ms of speech.

## Slow-operation handling
Table lookup > 1 s: "Let me check what we have for Saturday."

## Symptom decision tree
Cut off during number → endpoint rule (fixed). Kept talking at "no" → barge-in
gate too high + history not truncated (fixed). 2 s silences → LLM p95 (fix above).

## Test battery
| Scenario | Expected | Result | Conf. |
|---|---|---|---|
| Number read in 3 chunks with pauses | Captured whole | Pass | Medium |
| "Mm-hm" during confirmation | Agent continues | Pass | Medium |
| "No, Sunday" mid-confirmation | Stops; asks about Sunday | Pass | Medium |
| TV in background | No false barge-in | Fail — raise gate | Medium |

## Measures
Weekly: latency p50/p95, false cut-offs (callers saying "I wasn't finished"),
false barge-ins, "can you repeat that" rate.
```

## Techniques Used

- **CM-02 Constraint Specification** — latency targets and must-never behaviours.
- **DS-02 Metric Specification** — per-stage p50/p95 budget and turn-taking measures.
- **RT-10 Troubleshooting Decision Tree** — symptom to stage to test.
- **QA-10 Test Battery Protocol** — recorded scenario battery.
- **ST-03 Output Format Specification** — budget, rules, and battery tables.

## Related Prompts

- `domain-voice-conversational-ui/voice-design/voice_design_custom_voice_assistant.md` — component selection.
- `domain-voice-conversational-ui/voice-design/voice_design_ivr_call_flow.md` — phone menus and routing.
- `domain-voice-conversational-ui/chatbot-design/chatbot_design_llm_powered_architecture.md` — the LLM layer.
