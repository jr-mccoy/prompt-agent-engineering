---
title: "Video Script Slop Evaluator"
category: "productivity/validation"
description: "Score a video script against five retention axes and return strict JSON with surgical, exactly-located fixes that move a boring script toward one that holds viewers and drives action."
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
  - video-script
  - retention
  - quality-evaluation
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-productivity/validation/validation_final_gate.md
  - domain-productivity/validation/quality_slop_social_media.md
  - domain-productivity/validation/quality_slop_seo_content_brief.md
---

# Video Script Slop Evaluator

**Objective:** Judge whether a video script (explainer, demo, tutorial, marketing) will keep viewers watching past the first 10 seconds and drive the intended action — or whether they'll click away — and return a strict-JSON verdict with surgical fixes.

**When to use:**
- Before recording/producing a script you've invested production budget in.
- When videos show high early drop-off and you suspect the script.
- When auditing a batch of scripts for hook and CTA quality.

**When NOT to use:**
- For unscripted/improvised formats where there's no script to evaluate.
- For pure entertainment content where retention mechanics differ from explainer/demo logic.

**Audience:** Video producers, marketers, creators, and teams reviewing scripts pre-production.

---

## Inputs / Context

1. **The script** — the full script text (with any visual/scene directions) to be evaluated.
2. **Video type** — explainer, demo, tutorial, marketing (affects axis weighting).
3. **Optional: target action** — subscribe, click, sign up (helps judge CTA strength).

---

## Constraints

### Must
- Score every axis 0–5 using the anchors below; compute `overall_score` as the mean.
- Check each required element for presence and quality.
- Give 3–5 surgical fixes, each with an exact location (timestamp/scene), the exact problem, exact replacement text, and why it matters.
- Return strict, parseable JSON exactly matching the Output Format schema.

### Must Not
- Rewrite the whole script; point to exact spots and give exact replacement text only.
- Invent retention statistics, view counts, or savings/results claims about the script being judged — any numbers in example fixes are illustrative placeholders the creator must verify.
- Fabricate specifics (companies, dollar figures, metrics) to "improve" the script; prompt the creator for real ones and flag the gap.
- Pad to five fixes — give only the fixes that genuinely move REVISE → ACCEPT.

---

## Instructions

1. **Load the script** as the artifact under review.
2. **Run the evaluator prompt below verbatim**, pasting the script where indicated.
3. **Score, gap-check, and prioritize fixes**, then emit strict JSON.

```
You are evaluating a video script (explainer, demo, tutorial, marketing). Your
job: determine if this will keep viewers watching past 10 seconds — or if
they'll click away because it's boring or unclear.

Score each axis 0–5:

1. HOOK STRENGTH — do the first 10 seconds earn the next 50?
   5 = Surprising visual, counterintuitive statement, or immediate pain point.
   3 = Relevant but predictable; no urgency to keep watching.
   0 = Slow build, generic intro ("Hi, I'm... from..."), logo animation.

2. PACING AND MOMENTUM — does each scene advance understanding without drag?
   5 = No wasted words; every line reveals new info; visuals change every 3–5s.
   3 = Generally well-paced with slow or repetitive sections.
   0 = Repetitive, slow, filler-heavy; could be 30% shorter.

3. SHOW VS. TELL — does it demonstrate visually rather than just narrate?
   5 = Screen recordings/animations that show exactly what's discussed.
   3 = Some visuals but relies heavily on narration.
   0 = Mostly narration with generic stock footage or static slides.

4. CLARITY OF PROGRESSION — is it obvious what you're learning and why?
   5 = Clear, visually-signaled structure; each section connects to the last.
   3 = Some structure but abrupt transitions or unclear logic.
   0 = Jumps between topics; viewer gets lost.

5. CALL-TO-ACTION STRENGTH — is the next step clear and compelling?
   5 = Specific action, clear benefit, low friction.
   3 = CTA exists but generic or with friction.
   0 = No CTA, or vague "visit our website".

REQUIRED ELEMENTS (check present + quality):
- strong_hook — first 10 seconds justify watching the next 50
- visual_demonstration — screen recordings or animations that show key points
- clear_cta — a specific next step at the end

ANTI-PATTERNS to flag:
- Opening with a logo animation or "Hi, I'm..." instead of immediate value
- Too much narration, not enough showing
- No pace variation (monotone)
- Key points buried 2 minutes in (should be in first 30 seconds)
- Repetitive (says the same thing 3 ways)
- No visual cues for sections (viewer gets lost)
- Weak or missing CTA

RULES:
- Be surgical. Give 3–5 fixes with EXACT location (timestamp/scene), problem,
  exact replacement text, and why. Do not rewrite the whole script.
- Do NOT invent retention stats, view counts, or results claims about this
  script. Any numbers in your replacement text are illustrative placeholders the
  creator must verify; label them as such.
- Do NOT fabricate companies, dollar figures, or metrics to "improve" the
  script; prompt the creator for real specifics and flag the gap.
- Prioritize fixes by impact on retention and driving the intended action.
- Return STRICT JSON only, matching the provided schema.

[PASTE SCRIPT HERE]
```

4. **Apply the verdict thresholds** (below) to set `verdict`.
5. **Deliver** the strict JSON.

**Verdict thresholds:**
- **ACCEPT:** ≥4.2 overall, all required elements present, <2 critical gaps.
- **REVISE:** 3.0–4.1 overall, OR missing 1 required element, OR weak hook risks retention.
- **REJECT:** <3.0 overall, OR no visual demonstration, OR opens with logo animation.

---

## False-Positive Prevention

❌ **DON'T:**
- Invent retention numbers, view counts, or results to make the script look stronger.
- Claim a hook "will retain X%" — retention isn't predictable from text alone.
- Pass a script because the production value sounds high; specificity and pacing are what hold viewers.
- Rewrite the whole script instead of giving located fixes.

✅ **DO:**
- Treat any number in example replacement text as an illustrative placeholder labeled "verify."
- Ask the creator to supply real specifics rather than fabricating them.
- Point to exact timestamps/scenes with exact replacement text.
- Give only the fixes that genuinely change the verdict.

---

## Output Format

Return strict JSON only:

```json
{
  "overall_score": 3.6,
  "axis_scores": {
    "hook_strength": 3,
    "pacing_and_momentum": 4,
    "show_vs_tell": 3,
    "clarity_of_progression": 4,
    "call_to_action_strength": 3
  },
  "verdict": "REVISE",
  "required_elements": {
    "strong_hook": {"present": true, "quality": "opens with a problem but could be sharper"},
    "visual_demonstration": {"present": true, "quality": "some screen recordings, relies heavily on narration"},
    "clear_cta": {"present": true, "quality": "CTA present but generic"}
  },
  "critical_gaps": [
    "First 10 seconds have a slow build — risky for retention",
    "Section 2 is narration over static slides — should show the product"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Opening (0:00–0:10)",
      "problem": "Starts with a logo animation and company intro — slow hook",
      "fix": "Open on a concrete visual + counterintuitive outcome + promise of payoff drawn from a real result. [VISUAL + numbers illustrative; use the creator's real data.]",
      "why": "Immediate visual proof + counterintuitive outcome = retention"
    },
    {
      "priority": 2,
      "location": "'Why this matters' section (~0:45–1:20)",
      "problem": "Narration over generic slides — shows nothing",
      "fix": "Replace slides with a screen recording showing real before/after data with annotations. [Use the creator's actual metrics.]",
      "why": "Showing real data is more convincing than describing it"
    },
    {
      "priority": 3,
      "location": "End CTA (~3:40–3:50)",
      "problem": "Generic 'visit our website for more'",
      "fix": "Replace with a specific deliverable + clear benefit + removed friction (e.g. a free resource, no signup). [Confirm the real offer.]",
      "why": "Specific deliverable + benefit + low friction = higher conversion"
    }
  ]
}
```

---

## Verification

- [ ] Every axis scored 0–5 with anchors; `overall_score` is the mean.
- [ ] Each required element checked for presence and quality.
- [ ] 3–5 fixes, each with exact location (timestamp/scene), problem, replacement text, and why.
- [ ] No fabricated retention stats, view counts, or results about this script.
- [ ] Missing specifics flagged for the creator, not invented.
- [ ] Verdict matches the thresholds; output is strict, parseable JSON.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Fixes the job as judging retention and action, not rewriting the script.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five orthogonal axes (hook, pacing, show-vs-tell, progression, CTA).
- **DS-02 (Metric/Criteria Specification):** 0–5 anchors and verdict thresholds make scoring repeatable.
- **ST-02 (Structured Output Format):** Strict JSON schema for downstream tooling.
- **CM-02 (Explicit Constraints):** Must/Must-Not bars fabrication and whole-script rewrites.

---

## Related Prompts
- `domain-productivity/validation/validation_final_gate.md` — broader pre-ship gate before production.
- `domain-productivity/validation/quality_slop_social_media.md` — sibling evaluator for social posts.
- `domain-productivity/validation/quality_slop_seo_content_brief.md` — sibling evaluator for SEO briefs.
