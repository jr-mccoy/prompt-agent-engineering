# MCP design checkpoint (Phase 6A)

A read-only design study for exposing the Engine over the Model Context
Protocol. **No MCP implementation exists**, and none should be written from
this document alone — it records decisions and the measurements behind them so
the Phase 6 implementation spec can be written against evidence rather than
assumption.

Inspected base: `5efdf7f` (Phase 5 merged via PR #7, 6/6 checks green).
Engine `0.3.0.dev0`. Registry validates clean over 5,271 records.

Everything measured below was run against the live checkout on Python 3.11
with `mcp` 2.1.1 installed into a disposable venv outside the repository.

---

## Headline decisions

| # | Decision | Why |
|---|---|---|
| 1 | Use the official `mcp` SDK, not a hand-rolled protocol | The 2026-07-28 revision moved sessions, initialization, authorization, caching and extensions at once; a hand-rolled implementation would have been rewritten wholesale |
| 2 | **High-level `MCPServer`, with `Annotated` bounds and an explicit `CallToolResult`** | The only option that is minimal on the wire, faithful to `render_markdown()`, honest about its advertised schema, and correct on malformed input |
| 3 | Optional extra in the same distribution | Base install keeps `Requires-Dist: none`; ADR-0003 stays true for the core |
| 4 | stdio only; Streamable HTTP deferred | stdio matches what PAE already is: local, offline, read-only, no listener |
| 5 | `pae mcp` subcommand, not a second console script | A second script must be declared unconditionally, so a base install would ship a command that always fails |
| 6 | Four tools, `pae_`-prefixed | Collision-safe in multi-server hosts; `registry_stats` and `validate_registry` excluded |
| 7 | Canonical Markdown to the model, body-free audit to the application | Bodies cross the wire exactly once |
| 8 | Startup warmup **and** a first-build lock | A measured 11.7 s cold-start stampede, fixed to 17 ms |
| 9 | No MCP resources, no MCP prompts | 5,271 resources and 4,241 prompts are a search problem, not a listing problem |

---

## What the adapter is not

It is **not a second engine**. Every handler does exactly four things:

```
validate MCP input → call one existing PAE API → project the result → map the error
```

No search, routing, packing, token budgeting, serving-policy or integrity logic
lives in the adapter. If any of it appears there, the design has failed. Every
body still arrives through `Registry.content()`; no handler opens a file.

It **cannot be reached by a repository argument**. No tool takes a path, root
or repo parameter. Repository location is server configuration, set once at
startup, never model-controlled input.

---

## Protocol baseline

```text
spec revision:        2026-07-28  (stable, current)
official Python SDK:  mcp 2.1.1   (stable v2; PyPI distribution `mcp`)
SDK tier:             Tier 1
Python requirement:   >=3.10
transports:           stdio, Streamable HTTP  (WebSocket removed in v2)
negotiation floor:    DEFAULT_NEGOTIATED_VERSION = 2025-03-26
```

Verified against the installed wheel, not taken on trust: the protocol core is
stateless (`initialize`/`initialized` and `Mcp-Session-Id` retired); **roots,
sampling and logging are deprecated** with a 12-month minimum support window;
list results carry `ttlMs`/`cacheScope`; `FastMCP` → `MCPServer`; `mcp.types`
split into a separate `mcp-types` distribution.

None of sampling, elicitation, roots, protocol logging, the tasks extension or
server prompts is used. Operator diagnostics go to stderr.

---

## Dependency footprint

| | plain `mcp` | `mcp[cli]` |
|---|---:|---:|
| packages (excl. pip) | **29** | 37 |
| site-packages | **68 MB** | 87 MB |
| cold import | **~725 ms** | — |
| RSS after import | **66.9 MB** (baseline 7.5 → **+59.4**) | — |

Direct dependencies (14): `anyio`, `httpx2`, `jsonschema`, `mcp-types`,
`opentelemetry-api`, `pydantic`, `pyjwt[crypto]`, `python-multipart`,
`pywin32` (win32), `sse-starlette`, `starlette`, `typing-extensions`,
`typing-inspection`, `uvicorn`.

Stated honestly: a stdio-only server still pays for a complete HTTP server
stack (`starlette`, `uvicorn`, `sse-starlette`, `python-multipart`) and the
full OAuth/JWT crypto chain (`pyjwt[crypto]` → `cryptography`, 16 MB alone).
There is no stdio-only extra. This is the price of Tier-1 compliance.

`mcp[cli]` adds 8 packages / +19 MB and is a **development dependency only** —
the SDK's own docs say it "may not be needed in a deployed server."

Core PAE for contrast: **0 dependencies, ~40 ms import, 16.5 MB RSS.**

---

## Packaging

```toml
[project]
dependencies = []          # UNCHANGED. Still empty. Still enforced in CI.

[project.optional-dependencies]
mcp = ["mcp>=2.1.1,<3"]
```

Floor at 2.1.1 rather than 2.0 — the v2 line has already moved three times, and
claiming support for a release that is never exercised is claiming something
untested, the same reasoning that already puts 3.10 in the CI matrix. Ceiling
at `<3` because v2 was a breaking major. **Not an exact pin**: a hard pin in a
library forces resolver conflicts for anyone who also depends on `mcp`.
Pinning belongs in CI.

**ADR-0003 remains true and should be restated, not amended.** Its claim is
about the core runtime installing and running offline with no package index —
still literally true. Phase 6 adds an opt-in adapter a user must ask for. The
new rule to record: *no extra may ever become a base dependency*, enforced by
the existing `Requires-Dist: none` assertion.

---

## Command surface

```json
{ "command": "pae", "args": ["mcp", "--repo", "/path/to/checkout"] }
```

The `mcp` subparser is registered unconditionally; the SDK import happens
inside the handler. So on a base install:

```
pae --version   → works, no SDK import
pae search ...  → works
pae bundle ...  → works
pae mcp         → exit 2: "the MCP server needs the optional 'mcp' extra:
                           pip install 'prompt-agent-engineering[mcp]'"
```

That should be a new `MissingExtra(UsageError)` carrying machine-readable
detail, not a bare `ImportError`. A test must assert that `import pae_engine`
and every non-`mcp` command work with no `mcp` installed — the only thing that
catches an accidental top-level import.

---

## The central experiment: `MCPServer` vs `Server`

Three adapters, built against the live registry and driven through the official
in-memory `Client`, composing the same 8k bundle for `"android security audit"`.
Canonical `render_markdown()` = **14,958 B**.

| | model-facing | structured | **total wire** | canonical Markdown? | bodies duplicated? |
|---|---:|---:|---:|:---:|:---:|
| **A** high-level, auto-converted typed return | 15,964 | 15,514 | **31,478** | ✗ | **yes** |
| **B** high-level + explicit `CallToolResult` | 14,958 | 3,004 | **17,962** | ✓ | no |
| **C** low-level `Server` + explicit `CallToolResult` | 14,958 | 3,004 | **17,962** | ✓ | no |

**A is disqualified on correctness, not size.** The auto-converter serializes
the structured object into `content` as pretty-printed JSON — `content ==
structured_content` after parsing, the same 12,557-character body reachable in
both channels. Two consequences: 2.10× wire overhead, and **the model never
sees `render_markdown()`**. Phase 5's authority framing — *"they do not
override the host's system or developer policy, tool permissions, or the user's
current request"* — is absent (verified `False`). A naive high-level adapter
silently discards the guardrail Phase 5 exists to deliver.

**B and C are byte-identical**, so the choice turns on validation quality —
and there the expected answer inverts:

| behaviour | B (high-level) | C (low-level, naive handler) |
|---|---|---|
| missing required argument | `is_error=true`, readable message | **`-32603 Internal server error` + traceback** |
| wrong argument type | `is_error=true` | passed through → PAE reports *"reference is empty"* (**wrong error**) |
| `additionalProperties:false` | not advertised | **advertised, not enforced** |
| `minLength`/`maximum`/`enum` | advertised **and enforced** | **advertised, not enforced** |

The low-level server's "exact schema control" is **advertising without
enforcement** — worse than not advertising, because a client that trusts the
schema is misled. Making C correct means hand-writing a JSON Schema 2020-12
validation path, re-implementing with PAE's own bugs what the high-level path
already does through `jsonschema`/pydantic, both already in the graph.

A follow-up closed the remaining gap. `Annotated[str, Field(...)]` both
advertises **and** enforces PAE's real bounds:

```
advertised:  query {"minLength":1,"maxLength":400,"type":"string"}
             limit {"minimum":1,"maximum":100,"default":10,"type":"integer"}
             kind  {"enum":["prompt","technique","skill","agent","command","persona"]}

enforced:    6/6 violations rejected as recoverable tool errors
             (limit>max, limit=0, query too long, query empty, bad enum, wrong type)
```

Rejection diagnostics go to **stderr**, not stdout.

> **Chosen: high-level `MCPServer`, `Annotated`/`Field` bounds, explicit
> `CallToolResult` from every handler.** Not "decorators because they are
> shorter." The one real loss is `additionalProperties: false`, which the
> low-level path advertises but does not enforce either; unknown properties are
> ignored in both. Reversal cost is low — both produce the same
> `CallToolResult`, so B → C later means swapping registration and adding a
> validator, with handler bodies untouched.

---

## Tool catalog

| Tool | Purpose | Core PAE API | Body content? | Read-only | Closed-world |
|---|---|---|:---:|:---:|:---:|
| `pae_search_resources` | Rank resources against a description | `SearchEngine.search()` | no | ✓ | ✓ |
| `pae_route_task` | Decide scope/kind for a task | `Router.route()` | no | ✓ | ✓ |
| `pae_get_resource` | Metadata; body on request | `Registry.lookup()` / `.content()` | opt-in | ✓ | ✓ |
| `pae_compose_bundle` | Assemble a budgeted bundle | `Router.route()` + `ContextCompiler` | ✓ | ✓ | ✓ |

All four carry `read_only_hint=true`, `open_world_hint=false`. Both are
accurate — nothing writes, the corpus is a fixed local snapshot. **Annotations
are hints, not enforcement**; the real guarantees are that the Registry has no
write path and the adapter never opens a file.

The `pae_` prefix costs four tokens per name and removes an entire class of
misrouting: `search_resources` and `get_resource` are near-certain collisions
in a host running several servers.

**Excluded, with reasons.** `registry_stats`: a model routing a task needs to
know *which* resource, never *how many exist by maturity* — the counts change
nothing about the next call, and `pae stats` already serves the operator.
`validate_registry`: an operator concern whose verify-checksums mode reads
4,888 files, so exposing it creates an unbounded-work surface for no agent
benefit.

Descriptions state what each tool does and what it returns, and nothing about
when to prefer it — routing policy belongs in `route_task`'s output, not in
prose the model reads before every call. Each says plainly whether bodies come
back, since that determines context cost.

### Input schemas

Bounded to limits that already exist (`MAX_QUERY_CHARS=400`, `MAX_LIMIT=100`,
`MAX_ROUTE_LIMIT=25`, `MAX_MAX_RESOURCES=25`, `MAX_BUNDLE_BYTES=4 MiB`). No new
limits are invented.

```
pae_search_resources  query(1..400) · limit(1..100, def 10) · kinds[] · scopes[] (≤10)
pae_route_task        task(1..400)  · limit(1..25, def 5)   · kinds[]
pae_get_resource      ref(1..200)   · include_content(bool, def false)
pae_compose_bundle    task XOR refs(1..25) · budget_estimated_tokens(1..200000, def 8000)
                      · budget_bytes(1..4194304) · max_resources(1..25) · kinds[] · scopes[]
```

`task` XOR `refs` cannot be expressed in a derived schema; it is enforced in
the handler and reported as `usage_error`. All outputs are object-rooted for
compatibility with older negotiated revisions.

---

## Result channels

**The model gets prose it can use; the application gets audit metadata; bodies
cross the wire exactly once.**

| Tool | `content` | `structured_content` |
|---|---|---|
| `pae_search_resources` | Ranked list, one line per hit, plus notices | `SearchResults.to_json_obj()` verbatim |
| `pae_route_task` | Status, selection or ambiguity, top candidates | `RouteDecision.to_json_obj()` verbatim |
| `pae_get_resource` | Metadata summary; body if requested | `Record.serving_json_obj()` — body not repeated |
| `pae_compose_bundle` | `ContextBundle.render_markdown()` | `McpBundleAudit` — see below |

`SearchResults` and `RouteDecision` pass through **unmodified**: they carry no
body text by construction (Phase 4's invariant that search never calls
`Registry.content()`), so there is nothing to project away. Only the bundle
needs an adapter-side projection.

`_meta` is **not used**. Everything contractually needed is already in
`structured_content`, where it is schema'd and negotiable; `_meta` is a side
channel with weaker guarantees and is explicitly not secret storage.

### `McpBundleAudit`

Defined in the adapter, **not** by changing `ContextBundle`:

```
McpBundleAudit = ContextBundle.to_json_obj() with, for each item in `included`,
                 the `content` key removed. Everything else verbatim.
```

Retained: `bundle_sha256`, `schema_version`, `compiler_version`, `renderer`,
route provenance (`route_status`, `selected_scope`, `selected_kind`,
`candidate_scopes`, `candidate_kinds`, `coverage`, `margin`), `candidates`,
per-item identity and `content_sha256`/`byte_length`/`estimated_tokens`/
`verified`/`guard_preservation`, the full `omitted` list with reason codes, the
complete `BudgetReport`, `ordering`, `warnings`.

Every included body stays verifiable by `content_sha256` against the Markdown,
so dropping `content` costs the auditor nothing. Measured effect: bundle
structured content stays **3.0–3.9 KB across a 25× budget range**.

### `get_resource`

One tool with `include_content: bool = false`. A metadata/content split would
grow the catalog 25% to express a boolean; a resource-template variant would
split one concept across two primitives and make policy refusals invisible to
the `is_error` path.

Serving-policy behaviour is preserved with **no new logic** — every case
already has a distinct typed error, and the adapter only maps it:

| case | via MCP |
|---|---|
| excluded | `is_error`, `resource_excluded`, identity stub only |
| metadata_only | `is_error`, `content_refused` |
| tombstone | `is_error`, `no_addressable_content` + replacement |
| technique | `is_error`, `no_addressable_content` + `defined_in` |
| safety_gated | whole verified body, `guard_preservation` surfaced |
| attachments | not retrievable; no tool reaches them |
| unrecognised policy | fails closed to `metadata_only` |

The adapter performs no policy check of its own — a second policy
implementation is exactly the drift Phase 2 was built to prevent.

---

## Not adopted: resources and prompts

**MCP resources: NONE.** Enumerating 5,271 resources through `resources/list`
would produce a listing larger than any search result, on every connection.
Templates avoid the listing but duplicate `pae_get_resource` on a primitive
with weaker error semantics — a policy refusal becomes a read failure rather
than a typed `content_refused`, and the excluded-vs-nonexistent distinction the
Registry deliberately maintains becomes hard to express.

**MCP prompts: NONE.** PAE's 4,241 prompt-kind resources are not MCP prompts.
An MCP prompt is a parameterised message template a user invokes directly; a
PAE prompt is a governed document with serving policy, maturity, provenance,
checksums and guard preservation. Mapping the corpus wholesale would bypass
search and routing entirely, discard every governance field, and re-expose
bodies through a primitive with no serving-policy vocabulary.

Revisit either only if a concrete host workflow demands what tools cannot meet.

---

## Error model

| PAE exception | exit | MCP surface | `error.code` |
|---|---:|---|---|
| `UsageError` | 2 | tool error | `usage_error` |
| `MalformedReference` | 2 | tool error | `malformed_reference` |
| `InvalidBudget` / `BudgetTooSmall` | 2 | tool error | `invalid_budget` / `budget_too_small` |
| *(new)* `MissingExtra` | 2 | startup only, stderr | — |
| `RepositoryNotFound` | 3 | **startup failure**, stderr | — |
| `ResourceNotFound` | 4 | tool error | `resource_not_found` |
| `AccessRefused` / `ContentRefused` | 5 | tool error | `access_refused` / `content_refused` |
| `ResourceExcluded` | 5 | tool error, identity stub only | `resource_excluded` |
| `NoAddressableContent` | 6 | tool error | `no_addressable_content` |
| `SourceIntegrityError` subclasses | 7 | tool error, integrity class | `source_path_refused`, `source_unavailable`, `source_too_large`, `checksum_mismatch`, `content_encoding_error` |
| `IncompatibleRegistry` | 8 | **startup failure**, stderr | — |
| `RegistryValidationError` | 9 | tool error, integrity class | `registry_validation_failed` |
| unexpected `Exception` | 1 | tool error, **no traceback** | `internal_error` |

`PaeError.error` and `.details` already carry exactly the machine-readable
fields needed — this is a projection, not a new taxonomy.

Wire contract: explicit `CallToolResult(is_error=True)` with a structured
union, preferred over `ToolError` because it keeps one result shape and lets
`structured_content` carry the code.

```json
{ "ok": false,
  "error": { "code": "content_refused",
             "message": "...is served as metadata only; its body is withheld",
             "details": { "id": "...", "serving_policy": "metadata_only" } } }
```

Recoverable errors are readable and retryable. Integrity failures are also tool
errors but must say plainly that the operation **cannot safely complete** —
never suggest a retry.

**Details filtering is mandatory.** `PaeError.details` carries `path`,
`resolved` and `root` on integrity errors — absolute filesystem paths. The
projection must allowlist keys per code, drop `root`/`resolved` entirely, and
keep `path` only in the repo-relative form the registry stores. A test must
assert no model-facing error contains the repository root.

Framing and unknown-method faults stay protocol errors, handled by the SDK.
The high-level path is what makes that hold — the low-level experiment turned a
missing required argument into `-32603` plus a traceback.

---

## Lifecycle, concurrency and the cold-start stampede

```
startup → Repository.at(root)      # validates markers + schema
        → Registry.open()          # reads nothing
        → SearchEngine(registry)   # reads nothing
        → Router / ContextCompiler
        → warmup  (background, after listening)
        → MCPServer + stdio
```

Runtime construction measures **0.2 ms** — everything is lazy, as Phases 2–5
designed it. One process = one snapshot. No watcher, no reload, no root
switching, no cache. To see a changed checkout, restart.

**The finding most likely to bite in production.** The SDK runs synchronous
tool functions on a **thread pool** — 8 concurrent calls ran on 8 distinct
worker threads, none the event loop. `SearchEngine._ensure_index()` is a lazy,
unguarded memoisation. The two combine badly:

| remedy | warmup | burst | index builds | all succeeded |
|---|---:|---:|---:|:---:|
| **A** none (naive port) | — | **11,691 ms** | **8** | 8/8 |
| **B** first-build lock only | — | 1,058 ms | 1 | 8/8 |
| **C** startup warmup only | 1,122 ms | 19.7 ms | 1 | 8/8 |
| **D** warmup + lock | 1,157 ms | **17.0 ms** | 1 | 8/8 |

Results stayed *correct* under A — the build is idempotent, last write wins —
but the index was built **eight times**, costing ~11.7 s and eight simultaneous
~114 MB constructions. A host opening with a few parallel calls hits exactly
this.

**Adopt D.** The warmup moves the build off the first real call; the lock is
not redundant — it guards the window before warmup completes and the case where
warmup fails. Scope it to a double-checked `threading.Lock` around the *first
build only*, never held during a query.

Handlers stay **synchronous** and let the SDK's thread offload do its job —
measured to work correctly and keep the event loop free, with no
`asyncio.to_thread` of PAE's own.

---

## Transport and stdout purity

stdio only. HTTP is not a transport toggle but a different product: it needs
authorization (rewritten in 2026-07-28), bind/origin/Host defaults, TLS or
reverse-proxy termination, rate limiting, a written remote threat model,
observability, and an explicit decision on whether remote callers may read
`safety_gated` bodies at all. A loopback-only variant buys almost nothing over
stdio while still crossing the no-network line.

stdout is protocol-only; stderr is diagnostics. A real-subprocess experiment
produced a finding that changes how this must be tested:

> The official client **tolerates** non-JSON lines on stdout — it logs a parse
> failure and skips them. A deliberately contaminated server still completed a
> full `tools/list` + `tools/call` session.

So *"the session succeeded"* is **not** a purity test. A byte-level probe was
built and validated both ways:

```
CLEAN  → 1 stdout line,  1 valid JSON-RPC,  0 non-protocol   → PASS
DIRTY  → 4 stdout lines, 2 valid JSON-RPC,  2 non-protocol   → FAIL
         -> 'PAE Engine 0.3.0.dev0'
         -> 'repository: /home/user/prompt-agent-engineering'
```

The negative case is the point: it caught a version banner **and an absolute
repository path disclosure**. Phase 6 must ship this test with its contaminated
fixture, or the assertion is unfalsifiable.

---

## Measurements

| Operation | Result |
|---|---:|
| core `pae --version`, no MCP extra | ~70 ms wall |
| core `import pae_engine` | ~40 ms, 16.5 MB RSS |
| MCP SDK cold import | **~725 ms**, +59.4 MB RSS |
| PAE runtime construction (lazy) | 0.2 ms |
| server startup → ready (real subprocess) | **810 ms** |
| `tools/list` | 0.7 ms |
| first `search_resources` (builds index) | 1,224 ms |
| warm `search_resources` | **2.4 ms** (0.30 ms in-process) |
| warm `route_task` | 3.5 ms |
| `compose_bundle` 8k, warm | 63.0 ms |
| peak RSS, index built | **181.6 MB** (7.5 → 66.9 +SDK → 181.6 +index) |
| 8 concurrent cold calls, no remedy | 11,691 ms, 8 redundant builds |
| 8 concurrent cold calls, warmup + lock | **17.0 ms** |

Payload sizes through the official client:

| operation | content B | structured B | total B |
|---|---:|---:|---:|
| search limit=10 | 1,433 | 5,819 | 7,252 |
| search limit=100 | 14,279 | **57,907** | **72,186** |
| route limit=25 | 27 | 15,945 | 15,972 |
| bundle 8k | 14,958 | 3,004 | 17,962 |
| bundle 32k | 103,925 | 3,639 | 107,564 |
| bundle 200k (`max_resources`-bound) | 129,914 | 3,866 | 133,780 |

The persistent server earns its keep exactly as intended: a **1,224 ms** index
build paid once and amortised to **2.4 ms** per subsequent search — a 510×
improvement no per-invocation CLI can reach.

`search limit=100` is the largest non-bundle payload at 72 KB, 80% of it
structured (`match_terms`/`matched_fields` are verbose per hit). No core change
is warranted — the CLI needs that evidence — but docs should note 10–25 as the
useful range. `MAX_LIMIT` already bounds the worst case.

Corpus context: 4,888 servable bodies, median 9,694 B, p95 20,284 B, **max
76,818 B** (≈19k estimated tokens, 54.6× headroom under the 4 MiB ceiling).
That largest body is why `include_content` defaults to `false`.

---

## Security delta

| new threat | mitigation |
|---|---|
| untrusted tool arguments | enforced `Annotated` bounds (6/6 rejected); typed errors, never tracebacks |
| repository selection by the model | **no tool takes a path/root/repo argument**; binding is startup-only |
| stdout injection / path disclosure | byte-level purity test with a contaminated negative fixture |
| information exposure in errors | per-code allowlist on `details`; no env vars, absolute paths, home dir, interpreter path or exception reprs |
| large / repeated calls | existing bounds apply unchanged |
| concurrent cold-start amplification | warmup + first-build lock |
| content prompt injection | unchanged: bodies are data; framing preserved by using `render_markdown()` |
| dependency supply chain | 29 packages incl. `cryptography`; pinned range, two-point CI, opt-in |
| future network transport | deferred; prerequisites listed above |

Preserved without modification: read-only runtime, no arbitrary per-call paths,
registry checksums, serving policy, whole-body-or-absent, excluded-resource
secrecy, bundle authority framing, bounded queries and budgets.

Existing per-call bounds are adequate for local stdio; no timeout or
concurrency cap is recommended, since the caller is the machine owner and the
measured worst case after the warmup fix is ~65 ms.

> **Note on `excluded`.** The corpus currently holds **zero** excluded
> resources. Every exclusion path must still be implemented and tested exactly
> — the secrecy property is not testable in production if it is only written
> when first needed.

---

## Testing

1. **Pure adapter tests** — handlers and projections called directly, no SDK.
   Projection shape, error mapping, `details` allowlisting, `task` XOR `refs`.
2. **Official in-memory `Client`** — `Client(server)`, no subprocess. Schemas,
   annotations, structured outputs, every error case, concurrency bursts. Most
   MCP tests live here: fast, deterministic, no process management.
3. **Real stdio subprocess** — launches `pae mcp --repo ...`, full lifecycle,
   and the **byte-level stdout purity test with its contaminated fixture**.
   Non-negotiable, for the reason above.
4. **Tool-schema snapshots** — the catalog is product API and clients cache it.
   Freeze order, names, descriptions, input schemas, output shapes and
   annotations as one canonical blob. Determinism verified: three independent
   constructions produced an identical signature.

Also required: `import pae_engine` and every non-`mcp` command work with no
`mcp` installed; no tool schema contains a path-shaped parameter; no
model-facing error contains the repository root.

`mcp[cli]` is dev-only. Maintainers run the Inspector against the same command
a host uses — that one command is the whole workflow.

---

## Host integration

Verified from current official documentation. No credentials, no host app in CI.
Phase 6 **must not** auto-edit any host configuration file.

**Claude Code** — `claude mcp add`, storing to `.mcp.json` or `~/.claude.json`:

```json
{ "mcpServers": {
    "pae": { "command": "pae", "args": ["mcp", "--repo", "/path/to/checkout"] } } }
```

**VS Code / GitHub Copilot** — `.vscode/mcp.json`, `servers` key; stdio implied
by `command`/`args`:

```json
{ "servers": {
    "pae": { "command": "pae", "args": ["mcp", "--repo", "/path/to/checkout"] } } }
```

Codex/OpenAI local MCP was **not verified**; no configuration for it should be
published without checking current official documentation first.

---

## CI and version

**Core job** (existing, unchanged): no `pip install`, zero-dependency
assertion, `Requires-Dist: none`, wheel/sdist checks, `smoke_install.py`,
`validate-registry`. **Add**: `pae mcp` fails cleanly with the missing-extra
message — that is the base install's contract.

**MCP job** (new): installs `.[mcp]`; adapter tests, in-memory `Client` tests,
stdio subprocess smoke, purity test with dirty fixture, schema snapshots,
concurrency burst. Matrix over two SDK points — floor `mcp==2.1.1` and latest
`<3` — on Python 3.10 and 3.12.

**Version: `0.4.0.dev0`.** A new optional dependency, a new console subcommand
and a new public protocol surface are a minor bump under any reading. No
publication, no tag.

---

## Planned ADRs

- **0028** — MCP is an adapter, not a second engine.
- **0029** — Optional extra, and the scope of the zero-dependency guarantee.
- **0030** — stdio first; HTTP deferred, with prerequisites.
- **0031** — Result-channel split; records the 31,478 → 17,962 B measurement
  and the framing-loss finding.
- **0032** — High-level `MCPServer` with explicit results; records the
  advertise-vs-enforce evidence, so a future reader does not "upgrade" to the
  low-level server believing it gives more control.

---

## Open for maintainer decision

1. **Accept the 29-package / 68 MB / +59 MB-RSS graph as an opt-in extra?**
   *Recommend yes* — the price of Tier-1 compliance, opt-in, base install
   provably unchanged.
2. **`pae_*` prefix or bare tool names?** *Recommend the prefix.*
3. **Four tools, or add `registry_stats`?** *Recommend four.*
4. **Index-build lock in the adapter or in `SearchEngine`?** *Recommend the
   adapter for Phase 6* — core stays single-threaded by construction,
   relocatable later if a second concurrent consumer appears.
5. **Warmup blocking readiness (~1.1 s) or backgrounded after listening?**
   *Recommend backgrounded*, so `tools/list` answers in 0.7 ms while the index
   builds; the lock makes it safe. Blocking is simpler and also defensible.
6. **Bump to `0.4.0.dev0`?** *Recommend yes.*

---

## Carry-forward caveats

Two things the implementation spec should treat as open, not settled:

- `additionalProperties: false` is not advertised by the chosen path (unknown
  properties are ignored) — a real if minor gap.
- Codex/OpenAI host configuration was not verified and must be checked before
  any snippet is published.
