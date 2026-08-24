# GOLD STANDARD RUN — `deep-research-fleet`, End to End

> One worked run of the factory on a realistic use case, showing every gate firing — including a **Gate-B failure → fix** — with the **actual `scripts/*.py` commands and their real PASS/FAIL output**. The before/after bundle states are the shipped fixtures `samples/bundle-fail/` (no safety eval) and `samples/bundle-pass/` (complete), so you can reproduce every command below.
>
> Same use case as the design-side worked example in `authoring/system-patterns/templates/GOLD_STANDARD_AGENTIC_SYSTEM.md` — here we run it through the *factory* and its scripts.

**Use case:** a deep-research assistant that, given a question, returns a synthesized, fully-cited answer from many web sources. Canonical **orchestrator-workers (TP-06)**; untrusted web content + multi-agent ⇒ it exercises the hardest gates.

---

## Stage 0 — Justify (Gate 0)

Walk the ladder: not a function, not a single call, and a fixed fan-out can't adapt because the number/shape of subtopics is only knowable after initial retrieval. → an agent is justified. We record the marker + justification in `ARCHITECTURE.md §2`:

```
<!-- GATE-0: JUSTIFIED -->
<!-- JUSTIFICATION-START -->
An agent is required because the number and shape of research subtopics is input-dependent
and only knowable after initial retrieval ...; a deterministic workflow cannot, because it
would have to fix the subtopic set and source count in advance.
<!-- JUSTIFICATION-END -->
```

```bash
$ python3 scripts/check_gate.py --gate 0 samples/bundle-pass
PASS  Gate 0  samples/bundle-pass
```

## Stages 1–3 — Scope, Topology, Architecture

- **Scope:** every claim cites a retrieved source; **blast radius = read-only web access** (but untrusted content). Recorded in `ARCHITECTURE.md §1`.
- **Topology:** TP-06 orchestrator-workers (control = model, structure = parallel, plan = runtime). `§3`.
- **Architecture:** 1 orchestrator + N capped workers + 1 synthesizer; tools `research_sources_search` + `research_page_fetch` (read-only); per-worker isolated context returning condensed cited summaries. One `AGENT_SPEC` each (`agents/`), one `TOOL_SPEC` each (`tools/`). Stack-selection: **deferred** (`none`) — we'll stop at the agnostic bundle.

## Stage 4 — Gates (Gate A)

Blast radius is read-only, but the web is untrusted, so it earns a **full** Gate A: data/control separation (page text is data, never instructions), a deterministic tool allowlist `{search, fetch}`, least-privilege read-only tools, caps (`MAX_WORKERS`, `MAX_FETCHES`), and a `config.halt` kill switch. Markers set in `GATE_DESIGN.md`.

```bash
$ python3 scripts/check_gate.py --gate A samples/bundle-pass
PASS  Gate A  samples/bundle-pass
```

## Stage 5 — Eval (Gate B) — the failure → fix

**First attempt:** we wrote the ABC-valid capability suite (20 held-out questions, citation-coverage grader, trivial-agent baseline) and called it done. The factory caught the missing safety half. This is the state captured in `samples/bundle-fail/`:

```bash
$ python3 scripts/check_gate.py --gate B samples/bundle-fail
FAIL  Gate B  samples/bundle-fail
        - GATE-B-SAFETY marker missing (real-tool safety eval) — capability != safety
[exit 1]
```

The orchestrator **refuses to advance**. Capability ≠ safety. We add the separate real-tool safety eval aimed at the actual risk surface (untrusted page content): privacy-breach / malicious-content / harmful-decision scenarios, run benign + adversarial, rule-based + LLM-judge detection. That completes the harness (`samples/bundle-pass/`):

```bash
$ python3 scripts/check_gate.py --gate B samples/bundle-pass
PASS  Gate B  samples/bundle-pass
[exit 0]
```

> This is the single most instructive moment in the run: a capable, well-built system was **one marker away from shipping unsafe**, and the gate — enforced in code, not trust — stopped it.

## Stage 6 — Assemble, validate, score (Gate C)

We emit the observability plan, the 6-dimension disclosure manifest (including #6, reporting evals *actually run*), the runbook with a rollback path, the bundle index, and the rubric block. Then run the full Stage-6 gate:

```bash
$ python3 scripts/validate_bundle.py samples/bundle-pass \
    && python3 scripts/check_gate.py --gate C samples/bundle-pass \
    && python3 scripts/score_rubric.py samples/bundle-pass
PASS  samples/bundle-pass: all required artifacts present and non-empty
PASS  Gate C  samples/bundle-pass
PASS  samples/bundle-pass: 93/100 — Exemplary
[exit 0]
```

The bundle is **production-ready as a design**: 93/100, both load-bearing gates pass.

### Contrast: what "Needs work" looks like

The incomplete bundle scores high on paper but the load-bearing override caps it:

```bash
$ python3 scripts/score_rubric.py samples/bundle-fail
FAIL  samples/bundle-fail: 84/100 — Needs work (load-bearing gate failed)
        - Gate B fails (capability and/or safety marker missing) — caps tier
[exit 1]
```

84/100 but **not** production-ready — exactly the "production-ready overclaim" the research warns about, prevented mechanically.

## Stage 7 — Code-gen (optional, not exercised here)

No stack was committed (stack-selection = `none`), so the run terminates at the agnostic bundle — the source of truth. *If* the user had committed LangGraph, `/emit-stack-code` would first re-check Gate C, then transform via `stacks/langgraph.md`: the orchestrator→workers map compiles to a `StateGraph` with a `Send`-based fan-out `[verify against current docs]`; the deterministic allowlist becomes a guard node; `config.halt` becomes a `halt` channel checked before action nodes; loop bounds become a recursion limit. Version-sensitive facts are flagged "verify against current docs," never asserted.

## Reproduce the whole thing

```bash
python3 scripts/validate_bundle.py --self-check
python3 scripts/check_gate.py --self-check
python3 scripts/score_rubric.py --self-check
# each prints SELF-CHECK PASS and exits 0; bundle-fail demonstrably fails Gate B.
```

## What to copy from this run

1. **Gate 0 is won or lost on one honest sentence.** The justification is short but decisive.
2. **Blast radius drives the gates** — read-only still earned a full Gate A because the input is untrusted.
3. **The Gate-B failure is the point.** Capability and safety are separate, code-enforced gates; the factory caught a one-marker gap that "looked done."
4. **The rubric's load-bearing override** turns "84/100, ship it" into "Needs work" — mechanically, not by reviewer goodwill.
5. **The agnostic bundle is the deliverable**; code-gen is an optional, version-neutral transform.
