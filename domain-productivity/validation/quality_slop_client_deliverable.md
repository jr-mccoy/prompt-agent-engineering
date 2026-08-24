---
title: "Client Deliverable Slop Detector — Acts-On-Monday or Vague Advice?"
category: "productivity/validation"
description: "Score a consulting deliverable on five value dimensions (actionability, insight, evidence, prioritization, exec-readiness) and return strict JSON with an ACCEPT/REVISE/REJECT verdict and surgical fixes."
techniques:
  - ST-01
  - RT-02
  - DS-02
  - ST-02
  - CM-02
difficulty: intermediate
tags:
  - slop-detection
  - content-quality
  - client-deliverable
  - consulting
  - validation
  - actionability
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/quality_slop_executive_memo.md
  - domain-productivity/validation/quality_slop_case_study.md
  - domain-productivity/validation/validation_final_gate.md
---

# Client Deliverable Slop Detector — Acts-On-Monday or Vague Advice?

**Objective:** Determine whether a client can act on a consulting report/analysis/strategy document immediately — or whether it's vague recommendations that provide no value — scoring five dimensions and returning a strict-JSON verdict with exact fixes.

**When to use:**
- Before sending a consulting report, analysis, or strategy doc to a paying client.
- To screen AI-drafted deliverables for generic, un-implementable recommendations.
- When deliverables aren't getting implemented and you suspect they're too vague.
- As a quality gate before a client board presentation.

**When NOT to use:**
- For internal working notes not meant for client delivery.
- For short-form marketing content (use those evaluators).

**Audience:** Consultants, agencies, analysts, and internal strategy teams shipping client-facing work.

---

## Inputs / Context

Provide:
1. **The deliverable** — full document, including any executive summary, recommendations, and analysis.
2. **Client context** (optional) — the client's industry, the engagement scope, and the decision the deliverable supports.
3. **Available evidence** — note client data or benchmarks that exist but aren't yet cited, so the evaluator flags (not invents) missing backing.

---

## Constraints

### Must
- Score every dimension on the 0–5 anchored scale and compute `overall_score`.
- Quote the exact location of each flagged problem.
- Give 3–5 prioritized fixes with exact replacement text.
- Apply the verdict thresholds exactly.

### Must Not
- Invent client metrics, churn rates, benchmarks, or sources — flag missing evidence as a gap, never fabricate it.
- Rewrite the whole deliverable; stay surgical.
- Treat illustrative example figures in this prompt as facts about the user's document.
- Mark ACCEPT on score alone if a required element is missing.

---

## Instructions

1. Collect the deliverable and any client/evidence context.
2. Paste the evaluator block below verbatim, appending the document.
3. Have the model score each axis, check required elements, list gaps, and produce 3–5 surgical fixes.
4. Return strict JSON (skeleton in Output Format).

```
You are evaluating a client deliverable (consulting report, analysis, strategy doc).
Your job: determine if the client can act on this — or if it's vague recommendations
that provide no value.

WHY THIS MATTERS: Vague deliverables don't get implemented, damage relationships, and
cost months of rebuild. Actionable ones drive client action, referrals, and justify fees.

Score each dimension 0-5:

1. ACTIONABILITY — Can the client start Monday without clarifying calls?
   5: Specific actions with owners, sequence, timelines, success criteria
      ("Week 1: Sarah runs stakeholder interviews using template, p.X").
   3: Recommendations present but lack execution specifics.
   0: Vague advice ("improve operational efficiency") with no steps.

2. INSIGHT DENSITY — Does every section provide non-obvious value?
   5: Reveals patterns the client couldn't see; no filler.
   3: Mix of obvious and insightful; some padding.
   0: Obvious observations the client already knew.

3. EVIDENCE BACKING — Recommendations supported by data from THEIR business?
   5: Every claim backed by client data, benchmarks, or case studies
      ("Your 23% churn vs 12% industry avg, per Gartner, is driven by...").
   3: Some evidence; key recommendations unsupported.
   0: Assertions without backing; could be written without studying their business.

4. PRIORITIZATION — Clear what to do first vs later?
   5: Explicit sequencing with rationale and dependencies ("Phase 1 fixes data
      infra, required before Phase 2"). 3: Some priorities, unclear rationale.
   0: List of recommendations with no order or dependencies.

5. EXECUTIVE READINESS — Presentable to the client's board as-is?
   5: Exec summary, clear narrative, professional formatting, accurate.
   3: Good content but formatting/exec-summary gaps. 0: Reads like working notes.

REQUIRED ELEMENTS (must be present):
- Executive summary (1-page overview of findings and recommendations)
- Specific recommendations (actionable steps with owners and timelines)
- Evidence (client data or benchmarks supporting recommendations)
- Prioritization (clear guidance on what to do first)

ANTI-PATTERNS TO FLAG:
- Generic recommendations that could apply to any company
- No prioritization (20 recs, unclear where to start)
- Vague actions ("improve customer experience")
- Assertions without evidence ("your pricing is too high" — vs what?)
- No implementation roadmap; missing exec summary
- Obvious insights the client already knew; not client-ready (typos, draft quality)

RULES:
- Do NOT invent client metrics, benchmarks, or sources. Flag missing evidence as a
  gap; never fabricate it.
- Be surgical: 3-5 fixes that move REVISE -> ACCEPT. Quote exact locations and give
  exact replacement text. Do not rewrite the whole deliverable.
- Prioritize fixes by impact on the client's ability to act Monday morning.

VERDICT THRESHOLDS:
- ACCEPT: >=4.2 overall, all required elements present, <2 critical gaps
- REVISE: 3.0-4.1 overall, OR missing 1 required element, OR recommendations not actionable
- REJECT: <3.0 overall, OR generic advice that could apply to anyone, OR no evidence backing

Return strict JSON only, matching the provided schema.

DELIVERABLE TO EVALUATE:
<paste full document, plus client and available-evidence context, here>
```

---

## False-Positive Prevention

❌ **DON'T:**
- Score `evidence_backing` high because the doc cites numbers — check they're the client's data, not generic assertions.
- Invent a benchmark (e.g., a Gartner figure) to complete a fix.
- Accept a list of recommendations as "prioritized" without stated sequence/dependencies.
- Penalize a focused brief for lacking sections the engagement scope excluded.

✅ **DO:**
- Flag every assertion lacking client data and ask the user to supply it.
- Phrase example figures in fixes as clearly illustrative (e.g., "e.g., '23% churn vs 12% industry avg' — insert the client's real numbers and a real source").
- Check all four required elements independently of the score.
- Quote the exact recommendation being criticized.

---

## Output Format

```json
{
  "overall_score": 3.3,
  "axis_scores": {
    "actionability": 3,
    "insight_density": 3,
    "evidence_backing": 3,
    "prioritization": 3,
    "executive_readiness": 4
  },
  "verdict": "REVISE",
  "required_elements": {
    "executive_summary": {"present": true, "quality": "summary exists and is concise"},
    "specific_recommendations": {"present": true, "quality": "present but lack implementation detail"},
    "evidence": {"present": true, "quality": "some client data but missing benchmarks"},
    "prioritization": {"present": false, "quality": "no clear sequencing of recommendations"}
  },
  "critical_gaps": [
    "Recommendations lack specific implementation steps — client won't know how to execute",
    "No prioritization — unclear which of 12 recommendations to tackle first"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Recommendation 3: 'Improve customer onboarding process'",
      "problem": "Vague — doesn't tell the client what specific actions to take",
      "fix": "Replace with concrete steps, owners, timelines, and expected impact, e.g.: 'Cut onboarding from 45 to 20 days by (1) shipping a self-service checklist to 10 pilot customers by Oct 30, (2) hiring a dedicated onboarding PM by Nov 15, (3) automating provisioning (3 eng sprints from Dec 1).' Use real names/dates.",
      "why": "Steps + owners + timelines + expected impact = the client can execute immediately"
    },
    {
      "priority": 2,
      "location": "Missing from document",
      "problem": "12 recommendations with no guidance on sequence or priorities",
      "fix": "Add an 'Implementation Roadmap' grouping recommendations into Phase 1/2/3 with the rationale and the critical-path dependency (which rec must finish before another can start).",
      "why": "Sequencing + dependencies + rationale = the client knows where to focus first"
    },
    {
      "priority": 3,
      "location": "Analysis section, claim 'Your churn is high'",
      "problem": "Assertion without context — high compared to what?",
      "fix": "Replace with a benchmark + root cause from the client's own data, e.g.: 'Your 23% churn vs the ~12% B2B SaaS average (source: cite a real report); 68% of churned customers cited slow onboarding.' Use verified figures.",
      "why": "Benchmark + root cause from client data = actionable intelligence"
    }
  ]
}
```

---

## Verification

- [ ] All five axes scored 0–5 with `overall_score` computed.
- [ ] Verdict matches the threshold rules exactly.
- [ ] All four required elements checked independently of score.
- [ ] 3–5 fixes, each with location, problem, fix, and why.
- [ ] No fabricated client metrics or benchmarks; missing evidence flagged as a gap.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Frames the job as can-the-client-act-Monday.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five value axes with explicit anchors.
- **DS-02 (Metric/Criteria Specification):** Numeric thresholds and four required elements specified.
- **ST-02 (Structured Output Format):** Forces strict JSON.
- **CM-02 (Explicit Constraints):** Bars fabricated client data and whole-doc rewrites.

---

## Related Prompts
- `domain-productivity/validation/quality_slop_executive_memo.md` — sibling evaluator for decision-ready leadership memos.
- `domain-productivity/validation/quality_slop_case_study.md` — sibling evaluator for proof-heavy customer stories.
- `domain-productivity/validation/validation_final_gate.md` — final ship/no-ship gate before delivery.
