---
title: "Blog Post Slop Detector — Verifiable Value or Generic Filler?"
category: professional-writing/content-quality
description: "Score a blog post on five credibility dimensions (specificity, proof, positioning, differentiation, CTA) and return strict JSON with an ACCEPT/REVISE/REJECT verdict and surgical, location-anchored fixes."
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
  - blog-post
  - credibility
  - validation
  - content-marketing
updated: "2026-06-19"
related_prompts:
  - domain-professional-writing/content-quality/quality_slop_case_study.md
  - domain-professional-writing/content-quality/quality_slop_email_newsletter.md
  - domain-productivity/validation/validation_reality_check.md
---

# Blog Post Slop Detector — Verifiable Value or Generic Filler?

**Objective:** Determine whether a reader can verify the post's claims, learn something concrete, and take action — or whether it's generic content that could be about any product — scoring five dimensions and returning a strict-JSON verdict with exact fixes.

**When to use:**
- Before publishing a blog post that represents brand credibility.
- To screen AI-drafted articles for vague, unverifiable claims.
- When engagement is flat and you suspect the content is generic.
- As a quality gate in an editorial review pipeline.

**When NOT to use:**
- For short paid-ad creative (use the ad-copy evaluator).
- For recurring email content (use the newsletter evaluator).
- For purely opinion/thought-leadership pieces where proof density isn't the bar.

**Audience:** Content marketers, editors, founders, and writers reviewing long-form posts.

---

## Inputs / Context

Provide:
1. **The blog post** — full draft, including headline and CTA.
2. **Target audience & goal** (optional) — who it's for and what action it should drive.
3. **Available proof** — note any customer names, data, or case studies that exist but aren't yet in the draft, so the evaluator can flag (not invent) missing evidence.

---

## Constraints

### Must
- Score every dimension on the 0–5 anchored scale and compute `overall_score`.
- Quote the exact location of each flagged problem.
- Give 3–5 prioritized fixes with exact replacement text.
- Apply the verdict thresholds exactly.

### Must Not
- Invent statistics, customer names, benchmarks, or sources about the draft — flag missing proof as a gap, never fabricate it.
- Rewrite the whole post; stay surgical.
- Treat illustrative example metrics in this prompt as facts about the user's post.
- Mark a post ACCEPT on score alone if a required element is missing.

---

## Instructions

1. Collect the draft and any audience/goal/proof context.
2. Paste the evaluator block below verbatim, appending the draft.
3. Have the model score each axis, check required elements, list gaps, and produce 3–5 surgical fixes.
4. Return strict JSON (skeleton in Output Format).

```
You are evaluating a blog post. Your job: determine if a reader can verify the claims,
learn something concrete, and take action — or if this is generic content that could be
about any product.

WHY THIS MATTERS: Generic posts generate zero engagement, damage brand credibility, and
train readers to ignore future content.

Score each dimension 0-5:

1. SPECIFICITY — Concrete, verifiable examples vs generic claims?
   5: >=3 specific examples with customer names, real numbers, or precise dates
      (e.g., "Acme Corp cut data entry from 14 hrs/week to 2 hrs/week in 3 months").
   3: 1-2 specific examples; some claims still generic.
   0: Entirely generic ("many customers", "significant improvements") with no evidence.

2. PROOF DENSITY — Claims backed by data, quotes, case studies, or screenshots?
   5: Every major claim has evidence. 3: Some backed, key assertions unproven.
   0: All assertions, no backing; reader must take everything on faith.

3. POSITIONING CLARITY — Obvious who it's for and what problem it solves?
   5: First paragraph names the audience, their problem, and the solution.
   3: Somewhat clear but requires several paragraphs. 0: Unclear who should care.

4. DIFFERENTIATION — Explains why-not-a-competitor or status quo?
   5: Explicitly addresses alternatives and has a unique point of view.
   3: Mentions alternatives but doesn't clearly differentiate.
   0: Could be about any product in the category; nothing distinctive.

5. CALL-TO-ACTION — Clear, low-friction next step?
   5: Specific next step matching reader intent (try demo, read case study, download).
   3: Generic CTA ("learn more", "contact us") or unclear placement.
   0: No CTA, or buried and vague.

REQUIRED ELEMENTS (must be present):
- Concrete examples (>=1 customer name, specific number, or verifiable claim)
- Target audience (clear within first 2 paragraphs)
- Actionable next step (CTA telling the reader what to do)

ANTI-PATTERNS TO FLAG:
- "Best-in-class"/"industry-leading" with no benchmark
- Metrics without context ("40% faster" — than what? measured how?)
- "Trusted by 1000+ companies" naming none
- Generic pain points ("save time and money")
- Vague timeframes ("recently we've seen")
- Empty social proof ("many customers report")

RULES:
- Do NOT invent stats, names, benchmarks, or sources about this post. Flag missing
  proof as a gap; never fabricate it.
- Be surgical: 3-5 fixes that move REVISE -> ACCEPT. Quote exact locations and give
  exact replacement text. Do not rewrite the whole post.
- Prioritize fixes by impact on credibility and reader action.

VERDICT THRESHOLDS:
- ACCEPT: >=4.2 overall, all required elements present, <2 critical gaps
- REVISE: 3.0-4.1 overall, OR missing 1 required element, OR 3+ gaps
- REJECT: <3.0 overall, OR missing 2+ required elements, OR fundamentally unclear who it's for

Return strict JSON only, matching the provided schema.

BLOG POST TO EVALUATE:
<paste full draft, plus audience/goal/available-proof context, here>
```

---

## False-Positive Prevention

❌ **DON'T:**
- Score `proof_density` as 5 because the post *sounds* authoritative.
- Insert a plausible-looking metric to "complete" a fix.
- Treat a clear headline as positioning clarity without an actual stated audience+problem.
- Demand proof density from a genuine opinion piece the user flagged as such.

✅ **DO:**
- Flag every unbacked claim and recommend the user supply the source.
- Phrase any example metric in a fix as clearly illustrative (e.g., "e.g., 'Acme Corp reduced X from 14h to 2h' — replace with your verified figure").
- Check required elements independently of the numeric score.
- Quote the exact sentence being criticized.

---

## Output Format

```json
{
  "overall_score": 3.8,
  "axis_scores": {
    "specificity": 4,
    "proof_density": 3,
    "positioning_clarity": 4,
    "differentiation": 3,
    "call_to_action": 5
  },
  "verdict": "REVISE",
  "required_elements": {
    "concrete_examples": {"present": true, "quality": "one good example, could use more"},
    "target_audience": {"present": true, "quality": "clear in paragraph 2"},
    "actionable_next_step": {"present": true, "quality": "specific and relevant"}
  },
  "critical_gaps": [
    "Multiple claims lack proof — reader can't verify",
    "No differentiation from competitors mentioned"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Paragraph 3, sentence starting 'Many enterprise customers...'",
      "problem": "Generic claim with no verification possible",
      "fix": "Replace with a specific, sourced example, e.g.: 'Acme Corp reduced manual data entry from 14 hours/week to 2 hours/week within 3 months (source: case-study link).' Use your own verified figures.",
      "why": "Specific customer + metrics + timeframe + source = verifiable and credible"
    },
    {
      "priority": 2,
      "location": "Paragraph 5, claim about '40% faster processing'",
      "problem": "Metric lacks context — faster than what?",
      "fix": "Add context, e.g.: '40% faster than manual processing (2.5 hrs vs 4.2 hrs per batch, across 50 deployments in Q3 2024).' Substitute your real measurement.",
      "why": "Context makes the metric meaningful and checkable"
    },
    {
      "priority": 3,
      "location": "Section 'Why This Matters'",
      "problem": "Doesn't address why not just use a competitor product",
      "fix": "Add a differentiation paragraph contrasting your approach with the named alternative on a measurable axis (e.g., setup time, coverage).",
      "why": "Shows specific differentiation with a measurable advantage"
    }
  ]
}
```

---

## Verification

- [ ] All five axes scored 0–5 with `overall_score` computed.
- [ ] Verdict matches the threshold rules exactly.
- [ ] Required-element presence checked independently of score.
- [ ] 3–5 fixes, each with location, problem, fix, and why.
- [ ] No fabricated metrics, names, or sources; missing proof flagged as a gap.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Defines the job as a verifiability-and-action judgment.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five credibility axes with explicit anchors.
- **DS-02 (Metric/Criteria Specification):** Numeric thresholds and required elements specified.
- **ST-02 (Structured Output Format):** Forces strict JSON.
- **CM-02 (Explicit Constraints):** Bars fabrication and whole-post rewrites.

---

## Related Prompts
- `domain-professional-writing/content-quality/quality_slop_case_study.md` — sibling evaluator focused on proof-heavy customer stories.
- `domain-professional-writing/content-quality/quality_slop_email_newsletter.md` — sibling evaluator for recurring content value.
- `domain-productivity/validation/validation_reality_check.md` — find the objections experts would raise about the post's claims.
