# ADR-0018 — The Engine requires a checkout and bundles no corpus

## Status

Accepted. Implemented in Phase 3.

## Context

An installable tool that reads a 5,000-resource catalogue has to get the
catalogue from somewhere. Three options were live:

1. **Bundle it in the wheel.** `pip install` gives you everything; nothing to
   configure.
2. **Download it on first use.** Small wheel, always current.
3. **Read a local checkout.** Small wheel, nothing downloaded, but the user
   must have a checkout.

Option 1 puts ~10 MB of registry plus the corpus itself inside a package whose
code is ~30 KB, and freezes it at build time: the catalogue is stale the moment
it ships, and a resource body served from the wheel could differ from the same
resource in the repository the user is actually working in.

Option 2 makes the tool useless offline and in air-gapped environments,
introduces a network dependency into a deterministic lookup, and gives an agent
a way to bind to a catalogue nobody reviewed.

## Decision

The Engine reads a **local PAE checkout**, discovered at runtime. The wheel
contains code and nothing else; CI fails the build if `registry.jsonl` or
`registry-summary.json` appears in either artifact.

Discovery is exactly four steps, and there is no fifth:

1. an explicit `--repo` / `explicit=`;
2. the `PAE_REPO` environment variable;
3. the working directory and its ancestors;
4. failure — exit 3.

There is no `$HOME` scan, no downward filesystem scan, no sibling-directory
guess, no XDG config, no network location, no registry download, and **no
fallback to package data**.

**An explicit source never falls through.** If `--repo` is given and holds no
registry, that is an error; the Engine does not then try `PAE_REPO` or the
working directory. The failure mode being prevented is specific: an agent that
names a checkout, gets an answer, and never learns the answer came from
somewhere else.

A directory is a candidate when it holds **both** registry artifacts. If it
does, and the summary declares a schema this Engine does not implement, that is
**incompatible registry (exit 8)**, not "repository not found (exit 3)" — and
during the ancestor walk it *stops the walk* rather than stepping over it to
find a compatible checkout higher up.

## Consequences

- The Engine works offline, in air-gapped environments and in locked-down CI.
- The catalogue is never stale relative to the checkout being worked in,
  because it *is* the checkout being worked in.
- Users must have a checkout. This is stated plainly in the README and the
  getting-started guide rather than discovered through a confusing error.
- "Which catalogue answered this?" always has one auditable answer, printed by
  `pae where`.
- A future hosted or packaged-catalogue mode would be a new ADR, not a quiet
  addition to the discovery chain.
