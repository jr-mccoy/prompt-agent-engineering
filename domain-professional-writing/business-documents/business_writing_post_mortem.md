# Post-Mortem / Incident Report

**Source:** BUSINESS_WRITING_PROMPTS.md

**Category:** Business Writing / Incident Management

## Prompt

```
You are writing a post-mortem that documents what happened, why it happened, and how to prevent it from happening again.

CONTEXT:
Incident name: [BRIEF DESCRIPTION OF WHAT HAPPENED]
Date/time of incident: [WHEN THIS OCCURRED]
Severity: [IMPACT LEVEL - e.g. "production outage" or "data inconsistency" or "security incident"]
Affected systems/users: [WHAT/WHO WAS IMPACTED]
Team involved: [WHO RESPONDED]

INPUT PROVIDED:
[PASTE YOUR TIMELINE, MONITORING DATA, SLACK LOGS, ROOT CAUSE ANALYSIS, RESPONSE ACTIONS HERE]

YOUR TASK:
Create a post-mortem that helps the organization learn from this incident. This will be read by people who weren't involved and need to understand what happened and what changes we're making. Blameless tone is critical.

REQUIRED STRUCTURE:
1. **Summary** (What happened in 2-3 sentences - impact and duration)
2. **Timeline** (Chronological events from detection to resolution - use actual timestamps from inputs)
3. **Root Cause** (The actual underlying reason, not just the proximate trigger)
4. **Impact** (Quantified user/business impact - numbers from actual data)
5. **What Went Well** (What worked in our response - be specific)
6. **What Went Poorly** (What failed in detection, response, or prevention - be honest)
7. **Action Items** (Specific fixes with owners and deadlines - prevent recurrence)

CONSTRAINTS:
- Total length: 800 words maximum
- Summary: Must quantify impact (users affected, duration, revenue impact if available)
- Timeline: Must use actual timestamps from inputs (not rounded or estimated)
- Root cause: Must go deeper than surface trigger ("load increased" is not root cause - why didn't system handle load?)
- Impact: Must use actual numbers from monitoring/logs (not "many users" or "significant downtime")
- What went well: Must be specific actions/decisions, not generic praise
- What went poorly: Must focus on systems/processes, never individuals
- Action items: Must have owner name, specific deliverable, and date
- DO NOT blame: Focus on system failures, not people failures
- DO NOT sugarcoat: If something was broken, say it was broken
- Use only data from inputs - do not estimate impact or invent timeline events

TONE:
- Factual and learning-oriented, not defensive or blame-seeking
- Specific about failures ("Alert threshold was 5x too high") not vague ("Alerting could be better")
- Systems-focused ("We lacked redundancy") not people-focused ("Someone should have checked")
- Action-oriented in fixes, not just analysis

QUALITY CHECKS - Before outputting, verify:
- [ ] Summary includes actual numbers for impact and duration
- [ ] Timeline uses actual timestamps from inputs (e.g. "14:23:45 UTC" not "around 2pm")
- [ ] Root cause explains why the system failed, not just what failed
- [ ] Impact section uses actual metrics from monitoring data
- [ ] "What went well" lists specific actions with times/people
- [ ] "What went poorly" critiques systems/processes, never names individuals
- [ ] Every action item has specific owner name, deliverable, and deadline
- [ ] No blame language anywhere ("if someone had..." or "X should have known")
- [ ] Action items address root cause, not just symptoms
- [ ] Total word count is under 800 words

If any check fails, revise before outputting.
```

## Usage Notes

**Purpose:** Post-mortems exist to prevent recurrence through organizational learning, not to assign blame.

**Customization Options:**
- Adjust for incident management process (severity levels, SLO tracking, incident commanders)
- Modify for organization culture (emphasize blameless culture, action item tracking)
- Add sections for different incident types (security, data, performance, customer-facing, third-party)

**Common Pitfalls:**
- Blaming individuals instead of systems
- Surface-level root cause (symptom vs. cause)
- Vague impact ("several users affected")
- Timeline without specific timestamps
- Action items without owners or deadlines
- Action items that address symptoms not causes
