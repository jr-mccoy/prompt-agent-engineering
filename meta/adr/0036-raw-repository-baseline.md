# ADR-0036 — The raw-repository baseline is ripgrep, list and read

## Status

Accepted. Implemented in Phase 7.

## Context

Condition B carries the primary comparison, so its design decides whether the
headline means anything. A baseline that is too weak manufactures a win; one
that cannot be standardized makes the run unreproducible.

Four options were considered: filename listing plus exact or regex search; a
ripgrep-backed toolset; a generic BM25 index over the raw files; and shell
access.

## Decision

Three read-only tools: `repo_search` (ripgrep), `repo_list`, `repo_read`.

- **Ripgrep**, because that is what a real coding agent actually has. Choosing
  it is what makes the baseline honest rather than convenient.
- **Not generic BM25.** Building a retrieval system for the baseline converts
  the claim from "PAE versus generic access" into "PAE versus our BM25", and we
  would be tuning the competitor.
- **Not shell.** Impossible to standardize across machines, unbounded, and a
  security surface that would take longer to harden than the rest of the
  harness.
- **No hidden semantic index**, no PAE import, no MCP.

Limits: 200 matches, 120 characters per line, 64 KiB per search or list result,
500 paths per listing, 100 KiB per read, 2,000 lines by default. The same turn
budget, timeout and output cap as Condition D.

If `rg` is absent the condition **refuses to run**. Substituting a Python search
would silently change what the baseline is, and a sealed run would then be
comparing against something nobody chose.

Containment is enforced by resolving every path against the participant snapshot
root and requiring the result to remain inside — never by a denylist. A denylist
is a list of the attacks someone thought of, and the benchmark's gold labels are
exactly what an unlucky glob would reach. Absolute, drive-qualified, UNC,
NUL-containing, `..`-containing and escaping-symlink paths are all refused.

Each escape shape is tested textually as well as by resolution, because the
dangerous forms are platform-dependent: a drive-qualified path is absolute on
Windows and an ordinary relative path on POSIX, so a check that only calls
`Path.is_absolute()` passes on Linux while leaving the hole open.

## Consequences

- The baseline is defensible to a sceptical reader, which is the entire point.
- CI must provision ripgrep, and one integration test drives the real binary
  rather than a stub.
- Reading `meta/registry/registry.jsonl` is permitted — a generic agent could —
  and every byte is charged to B's token budget. That is an honest finding about
  what generic access costs, not a loophole.
