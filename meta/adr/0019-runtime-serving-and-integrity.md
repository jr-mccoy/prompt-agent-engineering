# ADR-0019 — Runtime content serving: whole bodies, verified, fail-closed

## Status

Accepted. Implemented in Phase 3. Builds on
[ADR-0015](0015-serving-policy-metadata.md) (the registry carries serving
policy) and [ADR-0016](0016-sha256-checksum-contract.md) (checksums are SHA-256
over raw source bytes).

## Context

Phase 2 put serving policy and checksums *in* the registry. Phase 3 is the
first thing that acts on them, which turns several previously abstract
questions into behaviour an agent will depend on:

- What does a `metadata_only` resource return?
- Is an `excluded` resource distinguishable from one that does not exist?
- Can a caller ask for the first 200 lines of a 3,000-line safety-gated prompt?
- What happens when the file on disk no longer matches the registry?
- Which of those is a *refusal* and which is an *absence*?

Getting these wrong is not a cosmetic problem. Many resources in this corpus
carry guards, disclaimers, scope gates and authorization requirements that only
work if they arrive attached to the content they qualify.

## Decision

**Policy is enforced in the library, below the CLI.** A future MCP server gets
the same answers without importing a line of CLI code.

**Bodies are whole or absent.** There is no `--head`, `--tail`, `--lines`,
`--max-bytes`, `--excerpt` or `--summarize`, and no library method returns part
of a body. For a guard-preserving resource this makes truncation *structurally
unavailable* rather than merely discouraged — a caller cannot strip the safety
section by accident, and the Engine cannot do it to protect a terminal.

**Integrity is mandatory and has no bypass.** Every content read hashes the
bytes and compares them with the registry's SHA-256. There is deliberately no
`--no-verify` flag: it would be four lines to implement, and the reason not to
is that "prove the file is the one the registry describes" stops meaning
anything the moment it is optional. A mismatch returns the expected digest, the
actual digest, the path and the identity — and no source bytes. If a genuine
use case for bypassing verification ever appears, it is a future API decision
with its own record.

**Unknown policy fails closed to `metadata_only`,** never to `standard`, and
the response says the declared value was not recognized. A registry written by
a newer producer must not be able to widen what this Engine will serve.

**Absence and refusal are different exit codes.** A tombstone (exit 6, the body
no longer exists) and a technique (exit 6, defined inside the master index
rather than by a file) are not withheld — they have nothing to withhold. A
`metadata_only` resource (exit 5) does. Collapsing these would tell a caller to
seek permission when what they need is a different resource.

**An excluded resource stays distinguishable from a nonexistent one.**
`resolve()` returns its identity; `get()` and `content()` refuse with exit 5
and an identity stub of `uid`, `id`, `kind`, `lifecycle`, `serving_policy` —
never its title, description, native metadata or body. Answering exit 4 would
be a lie; returning the record would defeat the exclusion.

**Every registry path is untrusted input.** Before any file is opened: reject
empty paths, NUL bytes, POSIX absolutes, Windows drive and UNC paths, backslash
separators and `..` components; join under the root; resolve symlinks; require
the resolved target to still be inside the root; require a regular file;
require it under a 4 MiB ceiling. A consumer may be reading a registry it did
not generate, so "the registry said so" is never sufficient reason to read a
file.

**Retrieved text is data.** No `eval`, `exec`, `compile`, subprocess, shell,
template expansion or interpretation of imperative content — asserted by tests
that walk the installed package's AST, not by convention.

## Consequences

- A resource arrives with its guards intact or does not arrive.
- An uncommitted local edit fails loudly, with an error that names the cause,
  instead of silently serving content the registry does not describe.
- The 4 MiB ceiling never touches a real resource (the largest today are tens
  of kilobytes) and bounds the damage from a pathological path.
- Six distinct failure codes exist because six distinct problems exist; an
  agent can branch on them without parsing prose.
- Adding a bypass, an excerpt mode or a permissive default later means
  superseding this record, which is the point of writing it down.
