# BUNDLE MANIFEST — `<system name>`

> The index of an emitted **design bundle** and the **single source of truth for the machine-readable markers** the factory's `scripts/*.py` read to enforce gates 0/A/B/C and score the rubric. Emit this as `BUNDLE_MANIFEST.md` at the root of your bundle directory. The scripts verify the *actual artifact files and their markers* — this manifest is the human-readable index, not a thing the scripts trust on its own.

**System:** `<name>` · **Bundle version:** `<…>` · **Date:** `<…>` · **Stack committed (Stage 7):** `<none | claude-agent-sdk | langgraph | openai-agents-sdk | google-adk | microsoft-agent-framework | llamaindex>`

---

## 1. Artifacts in this bundle (the 9 + 2)

`scripts/validate_bundle.py` checks each required file is present and non-empty.

| # | Artifact | File (required name) | From template | Required? |
|---|----------|----------------------|---------------|-----------|
| — | Bundle index | `BUNDLE_MANIFEST.md` | this file | ✅ |
| 1 | System design doc | `ARCHITECTURE.md` | `ARCHITECTURE_TEMPLATE.md` | ✅ |
| 2 | Per-agent specs (≥1) | `agents/<name>.md` | `AGENT_SPEC_TEMPLATE.md` | ✅ |
| 3 | Tool specs (≥1) | `tools/<name>.md` | `TOOL_SPEC_TEMPLATE.md` | ✅ |
| 4 | Gate / policy spec | `GATE_DESIGN.md` | `GATE_DESIGN_TEMPLATE.md` | ✅ |
| 5 | Eval harness | `EVAL_HARNESS.md` | `EVAL_HARNESS_TEMPLATE.md` | ✅ |
| 6 | Observability plan | `OBSERVABILITY.md` | — (free-form) | ✅ |
| 7 | Disclosure manifest | `DISCLOSURE_MANIFEST.md` | `DISCLOSURE_MANIFEST_TEMPLATE.md` | ✅ |
| 8 | Runbook | `RUNBOOK.md` | — (free-form) | ✅ |
| 9 | Rules file (if a coding agent builds it) | `CLAUDE.md` / `AGENTS.md` | — | optional |
| — | Rubric score | `RUBRIC_SCORE.md` | §4 below | ✅ |

---

## 2. The marker contract (what each gate script greps for)

Markers are **HTML comments** — invisible when rendered, trivial to parse. Place each in the file named. Two anti-gaming rules the scripts enforce: (1) markers inside code fences / inline code are **ignored** — the fenced examples below (and in every template) can never pass a gate; emit live markers in your artifact; (2) two same-name markers with **different values fail the gate closed** — delete stale examples instead of leaving them above the real value.

### Gate 0 — Justification (in `ARCHITECTURE.md`)
```
<!-- GATE-0: JUSTIFIED -->        or   <!-- GATE-0: WORKFLOW-STOP -->
<!-- JUSTIFICATION-START -->
<the one-sentence written reason an agent beats a deterministic workflow>
<!-- JUSTIFICATION-END -->
```
- `JUSTIFIED` ⇒ the justification block must be present and non-placeholder (no `<…>`).
- `WORKFLOW-STOP` ⇒ a valid terminal state; the design correctly stopped at a workflow.

### Gate A — Security / OWASP ASI (in `GATE_DESIGN.md`)
```
<!-- SAFE-01: enforced -->                 data/control separation   (LOAD-BEARING: must be enforced)
<!-- SAFE-02: enforced -->                 deterministic policy enforcement (LOAD-BEARING: must be enforced)
<!-- SAFE-04: enforced -->                 least-privilege tools     (enforced | na: <reason>)
<!-- DEFENSE-IN-DEPTH: 3-layers -->        input-detection + instruction-hierarchy + deterministic enforcement
<!-- KILL-SWITCH: present -->              an explicit code-level halt exists
```
- A marker value of `na` is allowed **only** for SAFE-04 and must be written `na: <reason>`. SAFE-01, SAFE-02, and the kill switch are non-waivable.

### Gate B — Evaluation (in `EVAL_HARNESS.md`) — two independent markers, both required
```
<!-- GATE-B-CAPABILITY: present -->        ABC-valid capability suite
<!-- GATE-B-SAFETY: present -->            real-tool safety eval (8 OpenAgentSafety categories)
```
- **Missing either ⇒ Gate B FAIL.** Capability ≠ safety; a capable, unevaluated-for-safety system is not production-ready.

### Gate C — Production-readiness / disclosure (in `DISCLOSURE_MANIFEST.md` + `RUNBOOK.md` + `OBSERVABILITY.md`)
```
<!-- DISCLOSURE-DIM-1: complete -->   …   <!-- DISCLOSURE-DIM-6: complete -->   (all six, in DISCLOSURE_MANIFEST.md)
<!-- ROLLBACK: present -->            (in RUNBOOK.md)
```
- `OBSERVABILITY.md` must exist and be non-empty.

---

## 3. Gate status (filled by the curator; verified by the scripts)

| Gate | Marker location | Pass condition | Status |
|------|-----------------|----------------|--------|
| 0 Justification | `ARCHITECTURE.md` | justified or workflow-stop | `<…>` |
| A Security | `GATE_DESIGN.md` | SAFE-01/02 enforced + kill switch | `<…>` |
| B Evaluation | `EVAL_HARNESS.md` | capability **and** safety markers | `<…>` |
| C Disclosure | `DISCLOSURE_MANIFEST.md` + `RUNBOOK.md` | 6 dims + rollback + observability | `<…>` |

---

## 4. Rubric score block (in `RUBRIC_SCORE.md`)

`scripts/score_rubric.py` parses this exact block. Categories and maxima mirror `authoring/system-patterns/SYSTEM_QUALITY_RUBRIC.md` (100 pts). **Load-bearing minimums:** `cat3_security ≥ 14` and Gate B must pass; failing either caps the tier at "Needs work" regardless of total.

```
<!-- RUBRIC
cat1_justification: 0      # /15  agent justification & complexity-appropriateness
cat2_topology: 0          # /15  topology fit & primitive correctness
cat3_security: 0          # /20  security gate vs OWASP ASI   (LOAD-BEARING ≥14)
cat4_eval: 0              # /20  eval validity (ABC) + real-tool safety
cat5_durability: 0        # /10  durability / observability / cost
cat6_documentation: 0     # /10  documentation completeness (3-layer + disclosure)
cat7_crosslink: 0         # /10  cross-link hygiene / no-fabrication
-->
```
- Tiers: **Exemplary** ≥ 90 · **Production-ready** 75–89 · **Needs work** < 75 *or* a load-bearing gate failed.
