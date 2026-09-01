# ADR-0008 — Every published repository count is generated and CI-verified

## Status

Accepted. Implemented.

## Context

Published counts had drifted badly and silently. `README.md` advertised "5,600+
prompts"; `CLAUDE.md` said "~2000 prompts across 22 domain directories";
`START_HERE_FOR_AI.md` said "~1,800" with skills at 186 and agents at 99 against
actual values of 330 and 143.

The reason drift went undetected is that the existing checks were
**phrase-matched**. `scripts/validate_technique_catalog.py` locates count claims
with literal regexes and iterates the matches — so when a sentence is reworded,
the regex finds nothing, the loop body never runs, and the check reports success.
The README badges matched no pattern at all and were validated by nothing.

Rewording documentation would therefore have silently disabled two live checks,
and replacing wrong numbers with right ones would have left them just as
unguarded.

One mechanism in the repository already did this correctly:
`domain-agentic-resources/inventory_counts.py` writes an
`<!-- INVENTORY_COUNTS: {...} -->` declaration into three READMEs, and its
`extract_decl` **raises** when the declaration is absent.

## Decision

Generalize that proven design rather than invent a second marker format.

`scripts/generate_repo_facts.py` is the single canonical facts generator. It
composes the repository's existing authoritative counters — `inventory_counts.py`
for skills/agents/commands, `validate_technique_catalog.py` for personas and the
technique catalog, `PROMPT_INDEX.json` for the artifact partition — and
cross-checks the two independent resource counters against each other rather
than reimplementing either.

It writes:

1. `meta/REPOSITORY_FACTS.json` — deterministic, committed, schema-versioned,
   with a stated membership rule for every fact and **no timestamp**, so the file
   changes only when the repository does.
2. Generated blocks in `README.md`, `CLAUDE.md`, `AGENTS.md`, and
   `START_HERE_FOR_AI.md`:

```text
<!-- REPO_FACTS:BEGIN name=counts -->
<!-- REPO_FACTS_DECLARATION: {"skills": 330, ...} -->
...generated prose...
<!-- REPO_FACTS:END name=counts -->
```

`--check` fails when a required block is missing, when a required declaration is
missing, when a declared value disagrees with computed truth, or when the block
body differs from its regenerated form (a hand edit). **A missing match is always
an error, never a pass.**

Legacy phrase checks are kept, not removed — CI stays at least as strict as
before — but they are no longer the primary protection for these documents.

## Consequences

- No repository count can be hand-edited or quietly rewritten into staleness.
- Adding a count to a primary document means adding it to the generator, which
  forces a membership rule to be stated first.
- Rewording surrounding prose is safe; rewording *inside* a generated block
  fails CI, which is the intended trade.
- A new `domain-*` directory that is not added to the index allowlist changes a
  fact and therefore surfaces as drift instead of vanishing.
