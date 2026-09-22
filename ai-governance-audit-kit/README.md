# AI Governance Audit Kit

A gated pipeline for auditing somebody else's prompt or agent corpus, and
handing back a registry their tools can open.

**This kit reports structure. It does not review content, assert a quality
tier, assert a copy relationship, or determine a licence.** Those are not
missing features; each one is a refusal with a reason, and the tests enforce
them.

```
Config → Inventory → Clusters → Observed scores → Findings
      → Report → Registry handback → Close-out
```

## What makes it a deliverable rather than a report

`Repository.at()` requires exactly two marker files at fixed relative paths and
a supported schema version. Nothing ties the PAE Engine to *this* repository's
content, only to that contract (ADR-0018).

So the kit writes a conformant `meta/registry/` **inside the client's tree**,
and the whole Engine — search, routing, context bundling, validation, the MCP
server — then works on their corpus unchanged:

```bash
PAE_REPO=/path/to/their/corpus pae stats
PAE_REPO=/path/to/their/corpus pae search "incident timeline"
PAE_REPO=/path/to/their/corpus pae validate-registry
```

If the unmodified Engine opens a registry this kit generated for a foreign
tree, the handback works. If it does not, the kit is a report generator.

## The four gates, enforced in code

| Gate | Question | Enforced by | Fails closed on |
|---|---|---|---|
| **0** Inventoriable | is there anything to audit? | `skills/corpus-inventory` | a config that matches nothing, an empty corpus, a duplicate public ID |
| **A** Scoreable | is this score a finding? | `skills/observed-scoring` | no rubric version, no stated provenance, an asserted tier |
| **B** Claim-safe | may the report say this? | `skills/claim-safety` | a direction with no interval, an ROI figure, an unstamped fixture number |
| **C** Handback complete | can the Engine open it? | `skills/registry-handback` | the Engine's own `validate_registry`, checksums verified |

Gate 0 exists because the worst thing an audit can produce is a confident,
empty, wrong answer. Gate B exists because the report is where a careful
evidence standard gets quietly forgotten — and of the four, it is the one that
protects the person selling the engagement.

## Layout

| Path | What it holds |
|---|---|
| `prompts/` | eight stage prompts, one per pipeline step |
| `skills/` | five skills, each with a stdlib-only script carrying `--self-check` |
| `commands/` | `/inventory`, `/cluster`, `/score-observed`, `/handback` |
| `agents/` | `audit-orchestrator`, `duplication-analyst`, `claim-safety-reviewer` |
| `config/` | `audit.json` — roots, exclusions, kind detectors, rubric, thresholds |
| `samples/` | two fixture corpora, five score records, eight reports — **most of them negative** |
| `referenced-prompts/` | 31 vendored governance and remediation prompts |
| `tests/` | 55 tests loading the same scripts the pipeline runs |

## Quick start

```bash
cd ai-governance-audit-kit

# every script proves itself against the tracked fixtures
for s in skills/*/scripts/*.py; do python3 "$s" --self-check; done
python3 -m unittest discover -s tests

# then, against a real corpus
python3 skills/corpus-inventory/scripts/inventory.py <corpus> --out audit/inventory.json
python3 skills/duplication-clusters/scripts/cluster.py --inventory audit/inventory.json
python3 skills/observed-scoring/scripts/observed_score.py <corpus>/skills/<bundle>
python3 skills/claim-safety/scripts/claim_guard.py audit/report.md
python3 skills/registry-handback/scripts/handback.py <corpus>          # dry run
python3 skills/registry-handback/scripts/handback.py <corpus> --write
```

`DRY_RUN.md` transcribes all four gates passing **and** blocking against the
fixtures, including every negative.

## What it reuses, and what is new

Most of this kit is assembly, and saying so is more useful than pretending
otherwise.

**Reused unchanged:** `pae_registry.identity.uid_for` for durable identities;
`pae_engine._lexical.LexicalIndex` for the BM25F ranking, so a cluster the
audit reports is a cluster the client's own `pae search` reproduces;
`pae_engine.validate.validate_registry` as Gate C itself; the
`agentic-system-factory` scorer's caps, load-bearing minimum and exit-code
contract; the four authoring rubrics as the criteria source; and
`client-services-studio`'s shape — stages, gates in code, negative fixtures,
`DRY_RUN.md`, tests.

**Genuinely new:** a config-driven membership layer (the parent's parses
`DOMAIN_DIRS` out of a script's *text*, a coupling no client tree can inherit);
near-neighbour clustering, which did not exist anywhere because this
repository's duplicate handling is deliberately edge-based; detectors that
score an artifact from itself rather than from the author's own rubric block;
and the claim-safety gate.

## Boundaries

- **Not a content review.** 46 of the authoring rubric's 100 points are
  judgements. The kit reports the other 54 with the denominator stated.
- **Not a security audit of what the artifacts do.** It finds credentials,
  absolute paths and contact details *in* artifacts. It does not analyse what a
  prompt or agent causes to happen.
- **Not a licence determination.** Every handback record says `unresolved`.
- **No network, no model, no embeddings.** Everything is standard library plus
  the PAE checkout the kit ships inside.

## Related

- `client-services-studio/` — qualify, scope, price, propose, contract, deliver,
  invoice and close out the engagement this kit performs.
- `agentic-system-factory/` — build an agentic system, rather than audit one.
- `meta/adr/0040-public-performance-claim-governance.md` — what Gate B enforces.
- `meta/adr/0012` (copies from explicit edges) and `meta/adr/0018` (the registry
  contract) — the two decisions that shape most of the kit's refusals.
