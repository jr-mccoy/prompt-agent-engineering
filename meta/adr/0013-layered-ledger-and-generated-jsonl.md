# ADR-0013 — Identity lives in reviewed ledgers; the registry is generated JSONL

## Status

Accepted. Implemented in Phase 2.

## Context

The registry holds 5,271 records. Storage shape determines whether it is
maintainable or merely correct.

A single `registry.json` would be roughly ten megabytes in one JSON blob: every
regeneration rewrites the whole file, every concurrent branch conflicts on it, and
no diff is readable. Per-resource sidecar files would mean 5,271 new files, which is
worse for both git and humans.

There is also a split of concerns. Most of a record is *derived* — recomputable from
the corpus at any time. A small part is *asserted* — identity that must survive, and
governance a human decided. Those two deserve different treatment: derived data
should be regenerable and diffable, asserted data should be small, reviewable and
guarded.

## Decision

Layer the storage.

**Reviewed and hand-maintained**: `identity.tsv` (5,271 short lines, the thing that
must survive), `aliases.tsv`, `relationships.tsv`, and `overrides/*.yaml` sharded by
kind so any file a human edits stays small.

**Generated**: `registry.jsonl` (one record per line, sorted by UID),
`registry-summary.json`, and `diagnostics.jsonl`.

JSONL sorted by a stable key means a changed resource is a one-line diff and an
added resource is a one-line insert, so git merges the registry like source code.

Generated artifacts carry **no timestamp** and must be byte-identical on repeat
generation from the same tree. CI regenerates and byte-compares, exactly as
`generate_repo_facts.py --check` already guards generated documentation blocks, so a
hand-edit of a generated file is caught rather than silently kept.

Schemas are published as real JSON Schema documents, but validated by a
standard-library subset validator: ADR-0003 keeps the core to the standard library
plus PyYAML, and an unsupported schema keyword is a hard error so the validator can
never drift behind the contract it enforces.

## Consequences

- Diffs stay reviewable at 5,000+ records.
- `identity.tsv` is small enough to audit by eye and is the single file CI freezes.
- The registry is regenerable from scratch: delete every generated artifact, run
  `--write`, and the result is byte-identical.
- Adding a schema keyword means teaching the validator about it, deliberately.
