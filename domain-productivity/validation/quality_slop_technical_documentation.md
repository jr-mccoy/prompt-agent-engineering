---
title: "Technical Documentation Slop Evaluator"
category: "productivity/validation"
description: "Score technical documentation against five implementability axes and return strict JSON with surgical, exactly-located fixes that move docs toward zero-support self-service implementation."
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
  - technical-documentation
  - developer-experience
  - quality-evaluation
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/validation_final_gate.md
  - domain-productivity/validation/quality_slop_support_response.md
  - domain-productivity/validation/quality_slop_seo_content_brief.md
---

# Technical Documentation Slop Evaluator

**Objective:** Judge whether technical documentation (API docs, integration guides, architecture docs) lets a developer implement successfully without asking for help — or whether they'll get stuck — and return a strict-JSON verdict with surgical fixes.

**When to use:**
- Before publishing or shipping developer-facing docs.
- When integration-related support tickets spike and you suspect the docs.
- When auditing docs for production-readiness, not just "it works" coverage.

**When NOT to use:**
- For internal design RFCs or proposals (these aren't implementation docs).
- For end-user product help where code examples and error references don't apply.

**Audience:** Technical writers, developer-experience teams, and engineers reviewing docs.

---

## Inputs / Context

1. **The documentation** — the doc text (and code examples) to be evaluated.
2. **Target audience level** — e.g. first-time integrator vs. experienced API user.
3. **Optional: the API/system specifics** — versions, auth model (to judge accuracy).

---

## Constraints

### Must
- Score every axis 0–5 using the anchors below; compute `overall_score` as the mean.
- Check each required element for presence and quality.
- Give 3–5 surgical fixes, each with an exact location, the exact problem, exact replacement text, and why it matters.
- Return strict, parseable JSON exactly matching the Output Format schema.

### Must Not
- Rewrite the whole doc; point to exact spots and give exact replacement text only.
- Invent error codes, rate limits, endpoint names, auth header formats, or API behavior that aren't in the doc — any such specifics in example fixes are illustrative placeholders the writer must verify against the real API.
- Assert that example code runs; if you can't confirm it, flag it as needing testing.
- Pad to five fixes — give only the fixes that genuinely move REVISE → ACCEPT.

---

## Instructions

1. **Load the documentation** as the artifact under review.
2. **Run the evaluator prompt below verbatim**, pasting the doc where indicated.
3. **Score, gap-check, and prioritize fixes**, then emit strict JSON.

```
You are evaluating technical documentation (API docs, integration guides,
architecture docs). Your job: determine if a developer can successfully
implement this — or if they'll get stuck and need to ask for help.

Score each axis 0–5:

1. COMPLETENESS — are all necessary steps and concepts covered?
   5 = Every step from setup to production; auth, error handling, rate limits,
       best practices.
   3 = Core functionality only; missing edge cases or production considerations.
   0 = Gaps in the critical path; developer will get stuck.

2. CODE EXAMPLE QUALITY — runnable and representative?
   5 = Complete, runnable examples for common use cases, with error handling
       and realistic scenarios.
   3 = Present but oversimplified or missing error handling.
   0 = No examples, or non-runnable pseudocode.

3. ERROR COVERAGE — likely errors documented with solutions?
   5 = Common errors with exact codes/messages and exact fixes.
   3 = Some error scenarios; missing common ones.
   0 = No error documentation.

4. STRUCTURAL CLARITY — can a developer find what they need in 60 seconds?
   5 = Clear navigation, TOC, progressive disclosure (quick start → reference).
   3 = Readable but suboptimal organization.
   0 = Wall of text; must read everything to find anything.

5. PRODUCTION READINESS — covers production concerns beyond "making it work"?
   5 = Rate limits, token rotation, scaling, monitoring, security best practices.
   3 = Thin coverage of production concerns.
   0 = Basic functionality only.

REQUIRED ELEMENTS (check present + quality):
- quick_start — a working example in <10 minutes
- complete_code_examples — runnable code for primary use cases
- error_documentation — common errors and how to fix them
- authentication — how to securely auth requests

ANTI-PATTERNS to flag:
- No quick start (20 pages of concepts before any code)
- Pseudocode that can't run
- Examples with no error handling
- No guidance on common errors
- Outdated examples (old versions / deprecated methods)
- Missing production considerations (rate limits, rotation, monitoring)
- Assumes knowledge with no prerequisite links
- No search or table of contents

RULES:
- Be surgical. Give 3–5 fixes with EXACT location, problem, exact replacement
  text, and why. Do not rewrite the whole doc.
- Do NOT invent error codes, rate limits, endpoints, auth formats, or API
  behavior. Any such specifics in your replacement text are illustrative
  placeholders the writer must verify against the real API; label them.
- Do NOT assert example code runs; if unverified, flag it as needing testing.
- Prioritize fixes by impact on self-service implementation.
- Return STRICT JSON only, matching the provided schema.

[PASTE DOCUMENTATION HERE]
```

4. **Apply the verdict thresholds** (below) to set `verdict`.
5. **Deliver** the strict JSON.

**Verdict thresholds:**
- **ACCEPT:** ≥4.2 overall, all required elements present, <2 critical gaps.
- **REVISE:** 3.0–4.1 overall, OR missing 1 required element, OR examples lack error handling.
- **REJECT:** <3.0 overall, OR no code examples, OR missing critical implementation steps.

---

## False-Positive Prevention

❌ **DON'T:**
- Invent an error code, rate limit, endpoint, or auth header format you can't confirm.
- Claim example code is runnable without it being tested.
- Pass docs because they're long and well-formatted — coverage of the critical path is what matters.
- Rewrite the whole doc instead of giving located fixes.

✅ **DO:**
- Treat API specifics and figures in example fixes as illustrative placeholders labeled "verify against the API."
- Flag unverified code as needing testing.
- Point to exact locations with exact replacement text.
- Give only the fixes that genuinely change the verdict.

---

## Output Format

Return strict JSON only:

```json
{
  "overall_score": 3.4,
  "axis_scores": {
    "completeness": 3,
    "code_example_quality": 3,
    "error_coverage": 3,
    "structural_clarity": 4,
    "production_readiness": 3
  },
  "verdict": "REVISE",
  "required_elements": {
    "quick_start": {"present": true, "quality": "exists but example omits authentication"},
    "complete_code_examples": {"present": true, "quality": "present but no error handling shown"},
    "error_documentation": {"present": false, "quality": "no dedicated error documentation"},
    "authentication": {"present": true, "quality": "auth mentioned but implementation unclear"}
  },
  "critical_gaps": [
    "Code examples omit error handling — will fail silently in production",
    "No documentation of common errors — developer gets stuck debugging"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Quick Start code example",
      "problem": "Shows a successful call but no error handling",
      "fix": "Wrap the call in try/catch and branch on the real error codes (rate-limit, auth-expired, fallback). [Use the API's actual error codes; test the snippet.]",
      "why": "A realistic example with error handling prevents production failures"
    },
    {
      "priority": 2,
      "location": "Missing from documentation",
      "problem": "No error reference — developers can't self-serve fixes",
      "fix": "Add a 'Common Errors' section mapping each real error code/message to an exact fix. [Populate with the API's actual codes; do not invent them.]",
      "why": "Exact errors + exact fixes = self-service instead of a support ticket"
    },
    {
      "priority": 3,
      "location": "Authentication section",
      "problem": "Says 'include API key in header' without the exact format",
      "fix": "Show the exact header format, a runnable example call, and a 'never commit keys' warning. [Confirm the real auth scheme.]",
      "why": "Exact format + security note + example = a clear implementation path"
    }
  ]
}
```

---

## Verification

- [ ] Every axis scored 0–5 with anchors; `overall_score` is the mean.
- [ ] Each required element checked for presence and quality.
- [ ] 3–5 fixes, each with exact location, problem, replacement text, and why.
- [ ] No invented error codes, rate limits, endpoints, auth formats, or behavior.
- [ ] Unverified code flagged for testing, not asserted as runnable.
- [ ] Verdict matches the thresholds; output is strict, parseable JSON.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Fixes the job as judging self-service implementability, not rewriting the doc.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five orthogonal axes (completeness, code quality, errors, structure, production).
- **DS-02 (Metric/Criteria Specification):** 0–5 anchors and verdict thresholds make scoring repeatable.
- **ST-02 (Structured Output Format):** Strict JSON schema for downstream tooling.
- **CM-02 (Explicit Constraints):** Must/Must-Not bars fabricated API facts and whole-doc rewrites.

---

## Related Prompts
- `domain-productivity/validation/validation_final_gate.md` — broader pre-ship gate before docs go live.
- `domain-productivity/validation/quality_slop_support_response.md` — sibling evaluator for support replies.
- `domain-productivity/validation/quality_slop_seo_content_brief.md` — sibling evaluator for SEO briefs.
