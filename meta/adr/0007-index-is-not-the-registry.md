# ADR-0007 — `PROMPT_INDEX.json` is not the registry, and its entry count is not a prompt count

## Status

Accepted. Implemented for counting; registry generation is future work.

## Context

`PROMPT_INDEX.json` was being treated as a list of prompts, and its entry total
was published as the number of prompts in the repository. Inspection showed the
total is a mixed population. At the time of this decision, of 5,597 entries:

| Population | Count |
|---|---|
| Domain prompts | 4,121 |
| Slash commands filed inside domain directories | 10 |
| Agentic resources (skills, agents, commands, personas, their docs) | 799 |
| Bundled component files (`references/`, `assets/`, `cards/`, …) | 667 |

The 667 include a skill's reference documentation and, in one case, individual
tarot cards. The index also carries no `id`, `kind`, `maturity`, `checksum`, or
`license` field, and its scope is a hand-maintained `DOMAIN_DIRS` allowlist that
had drifted — it named a directory that no longer existed and omitted one that
did.

## Decision

`PROMPT_INDEX.json` is a **discovery index over indexed Markdown files**, not the
PAE Registry. It keeps that role.

No public claim equates its entry count with a prompt count. Every published
count comes from `meta/REPOSITORY_FACTS.json`, which partitions the index into
categories with stated membership rules and reports the raw total under the
honest name *indexed artifacts*.

The stale `DOMAIN_DIRS` entry was corrected in this phase (a one-line swap that
brought `domain-product-management` into scope and dropped the nonexistent
`domain-professional-communication`), because a count that silently omits a whole
domain cannot be called canonical.

The registry proper — stable IDs, kinds, sidecar metadata, canonical/copy
relations, serving policy — is future work described in
[`../../ARCHITECTURE.md`](../../ARCHITECTURE.md).

## Consequences

- Headline numbers dropped: "5,600+ prompts" is now 4,121 domain prompts plus
  separately-named categories. The smaller number is the true one.
- `meta/REPOSITORY_FACTS.json` is the only place to read a count from, and the
  membership rule sits next to each value.
- The index remains useful for discovery and stays CI-verified as current.
- When the registry lands, `indexed artifacts` and `registry resources` will be
  two different, separately reported things.
