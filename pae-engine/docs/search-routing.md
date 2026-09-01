# Search and routing

How `pae search` and `pae route` work, what they will and will not do, and
where they are weak.

Both read **registry metadata only**. Neither calls `Registry.content()`, so
what a resource *says* can never influence where it ranks, and a search can
never become a way to read something serving policy withholds.

---

## Two commands, two questions

`pae search` ranks resources against a query. `pae route` decides which
**scope** and **resource kind** should handle a task, then offers the strongest
starting points. Routing can answer "this is ambiguous" — search cannot, and
should not.

```bash
pae search "android security audit"
pae route  "my model drifted in production and accuracy dropped"
```

Neither command executes a resource, and neither prints a body.

---

## Query normalization

One tokenizer serves indexing and querying. If they diverged, a document would
be findable by terms no query can produce.

```
NFKC → casefold → split on runs of [^0-9a-z] → drop stopwords → depluralize
```

Splitting on every non-alphanumeric run is why spelling variants collapse:

```
curriculum-architecture   ─┐
curriculum_architecture   ─┼─→  ["curriculum", "architecture"]
curriculum architecture   ─┘
```

It is also why acronyms and codes need no special handling — both sides split
identically:

```
ST-01 → ["st", "01"]      R8 → ["r8"]      MCP → ["mcp"]      CI/CD → ["ci", "cd"]
```

**Depluralization** is one rule, not a stemmer: `-ies → -y`, otherwise drop a
trailing `s` when the token is longer than three characters and does not end in
`ss`, `us`, `is` or `as`. It measured as the single highest-value normalization
step, worth about ten points of top-1 accuracy. The `-is` guard protects
`analysis` at the cost of leaving `apis` unfolded.

The **stopword list** is fixed and lives in `_lexical.py`. A stopword set that
changed underneath the index would silently change every score.

**Limitation:** non-ASCII letters are discarded. Indexing and querying do it
identically, so `café` still finds `café`; it will not find `cafe`, and a query
with no ASCII alphanumerics at all normalizes to nothing and is rejected.

---

## Ranking: BM25F with uniform weights

Ten fields are indexed — `title`, `pid`, `alias`, `desc`, `cat`, `tags`,
`tech`, `path`, `kind`, `name` — each with weight **1.0**.

```
pseudo_tf(t,d) = Σ_f  w_f · tf(t, d.f) / (1 − b + b · len(d.f) / avglen(f))
score(d)       = Σ_t  idf(t) · pseudo_tf(t,d) / (k1 + pseudo_tf(t,d))
idf(t)         = ln(1 + (N − df(t) + 0.5) / (df(t) + 0.5))
```

with `k1 = 1.2`, `b = 0.75`. `df` counts documents, not field occurrences. An
empty field contributes nothing, and a field no document populates is skipped.

Accumulating each field's length-normalized contribution *before* saturating is
the point of BM25F: it stops a forty-word skill description from drowning a
one-word title match.

Weights are uniform because hand-tuned weights measured **worse**, and a
relevance-bonus layer measured worse still. See
[ADR-0021](../../meta/adr/0021-deterministic-lexical-search.md).

### Fields that never affect relevance

`maturity`, `review_status`, `eval_status`, `license`, `provenance`,
`serving_policy`, `diagnostics`, `quality`, `metadata_completeness`, `related`,
`difficulty`, `agents_used`.

These filter and display. They do not rank. There are no quality tiers in this
registry, so there is no quality boost to invent — and there is no safety
penalty either: a `safety_gated` resource ranks on its words like anything else.

### Ties

`round(score, 9)` descending, then public ID ascending. Never hash, set or
filesystem iteration order. Repeating a query produces byte-identical JSON.

---

## Scores are not confidence

`score` is an unbounded lexical ranking number. It orders results **within one
query** and means nothing across queries. It is not a probability, not a
percentage, not calibrated. Nothing in the Engine emits a `confidence` field.

Explanations are observable evidence instead:

```json
{
  "matched_fields": ["title", "tags", "cat"],
  "match_terms": {
    "title": ["android", "audit", "security"],
    "tags":  ["android", "audit", "security"],
    "cat":   ["security"]
  }
}
```

---

## Scope derivation

One helper decides what a scope is, and search hits, `--scope`, router
aggregation and the diagnostics all use it.

| Public ID | Scope |
|---|---|
| `prompt:software-engineering/api/…` | `software-engineering` |
| `skill:financial-records-toolkit/…` | `financial-records-toolkit` |
| `skill:agentic-resources/cloud-infrastructure/…` | `agentic-resources/cloud-infrastructure` |
| `technique:ST-01` | `st` (its category) |

Two special cases earn their keep. `agentic-resources` alone spans 643
resources across four kinds, so routing a caller to it answers nothing — it is
split one level deeper. And a technique's ID has no path at all; treating
`ST-01` as a scope would invent 336 single-member scopes.

Scopes mix subject domains with toolkits. That is the registry's real shape,
not a modelling error.

---

## Eligibility

| Population | Default | Override |
|---|---|---|
| `serving_policy: excluded` | never searchable | **none, ever** |
| `lifecycle: tombstone` | hidden | `--include-tombstones` |
| `maturity: deprecated` (live) | hidden | `--include-deprecated` |
| `metadata_only` | searchable | — |
| `safety_gated` | searchable | — |

Ineligible records are absent from the index, not down-ranked. `metadata_only`
and `safety_gated` resources are searchable **by their metadata**; their bodies
remain governed by `Registry.content()` exactly as before.

Every tombstone is also marked deprecated, so `--include-tombstones` works on
its own — lifecycle inclusion wins for tombstones.

Because eligibility changes the corpus statistics every score depends on, it is
a **constructor** argument. `kinds`, `scopes`, `limit` and `include_copies`
only subset an existing ranking, so they are **query** arguments and do not
rebuild IDF.

---

## Copy clusters

59 registry records are registered copies of another resource, established
only from explicit `copy_of` / `copies` edges — never hashes or filenames
([ADR-0012](../../meta/adr/0012-one-record-per-copy.md)).

By default a cluster returns **one** hit: the highest-scoring eligible member,
tie-broken by public ID. That member may be a toolkit-local copy, which is
usually the one a caller working inside that toolkit wants. `canonical_uid` and
`copy_uids` make the suppression visible; `--include-copies` turns it off.

A copy whose canonical is **excluded** reports its own UID as `canonical_uid`.
Surfacing the excluded record's UID would let a caller enumerate excluded
resources by collecting cluster pointers that resolve to nothing.

---

## Exact references

If the whole query is a UID, a current public ID or a retired alias, it
resolves through the existing lookup path and comes back at rank 1 — **without
building the index**, so an exact reference stays as cheap as `pae get`.

This is a shortcut, not a score bonus, and it obeys every eligibility rule:

| The reference names… | Result |
|---|---|
| an eligible live resource | that resource, rank 1, `matched_fields: ["exact_reference"]` |
| a registered copy | that physical copy, not its canonical |
| a deprecated or tombstoned resource | zero hits **plus a notice** naming the flag that would include it |
| an excluded resource | zero hits, no notice, no metadata |
| nothing (but is reference-shaped) | falls through to ordinary lexical search |

A `--scope` filter forces the index to build, because validating a scope means
knowing the scope universe. `--kind` does not.

---

## Routing

The Router searches to depth 40 with cluster deduplication on, then:

```
scope_score(scope) = max(hit.score for hits in that scope)
kind_score(kind)   = max(hit.score for hits of that kind)
```

**Maximum, never sum.** Summing hands the answer to whichever kind has the most
members — with 4,196 prompts against 53 personas, a summing router scored 58.5%
on kind against maximum's 97.6% — and lets a registered copy vote twice for its
toolkit. `hit_count` is reported and never scored.

### Status

Two named quantities, neither called confidence:

- **coverage** — fraction of normalized query terms the top hit matched in
  `title`, `desc`, `pid` or `tags`;
- **margin** — `(top_scope − second_scope) / top_scope`; `1.0` with one scope,
  `0.0` with none.

```
no hits                                → no_route
coverage < 0.34                        → weak
≥2 scopes and margin < 0.25            → ambiguous
otherwise                              → matched
```

`selected_scope` and `selected_kind` are populated **only** when the status is
`matched`. A consumer that ignores `status` gets `null` rather than a guess.

**Every status exits 0.** Ambiguity is a result, not a failure. Branch on
`status`.

> The thresholds 0.34 and 0.25 are **provisional heuristics fitted on the
> project's own 120-case regression set**. They are not calibrated confidence
> thresholds and should be expected to move once an independently authored
> evaluation exists. An absolute score threshold was tested and measured inert.

`matched` is deliberately rare: on the regression set the Router returns
`ambiguous` for 64 cases and `matched` for 40. Returning ranked alternatives
beats manufacturing a single confident answer.

---

## Performance

The index is built lazily on the first lexical search, then reused immutably.

| Operation | Measured |
|---|---|
| `SearchEngine(...)` construction | no index build, no registry read |
| exact-reference search | ~11 ms, index still unbuilt |
| index build (5,217 documents, ~12,000 terms) | ~1.0 s |
| warm search | ~0.8 ms median |
| `pae search` one-shot | ~1.7 s |
| peak RSS | ~150 MB |

About a second of the one-shot cost is loading the registry and building
documents, which BM25F needs regardless: it depends on corpus-wide statistics,
so there is no streaming shortcut. A long-lived process — a future MCP server —
pays it once and then serves sub-millisecond queries.

A `SearchEngine` is a **snapshot**. If the checkout changes underneath a
long-lived process nothing is watched, invalidated or rebuilt; construct a new
engine to see a new registry.

---

## Limitations

- **Lexical retrieval fails in lexical ways.** "best hiking boots for wet
  granite" routes to software engineering, because `boots` depluralizes to
  `boot` and matches Spring Boot. There is no semantic understanding here.
- **No embeddings, no synonyms, no spelling correction.** A query that shares
  no vocabulary with a resource will not find it.
- **Thin metadata ranks poorly.** Techniques have no description and no path;
  agents and personas have no category and no tags. They are findable by title
  and name, and little else.
- **The regression set is not an evaluation.** `tests/data/search_routing_regression.v1.json`
  is an internal tuning and regression corpus whose labels were authored by the
  same process that selected the algorithm. It catches regressions. It is not
  evidence of general search quality.
- **Router thresholds are provisional**, as stated above.

---

## Python API

```python
from pae_engine import Registry, Repository, Router, SearchEngine

registry = Repository.discover().registry()
search = SearchEngine(registry, include_deprecated=False, include_tombstones=False)

results = search.search("android security audit", kinds=["skill"], limit=5)
for hit in results:
    print(hit.rank, hit.id, hit.score, hit.matched_fields)

decision = Router(search).route("my model drifted in production")
if decision.status == "matched":
    print(decision.selected_scope, decision.selected_kind)
else:
    print(decision.status, [c.name for c in decision.candidate_scopes])
```

`SearchHit.uid` is the durable identity. Hits deliberately carry **no source
path**: a path is a location, not a name, and a later phase resolves bodies
through `Registry.content(hit.uid)`.

Every model owns `to_json_obj()`, so an MCP server serializes without importing
the CLI.

---

## Diagnostics

```bash
PYTHONPATH=src python3 tests/run_search_routing_diagnostics.py --repo .. --compare
```

Reports search and routing metrics broken out by case class, and with
`--compare` re-scores the two rejected ranking baselines through the same index
and tokenizer. Development tooling; not part of the installed package.
