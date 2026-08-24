---
title: "OCR Pipeline Design"
category: AI-ML/specialized-ml/computer-vision
description: "Design a detect → recognize → post-process OCR pipeline with layout/structure recovery, language/script coverage, and CER/WER-based evaluation — matched to the document types, scripts, and downstream consumers, with template-overfit-aware splits."
techniques:
  - ST-02
  - RT-02
  - CM-02
  - DS-01
  - QA-12
difficulty: advanced
tags:
  - computer-vision
  - ocr
  - text-recognition
  - layout-analysis
  - cer-wer
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/specialized-ml/computer-vision/cv_task_framing.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_annotation_strategy.md
  - domain-AI-ML/specialized-ml/computer-vision/cv_object_detection_eval.md
---

# OCR Pipeline Design

**Objective:** Help the user design an OCR system as a multi-stage pipeline — text detection, text recognition, layout/structure recovery, and post-processing — rather than treating it as a single "read the image" black box. The decisions are how to detect text regions (and whether word-, line-, or block-level), how to recognize the cropped text (sequence models with appropriate decoding), how to recover reading order and structure (tables, forms, multi-column), what languages and scripts must be covered (and whether one model generalizes across them), and how to evaluate honestly with character and word error rates rather than a vague "accuracy." This prompt produces a framework-neutral design with a leakage-safe evaluation protocol that guards against template overfitting.

**When to Use:**
- You need to extract text from images or scanned documents and must choose detection, recognition, and structure components.
- Your documents have layout structure (forms, tables, receipts, multi-column pages) that downstream consumers depend on.
- You must support multiple languages or scripts and need a coverage and evaluation plan.

**When NOT to Use:**
- The task is general image classification or object detection, not text reading — use `cv_task_framing.md`.
- You only need an annotation plan for text regions — see `cv_annotation_strategy.md`.
- You need detection-metric design in isolation — see `cv_object_detection_eval.md`.

## Inputs / Context

Provide what you can:
- **Document types & sources** — printed/handwritten, scans/photos, forms/receipts/free text; image quality range.
- **Languages & scripts** — which languages, and whether scripts mix (Latin, Arabic, CJK, Cyrillic, Devanagari).
- **Structure requirements** — does the consumer need reading order, tables, key-value pairs, or just raw text?
- **Template metadata** — document template/form ID, vendor, or source — needed to prevent template-overfit leakage.
- **Volume & label availability** — number of documents and whether transcriptions/boxes exist.
- **Downstream consumer** — search index, data entry, RAG, accessibility — sets the error tolerance and structure needs.
- **Latency & deployment budget** — batch vs. real-time, on-device vs. server.

## Constraints

**Must:**
- Treat OCR as staged (detect → recognize → post-process) and justify each stage's granularity.
- Report evaluation in CER and WER (and structure metrics where layout matters), not bare "accuracy."
- State language/script coverage explicitly and whether a single model is expected to generalize across scripts.
- Group splits so documents sharing a template/form do not span train and test.

**Must Not:**
- Fabricate CER/WER, accuracy, or benchmark numbers from memory; reason from the user's data and mark unknowns "measure on your data."
- Assert version-specific API behavior of any OCR engine or library from memory — flag "verify against current docs."
- Assume one language/script model generalizes to others without measurement.
- Report a single end-to-end accuracy without CER/WER, or allow template-overfit leakage between splits.

**Instructions:**

1. **Restate the extraction goal and consumer.** Clarify whether the output is raw text, structured key-value pairs, or full layout — and what error tolerance the consumer has.
2. **Profile the documents.** Note print vs. handwriting, quality, skew, scripts, and structure (forms, tables, columns). These drive detection granularity and recognition difficulty.
3. **Design the detection stage.** Choose word/line/block granularity and an approach appropriate to layout density and orientation. Specify how reading order is established.
4. **Design the recognition stage.** Choose a sequence-recognition approach and decoding, matched to script and vocabulary. Flag scripts (e.g., RTL, complex shaping) needing special handling.
5. **Plan structure/layout recovery.** Decide whether to recover tables, key-value pairs, or multi-column order, and how (rules vs. learned layout model). Tie this to the consumer's needs.
6. **Set language/script coverage.** Enumerate required scripts; decide single multilingual model vs. per-script models, and commit to measuring cross-script generalization rather than assuming it.
7. **Design post-processing.** Add normalization, lexicon/spell correction, and confidence thresholds where they help the consumer — without masking recognition error in metrics.
8. **Define leakage-safe evaluation.** Group splits by template/form ID. Report CER and WER, plus structure metrics (e.g., field-level F1) where layout matters, and name a baseline. Flag all numbers as "to be measured."

**Output Format:**

A markdown design brief:
- **Extraction Goal & Consumer** — restated output and error tolerance.
- **Document Profile** — print/handwriting, quality, scripts, structure.
- **Detection Stage** — granularity, approach, reading-order handling.
- **Recognition Stage** — model family, decoding, script-specific notes.
- **Structure Recovery** — tables/KV/columns plan, or N/A.
- **Language/Script Coverage** — scripts, single vs. per-script, generalization test.
- **Post-Processing** — normalization, correction, confidence handling.
- **Evaluation Protocol** — template-grouped splits, CER/WER, structure metrics, baseline.
- **Open Questions / Measure-On-Your-Data** — unknowns flagged for empirical resolution.

## Verification

- [ ] The pipeline is staged (detect → recognize → post-process) with each stage's granularity justified.
- [ ] Evaluation reports CER and WER (and structure metrics where layout matters), not bare accuracy.
- [ ] Language/script coverage is explicit and cross-script generalization is a measured claim, not assumed.
- [ ] Splits are grouped by template/form so shared templates cannot leak across train/test.
- [ ] Post-processing improvements are not allowed to mask raw recognition error in reported metrics.
- [ ] No CER/WER or benchmark numbers are invented and no version-specific API behavior is asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Report a single end-to-end "accuracy" and treat it as sufficient — it hides character- and word-level error structure.
- Assume a model trained on one language/script reads another well without measuring it.
- Split documents randomly so the same form template appears in both train and test, overfitting to layout.
- Let lexicon correction in post-processing inflate metrics so the recognizer's true error is invisible.

✅ **DO:**
- Report CER and WER (plus field-level F1 for structured fields) on a held-out, template-disjoint set.
- Enumerate required scripts and test cross-script generalization explicitly before claiming coverage.
- Group splits by template/form ID so layout overfitting cannot leak into the test set.
- Evaluate raw recognition and post-processed output separately so correction gains are visible, not hidden.

## Example Output

```markdown
## Extraction Goal & Consumer
Extract key-value fields from supplier invoices → data-entry system. Field errors are costly.

### Document Profile
Printed invoices, mixed Latin + some CJK supplier names; tables present; moderate scan skew.

### Detection Stage
Line-level detection with orientation handling; reading order via geometric sort + table grouping.

### Recognition Stage
Sequence recognizer with CTC decoding; CJK handled by a multilingual head (generalization to be tested).

### Structure Recovery
Learned key-value linking for header fields; rule-based table cell grouping.

### Language/Script Coverage
Required: Latin + CJK. Single multilingual model; cross-script CER measured separately.

### Evaluation Protocol
Splits grouped by template/vendor ID. Report CER, WER, field-level F1.
Baseline: off-the-shelf engine. All numbers: measure on your data.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Ordered steps move goal → profile → detect → recognize → structure → evaluate.
- **RT-02 (Multi-Dimensional Analysis Framework):** Each stage choice is tied to a document property and consumer need.
- **CM-02 (Constraint Specification):** Detection granularity and single-vs-per-script models are weighed as tradeoffs.
- **DS-01 (Framework Application):** Named brief sections capture the staged design reproducibly.
- **QA-12 (False Positives Identification):** Checks force CER/WER reporting and template-disjoint splits.

**Related Prompts:**
- `cv_task_framing.md` — frames the task before committing to an OCR pipeline.
- `cv_annotation_strategy.md` — plans text-region and transcription annotation for training data.
- `cv_object_detection_eval.md` — defines IoU-based detection metrics applicable to the text-detection stage.
