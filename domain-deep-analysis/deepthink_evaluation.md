---
title: "Deep-Think: Evaluation"
category: deep-analysis/evaluation
description: "A multi-phase, multi-perspective evaluation system for reviewing an existing artifact, proposal, plan, design, document, or output. Drives the model through Frame → Decompose criteria & evidence → Multi-perspective → Stress-test → Synthesize, using AskUserQuestion at every gate. Terminal artifact: evaluation report with criteria, weighted findings, evidence gaps, recommendation, confidence, and reviewer caveats."
techniques:
  - ST-01
  - ST-02
  - ST-04
  - ST-42
  - RT-02
  - CM-02
  - QA-01
  - QA-02
  - QA-04
  - QA-09
difficulty: advanced
tags:
  - deep-analysis
  - evaluation
  - review
  - critique
  - evidence-assessment
  - weighted-criteria
  - askuserquestion
  - gated-workflow
updated: "2026-06-30"
related_prompts:
  - domain-deep-analysis/deepthink_problem_analysis.md
  - domain-deep-analysis/deepthink_decision.md
  - domain-deep-analysis/deepthink_plan.md
  - domain-deep-analysis/deepthink_design.md
  - domain-prompt-engineering/evaluation/correctness_pre_mortem.md
  - domain-prompt-engineering/evaluation/correctness_tradeoff_forcer.md
---

# Deep-Think: Evaluation

**Objective:** Evaluate an existing artifact, proposal, plan, design, document, or output at a depth that would normally require a review panel. Drive the model through five disciplined phases — Frame, Decompose criteria and evidence, Multi-perspective analysis, Stress-test, and Synthesize — pausing at each gate to let the user redirect, reprioritize, or go deeper. Produce an evaluation report that clearly separates strengths, defects, missing evidence, recommendation, confidence, and reviewer caveats.

**When to use:** The user already has something to review and needs a rigorous judgment of quality, readiness, correctness, risk, or fit-for-purpose. Examples: "Evaluate this launch plan", "Review this architecture proposal", "Assess this policy memo", "Is this AI output good enough to use?", "Grade this design against our requirements". Use this when *judging an existing object* is the goal. If the object does not exist yet, run `deepthink_design.md` or `deepthink_plan.md` first. If the evaluation is meant to choose among alternatives, run `deepthink_decision.md` after producing the evaluation report.

**Audience:** Reviewers, leads, solo operators, analysts, and anyone who needs a structured, evidence-aware critique rather than a vibe-based opinion.

---

## Inputs Required

1. **Object under review.** Paste or link the artifact, proposal, plan, design, document, output, or a concise description plus where to inspect it.
2. **Purpose / intended use.** What the object is supposed to accomplish and who will rely on it.
3. **Evaluation context.** Domain, audience, standards, constraints, or prior requirements the object should satisfy.
4. **Decision stakes.** What happens if the evaluator incorrectly passes, revises, or rejects it.
5. **Default or user-supplied criteria.** If the user has a rubric, use it. If not, propose criteria in Phase 2.
6. **Recommendation options.** Default to **pass / revise / reject** unless the domain requires a different gate.

If items 1–4 are missing, ask for them before starting Phase 1.

---

## Operating Mode

Inherit the shared deep-think operating model from [`BACKBONE.md`](BACKBONE.md): run the five phases in order, stop at every gate, use `AskUserQuestion` when available, and fall back to a labeled `**GATE:**` block in plain chat. For evaluations, use in-phase questions for clarifying scope, choosing or weighting criteria, resolving access to evidence, and confirming whether the review should be lenient, normal, or safety-critical.

Maintain a strict distinction between:

- **Evidence observed in the object** — quote or cite where possible.
- **Reasonable inference** — plausible but not directly proven.
- **Missing evidence** — information needed to evaluate a criterion but not available.
- **Reviewer judgment** — the evaluator's conclusion after weighing evidence and uncertainty.

---

## Instructions

### Phase 1 — Frame

**Goal:** Make sure the right object is being evaluated for the right purpose, under the right standard.

1. **Restate the object under review.** One sentence: "We are evaluating [object] for [intended use / audience] under [constraints or standard]."
2. **Define review boundary.** What is in scope vs. out of scope? For example: content quality but not legal compliance; architecture fit but not implementation correctness; plan feasibility but not budget approval.
3. **Surface stated vs. revealed evaluation.** The stated ask may be "is this good?" while the revealed ask is "is this safe to ship?", "will leadership approve it?", or "what must change before I can rely on it?" Name the gap if present.
4. **Calibrate review strictness.** Classify as low-stakes, normal-stakes, or safety-/mission-critical. Higher stakes require stronger evidence and lower tolerance for unknowns.
5. **Confirm recommendation gate.** Default to pass / revise / reject. If the domain needs different labels (e.g., accept / minor revision / major revision / reject), map them explicitly.

**GATE 1:** Confirm object, boundary, standard, and recommendation gate.

Use `AskUserQuestion`:

```
Question: "Is this the right evaluation scope, boundary, and standard before we go deep?"
Options:
- "Yes — proceed with this scope"
- "Narrow or widen the boundary — I'll specify"
- "Change the standard / strictness level"
- "Stop — I need to provide the object or requirements first"
```

---

### Phase 2 — Decompose Criteria and Evidence

**Goal:** Turn the review into explicit weighted criteria and an evidence map instead of an undifferentiated critique.

1. **List criteria.** Use the user's rubric if provided. Otherwise propose 4–8 criteria in the domain's language. Common buckets: correctness, completeness, feasibility, clarity, audience fit, risk control, evidence support, maintainability, usability, compliance, strategic alignment.
2. **Assign weights.** Weights must sum to 100%. Identify any **gating criteria** that can force revise/reject regardless of total score.
3. **Define what good looks like.** For each criterion, state observable markers of strong, adequate, and poor performance.
4. **Build an evidence map.** For each criterion, list observed evidence, contrary evidence, and missing evidence. Mark each item as observed / inferred / missing.
5. **Flag load-bearing unknowns.** Name missing evidence that could materially change the recommendation.

**GATE 2:** Confirm criteria, weights, gates, and evidence needs.

Use `AskUserQuestion`:

```
Question: "These are the evaluation criteria, weights, and evidence gaps. Adjust before perspectives?"
Options:
- "Looks right — proceed"
- "Change weights or gating criteria"
- "Add / remove a criterion"
- "Pause — I need to supply missing evidence"
```

---

### Phase 3 — Multi-perspective Analysis

**Goal:** Review the object through perspectives the user might not generate alone.

#### 3a. Run the mandatory roster (always)

Run the Phase 3 mandatory perspective roster defined in [`BACKBONE.md`](BACKBONE.md): red team, steel-man, blind-spot scan, future-self, naive newcomer, and affected party. For evaluations, each lens must include its lens statement, its take on the object under review, and the criterion or risk it most strongly affects.

#### 3b. Propose scope-specific additions

Use the evaluation candidate pool in [`BACKBONE.md`](BACKBONE.md) to propose 2–4 additional perspectives tailored to the artifact and domain. Confirm the additions with `AskUserQuestion`/`**GATE:**` and run only the perspectives the user picks.

#### 3c. After running all perspectives

Identify:

- **Convergent findings** — strengths or defects multiple genuinely different perspectives agree on.
- **Productive disagreement** — places where perspectives disagree because they value different criteria or assume different stakes.
- **Review-changing flags** — findings that could move the recommendation from pass to revise, or revise to reject.

**GATE 3:** Decide what to stress-test hardest.

Use `AskUserQuestion`:

```
Question: "Multi-perspective review is complete. What should we stress-test hardest?"
Options:
- "The strongest pass case"
- "The strongest revise/reject case"
- "The biggest missing-evidence gap"
- "All review-changing flags"
```

---

### Phase 4 — Stress-test

**Goal:** Try to break the evaluation before the user relies on it.

1. **False-pass pre-mortem.** Imagine the object was passed and later failed. What did the evaluation miss? Generate 3–5 plausible failure modes and the evidence that would have warned us.
2. **False-reject / over-critique check.** Imagine the object was rejected or heavily revised unnecessarily. What value did the review undervalue? What criticisms depend on preference rather than evidence?
3. **Criterion sensitivity.** If weights shift by 10–20 percentage points, does the recommendation change? If yes, name which criteria drive the instability.
4. **Evidence sufficiency check.** Which conclusions are strongly evidenced, weakly evidenced, or mostly inferred? Missing evidence should reduce confidence, not silently become a defect.
5. **Adversarial stakeholder check.** What would a smart defender of the object contest, and what would a smart harmed stakeholder contest?
6. **Confidence calibration.** Rate confidence high / medium / low, and name the specific evidence that would move it.

**GATE 4:** Decide what makes it into the evaluation report.

Use `AskUserQuestion`:

```
Question: "Which stress-test findings should shape the final evaluation report?"
Options:
- "All findings — full caveats and evidence gaps"
- "Emphasize pass/revise/reject rationale"
- "Emphasize missing evidence and uncertainty"
- "Loop back — criteria or scope need revision"
```

---

### Phase 5 — Synthesize

**Goal:** Produce an evaluation report that the user can act on. Take a position, but make uncertainty visible.

The terminal artifact must contain:

1. **Object under review.** Name the artifact and evaluation boundary.
2. **Evaluation criteria and weights.** Include gating criteria and a concise score or qualitative rating by criterion.
3. **Strengths.** Evidence-backed positives, not generic praise.
4. **Defects / risks.** Evidence-backed issues, severity, and likely consequence.
5. **Missing evidence.** Unknowns that materially limit the review or could change the recommendation.
6. **Pass / revise / reject recommendation.** Include rationale, required revisions if applicable, and any conditions for pass.
7. **Confidence and reviewer caveats.** Confidence level, what would move it, and limitations of the review.

After producing the synthesis:

**FINAL GATE:** Use `AskUserQuestion`:

```
Question: "Evaluation report is on the table. What's next?"
Options:
- "Act on the recommendation — done"
- "Convert required revisions to a plan (run /deepthink-plan)"
- "Re-run with new evidence"
- "Loop back — [specific phase] needs another pass"
```

---

## Constraints

### Must

- Run all five phases in order. Never skip Phase 1 (Frame) or Phase 4 (Stress-test).
- Stop at every gate and use `AskUserQuestion` (or labeled `**GATE:**`) before proceeding.
- Run the full core roster of six perspectives.
- Make criteria and weights explicit before judging the object.
- Distinguish observed evidence, inference, missing evidence, and reviewer judgment.
- Include the seven required sections in the terminal evaluation report.
- State pass / revise / reject clearly. Do not hide behind "it depends".

### Must Not

- Generate all five phases in one continuous output.
- Treat missing evidence as proof of a defect unless the criterion requires that evidence to exist.
- Give a high-confidence recommendation when load-bearing evidence is unavailable.
- Optimize for politeness over review usefulness. Strengths and defects both need evidence.

---

## Output Format

The final report must use this structure:

```markdown
# Evaluation Report: [Object]

## 1. Object Under Review
- **Object:** ...
- **Intended use / audience:** ...
- **Review boundary:** ...
- **Standard / strictness:** ...

## 2. Evaluation Criteria and Weights
| Criterion | Weight | Rating | Evidence summary | Gating? |
|---|---:|---|---|---|

## 3. Strengths
- **[Strength]:** Evidence and why it matters.

## 4. Defects / Risks
- **[Severity] [Defect/risk]:** Evidence, consequence, and likely mitigation.

## 5. Missing Evidence
- **[Unknown]:** Why it matters and how it could change the recommendation.

## 6. Recommendation
**Recommendation:** Pass / Revise / Reject

**Rationale:** ...

**Required revisions or conditions:** ...

## 7. Confidence and Reviewer Caveats
- **Confidence:** High / Medium / Low
- **What would move confidence:** ...
- **Reviewer caveats:** ...
```

## Verification Checklist

Before finalizing, verify:

- Criteria weights sum to 100%.
- Any gating criterion is explicitly marked.
- Every major strength and defect has evidence or is labeled as inference.
- Missing evidence is separated from defects.
- Recommendation is one of pass / revise / reject or an explicitly mapped domain equivalent.
- Confidence is consistent with evidence sufficiency and stakes.
