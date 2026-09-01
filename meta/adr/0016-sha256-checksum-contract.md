# ADR-0016 — Checksums are SHA-256 over a clearly defined payload

## Status

Accepted. Implemented in Phase 2.

## Context

`generate_prompt_index.py` hashes files with MD5 to detect byte-identical copies in
self-contained domains. That is fine for an internal dedup heuristic and wrong as a
public registry contract: MD5 is not collision-resistant, and a registry checksum is
something external consumers may rely on for integrity.

A checksum also needs a stated payload. "The hash of the resource" is ambiguous for a
skill, which is a directory containing a manifest plus references, scripts and
assets.

## Decision

SHA-256 everywhere in the registry, written with an explicit algorithm prefix
(`sha256:<hex>`) so the field can carry a different algorithm later without
ambiguity.

`content_sha256` is taken over the **raw bytes of the primary source file** — the
`SKILL.md` for a skill — and the record states this as
`checksum_payload: raw_source_bytes`. Raw bytes rather than normalized text: the
checksum's job is integrity and change detection, and normalizing would hide a real
edit.

Bundled resources additionally carry `bundle_sha256` and `bundle_file_count`, taken
over a deterministic manifest of `relative_path<TAB>sha256` lines for every file in
the bundle, sorted. The attachment list is derived from the same walk, so the digest
and the attachment list can never describe different sets of files.

The MD5 helper in the index generator is untouched; it remains an internal detail of
that script and is not part of any registry contract.

## Consequences

- Registry integrity metadata is cryptographically sound and self-describing.
- A skill's identity covers its whole bundle, so an edit to a bundled reference
  changes `bundle_sha256` while leaving `content_sha256` alone — the two answer
  different questions.
- Checksums are stable across platforms, so they participate in the byte-identical
  regeneration guarantee.
