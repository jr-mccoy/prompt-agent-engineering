# ADR-0010 — Identity is an immutable UID plus a mutable public ID

## Status

Accepted. Implemented in Phase 2.

## Context

The registry needs identity that survives being used: referenced from other
resources, from a CLI, from a future MCP server, and from documents outside this
repository. Identity is therefore public API, and changing it later is expensive.

Two models were compared against this corpus in the Phase 2A design checkpoint.

**A single persisted human-readable ID** works today. Simulated across all 5,226
first-class resources, a full-path scheme (`kind:scope/mid-path/slug`) produced
zero exact collisions, zero case-folding collisions, zero normalization merges and
zero malformed identifiers. A naive `kind:scope/slug` scheme, by contrast, produced
13 collision groups covering 27 resources — twelve of them from `commands/other/`
re-filing duplicates of categorized commands, and one three-way group from the
parallel learner guide tracks.

The problem with a single ID is not collisions; it is drift. `meta/REORG_MAP.tsv`
records 236 identity-preserving moves and 51 semantic replacements from a *single*
reorganization, and `CLAUDE.md` documents domain mis-filing as the recurring defect
its routing rules exist to prevent. Movement will continue. Under a single-ID
scheme, a prompt that moves from `domain-engineering-workflows/` to
`domain-business-strategy/` keeps `prompt:engineering-workflows/…` forever — a name
that asserts something untrue about the resource.

That is the same class of defect Phase 1 was spent removing, when the index stopped
claiming that a mixed artifact population was a prompt count. Reintroducing it at
5,000× scale, in a public identifier, would be a poor trade.

A UUID solves durability and destroys ergonomics: `urn:uuid:6f9619ff-…` cannot be
typed, read in a diff, or remembered. The durability requirement is only "never
changes, never collides", which 60 bits satisfies for this corpus with collision
probability around 1.4 × 10⁻¹¹.

## Decision

Every resource carries two identifiers.

**`uid`** — immutable internal key, `pae_` plus 12 Crockford base32 characters,
seeded deterministically at birth from `sha256(kind + NUL + birth_path)` truncated
to 60 bits. Crockford excludes `I`, `L`, `O` and `U`, so a UID cannot be misread
into a different UID. The seed depends only on kind and birth path — never on
title, frontmatter or content — so editing a resource can never move its identity.
Determinism makes pre-freeze dry runs reproducible; after the freeze commit,
`meta/registry/identity.tsv` is authoritative and the UID is never recomputed.

**`id`** — human-readable public handle, `kind:scope/mid-path/slug`, derived from the
current path with structural container segments (`skills/`, `agents/`, `commands/`,
`personas/`) removed. It may change when a resource moves to a new semantic home.
The retired value is written to `aliases.tsv`, stays permanently resolvable, and is
never reused by any resource.

Techniques namespace their existing catalog identifier directly — `technique:ST-01` —
rather than deriving a second slug.

Any collision, in any class, is a hard generation failure. No suffix is appended
silently.

## Consequences

- A rename becomes routine instead of breaking: the UID absorbs durability, the
  public ID absorbs meaning, and the two stop competing.
- Relationship edges are stored by UID, so they survive renames.
- The cost is one extra column in the ledger, one alias file, and the discipline of
  registering a retired ID whenever a public ID changes. CI enforces the last part.
- Consumers that want a stable key use `uid`; humans and CLIs use `id`.
