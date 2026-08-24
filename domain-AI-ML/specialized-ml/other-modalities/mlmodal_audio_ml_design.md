---
title: "Audio ML Design (Non-Speech)"
category: AI-ML/specialized-ml/other-modalities
description: "Design machine learning on audio that is not speech — sound events, music, machine and bioacoustic signals — choosing the representation against what the signal looks like in time and frequency, and preventing the recording-condition leakage that inflates audio results."
techniques:
  - RT-02
  - ST-02
  - CM-02
  - QA-12
  - DS-02
difficulty: advanced
tags:
  - audio-ml
  - sound-event-detection
  - spectrogram
  - acoustic-monitoring
  - audio-augmentation
updated: "2026-08-22"
related_prompts:
  - domain-AI-ML/specialized-ml/other-modalities/mlmodal_speech_asr_tts_framing.md
  - domain-AI-ML/specialized-ml/other-modalities/mlmodal_anomaly_outlier_detection.md
  - domain-AI-ML/specialized-ml/time-series/ts_anomaly_detection_design.md
  - domain-AI-ML/data-for-ml/mldata_data_leakage_detector.md
---

# Audio ML Design (Non-Speech)

**Objective:** Design a model for audio that is not speech — sound-event detection, acoustic monitoring, music, bioacoustics, machine-condition audio — by choosing the representation from the signal's own time and frequency structure, and by defending against the recording-condition leakage that makes audio results look far better than they are.

**When to Use:**
- Classifying, detecting, or monitoring non-speech sound: machinery, environment, wildlife, music, alarms.
- Audio anomaly detection where the normal condition is known and failures are rare.
- An audio model performs well in evaluation and poorly in deployment, which is usually leakage.

**When NOT to Use:**
- The task is speech — transcription, synthesis, speaker identification — use `mlmodal_speech_asr_tts_framing.md`.
- The signal is a non-audio time series; use `../time-series/`, though the leakage cautions here transfer.
- The task is generative audio, which is a different design problem.

## Inputs / Context

- **The sound of interest** — its duration, whether it is transient or sustained, and where its energy sits in frequency.
- **Recording conditions** — devices, placements, environments, and **whether these correlate with the label**, which is the central risk.
- **Background and interference** — what else is present, and whether it is stationary.
- **Label granularity** — clip-level (present somewhere), frame-level (when), or source-level (which and when).
- **Deployment constraints** — on-device or server, latency, and whether detection must be real-time.
- **Class balance** — for monitoring tasks, events are usually rare.

## Constraints

**Must:**
- Choose the representation from the signal's structure — window length must be short enough to resolve the event and long enough to capture it. A transient click and a sustained hum need different analysis windows, and a single default serves one badly.
- Split data by **recording session, device, and location**, never randomly. Random splitting on audio puts adjacent segments of the same recording in train and test, which is the leakage that produces excellent evaluation numbers and a model that has learned the room.
- Check whether recording conditions correlate with labels. If failures were recorded on one machine and normal operation on another, the model can classify the machine rather than the condition, and standard metrics cannot tell the difference.
- Match label granularity to the requirement: clip-level labels cannot train frame-level detection.
- Design augmentation against realistic deployment variation — device response, background, distance, reverberation — not against arbitrary transformations.

**Must Not:**
- Assert window sizes, sample rates, feature parameters, or model comparisons from memory; mark quantities `[choose from your signal's characteristics]`.
- Split randomly at the segment level, ever.
- Evaluate only on recordings from the same devices and locations as training, then claim generalization.
- Apply augmentations that destroy the discriminative property — pitch shifting where pitch is the signal, time stretching where rhythm is the signal.
- Report clip-level accuracy for a task that needs temporal localization.

**Instructions:**

1. **Characterize the signal in time and frequency.** Duration of the event, transient or sustained, and where its energy lies. This determines window length, hop size, and frequency resolution, and it is a measurement rather than a default.

2. **Audit recording conditions against labels — the decisive step.** Tabulate device, location, session, and time against the label. Any correlation is a leakage path: the model can achieve high accuracy by identifying the recording context rather than the sound. This audit precedes everything else because it can invalidate the entire dataset.

3. **Design the split.** Group by session, device, and location. Hold out **entire devices or locations** to measure generalization to unseen conditions, since that is what deployment requires. Report both within-condition and cross-condition performance; the gap between them is the honest measure of what the model learned.

4. **Choose the representation.**
   - *Time-frequency (spectrogram family)* — the default for most tasks; parameters set by step 1.
   - *Learned from raw waveform* — avoids fixed-parameter choices, needs more data.
   - *Hand-crafted acoustic features* — interpretable, strong where the discriminative property is known.
   - *Pretrained audio embeddings* — strong with limited data; check the pretraining domain resembles yours.
   State the parameters and their justification from the signal, not from convention.

5. **Match architecture to label granularity.** Clip-level classification, frame-level detection with temporal output, or source separation. Do not promise temporal localization from clip-level labels.

6. **Design augmentation from deployment variation.** Realistic device impulse responses, background mixing at realistic signal-to-noise ratios, distance and reverberation, and time shifts. **Exclude** any augmentation that destroys the signal — check each against the discriminative property before adopting it.

7. **Handle imbalance and temporal structure.** For rare events, decide the sampling and loss treatment. For temporal outputs, decide post-processing: smoothing, minimum event duration, and merging of adjacent detections. These post-processing choices frequently affect the reported metric more than the model does, so they belong in the design.

8. **Choose evaluation matched to the task.** Clip-level metrics for presence; event-based metrics with a tolerance for detection; and per-condition breakdowns throughout. State the tolerance explicitly, since event-based scores are highly sensitive to it.

9. **Plan the deployment check.** Record in the actual deployment environment with the actual device before trusting any number, because acoustic environments differ in ways no augmentation fully anticipates.

**Output Format:**

A markdown design:
- **Signal Characterization** — duration, transient/sustained, frequency content.
- **Recording-Condition Audit** — table: Condition | Correlates with label? | Leakage risk.
- **Split Design** — grouping, held-out conditions, what each measures.
- **Representation** — chosen, with parameters justified from the signal.
- **Architecture & Label Granularity** — matched pair.
- **Augmentation** — table: Augmentation | Simulates | Safe for this signal?
- **Imbalance & Post-Processing** — sampling, smoothing, minimum duration, merging.
- **Evaluation** — metrics, tolerance, per-condition breakdown.
- **Deployment Check** — what is recorded where, before trusting results.

## Verification

- [ ] Signal duration and frequency content are characterized before parameters are chosen.
- [ ] Recording conditions are audited against labels for correlation.
- [ ] Splits are grouped by session, device, and location — never random.
- [ ] Held-out devices or locations measure cross-condition generalization.
- [ ] Both within-condition and cross-condition performance are reported.
- [ ] Representation parameters are justified from the signal.
- [ ] Architecture matches the available label granularity.
- [ ] Every augmentation is checked against the discriminative property.
- [ ] Post-processing choices are stated as part of the design.
- [ ] A real-environment deployment check is planned.

## False-Positive Prevention

❌ **DON'T:**
- Split audio segments randomly — adjacent segments from one recording land on both sides, and the resulting scores measure memorization of the recording, not recognition of the sound.
- Report strong results without checking whether recording conditions correlate with labels; a model that identifies the machine rather than the fault scores identically on every standard metric.
- Use default spectrogram parameters for a transient event; a window long enough to smear a click destroys the thing you are trying to detect.
- Pitch-shift as augmentation when pitch carries the label, or time-stretch when rhythm does — the augmentation asserts an invariance that is false for your task.
- Claim temporal localization from a model trained on clip-level labels.
- Trust evaluation numbers from the same rooms and devices as training as evidence of deployment readiness.

✅ **DO:**
- Set window and hop from the measured event duration and frequency content.
- Run the condition-versus-label audit before anything else; it can invalidate the dataset.
- Group splits by session, device, and location, and hold out whole conditions.
- Report the within-condition and cross-condition gap as the honest generalization measure.
- Check each augmentation against the discriminative property before adopting it.
- Record in the real environment on the real device before believing the numbers.

## Example Output

```markdown
## Audio ML Design: Industrial Pump Fault Detection
Detect bearing faults from microphones near pumps, before failure.

### Signal Characterization
Bearing faults present as **periodic impulses** at fault frequencies related to rotation speed,
plus a broadband component. Events are **transient and repeating**, not sustained.
Implications: window short enough to resolve individual impulses; frequency resolution
sufficient to separate fault harmonics; hop small enough that impulses are not missed between
frames. `[choose all three from measured impulse duration and rotation speed — a default
configuration tuned for sustained sounds will smear exactly the feature that matters.]`

### Recording-Condition Audit — run this first
| Condition | Correlates with label? | Leakage risk |
|---|---|---|
| **Pump unit** | **Yes** — faults recorded on 3 units, normal on 11 | **Severe** |
| **Location** | **Yes** — faulty units are in the older hall | **Severe** |
| Microphone model | Partially — hall B uses newer mics | High |
| Time of day | No | Low |
| Season | Unknown — faults collected in one month | **Unknown, treat as risk** |

**This audit changes the project.** With faults recorded on 3 units in one hall, a model can
reach excellent accuracy by recognizing the hall's acoustics or the specific units — and every
standard metric will report success. Either collect fault audio from more units and halls, or
accept that cross-condition performance is the only number worth reporting.

### Split Design
Grouped by **pump unit**, so no unit appears in both train and test.
- **Within-condition:** held-out recordings from training units — measures fault recognition.
- **Cross-condition:** held-out **entire units and one entire hall** — measures what deployment
  actually needs.
Report both. The gap is the honest generalization measure, and given the audit above it is
expected to be large.

### Representation
Time-frequency, with window, hop, and frequency scale chosen from the impulse duration and fault
harmonic spacing measured in step 1. A perceptually-motivated frequency scale designed for speech
compresses the high frequencies where bearing fault energy sits — a linear or fault-frequency-
aligned scale is likely more appropriate here `[verify against your measured spectra]`.

### Architecture & Label Granularity
Available labels are **clip-level** (this recording contains a fault). Therefore: clip-level
classification. Frame-level "when did the fault occur" is **not** available from these labels and
must not be promised; obtaining it requires frame-level annotation that does not currently exist.

### Augmentation
| Augmentation | Simulates | Safe for this signal? |
|---|---|---|
| Background mixing (other machinery) at realistic SNR | different hall occupancy | **Yes** |
| Device impulse response variation | different microphone models | **Yes** |
| Distance / reverberation simulation | different mic placement | **Yes** |
| Time shift | arbitrary recording start | **Yes** |
| **Pitch shift** | — | **NO** — fault frequencies are the signal; shifting them destroys the label |
| **Time stretch** | — | **NO** — impulse periodicity is the signal |
| Loud additive white noise | — | **No** — masks the impulses at realistic fault amplitudes |

The two excluded augmentations are the two most standard in general audio pipelines. Adopting
them by default here would train the model to be invariant to the exact property that
distinguishes a fault.

### Imbalance & Post-Processing
Faults are rare. Sampling and loss treatment `[choose]`. Post-processing: a minimum consecutive
detection duration before an alert fires, to suppress isolated frame-level false positives.
**This threshold affects the reported metric more than most modelling choices** — it belongs in
the design and in the evaluation description, not in a serving script nobody reads.

### Evaluation
Clip-level metrics, matched to the clip-level labels. Per-condition breakdown by unit and hall,
always. Because faults are rare, report precision and recall rather than accuracy, and state the
operating threshold — a maintenance team's tolerance for false alarms sets it, not the F1 peak.

### Deployment Check
Before trusting anything: record on a **real pump in a hall not represented in training**, with
the **production microphone and placement**, and evaluate there. Acoustic environments differ in
reverberation, background machinery, and mounting resonance in ways no augmentation fully
anticipates, and this is the only measurement that reflects what will be deployed.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** signal structure × recording condition × representation × augmentation safety is the design grid.
- **ST-02 (Structured Sequential Instructions):** the condition audit precedes design because it can invalidate the dataset.
- **CM-02 (Constraint Specification):** the grouped-split and augmentation-safety rules are hard constraints.
- **QA-12 (False Positives Identification):** targets recording-condition leakage, the failure that makes audio results look excellent and deploy badly.
- **DS-02 (Metric Specification):** within-condition and cross-condition performance are specified as separate reportable quantities.

**Related Prompts:**
- `mlmodal_speech_asr_tts_framing.md` — when the audio is speech.
- `mlmodal_anomaly_outlier_detection.md` — the general anomaly framing for rare-event monitoring.
- `../time-series/ts_anomaly_detection_design.md` — for non-audio sensor signals from the same machines.
- `../../data-for-ml/mldata_data_leakage_detector.md` — the general leakage check behind the condition audit.
