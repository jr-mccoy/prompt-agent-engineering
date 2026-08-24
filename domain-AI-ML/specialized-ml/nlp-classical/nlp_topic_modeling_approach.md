---
title: "Topic Modeling & Unsupervised Text Structure Approach"
category: AI-ML/specialized-ml/nlp-classical
description: "Approach unsupervised text structure discovery — LDA vs embeddings+clustering — and validate it with coherence, stability, and human interpretability rather than trusting auto-discovered topics at face value."
techniques:
  - RT-02
  - ST-02
  - QA-12
  - DS-02
  - RT-05
difficulty: advanced
tags:
  - nlp
  - topic-modeling
  - lda
  - clustering
  - unsupervised
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_tokenization_representation_strategy.md
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_text_preprocessing_pipeline.md
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_text_classification_design.md
---

# Topic Modeling & Unsupervised Text Structure Approach

**Objective:** Design an approach to discovering latent structure in an unlabeled text corpus — choosing between probabilistic topic models (LDA-family) and embeddings-plus-clustering — and, crucially, a validation plan (coherence, stability across runs, human interpretability, downstream usefulness) that prevents accepting arbitrary or unstable "topics" as real findings.

**When to Use:**
- Exploring a large unlabeled corpus to find themes, clusters, or structure.
- Producing topic features or a taxonomy to seed downstream labeling/classification.
- An existing topic model produces topics stakeholders find incoherent or unstable.

**When NOT to Use:**
- You already have labels and want supervised classification (use `nlp_text_classification_design.md`).
- The need is generative summarization/labeling better served by an LLM (cross-link `genai-llm-engineering`).

## Inputs / Context

- **Goal of the analysis** — exploration, feature generation, taxonomy seeding, monitoring; who consumes the topics and how.
- **Corpus** — size, document length (tweets vs articles), language(s), domain, time span.
- **Granularity** — roughly how many themes are expected; whether topics should be stable over time.
- **Preprocessing done** — normalization, stopwords, n-grams (affects topic quality heavily).
- **Validation appetite** — availability of human raters for interpretability checks.
- **Constraints** — reproducibility needs, compute.

## Constraints

**Must:**
- Choose the method (LDA-family vs embeddings+clustering) by document length, corpus size, and interpretability/feature needs, and justify it.
- Validate topics on at least: coherence (e.g., C_v / NPMI), stability across random seeds/subsamples, and human interpretability — not just a single coherence score.
- Treat the topic count / cluster count as a tuned hyperparameter with a selection procedure, not a guess.

**Must Not:**
- Present auto-discovered topics as ground-truth themes without stability and human checks.
- Pick the number of topics arbitrarily or by eyeballing one run.
- Invent coherence numbers or claim a "best" topic count from memory — derive them from the user's corpus.

**Instructions:**

1. **Clarify the consumer.** State what the topics are for (exploration vs features vs taxonomy vs monitoring); this sets the validation bar — features tolerate noisier topics than a published taxonomy.

2. **Choose the method.** For short texts (tweets, queries) and modern setups, embeddings+clustering (e.g., density or centroid clustering on document embeddings) often beats LDA; for longer documents and probabilistic interpretability, LDA-family fits. Justify by length and goal.

3. **Set representation & preprocessing.** Align stopwords, n-grams, and (for LDA) term weighting; note that aggressive/insufficient cleaning is a leading cause of junk topics. Cross-link the representation/preprocessing prompts.

4. **Select the topic/cluster count.** Define a procedure — coherence/perplexity curves for LDA, or silhouette/density criteria + stability for clustering — sweeping a range rather than fixing one value.

5. **Validate coherence and stability.** Compute coherence (NPMI/C_v), and re-run across seeds/subsamples to measure topic stability (e.g., topic overlap / matching); unstable topics are artifacts.

6. **Run human interpretability.** Have raters label top-terms + representative docs per topic as interpretable/junk; report the interpretable fraction.

7. **Check downstream usefulness.** If topics are features or a taxonomy seed, verify they improve a downstream task or align with known categories — coherence alone is not utility.

8. **Document reproducibility.** Fix seeds, record preprocessing and hyperparameters, and report what makes a run reproducible.

**Output Format:**

A markdown approach:
- **Consumer & Validation Bar** — purpose + required rigor.
- **Method Choice** — LDA vs embeddings+clustering + rationale.
- **Representation & Preprocessing** — settings + rationale.
- **Topic-Count Selection** — sweep + criterion.
- **Validation Plan** — coherence + stability + human interpretability + downstream utility.
- **Reproducibility Notes** — seeds, params, preprocessing record.

## Verification

- [ ] Method is chosen by document length, corpus size, and consumer need.
- [ ] Topic/cluster count is selected by a procedure over a swept range, not guessed.
- [ ] Validation includes coherence AND stability AND human interpretability.
- [ ] Downstream usefulness is checked when topics are features/taxonomy.
- [ ] Reproducibility (seeds, params, preprocessing) is documented.

## False-Positive Prevention

❌ **DON'T:**
- Read top words of one run and declare them "the corpus themes" — re-running with a new seed often yields different topics.
- Trust a high coherence score as proof of useful topics; coherent ≠ interpretable ≠ useful.
- Run LDA on short, sparse texts (tweets, search queries) and expect clean topics — sparsity breaks it.
- Pick k by intuition; the wrong granularity merges or shatters real themes.

✅ **DO:**
- Measure topic stability across seeds/subsamples and discard unstable topics as artifacts.
- Pair coherence with human interpretability rating of top terms + exemplar docs.
- Use embeddings+clustering for short texts and justify k/cluster count via a sweep.
- For feature/taxonomy uses, confirm topics improve a downstream metric or match known labels.

## Example Output

```markdown
## Approach: Theme Discovery in 90k Support Chats (short, multi-turn)

### Consumer & Validation Bar
Output seeds a support-intent taxonomy → high bar: must be stable and human-interpretable, not just coherent.

### Method Choice
Embeddings + density clustering over LDA: chats are short and conversational; LDA topics were incoherent in a pilot. Embed per-chat, reduce, cluster.

### Representation & Preprocessing
Subword sentence embeddings; light cleaning (mask PII, URLs→<url>); no aggressive stopword removal (hurts short-text semantics).

### Topic-Count Selection
Sweep clustering density/min-size; choose by silhouette + a stability criterion; expect ~25–40 clusters.

### Validation Plan
- Coherence: NPMI on cluster keyword sets.
- Stability: re-cluster 5 subsamples; keep clusters with ≥0.7 Jaccard match. ~8 unstable clusters dropped.
- Human: 2 raters label top-terms + 5 exemplar chats/cluster; report interpretable fraction (target ≥ 80%).
- Downstream: clusters seed a 30-intent taxonomy; check coverage vs a hand-labeled 500-chat sample.

### Reproducibility Notes
Fixed seeds; embedding model + version, reducer/cluster params, preprocessing script all recorded.
```

**Techniques Used:**
- **RT-02 (Multi-Dimensional Analysis Framework):** method choice across length, size, interpretability, utility.
- **ST-02 (Structured Sequential Instructions):** consumer → method → representation → k → validation → reproducibility.
- **QA-12 (False Positives Identification):** central to rejecting unstable/incoherent topics as artifacts.
- **DS-02 (Metric Specification):** coherence/stability/silhouette metrics defined explicitly.
- **RT-05 (Evidence-Based Reasoning):** topics accepted only on measured stability + human + downstream evidence.

**Related Prompts:**
- `nlp_tokenization_representation_strategy.md` — representation choice strongly affects topic quality.
- `nlp_text_preprocessing_pipeline.md` — cleaning drives whether topics are coherent.
- `nlp_text_classification_design.md` — once topics seed a taxonomy, move to supervised classification.
