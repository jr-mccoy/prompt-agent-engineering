# ADR-0006 — Routing migration is staged; `CLAUDE.md` is the interim canonical router

## Status

Accepted. Stage 1 implemented.

## Context

Before this decision the repository maintained three routing surfaces by hand:

- `CLAUDE.md` (~3,100 lines) — the real, detailed router;
- `AGENTS.md` — a 64-line summary that had drifted, including a mapping that sent
  "professional communication" to the wrong domain;
- `START_HERE_FOR_AI.md` — a third routing table plus a folder inventory whose
  per-directory counts were wrong in nearly every row.

They disagreed with each other and with the repository. The product answer is
executable routing (`pae route`), but that command does not exist, and pointing
documentation at a nonexistent command would be worse than the drift.

## Decision

Migrate in two stages.

**Stage 1 (now).** `CLAUDE.md` is the single canonical human-readable routing
reference. `AGENTS.md` and `START_HERE_FOR_AI.md` become thin bootstraps that
point at it and keep no routing table of their own. Their stale counts are
replaced by a generated block (see
[ADR-0008](0008-generated-counts-control-plane.md)). The deep routing knowledge
in `CLAUDE.md` is preserved in full — nothing was deleted to shrink a file; the
duplicated tables were removed because they were both redundant and wrong.

**Stage 2 (after the engine exists and has regression coverage).** `pae route`
becomes the canonical router. Client bootstrap documents shrink substantially,
keeping a minimal documented fallback for environments without the CLI. The
executable router and any generated routing documentation derive from the same
canonical metadata wherever practical.

## Consequences

- One routing surface is maintained by hand instead of three.
- The canonical routing file is, for now, named after one vendor's client, which
  sits awkwardly with the project's framework-agnostic stance. This is accepted
  as an interim cost: relocating 3,000 lines of routing prose in this phase would
  be a large, risky diff that Stage 2 will supersede anyway.
- `CLAUDE.md` remains large. The token-efficiency rules at the end of that file
  are the mitigation until Stage 2.
- No document claims executable routing exists.
