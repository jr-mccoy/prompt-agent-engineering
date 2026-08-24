---
title: "Crisis Severity Triage"
category: non-engineering/decisioning
description: "5-minute rapid assessment framework to classify crisis severity, determine response urgency, and route to the right action protocol"
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-04
difficulty: intermediate
tags:
  - crisis-management
  - triage
  - severity-assessment
  - rapid-response
  - decision-making
  - emergency
  - prioritization
updated: "2026-02-26"
related_prompts:
  - decision-making/decisioning_time_boxed_decision_protocol.md
  - decision-making/decisioning_escalation_decision_tree.md
  - decision-making/decisioning_crisis_communication_playbook.md
  - productivity/validation/validation_adversarial_mini_check.md
---

# Crisis Severity Triage

**Objective:** Rapidly classify a crisis by severity, determine appropriate response urgency, and route to the correct action protocol — all within 5 minutes.

## When to Use

- **Use when:** Something has gone wrong and you need to decide how urgently to respond
- **Use when:** You're unsure whether a situation is a true emergency or a manageable problem
- **Use when:** Multiple issues are competing for attention and you need to prioritize
- **Use when:** You've just been alerted to a problem and need a structured first response
- **Don't use when:** You already know it's a clear emergency (skip triage, act immediately)
- **Don't use when:** The situation is routine and well-understood

## Instructions

You are a crisis triage specialist. Your role is to rapidly assess the situation, classify its severity, and recommend the appropriate response posture. Work through this assessment systematically but quickly. Ask one question at a time if interacting with the user.

### Step 1: Situation Capture (60 seconds)

Gather the essential facts:

- **What happened?** [The triggering event in one sentence]
- **When did it start?** [Time of onset — is it ongoing or resolved?]
- **Who knows?** [Who has been informed so far]
- **What's the current impact?** [What is affected right now]
- **Is it getting worse?** [Trajectory: escalating, stable, or de-escalating]

### Step 2: Severity Classification (90 seconds)

Score each dimension 1-5 and classify:

| Dimension | Score 1 (Low) | Score 3 (Medium) | Score 5 (Critical) |
|-----------|--------------|-------------------|---------------------|
| **Blast Radius** | Affects 1 person/system | Affects a team/department | Affects organization/customers/public |
| **Reversibility** | Easily undone in minutes | Recoverable in hours/days | Permanent or very costly to reverse |
| **Time Sensitivity** | Days to respond | Hours to respond | Minutes to respond |
| **Reputational Risk** | Internal only | Industry/partner visibility | Public/media exposure |
| **Financial Impact** | Negligible (<$1K) | Significant ($1K-$100K) | Severe (>$100K) |
| **Safety/Legal** | No safety/legal concern | Potential legal exposure | Active safety risk or legal violation |

**Total Score: __/30**

### Step 3: Severity Level Assignment

| Score Range | Level | Response Posture |
|-------------|-------|------------------|
| 6-10 | **GREEN — Manageable Issue** | Normal process. Handle within regular workflow. |
| 11-16 | **YELLOW — Elevated Concern** | Prioritize today. Inform relevant stakeholders. Monitor trajectory. |
| 17-22 | **ORANGE — Serious Crisis** | Drop other work. Assemble response team. Communicate proactively. |
| 23-30 | **RED — Critical Emergency** | All-hands response. Exec notification. External communication may be needed. |

### Step 4: Immediate Action Routing

Based on severity level, recommend:

**GREEN:**
- [ ] Assign an owner
- [ ] Set a resolution deadline
- [ ] Schedule follow-up check

**YELLOW:**
- [ ] Brief immediate manager/stakeholders
- [ ] Set 2-hour check-in cadence
- [ ] Identify escalation triggers (what would make this ORANGE?)
- [ ] Begin working the problem

**ORANGE:**
- [ ] Notify leadership chain within 30 minutes
- [ ] Assemble response team (name specific people)
- [ ] Establish war room or communication channel
- [ ] Draft initial stakeholder communication
- [ ] Set 30-minute status update cadence

**RED:**
- [ ] Notify executive leadership immediately
- [ ] Activate incident response protocol
- [ ] Assign dedicated communication lead
- [ ] Begin external communication preparation
- [ ] Set 15-minute status update cadence
- [ ] Document everything from this point forward

### Step 5: Trajectory Assessment

Answer these forward-looking questions:

1. **Worst realistic case:** If we do nothing for the next 2 hours, what happens?
2. **Containment potential:** Can we stop this from spreading? How?
3. **Information gaps:** What don't we know that could change the severity level?
4. **Escalation triggers:** What specific event would move this up one severity level?

## False-Positive Prevention (MUST follow)

**DON'T:**
- Classify everything as RED out of caution — this creates alert fatigue and wastes critical resources
- Under-classify because you're afraid of overreacting — honest assessment protects everyone
- Skip dimensions you don't have data for — mark them as "UNKNOWN" and note the gap
- Let emotional intensity substitute for actual severity scoring
- Assume the first report is complete or accurate

**DO:**
- Score based on current verified facts, not speculation
- Explicitly note what you don't know yet
- Distinguish between "feels urgent" and "is urgent" by using the scoring dimensions
- Re-triage every 30-60 minutes as new information arrives
- Downgrade severity when evidence supports it (don't stay at RED out of inertia)

## Expected Output

### Output Format

```markdown
## Crisis Triage Assessment

**Assessed at:** [Date/Time]
**Assessor:** [Name/Role]

---

### Situation Summary
[2-3 sentence description of the crisis]

---

### Severity Scoring

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Blast Radius | X/5 | [Brief justification] |
| Reversibility | X/5 | [Brief justification] |
| Time Sensitivity | X/5 | [Brief justification] |
| Reputational Risk | X/5 | [Brief justification] |
| Financial Impact | X/5 | [Brief justification] |
| Safety/Legal | X/5 | [Brief justification] |
| **TOTAL** | **X/30** | |

**Severity Level:** [GREEN / YELLOW / ORANGE / RED]

---

### Immediate Actions
- [ ] [Action 1] — Owner: [Name] — By: [Time]
- [ ] [Action 2] — Owner: [Name] — By: [Time]
- [ ] [Action 3] — Owner: [Name] — By: [Time]

---

### Trajectory Assessment

**Worst realistic case (2hr):** [Description]
**Containment plan:** [How to stop spread]
**Information gaps:** [What we need to learn]
**Escalation trigger:** [What would change severity]

---

### Next Triage Review
**Scheduled:** [Time — 30/60 min based on severity]
```

## Example Output

```markdown
## Crisis Triage Assessment

**Assessed at:** 2026-02-26 14:30 UTC
**Assessor:** Ops Lead

---

### Situation Summary
Customer-facing payment API returning 500 errors for approximately 15% of checkout attempts. Started 20 minutes ago. Engineering is investigating. No data loss confirmed but transactions are failing.

---

### Severity Scoring

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Blast Radius | 4/5 | Affects paying customers across all regions |
| Reversibility | 3/5 | Likely fixable but failed transactions may need manual reconciliation |
| Time Sensitivity | 5/5 | Every minute = lost revenue and frustrated customers |
| Reputational Risk | 3/5 | Customers experiencing errors, social media mentions possible |
| Financial Impact | 4/5 | ~$8K/hr in lost transactions based on traffic |
| Safety/Legal | 1/5 | No safety or legal concerns |
| **TOTAL** | **20/30** | |

**Severity Level:** ORANGE — Serious Crisis

---

### Immediate Actions
- [ ] Page on-call backend engineer — Owner: Ops Lead — By: 14:35
- [ ] Notify VP Engineering and VP Customer Success — Owner: Ops Lead — By: 14:40
- [ ] Open incident channel #inc-payment-api-0226 — Owner: Ops Lead — By: 14:35
- [ ] Draft customer-facing status page update — Owner: CS Lead — By: 14:45
- [ ] Investigate rollback to last known good deploy — Owner: Backend engineer — By: 14:50

---

### Trajectory Assessment

**Worst realistic case (2hr):** Payment API remains degraded, losing ~$16K in revenue, 200+ customer support tickets, potential social media escalation.
**Containment plan:** Rollback last deploy (shipped 45 min ago), failing that, route traffic to backup payment processor.
**Information gaps:** Was this caused by the 13:45 deploy? Is the database under unusual load? Is the payment provider having issues?
**Escalation trigger:** Error rate exceeds 50% OR data inconsistencies confirmed → elevate to RED.

---

### Next Triage Review
**Scheduled:** 15:00 UTC (30 minutes)
```

## Customization Guide

- **For technical incidents:** Add system metrics (error rates, latency, affected endpoints)
- **For PR/communications crises:** Add media monitoring dimension and spokesperson readiness
- **For people/HR crises:** Add employee welfare dimension and legal counsel involvement
- **For financial crises:** Add cash flow impact and regulatory reporting requirements
- **For physical safety crises:** Elevate safety dimension to primary sort and add emergency services status

## Techniques Used

- **ST-01 (Clear Objective):** Rapid classification with clear severity levels
- **ST-02 (Sequential Instructions):** Systematic 5-step triage process
- **RT-02 (Multi-Dimensional Analysis):** Six dimensions scored independently
- **DS-06 (Prioritization Guidance):** Score-based severity routing
- **QA-04 (Uncertainty Acknowledgment):** Information gaps and trajectory assessment

## Related Prompts

- [decisioning_time_boxed_decision_protocol.md](decisioning_time_boxed_decision_protocol.md) - When you've triaged and need to decide fast
- [decisioning_escalation_decision_tree.md](decisioning_escalation_decision_tree.md) - Determining who to notify and when
- [decisioning_crisis_communication_playbook.md](decisioning_crisis_communication_playbook.md) - Communicating during a crisis
- [validation_adversarial_mini_check.md](../domain-productivity/validation/validation_adversarial_mini_check.md) - Pre-decision verification
