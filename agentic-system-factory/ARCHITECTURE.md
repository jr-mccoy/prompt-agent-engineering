# ARCHITECTURE — Agentic System Factory

> The factory's own design manifest: why it exists, the loop it runs, the gates it enforces, and the seams between its parts. (This is the factory's architecture — not the architecture of a system it produces; that lives in each emitted bundle's `ARCHITECTURE.md`.)

---

## 1. Purpose & scope

The factory turns a stated use case into a **production-ready agentic-system design bundle** (always) and, optionally, **stack-specific scaffolding**. It is the executable half of the agentic-system authoring capability, operationalizing the manual in [`../authoring/system-patterns/`](../authoring/system-patterns/).

**Owner decisions baked in:**
- Dual output (D1): agnostic bundle first; optional Stage-7 code-gen for a committed stack.
- Stage-7 stacks (all six D3 targets): **Claude Agent SDK, LangGraph, OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, LlamaIndex** (MCP assumed as the tool-interop layer across all; the agnostic bundle remains the source of truth and ships first).
- Gates enforced by **runnable scripts** (code-not-trust), not advisory checklists.
- Reference, never duplicate (D5): the 42 `aiagent_*` prompts + `done-definition/` + `production-monitoring/` + `responsible-ai-governance/` are orchestrated by path, not copied.

**In scope:** sequencing, classification, critique, gate enforcement, and bundling. **Out of scope:** re-authoring design advice (that's the library), and building/deploying the user's actual service (the bundle + scaffolding hand off to a coding agent).

## 2. The four design imperatives (from the verified research base)

1. **Talk users down the complexity ladder.** Stage 0 is a gate, not a formality.
2. **Tools are authority boundaries.** The moment an agent can act, least privilege + deterministic policy enforcement + data/control separation are mandatory.
3. **Capability ≠ safety ≠ valid evaluation.** Three independent gates; frontier models are unsafe by default in real-tool settings.
4. **Design to the converging standards** — OWASP ASI (threats), NIST (identity), MCP (interop).

These shape every stage, gate, and the rubric.

## 3. The factory loop (stage purpose → inputs → process → output → seams)

| Stage | Purpose | Inputs | Output | Gate |
|-------|---------|--------|--------|------|
| 0 Justify | agent vs workflow | use case | `ARCHITECTURE.md §2` + GATE-0 marker | **0** |
| 1 Scope | bounded, checkable spec | justified use case | `ARCHITECTURE.md §1` | — |
| 2 Topology | lowest-complexity topology | scope | `ARCHITECTURE.md §3` | — |
| 3 Architecture | agents/tools/seams + stack choice | topology | `§4` + `agents/*` + `tools/*` | — |
| 4 Gates | security/HITL/kill switch | blast radius + tools | `GATE_DESIGN.md` + Gate-A markers | **A** |
| 5 Eval | capability + safety | risk surface | `EVAL_HARNESS.md` + Gate-B markers | **B** |
| 6 Assemble | bundle + disclosure + score | all artifacts | full bundle + `RUBRIC_SCORE.md` | **C** |
| 7 Codegen (opt) | stack scaffolding | Gate-C bundle + stack | scaffolding | (Gate C precondition) |

**Seams between factory parts:**
- **Stage prompt → bundle artifact** — each stage writes a specific file/section (the marker contract makes this checkable).
- **Bundle → gate script** — `scripts/*.py` read the emitted markers; the orchestrator reads exit codes.
- **Agnostic bundle → stack scaffold** — Stage 7 transforms, never replaces; the bundle stays the source of truth.

## 4. Gate definitions + kill switch (code-not-trust)

Gates are enforced by `scripts/check_gate.py` and `scripts/score_rubric.py` parsing HTML-comment markers (contract: [`templates/BUNDLE_MANIFEST_TEMPLATE.md`](templates/BUNDLE_MANIFEST_TEMPLATE.md)). The orchestrator refuses to advance on a non-zero exit. Anti-gaming rules: markers inside code fences / inline code are **ignored** (template examples can never pass a gate), and two same-name markers with different values **fail closed** (a stale example can't mask the real value). The scripts verify marker presence and shape, not truth — substance behind each marker is the orchestrator critique's job (see the stage prompts' False-Positive Prevention blocks).

| Gate | Guards | Pass condition | Enforced by |
|------|--------|----------------|-------------|
| 0 Justification | Stage 1 | `GATE-0` justified or workflow-stop (+ non-placeholder justification) | `check_gate.py --gate 0` |
| A Security | Stage 5 sign-off | SAFE-01 & SAFE-02 `enforced`, SAFE-04 `enforced` or `na: <reason>`, defense-in-depth 3-layers, kill switch present | `check_gate.py --gate A` |
| B Evaluation | "production-ready" stamp | **both** `GATE-B-CAPABILITY` and `GATE-B-SAFETY` present | `check_gate.py --gate B` |
| C Disclosure | deployable / Stage 7 | 6 disclosure dims + rollback + observability + rubric ≥75 (security ≥14, Gate B passing) | `check_gate.py --gate C` + `score_rubric.py` |

**Kill-switch analogue for the factory itself:** a Stage-0 `WORKFLOW-STOP` halts the pipeline cleanly — "don't build an agent" is a valid, common terminal state.

**Load-bearing rule (in `score_rubric.py`):** failing `cat3_security ≥ 14` *or* Gate B caps the tier at "Needs work" regardless of total — the security and eval gates are this system's False-Positive-Prevention equivalent.

## 5. Reference-don't-rebuild map

The factory is ~70% assembly. Each stage's `References` section and [`referenced-prompts/README.md`](referenced-prompts/README.md) point to the upstream prompt that authors that part (`aiagent_complexity_ladder_gate` for Stage 0, `aiagent_hard_gates_designer` for Stage 4, `aiagent_agentic_safety_eval_layer` for Stage 5, `done_definition_*` for the loop, `rai_documentation_suite_orchestrator` for disclosure, etc.). The only copied files are the 7 fill-in templates (self-containment).

## 6. Verification checklist (for the factory itself)

- [ ] `validate_bundle.py --self-check`, `check_gate.py --self-check`, `score_rubric.py --self-check` all exit 0.
- [ ] `samples/bundle-fail/` fails Gate B and is capped by the rubric (the gates demonstrably bite).
- [ ] `samples/templates-verbatim/` (verbatim, unfilled template copies) fails every gate — the markers cannot be satisfied by copying the templates.
- [ ] Scripts are stdlib-only (no third-party imports).
- [ ] No upstream prompt is copied into the factory (only the 7 templates).
- [ ] The orchestrator enforces every gate by running a script and reading its exit code.

## 7. Glossary

- **Bundle** — the directory of design artifacts the factory emits; the terminal deliverable.
- **Marker** — an HTML-comment status flag (`<!-- GATE-0: JUSTIFIED -->`) that the scripts parse.
- **Gate (0/A/B/C)** — a code-enforced checkpoint; non-zero script exit = refuse to advance.
- **Topology (TP-01…TP-09)** — the complexity-ladder catalog in `authoring/system-patterns/SYSTEM_PATTERN_INDEX.md`.
- **Agnostic bundle vs stack scaffold** — framework-neutral design (source of truth) vs a Stage-7 transform for a named stack.
