# Stage 2 — Duplication Clusters

*Clusters are findings for adjudication. This kit never names a canonical.*

**Objective:** Find repeated and near-repeated artifacts, with evidence, and
hand them to the corpus owner as a decision rather than as an instruction.

**When to Use:** After Gate 0 passes, before anything is scored or proposed.

**When NOT to use:** To decide which duplicate to keep — that is a judgement
about which artifact the organisation stands behind.

## Method

1. `python3 skills/duplication-clusters/scripts/cluster.py --inventory audit/inventory.json --out audit/clusters.json`
2. Work the **exact** clusters first. Similarity needs no adjudication there;
   only "which one do we keep" does.
3. Work **candidates** in descending similarity. Read the shared terms for each
   one before forming a view. A high score from shared boilerplate is a finding
   about the boilerplate.
4. For each candidate, ask the owner one question: *do these two do the same
   job for the same reader?* Similar vocabulary and distinct purpose is a
   legitimate, common answer.
5. If the candidate list is unworkably long, raise
   `clustering.candidate_threshold` and say in the report that you did, and to
   what. Do not quietly truncate.

## What the two tiers claim

| Tier | Evidence | Claim |
|---|---|---|
| `exact` | content hash equality | these files have the same bytes |
| `candidate` | BM25F query-by-document | these files use similar language |

Neither claims provenance. `canonical_uid` is `null` in every cluster: mtime is
a checkout artifact, a path is not evidence, and git history is deliberately
not read because a delivered snapshot does not have one.

## Output

`audit/clusters.json` — exact and candidate clusters, each with member UIDs and
paths, the similarity, both directional scores, the shared terms, and the
method that produced it.

## Verification

- [ ] Every candidate cluster carries directional scores and shared terms.
- [ ] No cluster names a canonical.
- [ ] Nothing in the output asserts a `copy_of` relationship.
- [ ] Any threshold change is recorded with its value.

## False-Positive Prevention

1. **Containment is not duplication.** A short checklist contained in a long
   handbook scores high in one direction only. The reported figure is the
   minimum of the two directions precisely to suppress this; if you override the
   figure by eye, you are reintroducing the error.
2. **A paraphrase is invisible.** Two artifacts doing the same job in different
   words will not appear here. State that as a limitation; do not let the empty
   result read as "no duplicates".
3. **Similar is not redundant.** Several artifacts may be near-identical in
   vocabulary and correctly distinct in purpose. Ask before proposing a merge.
4. **Do not report a duplication percentage.** It would be a directional claim
   about a corpus you have measured once, and Gate B will block it.

## Related

- `skills/duplication-clusters/SKILL.md`; `references/method.md` for the
  normalization and the stated limitations.
- Next: `stage-3-observed-scoring.md`.
