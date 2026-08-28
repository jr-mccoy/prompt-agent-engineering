---
title: "Case Study Slop Detector — Credible Transformation or Success Theater?"
category: professional-writing/content-quality
description: "Score a case-study draft on five believability dimensions (before-state, implementation, results, voice, relatability) and return strict JSON with an ACCEPT/REVISE/REJECT verdict and surgical fixes."
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
  - case-study
  - sales-enablement
  - validation
  - proof
updated: "2026-06-19"
related_prompts:
  - domain-professional-writing/content-quality/quality_slop_blog_post.md
  - domain-professional-writing/content-quality/quality_slop_client_deliverable.md
  - domain-productivity/validation/validation_reality_check.md
---

# Case Study Slop Detector — Credible Transformation or Success Theater?

**Objective:** Determine whether prospects will see themselves in the story and believe the results — or whether it's vague success theater that proves nothing — scoring five dimensions and returning a strict-JSON verdict with exact fixes.

**When to use:**
- Before a case study becomes a primary sales asset.
- To screen AI-drafted or vendor-written case studies for sanitized, unverifiable claims.
- When a case study isn't influencing deals and you suspect it's too generic.
- As a quality gate in a sales-enablement content pipeline.

**When NOT to use:**
- For short ad creative or recurring email (use those evaluators).
- For internal retrospectives not meant to persuade prospects.

**Audience:** Product marketers, sales enablement, content teams, and founders reviewing customer stories.

---

## Inputs / Context

Provide:
1. **The case-study draft** — before-state, implementation narrative, results, and any quotes.
2. **Target prospect profile** (optional) — the industry, size, and situation the story should resonate with.
3. **Available real data** — note metrics or quotes that exist but aren't yet in the draft, so the evaluator flags (not invents) gaps.

---

## Constraints

### Must
- Score every dimension on the 0–5 anchored scale and compute `overall_score`.
- Quote the exact location of each flagged problem.
- Give 3–5 prioritized fixes with exact replacement text.
- Apply the verdict thresholds exactly.

### Must Not
- Invent before/after metrics, customer names, quotes, or timeframes — flag missing proof as a gap, never fabricate it.
- Rewrite the whole case study; stay surgical.
- Treat illustrative example numbers in this prompt as facts about the user's draft.
- Mark ACCEPT on score alone if a required element is missing.

---

## Instructions

1. Collect the draft and any prospect/real-data context.
2. Paste the evaluator block below verbatim, appending the draft.
3. Have the model score each axis, check required elements, list gaps, and produce 3–5 surgical fixes.
4. Return strict JSON (skeleton in Output Format).

```
You are evaluating a case study draft. Your job: determine if prospects will see
themselves in this story and believe the results — or if it's vague success theater
that proves nothing.

WHY THIS MATTERS: Generic case studies get skipped. Specific, credible ones become
primary sales assets that close deals.

Score each dimension 0-5:

1. BEFORE-STATE SPECIFICITY — Concrete, relatable starting situation?
   5: Specific metrics, processes, pain points with numbers ("450 tickets/week,
      18-hour avg resolution"). 3: Some specifics, some generic pain.
   0: Vague ("needed to improve efficiency") with no measures.

2. IMPLEMENTATION DETAIL — Can a prospect understand HOW the change happened?
   5: Timeline, specific steps, workflow changes, obstacles encountered.
   3: Some detail but skips key steps or makes it sound too easy.
   0: Jumps from problem to results ("after implementing our solution...").

3. RESULTS PRECISION — Outcomes measured with specific metrics + context?
   5: Multiple metrics with before/after, timeframe, sample ("18h -> 4.5h within 2
      months, across 3,200 tickets"). 3: Some metrics, missing context/precision.
   0: Vague ("major improvements", "transformed operations").

4. CUSTOMER VOICE — Does the customer sound authentic, not like marketese?
   5: Direct quotes that sound like a real person, including doubts they had.
   3: Quotes present but scripted/overly positive.
   0: No quotes, or quotes that read like ad copy.

5. RELATABILITY — Can target prospects see their situation here?
   5: Clear company stage, team size, industry, situation ("that's like us").
   3: Some context, key relatable details missing. 0: Could be any company.

REQUIRED ELEMENTS (must be present):
- Specific before metrics (concrete starting point with numbers)
- Implementation timeline (how long, what steps)
- Specific after metrics (concrete results with numbers and timeframe)
- Customer quotes (real voice from an actual stakeholder)

ANTI-PATTERNS TO FLAG:
- Vague problems ("needed to improve efficiency")
- Magical results (problem -> implementation -> success, no obstacles/timeline)
- Percentage-only metrics ("50% improvement" — of what? from what baseline?)
- Sanitized marketese quotes ("best-in-class solution")
- Missing context (can't tell if this company is like the prospect)
- No implementation detail; results with no timeframe

RULES:
- Do NOT invent metrics, names, quotes, or timeframes about this draft. Flag missing
  proof as a gap; never fabricate it.
- Be surgical: 3-5 fixes that move REVISE -> ACCEPT. Quote exact locations and give
  exact replacement text. Do not rewrite the whole study.
- Prioritize fixes by impact on credibility and prospect self-identification.

VERDICT THRESHOLDS:
- ACCEPT: >=4.2 overall, all required elements present, <2 critical gaps
- REVISE: 3.0-4.1 overall, OR missing 1 required element, OR results lack precision
- REJECT: <3.0 overall, OR before-state is vague, OR no specific metrics

Return strict JSON only, matching the provided schema.

CASE STUDY TO EVALUATE:
<paste full draft, plus prospect profile and available-data context, here>
```

---

## False-Positive Prevention

❌ **DON'T:**
- Score `results_precision` high because percentages are present — percentages without baselines are a gap.
- Invent a baseline, sample size, or quote to complete a fix.
- Accept a sanitized quote as authentic customer voice.
- Penalize a story for omitting an obstacle the user confirmed didn't occur.

✅ **DO:**
- Flag percentage-only results and ask for absolute numbers + timeframe.
- Phrase example numbers in fixes as clearly illustrative (e.g., "e.g., '18h -> 4.5h across 3,200 tickets' — use the customer's real figures").
- Check all four required elements independently of the score.
- Quote the exact line being criticized.

---

## Output Format

```json
{
  "overall_score": 3.4,
  "axis_scores": {
    "before_state_specificity": 3,
    "implementation_detail": 3,
    "results_precision": 3,
    "customer_voice": 4,
    "relatability": 3
  },
  "verdict": "REVISE",
  "required_elements": {
    "specific_before_metrics": {"present": true, "quality": "some numbers but could be more precise"},
    "implementation_timeline": {"present": true, "quality": "mentions timeframe but skips key steps"},
    "specific_after_metrics": {"present": true, "quality": "percentages without baseline context"},
    "customer_quotes": {"present": true, "quality": "good authentic quotes"}
  },
  "critical_gaps": [
    "Before-state metrics lack context — can't tell how bad 'slow' actually was",
    "Results show percentages but not absolute numbers or measurement timeframe"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Before-state section: 'Acme Corp was struggling with slow customer support'",
      "problem": "'Slow' is vague — no concrete baseline",
      "fix": "Replace with the customer's real baseline, e.g.: 'Acme's 12-person support team handled 450 tickets/week with 18-hour avg resolution; complex tickets (30% of volume) took 3-4 days.' Insert verified figures.",
      "why": "Numbers + team size + complexity breakdown let prospects compare to themselves"
    },
    {
      "priority": 2,
      "location": "Results section: 'Reduced resolution time by 75%'",
      "problem": "Percentage without baseline or absolute numbers",
      "fix": "Replace with absolute before/after + timeframe + sample, e.g.: 'From 18 hours to 4.5 hours (75% reduction) within 2 months, measured across 3,200 tickets (Mar-May 2024).' Use real data.",
      "why": "Absolute numbers + timeframe + sample size = credible and comparable"
    },
    {
      "priority": 3,
      "location": "Implementation section (missing detail)",
      "problem": "Jumps from 'we implemented' to results — no realistic path",
      "fix": "Add a brief week-by-week rollout plus the biggest obstacle and how it was solved, drawn from the actual project.",
      "why": "A realistic timeline + a real obstacle = a believable path prospects can follow"
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
- [ ] No fabricated metrics, baselines, names, or quotes; missing proof flagged as a gap.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Frames the job as believability and prospect self-identification.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five believability axes with explicit anchors.
- **DS-02 (Metric/Criteria Specification):** Numeric thresholds and four required elements specified.
- **ST-02 (Structured Output Format):** Forces strict JSON.
- **CM-02 (Explicit Constraints):** Bars fabricated metrics/quotes and whole-draft rewrites.

---

## Related Prompts
- `domain-professional-writing/content-quality/quality_slop_blog_post.md` — sibling evaluator for long-form content credibility.
- `domain-professional-writing/content-quality/quality_slop_client_deliverable.md` — sibling evaluator for actionable, evidence-backed deliverables.
- `domain-productivity/validation/validation_reality_check.md` — surface the objections a skeptical prospect or expert would raise.
