# PAE Engine

The installable runtime for the **PAE Registry** — a read-only Python API and
`pae` command that resolve, inspect and serve the governed resources catalogued
in a local [prompt-agent-engineering](https://github.com/jr-mccoy/prompt-agent-engineering)
checkout.

```text
PAE Registry  →  pae_engine (Python API)  →  pae (CLI)
```

## Status

**Version 0.1.0 is the in-tree pre-release package version. The project has not
been published to PyPI.** Install it from a checkout; `pip install
prompt-agent-engineering` does not work yet and this document will say so until
a release actually exists.

Search, routing, context compilation and MCP are later phases. They are
deliberately absent rather than stubbed.

## What it does

| Command | Answers |
|---|---|
| `pae --version` | which engine, and which registry contract it implements |
| `pae where` | which checkout am I bound to, and how was it found |
| `pae stats` | what is in the registry, by lifecycle, kind, maturity, serving policy |
| `pae get <ref>` | resolve a UID, public ID or retired alias to its record |
| `pae get <ref> --content` | return the whole verified source body |
| `pae validate-registry` | is this checkout's registry safe to serve from |

## Design commitments

**A checkout is required.** The wheel contains no corpus and no registry. The
Engine reads `meta/registry/registry.jsonl` and
`meta/registry/registry-summary.json` from a checkout you supply. That keeps a
30 KB package from carrying a 10 MB catalogue that would be stale the moment it
shipped.

**Zero runtime dependencies.** Standard library only, so the Engine installs
and runs offline, in air-gapped environments, and in locked-down CI.

**Local only, and read-only.** Discovery never touches the network and never
falls back to a download. The Engine opens files for reading and does nothing
else to your filesystem — no writes, no deletes, no subprocesses, no sockets,
no `eval`. Automated tests walk the installed source's AST and fail if any of
that changes.

**Retrieved text is data.** A resource body is bytes handed back to the caller.
It is never templated, expanded, interpreted or executed, however imperative it
reads.

**Whole or nothing.** There is no `--head`, no `--max-bytes`, no excerpt mode
and no library method that returns part of a body. Many resources in this
corpus carry guards, disclaimers and authorization gates that are load-bearing;
truncation is structurally unavailable rather than merely discouraged.

**Integrity is not optional.** Every content read verifies the registry's
SHA-256 over the raw source bytes. There is no `--no-verify` flag. If a local
edit makes a file differ from the generated registry, the call fails and says
exactly that, and no bytes are returned.

## Repository discovery

Exactly four steps, in order, and an explicit source never falls through to the
next one:

1. `--repo PATH` (or `Repository.discover(explicit=...)`)
2. the `PAE_REPO` environment variable
3. the working directory and its ancestors
4. failure — exit 3

A directory is a candidate when it holds both registry artifacts. If it does
and the summary declares a schema this Engine does not implement, that is an
*incompatible registry* (exit 8), never "repository not found" — including
during the ancestor walk, which stops there rather than stepping over it.

## Serving policy

Enforced in the library, before any CLI formatting, so every consumer gets the
same answer.

| Policy | Metadata | Content |
|---|---|---|
| `standard` | served | whole verified body |
| `safety_gated` | served | whole verified body, guard metadata propagated |
| `metadata_only` | served | refused, exit 5 — the file is never opened |
| `excluded` | refused, exit 5, with an identity stub | refused, exit 5 |
| *unrecognized or missing* | served | refused — fails closed to `metadata_only`, never to `standard` |

An **excluded** resource stays distinguishable from one that does not exist:
`resolve()` returns its identity, and the refusal carries a stub of `uid`,
`id`, `kind`, `lifecycle` and `serving_policy` — but never its title,
description, native metadata or body.

**Tombstones** and **techniques** are not withheld, they have no addressable
body: a tombstone's file no longer exists, and a technique is defined inside
the master technique index rather than by a file of its own. Both return exit 6
for `--content`, which is a different problem from exit 5 and calls for a
different next step.

## Exit codes

| Code | Meaning |
|---|---|
| 0 | success |
| 1 | internal engine error |
| 2 | usage error or malformed reference |
| 3 | repository not found, or the named path holds no registry |
| 4 | well-formed reference, no such resource |
| 5 | access refused by serving policy |
| 6 | resource has no independently addressable body |
| 7 | source path, size, integrity or encoding failure |
| 8 | incompatible registry schema |
| 9 | runtime registry validation failure |

The distinctions are the point: an unknown reference is not a malformed one, a
withheld resource is not a nonexistent one, a missing body is not a withheld
one, and an integrity mismatch is not a policy refusal.

## Output contract

- stdout carries the answer. On any nonzero exit it is **empty**.
- stderr carries errors and diagnostics.
- `--json` emits one compact, key-sorted, UTF-8 JSON object with a trailing
  newline, and on failure emits exactly one JSON error object on stderr.
- `pae get --content` writes source bytes to stdout byte-for-byte, with no
  header, footer or added newline.
- `pae get --content --json` decodes strictly as UTF-8; a body that is not
  valid UTF-8 is an integrity failure, not an invitation to substitute
  replacement characters. Raw mode still returns those bytes exactly.

## Install

From a checkout:

```bash
git clone https://github.com/jr-mccoy/prompt-agent-engineering.git
cd prompt-agent-engineering
python3 -m venv .venv && source .venv/bin/activate
pip install -e ./pae-engine
```

See [docs/getting-started.md](docs/getting-started.md) for the full walkthrough.

## Python API

```python
from pae_engine import Repository

repository = Repository.discover()          # --repo / PAE_REPO / ancestors
registry = repository.registry()            # opens no registry data yet

registry.stats()                            # Summary, from the generated summary
registry.resolve("technique:ST-01")         # Resolution — identity only
registry.get("technique:ST-01")             # Record — full normalized metadata
registry.content("prompt:...").text()       # Content — whole, verified body

for record in registry.records():           # streaming, bounded memory
    ...
registry.load_all()                         # every record, memoized
```

Every public model exposes `to_json_obj()`, and the CLI uses those methods
rather than keeping a second description of the machine-readable shapes.

Typed errors carry machine-readable detail: `MalformedReference`,
`RepositoryNotFound`, `ResourceNotFound`, `ContentRefused`, `ResourceExcluded`,
`NoAddressableContent`, `PathSecurityError`, `ChecksumMismatch`,
`ContentEncodingError`, `IncompatibleRegistry`, `RegistryValidationError`.

## Public API stability

`0.1.0` is a pre-release. The surface below is stable enough to build later
phases on, but is **not** covered by a 1.0 semantic-versioning promise:

the `pae` command name · exit codes · `--json` field names · the `pae_engine`
import namespace · `Repository`, `Registry`, `Record`, `Resolution`,
`Content`, `Summary` · the typed exception hierarchy.

Underscore-prefixed modules and helpers are not public API.

## Licence

MIT. See [LICENSE](LICENSE), which is byte-identical to the repository licence
and is checked in CI.
