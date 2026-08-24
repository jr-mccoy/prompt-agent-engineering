# DISCLOSURE MANIFEST — `<system name>`

> Gate C artifact. Fill during Step 6. Six dimensions from the 2025 AI Agent Index (the categories developers most often leave blank are the safety ones — don't). Adapt `responsible-ai-governance/rai_documentation_suite_orchestrator.md` to generate the cross-referenced bundle.

**System:** `<name>` · **Version:** `<…>` · **Date:** `<…>`

---

## 1. Product Overview
- What the system does, intended users, intended use, explicit out-of-scope uses.

## 2. Company & Accountability
- Owner/maintainer; point of contact; responsible party for incidents; update cadence.

## 3. Technical Capabilities & System Architecture
- Topology (TP-0X); agents + tools; models used; memory/state; interop layer (MCP?); external dependencies (with provenance/AIBOM where applicable).

## 4. Autonomy & Control
- Autonomy level (acts vs recommends); authority boundaries (Can-Do / Ask-First / Never); HITL gates; kill switch; loop bounds.

## 5. Ecosystem Interaction
- External systems/tools it touches; inter-agent communication + trust model (if multi-agent); data it reads/writes; identity & auth model.

## 6. Safety, Evaluation & Impact
- **Capability evals run** (ABC-valid) — results + cost + CIs.
- **Safety evals actually run** (real-tool, 8 categories) — worst-category unsafe-action rate + mitigations.
- Known failure modes + residual risks; rollback path; monitoring in production.
- Third-party testing (if any).

---

## Completeness check
- [ ] No dimension left blank (especially #6 — the most-skipped in the field).
- [ ] Safety section reports evals **actually run**, not aspirational.
- [ ] Cross-links to the risk register (`rai_model_risk_register`) and any regulatory assessments (jurisdiction selector).

---

## Machine-readable markers (for the factory scripts)

> `scripts/check_gate.py --gate C` requires all six dimension markers in the emitted `DISCLOSURE_MANIFEST.md` (plus a rollback path in `RUNBOOK.md` and a present `OBSERVABILITY.md`). The fenced example below is **inert** — the script ignores markers inside code fences; emit live markers in your file, one per dimension *actually completed*. Full contract: [`BUNDLE_MANIFEST_TEMPLATE.md`](../../templates/BUNDLE_MANIFEST_TEMPLATE.md).

```
<!-- DISCLOSURE-DIM-1: complete -->   Product Overview
<!-- DISCLOSURE-DIM-2: complete -->   Company & Accountability
<!-- DISCLOSURE-DIM-3: complete -->   Technical Capabilities & Architecture
<!-- DISCLOSURE-DIM-4: complete -->   Autonomy & Control
<!-- DISCLOSURE-DIM-5: complete -->   Ecosystem Interaction
<!-- DISCLOSURE-DIM-6: complete -->   Safety, Evaluation & Impact (the most-skipped — do not leave blank)
```
