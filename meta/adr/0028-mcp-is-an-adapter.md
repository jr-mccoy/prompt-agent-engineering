# ADR-0028 — MCP is an adapter, not a second Engine

## Status

Accepted. Implemented in Phase 6 (`pae_engine.mcp`).

## Context

An MCP server is the first surface that lets a model call the Engine directly.
That creates an obvious temptation: the protocol wants tools, tools want
convenient behaviour, and convenient behaviour is easy to add inside a handler.
A tool that "just" re-ranked results, or "just" checked whether a body could be
served before asking, would be a second implementation of a decision the core
already makes — and the day the two disagreed, the disagreement would be
invisible.

The corpus makes the stakes concrete. Serving policy, checksum verification and
the excluded/nonexistent distinction are not conveniences; they are the
guarantees the Registry exists to provide.

## Decision

**Every tool does exactly four things**: validate transport input, call one
existing Engine API, project the result, map errors. Nothing in
`pae_engine/mcp/` ranks, routes, packs, or decides what may be served.

**Four tools, fixed**: `pae_search_resources`, `pae_route_task`,
`pae_get_resource`, `pae_compose_bundle`. No `registry_stats`, no
`validate_registry`, no reload. Operator questions are answered by the CLI,
which is where an operator already is; a model routing a task does not benefit
from knowing how many deprecated records exist.

**Bodies arrive only through `Registry.content()`** ([ADR-0024](0024-bodies-only-through-registry-content.md)).
The adapter opens no file, follows no link, reads no attachment, and performs no
policy check of its own.

**The repository is startup configuration, never model-controlled input.** No
tool accepts a `repo`, `root`, `path`, `file`, `cwd`, `directory` or `checkout`
argument, and a test enumerates the tool schemas to prove it. Resource identity
is a UID or public ID; a filesystem location is not a name.

**One process is one snapshot.** No watcher, no reload, no cache file, no
repository-switching tool. Restarting is the way to observe a changed checkout.

**The core does not learn that MCP exists.** `repository.py`, `registry.py`,
`search.py`, `routing.py`, `context.py` and `models.py` import no adapter code
and no third-party package, and `pae_engine/__init__.py` never imports the
adapter. Asserted by an AST scan.

## Consequences

The adapter is small and boring, which is the point: a reviewer can check that a
handler calls the API it claims to and stop there.

Behaviour is identical across surfaces by construction. A bundle composed over
MCP is byte-identical to one composed by `pae bundle`, because both call
`ContextCompiler` and render through the same function.

The concurrency guard is the one piece of genuinely new machinery, and it is
deliberately adapter-local — see [ADR-0032](0032-high-level-mcpserver.md). If a
second concurrent consumer ever appears, moving it into `SearchEngine` is a
contained change.

Adding a fifth tool is a product decision, not a refactor. The catalog is
snapshot-tested because clients cache it.
