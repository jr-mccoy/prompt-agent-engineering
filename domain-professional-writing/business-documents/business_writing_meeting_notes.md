# Meeting Notes (From Transcript or Raw Notes)

**Source:** BUSINESS_WRITING_PROMPTS.md

**Category:** Business Writing / Meeting Documentation

## Prompt

```
You are writing meeting notes that ensure follow-through and accountability.

CONTEXT:
Meeting: [MEETING NAME/TYPE]
Date: [DATE]
Attendees: [LIST ATTENDEES]
Purpose of meeting: [WHAT THIS MEETING WAS SUPPOSED TO ACCOMPLISH]

INPUT PROVIDED:
[PASTE TRANSCRIPT OR RAW NOTES HERE]

YOUR TASK:
Create meeting notes that help the team execute on what was discussed. These notes are used in our [WEEKLY STANDUP/PROJECT TRACKER/SLACK CHANNEL] where people check what they're responsible for.

REQUIRED STRUCTURE:
1. **Decisions Made** (what was decided, who made the decision)
2. **Action Items** (what needs to be done, who owns it, deadline)
3. **Open Questions** (what still needs resolution, who will resolve it)
4. **Key Discussion Points** (context for decisions, max 3 bullets)

CONSTRAINTS:
- Total length: 300 words maximum
- Decisions section: Must identify decision-maker by name
- Action items: Must follow format "ACTION: [what] | OWNER: [name] | DUE: [date]"
- Open questions: Must follow format "QUESTION: [what] | OWNER: [who will answer] | BY: [date]"
- DO NOT include: meeting pleasantries, general discussion that didn't lead to decisions
- DO NOT infer: If a decision wasn't explicitly made, put it in Open Questions
- Use only information from the input - do not add action items that weren't discussed

TONE:
- Direct and specific, not diplomatic
- Use names, not roles ("Sarah" not "the PM")
- No corporate hedging ("we should consider" → "Decision: we will do X")

QUALITY CHECKS - Before outputting, verify:
- [ ] Every decision has a named decision-maker
- [ ] Every action item has owner and specific date (not "soon" or "next week")
- [ ] If there are no decisions documented, I have confirmed nothing was actually decided
- [ ] No action item is vague (no "follow up on" or "look into")
- [ ] Open questions have assigned owners who will answer them
- [ ] Total word count is under 300 words
- [ ] I have not invented action items that weren't discussed in the meeting

If any check fails, revise before outputting.
```

## Usage Notes

**Purpose:** Meeting notes exist to ensure follow-through and accountability. The structure forces outcomes over narration.

**Customization Options:**
- Change workflow integration based on your tools (Asana/Jira/Linear format)
- Adjust for different meeting types (sprint planning, executive review, all-hands, 1-on-1s)
- Modify voice for your organization's culture (more diplomatic vs. direct)

**Common Pitfalls:**
- No decisions documented
- Action items without owners
- Vague deadlines ("next week")
- Made-up action items AI infers
