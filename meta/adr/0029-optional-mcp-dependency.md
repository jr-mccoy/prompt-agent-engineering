# ADR-0029 — Optional MCP dependency, and what "zero dependencies" now means

## Status

Accepted. Implemented in Phase 6. Refines, and does not supersede,
[ADR-0003](0003-dependency-light-core.md).

## Context

[ADR-0003](0003-dependency-light-core.md) committed the Engine to the standard
library so it installs and runs offline, air-gapped, and inside locked-down CI.
CI enforced it with a blunt and effective assertion: `Requires-Dist` must be
empty.

MCP cannot be served that way. The official Python SDK is Tier 1, tracks a
protocol that moved substantially in its 2026-07-28 revision, and brings ~29
packages — including a full HTTP server stack and a JWT/crypto chain that stdio
never touches. Hand-rolling JSON-RPC, framing, negotiation and the `_meta`
envelope to avoid that would mean owning protocol conformance and its security
patches forever, which is a far worse trade than a dependency.

But declaring an optional extra emits conditional metadata:

```
Provides-Extra: mcp
Requires-Dist: mcp<3,>=2.1.1; extra == "mcp"
```

so the literal assertion "`Requires-Dist` must be empty" can no longer hold —
even though the property it was protecting is completely intact.

## Decision

**The guarantee is restated precisely, not weakened:**

> The base install has zero *unconditional* runtime dependencies. The only
> permitted conditional requirement is the MCP SDK, gated by `extra == "mcp"`.

`pip install prompt-agent-engineering` still resolves to nothing but the
standard library. CI asserts exactly that, and additionally rejects any
unconditional `Requires-Dist` and any conditional requirement that is not the
MCP extra. **No future extra may become a base dependency.**

**One distribution, not two.** A separate `pae-mcp` package would buy isolation
the extra already provides, at the cost of a second release cadence and a
cross-version compatibility matrix.

**Constraint `mcp>=2.1.1,<3`.** The floor is the release actually exercised in
CI — claiming support for 2.0.0 without testing it would be claiming something
untested, the same reasoning that already puts Python 3.10 in the matrix. The
ceiling is `<3` because v2 was itself a breaking major. Not an exact pin: a hard
pin in a library forces resolver conflicts on anyone who also depends on `mcp`.
Pinning belongs in CI, which tests both the floor and the newest compatible
release.

**`mcp[cli]` is never a PAE dependency.** It exists for the MCP Inspector and is
a developer's own install.

**Nothing imports the SDK unless the server runs.** The `mcp` subcommand is
registered without importing it, so `pae mcp --help` works on a base install;
`pae_engine.mcp` itself is SDK-free so it can report a missing extra. Absence is
distinguished from breakage: a missing top-level `mcp` is `MissingExtra` (exit
2, with the install command); a missing *transitive* dependency is re-raised as
the real runtime fault it is, because telling someone to install a package they
already have sends them in a circle.

## Consequences

The zero-dependency claim survives where it matters and must now be *stated*
carefully. Documentation says "zero unconditional dependencies", not "no
`Requires-Dist`", and discloses what the extra costs.

The CI assertion became more specific rather than looser: it now checks the
shape of every requirement, not just the count.

An air-gapped or locked-down user is unaffected. A user who wants MCP accepts a
~68 MB dependency graph, and is told so before they install it.
