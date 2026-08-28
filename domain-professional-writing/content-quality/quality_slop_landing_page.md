---
title: "Landing Page Copy Slop Detector"
category: professional-writing/content-quality
description: "Score landing page copy (hero, benefits, CTAs) against five conversion axes and return surgical fixes so a first-time visitor grasps the value in seconds instead of bouncing."
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
  - landing-page
  - conversion-copy
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-professional-writing/content-quality/quality_slop_product_description.md
  - domain-professional-writing/content-quality/quality_slop_sales_outreach.md
  - domain-productivity/validation/validation_reality_check.md
---

# Landing Page Copy Slop Detector

**Objective:** Judge whether landing page copy makes value immediately clear and converts — or whether the visitor bounces because the benefit, proof, and next step are vague — and return exact, location-anchored fixes.

**When to use:**
- Before launching or iterating on a hero/benefits/CTA section.
- When a page has high traffic but low conversion or high bounce.
- To QA AI-drafted landing copy for generic, feature-first slop.

**When NOT to use:**
- A long-form sales letter or product spec page where depth matters more than scan-time.
- A product catalog listing — use the product-description detector.

**Audience:** Marketers, founders, growth/PMM teams, and anyone reviewing landing copy before publishing.

---

## Inputs / Context

1. **The copy** — hero headline, subhead, benefits, and CTA(s) being evaluated.
2. **Target visitor** — who lands here and what they're trying to accomplish.
3. **Goal** — the primary conversion action (trial start, demo, signup, purchase).

---

## Constraints

### Must
- Score all five axes 0–5 using the anchors provided.
- Anchor every fix to an exact location in the copy and give exact replacement text.
- Verify each required element is present and assess its quality.
- Return strict JSON only, matching the Output Format.

### Must Not
- Invent customer names, metrics, or testimonials about the product being judged; any specifics in *example* fix text are illustrative placeholders the author must replace with verifiable data.
- Fabricate social proof or claim the copy contains proof it does not — flag missing proof, never supply imaginary proof.
- Rewrite the whole page; restrict yourself to 3–5 high-impact surgical fixes.

---

## Instructions

1. Collect the copy, the target visitor, and the conversion goal.
2. Run the evaluator below verbatim against the copy.
3. Return strict JSON only (no prose outside the JSON).

```
# Landing Page Copy Quality Evaluator

You are evaluating landing page copy (hero section, benefits, CTAs). Your job: determine if a
visitor will convert—or bounce because value isn't immediately clear.

## Why This Matters
Bad landing pages get <2% conversion with high bounce rates. Good landing pages get 5-15%.
The difference: immediate value clarity, objection handling, and specific proof. Every second
of confusion costs conversions.

## Evaluation Dimensions (score each 0-5)

### 1. Value Proposition Clarity — can a first-time visitor understand the benefit in 5 seconds?
Score 5: Hero states a specific outcome in user language.
  ("Deploy new features 3x faster without breaking production.")
Score 3: Benefit present but requires reading multiple elements to understand.
Score 0: Generic or feature-first. ("The modern platform for teams.")

### 2. Specificity and Proof — claims backed by concrete evidence?
Score 5: Specific customer examples with metrics.
  ("Acme Corp reduced deployment time from 4 hours to 45 minutes.")
Score 3: Some proof but vague—"trusted by thousands" without specifics.
Score 0: All claims, no proof. ("Industry-leading" with nothing behind it.)

### 3. Objection Handling — addresses why not competitor/DIY/status quo?
Score 5: Explicitly handles the top 3 objections.
  ("Unlike Jenkins, no server maintenance. Unlike GitHub Actions, no YAML complexity. Set up in 10 minutes.")
Score 3: Addresses some objections implicitly through features but not explicitly.
Score 0: No objection handling. Assumes the visitor has no alternatives.

### 4. CTA Clarity and Friction — obvious what happens on click and how much effort is required?
Score 5: CTA specifies the exact next step and removes friction.
  ("Start free trial—No credit card, 14 days." / "Watch 2-min demo.")
Score 3: CTA present but outcome or effort level unclear.
Score 0: Vague CTA like "Get Started" or "Learn More" without specifics.

### 5. Message Hierarchy — do you read the most important information first?
Score 5: Hero states benefit, subheading adds specificity, visuals support. Natural eye path.
Score 3: Important info present but competes with less important elements.
Score 0: Layout buries key benefits. The visitor has to hunt for the value proposition.

## Required Elements (must have)
- Clear value proposition: specific benefit in the hero (not generic)
- Social proof: customer names, metrics, or credible testimonials
- Low-friction CTA: specific next step with friction removed

## Anti-Patterns to Flag (specific to landing pages)
- Generic hero: "The modern solution for..." (what does it do?)
- Feature-first: lists capabilities without outcomes
- No proof: "Trusted by thousands" without naming anyone
- Vague CTAs: "Get Started" (started with what? how long?)
- Missing objection handling: doesn't address obvious concerns
- No specificity: "Save time and money" (how much? for whom?)
- Competing CTAs: multiple buttons with unclear priority

## Verdict Thresholds
ACCEPT: >=4.2 overall, all required elements present, <2 critical gaps
REVISE: 3.0-4.1 overall, OR missing 1 required element, OR value prop unclear
REJECT: <3.0 overall, OR hero is generic/feature-first, OR no social proof

## Instructions
Be surgical: give 3-5 specific fixes that move REVISE -> ACCEPT.
Do not rewrite the whole thing. Point to exact locations and give exact replacement text.
Prioritize fixes by impact—what matters most for immediate value comprehension and conversion?
Do not invent customer names, metrics, or testimonials; flag missing proof rather than fabricating it.

Return strict JSON in the format specified below.
```

---

## False-Positive Prevention

❌ **DON'T:**
- Penalize a concise hero for being short when the outcome is specific and in the user's language.
- Reward number-laden copy whose metrics are unverifiable or invented.
- Supply a fabricated customer name or stat to "fix" weak proof.
- Demand objection handling for objections the audience doesn't actually have.

✅ **DO:**
- Reward a sharp, specific value proposition even when phrased in a single line.
- Treat illustrative customer names/metrics in fix text as placeholders to be replaced with real data.
- Flag missing or vague proof as a gap; instruct the author to add verifiable evidence.
- Match objection handling to the visitor's real alternatives (competitor, DIY, status quo).

---

## Output Format

```json
{
  "overall_score": 3.5,
  "axis_scores": {
    "value_proposition_clarity": 3,
    "specificity_and_proof": 3,
    "objection_handling": 3,
    "cta_clarity_and_friction": 4,
    "message_hierarchy": 4
  },
  "verdict": "ACCEPT | REVISE | REJECT",
  "required_elements": {
    "clear_value_proposition": {"present": true, "quality": "benefit mentioned but somewhat generic"},
    "social_proof": {"present": true, "quality": "mentions customers but no specific names or metrics"},
    "low_friction_cta": {"present": true, "quality": "CTA clear, friction removed"}
  },
  "critical_gaps": [
    "Hero is feature-focused, not outcome-focused",
    "No handling of the obvious objection about setup complexity"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Hero headline: 'Powerful CI/CD platform for modern teams'",
      "problem": "Generic and feature-focused—doesn't state a specific benefit",
      "fix": "Replace with: 'Deploy code to production in 15 minutes, not 4 hours.'",
      "why": "A specific time saving is a concrete benefit the visitor can evaluate; 'powerful platform' means nothing"
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
- [ ] No invented customer names, metrics, or testimonials; missing proof flagged, not fabricated.
- [ ] Output is strict JSON with no surrounding prose.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Frames the job as judging value clarity and conversion likelihood.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five orthogonal conversion axes structure the evaluation.
- **DS-02 (Metric/Criteria Specification):** 0–5 anchors and ACCEPT/REVISE/REJECT thresholds define scoring precisely.
- **ST-02 (Structured Output Format):** Strict JSON schema makes results machine-readable.
- **CM-02 (Explicit Constraints):** Must/Must-Not bound the evaluator and forbid fabricated proof.

---

## Related Prompts
- `domain-professional-writing/content-quality/quality_slop_product_description.md` — sibling detector for product/listing copy.
- `domain-professional-writing/content-quality/quality_slop_sales_outreach.md` — sibling detector for outreach messaging.
- `domain-productivity/validation/validation_reality_check.md` — surface objections a skeptical visitor would raise.
