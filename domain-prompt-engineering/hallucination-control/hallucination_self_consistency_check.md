---
title: "Self-Consistency Check — Sample N, Flag Disagreeing Claims"
category: prompt-engineering/hallucination-control
description: "Generate the response N times under varied seeds or temperature, decompose each into atomic claims, and flag claims that do not agree across samples."
techniques:
  - ST-01
  - ST-03
  - CM-02
  - QA-01
  - PR-02
difficulty: advanced
tags:
  - hallucination
  - self_consistency
  - sampling
  - claim_voting
  - reliability
updated: "2026-05-10"
related_prompts:
  - domain-prompt-engineering/hallucination-control/hallucination_calibrated_uncertainty_prompt.md
  - domain-prompt-engineering/hallucination-control/hallucination_invented_entity_audit.md
  - domain-prompt-engineering/reasoning-strategies/
---

# Self-Consistency Check

**Objective:** Run the same prompt N times, extract atomic claims from each response, and produce a per-claim agreement rate. Claims below an agreement threshold are flagged as low-reliability or dropped.

**When to use:** High-stakes factual or reasoning tasks where one shot is insufficient and the cost of N samples is acceptable. Especially: arithmetic, multi-hop, ambiguous extraction.

---

## Inputs

1. `prompt` — the task prompt.
2. `n_samples` — int, 3–9 (odd values resolve ties).
3. `sampling_strategy` — `temperature_jitter` (vary T across samples), `seed_jitter` (fixed T, vary seed), or `paraphrase_jitter` (vary the prompt phrasing slightly).
4. `agreement_threshold` — float 0.0–1.0; default 0.6.
5. `claim_match_mode` — `exact`, `normalized` (case/whitespace/numeric-format normalized), or `semantic` (embedding similarity ≥ τ).

---

## Constraints

### Must
- Run N independent samples. Do not reuse one sample's output as input to another.
- Decompose each sample into atomic claims (one fact per claim).
- Cluster equivalent claims across samples using `claim_match_mode`.
- For each cluster, compute `agreement_rate = cluster_size / n_samples`.
- Flag claims with rate below `agreement_threshold`.
- Report a deterministic action: `keep`, `flag`, or `drop` per claim.

### Must Not
- Average natural-language responses; cluster claims, then synthesize.
- Use `semantic` mode for numerics, dates, or named entities — exact only.
- Treat majority as truth on factual disagreement; majority is signal, not proof.
- Hide flagged claims by burying them in passive voice.
- Re-run the prompt to generate a "tiebreaker" sample after seeing results.

---

## Sampling Strategies

| Strategy | Knob | Best for |
|---|---|---|
| `temperature_jitter` | T ∈ {0.2, 0.5, 0.8} | Reasoning where exploration matters |
| `seed_jitter` | T fixed (e.g., 0.7), seed varied | Stochasticity at one regime |
| `paraphrase_jitter` | prompt rephrased N times | Sensitivity to prompt wording |

If the model API does not expose seeds, fall back to `paraphrase_jitter`.

---

## Instructions

1. Generate N responses per the chosen strategy.
2. Atomize each response: one factual or numeric assertion per claim.
3. Cluster claims across samples using `claim_match_mode`. For numerics, exact only — `12,345` and `12345` differ unless `normalized`.
4. For each cluster, compute agreement_rate.
5. Apply action policy:
   - `agreement_rate ≥ threshold` → keep.
   - `0.4 ≤ agreement_rate < threshold` → flag (include but label).
   - `agreement_rate < 0.4` → drop or refuse.
6. Compose the final answer from kept claims; emit the disagreement report.

---

## Output Format

```json
{
  "n_samples": <int>,
  "strategy": "temperature_jitter | seed_jitter | paraphrase_jitter",
  "claims": [
    {
      "canonical_text": "...",
      "agreement_rate": <float>,
      "supporting_samples": [<int>, ...],
      "competing_values": [{"text": "...", "support_count": <int>}],
      "action": "keep | flag | drop"
    }
  ],
  "final_answer": "<assembled from kept + flagged claims, with flags marked>",
  "drop_count": <int>,
  "flag_count": <int>
}
```

---

## Verification

- [ ] N independent samples generated.
- [ ] Every claim cluster has `agreement_rate` and `action`.
- [ ] No semantic match used for numerics, dates, or IDs.
- [ ] Final answer marks flagged claims (not silently kept).
- [ ] Disagreement report present even when all claims agree.

---

## Anti-Patterns

1. Asking the model to "be consistent" instead of running N samples — does not surface variability.
2. Using N=2 — no majority possible.
3. Semantic clustering of numerics — hides numeric drift.
4. Treating the modal sample as the answer wholesale — misses claim-level disagreement inside otherwise-similar samples.
5. Using self-consistency as the only guard — pair with `hallucination_invented_entity_audit.md` for entity-level checks.
