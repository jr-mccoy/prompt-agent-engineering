---
title: "Interview Bank: Search & Retrieval Systems"
category: AI-ML/learning-ai-ml/interview-bank
description: "A bank of search and retrieval ML-system-design interview questions, each paired with a junior→staff leveled rubric covering query understanding, retrieval vs ranking, relevance evaluation, latency budgets, and lexical/embedding hybrids."
techniques:
  - DS-01
  - ST-02
  - DS-06
  - RP-01
  - QA-12
difficulty: advanced
tags:
  - interview-prep
  - search
  - retrieval
  - system-design
  - rubric
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_ml_system_design_interview.md
  - domain-AI-ML/learning-ai-ml/interview-bank/mllearn_interview_scoring_rubric.md
  - domain-AI-ML/genai-llm-engineering/genai_rag_system_design.md
---

# Interview Bank: Search & Retrieval Systems

**Objective:** Produce a usable bank of search/retrieval ML-system-design interview questions, each with a leveled rubric (junior / mid / senior / staff) — so a learner can self-quiz, an interviewer can grade consistently, and the discriminators that separate seniority (relevance evaluation, latency budgets at scale, retrieval-vs-ranking separation, lexical/embedding hybrids) are explicit rather than implied.

**When to Use:**
- A learner is preparing for search/retrieval system-design rounds and wants questions + bars.
- An interviewer needs a consistent, level-calibrated rubric for these rounds.
- Self-assessing depth on query understanding → retrieval → ranking → relevance eval.

**When NOT to Use:**
- The learner wants an interactive mock (use `mllearn_ml_system_design_interview.md`).
- The round is concept/coding/stats quizzing (use `mllearn_ml_interview_prep.md`).
- They need the generic cross-topic rubric only (use `mllearn_interview_scoring_rubric.md`).

## Inputs / Context

- **Target level(s)** — which bars matter most.
- **Sub-focus** — web search, e-commerce search, enterprise/document retrieval, semantic search.
- **Use mode** — self-quiz, interviewer grading, or curriculum gap-finding.
- **Number of questions** — how many to generate.

## Constraints

**Must:**
- Pair every question with a leveled rubric escalating from "names retrieval + ranking" (junior) to "owns relevance evaluation, scale, and the hybrid-retrieval tradeoffs" (staff).
- Bake the search-specific discriminators into senior/staff bars: relevance evaluation methodology (offline judgments + online signals), latency/throughput at scale, retrieval vs ranking separation, and lexical (e.g., inverted index) vs embedding (vector) hybrids.
- Make "establishes what 'relevant' means and how it's measured before modeling" a pass condition at every level.

**Must Not:**
- Present these as real, specific company interview questions or attach fabricated scores/hiring facts.
- Reward "use embeddings + a vector DB" without a relevance-eval plan or latency budget.
- Treat retrieval and ranking as one undifferentiated step.

**Instructions:**

1. **Confirm scope.** Establish target level(s), sub-focus, use mode, and question count.

2. **Generate questions across the search design surface.** Cover query understanding, candidate retrieval, ranking, relevance evaluation, latency/scale, and hybrid lexical/semantic retrieval — as open design prompts.

3. **For each question, write the leveled rubric.** Four bars; each states what the answer demonstrates, with higher bars adding evaluation rigor and scale reality.

4. **Embed the discriminators.** Senior/staff bars require a relevance-eval methodology, latency budget at scale, retrieval/ranking separation, and a stated lexical-vs-embedding tradeoff.

5. **Add a "relevance & metrics gate".** For each question, note what "relevant" means here and how it's measured (offline judgments, click/engagement signals, their biases) before modeling.

6. **Note common failure signals.** List the seductive-but-failing answers (e.g., "just use a vector DB," no relevance eval, ignoring latency).

7. **Point to deeper study.** Link the retrieval/RAG prompts for concepts to shore up.

**Output Format:**

A markdown question bank:
- **Scope** — levels, focus, mode.
- **Questions** — for each: the design prompt, a Relevance & Metrics Gate, a 4-bar leveled rubric, and Common Failure Signals.
- **Study Pointers** — where to deepen weak areas.

## Verification

- [ ] Every question has a 4-bar (junior→staff) rubric with escalating expectations.
- [ ] Senior/staff bars require relevance-eval methodology, latency at scale, and hybrid tradeoffs.
- [ ] Each question has a relevance-and-metrics gate as a pass condition.
- [ ] Questions are framed as practice, not fabricated real company questions.
- [ ] Common failure signals are listed.

## False-Positive Prevention

❌ **DON'T:**
- Claim these are actual questions from named companies, or invent scores.
- Pass "embeddings + vector DB" with no relevance-eval plan or latency budget.
- Collapse retrieval and ranking into one step in the rubric.
- Ignore that click signals are biased relevance proxies.

✅ **DO:**
- Frame questions as practice and rubrics as demonstrated-reasoning bars.
- Require a relevance definition + measurement before modeling, at every level.
- Put relevance evaluation, latency/scale, and hybrid retrieval in senior/staff bars.
- List the fluent-but-failing answers explicitly.

## Example Output

```markdown
## Interview Bank — Search & Retrieval (levels: mid + senior; mode: interviewer grading)

### Q1: Design search for an e-commerce catalog.
**Relevance & Metrics Gate:** what counts as a relevant result (purchase intent? exact match?),
how relevance is judged offline (human labels) and online (CTR/conversion, and their biases),
latency budget, catalog scale.

**Rubric**
- *Junior:* names retrieval + ranking; basic features; some notion of relevance.
- *Mid:* separates retrieval from ranking; defines an offline relevance metric and an online metric;
  handles synonyms/typos in query understanding.
- *Senior:* designs a relevance-eval methodology (labeled judgments + debiased online signals),
  states a latency budget and how retrieval meets it at scale, weighs lexical vs embedding retrieval.
- *Staff:* designs a hybrid lexical+semantic system with a principled fusion, plans for query
  distribution shift, and builds an evaluation pipeline that detects relevance regressions pre-launch.

**Common Failure Signals:** "just use a vector DB"; no relevance-eval plan; ignores latency; treats
raw CTR as ground-truth relevance.

### Q2: Build semantic retrieval over an enterprise document corpus. …

### Study Pointers
Weak on semantic retrieval → `genai_rag_system_design.md`.
```

**Techniques Used:**
- **DS-01 (Framework Application):** the search design surface (query → retrieve → rank → eval) structures the bank.
- **ST-02 (Structured Sequential Instructions):** scope → questions → rubrics → gates → failure signals.
- **DS-06 (Prioritization & Severity Guidance):** leveled bars order discriminators by seniority.
- **RP-01 (Audience/Level Adaptation):** four bars calibrated junior→staff.
- **QA-12 (Rubric-Based Evaluation):** explicit, level-calibrated grading bars per question.

**Related Prompts:**
- `mllearn_ml_system_design_interview.md` — the interactive mock to practice these live.
- `interview-bank/mllearn_interview_scoring_rubric.md` — the universal dimension-by-dimension rubric.
- `genai_rag_system_design.md` — deepen retrieval/semantic-search concepts the senior bar requires.
