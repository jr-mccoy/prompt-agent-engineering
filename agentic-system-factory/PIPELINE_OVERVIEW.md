# PIPELINE OVERVIEW — Agentic System Factory

> The visual flow, stage I/O, gate truth table, terminal artifacts, and runtime modes. Walk this yourself for **manual** mode.

---

## Flow

```
                         ┌─────────────────────────────────────────────┐
   use case  ───────────▶│ STAGE 0  Justify (complexity ladder)        │
                         └───────────────┬─────────────────────────────┘
                          GATE 0 │ justified          │ workflow-stop
                                 ▼                     └────────▶ STOP (build a workflow — a win)
   ┌─────────┐   ┌──────────┐   ┌────────────────┐
   │ STAGE 1 │──▶│ STAGE 2  │──▶│ STAGE 3         │  scope → topology → architecture (+ stack choice)
   │ Scope   │   │ Topology │   │ Architecture    │
   └─────────┘   └──────────┘   └───────┬─────────┘
                                        ▼
                         ┌───────────────────────────┐
                         │ STAGE 4  Gates             │  GATE A: SAFE-01/02 enforced + kill switch
                         └───────────────┬───────────┘   (refuse → back to Stage 4)
                                         ▼
                         ┌───────────────────────────┐
                         │ STAGE 5  Eval              │  GATE B: capability AND safety
                         └───────────────┬───────────┘   (refuse → back to Stage 5)
                                         ▼
                         ┌───────────────────────────┐
                         │ STAGE 6  Assemble          │  GATE C: 6 dims + rollback + rubric ≥75
                         └───────────────┬───────────┘   ──▶ AGNOSTIC BUNDLE (source of truth)
                         stack committed? │ yes
                                          ▼
                         ┌───────────────────────────┐
                         │ STAGE 7  Codegen (optional)│  scaffolding for any of 6 stacks (Claude SDK | LangGraph | OpenAI | ADK | MS AF | LlamaIndex)
                         └───────────────────────────┘
```

## Stage I/O

| # | Stage | Inputs | Outputs | Gate |
|---|-------|--------|---------|------|
| 0 | Justify | use case | `ARCHITECTURE.md §2` + GATE-0 marker | 0 |
| 1 | Scope | justified use case | `ARCHITECTURE.md §1` (incl. blast radius) | — |
| 2 | Topology | scope | `ARCHITECTURE.md §3` + primitives | — |
| 3 | Architecture | topology | `§4` + `agents/*` + `tools/*` + stack choice | — |
| 4 | Gates | blast radius + tools | `GATE_DESIGN.md` + Gate-A markers | A |
| 5 | Eval | risk surface | `EVAL_HARNESS.md` + both Gate-B markers | B |
| 6 | Assemble | all artifacts | `OBSERVABILITY/DISCLOSURE/RUNBOOK/BUNDLE_MANIFEST/RUBRIC_SCORE` | C |
| 7 | Codegen | Gate-C bundle + stack | stack scaffold | (Gate C precondition) |

## Gates & kill-switch (truth table)

| Gate | Script | Pass condition | On fail |
|------|--------|----------------|---------|
| 0 | `check_gate.py --gate 0` | justified (+ honest justification) or workflow-stop | refuse → Stage 0 (or STOP cleanly) |
| A | `check_gate.py --gate A` | SAFE-01 & SAFE-02 enforced + SAFE-04 enforced or `na: <reason>` + defense-in-depth + kill switch | refuse → Stage 4 |
| B | `check_gate.py --gate B` | capability **and** safety markers present | refuse → Stage 5 |
| C | `check_gate.py --gate C` + `score_rubric.py` | 6 dims + rollback + observability + ≥75 (security ≥14, Gate B ok) | refuse → Stage 6 |

> A read-only system still earns a full Gate A when its inputs are untrusted (see the worked run).
>
> Markers count only when **live**: the scripts ignore markers inside code fences / inline code (the templates' fenced examples are inert), and two same-name markers with different values fail the gate closed.

## Where outputs land

```
<bundle>/
├── BUNDLE_MANIFEST.md   RUBRIC_SCORE.md
├── ARCHITECTURE.md      GATE_DESIGN.md     EVAL_HARNESS.md
├── OBSERVABILITY.md     DISCLOSURE_MANIFEST.md   RUNBOOK.md   [CLAUDE.md]
├── agents/<name>.md     tools/<name>.md
└── (Stage 7) <system>-<stack>/   # optional scaffolding
```

## Runtime modes

| Mode | Driver | How |
|------|--------|-----|
| Claude Code (guided) | `orchestrator_agentic_system.md` / `/author-agentic-system` | interview → classify → recommend ≤3 → critique → gate scripts |
| Claude Code (surgical) | `/justify-agent`, `/topology-pick`, `/agent-eval`, `/emit-stack-code` | one stage; gates between still apply |
| Codex / other agents | [`AGENTS.md`](AGENTS.md) | per-stage walkthrough + copy-paste gate commands |
| Manual | this file | walk the stages; run the scripts at each gate yourself |
