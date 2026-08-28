---
title: "Meeting Summary Slop Detector"
category: professional-writing/content-quality
description: "Score a meeting summary against five quality axes and return surgical fixes so someone who missed the meeting can catch up in 60 seconds and know exactly what to do — instead of reading a transcript dump."
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
  - meeting-summary
  - action-items
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-professional-writing/content-quality/quality_slop_internal_communication.md
  - domain-productivity/validation/validation_final_gate.md
  - domain-productivity/validation/validation_reality_check.md
---

# Meeting Summary Slop Detector

**Objective:** Judge whether a meeting summary lets an absentee catch up fast and act — or whether it's a vague transcript dump with no clear decisions, owners, or deadlines — and return exact, location-anchored fixes.

**When to use:**
- Before circulating a recap of a decision-making or planning meeting.
- When prior summaries led to dropped commitments or "wait, what did we decide?" confusion.
- To QA AI-generated meeting notes for transcript-dump slop.

**When NOT to use:**
- A raw verbatim transcript you intend to keep as a record (not a summary).
- A general policy announcement — use the internal-communication detector.

**Audience:** Meeting owners, chiefs of staff, PMs, and anyone reviewing meeting notes before they go out.

---

## Inputs / Context

1. **The summary** — the meeting summary being evaluated.
2. **Meeting context** — what the meeting was about and who attended (if known).
3. **Goal** — what readers should be able to do after reading (act on decisions, track items).

---

## Constraints

### Must
- Score all five axes 0–5 using the anchors provided.
- Anchor every fix to an exact location in the summary and give exact replacement text.
- Verify each required element is present and assess its quality.
- Return strict JSON only, matching the Output Format.

### Must Not
- Invent decisions, owners, dates, or attendees not present in the summary; any names/dates in *example* fix text are illustrative placeholders the author must replace with what was actually agreed.
- Fabricate rationale or action items the meeting didn't produce — flag missing owners/dates/context, never supply imaginary ones.
- Rewrite the whole summary; restrict yourself to 3–5 high-impact surgical fixes.

---

## Instructions

1. Collect the summary, the meeting context, and the goal.
2. Run the evaluator below verbatim against the summary.
3. Return strict JSON only (no prose outside the JSON).

```
# Meeting Summary Quality Evaluator

You are evaluating a meeting summary. Your job: determine if someone who missed the meeting can
catch up in 60 seconds and know exactly what they need to do—or if this is a vague transcript dump.

## Why This Matters
Bad meeting summaries force people to re-watch recordings, attend meetings they could have skipped,
or miss important action items. Good summaries save 15-30 minutes per person per meeting and prevent
dropped commitments.

## Evaluation Dimensions (score each 0-5)

### 1. Decision Clarity — decisions explicitly called out vs. buried in discussion?
Score 5: Dedicated "Decisions" section with 3-5 specific decisions, each with an owner and reasoning if non-obvious.
Score 3: Decisions mentioned but mixed with discussion notes, not clearly distinguished.
Score 0: No clear decisions identified, or you have to infer them.

### 2. Action Item Precision — each action has owner, due date, and success criteria?
Score 5: Every action has [Owner] [Due date] [Specific deliverable].
  ("[Sarah] [Oct 15] Send pricing deck to Acme Corp.")
Score 3: Actions listed but missing owner or due date, or the deliverable isn't specific.
Score 0: Vague actions like "Team to follow up on proposal" with no owner or timeline.

### 3. Context Efficiency — can an absentee understand WHY decisions were made?
Score 5: Each decision includes a 1-2 sentence rationale. Enough context, not a full transcript.
Score 3: Some context but too sparse (no reasoning) or too verbose (transcript dump).
Score 0: Either no context (just a list) or a full transcript that takes 10 minutes to read.

### 4. Open Question Tracking — unresolved questions explicitly listed for follow-up?
Score 5: "Open Questions" section with an owner assigned to resolve each one.
Score 3: Questions mentioned but not clearly separated or no owner assigned.
Score 0: Unresolved questions buried in notes or not captured at all.

### 5. Scanability — can you find what you need in 30 seconds?
Score 5: Clear sections (Decisions, Actions, Questions), bullets, bold for owners/dates.
Score 3: Some structure but dense paragraphs or unclear hierarchy.
Score 0: Wall of text or stream-of-consciousness notes.

## Required Elements (must have)
- Decisions section: what was decided (even if the decision was "defer until X")
- Action items: who owns what by when
- Attendees: who was there (context on who made decisions)

## Anti-Patterns to Flag (specific to meeting summaries)
- Transcript dump—paragraphs of discussion without distilling decisions
- Action items without owners: "We need to follow up on this"
- No due dates on action items
- Decisions buried in discussion notes instead of called out
- No distinction between "discussed" and "decided"
- Missing context on why decisions were made
- Open questions not tracked or no owner assigned to resolve

## Verdict Thresholds
ACCEPT: >=4.2 overall, all required elements present, <2 critical gaps
REVISE: 3.0-4.1 overall, OR missing 1 required element, OR action items lack owners/dates
REJECT: <3.0 overall, OR missing 2+ required elements, OR decisions not clearly identified

## Instructions
Be surgical: give 3-5 specific fixes that move REVISE -> ACCEPT.
Do not rewrite the whole thing. Point to exact locations and give exact replacement text.
Prioritize fixes by impact—what matters most for enabling people to act on the meeting outcomes?
Do not invent decisions, owners, dates, or attendees; flag missing items rather than fabricating them.

Return strict JSON in the format specified below.
```

---

## False-Positive Prevention

❌ **DON'T:**
- Penalize a tight summary for omitting discussion when every decision, owner, and date is present.
- Reward a long, well-formatted summary that still leaves actions ownerless.
- Assign an owner or deadline the meeting never set just to fill a gap.
- Demand rationale for a decision whose reasoning is genuinely obvious.

✅ **DO:**
- Reward clear Decisions/Actions/Questions sections even in a short recap.
- Treat illustrative names/dates in fix text as placeholders for what was actually agreed.
- Flag missing owners, dates, or context as gaps; never supply fabricated ones.
- Distinguish "discussed" from "decided" and call out where the summary blurs them.

---

## Output Format

```json
{
  "overall_score": 3.5,
  "axis_scores": {
    "decision_clarity": 3,
    "action_item_precision": 3,
    "context_efficiency": 4,
    "open_question_tracking": 3,
    "scanability": 4
  },
  "verdict": "ACCEPT | REVISE | REJECT",
  "required_elements": {
    "decisions_section": {"present": true, "quality": "decisions present but not clearly separated from discussion"},
    "action_items": {"present": true, "quality": "actions listed but some missing due dates"},
    "attendees": {"present": true, "quality": "attendee list included"}
  },
  "critical_gaps": [
    "Two action items have no owner assigned",
    "One decision has no context on why it was made"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Action items section, line 'Follow up with legal team'",
      "problem": "No owner or due date specified",
      "fix": "Replace with: '[Rahul] [Oct 18] Email legal team contract redlines for the Acme deal; response needed by Oct 22.'",
      "why": "Owner + deadline + specific deliverable = accountability and clarity"
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
- [ ] No invented decisions, owners, dates, or attendees; missing items flagged, not fabricated.
- [ ] Output is strict JSON with no surrounding prose.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Frames the job as judging 60-second catch-up and actionability.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five orthogonal axes (decisions, actions, context, open questions, scanability).
- **DS-02 (Metric/Criteria Specification):** 0–5 anchors and ACCEPT/REVISE/REJECT thresholds define scoring precisely.
- **ST-02 (Structured Output Format):** Strict JSON schema makes results machine-readable.
- **CM-02 (Explicit Constraints):** Must/Must-Not bound the evaluator and forbid fabricating decisions or owners.

---

## Related Prompts
- `domain-professional-writing/content-quality/quality_slop_internal_communication.md` — sibling detector for announcements and memos.
- `domain-productivity/validation/validation_final_gate.md` — final ship/no-ship gate before distribution.
- `domain-productivity/validation/validation_reality_check.md` — surface the questions an absentee would still have.
