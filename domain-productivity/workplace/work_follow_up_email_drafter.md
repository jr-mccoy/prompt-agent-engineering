---
title: "Follow-Up Email Drafter"
category: productivity/workplace
description: "Draft a structured follow-up email after a meeting, interview, or call that captures commitments and confirms next steps."
techniques:
  - ST-01
  - ST-02
  - DS-01
  - CM-02
  - QA-01
  - RT-06
difficulty: beginner
tags:
  - email
  - follow-up
  - communication
  - action-items
  - workplace
updated: "2026-05-12"
related_prompts:
  - domain-productivity/workplace/work_meeting_agenda_builder.md
  - domain-productivity/workplace/work_status_update_writer.md
  - domain-productivity/workplace/work_1on1_prep.md
  - domain-personal-development/prompts/agency/agency_next_action_spec.md
---

# Follow-Up Email Drafter

**Objective:** Draft a ready-to-send follow-up email after a meeting, interview, networking conversation, or client call. The email captures what was discussed, confirms commitments with owners and dates, and makes it easy for the recipient to know exactly what happens next.

**When to use:** Within 24 hours of any meeting or conversation where commitments were made or decisions were reached. Especially useful after: job interviews, client kickoff or check-in calls, networking coffees, internal project meetings where action items were assigned, and any conversation where you made a promise.

**Audience:** Anyone who needs to send a professional follow-up after a work conversation. Works for ICs, managers, job seekers, and client-facing roles. Not for casual social conversations or situations where no commitments were made and a quick "thanks for chatting" text suffices.

---

## Inputs Required

1. **Meeting type.** Choose: internal team meeting, job interview, client call, networking conversation, or sales/vendor call. Each type gets a different emphasis in the email structure.

2. **What was discussed.** A brief summary of the main topics or themes — 3–6 bullet points is enough. Do not try to capture everything; focus on what matters for follow-through.

3. **Commitments and action items.** List every action item that came out of the conversation: who does it, what it is, and when it is due. If no deadlines were set in the meeting, assign reasonable ones now — don't leave them open-ended.

4. **Decisions confirmed.** Any choices that were made or agreed to during the conversation. These should be explicitly restated in the email so both parties are on the same page.

5. **Relationship and tone.** Is this a new relationship (first or second interaction) or established? Is the register formal (executive, client) or informal (teammate, peer)? This affects word choice and length.

6. **For job interviews only.** One specific thing from the conversation you want to reference — a detail about the role, a problem they mentioned, something you learned that sharpened your interest. Generic "I'm very interested" without a specific hook is wasted space.

---

## Instructions

### Step 1 — Choose the right subject line

The subject line must be specific enough for the recipient to know exactly what email this is when they see it in their inbox three days later. Bad: "Following up." Good: "Action items from today's API roadmap sync" or "Thank you — [Company] [Role title] interview."

Format: `[Type] — [Meeting name or topic], [date]`

### Step 2 — Write the opening line

Do not open with "I hope this email finds you well," "It was great meeting with you," or any other filler. Open with the most important fact: what the email is about and why the recipient should read it.

Good openers:
- "Following our call today, here are the action items and decisions we landed on."
- "Thank you for the interview — I wanted to confirm next steps and share one thought."
- "Quick summary from this morning's kickoff, including what each team owns going forward."

### Step 3 — Structure the body by meeting type

**Internal team meeting:**
- One sentence on what the meeting covered
- Bulleted action items with owner and due date (format: `[Owner] — [Action] — by [date]`)
- Decisions confirmed
- Any open questions that still need resolution

**Job interview:**
- One sentence of genuine thanks (not effusive — one sentence)
- One specific thing from the conversation that sharpened your interest or that you want to address
- Reiterate your interest in the role (one sentence, not a paragraph)
- Confirm any next steps the interviewer mentioned
- Close with a clear prompt for next action if none was given

**Client call:**
- Brief recap of what the call covered (2–3 lines)
- Action items with owner and due date, separated by party (what you own vs. what they own)
- Any decisions made that need to be documented
- What the client needs to do and by when — make this impossible to miss

**Networking conversation:**
- One sentence of thanks for their time
- Reference one specific thing from the conversation that was useful or that you want to follow up on
- Any commitments you made (introductions, resources to share, follow-up meeting)
- A clear ask or next step, if any — or an explicit "no ask" so the relationship doesn't feel transactional

### Step 4 — Close with a clear next step

Every follow-up email must end with exactly one of:
- A specific next action for the recipient ("Please confirm by Friday whether the revised timeline works")
- A specific next action you are taking ("I'll send the draft by EOD Thursday")
- An explicit statement that no further action is needed ("No action needed from your side — I'll keep you posted on progress")

Do not close with "Let me know if you have any questions." It is filler and puts all the burden on the recipient.

---

## Constraints

### Must
- Open with a subject line that identifies the meeting, not just "Following up"
- Lead the body with the meeting's outcome or action items, not pleasantries
- Format action items as: [Owner] — [Action] — [Due date]
- Close with exactly one named next step or an explicit statement that none is needed
- Match length to the meeting: a 30-minute call → 3–5 short paragraphs or equivalent bullets; a 2-hour workshop → structured summary sections

### Must Not
- Open with "I hope this email finds you well" or any equivalent filler
- Write more than one page for any single meeting follow-up
- List action items without owners or due dates
- Use vague commitments like "we'll follow up on this" — every commitment must be owned and dated
- In client emails, reference internal team names, tools, or processes the client doesn't need to know about
- In interview follow-ups, write more than 2–3 short paragraphs

---

## False-Positive Prevention

1. **The wall of text:** Writing a narrative summary of everything discussed instead of structured bullets. The recipient needs to scan for their name and their action items — not read a meeting transcript.

2. **The ownerless action item:** Listing "the API spec needs to be finalized" without naming who does it. Unowned actions do not happen.

3. **The dateless commitment:** Writing "I'll send this over soon." Soon is not a date. Every commitment in a follow-up email must have a specific date or the word "today."

4. **The generic interview follow-up:** Writing "I'm very interested in this role and believe I'd be a great fit." Without a specific reference to something from the conversation, this reads as a form letter and is forgotten immediately.

5. **The filler close:** Ending with "Please don't hesitate to reach out if you have any questions." Replace with a concrete next step or an explicit confirmation that none is needed.

6. **The missing decision confirmation:** Sending a follow-up that lists action items but doesn't confirm the decisions that were actually made. If a decision was reached in the meeting, the follow-up is the record of it.

---

## Output Format

```
Subject: [Type] — [Meeting name or topic], [date]

[Opening line — what this email is about, specific and direct]

[For team meetings and client calls — 1–2 sentence meeting summary]

ACTION ITEMS
- [Owner] — [Action] — by [date]
- [Owner] — [Action] — by [date]
- [Owner] — [Action] — by [date]

DECISIONS CONFIRMED
- [Decision 1]
- [Decision 2]
[Remove this section if no decisions were made]

OPEN QUESTIONS (not yet resolved)
- [Question] — [who will resolve it and by when]
[Remove this section if nothing is outstanding]

[Closing line — one specific next step, or explicit statement that none is needed]

[Name]
```

**For job interview follow-ups:**
```
Subject: Thank you — [Role title] interview, [date]

[One sentence of thanks, specific to who you met with]

[One specific observation from the conversation — a problem they mentioned, a detail about the role or team, something that sharpened your understanding or interest]

[One sentence reaffirming your interest, tied to the specific detail above]

[Confirm the next steps they mentioned, or ask what to expect and when]

[Your name]
[Contact info / LinkedIn if not already shared]
```

---

## Verification

- [ ] Subject line identifies the meeting, not just "Following up"
- [ ] Email opens with substance, not pleasantries
- [ ] Every action item has an owner and a due date
- [ ] Decisions confirmed are listed separately from action items
- [ ] Email closes with one named next step or an explicit "no action needed"
- [ ] Length is proportionate to the meeting (not a wall of text for a short call)
- [ ] No internal jargon or tool names in client-facing emails
- [ ] Interview follow-ups reference one specific detail from the conversation
