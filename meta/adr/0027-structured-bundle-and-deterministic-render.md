# ADR-0027 — The structured bundle is the artifact; Markdown is the budgeted rendering

## Status

Accepted. Implemented in Phase 5 (`pae_engine.context`, `pae_engine._context_render`).

## Context

A bundle has two audiences that want different things. A model needs prose it
can read. A future evaluation, a reviewer, or an MCP server needs to know which
resources were candidates, which were included, what was left out and why, and
whether the whole thing can be reproduced.

Serving one shape to both would mean either an audit trail a model has to wade
through, or a rendering an auditor has to parse.

## Decision

**The structured `ContextBundle` is authoritative**, and it owns both
serializations: `to_json_obj()` and `render_markdown()`. The CLI selects
between them and formats nothing itself, so a future MCP server
([ADR-0023](0023-executable-routing-migration.md) sequencing) reaches the same
bytes without importing a line of CLI code. The bundle schema,
`pae-context-bundle/1`, is versioned independently of the registry record
contract and of the Engine.

**Markdown is the budgeted artifact**, always, even when the CLI emits JSON.
It is what a model actually receives, so identical candidates and options
select identical resources regardless of how the caller asked for the output.
JSON is transport and audit; it carries bodies exactly once and never embeds
the Markdown, which would double the payload and create a second divergeable
description of the same bundle.

**The rendering states requested budget, never used budget.** A figure that
changes the document it appears in cannot be measured into a stable fixed
point, so the rendering carries the requested limits, the byte ceiling and the
counter's identity and exactness — all known before measuring — while used and
remaining figures live only in `BudgetReport`.

**Bodies are emitted verbatim, delimited from the outside.** Frontmatter is
retained; nothing is rewritten, re-wrapped or re-indented. Instruction-bearing
resources are not wrapped in code fences — that would change how a consumer
reads them — but delimited by HTML comment markers whose identity derives from
the resource UID and its source checksum. If a body contains its own marker the
pair is extended deterministically (`n=2`, `n=3`, …) until unique; the body is
never altered to escape it.

**Authority framing is stated once, at bundle level, outside every body**: the
resources are retrieved project content that may carry task instructions but do
not override the host's system or developer policy, tool permissions, or the
user's current request. Nothing is injected into a body, which would break
checksum verifiability. The framing reduces ambiguity about provenance; it is
not a security control and the documentation does not claim it prevents prompt
injection.

**`bundle_sha256` is reproducible.** It is SHA-256 over a canonical JSON
manifest — sorted keys, tight separators, `ensure_ascii=False` — covering the
bundle and renderer versions, the registry contracts, source mode, task, route
provenance, candidate UID order, filters, ordering mode, included metadata with
each body's `content_sha256` and byte length, omitted identities with reasons,
budget configuration, counter identity, and warnings. It excludes timestamps,
absolute paths, process IDs, randomness, the hash itself, and raw bodies.
Bodies enter through their checksums, so an edited source changes the identity —
and would in any case fail verification first.

The Markdown carries no timestamp and no absolute path, so the same bundle
renders byte-identically in any checkout on any machine. Tests assert that two
fresh compilers agree on inclusions, omissions, budget report, hash, Markdown
bytes and JSON bytes, and that relocating the checkout does not move the hash.

**Runtime writes nothing.** `pae bundle` emits to stdout only. There is no
`--output`, no `--save`, no cache and no temporary file, keeping the decision to
write where it belongs — with the caller and their shell.

## Deferred

Two capabilities are specified but deliberately not built, because each needs a
**generator-side** change rather than compiler cleverness (see
[ADR-0024](0024-bodies-only-through-registry-content.md)):

- **Technique fragments** — add `{path, start/end locator, fragment_sha256}` to
  technique records, computed by the existing canonical catalog parser, then
  serve them through `Registry`. Backward compatible; identity unchanged.
- **Verified attachments** — promote `relationships.attachments` from bare path
  strings to `{path, sha256, bytes, media_type, role}` and add a
  checksum-and-path-safe accessor.

Both are additive optional fields on `pae-registry-record/1`. Neither blocked
Phase 5.

## Consequences

A later evaluation can compare raw corpus, search-selected resources and
compiled bundle, because the structured artifact preserves candidate
identities, inclusion order, omission reasons, source checksums, budget and
estimator identity, and full route/search provenance — and `bundle_sha256`
makes any run citable.
