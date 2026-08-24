# Agentic System Factory

> **Press-here-to-build for production-ready agentic systems.** Give it a use case; it interviews you, walks the 6-step authoring process, enforces hard gates 0/A/B/C as runnable scripts, and emits a framework-agnostic design bundle — plus, optionally, stack-specific scaffolding for any of the six supported stacks.

This is the **guided factory** (Phase 3) for the agentic-system authoring capability. It is the assembly line; [`authoring/system-patterns/`](../authoring/system-patterns/) is the manual that makes its output trustworthy. It **orchestrates and references** the repo's existing 42 `aiagent_*` design prompts + `done-definition/` + `production-monitoring/` + `responsible-ai-governance/` — it does not duplicate them (see [`referenced-prompts/README.md`](referenced-prompts/README.md)).

---

## Three ways to use it

- **Guided** (default) — run [`orchestrator_agentic_system.md`](orchestrator_agentic_system.md) (or `/author-agentic-system`). It interviews you, classifies which stage you're starting from, recommends ≤3 next stages, critiques each output, and enforces the gates by running the scripts.
- **Manual** — walk [`PIPELINE_OVERVIEW.md`](PIPELINE_OVERVIEW.md) yourself; pick stage prompts from [`prompts/`](prompts/). Gates are still enforced (run the scripts at each gate).
- **Surgical** — jump to one stage: `/justify-agent` (Gate 0), `/topology-pick` (Stage 2), `/agent-eval` (Stage 5), `/emit-stack-code` (Stage 7). Surgical jumps *between* gates, never *through* one.

## What you end up with (the terminal artifact)

A **framework-agnostic design bundle** (always): system design doc · per-agent specs · ACI tool specs · gate/policy spec + kill switch · eval harness (capability + safety) · observability plan · disclosure manifest · runbook · optional rules file. Schema + the machine-readable marker contract: [`templates/BUNDLE_MANIFEST_TEMPLATE.md`](templates/BUNDLE_MANIFEST_TEMPLATE.md). Optionally, **stack scaffolding** (Stage 7) once you commit a stack and pass Gate C.

## Build status

- ✅ Stages 0–7 prompts, orchestrator, 5 commands, 3 agents, 7 fill-in templates, **6 stack guides** (all target stacks).
- ✅ Gates enforced as **code-not-trust** by stdlib-only scripts (`scripts/`), proven on tracked sample bundles (`samples/`).
- ✅ Stage-7 code-gen for **all six target stacks** — Claude Agent SDK, LangGraph, OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, LlamaIndex (MCP assumed as the tool-interop layer across all).
- ✅ **Phase 4 (integration & discoverability) — done (2026-06-20):** routing rows added to the root `CLAUDE.md`; the 4 net-new `aiagent_*` prompts indexed in `PROMPT_INDEX.json`/`.md`; cross-links added from the sibling `authoring/*` READMEs; the three Anthropic engineering posts added to `domain-AI-ML/agentic-ai-systems/README.md`.
- ✅ **Phase 5 (validation) — done (2026-06-20):** the factory was exercised across four distinct topologies (single-agent, sequential pipeline, orchestrator-workers, evaluator-optimizer) plus a negative and the workflow-stop terminal; all pass the gate scripts and are wired into `--self-check` as permanent regression fixtures. See [`VALIDATION.md`](VALIDATION.md).
- ✅ **Hardening pass (2026-07-02) — adversarial script audit applied:** gate scripts are now game-resistant — markers inside code fences / inline code are **ignored** (a verbatim, unfilled template copy fails every gate; pinned by the `samples/templates-verbatim/` negative fixture), two same-name markers with different values **fail closed**, `SAFE-04: na` requires a real reason, values may contain `>`, a prose comment can no longer shadow the RUBRIC block, all three scripts gained argparse (`--help`, loud unknown-flag errors, consistent exit codes), and the Gate-0 `WORKFLOW-STOP` terminal is now a tracked fixture (`samples/workflow-stop/`). Every stage prompt gained a **False-Positive Prevention** block naming its marker-stuffing failure mode. See [`VALIDATION.md`](VALIDATION.md) §5.

## Three things to understand before you build

1. **Gate 0 can end the exercise — and that's a win.** The first job is to talk you *down* the complexity ladder. Most "I need an agent" cases are better as a deterministic workflow.
2. **Gates are scripts, not vibes.** `check_gate.py` and `score_rubric.py` parse machine-readable markers in your bundle and exit non-zero when a gate is unmet. The orchestrator refuses to advance on a non-zero exit. Capability and safety are **separate** gates.
3. **The agnostic bundle is the source of truth.** Stack code-gen (Stage 7) is a *transform* of it, version-neutral inside the named stack, with drifting facts flagged "verify against current docs."

## Setup / smoke test

Pure Python standard library — no install needed.

```bash
python3 scripts/validate_bundle.py --self-check
python3 scripts/check_gate.py --self-check
python3 scripts/score_rubric.py --self-check
```

All three should print `SELF-CHECK PASS` and exit 0 — demonstrating the gates bite (`samples/bundle-fail/` fails Gate B because it omits the safety eval, and `samples/templates-verbatim/` — unfilled template copies — fails every gate because fenced example markers don't count). A full worked run is in [`GOLD_STANDARD_RUN.md`](GOLD_STANDARD_RUN.md).

## Layout

```
agentic-system-factory/
├── README.md · ARCHITECTURE.md · PIPELINE_OVERVIEW.md · AGENTS.md   # three-layer docs (+ Codex entry)
├── orchestrator_agentic_system.md                                   # master conductor (3 modes)
├── GOLD_STANDARD_RUN.md                                             # one worked end-to-end run
├── prompts/        # stage-0…7 prompts (the 6-step process + optional code-gen)
├── stacks/         # 6 Stage-7 transform maps (claude-agent-sdk, langgraph, openai-agents-sdk, google-adk, microsoft-agent-framework, llamaindex)
├── commands/       # /author-agentic-system, /justify-agent, /topology-pick, /agent-eval, /emit-stack-code
├── agents/         # system-architect, security-gate-reviewer, eval-harness-writer
├── templates/      # 7 fill-in artifacts incl. BUNDLE_MANIFEST_TEMPLATE (the marker contract)
├── scripts/        # validate_bundle.py, check_gate.py, score_rubric.py (stdlib-only, --self-check)
├── samples/        # 7 fixtures: bundle-pass (93) + bundle-fail (trips Gate B) + single-agent-triage (91) + sequential-invoice-pipeline (91) + evaluator-optimizer-copy (87) + workflow-stop (Gate-0 terminal) + templates-verbatim (anti-gaming negative)
├── worked-runs/    # real end-to-end factory outputs (NOT fixtures — see worked-runs/README.md)
└── referenced-prompts/README.md   # pointers to the upstream prompts (D5: reference, don't copy)
```

## Related
- The manual this operationalizes: [`authoring/system-patterns/`](../authoring/system-patterns/) (6-step process, pattern index, 100-pt rubric, templates, gold-standard design).
- The design-advice library it orchestrates: [`domain-AI-ML/agentic-ai-systems/`](../domain-AI-ML/agentic-ai-systems/).
