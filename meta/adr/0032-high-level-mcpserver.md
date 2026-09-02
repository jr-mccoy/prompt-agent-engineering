# ADR-0032 — High-level `MCPServer` with explicit `CallToolResult`

## Status

Accepted. Implemented in Phase 6 (`pae_engine.mcp.tools`, `pae_engine.mcp.server`).

## Context

The official SDK offers two server APIs, and the intuitive reading is that the
low-level `Server` gives more control: you write the JSON Schema yourself and
build the result yourself, while the high-level `MCPServer` derives schemas from
type hints and converts return values for you.

That reading is wrong, and Phase 6A measured why. This ADR records the evidence
so a future contributor does not "upgrade" to the low-level server believing it
is stricter.

## Decision

**High-level `MCPServer`, with `Annotated`/`Field` parameter bounds, and every
handler returning an explicit `CallToolResult`.**

Three candidates were prototyped against the live registry and driven through
the official in-memory client.

**Auto-conversion is disqualified on correctness.** Returning a typed object let
the SDK serialize it into *both* channels — 31,478 wire bytes against 17,962 —
and replaced the model-facing Markdown with raw JSON, discarding the bundle's
authority framing entirely. See [ADR-0031](0031-result-channel-split.md).

**Explicit results are passed through unchanged.** `func_metadata.convert_result`
returns a `CallToolResult` as-is, so the high-level API gives full control of
both channels. The handoff document assumed otherwise; it is worth knowing that
the two APIs produce **byte-identical wire output** once results are explicit.

**So the choice turns on validation, and there the low-level server loses:**

| behaviour | high-level | low-level (naive handler) |
|---|---|---|
| missing required argument | recoverable tool error, readable message | **`-32603 Internal server error` + traceback** |
| wrong argument type | recoverable tool error | passed through; core reports a *wrong* error |
| `minLength` / `maximum` / `enum` | advertised **and enforced** | **advertised, not enforced** |

The low-level server's "exact schema control" is advertising without
enforcement. It publishes constraints it does not honour, which is worse than
not publishing them: a client that trusts the advertised schema is misled, and a
malformed call becomes a generic internal error the model cannot act on. Making
it correct would mean hand-writing a JSON Schema validator — reimplementing,
with PAE's own bugs, what the high-level path already does.

With `Annotated[str, Field(...)]` the high-level path both advertises and
enforces PAE's real bounds; all six malformed-input cases are rejected as
recoverable tool errors.

**Bounds are imported from the Engine, never retyped.** `MAX_QUERY_CHARS`,
`MAX_LIMIT`, `MAX_ROUTE_LIMIT`, `MAX_BUNDLE_BYTES`, `MAX_MAX_RESOURCES` come from
the core, and the catalog snapshot asserts the advertised numbers equal them. A
duplicated literal would drift the day someone tuned a core limit, and the
advertised contract would start lying with nothing failing. (The Phase 6A scratch
prototype used `maxLength: 400`; the real constant is 2000. Exactly the drift the
test now prevents.)

**Handlers stay synchronous.** The SDK dispatches them onto a thread pool; a
second `asyncio.to_thread` layer would add nothing.

**That thread pool required one new guard.** Eight concurrent cold calls built
the lexical index **eight times** — ~11.7 s instead of ~1.2 s. The fix is a
background warmup started once the server is listening, plus a double-checked
lock around the first build. Measured: 11,691 ms and 8 builds becomes 17 ms and
1 build. The guard is adapter-local, so the core stays single-threaded by
construction as Phases 2-5 designed it.

## Consequences

Handlers are short and the schemas are honest. The catalog is deterministic
across constructions and snapshot-tested, because clients cache `tools/list`.

One genuine limitation: the high-level path does not advertise
`additionalProperties: false`, so unknown properties are ignored rather than
rejected. The low-level path advertises it and ignores them too, so nothing is
lost by choosing high-level. A test asserts that unknown properties — including
a `repo` key — cannot influence a handler or the repository binding.

Migrating to the low-level server later is contained: both paths already produce
the same `CallToolResult`, so it would mean replacing tool registration and
adding a validator, leaving handler bodies and projections untouched.
