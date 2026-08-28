---
title: "Workflow Automation Opportunity Finder"
category: productivity/automation
description: "Analyze your manual workflows to find the highest-ROI automation opportunities — evaluates each step by frequency, creativity requirement, and error cost to identify what to automate first"
techniques:
  - ST-01
  - ST-02
  - CM-01
  - DS-06
  - RT-02
difficulty: beginner
tags:
  - personal-development
  - automation
  - productivity
  - workflows
  - efficiency
updated: "2026-06-21"
related_prompts:
  - domain-productivity/bottlenecks/bottleneck_open_loop_audit.md
  - domain-productivity/deep-work/deepwork_zombie_meeting_detector.md
  - domain-personal-development/prompts/solo-dev/solo_dev_automation_audit.md
---

# Workflow Automation Opportunity Finder

**Objective:** Analyze your manual workflows to identify the highest-ROI automation opportunities. Evaluates each step using a frequency × creativity × error-cost matrix, then recommends specific tools and approaches for the top candidates.

## When to Use

- Use when: you're doing the same manual multi-step task repeatedly and want to find the highest-ROI piece to automate first.
- Use when: you're scaling up and manual processes are becoming bottlenecks, or during a quarterly review of how you spend time.
- Use this when you have a **specific named workflow** to analyze. For a personal-developer-wide automation sweep, route to `solo_dev_automation_audit.md`. To clear out the unstructured mental backlog *before* deciding what's worth automating, run `domain-productivity/bottlenecks/bottleneck_open_loop_audit.md` first.
- Don't use when: the task requires human judgment or relationship nuance end-to-end — automating it is a false economy.

---

## Inputs / Context

**Workflow Steps:** [Paste a step-by-step description of a workflow you do regularly]

Example:
```
1. Check email for new client inquiries
2. Copy client info into CRM
3. Send welcome email from template
4. Schedule onboarding call
5. Create project folder from template
6. Send meeting link
```

**Frequency:** [How often you do this workflow — daily/weekly/monthly]
**Time per execution:** [How long it takes each time]
**Pain points:** [Which steps are most tedious or error-prone]

**Refusal / insufficiency logic:** Do not invent a workflow. If **Workflow Steps** is not supplied as concrete, observable steps, ask the user to paste them — ROI analysis on an imagined workflow is fiction. If **Frequency** and **Time per execution** are both missing, ask for at least a rough estimate before computing payback periods; never present a fabricated payback figure as if measured. If the user's stack/technical ability is unstated, default tool recommendations to the simplest tier (template / text-expansion / no-code) rather than assuming they can build custom scripts.

---

## Instructions

### Phase 1: Step Analysis

For each workflow step, evaluate:

| Step | Frequency | Creativity Required | Error Cost | Automation ROI |
|------|-----------|-------------------|------------|----------------|
| [Step 1] | daily/weekly | none/low/high | low/med/high | high/med/low |

**Scoring:**
- **High ROI:** Frequent + low creativity + any error cost = automate first
- **Medium ROI:** Less frequent or moderate creativity = automate when convenient
- **Low ROI:** Infrequent or requires judgment = keep manual

### Phase 2: Automation Candidates (Top 3-5)

For each high-ROI candidate:

**Candidate N: [Step Name]**
- **Current time:** [How long it takes manually]
- **Suggested tool:** Zapier / n8n / Make / custom script / native integration
- **Implementation approach:** [How to set it up]
- **Estimated setup time:** [Hours to implement]
- **Payback period:** [When automation saves more time than setup cost]

### Phase 3: Implementation Priority

Rank candidates by: `(time saved per month) / (setup effort)`

1. **[Top pick]** — Highest ratio. Start here.
2. **[Second]** — Do after #1 is working.
3. **[Third]** — Nice to have.

### Phase 4: Quick Wins

Identify any steps that can be improved WITHOUT automation:
- Templates that reduce manual typing
- Keyboard shortcuts or text expansion
- Batch processing instead of one-at-a-time
- Checklists that prevent errors

---

### False-Positive Prevention

- ❌ Do NOT recommend automating steps that require human judgment or relationship nuance
- ❌ Do NOT suggest complex automation for infrequent tasks — the setup cost won't pay off
- ❌ Do NOT ignore the maintenance cost of automations — they break and need updating
- ❌ Do NOT assume the user has technical skills to build custom scripts unless stated
- ✅ DO recommend the simplest tool that gets the job done (template > script > workflow tool)
- ✅ DO include quick wins that don't require any tools
- ✅ DO calculate payback periods honestly
- ✅ DO suggest starting with one automation and expanding once it's stable

---

## Expected Output

```markdown
# Automation Opportunity Report: [Workflow Name]

## Step Analysis
| Step | Frequency | Creativity | Error Cost | Automation ROI |
|------|-----------|-----------|------------|----------------|
| 1. Check email for inquiries | daily | none | low | High |
| 2. Copy info into CRM | daily | none | medium | High |
| 3. Send welcome email | daily | low | low | High |
| 4. Schedule onboarding call | daily | low | medium | Medium |
| 5. Create project folder | daily | none | low | High |

## Top Automation Candidates
### Candidate 1: Copy info into CRM
- Current time: ~4 min/run × 5/day = 20 min/day
- Suggested tool: Zapier (email parser → CRM create-record)
- Implementation: parser rule on inbound inquiry → map fields → create CRM contact
- Estimated setup: ~2 hours
- Payback period: ~6 working days

### Candidate 2: ...

## Implementation Priority (time saved/month ÷ setup effort)
1. Copy info into CRM — start here (highest ratio)
2. Welcome email auto-send
3. Project folder templating

## Quick Wins (no automation needed)
- Text-expansion snippet for the welcome email
- Saved CRM view to batch-process inquiries once daily
- Checklist to prevent skipped onboarding steps

## Recommendation
Automate Candidate 1 only this week. Re-run this audit once it has run stably for 2 weeks.
```

---

## Verification

Before delivering the report, confirm each of these. If any fails, fix it before responding:

- [ ] Every workflow step the user supplied appears in the step-analysis table with all three dimensions (frequency, creativity, error cost) scored.
- [ ] No step requiring **human judgment or relationship nuance** is recommended for full automation.
- [ ] Payback periods are computed from the user's **stated frequency/time**, not invented — and are labeled as estimates.
- [ ] Tool suggestions default to the **simplest tier that works** (template < text-expansion < no-code < script) and match the user's stated technical ability.
- [ ] **Maintenance cost** is acknowledged for any recommended automation (automations break).
- [ ] At least one **no-tool quick win** is included.
- [ ] The recommendation tells the user to start with **one** automation, not all of them.

---

## Techniques Used

- **ST-01** (Clear Objective Statement) — Automation opportunity identification with ROI ranking
- **ST-02** (Structured Sequential Instructions) — Analyze, evaluate, prioritize, implement
- **CM-01** (Explicit Context Framing) — Real workflow data as input
- **DS-06** (Prioritization Guidance) — ROI-based ranking with payback periods
- **RT-02** (Multi-Dimensional Analysis) — Frequency, creativity, error cost dimensions

---

## Related Prompts

- [domain-productivity/bottlenecks/bottleneck_open_loop_audit.md](../bottlenecks/bottleneck_open_loop_audit.md) — Identify tasks cluttering your mental space (run before deciding what to automate).
- [domain-productivity/deep-work/deepwork_zombie_meeting_detector.md](../deep-work/deepwork_zombie_meeting_detector.md) — Automate or eliminate meeting overhead.
- [solo_dev_automation_audit.md](../../domain-personal-development/prompts/solo-dev/solo_dev_automation_audit.md) — Deeper automation analysis for solo developers.

> **Boundary note:** Meeting/automation/focus overlap with [`domain-productivity/deep-work/`](../deep-work/) (calendar audits, meeting-to-async conversion). This prompt is the personal-development entry point; link across rather than duplicating that cluster.
