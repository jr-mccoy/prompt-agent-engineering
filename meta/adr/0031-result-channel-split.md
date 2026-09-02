# ADR-0031 — Model text and a body-free structured audit; bodies cross once

## Status

Accepted. Implemented in Phase 6 (`pae_engine.mcp.results`).

## Context

An MCP tool result carries two things: `content`, which the model reads, and
`structured_content`, which the application reads. They are for different
readers, and PAE bundles are large — a routine bundle is tens of kilobytes of
resource bodies.

The Phase 6A prototype measured what happens when that distinction is ignored.
Returning a typed object and letting the SDK convert it produced, for one 8k
bundle:

| | model-facing | structured | total |
|---|---:|---:|---:|
| auto-converted typed return | 15,964 B | 15,514 B | **31,478 B** |
| explicit two-channel result | 14,958 B | 3,004 B | **17,962 B** |

The auto-converted form put the *same* 12,557-character body in both channels.
Worse, the model-facing half became raw JSON — so
`ContextBundle.render_markdown()` never reached the model at all, and with it
went the authority framing Phase 5 exists to deliver. That is a correctness
failure, not a size problem.

## Decision

**A body crosses the wire exactly once, in the text channel.**

**`compose_bundle` text is exactly `render_markdown()`**, byte for byte, with
nothing prepended. The canonical renderer already carries its framing, and Phase
5 defined those bytes ([ADR-0027](0027-structured-bundle-and-deterministic-render.md)).

**Its structured output is an adapter-only audit projection**: `to_json_obj()`
minus `included[*].content`. Everything else survives — bundle hash, route
provenance, per-item checksums and byte lengths, the full omission list with
reason codes, the budget report, ordering, warnings. Each body stays verifiable
against the Markdown through its `content_sha256`, so an auditor loses nothing
and the wire loses a duplicate of every byte the model already has.

The projection lives in the adapter. `ContextBundle` is **not** changed for
transport convenience, and is not mutated.

**`get_resource` returns a body only in text**, with a short deterministic
framing block above it and boundary markers derived from the body's own
checksum. The body itself is verbatim: no truncation, no normalization, no
frontmatter stripping. `Content.to_json_obj()` is deliberately unused, because it
embeds the decoded text. Structured output carries metadata and the means to
verify — `byte_length`, `content_sha256`, `verified`, `serving_policy`,
`guard_preservation` — and never the body.

The framing states provenance and what the text does not outrank. **It does not
claim immunity to prompt injection**, because that would be a promise nobody can
keep.

**Search and route are body-free in both channels**, which is free: Phase 4
already forbids them from calling `Registry.content()`.

**Text is always independently sufficient.** A client negotiating an older
protocol revision may not receive structured output at all, so every tool's text
stands alone — ranked lists carry rank, id, title, kind, scope and score; route
text carries status, selection or ambiguity, coverage and margin.

**`_meta` is unused in Phase 6.** Everything contractual is in
`structured_content`, where it is schema'd; `_meta` is a weaker side channel and
explicitly not secret storage.

## Consequences

A 32k bundle costs 137,925 wire bytes instead of roughly double that, and the
model receives Markdown rather than JSON.

Tests assert the invariant directly with a distinctive body marker: for
`get_resource` and for every bundle, the marker must be absent from structured
output.

The audit projection is a second shape to maintain alongside `to_json_obj()`. It
is one dictionary comprehension, and the alternative — changing the core bundle
so transport is cheaper — would let a wire concern reach into the artifact.
