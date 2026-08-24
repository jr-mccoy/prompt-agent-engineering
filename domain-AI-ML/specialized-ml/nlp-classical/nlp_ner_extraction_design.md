---
title: "NER / Span Extraction Design"
category: AI-ML/specialized-ml/nlp-classical
description: "Design a named-entity / span extraction system — entity schema, annotation and tagging scheme (BIO/BILOU), boundary rules, and span-level evaluation that does not mistake token accuracy for extraction quality."
techniques:
  - ST-02
  - CM-02
  - DS-02
  - QA-12
  - RT-05
difficulty: advanced
tags:
  - nlp
  - named-entity-recognition
  - span-extraction
  - sequence-labeling
  - evaluation
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_text_classification_design.md
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_tokenization_representation_strategy.md
  - domain-AI-ML/specialized-ml/nlp-classical/nlp_text_preprocessing_pipeline.md
---

# NER / Span Extraction Design

**Objective:** Design a named-entity / span-extraction system end to end — a precise entity schema with boundary rules, an annotation plan with a consistent tagging scheme (BIO / BILOU), a sequence-labeling approach, and a span-level evaluation — so the system is measured by whether it extracts correct, correctly-bounded spans, not by token-level accuracy that masks boundary and entity errors.

**When to Use:**
- Extracting structured spans (people, orgs, dates, products, clauses, lab values) from text.
- A NER model shows high token accuracy but extracted entities are wrong or mis-bounded.
- Designing the annotation scheme and evaluation for a new extraction task.

**When NOT to Use:**
- You need a single label per document, not spans (use `nlp_text_classification_design.md`).
- The task is a generative extraction better served by an LLM workflow (cross-link `genai-llm-engineering`).

## Inputs / Context

- **Entity/span types** — the list, what each includes, and nearest-neighbor types that get confused.
- **Boundary expectations** — do titles/modifiers count ("Dr. Jane Smith" vs "Jane Smith"; "March 3" vs "early March")?
- **Overlap/nesting** — can spans nest or overlap (e.g., org inside a longer org)?
- **Text & domain** — genre, language(s), tokenization quirks (hyphenation, punctuation, units).
- **Data volume** — labeled sentences per type; rare types.
- **Downstream use** — is a partial-overlap match acceptable, or is exact-boundary required?

## Constraints

**Must:**
- Define each entity type with a boundary rule and a disambiguation rule against its nearest type, plus worked edge cases.
- Specify the tagging scheme (BIO vs BILOU) and how nested/overlapping spans are represented (or excluded).
- Evaluate at the span level (exact and/or partial-overlap), reporting per-type precision/recall/F1 — never headline token accuracy.

**Must Not:**
- Report token-level accuracy as the success metric (the all-O majority inflates it massively).
- Leave boundary handling implicit; ambiguous boundaries are the dominant NER error source.
- Invent type frequencies or expected F1 — request data and require empirical measurement.

**Instructions:**

1. **Lock the entity schema.** For each type: definition, what to include/exclude at boundaries (titles, modifiers, units), and the rule against the nearest confusable type. Decide nesting/overlap policy.

2. **Choose the tagging scheme.** Select BIO or BILOU, justify it, and define how multi-token, adjacent same-type, and (if allowed) nested spans are encoded.

3. **Plan annotation & agreement.** Specify boundary-strict guidelines, a span-level inter-annotator agreement metric, and an adjudication loop — boundary disagreements must be resolved by rule, not vote.

4. **Pick representation & model.** Recommend features/representation (token + char + shape/orthographic features for classical CRF/structured models; or classical embedding features) cross-linking the representation prompt; CRF-style structured prediction is a strong non-LLM baseline.

5. **Design leakage-safe splitting.** Split by document/source so sentences from one document don't straddle folds; respect templated/boilerplate text that repeats.

6. **Specify span-level evaluation.** Define exact-match and partial/overlap (e.g., type-match with boundary tolerance) span P/R/F1, per type; state which counts as "correct" for the downstream use.

7. **Build the error taxonomy.** Categorize errors: boundary (right type, wrong span edges), type confusion, missed span, spurious span — each drives a different fix.

8. **Set the acceptance bar.** Tie the required span-F1 and the exact-vs-partial choice to the downstream consumer's tolerance.

**Output Format:**

A markdown design:
- **Entity Schema** — table: Type | Definition | Boundary Rule | vs Nearest Type | Edge Case
- **Tagging Scheme** — BIO/BILOU + nesting policy.
- **Annotation & Agreement** — guidelines + span-level agreement metric + adjudication.
- **Representation & Model** — choice + rationale.
- **Leakage-Safe Split** — grouping rule.
- **Span-Level Evaluation** — exact/partial definition + per-type P/R/F1.
- **Error Taxonomy** — categories + remedies.
- **Acceptance Bar** — required F1 + exact-vs-partial.

## Verification

- [ ] Every entity type has explicit boundary and disambiguation rules.
- [ ] The tagging scheme and nesting/overlap policy are specified.
- [ ] Evaluation is span-level (per-type P/R/F1), not token accuracy.
- [ ] Splits group by document/source to prevent sentence leakage.
- [ ] Errors are categorized (boundary / type / miss / spurious) for actionable fixes.

## False-Positive Prevention

❌ **DON'T:**
- Report token-level accuracy — with mostly "O" tokens, 95% can mean nearly nothing extracted.
- Count a span as correct when the type matches but the boundary is off, if downstream needs exact spans.
- Leave "does the title count?" undecided — boundary inconsistency wrecks both labels and metrics.
- Split sentences from one document across train/test when documents share entities and templates.

✅ **DO:**
- Evaluate exact and partial span match per type and report which the downstream use requires.
- Write boundary rules (include/exclude titles, units, modifiers) and measure boundary errors separately.
- Group-split by document/source ID.
- Separate boundary errors from type-confusion and missed/spurious spans to target fixes.

## Example Output

```markdown
## NER Design: Clinical Med-Extraction (DRUG, DOSE, FREQUENCY, ROUTE)

### Entity Schema
| Type | Definition | Boundary Rule | vs Nearest | Edge Case |
|---|---|---|---|---|
| DRUG | Active ingredient/brand | exclude form ("tablet") | vs ROUTE: not "oral" | "metformin XR" → include "XR" |
| DOSE | Amount + unit | include unit ("500 mg") | vs FREQUENCY | "500mg" no space → one span |
| FREQUENCY | Schedule | include "BID","q8h" | vs DOSE | "twice daily" → 2 tokens |
| ROUTE | Admin route | "PO","IV" | vs DRUG | "by mouth" → multi-token |

### Tagging Scheme
BILOU (better boundary signal for short multi-token spans). No nesting allowed; overlaps disallowed by rule.

### Annotation & Agreement
Boundary-strict guidelines; span-level F1 agreement target ≥ 0.85; adjudicator resolves boundary disputes → rulebook update.

### Representation & Model
Token + char-prefix/suffix + orthographic shape + gazetteer features → CRF baseline (interpretable, strong on structured clinical text).

### Leakage-Safe Split
Group by `note_id` (one note repeats the same drug list across sections).

### Span-Level Evaluation
Exact-match span P/R/F1 per type (downstream e-prescribing needs exact DOSE). Also report partial for DRUG.

### Error Taxonomy
Boundary (DOSE missing unit) | Type (ROUTE↔DRUG) | Miss (rare drugs) | Spurious (negated meds "no aspirin"). Negation handling flagged as top fix.

### Acceptance Bar
DOSE/FREQUENCY exact-F1 ≥ 0.90 (safety); DRUG partial-F1 ≥ 0.85.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** schema → scheme → annotation → model → split → eval → errors.
- **CM-02 (Constraint Specification):** boundary rules and exact-vs-partial requirement govern design and metric.
- **DS-02 (Metric Specification):** span-level P/R/F1 instead of token accuracy.
- **QA-12 (False Positives Identification):** prevents token-accuracy inflation and boundary-blind metrics.
- **RT-05 (Evidence-Based Reasoning):** error taxonomy ties each fix to a measured error category.

**Related Prompts:**
- `nlp_text_classification_design.md` — when a document label, not spans, is the goal.
- `nlp_tokenization_representation_strategy.md` — feature/representation choices for the tagger.
- `nlp_text_preprocessing_pipeline.md` — normalization that must not destroy span boundaries.
