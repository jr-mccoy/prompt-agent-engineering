---
title: "Social Media Post Slop Evaluator"
category: professional-writing/content-quality
description: "Score a social media post against five engagement axes and return strict JSON with surgical, exactly-located fixes that move generic content toward scroll-stopping, response-earning posts."
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
  - social-media
  - engagement
  - quality-evaluation
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/validation_final_gate.md
  - domain-professional-writing/content-quality/quality_slop_seo_content_brief.md
  - domain-professional-writing/content-quality/quality_slop_video_script.md
---

# Social Media Post Slop Evaluator

**Objective:** Judge whether a social media post (LinkedIn, Twitter/X, etc.) will stop the scroll and earn engagement — or whether it's generic content people will skip — and return a strict-JSON verdict with surgical fixes.

**When to use:**
- Before publishing a post you've invested real thought or distribution in.
- When auditing a content calendar for posts likely to flop.
- When a draft "feels off" but you can't name why.

**When NOT to use:**
- For long-form articles or threads where structure matters more than a single-post hook (use the SEO brief evaluator or a dedicated long-form check).
- For paid-ad copy where conversion mechanics dominate over organic engagement.

**Audience:** Founders, marketers, creators, and anyone posting to earn reach and replies.

---

## Inputs / Context

1. **The post** — the full draft text to be evaluated.
2. **Platform** — LinkedIn, Twitter/X, etc. (affects format expectations).
3. **Optional: goal** — awareness, replies, clicks (helps weight engagement design).

---

## Constraints

### Must
- Score every axis 0–5 using the anchors below; compute `overall_score` as the mean.
- Check each required element for presence and quality.
- Give 3–5 surgical fixes, each with an exact location, the exact problem, exact replacement text, and why it matters.
- Return strict, parseable JSON exactly matching the Output Format schema.

### Must Not
- Rewrite the whole post; point to exact spots and give exact replacement text only.
- Invent engagement statistics, follower counts, or performance claims about the post being judged — any numbers in example fixes are illustrative and must be labeled as placeholders the author must verify.
- Fabricate specifics (companies, dollar figures, events) to "improve" the post; suggest the author supply real ones and flag the gap.
- Pad to five fixes — give only the fixes that genuinely move REVISE → ACCEPT.

---

## Instructions

1. **Load the post** as the artifact under review.
2. **Run the evaluator prompt below verbatim**, pasting the post where indicated.
3. **Score, gap-check, and prioritize fixes**, then emit strict JSON.

```
You are evaluating a social media post (LinkedIn, Twitter/X, etc.). Your job:
determine if this will earn engagement and stop the scroll — or if it's generic
content people will skip.

Score each axis 0–5:

1. HOOK STRENGTH — does the first sentence earn the read?
   5 = Specific, surprising, or contrarian opener that creates curiosity.
   3 = Relevant but predictable; no strong pull.
   0 = Generic opener ("Excited to share...", "I've been thinking...").

2. SPECIFICITY — concrete examples, numbers, or observations?
   5 = At least one specific data point, named example, or concrete scenario.
   3 = Some specificity mixed with generic statements.
   0 = Entirely abstract, no concrete illustration.

3. INSIGHT NOVELTY — fresh take, or generic wisdom everyone's heard?
   5 = Counterintuitive or uncommon angle that shifts the reader's thinking.
   3 = Valid but predictable.
   0 = Platitudes ("consistency is key", "communication matters").

4. ENGAGEMENT DESIGN — does it invite response or discussion?
   5 = Ends with a specific question, a take that begs response, or a gap
       readers want to fill.
   3 = Somewhat engaging; weak pull to respond.
   0 = No invitation to engage; reads like a broadcast.

5. FORMAT OPTIMIZATION — scannable and visually digestible?
   5 = Short paragraphs, line breaks, key phrases stand out; easy to scan.
   3 = Readable but needs more white space.
   0 = Wall of text; hard to scan on mobile.

REQUIRED ELEMENTS (check present + quality):
- strong_opening — first sentence earns the read (not "Excited to share")
- concrete_detail — at least one specific example, number, or observation
- engagement_hook — question, contrarian take, or invitation to respond

ANTI-PATTERNS to flag:
- "Excited to share", "I've been thinking", "Hot take:" openers
- Vague wisdom with no concrete example
- Wall of text, no line breaks
- No engagement invitation (just broadcasting)
- Humble-brag disguised as a lesson
- Lists with no context ("5 things every founder should know")

RULES:
- Be surgical. Give 3–5 fixes with EXACT location, problem, exact replacement
  text, and why. Do not rewrite the whole post.
- Do NOT invent engagement stats, follower counts, or performance claims about
  this post. Any numbers in your replacement text are illustrative placeholders
  the author must verify; label them as such.
- Do NOT fabricate companies, dollar figures, or events to "improve" the post;
  prompt the author for real specifics and flag the gap.
- Prioritize fixes by impact on stopping the scroll and earning engagement.
- Return STRICT JSON only, matching the provided schema.

[PASTE POST HERE]
```

4. **Apply the verdict thresholds** (below) to set `verdict`.
5. **Deliver** the strict JSON.

**Verdict thresholds:**
- **ACCEPT:** ≥4.2 overall, all required elements present, <2 critical gaps.
- **REVISE:** 3.0–4.1 overall, OR missing 1 required element, OR 3+ gaps.
- **REJECT:** <3.0 overall, OR missing 2+ required elements, OR opens with "Excited to share".

---

## False-Positive Prevention

❌ **DON'T:**
- Invent metrics, named examples, or events to make the post look stronger.
- Claim a hook "will get X engagement" — engagement is not predictable from text alone.
- Pass a post just because it's polished; polish without specificity is still slop.
- Rewrite the whole post instead of giving located fixes.

✅ **DO:**
- Treat any number in example replacement text as an illustrative placeholder labeled "verify."
- Ask the author to supply real specifics rather than fabricating them.
- Point to exact locations with exact replacement text.
- Give only the fixes that genuinely change the verdict.

---

## Output Format

Return strict JSON only:

```json
{
  "overall_score": 3.6,
  "axis_scores": {
    "hook_strength": 4,
    "specificity": 3,
    "insight_novelty": 3,
    "engagement_design": 4,
    "format_optimization": 4
  },
  "verdict": "REVISE",
  "required_elements": {
    "strong_opening": {"present": true, "quality": "good hook, could be sharper"},
    "concrete_detail": {"present": true, "quality": "one example, needs more specificity"},
    "engagement_hook": {"present": true, "quality": "question works well"}
  },
  "critical_gaps": [
    "Main insight is generic — many people have said similar things",
    "Missing concrete specifics to make the point land"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Opening sentence",
      "problem": "Starts with 'I've been thinking about leadership' — weak hook",
      "fix": "Replace with a specific, tension-creating opener drawn from a real moment the author experienced. [Author supplies the real detail.]",
      "why": "Creates immediate curiosity — reader must continue to resolve the tension"
    },
    {
      "priority": 2,
      "location": "Third paragraph, generic claim about 'better communication'",
      "problem": "Vague insight everyone has heard",
      "fix": "Replace with a concrete, self-aware example with real numbers from the author's experience. [Numbers illustrative; use the author's actual figures.]",
      "why": "Concrete specifics + self-awareness = memorable"
    },
    {
      "priority": 3,
      "location": "End of post",
      "problem": "No engagement invitation",
      "fix": "Add a specific question inviting readers to share a parallel experience.",
      "why": "A targeted question drives comments rather than a broadcast"
    }
  ]
}
```

---

## Verification

- [ ] Every axis scored 0–5 with anchors; `overall_score` is the mean.
- [ ] Each required element checked for presence and quality.
- [ ] 3–5 fixes, each with exact location, problem, replacement text, and why.
- [ ] No fabricated metrics, examples, or events about this post.
- [ ] Missing specifics flagged for the author, not invented.
- [ ] Verdict matches the thresholds; output is strict, parseable JSON.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Fixes the job as judging scroll-stopping potential, not rewriting the post.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five orthogonal axes (hook, specificity, novelty, engagement, format).
- **DS-02 (Metric/Criteria Specification):** 0–5 anchors and verdict thresholds make scoring repeatable.
- **ST-02 (Structured Output Format):** Strict JSON schema for downstream tooling.
- **CM-02 (Explicit Constraints):** Must/Must-Not bars fabrication and whole-post rewrites.

---

## Related Prompts
- `domain-productivity/validation/validation_final_gate.md` — broader pre-ship gate for higher-stakes posts.
- `domain-professional-writing/content-quality/quality_slop_seo_content_brief.md` — sibling evaluator for SEO briefs.
- `domain-professional-writing/content-quality/quality_slop_video_script.md` — sibling evaluator for video scripts.
