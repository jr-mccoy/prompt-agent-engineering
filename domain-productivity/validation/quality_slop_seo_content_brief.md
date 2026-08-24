---
title: "SEO Content Brief Slop Evaluator"
category: "productivity/validation"
description: "Score an SEO content brief against five quality axes and return strict JSON with surgical, exactly-located fixes that move a vague brief toward writer-executable content."
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
  - seo
  - content-brief
  - quality-evaluation
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/validation_final_gate.md
  - domain-productivity/validation/quality_slop_technical_documentation.md
  - domain-productivity/validation/quality_slop_video_script.md
---

# SEO Content Brief Slop Evaluator

**Objective:** Judge whether an SEO content brief gives a writer enough to produce differentiated, valuable content — or whether it is so vague the writer will produce generic SEO slop — and return a strict-JSON verdict with surgical fixes.

**When to use:**
- Before handing a brief to a writer or content agency.
- When auditing a backlog of briefs for the ones likely to produce content that ranks.
- When you suspect a brief is just a keyword list dressed up as instructions.

**When NOT to use:**
- To evaluate the finished article itself (this judges the brief, not the draft).
- For non-SEO editorial briefs where ranking and competitive gap analysis don't apply.

**Audience:** Content leads, SEO managers, editors, and anyone commissioning ranked content.

---

## Inputs / Context

1. **The brief** — the full SEO content brief text to be evaluated.
2. **Target keyword(s)** — if stated in the brief; otherwise note as missing.
3. **Optional: target audience / publication** — context for judging intent fit.

---

## Constraints

### Must
- Score every axis 0–5 using the anchors below; compute `overall_score` as the mean.
- Check each required element for presence and quality.
- Give 3–5 surgical fixes, each with an exact location, the exact problem, exact replacement text, and why it matters.
- Return strict, parseable JSON exactly matching the Output Format schema.
- Flag (do not fill in) any missing competitive analysis, intent, or proof requirements.

### Must Not
- Rewrite the whole brief; point to exact spots and give exact replacement text only.
- Invent statistics, ranking data, or competitor facts about the brief being judged — any numbers in example fixes are illustrative and must be labeled as placeholders the writer must verify.
- Fabricate a SERP analysis the brief doesn't contain; if competitive analysis is absent, mark it a critical gap.
- Pad to five fixes — give only the fixes that genuinely move REVISE → ACCEPT.

---

## Instructions

1. **Load the brief** as the artifact under review.
2. **Run the evaluator prompt below verbatim**, pasting the brief where indicated.
3. **Score, gap-check, and prioritize fixes**, then emit strict JSON.

```
You are evaluating an SEO content brief (instructions for writers to create
optimized content). Your job: determine if a writer can create effective,
differentiated content from this — or if the brief is so vague they'll produce
generic SEO slop.

Score each axis 0–5:

1. SEARCH INTENT CLARITY — does it explain what the searcher actually wants to
   accomplish and why they searched?
   5 = Specific intent with a concrete user scenario.
   3 = Intent mentioned but generic; no clear picture of user needs.
   0 = Just lists keywords, no insight into searcher intent.

2. COMPETITIVE GAP ANALYSIS — does it identify what currently-ranking content
   is missing?
   5 = Analyzes top-ranking pages and names 3+ specific gaps to exploit.
   3 = Mentions competitors but the analysis is superficial.
   0 = No competitive analysis; brief exists in a vacuum.

3. CONTENT STRUCTURE REQUIREMENTS — are structural requirements specific enough
   to guide writing?
   5 = Specifies required sections, what each covers, length per section, format.
   3 = Some structure guidance; leaves major decisions to the writer.
   0 = Vague "write comprehensive content about X" with no structure.

4. PROOF AND EXAMPLE REQUIREMENTS — does it specify the evidence and examples
   required?
   5 = Lists specific proof types (screenshots, data, examples, case studies)
       and how many.
   3 = Mentions examples but not type or quantity.
   0 = No proof guidance; writer might ship pure assertion.

5. DIFFERENTIATION STRATEGY — how will this stand out from what already ranks?
   5 = Clear differentiation angle the writer can execute.
   3 = Some differentiation idea, not fully developed.
   0 = No differentiation; will clone top-ranking content.

REQUIRED ELEMENTS (check present + quality):
- search_intent — what the searcher wants and why they searched
- content_angle — how this differs from ranking content
- structure_requirements — sections, format, approximate length
- proof_requirements — types and quantity of examples/evidence

ANTI-PATTERNS to flag:
- Keyword list with no searcher intent
- No analysis of what currently ranks
- "Write comprehensive guide" with no sections specified
- No proof requirements (writer ships generic claims)
- No differentiation (clone of top-ranking content)
- Word-count target with no content requirements (invites filler)
- Target keywords listed but no guidance on natural use

RULES:
- Be surgical. Give 3–5 fixes with EXACT location, problem, exact replacement
  text, and why. Do not rewrite the whole brief.
- Do NOT invent SERP data, competitor facts, or statistics about this brief.
  Any numbers in your replacement text are illustrative placeholders the
  writer must verify; label them as such.
- If competitive analysis, intent, or proof requirements are missing, flag the
  gap — never fabricate the missing content.
- Prioritize fixes by impact on producing differentiated, valuable content.
- Return STRICT JSON only, matching the provided schema.

[PASTE BRIEF HERE]
```

4. **Apply the verdict thresholds** (below) to set `verdict`.
5. **Deliver** the strict JSON.

**Verdict thresholds:**
- **ACCEPT:** ≥4.2 overall, all required elements present, <2 critical gaps.
- **REVISE:** 3.0–4.1 overall, OR missing 1 required element, OR no competitive analysis.
- **REJECT:** <3.0 overall, OR missing 2+ required elements, OR no differentiation strategy (will produce generic SEO slop).

---

## False-Positive Prevention

❌ **DON'T:**
- Invent a SERP/competitor analysis the brief doesn't contain.
- Cite a specific ranking position, traffic number, or savings figure as fact about this brief.
- Pass a brief just because it's long — word count is not quality.
- Rewrite the brief end-to-end instead of giving located fixes.

✅ **DO:**
- Treat any number in example replacement text as an illustrative placeholder labeled "verify."
- Flag missing intent, competitive analysis, or proof requirements as critical gaps.
- Point to exact locations with exact replacement text.
- Give only the fixes that genuinely change the verdict.

---

## Output Format

Return strict JSON only:

```json
{
  "overall_score": 3.4,
  "axis_scores": {
    "search_intent_clarity": 3,
    "competitive_gap_analysis": 3,
    "content_structure_requirements": 4,
    "proof_and_example_requirements": 3,
    "differentiation_strategy": 3
  },
  "verdict": "REVISE",
  "required_elements": {
    "search_intent": {"present": true, "quality": "mentions intent but not the user's situation"},
    "content_angle": {"present": true, "quality": "angle mentioned, not fully developed"},
    "structure_requirements": {"present": true, "quality": "clear section breakdown"},
    "proof_requirements": {"present": false, "quality": "no guidance on examples or evidence"}
  },
  "critical_gaps": [
    "No analysis of currently-ranking content or gaps to exploit",
    "Missing proof requirements — writer might ship generic claims"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Missing from brief",
      "problem": "No competitive gap analysis — writer can't differentiate",
      "fix": "Add a 'Competitive Analysis' section naming the top results and 3+ specific gaps to exploit (e.g. 'top results explain WHAT but not HOW — no console screenshots'). [Verify the ranking set before writing.]",
      "why": "Specific gaps prevent the writer from cloning existing content"
    },
    {
      "priority": 2,
      "location": "Search Intent section: 'User wants to reduce AWS costs'",
      "problem": "Too generic — doesn't capture the user's situation",
      "fix": "Replace with a concrete scenario: who they are, what triggered the search, their skill level, and the time/effort they'll spend. [Numbers illustrative; confirm against real audience data.]",
      "why": "A specific situation guides tone, complexity, and focus"
    },
    {
      "priority": 3,
      "location": "Missing from brief",
      "problem": "No proof requirements",
      "fix": "Add 'Required Proof Elements': N real examples with before/after numbers, screenshots per tip, and a doc link per recommendation. [Counts illustrative; set to your standard.]",
      "why": "Specific proof requirements force credible, actionable content"
    }
  ]
}
```

---

## Verification

- [ ] Every axis scored 0–5 with anchors; `overall_score` is the mean.
- [ ] Each required element checked for presence and quality.
- [ ] 3–5 fixes, each with exact location, problem, replacement text, and why.
- [ ] No fabricated SERP data, competitor facts, or statistics about this brief.
- [ ] Missing elements flagged as gaps, not invented.
- [ ] Verdict matches the thresholds; output is strict, parseable JSON.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Fixes the job as judging brief-to-content readiness, not rewriting the brief.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five orthogonal axes (intent, gaps, structure, proof, differentiation).
- **DS-02 (Metric/Criteria Specification):** 0–5 anchors and verdict thresholds make scoring repeatable.
- **ST-02 (Structured Output Format):** Strict JSON schema for downstream tooling.
- **CM-02 (Explicit Constraints):** Must/Must-Not bars fabrication and whole-brief rewrites.

---

## Related Prompts
- `domain-productivity/validation/validation_final_gate.md` — broader pre-ship gate once the brief produces a draft.
- `domain-productivity/validation/quality_slop_technical_documentation.md` — sibling evaluator for developer docs.
- `domain-productivity/validation/quality_slop_video_script.md` — sibling evaluator for video scripts.
