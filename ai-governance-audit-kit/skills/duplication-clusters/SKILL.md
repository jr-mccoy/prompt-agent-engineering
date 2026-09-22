---
name: duplication-clusters
description: Find repeated and near-repeated artifacts in a corpus and report them as adjudicable findings rather than as asserted copies. Use this skill to "find duplicate prompts", "how much of our library is repeated", "we think two teams wrote the same thing twice", "cluster our near-duplicates", or when a consolidation decision needs evidence. Reports exact clusters from content hashes and candidate clusters from BM25F query-by-document, and never names a canonical.
license: MIT
compatibility: Standard library only, Python 3.9+, plus the PAE checkout it ships inside for `pae_engine._lexical`. `scripts/cluster.py --self-check` proves the byte-identical pair is exact, the reworded pair is a candidate, the unrelated artifact is not clustered, and that no `copy_of` edge is emitted. No network, no embeddings, no writes unless `--out` is given.
metadata:
  tags: [audit, duplication, clustering, bm25f, governance, deduplication]
  updated: "2026-09-22"
---

# Duplication Clusters

## Purpose

The most expensive defect in a grown prompt library is two artifacts doing the
same job for the same reader. Nobody plans it; it arrives when two teams solve
the same problem in the same quarter.

Detecting it is genuinely new work. This repository's own duplicate handling is
deliberately **edge-based** — `copy_of` and `copies` come from explicit ledger
entries, "never hashes or filenames" (ADR-0012). That is right for a repository
that knows its own provenance and useless on a client corpus that has no ledger.

So this skill detects, and it is careful never to let detection masquerade as
provenance.

## Two tiers, and they are not the same claim

| Tier | Evidence | What it means |
|---|---|---|
| `exact` | `source.content_sha256` equality | byte-identical files |
| `candidate` | BM25F query-by-document | lexically similar; a human decides |

**Neither tier names a canonical.** Which of two byte-identical files came
first is not knowable from a checkout: mtime is an artifact of the clone and a
path is not provenance. `canonical_uid` is `null` with a stated basis, the same
refusal `pae_registry/governance.py` makes when it declines to infer a quality
tier from document structure.

## When to Use

- A consolidation decision needs evidence rather than an impression.
- After `corpus-inventory`, before any remediation is proposed.
- When a client asks "how much of this library is redundant".

## When NOT to Use

- To decide *which* duplicate to keep. That is a judgement about which one the
  organisation stands behind, and the kit deliberately refuses to make it.
- On this repository's own corpus, where `meta/VENDORED.tsv` already records
  every canonical→copy pair explicitly.

## Instructions

1. Run `scripts/cluster.py --inventory audit/inventory.json --out audit/clusters.json`.
2. Read the exact clusters first. They need no adjudication of *similarity*,
   only of which copy the organisation keeps.
3. Read candidates in descending similarity. The reported figure is the
   **minimum** of the two directional scores; `references/method.md` explains
   why that choice prevents the most common false positive.
4. Take the shared-term evidence to the corpus owner. A cluster without its
   evidence is an assertion.
5. Raise `clustering.candidate_threshold` if the candidate list is too noisy to
   work through; exact clusters are unaffected by the threshold.

## Bundled Resources

- `scripts/cluster.py` — exact and candidate clustering, and the CLI.
- `references/method.md` — the normalization, the conservative direction, the
  per-artifact neighbour cap, and what the evidence fields mean.

## Safety

Read-only. A candidate cluster is a finding, not an instruction: nothing here
deletes, merges or rewrites anything, and the output carries a disclosure
sentence saying so.

## Troubleshooting

- Everything clusters with everything: the corpus shares a heavy boilerplate
  header. Raise the threshold, or exclude the boilerplate from the indexed
  fields by moving it out of `description`.
- A known duplicate pair does not appear: the two are written in different
  vocabulary. Lexical similarity cannot see a paraphrase, and
  `references/method.md` says so as a stated limitation.

## Verification

- [ ] Every candidate cluster carries directional scores and shared terms.
- [ ] No cluster names a canonical.
- [ ] No output field asserts a `copy_of` relationship.

## Related Skills

- `corpus-inventory` — produces the inventory this reads.
- `registry-handback` — carries these findings as diagnostics, never as edges.
