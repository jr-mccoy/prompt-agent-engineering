---
title: "Internal Communication Slop Detector"
category: professional-writing/content-quality
description: "Score an internal announcement, memo, or update against five quality axes and return surgical fixes so employees know what changed, who's affected, and what to do — without a wave of follow-up questions."
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
  - internal-communication
  - change-management
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-professional-writing/content-quality/quality_slop_meeting_summary.md
  - domain-productivity/validation/validation_final_gate.md
  - domain-productivity/validation/validation_reality_check.md
---

# Internal Communication Slop Detector

**Objective:** Judge whether an internal communication (Slack announcement, email update, memo) will be understood on one read — or whether it will generate confusion and a flood of clarifying questions — and return exact, location-anchored fixes.

**When to use:**
- Before posting a policy change, process change, or org update.
- When prior announcements triggered many "does this apply to me?" threads.
- To QA AI-drafted internal comms for buried-lede slop.

**When NOT to use:**
- External customer/marketing messaging — use the landing-page or product-description detectors.
- A meeting recap — use the meeting-summary detector.

**Audience:** People managers, ops/HR leads, comms owners, and anyone reviewing internal announcements before broadcast.

---

## Inputs / Context

1. **The draft** — the full internal communication being evaluated.
2. **Audience** — who receives it (teams, regions, roles).
3. **Goal** — what the reader should understand and do after reading.

---

## Constraints

### Must
- Score all five axes 0–5 using the anchors provided.
- Anchor every fix to an exact location in the draft and give exact replacement text.
- Verify each required element is present and assess its quality.
- Return strict JSON only, matching the Output Format.

### Must Not
- Invent dates, deadlines, headcounts, or policy details about the draft being judged; any specifics in *example* fix text are illustrative placeholders the author must replace.
- Fabricate scope or rationale the draft does not state — flag missing scope/deadlines/rationale, never supply imaginary ones.
- Rewrite the whole communication; restrict yourself to 3–5 high-impact surgical fixes.

---

## Instructions

1. Collect the draft, the intended audience, and the goal.
2. Run the evaluator below verbatim against the draft.
3. Return strict JSON only (no prose outside the JSON).

```
# Internal Communication Quality Evaluator

You are evaluating internal company communication (Slack announcement, email update, memo).
Your job: determine if employees will understand what changed and what they need to do—or if
this creates confusion and follow-up questions.

## Why This Matters
Bad internal comms create noise, confusion, and dozens of clarifying questions that waste hours.
Good internal comms get read once, understood immediately, and require no follow-up. The
difference: clarity on what changed, who's affected, and what to do.

## Evaluation Dimensions (score each 0-5)

### 1. Change Clarity — immediately obvious what changed?
Score 5: First sentence states the change clearly.
  ("Starting Oct 15, all PTO requests require 2 weeks notice instead of 1 week.")
Score 3: Change stated but buried in context or requires reading multiple paragraphs.
Score 0: Change isn't clearly articulated. The reader has to infer what's different.

### 2. Scope Definition — clear who this affects?
Score 5: Explicitly states who is/isn't affected.
  ("This applies to all US employees. Canada and EU teams continue with the existing policy.")
Score 3: Scope somewhat clear but edge cases are ambiguous.
Score 0: Unclear who should care. Everyone reads it unsure if it applies to them.

### 3. Action Requirements — do people know what to do?
Score 5: Specific actions with owners and deadlines.
  ("If you have PTO booked for Q4, resubmit in the new system by Oct 20. Managers: approve/deny by Oct 25.")
Score 3: Actions mentioned but lack specificity about who does what by when.
Score 0: No clear actions, or vague "please update accordingly."

### 4. Reasoning — do people understand why this is happening?
Score 5: Clear 1-2 sentence rationale.
  ("California requires 2-week notice for PTO in audit. This aligns all US offices.")
Score 3: Some reasoning but thin or like an afterthought.
Score 0: No explanation. Just announces the change with no context.

### 5. Question Prevention — anticipates and answers likely questions?
Score 5: Includes an FAQ / "Common questions" section covering the top 3-5 likely questions.
Score 3: Answers some questions but misses obvious ones.
Score 0: Doesn't anticipate questions. Will generate dozens of Slack threads.

## Required Elements (must have)
- Clear change statement: what's different as of when
- Scope definition: who this affects (and who it doesn't)
- Action requirements: what people need to do by when

## Anti-Patterns to Flag (specific to internal comms)
- Buried lede: context before stating the change
- Unclear scope: everyone reads it unsure if it applies to them
- No actions specified: "Please make necessary updates" (which updates?)
- Missing deadlines: actions without a timeline
- No rationale: change with no explanation why
- Doesn't prevent obvious questions
- Too long—key info buried in paragraphs

## Verdict Thresholds
ACCEPT: >=4.2 overall, all required elements present, <2 critical gaps
REVISE: 3.0-4.1 overall, OR missing 1 required element, OR actions lack deadlines
REJECT: <3.0 overall, OR change unclear, OR scope undefined

## Instructions
Be surgical: give 3-5 specific fixes that move REVISE -> ACCEPT.
Do not rewrite the whole thing. Point to exact locations and give exact replacement text.
Prioritize fixes by impact—what matters most for immediate comprehension and minimizing follow-up questions?
Do not invent dates, deadlines, scope, or rationale; flag missing items rather than fabricating them.

Return strict JSON in the format specified below.
```

---

## False-Positive Prevention

❌ **DON'T:**
- Penalize a terse, well-scoped announcement for being short when change, scope, and action are all clear.
- Reward a long FAQ that pads filler while leaving the core change buried.
- Invent a deadline or rationale to "complete" the message.
- Treat a genuinely audience-wide change as needing scope carve-outs that don't exist.

✅ **DO:**
- Reward a clear lede, explicit scope, and dated actions even in a few sentences.
- Treat illustrative dates/headcounts in fix text as placeholders the author must replace.
- Flag missing deadlines, scope edges, or rationale as gaps; never supply fabricated ones.
- Distinguish a real edge case (contractors, other regions) from invented complexity.

---

## Output Format

```json
{
  "overall_score": 3.5,
  "axis_scores": {
    "change_clarity": 4,
    "scope_definition": 3,
    "action_requirements": 3,
    "reasoning": 3,
    "question_prevention": 3
  },
  "verdict": "ACCEPT | REVISE | REJECT",
  "required_elements": {
    "clear_change_statement": {"present": true, "quality": "change stated clearly in the first paragraph"},
    "scope_definition": {"present": true, "quality": "mentions who, but edge cases unclear"},
    "action_requirements": {"present": true, "quality": "actions mentioned but deadlines missing"}
  },
  "critical_gaps": [
    "No deadline specified for the required actions",
    "Edge case unclear—what about existing Q4 requests?"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Action section: 'Please update your PTO requests in the new system'",
      "problem": "No deadline or consequence if not done",
      "fix": "Replace with: 'ACTION REQUIRED by Oct 20: (1) All employees resubmit any Q4 PTO in the new system (link). (2) Managers approve/deny by Oct 25. Requests not resubmitted by Oct 20 are marked unapproved.'",
      "why": "Specific deadline + clear roles + consequence = people know exactly what to do and when"
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
- [ ] No invented dates, scope, or rationale; missing items flagged, not fabricated.
- [ ] Output is strict JSON with no surrounding prose.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Frames the job as judging one-read comprehension and follow-up prevention.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five orthogonal axes (change, scope, action, reasoning, question prevention).
- **DS-02 (Metric/Criteria Specification):** 0–5 anchors and ACCEPT/REVISE/REJECT thresholds define scoring precisely.
- **ST-02 (Structured Output Format):** Strict JSON schema makes results machine-readable.
- **CM-02 (Explicit Constraints):** Must/Must-Not bound the evaluator and forbid fabrication.

---

## Related Prompts
- `domain-professional-writing/content-quality/quality_slop_meeting_summary.md` — sibling detector for meeting recaps.
- `domain-productivity/validation/validation_final_gate.md` — final ship/no-ship gate before broadcast.
- `domain-productivity/validation/validation_reality_check.md` — surface the questions a confused reader would raise.
