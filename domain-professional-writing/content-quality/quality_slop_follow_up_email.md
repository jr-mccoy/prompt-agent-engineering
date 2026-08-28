---
title: "Follow-up Email Slop Detector"
category: professional-writing/content-quality
description: "Score a follow-up email (post-meeting/demo/proposal) against five quality axes and return surgical, location-specific fixes that move it from generic check-in to a response-worthy message."
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
  - follow-up-email
  - sales-enablement
  - anti-fabrication
updated: "2026-06-19"
related_prompts:
  - domain-professional-writing/content-quality/quality_slop_sales_outreach.md
  - domain-productivity/validation/validation_final_gate.md
  - domain-productivity/validation/validation_reality_check.md
---

# Follow-up Email Slop Detector

**Objective:** Judge whether a follow-up email advances the conversation — or is a generic check-in that gets ignored — and return a small set of exact, location-anchored fixes that raise response rate.

**When to use:**
- Before sending a follow-up after a meeting, demo, or proposal.
- When a sequence of follow-ups is getting low or no replies.
- To QA AI-drafted follow-ups for "just checking in" slop.

**When NOT to use:**
- A first-touch cold outreach email — use the sales-outreach detector instead.
- Internal status pings where no conversation is being advanced.

**Audience:** Salespeople, founders, account managers, and anyone reviewing follow-up email drafts before they ship.

---

## Inputs / Context

1. **The draft** — the full follow-up email being evaluated.
2. **Prior interaction** — what actually happened in the previous meeting/demo/call (topics, concerns, commitments).
3. **Goal** — what a positive reply should lead to (a meeting, a decision, a signed contract).

---

## Constraints

### Must
- Score all five axes 0–5 using the anchors provided.
- Anchor every fix to an exact location in the draft and give exact replacement text.
- Verify each required element is present and assess its quality.
- Return strict JSON only, matching the Output Format.

### Must Not
- Invent statistics, customer names, or metrics about the draft being judged; any names/numbers in *example* fix text are illustrative placeholders the author must replace with real data.
- Fabricate proof or claim the draft contains specifics it does not — flag missing proof, never supply imaginary proof.
- Rewrite the whole email; restrict yourself to 3–5 high-impact surgical fixes.

---

## Instructions

1. Collect the draft, prior-interaction context, and goal.
2. Run the evaluator below verbatim against the draft.
3. Return strict JSON only (no prose outside the JSON).

```
# Follow-up Email Quality Evaluator

You are evaluating a follow-up email (after meeting, demo, proposal, etc.). Your job:
determine if this advances the conversation—or if it's a generic check-in that gets ignored.

## Why This Matters
Bad follow-ups get <5% response rate and waste selling time. Good follow-ups get 20-40%.
The difference: specific reference to previous conversation, clear value add, and an
easy-to-answer question.

## Evaluation Dimensions (score each 0-5)

### 1. Conversation Continuity — references specific details from the previous interaction?
Score 5: References a specific topic discussed, concern raised, or commitment made.
  ("Following up on your question about SOC2 compliance during yesterday's demo...")
Score 3: Generic reference to the meeting but no specific details.
Score 0: Could be sent without any previous interaction. ("Checking in to see if you had questions.")

### 2. Value Addition — provides something useful beyond "just checking in"?
Score 5: Includes a specific resource, an answer to a question raised, or relevant new info.
  ("Attached is the ROI calculator you asked about, pre-filled with your team size.")
Score 3: Attempts value but it's generic or not clearly relevant.
Score 0: Pure check-in, no new information or value.

### 3. Response Facilitation — easy for the recipient to respond?
Score 5: Asks a specific yes/no question or gives clear options.
  ("Does Oct 15 or Oct 18 work for the technical deep-dive you mentioned?")
Score 3: Asks a question but it's somewhat open-ended.
Score 0: No question, or vague "Let me know if you have questions."

### 4. Urgency Without Pressure — a timing hook that's logical, not pushy?
Score 5: Natural timing trigger.
  ("Your trial ends Friday—want to lock in this pricing before renewal?")
Score 3: Some timing element but feels slightly forced.
Score 0: No timing context, or artificial urgency that feels pushy.

### 5. Clarity of Next Step — obvious what happens if they respond positively?
Score 5: Specific next step stated.
  ("If these dates work, I'll send a calendar invite with the technical team.")
Score 3: Next step implied but not explicit.
Score 0: Unclear what happens next. ("Let's continue the conversation.")

## Required Elements (must have)
- Specific reference: details from the previous interaction (not generic "our meeting")
- Value add: new information, resource, or answer to a question
- Easy response: a specific question or clear options (not open-ended)

## Anti-Patterns to Flag (specific to follow-up emails)
- "Just checking in" / "Wanted to circle back" with no specific reference
- No new value—just reminds them you exist
- Vague next steps: "Let me know if you want to chat further"
- Could be sent to anyone you've ever talked to—no specific details
- Open-ended question that requires the recipient to think hard
- Artificial urgency: "Limited spots remaining!" with no real constraint
- Too long—buries the ask in paragraphs

## Verdict Thresholds
ACCEPT: >=4.2 overall, all required elements present, <2 critical gaps
REVISE: 3.0-4.1 overall, OR missing 1 required element, OR adds no value
REJECT: <3.0 overall, OR "just checking in" with no specifics, OR adds no value beyond a reminder

## Instructions
Be surgical: give 3-5 specific fixes that move REVISE -> ACCEPT.
Do not rewrite the whole thing. Point to exact locations and give exact replacement text.
Prioritize fixes by impact—what matters most for response rate and moving the deal forward?
Do not invent metrics or customer proof; flag missing proof rather than fabricating it.

Return strict JSON in the format specified below.
```

---

## False-Positive Prevention

❌ **DON'T:**
- Penalize a short, sharp email for being short when it already references specifics and asks a clear question.
- Reward keyword-stuffed "personalization" that name-drops without advancing anything.
- Invent a response-rate number or a customer result to justify a score.
- Demand a timing hook when no genuine deadline exists.

✅ **DO:**
- Reward genuine continuity and a single easy-to-answer ask, even in a two-line email.
- Treat illustrative names/metrics in fix text as placeholders the author must replace.
- Flag missing proof as a gap; never supply fabricated proof.
- Distinguish a logical timing trigger from manufactured scarcity.

---

## Output Format

```json
{
  "overall_score": 3.6,
  "axis_scores": {
    "conversation_continuity": 4,
    "value_addition": 3,
    "response_facilitation": 4,
    "urgency_without_pressure": 3,
    "clarity_of_next_step": 3
  },
  "verdict": "ACCEPT | REVISE | REJECT",
  "required_elements": {
    "specific_reference": {"present": true, "quality": "mentions the meeting but vague on what was discussed"},
    "value_add": {"present": true, "quality": "offers to answer questions but provides nothing proactively"},
    "easy_response": {"present": true, "quality": "asks a clear yes/no question"}
  },
  "critical_gaps": [
    "Adds no new value—just reminds them of the previous meeting",
    "No timing context—unclear why this follow-up now"
  ],
  "top_fixes": [
    {
      "priority": 1,
      "location": "Opening: 'Just wanted to follow up on our meeting last week'",
      "problem": "Generic reference—could be any meeting with anyone",
      "fix": "Replace with: 'Following up on your question during Tuesday's demo about how we handle EU data residency.'",
      "why": "Specific day + specific question shows you listened and are addressing their real concern"
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
- [ ] No invented metrics, names, or proof about the draft; missing proof flagged, not fabricated.
- [ ] Output is strict JSON with no surrounding prose.

---

## Techniques Used
- **ST-01 (Clear Objective Statement):** Frames the job as judging whether the email advances the conversation.
- **RT-02 (Multi-Dimensional Analysis Framework):** Five orthogonal quality axes structure the evaluation.
- **DS-02 (Metric/Criteria Specification):** 0–5 anchors and ACCEPT/REVISE/REJECT thresholds define scoring precisely.
- **ST-02 (Structured Output Format):** Strict JSON schema makes results machine-readable.
- **CM-02 (Explicit Constraints):** Must/Must-Not bound the evaluator and forbid fabrication.

---

## Related Prompts
- `domain-professional-writing/content-quality/quality_slop_sales_outreach.md` — sibling detector for first-touch cold/warm outreach.
- `domain-productivity/validation/validation_final_gate.md` — final ship/no-ship gate before sending.
- `domain-productivity/validation/validation_reality_check.md` — surface objections a skeptical recipient would raise.
