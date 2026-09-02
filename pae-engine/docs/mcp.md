# The PAE MCP server

`pae mcp` serves one PAE checkout to an MCP client over stdio. It exposes four
read-only tools, and it is an **adapter**: every tool validates its input, calls
an existing Engine API, projects the result, and maps errors. Search ranking,
routing, packing, serving policy and integrity checking all stay where they
already live.

The MCP SDK is an **optional extra**. A plain `pip install` of the Engine still
resolves to nothing but the standard library.

---

## Install

The distribution is **not published to PyPI yet**, so install it from a local
checkout. `pip install prompt-agent-engineering[mcp]` will not work today.

```bash
python3 -m venv .venv-pae
.venv-pae/bin/pip install "/absolute/path/to/prompt-agent-engineering/pae-engine[mcp]"
```

Windows:

```powershell
py -m venv .venv-pae
.venv-pae\Scripts\pip install "C:\path\to\prompt-agent-engineering\pae-engine[mcp]"
```

Without `[mcp]` everything else still works, and `pae mcp` reports what is
missing rather than failing obscurely:

```
$ pae mcp --repo /path/to/repo
pae: missing_extra: the MCP server needs the optional 'mcp' extra, which is not installed
  install it with: pip install 'prompt-agent-engineering[mcp]'
```

### What the extra costs

Worth knowing before you add it. Measured on Python 3.11 with `mcp` 2.1.1:

| | base install | with `[mcp]` |
|---|---:|---:|
| packages | **0** | ~29 |
| installed size | ~0.3 MB | ~68 MB |
| cold import | ~40 ms | ~725 ms (Linux) |
| RSS after import | ~17 MB | ~67 MB |

The SDK unconditionally pulls a full HTTP server stack (`starlette`, `uvicorn`,
`sse-starlette`) and a JWT/crypto chain (`pyjwt[crypto]` → `cryptography`), none
of which stdio uses. There is no stdio-only extra upstream. That cost is exactly
why MCP is opt-in rather than a base dependency.

`mcp[cli]` (the MCP Inspector) is a developer convenience and is deliberately
**not** a PAE extra.

---

## Run it

```bash
pae mcp --repo /absolute/path/to/prompt-agent-engineering
```

`--repo` is strongly recommended over relying on discovery: an MCP host spawns
the server with an arbitrary working directory, so the ancestor walk that serves
the CLI well is unreliable here. `PAE_REPO` works too.

**One process is one snapshot.** The server answers from the checkout as it was
when the process started. There is no watcher, no reload and no cache. To pick up
a changed checkout — or a regenerated registry — **restart the server**.

stdout carries protocol traffic only. Diagnostics go to stderr.

---

## Host configuration

Verified against current official documentation on 2026-09-02. Prefer the
**absolute path to the `pae` executable inside your venv**: hosts do not
reliably inherit your shell `PATH`.

PAE never edits these files for you.

### Claude Code

`claude mcp add`, or `.mcp.json` (project scope) / `~/.claude.json`:

```json
{
  "mcpServers": {
    "pae": {
      "command": "/absolute/path/to/.venv-pae/bin/pae",
      "args": ["mcp", "--repo", "/absolute/path/to/prompt-agent-engineering"]
    }
  }
}
```

Equivalent CLI form:

```bash
claude mcp add --scope project --transport stdio pae \
  -- /absolute/path/to/.venv-pae/bin/pae mcp --repo /absolute/path/to/prompt-agent-engineering
```

Project-scoped servers require workspace-trust approval before first use.

### VS Code / GitHub Copilot

`.vscode/mcp.json` — note the top-level key is `servers`, not `mcpServers`:

```json
{
  "servers": {
    "pae": {
      "command": "/absolute/path/to/.venv-pae/bin/pae",
      "args": ["mcp", "--repo", "/absolute/path/to/prompt-agent-engineering"]
    }
  }
}
```

### Codex / ChatGPT

`~/.codex/config.toml`, or a project-scoped `.codex/config.toml` in a trusted
project:

```toml
[mcp_servers.pae]
command = "/absolute/path/to/.venv-pae/bin/pae"
args = ["mcp", "--repo", "/absolute/path/to/prompt-agent-engineering"]
```

---

## The four tools

| Tool | Core API | Returns a body? |
|---|---|---|
| `pae_search_resources` | `SearchEngine.search()` | no |
| `pae_route_task` | `Router.route()` | no |
| `pae_get_resource` | `Registry.lookup()` / `Registry.content()` | only with `include_content` |
| `pae_compose_bundle` | `Router.route()` + `ContextCompiler.compile_*()` | yes |

There is no `registry_stats`, no `validate_registry`, no MCP resources and no
MCP prompts. Operator questions are answered by the CLI (`pae stats`,
`pae validate-registry`), which is where they belong.

### `pae_search_resources`

Ranked metadata. Never reads a body, so what a resource *says* cannot influence
where it ranks, and search can never become a way to read something policy
withholds.

```
query   string, 1..2000 chars      (MAX_QUERY_CHARS)
limit   integer, 1..100, default 10 (MAX_LIMIT)
kinds   optional: prompt | technique | skill | agent | command | persona
scopes  optional list, max 25
```

### `pae_route_task`

Where a task belongs, plus candidate starting points. Reports `matched`,
`ambiguous`, `weak` or `no_route` — the last three are answers, not failures,
and the text says plainly that no route was selected.

`coverage` and `margin` are observed lexical quantities. **They are not
confidence scores** and nothing presents them as such.

```
task    string, 1..2000 chars
limit   integer, 1..25, default 5   (MAX_ROUTE_LIMIT)
kinds   optional kind list
```

### `pae_get_resource`

```
ref              string, 1..4096 chars (transport bound, not Registry grammar)
include_content  bool, default false
```

Serving policy is enforced by the Registry, unchanged:

| Case | Result |
|---|---|
| excluded | `resource_excluded` — identity stub only, never a title or description |
| metadata-only | `content_refused` |
| tombstone | `no_addressable_content` |
| technique | `no_addressable_content` (defined inside the technique index) |
| safety-gated | the whole verified body, or nothing |
| attachments | not reachable |

With `include_content`, the body is returned **in the text channel only**,
unchanged and whole, preceded by a short framing block and wrapped in boundary
markers derived from its own checksum. The framing states where the text came
from and what it does not outrank. It does not claim immunity to prompt
injection.

### `pae_compose_bundle`

```
task                     string   } exactly one
refs                     list, max 25 }
budget_estimated_tokens  integer, optional
budget_bytes             integer, optional, max 4 MiB (MAX_BUNDLE_BYTES)
max_resources            integer, 1..25, default 25
kinds / scopes           task mode only — rejected in refs mode, not ignored
```

**Budget rule.** If you supply *neither* budget field, the server uses a
convenient default of 8000 estimated tokens. If you supply *either*, only what
you supplied applies — a byte-only budget does **not** acquire a hidden token
cap.

The text channel is exactly `ContextBundle.render_markdown()`, byte for byte,
with nothing prepended: the canonical renderer already carries its own framing.

---

## Result channels

Two channels, two readers, and a body crosses the wire **exactly once**.

| Tool | text `content` | `structured_content` |
|---|---|---|
| search | deterministic ranked list | `SearchResults.to_json_obj()` |
| route | status, selection or ambiguity, candidates | `RouteDecision.to_json_obj()` |
| get | metadata, or framed body | record + serving + checksum, **never the body** |
| compose | canonical bundle Markdown | full bundle audit **minus** `included[*].content` |

The bundle audit keeps the bundle hash, route provenance, per-item checksums and
byte lengths, the complete omission list with reason codes, the budget report,
ordering and warnings. Each included body stays verifiable against the Markdown
through its `content_sha256`, so dropping the duplicate costs an auditor nothing.

Measured on the live 5,271-record registry:

| Operation | text bytes | structured bytes |
|---|---:|---:|
| search limit=10 | 2,011 | 5,819 |
| search limit=100 | 19,535 | 57,907 |
| get largest body (77 KB) | 77,570 | 2,834 |
| bundle 32k | 127,680 | 10,245 |

Text is always independently sufficient, because a client negotiating an older
protocol revision may not receive structured output at all.

`_meta` is not used.

---

## Errors

Recoverable failures come back as tool errors the model can read and retry:

```json
{ "ok": false,
  "error": { "code": "content_refused", "message": "…", "details": { } } }
```

Codes mirror the Engine's own taxonomy: `usage_error`, `malformed_reference`,
`invalid_budget`, `budget_too_small`, `resource_not_found`, `access_refused`,
`content_refused`, `resource_excluded`, `no_addressable_content`,
`source_path_refused`, `source_unavailable`, `source_too_large`,
`checksum_mismatch`, `content_encoding_error`, `registry_validation_failed`,
`internal_error`.

Error details are **allowlisted per code**. No model-facing message or detail
carries the checkout root, your home directory, an interpreter path, a traceback
or an exception repr. Two codes use a fixed message because their own text
embeds an absolute path that scrubbing cannot reach.

Startup failures — missing repository, incompatible registry, missing extra —
are process failures with a non-zero exit and a message on stderr, not tool
errors.

---

## Performance

The server exists to amortize the lexical index build. Measured on the live
registry (Windows, Python 3.13):

| Operation | Result |
|---|---:|
| runtime construction (lazy) | 1.4 ms |
| `tools/list` | 1.2 ms |
| first search (builds index) | 1,493 ms |
| warm search | **2.2 ms** |
| warm route | 5.8 ms |
| get metadata | 20 ms |
| bundle 8k | 586 ms |
| 8-call warm burst | 31 ms |
| peak RSS (index built) | 176 MB |

A background warmup starts as soon as the server is listening, so the first real
call is usually warm. A call that arrives mid-warmup waits on the same lock —
the index is built **once**, no matter how the calls interleave.

---

## Scope

Phase 6 is **stdio only**. There is no transport, host or port flag.

HTTP is not a toggle; it is a different product with a different threat model.
Before it could ship, PAE would need: authorization, bind defaults,
`Host`/`Origin` validation, TLS or reverse-proxy termination, rate limiting, a
written remote threat model, observability and audit, and an explicit decision
about whether remote callers may read safety-gated bodies at all. See
[ADR-0030](../../meta/adr/0030-stdio-first-http-deferred.md).

Also absent, deliberately: MCP resources, MCP prompts, extensions, sampling,
roots, protocol logging, and any tool that could switch repository.

### Known limitations

- The MCP extra is heavy relative to the core (~29 packages, ~68 MB).
- The base package is **zero-unconditional-dependency**, not literally free of
  `Requires-Dist` metadata — declaring an extra emits a conditional line.
- stdio only; no HTTP.
- No MCP resources or prompts.
- Unknown extra properties in tool arguments are ignored by the SDK rather than
  rejected; they cannot influence the handler or the repository binding, and a
  test asserts that.
- One process is one snapshot; restart to see checkout changes.
- The lexical index costs ~1.2 s to build and ~110 MB to hold.
- `search limit=100` produces verbose structured output (~58 KB).
- Retrieving a large body directly can consume a lot of context; the largest
  resource in the corpus is ~77 KB.

---

## Troubleshooting

**`missing_extra` on startup** — install the extra, or point the host at the
`pae` executable inside the venv that has it.

**`repository_not_found`** — pass an absolute `--repo`. The host's working
directory is not yours.

**Stale answers** — restart the server; one process is one snapshot.

**Nothing appears in the host** — check the host's MCP log. The server writes
diagnostics to stderr and never to stdout, so a silent stdout is correct.

**Inspecting the server yourself** — `mcp[cli]` provides the MCP Inspector.
Install it separately (it is not a PAE extra) and point it at the same command
your host uses.

---

## Related

- [`getting-started.md`](getting-started.md) — the CLI
- [`search-routing.md`](search-routing.md) — how ranking and routing behave
- [`context-compiler.md`](context-compiler.md) — what a bundle is
- ADRs [0028](../../meta/adr/0028-mcp-is-an-adapter.md),
  [0029](../../meta/adr/0029-optional-mcp-dependency.md),
  [0030](../../meta/adr/0030-stdio-first-http-deferred.md),
  [0031](../../meta/adr/0031-result-channel-split.md),
  [0032](../../meta/adr/0032-high-level-mcpserver.md)
