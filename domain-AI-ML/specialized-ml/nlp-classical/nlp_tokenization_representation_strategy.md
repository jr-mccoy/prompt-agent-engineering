---
title: "Tokenization & Text Representation Strategy"
category: AI-ML/specialized-ml/nlp-classical
description: "Choose a tokenization scheme and text representation — bag-of-words, TF-IDF, word, or subword embeddings — matched to the task, language, vocabulary behavior, and out-of-vocabulary risk, with a leakage-safe fitting boundary."
techniques:
  - RT-02
  - CM-02
  - DS-02
  - RT-05
  - QA-12
difficulty: intermediate
tags:
  - nlp
  - tokenization
  - representation
  - tf-idf
  - embeddings
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_text_classification_design.md
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_text_preprocessing_pipeline.md
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_ner_extraction_design.md
---

# Tokenization & Text Representation Strategy

**Objective:** Recommend a tokenization scheme and a text-representation method — bag-of-words/TF-IDF, word embeddings, or subword embeddings — for a non-LLM NLP task, justified by the task type, language morphology, vocabulary size and drift, out-of-vocabulary (OOV) risk, and interpretability needs, with the vocabulary/representation fitted on training data only so it cannot leak.

**When to Use:**
- Setting up the front end of a classical NLP pipeline (classification, NER, retrieval, clustering).
- A model struggles with OOV terms, morphologically rich text, noisy tokens, or multilingual input.
- Deciding between sparse count-based and dense embedding representations.

**When NOT to Use:**
- The task is committed to an LLM pipeline whose tokenizer is fixed by the model (cross-link `genai-llm-engineering`).
- You only need cleaning/normalization decisions (use `nlp_text_preprocessing_pipeline.md`).

## Inputs / Context

- **Task type** — classification / NER / clustering / retrieval (sequence vs document representation needs differ).
- **Language(s) & morphology** — agglutinative/inflected vs analytic; code-switching; scripts.
- **Text noise** — typos, hashtags, URLs, code, units, domain jargon.
- **Vocabulary behavior** — size, growth/drift over time, proportion of rare terms, expected OOV at serving.
- **Data volume** — corpus size (small favors count-based; large enables learned embeddings).
- **Constraints** — interpretability, latency, memory, multilingual coverage.

## Constraints

**Must:**
- Match tokenization to language and noise (word vs subword vs char n-grams), and justify the OOV handling.
- Fit vocabulary, IDF, and any learned embeddings on training data only; transform validation/test/serving with the frozen artifact.
- Tie the sparse-vs-dense choice to data volume, interpretability needs, and OOV/morphology pressure.

**Must Not:**
- Recommend pretrained word vectors for a domain with heavy OOV/jargon without an OOV strategy (subword, char n-grams, or in-domain training).
- Build the vocabulary on the full corpus before splitting.
- Quote embedding-quality benchmarks from memory — reason from the user's vocabulary behavior and require empirical comparison.

**Instructions:**

1. **Profile the vocabulary.** Estimate vocabulary size, rare-term fraction, OOV pressure at serving, and morphological complexity — these drive everything.

2. **Choose tokenization.** Recommend word-level, subword (BPE/WordPiece/Unigram-style), or character n-grams; justify by morphology, noise, and OOV. Note handling of casing, numbers, URLs, hashtags, emoji.

3. **Choose representation family.** Decide sparse count-based (BoW / TF-IDF, with n-gram and char-gram options) vs dense (averaged/trained word embeddings, or subword-pooled vectors), tied to data volume, interpretability, and signal.

4. **Set the OOV strategy.** Specify how unseen terms are handled at serving (subword fallback, char n-grams, UNK, hashing) and why it fits the OOV pressure.

5. **Fix the fitting boundary.** State exactly which artifacts (vocabulary, IDF, embedding tables) are fit on train only and frozen for transform — the leakage-critical step.

6. **Address dimensionality & weighting.** For sparse reps, set min/max document frequency, n-gram ranges, sublinear TF / IDF; for dense, set dimension and pooling. Note memory/latency.

7. **Define the comparison.** Specify a small bake-off (e.g., TF-IDF vs embedding rep) on the same folds with the task metric and intervals, since the right representation is empirical, not assumed.

**Output Format:**

A markdown strategy:
- **Vocabulary Profile** — size, rare fraction, OOV pressure, morphology.
- **Tokenization Choice** — scheme + casing/number/URL handling + rationale.
- **Representation Choice** — sparse vs dense + parameters + rationale.
- **OOV Strategy** — serving-time handling.
- **Fitting Boundary** — train-only artifacts, frozen for transform.
- **Comparison Plan** — bake-off + metric + intervals.

## Verification

- [ ] Tokenization is justified by language morphology and text noise.
- [ ] Vocabulary/IDF/embeddings are fit on train only and frozen for transform/serving.
- [ ] An explicit OOV strategy matches the serving OOV pressure.
- [ ] Sparse-vs-dense is tied to data volume and interpretability, with a planned empirical comparison.
- [ ] No embedding/benchmark numbers are asserted from memory.

## False-Positive Prevention

❌ **DON'T:**
- Use word-level tokenization for agglutinative/morphologically rich languages — vocabulary explodes and OOV soars; subword fits better.
- Build the TF-IDF vocabulary/IDF on the full corpus before splitting (test vocabulary leaks in).
- Apply pretrained general-domain word vectors to jargon-heavy text (clinical, legal, code) without an OOV fallback — most key terms map to UNK.
- Assume dense embeddings beat TF-IDF; on small or interpretability-bound tasks TF-IDF + linear often wins.

✅ **DO:**
- Profile OOV and morphology first, then pick subword/char-grams when OOV pressure is high.
- Fit and freeze the representation on training data; transform everything else with it.
- Choose an OOV strategy explicitly and match it to expected unseen-term rate at serving.
- Bake off sparse vs dense on the same folds with intervals before committing.

## Example Output

```markdown
## Representation Strategy: Multilingual Product-Review Sentiment (EN/DE/FI, noisy)

### Vocabulary Profile
~180k word types over 3 languages; Finnish agglutination inflates types; ~12% serving OOV (slang, brand names); heavy emoji/typos.

### Tokenization Choice
Subword (BPE) shared across languages + char 3–5 grams for typo/emoji robustness. Lowercase; map URLs→<url>, numbers→<num>; keep emoji as tokens (sentiment signal).

### Representation Choice
Two candidates: (a) TF-IDF over char-grams + word subwords (sparse, interpretable); (b) averaged subword embeddings (dense). Start with (a) given moderate data and need to explain flags.

### OOV Strategy
Char n-grams + subword fallback absorb unseen words (no hard UNK), matching the 12% OOV pressure.

### Fitting Boundary
TfidfVectorizer / subword vocab / IDF fit on train folds only; frozen and applied to val/test/serving.

### Comparison Plan
5-fold (grouped by reviewer) bake-off: TF-IDF+LinearSVC vs subword-embedding+GBM, macro-F1 with 95% CIs per language.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** tokenization/representation weighed across morphology, OOV, data size, interpretability.
- **CM-02 (Constraint Specification):** the fit-on-train boundary and OOV pressure are governing constraints.
- **DS-02 (Metric Specification):** the empirical bake-off fixes metric and intervals.
- **RT-05 (Evidence-Based Reasoning):** representation choice validated, not assumed from benchmarks.
- **QA-12 (False Positives Identification):** guards vocabulary leakage and OOV-blind embedding choices.

**Related Prompts:**
- `nlp_text_classification_design.md` — consumes this representation for document labels.
- `nlp_text_preprocessing_pipeline.md` — normalization decisions that precede tokenization.
- `nlp_ner_extraction_design.md` — span tasks need token/char features chosen here.
