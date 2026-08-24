# Other Modalities

The modalities that do not have a subdirectory of their own — multimodal fusion, speech, non-speech audio, and anomaly detection where the modality is not the defining feature.

**4 prompts.** Part of [`domain-AI-ML/`](../README.md) — see the domain README for the lifecycle routing table and the [boundary with adjacent domains](../README.md#boundary-with-adjacent-domains).

## When to enter here

- Combining inputs of different types in one model.
- Speech (ASR/TTS/diarization) or non-speech audio.
- Anomaly detection under extreme imbalance where the signal type is not the organizing question.

**Not here:**
- The audio is speech and the task is transcription or synthesis — that is `mlmodal_speech_asr_tts_framing.md` here, but check whether the real question is a vision or text one after transcription.
- The anomalies are in a temporal sensor signal — [`../time-series/ts_anomaly_detection_design.md`](../time-series/ts_anomaly_detection_design.md).

## Prompts

| Prompt | Use it to |
|---|---|
| [`mlmodal_multimodal_architecture.md`](mlmodal_multimodal_architecture.md) | Design a multimodal model for a combined-input task — fusion strategy, cross-modal alignment, modality dropout, and missing-modality handling — without assuming a fancy architecture is needed. |
| [`mlmodal_speech_asr_tts_framing.md`](mlmodal_speech_asr_tts_framing.md) | Frame a speech task — ASR, TTS, or diarization — pinning down its data requirements, the right metrics (WER/CER, MOS, DER), and the acoustic and evaluation pitfalls that fool teams new to audio. |
| [`mlmodal_audio_ml_design.md`](mlmodal_audio_ml_design.md) | Design machine learning on audio that is not speech — sound events, music, machine and bioacoustic signals — choosing the representation against what the signal looks like in time and frequency, and preventing the recording-condition leakage that inflates audio results. |
| [`mlmodal_anomaly_outlier_detection.md`](mlmodal_anomaly_outlier_detection.md) | Design anomaly/outlier detection under extreme class imbalance — choose unsupervised vs semi-supervised framing, set defensible thresholds, and evaluate with metrics that don't lie when positives are rare. |

## Conventions

- **Prefix:** `mlmodal_` — one prefix per subdirectory, so a filename identifies its home.
- **Frontmatter:** the domain's eight fields — `title`, `category` (`AI-ML/specialized-ml/other-modalities`), `description`, `techniques` (validated against `techniques/MASTER_TECHNIQUE_INDEX.md`), `difficulty`, `tags`, `updated`, `related_prompts`.
- **Structure:** five H2 sections — `Inputs / Context`, `Constraints`, `Verification`, `False-Positive Prevention`, `Example Output` — with `Objective`, `When to Use`, `When NOT to Use`, `Instructions`, `Output Format`, `Techniques Used`, `Related Prompts` as bold labels inside them.
- **No fabrication:** no invented benchmark numbers, accuracy figures, SOTA claims, or dataset statistics. Quantities that would change a decision are marked for measurement or verification.
- **Framework-neutral:** the user names the stack; prompts avoid hardcoding APIs that drift.

## What lives elsewhere

- Graph ML, which graduated to its own vertical → [`../graph-ml/`](../graph-ml/README.md).
- Vision-specific modalities (video, 3D, OCR) → [`../computer-vision/`](../computer-vision/README.md).
