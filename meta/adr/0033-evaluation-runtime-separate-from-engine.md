# ADR-0033 — The evaluation runtime is separate from the Engine runtime

## Status

Accepted. Implemented in Phase 7.

## Context

The Engine's identity is a set of negative guarantees: zero unconditional
dependencies ([ADR-0003](0003-dependency-light-core.md)), reads a local checkout
and downloads nothing ([ADR-0018](0018-checkout-required-runtime.md)), never
writes ([ADR-0019](0019-runtime-serving-and-integrity.md)). CI enforces all
three.

An evaluation harness is the opposite of every one of them. It calls provider
APIs over the network, needs credentials, spends money, and writes result files.

Sharing a package, an import path or a release cadence between the two would put
`anthropic` and `openai` one dependency-resolution step away from a runtime
whose entire selling point is that installing it resolves to nothing but the
standard library.

## Decision

The harness is its own project at `pae-engine/evaluation/`, distribution
`pae-eval`, import namespace `pae_eval`, versioned independently starting at
`0.1.0.dev0`.

- **Location.** `structure.yml` inspects depth 1 only and permits the literal
  `pae-engine`, so a nested directory is invisible to the gate.
  [ADR-0001](0001-engine-location.md) anticipated exactly this. A new root
  `benchmarks/` or `evaluation/` would be rejected, which is why neither is
  proposed.
- **Packaging.** `packages.find` is scoped to `src/`, so the wheel cannot
  contain it, and `MANIFEST.in` gains an explicit `prune evaluation` as defence
  in depth. Both artifacts are asserted clean by test.
- **Import direction.** `pae_eval` may import `pae_engine`. `pae_engine` may
  never import `pae_eval`, and no `pae` subcommand or `pae mcp` code path may
  reach it. Enforced by an AST scan over the Engine sources.
- **Command surface.** `python -m pae_eval`, never `pae eval`. The boundary
  should be visible in the thing people type.
- **Dependencies.** The harness itself declares none. Providers, MCP and SciPy
  are optional extras. `plan`, `validate-benchmark`, fake-provider runs, the
  statistics core and reporting all work with nothing installed.

The Engine version does not move because evaluation infrastructure was added
outside its runtime.

## Consequences

- The Engine's zero-dependency assertion keeps passing unchanged.
- The harness can take any dependency it needs without negotiating with the
  Engine's constraints.
- Two version numbers to track. Worth it: the alternative couples a benchmark
  revision to an Engine release for no reason.
- Someone will eventually propose `pae eval` as a convenience. The answer is no;
  the reason is this ADR.
