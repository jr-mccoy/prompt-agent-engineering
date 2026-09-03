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
| [0001](0001-engine-location.md) | The PAE Engine lives at `pae-engine/`, and the structure gate is amended deliberately | Accepted (amended by 0017) |
| [0002](0002-preserve-root-tests.md) | Root `tests/` stays the prompt/technique experimentation area | Accepted |
| [0003](0003-dependency-light-core.md) | Engine core is dependency-light and offline-capable; extras carry the rest | Accepted (amended: core is stdlib-only) |
| [0004](0004-normalize-not-rewrite.md) | The registry normalizes heterogeneous source schemas instead of rewriting the corpus | Accepted |
| [0005](0005-quality-and-maturity-are-separate.md) | Quality and maturity are separate axes | Accepted |
| [0006](0006-staged-router-migration.md) | Routing migration is staged; `CLAUDE.md` is the interim canonical router | Accepted (stage 2 begun in 0023) |
| [0007](0007-index-is-not-the-registry.md) | `PROMPT_INDEX.json` is not the registry, and its entry count is not a prompt count | Accepted |
| [0008](0008-generated-counts-control-plane.md) | Every published repository count is generated and declared in a CI-verified marker | Accepted |
| [0009](0009-engine-docs-naming-conventions.md) | `pae-engine/` is intentionally outside the corpus Markdown naming conventions | Accepted |
| [0010](0010-uid-and-public-id.md) | Identity is an immutable UID plus a mutable public ID | Accepted |
| [0011](0011-explicit-roots-and-shape-detection.md) | Membership is explicit roots plus shape detection; exclusions are anchored prefixes | Accepted |
| [0012](0012-one-record-per-copy.md) | One record per physical copy; copy edges require explicit evidence | Accepted (search behaviour amended by 0021) |
| [0013](0013-layered-ledger-and-generated-jsonl.md) | Identity lives in reviewed ledgers; the registry is generated JSONL | Accepted |
| [0014](0014-degraded-records-not-global-failure.md) | Metadata may degrade; identity may not | Accepted |
| [0015](0015-serving-policy-metadata.md) | The registry carries serving-policy metadata with a fail-closed default | Accepted |
| [0016](0016-sha256-checksum-contract.md) | Checksums are SHA-256 over a clearly defined payload | Accepted |
| [0017](0017-engine-package-identity.md) | The Engine is `prompt-agent-engineering` / `pae_engine` / `pae` | Accepted |
| [0018](0018-checkout-required-runtime.md) | The Engine requires a local checkout and bundles no corpus | Accepted |
| [0019](0019-runtime-serving-and-integrity.md) | Content is served whole, verified, and fails closed | Accepted |
| [0020](0020-consumer-vs-generator-validation.md) | Consumer validation is distinct from the generator's check | Accepted |
| [0021](0021-deterministic-lexical-search.md) | Search is deterministic, lexical, and reads metadata only | Accepted |
| [0022](0022-routing-by-max-aggregation.md) | Routing aggregates by maximum, and ambiguity is a result | Accepted |
| [0023](0023-executable-routing-migration.md) | Executable routing replaces table mechanics, not routing policy | Accepted |
| [0024](0024-bodies-only-through-registry-content.md) | Bundled bodies come only from `Registry.content()`, whole, with no expansion | Accepted |
| [0025](0025-token-estimate-byte-guarantee.md) | The token count is an estimate; the byte ceiling is the guarantee | Accepted |
| [0026](0026-rank-greedy-packing-and-ambiguity.md) | Rank-preserving greedy packing, with one promotion for an ambiguous route | Accepted |
| [0027](0027-structured-bundle-and-deterministic-render.md) | The structured bundle is the artifact; Markdown is the budgeted rendering | Accepted |
| [0028](0028-mcp-is-an-adapter.md) | MCP is an adapter, not a second Engine | Accepted |
| [0029](0029-optional-mcp-dependency.md) | Optional MCP dependency, and what "zero dependencies" now means | Accepted |
| [0030](0030-stdio-first-http-deferred.md) | stdio first; HTTP deferred | Accepted |
| [0031](0031-result-channel-split.md) | Model text and a body-free structured audit; bodies cross once | Accepted |
| [0032](0032-high-level-mcpserver.md) | High-level `MCPServer` with explicit `CallToolResult` | Accepted |
| [0033](0033-evaluation-runtime-separate-from-engine.md) | The evaluation runtime is separate from the Engine runtime | Accepted |
| [0034](0034-independent-benchmark-separate-from-tuning-data.md) | The independent benchmark is separate from tuning data | Accepted |
| [0035](0035-four-condition-comparison.md) | Four conditions, with D vs B as the primary comparison | Accepted |
| [0036](0036-raw-repository-baseline.md) | The raw-repository baseline is ripgrep, list and read | Accepted |
| [0037](0037-benchmark-leakage-isolation.md) | Benchmark isolation by construction, and the participant snapshot | Accepted |
| [0038](0038-frozen-plan-and-append-only-evidence.md) | A frozen plan and append-only evidence | Accepted |
| [0039](0039-statistical-primary-endpoint.md) | Paired task pass rate, exact McNemar, and the confirmatory repeat | Accepted |
| [0040](0040-public-performance-claim-governance.md) | Public performance-claim governance | Accepted |
| [0041](0041-author-reviewer-separation.md) | Author/reviewer separation and the masked authoring firewall | Accepted |
| [0042](0042-prompt-caching-on-the-paid-path.md) | Prompt caching on the paid path, and the token accounting it requires | Accepted |

## Related

- [`../../ARCHITECTURE.md`](../../ARCHITECTURE.md) — current vs planned architecture
- [`../../ROADMAP.md`](../../ROADMAP.md) — sequencing
