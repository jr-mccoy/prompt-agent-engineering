---
title: "Post-Mortem Root Cause Ladder"
category: engineering-workflows/workflows
description: "Transform an incident summary into a blameless root-cause analysis using parallel Five Whys threads, categorized root causes, and prioritized corrective actions with owners, deadlines, and verification."
techniques:
  - ST-01
  - ST-02
  - RT-02
  - DS-06
  - QA-01
difficulty: intermediate
tags:
  - incident-response
  - post-mortem
  - root-cause-analysis
  - five-whys
  - reliability
updated: "2026-06-07"
related_prompts:
  - domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md
  - domain-engineering-workflows/workflows/engineering_debugging_root_cause.md
  - domain-engineering-workflows/workflows/engineering_prompt_for_debugging_code.md
---

# Post-Mortem Root Cause Ladder

**Objective:** Transform an incident summary into a blameless, actionable root-cause analysis — using parallel Five Whys threads to reach systemic causes, categorizing them, and producing prioritized corrective actions with owners, deadlines, and verification criteria.

**When to use:**
- After a production incident or service disruption.
- When a critical bug reached customers, or a deployment failed.
- Investigating a recurring issue or running a reliability review.

**When NOT to use:**
- Diagnosing a live bug you're still actively debugging — use `engineering_debugging_root_cause.md`.
- A facilitated, multi-thread, audited deep postmortem — use `engineering_postmortem_blueprint.md`.
- When no incident facts/timeline are available yet (collect them first).

**Audience:** Engineers, SREs, and incident commanders writing a postmortem.

---

## Your Input

**Incident Summary:** [Brief description of what went wrong]

**Timeline:**
```
[Timestamp] - [Event description]
[Timestamp] - [Event description]
...
```

**Systems Affected:** [List of services, databases, integrations involved]

**Impact:**
- Duration: [How long the incident lasted]
- Users Affected: [Number or percentage]
- Revenue Impact: [If applicable]
- SLA Breach: [Yes/No, which SLAs]

**Initial Observations:** [What responders noted during the incident]

---

## Inputs / Context

The user supplies the incident summary, timeline, systems affected, impact metrics (duration, users, revenue, SLA), and responders' initial observations. Wrap any pasted logs or alert text in a `<logs>` tag. If impact metrics are unknown, write "unknown" — do not estimate revenue or user counts.

---

## Constraints

### Must
- Reach systemic root causes via Five Whys (run parallel threads for multiple failure modes).
- Categorize each root cause (process / detection / technical-debt / human-factor / external).
- Give each corrective action a priority (P1/P2/P3), owner, deadline, and verification.
- Keep the analysis blameless — focus on system gaps, not individuals.

### Must Not
- Stop at "human error" — ask why the system allowed it.
- Invent impact figures (revenue, users, MTTR) not provided — mark unknowns.
- Propose vague actions ("more testing") — specify which tests, for what scenarios.
- Leave any corrective action without an owner, deadline, and verification.

---

## Instructions

Perform a systematic post-mortem analysis following these steps:

**Step 1: Incident Framing**
Restate the incident in clear, factual terms:
- What was expected to happen
- What actually happened
- When the deviation was first detected
- Who detected it and how

**Step 2: Impact Assessment**
Quantify the incident's impact across dimensions:
- **Customer Impact:** User-facing effects
- **Business Impact:** Revenue, reputation, SLA
- **Technical Impact:** System health, data integrity
- **Team Impact:** On-call burden, context switching

**Step 3: Five Whys Deep Dive**
For the primary failure mode, apply the Five Whys:

**Why #1:** [Surface cause] → [Answer]
**Why #2:** [Deeper cause] → [Answer]
**Why #3:** [Process/system gap] → [Answer]
**Why #4:** [Organizational factor] → [Answer]
**Why #5:** [Root cause] → [Answer]

If multiple failure modes exist, run parallel Five Whys threads.

**Step 4: Categorize Root Causes**
Classify each root cause:
- **Process Gap:** Missing or inadequate procedure
- **Detection Gap:** Monitoring/alerting failure
- **Technical Debt:** Known issue that wasn't addressed
- **Human Factor:** Training, communication, handoff
- **External Factor:** Third-party, environmental

**Step 5: Generate Corrective Actions**
For each root cause, propose actions with:
- **Action:** Specific change to implement
- **Priority:** P1 (immediate), P2 (this sprint), P3 (this quarter)
- **Owner:** Who is responsible
- **Verification:** How to confirm it's working
- **Timeline:** Specific deadline

**Step 6: Self-Audit**
Verify your analysis:
- [ ] Exactly 5 Why layers reached per thread
- [ ] At least 2 corrective actions per root cause
- [ ] All actions have owners and deadlines
- [ ] No blame assigned to individuals
- [ ] Focus on systemic improvements


**Output Format**

Structure your response as:

```xml
<incident_summary>
  <title>[Incident Title]</title>
  <date>[Date]</date>
  <duration>[Total duration]</duration>
  <severity>SEV-1|SEV-2|SEV-3</severity>
</incident_summary>

<impact_assessment>
  <customer_impact>[Description]</customer_impact>
  <business_impact>[Description]</business_impact>
  <technical_impact>[Description]</technical_impact>
  <metrics>
    <users_affected>[Number]</users_affected>
    <revenue_impact>[Amount or N/A]</revenue_impact>
    <mttr>[Mean time to recovery]</mttr>
  </metrics>
</impact_assessment>

<five_whys_analysis>
  <thread id="1">
    <symptom>[Starting point]</symptom>
    <why level="1">[Answer]</why>
    <why level="2">[Answer]</why>
    <why level="3">[Answer]</why>
    <why level="4">[Answer]</why>
    <why level="5">[Answer]</why>
    <root_cause>[Final root cause]</root_cause>
  </thread>
  <!-- Additional threads if needed -->
</five_whys_analysis>

<root_cause_summary>
  <cause category="process|detection|debt|human|external">
    [Root cause description]
  </cause>
</root_cause_summary>

<corrective_actions priority="P1|P2|P3">
  <action>
    <description>[What to do]</description>
    <owner>[Who]</owner>
    <deadline>[When]</deadline>
    <verification>[How to confirm]</verification>
  </action>
</corrective_actions>

<lessons_learned>
  <lesson>[Key insight]</lesson>
</lessons_learned>
```

Keep total output under 400 tokens. If exceeding, prioritize P1 actions and shorten action descriptions.

---

## Example Output

> Illustrative. The figures below (e.g. $127K, user counts, MTTR) are example values to show format — use only metrics actually provided for a real incident.

```xml
<incident_summary>
  <title>Payment Processing Outage</title>
  <date>2025-01-15</date>
  <duration>47 minutes</duration>
  <severity>SEV-1</severity>
</incident_summary>

<impact_assessment>
  <customer_impact>Users unable to complete purchases; checkout flow returned 500 errors</customer_impact>
  <business_impact>Estimated $127K in lost transactions during peak hours</business_impact>
  <technical_impact>Payment service crashed; database connection pool exhausted</technical_impact>
  <metrics>
    <users_affected>12,847</users_affected>
    <revenue_impact>$127,000</revenue_impact>
    <mttr>47 minutes</mttr>
  </metrics>
</impact_assessment>

<five_whys_analysis>
  <thread id="1">
    <symptom>Payment service returned 500 errors</symptom>
    <why level="1">Database connections timed out</why>
    <why level="2">Connection pool was exhausted (100/100 in use)</why>
    <why level="3">Connections weren't being released after transactions</why>
    <why level="4">Exception handler didn't close connections on error paths</why>
    <why level="5">No connection leak detection in code review checklist or CI pipeline</why>
    <root_cause>Missing automated detection for connection management issues in development workflow</root_cause>
  </thread>
  <thread id="2">
    <symptom>47-minute detection delay</symptom>
    <why level="1">Alert fired but was classified as low priority</why>
    <why level="2">Alert threshold was set too high (90% pool usage)</why>
    <why level="3">Threshold was copied from template without customization</why>
    <why level="4">No runbook requiring threshold review for new services</why>
    <why level="5">Service launch checklist doesn't include monitoring tuning step</why>
    <root_cause>Service deployment checklist lacks mandatory monitoring configuration review</root_cause>
  </thread>
</five_whys_analysis>

<root_cause_summary>
  <cause category="process">Missing connection leak detection in CI pipeline</cause>
  <cause category="detection">Alert thresholds not tuned for service-specific requirements</cause>
</root_cause_summary>

<corrective_actions priority="P1">
  <action>
    <description>Add connection pool leak detection test to CI pipeline</description>
    <owner>Platform Team</owner>
    <deadline>2025-01-22</deadline>
    <verification>PR merged; test blocks builds with leaks</verification>
  </action>
  <action>
    <description>Fix exception handler to release connections on all paths</description>
    <owner>Payments Team</owner>
    <deadline>2025-01-16</deadline>
    <verification>Load test shows stable pool usage under error conditions</verification>
  </action>
</corrective_actions>

<corrective_actions priority="P2">
  <action>
    <description>Update service launch checklist with monitoring tuning requirement</description>
    <owner>SRE Team</owner>
    <deadline>2025-01-29</deadline>
    <verification>Checklist updated; next launch uses new process</verification>
  </action>
  <action>
    <description>Lower connection pool alert threshold to 70% with 5-minute window</description>
    <owner>Payments Team</owner>
    <deadline>2025-01-18</deadline>
    <verification>Alert fires in staging test; PagerDuty receives notification</verification>
  </action>
</corrective_actions>

<corrective_actions priority="P3">
  <action>
    <description>Implement automated alert threshold recommendations based on service type</description>
    <owner>Platform Team</owner>
    <deadline>2025-02-28</deadline>
    <verification>New services get suggested thresholds during onboarding</verification>
  </action>
</corrective_actions>

<lessons_learned>
  <lesson>Connection management requires explicit verification in error paths—happy path testing is insufficient</lesson>
  <lesson>Default alert thresholds should be conservative; services can relax them after baseline is established</lesson>
  <lesson>Launch checklists need enforcement mechanisms, not just documentation</lesson>
</lessons_learned>
```


**Common Pitfalls to Avoid:**

| Pitfall | Why It's Wrong | Better Approach |
|---------|----------------|-----------------|
| Stopping at "human error" | Blames individuals, not systems | Ask why the system allowed the error |
| Accepting "we need more testing" | Too vague to action | Specify which tests, for what scenarios |
| Proposing only technical fixes | Ignores process gaps | Include process and detection improvements |
| Single-threaded analysis | Misses contributing factors | Run parallel Why threads for complex incidents |
| No verification criteria | Can't confirm fix worked | Every action needs measurable verification |

---

## False-Positive Prevention

❌ **DON'T:**
- Don't stop the Why chain at "human error" — keep asking why the system permitted it.
- Don't invent impact metrics (revenue, users, MTTR) — mark unknowns as unknown.
- Don't write vague corrective actions like "more testing."
- Don't blame named individuals.

✅ **DO:**
- Reach a systemic root cause on each thread; run parallel threads for multiple failure modes.
- Use only provided metrics; label gaps.
- Make every action specific, owned, dated, and verifiable.
- Keep the analysis blameless and system-focused.

---

## Verification

- [ ] Five Why layers reached per thread; parallel threads for multiple failure modes.
- [ ] Each root cause categorized (process/detection/debt/human/external).
- [ ] ≥2 corrective actions per root cause, each with owner, deadline, verification.
- [ ] No blame on individuals; focus on system gaps.
- [ ] No fabricated impact metrics; unknowns labeled.
- [ ] Corrective actions are specific (named tests/process changes, not "more testing").

---

## Techniques Used

- **ST-01 (Clear Objective Statement):** Frames the blameless, actionable postmortem goal.
- **ST-02 (Structured Sequential Instructions):** Frame → impact → Five Whys → categorize → actions → self-audit.
- **RT-02 (Multi-Dimensional Analysis):** Assesses customer/business/technical/team impact and parallel cause threads.
- **DS-06 (Prioritization and Severity Guidance):** P1/P2/P3 ranking orders corrective actions.
- **QA-01 (Self-Verification):** Self-audit step enforces depth, ownership, and blamelessness.

---

## Related Prompts

- `domain-engineering-workflows/workflows/engineering_postmortem_blueprint.md` — Facilitated, audited deep postmortem process.
- `domain-engineering-workflows/workflows/engineering_debugging_root_cause.md` — Root-cause analysis during active debugging.
- `domain-engineering-workflows/workflows/engineering_prompt_for_debugging_code.md` — Stuck-bug diagnosis with tracking metrics.
