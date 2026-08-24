---
title: "Ad Copy Slop Detector — Will This Convert or Waste Spend?"
category: "productivity/validation"
description: "Score paid-ad copy (Google, Meta, LinkedIn) on five conversion dimensions and return strict JSON with an ACCEPT/REVISE/REJECT verdict plus surgical, location-anchored fixes."
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
  - ad-copy
  - conversion
  - validation
  - paid-media
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/quality_slop_email_campaign.md
  - domain-productivity/validation/quality_slop_blog_post.md
  - domain-productivity/validation/validation_reality_check.md
---

# Ad Copy Slop Detector — Will This Convert or Waste Spend?

**Objective:** Determine whether a piece of paid-ad copy will convert cold traffic or burn budget on vague promises nobody believes — scoring it across five conversion dimensions and returning a strict-JSON verdict with exact, paste-ready fixes.

**When to use:**
- Before launching a Google, Meta, or LinkedIn ad and committing spend.
- When CTR or CPA is underperforming and you suspect the creative, not the targeting.
- To pressure-test AI-generated ad variants before they enter rotation.
- As a gate in a creative-review workflow where many variants compete.

**When NOT to use:**
- For organic/long-form content (use the blog-post or newsletter evaluators).
- For brand-awareness creative where direct response isn't the goal.
- When you have no benefit or audience context to judge relevance against.

**Audience:** Performance marketers, growth teams, founders, and copywriters reviewing paid creative.

---

## Inputs / Context

Provide:
1. **The ad copy** — headline(s), body/primary text, and CTA, exactly as written.
2. **Platform** — Google Search, Meta, LinkedIn, etc. (affects length and intent norms).
3. **Audience & offer context** (optional but recommended) — who the ad targets, the product, and the desired action.

If proof points (customers, stats, reviews) exist but aren't in the copy, note that — the evaluator flags missing proof rather than inventing it.

---

## Constraints

### Must
- Score every dimension on the 0–5 anchored scale and compute `overall_score`.
- Anchor each fix to an exact location (quote the offending headline/line).
- Give 3–5 prioritized fixes with exact replacement text.
- Apply the verdict thresholds exactly as specified.

### Must Not
- Invent statistics, customer names, CTR figures, or proof about the draft being judged — flag missing proof as a gap; never fabricate it.
- Rewrite the whole ad; stay surgical and location-specific.
- Treat illustrative examples in this prompt as facts about the user's ad.
- Pass copy that scores ≥4.2 numerically but is missing a required element.

---

## Instructions

1. Collect the ad copy, platform, and any audience/offer context.
2. Paste the evaluator block below verbatim, appending the copy to evaluate.
3. Have the model score each dimension, check required elements, list critical gaps, and produce 3–5 surgical fixes.
4. Return the result as strict JSON (skeleton in Output Format).

```
You are evaluating ad copy (Google, Meta, LinkedIn, etc.). Your job: determine if
this will convert cold traffic — or waste ad spend on vague promises nobody believes.

WHY THIS MATTERS: Generic ads get <1% CTR and fail to convert; good ads get 3-8% CTR
with qualified clicks. The difference is specific benefits, objection handling, and
clarity on what happens next.

Score each dimension 0-5:

1. BENEFIT CLARITY — Is the benefit specific and stated in the first 5 words?
   5: Specific outcome in first 5 words ("Cut AWS costs 40%", "Deploy in 10 minutes").
   3: Benefit present but not immediately obvious or somewhat vague.
   0: Feature-first or generic ("Powerful platform", "All-in-one solution").

2. OBJECTION HANDLING — Does it address why-not-a-competitor or status quo?
   5: Explicitly handles a likely objection ("No code required", "No credit card").
   3: Implicitly addresses objections but never calls them out.
   0: No objection handling; just states what you do.

3. URGENCY CREATION — Is there a time-bound trigger to act now?
   5: Specific reason to act now ("Offer ends Friday", "Last 3 spots").
   3: Soft urgency that isn't compelling.
   0: No urgency; could wait 6 months with no consequence.

4. FRICTION REMOVAL — Is it crystal clear what happens when they click?
   5: Exact next step stated ("Watch 2-min demo", "Download template", "See pricing").
   3: Next step implied but not fully clear.
   0: Vague CTA ("Learn more", "Get started") with no clarity on what that means.

5. TRUST SIGNALS — Is there specific proof this works?
   5: Specific customer, stat, or credential ("Used by 1,200 teams", "4.8/5 on G2,
      340 reviews"). 3: Generic claim ("Trusted by thousands"). 0: No proof at all.

REQUIRED ELEMENTS (must be present):
- Specific benefit (concrete outcome, not vague promise)
- Clear next step (obvious what happens on click)
- Trust signal (proof point that it actually works)

ANTI-PATTERNS TO FLAG:
- Leading with features not benefits ("Powerful API" vs "Deploy in 10 minutes")
- Vague promises ("Transform your business", "10x your productivity")
- No clear next step ("Learn more" with no object)
- Generic trust ("Trusted by thousands" naming no one)
- No objection handling; no urgency

RULES:
- Do NOT invent stats, customer names, or CTR numbers about this ad. If proof is
  missing, flag it as a gap — never fabricate it.
- Be surgical: 3-5 fixes that move REVISE -> ACCEPT. Quote exact locations and give
  exact replacement text. Do not rewrite the whole ad.
- Prioritize fixes by impact on CTR and qualified click-through.

VERDICT THRESHOLDS:
- ACCEPT: >=4.2 overall, all required elements present, <2 critical gaps
- REVISE: 3.0-4.1 overall, OR missing 1 required element, OR 3+ gaps
- REJECT: <3.0 overall, OR benefit is vague, OR CTA doesn't specify what happens next

Return strict JSON only, matching the provided schema.

AD COPY TO EVALUATE:
<paste headline(s), body, CTA, platform, and audience context here>
```

---

## False-Positive Prevention

❌ **DON'T:**
- Assume a missing stat is true and "score it as present."
- Invent a customer name or CTR to fill a `trust_signal` field.
- Mark copy ACCEPT on score alone while a required element is missing.
- Penalize a short Google headline for not containing a full case study — judge against platform norms.

✅ **DO:**
- Flag absent proof as a critical gap and recommend the user supply it.
- Phrase replacement proof as clearly illustrative (e.g., "e.g., '4.8/5 on G2 (340 reviews)' — insert your real figure").
- Enforce required-element presence independently of the numeric score.
- Quote the exact offending line so the fix is unambiguous.

---

## Output Format

```json
{
  "overall_score": 3.5,
  "axis_scores": {
    "benefit_clarity": 4,
    "objection_handling": 3,
    "urgency_creation": 2,
    "friction_removal": 4,
    "trust_signals": 3
  },
  "verdict": "REVISE",
  "required_elements": {
    "specific_benefit": {"present": true, "quality": "benefit clear but could be more specific"},
    "clear_next_step": {"present": true, "quality": "CTA is obvious"},
    "trust_signal": {"present": false, "quality": "mentions customers but no specific names or numbers"}
  },
  "critical_gaps": [
    "No urgency — no reason to act now vs. next month",
    "Doesn't handle the likely objection about implementation complexity"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Headline: 'Powerful marketing automation platform'",
      "problem": "Feature-first, vague, could be any tool",
      "fix": "Replace with: 'Send 10,000 personalized emails in 3 clicks'",
      "why": "Specific capability + concrete simplicity = clear benefit"
    },
    {
      "priority": 2,
      "location": "Body copy, no mention of implementation",
      "problem": "Missing objection handling — people worry about complexity",
      "fix": "Add line: 'No code. No IT team. Set up in 10 minutes.'",
      "why": "Addresses the top objection with specific reassurance"
    },
    {
      "priority": 3,
      "location": "End of ad",
      "problem": "No urgency, no reason to act today",
      "fix": "Add: 'Free plan ends March 1 — lock in your access now.'",
      "why": "A specific deadline creates a time-bound reason to act"
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
- [ ] No fabricated stats, names, or CTR figures; missing proof flagged as a gap.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Frames the job as a convert-or-waste judgment, not a rewrite.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five orthogonal conversion axes with explicit score anchors.
- **DS-02 (Metric/Criteria Specification):** Verdict thresholds and required elements are spelled out numerically.
- **ST-02 (Structured Output Format):** Forces strict JSON for downstream tooling.
- **CM-02 (Explicit Constraints):** Must/Must-Not bar fabrication and whole-ad rewrites.

---

## Related Prompts
- `domain-productivity/validation/quality_slop_email_campaign.md` — sibling evaluator for conversion-driven email sequences.
- `domain-productivity/validation/quality_slop_blog_post.md` — sibling evaluator for long-form content.
- `domain-productivity/validation/validation_reality_check.md` — surface the objections experts would raise about the claims in the ad.
