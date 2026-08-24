# Referenced Prompts (vendored)

*For informational and research purposes only. Not financial, investment, or tax advice.*

This directory contains **pinned copies** of the analytical prompts the toolkit's stages
orchestrate. They are vendored here so the toolkit is **self-contained** — you can unpack the
`ai-investment-research-toolkit/` directory on its own and run the full loop without the rest of
the parent prompt repository.

## What's here

| Subdir | Count | Used by |
|---|---|---|
| `domain-finance/investing-research/` | 5 | Stage 2 (thesis, moat, catalysts, short thesis), Stage 6 (position sizing) |
| `domain-finance/valuation/` | 1 | Stage 2 (reverse-DCF expectations) |
| `domain-finance/crypto/` | 3 | Stage 2 (token valuation, on-chain metrics, smart-contract risk) |
| `domain-finance/options/` | 2 | Stage 2 (options structure, IV/Greeks) |
| `domain-finance/quant-fintech-data/` | 4 | Stage 3 (backtest critique, alt-data eval, signal-decay), Stage 6 (strategy pre-mortem) |
| `domain-finance/markets-macro/` | 1 | Stage 4/5 (sector rotation) |
| `domain-reasoning-craft/forecasting/` | 5 | Stage 3 (base rates, signal-vs-noise), Stage 5 (what-would-change-my-mind), Stage 7 (Brier tracker, calibration self-audit) |
| **Total** | **21** | |

## Provenance & maintenance

- These are **copies**, pinned at packaging time. The **canonical, maintained originals** live in
  the parent repo under `domain-finance/` and `domain-reasoning-craft/forecasting/`.
- Cross-references *inside* these vendored files (their `related_prompts:` frontmatter, "see also"
  links) still point at the parent repo's paths and are intentionally left unmodified — they are
  upstream pointers, not part of this toolkit's runtime.
- If you sync this toolkit back into the full repo, prefer the canonical originals; treat anything
  here as potentially behind the upstream version.

## How the toolkit references these

The stage prompts, agents, and commands reference these by their local path, e.g.
`referenced-prompts/domain-finance/investing-research/finance_investment_thesis_builder.md`.
Nothing in the toolkit depends on the parent repo being present.
