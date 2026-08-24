---
title: "Evidence Quality Score — Rate a Piece of Evidence on a Transparent Rubric"
category: reasoning-craft/epistemic
description: "Score a single piece of evidence (study, dataset, expert opinion, anecdote, news report) on a transparent multi-criterion rubric — design, sample, replication, source credibility, conflict of interest, recency, relevance — with a 1–5 score and justification per criterion, a composite with a confidence range, and a one-line statement of the load-bearing weakness. Counters the failure mode of treating all citations as equally probative and of letting a single strong-sounding source carry a conclusion it can't bear."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-01
  - DS-02
  - CM-02
  - QA-01
difficulty: intermediate
tags:
  - epistemic
  - evidence-quality
  - rubric
  - source-evaluation
  - critical-appraisal
updated: "2026-05-21"
reasoning:
  styles: [analytical, evaluative, structural]
  stakes: variable
  horizon: variable
  uncertainty: ambiguity
  evidence_quality: variable
  domain_complexity: variable
  collaboration: solo
  output_format: rubric_score_table
  user_role: [researcher, analyst, clinician, journalist, individual]
  mode: [audit, diagnose]
related_prompts:
  - domain-reasoning-craft/epistemic/epistemic_source_credibility_triangulation.md
  - domain-research-academic/research_evidence_map.md
  - domain-reasoning-craft/reasoning-moves/reasoning_bayesian_belief_update.md
---

# Evidence Quality Score

**Objective:** Score one piece of evidence on a transparent rubric so its probative weight can be compared, aggregated, or discounted explicitly. Each criterion — design/methodology, sample size/representativeness, replication/corroboration, source credibility, conflict of interest, recency, relevance to the claim — gets a 1–5 score with a one-line justification. Output a composite score with a confidence range and a single sentence naming the load-bearing weakness (the criterion that most limits how much this evidence can support). Designed to feed `research_evidence_map.md` and Bayesian updates with calibrated weights instead of vibes.

**When to use:**
- You're weighing a specific study, report, or claim and need to decide how much it should move your belief.
- Building an evidence map and need a consistent quality score per source.
- A conclusion rests heavily on one source and you want to know whether it can bear the weight.
- Comparing evidence items of different types (a trial vs an expert opinion vs an anecdote) on a common scale.

**When NOT to use:**
- You're comparing the *credibility of sources* against each other rather than scoring one item's quality — use `epistemic_source_credibility_triangulation.md`.
- You need to cross-check what multiple sources *say* about a claim — use `research_source_triangulation.md`.
- The evidence type has a domain-standard appraisal tool you should use instead (e.g., a formal risk-of-bias instrument for a clinical trial in a systematic review); this rubric is a general-purpose first pass.

**Audience:** Researchers, analysts, clinicians, journalists, and individuals deciding how much a given piece of evidence should count.

---

## Inputs / Context

1. **The evidence item.** What it is (study, dataset, expert statement, anecdote, report) and its content.
2. **The claim it's being used to support.** Relevance is judged against a specific claim, not in the abstract.
3. **Provenance.** Who produced it, who funded it, when, and where it was published or sourced.
4. **What's known about replication/corroboration.** Has it been confirmed independently?

---

## Scoring rubric (each 1–5)

- **Design / methodology** — how well the method supports the inference. (5: rigorous design appropriate to the question; 1: design can't support the claim — e.g., correlational evidence for a causal claim.)
- **Sample size / representativeness** — adequacy and generalizability of the sample. (5: well-powered, representative; 1: tiny or biased sample.)
- **Replication / corroboration** — independent confirmation. (5: replicated by independent groups; 1: single unreplicated result.)
- **Source credibility** — track record and transparency of the producer. (5: credible, transparent, methods available; 1: opaque or poor track record.)
- **Conflict of interest** — independence from interested parties. (5: no conflict; 1: produced/funded by a party with a stake in the result.)
- **Recency** — currency relative to how fast the field moves. (5: current; 1: superseded.)
- **Relevance to the claim** — how directly the evidence bears on *this* claim. (5: direct; 1: tangential or requires a long inferential leap.)

(Score only criteria that apply; mark others "n/a" with a reason.)

---

## Constraints

### Must
- Score each applicable criterion 1–5 with a one-line justification grounded in the actual evidence.
- Produce a **composite** — a weighted or explained aggregate, not a blind average — and state how it was formed.
- Attach a **confidence range** to the composite reflecting how much is unknown about the evidence.
- Name the **single load-bearing weakness**: the criterion that most constrains how much this evidence can support.
- State what claim-strength the evidence *can* support after scoring (e.g., "supports a weak directional prior, not a confident causal claim").

### Must Not
- Collapse to a single gut score without the per-criterion breakdown.
- Average mechanically across criteria when one criterion is disqualifying. A fatal conflict of interest or a design that can't support the claim caps the composite regardless of other strengths.
- Conflate "source is prestigious" with "evidence is strong." Prestige is one input to one criterion.
- Score relevance in the abstract — always against the specific claim.
- Treat a high score as proof the claim is true. A strong piece of evidence raises support; it doesn't settle the claim alone.

---

## Instructions

### Step 1 — State the evidence and the claim
One line each: what the evidence is, what claim it's being used to support.

### Step 2 — Score each criterion
Walk the rubric. For each applicable criterion, assign 1–5 and justify in one line from the evidence itself. Mark inapplicable criteria n/a with a reason.

### Step 3 — Identify caps
Check for disqualifying criteria: a design that can't support the claim, a fatal conflict of interest, or zero relevance. Any of these caps the composite regardless of other scores.

### Step 4 — Form the composite
Aggregate the scores, applying any caps and explaining the weighting (e.g., "design and relevance weighted heaviest for a causal claim"). Don't present a blind mean.

### Step 5 — Confidence range
State a range around the composite reflecting unknowns (missing methods, unverified provenance). Wide range = much is unknown.

### Step 6 — Load-bearing weakness
Name the one criterion that most limits the evidence's usefulness. This is the thing to fix or watch.

### Step 7 — Claim-strength statement
State what the evidence can legitimately support after scoring — the calibrated takeaway for a downstream evidence map or Bayesian update.

---

## False-Positive Prevention

1. **Single-number collapse.** Reporting one score with no breakdown. The per-criterion detail is the value; the composite is a summary of it.
2. **Mechanical averaging.** Letting strong criteria paper over a disqualifying one. A fatal conflict or a question-incapable design caps the composite — say so.
3. **Prestige halo.** Scoring a famous journal or name as automatically high quality across all criteria. Prestige touches credibility, not design, sample, or conflict.
4. **Abstract relevance.** Scoring relevance without a specific claim in hand. Relevance is always to *this* claim.
5. **Quality-as-truth.** Treating a high composite as proving the claim. Strong evidence updates belief; it doesn't close the question by itself.
6. **Hidden weighting.** Aggregating with undisclosed weights. State which criteria you weighted heaviest and why.
7. **False precision.** A 4.27 composite implies more than the inputs support. Use coarse scores and an explicit range.
8. **Ignoring the unknown.** Scoring confidently when methods or provenance are unavailable. Reflect that ignorance in a wide confidence range, not a confident point score.

---

## Output Format

```
# Evidence quality score — [evidence item]

## Evidence and claim
- Evidence: [what it is]
- Claim it supports: [the specific claim]

## Rubric scores
| Criterion                     | Score (1–5 / n/a) | Justification (1 line) |
|-------------------------------|-------------------|------------------------|
| Design / methodology          |                   |                        |
| Sample size / representativeness |                |                        |
| Replication / corroboration   |                   |                        |
| Source credibility            |                   |                        |
| Conflict of interest          |                   |                        |
| Recency                       |                   |                        |
| Relevance to the claim        |                   |                        |

## Caps applied
[Any disqualifying criterion that limits the composite, or "none"]

## Composite
- Score: [n/5], formed by [weighting/explanation]
- Confidence range: [low–high] because [what's unknown]

## Load-bearing weakness
[The single criterion that most limits this evidence]

## What this evidence can support
[Calibrated claim-strength statement for downstream use]
```

---

## Verification

- [ ] Each applicable criterion scored 1–5 with a one-line justification.
- [ ] Inapplicable criteria marked n/a with a reason.
- [ ] Any disqualifying cap identified and applied.
- [ ] Composite explained (weighting stated), not a blind average.
- [ ] Confidence range attached and tied to specific unknowns.
- [ ] Single load-bearing weakness named.
- [ ] Claim-strength statement provided for downstream use.
- [ ] High scores not treated as proof the claim is true.
