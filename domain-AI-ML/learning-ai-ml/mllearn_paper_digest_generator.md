---
title: "ML Paper Digest Generator"
category: AI-ML/learning-ai-ml
description: "Produce a structured digest of a paper the user provides — problem, method, results, limitations, and relevance — grounded strictly in the paper's content with no fabricated numbers."
techniques:
  - ST-03
  - ST-02
  - RT-05
  - QA-01
  - DS-02
difficulty: intermediate
tags:
  - paper-digest
  - summarization
  - research
  - limitations
  - grounded
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/learning-ai-ml/mllearn_paper_reading_guide.md
  - domain-AI-ML/learning-ai-ml/mllearn_reproduce_a_paper_plan.md
  - domain-AI-ML/learning-ai-ml/mllearn_glossary_builder.md
---

# ML Paper Digest Generator

**Objective:** Produce a faithful, structured digest of a paper the user supplies — capturing the problem, method, key results with their baselines, limitations, and relevance — grounded strictly in the paper's actual content, so the reader gets an accurate map of the work without the digest inventing or inflating anything.

**When to Use:**
- The user provides a paper (or its text) and wants a structured, reliable summary.
- Building a literature-review entry or a reading-list note.
- Triaging whether a paper is worth a deep read.

**When NOT to Use:**
- The goal is to learn the skill of reading papers (use `mllearn_paper_reading_guide.md`).
- You don't have the paper's content — do not digest from memory of the title.

## Inputs / Context

- **The paper** — full text, sections, or at minimum abstract + results (the more provided, the more reliable the digest).
- **Reader's purpose** — quick triage, lit-review note, find a baseline, decide whether to reproduce.
- **Reader's background** — to calibrate how much to define.

## Constraints

**Must:**
- Ground every claim, number, and result in the provided text; quote or cite the section for key results.
- Report results with their baselines and the metric used — never a naked "improved by X%."
- Capture limitations the authors state AND obvious ones they omit, clearly distinguishing the two.

**Must Not:**
- Fabricate or recall numbers/results not present in the provided text; if a detail isn't given, mark it "not reported."
- Inflate the contribution beyond what the paper claims, or launder the authors' framing as established fact.
- Digest a paper you weren't given — refuse and request the content rather than reconstructing from memory.

**Instructions:**

1. **Confirm you have the content.** If only a title/abstract is provided, state the digest's reliability is limited to that and ask for more, or scope the digest explicitly to what's available.

2. **Capture the problem and contribution.** State the problem the paper addresses and what it claims is new — in the paper's own terms, attributed as a claim.

3. **Summarize the method.** Describe the core approach in a few sentences a knowledgeable reader could follow; name the key components without copying the whole section.

4. **Report results faithfully.** Extract headline results WITH their baselines, datasets, and metrics. Note whether results are single-run or averaged, and whether ablations isolate the contribution.

5. **Extract limitations.** List the authors' stated limitations, then add evident gaps (weak baseline, narrow eval, no significance test) labeled as your assessment, not theirs.

6. **Assess relevance and reliability.** State who this matters to and a calibrated confidence in the central claim based on the evidence presented.

7. **Pull key terms.** List notable terms/methods for follow-up, suitable to feed a glossary.

**Output Format:**

A markdown digest:
- **Citation & Scope** — what was provided; reliability caveat if partial.
- **Problem & Contribution (as claimed)** — attributed to the authors.
- **Method** — core approach in brief.
- **Key Results** — table: Result | Baseline | Dataset | Metric | Single/averaged.
- **Limitations** — Authors' stated | Reviewer-noted (clearly separated).
- **Relevance & Confidence** — who cares + calibrated belief in the claim.
- **Key Terms for Follow-up**.

## Verification

- [ ] Every number/result is from the provided text, with section cited for key results.
- [ ] Results reported with baseline, dataset, and metric — no naked percentages.
- [ ] Author-stated vs reviewer-noted limitations are separated.
- [ ] Nothing fabricated; missing details marked "not reported."
- [ ] Contribution attributed as a claim, not asserted as fact.

## False-Positive Prevention

❌ **DON'T:**
- Recall the paper's results "from memory" if the text wasn't provided.
- Report "+5 points" without saying over what baseline, on what dataset, by what metric.
- Repeat the authors' "state-of-the-art" framing as established fact.
- Blur the authors' admitted limitations with your own critical observations.

✅ **DO:**
- Digest only the provided content; flag partial input as a reliability limit.
- Pin every result to baseline + dataset + metric + run-count.
- Attribute claims to the authors and add your assessment separately.
- Keep author-stated and reviewer-noted limitations in distinct buckets.

## Example Output

```markdown
## Digest — "[Method] for Low-Resource [Task]" (provided: full text)

### Citation & Scope
Full paper provided; digest is reliable across all sections.

### Problem & Contribution (as claimed)
Authors claim existing methods need large labeled sets; they propose [method] that
reaches competitive accuracy with ~10× less labeled data. (Claim, §1.)

### Method
A two-stage approach: self-supervised pretraining on unlabeled in-domain text, then
fine-tuning on the small labeled set with a consistency-regularization loss. (§3.)

### Key Results (§5, Table 2)
| Result | Baseline | Dataset | Metric | Runs |
|---|---|---|---|---|
| 88.1 F1 @ 1k labels | 84.3 (strong supervised) | [DatasetA] | F1 | 5 seeds, ±0.4 |
| 85.0 F1 @ 200 labels | 79.1 | [DatasetA] | F1 | 5 seeds |

### Limitations
- Authors' stated: only evaluated on English; pretraining cost high. (§6.)
- Reviewer-noted: single dataset family; no comparison to the most recent semi-supervised
  baseline; gains may not transfer to other domains.

### Relevance & Confidence
Relevant if you have abundant unlabeled but scarce labeled data. Confidence in the core
claim: moderate-high — multi-seed with CIs and a strong baseline, but narrow eval scope.

### Key Terms for Follow-up
self-supervised pretraining, consistency regularization, low-resource learning.
```

**Techniques Used:**
- **ST-03 (Output Format Specification):** a fixed digest structure.
- **ST-02 (Structured Sequential Instructions):** problem → method → results → limitations.
- **RT-05 (Evidence-Based Reasoning):** every claim pinned to the text.
- **QA-01 (Self-Verification):** the no-fabrication and reliability checks.
- **DS-02 (Metric Specification):** results reported with baseline/dataset/metric.

**Related Prompts:**
- `mllearn_paper_reading_guide.md` — build the skill instead of consuming a digest.
- `mllearn_reproduce_a_paper_plan.md` — plan a reproduction from the digest.
- `mllearn_glossary_builder.md` — turn the key terms into a personal glossary.
