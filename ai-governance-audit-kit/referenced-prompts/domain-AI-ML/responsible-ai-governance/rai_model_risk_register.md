---
title: "RAI Model Risk Register"
category: AI-ML/responsible-ai-governance
description: "Author and maintain a living model risk register — structured risk entries with severity, likelihood, controls, residual risk, owner, and review cadence — kept current across model and data changes rather than produced once and abandoned."
techniques:
  - ST-03
  - DS-01
  - RT-05
  - QA-12
  - RP-02
difficulty: advanced
tags:
  - model-risk
  - risk-register
  - governance
  - residual-risk
  - responsible-ai
updated: "2026-06-19"
related_prompts:
  - domain-AI-ML/responsible-ai-governance/rai_model_risk_assessment.md
  - domain-AI-ML/responsible-ai-governance/rai_governance_framework_design.md
  - domain-AI-ML/production-monitoring/mlmonitor_ml_incident_response.md
---

# RAI Model Risk Register

**Objective:** Build and operate a living register of model risks — each scored, controlled, owned, and on a review cadence — so risk posture stays current as the model and its data change over time.

**When to Use:**
- You have a model in or approaching production and need an auditable, continuously maintained record of its risks.
- A one-time risk assessment already exists and you now need an ongoing artifact that tracks risks through their lifecycle (open → mitigated → closed).
- Governance, audit, or regulators require a maintained register with owners, controls, and review dates.

**When NOT to Use:**
- You need a single point-in-time analysis of whether to deploy — use `rai_model_risk_assessment.md` instead; this prompt assumes that assessment feeds the register.
- You are designing the governance program itself (roles, gates, escalation paths) — use `rai_governance_framework_design.md`.

## Inputs / Context

- **Model description** — purpose, deployment context, affected populations, decision stakes.
- **Existing assessments** — outputs of prior risk assessments, bias audits, or evaluations (if any).
- **Change log** — recent model retrains, data composition shifts, scope expansions, incident reports.
- **Control inventory** — current technical and process controls (monitoring, human review, thresholds, rollback).
- **Ownership & cadence** — named risk owners and the organization's review frequency (e.g., monthly, per-release).

## Constraints

**Must:**
- Treat the register as a *maintained* artifact: every entry carries a status, an owner, and a next-review date.
- Score each risk on severity AND likelihood explicitly, then derive residual risk after controls.
- Define an operating cadence: how new risks enter, how entries are re-scored after changes, and closure criteria.
- Keep each entry traceable to its evidence source (assessment, audit, incident, monitoring signal).

**Must Not:**
- Never invent severity scores, likelihoods, incident counts, dates, or affected-population figures. Reason only from supplied inputs; mark anything unsupported as `UNKNOWN — needs assessment` rather than guessing.
- Do not silently close risks; closure requires stated, verifiable criteria.
- Do not collapse distinct risks into one entry to make the register look shorter.

**Instructions:**

1. **Establish the schema.** Lock the columns every entry uses (id, description, category, affected population, severity, likelihood, current controls, residual risk, owner, status, review date, evidence link).
2. **Seed entries from evidence.** Convert each finding from prior assessments, audits, and incidents into a register row. Mark gaps as `UNKNOWN`.
3. **Score severity × likelihood.** Use a defined scale (e.g., 1–5 each). Derive an inherent risk level, then a residual level after current controls.
4. **Assign ownership and review dates.** Each open risk gets a named owner and a concrete next-review date tied to the cadence.
5. **Define the operating cadence.** Specify intake of new risks, triggers for re-scoring (retrain, data shift, incident), and closure criteria.
6. **Summarize posture.** Roll up open/high-residual risks and overdue reviews into a one-screen status.

**Output Format:**

A register table (one row per risk) plus an "Operating Cadence" section and a "Posture Summary" section. Use `UNKNOWN` markers for missing data and a refresh-trigger list.

## Verification

- [ ] Every entry has id, severity, likelihood, residual risk, owner, status, and review date.
- [ ] Residual risk reflects current controls, not inherent risk.
- [ ] No score, count, or date is asserted without an input source; gaps are marked `UNKNOWN`.
- [ ] Closure criteria are stated for any closed/accepted risk.
- [ ] The cadence section defines intake, re-scoring triggers, and closure.

## False-Positive Prevention

❌ **DON'T:**
- Mark a risk "mitigated" because a control exists, without evidence the control reduces residual likelihood/severity.
- Assign every risk the same review date, producing a register that goes stale in lockstep.
- Carry forward an old severity score after a retrain or data shift without re-scoring.
- Invent a plausible-sounding likelihood (e.g., "Low") for a risk you have no data on.

✅ **DO:**
- Tie residual risk to named, verifiable controls and show inherent-vs-residual deltas.
- Stagger review dates by risk severity (high-residual reviewed more often).
- Add a re-scoring trigger entry whenever the change log shows a retrain or data composition change.
- Use `UNKNOWN — needs assessment` and route it to an owner.

## Example Output

```markdown
# Model Risk Register — Loan Default Classifier v4.2

| ID | Description | Category | Affected Pop. | Sev | Lik | Controls | Residual | Owner | Status | Review |
|----|-------------|----------|---------------|-----|-----|----------|----------|-------|--------|--------|
| MR-01 | Higher false-decline rate for applicants <25 | Fairness | Young applicants | 4 | 3 | Per-group monitor + monthly review | Medium | A. Okafor | Open | 2026-07-15 |
| MR-02 | Feature drift on income field after data-vendor change | Robustness | All | 3 | 4 | Drift monitor; alert at PSI>0.2 | Medium | R. Singh | Open | 2026-07-01 |
| MR-03 | No documented recourse path for declined users | Transparency | Declined applicants | 3 | UNKNOWN | None | UNKNOWN — needs assessment | Legal | Open | 2026-06-30 |
| MR-04 | Stale training labels (>18mo) | Validity | All | 2 | 2 | Quarterly relabel sample | Low | Data team | Mitigated | 2026-09-01 |

## Operating Cadence
- **Intake:** New risks enter from monitoring alerts, incident reports, audits, or quarterly review. File within 2 business days.
- **Re-scoring triggers:** Any retrain, data-source change, scope expansion, or P1 incident forces re-scoring of affected rows.
- **Closure criteria:** Residual = Low for two consecutive reviews AND control verified in production = candidate for "Closed"; sign-off by owner + governance lead.

### Posture Summary
- Open high-residual risks: 0 | Medium: 2 | Unknown: 1 (MR-03 blocking)
- Overdue reviews: 0 | Next forced re-score: on v4.3 retrain (scheduled)
```

**Techniques Used:**
- **ST-03 (Output Format Specification):** Locks the register schema so entries stay comparable and auditable over time.
- **DS-01 (Decomposition):** Splits "model risk" into discrete, individually scored and owned entries.
- **RT-05 (Self-Verification):** Verification checklist forces re-scoring and ownership before the register is trusted.
- **QA-12 (Uncertainty Flagging):** `UNKNOWN — needs assessment` markers prevent fabricated scores from entering the register.
- **RP-02 (Role Priming):** Frames the author as a risk owner maintaining a living artifact, not a one-shot report writer.

**Related Prompts:**
- `rai_model_risk_assessment.md` — one-time, point-in-time deploy/no-deploy risk analysis that seeds this register.
- `rai_governance_framework_design.md` — designs the roles, gates, and escalation paths the register operates within.
- `mlmonitor_ml_incident_response.md` — incident workflow whose findings flow back into the register as new or re-scored entries.
