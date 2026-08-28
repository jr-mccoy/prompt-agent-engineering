---
title: "Support Response Slop Evaluator"
category: professional-writing/content-quality
description: "Score a customer support response against five resolution axes and return strict JSON with surgical, exactly-located fixes that move a generic reply toward first-contact resolution."
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
  - customer-support
  - first-contact-resolution
  - quality-evaluation
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/validation_final_gate.md
  - domain-professional-writing/content-quality/quality_slop_technical_documentation.md
  - domain-professional-writing/content-quality/quality_slop_seo_content_brief.md
---

# Support Response Slop Evaluator

**Objective:** Judge whether a customer support response (email, chat, ticket reply) will actually solve the customer's problem on first contact — or whether it's generic copy-paste that triggers a follow-up — and return a strict-JSON verdict with surgical fixes.

**When to use:**
- Before an agent sends a reply on a non-trivial or high-value ticket.
- When QA-reviewing a sample of support responses for ping-pong risk.
- When training or auditing AI-drafted support replies.

**When NOT to use:**
- For pure acknowledgment messages ("we've received your request") where resolution isn't expected.
- For policy/legal escalations where the answer is a routing decision, not a solution.

**Audience:** Support agents, support QA leads, and teams reviewing AI-generated replies.

---

## Inputs / Context

1. **The customer's message** — the original question/issue.
2. **The draft response** — the reply to be evaluated.
3. **Optional: customer context** — plan type, usage, prior tickets (helps judge context awareness).

---

## Constraints

### Must
- Score every axis 0–5 using the anchors below; compute `overall_score` as the mean.
- Check each required element for presence and quality.
- Give 3–5 surgical fixes, each with an exact location, the exact problem, exact replacement text, and why it matters.
- Return strict, parseable JSON exactly matching the Output Format schema.

### Must Not
- Rewrite the whole response; point to exact spots and give exact replacement text only.
- Invent product behavior, pricing, menu paths, plan limits, or customer history that aren't given — any such specifics in example fixes are illustrative placeholders the agent must verify against the real product.
- Fabricate that a step will work; if a step can't be verified, flag it as needing confirmation.
- Pad to five fixes — give only the fixes that genuinely move REVISE → ACCEPT.

---

## Instructions

1. **Load the customer message and draft response** as the artifact under review.
2. **Run the evaluator prompt below verbatim**, pasting both where indicated.
3. **Score, gap-check, and prioritize fixes**, then emit strict JSON.

```
You are evaluating a customer support response (email, chat, ticket reply).
Your job: determine if this actually solves the customer's problem on first
contact — or if it's generic copy-paste that will create a follow-up.

Score each axis 0–5:

1. PROBLEM COMPREHENSION — does it show understanding of the specific issue?
   5 = Accurately paraphrases the issue and answers the actual question asked.
   3 = Generally understands but misses nuance or part of the question.
   0 = Generic; could be answering a different question.

2. SOLUTION COMPLETENESS — everything needed to resolve the issue?
   5 = Step-by-step, covers edge cases, anticipates follow-ups; executable
       without asking again.
   3 = Solution present but missing steps or assumes knowledge.
   0 = Vague ("check your settings") with no specifics.

3. CLARITY AND PRECISION — can a non-technical user follow it?
   5 = Numbered steps, exact click locations, what to expect, specific field
       names.
   3 = Generally clear but some ambiguity or unexplained jargon.
   0 = Jargon, vague directions, no specifics.

4. CONTEXT AWARENESS — does it reference the customer's situation?
   5 = Personalized to plan type, usage, or prior interactions.
   3 = Some personalization, mostly generic.
   0 = Copy-paste that ignores context.

5. PROACTIVE GUIDANCE — does it prevent related problems / point to resources?
   5 = Anticipates the next question, links related docs, offers proactive help.
   3 = Solves the immediate problem only.
   0 = Bare-minimum answer.

REQUIRED ELEMENTS (check present + quality):
- problem_acknowledgment — shows the specific issue was understood
- complete_solution — all steps to resolve, no gaps
- next_step_clarity — what to do now and what to expect

ANTI-PATTERNS to flag:
- Generic greeting with no issue acknowledgment ("Thanks for reaching out!")
- Copy-paste answer to a related-but-different question
- Vague instructions ("check your account settings" — which? where?)
- Unexplained technical jargon
- Missing steps that assume customer knowledge
- No validation that the solution fits the customer's situation
- No clear "what happens next"

RULES:
- Be surgical. Give 3–5 fixes with EXACT location, problem, exact replacement
  text, and why. Do not rewrite the whole response.
- Do NOT invent product behavior, menu paths, pricing, plan limits, or customer
  history. Any such specifics in your replacement text are illustrative
  placeholders the agent must verify against the real product; label them.
- If a step's correctness can't be confirmed, flag it as needing verification
  rather than asserting it works.
- Prioritize fixes by impact on first-response resolution.
- Return STRICT JSON only, matching the provided schema.

[PASTE CUSTOMER MESSAGE AND DRAFT RESPONSE HERE]
```

4. **Apply the verdict thresholds** (below) to set `verdict`.
5. **Deliver** the strict JSON.

**Verdict thresholds:**
- **ACCEPT:** ≥4.2 overall, all required elements present, <2 critical gaps.
- **REVISE:** 3.0–4.1 overall, OR missing 1 required element, OR solution has gaps the customer can't fill.
- **REJECT:** <3.0 overall, OR doesn't address the actual question, OR instructions are too vague to execute.

---

## False-Positive Prevention

❌ **DON'T:**
- Invent a menu path, setting name, price, or plan limit you can't confirm.
- Assert that "this will fix it" when the step is unverified.
- Pass a polite-but-empty reply just because the tone is warm.
- Rewrite the whole response instead of giving located fixes.

✅ **DO:**
- Treat product specifics and figures in example fixes as illustrative placeholders labeled "verify against the product."
- Flag any unverifiable step as needing confirmation.
- Point to exact locations with exact replacement text.
- Give only the fixes that genuinely change the verdict.

---

## Output Format

Return strict JSON only:

```json
{
  "overall_score": 3.7,
  "axis_scores": {
    "problem_comprehension": 4,
    "solution_completeness": 3,
    "clarity_and_precision": 4,
    "context_awareness": 3,
    "proactive_guidance": 4
  },
  "verdict": "REVISE",
  "required_elements": {
    "problem_acknowledgment": {"present": true, "quality": "acknowledges the issue correctly"},
    "complete_solution": {"present": true, "quality": "present but missing one step"},
    "next_step_clarity": {"present": true, "quality": "clear what to do next"}
  },
  "critical_gaps": [
    "Missing the navigation step between two instructions — customer will guess",
    "Doesn't confirm the feature is available on the customer's plan"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Step 2 ('Click Settings and find your API key')",
      "problem": "Jumps from Settings to the key with no navigation path",
      "fix": "Replace with an exact path (menu name, location, visual landmark, where in the page). [Confirm the real menu structure before sending.]",
      "why": "Exact path + landmark = customer executes without guessing"
    },
    {
      "priority": 2,
      "location": "Missing from response",
      "problem": "Doesn't check the customer's plan has this feature",
      "fix": "Add a plan check and an alternative if it's not available. [Verify the customer's actual plan and feature availability.]",
      "why": "Validates the solution fits, preventing a dead-end reply"
    },
    {
      "priority": 3,
      "location": "End of response",
      "problem": "No expectations for what happens after the steps",
      "fix": "Add expected timing and a clear escalation path if it still fails. [Use the real activation time.]",
      "why": "Sets timing expectations and a fallback if the fix doesn't work"
    }
  ]
}
```

---

## Verification

- [ ] Every axis scored 0–5 with anchors; `overall_score` is the mean.
- [ ] Each required element checked for presence and quality.
- [ ] 3–5 fixes, each with exact location, problem, replacement text, and why.
- [ ] No invented product behavior, paths, pricing, plan limits, or history.
- [ ] Unverifiable steps flagged for confirmation, not asserted.
- [ ] Verdict matches the thresholds; output is strict, parseable JSON.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Fixes the job as judging first-contact resolution, not rewriting the reply.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five orthogonal axes (comprehension, completeness, clarity, context, proactivity).
- **DS-02 (Metric/Criteria Specification):** 0–5 anchors and verdict thresholds make scoring repeatable.
- **ST-02 (Structured Output Format):** Strict JSON schema for downstream tooling.
- **CM-02 (Explicit Constraints):** Must/Must-Not bars fabricated product facts and whole-reply rewrites.

---

## Related Prompts
- `domain-productivity/validation/validation_final_gate.md` — broader pre-ship gate for high-stakes replies.
- `domain-professional-writing/content-quality/quality_slop_technical_documentation.md` — sibling evaluator for developer docs.
- `domain-professional-writing/content-quality/quality_slop_seo_content_brief.md` — sibling evaluator for SEO briefs.
