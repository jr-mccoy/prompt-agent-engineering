# ADR-0024 — Bundled bodies come only from `Registry.content()`, whole, with no expansion

## Status

Accepted. Implemented in Phase 5 (`pae_engine.context`).

## Context

The context compiler assembles resource bodies for a model to read. That makes
it the first component with a motive to read a file: it wants text, and the
text is sitting on disk behind a path the registry record already names.

Three tempting shortcuts were all rejected on measurement.

**Reading a source path directly** would bypass serving policy and checksum
verification in a single step. [ADR-0019](0019-runtime-serving-and-integrity.md)
put both behind `Registry.content()`; a second reader would mean a second
policy implementation, and the two would drift.

**Expanding skill attachments.** 230 of 339 skills carry attachments — 1,021
entries in total, median 2 per skill and up to 82. Against a median `SKILL.md`
body of ~2,500 estimated tokens, the attachment payload runs a median 1.72×,
p90 6.13× and a maximum of **93.5×**: one skill has a 1,743-token body and
162,966 tokens of attachments, five times the largest budget the compiler is
expected to serve. Worse, `relationships.attachments` holds bare path strings
with no per-file checksum — only a directory-level `bundle_sha256` — so an
attachment cannot be integrity-verified individually, and 159 of the entries
are `.py` or `.sh` files the Engine must never execute.

**Serving technique bodies.** All 336 technique records have no `source_path`;
they share one `defined_in`, `techniques/MASTER_TECHNIQUE_INDEX.md`, at 356 KB.
Their entries are fragment-shaped and cheap (median ~227 estimated tokens), but
locating them means parsing that catalog, and the repository already has one
canonical parser encoding semantics a naive reader gets wrong — code-fence
stripping, `###`/`####` headings, `**ID:**` bold definitions, the tombstone
test, ID reuse, `(also XX-NN)` aliases. A deliberately naive heading scan
resolves 298 of 336 records and produces two non-unique IDs.

**Relationship expansion** was rejected for lack of room rather than lack of
appeal: rank-greedy packing fits a mean of 2.72 resources at an 8k budget, so
every expanded neighbour displaces a directly-ranked hit. Techniques have no
bodies, and `copy_of`/`copies` edges are duplicates by construction — expanding
them would add the same text twice.

## Decision

Every bundled body comes from `Registry.content(uid)` and nothing else. The
compiler never opens a path, reads an attachment, follows a Markdown link, or
imports repository-maintenance tooling; a source-level test asserts the absence
of `open`, `read_text`, `read_bytes`, `Path`, `glob` and `source_path` from
`context.py` and `_context_render.py`.

Bodies are served **whole or not at all**, for `standard` and `safety_gated`
alike. Phase 5 ships no truncation, excerpt, heading-subset or summarization
path, and no frontmatter stripping. A body that does not fit becomes an
`OmittedItem` and packing continues.

Non-body resources degrade to closed omission reasons in ranked modes —
`metadata_only`, `tombstone`, `no_addressable_body`, `excluded` — and raise for
explicit references, because a caller who named a resource by hand is asking a
different question than a ranking that merely suggested one. An excluded
resource contributes policy-permitted identity only, never a title, even one a
search hit already disclosed.

Integrity failures — checksum mismatch, path security, unreadable source,
undecodable bytes — abort the whole compile. They are never downgraded to
omissions: a registry that disagrees with disk cannot produce a trustworthy
bundle.

## Consequences

The compiler cannot serve a technique body or a skill attachment, and says so
in a machine-readable reason code rather than silently returning less. Both
capabilities are deferred to a **generator-side** extension, specified in
[ADR-0027](0027-structured-bundle-and-deterministic-render.md#deferred) and
sketched in `pae-engine/docs/context-compiler.md`: technique fragments need
`{path, start/end locator, fragment_sha256}` emitted by the existing canonical
parser, and attachment serving needs `{path, sha256, bytes, media_type, role}`
plus a checksum-and-path-safe accessor. Neither requires a registry v2; both
are additive optional fields on `pae-registry-record/1`.

Truncation is not merely discouraged, it is structurally absent — matching
`Content`, which has no partial variant, and honouring the
`guard_preservation.must_not_truncate` flag that all 1,319 safety-gated records
already carry.
