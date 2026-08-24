# Stage 3 — Claim–Source Matching & Weighting

**Role in pipeline:** Decide whether each candidate source *actually supports its claim*, weigh source quality/credibility, triangulate, and resolve conflicts — producing a per-claim verdict.

**Objective:** Convert candidate sources into a defensible verdict per claim: SUPPORTED / PARTIAL / CONTESTED / UNVERIFIED — with the quality-weighted evidence behind it.

**Orchestrates:** `domain-research-academic/research_source_triangulation.md`, `domain-reasoning-craft/epistemic/epistemic_evidence_quality_score.md`, `domain-reasoning-craft/epistemic/epistemic_source_credibility_triangulation.md`, `domain-research-academic/research_evidence_map.md`, `domain-prompt-engineering/rag-prompts/rag_conflict_resolution_across_sources.md`.

---

## Inputs
- Candidate sources per claim (Stage 2).
- Scope Record (profile's `minimum_anchor_tier`, recency caution, conflict rule).

## Instructions
1. **Support check (CRITICAL).** For each candidate, compare the source's actual passage to the claim. Does it support *this specific claim*, at the *same strength*? Topical relatedness is not support.
   - Fully supports, same strength → counts as support.
   - Supports a weaker/narrower version → PARTIAL (note the gap).
   - Doesn't actually support it → discard the source (misattribution risk).
2. **Quality-score** each supporting source (design, sample, credibility, COI, recency vs profile caution, relevance). Below-`minimum_anchor_tier` sources can corroborate but shouldn't solely anchor a claim.
3. **Triangulate.** Prefer independent support from ≥2 source types. Note where apparent agreement is actually one original source echoed (not independent).
4. **Resolve conflicts.** If credible sources disagree, apply the profile `conflict_rule` (surface the disagreement; prefer higher-tier + more recent + more specific). Don't average it away.
5. **Assign the verdict:**
   - `SUPPORTED` — ≥1 source at/above anchor tier directly supports; no strong contradiction.
   - `PARTIAL` — supported only in a narrower/weaker form (record the sourced version).
   - `CONTESTED` — credible sources genuinely disagree.
   - `UNVERIFIED` — no candidate actually supports it at an acceptable tier.
6. **Attach the certainty the evidence licenses** (feeds Stage 4 SOFTEN decisions).

## Output Format
```
## Claim Verdicts
| Claim # | Verdict | Anchor source(s) | Quality | Licensed certainty | Note |
|---------|---------|------------------|---------|--------------------|------|
| 1 | SUPPORTED | S1 (tier1), S3 (tier2) | high | "established" | independent triangulation |
| 2 | PARTIAL | S5 (tier2) | med | "one study suggests" | source narrower than claim |
| 4 | CONTESTED | S7 vs S9 | mixed | "debated" | surface both |
| 6 | UNVERIFIED | — | — | — | no source actually supports |

## Notes
- Echo-chamber flags (non-independent agreement): [...]
- Conflicts surfaced: [...]
```

## Verification
- [ ] Support checked at the substance level (passage vs claim), not by link presence.
- [ ] Sources quality-scored; sub-tier sources not used as sole anchors.
- [ ] Non-independent agreement flagged, not counted as triangulation.
- [ ] Conflicts surfaced per the profile rule, not averaged.
- [ ] Every claim has a verdict + licensed-certainty note.
