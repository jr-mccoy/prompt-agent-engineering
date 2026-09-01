# ADR-0021 — Search is deterministic, lexical, and reads metadata only

## Status

Accepted. Implemented in Phase 4.

## Context

The Engine had exact lookup and nothing else. A user with a task rather than a
reference had no way in, and the repository's answer to "which resource for
this job?" was 3,100 lines of hand-maintained prose.

Phase 4A ran the alternatives as measured experiments over the live registry
rather than choosing by intuition. Phase 4 then rebuilt the winner inside the
Engine and re-ran the comparison through one code path, because the Phase 4A
report quoted numbers produced at different stages of experimentation and they
did not all agree.

The reproducible comparison, 120 labelled cases, one index, one tokenizer:

| Ranker | resource@1 | resource@3 | MRR | scope@1 | kind@1 |
|---|---|---|---|---|---|
| weighted token overlap | 56.1% | 75.8% | 0.665 | 72.9% | 68.3% |
| flat BM25 | 75.8% | 81.8% | 0.805 | 81.2% | 97.6% |
| **BM25F, uniform weights** | **77.3%** | **84.8%** | **0.817** | **83.5%** | **97.6%** |

Three results are worth recording because they contradict the obvious guess.

**Hand-tuned field weights were worse than uniform.** Every weighting tried in
Phase 4A — title-heavy, description-heavy, tag-heavy, and several balanced
combinations — scored at or below uniform. Uniform sits on a plateau where
perturbing one field weight moves top-1 accuracy by at most a single query.

**A relevance-bonus layer made ranking worse.** Additive bonuses for exact tag,
category and technique matches dropped resource@1 from 77.3% to 68.2%. The
technique bonus was structurally wrong: matching `ST-01` rewarded the ~3,900
prompts that *cite* ST-01 and buried the technique record itself, which plain
BM25F already ranks first with no special case. A corrected multiplicative
version still lost to no bonuses at all.

**Depluralization is the single highest-value normalization step**, worth about
ten points of top-1 accuracy. Emitting compact code forms for `ST-01` was
worth nothing, because symmetric splitting already handles it.

## Decision

Search is **BM25F over registry metadata** with **uniform field weights**,
`k1 = 1.2`, `b = 0.75`. Ten fields are indexed: title, public-ID path, aliases,
description, category, tags, technique IDs, source path, kind and native name.

No relevance bonuses. No tuned coefficients. No stemmer, synonym list, spelling
model or n-gram layer.

One shared normalizer serves indexing and querying: NFKC, casefold, split on
runs of non-`[0-9a-z]`, drop a fixed source-controlled stopword list,
depluralize with one four-line rule.

**Relevance never reads a body.** `Registry.content()` is not called from the
search or routing modules — enforced by a source-level check and a behavioural
test that makes the call fail loudly.

**Governance never ranks.** Maturity, review status, eval status, licence,
provenance, serving policy, quality assertions and metadata completeness filter
and display; they do not score. There are no quality tiers in this registry, so
there is no quality boost to invent.

The index is **in-memory, immutable, and built lazily** on the first lexical
search. No committed index artifact, no cache directory, no database, no
sidecar file, nothing written at runtime. An exact UID or public ID resolves
through the existing lookup path without building it at all.

Ordering is `round(score, 9)` descending, then public ID ascending. Never
hash, set or filesystem iteration order.

## Consequences

- A `score` is an unbounded ranking number that orders one query's results. It
  is not a probability, a percentage or a confidence, and no output presents it
  as one.
- Explanations are `matched_fields` and `match_terms` — observable evidence.
  Per-term BM25F arithmetic stays private so `k1`, `b` and the field set are
  not frozen into the public contract.
- One-shot `pae search` pays roughly 1.7 s: about 1 s of that is loading the
  registry and building documents, which BM25F needs regardless because it
  depends on corpus-wide statistics. Warm queries are sub-millisecond, which is
  the case a long-lived MCP process will live in.
- Lexical retrieval fails in lexical ways. "best hiking boots for wet granite"
  routes to software engineering, because `boots` depluralizes to `boot` and
  matches Spring Boot. Semantic retrieval is not in scope, and pretending a
  BM25F score is understanding would be worse than the miss.
- Non-ASCII letters are dropped by the tokenizer. Indexing and querying do it
  identically, so `café` still finds `café`; it will not find `cafe`, and a
  query with no ASCII alphanumerics is rejected as a usage error.

## Alternatives rejected

- **Weighted token overlap** — 21 points worse on resource@1.
- **Flat BM25** — competitive on resource retrieval, 2.3 points worse on scope
  accuracy. Per-field length normalization is what stops a forty-word skill
  description from drowning a one-word title.
- **Hand-tuned field weights and a bonus layer** — measured worse, and they
  would freeze arbitrary constants into a public contract.
- **A committed index artifact** — a second generated source of truth that can
  disagree with `registry.jsonl`; the hazard [ADR-0007](0007-index-is-not-the-registry.md)
  and [ADR-0013](0013-layered-ledger-and-generated-jsonl.md) exist to prevent.
- **A writable cache or database** — contradicts the read-only runtime
  ([ADR-0019](0019-runtime-serving-and-integrity.md)).
- **Embeddings or a vector store** — a runtime dependency, a model dependency
  and a network dependency, against [ADR-0003](0003-dependency-light-core.md)
  and [ADR-0018](0018-checkout-required-runtime.md).

## Related

- [ADR-0003](0003-dependency-light-core.md) — stdlib-only core
- [ADR-0015](0015-serving-policy-metadata.md) — serving policy fails closed
- [ADR-0019](0019-runtime-serving-and-integrity.md) — read-only runtime
- [ADR-0022](0022-routing-by-max-aggregation.md) — routing on top of this
