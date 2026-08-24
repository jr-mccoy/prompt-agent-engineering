# Healthcare Clinical Domain Expansion Roadmap (Weeks 1–7)

## Purpose
This roadmap defines the 7-week expansion plan for `domain-healthcare-clinical/`, including scope lanes, phased deliverables, quality checkpoints, and safety boundaries.

---

## 1) Scope Split

### A. Clinical Reasoning Support
Focus: clinician-facing reasoning assistance and structured analysis.

Includes:
- Differential diagnosis framing
- Workup planning and interpretation scaffolds
- Risk stratification and prioritization support
- Care transition and handoff reasoning templates

### B. Operational / Communication Support
Focus: workflow, documentation, and communication artifacts that improve safe execution.

Includes:
- Clinical documentation templates
- Handoff, consent, discharge, and escalation communication prompts
- Team coordination and policy/protocol communication assets
- Quality/safety incident communication tooling

### C. Education / Training Support
Focus: medical learning, teaching, simulation, and competency development.

Includes:
- Case-based teaching prompts
- Preceptor/coaching frameworks
- Simulation/debrief templates
- Self-audit and reflective practice guides

---

## 2) Timeline by Phase (Weeks 1–7)

## Phase 1 — Foundation & Safety Alignment (Week 1)
- Confirm taxonomy, naming, and folder structure.
- Map all net-new artifacts to healthcare safety overlay requirements.
- Define acceptance criteria and QA checklist schema used in later phases.

## Phase 2 — Core Buildout (Weeks 2–3)
- Produce first wave of high-priority artifacts across all 3 scope lanes.
- Prioritize reusable prompts and companion templates.
- Draft initial implementation guides for contributor consistency.

## Phase 3 — Extended Coverage (Weeks 4–5)
- Add second wave assets covering additional clinical contexts and workflows.
- Expand education/training depth (simulation + coaching variants).
- Standardize formatting and cross-linking across artifacts.

## Phase 4 — QA, Hardening, and Publish Readiness (Weeks 6–7)
- Run full QA pass against safety and style criteria.
- Resolve gaps, deduplicate overlaps, and improve discoverability.
- Finalize release notes and maintenance handoff guidance.

---

## 3) Deliverable Counts per Phase

| Phase | Weeks | Prompts | Templates | Guides | QA Artifacts |
|---|---:|---:|---:|---:|---:|
| Phase 1: Foundation & Safety Alignment | 1 | 0 | 2 | 1 | 2 |
| Phase 2: Core Buildout | 2–3 | 9 | 6 | 2 | 2 |
| Phase 3: Extended Coverage | 4–5 | 8 | 6 | 2 | 2 |
| Phase 4: QA & Publish Readiness | 6–7 | 3 (revised/finalized) | 2 (revised/finalized) | 1 | 4 |
| **Total (Weeks 1–7)** |  | **20** | **16** | **6** | **10** |

### Count Notes
- “Prompts” are user-facing prompt assets intended for direct use.
- “Templates” are structured output shells/checklists/forms.
- “Guides” are contributor or usage documents.
- “QA Artifacts” include checklists, validation matrices, and review logs.

---

## 4) Explicit Out-of-Scope Boundaries

The expansion **must not** include:
- Direct patient diagnosis.
- Direct treatment recommendations or prescriptive care plans.
- Medication dosing or prescribing instructions as definitive guidance.
- Any output framing that substitutes for licensed clinician judgment.

All assets remain informational decision-support resources for trained professionals and must preserve escalation language when red flags are present.

---

## 5) Dependencies and Alignment References

This roadmap depends on and must remain aligned with:

1. Domain framing and applicability:
   - `domain-healthcare-clinical/README.md`

2. Existing prompt inventory and technique patterns:
   - `domain-healthcare-clinical/prompts/field_guide.md`

3. Mandatory safety policy overlay:
   - `domain-agentic-resources/documentation/policies/healthcare_safety_overlay.md`

Implementation and QA decisions should treat these files as normative anchors for scope, terminology, and safety constraints.
