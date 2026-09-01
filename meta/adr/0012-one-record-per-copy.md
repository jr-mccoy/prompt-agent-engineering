# ADR-0012 — One registry record per physical copy, and copy edges require explicit evidence

## Status

Accepted. Implemented in Phase 2. **Search behaviour amended in Phase 4** —
see [Amendment: canonical-cluster deduplication](#amendment-phase-4--canonical-cluster-deduplication)
at the end of this record. The identity decision is unchanged.

## Context

Several directories are self-contained by design and carry copies of prompts, skills
and agents that also live in a canonical home. `meta/VENDORED.tsv` registers 154 such
pairs; 59 of them have a first-class resource on both sides.

Two representations were possible: give every physical copy its own record with a
`copy_of` edge, or model one logical resource owning several physical instances.

Measurement settles it. Of the 59 registry-visible pairs, **22 are adapted and
genuinely differ from their canonical** — `check_vendored_copies.py` explicitly
*expects* a copy to differ in relative links and in its `category:` frontmatter,
because re-pointed links are what make a bundle self-contained. A single logical
resource cannot have two different bodies, two different checksums, or two different
link graphs. The one-logical-resource model would have to misrepresent at least 22
resources on the day it shipped.

The separate temptation is to detect copies by content hash. That is also
measurably wrong here. Among registry candidates there are 37 byte-identical content
groups, and **all 37 are already explained by an explicit `VENDORED.tsv` edge — zero
unexplained**. Meanwhile 78 Markdown files sit in deliberately adapted, deliberately
*unregistered* trees that `VENDORED.tsv` documents as not-mirrors:
`portable-prompt-system/guides/`, `agentic-system-factory/templates/`,
`agentic-system-factory/samples/` and `childrens-book-studio/design-bundle/agents/`.
The last of those contains a `nonfiction-accuracy-checker.md` that a similarity
heuristic would happily merge with the studio's shipped agent of a similar name, and
which is a different artifact.

So hashing offers no benefit the explicit registry does not already provide, and
carries a real risk of collapsing two distinct resources into one identity.

## Decision

Every physical first-class copy gets its own record, its own UID, its own checksum
and a `copy_of` edge to its canonical. The canonical carries the reverse `copies`
list.

Copy relations are established **only** from `meta/VENDORED.tsv`. They are never
inferred from content similarity, hash equality, or filename resemblance.

Search-layer de-duplication is a query concern — hide `copy_of != null` by default —
not an identity concern.

## Consequences

- 59 copy edges are recorded; adapted copies keep their own content hash and their
  own re-pointed links, truthfully.
- A user can address the specific copy a self-contained toolkit ships, which is
  usually the one they actually want.
- Registering a new copy is a `VENDORED.tsv` edit, which
  `check_vendored_copies.py` already validates for drift.

---

## Amendment (Phase 4) — canonical-cluster deduplication

The sentence above — "Search-layer de-duplication is a query concern — hide
`copy_of != null` by default" — was written before search existed. Phase 4
implemented search and measured the alternatives; the default is now
**canonical-cluster deduplication** rather than hiding copies.

### What changed

A registered canonical and its copies form one cluster, keyed on the
canonical's UID. Search scores every eligible physical member and returns
**one** result per cluster: the highest-scoring member, tie-broken by public
ID. `--include-copies` returns the physical members separately. Every hit
carries `canonical_uid` and `copy_uids`, so the suppression is visible rather
than silent.

### Why the earlier default was wrong

Retrieval metrics do not decide this. Over 120 labelled cases, hide-copies,
include-everything and cluster deduplication landed within 1.5 points of each
other — one query — and under the shipped uniform-weight ranker, cluster
deduplication and no deduplication scored **identically** at 77.3% top-1. The
deciding argument is the one this ADR already made two paragraphs earlier:

> A user can address the specific copy a self-contained toolkit ships, which is
> usually the one they actually want.

Hiding `copy_of != null` structurally prevents that. It can *never* return the
toolkit-local copy, however well it matches a toolkit-scoped query. Cluster
deduplication returns whichever member the query actually fits, and names the
canonical alongside it.

### What did not change

Clusters are still built **only** from explicit `copy_of` / `copies` edges
sourced from `meta/VENDORED.tsv`. They are never inferred from content hashes,
filename resemblance or path similarity — the reasoning in this record's
Context section stands unaltered, and the implementation reads registry
relationships exclusively.

One safety refinement was added: a copy whose canonical is **excluded** does
not report that canonical's UID. The cluster key is still used internally so
two copies of an excluded canonical collapse correctly, but the reported
`canonical_uid` falls back to the copy's own UID. Surfacing it would let a
caller enumerate excluded resources by collecting cluster pointers that resolve
to nothing — the disclosure path
[ADR-0015](0015-serving-policy-metadata.md) exists to close.

See [ADR-0021](0021-deterministic-lexical-search.md).
