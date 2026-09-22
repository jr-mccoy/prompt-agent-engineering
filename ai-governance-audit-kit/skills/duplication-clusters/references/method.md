# Clustering method

## Exact clusters

Group by `source.content_sha256`. Every inventory record already carries the
hash, so this tier is free and its evidence is complete: two files either have
the same bytes or they do not.

## Candidate clusters

All-pairs **query-by-document** over `pae_engine._lexical.LexicalIndex` — the
same BM25F index `pae search` uses. Each artifact's own normalized terms become
a query; the ranked results are its lexical neighbours.

Importing the Engine's index rather than writing a second BM25F is deliberate.
A private implementation would drift, and a cluster the audit reports would
stop matching what the client's own `pae search` shows them. It also honours
ADR-0003: lexical only, no embeddings, no network, no model.

### Normalization

Raw BM25F sums are not comparable across documents. A long artifact generates
more query terms and therefore a larger score, so a fixed threshold on raw
scores silently ranks by length.

Each pair is scored **in both directions** and divided by the querying
document's own self-score, which is the maximum that query can reach. The
result is a ratio in `[0, 1]`.

### The reported figure is the minimum of the two directions

This is the false-positive prevention, and it is the one design choice in this
skill worth arguing about.

A short artifact whose every term appears inside a long one scores high in one
direction — the short query is fully satisfied — and low in the other, because
the long document's many other terms are absent from the short one. Reporting
the maximum, or the mean, would call that pair a near-duplicate. It is
containment, not duplication: a two-line checklist is not a duplicate of the
handbook that contains it.

Taking the minimum requires **mutual** similarity. Both directional scores are
kept in the evidence, so a reader can see the asymmetry the headline figure
suppressed.

### Per-artifact neighbour cap

Applied after ordering by similarity, so the strongest candidates survive the
cap rather than whichever pair happened to be walked first. Without ordering
first, a boilerplate-heavy corpus fills each artifact's quota with its weakest
neighbours.

## What a canonical would require, and why there is none

`canonical_uid` is `null` in every cluster, with a stated basis.

- **mtime** is an artifact of the checkout, not of authorship.
- **Path** is not provenance. `prompts/final/` is not evidence.
- **Git history** would be evidence, and the kit deliberately does not read it:
  a corpus audit that requires a full history cannot run on a delivered
  snapshot, which is what clients send.

This mirrors `pae_registry/governance.py`, which refuses to assert a quality
tier because *"inferring one from document structure would be fabricating a
rubric score."* Naming a canonical from a hash would be the same fabrication
wearing a different hat.

The client names the canonical. The kit hands them the cluster and its
evidence.

## Stated limitations

- **A paraphrase is invisible.** Two artifacts doing the same job in different
  vocabulary will not cluster. Lexical similarity cannot see intent.
- **Shared boilerplate creates noise.** A corpus where every artifact carries
  the same 200-word header will cluster broadly. Raise the threshold, or move
  the boilerplate out of the indexed fields.
- **Similarity is not redundancy.** Two prompts may be near-identical in
  vocabulary and correctly distinct in purpose — this repository keeps several
  weekly-review prompts on exactly that basis. That is why the output is a
  finding for adjudication rather than a consolidation instruction.

## Evidence fields

| Field | Meaning |
|---|---|
| `similarity` | the reported figure: minimum of the two directions |
| `evidence.directional` | both directional ratios, keyed by path |
| `evidence.reported` | which of the two the headline figure is |
| `evidence.shared_terms` | up to 20 normalized terms both artifacts carry |
| `evidence.shared_term_count` | how many there are in total |
| `evidence.basis` | the index and method, named |

A cluster without its evidence is an assertion. Take the evidence to the
corpus owner.
