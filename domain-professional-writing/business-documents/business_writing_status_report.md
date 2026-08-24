# Status Report (Weekly/Monthly Updates)

**Source:** BUSINESS_WRITING_PROMPTS.md

**Category:** Business Writing / Project Reporting

## Prompt

```
You are writing a status report that surfaces blockers and enables resource allocation decisions.

CONTEXT:
Project/Team: [PROJECT OR TEAM NAME]
Reporting period: [DATE RANGE]
Report audience: [WHO READS THIS - e.g. "Engineering leadership team"]
Next review: [WHEN THIS WILL BE REVIEWED - e.g. "Monday standup"]

INPUT PROVIDED:
[PASTE YOUR RAW UPDATES, NOTES, DATA, METRICS HERE]

YOUR TASK:
Create a status report that helps leadership understand project health and unblock your team. This report is used to make resource allocation decisions and escalate problems.

REQUIRED STRUCTURE:
1. **Status** (One sentence: On track / At risk / Blocked - with reason)
2. **Progress This Period** (What shipped or completed - max 3 items, metrics where relevant)
3. **Blockers** (What's preventing progress - must include impact and owner)
4. **Priorities Next Period** (What you'll focus on - max 3 items)
5. **Asks** (What you need from leadership - be specific)

CONSTRAINTS:
- Total length: 400 words maximum
- Status line: Must be one of "On track", "At risk: [reason]", "Blocked: [reason]"
- Progress items: Use past tense and metrics ("Shipped feature X, reduced load time by 40%")
- Blockers: Must follow format "BLOCKER: [what] | IMPACT: [consequence] | OWNER: [who's working it] | BLOCKED SINCE: [date]"
- Priorities: Use future tense and outcomes ("Will complete Y to enable Z")
- Asks: Must be specific and actionable ("Need design resource for 20 hours next week")
- DO NOT include: explanations of why things went well, team celebrations, general updates
- DO NOT soften: If blocked, say blocked. If at risk, say at risk. Don't hide problems.
- Use only data from the input - do not estimate progress you don't have data for

TONE:
- Factual and unvarnished, not optimistic or defensive
- Use metrics for progress claims ("increased conversion by 12%", not "improved conversion")
- Be specific about problems ("3 days blocked waiting for API keys", not "experiencing delays")
- No corporate hedging ("we're blocked" not "we're facing some challenges")

QUALITY CHECKS - Before outputting, verify:
- [ ] Status line is present and uses exact format (On track / At risk / Blocked)
- [ ] Every progress item has a metric or specific deliverable
- [ ] Every blocker has impact, owner, and date it started
- [ ] Priorities are stated as outcomes, not activities
- [ ] Every ask is specific enough that someone can say yes or no
- [ ] If status is "At risk" or "Blocked", there's a corresponding blocker or ask
- [ ] No metric is estimated - all numbers come from input data
- [ ] Total word count is under 400 words

If any check fails, revise before outputting.
```

## Usage Notes

**Purpose:** Status reports exist to surface blockers and enable resource allocation decisions, not to provide general updates.

**Customization Options:**
- Adjust for different reporting contexts (engineering, product, sales, marketing, operations)
- Modify for different cadences (daily standups vs. weekly reports vs. board updates)
- Add metrics section for investor/board reporting

**Common Pitfalls:**
- Hiding bad news with diplomatic language
- Vague progress claims without metrics
- No clear asks for leadership
- Burying blockers in narrative
