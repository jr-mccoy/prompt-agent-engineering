---
title: "Product Description Slop Detector"
category: "productivity/validation"
description: "Score a product description (e-commerce, SaaS page, marketplace listing) against five quality axes and return surgical fixes so a buyer can confidently evaluate fit instead of bouncing on vague marketing."
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
  - product-description
  - conversion-copy
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/quality_slop_landing_page.md
  - domain-productivity/validation/quality_slop_sales_outreach.md
  - domain-productivity/validation/validation_reality_check.md
---

# Product Description Slop Detector

**Objective:** Judge whether a product description lets a buyer confidently evaluate fit — or whether it's vague marketing that could describe anything — and return exact, location-anchored fixes.

**When to use:**
- Before publishing an e-commerce, SaaS, or marketplace listing.
- When a product page has traffic but low conversion or high return/support volume.
- To QA AI-drafted product copy for "could describe any product" slop.

**When NOT to use:**
- A full landing page with hero + CTAs — use the landing-page detector.
- Internal product documentation aimed at existing users, not buyers.

**Audience:** PMMs, e-commerce/merchandising teams, founders, and anyone reviewing product copy before publishing.

---

## Inputs / Context

1. **The description** — the product copy being evaluated.
2. **Target buyer** — the persona/company type the product is designed for.
3. **Goal** — the buying decision the copy should enable (purchase, trial, add-to-cart).

---

## Constraints

### Must
- Score all five axes 0–5 using the anchors provided.
- Anchor every fix to an exact location in the description and give exact replacement text.
- Verify each required element is present and assess its quality.
- Return strict JSON only, matching the Output Format.

### Must Not
- Invent competitor comparisons, specs, prices, or capabilities about the product being judged; any specifics in *example* fix text are illustrative placeholders the author must replace with verified data.
- Fabricate differentiation or proof the copy lacks — flag missing comparisons/specs, never supply imaginary ones.
- Rewrite the whole description; restrict yourself to 3–5 high-impact surgical fixes.

---

## Instructions

1. Collect the description, the target buyer, and the goal.
2. Run the evaluator below verbatim against the description.
3. Return strict JSON only (no prose outside the JSON).

```
# Product Description Quality Evaluator

You are evaluating a product description (e-commerce, SaaS product page, marketplace listing).
Your job: determine if a buyer can confidently evaluate fit—or if this is vague marketing that
could describe anything.

## Why This Matters
Bad product descriptions create returns, support tickets, and low conversion. Generic descriptions
get <2% conversion. Good descriptions get 5-12%. The difference: specificity about who it's for,
what problem it solves, and how it's different.

## Evaluation Dimensions (score each 0-5)

### 1. Use Case Specificity — clear who should buy this and for what purpose?
Score 5: Names specific buyer personas and exact use cases with scenarios.
  ("For marketing teams (10-50 people) who coordinate content calendars across 3+ channels.")
Score 3: Somewhat clear but could apply to a broader audience; use cases implied, not explicit.
Score 0: "For anyone who wants to improve productivity." Could be for anyone.

### 2. Problem-Solution Mapping — articulates the specific pain point this addresses?
Score 5: Clear problem statement with why current alternatives fail.
  ("Spreadsheets break when 5+ people edit them. Slack threads get lost. This keeps everything synced.")
Score 3: Problem implied but not explicitly stated.
Score 0: Just describes features; doesn't explain what problem exists.

### 3. Differentiation — explains why not alternatives (competitors, DIY, status quo)?
Score 5: Explicit comparison.
  ("Unlike Competitor X which requires manual export/import, we sync automatically.")
Score 3: Differentiation implied through features but not explicit.
Score 0: No mention of alternatives. Unclear why not just use something else.

### 4. Technical Precision — specs detailed enough to evaluate fit without guessing?
Score 5: Specific measurements, capacities, requirements.
  ("Handles up to 50,000 records, processes in <200ms, requires 2GB RAM.")
Score 3: Some specs but missing key details someone would need.
Score 0: Vague technical claims: "Fast," "powerful," "scales easily" with no numbers.

### 5. Objection Preemption — addresses likely concerns before they become blockers?
Score 5: Anticipates and addresses the top 3 concerns.
  ("No credit card required," "Cancel anytime," "Works with your existing tools (list).")
Score 3: Addresses some concerns but misses obvious ones.
Score 0: Doesn't anticipate or address buyer concerns.

## Required Elements (must have)
- Target user: specific persona or company type this is designed for
- Problem statement: what pain point this solves
- Key differentiator: why not alternatives (at least one specific comparison)

## Anti-Patterns to Flag (specific to product descriptions)
- Could describe any similar product—nothing distinctive
- No specific use cases—just feature lists
- Feature dump without explaining benefits or context
- Vague specs: "Fast processing" without defining fast
- No comparison to alternatives—exists in a vacuum
- Doesn't address obvious concerns (pricing, setup time, integration)

## Verdict Thresholds
ACCEPT: >=4.2 overall, all required elements present, <2 critical gaps
REVISE: 3.0-4.1 overall, OR missing 1 required element, OR 3+ gaps
REJECT: <3.0 overall, OR missing 2+ required elements, OR could describe any similar product

## Instructions
Be surgical: give 3-5 specific fixes that move REVISE -> ACCEPT.
Do not rewrite the whole thing. Point to exact locations and give exact replacement text.
Prioritize fixes by impact—what matters most for buyer confidence and conversion?
Do not invent comparisons, specs, or prices; flag missing items rather than fabricating them.

Return strict JSON in the format specified below.
```

---

## False-Positive Prevention

❌ **DON'T:**
- Penalize a concise description for being short when buyer, problem, and differentiator are all clear.
- Reward feature-laden copy that lists capabilities but never names who it's for or why it's different.
- Supply a fabricated competitor comparison or spec to "fix" weak differentiation.
- Demand objection handling for concerns this buyer doesn't actually have.

✅ **DO:**
- Reward specific personas, an explicit problem, and at least one real comparison even in short copy.
- Treat illustrative specs/comparisons in fix text as placeholders to be replaced with verified data.
- Flag missing specs, comparisons, or proof as gaps; never invent them.
- Match objection preemption to the buyer's real concerns (pricing, setup, integration).

---

## Output Format

```json
{
  "overall_score": 3.6,
  "axis_scores": {
    "use_case_specificity": 4,
    "problem_solution_mapping": 3,
    "differentiation": 3,
    "technical_precision": 4,
    "objection_preemption": 3
  },
  "verdict": "ACCEPT | REVISE | REJECT",
  "required_elements": {
    "target_user": {"present": true, "quality": "mentions team size but vague on role"},
    "problem_statement": {"present": true, "quality": "implies the problem but doesn't state it"},
    "key_differentiator": {"present": false, "quality": "no comparison to alternatives mentioned"}
  },
  "critical_gaps": [
    "No explicit comparison to alternatives—unclear why not use Competitor X",
    "Doesn't address the setup-time concern buyers typically have"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Opening paragraph",
      "problem": "Doesn't explicitly state who this is for",
      "fix": "Add: 'Built for B2B sales teams (5-50 reps) who need to track deals across multiple stakeholders without complex CRM setup.'",
      "why": "Specific persona + company size + use case + implicit objection (complexity) = clear targeting"
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
- [ ] No invented comparisons, specs, or prices; missing items flagged, not fabricated.
- [ ] Output is strict JSON with no surrounding prose.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Frames the job as judging buyer confidence and fit-evaluation.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five orthogonal axes (use case, problem-solution, differentiation, precision, objection preemption).
- **DS-02 (Metric/Criteria Specification):** 0–5 anchors and ACCEPT/REVISE/REJECT thresholds define scoring precisely.
- **ST-02 (Structured Output Format):** Strict JSON schema makes results machine-readable.
- **CM-02 (Explicit Constraints):** Must/Must-Not bound the evaluator and forbid fabricated specs or comparisons.

---

## Related Prompts
- `domain-productivity/validation/quality_slop_landing_page.md` — sibling detector for hero/benefits/CTA landing copy.
- `domain-productivity/validation/quality_slop_sales_outreach.md` — sibling detector for outreach messaging.
- `domain-productivity/validation/validation_reality_check.md` — surface objections a skeptical buyer would raise.
