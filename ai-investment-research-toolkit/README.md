# AI Investment Research Toolkit

*For informational and research purposes only. Not financial, investment, or tax advice.
Nothing here places real-money trades.*

**Status: PHASES 1–7 BUILT (the paper loop is executable, wired end-to-end, + the gates are proven).**
All 8 stage prompts, the five skills (`data-source-adapter`, `pattern-knowledge-base`,
`prediction-journal`, `paper-trade-executor`, `output-guard`), the orchestrator, the 4 slash commands,
the 3 agents, and the 8 net-new `domain-finance` prompts exist and are registered in `PROMPT_INDEX`. As of
**Phase 6**, the four core skill scripts are working, stdlib-first Python: `validate_pattern.py` (Gate A),
`score_brier.py` (Brier + calibration + Gate C progress), `brokers.py` (paper simulator + Gate B + kill
switch + `load_config`), and `adapters.py` (manual-only point-in-time reads + `load_data_sources`).
**Phase 7** wired every stage prompt / command / the orchestrator to those scripts with exact CLIs and
added the executable glue the stages lacked — `build_snapshot.py` (immutable, look-ahead-safe Stage 1
universe writer), `screen_rank.py` (Gate A enforced at Stage 4 ranking time), and `brokers.py --report`
(read-only exposure). A hardening pass added more code-enforced guards: **journal integrity /
tamper-evidence** (`journal_integrity.py`, folded into `score_brier.py` so `gate_c.integrity_clean` is
required to unlock), **INDEX/record reconciliation** (`validate_pattern.py --reconcile`), **egress /
secret-leak scanning** before writes (`output-guard` / `egress_check.py`), and **config-level
`run_limits`** in `mandate.yaml` (stage-reentry / unavailable-retry / dossier-per-run caps,
orchestrator-enforced). Each script has a `--self-check`; the test suite now runs **35 tests**
(`tests/test_gates.py` + `tests/test_injection.py` + `tests/test_hardening.py`) and
[`DRY_RUN.md`](DRY_RUN.md) proves every gate fires on the [`samples/`](samples/) fixtures, with **no
real-money path** — the `LiveBrokerAdapter` stays a disabled stub (ARCHITECTURE §13 step 7, deferred
behind Gate C). See
[`PIPELINE_OVERVIEW.md`](PIPELINE_OVERVIEW.md) for live status and
[`ARCHITECTURE.md`](ARCHITECTURE.md) for the design/manifest.

## What this is (intended end state)

A portable, local-first toolkit you can drop into a private repo and run with Claude Code
or Codex on your own machine. It wraps the analytical prompts already in
[`referenced-prompts/domain-finance/`](referenced-prompts/domain-finance/) inside an **AI-native research loop**:

```
Mandate → Universe & Data → Deep Research → Pattern Knowledge Base
   → Screener → Monitor/Tripwires → Decision (PAPER only) → Journaling & Calibration
        ↑___________________________ feedback _______________________________|
```

**Self-contained.** Every analytical prompt the loop orchestrates (16 `domain-finance` +
5 `domain-reasoning-craft/forecasting`) is vendored under
[`referenced-prompts/`](referenced-prompts/), so this directory unpacks and runs with nothing
else from the parent repo. Those are pinned copies; the canonical, maintained originals live
in the main repo (see [`referenced-prompts/README.md`](referenced-prompts/README.md)).

## Hardening & security docs

A review pass (applying the repo's `domain-AI-ML/agentic-ai-systems` and `model-evaluation`
frameworks to this system) produced four robustness artifacts — read these before running with
real data or wiring live adapters:

- [`SECURITY.md`](SECURITY.md) — prompt-injection / untrusted-content threat model (filings, news,
  web, on-chain data feed agents that can act). Trust boundaries + a runnable checklist.
- [`FAILURE_MODES.md`](FAILURE_MODES.md) — prioritized failure-mode catalog (loops, runaway cost,
  hallucinated fills, gate bypass), each with a detection signal and bounded recovery.
- [`OBSERVABILITY_AND_EVAL.md`](OBSERVABILITY_AND_EVAL.md) — per-cadence run-log schema + an agent
  eval harness (tests the agents' *decisions*, not just the scripts `tests/test_gates.py` covers).
- [`skills/pattern-knowledge-base/references/leakage_and_skepticism_audit.md`](skills/pattern-knowledge-base/references/leakage_and_skepticism_audit.md)
  — leakage + result-skepticism audit that hardens Stage 3 / Gate A beyond what `validate_pattern.py`
  can check in code.

## Three things to understand before building

1. **Paper-first, by design.** Real-money execution is deliberately gated off behind a
   recorded calibration track record and a manual switch you control. The toolkit is built
   so you can run the *whole* loop against a simulated account first.
2. **The pattern knowledge base is the risky part.** "Find the details that predict
   winners" is where overfitting, survivorship bias, look-ahead bias, and data-snooping
   live. The discipline layer (hypothesis registration, out-of-sample validation,
   calibration/Brier scoring, kill criteria) is treated as load-bearing — see ARCHITECTURE.md.
3. **You bring the data.** It's data-source-agnostic: every market-data and brokerage
   touchpoint is an adapter seam you wire to a provider you supply. ARCHITECTURE.md lists
   what you'd need to acquire.

## Next step

The whole loop runs on paper today. To see the gates fire on the bundled fixtures (all stdlib,
no API or install needed):

```bash
python -m unittest discover -s tests -v     # 35 tests (gates + injection + hardening)
# then read DRY_RUN.md for the one-candidate paper walkthrough
```

To run it for real research, walk [`AGENTS.md`](AGENTS.md) or
[`PIPELINE_OVERVIEW.md`](PIPELINE_OVERVIEW.md), set `config/*.yaml`, paste data into `data/input/`,
and run the stage prompts (or `/investment-run` in Claude Code). The only thing left to build is
the real-money `LiveBrokerAdapter` — deliberately deferred behind Gate C
([`ARCHITECTURE.md`](ARCHITECTURE.md) §13 step 7).
