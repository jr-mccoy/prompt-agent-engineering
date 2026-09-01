# Architecture Decision Records

Short records of decisions that are **settled**. They exist so that later
contributors — human or agent — do not reopen questions that have already been
argued and answered.

## Format

One file per decision, `NNNN-slug.md`, with four sections: **Status**,
**Context**, **Decision**, **Consequences**. Keep them short. If a decision is
later reversed, add a new ADR that supersedes the old one and mark the old one
`Superseded by ADR-NNNN` — do not rewrite history.

## Index

| ADR | Decision | Status |
|---|---|---|
| [0001](0001-engine-location.md) | The PAE Engine lives at `pae-engine/`, and the structure gate is amended deliberately | Accepted |
| [0002](0002-preserve-root-tests.md) | Root `tests/` stays the prompt/technique experimentation area | Accepted |
| [0003](0003-dependency-light-core.md) | Engine core is dependency-light and offline-capable; extras carry the rest | Accepted |
| [0004](0004-normalize-not-rewrite.md) | The registry normalizes heterogeneous source schemas instead of rewriting the corpus | Accepted |
| [0005](0005-quality-and-maturity-are-separate.md) | Quality and maturity are separate axes | Accepted |
| [0006](0006-staged-router-migration.md) | Routing migration is staged; `CLAUDE.md` is the interim canonical router | Accepted |
| [0007](0007-index-is-not-the-registry.md) | `PROMPT_INDEX.json` is not the registry, and its entry count is not a prompt count | Accepted |
| [0008](0008-generated-counts-control-plane.md) | Every published repository count is generated and declared in a CI-verified marker | Accepted |
| [0009](0009-engine-docs-naming-conventions.md) | `pae-engine/` is intentionally outside the corpus Markdown naming conventions | Accepted |

## Related

- [`../../ARCHITECTURE.md`](../../ARCHITECTURE.md) — current vs planned architecture
- [`../../ROADMAP.md`](../../ROADMAP.md) — sequencing
