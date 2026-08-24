# ARCHITECTURE — `<system name>`

> Fill this during stages 1–3 (see `../PIPELINE_OVERVIEW.md` and `../prompts/`). It is the load-bearing decisions doc — the "why," not just the "what." Keep it honest: record rejected options and open questions. *(Self-contained copy of `authoring/system-patterns/templates/ARCHITECTURE_TEMPLATE.md` with factory marker footers added.)*

**System:** `<name>`
**Author / date:** `<who, when>`
**Status:** `draft | reviewed | approved`

---

## 1. Use case & scope (Step 1)

- **One-sentence use case:** `<…>`
- **Job-to-be-done:** `<the underlying job the user is hiring this to do>`
- **Success criteria (observable gates, not vibes):**
  - [ ] `<criterion 1, checkable>`
  - [ ] `<criterion 2, checkable>`
- **Inputs:** `<type, format, volume, trust level — flag untrusted external content>`
- **Outputs:** `<type, format, consumer>`
- **Autonomy level:** `<acts | recommends-only>`
- **Blast radius (worst case action):** `<e.g., reads web only / writes files / sends email / moves money>`
- **Out of scope:** `<explicit non-goals>`

## 2. Step-0 justification (the gate)

> Required. If you can't complete this honestly, stop and recommend a workflow.

> *"An agent is required because ____, and a deterministic workflow cannot because ____."*

- **Rung chosen on the complexity ladder:** `<TP-01…TP-09>`
- **Rejected lower rungs and why:** `<…>`
- **Accepted cost multiple:** `<~4× single / ~15× multi> for <stated value>`

## 3. Topology & primitives (Step 2)

- **Topology:** `<TP-0X — name>` (aliases: `<vendor names>`)
- **Selection-variable rationale:** control = `<code|model>`; structure = `<sequence|parallel|conversation>`; plan = `<known|runtime>`.
- **Primitives used:**
  | Primitive | Present? | Notes |
  |-----------|----------|-------|
  | Model call(s) | | `<which models, right-sized>` |
  | Tool(s) | | `<count, namespaced groups>` |
  | State | | `<shared? typed? persisted where?>` |
  | Memory | | `<in-context | external notes | RAG>` |
  | Agent(s) | | `<how many, roles>` |
  | Handoff | | `<deterministic route | agent-decided>` |
  | Guardrail(s) | | `<positions: input/tool/output/final>` |
  | Tracing | | `<per-agent + whole-system>` |
  | HITL checkpoint | | `<where, approval vs feedback>` |

## 4. Architecture (Step 3)

### 4.1 Component / agent map
```
<ASCII or mermaid: orchestrator → workers, routes, loops, gates>
```
- Per-agent details → one [`AGENT_SPEC_TEMPLATE.md`](../../templates/AGENT_SPEC_TEMPLATE.md) each.
- Per-tool details → one [`TOOL_SPEC_TEMPLATE.md`](../../templates/TOOL_SPEC_TEMPLATE.md) each.

### 4.2 Seams (where control/data crosses a boundary)
| Seam | From → To | What crosses | Validation at the seam |
|------|-----------|--------------|------------------------|
| | | | |

### 4.3 Context / durability strategy
- **Per-hop context decision:** `<full-raw | summary | fresh-instruction-only>` and why.
- **Long-horizon techniques applied:** `[ ] compaction  [ ] agentic note-taking  [ ] sub-agent isolation`
- **State persistence:** `<store, checkpoint cadence, resume design>`

### 4.4 Cost / model right-sizing
| Step / agent | Model | Why | Est. tokens/run |
|--------------|-------|-----|-----------------|
| | | | |

### 4.5 System-prompt "altitude"
- `<note where prompts are intentionally heuristic vs prescriptive>`

## 5. Failure modes (seed; expand in the eval + runbook)

| Failure | Likelihood | Impact | Mitigation | Detected by |
|---------|-----------|--------|------------|-------------|
| | | | | |

## 6. Gates summary (detail in GATE_DESIGN)

- Gate 0 (justification): `<done — see §2>`
- Gate A (security): `<→ GATE_DESIGN_TEMPLATE>`
- Gate B (eval): `<→ EVAL_HARNESS_TEMPLATE>`
- Gate C (production-readiness/disclosure): `<→ DISCLOSURE_MANIFEST_TEMPLATE>`
- Kill switch: `<where/how>`

## 7. Open questions & decisions log

| # | Question / decision | Status | Resolution |
|---|---------------------|--------|------------|
| | | | |

## 8. Referenced existing prompts (reuse, don't reinvent)

- `<aiagent_* / done_definition_* / mlmonitor_* / rai_* used and where>`

---

## Machine-readable markers (for the factory scripts)

> The factory's `scripts/check_gate.py` reads these from the **emitted** `ARCHITECTURE.md`. Set them when you fill §2. Markers are HTML comments (invisible when rendered). Full contract: [`BUNDLE_MANIFEST_TEMPLATE.md`](../../templates/BUNDLE_MANIFEST_TEMPLATE.md).

```
<!-- GATE-0: JUSTIFIED -->            (or WORKFLOW-STOP if Step 0 ended the exercise)
<!-- JUSTIFICATION-START -->
An agent is required because <…>, and a deterministic workflow cannot because <…>.
<!-- JUSTIFICATION-END -->
```
- `GATE-0: JUSTIFIED` requires a non-empty, non-placeholder justification block.
- `GATE-0: WORKFLOW-STOP` is a valid terminal state (you correctly talked yourself down the ladder) — the bundle stops here.
