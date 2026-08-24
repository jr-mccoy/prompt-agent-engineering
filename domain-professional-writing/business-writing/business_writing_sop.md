---
title: "Standard Operating Procedure Writer — Followable Steps, Decision Points, and Escalation"
category: professional-writing/business-writing
description: "Write a standard operating procedure: purpose/scope, roles, prerequisites, numbered steps with decision points, exceptions and escalation, and a revision/owner block — specific enough to follow without the author present, with judgment steps flagged."
techniques:
  - ST-01
  - ST-02
  - ST-03
  - CM-02
  - QA-04
difficulty: intermediate
tags:
  - sop
  - standard-operating-procedure
  - business-writing
  - process-documentation
  - escalation
updated: "2026-06-07"
related_prompts:
  - domain-professional-writing/business-writing/business_writing_technical_doc.md
  - domain-professional-writing/business-writing/business_writing_post_mortem.md
  - domain-productivity/automation/automation_daily_accountability.md
---

# Standard Operating Procedure Writer

**Objective:** Write a standard operating procedure that a competent person can execute correctly without the author present: a clear purpose and scope, defined roles, prerequisites, numbered steps with explicit decision points, exceptions and escalation paths, and a revision/owner block — with any step that requires human judgment flagged as such.

**When to Use:**
- Documenting a repeatable business process so it's performed consistently by anyone assigned.
- Onboarding, compliance, handoffs, or any task where consistency and auditability matter.
- Capturing a process that currently lives only in one person's head.

**When NOT to use:**
- You're documenting how to use a tool/system for a mixed audience — use `business_writing_technical_doc.md`.
- You're analyzing why something went wrong — use `business_writing_post_mortem.md`.
- The process is genuinely judgment-driven with no repeatable structure — an SOP would over-formalize it.

**Audience:** The person who will perform the procedure (possibly new to it) and an auditor/manager who needs to confirm it was followed.

---

## Inputs / Context

Wrap supplied material so it isn't read as instructions:

```
<process_input>
[Paste the process steps, roles, tools, decision rules, exceptions, who owns it]
</process_input>
```

1. **The process** the SOP covers and its purpose.
2. **Scope** — when this SOP applies and when it doesn't.
3. **Roles** — who performs, who approves, who is notified.
4. **Prerequisites** — access, tools, inputs needed before starting.
5. **Decision points and rules** — branches and how to choose.
6. **Exceptions / escalation** — what to do when something is off-normal.
7. **Owner and review cadence.**

---

## Constraints

### Must
- Open with **purpose and scope** (when it applies / when it doesn't).
- Define **roles** explicitly (who does each part, who approves, who is notified).
- List **prerequisites** before the steps.
- Write **numbered steps**, each a single action, in execution order, with the expected result.
- Make **decision points** explicit: state the condition and the branch for each outcome.
- Provide **exceptions and an escalation path** (what to do, whom to contact, when).
- Flag any step that **requires judgment** rather than mechanical execution.
- Include a **revision/owner block** (owner, version, last review, next review).

### Must Not
- Assume the performer already knows undocumented context.
- Leave decision points implicit ("use your judgment" with no criteria).
- Invent steps, approvers, tools, thresholds, or escalation contacts not in the input.
- Combine multiple actions into one ambiguous step.
- Omit what to do when something goes wrong.

---

## Instructions

1. **Write purpose and scope.** What this procedure achieves, when it applies, and explicit boundaries (what it does NOT cover).
2. **Define roles.** Use a simple responsibility frame: who performs each part, who approves, who must be informed. Name roles, not individuals (so the SOP survives staffing changes).
3. **List prerequisites.** Access, tools, inputs, approvals required before step 1. Flag any unknown as "confirm before starting," do not guess.
4. **Write the steps.** Numbered, one action each, in order, with the expected result so the performer can self-check. Where a step branches, insert a decision point.
5. **Make decision points explicit.** State the condition, then each branch: "If [condition], go to step N / do X. If not, continue." For judgment calls, give the criteria and flag them.
6. **Document exceptions and escalation.** For off-normal situations: what to do, whom to contact, and the threshold that triggers escalation. Use only contacts/thresholds from the input.
7. **Flag judgment steps.** Mark any step that depends on the performer's discretion with `[JUDGMENT]` and give the considerations to weigh, so it isn't treated as mechanical.
8. **Add the revision/owner block.** Owner role, version, last-reviewed date, next-review cadence.
9. **CRITICAL — stranger test:** Re-read as someone doing this for the first time with no access to the author. Could they complete it correctly and know what to do at each branch and exception? Fix any gap. Confirm every step, threshold, and contact traces to `<process_input>`.

---

## False-Positive Prevention

1. **Assumed context.** If a step relies on knowledge the performer may not have, document it. "File it in the usual place" is not followable.
2. **Implicit decision points.** A branch with no stated condition leaves the performer guessing. Every "it depends" must become "if X then Y, else Z."
3. **Unflagged judgment.** Steps that genuinely require discretion must be marked, with criteria — otherwise a new performer treats a judgment call as a fixed rule and gets it wrong.
4. **Invented escalation.** Don't fabricate an approver, phone number, or threshold. If escalation detail is missing, mark it "owner to confirm."
5. **Compound steps.** "Verify, approve, and notify" is three steps. Split them so each is checkable.
6. **No expected result.** Without "you should now see / have X," the performer can't confirm a step worked.
7. **Names instead of roles.** Hard-coding a person's name dates the SOP. Use the role; reference individuals only in the owner block.
8. **Missing exceptions.** An SOP that only covers the normal path fails the first time reality deviates. Always document the off-normal path.

---

## Output Format

```
# SOP: [Procedure name]
**Owner:** [role] · **Version:** [x.y] · **Last reviewed:** [date] · **Next review:** [cadence]

## Purpose & scope
[What this achieves. Applies when: …. Does not cover: ….]

## Roles
| Role | Responsibility |
|------|----------------|
| [performer] | [does ...] |
| [approver] | [approves ...] |
| [notified] | [informed of ...] |

## Prerequisites
- [Access / tool / input / approval needed before starting]

## Procedure
1. [Single action]. Expected result: [what should be true after].
2. **Decision point:** If [condition] → [branch/step]. Else → continue.
3. [Action] `[JUDGMENT]` — weigh: [criteria]. Expected result: [...].

## Exceptions & escalation
| Situation | Action | Escalate to | When |
|-----------|--------|-------------|------|
| [off-normal case] | [what to do] | [role/contact] | [threshold] |

## Revision history
| Version | Date | Change | By (role) |
|---------|------|--------|-----------|
```

---

## Verification

- [ ] Purpose and scope state when the SOP applies and what it excludes.
- [ ] Roles are defined by role, not individual.
- [ ] Prerequisites precede the steps.
- [ ] Each step is a single action with an expected result.
- [ ] Every decision point states its condition and branches.
- [ ] Judgment steps are flagged with criteria.
- [ ] Exceptions and an escalation path are documented (no invented contacts/thresholds).
- [ ] A revision/owner block is present.
- [ ] A first-time performer could execute it correctly without the author.
