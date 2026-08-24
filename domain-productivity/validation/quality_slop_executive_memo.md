---
title: "Executive Memo Slop Detector — Decide in 10 Minutes or Schedule a Meeting?"
category: "productivity/validation"
description: "Score an executive memo on five decision-enablement dimensions (BLUF, decision quality, data, risk, scannability) and return strict JSON with an ACCEPT/REVISE/REJECT verdict and surgical fixes."
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
  - executive-memo
  - decision-enablement
  - validation
  - leadership-communication
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/quality_slop_client_deliverable.md
  - domain-productivity/validation/validation_final_gate.md
  - domain-productivity/validation/validation_reality_check.md
---

# Executive Memo Slop Detector — Decide in 10 Minutes or Schedule a Meeting?

**Objective:** Determine whether an executive can make an informed decision from a memo in under 10 minutes — or whether it requires multiple clarifying meetings — scoring five dimensions and returning a strict-JSON verdict with exact fixes.

**When to use:**
- Before sending a strategy doc, decision proposal, or leadership status update.
- To screen AI-drafted memos for buried ledes and one-sided advocacy.
- When decisions stall because memos prompt follow-up meetings.
- As a gate before circulating to a board or exec team.

**When NOT to use:**
- For detailed operational/technical specs not aimed at a decision.
- For marketing or client-facing content (use those evaluators).

**Audience:** Founders, executives, chiefs of staff, and managers writing up or up.

---

## Inputs / Context

Provide:
1. **The memo** — full text, including any executive summary, recommendation, and analysis.
2. **The decision** (optional) — what the exec must decide and by when.
3. **Available data** — note figures, sources, or alternatives that exist but aren't yet in the memo, so the evaluator flags (not invents) missing support.

---

## Constraints

### Must
- Score every dimension on the 0–5 anchored scale and compute `overall_score`.
- Quote the exact location of each flagged problem.
- Give 3–5 prioritized fixes with exact replacement text.
- Apply the verdict thresholds exactly.

### Must Not
- Invent figures, sources, deal terms, or alternatives — flag missing data as a gap, never fabricate it.
- Rewrite the whole memo; stay surgical.
- Treat illustrative example numbers in this prompt as facts about the user's memo.
- Mark ACCEPT on score alone if a required element is missing.

---

## Instructions

1. Collect the memo and any decision/data context.
2. Paste the evaluator block below verbatim, appending the memo.
3. Have the model score each axis, check required elements, list gaps, and produce 3–5 surgical fixes.
4. Return strict JSON (skeleton in Output Format).

```
You are evaluating an executive memo (strategy doc, decision proposal, leadership status
update). Your job: determine if an exec can make an informed decision in <10 minutes — or
if this requires multiple clarifying meetings.

WHY THIS MATTERS: Weak memos waste exec time, delay decisions by weeks, and cause wrong
decisions due to missing context. Strong memos enable fast, informed decisions without meetings.

Score each dimension 0-5:

1. BOTTOM LINE UP FRONT (BLUF) — Recommendation/ask/status clear in paragraph 1?
   5: First paragraph states exactly the ask/report ("Recommending we acquire Acme for
      $50M; doubles our enterprise customer count"). 3: Buries it after context.
   0: Recommendation unclear until the final page, or absent.

2. DECISION QUALITY — Provides a framework for deciding?
   5: States options considered, pros/cons, why the recommended one is best, and the
      cost of not deciding. 3: Some options, shallow analysis.
   0: Advocates one option without considering alternatives.

3. DATA SPECIFICITY — Claims backed by concrete numbers and sources?
   5: Key metrics with sources ("145 enterprise customers per their S-1; ~$75K ACV from
      10 reference calls"). 3: Some data, missing sources/precision.
   0: Vague ("significant growth opportunity") with no numbers.

4. RISK IDENTIFICATION — Downsides and risks explicitly addressed?
   5: Dedicated risks section with likelihood, impact, and mitigation; no hidden bad news.
   3: Some risks, incomplete or glossed. 0: No risk discussion; upsides only.

5. SCANNABILITY FOR A BUSY EXEC — Key points in 3 minutes of scanning?
   5: Exec summary, clear headers, key points bolded, numbers stand out.
   3: Readable but requires focus. 0: Dense paragraphs; must read every word.

REQUIRED ELEMENTS (must be present):
- Clear recommendation (the ask, in the first paragraph)
- Options analysis (alternatives considered and why not chosen)
- Key data (numbers supporting the recommendation)
- Risks (downsides and how to mitigate)

ANTI-PATTERNS TO FLAG:
- Buried lede (recommendation on page 3 instead of paragraph 1)
- No alternatives discussed (appears the exec has only one option)
- Vague data ("significant revenue opportunity")
- Cherry-picking (only data supporting the recommended option)
- No risk discussion; missing financial implications
- No timeline (when the decision is needed and why); too long for the decision

RULES:
- Do NOT invent figures, sources, deal terms, or alternatives. Flag missing data as a
  gap; never fabricate it.
- Be surgical: 3-5 fixes that move REVISE -> ACCEPT. Quote exact locations and give
  exact replacement text. Do not rewrite the whole memo.
- Prioritize fixes by impact on enabling a fast, informed decision.

VERDICT THRESHOLDS:
- ACCEPT: >=4.2 overall, all required elements present, <2 critical gaps
- REVISE: 3.0-4.1 overall, OR missing 1 required element, OR recommendation not in paragraph 1
- REJECT: <3.0 overall, OR no clear recommendation, OR no alternatives analyzed

Return strict JSON only, matching the provided schema.

MEMO TO EVALUATE:
<paste full memo, plus the decision and available-data context, here>
```

---

## False-Positive Prevention

❌ **DON'T:**
- Score `data_specificity` high because numbers appear — check they carry sources.
- Invent a deal term, ACV, or competitor figure to complete a fix.
- Accept "we considered other options" as options analysis without actual alternatives + trade-offs.
- Penalize a deliberately short status memo for lacking a full options matrix the situation doesn't warrant.

✅ **DO:**
- Flag every unsourced figure and ask the user to supply the source.
- Phrase example numbers in fixes as clearly illustrative (e.g., "e.g., 'Acquire Acme for $50M; decision needed by Oct 15' — use real terms and dates").
- Check all four required elements independently of the score.
- Quote the exact sentence (or note the missing section) being criticized.

---

## Output Format

```json
{
  "overall_score": 3.5,
  "axis_scores": {
    "bottom_line_up_front": 3,
    "decision_quality": 3,
    "data_specificity": 4,
    "risk_identification": 3,
    "scannability": 4
  },
  "verdict": "REVISE",
  "required_elements": {
    "clear_recommendation": {"present": true, "quality": "stated but buried in the second paragraph"},
    "options_analysis": {"present": true, "quality": "alternatives mentioned but analysis is thin"},
    "key_data": {"present": true, "quality": "good data with sources"},
    "risks": {"present": true, "quality": "risks mentioned but no mitigation plans"}
  },
  "critical_gaps": [
    "Recommendation isn't in the first paragraph — the exec has to hunt for the ask",
    "No mitigation plans for identified risks"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Opening paragraph: starts with context about market trends",
      "problem": "Buries the lede — the exec doesn't know what's being asked",
      "fix": "Lead with the ask + timing + key trade-off, e.g.: 'Recommendation: Acquire Acme for $50M to double our enterprise base. Decision needed by Oct 15 to match their raise. Trade-off: high price but the fastest path to 300 enterprise customers vs 2-3 years organic.' Use real terms/dates.",
      "why": "Recommendation + timing + trade-off in paragraph 1 = the exec immediately knows the stakes"
    },
    {
      "priority": 2,
      "location": "Alternatives section: briefly mentions 'build vs buy'",
      "problem": "Doesn't actually analyze the alternative with numbers",
      "fix": "Expand each alternative with timeline, cost, and key risk (e.g., build: 18-24 months, $8M eng, still needs customer acquisition). Use your real estimates.",
      "why": "Specific timelines + costs + trade-offs let the exec evaluate alternatives"
    },
    {
      "priority": 3,
      "location": "Risks section: lists 'integration risk' and 'retention risk'",
      "problem": "Identifies risks but provides no mitigation plan",
      "fix": "Add a concrete mitigation per risk (e.g., retain the acquired team 12 months via offer terms; pre-close account reviews of the top customers by ARR).",
      "why": "Risk + mitigation lets the exec judge whether risks are manageable"
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
- [ ] No fabricated figures, sources, or deal terms; missing data flagged as a gap.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Frames the job as decide-in-10-minutes enablement.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five decision-enablement axes with explicit anchors.
- **DS-02 (Metric/Criteria Specification):** Numeric thresholds and four required elements specified.
- **ST-02 (Structured Output Format):** Forces strict JSON.
- **CM-02 (Explicit Constraints):** Bars fabricated figures/terms and whole-memo rewrites.

---

## Related Prompts
- `domain-productivity/validation/quality_slop_client_deliverable.md` — sibling evaluator for actionable, evidence-backed client work.
- `domain-productivity/validation/validation_final_gate.md` — final ship/no-ship gate before circulation.
- `domain-productivity/validation/validation_reality_check.md` — surface the objections execs would raise about the recommendation.
