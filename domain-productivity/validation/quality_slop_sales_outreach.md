---
title: "Sales Outreach Email Slop Detector"
category: "productivity/validation"
description: "Score a cold/warm outreach email against five quality axes and return surgical fixes so a busy exec can tell it was written for them — not blasted to 1,000 prospects with find-replace."
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
  - sales-outreach
  - cold-email
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/quality_slop_follow_up_email.md
  - domain-productivity/validation/quality_slop_landing_page.md
  - domain-productivity/validation/validation_reality_check.md
---

# Sales Outreach Email Slop Detector

**Objective:** Judge whether a cold/warm outreach email reads as specifically written for the recipient — or as a mass-mailable template — and return exact, location-anchored fixes that raise response rate.

**When to use:**
- Before sending a first-touch cold or warm outreach email.
- When an outreach sequence is getting near-zero replies.
- To QA AI-drafted outreach for "I hope this finds you well" template slop.

**When NOT to use:**
- A follow-up after an existing conversation — use the follow-up-email detector.
- Bulk newsletter or marketing-broadcast copy (different intent and metrics).

**Audience:** SDRs, AEs, founders, and anyone reviewing outreach drafts before they send.

---

## Inputs / Context

1. **The draft** — the outreach email being evaluated.
2. **Recipient context** — who they are and any real, observable signals (funding, hiring, launch, role change).
3. **Goal** — the low-friction next step a positive reply should produce.

---

## Constraints

### Must
- Score all five axes 0–5 using the anchors provided.
- Anchor every fix to an exact location in the draft and give exact replacement text.
- Verify each required element is present and assess its quality.
- Return strict JSON only, matching the Output Format.

### Must Not
- Invent recipient signals, customer names, or metrics about the draft being judged; any specifics in *example* fix text are illustrative placeholders the author must replace with verified research and proof.
- Fabricate personalization or social proof the draft lacks — flag missing research/proof, never supply imaginary signals.
- Rewrite the whole email; restrict yourself to 3–5 high-impact surgical fixes.

---

## Instructions

1. Collect the draft, the recipient context, and the goal.
2. Run the evaluator below verbatim against the draft.
3. Return strict JSON only (no prose outside the JSON).

```
# Sales Outreach Email Quality Evaluator

You are evaluating a cold/warm sales outreach email. Your job: determine if a busy exec can tell
this email is specifically for them—or if it could be sent to 1,000 people with find-replace.

## Why This Matters
Bad outreach burns prospect relationships, wastes sales capacity, and damages sender reputation.
Generic emails get 0-2% response rates. Good emails get 8-15%. The difference is personalization
and relevance.

## Evaluation Dimensions (score each 0-5)

### 1. Personalization Depth — evidence of research beyond company name?
Score 5: References a specific recent event (funding, hiring, launch, exec change) with an
  observation about what it means. Shows 5+ minutes of research.
Score 3: Mentions a company-specific detail but surface-level. Could be automated research.
Score 0: "Hi [FirstName], I see you work at [Company]" with no other personalization. Pure template.

### 2. Problem Hypothesis — a specific, educated guess at their pain point?
Score 5: Names a specific problem tied to their situation with reasoning.
  ("You just posted 4 SDR roles—guessing onboarding speed is critical right now.")
Score 3: Generic problem that applies to all companies in their category.
Score 0: No problem hypothesis. Just describes what you do.

### 3. Relevance Signal — a clear reason why this email matters now?
Score 5: Timing trigger is explicit and logical (hiring spike, launch, funding, seasonal factor).
Score 3: Some relevance but timing is vague or assumed.
Score 0: No timing hook. ("Reaching out to see if you're interested.")

### 4. Value Clarity — benefit stated in their outcomes, not your features?
Score 5: Specific customer outcome with numbers.
  ("Acme reduced sales onboarding from 8 weeks to 3 weeks.")
Score 3: Mentions benefits but stays generic or feature-focused.
Score 0: Feature dump. ("Our platform offers X, Y, Z capabilities.")

### 5. Ask Size — requested commitment appropriately low-friction?
Score 5: Micro-ask matched to the relationship stage.
  ("Worth a look?" / "Should I send you the 2-minute demo?")
Score 3: Reasonable ask but slightly heavy for cold outreach ("15-minute call").
Score 0: High-friction ask for cold email ("30-minute demo" or vague "let's chat").

## Required Elements (must have)
- Personalization signal: evidence of research specific to this recipient
- Problem hypothesis: educated guess at what they care about right now
- Low-friction ask: clear next step that takes <5 minutes to evaluate

## Anti-Patterns to Flag (specific to sales outreach)
- "I hope this email finds you well" / "Reaching out to connect"
- Could be sent to 1,000 people with company-name find-replace
- No hypothesis about their actual problems—just pitching your product
- High-friction ask on cold email: "30-minute demo," "Let's schedule time"
- Feature dump without customer proof or outcomes
- No timing trigger—why this email now vs. 6 months ago?

## Verdict Thresholds
ACCEPT: >=4.2 overall, all required elements present, <2 critical gaps
REVISE: 3.0-4.1 overall, OR missing 1 required element, OR 3+ gaps
REJECT: <3.0 overall, OR could be sent to 1,000 people with find-replace, OR starts with "I hope this finds you well"

## Instructions
Be surgical: give 3-5 specific fixes that move REVISE -> ACCEPT.
Do not rewrite the whole thing. Point to exact locations and give exact replacement text.
Prioritize fixes by impact—what matters most for proving you're not mass-mailing 500 prospects?
Do not invent recipient signals, customer names, or metrics; flag missing research/proof rather than fabricating it.

Return strict JSON in the format specified below.
```

---

## False-Positive Prevention

❌ **DON'T:**
- Penalize a short, sharp email for being short when it shows real research and a low-friction ask.
- Reward a templated line dressed up with a company name but no genuine insight.
- Invent a funding round, hire, or customer metric to "fix" weak personalization.
- Demand a timing trigger when no real, observable signal exists.

✅ **DO:**
- Reward a genuine, researched signal plus a relevant problem hypothesis even in two lines.
- Treat illustrative signals/metrics in fix text as placeholders for verified research and proof.
- Flag missing personalization or proof as a gap; never fabricate a signal or a customer result.
- Match ask size to the relationship stage (cold = micro-ask).

---

## Output Format

```json
{
  "overall_score": 3.4,
  "axis_scores": {
    "personalization_depth": 4,
    "problem_hypothesis": 3,
    "relevance_signal": 3,
    "value_clarity": 3,
    "ask_size": 4
  },
  "verdict": "ACCEPT | REVISE | REJECT",
  "required_elements": {
    "personalization_signal": {"present": true, "quality": "mentions recent funding but doesn't connect it to a problem"},
    "problem_hypothesis": {"present": true, "quality": "generic for their industry"},
    "low_friction_ask": {"present": true, "quality": "good—just asks if it's worth exploring"}
  },
  "critical_gaps": [
    "Problem hypothesis is generic—could apply to any SaaS company",
    "No clear reason why this matters now vs. 3 months ago"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Opening line",
      "problem": "Starts with 'I hope this email finds you well'—instant delete signal",
      "fix": "Replace with: 'Saw you just posted 6 sales roles on LinkedIn—congrats on the growth.'",
      "why": "Shows research, references a specific observable event, creates relevance"
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
- [ ] No invented signals, customer names, or metrics; missing research/proof flagged, not fabricated.
- [ ] Output is strict JSON with no surrounding prose.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Frames the job as judging whether the email reads as written-for-them.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five orthogonal axes (personalization, problem hypothesis, relevance, value, ask size).
- **DS-02 (Metric/Criteria Specification):** 0–5 anchors and ACCEPT/REVISE/REJECT thresholds define scoring precisely.
- **ST-02 (Structured Output Format):** Strict JSON schema makes results machine-readable.
- **CM-02 (Explicit Constraints):** Must/Must-Not bound the evaluator and forbid fabricated signals or proof.

---

## Related Prompts
- `domain-productivity/validation/quality_slop_follow_up_email.md` — sibling detector for post-conversation follow-ups.
- `domain-productivity/validation/quality_slop_landing_page.md` — sibling detector for conversion landing copy.
- `domain-productivity/validation/validation_reality_check.md` — surface objections a skeptical prospect would raise.
