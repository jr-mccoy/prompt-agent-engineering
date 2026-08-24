---
title: "Speech Task Framing (ASR / TTS / Diarization)"
category: AI-ML/specialized-ml/other-modalities
description: "Frame a speech task — ASR, TTS, or diarization — pinning down its data requirements, the right metrics (WER/CER, MOS, DER), and the acoustic and evaluation pitfalls that fool teams new to audio."
techniques:
  - ST-02
  - DS-02
  - CM-02
  - QA-12
  - RT-05
difficulty: intermediate
tags:
  - speech
  - asr
  - tts
  - diarization
  - audio-metrics
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/other-modalities/mlmodal_multimodal_architecture.md
  - domain-AI-ML/specialized-ml/other-modalities/mlmodal_anomaly_outlier_detection.md
  - domain-AI-ML/specialized-ml/graph-ml/graphml_task_framing.md
---

# Speech Task Framing (ASR / TTS / Diarization)

**Objective:** Frame a speech/audio task — automatic speech recognition (ASR), text-to-speech (TTS), or speaker diarization — into a well-posed problem: what data it requires, the correct evaluation metrics (WER/CER, MOS/intelligibility, DER), and the acoustic, linguistic, and evaluation pitfalls that mislead teams new to the audio modality, before model selection.

**When to Use:**
- You are scoping a speech project and need the data, metric, and pitfall picture before building.
- A speech model "looks good" on a generic benchmark but fails on the target audio conditions.
- You must choose the right metric and split for a specific speech subtask.

**When NOT to Use:**
- The task is a general multimodal fusion problem where speech is one input (use `mlmodal_multimodal_architecture.md`).
- You need an algorithm-family decision for non-speech RL/graph tasks (use the relevant prompt).

## Inputs / Context

Provide what you can:
- **Subtask** — ASR (speech→text), TTS (text→speech), diarization (who spoke when), or a combination.
- **Audio conditions** — sampling rate, mono/multichannel, noise/reverb, far-field vs close-talk, codec.
- **Language / domain** — languages, accents, code-switching, domain vocabulary (medical, names, jargon).
- **Speaker set** — number of speakers, overlap, known vs unknown speakers (for diarization/verification).
- **Available data** — transcribed audio hours, alignment quality, reference recordings (for TTS).
- **Deployment** — streaming vs batch, latency budget, on-device vs server.

## Constraints

**Must:**
- Select metrics that match the subtask and the way errors actually matter (WER/CER for ASR, MOS + objective proxies for TTS, DER for diarization).
- Specify a data split that prevents speaker and recording-session leakage across train/test.
- State the acoustic-condition match required between training data and deployment audio.

**Must Not:**
- Report a single WER without noting reference normalization (casing, punctuation, numbers) and the condition it was measured on.
- Quote benchmark WER/MOS numbers from memory as if measured on the user's data.
- Treat subjective TTS quality (MOS) as if it were an automatic metric that needs no human ratings.

**Instructions:**

1. **Pin the subtask and output contract.** State exactly what is consumed and produced (audio→text tokens, text→waveform, audio→speaker-labeled segments), including streaming vs full-utterance and any timing requirements.

2. **Profile the acoustic & linguistic conditions.** Document sampling rate, noise/reverb, far/near field, channels, accents, code-switching, and domain vocabulary. Mismatch here is the dominant real-world failure cause.

3. **Define the data requirements and split.** Specify transcription/alignment quality and required hours. Design the split to keep the *same speaker* and *same recording session* out of both train and test — speaker/session leakage silently inflates ASR/diarization scores.

4. **Select metrics matched to the subtask.** ASR: WER/CER with explicit normalization rules (and substitutions/insertions/deletions breakdown); consider domain-weighted error for critical terms. TTS: MOS / preference tests as primary (human), with intelligibility (WER through ASR) and objective proxies as supporting — never MOS-by-fiat. Diarization: DER with collar and overlap handling stated.

5. **Surface subtask-specific pitfalls.** ASR: rare-word/named-entity errors hidden by overall WER, normalization gaming. TTS: pronunciation of names/numbers, prosody, hallucinated or skipped words. Diarization: overlapped speech, speaker count estimation, short-segment boundaries.

6. **Plan condition-stratified evaluation.** Break metrics out by noise level, accent, speaker, and domain segment so an aggregate number can't hide failure on a critical slice (the audio analog of slice-based evaluation).

7. **Decide build-vs-adapt.** Given conditions and data, decide whether a pretrained/foundation speech model fine-tuned/adapted suffices, or a from-scratch model is warranted — and what data each path needs.

8. **Deliver the framing + measurement plan.** Output the task contract, data/split plan, metric definitions, pitfall watchlist, and the stratified eval design.

**Output Format:**

A markdown report:
- **Task Contract** — subtask, I/O, streaming/latency.
- **Acoustic & Linguistic Profile** — conditions, accents, vocabulary; deployment-match note.
- **Data & Split Plan** — hours/quality; speaker/session-leakage-safe split.
- **Metrics** — table: Metric | Subtask role | Definition/normalization | Human vs automatic.
- **Pitfall Watchlist** — subtask-specific failure modes.
- **Stratified Eval Design** — slices to report.
- **Build vs Adapt** — recommendation + data needs.

## Verification

- [ ] Metrics match the subtask (WER/CER, MOS+intelligibility, DER) with definitions/normalization stated.
- [ ] The split prevents speaker and recording-session leakage.
- [ ] Acoustic/linguistic conditions are profiled and matched to deployment.
- [ ] TTS quality plan includes human ratings, not just objective proxies.
- [ ] Evaluation is stratified by condition/accent/speaker, not aggregate-only.
- [ ] No fabricated benchmark numbers; external claims marked unverified.

## False-Positive Prevention

❌ **DON'T:**
- Trust a low overall WER that hides large errors on names, numbers, or a key accent.
- Put the same speaker or recording session in train and test — it inflates ASR/diarization scores like data leakage.
- Report TTS as "good" from an objective proxy alone without human MOS/preference tests.
- Compare WER numbers measured under different normalization rules as if equivalent.

✅ **DO:**
- Stratify metrics by noise, accent, speaker, and domain to expose hidden failures.
- Enforce speaker- and session-disjoint splits.
- Anchor TTS quality in human ratings, with intelligibility (ASR-WER) and proxies as support.
- State and hold constant the reference normalization (case, punctuation, numbers) for every WER.

## Example Output

```markdown
## Speech Framing: Clinical Dictation ASR (English, far-field exam rooms)

### Task Contract
ASR, streaming, partial results <300 ms latency; output text with medical terms preserved.

### Acoustic & Linguistic Profile
16 kHz mono, far-field, HVAC + multi-speaker background; accented clinicians; heavy medical vocabulary and drug names. Deployment audio is noisier than typical training corpora → condition mismatch risk HIGH.

### Data & Split Plan
Need ≥300 hrs in-domain. Split by clinician AND by room/session — no clinician or recording session in both train and test (else leakage inflates WER).

### Metrics
| Metric | Role | Definition/normalization | Human/auto |
|---|---|---|---|
| WER | Primary | lowercased, punctuation-stripped, numbers spoken-form | auto |
| Drug-term error rate | Critical | weighted over a curated drug lexicon | auto |
| S/I/D breakdown | Diagnostic | per error type | auto |

### Pitfall Watchlist
- Overall WER masks drug-name errors (clinically critical).
- Normalization could hide capitalization/number errors that matter in notes.
- Far-field noise degrades far below benchmark numbers.

### Stratified Eval Design
Report WER by: noise level (quiet/HVAC/crowded), accent group, clinician, specialty vocabulary.

### Build vs Adapt
Adapt a pretrained foundation ASR model with in-domain fine-tuning + a medical lexicon/biasing list; from-scratch unjustified given limited hours.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** contract → conditions → data/split → metrics → pitfalls → eval.
- **DS-02 (Metric Specification):** WER/CER/MOS/DER definitions and normalization rules.
- **CM-02 (Constraint Specification):** acoustic-condition match and leakage-safe split as constraints.
- **QA-12 (False Positives Identification):** catches speaker/session leakage and aggregate-WER masking.
- **RT-05 (Evidence-Based Reasoning):** ties metric and pitfall choices to the stated conditions.

**Related Prompts:**
- `mlmodal_multimodal_architecture.md` — when speech is one input among several.
- `mlmodal_anomaly_outlier_detection.md` — flag out-of-condition audio at inference.
- `../graph-ml/graphml_task_framing.md` — for relational tasks unrelated to speech.
