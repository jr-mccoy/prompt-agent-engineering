---
title: "Pre-Meeting Prep and Post-Meeting Processing of Raw Notes"
category: business-strategy/chief-of-staff
description: "A two-part protocol: a lightweight pre-meeting brief that names the user's intent, the key decision, and the worst outcome; and a post-meeting processor that turns raw notes into commitments, decisions, and owned next actions."
techniques:
  - ST-01
  - ST-02
  - CM-02
  - RT-02
  - QA-01
difficulty: intermediate
tags:
  - chief-of-staff
  - meetings
  - prep
  - notes
  - follow-up
updated: "2026-04-20"
related_prompts:
  - domain-business-strategy/chief-of-staff/cos_morning_briefing.md
  - domain-productivity/deep-work/deepwork_meeting_cost_estimator.md
  - domain-productivity/deep-work/deepwork_meeting_to_async_converter.md
---

# Pre-Meeting Prep and Post-Meeting Processing

**Objective:** Two short protocols, one before and one after a meeting. The pre protocol names the user's intent, the key decision, and the worst outcome. The post protocol turns raw notes into three clean lists — commitments made, decisions recorded, and next actions owned — with nothing falling through the cracks.

**When to use:**
- **Pre:** Before any meeting ≥30 minutes, or any meeting with more than two attendees, or any meeting where a decision is supposed to happen. ~5 minutes.
- **Post:** Within 30 minutes of meeting end, while memory is fresh. ~5–10 minutes.

**Audience:** Individual knowledge worker or executive. Self-run. Outputs are short enough to paste into a calendar event or a follow-up email.

---

## Inputs Required

### For pre-meeting
1. **Meeting title, attendees, duration, and who called it.**
2. **Why the user is attending.** One sentence.
3. **Any pre-read the user has seen.** Name it or say "none."

### For post-meeting
1. **Raw notes from the meeting.** Verbatim. Typos fine.
2. **A list of who was in the room/call**, if not obvious from notes.
3. **Any recordings/transcripts** the user wants parsed alongside notes.

If the user only has "I remember roughly what happened," the post step will still run, but flag that the output is reconstructed, not captured.

---

## Instructions

### Part A — Pre-meeting prep (5 minutes)

#### A1. Name the user's real intent
One sentence answering: what does the user need to walk away with? Must be one of:
- A decision made.
- Specific information learned.
- A relationship moved forward.
- A commitment secured from someone else.
- A commitment made by the user.

"Being present" is not a valid intent. If that's the only honest answer, flag the meeting as a decline candidate.

#### A2. Identify the key decision (if any)
If a decision is supposed to happen, state it as "[A] or [B]" or "whether to [X]." If no decision is supposed to happen, say "no decision expected; this is [info/align/relationship]."

#### A3. Name the worst outcome
One sentence: what is the worst realistic outcome of this meeting? Not apocalyptic — just the specific failure that would be bad. This pre-emptively surfaces what the user should watch for.

#### A4. Prep actions (capped at three)
Up to three things the user needs to do before the meeting:
- Read [X].
- Draft [Y position].
- Bring [Z data].

If the user needs more than three, the meeting is under-prepped given available time — flag that.

### Part B — Post-meeting processing (5–10 minutes)

#### B1. Parse every statement into one of four categories
Read the notes. Tag each substantive line:
- **Commitment** (someone said they'd do something).
- **Decision** (a choice was made).
- **Information** (a fact or context shared).
- **Parking-lot** (raised but not resolved).

Side-chatter and process ("let's move on") does not get tagged.

#### B2. Extract commitments
For each commitment:
- Who committed.
- What exactly.
- By when.
- How the user will know it happened.

If a commitment was made in vague language ("I'll look into it"), write it down as vague — do not invent a deadline the person didn't give. Flag for follow-up.

#### B3. Record decisions
For each decision:
- What was decided.
- Who decided (or "the group").
- What alternatives were considered, briefly.
- What this decision blocks or unblocks.

#### B4. Own the user's next actions
From the commitments list, pull out the ones the user made. Also include any implicit actions ("I should follow up with Alice"). Give each:
- Verb-first one-liner.
- By when.
- First move.

#### B5. Flag what was unsaid
One short section: what should have been decided or committed but wasn't? This is the highest-value part of the protocol. Examples: "no one owns the integration follow-up," "the budget question got deferred for the third meeting in a row," "[name] didn't speak."

---

## Constraints

### Must
- Pre: name intent, key decision (or absence), worst outcome, up to three prep actions.
- Post: produce four lists (commitments, decisions, information-captured, parking-lot) plus user's own next actions plus unsaid flags.
- Quote notes verbatim when a commitment's exact wording matters.
- Call vague commitments vague; do not sharpen them without basis.

### Must Not
- Invent commitments or decisions that weren't in the notes.
- Smooth out political tension by summarizing it away.
- Turn the post-processing into a narrative of the meeting.
- Assign commitments to people who did not make them.
- Produce a long document. Both parts are short by design.

---

## False-Positive Prevention

1. **Don't upgrade "I'll think about it" to "Will decide by Friday."** Vague commitments are data — sharpening them without the person's words fabricates a record.
2. **Don't let the user off the hook.** If the user made a commitment, it goes into their action list. Do not move it to "the team will do this."
3. **Don't collapse parking-lot into decisions.** If something was raised and not resolved, it stays parked, with a name attached.
4. **Don't skip the unsaid flags.** The value of post-processing is often in what wasn't said, not what was.
5. **If the raw notes are thin,** say so and produce a shorter output. Don't pad.

---

## Output Format

### Pre-meeting brief
```
# Pre: [meeting title] — [time]

## Intent
[One sentence. If "just being present," flag decline candidate.]

## Key decision
[A or B, or "no decision expected — info/align/relationship."]

## Worst realistic outcome
[One sentence.]

## Prep (up to 3)
- [ ] [Action]
- [ ] [Action]
- [ ] [Action]
```

### Post-meeting processed notes
```
# Post: [meeting title] — [date]

## Commitments
| Who    | What                    | By when       | How I'll know |
|--------|-------------------------|---------------|---------------|

(Flag any vague commitments as such.)

## Decisions
- [What was decided] — by [who]; alternatives: [brief]; unblocks: [what].

## Information captured
- [Fact / context / signal]

## Parking-lot
- [Raised but unresolved] — parked with: [owner, if named].

## My next actions
- [Verb-first], by [when]. First move: [specific].

## Unsaid / should-have-happened
- [What didn't get decided or committed that should have.]
```

---

## Verification

- [ ] Pre has intent, decision status, worst outcome, prep.
- [ ] Post has all four note categories.
- [ ] Vague commitments are flagged as vague.
- [ ] The user's own actions are separated out.
- [ ] At least one "unsaid" flag or an honest "nothing notable unsaid."
- [ ] Each protocol fits on one screen.
