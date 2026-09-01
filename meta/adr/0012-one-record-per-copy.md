# ADR-0012 — One registry record per physical copy, and copy edges require explicit evidence

## Status

Accepted. Implemented in Phase 2.

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
