# ADR-0003 — Engine core is dependency-light and offline-capable

## Status

Accepted. The core layer is implemented in Phase 3, tightened as recorded in
the amendment below. The optional extras remain unimplemented.

## Context

The repository is deliberately frugal about dependencies. `requirements-ci.txt`
contains PyYAML and nothing else; `continuity-kit` declares zero runtime
dependencies by design and puts its MCP server behind an optional extra; the
agentic-system-factory gate scripts are standard-library only so they can be
trusted as "code, not prose".

A search-and-routing engine invites the opposite: an LLM SDK, a vector database,
an embedding service, a tokenizer. Each of those makes the tool unusable
offline, unusable in a locked-down environment, and slower to install for people
who only want deterministic search.

## Decision

Layer the dependencies.

**Core** — standard library plus PyYAML (needed because repository metadata is
YAML frontmatter). The core must run offline and must not require a network
call, an API key, or a model. Catalog loading, identity resolution, metadata
filtering, structural validation, and checksums are all deterministic work that
needs no model.

**Optional extras**, added when the capability is actually implemented, along
the lines of `[mcp]`, `[eval]`, `[tokenizers]`, `[dev]`. Exact names and pinned
packages are chosen at implementation time.

**MCP** ships as an optional extra, following `continuity-kit`'s precedent: the
entry point is always installed but prints install guidance and exits non-zero
if the extra is absent, and never imports the SDK at module load.

**Model-provider SDKs**, if reproducible model-dependent evaluation ever needs
them, belong in an evaluation extra — never in the core runtime.

## Consequences

- `pip install prompt-agent-engineering` stays small and fast, and works in
  air-gapped environments.
- Anyone wanting MCP or evaluation opts in explicitly and can see what they are
  taking on.
- Ranked retrieval must be designed to work without embeddings. If semantic
  retrieval is later added, it is an extra, and the deterministic path remains
  the default.

## Amendment (Phase 3) — the installed core is standard library only

The original decision put PyYAML in the core, because repository metadata is
YAML frontmatter. Phase 2 removed the need: the registry normalizes every
source schema into JSONL, so the Engine reads JSON and never sees frontmatter.

The installed core is therefore **standard library only**:

```toml
dependencies = []
```

PyYAML remains a *repository-maintenance* dependency — `requirements-ci.txt`,
`scripts/pae_registry/` and the generators still need it — but it is not an
Engine dependency and is never installed by `pip install
prompt-agent-engineering`.

CI asserts this rather than trusting it: after installing the built wheel into
a clean virtual environment, the workflow fails if `Requires-Dist` is non-empty
or if anything beyond pip/setuptools/wheel appears in the environment.

The layering above is otherwise unchanged. Extras (`[mcp]`, `[eval]`,
`[tokenizers]`, `[dev]`) are still the mechanism for anything heavier, and none
of them exists yet.
