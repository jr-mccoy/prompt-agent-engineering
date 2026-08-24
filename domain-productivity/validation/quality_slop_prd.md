---
title: "PRD Slop Detector"
category: "productivity/validation"
description: "Score a product requirements document against five quality axes and return surgical fixes so an engineering team can build it without rounds of clarifying meetings — replacing vague requirements with testable specs."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - ST-02
  - CM-02
difficulty: intermediate
tags:
  - validation
  - slop-detection
  - content-quality
  - prd
  - product-requirements
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/quality_slop_internal_communication.md
  - domain-productivity/validation/validation_final_gate.md
  - domain-productivity/validation/validation_reality_check.md
---

# PRD Slop Detector

**Objective:** Judge whether a PRD is buildable without three clarifying meetings — or whether vague, untestable requirements will cause rework cycles — and return exact, location-anchored fixes.

**When to use:**
- Before handing a PRD to engineering for estimation or build.
- When prior specs caused rework, scope creep, or "we built the wrong thing."
- To QA AI-drafted PRDs for vague, untestable requirements.

**When NOT to use:**
- A high-level product vision or strategy doc not meant to be built from.
- A bug ticket or small change request that doesn't warrant a full PRD review.

**Audience:** Product managers, eng leads, and anyone reviewing a PRD before it enters the build pipeline.

---

## Inputs / Context

1. **The PRD** — the document being evaluated.
2. **Build context** — the team, stack, or constraints the requirements must fit.
3. **Goal** — what "built correctly the first time" looks like for this release.

---

## Constraints

### Must
- Score all five axes 0–5 using the anchors provided.
- Anchor every fix to an exact location in the PRD and give exact replacement text.
- Verify each required element is present and assess its quality.
- Return strict JSON only, matching the Output Format.

### Must Not
- Invent metrics, thresholds, dependencies, or constraints not present in the PRD; any numbers in *example* fix text are illustrative placeholders the author must replace with real targets.
- Fabricate acceptance criteria or success metrics the PRD lacks — flag missing/untestable items, never supply imaginary measured values.
- Rewrite the whole PRD; restrict yourself to 3–5 high-impact surgical fixes.

---

## Instructions

1. Collect the PRD, the build context, and the goal.
2. Run the evaluator below verbatim against the PRD.
3. Return strict JSON only (no prose outside the JSON).

```
# PRD (Product Requirements Document) Quality Evaluator

You are evaluating a PRD. Your job: determine if an engineering team can build this without 3
clarifying meetings—or if this is vague requirements that will cause rework cycles.

## Why This Matters
Bad PRDs waste 30+ person-hours in clarifying meetings, cause 2-week delays, and result in
building the wrong thing. Good PRDs get built correctly the first time with minimal back-and-forth.

## Evaluation Dimensions (score each 0-5)

### 1. Completeness — all critical sections present and sufficiently detailed?
Score 5: Problem statement, user stories, acceptance criteria, success metrics, non-goals,
  dependencies, and edge cases all present with detail.
Score 3: Most sections present but some lack depth or miss edge cases.
Score 0: Missing critical sections. Engineer doesn't know what success looks like or what's out of scope.

### 2. Testability — can QA write test cases directly from this?
Score 5: Every requirement has measurable acceptance criteria.
  ("P95 response time <200ms for queries with <1000 results.")
Score 3: Some testable criteria but many requirements are vague ("should be fast," "user-friendly").
Score 0: All requirements are subjective or unmeasurable. ("System should be performant.")

### 3. Scoping Clarity — obvious what's in/out of scope for this release?
Score 5: Clear "In scope" and "Non-goals" sections; explicitly calls out what won't be built and why.
Score 3: Scope somewhat clear but edge cases / related features aren't explicitly in or out.
Score 0: No clear boundaries. Engineer doesn't know if feature X is part of this PRD or future work.

### 4. Decision Framework — trade-offs and constraints documented?
Score 5: Technical constraints, trade-offs considered, and why approaches were chosen.
  ("Using PostgreSQL not DynamoDB because we need ACID transactions for billing.")
Score 3: Some decisions explained but rationale is thin or missing for key choices.
Score 0: No explanation of trade-offs or constraints. Just states requirements.

### 5. Dependency Mapping — dependencies on other teams, systems, or timing identified?
Score 5: Lists all dependencies with owners and required completion dates.
  ("Needs new auth endpoint from Platform team by Oct 1.")
Score 3: Some dependencies mentioned but incomplete or no owners/timing.
Score 0: No dependency identification. Engineer discovers blockers mid-build.

## Required Elements (must have)
- Acceptance criteria: measurable definition of done for each requirement
- Success metrics: how we'll know if this solved the problem
- Non-goals: what's explicitly out of scope
- Dependencies: what needs to happen first or concurrently

## Anti-Patterns to Flag (specific to PRDs)
- "System should be performant" (not testable—by what measure?)
- "Improve UX" (not measurable—what specifically should improve?)
- No edge case handling specified (what happens when X fails?)
- Missing acceptance criteria—just describes the feature
- No non-goals—scope creep inevitable
- No dependencies mapped—discovers blockers mid-sprint
- Vague user stories without concrete scenarios
- No success metrics—can't tell if it worked

## Verdict Thresholds
ACCEPT: >=4.2 overall, all required elements present, <2 critical gaps
REVISE: 3.0-4.1 overall, OR missing 1 required element, OR acceptance criteria not testable
REJECT: <3.0 overall, OR missing 2+ required elements, OR requirements are fundamentally vague

## Instructions
Be surgical: give 3-5 specific fixes that move REVISE -> ACCEPT.
Do not rewrite the whole thing. Point to exact locations and give exact replacement text.
Prioritize fixes by impact—what matters most for enabling engineering to build correctly the first time?
Do not invent metrics, thresholds, or dependencies; flag missing/untestable items rather than fabricating them.

Return strict JSON in the format specified below.
```

---

## False-Positive Prevention

❌ **DON'T:**
- Penalize a tightly scoped PRD for omitting sections that are genuinely irrelevant to this release.
- Reward dense prose that reads thorough but leaves criteria subjective ("fast," "easy").
- Supply a specific latency target or metric the PRD never set just to make it "testable."
- Demand dependency mapping when the feature genuinely has none.

✅ **DO:**
- Reward measurable acceptance criteria and explicit non-goals even in a short PRD.
- Treat illustrative numbers in fix text as placeholders the author must replace with real targets.
- Flag vague or missing criteria, metrics, and dependencies as gaps; never invent measured values.
- Distinguish a genuinely out-of-scope item from one the PRD simply forgot to address.

---

## Output Format

```json
{
  "overall_score": 3.3,
  "axis_scores": {
    "completeness": 3,
    "testability": 3,
    "scoping_clarity": 3,
    "decision_framework": 3,
    "dependency_mapping": 4
  },
  "verdict": "ACCEPT | REVISE | REJECT",
  "required_elements": {
    "acceptance_criteria": {"present": true, "quality": "some criteria but many are vague or untestable"},
    "success_metrics": {"present": false, "quality": "no clear metrics for evaluating success"},
    "non_goals": {"present": true, "quality": "non-goals section exists and is clear"},
    "dependencies": {"present": true, "quality": "dependencies identified with owners"}
  },
  "critical_gaps": [
    "Multiple requirements are not testable—use subjective language like 'fast' and 'easy'",
    "Missing success metrics—no way to measure if this solved the problem"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Acceptance Criteria section, item 3: 'System should load quickly'",
      "problem": "Not testable—'quickly' is subjective",
      "fix": "Replace with: 'Initial page load completes in <1.5s (P95) for queries returning <1000 results, measured from navigation start to DOMContentLoaded.'",
      "why": "Specific threshold + percentile + measurement method = QA can write an exact test"
    }
  ]
}
```

---

## Verification

- [ ] All five axes scored 0–5 with anchors applied.
- [ ] Each required element marked present/absent with a quality note.
- [ ] Each fix has location, problem, fix (exact replacement text), and why.
- [ ] Verdict matches the thresholds (ACCEPT/REVISE/REJECT).
- [ ] No invented metrics, thresholds, or dependencies; missing/untestable items flagged, not fabricated.
- [ ] Output is strict JSON with no surrounding prose.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Frames the job as judging buildability without clarifying meetings.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five orthogonal axes (completeness, testability, scope, decisions, dependencies).
- **DS-02 (Metric/Criteria Specification):** 0–5 anchors and ACCEPT/REVISE/REJECT thresholds define scoring precisely.
- **ST-02 (Structured Output Format):** Strict JSON schema makes results machine-readable.
- **CM-02 (Explicit Constraints):** Must/Must-Not bound the evaluator and forbid fabricated metrics or criteria.

---

## Related Prompts
- `domain-productivity/validation/quality_slop_internal_communication.md` — sibling detector for written internal docs.
- `domain-productivity/validation/validation_final_gate.md` — final ship/no-ship gate before handoff to engineering.
- `domain-productivity/validation/validation_reality_check.md` — surface objections an engineer would raise about the spec.
