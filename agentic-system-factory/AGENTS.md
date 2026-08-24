# AGENTS.md — Codex / Coding-Agent Entry Point

> How a coding agent (Codex, Claude Code, or any harness) runs the agentic-system factory. Pairs with [`README.md`](README.md) (human overview), [`ARCHITECTURE.md`](ARCHITECTURE.md) (design), and [`PIPELINE_OVERVIEW.md`](PIPELINE_OVERVIEW.md) (flow).

---

## Ground rules

1. **Reference, don't duplicate.** Author design content by *running* the upstream prompts listed in [`referenced-prompts/README.md`](referenced-prompts/README.md). Only the 7 `templates/` are copied here.
2. **Gates are scripts, not trust.** Never declare a stage or the bundle "done" on your own judgment alone — run the relevant `scripts/*.py` and obey the exit code. Non-zero = refuse to advance and report the unmet conditions the script printed.
3. **The agnostic bundle is the source of truth.** Stage 7 code-gen is a transform; keep it version-neutral inside the named stack and flag drifting facts "verify against current docs."
4. **Capability ≠ safety.** Stage 5 must emit *both* Gate-B markers. A capable system with no safety eval does not pass.
5. **Write only inside the bundle directory.** Don't modify the factory's own files during a run.

## Gate commands (copy-paste)

```bash
# point BUNDLE at your working bundle directory
BUNDLE=./bundle

python3 scripts/check_gate.py --gate 0 "$BUNDLE"     # after Stage 0
python3 scripts/check_gate.py --gate A "$BUNDLE"     # after Stage 4
python3 scripts/check_gate.py --gate B "$BUNDLE"     # after Stage 5
python3 scripts/validate_bundle.py "$BUNDLE" \
  && python3 scripts/check_gate.py --gate C "$BUNDLE" \
  && python3 scripts/score_rubric.py "$BUNDLE"        # Stage 6 → production-ready iff all exit 0

# prove the tooling on the shipped fixtures (no setup needed)
python3 scripts/validate_bundle.py --self-check
python3 scripts/check_gate.py --self-check
python3 scripts/score_rubric.py --self-check
```

All scripts are Python standard library only — no `pip install`.

## Per-stage walkthrough

| Stage | Run prompt | Produce (in `$BUNDLE`) | Then verify |
|-------|------------|------------------------|-------------|
| 0 | `prompts/stage-0-justify.md` | `ARCHITECTURE.md §2` + `GATE-0` marker | `check_gate.py --gate 0` |
| 1 | `prompts/stage-1-scope.md` | `ARCHITECTURE.md §1` (blast radius!) | stage-1 checklist |
| 2 | `prompts/stage-2-topology.md` | `ARCHITECTURE.md §3` | stage-2 checklist |
| 3 | `prompts/stage-3-architecture.md` | `§4` + `agents/*.md` + `tools/*.md` + stack choice | stage-3 checklist |
| 4 | `prompts/stage-4-gates.md` | `GATE_DESIGN.md` + Gate-A markers | `check_gate.py --gate A` |
| 5 | `prompts/stage-5-eval.md` | `EVAL_HARNESS.md` + both Gate-B markers | `check_gate.py --gate B` |
| 6 | `prompts/stage-6-assemble.md` | `OBSERVABILITY/DISCLOSURE_MANIFEST/RUNBOOK/BUNDLE_MANIFEST/RUBRIC_SCORE` | validate + `--gate C` + `score_rubric.py` |
| 7 | `prompts/stage-7-codegen.md` + `stacks/<stack>.md` | `<system>-<stack>/` scaffold | preconditions: Gate C PASS + committed stack |

## Marker contract

Every gate reads HTML-comment markers. The single source of truth is [`templates/BUNDLE_MANIFEST_TEMPLATE.md`](templates/BUNDLE_MANIFEST_TEMPLATE.md) §2. When you fill a template, set its markers (each copied template has a "Machine-readable markers" footer telling you which). Two rules: markers count only **outside** code fences / inline code (the templates' fenced examples are inert — copying a template unfilled fails every gate), and two same-name markers with **different values fail closed** — delete stale examples rather than leaving them above the real value.

## Layout (what's tracked vs ignored)

- **Tracked:** everything in this directory except user run output. `samples/` holds **only** script fixtures, tracked on purpose (they back `--self-check`); real end-to-end factory outputs live in `worked-runs/` (tracked as worked examples, never wired into the scripts).
- **Ignored** (`.gitignore`): `bundle/`, `output/`, `*.local.md`, `__pycache__/`. Your generated bundles are yours — keep PII out of version control.

## Worked example

[`GOLD_STANDARD_RUN.md`](GOLD_STANDARD_RUN.md) traces the `deep-research-fleet` use case through stages 0→7, including a Gate-B failure→fix, with the real script commands and their PASS/FAIL output.
