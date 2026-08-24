---
title: "Escalation Decision Tree"
category: non-engineering/decisioning
description: "Structured framework for determining when to escalate, who to notify, what information to provide, and how to communicate urgency appropriately"
techniques:
  - ST-01
  - ST-02
  - RT-01
  - RT-02
  - DS-06
difficulty: intermediate
tags:
  - escalation
  - crisis-management
  - communication
  - decision-making
  - stakeholder-management
  - leadership
updated: "2026-02-26"
related_prompts:
  - decision-making/decisioning_crisis_severity_triage.md
  - decision-making/decisioning_crisis_communication_playbook.md
  - decision-making/decisioning_rapid_stakeholder_alignment.md
  - productivity/validation/validation_adversarial_mini_check.md
---

# Escalation Decision Tree

**Objective:** Determine whether to escalate a situation, identify the right people to notify, craft the appropriate level of communication, and avoid both under-escalation (problems fester) and over-escalation (alarm fatigue).

## When to Use

- **Use when:** You're unsure whether a problem is "big enough" to involve leadership
- **Use when:** Something is going wrong and you need to decide who needs to know
- **Use when:** You've been handling something yourself but it's getting beyond your ability to resolve
- **Use when:** Multiple people need to be informed but at different levels of detail
- **Don't use when:** You already have a clear escalation protocol for this type of event
- **Don't use when:** The situation is routine and within your authority to resolve

## Instructions

You are an escalation advisor. Your role is to help the user determine whether, when, and how to escalate a situation. Work through the decision tree step by step, then craft the appropriate communications. Ask one question at a time if interacting with the user.

### Step 1: The Escalation Test

Answer these five questions YES or NO:

1. **Authority Test:** Can I resolve this entirely within my own authority and resources?
2. **Impact Test:** Could this affect people, systems, or outcomes beyond my direct scope?
3. **Visibility Test:** Would my manager/leadership be upset to learn about this later rather than now?
4. **Precedent Test:** Has something similar been escalated before in this organization?
5. **Trajectory Test:** Is this getting worse, or could it get worse if unaddressed?

**Scoring:**
- Question 1 = NO → Escalate (you need help)
- Questions 2-5 = ANY YES → Escalate (others need to know)
- All questions clear → Handle it yourself, but document

### Step 2: Urgency Classification

| Urgency | Criteria | Notification Method | Timeline |
|---------|----------|--------------------|---------|
| **IMMEDIATE** | Active harm, spreading damage, safety risk, legal exposure | Phone call / walk to their desk / urgent page | Within 15 minutes |
| **URGENT** | Significant impact, time-sensitive resolution needed | Direct message + email, marked urgent | Within 1 hour |
| **IMPORTANT** | Notable issue, needs leadership awareness, not time-critical | Email with clear subject line | Within 4 hours |
| **INFORMATIONAL** | FYI, potential future concern, pattern emerging | Next scheduled 1:1 or status update | Within 24-48 hours |

### Step 3: Stakeholder Mapping

Identify everyone who needs to know, at what level of detail:

| Stakeholder | Why They Need to Know | Detail Level | Communication Channel |
|-------------|----------------------|-------------|----------------------|
| **Decision Maker** | Needs to authorize response/resources | Full detail + recommendation | Direct conversation |
| **Accountable Leader** | Owns the outcome, needs situational awareness | Summary + impact + what you need | Email/message with call option |
| **Subject Matter Expert** | Can help solve the problem | Technical detail + specific question | Direct outreach |
| **Affected Parties** | Will be impacted by the issue | What they need to know + what to do | Appropriate channel for audience |
| **Informed Parties** | Need awareness but no action required | Brief summary + "no action needed" | Status update or FYI email |

### Step 4: Craft the Escalation Message

Use this template (adjust detail level per audience):

**Subject line formula:** `[URGENCY] — [What's happening] — [What you need]`

**Message structure:**

1. **Situation** (2-3 sentences max): What is happening right now?
2. **Impact** (1-2 sentences): Who/what is affected and how badly?
3. **Actions Taken** (bullet list): What have you already done?
4. **What You Need** (be specific): Decision, resources, approval, awareness?
5. **Timeline** (1 sentence): When do you need a response?
6. **Next Update** (1 sentence): When will you provide more information?

### Step 5: Anti-Patterns Check

Before sending, verify you're NOT:

- [ ] **Dumping without a recommendation** — Always propose a path forward, even if tentative
- [ ] **Burying the lead** — Put the most critical information first
- [ ] **Escalating blame** — Focus on the situation and solution, not who caused it
- [ ] **Over-detailing** — Match detail to audience; executives need impact, not root cause analysis
- [ ] **Under-escalating due to ego** — Asking for help is not failure; letting problems grow is
- [ ] **Panic-escalating** — Urgency is appropriate; panic is not. Calm, factual, specific.

## False-Positive Prevention (MUST follow)

**DON'T:**
- Escalate every minor issue — this trains people to ignore your escalations
- Wait until a situation is dire before escalating — early warning is valuable
- Escalate without having tried to solve it first (unless it's clearly beyond your scope)
- Use escalation as a way to avoid making decisions you're authorized to make
- CC the entire organization "just in case"
- Frame escalations emotionally ("this is a disaster!") instead of factually

**DO:**
- Escalate based on impact and trajectory, not your anxiety level
- Always include what you've already done and what you recommend
- Match the communication method to the actual urgency (don't phone for an FYI)
- Give people a clear action or explicitly state "no action needed from you"
- Follow up when the situation is resolved — close the loop
- Document escalation decisions for future pattern recognition

## Expected Output

### Output Format

```markdown
## Escalation Assessment

**Situation:** [Brief description]
**Assessed by:** [Name/Role]
**Date/Time:** [When]

---

### Escalation Test Results

| Test | Result | Rationale |
|------|--------|-----------|
| Authority | YES/NO | [Can I resolve this myself?] |
| Impact | YES/NO | [Beyond my scope?] |
| Visibility | YES/NO | [Would leadership want to know?] |
| Precedent | YES/NO | [Has similar been escalated?] |
| Trajectory | YES/NO | [Getting worse?] |

**Decision:** ESCALATE / HANDLE INTERNALLY
**Urgency:** IMMEDIATE / URGENT / IMPORTANT / INFORMATIONAL

---

### Stakeholder Notification Plan

| Who | Role | Detail Level | Channel | By When |
|-----|------|-------------|---------|---------|
| [Name] | Decision Maker | Full | [Channel] | [Time] |
| [Name] | Accountable | Summary | [Channel] | [Time] |
| [Name] | SME | Technical | [Channel] | [Time] |

---

### Escalation Message

**To:** [Primary recipient]
**CC:** [Others]
**Subject:** [URGENCY] — [Situation] — [Ask]

**Situation:** [2-3 sentences]

**Impact:** [1-2 sentences]

**Actions Taken:**
- [What you've done]
- [What you've done]

**What I Need:**
- [Specific ask]

**Timeline:** [When you need response]
**Next Update:** [When you'll provide more info]
```

## Example Output

```markdown
## Escalation Assessment

**Situation:** Key vendor contract auto-renewal deadline is tomorrow; legal review reveals unfavorable terms we missed
**Assessed by:** Procurement Manager
**Date/Time:** 2026-02-26, 10:15 AM

---

### Escalation Test Results

| Test | Result | Rationale |
|------|--------|-----------|
| Authority | NO | Contract value ($400K) exceeds my approval authority |
| Impact | YES | Affects engineering team's tooling budget for next year |
| Visibility | YES | CFO would absolutely want to know before auto-renewal |
| Precedent | YES | Similar vendor issue was escalated last quarter |
| Trajectory | YES | Auto-renews tomorrow — getting worse by the hour |

**Decision:** ESCALATE
**Urgency:** URGENT (1-hour response needed)

---

### Stakeholder Notification Plan

| Who | Role | Detail Level | Channel | By When |
|-----|------|-------------|---------|---------|
| CFO | Decision Maker | Full detail + options | Direct message + call | 10:30 AM |
| VP Engineering | Accountable | Impact on team + recommendation | Slack message | 11:00 AM |
| Legal Counsel | SME | Contract terms + cancellation clause | Email with attachment | 10:45 AM |
| Procurement team | Informed | FYI, no action | Team Slack | 11:30 AM |

---

### Escalation Message (to CFO)

**To:** CFO
**CC:** VP Engineering
**Subject:** URGENT — Vendor contract auto-renews tomorrow with unfavorable terms — need decision by 2pm

**Situation:** Our CloudTools Inc. contract ($400K/yr) auto-renews tomorrow at midnight. Legal review discovered a 12% rate increase clause and new data retention terms that weren't in the original agreement.

**Impact:** If auto-renewed, we're locked into $448K for 2 years with terms that conflict with our data policy. Engineering uses this tool daily — disruption risk if we cancel without a migration plan.

**Actions Taken:**
- Had Legal flag the specific problematic clauses (attached)
- Confirmed cancellation window closes tomorrow 11:59 PM
- Identified two alternative vendors with preliminary pricing
- Drafted a 30-day extension request letter to send if approved

**What I Need:**
- Decision: Send cancellation notice + request 30-day extension to renegotiate, OR approve auto-renewal as-is
- My recommendation: Cancel auto-renewal and request 30-day extension

**Timeline:** Need decision by 2:00 PM to give Legal time to send notice
**Next Update:** I'll send the alternative vendor comparison by 1:00 PM
```

## Customization Guide

- **For engineering incidents:** Add system metrics, error rates, and customer impact numbers
- **For people/HR issues:** Add confidentiality requirements and legal counsel notification
- **For security incidents:** Add containment status and regulatory notification requirements
- **For customer escalations:** Add customer tier, revenue at risk, and relationship history
- **For project delays:** Add milestone impact, dependency chain effects, and recovery options

## Techniques Used

- **ST-01 (Clear Objective):** Specific escalation question with binary test
- **ST-02 (Sequential Instructions):** Five-step process from assessment to communication
- **RT-01 (Chain of Thought):** Step-by-step reasoning through escalation decision
- **RT-02 (Multi-Dimensional Analysis):** Five independent test dimensions
- **DS-06 (Prioritization Guidance):** Urgency classification with matched response

## Related Prompts

- [decisioning_crisis_severity_triage.md](decisioning_crisis_severity_triage.md) - Classify crisis severity before escalating
- [decisioning_crisis_communication_playbook.md](decisioning_crisis_communication_playbook.md) - Broader crisis communication strategy
- [decisioning_rapid_stakeholder_alignment.md](decisioning_rapid_stakeholder_alignment.md) - Getting stakeholder alignment quickly
- [validation_adversarial_mini_check.md](../domain-productivity/validation/validation_adversarial_mini_check.md) - Pre-decision verification
