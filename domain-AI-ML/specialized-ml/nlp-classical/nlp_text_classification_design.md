---
title: "Classical Text Classification Pipeline Designer"
category: AI-ML/specialized-ml/nlp-classical
description: "Design a non-LLM text classification pipeline — representation, model, evaluation, and class-imbalance handling — with leakage-safe preprocessing and metrics that survive imbalanced, multi-label, or skewed-cost settings."
techniques:
  - ST-02
  - RT-02
  - DS-02
  - QA-12
  - CM-02
difficulty: intermediate
tags:
  - nlp
  - text-classification
  - tf-idf
  - imbalance
  - evaluation
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_tokenization_representation_strategy.md
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_text_preprocessing_pipeline.md
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_ner_extraction_design.md
---

# Classical Text Classification Pipeline Designer

**Objective:** Produce an end-to-end design for a non-LLM text classification system — choosing the text representation, the model, the evaluation protocol, and the class-imbalance strategy — with preprocessing placed so it cannot leak, and metrics chosen so they reflect performance on rare and high-cost classes rather than being inflated by a dominant majority class.

**When to Use:**
- Building a classical (TF-IDF / linear / tree / classical-embedding) text classifier where an LLM is overkill, too costly, too slow, or non-explainable.
- A text classifier reports high accuracy but fails on the classes that matter.
- Choosing between bag-of-words baselines and embedding-based classical models.

**When NOT to Use:**
- The task genuinely needs an LLM workflow (cross-link `genai-llm-engineering`).
- You need entity/span extraction, not whole-document labels (use `nlp_ner_extraction_design.md`).

## Inputs / Context

- **Task** — single-label / multi-label / multi-class; the label set and what each label means.
- **Class distribution** — frequencies; which classes are rare and which are costly to miss.
- **Text characteristics** — length, language(s), domain jargon, noise (typos, code-switching), source (reviews, tickets, logs).
- **Data volume** — labeled examples per class; availability of unlabeled text.
- **Constraints** — latency, interpretability needs, deployment footprint.
- **Cost asymmetry** — relative cost of each error type (e.g., missing a fraud/abuse label vs a false flag).

## Constraints

**Must:**
- Fit all representation and preprocessing (vectorizer vocabulary, IDF, scaling, resampling) on the training fold only, inside a pipeline/CV — never on the full corpus.
- Choose metrics for the imbalance/multi-label reality: macro/weighted F1, PR-AUC, per-class recall — and always state a majority-class / random baseline.
- Tie the operating threshold to the per-class cost asymmetry the user described.

**Must Not:**
- Report raw accuracy on imbalanced data as the headline metric.
- Apply resampling (e.g., SMOTE/oversampling) or feature selection before the split.
- Quote expected accuracy figures from memory; reason from the user's data and require empirical baselines.

**Instructions:**

1. **Frame the label problem.** Confirm single-label vs multi-label vs multi-class, the label definitions, and the per-class cost of errors. This drives metric and threshold choices.

2. **Choose the representation.** Recommend a representation matched to data size and signal — bag-of-words/TF-IDF (n-grams, char-grams for noisy/morphologically rich text) as a strong baseline, or averaged/classical word embeddings — cross-linking the representation strategy prompt for depth.

3. **Pick the model.** Map representation + data volume to a model (linear SVM / logistic regression for sparse high-dim TF-IDF; gradient-boosted trees or simple MLP for dense embeddings), noting interpretability tradeoffs.

4. **Design leakage-safe preprocessing.** Place tokenization, vectorization, IDF, and any resampling inside a pipeline fit per fold; ensure de-duplication and grouping (same author/thread/template) respect the split.

5. **Handle imbalance.** Choose among class weighting, threshold moving, and resampling-inside-CV; state why, and avoid resampling artifacts (synthetic-text duplication leaking across folds).

6. **Specify the evaluation.** Stratified (or grouped) CV; macro + per-class F1/recall; PR curves for rare classes; report against the majority/random baseline with confidence intervals.

7. **Set the operating point.** Recommend thresholds per class from the cost asymmetry, shown on PR curves, not a single default 0.5.

8. **Define the error analysis loop.** Specify reviewing the confusion matrix and a sample of misclassifications per class to find systematic failures (ambiguous labels, jargon, length effects).

**Output Format:**

A markdown design:
- **Label Problem** — type + definitions + cost asymmetry.
- **Representation & Model** — choice + rationale (with baseline).
- **Leakage-Safe Pipeline** — ordered steps and the fit-on-train boundary.
- **Imbalance Strategy** — method + justification.
- **Evaluation Protocol** — CV scheme, metrics, baselines, intervals.
- **Operating Points** — per-class thresholds + rationale.
- **Error-Analysis Loop** — what to inspect.

## Verification

- [ ] All preprocessing/representation is fit on train folds only, inside the pipeline.
- [ ] Metrics are imbalance-appropriate (macro/per-class F1, PR-AUC) with a stated baseline.
- [ ] Resampling, if used, happens inside CV and does not leak synthetic/near-duplicate text across folds.
- [ ] Grouping (author/thread/template) is respected in the split.
- [ ] Per-class operating thresholds are tied to cost asymmetry.

## False-Positive Prevention

❌ **DON'T:**
- Fit the TF-IDF vocabulary/IDF on the whole corpus before splitting — test vocabulary leaks into training.
- Report 94% accuracy when the positive class is 6% of data; that's near the majority baseline.
- Run SMOTE on the full dataset before CV — synthetic neighbors of test points contaminate training.
- Let multiple near-duplicate messages from one ticket thread span train and test.

✅ **DO:**
- Wrap vectorizer + resampler + model in one pipeline and fit inside each CV fold.
- Lead with macro-F1 / per-class recall and compare to the majority-class baseline.
- Group-split by author/thread/template to stop duplicate leakage.
- Move per-class thresholds to match the cost of missing each label.

## Example Output

```markdown
## Design: Support-Ticket Intent Classifier (12 classes, "billing_fraud" rare + high-cost)

### Label Problem
Single-label, 12 intents. "billing_fraud" = 1.8% of tickets, costliest to miss; "general_question" = 38%.

### Representation & Model
TF-IDF (word 1–2 grams + char 3–5 grams for typos), linear SVM. Baseline: majority class → 0.38 accuracy / 0.05 macro-F1. Char-grams chosen for misspelling robustness.

### Leakage-Safe Pipeline
[clean → TfidfVectorizer → (class_weight) LinearSVC], fit per fold. De-dup identical bodies; group by `ticket_thread_id`.

### Imbalance Strategy
Class weighting (balanced) over resampling — avoids synthetic-text leakage; threshold-move "billing_fraud" via calibrated scores.

### Evaluation Protocol
Grouped 5-fold by thread; report macro-F1, per-class recall, PR-AUC for rare classes, 95% CIs vs baseline.

### Operating Points
"billing_fraud": lower threshold to reach recall ≥ 0.85 (cost of miss high), accept precision ~0.55 with human review. Others at F1-optimal.

### Error-Analysis Loop
Confusion matrix + 30 misclassified "billing_fraud" tickets per fold → most confused with "billing_question"; refine label rulebook.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** label → representation → pipeline → imbalance → eval → operating point.
- **RT-02 (Multi-Dimensional Analysis Framework):** representation/model choices across signal, size, interpretability.
- **DS-02 (Metric Specification):** imbalance-appropriate metrics with baselines and intervals.
- **QA-12 (False Positives Identification):** catches vocabulary/resampling leakage and accuracy-on-imbalance traps.
- **CM-02 (Constraint Specification):** cost asymmetry and the fit-on-train boundary govern the design.

**Related Prompts:**
- `nlp_tokenization_representation_strategy.md` — choose the representation in depth.
- `nlp_text_preprocessing_pipeline.md` — the leakage-safe cleaning that feeds this.
- `nlp_ner_extraction_design.md` — when you need spans, not document labels.
