---
title: "Failed/Stalled ML Project Postmortem"
category: AI-ML/ai-product-leadership
description: "Run a blameless postmortem on a failed or stalled ML project, separating symptom from root cause and extracting systemic fixes that prevent the next failure."
techniques:
  - ST-02
  - RT-05
  - DS-06
  - QA-01
  - NE-13
difficulty: intermediate
tags:
  - postmortem
  - root-cause
  - blameless
  - systemic-fixes
  - ml-project
updated: "2026-05-29"
related_prompts:
  - domain-AI-ML/ai-product-leadership/aipm_ml_project_scoping.md
  - domain-AI-ML/ai-product-leadership/aipm_mlops_maturity_for_leaders.md
  - domain-AI-ML/ai-product-leadership/aipm_use_case_prioritization.md
---

# Failed/Stalled ML Project Postmortem

**Objective:** Conduct a blameless postmortem on a failed or stalled ML project that distinguishes proximate symptoms from systemic root causes — and produces specific, owned, preventive fixes — so the organization learns rather than repeats the failure on the next ML bet.

**When to Use:**
- An ML project was cancelled, missed its goal, or has stalled with no clear path forward.
- A model shipped but failed to deliver the expected value or broke in production.
- Before starting a similar initiative, to avoid repeating a known failure pattern.

**When NOT to Use:**
- The project is healthy and you're scoping the next one (use `aipm_ml_project_scoping.md`).
- The issue is purely operational tooling maturity (use `aipm_mlops_maturity_for_leaders.md`).

## Inputs / Context

- **Project summary** — goal, what was built, what happened, when it stalled/failed.
- **Timeline** — key decisions, milestones hit/missed, signals that were or weren't acted on.
- **The teams involved** — ML, data, product, stakeholders, and how they interacted.
- **Symptoms observed** — the visible failure (low adoption, poor metrics, prod incidents, missed deadlines).
- **Known constraints** — data, talent, scope changes, organizational factors.

## Constraints

**Must:**
- Stay blameless — attribute outcomes to systems, decisions, and conditions, never to individuals' character.
- Separate symptom from root cause; trace each symptom back through a "why" chain to a systemic origin.
- Produce fixes that are specific, owned, and preventive (change a process/gate), not "try harder next time."

**Must Not:**
- Assign blame to a person or name individuals as the cause.
- Stop at the proximate cause ("the model underperformed") without reaching the systemic one (e.g., the success criteria were never defined).
- Invent facts about the timeline; mark gaps as unknown and list them as things to confirm.

**Instructions:**

1. **Establish the factual timeline.** Reconstruct what happened and when, decision by decision, separating fact from interpretation. Flag unknowns rather than filling them.

2. **Name the symptoms precisely.** What visibly went wrong (no adoption, metrics didn't hold in prod, deadline slipped, scope thrashed). These are not yet causes.

3. **Trace each symptom to root cause.** For each symptom, ask "why" repeatedly until you reach a systemic origin — often one of the classic ML failure patterns: no success criteria, data not ready, leakage inflated offline metrics, no production path, value not wired to an action, misaligned stakeholders, or scope drift.

4. **Classify the root causes.** Bucket them: framing (wrong problem/criteria), data, modeling/eval, delivery/MLOps, or organizational/process. This reveals whether the failure was technical or systemic.

5. **Identify what would have caught it earlier.** For each root cause, the gate or signal that, if present, would have surfaced the problem in time (a pre-mortem, a data-readiness gate, a leakage audit, a stakeholder alignment check).

6. **Prescribe systemic fixes.** Translate each root cause into a process change with an owner — a gate to add, a definition to require, a review to institute. Prioritize by how many future projects each fix protects.

7. **Extract the lessons.** A short, reusable list other teams can apply, and a verdict on whether the underlying idea was wrong or just the execution.

**Output Format:**

A markdown postmortem:
- **Summary** — what happened, in two sentences, blameless.
- **Timeline** — key events/decisions; unknowns flagged.
- **Symptoms** — the visible failures.
- **Root Cause Analysis** — table: Symptom | Why-chain | Root Cause | Category.
- **What Would Have Caught It** — the missing gate/signal per root cause.
- **Systemic Fixes** — fix | owner | which future projects it protects | priority.
- **Lessons & Verdict** — reusable takeaways; was the idea or the execution wrong?

## Verification

- [ ] Analysis is blameless; no individual named as cause.
- [ ] Every symptom traced through a why-chain to a systemic root cause.
- [ ] Root causes classified (framing/data/modeling/delivery/org).
- [ ] Each fix is specific, owned, and preventive — not exhortation.
- [ ] Timeline unknowns flagged, not invented.

## False-Positive Prevention

❌ **DON'T:**
- Conclude "the data scientist's model wasn't good enough" and stop there.
- Treat the proximate symptom (low accuracy) as the root cause when the real issue was undefined success criteria.
- Propose "communicate better" or "be more careful" as fixes.
- Declare the whole idea dead when only the execution failed (or vice versa).

✅ **DO:**
- Trace to systemic origins — framing, data readiness, leakage, missing production path, value not actioned.
- Distinguish "the model was bad" from "we never defined what good meant."
- Convert each root cause into a concrete gate/process with an owner.
- Separate idea-failure from execution-failure so the next decision is informed.

## Example Output

```markdown
## Postmortem — Demand Forecasting Project (cancelled after 2 quarters)

### Summary
A demand-forecasting model was built and showed strong offline metrics but was never
adopted by planners and was cancelled. Blameless: this was a framing + delivery gap.

### Timeline
- Q1: project kicked off, goal "improve forecasting." (No success metric defined — flagged.)
- Q1: model built, offline MAPE looked strong.
- Q2: piloted with planners; they didn't trust or use it. Stalled, then cancelled.

### Symptoms
Strong offline metrics, zero adoption, eventual cancellation.

### Root Cause Analysis
| Symptom | Why-chain | Root Cause | Category |
|---|---|---|---|
| Zero adoption | Planners didn't trust it → not involved in design → output didn't fit workflow | No user/stakeholder integration | Framing/Org |
| "Improved" but no value | No baseline or success metric defined at start | Success criteria never specified | Framing |
| Offline-strong | Backtest used future-informed features | Possible temporal leakage (unconfirmed) | Data/Eval |

### What Would Have Caught It
- A success-criteria gate at kickoff. - Planner involvement in design. - A leakage audit before trusting offline metrics.

### Systemic Fixes
| Fix | Owner | Protects | Priority |
|---|---|---|---|
| Require defined success metric + baseline before build | PM lead | All ML projects | High |
| Mandate end-user in design from day 1 | Product | All applied ML | High |
| Add leakage audit to model review gate | ML lead | All models | Med |

### Lessons & Verdict
The idea (forecasting) was sound; execution failed on framing and adoption. Re-attemptable
with success criteria and planner co-design. The offline-metric trust without a leakage
check is the most transferable lesson.
```

**Techniques Used:**
- **ST-02 (Structured Sequential Instructions):** timeline → symptoms → root cause → fixes.
- **RT-05 (Evidence-Based Reasoning):** every cause traced through an evidenced why-chain.
- **DS-06 (Prioritization & Severity Guidance):** fixes prioritized by future projects protected.
- **QA-01 (Self-Verification):** symptom-vs-cause separation is the built-in check.
- **NE-13 (Technical-to-Business Translation):** technical failure rendered as systemic/process learning.

**Related Prompts:**
- `aipm_ml_project_scoping.md` — the gates this postmortem says were missing.
- `aipm_mlops_maturity_for_leaders.md` — if delivery/MLOps was a root cause.
- `aipm_use_case_prioritization.md` — re-decide whether the idea is worth a second attempt.
