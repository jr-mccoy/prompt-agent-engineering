# Architecture

## The shape of the problem

An audit of somebody else's corpus has one catastrophic failure mode and it is
not a wrong number. It is a **confident, empty, wrong answer**: a misconfigured
run that finds nothing and reports a clean corpus. Every structural decision
below exists to make that impossible, or to make the resulting claim unsayable.

## Data flow

```
config/audit.json
        │
        ▼
  inventory.py ──────── Gate 0 ──────► audit/inventory.json
        │                                   │
        │                        ┌──────────┴──────────┐
        │                        ▼                     ▼
        │                  cluster.py          observed_score.py ── Gate A
        │                        │                     │
        │                        └──────────┬──────────┘
        │                                   ▼
        │                            audit/findings.md
        │                                   │
        │                                   ▼
        │                            claim_guard.py ──── Gate B ──► report
        │                                   │
        └───────────────────────────────────┴──► handback.py ── Gate C
                                                        │
                                                        ▼
                                        <corpus>/meta/registry/
```

One walk of the tree. Everything downstream reads `audit/inventory.json`, so a
correction to membership propagates and a correction anywhere else does not.

## Why identity lives in the inventory

`uid_for(kind, birth_path)` is imported from
`scripts/pae_registry/identity.py` and used unchanged. It is
`sha256(kind + "\0" + birth_path)` folded to 60 bits of Crockford base32; it
takes two strings and knows nothing about this repository, which is exactly
what makes it correct on a foreign tree.

Assigning identity at discovery rather than at handback means the cluster
output, the score records and the registry all name artifacts the same way. A
second identity implementation would eventually disagree with the Engine that
has to open the handback, and the disagreement would surface at the worst
possible moment — in front of the client, at Gate C.

Public IDs are the one place the kit diverges: the *shape*
(`<kind>:<scope>/<slug>`) and the component normalisation are the parent's, but
the scope comes from config, because a client tree has no `domain-` prefixes
to strip.

## Why the kit imports the Engine rather than mirroring it

Three imports, each load-bearing:

| Import | Used for | Why not reimplement |
|---|---|---|
| `pae_registry.identity` | UIDs | a divergent UID breaks the handback |
| `pae_engine._lexical` | BM25F ranking | a private ranker would stop matching the client's own `pae search` |
| `pae_engine.validate` | Gate C | the gate should *be* the Engine's verdict, not a lookalike |

The cost is a stated dependency: the kit needs the PAE checkout it ships
inside, and each script says so in its import error. The `referenced-prompts/`
tree is what makes the *content* self-contained; the Python deliberately is not.

## Why the registry is written inside the corpus

`validate_registry` resolves every record's `source.path` against the
repository root and verifies its checksum. A registry written beside the corpus
produces `missing_source_file` on every record.

This also means the dry run cannot write in place. It copies the corpus to a
temporary directory, builds and validates there, and discards it — so a failed
build can never leave a partial registry in a client tree.

## The four gates and their placement

Each gate sits in the skill that owns the artifact it guards, not in a central
gate module. A gate separated from its data grows a second, stale copy of that
data's rules.

- **Gate 0** is in `inventory.py` because only discovery knows whether the
  config matched anything.
- **Gate A** is in `observed_score.py` because only the scorer knows the
  observable maximum per category.
- **Gate B** is in `claim_guard.py`, which is the only script that reads prose.
- **Gate C** is in `handback.py` and delegates its verdict to the Engine.

## Detectors versus judgement

The scripts observe structure. The vendored prompts in `referenced-prompts/`
carry the judgement, with a human in the loop.

Keeping the two apart is what lets the machine half refuse to assert a tier
while the engagement still produces an opinion — a clearly attributed one. It
is also why `observed_score.py` reports 54 of the rubric's 100 points with the
denominator stated: the other 46 are the prompts' territory, and printing 100
would claim coverage of them.

## The refusals, and where they are enforced

| Refusal | Enforced by |
|---|---|
| no quality tier | `gate_a` rejects a non-null `tier`; `assert_nothing_invented` checks the scheme |
| no copy edge | `assert_nothing_invented`; cluster output carries no `copy_of` field at all |
| no canonical in a cluster | `canonical_uid` is `null` with a stated basis; tested both tiers |
| no licence | every record writes `unresolved` |
| no unlicensed claim | `claim_guard.py`, six rules, any finding blocks |
| no bare-segment exclusion | `validate_config`, which refuses to run |

Six refusals, six enforcement points, and a test for each. A refusal that lives
only in prose is a preference.

## Anti-gaming

Two rules carried over from `agentic-system-factory/scripts/check_gate.py`,
because a template's worked example must never satisfy or trip a check:

1. **Prose detectors strip fenced blocks and inline code spans.** Without this,
   `claim-safety/references/forbidden-claims.md` — which quotes every forbidden
   sentence — could not exist.
2. **Security detectors do the opposite**, reading the unstripped text across
   the whole bundle. A credential inside a code fence is still a credential in
   the file, and a bundled script is the likelier place to find one.

## Fixture design

`samples/` is mostly negative, deliberately: two corpora (one that blocks Gate
0), five score records (four that fail Gate A), eight reports (six that fail
Gate B). A gate proved only against the case it passes has not been proved.
