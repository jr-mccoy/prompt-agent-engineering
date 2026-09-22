# Agent Guide — AI Governance Audit Kit

**Read this before running anything in this directory.**

## What this kit is

A gated pipeline for auditing a corpus that is not yours, ending in a registry
the PAE Engine can open. Eight stages, four gates, five stdlib-only scripts.

## What it will not do, and will not be talked into

| Refusal | Why |
|---|---|
| assert a quality tier | only 54 of the rubric's 100 points are observable; inferring the rest fabricates a score |
| assert a copy relationship | copies come from explicit edges, never hashes or filenames (ADR-0012) |
| name a canonical in a cluster | mtime is a checkout artifact and a path is not provenance |
| determine a licence | guessing a client's licensing is the most expensive possible error |
| report a corpus quality percentage | it is a directional claim about a corpus measured once |

Each is enforced by a gate and pinned by a test. If a user asks for one of
these, explain the refusal and offer what the kit *can* say — which is usually
a count, a location, or a disclosed score.

## Running order

1. `prompts/stage-0-engagement-config.md` — write `config/audit.json` **with
   the corpus owner**. Do not copy the shipped roots; they describe the fixture.
2. `/inventory` — Gate 0. Read exclusions before counts.
3. `/cluster` — Stage 2.
4. `/score-observed` — Gate A.
5. `prompts/stage-4-governance-findings.md` — collate, rank, attribute.
6. `/handback` dry run — Gate C — then `--write`.
7. `claim_guard.py` on the report — Gate B — before anything ships.
8. `prompts/stage-7-closeout-and-remediation-plan.md`.

Gate B is listed after Gate C only because the handback is usually proved
before the report is written. Nothing ships until B passes.

## House rules

- **Check exit codes, not prose.** Every gate is a script with a documented
  exit code. 0 = pass, 1 = block, 2 = usage error.
- **Never advance past a block.** Fix at the source — the corpus or the config
  — never in the output.
- **Never hand-edit a generated file.** Both registry marker files are written
  together; `summary_drift` will catch a hand edit after the client has it.
- **Never quote a score against 100.** The denominator is 54.
- **Never quote a resource count without its exclusion partition.**

## Before you commit a change to this kit

```bash
for s in skills/*/scripts/*.py; do python3 "$s" --self-check; done
python3 -m unittest discover -s tests
```

Both must be clean. The self-checks run against `samples/`, which is mostly
negative fixtures — a gate proved only against the case it passes has not been
proved.

## Dependencies

Standard library, plus the PAE checkout this kit ships inside:
`pae_registry.identity` (UIDs), `pae_engine._lexical` (BM25F),
`pae_engine.validate` (Gate C). Each import failure names what it needed and
why it is not reimplemented. No network, no model, no embeddings.
