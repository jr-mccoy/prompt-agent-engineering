---
title: "Founder Bottleneck & Week-Away Test"
category: business-strategy/ambition-leverage
description: "Help a founder stop being the operational bottleneck by defining founder-only work, mapping what routes through them, stress-testing each path with the week-away test, and deciding what to automate, delegate, or keep."
techniques:
  - RT-02
  - DS-06
  - NE-02
  - QA-08
  - DP-05
difficulty: intermediate
tags:
  - founder-bottleneck
  - delegation
  - automation
  - scaling
  - week-away-test
updated: "2026-06-19"
related_prompts:
  - domain-business-strategy/ambition-leverage/ambition_leadership_audit.md
  - domain-business-strategy/ambition-leverage/ambition_insight_to_action_workflow.md
  - domain-business-strategy/startup/startup_ai_native_lifecycle_navigator.md
---

# Founder Bottleneck & Week-Away Test

**Objective:** Get a founder or leader out of the critical path by separating the work only they should do from everything else, mapping every workflow and approval that routes through them, stress-testing each with the week-away test, and producing a clear automate / delegate / keep decision with handoff criteria for the paths that stall.

**When to Use:**
- Decisions that should take an hour now take a week because they wait on you.
- Support requests or operational tasks pile up because only you know the answer or remember to do them.
- You want to scale capacity without simply working more hours.

**When NOT to Use:**
- You are pre-traction and the founder genuinely should be doing nearly everything — premature delegation wastes scarce judgment.
- You only need to clarify stated-vs-revealed ambition (use `ambition_leadership_audit.md`).

**Source:** Frameworks are drawn from a vendor report, Anthropic's *The Founder's Playbook: Building an AI-Native Startup* (2026) — attributed inline; no source text reproduced.

## Inputs / Context

Provide what you can; the output degrades gracefully if some are missing:
- **Your recurring work** — the workflows, decisions, and approvals you touch in a typical week.
- **Founder-only candidates** — work you believe only you can or should do.
- **Bottleneck symptoms** — where things stall, pile up, or wait on you.
- **Available capacity** — who else exists (team, contractors) and what can be automated.
- **Stakes** — which paths are high-blast versus routine.

## Constraints

**Must:**
- Build a founder-priority list of "the things only I should be doing"; treat everything off it as a delegation/automation candidate.
- Apply the week-away test to every path that routes through the founder.
- For each task, decide automate entirely / needs a human but not you / requires founder judgment, and design workflow logic for the middle bucket.

**Must Not:**
- Keep a task as founder-only just because the founder enjoys it or has always done it.
- Mark a path "fine" without asking what happens when the founder is unavailable for a week.
- Recommend delegation without handoff criteria, escalation paths, or exception handling for the paths that stall.

**Instructions:**

1. **Build the founder-priority list.** Define "the things only I should be doing" — e.g., product narrative, board relationships, enterprise deals, founder-to-founder conversations. Anything not on this list is a delegation or automation candidate by default.

2. **Map the bottleneck.** List every workflow, decision, and approval that routes through the founder. For each, capture what it is, how often it happens, and who else is involved.

3. **Run the week-away test.** For each mapped path, ask: "What happens to this when I'm unavailable for a week?" Workflows that STALL are exactly where handoff criteria, escalation paths, or exception handling need tightening — those are the priority targets.

4. **Triage operational load.** Categorize each recurring task: automate entirely / needs a human but not you / requires founder judgment. Be honest — most "requires me" tasks are really "requires someone who knows the answer," which is a documentation and handoff problem, not a founder problem.

5. **Design workflow logic for the middle bucket.** For "needs a human but not you" tasks, specify the workflow: trigger, decision rules, output, and destination — so the task can run without the founder in the loop.

6. **Surface the telltale bottleneck signs.** Explicitly check for: decisions that should take an hour now taking a week; support requests piling up because only the founder knows the answer; ops tasks that happen only when the founder remembers them. Each sign points to a specific path to fix.

7. **Write handoff criteria for the stalling workflows.** For every path that stalled the week-away test, define what a clean handoff requires: who owns it, the decision rules they follow, when they escalate, and how exceptions are handled.

**Output Format:**

A markdown bottleneck plan:
- **Founder-Priority List** — the things only the founder should do
- **Bottleneck Map** — table: Workflow | Routes through me? | Stalls when I'm away? | Verdict (automate/delegate/keep)
- **Operational-Load Triage** — per task: automate entirely / human-but-not-you / founder judgment, with workflow logic for the middle bucket
- **Telltale Signs Check** — which symptoms are present and the path each points to
- **Handoff Criteria** — for each stalling workflow: owner, decision rules, escalation, exceptions

## Verification

- [ ] A founder-priority list exists and everything off it is treated as a candidate.
- [ ] Every path that routes through the founder is run through the week-away test.
- [ ] Each task has an automate/delegate/keep verdict with reasoning.
- [ ] Middle-bucket tasks have workflow logic (trigger, rules, output, destination).
- [ ] Every stalling workflow has handoff criteria including escalation and exception handling.

## False-Positive Prevention

❌ **DON'T:**
- Keep a task as "founder judgment" when it is really "no one else has the context yet."
- Mark a path safe because it has never broken — it has never broken because you have never been away.
- Automate a high-stakes judgment call to look productive.
- Delegate without writing down decision rules, leaving the team to escalate everything back to you anyway.

✅ **DO:**
- Test each path against a real week of founder absence, not a good day.
- Treat "only I know the answer" as a documentation gap to close, not a permanent founder duty.
- Reserve founder judgment for genuinely irreversible, high-context, or relationship-defining work.
- Make handoffs concrete enough that the team can act without you and knows exactly when to escalate.

## Example Output

```markdown
## Founder Bottleneck Plan — Seed-Stage SaaS Founder

### Founder-Priority List
- Product narrative & roadmap direction
- Board and investor relationships
- Enterprise/strategic deals
- Founder-to-founder and key-hire conversations

### Bottleneck Map
| Workflow | Routes through me? | Stalls when I'm away? | Verdict |
|---|---|---|---|
| Approving refunds <$500 | Yes | Yes — piles up | Delegate (rule-based) |
| Tier-2 support answers | Yes | Yes — only I know | Delegate after documenting |
| Vendor invoice approval | Yes | Yes | Automate (threshold + auto-approve) |
| Enterprise contract terms | Yes | Yes | Keep (founder judgment) |
| Weekly metrics report | Yes | No (assistant runs it) | Already delegated |

### Operational-Load Triage
- Automate entirely: invoice approval under $1k → trigger: invoice received; rule: known vendor + under threshold → auto-approve; output: paid; destination: finance log.
- Human-but-not-you: refunds, tier-2 support → owner: support lead, with a decision rulebook.
- Founder judgment: enterprise terms, board, narrative.

### Telltale Signs Check
- "Hour-long decisions taking a week" → refund approvals (present). 
- "Support piles up, only I know" → tier-2 answers (present; documentation gap).
- "Ops only when I remember" → vendor invoices (present; automate).

### Handoff Criteria
- Refunds: support lead approves <$500 by rulebook; escalate disputes >$500 or repeat offenders; exceptions (chargebacks) flagged to finance.
- Tier-2 support: build an answer doc from past tickets; lead handles documented cases; escalate novel/legal questions to founder.
```

**Techniques Used:**
- **RT-02 (Role-Based Expertise):** reasons as an operations/scaling advisor to a founder.
- **DS-06 (Prioritization & Severity Guidance):** stalling, high-blast paths set the priority for action.
- **NE-02 (Adversarial / Devil's-Advocate Framing):** the week-away test stress-tests each path against founder absence.
- **QA-08 (Self-Consistency Check):** the telltale-signs check tests the map against known bottleneck symptoms.
- **DP-05 (Decision Routing / Disposition):** the automate / delegate / keep verdict routes each task to the right owner.

**Related Prompts:**
- `ambition_leadership_audit.md` — clarify stated-vs-revealed ambition before deciding what to let go.
- `ambition_insight_to_action_workflow.md` — compress lead time once paths are handed off.
- `domain-business-strategy/startup/startup_ai_native_lifecycle_navigator.md` — situate bottleneck removal in the founder lifecycle.
