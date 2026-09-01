# ADR-0025 — The token count is an estimate; the byte ceiling is the guarantee

## Status

Accepted. Implemented in Phase 5 (`pae_engine.context`).

## Context

A budgeted bundle has to answer "does this fit?", and there is no
provider-independent tokenizer to answer it with. The Engine has zero runtime
dependencies ([ADR-0003](0003-dependency-light-core.md)) and is not going to
acquire a tokenizer SDK to gain one.

Candidate estimators were calibrated against real BPE tokenizers over all 4,888
addressable bodies in the live corpus (in disposable scratch work; no tokenizer
entered the package). The corpus averages **4.367 UTF-8 bytes per token**.

| Estimator | median error | worst underestimate | share underestimated | min ratio |
|---|---:|---:|---:|---:|
| `ceil(chars/4)` | +170 | 840 | 12.4% | 0.761 |
| `ceil(bytes/4)` | +189 | 793 | 10.8% | 0.771 |
| `ceil(bytes/3.5)` | +532 | 283 | 0.9% | 0.881 |
| `ceil(bytes/3)` | +988 | 0 | 0.0% | 1.028 |
| `ceil(bytes/2)` | +2,621 | 0 | 0.0% | 1.541 |

`bytes/3` looks safe and is not. Its 2.8% margin is a property of this corpus,
not of the arithmetic: markdown-heavy text lands at exactly 3.00 bytes/token
(ratio 1.000, zero margin), and plausible content defeats it outright — Korean
0.893, Arabic 0.822, emoji 0.470, base64 0.457, hex 0.381. Buying that illusory
safety costs a 45.7% median overestimate, roughly a third of every bundle left
empty.

Per-resource error also overstates the risk. Measured at **bundle** level,
where errors average out, `bytes/4` overflowed a stated token budget in 0–2.5%
of bundles with a worst case of +291 tokens (3.6% of an 8k budget).

## Decision

Three quantities, never conflated.

**`budget_bytes` is exact and enforced.** A hard ceiling on the rendered
bundle's UTF-8 length, capped by an engine-wide `MAX_BUNDLE_BYTES` of 4 MiB
mirroring the per-resource `MAX_CONTENT_BYTES`. This is the only promise the
compiler can actually keep, because bytes are measured rather than modelled.

**`budget_estimated_tokens` is advisory and named as an estimate.**
`ApproximateTokenCounterV1` is `ceil(utf8_bytes / 4)`, ships with
`exact = False`, and is called `utf8-bytes-div4` rather than after any provider.
No field is named `tokens`. The docstring states plainly that it is not a safe
upper bound, and a test asserts the public prose never claims otherwise.

**Exactness is available by injection.** A `TokenCounter` protocol —
`name`, `version`, `exact`, `count(text)` — lets a caller supply a real
tokenizer. `estimator_exact` then propagates into `BudgetReport`, and the
counter's identity enters the bundle hash so two counters cannot produce the
same bundle identity from different arithmetic.

When only a token limit is given and the default counter is in use, the byte
ceiling is derived as `tokens * 4`, which is *exactly* equivalent for this
estimator (`ceil(b/4) <= T` iff `b <= 4T`) and says nothing about any model's
real tokenizer. `byte_ceiling_source` reports which of `explicit`,
`derived_from_default_estimator` or `engine_safety_ceiling` applied.

The budget covers the **entire canonical Markdown rendering** — framing,
manifest, provenance, resource headers, markers, bodies, omission summary,
warnings and hash — not the bodies alone. Wrapper overhead is real: measured
during design at roughly 550 tokens fixed plus ~104 per included resource,
which is 27.5% of a 2,000-token budget before any body. Those figures are
design measurements and appear nowhere in the code; the shipped compiler
derives overhead by subtracting measured body tokens from the measured render.

## Consequences

A caller with a real tokenizer gets an exact fit. A caller without one gets an
honest estimate plus an exact byte bound, and the bundle never claims more than
that. A budget below 4,000 estimated tokens still compiles but carries a
`low_estimated_token_budget` warning, because the corpus median body is ~2,400
estimated tokens and 69.6% exceed 2,000 — at 2k the packer retained the top hit
in 4.3% of cases. A budget that cannot hold the framing with zero bodies raises
`BudgetTooSmall`, which is a configuration error rather than an empty result.

Both new errors map to the existing exit 2. No new exit code was allocated.
