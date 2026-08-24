---
title: "Email Campaign Slop Detector — Conversion or Unsubscribe?"
category: "productivity/validation"
description: "Score a conversion-driven marketing email (promo, product update, sequence send) on five engagement dimensions and return strict JSON with an ACCEPT/REVISE/REJECT verdict and surgical fixes."
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
  - email-campaign
  - conversion
  - validation
  - lifecycle-marketing
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/quality_slop_email_newsletter.md
  - domain-productivity/validation/quality_slop_ad_copy.md
  - domain-productivity/validation/validation_reality_check.md
---

# Email Campaign Slop Detector — Conversion or Unsubscribe?

**Objective:** Determine whether recipients will engage with a conversion-driven marketing email — a promotion, product update, or sequence send aimed at a specific action — or mark it as spam and unsubscribe. Scores five dimensions and returns a strict-JSON verdict with exact fixes.

**Scope note:** This evaluator targets *campaign* email — single-purpose, conversion-oriented sends and sequences. For recurring relationship/value content, use the **newsletter** evaluator instead.

**When to use:**
- Before launching a promo, product-announcement, or nurture-sequence send.
- To screen AI-drafted campaign emails for company-centric, low-conversion copy.
- When click rates are low or unsubscribes are spiking on campaign sends.
- As a gate in a lifecycle-marketing review.

**When NOT to use:**
- For recurring newsletters (use `quality_slop_email_newsletter.md`).
- For 1:1 sales outreach or transactional/system emails.

**Audience:** Lifecycle and growth marketers, founders, and copywriters reviewing campaign email.

---

## Inputs / Context

Provide:
1. **The email** — subject line, preview/opening, body, and CTA(s), as written.
2. **Segment & goal** (optional) — who receives it and the single action it should drive.
3. **Available proof** — note customer results or data that exist but aren't yet in the email, so the evaluator flags (not invents) missing proof.

---

## Constraints

### Must
- Score every dimension on the 0–5 anchored scale and compute `overall_score`.
- Quote the exact location of each flagged problem (subject line, opening, etc.).
- Give 3–5 prioritized fixes with exact replacement text.
- Apply the verdict thresholds exactly.

### Must Not
- Invent customer names, survey results, or engagement stats — flag missing proof as a gap, never fabricate it.
- Rewrite the whole email; stay surgical.
- Treat illustrative example metrics in this prompt as facts about the user's email.
- Mark ACCEPT on score alone if a required element is missing.

---

## Instructions

1. Collect the email, segment/goal, and any proof context.
2. Paste the evaluator block below verbatim, appending the email.
3. Have the model score each axis, check required elements, list gaps, and produce 3–5 surgical fixes.
4. Return strict JSON (skeleton in Output Format).

```
You are evaluating a conversion-driven marketing email (promotion, product update, or
sequence send). Your job: determine if recipients will engage and take the intended
action — or mark it as spam and unsubscribe.

WHY THIS MATTERS: Generic campaigns get <1% click rates and 2-5% unsubscribe rates;
strong ones get 3-8% clicks and <0.5% unsubscribe. The campaign exists to drive ONE
conversion action.

Score each dimension 0-5:

1. SUBJECT LINE SPECIFICITY — Concrete promise or specific curiosity?
   5: Specific benefit/surprise ("We cut our AWS bill 47% with 3 config changes").
   3: Relevant but generic ("New features you'll love"). 0: Vague/salesy
      ("Exciting news!", "Don't miss this!").

2. PERSONALIZATION SIGNALS — Segmentation beyond "Hi {FirstName}"?
   5: Content clearly tailored to recipient behavior/role/company; segments differ.
   3: Some personalization, mostly one-size-fits-all. 0: Only mail-merge name.

3. VALUE PROPOSITION CLARITY — Benefit obvious in the first sentence?
   5: First sentence states a specific benefit/relevance (knows in 5 seconds).
   3: Benefit present but buried. 0: Opens with "We're excited to announce".

4. SOCIAL PROOF — Claims backed by customer evidence or data?
   5: Specific customers named, concrete results, verifiable data.
   3: Vague ("thousands of customers"). 0: All claims, no proof.

5. FRICTION REDUCTION — Single, low-effort CTA?
   5: One obvious CTA, one click to value, clear outcome.
   3: CTA present but competing priorities/unclear outcome.
   0: Multiple competing CTAs or a high-friction ask in a promo.

REQUIRED ELEMENTS (must be present):
- Specific subject line (concrete promise, not vague excitement)
- Clear value (first sentence explains why the recipient should care)
- Single CTA (one primary action, obvious what to click)

ANTI-PATTERNS TO FLAG:
- Subject "Exciting updates!"/"You're going to love this!" (could be anything)
- Opens with "We're thrilled to announce" (company-centric)
- Multiple competing CTAs
- Personalization is only "Hi {FirstName}"
- No social proof for claims; unclear what happens on click

RULES:
- Do NOT invent customer names, survey results, or engagement stats. Flag missing
  proof as a gap; never fabricate it.
- Be surgical: 3-5 fixes that move REVISE -> ACCEPT. Quote exact locations and give
  exact replacement text. Do not rewrite the whole email.
- Prioritize fixes by impact on open rate, click rate, and preventing unsubscribes.

VERDICT THRESHOLDS:
- ACCEPT: >=4.2 overall, all required elements present, <2 critical gaps
- REVISE: 3.0-4.1 overall, OR missing 1 required element, OR 3+ gaps
- REJECT: <3.0 overall, OR subject line is vague, OR opens with "We're excited to announce"

Return strict JSON only, matching the provided schema.

EMAIL TO EVALUATE:
<paste subject, opening, body, CTA(s), segment/goal, and available-proof context here>
```

---

## False-Positive Prevention

❌ **DON'T:**
- Score `social_proof` high because the email names a number — check it's real customer evidence, not "thousands of customers."
- Invent a beta-survey result or customer name to complete a fix.
- Accept several links as "single CTA"; competing CTAs are a friction gap.
- Confuse this with a newsletter — a campaign should drive one action, not curate many items.

✅ **DO:**
- Flag unbacked claims and ask the user to supply real proof.
- Phrase example proof in fixes as clearly illustrative (e.g., "e.g., 'beta customers saved 2.3 hrs/week, N=45' — insert your real survey figure").
- Check required elements independently of the score.
- Quote the exact subject line or sentence being criticized.

---

## Output Format

```json
{
  "overall_score": 3.7,
  "axis_scores": {
    "subject_line_specificity": 4,
    "personalization_signals": 3,
    "value_proposition_clarity": 4,
    "social_proof": 3,
    "friction_reduction": 4
  },
  "verdict": "REVISE",
  "required_elements": {
    "specific_subject_line": {"present": true, "quality": "concrete but could be sharper"},
    "clear_value": {"present": true, "quality": "benefit stated in first paragraph"},
    "single_cta": {"present": true, "quality": "primary CTA clear"}
  },
  "critical_gaps": [
    "No customer proof for main claims — all assertions",
    "Personalization is just name insertion, no segmentation visible"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Subject line: 'Exciting product updates'",
      "problem": "Vague — doesn't tell the recipient what to expect or why it matters",
      "fix": "Replace with a specific benefit, e.g.: 'New Slack integration saves 2 hours/week on status updates.' Use your real feature + outcome.",
      "why": "Specific feature + concrete time savings = clear value in the subject"
    },
    {
      "priority": 2,
      "location": "Opening paragraph: 'We're excited to announce...'",
      "problem": "Company-centric opening, no immediate reader benefit",
      "fix": "Lead with the reader benefit, e.g.: 'You can now sync project status directly to Slack — no more copy-pasting updates between tools.'",
      "why": "Reader benefit first, with the pain point addressed immediately"
    },
    {
      "priority": 3,
      "location": "Claim about 'improved efficiency'",
      "problem": "Generic claim with no proof",
      "fix": "Add real proof, e.g.: 'Beta customers report saving ~2.3 hours/week on status reporting (source: beta survey, N=45).' Substitute your verified figure.",
      "why": "Specific customer + metric + methodology = credible"
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
- [ ] No fabricated customer names or stats; missing proof flagged as a gap.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Frames the job as a single-conversion engage-or-unsubscribe judgment.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five engagement axes with explicit anchors.
- **DS-02 (Metric/Criteria Specification):** Numeric thresholds and required elements specified.
- **ST-02 (Structured Output Format):** Forces strict JSON.
- **CM-02 (Explicit Constraints):** Bars fabricated proof and whole-email rewrites.

---

## Related Prompts
- `domain-productivity/validation/quality_slop_email_newsletter.md` — sibling evaluator for recurring value/relationship content (the non-conversion counterpart).
- `domain-productivity/validation/quality_slop_ad_copy.md` — sibling evaluator for paid conversion creative.
- `domain-productivity/validation/validation_reality_check.md` — surface objections recipients would raise about the claims.
