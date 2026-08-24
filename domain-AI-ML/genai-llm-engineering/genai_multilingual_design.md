---
title: "Multilingual LLM/NLP System Design"
category: AI-ML/genai-llm-engineering
description: "Design a multilingual LLM system — tokenizer/script coverage, cross-lingual transfer, unified vs language-specific models, and per-language evaluation — so quality holds across the full language set instead of collapsing on low-resource languages."
techniques:
  - ST-02
  - RT-02
  - DS-01
  - CM-02
  - QA-12
difficulty: advanced
tags:
  - multilingual
  - cross-lingual
  - tokenizer
  - low-resource
  - per-language-evaluation
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/genai-llm-engineering/genai_embedding_model_selection.md
  - domain-AI-ML/genai-llm-engineering/genai_llm_evaluation_design.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
---

# Multilingual LLM/NLP System Design

**Objective:** Produce a defensible design for a system that must serve multiple languages, deciding tokenizer/script coverage, whether to route to a unified model or language-specific models, how much to lean on cross-lingual transfer, and — most importantly — how to evaluate per-language so that a strong aggregate score never disguises catastrophic failure on a low-resource language. The output makes the language set, the coverage gaps, and the degradation strategy explicit rather than assuming an English-centric model "just works" elsewhere.

**When to Use:**
- You are building a product that must handle two or more languages, especially a mix of high- and low-resource ones.
- You suspect token inflation, script coverage, or transliteration is silently hurting non-English quality or cost.
- You need to choose between one unified multilingual model and a set of per-language models or adapters.

**When NOT to Use:**
- The system is genuinely single-language — skip this and tune that one language directly.
- The core question is which embedding model to use for retrieval — use `genai_embedding_model_selection.md`.
- You only need to design the evaluation harness, not the system — use `genai_llm_evaluation_design.md`.

## Inputs / Context

Provide what you can:
- **Language set** — every language and script the system must support, with rough traffic share per language.
- **Resource tier per language** — which languages are high-resource vs low-resource for your domain (not just on the web).
- **Task type** — generation, classification, extraction, retrieval, or conversation; tolerance for errors differs by task.
- **Latency / cost budget** — per-request ceilings, since token inflation makes some languages far more expensive.
- **Candidate models** — any unified multilingual models, regional models, or adapters under consideration.
- **Quality floor** — the minimum acceptable per-language quality below which you will degrade gracefully or route to a human.
- **Data availability** — labeled eval/fine-tune data you actually hold per language, and gaps.

## Constraints

**Must:**
- Enumerate the full language set and resource tier before recommending any model.
- Report and decide on quality **per language**, never as a single cross-language average.
- Define an explicit graceful-degradation path for languages below the quality floor (fallback model, human handoff, or honest "unsupported").
- Account for tokenizer/script coverage and token-inflation effects on both cost and context budget.

**Must Not:**
- Invent benchmark/MTEB/eval numbers from memory or assume English benchmark results transfer to other languages — measure on your data per language and mark unknowns.
- Assert version-specific model/API language coverage or context behavior from memory — verify against current docs.
- Recommend a single model as "best multilingual" without per-language evidence on the user's corpus.
- Treat machine-translated eval data as ground truth without native review.

**Instructions:**

1. **Pin the language set and resource tiers.** List every language, its script, traffic share, and whether it is high- or low-resource *for this domain*. A language can be high-resource generally but low-resource for your jargon.
2. **Audit tokenizer and script coverage.** For each candidate model, check whether scripts are represented and estimate token inflation (e.g., a sentence costing 2-3x more tokens in some scripts). Inflation hits cost, latency, and effective context length.
3. **Decide unified vs language-specific.** Weigh one multilingual model (simpler ops, cross-lingual transfer) against per-language models/adapters (better tails, more ops). Document the tradeoff; do not default to unified for convenience.
4. **Plan cross-lingual transfer deliberately.** Identify which low-resource languages can ride on transfer from related high-resource languages, and where transfer is unlikely (distant scripts/morphology). Mark transfer as a hypothesis to test, not a guarantee.
5. **Design per-language evaluation.** For each language, define a held-out eval set with native-quality references and per-language metrics. Set a quality floor and flag every language that you cannot yet evaluate.
6. **Define graceful degradation.** For languages below the floor or without eval data, specify the fallback: alternate model, translation bridge, human handoff, or an explicit "not supported" message — never silent low-quality output.
7. **Estimate cost/latency per language.** Combine token inflation with traffic share to produce a per-language cost and latency picture; surface any language that is disproportionately expensive.
8. **Recommend and stage rollout.** Propose the design, then a rollout order (highest-confidence languages first) with eval gates before adding tail languages.

**Output Format:**

A markdown design brief:
- **Language Set & Tiers** — table of language, script, traffic share, resource tier.
- **Tokenizer/Script Coverage** — per-model coverage and token-inflation estimates.
- **Architecture Decision** — unified vs language-specific, with the rationale and tradeoffs.
- **Cross-Lingual Transfer Plan** — which languages lean on transfer and the risk per case.
- **Per-Language Evaluation Plan** — eval set source, metrics, quality floor, and known gaps.
- **Graceful Degradation** — fallback path for each below-floor or unevaluated language.
- **Cost & Latency by Language** — per-language estimates flagged against budget.
- **Rollout Sequence** — staged order with eval gates.

## Verification

- [ ] Every supported language is listed with script, traffic share, and resource tier.
- [ ] Quality is reported per language, with an explicit floor; no decision rests on a cross-language average.
- [ ] A concrete degradation path exists for each below-floor or unevaluated language.
- [ ] Tokenizer/script coverage and token inflation are accounted for in cost and context budgets.
- [ ] The rollout has eval gates before tail languages are enabled.
- [ ] No benchmark/eval numbers are stated from memory; unknowns are marked and English results are not assumed to transfer.

## False-Positive Prevention

❌ **DON'T:**
- Report one aggregate accuracy/F1/BLEU across all languages — a 0.88 average can hide a 0.31 on a low-resource language.
- Assume an English eval (or English benchmark leaderboard) predicts non-English quality.
- Treat "the model supports 100+ languages" marketing as evidence it works on *your* tasks in those languages.
- Use back-translated or MT-generated references as ground truth without native verification.

✅ **DO:**
- Break out every metric by language and inspect the worst performers, not the mean.
- Build native-reviewed eval sets per language, even small ones, before claiming support.
- Quantify token inflation per script and fold it into cost, latency, and context-length planning.
- Ship an explicit degradation path so a weak language fails safely instead of producing confident garbage.

## Example Output

```markdown
## Language Set & Tiers
| Language | Script | Traffic | Tier (for our domain) |
|----------|--------|---------|-----------------------|
| English  | Latin  | 55%     | High                  |
| Spanish  | Latin  | 25%     | High                  |
| Hindi    | Deva.  | 12%     | Medium                |
| Swahili  | Latin  | 5%      | Low                   |
| Amharic  | Ge'ez  | 3%      | Low (poor coverage)   |

### Architecture Decision
Unified multilingual model for EN/ES/HI (strong transfer, simpler ops).
Amharic routed separately: token inflation ~3.1x and weak script coverage
make it both expensive and unreliable on the unified model.

### Per-Language Evaluation Plan
Per-language held-out sets (native-reviewed): EN/ES/HI = 300 items each;
SW = 120; AM = 0 (NO EVAL DATA — marked UNVERIFIED). Floor = 0.80 task acc.
Measured (our corpus): EN 0.91, ES 0.89, HI 0.83, SW 0.71 (below floor).

### Graceful Degradation
- SW (0.71 < 0.80): human handoff for high-stakes outputs until improved.
- AM (no eval): labeled "limited support"; no autonomous actions taken.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** Drives the design through pin-set → coverage → architecture → transfer → eval → degradation in fixed order.
- **RT-02 (Multi-Dimensional Analysis Framework):** Frames the model as a multilingual ML architect accountable for the worst language, not the average.
- **DS-01 (Framework Application):** Splits the system into per-language slices so tail languages are reasoned about individually.
- **CM-02 (Constraint Specification):** Forces per-language reporting and a quality floor, blocking aggregate-only conclusions.
- **QA-12 (False Positives Identification):** Surfaces languages with missing eval data or coverage gaps rather than silently assuming support.

**Related Prompts:**
- `genai_embedding_model_selection.md` — choosing embedding models, including multilingual retrieval considerations.
- `genai_llm_evaluation_design.md` — building the per-language evaluation harness this design depends on.
- `genai_rag_system_design.md` — retrieval design when the multilingual system is RAG-based.
